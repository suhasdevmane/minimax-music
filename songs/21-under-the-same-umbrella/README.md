# Under the Same Umbrella

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-first song. **Female + male duet** — Mahima on the lead, Kai as the
stranger with the umbrella — Bollywood-pop fusion, a monsoon romance with
tabla, sitar-like plucks, cinematic strings and modern bass. 98 BPM, D
minor. Same singer as songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 633 sung words, every repeat written out |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock; a warm male tenor added as Singer B with a section-by-section duet structure. 98 BPM, D minor, tabla, sitar-style plucks, strings, the rain and bus-horn textures. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 68 entries — a single monsoon street, a two-lead character bible, the umbrella-in-every-frame rule, workflow, the umbrella-share challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 21-under-the-same-umbrella
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\21-under-the-same-umbrella\caption.txt `
  --lyrics-file songs\21-under-the-same-umbrella\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\21-under-the-same-umbrella\output\under_the_same_umbrella.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *which way* and *ask me at the corner* removed | Punctuation is not sung; the lines read the same as plain speech |
| The descriptive tag lines (*intro – rain, a pluck and piano*, *verse 1 – her*, *final chorus – highest, fullest*) reduced to plain tags | The model only knows plain section tags; the performance notes live in the caption |
| Both pre-choruses and all three choruses written out in full | The model sings the lyric body literally; a *(repeat)* line would be sung |
| Who sings what moved into the caption's `Duet Structure` line | The model has no per-line singer control; the split lives in the caption |
| **Craft pass:** the bridge's last line, *"And we're standing in the flood with nowhere left to go"* → *"...and I've never felt less alone"* | The bridge's second half ended two lines on the same word, *go*, which `LYRIC_CRAFT.md` forbids outright. *Alone* keeps the slant rhyme the song uses throughout and lands the bridge on the feeling rather than the geography |

Kept exactly as written: every lyric line, 98 BPM, D minor, the
instrumentation, the mood arc. No trimming was needed — 634 words fits.

## The story and the hooks

The sky opens over a market street and everyone runs. She's counting six
blocks to the bus stop when a stranger tilts a black umbrella over her. They
walk. His sleeve soaks on the uncovered side and he doesn't mind. The chai
wallah gives them two cups for the price of one. Her blue dupatta bleeds
onto his white shirt. She stops checking where the bus stop is; he starts
walking slower. Then the bus arrives, the door swings wide, the driver
leans on the horn, and neither of them moves. It pulls away with an empty
seat by the window, and they turn around and walk the wrong way back to
the chai stall. She never does tell him her name.

**The hook:** *"Under the same umbrella, we're the only ones dry"* — one
image, caption-ready, monsoon-season native.

**The line for captions:** *"Six blocks is a lifetime when you're waiting on
a bus."*

**The turn:** the bus door open, the horn, and *"Say the word and I'll stay
/ I don't know your name, but I know I don't want to go."*

**The quote:** *"I'm not going to the bus stop, I'm just going with you."*

**Why it can travel:** it's a first-meeting story with one prop, one
street and one decision, in a sound that sits between Bollywood strings and
a modern pop bass, and *let it pour* is a ready-made rain-video sound.

## Lyrics as they will be sung

```
[intro]
The sky cracked open right over the market,
Every rickshaw ran for the shade of a tree.
I was counting how far I would have to run,
When a stranger held a black umbrella over me.

[verse]
You said, which way, and I pointed anywhere,
The gutters running gold with the light from the signs.
Your left sleeve was soaking on the side that wasn't covered,
And you smiled like you didn't even mind.
Six blocks to the bus stop, one bus every hour,
The chai stall's got a tarp and a pot that never sleeps.
You asked me for my name, I said, ask me at the corner,
Some things go better slow when the whole street's running deep.

[pre-chorus]
Every step, the puddles clap under our feet,
Every step, your shoulder gets closer to mine.
Don't look at the sky, don't look at the time,
Just walk, just walk, just walk.

[chorus]
Under the same umbrella, we're the only ones dry,
Two strangers in a monsoon, let the whole town go by.
The rain's got the city, the city's got us,
Six blocks is a lifetime when you're waiting on a bus.
Under the same umbrella, count the corners, one, two,
I'm halfway to the bus stop, and I'm halfway to you.

[verse]
I only had the one umbrella, I was headed the other way,
But you looked like you'd run for it, and I couldn't watch that.
The chai wallah gave us two cups for the price of one,
Said the rain does this to strangers, and he tipped his cap.
Your dupatta's dripping blue all down my white shirt,
It's the best that shirt has ever looked, I swear.
Three blocks in, you've stopped checking where the bus stop is,
And I'm walking slower, like I don't want to get there.

[pre-chorus]
Every step, the puddles clap under our feet,
Every step, your shoulder gets closer to mine.
Don't look at the sky, don't look at the time,
Just walk, just walk, just walk.

[chorus]
Under the same umbrella, we're the only ones dry,
Two strangers in a monsoon, let the whole town go by.
The rain's got the city, the city's got us,
Six blocks is a lifetime when you're waiting on a bus.
Under the same umbrella, count the corners, one, two,
I'm halfway to the bus stop, and I'm halfway to you.

[instrumental]

[bridge]
There's the bus stop, there's the bus, there's the door swinging wide,
And the driver's on the horn like he's got somewhere to be.
You could keep the umbrella, I could walk home in the rain,
Or the next one's in an hour, and the chai is still on me.
Say the word and I'll stay, say the word and I'll stay,
I don't know your name, but I know I don't want to go.
So the bus pulls away with an empty seat by the window,
And we're standing in the flood, and I've never felt less alone.

[chorus]
Under the same umbrella, let the bus roll on by,
Two strangers in a monsoon, and neither says goodbye.
The rain's got the city, the city's got us,
Who needs a lifetime when you're missing every bus.
Under the same umbrella, count the corners, one, two,
I'm not going to the bus stop, I'm just going with you.

[post-chorus]
Let it pour, let it pour, we're not going anywhere,
Let it pour, let it pour, there's a whole night to spare.
Let it pour, let it pour, on the market, on the street,
The only ones dry from our heads to our feet.

[outro]
The sky's still open right over the market,
The rickshaws are still hiding under the tree.
I never did tell you my name at the corner,
You just kept the umbrella over me.
You just kept the umbrella over me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 634 → ~5.5 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2408 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
