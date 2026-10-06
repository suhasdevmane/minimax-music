# Best Friend Blueprint

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixty-fourth song. Female lead **Mahima**, bright uptempo pop, US register,
118 BPM, F major. The second uptempo song in the catalogue after song 8. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 759 sung words, uptempo class |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 118 BPM, F major, plucked-synth hook, real room-recorded claps as the second lead instrument, brass stabs, electric piano only in the bridge. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 81 entries — with a four-look character bible, Priya as the second lead, a faceless ex, the three repeating set-ups, workflow, the clap-routine challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 64-best-friend-blueprint
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\64-best-friend-blueprint\caption.txt `
  --lyrics-file songs\64-best-friend-blueprint\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\64-best-friend-blueprint\output\best_friend_blueprint.wav
```

Expected ~2 h.

## One thing to know before rendering: pacing

This is the catalogue's second uptempo song and, like song 8, its length is a
projection rather than a measurement. Every ballad so far has sung at 116–153
words per minute. This one is 118 BPM with a chant-heavy post-chorus that will
pace much faster than a verse. The lyrics are 759 words. What that means
against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 130 wpm | 5.8 min | 97% |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 155 wpm | 4.9 min | 82% |

The three post-chorus sections are 152 of the 759 words and will run at chant
speed, so a blended estimate of 145–155 wpm is realistic and lands around five
minutes. The guard is set at a deliberately conservative 140. **If the first
render truncates the outro, the fix is to drop the second post-chorus (34
words, an exact repeat of the first) and re-render.** The measured pacing
should go into `docs/VOICE_RECIPE.md` either way.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads em-dashes unpredictably |
| Every number spelled as a word — *nine years*, *two cities*, *three phones*, *eleven days*, *four hours* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro — filtered arpeggio, one clap, no kick]`, `[verse 1]`, `[final chorus]`) reduced to plain `[intro]` `[verse]` `[chorus]` `[post-chorus]` | Only the documented plain tags exist; anything else is dropped or sung |
| Every repeated chorus and post-chorus written out in full rather than marked as a repeat | A repeat marker would be sung as a lyric |
| Performance directions (the kick dropping out under the pre-chorus, the drumless bridge, the gang vocal, the filtered vocal chop of the title) moved into `caption.txt` | The model sings the lyric body literally |
| Four lines tightened by one word each | The submission came in at 764 words, above the uptempo target band; the trims are in the intro, the bridge and the repeated post-chorus line |
| `render.json` added with `wpm: 140` | Uptempo songs pace far faster than the 116 wpm ballad default the verify script assumes |

Kept exactly as written: every other lyric line, 118 BPM, F major, the
instrumentation, the three-set-up video concept and the mood arc.

## The story and the hooks

Nine years, two cities, one charger. The friend shows up on the doorstep with
two bags of snacks held up like evidence, does not ask whether she is fine,
puts the kettle on and lets her cry, then tells her the truth in the exact
right order — nice part first. She takes the phone at midnight, then the keys,
then the wheel. Verse two is the cost of that: she told the truth about him in
a parking lot and got eleven days of silence for it, and she did not chase,
she just left the door unlocked and saved half of everything. Then a stairwell
call answered on the first ring, four hours of interstate and a bag of sour
candy passed sideways without a word. The bridge is the reversal — last year
it was the other way round, and the look on her face when somebody finally
drove the four hours for her is the whole point. The last chorus is the same
words with the pronouns swapped.

**The hook:** *"You're the blueprint, best friend, everyone else is a copy."*

**The line for captions:** *"Everybody wants a love song, I'm not writing one /
This one's for the girl who drove four hours in the dark."*

**The turn:** *"If this is the great romance of my life, then fine / Nine
years, no contract, and nobody had to sign."*

**The chant:** *"Blueprint, blueprint, everyone else is a copy."*

**Why it can travel:** friendship anthems have a permanent, recurring occasion
attached to them — birthdays, anniversaries, going-away posts — and there are
far fewer of them than love songs. The chant is four words long, the video
device is a four-move clap routine anybody can film against a wall, and the
last chorus gives the friend her own verse of credit by swapping the roles.

## Lyrics as they will be sung

```
[intro]
Nine years, two cities and a group chat with a name,
Three phones, one charger, and a car that barely runs.
I have never had to explain myself to you,
Not one time, not once.

[verse]
You show up with snacks like it's a medical emergency,
Sour candy and a bag of something fried.
You don't ask me if I'm fine, you just start unpacking,
And you put the kettle on and let me cry.
You tell me the truth in the exact right order,
The nice part first, then the part I need to hear.
You said, that dress is not the problem, and you're right,
And I put on the other one and we got out of there.

[pre-chorus]
Every friend I've ever made, I measured against you,
And every single one of them came up short.
You're not the bar, you're the whole entire building,
You're the reason I know what a person's worth.

[chorus]
You're the blueprint, best friend, everyone else is a copy,
Cheap ink, wrong size, and the second page is gone.
You take my phone at midnight, then the keys, then the wheel,
You tell me what I look like when I won't say how I feel.
Everybody wants a love song, I'm not writing one,
This one's for the girl who drove four hours in the dark.
Say it in a toast, say it on a card,
You're the blueprint, best friend, everyone else is a copy.

[post-chorus]
Blueprint, blueprint, everyone else is a copy,
Blueprint, blueprint, nobody else got it right.
Blueprint, blueprint, everyone else is a copy,
You're the original, honey, I got the only one.

[verse]
You told me the truth about him in a parking lot,
And I didn't speak to you for eleven days.
You never chased me down, you left the door unlocked,
And you saved me half of everything anyway.
Then I called you from a stairwell, you picked up on the first ring,
You didn't say I told you so, you said, I'm in the car.
Four hours in the dark with a bag of sour candy,
And you never once asked me how I let it get that far.

[pre-chorus]
Every love I've ever lost, I got over in your kitchen,
And every version of me, you have kept them all.
You're not a chapter in the book, you're the spine,
And I would sign up for the whole nine years again.

[chorus]
You're the blueprint, best friend, everyone else is a copy,
Cheap ink, wrong size, and the second page is gone.
You take my phone at midnight, then the keys, then the wheel,
You tell me what I look like when I won't say how I feel.
Everybody wants a love song, I'm not writing one,
This one's for the girl who drove four hours in the dark.
Say it in a toast, say it on a card,
You're the blueprint, best friend, everyone else is a copy.

[post-chorus]
Blueprint, blueprint, everyone else is a copy,
Blueprint, blueprint, nobody else got it right.
Blueprint, blueprint, everyone else is a copy,
You're the original, honey, I got the only one.

[instrumental]

[bridge]
Last year it was your turn and I got to hold the door,
I drove the four hours and I didn't say a thing.
And you looked at me like no one ever did that before,
And I thought, so that's what she's been doing all along.
If this is the great romance of my life, then fine,
Nine years, no contract, and nobody had to sign.

[chorus]
You're the blueprint, best friend, everyone else is a copy,
Cheap ink, wrong size, and the second page is gone.
I take your phone at midnight, then the keys, then the wheel,
I tell you what you look like when you won't say how you feel.
Everybody wants a love song, so here's the only one,
For the girl who drove four hours and the girl who drove them back.
Say it in a toast, say it on a card,
You're the blueprint, best friend, everyone else is a copy.

[post-chorus]
Blueprint, blueprint, everyone else is a copy,
Blueprint, blueprint, nobody else got it right.
Blueprint, blueprint, everyone else is a copy,
Blueprint, blueprint, and I'm keeping you for life.
You're the original, honey, I got the only one,
Blueprint, blueprint, everyone else is a copy.

[outro]
Nine years, two cities and a group chat with a name,
Three phones, one charger, and a car that finally died.
I have never had to explain myself to you,
And I'm not about to start tonight.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 759 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2381 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
