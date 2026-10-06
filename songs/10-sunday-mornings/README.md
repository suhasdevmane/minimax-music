# Sunday Mornings

**Status: written and verified, NOT rendered. Not yet in the queue.**

Tenth song. Female lead **Mahima**, warm indie-pop / sunlit bedroom pop with
jangly guitar, soft claps and mellotron, 100 BPM, D major. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 100 BPM, D major, jangly guitar, soft claps, mellotron flute and strings, birdsong and a mug set down on wood as the ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 67 entries — built from the submission's scene direction, plus a three-look character bible, Kai as the boyfriend with a face, the window-as-clock rule, the accumulating-objects rule, workflow, Sunday-count challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 10-sunday-mornings
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\10-sunday-mornings\caption.txt `
  --lyrics-file songs\10-sunday-mornings\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\10-sunday-mornings\output\sunday_mornings.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"okay, I could get used to this"*, *"I could stand here all my life"*, *"that's you"*, *"go back to sleep"* and *"I know, I've known for weeks"* removed | Punctuation is not sung; commas carry the same pause |
| Sunday numbers kept as words (*Sunday number six*, *twenty*, *fifty*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – hushed, one guitar…]*, *[final chorus – full width…]*) reduced to plain tags | The model only knows the plain section tags |
| Both pre-choruses and all three choruses written out in full | The model sings whatever is in the body; a *(repeat)* line would be sung |
| **Craft pass:** the second half of each verse re-rhymed — *"and you didn't have to ask"* → *"and you never asked me twice"*, and verse 2's *"either one of us can name / the plant's got a name / stopped counting anything"* → *"we have seen before / kept alive two years / I don't count it anymore"* | Both verses open in a strict ballad stanza (lines two and four rhyme) and then dropped it; verse 2 also ended two consecutive lines on the word *name*, which `LYRIC_CRAFT.md` forbids outright. Every image is kept, and the new verse-2 close pays off the intro's ceiling cracks directly |

Kept exactly as written: every other line, 100 BPM, D major, the
instrumentation, the mood arc. No trimming was needed — 602 words fits.

## The story and the hooks

Sunday number one: she wakes first in a bed that isn't hers and doesn't
move, counting ceiling cracks, and he mumbles something about coffee in his
sleep. Sunday six he knows her order. Sunday twenty there's frost on the
rail and one blanket for two. Sunday thirty she makes him soup. Sunday
fifty there's a cat they didn't plan, a plant with a name and pancakes
shaped like nothing. Then one Sunday, with the light coming through the
leaves, she does the math on every Monday she'd ever have to leave and
realises she doesn't want one without him. She wakes him to tell him; he
says go back to sleep, then pulls her in: *I know, I've known for weeks.*
The last chorus asks for Mondays and Wednesdays too, and the outro reverses
the first morning: now he's the one awake and not moving.

**The hook:** *"Give me Sunday mornings, messy hair and coffee rings"* —
a list that fits in a caption and a frame.

**The line for captions:** *"Give me Sunday mornings, I don't need more than
that."*

**The turn:** *"Turns out Sunday's just the day I get to see you best."*

**The quote:** *"I know, I've known for weeks."*

**Why it can travel:** the Sunday-count structure is a template people can
fill in with their own number and one object, and the window that changes
season in a single push-in is the visual that gets reposted.

## Lyrics as they will be sung

```
[intro]
The first one, I woke up before you and I didn't move,
Counting the cracks in a ceiling that wasn't mine.
You mumbled something about coffee in your sleep,
And I thought, okay, I could get used to this in time.

[verse]
Sunday number one, we were shy about the light,
You kept the curtains closed like the morning might stare.
I wore your flannel to my knees and I burned the eggs,
You ate them anyway and swore you didn't care.
Sunday number six, you already knew my order,
Two sugars and a splash, and you never asked me twice.
I stood in the doorway while you poured out two,
Thinking, I could stand here all my life.

[pre-chorus]
Monday's got alarms, and Tuesday's got the train,
Wednesday wants an answer, Thursday wants my name.
But Sunday doesn't ask me to be anyone,
Just barefoot on your balcony, that's all.

[chorus]
Give me Sunday mornings, messy hair and coffee rings,
Your voice before you're really awake, a window open, small things.
Give me Sunday mornings, no alarm, no place to be,
Sun across the pillow and your arm across me.
Give me every Sunday, and the Sundays after that,
Give me Sunday mornings, I don't need more than that.

[verse]
Sunday number twenty, there was frost along the rail,
Two mugs, one blanket, and the paper split in two.
Sunday number thirty, you were sick, I made the soup,
You said it tasted like a home, and I said, that's you.
Sunday number fifty, there's a cat we didn't plan,
Pancakes in the shape of nothing we have seen before,
There's a plant on the sill that we've kept alive two years,
And the ceiling that I counted, I don't count it anymore.

[pre-chorus]
Monday's got alarms, and Tuesday's got the train,
Wednesday wants an answer, Thursday wants my name.
But Sunday doesn't ask me to be anyone,
Just barefoot on your balcony, that's all.

[chorus]
Give me Sunday mornings, messy hair and coffee rings,
Your voice before you're really awake, a window open, small things.
Give me Sunday mornings, no alarm, no place to be,
Sun across the pillow and your arm across me.
Give me every Sunday, and the Sundays after that,
Give me Sunday mornings, I don't need more than that.

[instrumental]

[bridge]
Then one Sunday you were sleeping, and the light came through the leaves,
And I did the math on all the Mondays I would ever have to leave.
And I don't want a single one without you in it,
Not a Tuesday, not a Thursday, not a minute.
I used to think that Sunday was the day I got to rest,
Turns out Sunday's just the day I get to see you best.
So I woke you up to tell you, and you said, go back to sleep,
Then you pulled me in and said, I know, I've known for weeks.

[chorus]
Give me Sunday mornings, messy hair and coffee rings,
Give me Monday mornings too, the alarms and everything.
Give me Sunday mornings, and the Wednesdays in between,
Sun across the pillow and your arm across me.
Give me every Sunday, and the Sundays after that,
Give me all the mornings, I don't need more than that.

[post-chorus]
Messy hair, coffee rings,
Cat on the bed, the window open, small things.
Messy hair, coffee rings,
Fifty Sundays down, and I'm not counting anything.

[outro]
Sunday number one, I didn't move, I didn't dare,
Sunday number fifty, I'm the one still sleeping there.
So if you wake before me, don't move, there's nowhere to be,
It's Sunday, it's Sunday, and you get to look at me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 602 → ~5.2 min at 116 wpm, 86% of frame cap |
| Caption + lyrics tokens | 2160 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
