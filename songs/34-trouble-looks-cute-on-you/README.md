# Trouble Looks Cute on You

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song thirty-four. Female lead **Mahima**, Latin-pop with a live salsa-bar
band — nylon guitar, congas and brass — flirty, slow-burning, US register.
105 BPM, G minor, ballad/mid pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 631 sung words, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 105 BPM, G minor, the nylon-guitar-and-brass lifecycle and the half-time rooftop bridge. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look character bible, Kai as the man, a faceless woman at the end of the bar, the red-light-versus-daylight rule, workflow and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 34-trouble-looks-cute-on-you
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\34-trouble-looks-cute-on-you\caption.txt `
  --lyrics-file songs\34-trouble-looks-cute-on-you\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\34-trouble-looks-cute-on-you\output\trouble_looks_cute_on_you.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | Punctuation is not sung; the model reads the lyric body literally |
| Digits spelled as words (*two in the morning*, *four in the morning*) | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – congas already moving…]`, `[chorus – brass wide open]`, `[verse 1]`, `[pre-chorus 2]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| Every repeated section written out in full — both pre-choruses, all three choruses | `(repeat)` would be sung as the word |
| The band-break stage direction and the half-time bridge note moved into the caption | Stage directions in the body get sung |

Kept exactly as written: every lyric line, 105 BPM, G minor, the
instrumentation, the mood arc, the rooftop turn.

## The story and the hooks

A salsa bar at one in the morning under a single red bulb. Everyone in the
room has already warned her about him, and she checks every warning herself:
his friends won't meet her eyes, the barman pours before he talks, and he
doesn't lie about any of it. She stays. At two the band takes a break and he
tells her the worst of himself — the job he walked out of, the bridge he
burned, the woman at the end of the bar who still turns at his laugh — and
she listens the way you read a menu and orders the thing she knows will undo
her. Then the fire door, the roof, four in the morning, and no red light to
be flattered by. He says one true thing. In the daylight the decision holds.

**The hook:** *"Trouble looks cute on you, so I'll take my chances"* — the
title lands on the downbeat, first and last line of every chorus.

**The line for captions:** *"I read every warning. I stayed for the second
dance."*

**The knife line:** *"You say, you can still leave, the door is right there
/ And I say, I've counted every step, I don't care."*

**The turn:** *"And trouble looks different when it's cold and it's honest /
It looks like a man who might actually stay."*

**Why it can travel:** it is a flirt song where the woman is the one doing
the deciding, and it has an actual second act — the roof at four in the
morning is where the flirtation turns into something with a pulse. The
chorus is a two-dance edit ready-made for vertical video.

## Lyrics as they will be sung

```
[intro]
Red bulb over the bar and the brass coming down,
Somebody says your name like a warning to me.
The congas keep going, nobody's sitting,
And you cross the whole room way too easy.

[verse]
Your friends won't meet my eyes, that's the first thing I clock,
Second, the barman pours before you talk.
Third, you don't lie about a single part,
You just say it plain and let me choose my heart.
There's a nick on your knuckle from a bad last spring,
And a chain at your collar holding somebody's ring.
I should be saying goodnight, I should be gone,
But the nylon guitar keeps talking me on.

[pre-chorus]
Every warning that they gave me had your name inside,
Every one of them was right, and I decide.
Keep your hand right where it is, don't lose the beat,
I'm not looking for the door, I'm looking at your feet.

[chorus]
Trouble looks cute on you, so I'll take my chances,
Red light, wrong man, right song, two dances.
I know how this ends, I've been told twice tonight,
And I'd still pick the floor over doing it right.
Trouble looks cute on you, you wear it like linen,
Loose at the shoulder and the whole room is in it.
Call it a mistake, I'll call it mine,
Trouble looks cute on you, and I've got time.

[verse]
Two in the morning and the band takes a break,
You give me the version your mother would hate.
A job that you walked out of, a bridge that you burned,
A girl at the end of the bar who still turns.
I'm nodding along like I'm reading a menu,
Choosing the one thing I know will undo me.
You say, you can still leave, the door is right there,
And I say, I've counted every step, I don't care.

[pre-chorus]
Every red flag in this room is doing a slow wave,
Every single one is right, and I stay.
Keep your hand right where it is, don't lose the beat,
I'm not looking for the door, I'm looking at your feet.

[chorus]
Trouble looks cute on you, so I'll take my chances,
Red light, wrong man, right song, two dances.
I know how this ends, I've been told twice tonight,
And I'd still pick the floor over doing it right.
Trouble looks cute on you, you wear it like linen,
Loose at the shoulder and the whole room is in it.
Call it a mistake, I'll call it mine,
Trouble looks cute on you, and I've got time.

[instrumental]

[bridge]
Up on the roof there's no red light to hide in,
Just the city on its four in the morning hum.
You go quiet, and you tell me one true thing,
Not the dangerous kind, the kind that's hard to say.
And trouble looks different when it's cold and it's honest,
It looks like a man who might actually stay.

[chorus]
Trouble looks cute on you, so I took my chances,
Dawn light, same man, one more of those dances.
I knew how this ends, they told me twice that night,
And I'd pick this roof again and call it right.
Trouble looks cute on you, you wear it like linen,
Loose at the shoulder with the sun coming in it.
Call it a mistake, I'll call it mine,
Trouble looks cute on you, and I've got time.

[post-chorus]
So I'll take my chances, so I'll take my chances,
Red light, wrong man, right song, two dances.
So I'll take my chances, so I'll take my chances,
Trouble looks cute on you.

[outro]
Bar is shut, the brass is packed away,
Your jacket on my shoulders and the street is grey.
Somebody's going to say your name like a warning,
And I'll smile and I'll say, I know, and I'll stay.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 631 → ~5.4 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2036 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
