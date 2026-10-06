# Fireflies and Porch Lights

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixty-second song. Female lead **Mahima**, contemporary folk-pop / Americana,
US register, 94 BPM, G major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, ballad class |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 94 BPM, G major, fingerpicked acoustic spine, mandolin and fiddle, strings from the first pre-chorus, porch ambience throughout. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a three-age character bible, Kai as the boy across the fence, the three matched cranes, the fireflies-in-post rule, workflow, the leave-the-light-on challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 62-fireflies-and-porch-lights
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\62-fireflies-and-porch-lights\caption.txt `
  --lyrics-file songs\62-fireflies-and-porch-lights\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\62-fireflies-and-porch-lights\output\fireflies_and_porch_lights.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads em-dashes unpredictably |
| Every number spelled as a word — *six holes*, *half past eight*, *ten more minutes*, *fourteen*, *at nine* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro — porch ambience, one guitar, no drums]`, `[verse 1]`, `[final chorus]`) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the documented plain tags exist; anything else is dropped or sung |
| Every repeated chorus written out in full rather than marked as a repeat | A repeat marker would be sung as a lyric |
| Performance directions (the drumless intro, the half-time bridge, the bass dropping out for two lines in verse two) moved into `caption.txt` | The model sings the lyric body literally |
| Two lines shortened by one word each | The submission came in at 642 words, two over the ballad cap; the trims are in the bridge and the last line of verse two and change no image |

Kept exactly as written: every other lyric line, 94 BPM, G major, the
instrumentation, the two-porch video concept and the mood arc.

## The story and the hooks

A jar with six nail-punched holes, a low chain-link fence, and a boy from two
houses down who came over at half past eight every night the summer they were
fourteen. Her mother counting ten more minutes through the screen. Then the
last August: he is taller and driving, she has a summer job, and they sit a
foot apart on the same steps and do not say anything. He kisses her at the
gate, his father's truck is already roped down at the curb, and she lets the
last firefly out of the jar and stands in the yard until there is nothing
left to see. The turn is the bridge, years on: her own porch, her own bulb
left on out of habit, and two kids cutting across her lawn with a jar of
their own. She does not stop them. That is what a porch light is for.

**The hook:** *"Fireflies and porch lights, you and me and July."*

**The line for captions:** *"Nothing ever happened and it changed my whole
life."*

**The turn:** *"Some kids came through with a jar and a nail-punched lid /
And I let them have the yard, the way somebody did."*

**The quote:** *"A light like that was only ever passing anyway."*

**Why it can travel:** it is a first-love song with no relationship in it,
which is the version most people actually had. The video device — a porch, a
dusk, a jar — costs nothing to recreate, and the ending is generous rather
than heartbroken, which makes it postable in a way that most nostalgia songs
are not.

## Lyrics as they will be sung

```
[intro]
Screen door banging on a hinge that never got fixed,
Cut grass and citronella in the air.
Somebody's sprinkler ticking two yards over,
And the light comes on before we know it's there.

[verse]
We had a jar with a lid my dad punched with a nail,
Six holes and a blade of grass for a bed.
You'd come across the fence at half past eight,
With grass stains and whatever your mother said.
We were bad at catching, better at the chasing,
Barefoot on a lawn that hadn't cooled off yet.
My knees in the dirt and your hand in the dark,
Two kids and a hundred nights we hadn't spent.

[pre-chorus]
Mama's voice through the screen saying, ten more minutes,
Ten more minutes, and then ten more again.
Porch light doing that thing where it hums,
And neither of us ever going in.

[chorus]
Fireflies and porch lights, you and me and July,
Two houses and a fence and a whole lot of sky.
We caught them in a jar and we let them go at nine,
Because a light that small is only borrowed for a time.
I can still hear the hinge, I can still smell the grass,
I can still feel fourteen when the summer gets like this.
Nothing ever happened and it changed my whole life,
Fireflies and porch lights, you and me and July.

[verse]
Last August you were taller and you drove,
And I had a summer job and plans for the fall.
You knocked on the screen at half past eight anyway,
And we sat on the steps and hardly talked at all.
Then you kissed me by the gate like it was nothing,
And your dad's truck was already packed to leave.
I let the last one out of the jar that night,
And I stood in the yard till there was nothing to see.

[pre-chorus]
No voice through the screen now, nobody counting,
Ten more minutes and the whole house still.
Porch light doing that thing where it hums,
And neither of us saying what we feel.

[chorus]
Fireflies and porch lights, you and me and July,
Two houses and a fence and a whole lot of sky.
We caught them in a jar and we let them go at nine,
Because a light that small is only borrowed for a time.
I can still hear the hinge, I can still smell the grass,
I can still feel fourteen when the summer gets like this.
Nothing ever happened and it changed my whole life,
Fireflies and porch lights, you and me and July.

[instrumental]

[bridge]
I've got a porch of my own on a street you never knew,
Two chairs and a bulb I leave on after dark.
When the heat leaves the grass I still go out at eight
And let the evening take its time to start.
Some kids came through with a jar and a nail-punched lid,
And I let them have the yard, the way somebody did.

[chorus]
Fireflies and porch lights, you and me and July,
Two houses and a fence and a whole lot of sky.
I don't need it in a jar, I don't need it to stay,
A light like that was only ever passing anyway.
I can still hear the hinge, I can still smell the grass,
I can still feel fourteen when the summer gets like this.
Nothing ever happened and it changed my whole life,
Fireflies and porch lights, you and me and July.

[post-chorus]
You and me and July,
Two kids and a jar and a sky.
You and me and July,
Let it go, let it go, let it fly.

[outro]
Screen door banging on a hinge that never got fixed,
Somebody out there is fourteen tonight.
I'll leave it on, I'll leave it on till the morning,
Fireflies and porch lights, you and me and July.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2069 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
