# TODO

## Where the catalogue stands

**Songs 09–100 are written, verified and audited — 92 of 92.** None are
rendered yet. Songs 01–06 are rendered; 07 and 08 are written and waiting.

```powershell
.\.venv\Scripts\python.exe scripts\audit_catalogue.py        # full check, ~20 s
.\.venv\Scripts\python.exe scripts\update_checklist.py       # re-tick CATALOGUE.md
```

Last full run: **100 songs audited, 0 problems**, plus 17 pre-template notes
on songs 01–08 (those predate `docs/SONG_TEMPLATE.md` and most are already
rendered, so the audit reports them without failing on them).

| | |
|---|---|
| New songs | 92 (`songs/09-…` … `songs/100-…`) |
| Ballad/mid (no `render.json`) | 65 |
| Uptempo (`render.json`, wpm 140) | 27 |
| Duets and male features | 19 captions declare Singer B |
| Sung words written | 61,173 — 602 to 760 per song, mean 664 |
| Rendered | 0 of 92 |

## Overnight render, started 2026-10-06 02:13

Songs 101 to 105 (the male father-to-daughter family) are rendering in
order. Expected about 2 hours each, so roughly 10 to 11 hours in total.
Check progress with `render_queue.status` and `songs/10[1-5]-*/logs/render.log`.

- [ ] 101 The Day You Found Me
- [ ] 102 When the World Gets Loud
- [ ] 103 Your Little Book of Life
- [ ] 104 Small Hands, Big World
- [ ] 105 I'll Be There in Every Tomorrow

Songs 101 to 105 verify against song 101's voice lock, not song 01's. The
render queue maps each family to its own reference (see `voice_ref_for` in
`scripts/render_queue.py`). Before the queue knew this, all five failed the
pre-flight check against song 01 and rendered nothing.

After the renders land, listen-check each one for a consistent male lead,
the father-daughter voice mix, and that no character name is sung. Songs 101 and 102 have an
`[instrumental]` section; 103 to 105 do not, following the source drafts.

## The render backlog

At the measured ~23× realtime, a 5–6 minute song costs about **2 hours** of
GPU. Ninety-two songs is roughly **190 hours — eight days of continuous
rendering**. That is the single biggest thing left, and it is unattended
work, not authoring work.

The runner takes song folders and skips any whose output WAV already
exists, so it is safe to stop and re-run:

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 09-slow-dance-in-the-kitchen 10-sunday-mornings 11-eyes-on-me
```

Suggested order — render the experiments first, because what they teach
changes the rest:

- [ ] **1. One uptempo song, to measure pacing.** `41-weekend-starts-on-thursday`
      or `45-windows-down`. Every song rendered so far is a ballad at
      92–98 BPM; all 27 uptempo songs carry a *guessed* 140 wpm guard. One
      render replaces the guess with a number. Record it in
      `docs/VOICE_RECIPE.md`.
- [ ] **2. One duet with a rap feature.** `39-your-place-or-mine` or
      `52-after-hours`. The model has no per-line singer control, so the
      split lives in the caption's `Duet Structure` line and is followed
      loosely. Song 04's duet is still unverified by ear. This is the
      riskiest assumption in the catalogue.
- [ ] **3. Then the rest**, in catalogue order.

**If an uptempo outro truncates**, each of those READMEs names the section
to drop (usually the second post-chorus) before re-rendering.

## Carried over from the previous batch

- [ ] Re-render without the character name — **paused mid-run**:
      `02-someone-elses-forever`, `03-hey-stranger`, `05-last-train-home`.
      Previous takes are archived in each song's `output/v1-with-name/`.
      Resume: `.\.venv\Scripts\python.exe scripts\render_queue.py 02-someone-elses-forever 03-hey-stranger 05-last-train-home`
- [ ] Listen-check the rendered songs: voice consistent with song 1, song 4's
      duet actually two voices, and no character name sung.
- [ ] Add peak-normalise (−1 dBFS) to `scripts/generate.py`. Clipped-sample
      counts trended 0 → 6 → 33 → 278 across the first batch.
- [ ] Quantisation experiment: load the 8B LM in 8-bit/4-bit so it sits in
      VRAM instead of streaming over PCIe, which is the current bottleneck.
      Listen-test against song 1 before adopting.

## Known quirks

- **Song 01's output filename.** The queue derives `fire_in_the_rain.wav`
  from the folder name, but the actual rendered file is
  `fire_in_the_rain_full.wav` from an earlier naming convention. The queue
  would therefore try to render song 01 again. Don't put it in a queue, or
  rename the file first. Every other song's README command matches what the
  queue derives — `scripts/audit_catalogue.py` now enforces that.
- **Uptempo pacing is unmeasured.** See item 1 above.

## What the audit covers

`scripts/audit_catalogue.py` checks each song for required files, the
word budget for its pacing class, the legal section-tag set, banned
characters, README-to-lyrics byte identity, shot-list coverage of every
lyric line, the voice lock against song 01, `Duet Partner`/`Duet Structure`
on every song the catalogue marks as a duet or male feature, an intact
render command, stray control characters, and the token limit. Across
songs it checks that no lyric line of five or more words is shared between
any two songs, and that no title repeats.
