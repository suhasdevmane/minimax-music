"""Generate music locally with MiniMax Music 3 (diffusers modular pipeline).

Tuned for a 16 GB GPU: components are auto-offloaded to CPU and the 8B language
model is streamed layer-by-layer so peak VRAM stays low.

Usage:
    .venv\\Scripts\\python.exe generate.py --duration 30 --out song.wav
"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from diffusers import ComponentsManager, ModularPipeline
from diffusers.hooks import apply_group_offloading

REPO_ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = REPO_ROOT / "minimax_ttm"

DEFAULT_PROMPT = (
    "Genre: acoustic pop. BPM: 96. Key: C major. Warm and intimate, building gently "
    "into the chorus. Vocals: soft female lead, close and breathy, light stacked "
    "harmonies in the chorus. Arrangement: fingerpicked guitar and soft piano; "
    "brushed drums and upright bass enter in the chorus."
)

DEFAULT_LYRICS = """[verse]
Morning light filtering through the pine
Every quiet street is yours and mine
[chorus]
Softly the world begins to breathe"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", default=DEFAULT_PROMPT, help="music description")
    ap.add_argument("--lyrics", default=DEFAULT_LYRICS, help="lyrics with [section] tags")
    ap.add_argument("--lyrics-file", type=Path, help="read lyrics from a file instead")
    ap.add_argument("--prompt-file", type=Path, help="read the description from a file instead")
    ap.add_argument("--duration", type=float, default=30.0, help="seconds of audio")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out", type=Path, default=Path("song.wav"))
    ap.add_argument(
        "--model-dir",
        type=Path,
        default=MODEL_DIR,
        help="local MiniMax-Music3 folder (default: <repo>/minimax_ttm)",
    )
    ap.add_argument(
        "--no-stream-lm",
        action="store_true",
        help="keep the LM resident (needs ~22 GB VRAM; fails on a 16 GB card)",
    )
    ap.add_argument(
        "--offload-type",
        default="leaf_level",
        choices=["leaf_level", "block_level"],
        help=(
            "LM streaming granularity. Keep leaf_level: the pipeline calls "
            "embed_tokens/lm_head directly, and only leaf_level hooks those, so "
            "block_level leaves them stranded on CPU and crashes."
        ),
    )
    ap.add_argument(
        "--blocks-per-group",
        type=int,
        default=4,
        help="transformer blocks resident at once when using block_level",
    )
    args = ap.parse_args()

    lyrics = args.lyrics_file.read_text(encoding="utf-8") if args.lyrics_file else args.lyrics
    prompt = args.prompt_file.read_text(encoding="utf-8") if args.prompt_file else args.prompt

    free, total = torch.cuda.mem_get_info()
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM free: {free / 1024**3:.1f} GB of {total / 1024**3:.1f} GB")

    print("Loading components (this takes a few minutes on first run)...")
    t0 = time.time()
    manager = ComponentsManager()
    manager.enable_auto_cpu_offload(device="cuda")
    pipe = ModularPipeline.from_pretrained(str(args.model_dir), components_manager=manager)
    pipe.load_components(dtype=torch.bfloat16)

    if not args.no_stream_lm:
        # The 8B LM is ~16.4 GB in bf16 and cannot stay resident on a 16 GB card,
        # so it is streamed. block_level moves whole transformer blocks and is
        # usually faster than leaf_level, which shuttles individual Linears.
        kwargs = {}
        if args.offload_type == "block_level":
            kwargs["num_blocks_per_group"] = args.blocks_per_group
        apply_group_offloading(
            pipe.language_model,
            onload_device=torch.device("cuda"),
            offload_type=args.offload_type,
            use_stream=True,
            **kwargs,
        )
    print(f"Loaded in {time.time() - t0:.0f}s")

    print(f"Generating {args.duration:.0f}s of audio (seed {args.seed})...")
    t0 = time.time()
    audio = pipe(
        prompt=prompt,
        lyrics=lyrics,
        audio_duration=args.duration,
        generator=torch.Generator("cuda").manual_seed(args.seed),
        output="audios",
    )[0]
    print(f"Generated in {time.time() - t0:.0f}s")

    # The pipeline may hand back a torch tensor or a numpy array depending on
    # version; normalise before writing. Dump the raw array first so a write
    # failure never costs a full regeneration.
    if isinstance(audio, torch.Tensor):
        samples = audio.T.float().cpu().numpy()
    else:
        samples = np.asarray(audio).T.astype(np.float32)

    # The model's output peaks at exactly 1.0 and the WAV writer hard-clips
    # above it (0 / 6 / 33 / 278 clipped samples across the first batch).
    # Scale down only when needed so quieter renders are left untouched.
    peak_in = float(np.abs(samples).max())
    if peak_in > 0.95:
        samples = samples * (0.95 / peak_in)
        print(f"Peak-normalised {peak_in:.3f} -> 0.950")

    raw = args.out.with_suffix(".npy")
    np.save(raw, samples)

    sr = getattr(pipe, "sampling_rate", 32000)
    sf.write(str(args.out), samples, sr)
    raw.unlink(missing_ok=True)

    # Sidecar with everything needed to reproduce this render. The caption is
    # stored verbatim because vocal character is driven by its wording, not the
    # seed -- the seed alone does not pin the voice.
    meta = {
        "output": args.out.name,
        "seed": args.seed,
        "audio_duration_requested": args.duration,
        "audio_duration_actual": round(len(samples) / sr, 2),
        "sampling_rate": sr,
        "caption": prompt,
        "lyrics": lyrics,
        "offload_type": args.offload_type,
        "dtype": "bfloat16",
        "model_dir": str(args.model_dir),
        "versions": {
            "torch": torch.__version__,
            "diffusers": importlib.metadata.version("diffusers"),
            "transformers": importlib.metadata.version("transformers"),
        },
    }
    args.out.with_suffix(".json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    peak = torch.cuda.max_memory_allocated() / 1024**3
    print(f"Wrote {args.out.resolve()}  |  {sr} Hz  |  peak VRAM {peak:.1f} GB")


if __name__ == "__main__":
    main()
