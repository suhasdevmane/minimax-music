# Small Hands, Big World

**Status: written and verified, rendering overnight. Not yet rendered.**

Song 104. Male lead **Kai** (Singer A), a father singing to his six-year-old daughter, cinematic country-pop ballad, 70 BPM, G major. The voice lock matches song 101.

Source of record: [`source/original-submission.md`](source/original-submission.md) — the song and its scene-by-scene direction, before cleanup for the lyric body.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 623 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 101, the voice lock. 70 BPM, G major, the steel guitar, upright bass and brush kit per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 114 entries — built from the submission's direction, plus a Kai and Ellie character bible, workflow, edit notes and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 104-small-hands-big-world
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\104-small-hands-big-world\caption.txt `
  --lyrics-file songs\104-small-hands-big-world\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\104-small-hands-big-world\output\small_hands_big_world.wav
```

Render time not yet measured; the first render will set the figure.

## What changed from the submission

| Change | Why |
|---|---|
| Sung length | Fitted to the ballad budget of 600 to 640 sung words (623 here), so the song finishes inside the frame cap |
| Every theme and central image kept | The pencil, the house with seven windows, the rainbow, the animals across the hallway, the falls and the courage, the bridge promise, "small hands, big world" all stay |
| One repeated chorus written out once fewer | The chorus is written out three times, not four, as the chorus repeats; the hook still lands three times |
| The pre-chorus kept | "You rescue me each day" sits after the third verse, before the second chorus, where the father turns to the child directly |
| Repeats written out in full | The model sings the lyric body literally; every chorus is written out in full, never as `(repeat)` |
| Digits spelled out, no quotation marks, no em-dashes | The model sings digits unpredictably; the body contains only sung words and plain section tags |

## The story and the hooks

A father kneels to his six-year-old daughter's height and sees how much courage and imagination she has in a body that still fits inside his arms. She draws a house with seven windows, lines her plush animals across the hallway, falls in the playground and gets back up. He tells her, plainly, what she has taught him. The bridge is his promise: he will be there when she loses her way, and she will always have his hands.

**The hook:** *"Small hands, big world"* — two words that are the whole song in a caption.

**The line for captions:** *"With your small hands in my hands."*

**The turn:** the bridge. *"The strongest rivers start as drops, the tallest trees once grew low."* The song's one moment of advice, sung almost as speech.

**Why it can travel:** it is about a parent and a child, with no fight, no break-up and no twist. A child's drawing, a scraped knee and a held hand are shareable images on their own.

## Lyrics as they will be sung

```
[intro]
You hold a pencil like a captain
Gripping hard the wheel,
You draw a house with seven windows
And a garden of a field.

[verse]
You say, this one is for Daddy,
This one's where the flowers grow,
Then you add a little rainbow
To a sky I used to know.
You solve your tiny puzzles
With a focus fierce and bright,
You turn the pieces over
Till the picture comes to light.
You may be small enough to fit
Inside my waiting arms,
But there is something powerful
In all your little charms.

[chorus]
Small hands, big world,
Big dreams in a little girl.
You carry more light
Than the stars in the night.
You teach my heart to see
Who I was and who I can be.
Small hands, big world,
You are my precious girl.
You make me laugh,
You make me strong,
You show me where my heart belongs.
And every day I understand
A better life begins
With your small hands in my hands.

[verse]
You lined your animals up
Across the hallway floor,
The lion was the teacher,
The rabbit guarded the door.
The little bear was sleeping,
The elephant was late,
And you explained the whole plan to me
With a serious little face.
You organise the whole world
In your wonderfully bright way,
You make a home from anything,
A game from any day.
Your mind is full of questions,
Your spirit full of flight,
You find a hundred possibilities
Inside a single night.

[verse]
Sometimes you fall and scrape your knee
And tears begin to rise,
You look at me, then stand again
With courage in your eyes.
I kiss the place that hurts you,
But you're stronger than the pain,
You take a breath and run again
Into the sun and rain.
I wish I could protect you
From every difficult road,
Carry every burden
And lighten every load.
But life will have its lessons,
And you'll learn them as you grow,
I'll be beside you, cheering
Every step you choose to go.

[pre-chorus]
You don't know it, little darling,
But you rescue me each day,
You bring my tired heart back home
In your own special way.

[chorus]
Small hands, big world,
Big dreams in a little girl.
You carry more light
Than the stars in the night.
You teach my heart to see
Who I was and who I can be.
Small hands, big world,
You are my precious girl.
You make me laugh,
You make me strong,
You show me where my heart belongs.
And every day I understand
A better life begins
With your small hands in my hands.

[bridge]
If the world tells you you're too small,
Remember what I know,
The strongest rivers start as drops,
The tallest trees once grew low.
A seed can split the earth apart,
A spark can light the sky,
And you have more inside your heart
Than you can see tonight.
So dream as wide as oceans,
Walk as far as you can see,
Be gentle with the world, my child,
But never hide your wings.
And if you ever lose your way,
I'll help you understand,
You'll always have your father's voice
And a place within his hands.

[chorus]
Small hands, big world,
Brave heart in a little girl.
You carry more hope
Than the wildest wind can blow.
You teach my heart to see
The best that life can be.
Small hands, big world,
You are my precious girl.
You make me laugh,
You make me strong,
You are the reason I belong.
And every day I understand
A better life begins
With your small hands in my hands.

[outro]
Small hands, big world,
My forever little girl.
No matter where you stand,
You'll always hold my hand.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 623 → ~5.4 min at 116 wpm, 90% of frame cap (8056 of 9000 frames) |
| Caption + lyrics tokens | 1672 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 101 | byte-identical |
