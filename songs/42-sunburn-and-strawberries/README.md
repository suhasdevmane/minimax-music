# Sunburn and Strawberries

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty-two. Female lead **Mahima**, summer pop with a surf-rock spine —
spring-reverb guitars, gang handclaps and a whistled hook — **Australian
register**. 118 BPM, A major, uptempo pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 741 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 118 BPM, A major, the surf-guitar lifecycle, the whistled counter-melody and the drumless bridge. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 83 entries — with a one-look character bible, Kai as the man, a recurring seagull, three matched wides across the day, the sunburn-progression rule, workflow and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 42-sunburn-and-strawberries
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\42-sunburn-and-strawberries\caption.txt `
  --lyrics-file songs\42-sunburn-and-strawberries\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\42-sunburn-and-strawberries\output\sunburn_and_strawberries.wav
```

Expected ~2 h.

## Pacing warning

**This is an uptempo song and its pacing is unmeasured.** Ballads on this
setup measured 116–153 words per minute; at 118 BPM with a repeated chanted
post-chorus this will sing faster, but by how much is a guess until it
renders. The lyrics are 741 words. Against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| 130 wpm | 5.7 min | 95% |
| **140 wpm (the guard setting)** | 5.3 min | 88% |
| 155 wpm | 4.8 min | 80% |
| 170 wpm | 4.4 min | 73% |

118 BPM is the slowest uptempo tempo in the catalogue, so this one is likelier
than most to sit near the guard rather than far above it; the three
post-chorus chants are 84 of the 741 words and will pace fastest. A blended
estimate of 140–150 wpm is reasonable. **If the first render truncates the
outro, the fix is to drop the third post-chorus (28 words, a verbatim repeat)
and re-render.** The measured pacing goes into `docs/VOICE_RECIPE.md` either
way.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | Punctuation is not sung; the model reads the lyric body literally |
| Digits spelled as words (*half five*, *eight*, *two o'clock*, *eleven of us*, *four o'clock*, *twenty years*) | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – one surf guitar, car door, gravel]`, `[chorus – twin guitars and the whistle]`, `[post-chorus – whistle and claps]`, `[verse 2]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| Every repeated section written out in full — both pre-choruses, all three choruses, all three post-choruses | `(repeat)` would be sung as the word |
| Three lines lengthened slightly | 719 words rose to 741, nearer the top of the 700–760 uptempo band, which protects the running time |

Kept exactly as written: every lyric line, 118 BPM, A major, the
instrumentation, the mood arc, the Australian idiom, the bridge turn.

## The story and the hooks

Alarm at half five, four people in a small car, a punnet of strawberries
bought off a highway stall, and a whole day with nothing planned in it. The
back window is stuck, the radio is cactus, the car park is full by eight and
the sand is already too hot to stand on. His brother puts the footy in the
water, a seagull runs a plan on the chips, and she draws a stripe of zinc
across his nose and he lets her — which is the entire romance, and neither of
them mentions it. By two the tide has taken half their belongings and nobody
moves. His mum rings about tea and he says maybe in a voice that means no.
The van comes, eleven of them queue with coins scraped out of a car, and at
four the good light arrives and a nothing sort of Saturday turns into the
one. The bridge says why: you don't get told which day it is until it's gone,
and you find out in April.

**The hook:** *"Sunburn and strawberries, that's my kind of summer"* — opens
both halves of every chorus and closes them.

**The line for captions:** *"You don't get told which day it is until it's
gone."*

**The turn:** *"We'll be telling this one wrong for the next twenty years /
And nobody will fix it, and nobody cares."*

**The quote:** *"A nothing sort of Saturday has got something to prove."*

**Why it can travel:** it is a summer record that is specific enough to be
believed — thongs on hot sand, sand in the sandwich, coins out of a cup
holder, an ice-cream van doing the same eight bars — and the flirtation is a
single wordless gesture rather than a chorus of intent. The zinc stripe is
the shareable frame and the whistle is the earworm.

## Lyrics as they will be sung

```
[intro]
Alarm at half five and the kettle's not on,
Four of us awake and the boot's already done.
Punnet of strawberries from a stall on the road,
And a whole day in front of us and nowhere to go.

[verse]
The back window's stuck so we cop it all the way,
Radio's cactus so we sing to fill the day.
Sunnies on your head and your feet up on the dash,
And a bag of hot chips going cold in the back.
Car park's full by eight and the sand is already hot,
Thongs off, straight in, and we don't check the spot.
Your brother's launched the footy and it's landed in the drink,
And a seagull's got a plan and it's closer than you think.
I put zinc across your nose and you just let me do it,
You don't say a word about it, but I know that you knew it.

[pre-chorus]
Salt in everything, sand in the bread,
Somebody's towel is on somebody's head.
The jetty's got a queue and the queue's got a dare,
And the whole day's going nowhere and I don't care.

[chorus]
Sunburn and strawberries, that's my kind of summer,
Red on my shoulders and red on the back of my hands.
There's an ice-cream van doing the same eight bars,
And a mile of nothing but water and sand.
Sunburn and strawberries, that's my kind of summer,
Salt in my hair and my thongs going west.
I'll be peeling by Wednesday and I'd do it all again,
Sunburn and strawberries, and today was the best.

[post-chorus]
Sunburn and strawberries, sunburn and strawberries,
That's my kind, that's my kind of summer.
Sunburn and strawberries, sunburn and strawberries,
Salt on my mouth and the sun going under.

[verse]
Two o'clock and the tide has come a long way in,
Half our stuff is floating and we're laughing at the win.
Your mum's on the phone about coming back for tea,
And you say, maybe, in a voice that means, not me.
Ice-cream van rolls up and plays the same eight bars,
Eleven of us queue with the coins we found in cars.
You take the one with bubblegum stuck on its nose,
And you eat it in the water and you don't come in close.
Four o'clock, the good light, and nobody has moved,
And a nothing sort of Saturday has got something to prove.

[pre-chorus]
Salt in everything, sand in the cake,
Half the arvo gone and nobody's awake.
The jetty's got a queue and the queue's got a dare,
And I'm up on the rail and I'm already there.

[chorus]
Sunburn and strawberries, that's my kind of summer,
Red on my shoulders and red on the back of my hands.
There's an ice-cream van doing the same eight bars,
And a mile of nothing but water and sand.
Sunburn and strawberries, that's my kind of summer,
Salt in my hair and my thongs going west.
I'll be peeling by Wednesday and I'd do it all again,
Sunburn and strawberries, and today was the best.

[post-chorus]
Sunburn and strawberries, sunburn and strawberries,
That's my kind, that's my kind of summer.
Sunburn and strawberries, sunburn and strawberries,
Salt on my mouth and the sun going under.

[instrumental]

[bridge]
You don't get told which day it is until it's done,
You just wake up in April and you know that it's gone.
So I'm keeping the sand in my shoe and the strawberry stain,
And the photo where your eyes are shut and mine are the same.
We'll be telling this one wrong for the next twenty years,
And nobody will fix it, and nobody cares.

[chorus]
Sunburn and strawberries, that's my kind of summer,
Red on my shoulders and red on the back of my hands.
Ice-cream van's gone and the car park's clear,
And a mile of nothing but water and sand.
Sunburn and strawberries, that's my kind of summer,
Salt in my hair and my sunnies gone west.
I'll be peeling by Wednesday and I'd do it all again,
Sunburn and strawberries, and today was the best.

[post-chorus]
Sunburn and strawberries, sunburn and strawberries,
That's my kind, that's my kind of summer.
Sunburn and strawberries, sunburn and strawberries,
Salt on my mouth and the sun going under.

[outro]
Headlights on the coast road and the seats are all wet,
Somebody's asleep with a towel on their head.
Half a punnet left and it's going hand to hand,
Sunburn and strawberries, and a whole lot of sand.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 741 at 140 wpm → ~5.3 min, 88% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2314 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
