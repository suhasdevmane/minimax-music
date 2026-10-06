# Read at Eleven Fifty-Nine

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirty-second song. Female lead **Mahima**, trap-R&B with sliding 808s and
chopped vocal textures, **with her melodic-rap second verse** per the
catalogue's rap map. US register. 90 BPM, F♯ minor, ballad pacing. Same singer
as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 635 sung words, every repeated section written out in full. Verse two is the melodic rap: ten dense internally rhymed bars. |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 90 BPM, F♯ minor, half-time feel, the melodic-rap delivery and its stripped beat described in the emotional progression and arrangement blocks. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look bible for Mahima, a faceless male lead throughout, the split-screen structure and its single collapse, and the every-screen-is-composited rule |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 90 BPM this is a ballad and the verify script's 116 wpm
default applies. The melodic-rap verse will pace faster than that, which makes
the length estimate conservative rather than risky.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 32-read-at-eleven-fifty-nine
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\32-read-at-eleven-fifty-nine\caption.txt `
  --lyrics-file songs\32-read-at-eleven-fifty-nine\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\32-read-at-eleven-fifty-nine\output\read_at_eleven_fifty_nine.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed and em-dashes replaced with commas | Punctuation is not sung |
| Every time spelled out: *eleven fifteen*, *eleven twenty-nine*, *eleven forty*, *eleven fifty-nine*, *twelve oh four*; also *nine miles*, *eighty*, *thirty-mile* | The model sings digits unpredictably, and this song is made of clock times |
| `[verse 1]` / `[verse 2]` / `[rap]` / `[final chorus]` and the descriptive tag lines reduced to plain `[verse]`, `[chorus]` and `[bridge]` | Only the checkpoint's documented tags exist; `[rap]` in particular is dropped or sung |
| The melodic-rap delivery moved out of the lyric body into the caption's emotional-progression and arrangement blocks | The model has no per-section delivery tag; the flow lives in the caption |
| Every repeated chorus and pre-chorus written out in full | The verify script flags parentheses-only lines, and the model would sing *"repeat"* |
| One couplet cut from verse one, one from the rap verse, plus small trims across the choruses, bridge and outro | The submission ran to 691 sung words, well over the ballad budget. The rap verse is ten bars rather than twelve and reads tighter for it. |

Kept exactly as written: every other line, 90 BPM, F♯ minor with no
modulation, the half-time feel, the instrumentation, the drumless bridge, and
the ending four minutes past midnight.

## The story and the hooks

Eleven fifteen, the room is too warm, and the green dot went gray an hour ago.
She writes the message twice, deletes the nice one and sends the flat one, then
walks away from the phone and reads every clock in the apartment twice. The
second verse is the melodic rap: ten bars of somebody who genuinely knows this
game — she wrote half the rules and taught the group chat how to leave a man on
cool — and whose heart is doing eighty in a thirty. The read receipt lands at
eleven fifty-nine, which is not a reply and is completely an answer. Then the
bridge: the message that finally comes through is not words at all, just a
street and a number and a car at the curb, and every clever thing she had goes
off the list. The buzzer goes at twelve oh four and she does not fix her hair.

**The hook:** *"You read it at eleven fifty-nine, and I know you're on your
way."*

**The line for captions:** *"I'm not waiting, I'm just up, that's a difference,
that's a line."*

**The rap bar:** *"Three little dots doing more to me than most men."*

**The turn:** *"Then it came through, and it wasn't even words, just a street
and a number and a car at the curb."*

**Why it can travel:** the read receipt and the typing dots are a universal
piece of modern language nobody has written a proper hook about; the video is
a split screen whose halves post as vertical duets on their own; and the whole
song is a flirtation rather than a heartbreak, which is a register this
catalogue's phone songs have not used.

## Lyrics as they will be sung

```
[intro]
Eleven fifteen and this room is too warm,
Fan on the dresser doing nothing at all.
Green dot went gray about an hour ago,
And I'm not checking, but I know.

[verse]
I wrote the whole thing twice and I deleted the nice one,
Sent the flat one instead like it cost me nothing.
One earring off, one earring still in, and my lipstick on,
Show I'm not watching and a candle going wrong.
I'm not waiting, I'm just up, that's a difference, that's a line,
And the clock on the microwave said eleven twenty-nine.

[pre-chorus]
Tick, tick, tick, and the room's getting small,
Tick, tick, tick, and I'm not gonna call.
I could put it down, I could turn off the light,
But you know what you're doing, and so do I.

[chorus]
You read it at eleven fifty-nine, and I know you're on your way,
Dots on the screen for a minute and you still didn't say.
Nine miles and a river and a driver who don't know,
But you read it at eleven fifty-nine, and that means go.
Don't type it, don't send it, don't call,
Door's on the latch and the lamp turned down small.
Midnight's a minute and you're wasting my time,
You read it at eleven fifty-nine.

[verse]
Eleven forty and I'm not checking, I'm just holding it,
Screen down on my knee like I'm not the type to notice it.
You typed, and you stopped, and you typed, and you stopped again,
Three little dots doing more to me than most men.
I know the game, I wrote the second half of the rules,
Taught the whole group chat how to leave a man on cool.
But my heart's doing eighty in a thirty-mile zone,
And the loudest thing in this apartment is my phone.
So say it or don't, but the minute hand is mine,
And the minute hand is sitting on eleven fifty-nine.

[pre-chorus]
Tick, tick, tick, and the room's getting small,
Tick, tick, tick, and I'm not gonna call.
I could put it down, I could turn off the light,
But you know what you're doing, and so do I.

[chorus]
You read it at eleven fifty-nine, and I know you're on your way,
Dots on the screen for a minute and you still didn't say.
Nine miles and a river and a driver who don't know,
But you read it at eleven fifty-nine, and that means go.
Don't type it, don't send it, don't call,
Door's on the latch and the lamp turned down small.
Midnight's a minute and you're wasting my time,
You read it at eleven fifty-nine.

[instrumental]

[bridge]
Then it came through, and it wasn't even words,
Just a street and a number and a car at the curb.
And I stood in the hallway with my keys in my fist,
And every clever thing I had went off the list.
So I'm done playing chicken and I'm done playing cool,
I'll say the whole thing when I'm looking at you.

[chorus]
You read it at eleven fifty-nine, and I know you're on your way,
Dots on the screen for a minute and you still didn't say.
Nine miles and a river and a driver who don't know,
But you read it at eleven fifty-nine, and that means go.
No more games, no more almost, no more small,
Just headlights on the street and your hand on my wall.
Midnight came and went and I'm still on the line,
You read it at eleven fifty-nine.

[post-chorus]
Eleven fifty-nine, eleven fifty-nine,
Two lights on the bridge and a green line.
Eleven fifty-nine, eleven fifty-nine,
Don't say sorry, say you're outside.

[outro]
Twelve oh four, and the buzzer goes off,
I don't fix my hair and I don't check the clock.
I read you, you read me, and neither of us lied,
Eleven fifty-nine.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 635 at 116 wpm → ~5.5 min, 91% of frame cap |
| Caption + lyrics tokens | 2217 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
