# Mirror, Mirror

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirty-seventh song. Female lead **Mahima**, hyperpop-leaning pop with pitched
vocal chops and distorted bass, a getting-ready-for-the-night confidence
anthem. 130 BPM, A minor, uptempo. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — full verses, two post-choruses, a bridge with the turn |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 130 BPM, A minor, distorted saw bass, pitched vocal chops, supersaw stabs, the bathroom tap and lipstick-cap ear candy. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 89 entries — built from the submission's scene direction, plus a three-look character bible, a screen-only ex, three friends, a mirror-in-every-frame rule, workflow, get-ready-with-me challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 37-mirror-mirror
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\37-mirror-mirror\caption.txt `
  --lyrics-file songs\37-mirror-mirror\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\37-mirror-mirror\output\mirror_mirror.wav
```

Expected ~2 h.

## Pacing note before rendering

Pacing is unmeasured for this tempo, and it's the only real risk. The
ballads sang at 116–153 words per minute; this is 130 BPM with two chant
post-choruses, which will pace faster, but by how much is a guess until it
renders. The lyrics are 727 words. Against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.3 min | **overrun — outro lost** |
| 125 wpm | 5.8 min | 97% |
| **140 wpm (the guard setting)** | 5.2 min | 87% |
| 160 wpm | 4.5 min | 76% |

The guard is set at a deliberately conservative 140. **If the first render
truncates the outro, the fix is to drop the second post-chorus (26 words, a
repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| `9:30` → *"Half past nine"* | The model sings digits unpredictably |
| Quotation marks around *"Hey, you. Stay calm."* removed | Punctuation is not sung |
| `[verse 1]`/`[verse 2]`, `[final chorus]` and the descriptive tag lines reduced to plain tags | The model only knows plain section tags |
| The `(repeat)` choruses written out in full | The model would sing the word "repeat" |

Kept exactly as written: every other line, 130 BPM, A minor, the
instrumentation, the mood arc.

## The story and the hooks

Half past nine, steam on the bathroom mirror, one palm wipes an arc and
there she is. The ritual runs item by item: the eyeliner wing on the first
try, the pins coming out of the curls, the glitter on the floor, the red
lipstick going on slow. The mirror is her hype girl. Then a name she doesn't
need lights up the phone; she flips it face down on the sink and the red
wins. Dress, heels, perfume, rings, three friends screaming at the door, a
last kiss to the glass. The second pre-chorus admits the mirror saw the
nights she cried, and stayed. The bridge says the truth: the mirror is only
glass, it shows back what she carries, and she's carried it through every
bad night. The club doors open, the whole floor turns, and she walks home
at half past twelve with every shiny thing in the city agreeing.

**The hook:** *"Mirror, mirror, tell me who's the baddie"* — caption-ready,
built for the mirror-transition format.

**The line for captions:** *"Don't wish me luck, wish the city luck."*

**The turn:** *"The mirror is just glass, it's got nothing to prove / It
only shows back what I carry inside."*

**The chant:** *"Say it, say it, who's the baddie / Lights up, doors up,
it's me, it's me."*

**Why it can travel:** get-ready-with-me is one of the most-filmed formats
there is, the post-chorus is a built-in before-and-after transition, and the
mirror-as-hype-girl idea is one everyone has privately done.

## Lyrics as they will be sung

```
[intro]
Lights on, phone down, speakers loud,
Half past nine, I'm a one-woman crowd.
Steam on the glass, I wipe it with my palm,
There she is. Hey you. Stay calm.

[verse]
Hair up in a towel and a song I know by heart,
Every night out is a ritual, and this is the part
Where the bathroom's a temple and the bulbs are a crown,
And nobody gets to tell me to turn it down.
Eyeliner wing so sharp it could cut,
First try, no shake, that's how I know it's my luck.
Curls falling out of the pins one by one,
I'm not even dressed yet and I'm already the fun.
Gloss on the counter, glitter on the floor,
A dress on the hook that I've been saving for.
Hype on the speaker, I'm singing off-key,
The mirror's my hype girl, and she's staring at me.

[pre-chorus]
Ask the glass, it's never lied,
It's the only one that's always on my side.
One deep breath, the red goes on slow,
Say it with me, mirror, you already know.

[chorus]
Mirror, mirror, tell me who's the baddie,
Don't act shy, you've been looking at me.
Mirror, mirror, say it to my face,
Nobody in this city's gonna take my place.
I'm the whole event, I'm the reason they came,
Every bulb around you is spelling my name.
Mirror, mirror, tell me who's the baddie,
You already know, and baby, so does everybody.

[post-chorus]
Say it, say it, who's the baddie,
Say it to my face, say it back at me.
Say it, say it, who's the baddie,
Lights up, doors up, it's me, it's me.

[verse]
Phone lights up, it's a name I don't need,
Someone who used to say I was too much to be seen.
Cute. I flip it face down on the sink,
This red on my lips is louder than anything he thinks.
Zip on the dress, it's black and it's mean,
Heels that could walk straight out of a magazine.
Perfume on the wrist, on the neck, in the air,
Rings on every finger and a clip in my hair.
The girls at the door, all three of them screaming,
Phone up, flash on, this is the reveal scene.
Keys, gloss, one last kiss to the glass,
Don't wish me luck, wish the city luck, I'm out the door at last.

[pre-chorus]
Ask the glass, it's never lied,
Even on the nights I cried, it stayed on my side.
One deep breath, the door's about to go,
Say it with me, mirror, you already know.

[chorus]
Mirror, mirror, tell me who's the baddie,
Don't act shy, you've been looking at me.
Mirror, mirror, say it to my face,
Nobody in this city's gonna take my place.
I'm the whole event, I'm the reason they came,
Every bulb around you is spelling my name.
Mirror, mirror, tell me who's the baddie,
You already know, and baby, so does everybody.

[instrumental]

[bridge]
Lean in close, I'll tell you the truth,
The mirror is just glass, it's got nothing to prove.
It only shows back what I carry inside,
And I've been carrying it through every bad night.
The girl who cried at it, she's still in there,
She just learned to walk in like she owns the air.
So when the doors swing open and the whole floor turns,
That's not a trick of the light, that's the thing I earned.

[chorus]
Mirror, mirror, tell me who's the baddie,
Don't act shy, you've been looking at me.
Mirror, mirror, I don't need you to say,
I took your answer with me when I walked away.
I'm the whole event, I'm the reason they came,
Every light in this club is spelling my name.
Mirror, mirror, tell me who's the baddie,
You already know, and baby, so does everybody.

[post-chorus]
Say it, say it, who's the baddie,
Say it to my face, say it back at me.
Say it, say it, who's the baddie,
Lights up, doors up, it's me, it's me.

[outro]
Lights low, phone up, the bass in my chest,
Half past twelve and I'm still the best dressed.
Somebody's staring, I'll let him stare,
Every mirror in this building knows I'm here.
Catch me in the window, catch me in the chrome,
Every shiny thing in this city's gonna walk me home.
Mirror, mirror, you were right about me,
You were right about me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 727 at 140 wpm → ~5.2 min, 87% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2519 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
