# The Way You Say Good Morning

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-seventh song. Female lead **Mahima**, slow modern R&B — finger snaps
instead of a snare, electric piano, deep harmony stacks — US register. 92 BPM,
D♭ major, ballad pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 633 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 92 BPM, D♭ major with no modulation, snaps carrying the rhythm in place of a snare, a drumless piano bridge, and the ceiling-fan and phone-on-wood ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 67 entries — with a two-look bible for Mahima, Kai's single look, the climbing-light continuity rule, the five-light-position build method and the tasteful-framing rule |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 92 BPM this is a ballad and the verify script's 116 wpm
default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 27-the-way-you-say-good-morning
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\27-the-way-you-say-good-morning\caption.txt `
  --lyrics-file songs\27-the-way-you-say-good-morning\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\27-the-way-you-say-good-morning\output\the_way_you_say_good_morning.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed and em-dashes replaced with commas | Punctuation is not sung |
| Digits spelled out: *ten to seven*, *two words*, *six alarms*, *forty years* | The model sings digits unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines (*"pad, one piano chord, no drums"*, *"asking for it again"*) reduced to plain tags | Only the checkpoint's documented tags exist; anything else on a tag line is dropped or sung |
| Every repeated chorus and pre-chorus written out in full | The verify script flags parentheses-only lines, and the model would sing *"repeat"* |
| Two couplets cut from the verses: *"Low and half a note under where it sits at noon / Gravel in the middle of a perfectly good tune"* and *"I used to run at six, I used to beat the sun / Now the best part of my day is already done"* | The submission ran to 678 sung words, well over the ballad budget. Both cuts also fixed craft problems: the first pre-empted the chorus's *"all gravel"* image before the hook landed, and the second said in verse two what the bridge says better. |

Kept exactly as written: every other line, 92 BPM, D♭ major with no
modulation, the instrumentation, the lift built from harmony stacks rather
than volume, and the ending on a held breath.

## The story and the hooks

The whole song holds still inside about ninety minutes of one real morning
and refuses to let the day start. His voice before coffee is wrecked, half a
note under where it sits at noon, and he says two words into her shoulder
with his eyes still shut. Verse two is everything outside the bedroom asking
for attention and losing: a meeting at nine, a car with a flat, a phone
buzzing itself across the nightstand, a mug of coffee going cold on the
counter for the second time this week. The bridge is the turn — she used to
set six alarms and wake up already tired, and the first thing in the world
used to be the worst part of it. Now she wakes before the sun on purpose.

**The hook:** *"The way you say good morning makes me wanna stay in bed."*

**The line for captions:** *"You haven't opened both eyes and you've already
won."*

**The turn:** *"And the first thing in the world stopped being the worst
part."*

**The quiet one:** *"And the outside world can take a number and wait."*

**Why it can travel:** the post-chorus is two words over a bare snap groove,
which is a ready-made audio for morning-routine and couple content; the song
is sensual without a single line that a platform would touch; and it is about
a sound rather than a scene, which nobody else in the catalogue is doing.

## Lyrics as they will be sung

```
[intro]
Ten to seven and the room goes gray to gold,
Blinds laying stripes across the both of us.
The fan is turning slow, your arm across my back,
You say two words and I lose the whole day to that.

[verse]
There's a strip of light across the ceiling and your jaw,
And your voice comes out like it's been dragged across a floor.
You say it into my shoulder with your eyes still shut,
Like the day is a rumor that you haven't heard about.
I have got a whole list of things I meant to be,
And not one of them is stronger than you saying it to me.

[pre-chorus]
So say it slow, say it into the pillow,
Say it before the room gets any older.
Two words, no rush, don't clear your throat,
Say it like you mean the whole day that you wrote.

[chorus]
The way you say good morning makes me wanna stay in bed,
Half a word, all gravel, and it goes right through my head.
You haven't opened both eyes and you've already won,
Say it one more time and the day can come undone.
The way you say good morning, low and slow and rough,
Sunday doesn't start until you say enough.
Pull the blinds, let the light come down in lines,
The way you say good morning makes the morning mine.

[verse]
There's a meeting at nine and a car that needs the shop,
And a phone on the nightstand that has buzzed and will not stop.
Your hand finds the small of my back like it knows the way,
And the outside world can take a number and wait.
Coffee went cold on the counter, that's twice this week,
And I'd let it go cold again for the sound of you half asleep.

[pre-chorus]
So say it slow, say it into the pillow,
Say it before the room gets any older.
Two words, no rush, don't clear your throat,
Say it like you mean the whole day that you wrote.

[chorus]
The way you say good morning makes me wanna stay in bed,
Half a word, all gravel, and it goes right through my head.
You haven't opened both eyes and you've already won,
Say it one more time and the day can come undone.
The way you say good morning, low and slow and rough,
Sunday doesn't start until you say enough.
Pull the blinds, let the light come down in lines,
The way you say good morning makes the morning mine.

[instrumental]

[bridge]
I used to hate the morning, set six alarms in a row,
Wake up already tired with nowhere good to go.
Then a Sunday in the spring and a voice in the dark,
And the first thing in the world stopped being the worst part.
Now I wake before the sun just to be early to you,
And I lie here in the quiet till you move.

[chorus]
The way you say good morning makes me wanna stay in bed,
Half a word, all gravel, and it goes right through my head.
Forty years of mornings and I'd take every one,
If it starts with your voice and it ends with the sun.
The way you say good morning, low and slow and rough,
Sunday doesn't start until you say enough.
Pull the blinds, let the light come down in lines,
The way you say good morning makes the morning mine.

[post-chorus]
Good morning, good morning,
Say it low, say it slow, say it just to me.
Good morning, good morning,
And the rest of the day can be what it wants to be.

[outro]
Blinds down, light in lines across the sheet,
Your voice in the dark before the day begins.
Don't get up yet, don't say anything else,
Just say it to me one more time.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 633 at 116 wpm → ~5.5 min, 91% of frame cap |
| Caption + lyrics tokens | 2008 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
