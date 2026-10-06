# Rooftop Radio

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty-three. Female lead **Mahima**, disco-pop with a live string
section, 120 BPM, B♭ major lifting to C for the final chorus, uptempo pacing.
Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 760 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 120 BPM, B♭ major, funk guitar and octave disco bass, live strings as the second hook, the radio-band filter sweep in the instrumental break. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo, so the ballad default would misread the length |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 83 entries — with a two-look character bible, the neighbour, the no-male-lead rule, the light-only-moves-forward rule, workflow, the freeze challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 43-rooftop-radio
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\43-rooftop-radio\caption.txt `
  --lyrics-file songs\43-rooftop-radio\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\43-rooftop-radio\output\rooftop_radio.wav
```

Expected ~2 h.

## Pacing warning

This is an uptempo song and its length is an estimate, not a measurement.
The ballads in this catalogue sang at 116–153 words per minute; a 120 BPM
disco-pop record with a chanted post-chorus will pace faster than any of
them, but by how much is unknown until it renders. At 760 sung words:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.6 min | **overrun — outro lost** |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 155 wpm | 4.9 min | 82% |

The guard in `render.json` is a deliberately conservative 140. **If the first
render truncates the outro, drop the second post-chorus (twenty-eight words,
a repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads the body literally |
| Digits spelled as words (*six flights*, *fourth floor*, *on three, on two*) | The model sings digits unpredictably |
| Descriptive tag lines (*[verse 1 — funk guitar, bass, tambourine]*) reduced to plain `[verse]` etc. | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses and post-choruses written out in full instead of *(repeat)* | The model would sing the word |
| Performance and production notes (radio-band filter, string glissando, crowd bed) moved into the caption | Stage directions in the lyric body get sung |

Kept exactly as written: every lyric line, 120 BPM, B♭ major with the whole-step
lift, the instrumentation, the one-location structure and the mood arc.

## The story and the hooks

Six flights up, on the roof of a walk-up building whose landlord is away for
the month, one old silver radio on an upturned crate turns into a block
party. A cooler comes up the stairs, folding chairs open, fairy lights go on
the water tank. The antenna gets wrapped in foil and pointed at the moon, and
when the station finally lands the whole roof moves. The third-floor
neighbour leans out to complain, hears the chorus, and comes up with a plate
and a paper fan to show everyone how the step actually goes. A patrol car
slows, looks, and drives on. By the last chorus every window on the street is
open, and by dawn there is nobody left but a sleeping woman in a folding
chair and a radio running out of batteries.

**The hook:** *"Rooftop radio, turn it up, let the whole block know"* — a
title you can shout, on a downbeat, with a physical action attached to it.

**The line for captions:** *"We got no permit and we got nowhere else to go."*

**The chant:** *"Turn it up, turn it up, till the batteries go."*

**The turn:** *"None of us own a window with a view / We split a rent that we
can barely do / But nobody lives above the sixth floor sky."*

**Why it can travel:** the freeze in the pre-chorus is a ready-made group
clip, the chorus is one line and one gesture, and the neighbour who came to
complain and stayed to dance is the emotional beat that makes a party song
worth reposting.

## Lyrics as they will be sung

```
[intro]
Six flights up with a radio under my arm,
Tar still soft from the heat of the day.
Somebody propped the hatch with an empty paint can,
And the whole sky opened up our way.
Nobody called it, nobody planned it,
It just started playing and we stayed.

[verse]
Landlord's gone to Miami till the end of July,
Nobody up here's asking who's allowed tonight.
A fresh pack of batteries, a dial that sticks,
One old silver radio and a hundred feet of bricks.
Girl from the fourth floor hauled a cooler up the stairs,
Somebody's cousin showed up with a stack of folding chairs.
We swept the broken glass and strung a line of lights,
And the water tank's a stage if you can climb it right.

[pre-chorus]
Antenna wrapped in foil and pointed at the moon,
Hold it still, hold it still, there it is, that's the tune.
Everybody freeze, then everybody move,
On three, on two,

[chorus]
Rooftop radio, turn it up, let the whole block know,
We got no permit and we got nowhere else to go.
Antenna in the air like a hand in the air,
And the city's looking up at us like we put it there.
Rooftop radio, turn it up, let the whole block know,
Everybody dancing on a roof that isn't ours,
Half the song is static and we sing the rest out loud,
Six flights over Sunday, and tonight we are the sound.

[post-chorus]
Turn it up, turn it up, let the whole block know,
Turn it up, turn it up, till the batteries go.
Hands on the water tank and feet down on the tar,
Turn it up, turn it up, that's how loud we are.

[verse]
The lady on the third floor leaned out to complain,
Then she caught the chorus and she asked us for a name.
Now she's up here with a plate and a folding paper fan,
Saying she danced to this one back before the block began.
The guy from the corner store brought ice up in a crate,
Two kids from the stairwell swore they'd only stay till eight.
At midnight the dial slipped and found a song from way back when,
And nobody knew how, but every one of us came in.

[pre-chorus]
A squad car turned the corner, slowed down and drove away,
Somebody's grandmother is teaching me to sway.
Everybody freeze, then everybody move,
On three, on two,

[chorus]
Rooftop radio, turn it up, let the whole block know,
We got no permit and we got nowhere else to go.
Antenna in the air like a hand in the air,
And the city's looking up at us like we put it there.
Rooftop radio, turn it up, let the whole block know,
Everybody dancing on a roof that isn't ours,
Half the song is static and we sing the rest out loud,
Six flights over Sunday, and tonight we are the sound.

[post-chorus]
Turn it up, turn it up, let the whole block know,
Turn it up, turn it up, till the batteries go.
Hands on the water tank and feet down on the tar,
Turn it up, turn it up, that's how loud we are.

[instrumental]

[bridge]
None of us own a window with a view,
We split a rent that we can barely do.
But nobody lives above the sixth floor sky,
And nobody's charging extra for the night.
So play it for the ones who worked all week,
Play it for the ones who couldn't sleep,
Play it till the tar goes cool and the east turns gold,
Play it till the batteries go cold.

[chorus]
Rooftop radio, turn it up, let the whole block know,
We got no permit and we got nowhere else to go.
Antenna in the air like a hand in the air,
And the city's looking up at us like we put it there.
Rooftop radio, turn it up, let the whole block know,
Every window on the street is open now,
Half the song is static and we sing the rest out loud,
Six flights over Sunday, and tonight we are the sound.

[post-chorus]
Turn it up, turn it up, let the whole block know,
Turn it up, turn it up, till the batteries go.
Hands on the water tank and feet down on the tar,
Turn it up, turn it up, that's how loud we are.

[outro]
Sun coming up behind the tank and the wires,
Somebody's asleep in a folding chair.
The radio is still going on the last of the batteries,
And the whole block knows, and the whole block knows.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 760 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2292 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
