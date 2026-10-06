# When the World Gets Loud

**Status: written and verified, rendering overnight. Not yet rendered.**

Song 102. Male lead, a father singing to his young daughter: an emotional piano-and-strings ballad, 68 BPM, D minor, a warm baritone close to the microphone with a single male harmony on the choruses. Singer A is a male lead here, so the voice lock is the one shared with song 101 rather than the female-lead set from songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the theme, scene-by-scene direction and the submitted draft's story, kept as source material.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — eleven sections, 80 sung lines, 622 sung words. The submission's story and images, cut to the ballad budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 101 — the voice lock. 68 BPM, D minor, piano-and-strings instrumentation, the lift from the pre-chorus through the final chorus |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One shot per lyric line** — 80 numbered entries — plus five instrumental shots, the Kai and Ellie character bible, the flower motif, workflow, edit and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 102-when-the-world-gets-loud
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\102-when-the-world-gets-loud\caption.txt `
  --lyrics-file songs\102-when-the-world-gets-loud\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\102-when-the-world-gets-loud\output\when_the_world_gets_loud.wav
```

## What changed from the submission

| Change | Why |
|---|---|
| Sung length | Fitted to the ballad budget of 600 to 640 sung words, so the song finishes inside the frame cap |
| This version keeps every theme and central image: the loud day, the traffic, the meeting face, the front door, the hand, the spin in the hall, the bent flower, the glass by the window, the flower standing up | Those images are the song. Length was cut, not the story |
| Fits the 600–640 sung-word ballad budget: 622 sung words | Verse and chorus lengths trimmed; the bridge is shorter; the pre-chorus repeats are kept |
| Repeated sections written out in full | The model sings the lyric body literally; `(repeat)` would be sung |
| The outro gained four lines | The flower standing up and the phone, the traffic and the hall are closed on, so the last section is the arrival and not a fade |
| Quotation marks, em-dashes and digits removed; section tags reduced to the plain set | The model sings the lyric body literally and only knows the plain section tags |

Kept exactly as written: the story, the hook, the central images, the 68 BPM and D minor, the instrumentation and the mood arc.

## The story and the hooks

A father comes home from a loud day: a phone that will not stop, traffic that stalls and starts, a man who wants a number that will not close, a meeting he has to smile through. He keeps the face on all day and does not say how it went. At the front door his small daughter is already dancing in the hall with the radio on. She does not ask for the report. She takes his hand and spins him until he loses the thread. Later she brings in a flower with a bent stem from the fence, sets it in a glass of water by the window, and checks on it at bedtime and at dawn until it stands up. The bridge is his reckoning with that: the grown men who never learned to care, and the strength that is in softness. The last image is the two of them at the sink with the flower upright and the phone ringing unanswered.

**The hook:** *"When the world gets loud, you're the quiet I come back to."* — the line a parent can put on any come-home video.

**The line for captions:** *"You don't fix a single thing."*

**The turn:** *"There's a flower on the windowsill and it is standing up."* — the flower image is the lesson, and it is in the outro, not the chorus.

**Why it can travel:** it is a quiet, true thing that almost everyone has felt on either side of a front door, in a short, warm, singable form, with no novelty and nothing to explain.

## Lyrics as they will be sung

```
[intro]
Some days start with thunder
Before the sun is high,
A hundred voices asking
And no good way to reply.

[verse]
The phone goes off at seven with a problem I can't name,
The traffic sits and doesn't move and then it moves again.
There's a man who wants an answer and a number that won't close,
And a meeting in an hour where I'll say that it's all fine.
I keep a face for all of it, I've worn it till it fits,
I can carry a whole bad week and never let it slip.
Then I come in through the front door, drop my bag against the wall,
And there's music in the kitchen and you dancing in the hall.
You don't stop to look at me, you're too far into the song,
You just reach out for my hand and pull me where you are.

[pre-chorus]
You don't ask me how it went,
You don't need the whole report,
You just take my hand and spin me
Till I've lost the thread of it.

[chorus]
When the world gets loud,
You're the quiet I come back to.
When I can't hear myself,
I just stand here and I watch you.
You don't fix a single thing,
You don't know there's any weight,
You just put your hand in mine
And the shouting goes away.

[verse]
You brought a flower in to me from somewhere near the fence,
The stem was bent, the petals torn, it didn't make much sense.
You said that it was only tired and wanted somewhere small,
So we filled a glass with water and we set it by the wall.
You checked on it at bedtime and you checked on it at dawn,
You turned it to the window so it knew which way was warm.
By Thursday it was standing and you never said a thing,
You just carried on with breakfast like it's normal to be mending.
I have spent my whole life hammering at problems till they break,
And you fixed a broken flower with a glass and three days' faith.

[pre-chorus]
You don't ask me how it went,
You don't need the whole report,
You just take my hand and spin me
Till I've lost the thread of it.

[chorus]
When the world gets loud,
You're the quiet I come back to.
When I can't hear myself,
I just stand here and I watch you.
You don't fix a single thing,
You don't know there's any weight,
You just put your hand in mine
And the shouting goes away.

[instrumental]

[bridge]
I don't know how to tell you
That the thing you do is rare,
That there are grown men twice your size
Who have never learned to care
The way you cared about a flower
With a stem that wouldn't hold.
So if anybody ever says
Your softness makes you small,
They have never been the broken thing
You carried down the hall.
They have never been the tired man
You turned towards the sun.

[chorus]
When the world gets loud,
You're the quiet I come back to.
When I can't hear myself,
I just stand here and I watch you.
I came here to be the shelter,
To stand between you and the rain,
And you've been the one who's quietly
Been taking it away.

[post-chorus]
The world can keep on shouting,
The night can rise and fall,
There's a glass beside the window
And you dancing in the hall.

[outro]
So let it all get louder,
Let the thunder do its worst.
There's a flower on the windowsill
And it is standing up.
So let the phone keep ringing,
Let the traffic have its say,
I've got a little hand to hold
And a whole hall left to play.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 622 → about 5.4 min at 116 wpm, 89% of frame cap |
| Caption + lyrics tokens | 1665 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 101 | byte-identical |
