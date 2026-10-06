# Thank You for Leaving

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-one. Female lead **Mahima**, piano pop ballad with cinematic
strings, 84 BPM, D♭ major, a genuine, unbitter thank-you to the one who
left. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, trimmed by twelve words to sit inside the ballad budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 84 BPM, D♭ major, felt piano, strings and the train-platform ambience per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 74 entries — built from the submission's scene direction, plus a three-look character bible, a faceless ex, the plant-as-clock rule, workflow, plant challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 71-thank-you-for-leaving
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\71-thank-you-for-leaving\caption.txt `
  --lyrics-file songs\71-thank-you-for-leaving\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\71-thank-you-for-leaving\output\thank_you_for_leaving.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from *"look at you"* and *"you seem lighter"* | Punctuation is not sung; the model would voice it |
| *"And I hated you in March"* → *"I hated you in March"*, *"Learned how to"* → *"Learned to"*, *"Oh, I arrived"* → *"I arrived"* and three more small trims | The submission ran to 650 sung words; twelve were cut to land at 638, inside the ballad frame |
| *"the flat"* → *"my place"* / *"the place"* | US register per the catalogue |
| `[verse 1]`/`[verse 2]`, `[final chorus]` and the descriptive tag lines reduced to plain tags; every repeated chorus written out in full | The model only knows plain section tags and sings the body literally |

Kept exactly as written: every image, 84 BPM, D♭ major, the instrumentation,
the mood arc, the plant.

## The story and the hooks

He left on a winter platform and didn't look back. She moved into a place
with a crack in the wall, one chair, one plate, and bought a half-dead plant
from the corner store. She hated him in March. By June she was running. By
August she was up. The plant grew a leaf; she fixed the sink from a video;
she ran into his sister by the fruit and didn't ask. A year on there's a rug,
a friend with a key, a spare chair at the table and a plant touching the
ceiling, and the only thing she wants to say to him is thank you, and she
means it.

**The hook:** *"Thank you for leaving, I finally arrived"* — the glow-up
line, caption-ready.

**The line for captions:** *"You thought you were the ending, you were only
the ride."*

**The quote:** *"Some people are a home, and some people are a train."*

**The turn:** *"I'd have waited on that platform till my hair turned grey /
So thank God, thank you, thank the day you pulled away."*

**Why it can travel:** it's the moving-on song with no bitterness in it,
which is rarer and more shareable than revenge; the plant gives every
listener a then-and-now to post; and the final chorus swaps the handshake
for a coffee, which is the kind of detail people quote.

## Lyrics as they will be sung

```
[intro]
I found the box of your things last week,
Sat on the floor and I didn't even weep.
Just a jacket, a charger, a ticket stub,
And a version of me I've stopped dreaming of.

[verse]
The night you left, the platform was cold,
You didn't look back, and I didn't hold.
I stood there shaking with my hands in my sleeves,
Thinking nobody survives when the whole train leaves.
I moved to a place with a crack in the wall,
One chair, one plate, one mattress, that's all.
Bought a plant from the corner store, half dead,
Put it by the window and I went to bed.

[pre-chorus]
I hated you in March, I'll be honest, it was rough,
By June I was running, and by August I was up.
Turns out the silence you left me had room
For all of the things I never got to bloom.

[chorus]
Thank you for leaving, I finally arrived,
You closed a door and I walked out into the light.
You took the girl who waited by the phone,
And left me with a woman who can make it on her own.
Thank you for leaving, I mean it, no spite,
I'd shake your hand on that platform tonight.
You thought you were the ending, you were only the ride,
Thank you for leaving, I finally arrived.

[verse]
The plant grew a leaf in the middle of May,
Said, look at you, out loud, to a plant, okay.
Learned to fix the sink from a video,
Learned to fall asleep with the radio low.
Ran into your sister at the grocery store,
She hugged me and said, you seem lighter than before.
I said, I am, and I didn't have to try,
I didn't ask about you, and she didn't say why.

[pre-chorus]
I hated you in March, I'll be honest, it was rough,
By June I was running, and by August I was up.
Now my place has got a rug and a friend with a key,
And a window full of green that's growing just for me.

[chorus]
Thank you for leaving, I finally arrived,
You closed a door and I walked out into the light.
You took the girl who waited by the phone,
And left me with a woman who can make it on her own.
Thank you for leaving, I mean it, no spite,
I'd shake your hand on that platform tonight.
You thought you were the ending, you were only the ride,
Thank you for leaving, I finally arrived.

[instrumental]

[bridge]
If you're wondering if I'm bitter, come and see,
There's a spare chair at my table that wasn't there for me.
I don't play our song, I don't drive down your street,
I don't wish you badly, I wish you well, and I mean it.
Some people are a home, and some people are a train,
You pull out of the station and don't come back again.
I'd have waited on that platform till my hair turned grey,
So thank God, thank you, thank the day you pulled away.

[chorus]
Thank you for leaving, I finally arrived,
The plant's touching the ceiling and I'm doing alright.
You took the girl who waited by the phone,
And left me with a woman who can make it on her own.
Thank you for leaving, I mean it, no spite,
I'd buy you a coffee on that platform tonight.
You thought you were the ending, you were only the ride,
Thank you for leaving, I finally arrived.

[post-chorus]
I arrived, I arrived,
Watered myself and I came back alive.
I arrived, I arrived,
Thank you for leaving, look at me thrive.

[outro]
I found the box of your things last week,
Left it on the platform for the city to keep.
Kept the plant, kept the place, kept the sky,
Thank you for leaving, I finally arrived.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2145 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
