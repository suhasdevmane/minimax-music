# Butterflies Don't Lie

**Status: written and verified, NOT rendered. Not yet in the queue.**

Fifteenth song. Female lead **Mahima**, bubbly synth-pop, 122 BPM, C major,
US register. Uptempo. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 743 sung words, uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 122 BPM, C major, plucky arpeggio signature, four-on-the-floor choruses, café ambience and a low watch-buzz tick as ear candy. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo song, see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 81 entries — with a two-look character bible, three named friends, Kai held back until verse two, the body-truth cutting rule, the composited-UI note, workflow, the heart-rate challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 15-butterflies-dont-lie
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\15-butterflies-dont-lie\caption.txt `
  --lyrics-file songs\15-butterflies-dont-lie\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\15-butterflies-dont-lie\output\butterflies_dont_lie.wav
```

Expected ~2 h.

## Pacing: uptempo, and the length is an estimate

This is a 122 BPM synth-pop record, not a ballad. Every measured song in the
catalogue so far paced between 116 and 153 words per minute, all of them at
84–98 BPM. At 122 BPM over a four-on-the-floor the vocal will pace faster,
but by how much is a guess until it renders. The lyrics are **743 words**.
What that means against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| 130 wpm | 5.7 min | 95% |
| **140 wpm (the guard setting)** | 5.3 min | 88% |
| 155 wpm | 4.8 min | 80% |

The short-lined chorus and the two chant post-choruses will run well above
the average; the talky verses will run below it. A blended estimate of
140–150 wpm lands between 5.0 and 5.3 minutes. The guard in `render.json` is
set at a conservative 140. **If the first render truncates the outro, drop
the second post-chorus (twenty-eight words, a near-exact repeat) and
re-render.** The measured pacing goes into `docs/VOICE_RECIPE.md` either way.

## What changed from the submission

| Change | Why |
|---|---|
| Digits spelled out throughout — *three iced coffees*, *fourteen good excuses*, *forty minutes*, *two letters*, *the fourth of March* | The model sings digits unpredictably |
| Quotation marks and em-dashes removed from the sung lines | Punctuation is not sung; the model sings the lyric body literally |
| Descriptive tag lines (*intro – plucky arpeggio*, *bridge – electric piano, shaker, no drums*) reduced to plain `[intro]`, `[bridge]` and so on; all performance direction moved into the caption | Only the checkpoint's documented tags exist, and anything left in the body gets sung |
| The repeated chorus, both chant sections and the bookend outro written out in full instead of marked as repeats | The verify script flags parentheses-only lines and the model would sing them |
| The chant placed as a `[post-chorus]` after chorus one as well as after the final chorus | The uptempo word budget is met by adding sections, not by inflating verses |

Kept exactly as written: every image, 122 BPM, C major, the arpeggio-led
production list, the one cool-graded sequence, the sunflower beat and the six
viral moments.

## The story and the hooks

She has told the table it is nothing. Four times. Meanwhile her smartwatch is
reporting a high heart rate while she is sitting still, her ears have gone
pink, her fingers have shredded a napkin into a pile without her noticing,
and somebody has kept a screenshot from June and is reading it back to her in
her own voice. On Tuesday she spent forty minutes on a two-letter message. On
Thursday he was early on a cold corner with two coffees and her order right.
Then she stops arguing, says it out loud at the same table, and the ceiling
declines to fall in.

**The hook:** *"My mouth says maybe, but butterflies don't lie."*

**The line for captions:** *"I get one vote in this body and I lose it every
time."*

**The chant:** *"Don't lie, don't lie, they never learned how."*

**The turn:** *"I said it out loud in a room full of people, and the ceiling
didn't fall out of the sky."*

**Why it can travel:** it is the funniest and most universal part of a crush
— the body telling on you in front of your friends — written as a real pop
song rather than a joke, with a chorus built to be shouted across a table and
a smartwatch screenshot as a ready-made challenge.

## Lyrics as they will be sung

```
[intro]
Table for four on a Saturday, sun through the glass,
I said his name like it was nothing and the whole table laughed.
Three iced coffees and a plate we're all pretending to share,
And I'm suddenly the only one who's going pink in here.

[verse]
I said it's nothing, honestly, we're only talking a bit,
He texted twice this morning and I haven't answered it.
Then somebody says his name a second time out loud,
And the sunflower on the table turns around to look at me.
My watch buzzes, tells me that my heart rate's high for sitting,
The waiter asks if I'm alright and I say I'm doing fine.
The group chat has the receipts and the receipts run long,
Somebody kept a screenshot of the things I said in June,
And they read the whole thing back to me in my own voice.

[pre-chorus]
I can talk my way around it, I can argue it to death,
I had fourteen good excuses and I'm somewhere down to nine.
But my hands are on the table doing something on their own,
And nobody has to ask me, they can watch me lose the line.

[chorus]
My mouth says maybe,
But butterflies don't lie.
I can hold it together in a room full of people,
I just can't hold it together on the inside.
Ask the goosebumps, ask the shaking in my knee,
Ask whoever's running things down there instead of me.
I get one vote in this body and I lose it every time.
My mouth says maybe,
But butterflies don't lie.

[post-chorus]
Don't lie, don't lie, they never learned how,
Don't lie, don't lie, and they're telling on me now.
Don't lie, don't lie, they never learned how,
My mouth says maybe but the butterflies are loud.

[verse]
Tuesday, he asks if I'm free and I typed out a no,
Sat and read it for a minute and I let it go.
Deleted every letter, wrote a yes with a little too much,
Took the mark off, put it back, then took it off again.
Forty minutes on a message that was two letters long.
Thursday he was early, on the corner in the cold,
Two coffees and my order right and I had never told him.
I had a whole speech ready about keeping this thing light,
Then my body walked me over there before I said a word.

[pre-chorus]
I could talk my way around it, I could argue it all week,
I had fourteen good excuses and I'm down to about two.
But my face went and answered while my mouth was still deciding,
And the girls don't say a word, they let me dig myself through.

[chorus]
My mouth says maybe,
But butterflies don't lie.
I can hold it together in a room full of people,
I just can't hold it together on the inside.
Ask the goosebumps, ask the shaking in my knee,
Ask whoever's running things down there instead of me.
I get one vote in this body and I lose it every time.
My mouth says maybe,
But butterflies don't lie.

[instrumental]

[bridge]
Fine. Fine. You want it slow and out loud,
I like him. I like him. I have liked him since the fourth of March.
I like the way he listens with his whole entire face,
I like that he remembered something I said and didn't mean,
I like that he is not smooth about it, not at all.
So take the plate away, I'm not eating anything,
I have got a stomach full of something with a mind of its own.

[chorus]
My mouth says maybe,
But butterflies don't lie.
I said it out loud in a room full of people,
And the ceiling didn't fall out of the sky.
Ask the goosebumps, ask the shaking in my knee,
Ask whoever's running things down there instead of me.
I got one vote in this body and I finally let it go.
My mouth said maybe,
But the butterflies were right.

[post-chorus]
Don't lie, don't lie, they never learned how,
Don't lie, don't lie, and they're telling on me now.
Don't lie, don't lie, they never learned how,
My mouth said maybe but the butterflies were loud.

[outro]
Table for four on a Saturday, sun through the glass,
I said his name like it was something and the whole table clapped.
Same iced coffee, same plate that we never share,
And I'm the only one still smiling like an idiot in here.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 743 at 140 wpm → ~5.3 min, 88% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2234 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
