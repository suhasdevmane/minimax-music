# Cheap Champagne

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty-eight. Female lead **Mahima**, indie-dance pop, 114 BPM, F major,
mid pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 632 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 114 BPM, F major, chorus-pedal guitar and live disco bass, foil cap and cork used as percussion, a gang vocal taking the final hook. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 69 entries — with a two-look character bible, the two friends, the repeated fire-escape framing across five seasons, the flash forward, workflow, the toast challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 114 BPM this sits in the ballad/mid class and the verify
script's 116 wpm default is the right guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 48-cheap-champagne
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\48-cheap-champagne\caption.txt `
  --lyrics-file songs\48-cheap-champagne\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\48-cheap-champagne\output\cheap_champagne.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads the body literally |
| Digits spelled as words (*seven dollars*, *two days*, *three flights*, *count to three*) | The model sings digits unpredictably |
| Descriptive tag lines (*[verse 1 — soft kick, shaker, three small wins]*) reduced to plain `[verse]` etc. | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses, pre-choruses and toasts written out in full instead of *(repeat)* | The model would sing the word |
| One line cut from the intro, one from the outro, and the middle toast removed | Word budget: the submission ran to 673 sung words, over the 640 cap for this pacing class |
| Performance notes (the silent beat before the cork, the mug clinks, the crowd answering the toast) moved into the caption | Stage directions in the lyric body get sung |

Kept exactly as written: the hook, both verses, the bridge turn, 114 BPM,
F major, the instrumentation and the mood arc.

## The story and the hooks

Three friends, one fire escape, one seven dollar bottle with a foil cap
bought from the corner store because the cold ones cost more. The rent went
through on Thursday with two days to spare. The friend in glasses got the
email he had stopped believing in and reads it out twice. And the third of
them walked in tonight looking like herself, which is a sentence that could
not have been said in March. So the twenty came out of the jar marked for
emergencies, because this is one. Verse two goes back to the same three metal
steps a year earlier, with a plastic bottle and a stack of unopened letters
and no announcement of anything: it just got a little lighter every couple of
months. The bridge looks forward to a room where the glasses match and
somebody else pours, and knows exactly what it will be thinking about. By the
last chorus every window in the building is lit and a neighbour two floors up
is raising a mug back.

**The hook:** *"Cheap champagne on the fire escape, tonight we're rich"* —
the title in the first line of the chorus, the contradiction that carries the
whole song.

**The line for captions:** *"To the small ones, to the small ones, here's to
every small one that we won."*

**The turn:** *"One day one of us will have the kind of job / Where the
glasses match and somebody else pours."*

**The knife line:** *"And the third of us walked in tonight looking like
herself, / Which is a sentence I could not have said in March."*

**Why it can travel:** everybody has a win nobody threw them a party for. The
toast is two lines long, needs no choreography and works with a mug, and the
seasonal fire-escape dissolve tells the entire story with no words at all.

## Lyrics as they will be sung

```
[intro]
Seven dollars at the corner store for something with a foil top,
You went out the window first and held the bottle while I climbed,
And the whole city just sat there like it was waiting for us.

[verse]
Rent went through on Thursday with two days left to spare,
First time in a year that the number didn't scare.
You got the email that you'd given up on getting,
Read it out to us twice, then you read it out again.
And the third of us walked in tonight looking like herself,
Which is a sentence I could not have said in March.
So I took the twenty from the jar that says emergencies,
And I have decided this is one.

[pre-chorus]
Out through the window, over the sill,
Two cups, no glasses, hold still.
The bottle's warm, the night is not,
Count to three and let it pop.

[chorus]
Cheap champagne on the fire escape, tonight we're rich,
Seven dollars at the corner store and not one thing to fix.
Three flights over a city that we're never gonna own,
But you can see the whole of it from here, so it's on loan.
Cheap champagne on the fire escape, tonight we're rich,
To the rent, to the job, to the one who made it through.
Warm and flat and perfect and I wouldn't switch,
Cheap champagne on the fire escape, tonight we're rich.

[post-chorus]
To the small ones, to the small ones,
Here's to every small one that we won.

[verse]
This time last September we were out here with nothing,
Passing round the cheapest thing and calling it a night.
You were pulling doubles and I had a stack of letters
That I hadn't opened since the middle of July.
Nobody announced it, nothing turned around at once,
It just got a little lighter every couple of months.
Same three people on the same three metal steps,
Same warm bottle and it tastes like something else.

[pre-chorus]
Out through the window, over the sill,
Two cups, then a third, hold still.
The bottle's warm, the night is not,
Count to three and let it pop.

[chorus]
Cheap champagne on the fire escape, tonight we're rich,
Seven dollars at the corner store and not one thing to fix.
Three flights over a city that we're never gonna own,
But you can see the whole of it from here, so it's on loan.
Cheap champagne on the fire escape, tonight we're rich,
To the rent, to the job, to the one who made it through.
Warm and flat and perfect and I wouldn't switch,
Cheap champagne on the fire escape, tonight we're rich.

[instrumental]

[bridge]
One day one of us will have the kind of job
Where the glasses match and somebody else pours.
I'll be standing in a room that cost a fortune
Thinking of a metal step and a seven dollar cork.
You don't get this twice, so raise it while it's cheap,
Drink it while it still means everything to me.

[chorus]
Cheap champagne on the fire escape, tonight we're rich,
Every window in the building lit and not one thing to fix.
Three flights over a city that we're never gonna own,
But you can see the whole of it from here, so it's on loan.
Cheap champagne on the fire escape, tonight we're rich,
To the year, to the three of us, to the ones who made it through.
Warm and flat and perfect and I wouldn't switch,
Cheap champagne on the fire escape, tonight we're rich.

[post-chorus]
To the small ones, to the small ones,
Here's to every small one that we won.

[outro]
Bottle's empty, city's loud, and nobody wants to go in,
When they ask me for the best night I have ever had,
I'll say a metal step, three cups, and cheap champagne.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 632 → ~5.4 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2077 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
