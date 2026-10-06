# Never Yours to Break

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-six. Female lead **Mahima**, cinematic pop with orchestral scale
and a modern low end — felt piano, full string section, choir pad and a deep
808. 92 BPM, E minor lifting to G major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 638 sung words, ballad pacing class, tightened line by line to fit the budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 92 BPM, E minor with the modulation to G, felt piano, strings, choir, 808, and the thunder-and-rain-on-glass ambience per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 75 entries — built from the submission's scene direction, plus a three-look character bible, a faceless ex who never enters the house, the glass-never-breaks rule, workflow, the standing-still challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 76-never-yours-to-break
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\76-never-yours-to-break\caption.txt `
  --lyrics-file songs\76-never-yours-to-break\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\76-never-yours-to-break\output\never_yours_to_break.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Every line tightened by one to two words | The submission ran 726 sung words, well over the 640-word ballad budget; the meaning and the rhyme scheme are unchanged, the padding is gone |
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Digits spelled as words | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – single low piano note, thunder, rain on glass]*, *[verse 2 – piano and 808, strings low]*, *[final chorus – modulation to G]*) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the checkpoint's documented tags exist; anything else is dropped or sung |
| The repeated second chorus written out in full | `(repeat)` in the body would be sung as the word |
| All performance and arrangement direction moved into `caption.txt` | Stage directions in the lyric body get sung |

Kept exactly as written: the story, the property metaphor, 92 BPM, E minor
with the lift to G, the instrumentation, the mood arc, the bridge admission.

## The story and the hooks

He has been telling people he broke her. She answers once, calmly, and the
answer turns out to be an argument about ownership. He took the mirror off
the wall and the salt off the sill and a jacket and a playlist and a Sunday —
and that is the entire inventory. He never took the roof, never touched the
wiring, never had a hand on the frame. Every crack he likes to point at was
put there by her, years before she heard his name. The bridge refuses to be
smug about it: she lost sleep, lost weight, lost a friend, sat in a car
outside a house she does not drive to any more. Then it withdraws all of that
from him. He was weather, and the town spent all night waiting for the sound
of a glass house coming down that never came.

**The hook:** *"My heart was never yours to break"* — the title lands on the
last line of every chorus, held rather than belted.

**The line for captions:** *"You were weather. I have lived through harder
weather."*

**The knife line:** *"You never held a key, never held the deed."*

**The turn:** *"But hurting isn't ruin, a bruise is not a wound, / and
nothing you carried out of here was mine."*

**Why it can travel:** the property framing gives a very familiar feeling a
line nobody has used on it, and the video is one image — a lit glass house in
a storm that does not break — which is a single shareable frame rather than a
montage. It is a strength record that never raises its voice.

## Lyrics as they will be sung

```
[intro]
A house of glass at the edge of the hill,
And the town waited to hear it come down.
Thunder came in like it had something to prove,
Wind on the panes, rattling the ground.
I stood in the middle, hands at my sides,
And let the sky throw all that it had.

[verse]
You came in like a season, you left like a bill,
Took the mirror off the wall, the salt off the sill.
Told your friends a version where I came apart,
Where you did the holding and I did the harm.
I was never once the thing that you dropped,
I was the floor you stood on while you talked.
Every crack you point at, I put there myself,
Long before I heard your name from someone else.

[pre-chorus]
You tell it like a rescue that went wrong,
Like the roof caved in the second you left.
Come and see it then, come stand in my doorway,
There's nothing on this floor to sweep up yet.

[chorus]
You call it a wreckage, I call it a home,
Windows intact and the lights still on.
Say that you broke me if it helps you sleep,
You never held a key, never held the deed.
I was standing here before you learned my name,
Still in the storm, and I'm not the one who changed.
Say it loud, say it twice, whatever it takes,
My heart was never yours to break.

[verse]
Heard you tell it a different way this winter,
That the girl in your version got quieter each year.
Funny, I've been loud in every room I walk in,
And none of them has watched me disappear.
You took a jacket and a playlist and a Sunday,
And a couple of the words I don't say the same.
You never took the roof, never touched the wiring,
Never had a hand on the frame.

[pre-chorus]
You tell it like a rescue that went wrong,
Like the ceiling came down when you were gone.
Come and see it then, come knock on the glass,
Same house, still standing, the storm already passed.

[chorus]
You call it a wreckage, I call it a home,
Windows intact and the lights still on.
Say that you broke me if it helps you sleep,
You never held a key, never held the deed.
I was standing here before you learned my name,
Still in the storm, and I'm not the one who changed.
Say it loud, say it twice, whatever it takes,
My heart was never yours to break.

[instrumental]

[bridge]
I won't pretend it didn't hurt, because it did,
Months I couldn't hear your name out loud.
Lost the sleep, lost the weight, lost a friend or two,
Sat outside a house I don't drive to now.
But hurting isn't ruin, a bruise is not a wound,
And nothing you carried out of here was mine.
You were weather. I have lived through harder weather.
The lights are on in every window down the line.

[chorus]
You call it a wreckage, I call it a home,
Every light in every window, and I turned them on.
Say that you broke me if it helps you sleep,
You never held a key, never held the deed.
I was standing here before you learned my name,
Still in the sunrise, and I'm not the one who changed.
Say it loud, say it twice, whatever it takes,
My heart was never yours to break.

[post-chorus]
Never yours, never yours,
Not the windows, not the walls, not the doors.
Never yours, never yours to take,
Never yours, and it never was yours to break.

[outro]
A house of glass at the edge of the hill,
And the town got tired of waiting for the fall.
Morning came in gold on the floor of the hall,
And it never was your house at all.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2070 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
