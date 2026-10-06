# Unfollowed

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song sixty-eight. Female lead **Mahima**, contemporary pop with a piano
spine, finger snaps and trap hi-hats, 100 BPM, A minor, US register, with a
half-rapped bridge sung by the same lead. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 619 sung words, mid-tempo budget, no `render.json` |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock, plus a `Rap and Spoken Delivery` line for the half-rapped bridge. 100 BPM, A minor, the piano-snaps-hats arrangement, the kettle and room-tone textures, and the silent bar inside the instrumental. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 77 entries — with a three-look character bible, an ex who is never generated at all, the gallery bridge sequence, workflow, the anticlimax challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 68-unfollowed
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\68-unfollowed\caption.txt `
  --lyrics-file songs\68-unfollowed\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\68-unfollowed\output\unfollowed.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Digits spelled out — *half past one*, *one and two and three* | The model sings digits unpredictably |
| Descriptive tag lines (`[bridge — half-rapped, dry and close]`, `[pre-chorus 1 — hats drop out]`) reduced to plain `[bridge]`, `[pre-chorus]` | Only the documented plain tags exist; text on a tag line is dropped |
| The half-rap direction moved out of the lyric body into the caption's `Rap and Spoken Delivery` line | The model sings the lyric body literally; delivery instructions belong in the caption |
| Every repeated chorus written out in full; the final chorus given its own varied lines six and eight | The model would sing a `(repeat)` marker, and the varied final chorus is where the quiet turns from empty to clear |

Kept exactly as written: the hook, 100 BPM, A minor, the arrangement list,
the twelve-bar bridge and every image in the submission.

## The story and the hooks

She has been rehearsing a two-second act for a season: telling her sister
she will do it in the spring, sitting up past midnight with her thumb above
the glass and putting the phone back down. He was never cruel — that was the
worst of it — he just got quieter until quiet was the weather. On an
ordinary Tuesday with the coffee going cold she presses the button, and
nothing at all happens to her face. Then a week: a park bench, a toddler
losing to a pigeon, a dress in a colour he would have called a lot, a fringe
she will have to live with, and his name said at a dinner table where she
passes the bread and answers like a stranger. The bridge is the confession
underneath it, half-rapped: she had been running a museum with one exhibit
and giving herself the tour at one and two and three. Then she turned the
picture light off.

**The hook:** *"Unfollowed, unbothered, un-yours."*

**The line for captions:** *"I thought that it would feel like losing. It
feels like setting a heavy bag down."*

**The knife line:** *"You were never even cruel, that was the worst of it."*

**The turn:** *"I just took my name off a room I'd been cleaning / Not a
punishment, no flex, not a quiet little war."*

**Why it can travel:** it is the moving-on song that refuses to be a revenge
song, and the hook is three words that already work as a caption. The video
never shows the ex at all, which is the whole joke and the whole point.

## Lyrics as they will be sung

```
[intro]
Tuesday, nothing special, coffee going cold,
My thumb above your name in the usual place,
One small button and one small sound,
And nothing at all happened to my face.

[verse]
I rehearsed it for a season like a speech,
Told my sister I would do it in the spring.
Then I'd sit up past midnight with my thumb above the glass,
And put the phone back down and not do a thing.
You were never even cruel, that was the worst of it,
You just got quieter until the quiet was the norm.
I kept your tab open like a window in a storm,
Let the cold come in and I called that keeping warm.

[pre-chorus]
No speech today, no closing line,
No paragraph I wrote and never sent,
Just a thumb, a quiet little sound,
And a whole year finally spent.

[chorus]
Unfollowed, unbothered, un-yours,
And the sky did not fall down on me,
The kettle clicked, the bus came on time,
The dog next door barked at the tree.
I thought that it would feel like losing,
It feels like setting a heavy bag down.
Unfollowed, unbothered, un-yours,
And nothing in the world made a sound.

[verse]
I took my coffee to the park at half past one,
Watched a kid start a war with a pigeon and win.
Sat there till the light went orange on the water,
And nobody came to ask me where I'd been.
Bought a dress in a colour you would call a lot,
Cut a fringe I am going to have to live with for a while.
Somebody said your name at dinner on the Friday,
I passed the bread and answered with a stranger's smile.

[pre-chorus]
No paragraph, no closing line,
No last look at a face I know by heart,
Just the same small sound in a different week,
And a photograph with your half torn apart.

[chorus]
Unfollowed, unbothered, un-yours,
And the sky did not fall down on me,
The kettle clicked, the bus came on time,
The dog next door barked at the tree.
I thought that it would feel like losing,
It feels like setting a heavy bag down.
Unfollowed, unbothered, un-yours,
And nothing in the world made a sound.

[instrumental]

[bridge]
Let me be honest, I was running a museum,
One exhibit, one man, and the only guide was me.
Every post became a plaque, every photo a display,
And I gave myself the tour at one and two and three.
I called it keeping up, I called it being kind,
It was homework on a person who had already resigned.
And the truth is not dramatic, it is boring and it's plain,
You don't get a lightning bolt, you get a Tuesday and some rain.
So I didn't write a paragraph, I didn't make a scene,
I just took my name off a room I'd been cleaning.
Not a punishment, no flex, not a quiet little war,
Just a door I had been holding, and I'm not holding it anymore.

[chorus]
Unfollowed, unbothered, un-yours,
And the sky did not fall down on me,
The kettle clicked, the bus came on time,
The dog next door barked at the tree.
I thought that it would feel like losing,
It feels like the first clean morning in a year.
Unfollowed, unbothered, un-yours,
And the quiet is not empty, it is clear.

[post-chorus]
Unfollowed in the morning, unbothered by the night,
Un-yours by the time the streetlights came on,
Unfollowed, unbothered, un-yours,
And the day just carried on.

[outro]
Coffee going cold on a table by the window,
A fringe I'm still getting used to in the glass,
Somebody will ask me and I'll tell them it went fine,
And it will be the truth, at last.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 619 → ~5.3 min at 116 wpm, 89% of frame cap |
| Caption + lyrics tokens | 2138 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
