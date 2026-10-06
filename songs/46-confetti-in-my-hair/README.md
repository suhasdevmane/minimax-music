# Confetti in My Hair

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty-six. Female lead **Mahima**, party pop with a live brass section,
126 BPM, C major, uptempo pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 747 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 126 BPM, C major, live brass answering every hook line, gang vocals in a room, the another-room filter on the hook inside the break. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo, so the ballad default would misread the length |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 75 entries — with a three-look character bible, the leaving friend, the two-grade rule, matched-frame pairs, workflow, the six-faces challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 46-confetti-in-my-hair
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\46-confetti-in-my-hair\caption.txt `
  --lyrics-file songs\46-confetti-in-my-hair\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\46-confetti-in-my-hair\output\confetti_in_my_hair.wav
```

Expected ~2 h.

## Pacing warning

This is an uptempo song and its length is an estimate, not a measurement.
The ballads in this catalogue sang at 116–153 words per minute; a 126 BPM
party-pop record with a chanted post-chorus will pace faster than any of
them, but by how much is unknown until it renders. At 747 sung words:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| **140 wpm (the guard setting)** | 5.3 min | 89% |
| 155 wpm | 4.8 min | 80% |

The guard in `render.json` is a deliberately conservative 140. **If the first
render truncates the outro, drop the second post-chorus (twenty-six words, a
repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads the body literally |
| Digits spelled as words (*eight in the morning*, *about eleven*, *twenty minutes*, *ten hours north*) | The model sings digits unpredictably |
| Descriptive tag lines (*[verse 1 — dry kick, shaker, the inventory]*) reduced to plain `[verse]` etc. | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses and post-choruses written out in full instead of *(repeat)* | The model would sing the word |
| Two lines cut from each verse and one post-chorus removed | Word budget: the submission ran to 854 sung words, well over the uptempo cap |
| Performance and production notes (the another-room filter, the confetti-cannon percussion, the bar of silence) moved into the caption | Stage directions in the lyric body get sung |

Kept exactly as written: the hook, the turn in verse two, 126 BPM, C major,
the brass-led arrangement and the mood arc.

## The story and the hooks

Eight in the morning in a flat that lost. There is a sock in the fruit bowl,
a shoe standing upright in a plant pot, a hat on a lamp, half a slice of cake
and a phone number in green pen up the back of her hand. Six people stand at
a counter squinting over mugs, and then all of them laugh at once because
they all remembered the same thing. Verse two rewinds to eleven the night
before: the neighbours came up, somebody's little brother turned out to be
able to play, and a confetti cannon fired into a ceiling fan snowed on the
room for twenty minutes. And then the reason: one of them was flying out in
the morning to a city ten hours north, so they made the night bigger than it
had any right to be, and stood in a dark kitchen holding on without saying
goodbye. The bridge is the year that made the party necessary. The last
chorus carries a suitcase down a stairwell, and on Sunday she finds one gold
disc in a shoe and puts it in a jar by the door.

**The hook:** *"Woke up with confetti in my hair, and I don't even care"* —
a whole image and a whole attitude in one line, and it is the title.

**The line for captions:** *"Let the floor keep the evidence, let the kitchen
keep the proof."*

**The turn:** *"Then we stood there in the kitchen with the big light
switched off / And nobody said goodbye out loud, we just held on a bit too
long."*

**The quote:** *"Last night was the first night in a long time that nobody in
this room had to try."*

**Why it can travel:** it is a party song that is really a friendship song.
The comedy of the first verse buys the second verse's goodbye, and the
morning-after format — everyone has that photo — makes the hook line a
caption people already wanted to write.

## Lyrics as they will be sung

```
[intro]
Morning came in sideways through a curtain nobody closed,
Landed on a room that looks like it went ten rounds.
I sat up on the carpet and I felt it in my hair,
Little gold and pink and silver, still there.

[verse]
Eight in the morning and the living room's a crime scene,
There's a sock inside the fruit bowl and I don't know what that means.
The tall one's on the sofa with a cushion on his head,
The quiet one is stacking paper plates instead.
There's a slice of cake with one bite gone beside the chair,
And the balloons are half the height they were last night in here.
My mascara took the pillowcase down with it in the night,
And I've never been so glad to see a mess in daylight.

[pre-chorus]
Kettle's on, and nobody is talking,
Six of us just squinting at the light.
Somebody laughs and then everybody's laughing,
Because we all just remembered the same thing.

[chorus]
Woke up with confetti in my hair, and I don't even care,
Sun through the curtains like it's proud of what went on in here.
There's a shoe in the plant and a hat on the lamp,
And a phone number written up the back of my hand.
Woke up with confetti in my hair, and I don't even care,
Nobody is touching a broom in this apartment soon.
Let the floor keep the evidence, let the kitchen keep the proof,
Woke up with confetti in my hair, and I don't even care.

[post-chorus]
Confetti in my hair, confetti in my hair,
Little bit of last night stuck to everywhere.
Confetti in my hair, confetti in my hair,
And I don't even care, no, I don't even care.

[verse]
Rewind to about eleven when the neighbors came up too,
And somebody's little brother played a keyboard like he knew.
Someone fired the cannon early, aimed it up into the fan,
So it snowed on us for twenty minutes longer than it planned.
She was leaving in the morning for a city ten hours north,
So we made the whole night bigger than the rest of it was worth.
Then we stood there in the kitchen with the big light switched off,
And nobody said goodbye out loud, we just held on a bit too long.

[pre-chorus]
Kettle's on again, still nobody's talking,
Six of us, and one of us is packed.
Somebody laughs and then everybody's laughing,
Then we're crying, then we're laughing, and that's that.

[chorus]
Woke up with confetti in my hair, and I don't even care,
Sun through the curtains like it's proud of what went on in here.
There's a shoe in the plant and a hat on the lamp,
And a phone number written up the back of my hand.
Woke up with confetti in my hair, and I don't even care,
Nobody is touching a broom in this apartment soon.
Let the floor keep the evidence, let the kitchen keep the proof,
Woke up with confetti in my hair, and I don't even care.

[instrumental]

[bridge]
It was a year that took a lot out of all of us,
A bad spring and a worse July.
Last night was the first night in a long time
That nobody in this room had to try.
So I'm not sweeping yet and I'm not washing out my hair,
I'll keep the whole night on me for as long as it will stay.

[chorus]
Woke up with confetti in my hair, and I don't even care,
Sun through the curtains like it's proud of what went on in here.
There's a shoe in the plant and a hat on the lamp,
And her ticket folded up where her jacket used to hang.
Woke up with confetti in my hair, and I don't even care,
We will clean it up tomorrow or we won't, and that's the truth,
Let the floor keep the evidence, let the kitchen keep the proof,
Woke up with confetti in my hair, and I don't even care.

[post-chorus]
Confetti in my hair, confetti in my hair,
Little bit of last night stuck to everywhere.
Confetti in my hair, confetti in my hair,
And I don't even care, no, I don't even care.

[outro]
Sweeping up on Sunday and I found one in my shoe,
Little gold circle from a night I'm not gonna lose.
Put it in a jar on the shelf beside the door,
Woke up with confetti in my hair, and I don't even care.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 747 at 140 wpm → ~5.3 min, 89% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2262 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
