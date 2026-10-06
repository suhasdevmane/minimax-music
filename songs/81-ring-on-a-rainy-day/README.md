# Ring on a Rainy Day

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song eighty-one. **Female + male duet** — Mahima on the lead and the hook,
a male lead on verse two and the second half of the bridge — modern wedding
ballad / cinematic acoustic pop, 82 BPM, E♭ major lifting a whole step to F
for the final chorus. Same singer as songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 638 sung words, ballad budget, no trimming needed at render time |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock — plus a `Duet Partner` and `Duet Structure` line for the male lead. 82 BPM, E♭ major with the modulation, the string and piano build and the rain-on-canvas ambience. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 69 entries — with a three-look character bible for Mahima, Kai as the groom, the workflow, the wet-wedding challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 81-ring-on-a-rainy-day
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\81-ring-on-a-rainy-day\caption.txt `
  --lyrics-file songs\81-ring-on-a-rainy-day\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\81-ring-on-a-rainy-day\output\ring_on_a_rainy_day.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung; the model renders the body literally |
| Digits spelled as words (*a hundred percent*, *seven*, *ten*, *fifty people*) | The model sings digits unpredictably |
| The descriptive tag lines (`[intro – piano and rain only, half-smiling]`, `[verse 2 – male lead]`, `[final chorus – modulated]`) reduced to plain `[intro]`, `[verse]`, `[chorus]` | Only the checkpoint's plain section tags exist; anything else is dropped or sung |
| Who sings what moved out of the lyric body and into the caption's `Duet Structure` line | The model has no per-line singer control; the split lives in the caption |
| Both choruses and the pre-chorus refrain written out in full rather than marked as repeats | A `(repeat)` line would be sung |
| Verse one and verse two trimmed to seven lines each to land inside the ballad budget | 682 words on the first pass; the budget is 600–640 |

Kept exactly as written: the hook, the proposal, the thunder in the vows, the
mother's sunlit album, the flooded dance floor, 82 BPM, E♭ major with the
lift, the instrumentation and the mood arc.

## The story and the hooks

He proposed a year ago in a gravel parking lot above a grey sea, in weather
coming sideways, because he could not wait for a better day. The wedding gets
the same sky. Chairs go inside, the flowers move twice, the tent man never
shows and the aisle turns to clay, and every single person at the venue
apologises for the weather to the only two people who are glad of it. His
verse is the morning: the ironed collar going soft, his father holding a
jacket over his mother, thunder taking half of his vows so he says them again
louder. Her bridge is her mother's cloudless wedding album and the house that
marriage ended in. Then the first dance happens outdoors anyway, the marquee
floor floods, and nobody goes in.

**The hook:** *"You gave me a ring on a rainy day, so let it rain."*

**The line for captions:** *"Every good thing I have came the same way."*

**The knife line:** *"An album full of sunshine and a house she had to leave."*

**The turn:** *"I will take a roof that leaks above a man who doesn't."*

**Why it can travel:** almost every wedding has a weather story, and this one
takes the side of the weather. It is a first-dance record and an engagement
reel at the same time, and the last line — *"it kept its word, and so did
we"* — is a vow in eight words.

## Lyrics as they will be sung

```
[intro]
The forecast said a hundred percent by four,
So we bought the cheap umbrellas at the corner store.
You said that we could wait for a kinder sky,
I said the sky has had its whole life to try.

[verse]
You went down on the wet in a parking lot by the water,
Gray coming sideways off the sea behind your back.
The box would not open and your hands were shaking,
And I was crying before you got the question out.
Your knee left a print in the gravel and the rain,
My mascara took a shortcut down my chin.
And you laughed like the weather was a friend of yours.

[pre-chorus]
They moved the chairs inside, they moved the flowers twice,
The tent man never showed and the aisle turned to clay.
Everyone kept apologizing for the sky,
And the two of us were the only ones okay.

[chorus]
You gave me a ring on a rainy day,
So let it rain, let it come, let it stay.
Let it soak through the silk and ruin the shoes,
There is nothing in this garden I would trade for you.
The band's under the awning and the cake's in the hall,
And your hand is on my back and I don't care at all.
Every good thing I have came the same way,
You gave me a ring on a rainy day.

[verse]
I ironed a shirt at seven and it lost by ten,
Stood at the end of the aisle with my collar going soft.
My father held his jacket like a roof over my mother,
And your uncle raised a golf umbrella like a flag.
Then the doors came open and none of it mattered,
Thunder took the second half of what I meant to say,
So I said it again louder, and I'd say it in worse.

[pre-chorus]
The photographer kept waiting for a break in it,
Then the light went strange and gold behind the gray.
Everyone kept apologizing for the sky,
And we were the only two who wanted it this way.

[chorus]
You gave me a ring on a rainy day,
So let it rain, let it come, let it stay.
Let it soak through the silk and ruin the shoes,
There is nothing in this garden I would trade for you.
The band's under the awning and the cake's in the hall,
And your hand is on my back and I don't care at all.
Every good thing I have came the same way,
You gave me a ring on a rainy day.

[instrumental]

[bridge]
My mother married in a heatwave, not a cloud to spare,
An album full of sunshine and a house she had to leave.
So keep the painted blue, keep the perfect afternoon,
I will take a roof that leaks above a man who doesn't.
And I will take the woman who kicked her heels off early,
Who never checked her hair and walked out into it.

[chorus]
You gave me a ring on a rainy day,
So let it rain, let it come, let it stay.
Let it flatten every curl that took an hour to do,
There is nothing in this garden I would trade for you.
There's a river running under the floor of the tent,
And we're barefoot in the middle of it, soaked and content.
Every good thing we have came the same way,
You gave me a ring on a rainy day.

[post-chorus]
So let it rain, so let it rain,
On the folding chairs and the paper chain.
So let it rain, so let it rain,
We are not going in, we are not going in.

[outro]
The last song finished and nobody moved,
Fifty people dancing in a garden turned to mud.
The forecast said a hundred percent by four,
And it kept its word, and so did we.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2247 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
