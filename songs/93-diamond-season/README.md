# Diamond Season

**Status: written and verified, NOT rendered. Not yet in the queue — say when.**

Ninety-third song. Female lead, same singer as the rest of the catalogue —
cinematic dance-pop with **a rapped second verse by the same female lead**.
126 BPM, B minor, no modulation. Glass-like synth plucks are the signature,
alone in the intro and alone again in the outro, with a four-on-the-floor
chorus and a wide instrumental drop in between.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 728 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 126 BPM, B minor, the glass-pluck signature, the half-time rapped verse and the drop. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 89 entries — with the character bible, the three-world grade table, the four match cuts on the drop, and the transformation-cut challenge |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 93-diamond-season
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\93-diamond-season\caption.txt `
  --lyrics-file songs\93-diamond-season\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\93-diamond-season\output\diamond_season.wav
```

Expected ~2 h.

## Pacing: the one thing to watch

This is an uptempo song with a rapped verse, and uptempo pacing is still
unmeasured across the catalogue. Every rendered song so far has been a
ballad at 92–98 BPM singing at 116–153 words per minute. At 126 BPM with a
half-time rap verse this will pace faster, but by how much is a guess until
it renders. The lyrics are 728 words:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.3 min | **overrun — outro lost** |
| **140 wpm (the guard setting)** | 5.2 min | 87% |
| 160 wpm | 4.6 min | 76% |

`render.json` sets a deliberately conservative 140 wpm for the length guard.
**If the first render truncates the outro, drop the second post-chorus and
re-render.** The measured pacing should be recorded in
[`docs/VOICE_RECIPE.md`](../../docs/VOICE_RECIPE.md) either way.

## What changed from the submission

| Change | Why |
|---|---|
| Descriptive tag lines reduced to plain `[intro]`, `[verse]`, `[chorus]` etc. | Text on a tag line is silently dropped, and only the documented tags exist |
| `[rap]` → `[verse]`; the rapped delivery moved into the caption | The checkpoint has no rap tag; delivery direction belongs in the caption or it gets sung as words |
| Arrangement and performance direction moved out of the lyric body into the caption's `Arrangement` and `Global Emotional Progression` blocks | The model sings the lyric body literally |
| Quotation marks and em-dashes removed; digits spelled as words | Punctuation is not sung and digits are sung unpredictably |

Kept exactly as written: every lyric line, 126 BPM, B minor with no
modulation, the instrumentation, the energy arc and the four viral moments.

## The story and the hooks

She spent years on the night shift cleaning the glass over other people's
jewellery. The video takes her from that display case, down into a dark seam
of rock, and out onto a gala staircase. The second verse is the same singer
rapping a cold, precise ten-year account over half-time drums. The bridge
deliberately refuses the suffering-is-beautiful reading: the pressure is not
what made her worth the light, it is only what she survived.

**The hook:** *"Diamond season."*

**The caption line:** *"Every cut you ever gave me is a facet in the end."*

**The rap clip:** *"That is not luck, that's geometry, friend."*

**The quote card:** *"I did not need the pressure to be worth the light. But
the pressure came, and I did not break, and that is mine."*

**The challenge:** the transformation cut — film yourself in your work
clothes, cut on the first *"carbon, carbon"* and land on the version of you
that took ten years.

**Why it can travel:** it is a glow-up record with an actual argument in it,
at a tempo the transformation edit already uses, and the four match cuts on
the drop are built to be copied frame for frame.

## Lyrics as they will be sung

```
[intro]
Night shift, glass case, cloth in my hand,
Wiping other people's diamonds off the stand.
Somebody said, that's as close as you get,
I said, give it ten years, and I'll take that bet.

[verse]
Twenty-two, two jobs and a folding bed,
Four Cs on a poster and they lived in my head.
Cut, colour, clarity, carat, in that order,
Said them like a prayer while I locked the door.
Everybody's diamond came out of the dark,
Nobody asks a stone what it cost to start.
They only see the setting, they never see the mine,
Never see the hands that put the shine on the shine.
So I kept my head down and I let it press,
Diamonds don't get made out of comfort and rest.

[pre-chorus]
Two thousand degrees and a mile of stone,
Nobody heard a thing, I was down there alone.
Now the lid comes off and the room goes still,
Count it down and let the light spill.
Here we go.

[chorus]
Pressure made me, now it's diamond season,
You can hate the way I shine, you don't get a reason.
I was carbon in the dark with a weight on my chest,
Now the light goes right through me and comes out the best.
Turn me, turn me, catch the edge,
Every cut you ever gave me is a facet in the end.
Pressure made me, now it's diamond season,
Diamond season, diamond season.

[post-chorus]
Carbon, carbon, hold the line,
Carbon, carbon, give it time.
Pressure, pressure, hold me down,
That is how a diamond gets its crown.
Diamond season, diamond season,
Ten years cooking, here's the reason.

[verse]
Ten years pressing, ten years quiet, ten years carbon in the seam,
Every no was a hundred atmospheres, every knockback was a squeeze.
They said the girl with the cloth ain't the girl on the tray,
Now the girl with the cloth got the loupe and the say.
Cut me at an angle where the light has to bend,
That is not luck, that's geometry, friend.
Clarity is nothing but the flaws I outgrew,
Colour is the temper that the fire ran through.
Carat is the years, so go on, count the weight,
I don't shine for a room, the room can catch up late.
Put a hand on the velvet, but don't touch the glass,
Everything I am I made out of the past.

[pre-chorus]
Two thousand degrees and a mile of stone,
Nobody heard a thing, I was down there alone.
Now the doors come off and the whole room turns,
Count it down and let it burn.
Here we go.

[chorus]
Pressure made me, now it's diamond season,
You can hate the way I shine, you don't get a reason.
I was carbon in the dark with a weight on my chest,
Now the light goes right through me and comes out the best.
Turn me, turn me, catch the edge,
Every cut you ever gave me is a facet in the end.
Pressure made me, now it's diamond season,
Diamond season, diamond season.

[instrumental]

[bridge]
Do not get it wrong, I would not wish the weight,
I am not the girl who says the dark was great.
Nobody needs a mile of stone on their chest
To be worth the velvet, to be worth the rest.
I did not need the pressure to be worth the light,
But the pressure came, and I did not break, and that is mine.
So I will take the season and I will take the shine,
And I'll leave the door open for the next one in line.

[chorus]
Pressure made me, now it's diamond season,
You can hate the way I shine, you don't get a reason.
I was cloth on a glass case, closing up alone,
Now the case is open and the light is my own.
Turn me, turn me, catch the edge,
Every cut you ever gave me is a facet in the end.
Pressure made me, now it's diamond season,
Diamond season, diamond season.

[post-chorus]
Carbon, carbon, hold the line,
Carbon, carbon, give it time.
Pressure, pressure, hold me down,
That is how a diamond gets its crown.
Diamond season, diamond season,
Ten years cooking, here's the reason.

[outro]
Night shift, glass case, cloth in her hand,
Somebody's wiping the glass where I stand.
I told her, ten years, and I meant every one,
Diamond season, and it's only begun.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 728 at 140 wpm → ~312 s (5.2 min), 7800/9000 frames (87% of cap) |
| Caption + lyrics tokens | 2292 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
