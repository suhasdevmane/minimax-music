# Photo Booth Strip

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixty-third song. Female lead **Mahima**, jangly indie pop, US register,
108 BPM, E major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words, mid class |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 108 BPM, E major, two interlocking clean guitars, tambourine shuffle, electric piano only in the bridge, no strings anywhere. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look character bible, Kai in the booth, a faceless mall guard, the composited-strip rule, workflow, the frame-four challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 63-photo-booth-strip
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\63-photo-booth-strip\caption.txt `
  --lyrics-file songs\63-photo-booth-strip\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\63-photo-booth-strip\output\photo_booth_strip.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads em-dashes unpredictably |
| Every number spelled as a word — *two dollars*, *frame one*, *four little squares*, *four inches* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro — mall room tone, one guitar, no drums]`, `[verse 1]`, `[final chorus]`) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the documented plain tags exist; anything else is dropped or sung |
| Every repeated chorus written out in full rather than marked as a repeat | A repeat marker would be sung as a lyric |
| Performance directions (the drumless intro, the half-feel bridge, the flash stab on the word flash, the beat of silence under the blur) moved into `caption.txt` | The model sings the lyric body literally |
| Four lines tightened by one word each | The submission came in at 649 words, over the ballad cap; the trims are in three chorus lines and the first line of the bridge and change no image |

Kept exactly as written: every other lyric line, 108 BPM, E major, the
instrumentation, the four-frame video concept and the mood arc.

## The story and the hooks

Two dollars in quarters, fifteen minutes before a mall closes, and a red
curtain. Frame one is her being photographed properly. Frame two is his two
fingers turning her chin. Frame three is a joke about a sandwich and her
laughing with her eyes gone. Frame four is a blur, because he turned to say
something and the flash caught the motion and none of the sound, and she still
does not know how that sentence ended. They tear the strip in half at the top
of a stopped escalator and he takes the frames where she looks good. Years
later she finds her half in a coat pocket in November with a receipt, and the
turn is that the ruined frame is the one she keeps: they were both already
moving when it went off, and that is the truest thing on the paper. The mall
is a parking structure now. The strip is not on the fridge and not in a frame.
It is in a coat, on purpose.

**The hook:** *"Four frames, one night, photo booth strip of my life."*

**The line for captions:** *"Cut it down the middle, you still can't tell us
apart."*

**The turn:** *"We were both already moving when the last flash went / And I'd
rather have a blur than a night I never spent."*

**The chant:** *"A smile, a kiss, a laugh, a blur."*

**Why it can travel:** the four-frame strip is a universal object with a
built-in structure, and the post-chorus is written to be cut one word per
frame. The invitation — caption the fourth frame, the bad one, with what was
really happening — is a format anybody with an old strip can run.

## Lyrics as they will be sung

```
[intro]
Curtain the color of a cheap red wine,
Two dollars in quarters and a boy with a plan.
The mall is closing, the escalator's stopped,
And we're the only ones still standing where we stand.

[verse]
Frame one, I'm looking at the lens like I'm supposed to,
Hair behind my ear and my hands in my lap.
You're half a second late and your eyes are on me,
So the first of the four is already a trap.
Frame two, you turn my face with two fingers,
And the flash catches the second I say okay.
Somebody's mom is waiting on the bench outside,
And I forget my own name in the easiest way.

[pre-chorus]
The machine counts down in a voice like a school bell,
Four little squares and no way to choose.
No take it again, no do it better,
Just whatever we were, and then the proof.

[chorus]
Four frames, one night, photo booth strip of my life,
A smile, a kiss, a laugh and a blur on the right.
Two dollars, a curtain, and a flash in the dark,
Cut it down the middle, you still can't tell us apart.
Everybody gets a wall, a shoebox, a shelf,
I got four inches of paper that I keep to myself.
In a wallet, in a coat pocket, out of the light,
Four frames, one night, photo booth strip of my life.

[verse]
Frame three, you say the thing about the sandwich,
And I'm laughing with my whole face, eyes gone.
Frame four is a blur, you turn to tell me something,
And the flash gets the motion and none of the sound.
I still don't know the end of that sentence,
The mall guy kills the lights and rolls the gate.
We tear it down the middle on the escalator,
And you get the frames where I look great.

[pre-chorus]
The machine counts down in a voice like a school bell,
Four little squares and no way to choose.
Nobody tells you when you're in the last one,
You find that out later, and it lands like news.

[chorus]
Four frames, one night, photo booth strip of my life,
A smile, a kiss, a laugh and a blur on the right.
Two dollars, a curtain, and a flash in the dark,
Cut it down the middle, you still can't tell us apart.
Everybody gets a wall, a shoebox, a shelf,
I got four inches of paper that I keep to myself.
In a wallet, in a coat pocket, out of the light,
Four frames, one night, photo booth strip of my life.

[instrumental]

[bridge]
Found it in a coat in November with a receipt,
Half a strip, three good frames and one that came out wrong.
Everybody wants the kiss, everybody wants the laugh,
But the wrong one is the one I've kept this long.
We were both already moving when the last flash went,
And I'd rather have a blur than a night I never spent.

[chorus]
Four frames, one night, photo booth strip of my life,
A smile, a kiss, a laugh and a blur on the right.
Two dollars, a curtain, and a flash in the dark,
Cut it down the middle, you still can't tell us apart.
Everybody gets a wall, a shoebox, a shelf,
I got four inches of paper that I keep to myself.
Not on the fridge, not in a frame, just out of sight,
Four frames, one night, photo booth strip of my life.

[post-chorus]
A smile, a kiss, a laugh, a blur,
A smile, a kiss, a laugh, a blur.
Four frames, one night,
A smile, a kiss, a laugh, a blur.

[outro]
The mall came down the summer after,
There's a parking structure where the booth used to stand.
I've still got four inches of a Tuesday,
And a laugh with my eyes gone and your hand.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2078 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
