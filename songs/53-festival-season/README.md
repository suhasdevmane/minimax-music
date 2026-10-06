# Festival Season

**Status: written and verified, NOT rendered. Not yet in the queue.**

Fifty-third song. Female lead **Mahima**, festival EDM-pop / big-room dance
pop with supersaw drops and a crowd-chant post-chorus, 128 BPM, F♯ minor.
Uptempo, US register. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 748 sung words, every chorus and chant written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 128 BPM, F♯ minor, supersaws, sidechained sub, the chant post-chorus, the half-time breakdown in the instrumental, the four a.m. bridge on piano and pad. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 87 entries — a three-look weekend-order character bible, the crew and the two flags, a faceless bucket-hat stranger, workflow, the recap challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 53-festival-season
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\53-festival-season\caption.txt `
  --lyrics-file songs\53-festival-season\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\53-festival-season\output\festival_season.wav
```

Expected ~2 h.

## Pacing is unmeasured

This is an uptempo song at 128 BPM with a chant post-chorus, and it will
pace faster than the ballads (which measured 116–153 words per minute). The
lyrics are 748 words. Against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| 125 wpm | 6.0 min | **at the edge** |
| **140 wpm (the guard setting)** | 5.3 min | 89% |
| 160 wpm | 4.7 min | 78% |

The chant sections (48 of the 748 words) sing fast, and EDM-pop verses at
this tempo usually sit around 140–150 wpm, so a blended estimate lands near
5.2 minutes. The guard is set at a conservative 140. **If the first render
truncates the outro, drop the second post-chorus (24 words, a repeat) and
re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| `4 a.m.`, `2%`, `10,000` → *"Four a.m."*, *"two percent"*, *"ten thousand"* | The model sings digits unpredictably |
| Descriptive tag lines (*[chorus – the drop, huge, singalong]*) reduced to plain tags | The model only knows plain section tags |
| Every repeated chorus, pre-chorus and chant written out in full | The model sings the lyric body literally; a *(repeat)* would be sung |
| Quotation marks removed from the bucket-hat line and the whisper | Punctuation is not sung |
| *mum* → *mom* | US register per the catalogue |

Kept exactly as written: every other line, 128 BPM, F♯ minor, the
production list, the mood arc.

## The story and the hooks

Friday noon: the wristband clicks, the tent is half up, the bass is in the
grass before the stage is in view. Rain at four and nobody runs. Two flags
on poles so the lost ones can find the crew. Phone at two percent and she
leaves it there. Saturday: sunburnt shoulders, the crew lost and found by
a flag, a stranger's shoulders above ten thousand phone lights, a moment
she doesn't need to own. Four a.m.: the main stage dark, a small tent still
going, a sunrise set, and a girl in a puddle's reflection she really likes.
Sunday: tent down, the bus, the wristband stays on.

**The hook:** *"It's festival season, and we're not going home"* — the drop
line and the recap caption.

**The chant:** *"Not going home, not going home / Oh oh, oh oh oh, we're not
going home."*

**The line for captions:** *"Some nights you get a moment and you don't have
to own it."*

**The turn:** *"Monday's got a train and a desk and a boss who knows my name
/ But right now I'm the girl in the field who danced through all the rain."*

**Why it can travel:** it is built for festival recap reels at a tempo they
actually use, the chant is a clap-along, and the sunrise bridge gives the
drop an emotional reason to exist.

## Lyrics as they will be sung

```
[intro]
Wristband on and the tent's half up,
Warm cider in a paper cup.
Bass in the ground before we see the stage,
Three days off from acting my age.

[verse]
Parked in a field in the wrong kind of shoes,
Glitter on my cheekbones and nothing to lose.
Rain came down at four and nobody ran,
Mud to the ankles, we danced where we stand.
Flags on long poles so the lost ones can find us,
A yellow one, a pink one, the whole crew behind us.
Someone's got a speaker, someone's got a drum,
Someone's mom packed sandwiches enough for everyone.
Phone at two percent and I'm not gonna charge it,
Whatever this weekend is, I don't wanna watch it.
Walk through the gate like we've done it a hundred times,
Big wheel turning slowly on the far end of the sky.

[pre-chorus]
Hear that low end rolling in over the hill,
Ten thousand strangers going quiet and still.
Hands up, lights out, one breath, then the drop,
Somebody count me in, I'm never gonna stop.

[chorus]
It's festival season, and we're not going home,
Glitter in the mud and my voice is gone.
Sing it with the stranger on your left and your right,
We came for the weekend, we're staying for the light.
It's festival season, and the field's on fire,
Every flag's a friend and every song's a choir.
Hands up high, it's festival season,
And we're not going home, no, we're not going home.

[post-chorus]
Not going home, not going home,
Oh oh, oh oh oh, we're not going home.
Not going home, not going home,
Oh oh, oh oh oh, we're not going home.

[verse]
Saturday, sunburnt shoulders and a borrowed hat,
Lost the crew by the food trucks, found them just like that.
A boy in a bucket hat said, can you see from there,
Then he lifted me up and I was waving in the air.
Ten thousand phone lights like a low-hung sky,
Confetti cannons and the drummer up high.
I don't know his name and I don't need to know it,
Some nights you get a moment and you don't have to own it.

[pre-chorus]
Hear that low end rolling in over the hill,
Ten thousand strangers going quiet and still.
Hands up, lights out, one breath, then the drop,
Somebody count me in, I'm never gonna stop.

[chorus]
It's festival season, and we're not going home,
Glitter in the mud and my voice is gone.
Sing it with the stranger on your left and your right,
We came for the weekend, we're staying for the light.
It's festival season, and the field's on fire,
Every flag's a friend and every song's a choir.
Hands up high, it's festival season,
And we're not going home, no, we're not going home.

[post-chorus]
Not going home, not going home,
Oh oh, oh oh oh, we're not going home.
Not going home, not going home,
Oh oh, oh oh oh, we're not going home.

[instrumental]

[bridge]
Four a.m., the main stage dark, the small tent's still going,
Sunrise set, the sky turns pink and nobody is slowing.
My legs are gone, my voice is gone, there's glitter in my hair for weeks,
But I found a girl I really like, and she looks a lot like me.
Monday's got a train and a desk and a boss who knows my name,
But right now I'm the girl in the field who danced through all the rain.
The sun climbs up the ferris wheel, the last DJ takes a bow,
And ten thousand people whisper, we're not going anywhere now.

[chorus]
It's festival season, and we're not going home,
The sun's coming up and my voice is gone.
Sing it with the stranger on your left and your right,
We came for the weekend, we're leaving with the light.
It's festival season, and the field's still on fire,
Every flag's a friend and every song's a choir.
Hands up high, it's festival season,
And we're not going home, no, we're not going home.

[post-chorus]
Not going home, not going home,
Oh oh, oh oh oh, we're not going home.
Not going home, not going home,
Oh oh, oh oh oh, we're not going home.

[outro]
Sunday, tent down, mud on my knees,
Wristband stays on till it falls off me.
Bus back to the city with my head on the glass,
Still hear the drop, still feel the bass.
Same field next year, same crew, same song,
It's festival season, and we're not going home.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 748 at 140 wpm → ~5.3 min, 89% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2261 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
