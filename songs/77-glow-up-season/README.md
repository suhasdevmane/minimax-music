# Glow Up Season

**Status: written and verified, NOT rendered. Not yet in the queue.**

Seventy-seventh song. Female lead **Mahima** with a male rap feature on the
bridge, bright dance-pop with a drop chorus, 122 BPM, A major lifting one
step for the final chorus. Uptempo class. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock; a male pop-rapper added as Singer B with a `Duet Structure` line for the bridge. 122 BPM, A major, the drop, the chant post-chorus and the alarm-clock / camera-shutter ear candy per the submission. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 96 entries — built from the submission's scene direction, plus a three-look character bible, Kai as the rapper at the party, a faceless ex, the light-only-gets-warmer rule, workflow, the four-frame challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 77-glow-up-season
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\77-glow-up-season\caption.txt `
  --lyrics-file songs\77-glow-up-season\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\77-glow-up-season\output\glow_up_season.wav
```

Expected ~2 h.

## Pacing is unmeasured

Every ballad in the catalogue has sung at 116–153 words per minute. This
one is 122 BPM dance-pop with a twelve-bar rap bridge, so it will pace
faster, but by how much is a guess until it renders. The lyrics are 724
words. Against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.2 min | **overrun — outro lost** |
| 125 wpm | 5.8 min | 97% |
| **140 wpm (the guard setting)** | 5.2 min | 86% |
| 160 wpm | 4.5 min | 75% |

A reasonable blended estimate is 145–155 wpm, which lands around 4.8–5
minutes. The guard is set at a deliberately conservative 140. **If the
first render truncates the outro, drop the second post-chorus (16 words, a
repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| `6 a.m.` → *"Six a.m."* | The model sings digits unpredictably |
| Quotation marks around *"take it shorter"* and *"who is she"* removed | Punctuation is not sung |
| The bridge's performance direction (*male rap feature, stripped beat*) moved into the caption's `Duet Structure` line | The model sings the lyric body literally and only knows plain section tags |
| Repeated choruses and post-choruses written out in full | The verify script flags `(repeat)` and the model would sing it |

Kept exactly as written: every other line, 122 BPM, A major with the lift,
the instrumentation, the mood arc. No trimming was needed — 724 words fits
the uptempo budget.

## The story and the hooks

He left and assumed the light left with him. She got up at six, cut her
hair on a Tuesday, ran the river loop, walked into the gym that scared her,
bought the red dress that had been sitting in her cart since winter, signed
a lease with a view and painted the walls a colour he'd have hated. By the
bridge a stranger at her rooftop party is describing her to the person next
to him, and by the outro she's alone on the roof with the last of the light
and an alarm set for six again.

**The hook:** *"It's glow up season, and I'm the sun."*

**The line for captions:** *"Sleeping through the night is a work of art."*

**The four-beat line:** *"New hair, new dress, new door, new number"* — the
challenge.

**The rap clip:** *"She don't need a co-star, she's the whole view."*

**The turn:** *"Never was his shadow, I was always the one."*

**Why it can travel:** it's the glow-up reel as a real song — specific,
funny, unbitter, at a tempo transformation edits actually use — and the
four-beat line is a ready-made template.

## Lyrics as they will be sung

```
[intro]
Six a.m. and I didn't hit snooze,
Laced up the white ones, got nothing to lose.
Playlist loud and the blinds pulled wide,
This is the year I stop hiding the light.

[verse]
Booked the salon on a Tuesday afternoon,
Told her, take it shorter, I've got somewhere to be soon.
Watched the old length fall like it was never mine,
Walked out lighter with the sun on my mind.
Group chat blowing up, they said, who is she,
Same girl, new light, that's the whole story.
Ran the long loop by the river, lungs on fire,
Every mile a little further from the liar.
Gym at seven, I was scared of the room,
Now the room knows my name and my favourite tune.
Little wins stacking like a tower of gold,
I'm twenty-four and I've never felt this bold.

[pre-chorus]
He said I'd never shine without him,
Look who's lighting up the room.
Don't need a reason, don't need a witness,
Sunrise came early and it's coming through.

[chorus]
It's glow up season, and I'm the sun,
Look at me shining, yeah, look what I've become.
New hair, new dress, new door, new number,
Turned my whole winter into a summer.
It's glow up season, and I'm the sun,
Nobody's shadow, I'm the only one.
Watch me rise, watch me run,
It's glow up season, and I'm the sun.

[post-chorus]
Shine, shine, that's the season,
Glow, glow, I don't need a reason.
Shine, shine, that's the season,
It's glow up season.

[verse]
Bought the red dress that I saved in the cart,
Six months waiting for the nerve to start.
Wore it to brunch with nowhere special to be,
Corner booth, sunlight, the whole place looking at me.
Laughing so loud with my girls on the patio,
Haven't checked his page in weeks, and I don't know
What he's up to, and that's the sweetest part,
Sleeping through the night is a work of art.
Signed the lease on a place with a view,
Painted every wall a colour he'd have hated too.
Plants on the sill and a mirror by the door,
And the girl in it is somebody I'm rooting for.

[pre-chorus]
He said I'd fall apart without him,
Look who's holding the whole room.
Don't need a reason, don't need a witness,
Sunrise came early and it's coming through.

[chorus]
It's glow up season, and I'm the sun,
Look at me shining, yeah, look what I've become.
New hair, new dress, new door, new number,
Turned my whole winter into a summer.
It's glow up season, and I'm the sun,
Nobody's shadow, I'm the only one.
Watch me rise, watch me run,
It's glow up season, and I'm the sun.

[post-chorus]
Shine, shine, that's the season,
Glow, glow, I don't need a reason.
Shine, shine, that's the season,
It's glow up season.

[instrumental]

[bridge]
Saw her cross the room and the whole vibe shifted,
Not the dress, not the hair, it's the way she's lifted.
Heard some guy walked out, thought he took the light,
Now she's running every morning, sleeping every night.
Main character energy, no script, no cue,
She don't need a co-star, she's the whole view.
Every L he handed her, she flipped to a lesson,
Every door he slammed became a door to a blessing.
So if you see her shining, don't ask who she's with,
She's with herself, and honestly, that's the gift.
Glow up season, tell your friends,
Once the sun comes out, it doesn't set again.

[chorus]
It's glow up season, and I'm the sun,
Look at me shining, yeah, look what I've become.
New hair, new dress, new door, new number,
Turned my whole winter into a summer.
It's glow up season, and I'm the sun,
Never was his shadow, I was always the one.
Hands up higher, here it comes,
It's glow up season, and I'm the sun.

[post-chorus]
Shine, shine, that's the season,
Glow, glow, I don't need a reason.
Shine, shine, that's the season,
It's glow up season.

[outro]
Rooftop, last light, still warm on my face,
Didn't need him back, I just needed the space.
Tomorrow's a Monday and I'm up at six,
Glow up season, and this is just the start of it.
No countdown, no comeback, nothing to prove,
Just a girl and a sky and a whole lot of room.
It's glow up season, and I'm the sun.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 724 at 140 wpm → ~5.2 min, 86% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2547 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
