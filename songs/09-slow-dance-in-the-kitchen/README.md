# Slow Dance in the Kitchen

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninth song. **Female + male duet** — Mahima on the lead, a soft male
baritone-tenor as Singer B — warm acoustic pop ballad / indie-folk duet,
88 BPM, G major, brushed drums, upright piano and nylon guitar. Same singer
as songs 1–8 for the female lead; the male voice modelled on song 4's
Singer B.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 638 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock; Singer B added with a section-by-section duet structure. 88 BPM, G major, felt piano, nylon guitar, upright bass, brushes, the fridge hum and the kitchen timer as ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — one kitchen, one evening, a two-lead character bible with Kai, an object list, the composited-flyer note, workflow, kitchen slow-dance challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 09-slow-dance-in-the-kitchen
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\09-slow-dance-in-the-kitchen\caption.txt `
  --lyrics-file songs\09-slow-dance-in-the-kitchen\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\09-slow-dance-in-the-kitchen\output\slow_dance_in_the_kitchen.wav
```

Expected ~2 h.

## One thing to know before rendering: it's a duet

Same situation as songs 4 and 8: the model has no per-line singer control,
so the split lives in the caption's `Duet Structure` line and the model
follows it loosely. Expect the choruses as two voices; the second verse is
the one that should come out male, and the count-of-three in the bridge is
where the trade matters most. Treat the first render as a test of that.

## What changed from the submission

| Change | Why |
|---|---|
| `1, 2, 3` and `11 dollars` → *"one, two, three"*, *"eleven dollars"* | The model sings digits unpredictably |
| Quotation marks around *"come here"* and *"let's skip it"* removed | Punctuation is not sung; commas carry the pause |
| `[verse 1 – her]`, `[chorus – both, fuller]` and the other descriptive tag lines reduced to plain tags; the her / him / both split moved to the caption's `Duet Structure` line | The model only knows plain section tags and sings the lyric body literally |
| Repeated pre-chorus and choruses written out in full | The model would sing a `(repeat)` line |

Kept exactly as written: every other line, 88 BPM, G major, the
instrumentation, the mood arc. Trimmed from a 665-word first draft to 638 to
sit inside the ballad budget; the cuts were filler words, not images.

## The story and the hooks

Rent came out, so they're staying in. A bottle with a screw cap, a chipped
mug and a jam jar, the blinds pulled down, the string lights from last
December still taped to the cabinets. His socks slide on the tile, the pot
boils over, the toast burns, and she counts them in to a slow dance between
the fridge and the sink with the oven timer as the metronome. His verse is
the apology for the night out he couldn't afford, turned into eleven dollars
and a feeling. Then the bridge: she's been holding a sentence behind her
teeth, he's been practising it in the hallway mirror, they agree to say it
on three, and he says it on two. The timer dings. The final chorus has flour
on his shirt and a ring pull on her finger.

**The hook:** *"Turn the radio low, we don't need a floor / Slow dance in
the kitchen, that's what the kitchen's for."*

**The line for captions:** *"We don't need a ballroom, don't need a band."*

**The turn:** *"So let's say it on the count, let's say it on three / One,
two, and you said it before me."*

**The quote:** *"I'll take the kitchen if the kitchen comes with you."*

**Why it can travel:** it's a couple's video that costs nothing to recreate
— socks, a kitchen, a radio — and the count of three is a built-in
challenge beat.

## Lyrics as they will be sung

```
[intro]
Rent came out on Friday, so we're staying in,
One bottle of the cheap stuff, two mismatched cups.
You pulled the blinds down on the world outside,
Now it's just the fridge light and the two of us.

[verse]
Your socks keep sliding on the tile, you almost fall,
I'm laughing so hard I can barely stand.
The oven timer's ticking like a metronome,
So you set the bottle down and say, come here.
There's string lights on the cabinet we never took down,
There's steam rising off a pot we both forgot.
We can't afford the place with the candles and the view,
But look at what we've got, look at what we've got.

[pre-chorus]
Put your hand right here, your chin on my shoulder,
I'll count us in, one, two, three, here we go.
The whole world's out there and the rent is still due,
But in here it's slow, in here it's slow.

[chorus]
Turn the radio low, we don't need a floor,
Slow dance in the kitchen, that's what the kitchen's for.
Socks on the tile and the toast gone black,
Spinning by the sink, never going back.
We don't need a ballroom, don't need a band,
Just the hum of the fridge and your hand in my hand.
Turn the radio low, lock the front door,
Slow dance in the kitchen, that's what the kitchen's for.

[verse]
I know I promised you a night out somewhere nice,
White tablecloths and a waiter we could tip.
But the toast went black and you laughed till you cried,
Then you turned the music up and said, let's skip it.
The smoke alarm's got tape across its mouth,
The chair beside the window only stands on three.
I've got eleven dollars and a feeling in my chest,
And the feeling's worth more than anything to me.

[pre-chorus]
Put your hand right here, your chin on my shoulder,
I'll count us in, one, two, three, here we go.
The whole world's out there and the rent is still due,
But in here it's slow, in here it's slow.

[chorus]
Turn the radio low, we don't need a floor,
Slow dance in the kitchen, that's what the kitchen's for.
Socks on the tile and the toast gone black,
Spinning by the sink, never going back.
We don't need a ballroom, don't need a band,
Just the hum of the fridge and your hand in my hand.
Turn the radio low, lock the front door,
Slow dance in the kitchen, that's what the kitchen's for.

[instrumental]

[bridge]
I've been holding a sentence behind my teeth,
Since you burned the toast in the middle of the week.
I've been practising in the mirror down the hall,
Every morning, every evening, never said it at all.
So let's say it on the count, let's say it on three,
One, two, and you said it before me.
I love you, I love you, out loud by the stove,
And the timer went off like it already knows.

[chorus]
Turn the radio low, we don't need a floor,
Slow dance in the kitchen, that's what the kitchen's for.
Flour on your shirt and a ring pull for a ring,
Say it one more time, I'll say it back and sing.
We don't need a ballroom, don't need a band,
Just the hum of the fridge and your hand in my hand.
Turn the radio low, lock the front door,
Slow dance in the kitchen, that's what the kitchen's for.

[post-chorus]
That's what the kitchen's for,
Two left feet on a checkered floor.
That's what the kitchen's for,
Every night I'll ask you for one more.

[outro]
The bottle's empty and the song's nearly gone,
The string lights flicker but you keep on holding on.
One day we'll have the candles and the view,
But I'll take the kitchen if the kitchen comes with you.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2536 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
