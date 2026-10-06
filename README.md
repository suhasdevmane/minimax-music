# minimax-music

Local song generation with [MiniMax Music 3](https://huggingface.co/MiniMaxAI/MiniMax-Music3)
on a single 16 GB GPU, plus the songs made with it.

## Layout

```
minimax-music/
├── README.md                  ← this file
├── requirements.txt
├── docker-compose.yml         ← render service; fetches weights on first start
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh          ← ensures the 54 GB of weights exist, then runs
├── scripts/
│   ├── generate.py            ← render a song (writes WAV + .json sidecar)
│   ├── verify_lyrics.py       ← check one song folder against model limits
│   ├── render_queue.py        ← render a list of songs unattended
│   ├── render_pending.py      ← render every song that has no audio yet
│   ├── fetch_model.py         ← download the weights and fix the model index
│   ├── bootstrap.sh           ← set up on a bare host, no Docker, no root
│   ├── audit_catalogue.py     ← check every song folder, and cross-song originality
│   └── update_checklist.py    ← tick CATALOGUE.md from what is on disk
├── docs/
│   ├── VOICE_RECIPE.md        ← how the voice is kept consistent across songs
│   ├── SONG_TEMPLATE.md       ← the file spec every song folder follows
│   └── LYRIC_CRAFT.md         ← the craft standard the lyrics are held to
├── songs/
│   ├── CATALOGUE.md                ← the 92-song plan, briefs and checklist
│   ├── 01-fire-in-the-rain/        ← rendered 4:18
│   ├── 02-someone-elses-forever/   ← rendered 4:50
│   ├── 03-hey-stranger/            ← rendered 3:59
│   ├── 04-polaroids-in-my-pocket/  ← rendered 5:13 (duet)
│   ├── 05-last-train-home/         ← rendered 5:11
│   ├── 06-you-lost-me-i-found-me/  ← rendered 4:52
│   ├── 07-ghost-in-my-dms/         ← written, awaiting render
│   ├── 08-power-back-on/           ← written, awaiting render (uptempo duet + rap)
│   └── 09-…/ … /100-…/             ← the catalogue, written to the same template
├── experiments/
│   └── smoke-test/            ← first pipeline proof, not a deliverable
├── minimax_ttm/               ← model weights (54 GB, not in git)
└── .venv/                     ← isolated Python env (not in git)
```

Every song folder is self-contained and follows the same template:

```
songs/NN-song-name/
├── README.md          ← song sheet: theme, arc, lyrics, render facts
├── caption.txt        ← music description fed to the model
├── lyrics.txt         ← render-ready lyrics
├── source/            ← original drafts / submissions (optional)
├── video/             ← video prompts, shot lists (optional)
├── output/            ← rendered .wav / .mp3 and the .json sidecar
└── logs/              ← render logs
```

Folder and file names use the song title, never a character name.

## Setup (once)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cu126
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
hf download MiniMaxAI/MiniMax-Music3 --local-dir .\minimax_ttm
```

Then point the model index at the local folder — it ships hardcoded to the hub
repo id and would otherwise re-download 30 GB into the HF cache:

```powershell
(Get-Content minimax_ttm\modular_model_index.json) -replace '"MiniMaxAI/MiniMax-Music3"', '"C:/Users/suhas/Documents/minimax-music/minimax_ttm"' | Set-Content minimax_ttm\modular_model_index.json
```

Re-running `hf download` reverts that patch. The original is kept as
`modular_model_index.json.orig`.

## What is not in git

Two things are deliberately excluded, and both come back automatically.

| Excluded | Size | How it comes back |
|---|---|---|
| `minimax_ttm/` model weights | 54 GB | `scripts/fetch_model.py`, run by the container entrypoint and by `bootstrap.sh` |
| Rendered `.wav` / `.mp3` / `.mp4` | ~920 MB | Re-rendered from each song's `caption.txt` + `lyrics.txt` at seed 42 |

A fresh clone is a few megabytes. The `.json` sidecar beside every render
**is** tracked, so the seed, caption, lyrics and library versions that
produced each take stay in history even though the audio does not.

The weights need one fix that cannot be committed: the checkpoint hardcodes
its Hugging Face repo id inside `modular_model_index.json`, and left alone
the pipeline re-downloads about 30 GB into the HF cache at load time. The
value has to be the local directory's absolute path, which differs per
machine. `scripts/fetch_model.py` rewrites it, rebuilding from the pristine
`.orig` backup each run so it never inherits another machine's path.

## Deploying on a server

### With Docker

```bash
cp .env.example .env          # optional; defaults work
docker compose up --build     # first start downloads ~54 GB, then renders
docker compose logs -f render
```

Needs the NVIDIA container runtime. Weights persist in the `models` volume,
so the download is paid once. Finished audio lands in `./songs/*/output/`
on the host.

### Without Docker, and without root

This is the path for a shared machine where you have no sudo:

```bash
bash scripts/bootstrap.sh     # venv, torch cu126, deps, then the weights
tmux new -s render
. .venv/bin/activate && python scripts/render_pending.py
# detach: Ctrl+B then D
```

Use tmux, or the render dies with your SSH session: each song takes about
two hours. On a shared GPU, pin a card with `CUDA_VISIBLE_DEVICES=0` and
check `nvidia-smi` first. Bind nothing to `0.0.0.0`.

### Checking state without a GPU

```bash
python scripts/fetch_model.py --check      # are the weights complete and patched
python scripts/render_pending.py --list    # what still needs rendering
python scripts/audit_catalogue.py --no-verify
```

## The catalogue

[`songs/CATALOGUE.md`](songs/CATALOGUE.md) holds the plan for songs 09–100:
a brief per song (slug, genre, BPM, key, solo or duet, pacing class, hook,
concept, video world), the production standard the writing is held to, the
rap-and-delivery map, the US/UK register map, and the completion checklist.

## Make a song

1. Create `songs/NN-song-name/` from the template above. The full spec is
   [`docs/SONG_TEMPLATE.md`](docs/SONG_TEMPLATE.md); the craft standard for
   the words themselves is [`docs/LYRIC_CRAFT.md`](docs/LYRIC_CRAFT.md).
2. Write `caption.txt` and `lyrics.txt`. To keep the established voice, copy
   the `Vocal Details` and `Sonics` blocks from song 1 verbatim — see
   [`docs/VOICE_RECIPE.md`](docs/VOICE_RECIPE.md).
3. Verify before spending GPU time:

   ```powershell
   .\.venv\Scripts\python.exe scripts\verify_lyrics.py songs\NN-song-name --voice-ref songs\01-fire-in-the-rain
   ```

   To check the whole catalogue at once, including cross-song originality:

   ```powershell
   .\.venv\Scripts\python.exe scripts\audit_catalogue.py
   ```

4. Render:

   ```powershell
   .\.venv\Scripts\python.exe scripts\generate.py `
     --prompt-file songs\NN-song-name\caption.txt `
     --lyrics-file songs\NN-song-name\lyrics.txt `
     --duration 355 --seed 42 `
     --out songs\NN-song-name\output\song-name.wav
   ```

   A `.json` sidecar with seed, caption, lyrics and library versions is written
   next to the WAV.

## Hard limits (verified in the pipeline source)

| Limit | Value |
|---|---|
| Audio length | 9000 frames at 25 fps = 6.0 min. `--duration` is a ceiling; the model stops early when the lyrics are done. |
| Prompt | caption + lyrics ≤ 5000 tokens |
| Pacing | ~116 sung words per minute measured here → keep lyrics under ~620 words |
| Section tags | `[verse]`, `[chorus]` etc. **alone on their line**. Text on a tag line is silently dropped. |
| Stage directions | Never in the lyric body — they get sung. Put them in the caption's `Arrangement` block. |
| Output | 44.1 kHz stereo (the README's "32 kHz" applies to the SGLang path) |

## Performance (RTX 4090 Laptop, 16 GB)

| Audio | Render |
|---|---|
| 30 s | 682 s |
| 60 s | 1307 s |
| 4.3 min | 6041 s (1 h 41 m) |

Roughly 23× realtime. The 8B language model does not fit in 16 GB, so it is
streamed layer-by-layer (`leaf_level`); this is the only working mode on this
card — details in `docs/VOICE_RECIPE.md`. Free the GPU first: ollama and
ComfyUI together were holding 13 GB.

## Git notes

Not yet a git repository. When initialising: `.venv/` and `minimax_ttm/` are
ignored; rendered audio is tracked through Git LFS (see `.gitattributes`).
