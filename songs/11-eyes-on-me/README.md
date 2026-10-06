# Eyes on Me

**Status: written and verified, NOT rendered. Not yet in the queue.**

Eleventh song. Female lead **Mahima**, modern pop-R&B / late-night
slow-groove with a half-rapped second verse in a US R&B cadence, 94 BPM,
B♭ minor. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 94 BPM, B♭ minor, no modulation; finger snaps, sub-bass and Rhodes, with the half-rapped second verse described as a delivery change in the caption rather than a tag. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — from the submission's scene direction, with a three-look character bible, Kai as the man across the room, slow-motion party crowd guidance, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 11-eyes-on-me
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\11-eyes-on-me\caption.txt `
  --lyrics-file songs\11-eyes-on-me\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\11-eyes-on-me\output\eyes_on_me.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the dialogue lines (*"hey, what's your name,"* *"I know, I picked it"*) | Punctuation is not sung, and quote marks around a sung phrase can be read as a break |
| Descriptive tag lines — `[intro – filtered, behind a wall, then close]`, `[chorus – wide, slow, seductive]`, `[verse 2 – half-rapped, dry, snaps and sub only]`, `[bridge – near-spoken, then building]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; the variation lives in the words, not the tag |
| The half-rap direction moved into the caption's `Vocal Style` progression and `Global Emotional Progression` | There is no `[rap]` tag; the delivery change has to be described, not tagged |
| Every repeated chorus and pre-chorus written out in full | `(repeat)` would be sung as the word |

Kept exactly as written: every lyric line, 94 BPM, B♭ minor, the
instrumentation, the mood arc, the twist in the bridge. No trimming was
needed — 636 words fits.

## The story and the hooks

She wasn't even going to come. Somebody's playlist, somebody's kitchen, a
red cup and a red dress, and then from the staircase she feels it: somebody
is looking, and she knows exactly who. He's by the speaker pretending the
song is what he's into. She could walk over and make it easy. Instead she
takes the long way round the room, touches her hair, laughs at nothing, and
lets him do the work. The second verse reads him line by line — the frozen
mid-laugh, the fake phone check at eleven on a Friday, the conversation that
went flat when she took her jacket off. Then the bridge turns it: she has
been watching him watching her since she walked in. The eyes on her were
hers on him the whole time. Half past two, his jacket on her shoulders.

**The hook:** *"Keep your eyes on me, I know you already do"* — a line you
can say straight down the lens.

**The line for captions:** *"Keep your eyes on me, I know you already do."*

**The rap clip:** *"Nobody's texting you at eleven on a Friday / Put it down,
look up, we can do this my way."*

**The turn:** *"The eyes on me were mine on you the whole time, that's the
twist."*

**Why it can travel:** it is a whole flirtation with no touching in it — one
glance held across a room for a full chorus — which makes it a walk-in
transition, a getting-ready reel and a slow-motion turn, all from one song.

## Lyrics as they will be sung

```
[intro]
Somebody's playlist, somebody's kitchen, somebody's cousin at the door,
Red cup, red dress, I wasn't even gonna come.
Then I felt it from the staircase like a hand across the room,
Somebody's looking, and I know exactly who.

[verse]
You're by the speaker acting like the song is what you're into,
But your head keeps turning every time I move.
Your boy is talking, and you're nodding, but you're not there,
You're a satellite tonight, and I'm the view.
I could make it easy, I could walk on over,
Say hey, what's your name, and let it play.
But where's the fun in easy when you're watching like that?
Baby, I'm gonna make you work for what you're gonna say.

[pre-chorus]
So I'm gonna take the long way round the room,
Touch my hair, laugh at nothing, take my time.
Every step I take is a step you gotta follow,
Don't you look away, you're doing fine.

[chorus]
Keep your eyes on me, I know you already do,
I felt it from the staircase, now I'm proving it to you.
Keep your eyes on me, don't blink and don't pretend,
I'll keep you looking, baby, till the song is at its end.
Eyes on me, eyes on me,
I know you already do.

[verse]
Look, I saw you clock me when I came in the back,
Red dress, no stress, you froze mid-laugh,
Your whole conversation went flat, and I like that,
I didn't do a thing yet, I just took off my jacket.
Now you're doing that thing where you check your phone,
Like you got a text, but I know that you don't,
Nobody's texting you at eleven on a Friday,
Put it down, look up, we can do this my way.
I'm not gonna wave, I'm not gonna call you over,
I'm gonna let the whole room turn in slow motion,
You'll find me by the window when your nerve kicks in,
Take your time, I got all night, and I already win.

[pre-chorus]
So I'm gonna take the long way round the room,
Touch my hair, laugh at nothing, take my time.
Every step I take is a step you gotta follow,
Don't you look away, you're doing fine.

[chorus]
Keep your eyes on me, I know you already do,
I felt it from the staircase, now I'm proving it to you.
Keep your eyes on me, don't blink and don't pretend,
I'll keep you looking, baby, till the song is at its end.
Eyes on me, eyes on me,
I know you already do.

[instrumental]

[bridge]
When you finally cross the floor, two hundred people in the way,
I'm gonna act surprised, like I didn't plan the whole thing.
You'll say something about the song, I'll say, I know, I picked it,
Then you'll laugh, and that's the moment, I'll admit it.
Cause I've been watching you watching me since I walked in,
The eyes on me were mine on you the whole time, that's the twist.
So say it, say the thing you've been rehearsing by the speaker,
I'll say yes before you finish, and we'll take it from there.

[chorus]
Keep your eyes on me, I know you already do,
I felt it from the staircase, now I'm standing next to you.
Keep your eyes on me, don't blink and don't pretend,
Turns out I was looking too, so let's call it even then.
Eyes on me, eyes on me,
I know you already do.

[post-chorus]
Eyes on me, don't look away,
I know you already do.
Eyes on me, it's okay,
Cause my eyes are on you.

[outro]
Somebody's kitchen, half past two, the music's low,
Red cup empty, red dress, your jacket on my shoulders now.
Yeah, I felt it from the staircase, and I knew exactly who,
Keep your eyes on me, I know you already do.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 636 → ~5.5 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2285 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
