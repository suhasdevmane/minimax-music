# Grow Old Loud

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song eighty-four. **Female + male duet** — Mahima and a male lead trading
verses and doubling every hook — anthemic pop-rock with brass and gang
vocals, 118 BPM, E major lifting a whole step to F♯. The batch's uptempo
song. Same singer as songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 722 sung words, uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock — plus `Duet Partner` and `Duet Structure` for the male lead. 118 BPM, E major with the modulation, two guitars, four-piece brass, gang vocals and the false ending in the instrumental. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 79 entries — with a five-identity character bible spanning sixty years, the ghost timeline, the fixed-doorway decade montage, workflow, the age-jump challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 84-grow-old-loud
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\84-grow-old-loud\caption.txt `
  --lyrics-file songs\84-grow-old-loud\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\84-grow-old-loud\output\grow_old_loud.wav
```

Expected ~2 h.

## One thing to know before rendering: pacing

This is an uptempo song and uptempo pacing is still unmeasured on this setup.
Every ballad so far has sung at 116–153 words per minute; 118 BPM with gang
vocals and a chanted post-chorus will pace faster than that, but by how much
is a guess until it renders. The lyrics are 722 words. What that means at
different pacings against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.2 min | **overrun — outro lost** |
| 125 wpm | 5.8 min | 96% |
| **140 wpm (the guard setting)** | 5.2 min | 86% |
| 155 wpm | 4.7 min | 78% |

The chant sections and the two ten-line choruses sing fast; a reasonable
blended estimate is 140–150 wpm, which lands around five minutes. The guard is
set at a conservative 140. **If the first render truncates the outro, the fix
is to drop the second post-chorus (nineteen words, a repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung; the model renders the body literally |
| Digits spelled as words (*twenty-two*, *forty*, *ninety*, *eighty*, *sixty years*) | The model sings digits unpredictably |
| The descriptive tag lines (`[intro – stomps, claps, one dry guitar]`, `[verse 2 – male lead]`, `[bridge – organ and voice, half-time]`, `[final chorus – modulated]`) reduced to plain tags | Only the checkpoint's plain section tags exist; anything else is dropped or sung |
| Who sings what moved out of the lyric body into the caption's `Duet Structure` line | The model has no per-line singer control; the split lives in the caption |
| Both post-choruses and all three choruses written out in full | A `(repeat)` line would be sung |
| UK spellings normalised to US (*neighbours* → *neighbors*, *grey* → *gray*) | The catalogue's register map puts this song in the default US voice |

Kept exactly as written: the hook, the ghost couple, the thermostat, the bench
with the plaque, the father in the bridge, the emptied function room, 118 BPM,
E major with the lift, the instrumentation and the mood arc.

## The story and the hooks

Two twenty-two-year-olds get told to keep it down at a family party, and one
of them turns it into a vow. Not a vow to stay — that is assumed — a vow about
*how*. Verse one is the version of them that goes quiet at forty: beige,
careful, ordering the same thing for a decade, sitting at the back of the
wedding saying we used to. Verse two is his answer, which is a picture of
eighty: matching jackets nobody asked for, the front row at a show for a band
they outlived, a camper van and an argument at lunch, and a bench with their
names on it that they are never sitting on. Then the bridge stops being funny
for eight lines — his father went out politely, holding the door for everyone
— and the song turns from a joke into a decision. The last chorus is a
function room with the house lights up, the chairs stacked, and two people in
their eighties who will not leave the floor.

**The hook:** *"Let's grow old loud, baby, never grow old quiet."*

**The line for captions:** *"Do not let me die of being sensible."*

**The joke that lands:** *"I'll be the one still shouting when you can't
hear."*

**The turn:** *"When they turn the volume on the world down for us, let's find
the dial and break it off."*

**Why it can travel:** it is a wedding-reception record and an anniversary
record at once, it is funny without being a novelty, and the age-up video is
the most shareable format on the internet attached to a song that earns it.

## Lyrics as they will be sung

```
[intro]
Somebody's grandmother told us to keep it down,
We were twenty-two and wrong about everything but this.
So here's a promise with my whole chest in it,
We are going to be the loudest old people in this town.

[verse]
There's a version of us that goes quiet at forty,
Beige and careful with a lawn and a schedule.
Sits at the back at the wedding with a plate on their knees,
Says we used to, we used to, and never says we will.
I have met them, I have sat across from them at dinner,
They ordered the same thing they have ordered for a decade.
And I love a routine, I do, I will take the Tuesday,
But do not let me die of being sensible.

[pre-chorus]
So swear it on the driveway, swear it on the porch,
Swear it on whatever we still own at ninety.
No inside voice, no sitting one out,
No wondering what the neighbors think.

[chorus]
Let's grow old loud, baby, never grow old quiet,
Turn it up in the kitchen till the pictures leave the wall.
Let's be the ones they talk about at every family thing,
The two at the front of the dance floor who should not be there at all.
Gray hair, bad knees, brand new speakers,
Same fight about the thermostat for sixty years.
Let's grow old loud, baby, never grow old quiet,
I'll be the one still shouting when you can't hear.

[post-chorus]
Loud, loud, never grow old quiet,
Loud, loud, we are not going to try it.
Loud, loud, put the windows down,
We're the loudest old people in this town.

[verse]
I looked at you today across a sink of dishes,
And I saw the whole thing, eighty and still ridiculous.
Matching jackets that nobody on earth asked us to wear,
Front row at a show for a band that we outlived.
You singing the wrong words with total confidence,
Me swearing that the wrong words are the right ones.
A camper van, a bad map and an argument at lunch,
And a bench with our names on it that we're never sitting on.

[pre-chorus]
So swear it in the driveway, swear it in the car,
Swear it on the day a doctor says take it easy.
No inside voice, no sitting one out,
No dying with a good song left unplayed.

[chorus]
Let's grow old loud, baby, never grow old quiet,
Turn it up in the kitchen till the pictures leave the wall.
Let's be the ones they talk about at every family thing,
The two at the front of the dance floor who should not be there at all.
Gray hair, bad knees, brand new speakers,
Same fight about the thermostat for sixty years.
Let's grow old loud, baby, never grow old quiet,
I'll be the one still shouting when you can't hear.

[instrumental]

[bridge]
My father went out whispering, he was polite about it,
Held the door for everybody right up to the end.
And I loved him and I am not doing that,
I want the neighbors calling and the ceiling coming down.
So if we get the forty years, let's spend them like they're stolen,
Let's be embarrassing in every photograph.
And when they turn the volume on the world down for us,
Let's find the dial and break it off.

[chorus]
Let's grow old loud, baby, never grow old quiet,
Turn it up in the kitchen till the pictures leave the wall.
Let's be the ones they talk about at every family thing,
The two at the front of the dance floor who should not be there at all.
Gray hair, bad knees, brand new speakers,
Same fight about the thermostat for sixty years.
No last dance, no lights up, no thank you for coming,
We are staying till they stack the chairs and sweep the floor.
Let's grow old loud, baby, never grow old quiet,
I'll be the one still shouting when you can't hear.

[post-chorus]
Loud, loud, never grow old quiet,
Loud, loud, we are not going to try it.
Loud, loud, put the windows down,
We're the loudest old people in this town.

[outro]
Somebody's grandmother told us to keep it down,
And she was the last one standing at eleven.
So here's to the noise and the knees and the years,
Let's grow old loud and let them hear.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 722 at 140 wpm → ~5.2 min, 86% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2450 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
