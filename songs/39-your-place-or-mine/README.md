# Your Place or Mine

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirty-ninth song. Female lead **Mahima** with a male rap feature (Singer B)
after the instrumental — house-pop / piano house, 122 BPM, F minor, **UK
register** throughout. Uptempo class, so it carries a `render.json`. Same
singer as songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock. A London rapper added as Singer B with a section-by-section `Duet Structure`. 122 BPM, F minor, no key change; stabbed piano house chords, rolling sub-bass, pitched vocal chops, and the drizzle, cab-idle, coin-spin and kettle textures. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 81 entries — from the submission's scene direction, with a two-look character bible, Kai at the taxi rank, a rear-view-mirror-only driver, the coin motif, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 39-your-place-or-mine
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\39-your-place-or-mine\caption.txt `
  --lyrics-file songs\39-your-place-or-mine\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\39-your-place-or-mine\output\your_place_or_mine.wav
```

Expected ~2 h.

## Pacing is estimated, not measured

Uptempo song, same open question as song 8. The lyrics are **754 words**.
What that means at different pacings against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 125 wpm | 6.0 min | **overrun** |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 160 wpm | 4.7 min | 79% |
| 180 wpm | 4.2 min | 70% |

The two post-chorus chants are near-spoken and will run very fast, and the
male rap verse (109 of the 754 words) at 122 BPM in a dry London flow is
typically 160–190 wpm; a blended estimate is 145–155 wpm, landing near 5.1
minutes. The guard is set at a deliberately conservative 140. **If the first
render truncates the outro, drop the second post-chorus (28 words, a repeat)
and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the dialogue lines (*"the Tube's shut,"* *"where you heading,"* *"drive,"* *"you're negotiating,"* *"cute,"* *"seriously though,"* *"get lost"*) | Punctuation is not sung; a quoted phrase can be read as a break in the line |
| The question mark in the hook — *"Your place or mine?"* → *"Your place or mine,"* | The hook runs straight into *either way, you're mine tonight*; a question mark there invites the model to lift the phrase and break the line |
| Descriptive tag lines — `[intro – close, amused, over the filtered piano loop]`, `[chorus – big, sunny, piano house drop]`, `[post-chorus – chant]`, `[bridge – stripped to one piano chord, the coin in the air]`, `[outro – piano only, morning]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[rap verse – male feature, Singer B]` → `[verse]`, `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | There is no `[rap]` tag; the male feature is carried by the caption's `Duet Structure` line instead |
| The two `(repeat)` markers — the second chorus and the second post-chorus — written out in full | The verify script flags them and the model would sing the word |

Kept exactly as written: every lyric line, 122 BPM, F minor, the UK register
and its London detail, the instrumentation, the mood arc, the six viral
moments. The lyric body already spelled its numbers as words (*four in the
morning*, *half past two*), so no digit cleanup was needed, and 754 words
fits the uptempo budget.

## The story and the hooks

Lights up, last tune, the bouncer calling time, and he is stood behind her
in the coat-check queue. Four in the morning on a London corner, the chicken
shop glowing like a chapel, the Tube shut, the taxi rank a crowd. She plays
the whole thing as a negotiation she has already won: two doors in this
city, and one of them is the answer, so he can pick the postcode and she
will pick everything after. In the black cab they trade terms — his flatmate
is in, hers is out, but he has a rooftop in Peckham with the whole skyline
for free. The male feature answers from the rank and cheerfully concedes: he
had a line rehearsed and lost it at the door, and he would row across the
Thames in a bin bag in this weather. Then the bridge takes the game away —
the coin goes up, she catches it and covers it and never looks, because it
was never the postcode and never the door. It is who is making tea in the
morning. The outro is her kitchen, the kettle on, his jacket on her chair,
sun through the blinds.

**The hook:** *"Your place or mine, either way, you're mine tonight."*

**The line for captions:** *"You can pick the postcode, I'll be picking
everything after."*

**The rap clip:** *"I'd row across the Thames in a bin bag in this
weather."*

**The turn:** *"It was never the postcode, it was never the door, / It's
who's making tea in the morning, and I know that's you, for sure."*

**The chant:** the post-chorus — *"Your place, my place, your place, my
place"* — is a point-left, point-right group move that works at a taxi rank
and in a kitchen.

**Why it can travel:** the coin flip is a one-take format anybody can film,
the chant is a dance with no choreography to learn, and the whole thing is
PG-13 — it ends with a kettle, not a bedroom.

## Lyrics as they will be sung

```
[intro]
Lights up, last tune, the bouncer's calling time,
Coat check queue and you're stood behind me in the line.
Ears still ringing with the bass from the floor,
And you're looking at me like the night wants more.

[verse]
Chicken shop glowing like a chapel on the corner,
Four in the morning and the pavement's getting warmer.
You said, the Tube's shut, and I said, I know,
You said, where you heading, I said, depends where we go.
You're proper fit but I'm not saying that out loud,
I let my eyes do the talking while the taxi rank's a crowd.
You've got that nervous little laugh when I lean in,
Boy, I've had you sorted since the second song came in.

[pre-chorus]
Don't act like this is up to you,
I made my mind up at the bar at half past two.
Two doors in this city and one of them's the answer,
You can pick the postcode, I'll be picking everything after.

[chorus]
Your place or mine, either way, you're mine tonight,
Flip a coin, heads or tails, I win on both sides.
North of the river or south of the line,
Call it a cab, call it fate, call it whatever you like,
You can tell him the street, I'll be telling him drive,
Your place or mine, either way, you're mine tonight.

[post-chorus]
Your place, my place, your place, my place,
Either way I'm getting my way.
Your place, my place, your place, my place,
Either way I'm getting my way.

[verse]
Black cab, light on, orange through the drizzle,
You're checking your phone like the answer's in a riddle.
Your flatmate's in, my flatmate's out, so that's a point to me,
But you've got a rooftop in Peckham with the whole skyline for free.
I say, you're negotiating, you say, I'm just being fair,
I say, cute, and I fix the collar on the jacket that you wear.
You say, seriously though, and I say, seriously, hun,
You've had one job all night and it's the easy one.

[pre-chorus]
Don't act like this is up to you,
I clocked you at the bar at half past two.
Two doors in this city and one of them's the answer,
You can pick the postcode, I'll be picking everything after.

[chorus]
Your place or mine, either way, you're mine tonight,
Flip a coin, heads or tails, I win on both sides.
North of the river or south of the line,
Call it a cab, call it fate, call it whatever you like,
You can tell him the street, I'll be telling him drive,
Your place or mine, either way, you're mine tonight.

[instrumental]

[verse]
Cool, cool, I'll admit it, I was done at the door,
Had a line rehearsed and I've lost it, what's it for?
You walked in like the room was a rumour you started,
Now I'm stood at the rank and the whole plan's departed.
Dalston or Brixton, honestly, whatever,
I'd row across the Thames in a bin bag in this weather.
You say mine and I'm texting my flatmate, get lost,
You say yours and I'm asking the driver what it costs.
Not even pretending that I'm the one who decides,
So flip your coin, love, heads or tails, I'll abide,
Either way, I'm the one who's yours tonight.

[bridge]
Coin's in the air and the cab's at the kerb,
Driver's got his window down, waiting on a word.
Heads is your kitchen, tails is my stairs,
And honestly I'd take the night bus as long as you're there.
I catch it, I cover it, I don't even look,
It was never the postcode, it was never the door,
It's who's making tea in the morning, and I know that's you, for sure.

[chorus]
Your place or mine, either way, you're mine tonight,
Flip a coin, heads or tails, I win on both sides.
North of the river or south of the line,
Call it a cab, call it fate, call it whatever you like,
So I tell the driver my street and you don't even try,
Your place or mine, either way, you're mine tonight.

[post-chorus]
Your place, my place, your place, my place,
Either way I'm getting my way.
Your place, my place, your place, my place,
Either way I'm getting my way.

[outro]
Kettle on, keys on the side, your jacket on my chair,
Sun coming through the blinds and look at that, you're still there.
Your place or mine, well, I suppose that's decided,
Mine, and you're mine, and I'm not even trying to hide it.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 754 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2682 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
