# Dance Like Nobody's Sober

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song thirty-six. Female lead **Mahima**, party pop with a live-band wedding-
reception energy — big supersaw synths, brass stabs, handclaps and a whole-
room gang vocal — US register. 126 BPM, D major, uptempo pacing. Same singer
as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 748 sung words, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 126 BPM, D major, the gang-vocal lifecycle, the beatless piano bridge and the hard drop before it. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 83 entries — with a one-look character bible, a recurring grandmother, a named cast of wedding guests, the crowd-layering workflow note and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 36-dance-like-nobodys-sober
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\36-dance-like-nobodys-sober\caption.txt `
  --lyrics-file songs\36-dance-like-nobodys-sober\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\36-dance-like-nobodys-sober\output\dance_like_nobodys_sober.wav
```

Expected ~2 h.

## Pacing warning

**This is an uptempo song and its pacing is unmeasured.** Ballads on this
setup measured 116–153 words per minute; at 126 BPM with a chant post-chorus
repeated three times this will sing considerably faster, but by how much is a
guess until it renders. The lyrics are 748 words. Against the model's
six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| 130 wpm | 5.8 min | 96% |
| **140 wpm (the guard setting)** | 5.3 min | 89% |
| 155 wpm | 4.8 min | 80% |
| 170 wpm | 4.4 min | 73% |

The three post-chorus chants are 60 of the 748 words and will pace fastest of
anything here; a blended estimate of 145–155 wpm is reasonable, landing near
five minutes. The guard is set at a deliberately conservative 140. **If the
first render truncates the outro, the fix is to drop the third post-chorus
(20 words, a verbatim repeat) and re-render.** The measured pacing goes into
`docs/VOICE_RECIPE.md` either way.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | Punctuation is not sung; the model reads the lyric body literally |
| Digits spelled as words (*eleven minutes*, *seventeen*, *table nine*, *half past one*, *half five*) | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – filtered kick…]`, `[chorus – whole-room gang vocal]`, `[post-chorus – shouted chant]`, `[verse 2]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| Every repeated section written out in full — both pre-choruses, all three choruses, all three post-choruses | `(repeat)` would be sung as the word |
| The gang-vocal, shout and beatless-bridge directions moved into the caption | Stage directions in the body get sung |

Kept exactly as written: every lyric line, 126 BPM, D major, the
instrumentation, the mood arc, the bridge turn.

## The story and the hooks

Eleven at night, a reception hall, string lights over the parking lot. The
best man ran eleven minutes over, there is a napkin in the punch bowl, table
nine has given up on sitting down and the kids in socks are skidding the
length of the parquet. Her shoes are in a plant pot and she is not going back
for them. Verse two stops cataloguing and starts naming: the bride with her
dress hitched, her mother on the floor and her father filming from a chair,
two aunties who have not spoken since a funeral in June holding both hands
and howling the same chorus, the waiters giving in, and somebody's
grandmother at the front of the conga line. Then half past one, the room goes
soft for a beat, there is a kid asleep on a mountain of coats, and she works
out why the night matters: this exact room will not happen twice. So she
takes the nearest hand and puts it back in the air.

**The hook:** *"Dance like nobody's sober, sing like nobody's home"* — first
and fifth line of every chorus, with the title closing it too.

**The chant:** *"Left foot, wrong foot, doesn't matter, doesn't matter."*

**The line for captions:** *"This exact room will not happen twice."*

**The turn:** *"And I look at every face that I grew up beside / And I know
that this exact room will not happen twice."*

**Why it can travel:** it is a wedding record that is genuinely funny in the
verses and genuinely moving in the bridge, and the funny parts are true
rather than written as jokes. Every family has table nine, the uncle, and the
grandmother who leads the conga line. The chant is a three-second vertical
edit on its own.

## Lyrics as they will be sung

```
[intro]
String lights over the parking lot, band's loading in,
Somebody's grandma's already three glasses in.
The DJ says, one more, and the whole room roars,
And a hundred pairs of shoes hit the floor.

[verse]
There's a napkin in the punch bowl and a fork on the floor,
The best man ran eleven minutes, then he ran some more.
Cousins from three time zones that nobody has seen
Since the summer that we all turned seventeen.
Table nine has given up on ever sitting down,
And the kids in socks go skidding past the sound.
My shoes are in a plant pot and I'm leaving them right there,
There's frosting on my elbow and I'm past the point of care.
Somebody's uncle does the shoulder thing he does,
And the whole room comes apart, and I'm in love with us.

[pre-chorus]
The DJ takes a request from a woman in a hat,
Plays it twice in a row and nobody minds that.
Bass in the folding chairs, the ceiling's coming loose,
Grab a hand, any hand, we've got nothing left to lose.

[chorus]
Dance like nobody's sober, sing like nobody's home,
Left foot, wrong foot, doesn't matter, it's our own.
Hands up, ceiling down, throw the whole night over,
Nobody's watching, and nobody's sober.
Dance like nobody's sober, sing like nobody's home,
Every song's our song when the speakers get blown.
Turn it up, hold on, this is what we came for,
Dance like nobody's sober till they throw us out the door.

[post-chorus]
Left foot, wrong foot, doesn't matter, doesn't matter,
Left foot, wrong foot, let the whole floor shatter.
Left foot, wrong foot, doesn't matter, doesn't matter,
Dance like nobody's sober, and nobody's sober.

[verse]
The bride has got her dress hitched up above her knees,
Her mother's on the floor and her father's on his feet.
Two aunties who have not spoken since a funeral in June
Are holding both hands, screaming out the same tune.
The groom has lost his jacket and I think he's lost a shoe,
The photographer gave up an hour or two ago too.
There's a cousin on a chair who should not be on a chair,
And a conga line has started and I don't know where.
The waiters have stopped pretending, they are in it now,
And somebody's grandma's leading it, don't ask me how.

[pre-chorus]
The DJ's taking requests from a queue outside the booth,
The bride says, play it one more time, and that's the truth.
Bass in the folding chairs, the ceiling's coming loose,
Grab a hand, any hand, we've got nothing left to lose.

[chorus]
Dance like nobody's sober, sing like nobody's home,
Left foot, wrong foot, doesn't matter, it's our own.
Hands up, ceiling down, throw the whole night over,
Nobody's watching, and nobody's sober.
Dance like nobody's sober, sing like nobody's home,
Every song's our song when the speakers get blown.
Turn it up, hold on, this is what we came for,
Dance like nobody's sober till they throw us out the door.

[post-chorus]
Left foot, wrong foot, doesn't matter, doesn't matter,
Left foot, wrong foot, let the whole floor shatter.
Left foot, wrong foot, doesn't matter, doesn't matter,
Dance like nobody's sober, and nobody's sober.

[instrumental]

[bridge]
Half past one, and the room goes soft for a beat,
There's a kid asleep on a mountain of coats by our feet.
And I look at every face that I grew up beside,
And I know that this exact room will not happen twice.
So I take the nearest hand and I lift it in the air,
While the song is still playing and the floor is still there.

[chorus]
Dance like nobody's sober, sing like nobody's home,
Left foot, wrong foot, doesn't matter, it's our own.
Hands up, lights up, last ones on the floor,
Nobody's leaving, and nobody's sober.
Dance like nobody's sober, sing like nobody's home,
Every song's our song and the speakers have blown.
Turn it up, hold on, this is what we came for,
Dance like nobody's sober till they throw us out the door.

[post-chorus]
Left foot, wrong foot, doesn't matter, doesn't matter,
Left foot, wrong foot, let the whole floor shatter.
Left foot, wrong foot, doesn't matter, doesn't matter,
Dance like nobody's sober, and nobody's sober.

[outro]
Car park, half five, and the sky is going grey,
Shoes in one hand, cake in a napkin, on our way.
Somebody starts the chorus in the taxi line once more,
Dance like nobody's sober till they throw us out the door.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 748 at 140 wpm → ~5.3 min, 89% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2310 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
