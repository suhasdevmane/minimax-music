# Airplane Mode

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixteenth song. Female lead **Mahima**, chill pop with lo-fi drums, 98 BPM,
G minor, US register. Ballad/mid pacing, no `render.json`. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 637 sung words, ballad budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 98 BPM, G minor, clean guitar harmonics as the signature line, warm analogue pads, and road noise, water, wind and a very low kettle as ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look character bible, Kai as the male lead, no third character at all, the fixed table angle as the spine of the film, the composited-UI note, workflow, the airplane-mode challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 16-airplane-mode
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\16-airplane-mode\caption.txt `
  --lyrics-file songs\16-airplane-mode\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\16-airplane-mode\output\airplane_mode.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Digits spelled out throughout — *two hours*, *two cards*, *two whole days*, *a hundred things*, *three at once* | The model sings digits unpredictably |
| Quotation marks and em-dashes removed from the sung lines | Punctuation is not sung; the model sings the lyric body literally |
| Descriptive tag lines (*intro – guitar harmonics over road noise*, *bridge – no drums*) reduced to plain `[intro]`, `[bridge]` and so on; all performance direction moved into the caption | Only the checkpoint’s documented tags exist, and anything left in the body gets sung |
| The two repeated choruses written out in full instead of marked as repeats | The verify script flags parentheses-only lines and the model would sing them |
| No `render.json` | At 98 BPM this is a ballad/mid song; the verify script’s 116 wpm default is the right guard |

Kept exactly as written: every image, 98 BPM, G minor, the instrumentation
list, the mood arc, the fixed table shot and the six viral moments. No
trimming was needed — 637 words fits the ballad budget with room.

## The story and the hooks

They drive until the bars drop off one at a time and the map goes blank, find
the key under a rock, and put both phones flat on the cabin table where they
stay for two days. The kettle is older than either of them. The deck of cards
is missing two, so they draw replacements. On the second afternoon he asks
her something small she has been avoiding for a year, and she answers it out
loud because there is nowhere else to look. There is a signal up on the ridge
and they decide not to walk up to it. On the way home the bars come back like
weather, and he slides her phone under the seat.

**The hook:** *"Put the world on airplane mode, it’s just you and me
tonight."*

**The line for captions:** *"Turns out I was never tired, I was only being
reached."*

**The turn:** *"So the ridge can keep its one bar and the week can hold its
breath."*

**The last gesture:** *"You reached over and you slid my phone beneath the
seat, and said not yet, and I said not yet, and we drove on."*

**Why it can travel:** the phone-off weekend is the most wanted and least
taken thing in modern life, the hook is already a phone setting everyone
recognises, and the video’s whole concept is one repeatable image — two
phones flat on a table — that anybody can post.

## Lyrics as they will be sung

```
[intro]
Two hours out of the city and the bars start dropping,
One, then none, and the little map goes plain.
You said we could turn back, I said keep driving,
And the radio gave up somewhere past the county line.

[verse]
The key was under a rock exactly where they said it was,
The kettle's older than the both of us and whistles like a train.
There's a drawer of someone's postcards and a deck with two cards missing,
And a window with nothing in it but the water and the pines.
You put your phone down on the table, screen flat, and slid it over,
I put mine beside it and we never said a word.
Two whole days and nobody needs us, nobody knows,
And the quiet came in through the screen door like a guest.

[pre-chorus]
There's a whole week in my shoulders that I'm setting on the floor,
There's a hundred things unanswered and they'll all still be there.
Let them wait, let them wonder where I've gone,
I have got somewhere better to be and it is right here.

[chorus]
Put the world on airplane mode,
It's just you and me tonight.
No little lights, no half a conversation,
Nobody pulling on my sleeve to be somewhere else.
Let the sky keep whatever it was going to say,
I am not taking anything today.
Put the world on airplane mode,
It's just you and me tonight.

[verse]
Saturday the lake was cold enough to make me shout,
You went in like a lunatic and stayed in twice as long.
We played that broken deck all afternoon and made the missing up,
You cheated, badly, and I let you have it anyway.
Then you asked me something small that I had spent a year avoiding,
And I answered it out loud because there was nowhere else to look.
Turns out I have plenty to say when nothing interrupts,
Turns out I was never tired, I was only being reached.

[pre-chorus]
There's a whole year in my jaw that I am putting down as well,
There's a version of me answering at midnight in my head.
She can wait, she can sit outside the door,
I'm not letting her back in until the drive home instead.

[chorus]
Put the world on airplane mode,
It's just you and me tonight.
No little lights, no half a conversation,
Nobody pulling on my sleeve to be somewhere else.
Let the sky keep whatever it was going to say,
I am not taking anything today.
Put the world on airplane mode,
It's just you and me tonight.

[instrumental]

[bridge]
Monday's coming for us both with all its little teeth,
There's a signal on the ridge if we walk up and let it in.
But the fire's going and the kettle's going and you're reading me the postcards
From people we will never meet, from summers we were not in.
So the ridge can keep its one bar and the week can hold its breath,
I'll take the last of the quiet and I'll take it here with you.

[chorus]
Put the world on airplane mode,
It's just you and me tonight.
No little lights, no half a conversation,
Nobody pulling on my sleeve to be somewhere else.
Let the sky keep whatever it was going to say,
I'll pick it up on Monday, not today.
Put the world on airplane mode,
It's just you and me tonight.

[post-chorus]
Airplane mode, airplane mode,
Nothing coming in and nothing going out.
Airplane mode, airplane mode,
Just the water and the woodsmoke and your mouth.

[outro]
We drove back down on Sunday and the bars came back like weather,
Three at once, then a hundred, then a hum.
You reached over and you slid my phone beneath the seat,
And said not yet, and I said not yet, and we drove on.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2039 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
