# Power Back On

**Status: written and verified, NOT rendered. Not yet in the queue — queue after song 7.**

Eighth song. **Female + male duet with rap** — Mahima on the melodic lead,
a male rapper on the verses — cinematic trap-pop / motivational hip-hop with
a stadium-rock chorus. 136 BPM, the first uptempo song in the catalogue.
Same singer as songs 1–7 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction exactly as
submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1; a rapper added as Singer B with a section-by-section duet structure. 136 BPM, E minor lifting toward G, the full production list and the electrical-hum / heartbeat / breathing textures. |
| [`render.json`](render.json) | **New:** per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 123 entries — from the submission's direction, with a two-lead character bible, the light-only-increases rule, mini-story extras, OpenPose guidance for every exercise, and the four edit-ready cuts |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 08-power-back-on
```

Expected ~2 h.

## Two things to know before rendering

**1. Pacing is unmeasured, and it's the only real risk here.** Every song so
far has been a ballad at 92–98 BPM, singing at 116–153 words per minute. This
one is 136 BPM with two rap verses, which will pace far faster — but by how
much is a guess until it renders. The lyrics are 781 words. What that means
at different pacings against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.7 min | **overrun — outro lost** |
| 125 wpm | 6.3 min | **overrun** |
| **140 wpm (the guard setting)** | 5.6 min | 93% |
| 160 wpm | 4.9 min | 81% |
| 180 wpm | 4.3 min | 72% |

A rap verse at 136 BPM is typically 180–220 wpm, and the two rap verses are
219 of the 781 words; the chant sections are fast too. A reasonable blended
estimate is 150–160 wpm, which lands around 5 minutes. The guard is set at a
deliberately conservative 140. **If the first render truncates the outro,
the fix is to drop the second post-chorus (14 words, a repeat) and
re-render.** The measured pacing goes into `docs/VOICE_RECIPE.md` either way.

**2. It's a duet with rap, and the model has no per-line singer control.**
Same situation as song 4: the split lives in the caption's `Duet Structure`
line, and the model follows it loosely. Song 4's result is still unverified
by ear. Expect the choruses as two voices; expect the rap verses to be the
real test — a gritty male rap is a bigger ask of this model than a male
harmony. Treat the render as an experiment.

## What changed from the submission

| Change | Why |
|---|---|
| All performance directions — *(Low electrical hum…)*, **Female, whispered:**, **Male rap:**, *(16–32 bars…)* etc. — moved out of the lyric body into the caption | The model sings the lyric body literally |
| `[rap]` → `[verse]`; `[final chorus]` → `[chorus]`; the final "Repeat chant" → a second `[post-chorus]`; the male ad-libs placed as two lines inside the final chorus | Only the checkpoint's documented tags exist; ad-libs can't be layered over a chorus, so they're sung as lines within it |
| Quotation marks and em-dashes removed | Punctuation is not sung |

Kept exactly as written: every lyric line, 136 BPM, E minor with the lift
to G, the production list, the energy arc, the four viral moments.

## The story and the hooks

Two people enter a dead power station before dawn — she with a broken neon
sign, he with a rusted key. Every rep, sprint and slam switches something
on: a lamp, a floor, a city block. The generator fires on the chorus drop,
the roof opens on *"I become the dawn,"* they pull the main lever together,
and run out into a city that's alive. Then the bridge on the rooftop, no
gym, no pressure: *"You don't have to be fearless, you just have to move
your feet."*

**The hook:** *"Power back on, power back on / I was down, but I was never
gone."*

**The chant:** *"Not done. Not done. / Still here. Still strong."*

**The rap clip:** *"I don't chase perfect, I chase progress / Small wins
stack till they look like a process."*

**The quote:** *"You don't have to be fearless, you just have to move your
feet."*

**Why it can travel:** it's built for gym, running and comeback edits at a
tempo those edits actually use, and the message is move-first rather than
beat-someone.

## Lyrics as they will be sung

```
[intro]
City went quiet, lights went thin,
I heard my own heart booting again.
No rescue. No shortcut.
Just one more breath,
Power back on.

[verse]
Came in with the weight of a week on my chest,
No sleep, no peace, still I showed up dressed.
World said, slow down, doubt said, sit down,
I put both feet on the ground, said, watch this now.
No silver spoon, no perfect plan,
Just scars on my hands and a fire I understand.
Every bad day got a lesson inside,
Every closed door taught me how to build my side.
I was running on empty, but empty ain't done,
Battery low, still I'm chasing the sun.
They only see the glow when the whole thing's lit,
They never see the dark where you learn not to quit.

[verse]
I used to wait for the perfect day,
For all my fear to fade away.
But the mirror said, girl, you're still here,
So I tied my hair and faced the year.
I had a storm behind my eyes,
A hundred reasons to compromise.
Then I learned that strength is quiet too,
It starts when nobody's clapping for you.
One step, one breath, one more round,
I found my rhythm in the underground.
No crown, no crowd, no finish line,
Just me becoming more than mine.

[pre-chorus]
Feel that pulse beneath the pain,
That's not weakness, that's your name.
If the night says, you can't go on,
Turn your hurt into a power song.
Breathe in. Lock in. Rise up.

[chorus]
Power back on, power back on,
I was down, but I was never gone.
Turn the pressure into pulse,
Turn the fear into muscle.
I don't need luck, I don't need saving,
I've got a heart that keeps creating.
Power back on, power back on,
When the world goes dark, I become the dawn.
One more rep, one more run,
Power back on, I'm not done.

[post-chorus]
Not done. Not done.
Still here. Still strong.
Power back on.
Power back on.

[verse]
No fake flex, I got proof in the pace,
Every time I lost, I rebuilt the base.
No someday talk, I'm here right now,
Sweat on the floor, got dirt on my crown.
This for the kid who got laughed out the room,
For the girl who was told she was taking up room,
For the one who got tired but never got weak,
For the voice in your head that you're learning to beat.
I don't chase perfect, I chase progress,
Small wins stack till they look like a process.
Mind on calm, but the engine on loud,
I don't need a stage, I can light up a crowd.

[verse]
I don't need to outrun my past,
I let it teach me how to last.
Every version that broke before
Built the girl who walks through this door.
I can rest without giving in,
I can heal and still want to win.
Soft heart, strong mind, steady feet,
Peace in my head with a fire in my beat.

[pre-chorus]
(repeat)

[chorus]
(repeat)

[instrumental]

[bridge]
If today is all you can carry,
Carry today and let it be.
You don't have to be fearless,
You just have to move your feet.
You can pause. You can breathe. You can start again.
The strongest thing you'll ever do
Is believe you're not at the end.
We don't break, we bend, then grow.
We don't wait, we make the road.

[chorus]
Power back on, power back on,
I was down, but I was never gone.
Turn the pressure into pulse,
Turn the fear into muscle.
I don't need luck, I don't need saving,
I've got a heart that keeps creating.
No quit! No fear! New day, new gear!
Stand tall, breathe deep, your future starts here!
Power back on, power back on,
When the world goes dark, I become the dawn.
One more rep, one more run,
Power back on, I'm not done.

[post-chorus]
Not done. Not done.
Still here. Still strong.
Power back on.
Power back on.

[outro]
I was down,
But I was never gone.
Take your time.
Then turn your power back on.
Power back on.
Power back on.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 781 at 140 wpm → ~5.6 min, 93% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2476 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
