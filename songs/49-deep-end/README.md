# Deep End

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty-nine. Female lead **Mahima**, classic house, 124 BPM, A minor,
uptempo pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 739 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 124 BPM, A minor, filtered piano stabs, deep sub-bass, the drums cutting on the last pre-chorus line, the swept underwater filter and the chopped hook. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo, so the ballad default would misread the length |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 76 entries — with a two-look character bible, Kai, the one-time light handover, the water workflow, the PG-13 rule, the dive clip and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 49-deep-end
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\49-deep-end\caption.txt `
  --lyrics-file songs\49-deep-end\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\49-deep-end\output\deep_end.wav
```

Expected ~2 h.

## Pacing warning

This is an uptempo song and its length is an estimate, not a measurement.
The ballads in this catalogue sang at 116–153 words per minute; a 124 BPM
house record with a chopped post-chorus will pace faster than any of them,
but by how much is unknown until it renders. At 739 sung words:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| **140 wpm (the guard setting)** | 5.3 min | 88% |
| 155 wpm | 4.8 min | 79% |

The guard in `render.json` is a deliberately conservative 140. **If the first
render truncates the outro, drop the second post-chorus (thirty-two words, a
repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads the body literally |
| Digits spelled as words (*seven o'clock*, *forty people*, *six feet*, *count me down from three*) | The model sings digits unpredictably |
| Descriptive tag lines (*[pre-chorus — filter opening, drums cut on the last line]*) reduced to plain `[pre-chorus]` etc. | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses, pre-choruses and post-choruses written out in full instead of *(repeat)* | The model would sing the word |
| One intro line and the middle post-chorus removed | Word budget: the submission ran to 788 sung words, over the uptempo cap |
| Performance and production notes (the swept underwater filter, the silent bar before the drop, the chopped hook) moved into the caption | Stage directions in the lyric body get sung |

Kept exactly as written: the hook, both verses, the bridge, 124 BPM, A minor,
the house arrangement and the mood arc.

## The story and the hooks

Seven in the evening on a rooftop pool. The sun is coming down the side of a
glass tower and turning the water the colour of a coin, and forty people are
standing in the shallow end with their glasses at their chins. Nobody's hair
is wet. She has been that person for two summers — perfect hair, perfect
distance, perfect lie — and she says so. Then someone comes up the steps at
the far end and does not look away. He asks what she is waiting for; she says
she has a rule, and the last one left her sitting on an edge for half a year;
he says the shallow end is where the loud ones stay, and walks off toward the
deep end without pressing it. So she sets her glass down on hot tile, takes
the pins out of her hair, drops her earrings in a towel and goes in headfirst.
By the last chorus the whole roof is in the water and there is not a dry head
left on it.

**The hook:** *"Meet me at the deep end, I'm done with wading in"* — an
invitation, a decision and a location in one line.

**The line for captions:** *"I'd rather be the girl who jumped than the girl
who didn't move."*

**The chant:** *"Deep end, deep end, I am not staying dry for you."*

**The turn:** *"You said the shallow end is where the loud ones stay, / Then
you turned around and walked the other way."*

**Why it can travel:** the shallow-end image is a joke everybody has seen at
a real party, the dive is the most repostable single frame in this batch, and
the metaphor does the flirting so the song never has to be explicit.

## Lyrics as they will be sung

```
[intro]
Sun coming down the side of the building like it's pouring,
Turning the whole pool the color of a coin.
Everybody's on the edge with their feet in and their phones out,
Nobody in past the second step.
I've been the queen of the second step.

[verse]
Seven o'clock and the tiles are still warm from the sun,
Half the city down below us and the evening just begun.
Forty people in the shallow end with glasses at their chins,
Nobody's hair is wet, and nobody goes in.
I have been that girl for two whole summers, careful, dry,
Perfect hair, perfect distance, perfect lie.
Then you came up the steps at the far end of the blue,
And you didn't look away, and neither did I.

[pre-chorus]
Somebody turned the lights on underneath the water,
The whole roof went quiet and the whole pool went blue.
I've got one shoe off and one hand on the rail,
And the drop is only six feet, so

[chorus]
Meet me at the deep end, I'm done with wading in,
Standing in the shallow with a glass up to my chin.
Six feet of nothing underneath and neon on the blue,
Count me down from three and I'll come up looking at you.
Meet me at the deep end, I'm done with wading in,
Everybody's careful, I've been careful for a while,
So kick the whole year off and let it sink under the tile,
Meet me at the deep end, I'm going in.

[post-chorus]
Deep end, deep end, water going gold to blue,
Deep end, deep end, I am not staying dry for you.
Deep end, deep end, hair down and hands up high,
Deep end, deep end, meet me at the deep end.

[verse]
You asked me what I'm waiting for, I said I've got a fear,
The last one left me sitting on an edge for half a year.
You said the shallow end is where the loud ones stay,
Then you turned around and walked the other way.
Somebody laughed and somebody held a phone up in the air,
I put my glass down on the tile and pulled the pins out of my hair.
Two whole summers keeping every single thing in reach,
Gone in about the time it takes to breathe.

[pre-chorus]
Everybody's phone is up, the underwater lights are on,
The whole roof went quiet and the whole pool went blue.
I've got both shoes off now and no hand on the rail,
And the drop is only six feet, so

[chorus]
Meet me at the deep end, I'm done with wading in,
Standing in the shallow with a glass up to my chin.
Six feet of nothing underneath and neon on the blue,
Count me down from three and I'll come up looking at you.
Meet me at the deep end, I'm done with wading in,
Everybody's careful, I've been careful for a while,
So kick the whole year off and let it sink under the tile,
Meet me at the deep end, I'm going in.

[instrumental]

[bridge]
I've spent a long time with my feet on solid ground,
Reading every room before I ever made a sound.
The shallow end is safe and it is boring and it's small,
And I have been so careful that I hardly lived at all.
So if this is a mistake, then it's a mistake I choose,
And I'd rather be the girl who jumped than the girl who didn't move.

[chorus]
Meet me at the deep end, I'm done with wading in,
Hair already ruined and there's neon on my skin.
Six feet of nothing underneath and neon on the blue,
Count me down from three and I'll come up looking at you.
Meet me at the deep end, I'm done with wading in,
Everybody's in the water and there's nobody left dry,
The whole roof going under and the whole year going by,
Meet me at the deep end, I'm going in.

[post-chorus]
Deep end, deep end, water going gold to blue,
Deep end, deep end, I am not staying dry for you.
Deep end, deep end, hair down and hands up high,
Deep end, deep end, meet me at the deep end.

[outro]
Wet hair on a rooftop with a towel round my shoulders,
City carrying on below us like it always does.
You said, what took you so long, and I said, nothing, I'm here,
Meet me at the deep end, I'm already in.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 739 at 140 wpm → ~5.3 min, 88% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2265 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
