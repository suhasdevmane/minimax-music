# Your Name in Cursive

**Status: written and verified, NOT rendered. Not yet in the queue.**

Fourteenth song. Female lead **Mahima**, cinematic pop with a soft trap
underpinning, romance, US register. 92 BPM, F minor lifting to A♭ major on
the final chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission cleaned for the engine and revised at two points (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 92 BPM, F minor lifting to A♭, felt piano, strings, trap hats, and the pen-on-paper and page-turn ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 79 entries — built from the submission's scene direction, plus a three-look character bible, Kai faceless until the library, the never-legible-handwriting rule, workflow, the surface challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json` — 92 BPM is a ballad and the 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 14-your-name-in-cursive
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\14-your-name-in-cursive\caption.txt `
  --lyrics-file songs\14-your-name-in-cursive\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\14-your-name-in-cursive\output\your_name_in_cursive.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech in both pre-choruses and the library scene | Punctuation is not sung, and quotes in the body confuse the phrasing |
| Descriptive tag lines reduced to plain tags; `[final chorus]` → `[chorus]`; every repeated chorus written out in full | Only the checkpoint's documented tags exist, and the model would sing the word repeat |
| `[verse 2]` lines three to eight rewritten | Craft pass: the second half of verse two had four orphan lines — *liar*, *red*, *December* and *off* rhymed with nothing, while verse one is cleanly ABCB / DEDE throughout. The rewrite keeps every image (the library, the red ears, the fog, the frost, the wrist) and restores the scheme: *page / shape / liar / escape*, then *name / light / same / right*. The ink on her wrist is now blue, which ties it back to the blue pen in the intro. |
| The bridge's last two lines rewritten | Craft pass: *"I'm gonna say it like everybody knows"* paraphrased the hook one line before the hook lands, which flattens it. Replaced with *"You're standing right here and the room's gone still, / And if I don't do it now, then I never will"* — the same launch, no pre-echo, and the rhyme scheme stays in couplets |

Kept exactly as written: the intro, verse one, both pre-choruses, all four
choruses, the post-chorus, the outro, 92 BPM, F minor with the lift to A♭,
the instrumentation and the mood arc. 618 words became 624, still inside the
ballad budget.

## The story and the hooks

She has been writing his name since the first week of September and never
once said it. It goes in the margin where the notes should be, into the
steam on a bathroom mirror, onto the back of a café receipt folded into a
coat pocket, into wet sand for the tide to take, and eventually onto the
inside of her own wrist in blue ink she keeps redrawing. Her friends tell
her it is not that deep. It is the deepest thing she knows how to keep. He
catches her at it in a library, calls her a terrible liar, and goes red
himself, which she does not notice. Then she finds his notebook open on a
table by a door, and her own name is looping down every page in a hand that
is not hers. So she puts the pen down and speaks.

**The hook:** *"I wrote your name in cursive, now I'm saying it out loud"* —
the title sits in the first two lines of the chorus and again in the last
two, and the whole song is the distance between the two halves of it.

**The line for captions:** *"But my face has never been the honest place."*

**The turn:** the bridge. *"Little loops in the margin in a hand that wasn't
mine, / Mine, in cursive, over and over, every page, every line."* It was
mutual the entire time and both of them were writing instead of speaking.

**The quote:** *"I've been carrying you round like a word I can't say
right."*

**Why it can travel:** the handwriting motif is free to reproduce — steam,
frost, sand, a receipt, a wrist, anybody's phone — and the emotion is the
most common one there is: knowing and not saying. The final chorus changes
one line to *"say it back to me now"*, which gives the video its single
screenshot.

## Lyrics as they will be sung

```
[intro]
First week of September, back row, blue pen,
I wrote it once and then I wrote it again.
Little loops in the margin where the notes should be,
A secret in my handwriting that only I could read.

[verse]
I wrote it in the steam on the bathroom glass,
Watched it run before the mirror went clear.
I wrote it on the back of a café receipt,
Folded it in my coat pocket like it was worth something here.
I dragged it in the sand with the side of my shoe,
Let the tide come and take it, cause the tide doesn't tell.
Every notebook I own has a page that's just you,
I've been spelling out the thing that I can't say too well.

[pre-chorus]
And my friends all say, just tell him, it's not that deep,
But it's the deepest thing I know how to keep.
I've got a thousand little versions in a thousand little lines,
And not one of them has ever left this mouth of mine.

[chorus]
I wrote your name in cursive,
Now I'm saying it out loud.
Every loop, every letter,
I'm not hiding it now.
I wrote it small, I wrote it soft,
I wrote it where nobody looks,
But you're not a secret anymore,
You're the title of my book.
I wrote your name in cursive,
Now I'm saying it out loud.

[verse]
You caught me in the library, my hand across the page,
Asked me what I was drawing, I said, nothing, just a shape.
You laughed and said, you're a terrible liar,
Then your ears went red and you looked for an escape.
Now it's fog on the bus window, one finger, one name,
In the frost on the car in the cold morning light,
On the inside of my wrist in a blue that stays the same,
I've been carrying you round like a word I can't say right.

[pre-chorus]
And my friends all say, girl, he can see it on your face,
But my face has never been the honest place.
It's my hands that give me up, it's my hands that know,
And my hands have been saying it for months now, so.

[chorus]
I wrote your name in cursive,
Now I'm saying it out loud.
Every loop, every letter,
I'm not hiding it now.
I wrote it small, I wrote it soft,
I wrote it where nobody looks,
But you're not a secret anymore,
You're the title of my book.
I wrote your name in cursive,
Now I'm saying it out loud.

[instrumental]

[bridge]
You left your notebook open on the table by the door,
I wasn't gonna look, but I looked, and there was more.
Little loops in the margin in a hand that wasn't mine,
Mine, in cursive, over and over, every page, every line.
So I'm done with the pen, I'm done with the glass,
I'm done writing down a thing that I could just ask.
You're standing right here and the room's gone still,
And if I don't do it now, then I never will.

[chorus]
I wrote your name in cursive,
Now I'm saying it out loud.
Every loop, every letter,
Say it back to me now.
I wrote it small, I wrote it soft,
I wrote it where nobody looks,
But you're not a secret anymore,
You're the title of my book.
I wrote your name in cursive,
Now I'm saying it out loud.

[post-chorus]
Out loud, out loud,
No more margins, no more doubt.
Out loud, out loud,
Your name, out loud.

[outro]
First week of September, back row, blue pen,
I wrote it once and then I wrote it again.
Now it's written on my face where the whole world can see,
And you're writing mine in cursive right next to me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 624 → ~5.4 min at 116 wpm, 90% of frame cap |
| Caption + lyrics tokens | 2117 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
