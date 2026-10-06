# Dating Myself

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-five. Female lead **Mahima**, contemporary R&B with neo-soul
warmth — silky electric piano, fretless bass, finger snaps and thick harmony
stacks. 94 BPM, C major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 621 sung words, ballad/mid pacing class, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 94 BPM, C major, electric piano, fretless bass, snaps, vibraphone on the last hook, and the restaurant-ambience ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 79 entries — built from the submission's scene direction, plus a three-look character bible, the empty-chair reverse-angle rule, a faceless lobby stranger, workflow, the solo-date challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 75-dating-myself
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\75-dating-myself\caption.txt `
  --lyrics-file songs\75-dating-myself\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\75-dating-myself\output\dating_myself.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Digits spelled as words (*four*, *two*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – electric piano, brushed rim, no drums]*, *[verse 1 – snaps, fretless bass, the pocket]*, *[final chorus – fullest harmonies]*) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the checkpoint's documented tags exist; anything else is dropped or sung |
| The repeated second chorus written out in full | `(repeat)` in the body would be sung as the word |
| All performance and arrangement direction moved into `caption.txt` | Stage directions in the lyric body get sung |

Kept exactly as written: every lyric line, 94 BPM, C major, the
instrumentation, the mood arc, the joke in verse two.

## The story and the hooks

She books a table under her own name on an ordinary Tuesday, puts the good
earrings in, and walks the long way there because she can. The waiter asks if
she is waiting for someone and she says no, go ahead. The phone goes
face-down in the bag and stays there — no proof required. Later there are
peonies on a Wednesday for no reason at all, moved two inches so they line up
with where she actually sits, and a matinee at four with both armrests to
herself. A kind man asks her out in the lobby and she tells him, truthfully,
that she is seeing someone. The bridge refuses the easy version of the
message: she would love a hand to hold, she is just not going hungry at a
table for two to prove she is not alone. Then two desserts, and home to a
lamp she left on for herself that morning.

**The hook:** *"I'm dating myself, and honestly it's going great"* — a bio, a
caption and a punchline that is also true.

**The line for captions:** *"Nobody's bad mood that I have to translate."*

**The knife line:** *"I said, I'm seeing someone, and I'm loyal, my friend."*

**The turn:** *"I'm not waiting to start, I already started, / and you'd be
joining something good, not fixing something poor."*

**Why it can travel:** the video shoots a solo date with the exact grammar of
a romance and puts the reverse angle on an empty chair, which is one
screenshot away from a meme that still respects the song. The bridge keeps it
out of anti-love territory, so it plays for people in relationships too.

## Lyrics as they will be sung

```
[intro]
Made the reservation under my own name,
Table for one, and the host didn't blink.
Gold earrings out for an ordinary Tuesday,
Walked the long way over just to think.
Nobody's evening to carry but my own,
Nobody waiting on me at the door.

[verse]
Ordered the one thing I'd never get for two,
Olives on the side and a small glass of red.
Waiter came around and asked me if I was waiting,
I said, no, I'm all here, go ahead.
Phone in my bag with the screen facing down,
No proof required and no one to impress.
Watched the whole room like the opening of a movie,
And I liked the girl who came in that dress.

[pre-chorus]
Used to think a Friday on my own was a loss,
Something you survive, something you hide.
Now I light the candle and I take my time,
And I don't leave until I decide.

[chorus]
I'm dating myself, and honestly it's going great,
She shows up on time and she never makes me wait.
Reservation for one, and I said it out loud,
Corner booth, candle lit, and I'm proud.
I'm dating myself, no notes and no complaints,
Nobody's bad mood that I have to translate.
Ordered the dessert and I finished the plate,
I'm dating myself, and honestly it's going great.

[verse]
Peonies on a Wednesday, no occasion,
Paid the full price and I carried them home.
Put them where the sofa sees them in the morning,
Not the hall where they'd be blooming for someone unknown.
Matinee at four, back row, lights low,
Both of the armrests mine and I cried at the end.
Somebody kind asked me out in the lobby,
I said, I'm seeing someone, and I'm loyal, my friend.

[pre-chorus]
Used to call it lonely when the place went quiet,
Used to fill it up with anyone I could find.
Now the quiet is the part I look forward to,
And I don't rush a single thing that's mine.

[chorus]
I'm dating myself, and honestly it's going great,
She shows up on time and she never makes me wait.
Reservation for one, and I said it out loud,
Corner booth, candle lit, and I'm proud.
I'm dating myself, no notes and no complaints,
Nobody's bad mood that I have to translate.
Ordered the dessert and I finished the plate,
I'm dating myself, and honestly it's going great.

[instrumental]

[bridge]
This is not a speech about not needing nobody,
I would love a hand to hold when the winter comes.
But I'm not going hungry at a table for two
Just to say that I wasn't the only one.
So whoever you are, you can take your sweet time,
I'm not standing at the window keeping score.
I'm not waiting to start, I already started,
And you'd be joining something good, not fixing something poor.

[chorus]
I'm dating myself, and honestly it's going great,
She shows up on time and she's never running late.
Reservation for one, and I said it out loud,
Corner booth, candle lit, and I'm proud.
I'm dating myself and I'm easy to date,
Nobody's silence that I have to translate.
Ordered two desserts and I finished them straight,
I'm dating myself, and honestly it's going great.

[post-chorus]
Going great, going great,
Table for one and I'm never running late.
Going great, going great,
Flowers on a Wednesday and nothing to celebrate.
Going great, going great,
Nobody to answer to and nobody to wait.
Going great, going great,
I'm dating myself and it's going great.

[outro]
Walked home slow with the peonies wrapped in paper,
Keys in the door and the lamp already on.
Poured one glass and I put on a record,
And I stayed up late with the best company I've known.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 621 at 116 wpm → ~5.4 min, 89% of frame cap |
| Caption + lyrics tokens | 2009 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
