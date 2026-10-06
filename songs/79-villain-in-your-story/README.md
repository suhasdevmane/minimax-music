# Villain in Your Story

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-nine. Female lead **Mahima**, dark pop with cinematic scale and a
**rap-sung second verse in a British register** — half-time drums, staccato
choir hits, sub-heavy cinematic bass and finger snaps. 98 BPM, D minor. Same
singer as songs 1–8; the rap verse is hers, not a feature.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, ballad/mid pacing class, tightened to fit the budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock, plus a `Delivery Note` line describing the rap-sung second verse. 98 BPM, D minor, cinematic bass, choir hits, snaps, and the shutter-click and heel-on-marble ambience per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 74 entries — built from the submission's scene direction, plus a three-look character bible, a faceless ex, the two-frame crown rule, the red-versus-blue grade rule, workflow, the staircase challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 79-villain-in-your-story
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\79-villain-in-your-story\caption.txt `
  --lyrics-file songs\79-villain-in-your-story\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\79-villain-in-your-story\output\villain_in_your_story.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| `[rap]` on verse two → plain `[verse]`, with the delivery moved into the caption as a `Delivery Note` line | Only the checkpoint's documented tags exist; the model takes performance direction from the caption, never the body |
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Every line tightened by one to two words; the chorus reduced from eight lines to seven | The submission ran 720 sung words, well over the 640-word ballad budget. The rap verse is deliberately the densest section and was cut least |
| Descriptive tag lines (*[intro – bass drone, one struck piano note]*, *[verse 2 – rap-sung, snaps, trap hats]*, *[final chorus – fullest arrangement]*) reduced to plain tags | Same reason |
| The repeated second chorus written out in full | `(repeat)` in the body would be sung as the word |

Kept exactly as written: the story, the UK register and idiom, 98 BPM, D
minor with no modulation, the instrumentation, the mood arc, and every bar of
the rap verse's internal rhyme.

## The story and the hooks

A version of her got to the party before she did. He has been telling it all
week — she is ruthless, she is ice, she burned a perfectly good house down —
and by the time she zips the black dress and takes a cab off the Strand, the
room already knows the story. She does not correct it. The actual charge
sheet, if anyone wants it read, is that she stopped apologising for the room
she fills and asked out loud what she was worth. The rap verse is the
briefing seen from her side: the script, the spin, the mate in the corner
doing PR, the maths she did on her own value and sent him as a rate. The
bridge finds the flaw in the whole case — every story has a narrator, and in
this one it is the man holding the pen. Then a terrace, a coat, a black cab
down the Strand, and heels carried barefoot over a bridge at sunrise.

**The hook:** *"I'll be the villain in your story, the hero in mine"* — the
title lands twice a chorus and is designed to be captioned.

**The line for captions:** *"Same girl, two books, and I'm fine with the
line."*

**The knife line:** *"Villain's just a woman who declined the blame."*

**The rap clip:** *"Call me calculating, that's a compliment, mate, / did the
maths on my worth and sent you the rate."*

**The turn:** *"Course I come out badly when you hold the pen."*

**Why it can travel:** the register does the work — the hardest lines are
delivered flattest, which is exactly how this record should sound coming out
of London. The video is one staircase and one colour cut, and the descent is
a fifteen-second format anyone can film on any stairs with a red bulb.

## Lyrics as they will be sung

```
[intro]
There's a version of me round Mayfair tonight,
Doing terrible things in somebody's mouth.
Apparently I'm ruthless, apparently I'm ice,
Apparently I burned a perfectly good house.
Black dress zipped, called a cab off the Strand,
Walked in on time with a drink in my hand.

[verse]
They're polite when they think you can't hear,
Same room, same champagne, same knives.
I was quiet for years, I made myself small,
Then I asked what I'm worth and I ruined our lives.
That's the charge sheet, if you want it read,
I stopped apologising for the room that I fill.
I never took a thing that wasn't mine,
I just stopped giving mine away, and I never will.

[pre-chorus]
Put me in the black hat, put me in the wrong,
Give the tragic bit to you, I'll take the song.
There's a mirror on the landing, it doesn't say cruel,
It says girl who finally stopped losing to you.

[chorus]
Tell it how you tell it, I'll allow it,
Paint me in the red light, make it loud.
Every story needs a shadow at the party,
And I wear it better than you wore the crown.
I'll be the villain in your story, the hero in mine,
Same girl, two books, and I'm fine with the line.
I'll be the villain in your story, the hero in mine.

[verse]
Cameras on the staircase, I don't blink, don't dip,
Red light on the marble, got a smirk on my lip.
Briefing all week, got a script, got a spin,
Mate in the corner doing PR for your sin.
Call me calculating, that's a compliment, mate,
Did the maths on my worth and sent you the rate.
You liked me when I whispered, loved me when I shrank,
Now the girl in the glass has a crown and a bank.
Spell it properly when you take my name in vain,
Villain's just a woman who declined the blame.

[pre-chorus]
Put me in the black hat, keep me in the wrong,
Give the tragic bit to you, I've got the song.
There's a mirror on the landing, it doesn't say cruel,
It says girl who finally stopped bleeding for you.

[chorus]
Tell it how you tell it, I'll allow it,
Paint me in the red light, make it loud.
Every story needs a shadow at the party,
And I wear it better than you wore the crown.
I'll be the villain in your story, the hero in mine,
Same girl, two books, and I'm fine with the line.
I'll be the villain in your story, the hero in mine.

[instrumental]

[bridge]
Every story's got a narrator and it's you,
Course I come out badly when you hold the pen.
Stayed small and grateful, I'd be lovely in your book,
And I'd be sat here with nothing all over again.
Write it. Print it. Put my name in bold.
Read worse about myself and slept just fine.
Some of us are villains for an hour in one telling,
And the lead in every other, all of the time.

[chorus]
Tell it how you tell it, I'll allow it,
Paint me in the red light, make it loud.
Every story needs a shadow on the staircase,
And I wear it better than you wore the crown.
I'll be the villain in your story, the hero in mine,
Call me cold, call me clever, call it what you like,
I'll be the villain in your story, the hero in mine.

[post-chorus]
Villain, villain, say it like a curse,
Been called a lot of things and villain isn't worse.
Villain, villain, in your telling of the night,
Hero in mine, and I'm sleeping alright.

[outro]
Black cab down the Strand and the city looking new,
Heels in my hand and the sky going blue.
Somewhere in your version I'm still doing the crime,
And I'm the hero in mine.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2246 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
