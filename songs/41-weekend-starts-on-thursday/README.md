# Weekend Starts on Thursday

**Status: written and verified, NOT rendered. Not yet in the queue.**

Forty-first song. Female lead **Mahima**, dance-pop / nu-disco with a
countdown chant, office-to-rooftop, leaving-work-early energy. 124 BPM,
G major lifting to A for the last chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 124 BPM, G major with the lift, disco bass, claps, strings and brass, the ticking-clock / laptop-click / elevator-ding ear candy per the submission. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 85 entries — built from the submission's scene direction, plus a three-look character bible, Kai with the tie headband, the crew and the taxi driver, workflow, the countdown challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 41-weekend-starts-on-thursday
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\41-weekend-starts-on-thursday\caption.txt `
  --lyrics-file songs\41-weekend-starts-on-thursday\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\41-weekend-starts-on-thursday\output\weekend_starts_on_thursday.wav
```

Expected ~2 h.

## One thing to know before rendering: pacing

**Pacing is unmeasured, and it's the only real risk here.** The ballads
measured 116–153 words per minute. This one is 124 BPM dance-pop with three
countdown chants, which will pace faster — but by how much is a guess until
it renders. The lyrics are 718 words. What that means at different pacings
against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.2 min | **overrun — outro lost** |
| 125 wpm | 5.7 min | 96%, at the edge |
| **140 wpm (the guard setting)** | 5.1 min | 85% |
| 160 wpm | 4.5 min | 75% |
| 180 wpm | 4.0 min | 66% |

The countdown chants are fast and the verses are wordy, so a blended
estimate of 145–155 wpm is reasonable, landing around 4.8 minutes. The guard
is set at a deliberately conservative 140. **If the first render truncates
the outro, the fix is to drop the third post-chorus (19 words, a repeat)
and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| `4:59` → *"Four fifty-nine"* | The model sings digits unpredictably |
| `"out?"` → *out, no question mark* — the quotation marks and the question mark dropped | Punctuation is not sung; the line already says there's no question mark |
| Quotation marks and em-dashes removed; `[verse 1]`/`[verse 2]`, `[final chorus]` and the descriptive tag lines reduced to plain tags | The model sings the lyric body literally and only knows plain section tags |
| Repeated choruses, pre-choruses and post-choruses written out in full | `(repeat)` would be sung |
| The countdown post-chorus kept as sung lines (`Five, four, three, two, one`) rather than a chant direction | The model has no chant instruction; as sung words with the gang-vocal note in the caption it comes out as a chant anyway |

Kept exactly as written: every other line, 124 BPM, G major with the lift,
the instrumentation, the mood arc, the six viral moments.

## The story and the hooks

Four fifty-nine on a Thursday and the clock is stuck. One laptop shuts,
then another, then a one-word text from him, and she's swapping flats for
heels and dragging the girls into a lift full of people shouting a
countdown at the floor numbers. The doors open onto a rooftop at sunset,
first drink, glasses up. An hour later he's singing the wrong words with
his tie around his head, six of them are in a taxi built for four, and the
driver has never seen anything like it. On the last rooftop at dawn she
admits there's an alarm set for seven and a meeting she forgot, and then
the turn: it was never about the calendar, it was him. Monday finds her in
the lift in sunglasses, humming, counting down to Thursday.

**The hook:** *"Weekend starts on Thursday when I'm with you"* — a caption,
a plan, a whole personality.

**The line for captions:** *"Friday is a rumour, Saturday can wait too."*

**The chant:** *"Five, four, three, two, one / Thursday night, here we
come."*

**The turn:** *"But it was never about the calendar, never about the day /
Every hour feels like the weekend when you're looking at me that way."*

**Why it can travel:** everyone has a four fifty-nine; the countdown is a
ready-made lift-and-office challenge, the tie headband and the six-in-a-taxi
are group-chat bait, and the Monday-sunglasses outro is its own post.

## Lyrics as they will be sung

```
[intro]
Four fifty-nine and the clock is stuck,
Fluorescent lights and I'm out of luck.
Then a laptop shuts across the room,
And the whole floor starts to hum.
Somebody's phone lights up with a plan,
Somebody's already got a drink in hand.
Printer's jammed and I don't even care,
I can hear the weekend on the stairs.

[verse]
Monday was a marathon, Tuesday was a blur,
Wednesday I was talking to a plant that didn't care.
Coffee number seven going cold beside my screen,
Spreadsheet in my eyeballs, I forgot what colours mean.
Then a text from you, one word, out, no question mark,
And my heart does a drum roll like the party's about to start.
Heels under the desk, I'm swapping out my flats,
Grab my jacket, grab the girls, and we are not coming back.

[pre-chorus]
Lock the screen, kill the lights, let the inbox wait,
Everybody grab a hand, we are not gonna be late.
Elevator going down, counting every floor,
Ten, nine, eight, seven, we're already out the door.

[chorus]
Weekend starts on Thursday when I'm with you,
Friday is a rumour, Saturday can wait too.
First drink on the rooftop, sunset bleeding through,
Weekend starts on Thursday when I'm with you.
Tell the boss I'm sorry, tell the week we're through,
Clocking out my worries, got better things to do.
Glasses up, glasses up, one more for the crew,
Weekend starts on Thursday when I'm with you.

[post-chorus]
Five, four, three, two, one,
Thursday night, here we come.
Five, four, three, two, one,
The week is done, the week is done.

[verse]
Rooftop bar and the speakers play a song from when we were seventeen,
You know every word, you sing it wrong, it's the best thing I have ever seen.
Somebody ordered the sharing plate, nobody's sharing, it's a war,
Your tie is now a headband and I'm not sure what the tie was for.
Taxi waiting with the meter on, six of us in a car for four,
Driver says he's seen it all, then he says he hasn't seen this before.
Neon on your cheekbones, my mascara's holding on for dear life,
This is the night we'll be quoting back every time that Monday picks a fight.

[pre-chorus]
Lock the screen, kill the lights, let the inbox wait,
Everybody grab a hand, we are not gonna be late.
Next stop is downtown, driver, drop us at the door,
Ten, nine, eight, seven, we're already wanting more.

[chorus]
Weekend starts on Thursday when I'm with you,
Friday is a rumour, Saturday can wait too.
First drink on the rooftop, sunset bleeding through,
Weekend starts on Thursday when I'm with you.
Tell the boss I'm sorry, tell the week we're through,
Clocking out my worries, got better things to do.
Glasses up, glasses up, one more for the crew,
Weekend starts on Thursday when I'm with you.

[post-chorus]
Five, four, three, two, one,
Thursday night, here we come.
Five, four, three, two, one,
The week is done, the week is done.

[instrumental]

[bridge]
There's an alarm set for seven, there's a meeting I forgot,
There's a version of tomorrow where I'm paying for this a lot.
But it was never about the calendar, never about the day,
Every hour feels like the weekend when you're looking at me that way.
So I'll take the Monday headache, I'll take the Tuesday blues,
As long as every Thursday is a Thursday spent with you.
The week can have my mornings, it can have my nine to five,
But the nights belong to us and that's the part where I'm alive.

[chorus]
Weekend starts on Thursday when I'm with you,
Friday is a rumour, Saturday can wait too.
Last dance on the rooftop, morning coming through,
Weekend starts on Thursday when I'm with you.
Tell the boss I'm sorry, tell the week we're through,
Clocking out my worries, got better things to do.
Glasses up, glasses up, one more for the crew,
Weekend starts on Thursday when I'm with you.

[post-chorus]
Five, four, three, two, one,
Thursday night, here we come.
Five, four, three, two, one,
The week is done, the week is done.

[outro]
Monday's gonna find me with my sunglasses on,
Humming in the elevator, playing this song.
Counting down the hours, counting down to you,
Weekend starts on Thursday, and Thursday starts with you.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 718 at 140 wpm → ~5.1 min, 85% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2385 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
