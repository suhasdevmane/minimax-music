# Late Checkout

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty. Female lead **Mahima**, chill tropical pop, 100 BPM, G major,
ballad/mid pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 637 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 100 BPM, G major, close-mic nylon guitar, steel-drum synths answering the verse lines, the dubby tape-delay section in the break and the sea under everything. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 67 entries — with a two-look character bible, Kai, the front-desk woman, the shutter-light continuity rule, workflow, the late-checkout challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 100 BPM this is a mid-tempo song and the verify script's
116 wpm ballad default is the right guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 50-late-checkout
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\50-late-checkout\caption.txt `
  --lyrics-file songs\50-late-checkout\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\50-late-checkout\output\late_checkout.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads the body literally |
| Digits spelled as words (*eleven in the morning*, *the second day*, *till two*, *sixty minutes*) | The model sings digits unpredictably |
| Descriptive tag lines (*[verse 1 — soft kick, shaker, steel drums answering]*) reduced to plain `[verse]` etc. | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses, pre-choruses and post-choruses written out in full instead of *(repeat)* | The model would sing the word |
| One intro line, one verse-one couplet, one bridge line and the middle post-chorus removed | Word budget: the submission ran to 689 sung words, over the 640 cap for this pacing class |
| Performance and production notes (the tape delay on the pre-chorus endings, the key card and door latch as percussion, the plane over the last chord) moved into the caption | Stage directions in the lyric body get sung |

Kept exactly as written: the hook, both verses, the bridge, 100 BPM, G major,
the instrumentation and the mood arc.

## The story and the hooks

Eleven o'clock on the last morning. The shutter light is lying across the
floor and stopping exactly where the packed bag is, and neither of them has
started packing the rest. There is a shell on the nightstand from the second
day, a shirt on the chair with the salt still in it, a suitcase that has been
open all week and a towel on the balcony rail that has not dried once. There
is also a phone by the bed with the front desk number on it, and a hand on her
back saying go on, ask. So she asks. In verse two the world gets into the
room — an inbox with a hundred things unread, a coat in a closet in a city
where it rains, and the certainty that the girl who gets off the plane
tomorrow is careful and quiet and busy again by ten — and then the phone
clicks back on and they have got until two. The bridge is the honest version
of the request. They spend the extra hours going into the sea in their
clothes, and it ends with a key card on a counter and a sea that carries on.

**The hook:** *"Give me a late checkout, one more hour of you"* — an ask
anyone who has ever been on a holiday has made, doing the work of a much
larger feeling.

**The line for captions:** *"I'm not asking for forever, I'm just asking for
an hour."*

**The turn:** *"I know the girl who gets off that plane tomorrow morning / Is
careful and quiet and busy again by ten."*

**The quote:** *"And I have never loved a stranger like I loved her then."*

**Why it can travel:** the phone call is a universal, filmable, three-second
moment, the metaphor never has to be explained, and the song is romantic
without a single line that could not be played anywhere.

## Lyrics as they will be sung

```
[intro]
Eleven in the morning and the light comes through the slats,
Falls across the floor and stops right where your bag is.
And the sea is doing what it always does.

[verse]
The fan is still turning and the room is still warm,
There's a shell on the nightstand from the second day.
Your shirt is on the chair with the salt still in it,
And my case has been open since we got here anyway.
The towel on the rail has not dried out all week,
And the sea keeps on saying the same thing to me.

[pre-chorus]
There's a number by the bed for the front desk,
And your hand on my back saying, go on, ask.
It's a small thing to want and a small thing to say,
So I picked it up and asked her if we could stay.

[chorus]
Give me a late checkout, one more hour of you,
Sun on the sheets and the sea coming through.
I will pay for the hour, I will pay for the day,
Anything to keep the eleven o'clock away.
Give me a late checkout, let the coffee go cold,
Leave the shutters wide and the suitcase in the hall.
There's a plane with our names on it, I know, I know,
Give me a late checkout before we have to go.

[post-chorus]
One more hour, one more hour,
Everything else can wait downstairs.

[verse]
The woman at the desk said that she'd have to go and check,
And we sat down on the end of the bed like it was a test.
I know there's an inbox with a hundred things unread,
And a coat in a closet in a city where it's wet.
I know the girl who gets off that plane tomorrow morning
Is careful and quiet and busy again by ten.
Then the phone clicked back on and she said we've got till two,
And I have never loved a stranger like I loved her then.

[pre-chorus]
There's a number by the bed for the front desk,
And your hand on my back saying, ask her again.
It's a small thing to want and a small thing to say,
So I picked it up and asked her if we could stay.

[chorus]
Give me a late checkout, one more hour of you,
Sun on the sheets and the sea coming through.
I will pay for the hour, I will pay for the day,
Anything to keep the eleven o'clock away.
Give me a late checkout, let the coffee go cold,
Leave the shutters wide and the suitcase in the hall.
There's a plane with our names on it, I know, I know,
Give me a late checkout before we have to go.

[instrumental]

[bridge]
I'm not asking for forever, I'm just asking for an hour,
But if the two of us out here on this balcony
Can make it to the airport, we can make it through the rest.
So give me sixty minutes and a door we haven't shut,
And I'll go quietly, I promise, when it's up.

[chorus]
Give me a late checkout, one more hour of you,
Sun on the sheets and the sea coming through.
She gave us until two and she did not have to,
And I'm spending all of it right here with you.
Give me a late checkout, let the coffee go cold,
Leave the shutters wide and the suitcase in the hall.
There's a plane with our names on it, I know, I know,
Give me a late checkout before we have to go.

[post-chorus]
One more hour, one more hour,
Everything else can wait downstairs.

[outro]
Key card on the counter and the door clicks shut,
The sea is still going and it doesn't know we left.
Somewhere over water I'll be holding on to your hand,
Still asking anybody for a late checkout.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2074 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
