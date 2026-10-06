# Kids on Bicycles

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty-eight. Female lead **Mahima**, indie folk with fingerpicked
acoustic guitar, glockenspiel, a small string section and a communal group
vocal. 92 BPM, C major, ballad pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 632 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1. 92 BPM, C major, fingerpicked acoustic, glockenspiel, cello into violins, the group vocal that grows each chorus, and the bicycle-sound percussion. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with an aged-down child bible, the parents-never-above-the-chest rule, the no-memory-effect rule, matched streetlight framing, OpenPose guidance for every riding shot and a QC checklist |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

No `render.json` — at 92 BPM this is a ballad and the verify script's
116 wpm default is the right guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 58-kids-on-bicycles
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\58-kids-on-bicycles\caption.txt `
  --lyrics-file songs\58-kids-on-bicycles\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\58-kids-on-bicycles\output\kids_on_bicycles.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung |
| Digits spelled as words (*two dollars*, *nine years old*, *four streets square*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – one guitar, summer ambience, no drums]*, *[verse 2 – the plan and the truck]*) reduced to plain tags | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| The group-vocal and bicycle-percussion direction moved out of the lyric body into the caption | The model sings the lyric body literally |
| Repeated choruses and pre-choruses written out in full | The model would sing a repeat marker |

Kept exactly as written: every lyric line, 92 BPM, C major, the folk
arrangement, the bridge in the car, the bookended intro and outro, the viral
moments.

## The story and the hooks

Four children, four streets, one summer. A ramp made from a plank and a
brick, a knee held under a garden hose, a dog two doors down who knew all
four of them by the sound of a freewheel, and an ice cream truck that was the
only clock in town. They were going to buy four houses in a row and cut a
gate in every fence. Then a removal truck arrived in the last week of June, a
bike went in the back of it, and three of them rode abreast around the same
corner until the light failed with nobody saying anything. The bridge is the
only part of the song written from adulthood: a car in spring rain, the ramp
gone, the fences gone, the streetlight replaced with a cold white one that
burns all night. Then the final chorus goes back into the summer without
apologising, and hopes there are four of them out late somewhere still.

**The hook:** *"We were kids on bicycles, racing the streetlights home."*

**The line for captions:** *"We didn't know it was the best of it, we just
knew it was ours."*

**The knife line:** *"We rode three abreast and the gap was loud."*

**The turn:** *"And a part of me is nine, and she never came in."*

**Why it can travel:** every object in it is universal and free — a card in a
spoke, a hose, a ramp, a streetlight as a curfew — and the song never once
tells you how to feel about them. The three-abreast line is the part people
will quote, and the card in the spoke is a sound anyone can film.

## Lyrics as they will be sung

```
[intro]
Cut grass and hot tar and a hose in the sun,
Screen door banging and the day just begun.
Somebody's mother calling somebody in,
And the whole street waking up again.

[verse]
We built a ramp from a plank and a brick,
Argued an hour over who would go quick.
I went last and I went too slow,
Took the gravel on the drive below.
Nobody cried and nobody told,
Ran it under the hose and called it cold.
The dog two doors down knew all four of us by sound,
And the ice cream truck was the only clock in town.

[pre-chorus]
Chalk on the driveway and a sprinkler on the lawn,
Two dollars between four of us and the whole day long.
Somebody's father whistling at the door,
And we knew what it meant and we rode one more.

[chorus]
We were kids on bicycles, racing the streetlights home,
Handlebars and hollering, and nobody rode alone.
Cards in the spokes making engines out of air,
Nine years old and the whole wide world was four streets square.
We were kids on bicycles, and the only rule we knew
Was be up on the porch by the time the yellow came through.
We didn't know it was the best of it, we just knew it was ours,
We were kids on bicycles, racing the streetlights home.

[verse]
We swore we'd buy four houses in a row,
Cut a gate in every fence so we could go
Through each other's back yards for the rest of our lives,
And nobody laughed at it, nobody thought twice.
Then a moving truck came in the last week of June,
And a bike went in the back of it too soon.
We rode three abreast and the gap was loud,
And nobody said it, and we rode round and round.

[pre-chorus]
Chalk washing off in the rain on the lawn,
Three bikes on the corner and a fourth one gone.
Somebody's father whistling at the door,
And we came in early and we didn't know what for.

[chorus]
We were kids on bicycles, racing the streetlights home,
Handlebars and hollering, and nobody rode alone.
Cards in the spokes making engines out of air,
Nine years old and the whole wide world was four streets square.
We were kids on bicycles, and the only rule we knew
Was be up on the porch by the time the yellow came through.
We didn't know it was the best of it, we just knew it was ours,
We were kids on bicycles, racing the streetlights home.

[instrumental]

[bridge]
I drove down that street in the spring, in the rain,
Slowed to a crawl and I sat there again.
The ramp is long gone and the fences came down,
And the streetlight is white and it burns all night now.
But I know the sound of a card in a spoke,
And a part of me is nine, and she never came in.

[chorus]
We were kids on bicycles, racing the streetlights home,
Handlebars and hollering, and nobody rode alone.
Cards in the spokes making engines out of air,
Nine years old and the whole wide world was four streets square.
We were kids on bicycles, and I hope that somewhere still
There are four of them out late at the top of the hill.
We didn't know it was the best of it, we just knew it was ours,
We were kids on bicycles, racing the streetlights home.

[post-chorus]
Ride till the yellow comes on,
Ride till somebody calls,
Ride like the summer is long,
Ride like it never ends at all.

[outro]
Cut grass and hot tar and a hose in the sun,
Four bikes on their sides where the pavement runs.
The light on the corner is warming to gold,
And nobody's going in, and nobody's old.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 632 → ~5.4 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2178 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
