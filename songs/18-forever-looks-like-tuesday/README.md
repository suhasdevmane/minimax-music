# Forever Looks Like Tuesday

**Status: written and verified, NOT rendered. Not yet in the queue.**

Eighteenth song. **Female + male duet** — Mahima on the lead with a male
baritone on verse two and in close harmony throughout — country-pop ballad,
84 BPM, D major, US register. Ballad pacing, no `render.json`. Same singer as
songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 624 sung words, ballad budget |
| [`caption.txt`](caption.txt) | Music description. Mahima’s `Vocal Details` lines and the `Sonics` block byte-identical to song 1; a male baritone added as Singer B with a section-by-section duet structure. 84 BPM, D major, pedal steel and brushed snare, with a kitchen faucet dripping under the intro and stopping for good after the bridge. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — with a two-look character bible, Kai carrying a full verse on camera, the sub-second wedding-flash rule, the composited-writing note, workflow, the ordinary-Tuesday challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 18-forever-looks-like-tuesday
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\18-forever-looks-like-tuesday\caption.txt `
  --lyrics-file songs\18-forever-looks-like-tuesday\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\18-forever-looks-like-tuesday\output\forever_looks_like_tuesday.wav
```

Expected ~2 h.

## One thing to know before rendering: it is a duet, and the model has no per-line singer control

Same situation as songs 4 and 8. The split lives in the caption’s
`Duet Structure` line and the model follows it loosely. Expect the choruses
as two voices in harmony, which is what this arrangement is built on; the
real test is verse two, which is written for the male voice alone and is the
emotional centre of the record. If the model sings verse two in the female
voice the song still works — it simply becomes her memory rather than his —
so this is a low-risk duet compared with song 8’s rap.

## What changed from the submission

| Change | Why |
|---|---|
| Digits spelled out and kept as words throughout — *two people*, *second row*, *one line shorter* | The model sings digits unpredictably |
| Quotation marks and em-dashes removed from the sung lines | Punctuation is not sung; the model sings the lyric body literally |
| Descriptive tag lines (*intro – fingerpicked guitar*, *verse 2 – male lead*, *bridge – no drums, a line each*) reduced to plain `[intro]`, `[verse]`, `[bridge]`; every singer marking and performance direction moved into the caption’s `Duet Structure` line | Only the checkpoint’s documented tags exist, and anything left in the body gets sung |
| The two repeated choruses written out in full instead of marked as repeats | The verify script flags parentheses-only lines and the model would sing them |
| No `render.json` | At 84 BPM this is a ballad; the verify script’s 116 wpm default is the right guard |

Kept exactly as written: every line, 84 BPM, D major, the instrumentation
list, the hospital-parking-lot verse, the bridge trade and the six viral
moments. No trimming was needed — 624 words fits the ballad budget.

## The story and the hooks

The faucet has been dripping since spring. There is a dead bulb above the stairs
they both walk around and a list on the fridge that never gets shorter. It is
a Tuesday with nothing on the calendar: he is on the kitchen floor with his
shoulder inside the sink cupboard, she is on the sofa losing to a tax form,
and neither of them would trade the afternoon. Then he takes the second verse
and tells the other Tuesday — the winter her father was in hospital, the
takeout eaten in the parking lot, her asleep against his coat with a paper cup
in both hands — and says that is where he understood what the word meant.
They spend the bridge on the kitchen floor listing everything they will take.
By the last shot the faucet is dry, the stairs are lit, and the list is one line
shorter.

**The hook:** *"Forever looks like Tuesday, and Tuesday looks like you."*

**The line for captions:** *"Nobody writes it down, nobody makes a fuss, but
the ordinary hours are the best of us."*

**The turn:** *"That was a Tuesday too. Nobody sang about it."*

**The trade:** the bridge, six lines, one each — *"I’ll take the trash night
and the shoes piled by the door, I’ll take the way you always buy too many
eggs."*

**Why it can travel:** it is a first-dance and anniversary song that is not
about a wedding, it gives couples a six-line format they can copy word for
word about their own house, and the hospital verse gives it the weight that
keeps it from being merely charming.

## Lyrics as they will be sung

```
[intro]
The faucet in the kitchen has been dripping since the spring,
You've been meaning to look at it since May.
There's a light bulb out above the stairs we walk around,
And a list up on the fridge that never gets shorter.

[verse]
It's a Tuesday, and there's nothing on the calendar at all,
Just the trash, and the bank, and a form I have to sign.
You've got the cupboard open and your shoulder in the pipe,
I've got the laptop on my knees and I am losing at the taxes.
There's a shirt of yours drying on the radiator wrong,
And the good scissors are somewhere neither of us can name.
Nobody's taking pictures, nobody got dressed up,
And I wouldn't trade this afternoon for anything.

[pre-chorus]
They told me it would look like a church and a dress,
Rice in my hair and your hand holding mine.
And it did, for a day. But mostly it looks like this,
Two people and a Tuesday and a job half done.

[chorus]
Forever looks like Tuesday,
And Tuesday looks like you.
Wet hands, a wrench, a radio on low,
And a coffee going cold and a whole afternoon to go.
Nobody writes it down, nobody makes a fuss,
But the ordinary hours are the best of us.
Forever looks like Tuesday,
And Tuesday looks like you.

[verse]
I thought forever came with fireworks and a plane,
Some big loud proof that you could point to on a wall.
Then the winter that your father was in the hospital,
And we ate out in the parking lot and you slept against my coat.
That was a Tuesday too. Nobody sang about it.
You held the paper cup with both your hands and you were fine.
And I knew right then, whatever this thing is,
It isn't in the party, it's in getting through the week.

[pre-chorus]
They told us it would look like a stage and a speech,
Somebody's mother crying in the second row.
And it did, for an hour. But mostly it looks like this,
Two people and a Tuesday and a job half done.

[chorus]
Forever looks like Tuesday,
And Tuesday looks like you.
Wet hands, a wrench, a radio on low,
And a coffee going cold and a whole afternoon to go.
Nobody writes it down, nobody makes a fuss,
But the ordinary hours are the best of us.
Forever looks like Tuesday,
And Tuesday looks like you.

[instrumental]

[bridge]
I'll take the faucet that drips, I'll take the burnt-out bulb,
I'll take the taxes and the form you never signed.
I'll take your terrible singing coming through the wall,
I'll take the way you fall asleep in the middle of the film.
I'll take the trash night and the shoes piled by the door,
I'll take the way you always buy too many eggs.
And if forever's just a lot of Tuesdays in a row,
Then I'll take Tuesday, and I'll take it slow.

[chorus]
Forever looks like Tuesday,
And Tuesday looks like you.
Wet hands, a wrench, a radio on low,
And the faucet has stopped its dripping and there's still a night to go.
Nobody writes it down, nobody makes a fuss,
But the ordinary hours are the best of us.
Forever looks like Tuesday,
And Tuesday looks like you.

[post-chorus]
Tuesday, Tuesday, and the week rolling on,
Tuesday, Tuesday, and I want every one.
Tuesday, Tuesday, and the light turning gold,
Forever looks like Tuesday, and I'll take it till we're old.

[outro]
The faucet in the kitchen isn't dripping anymore,
There's a bulb above the stairs and we can see the floor.
The list up on the fridge is one line shorter than it was,
And that is what a good life looks like, I suppose.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 624 → ~5.4 min at 116 wpm, 90% of frame cap |
| Caption + lyrics tokens | 2287 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima’s `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
