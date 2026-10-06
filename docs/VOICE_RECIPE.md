# Voice Recipe

How the female lead voice established in [Fire in the Rain](../songs/01-fire-in-the-rain/README.md)
is carried into every later song.

## Read this first: the seed does not lock the voice

MiniMax Music 3 has **no voice conditioning**. The pipeline accepts only
`prompt`, `lyrics`, `audio_duration`, `generator`, `num_inference_steps` —
there is no speaker embedding, no voice cloning, no reference-audio input.
(Verified against `modular_blocks_minimax_music3.py`.)

Vocal identity emerges from two things, in this order of importance:

1. **The `Vocal Details` wording in the caption** — the dominant lever. Keep it
   byte-identical and the timbre stays in the same family.
2. **The seed** — controls the sampling trajectory. Identical seed + identical
   caption + identical lyrics reproduces a render exactly. But **change the
   lyrics and the token sequence changes**, so the RNG stream diverges and the
   voice will be *similar, not identical*.

So: for a new song in this voice, copy the `Vocal Details` and `Sonics &
Production Profile` blocks from `songs/01-fire-in-the-rain/caption.txt`
**verbatim** and keep seed 42. Expect a consistent character, not a cloned
singer. If a particular take is perfect, that exact WAV is the only guaranteed
copy of it.

`scripts/verify_lyrics.py --voice-ref songs/01-fire-in-the-rain` checks the
two blocks are byte-identical before you render.

## The locked settings

| Setting | Value |
|---|---|
| Seed | `42` |
| Reference caption | `songs/01-fire-in-the-rain/caption.txt` |
| Blocks to copy verbatim | `Vocal Details`, `Sonics & Production Profile` |
| BPM / key | 96, F♯ minor (change only if the song needs it) |
| Sampling rate | 44100 Hz stereo (pipeline value; README's "32 kHz" is stale) |
| dtype | `bfloat16` |
| Offload | `leaf_level` streaming (mandatory on 16 GB — see below) |
| Inference steps | 30 (default, unchanged) |

Everything else in the caption — emotional progression, imagery, section
dynamics, percussion texture — is free to change per song.

## Writing new lyrics for this voice

- **Never put the character's name in the sung lyrics.** "Mahima" is the
  video character only. Songs 2, 3 and 5 were first rendered with the name
  sung once each; those takes are archived in `output/v1-with-name/` and the
  songs re-rendered without it. `verify_lyrics.py` now fails any lyrics that
  contain the name. (Rule set 2026-09-03; song 6's first render was aborted
  over it.)

- **Budget ~116 words per minute of music.** Measured on this setup: 500 sung
  words rendered to 258 s. MiniMax's own reference example implies 90 wpm
  (429 words → 284.9 s), so pacing varies with style — treat 90 as the
  conservative end and 116 as typical for this caption.
- **Hard cap 9000 frames at 25 fps = 6.0 minutes.** At 116 wpm that is ~696
  words. Stay under ~620 words for safety margin.
- **Section tags go on their own line** — `[intro]`, `[verse]`, `[pre-chorus]`,
  `[chorus]`, `[instrumental]`, `[bridge]`, `[outro]`. Text on the same line as
  a tag **is silently dropped** by the checkpoint's input contract.
- **Never put stage directions in the lyrics.** Anything like
  `*(half-time, piano only)*` gets **sung as words**. Put it in the caption's
  `Arrangement` section instead.
- Caption + lyrics must fit 5000 tokens (a typical pair uses ~1800).

## Environment

Isolated venv at `.venv` — deliberately separate from the global Python, which
has CPU-only torch.

```
torch          2.13.0+cu126
diffusers      0.40.0.dev0   (PR build dafe3733, minimax-music3-integration)
transformers   5.16.1
accelerate     1.14.0
soundfile      0.14.0
numpy          2.2.6
```

`minimax_ttm/modular_model_index.json` is patched to point at the local model
directory. Re-running `hf download` reverts it and will silently re-download
~30 GB into the HF cache. Original preserved as `modular_model_index.json.orig`.

## Performance on RTX 4090 Laptop (16 GB)

| Song | Words | Audio | Pacing | Render time |
|---|---|---|---|---|
| smoke test | — | 30 s | — | 682 s |
| song 1 sample | 77 | 58 s | — | 1307 s |
| 01 Fire in the Rain | 500 | 4:18 | 116 wpm | 6041 s (1 h 41 m) |
| 02 Someone Else's Forever | 614 | 4:50 | 127 wpm | 7098 s (1 h 58 m) |
| 03 Hey Stranger | 613 | 3:59 | 153 wpm — short chanted hook lines pace fast | 5632 s (1 h 34 m) |
| 04 Polaroids in My Pocket | 632 | 5:13 | 121 wpm | 7458 s (2 h 04 m) |
| 05 Last Train Home | 626 | 5:11 | 121 wpm | 7423 s (2 h 04 m) |

Pacing ranges 116–153 wpm depending on how chant-like the lyrics are. Plan
with 120 wpm for verse-heavy songs; hook-heavy songs can carry ~25% more
words. Render time is ~23–24× the audio length regardless.

All of those are ballads at 92–98 BPM. For an uptempo or rap song, put a
`render.json` in the song folder — `{"wpm": 140}` — and `verify_lyrics.py`
uses that instead of the 116 default for the length guard. Song 8 (136 BPM,
rap) is the first; its measured pacing should be recorded here after it
renders.

Peak VRAM 6.9–7.3 GB — this is **not** spare headroom. It is low precisely
because `leaf_level` streaming keeps only one leaf module resident at a time.

Two faster configurations were tested and **both fail on a 16 GB card**:

- `--no-stream-lm` — needs the 8B LM resident (~16.4 GB in bf16) plus the RVQ
  depth decoder; exceeds 16 GB. Raises "language model and the RVQ depth
  decoder must fit on the device together".
- `--offload-type block_level` — the pipeline calls `embed_tokens` / `lm_head`
  directly, and only `leaf_level` hooks those submodules. Block-level leaves
  their weights on CPU: "Expected all tensors to be on the same device".

`leaf_level` is the only working mode here. For real speedup the path is
SGLang-Omni under WSL2, which would use the `dav.pth` / `flowmatching_vae.pth` /
`qwen_7B/` weights already on disk (untested).

## The male family (songs 101 to 105)

Songs 101 to 105 are sung by a father to his daughter, so they cannot use
the female lead of songs 01 to 100. They form their own voice family.

- **The reference is song 101** (`songs/101-the-day-you-found-me/caption.txt`).
  Its `Sonics` and `Vocal Details` blocks are the lock for all five songs.
- Songs 102 to 105 copy those blocks byte-for-byte. Only the global metadata,
  arrangement and imagery change per song.
- The render queue verifies each family against its own reference (see
  `voice_ref_for` in `scripts/render_queue.py`), and the audit does the same.
- Keep the same seed, 42, for the family, as the female family does.
