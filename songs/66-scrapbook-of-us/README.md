# Scrapbook of Us

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixty-sixth song. Female lead **Mahima**, cinematic piano pop, US register,
86 BPM, A major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, ballad class |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 86 BPM, A major, close-mic'd felt upright piano, upright bass, brushed kit, a full string section, no guitars and no synthesisers anywhere. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a four-look character bible, Kai as the partner, the locked-off overhead book device, the composited-handwriting rule, workflow, the page-one challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 66-scrapbook-of-us
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\66-scrapbook-of-us\caption.txt `
  --lyrics-file songs\66-scrapbook-of-us\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\66-scrapbook-of-us\output\scrapbook_of_us.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads em-dashes unpredictably |
| Every number spelled as a word — *nine tea lights*, *page one*, *at three*, *eleven years*, *a hundred times* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro — felt piano, room tone, no drums]`, `[verse 1]`, `[final chorus]`) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the documented plain tags exist; anything else is dropped or sung |
| Every repeated chorus written out in full rather than marked as a repeat | A repeat marker would be sung as a lyric |
| Performance directions (the drumless intro, the two lines of piano and voice in verse two, the half-time bridge, the pedal noise left in the mix) moved into `caption.txt` | The model sings the lyric body literally |
| Seventeen lines tightened by one or two words each | The submission came in at 665 words, well over the ballad cap; the trims are spread across the intro, both verses, both pre-choruses, the repeated chorus lines, the bridge and the outro, and change no image and no rhyme |

Kept exactly as written: every lyric line's content, 86 BPM, A major, the
instrumentation, the page-per-line video concept and the mood arc.

## The story and the hooks

Eleven years in, she hands him a book she made by hand and has been hiding
since February. Page one is a bar napkin with his number written upside down
in a pen that hardly worked. Page two is a diner receipt from three in the
morning with the total circled and the date beside it, because she already
knew she would want the proof. The pre-choruses admit the method: he never saw
her keep any of it, because he was looking at her. Then the hard pages — a
hospital wristband with his name typed wrong, a folded note glued at one edge
with the thing she would have said if he had stayed, a lease, a paint swatch,
and a year that is mostly blank and does not need explaining. The bridge is
the turn: the last page is empty on purpose, there is a line of dried glue and
a space for a date, and she is not asking a question. The last thing that
happens is that she gives him the pen.

**The hook:** *"Every page in the scrapbook of us, I'd live again."*

**The line for captions:** *"A box you never empty is a love song."*

**The turn:** *"The last page is empty and I left it that way / A line of
dried glue and a space for a date."*

**The quote:** *"I'm telling you I'm nowhere near done, and I'll wait."*

**Why it can travel:** anniversaries are a recurring, dateable occasion and
there is very little written for the eleventh one. The song is about a
physical object anybody can hold up, the video device is one locked-off
overhead of a book turning a page per line, and the invitation — show the
oldest piece of paper you kept from somebody — needs no production at all.

## Lyrics as they will be sung

```
[intro]
Glue on my fingers, a shoebox on the floor,
Nine tea lights and a table set for two.
I have been hiding this since February,
And tonight I'm handing it to you.

[verse]
Page one is a napkin from a bar on Delancey,
Your number in a pen that hardly worked at all.
You wrote it upside down so I'd have to turn it,
And I've turned it over ever since that fall.
Page two is a receipt from a diner at three,
Two coffees and a plate of fries we didn't share.
I circled the total and wrote the date beside it,
Because I knew already I'd want the proof somewhere.

[pre-chorus]
You never saw me keep them, you were watching me,
A ticket in my pocket, a stub up my sleeve.
Eleven years of small and careful stealing,
From every single room that we would leave.

[chorus]
Every page in the scrapbook of us, I'd live again,
Soft ones, sharp ones, and the ones that left a stain.
A napkin, a wristband, a flower pressed to dust,
A ticket to a movie we walked out of, and us.
I never called it saving, I just never threw it out,
And a box you never empty is a love song.
Take your time, there's a page for every when,
Every page in the scrapbook of us, I'd live again.

[verse]
Page nine is a wristband from a hospital in April,
Your name typed wrong, and I never got it changed.
Page ten is only a folded piece of paper,
With the thing I would have said if you had stayed.
Page eleven is a lease with both our names,
Page twelve is mostly empty, and we know why.
A swatch of the wall we painted twice,
And a note that I have read a hundred times.

[pre-chorus]
I didn't keep the bad ones to make a point,
I kept them because they belong to us the same.
Eleven years of getting half of it right,
And I wouldn't give a single Tuesday away.

[chorus]
Every page in the scrapbook of us, I'd live again,
Soft ones, sharp ones, and the ones that left a stain.
A napkin, a wristband, a flower pressed to dust,
A ticket to a movie we walked out of, and us.
I never called it saving, I just never threw it out,
And a box you never empty is a love song.
Take your time, there's a page for every when,
Every page in the scrapbook of us, I'd live again.

[instrumental]

[bridge]
The last page is empty and I left it that way,
A line of dried glue and a space for a date.
There's no question in this, there's nothing to say,
I'm telling you I'm nowhere near done, and I'll wait.
Keep your thumb in the gap and hold our place,
And we'll fill it the slow way, at the pace we make.

[chorus]
Every page in the scrapbook of us, I'd live again,
Soft ones, sharp ones, and the ones that left a stain.
A napkin, a wristband, a flower pressed to dust,
A ticket to a movie we walked out of, and us.
You're holding eleven years in the palm of one hand,
And the box is only half full, which was more or less the plan.
Take your time and turn them, then hand me back the pen,
Every page in the scrapbook of us, I'd live again.

[post-chorus]
I'd live it again, I'd live it again,
Every wrong turn, every long way round.
I'd live it again, I'd live it again,
Turn the page, I'm not putting it down.

[outro]
Glue on your fingers now, the shoebox on the floor,
The candles are down to nothing, the tea's gone cold.
You've got one page left and a pen in your hand,
And I'm not saying anything. Go on. Write.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2136 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
