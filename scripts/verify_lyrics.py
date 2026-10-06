"""Check a song folder against the model's hard limits before spending GPU hours.

Usage:
    .venv\\Scripts\\python.exe scripts\\verify_lyrics.py songs\\02-someone-elses-forever
    .venv\\Scripts\\python.exe scripts\\verify_lyrics.py songs\\02-someone-elses-forever --voice-ref songs\\01-fire-in-the-rain

Checks:
  - sung-word count and estimated length vs the 9000-frame (6 min) cap
  - caption + lyrics token count vs the 5000-token prompt limit
  - every section tag sits alone on its line (text on a tag line is dropped)
  - no stage directions in the lyric body (they would be sung)
  - optionally, that the Vocal Details and Sonics blocks are byte-identical to
    a reference song's caption (the voice lock)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENIZER_DIR = ROOT / "minimax_ttm" / "tokenizer"

MAX_FRAMES = 9000
FRAME_RATE = 25
MAX_TOKENS = 5000
WORDS_PER_MIN = 116  # measured on this setup; MiniMax's own example implies ~90
SAFE_FRAME_FRACTION = 0.93

TAG_RE = re.compile(r"\[[a-z\- ]+\]")


def block(text: str, start: str, end: str) -> str:
    i = text.index(start)
    return text[i : text.index(end, i)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("song_dir", type=Path)
    ap.add_argument("--voice-ref", type=Path, help="song folder whose caption defines the voice")
    args = ap.parse_args()

    caption = (args.song_dir / "caption.txt").read_text(encoding="utf-8")
    lyrics = (args.song_dir / "lyrics.txt").read_text(encoding="utf-8")
    ok = True

    # Optional per-song overrides: songs/<song>/render.json {"wpm": 140}.
    # Uptempo / rap songs sing far faster than the ballad default.
    wpm = WORDS_PER_MIN
    cfg_path = args.song_dir / "render.json"
    if cfg_path.exists():
        import json
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        wpm = float(cfg.get("wpm", wpm))

    def report(label: str, passed: bool, detail: str) -> None:
        nonlocal ok
        ok &= passed
        print(f"  [{'OK' if passed else 'FAIL'}] {label}: {detail}")

    print(f"Checking {args.song_dir}")

    words = len(lyrics.split()) - lyrics.count("[")
    seconds = words / wpm * 60
    frames = seconds * FRAME_RATE
    report(
        "length",
        frames < MAX_FRAMES * SAFE_FRAME_FRACTION,
        f"{words} sung words at {wpm:.0f} wpm -> ~{seconds:.0f}s ({seconds/60:.1f} min), "
        f"{frames:.0f}/{MAX_FRAMES} frames ({frames/MAX_FRAMES*100:.0f}% of cap)"
        + (" [wpm from render.json]" if wpm != WORDS_PER_MIN else ""),
    )

    try:
        from transformers import AutoTokenizer

        tok = AutoTokenizer.from_pretrained(str(TOKENIZER_DIR))
        n = len(tok(caption + lyrics).input_ids)
        report("tokens", n < MAX_TOKENS, f"caption + lyrics = {n}/{MAX_TOKENS}")
    except Exception as exc:  # tokenizer missing is not fatal for the other checks
        report("tokens", False, f"could not tokenize: {exc}")

    bad_tags = [
        line for line in lyrics.splitlines()
        if line.strip().startswith("[") and not TAG_RE.fullmatch(line.strip())
    ]
    report("section tags", not bad_tags, "all alone on their line" if not bad_tags else f"text on tag line: {bad_tags}")

    directions = [line for line in lyrics.splitlines() if "*" in line or re.search(r"^\s*\(.*\)\s*$", line)]
    report("stage directions", not directions, "none in lyric body" if not directions else f"would be sung: {directions}")

    # The video character's name must never be sung (user rule, 2026-09-03).
    named = [line.strip() for line in lyrics.splitlines() if "mahima" in line.lower()]
    report("character name", not named, "not in lyrics" if not named else f"NAME IN LYRICS: {named}")

    if args.voice_ref:
        ref = (args.voice_ref / "caption.txt").read_text(encoding="utf-8")
        # Sonics must match exactly.
        s, e = "Sonics & Production Profile:", "\nVocal Details"
        same = block(ref, s, e) == block(caption, s, e)
        report("voice lock / Sonics", same, "byte-identical to reference" if same else "DIFFERS from reference")
        # Vocal Details: every reference line must be present verbatim. Extra
        # lines are allowed so a duet can add a second singer without
        # touching the lead's description.
        s, e = "Vocal Details\n", "\nArrangement"
        ref_lines = [l for l in block(ref, s, e).splitlines() if l.strip() and l.strip() != "Vocal Details"]
        new_block = block(caption, s, e)
        missing = [l.split(":")[0] for l in ref_lines if l not in new_block]
        report(
            "voice lock / Vocal Details",
            not missing,
            "all reference lines present verbatim" if not missing else f"changed or missing: {missing}",
        )

    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
