# City Lights Don't Sleep

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninety-ninth song. Female lead **Mahima**, modern synthwave in a UK northern
register with a fully spoken-word bridge. 114 BPM, F minor. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words, ballad/mid budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 114 BPM, F minor, sixteenth-note bass arpeggio, gated reverb drums, chorused guitar, and the tram, ring-road, cafe and siren textures. A `Delivery Note` line carries the northern register and the spoken-word bridge. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — with a two-look character bible, a seven-person night-shift bible, the one-light-per-frame rule, the single-take bridge, the streetlights challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 114 BPM this is a ballad/mid song and the length guard's
116 wpm default is the right estimate. The spoken bridge will pace faster than
sung lines, which gives the outro a little extra headroom rather than less.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 99-city-lights-dont-sleep
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\99-city-lights-dont-sleep\caption.txt `
  --lyrics-file songs\99-city-lights-dont-sleep\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\99-city-lights-dont-sleep\output\city_lights_dont_sleep.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from *get some rest* in the bridge | Punctuation is not sung and quotation marks confuse the tokenizer |
| Em-dashes in the bridge and the post-chorus replaced with commas | The model sings the lyric body literally |
| `3am` → *"Three in the morning"*; `3:30` → *"half past three"*; `4am` → *"four"*; `5:30` → *"Half five"* | The model sings digits unpredictably |
| The spoken-word direction moved out of the lyric body into the caption as a `Delivery Note` line | Stage directions in the body get sung |
| `[verse 1]` / `[verse 2]` / `[spoken bridge]` / `[final chorus]` reduced to plain tags | Only the checkpoint's documented tags exist; there is no `[spoken]` tag, so the delivery lives in the caption |
| The final chorus written out in full rather than `(as chorus 1)`, keeping its two past-tense variant lines | The verify script flags `(repeat)`, and the model would sing it |
| Trimmed thirty words across the choruses, verses, pre-choruses and bridge | 669 words overran the 640-word ballad budget; the cuts were auxiliaries and articles, and no image was lost |

Kept exactly as written: every image, 114 BPM, F minor, the instrumentation,
the northern register, and the bridge's argument word for word.

## The story and the hooks

Three in the morning, wide awake and not remotely sad about it. She takes her
coat off the back of the door and goes to see who else is still up. An empty
tram with all its lights on. A lad hosing down the front of a chip shop. A fox
on a corner that will not move for her. A canal holding the whole of Ancoats
on a surface with no ripple in it. Then the second population: the night shift,
the sleepless and the ones just clocking off, who nod at her like a handover
and never ask a question. At four there is a caff on Oldham Street where the
woman behind the counter pours before she asks, and nobody in the room is
anybody's problem. The bridge is spoken, not sung, and it is the whole record:
people say get some rest as if rest were somewhere you drive to, the offices
are empty and the windows are still on, and she has decided that is kindness
rather than waste. At half five the streetlights go out and she goes home.

**The hook:** *"City lights don't sleep, and neither do we."*

**The line for captions:** *"Not lonely, just running on a different clock."*

**The quote, spoken:** *"The offices are empty and the windows are still on,
which is either a waste or a kindness, and I've decided it's kindness."*

**The turn:** *"So no, I'm not broken because I'm awake at four / I'm just
keeping the same hours as everything I love."*

**Why it can travel:** it takes insomnia and refuses to make it a symptom. The
whole second half is an argument that lands in a spoken bridge — the most
quotable ninety seconds in the catalogue — and the video's closing image, a
whole street of lamps cutting out at once, is something everyone has seen and
nobody has filmed.

## Lyrics as they will be sung

```
[intro]
Three in the morning and my ceiling knows my face,
Not sad, just wired, just awake.
I take my coat off the back of the door,
And go and see who else is still here.

[verse]
The tram goes past empty with its lights all on,
Like it's doing somebody a favour for nothing.
There's a lad hosing down the front of a chip shop,
And a fox on the corner that won't move for me.
The canal holds the orange of all of Ancoats,
And the water doesn't shiver, it just carries it.
Everybody I know is asleep in a postcode,
And I've never in my life felt less alone.

[pre-chorus]
The night shift and the sleepless and the lads just clocking off,
We nod like a handover, we don't ask a thing.
There's nothing to explain at half past three,
And the ring road hums a note I can sing.

[chorus]
City lights don't sleep, and neither do we,
Sodium gold and a window still green.
Not lonely, just running on a different clock,
And the whole of the skyline is up with me.
City lights don't sleep, they just turn themselves down,
They keep one eye open for whoever's around.
Put your hand on the glass and count them with me,
City lights don't sleep, and neither do we.

[verse]
There's a caff on Oldham Street that opens at four,
And the woman on the counter knows I take it strong.
Two builders, a driver, a girl in last night's dress,
And a radio that only plays songs nobody wants.
Nobody here is anybody's problem,
Nobody here is going to ask how I've been.
We're just the people that the daylight hasn't counted,
And I like the arithmetic that leaves us in between.

[pre-chorus]
The gritters and the bakers and the ones who cannot stop,
We nod like a handover, we don't ask a thing.
There's nothing to explain when the sky goes grey,
And the ring road hums a note I can sing.

[chorus]
City lights don't sleep, and neither do we,
Sodium gold and a window still green.
Not lonely, just running on a different clock,
And the whole of the skyline is up with me.
City lights don't sleep, they just turn themselves down,
They keep one eye open for whoever's around.
Put your hand on the glass and count them with me,
City lights don't sleep, and neither do we.

[instrumental]

[bridge]
People say get some rest, like rest is somewhere you drive to.
I've tried. I've laid there and listened to my own blood.
Out here the city is doing the same thing I am,
Holding a light up because somebody has to.
The offices are empty and the windows are still on,
Which is either a waste or a kindness, and I've decided it's kindness.
So no, I'm not broken because I'm awake at four,
I'm just keeping the same hours as everything I love.

[chorus]
City lights don't sleep, and neither do we,
Sodium gold and a window still green.
Not lonely, just running on a different clock,
And the whole of the skyline is up with me.
City lights don't sleep, they just turn themselves down,
They kept one eye open till the morning came round.
Put your hand on the glass, you were counting with me,
City lights don't sleep, and neither do we.

[post-chorus]
Leave it on, leave it on, out to the ring road,
Leave it on, leave it on, till the morning takes over.
Somebody out there is watching the same light,
Leave it on, leave it on, we'll get there together.

[outro]
Half five and the sky turns the colour of a bruise,
Then it fades like a dimmer and the streetlights go out.
I'll sleep when the buses are full and the city has company,
City lights don't sleep, and neither do we.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2227 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
