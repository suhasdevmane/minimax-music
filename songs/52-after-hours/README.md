# After Hours

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty-two. Female lead **Mahima** with a male MC feature — UK garage /
two-step with organ stabs, chopped vocal science and a London MC hosting the
third verse. 132 BPM, C minor, uptempo, UK register. Same singer as songs
1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 753 sung words |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1; the MC added as Singer B with a section-by-section duet structure. 132 BPM, C minor, two-step drums, sub-bass, organ stabs, vocal chops and the kettle/bin-lorry/shutter ambience. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 89 entries — with a two-look bible for Mahima, the MC as the host, the light-runs-one-way rule, the trembling-glass and shop-shutter motifs, composited-UI note and a QC checklist |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 52-after-hours
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\52-after-hours\caption.txt `
  --lyrics-file songs\52-after-hours\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\52-after-hours\output\after_hours.wav
```

Expected ~2 h.

## Pacing note

This is an uptempo song and pacing is a guess until it renders. The lyrics
are 753 words, and the MC verse is a spoken hundred of them. Against the
model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 125 wpm | 6.0 min | **at the cap** |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 155 wpm | 4.9 min | 81% |

Two-step top lines and a spoken MC verse both run well above 140, so the
guard is deliberately conservative. **If the first render truncates the
outro, drop the second post-chorus (twenty words, a repeat) and re-render.**

The MC feature is the other risk: as with songs 4 and 8, the model has no
per-line singer control, so the split lives entirely in the caption's
`Duet Structure` line and will be followed loosely. Expect the choruses to
land; treat the spoken verse as the experiment.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung |
| Digits spelled as words (*half four*, *two stops*, *two flights*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – no drums, strip-light hum]*, *[MC verse – stripped beat]*) reduced to plain tags | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| `[MC verse]` written as a plain `[verse]` after the instrumental | There is no rap tag; the feature is described in the caption instead |
| Repeated choruses, pre-choruses and the post-chorus written out in full | The model would sing a repeat marker |

Kept exactly as written: every lyric line, 132 BPM, C minor, the two-step
arrangement, the UK register, the shutter bookend, the viral moments.

## The story and the hooks

The club puts its strip lights on and nobody wants their own bed. Somebody's
sister has a flat two stops away, two floors above a fryer, up a stairwell
whose light has been broken since the year before last. The big light goes
off, one lamp goes on, the coats go on the bed, and by half four a mate on
the floor is saying his dad has been ill since the spring and a girl in the
doorway is reading out her resignation to nine people who cheer. The man
whose flat it is makes four teas at once and clocks who is going to break
before he even walks. Then a balcony, a bin lorry, a fox, and a sky that has
gone grey and gold. The video ends where it began, on flat honest light —
except now it suits her.

**The hook:** *"After hours, that's when the night gets honest."*

**The line for captions:** *"Nothing happened here, and it's the truest
thing I knew."*

**The chant:** *"Four in the morning, four in the morning / Nobody's leaving
without saying something."*

**The MC clip:** *"Four in the morning is a country of its own / Passport is
a mug of tea, and nobody goes home."*

**The turn:** the party never gets bigger. It gets quieter, and that is the
lift.

**Why it can travel:** everybody has been in that flat. The hook is a thesis
you can put over any four-a.m. clip, the chant is four words, and the
big-light-off switch is a one-frame edit anyone can copy.

## Lyrics as they will be sung

```
[intro]
Strip lights up and the music is gone,
Doorman counting us out one by one.
Everybody's got a bed and nobody wants it,
Somebody's got a key in their pocket,
So the night is only halfway done.

[verse]
Out on the pavement and my ears are still ringing,
Lost the cloakroom ticket and my mate is still singing.
Somebody says, my sister's flat, it's two stops on the bus,
So we're up on the top deck with the windows full of us.
Past the shutter coming down and the fella with the mop,
Two flights up above the fryers where the smell doesn't stop.
The hallway light's been broken since the year before last,
So we're going up on phone torch and we're going up fast.

[pre-chorus]
Big light off and the little lamp on,
Somebody's playing an old garage song.
The coats are all piled on the end of the bed,
And the truth gets a chair and it sits down instead.

[chorus]
After hours, that's when the night gets honest,
Nobody's posing and nobody's promised.
Kettle going and the bassline low,
Say the thing that you couldn't say downstairs, then let it go.
After hours, when the shutters come down,
Half a flat, half a city, one sound,
You can tell me anything, I'm not going home,
After hours, that's when the night gets honest.

[post-chorus]
Four in the morning, four in the morning,
Nobody's leaving without saying something.
Four in the morning, four in the morning,
That's when the night gets honest.

[verse]
Half four and the tunes have gone soft and gone slow,
And my mate on the floor says a thing I didn't know.
Says his dad's been ill since the spring and he kept it in,
Says he couldn't say it sober so he says it with a grin.
The girl in the doorway is handing in her notice,
Typing it out on her phone and reading it to all of us.
I have known this lot for years and I met them all tonight,
Everything you swallow at the bar comes up in this light.

[pre-chorus]
Big light off and the balcony door,
Somebody's crying and laughing at four.
The coats are all piled and the tea's going cold,
And nobody's leaving till somebody's told.

[chorus]
After hours, that's when the night gets honest,
Nobody's posing and nobody's promised.
Kettle going and the bassline low,
Say the thing that you couldn't say downstairs, then let it go.
After hours, when the shutters come down,
Half a flat, half a city, one sound,
You can tell me anything, I'm not going home,
After hours, that's when the night gets honest.

[instrumental]

[verse]
Two flights, one lift that has not worked since I moved in,
Coat on the radiator, kettle doing overtime, tune in.
I do the door, I do the drinks, I do the peace talks,
I clock who is going to break before he even walks.
No performance in a room this small and this warm,
You get honest when your back is on the wall by the door.
I have heard things in this kitchen that a priest would bin,
Grey light through the blind and I am the one who lets it in.
Four in the morning is a country of its own,
Passport is a mug of tea, and nobody goes home.

[bridge]
Out on the balcony the sky's gone grey and gold,
Bin lorry grinding and a fox crossing the road.
Somebody's asleep in a parka in the hall,
Somebody's playing the first tune of them all.
I will keep this hour longer than the club or the queue,
Nothing happened here, and it's the truest thing I knew.

[chorus]
After hours, that's when the night gets honest,
Nobody's posing and nobody's promised.
Kettle going and the bassline low,
Say the thing that you couldn't say downstairs, then let it go.
After hours, when the shutters come down,
Half a flat, half a city, one sound,
Sun on the tiles and the tunes running out,
Nobody's sorry and nobody's proud.
You can tell me anything, I'm not going home,
After hours, that's when the night gets honest.

[post-chorus]
Four in the morning, four in the morning,
Nobody's leaving without saying something.
Four in the morning, four in the morning,
That's when the night gets honest.

[outro]
Bus stop, daylight, jacket in my hand,
Baker's open and the shutter's going up again.
Somebody messages, same time next week,
And I'm smiling at my phone on an empty street.
After hours, that's when the night gets honest.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 753 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2541 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
