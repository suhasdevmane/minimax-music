# Borrowed Shirt

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song thirty-five. Female lead **Mahima**, bedroom R&B with neo-soul warmth —
soft electric piano, vinyl crackle, muted guitar — flirty and intimate,
tasteful throughout, US register. 84 BPM, B♭ major, ballad pacing. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 84 BPM, B♭ major, the electric-piano spine, the run-out-groove crackle and the drum-free bridge. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a single-look character bible, Kai as the man, the light-as-clock rule, the tasteful-framing rule, workflow and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 35-borrowed-shirt
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\35-borrowed-shirt\caption.txt `
  --lyrics-file songs\35-borrowed-shirt\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\35-borrowed-shirt\output\borrowed_shirt.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | Punctuation is not sung; the model reads the lyric body literally |
| Digits spelled as words (*three buttons deep*, *two spoons*, *fourth Sunday*) | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – crackle, one chord…]`, `[chorus – wide and warm, not loud]`, `[verse 2]`, `[pre-chorus 2]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| Every repeated section written out in full — both pre-choruses, all three choruses | `(repeat)` would be sung as the word |
| Two lines shortened in the chorus to hold the word budget | 653 words fell to 639, inside the 600–640 ballad band |

Kept exactly as written: every image, 84 BPM, B♭ major, the instrumentation,
the mood arc, the bridge turn.

## The story and the hooks

She wakes in his flat on a Sunday in his pale blue shirt with the sleeves
rolled twice, and the song never leaves the apartment. The kettle rattles its
lid, he is face down in the pillow, she takes the chipped mug instead of the
matching ones and makes the coffee far too sweet so he will steal a sip.
Then verse two turns the morning into a pattern: fourth Sunday in a row, a
hair tie on his wrist that isn't his, her charger living in his bedside
drawer, her milk on the shopping list in a second handwriting. She nearly
asks the question at the counter and asks about the toast instead. In the
bridge she folds the shirt to give it back and he tells her to keep it, and
that is the closest either of them comes to saying anything.

**The hook:** *"I'm wearing your shirt and nothing else is on my mind"* —
first and last line of every chorus, and the joke inside it stays PG-13.

**The line for captions:** *"He said keep it. That was the whole
conversation."*

**The turn:** *"So I don't make a speech and I don't ask for proof / I just
put it back on, and that's the whole truth."*

**The quote:** *"Small and ordinary and holy as it gets."*

**Why it can travel:** it is a soft-launch record. Every detail is an object
somebody watching owns — the chipped mug, the drawer, the list on the fridge
— and the whole emotional payload lands without either character saying what
they are. The borrowed-clothes challenge writes itself.

## Lyrics as they will be sung

```
[intro]
Needle at the end of the record, going round,
Making that soft little scratch instead of sound.
Curtains half open on a street still asleep,
And your shirt on my shoulders, three buttons deep.

[verse]
The kettle's doing that thing where it rattles the lid,
You're still under the blanket, doing what you did,
Which is nothing, beautifully, one arm hanging loose,
Face down in the pillow like you've got no excuse.
I roll the sleeves up twice and they swallow my hands,
Smells like cedar and the rain that we walked in.
I take the ugly mug, the one with the chip,
Make the coffee far too sweet so you'll steal a sip.

[pre-chorus]
There's a watch face down on the windowsill,
There's a shoe by the door lying where it fell.
Nothing here is tidy, nothing here is planned,
And I've never felt this easy standing where I stand.

[chorus]
I'm wearing your shirt and nothing else is on my mind,
No plans, no phone, no reason to be on time.
The sunlight's doing slow laps across the floor,
And I'm not thinking past the kitchen door.
Small and ordinary and holy as it gets,
Toast and butter, two spoons, and the radio set.
Say my name low, say it one more time,
I'm wearing your shirt and nothing else is on my mind.

[verse]
Fourth Sunday in a row that I've woken up here,
Which is not an accident, let's be clear.
There's a hair tie on your wrist that is not yours,
And my charger's got a home in your bedside drawer.
I nearly ask the question at the counter, then I don't,
I ask about the toast instead and you say, sure, both.
You come in half asleep and you kiss my shoulder,
Not my mouth, my shoulder, and somehow that's bolder.

[pre-chorus]
There's a watch lying face down where you left it,
There's a list on the fridge and my milk is on it.
Nothing here is tidy, nothing here is planned,
And I've stopped counting mornings on one hand.

[chorus]
I'm wearing your shirt and nothing else is on my mind,
No plans, no phone, no reason to be on time.
The sunlight's doing slow laps across the floor,
And I'm not thinking past the kitchen door.
Small and ordinary and holy as it gets,
Toast and butter, two spoons, and the radio set.
Say my name low, say it one more time,
I'm wearing your shirt and nothing else is on my mind.

[instrumental]

[bridge]
I fold it on the bed like I'm handing it back,
Sleeves squared and the collar smoothed flat.
You look at the shirt and you look at my face,
And you say, that one is yours now, it lives at your place.
So I don't make a speech and I don't ask for proof,
I just put it back on, and that's the whole truth.

[chorus]
I'm wearing your shirt and nothing else is on my mind,
No plans, no phone, no reason to be on time.
The sunlight's doing slow laps across the floor,
And I'm not thinking past the kitchen door.
It's not a big love song, it's a Sunday and a shine,
Your shirt, my coffee, and the rest of it is fine.
Say my name low, say it one more time,
I'm wearing your shirt and nothing else is on my mind.

[post-chorus]
Nothing else, nothing else, nothing else is on my mind,
Just the kettle and the light and you taking your time.
Nothing else, nothing else, nothing else is on my mind,
Your shirt on my shoulders and the whole day mine.

[outro]
Needle at the end of the record, going round,
Neither of us getting up to fix the sound.
Your shirt on my shoulders, three buttons deep,
And the best part of Sunday is the part we don't speak.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2019 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
