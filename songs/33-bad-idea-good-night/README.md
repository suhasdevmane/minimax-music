# Bad Idea, Good Night

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirty-third song. Female lead **Mahima**, pop-punk / power-pop with
shouted gang vocals, 150 BPM, E major, fast and reckless, one wild night
from the group-chat vote to a gas station curb at sunrise. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 150 BPM, E major, double-tracked power chords, gang vocals, the stick count-in and the red-light stop per the submission. |
| [`render.json`](render.json) | Uptempo pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 87 entries — built from the submission's scene direction, plus a three-look character bible, Kai with a scar and a scooter, faceless one-star girls, a screen-only group chat, workflow, the seven-to-nothing challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 33-bad-idea-good-night
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\33-bad-idea-good-night\caption.txt `
  --lyrics-file songs\33-bad-idea-good-night\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\33-bad-idea-good-night\output\bad_idea_good_night.wav
```

Expected ~2 h.

## Pacing is unmeasured

Every ballad so far sang at 116–153 words per minute. This is 150 BPM
pop-punk with a chanted post-chorus, which will pace faster, but by how much
is a guess until it renders. The lyrics are 715 words. Against the model's
6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.2 min | **overrun — outro lost** |
| 125 wpm | 5.7 min | 95% |
| **140 wpm (the guard setting)** | 5.1 min | 85% |
| 160 wpm | 4.5 min | 74% |

A shouted pop-punk chorus at 150 BPM usually lands around 150–170 wpm,
which puts this near 4.5–5 minutes. The guard is set at a deliberately
conservative 140. **If the first render truncates the outro, the fix is to
drop the post-chorus (24 words, a chant) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| `7 to 0` → *"seven to nothing"*, `2 a.m.` → *"at two"* | The model sings digits unpredictably |
| Quotation marks around the spoken lines (*do not do it*, *I know what they say*, *hop on*, *ask me tomorrow*) removed; commas instead | Punctuation is not sung |
| `[verse 1]`/`[verse 2]`, `[final chorus]` and the descriptive tag lines reduced to plain tags | The model only knows plain section tags |
| Repeated choruses written out in full | The model would sing a `(repeat)` line |

Kept exactly as written: every other line, 150 BPM, E major, the
instrumentation, the mood arc, the red-light motif. No trimming was needed;
715 words fits the uptempo budget.

## The story and the hooks

Her best friend says don't. Her sister says don't. The group chat votes
seven to nothing. She agrees with all of them — the scar, the chipped
polish, the slushie-smelling jacket, the one-star reviews in the parking
lot — and gets on the back of his scooter anyway. A skate park after dark
and a scraped knee he kisses better. A basement gig with a terrible band
and a dripping ceiling. Chips bought with his last four coins. A roundabout
at two in the morning with the lights on amber. Maybe he ghosts her by
Thursday. She'll still have the night. Sunrise on a gas station curb, a
blue slushie, forty unread messages, and *"ask me tomorrow."*

**The hook:** *"You're a bad idea, but a good night"* — a caption before it
is a chorus.

**The line for captions:** *"I knew better and I did it anyway."*

**The turn:** *"Better never made me laugh until I couldn't breathe /
Better never had a scar and a story to say."*

**The chant:** *"Seven to nothing, they were right / Bad idea, but a good
night."*

**Why it can travel:** it is the night everyone has been warned out of,
told with the grin left in; the group-chat vote is a ready-made challenge
and the red light is a ready-made frame.

## Lyrics as they will be sung

```
[intro]
My best friend texted, do not do it,
My sister sent a warning too.
The group chat voted, seven to nothing,
Every single one of them said you.

[verse]
You got a scar above your eyebrow and a story to go with it,
Chipped black polish and a board with the trucks worn thin.
You said, I know what they say, and I said, yeah, so do I,
Then you held out your hand and I said, let's begin.
You showed up on a scooter with a cracked headlight,
Said, hop on, and I looked at the sky like, really?
Everyone I love has got a spreadsheet of your damage,
And I'm about to put my name on it, honestly.
Your jacket smells like a gas station slushie,
Your playlist is loud and it's ninety percent screaming.
You laugh at your own jokes before you finish them,
And somehow every red flag has me leaning in.

[pre-chorus]
Yeah I read the reviews, one star, one star,
Every girl you dated left a warning in the parking lot.
I know exactly what this is,
And I'm doing it anyway, ready or not.

[chorus]
You're a bad idea, but a good night,
Wrong on paper, but the timing's right.
I'll regret you in the morning, that's the deal,
But tonight I'm gonna feel what I feel.
Whoa oh, tell my friends I'm sorry,
Whoa oh, tell my mum don't worry.
You're a bad idea, but a good night,
And the best ones always start with a red light.

[verse]
Skate park after dark, you're teaching me to drop in,
I'm screaming on the ramp and you're screaming louder.
Concrete kissed my knee, you kissed it better,
Then you laughed and said, I told you I was trouble.
Basement gig at midnight, your friend's band is terrible,
The ceiling's dripping and the amp keeps cutting out.
You pulled me in the pit and held onto my hoodie,
And I sang words I didn't know at the top of my mouth.
Chips from the van with your last four coins,
You said, I'm broke, I said, I noticed, I don't care.
Your friend's band's name in marker on my forearm,
Your number on yours, and half of it isn't there.

[pre-chorus]
Yeah I read the reviews, one star, one star,
But the reviews never mentioned the way you laugh.
I know exactly what this is,
And I'm doing it anyway, don't do the math.

[chorus]
You're a bad idea, but a good night,
Wrong on paper, but the timing's right.
I'll regret you in the morning, that's the deal,
But tonight I'm gonna feel what I feel.
Whoa oh, tell my friends I'm sorry,
Whoa oh, tell my mum don't worry.
You're a bad idea, but a good night,
And the best ones always start with a red light.

[instrumental]

[bridge]
Two on a scooter, no helmets, sorry mother,
Doing thirty through the roundabout at two.
The streetlights blinking orange like they're judging us,
And I'm holding on and laughing, and so are you.
Maybe you'll ghost me by Thursday,
Maybe you'll forget my name.
But I'll have this, the wind and the sirens,
And the night I said yes to the flame.
They'll say, you should've known better, and I did,
I knew better and I did it anyway.
Better never made me laugh until I couldn't breathe,
Better never had a scar and a story to say.

[chorus]
You're a bad idea, but a good night,
Wrong on paper, but the timing's right.
I'll regret you in the morning, if I do,
But right now the only plan I've got is you.
Whoa oh, tell my friends I'm sorry,
Whoa oh, tell my mum don't worry.
You're a bad idea, but a good night,
And the best ones always start with a red light.

[post-chorus]
Bad idea, bad idea, good night,
Bad idea, bad idea, good night,
Seven to nothing, they were right,
Bad idea, but a good night.

[outro]
Sun's coming up on a gas station curb,
Slushie for breakfast, blue tongue, no sleep.
Your board under my feet, your jacket on my shoulders,
Forty messages waiting and I'm not gonna read.
You said, so was it worth it, and I said, ask me tomorrow,
Then I kissed you like a secret I don't plan to keep.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 715 at 140 wpm → ~5.1 min, 85% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2335 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
