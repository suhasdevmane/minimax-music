# Hold My Hand in Public

**Status: written and verified, NOT rendered. Not yet in the queue.**

Nineteenth song. Female lead **Mahima**, modern pop with hard piano stabs and
a very large chorus, 104 BPM, E flat major, US register. Mid pacing, no
`render.json`. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, ballad/mid budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 104 BPM, E flat major, dry percussive piano and snaps in the verses, a full kick-and-clap chorus, and two written silent beats in the arrangement. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a three-look character bible, Kai as the male lead, his mother's withheld face, the fantasy-versus-real grade rule, the composited-UI note, workflow, the crossing challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 19-hold-my-hand-in-public
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\19-hold-my-hand-in-public\caption.txt `
  --lyrics-file songs\19-hold-my-hand-in-public\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\19-hold-my-hand-in-public\output\hold_my_hand_in_public.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Digits spelled out throughout — *six months*, *count to twenty*, *two blocks* | The model sings digits unpredictably |
| Quotation marks removed from the reported speech in verse two (*this is my friend*, *are you mad*) and em-dashes removed everywhere | Punctuation is not sung; the model sings the lyric body literally |
| Descriptive tag lines (*intro – one dry piano chord*, *bridge – piano and voice, no drums*, *final chorus – he answers*) reduced to plain `[intro]`, `[bridge]`, `[chorus]`; all performance direction and the two written silent beats moved into the caption | Only the checkpoint’s documented tags exist, and anything left in the body gets sung |
| The repeated chorus written out in full instead of marked as a repeat | The verify script flags parentheses-only lines and the model would sing them |
| No `render.json` | At 104 BPM this sits in the ballad/mid class; the verify script’s 116 wpm default is the right guard |

Kept exactly as written: every line, 104 BPM, E flat major, the piano-and-snaps
production, the fantasy-chorus staging, the birthday verse and the six viral
moments. Two words were trimmed in the intro and verse two to bring the count
inside the ballad budget; nothing else was cut.

## The story and the hooks

Six months of back stairs, a car parked round the block and a door code she
knows by heart. She takes the stairs and counts to twenty so they can arrive
at the same party like a coincidence. In the group photo she is the elbow at
the edge. She is saved in his phone as somebody from work, which is funny,
because he does not work. Then at his birthday he introduces her as his
friend, she shakes his mother's hand, and she ends up in the hallway with a
coat over her arm listening to her own voice being polite from far away — in
a room she decorated that afternoon. The bridge is not an ultimatum until the
last line, and then it is. And on a Thursday, on a crossing full of
strangers, he takes her hand without ceremony, and knocks on his mother's
door, and says her name out loud.

**The hook:** *"Hold my hand in public, let the whole street know."*

**The line for captions:** *"I don't want a secret, I want a front door."*

**The knife line:** *"I'm saved in your phone as somebody from work, which is
funny, because you don't work."*

**The turn:** *"A girl who used to take up space is holding still."*

**Why it can travel:** the soft launch and the hard launch are the current
grammar of a relationship, and this is the first song written about the gap
between them — with a chorus small enough to be a caption and a bridge that
gives anyone in the same position the words for it.

## Lyrics as they will be sung

```
[intro]
Six months of back stairs and the side of the building,
Six months of your car parked around the block.
I know the code to your door and the names of your sisters,
And nobody knows mine.

[verse]
You take the elevator, I take the stairs and count to twenty,
We arrive at the same party like a coincidence.
There's a photograph of everybody in that kitchen,
And I am the elbow at the edge of it.
I'm saved in your phone as somebody from work,
Which is funny, because you don't work.
And I laughed the first time, honestly I did,
But the joke has got a little older every month.

[pre-chorus]
I don't need a ring, I don't need a speech,
Don't need your whole life rearranged.
I just want to walk two blocks and be a person that you know,
In the daylight, in front of people, with a name.

[chorus]
Hold my hand in public,
Let the whole street know.
Not a message, not a maybe, not a coat on the back of a chair,
Just your hand and my hand and the ordinary air.
I don't want a secret, I want a front door,
I want to be the one you're walking in with, not the one before.
Hold my hand in public,
Let the whole street know.

[verse]
Friday at your birthday you said, this is my friend,
And I said it back and shook your mother's hand.
I stood out in the hallway with a coat over my arm,
And I heard my own voice being polite from far away.
Then I walked to the corner and I called myself a car,
And you messaged me at midnight, are you mad.
And I typed out a paragraph and sent a single word,
And I never felt so small in a room I helped set up.

[pre-chorus]
I don't need the whole world, I don't need a post,
Don't need your friends to love me by the spring.
I just want to stand beside you in a room with the lights on,
And be a person, not a rumor, not a thing.

[chorus]
Hold my hand in public,
Let the whole street know.
Not a message, not a maybe, not a coat on the back of a chair,
Just your hand and my hand and the ordinary air.
I don't want a secret, I want a front door,
I want to be the one you're walking in with, not the one before.
Hold my hand in public,
Let the whole street know.

[instrumental]

[bridge]
It isn't about the street, it isn't about the photograph,
It's that I have started making myself smaller in the door.
I check the window before I laugh, I check the room before I lean,
And a girl who used to take up space is holding still.
So if you can't, then say you can't, and I will understand,
But I am not shrinking anymore to fit inside a hand.

[chorus]
Hold my hand in public,
Let the whole street know.
And you did, on a Thursday, on a crossing full of strangers,
With the light about to change and your fingers finding mine.
I don't want a secret, I want a front door,
And you knocked on your mother's and you said my name out loud.
Hold my hand in public,
Let the whole street know.

[post-chorus]
Let the whole street know, let the whole street know,
Take the long way home and take it slow.
Let the whole street know, let the whole street know,
It was never about the street, but let them know.

[outro]
Six months of back stairs, and then a Thursday in the sun,
Your car out at the front and both the windows down.
There's a photograph of everybody in that kitchen,
And I'm the one in the middle, and I've got a name.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2062 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
