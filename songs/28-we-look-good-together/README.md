# We Look Good Together

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-eighth song. **Female + male duet** — Mahima and Kai trading the hook
line for line — modern funk-pop on slap bass, wah guitar and a three-piece
brass section, US register. 116 BPM, E minor, mid pacing. Same singer as songs
1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock — with Singer B added as `Duet Partner` and a section-by-section `Duet Structure`. 116 BPM, E minor, slap bass as the lead instrument, a brass stack per chorus, and a brass-free Rhodes bridge. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 72 entries — with two looks each for Mahima and Kai, a faceless ex, the reflection motif, the reflections-are-composited rule and the three-plate crosswalk outfit transition |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 116 BPM this sits inside the mid-tempo class and the
verify script's 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 28-we-look-good-together
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\28-we-look-good-together\caption.txt `
  --lyrics-file songs\28-we-look-good-together\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\28-we-look-good-together\output\we_look_good_together.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"absolutely not"* removed; em-dashes replaced with commas | Punctuation is not sung |
| Digits spelled out: *one, two*, *a quarter past one* | The model sings digits unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines (*"slap bass and hi-hat, both voices"*, *"no brass, Rhodes and clean guitar"*) reduced to plain tags | Only the checkpoint's documented tags exist; anything else on a tag line is dropped or sung |
| Every repeated chorus and pre-chorus written out in full | The verify script flags parentheses-only lines, and the model would sing *"repeat"* |
| The line-by-line duet split moved out of the lyric body into the caption's `Duet Structure` line | The model has no per-line singer control |
| Fourteen words trimmed across the intro, verses, pre-choruses, bridge and outro | The submission ran to 654 sung words, over the mid-class budget |

Kept exactly as written: every lyric line, 116 BPM, E minor, the
instrumentation, the brass-stack-per-chorus lift, the brass-free bridge, and
the photo that never gets posted.

## The story and the hooks

Two people who know exactly what they look like and enjoy it out loud. Verse
one is the getting-ready hour: an hour-long argument about a jacket that both
of them win, a spin nobody asked for, and a corner shop window they use as a
mirror for the same photo every Friday. Verse two is his side of the arrival —
a doorman holding the door two beats too long, somebody's ex going quiet
mid-song, and a group at the bar copying the pose off a picture they posted.
Then the bridge takes all of it off: the good coat on the chair, flour in her
hair on a Tuesday, one flat overhead kitchen light and nobody watching. The
last chorus puts them in the rain, in flat midday sun and in an airport line
at a quarter past one, still enjoying it. The outro is a photo taken and
deliberately not posted.

**The hook:** *"Baby, we look good together, and we know it."*

**The line for captions:** *"We didn't come to the party, we're the reason it
goes."*

**The knife line:** *"But they can't get the part where you laugh at my joke,
the one that isn't funny and you laugh at it the most."*

**The turn:** *"Don't tell the internet, but I like this version more."*

**Why it can travel:** the strut is built on a crosswalk, so the
outfit-transition format is inside the video rather than bolted on; the hook
is a two-person lip-sync by design; and the bridge gives a flex song a reason
to exist, which is what stops it being a novelty.

## Lyrics as they will be sung

```
[intro]
Mirror by the door and the keys in my hand,
Green light on the corner, whole block understands.
Turn the collar up, do the thing with the shades,
Baby, look at what we made.

[verse]
I picked the jacket and you picked the shoes,
We argued for an hour and the argument was the truth.
You came out the bedroom doing that stupid little spin,
And I said, absolutely not, then I let you win.
There's a window on the corner where the light hits right,
And we take the same photo there every Friday night.
Two coffees, one straw, and a plan we didn't make,
And the afternoon's a scene we didn't have to stage.

[pre-chorus]
Count it in, one, two, hit the corner clean,
Bass in the chest and the whole street lean.
Are you ready, are you ready, don't break stride,
Chin up, shoulders back, and glide.

[chorus]
Baby, we look good together, and we know it,
Every window in the city is a stage and we show it.
Green light, gold hour, and the whole block slows,
We didn't come to the party, we're the reason it goes.
Baby, we look good together, say it with your chest,
Two of us on one sidewalk and the sidewalk is a set.
You can look, you can love it, you can put it on your screen,
Baby, we look good together, and we know it.

[verse]
Doorman did a double take and held the door too long,
Somebody's ex went quiet in the middle of a song.
You walked in like the floor was on your payroll,
And I held both the drinks and let the whole room go slow.
They can copy the fit, they can borrow the pose,
Take it frame for frame off a picture that we posted.
But they can't get the part where you laugh at my joke,
The one that isn't funny and you laugh at it the most.

[pre-chorus]
Count it in, one, two, hit the corner clean,
Bass in the chest and the whole street lean.
Are you ready, are you ready, don't break stride,
Chin up, shoulders back, and glide.

[chorus]
Baby, we look good together, and we know it,
Every window in the city is a stage and we show it.
Green light, gold hour, and the whole block slows,
We didn't come to the party, we're the reason it goes.
Baby, we look good together, say it with your chest,
Two of us on one sidewalk and the sidewalk is a set.
You can look, you can love it, you can put it on your screen,
Baby, we look good together, and we know it.

[instrumental]

[bridge]
Take the gold off, hang the good coat on the chair,
Tuesday, no filter, and there's flour in your hair.
Nobody's watching and there's nothing to prove,
And I still catch myself just looking at you.
That's when we look the best, with the lights off the floor,
Don't tell the internet, but I like this version more.

[chorus]
Baby, we look good together, and we know it,
Every window in the city is a stage and we show it.
Green light, gold hour, and the whole block slows,
We didn't come to the party, we're the reason it goes.
Baby, we look good together, in the rain, in the sun,
In the line at the airport at a quarter past one.
You can look, you can love it, you can put it on your screen,
Baby, we look good together, and we know it.

[post-chorus]
Look at us, look at us,
Every shop window agrees with us.
Look at us, look at us,
Nobody had to tell us, we just knew.

[outro]
Turn the lock, kick the shoes down the hall,
Take the picture, don't post it, this one isn't theirs.
Baby, we look good together,
And we know it.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2352 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
