# Blocked and Blooming

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-four. Female lead **Mahima**, Afro-pop with modern pop polish —
log drums, highlife-leaning guitar and shakers under a conversational
Western pop vocal. 108 BPM, F major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 621 sung words, ballad/mid pacing class, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 108 BPM, F major, log drums, bright guitar, shakers, talking drum, and the blind-and-birdsong ambience per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 77 entries — built from the submission's scene direction, plus a three-look character bible, a completely unseen ex, a faceless friend, the recurring grey cat, workflow, the December-to-May challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 74-blocked-and-blooming
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\74-blocked-and-blooming\caption.txt `
  --lyrics-file songs\74-blocked-and-blooming\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\74-blocked-and-blooming\output\blocked_and_blooming.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Digits spelled as words (*three flights*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – guitar, shaker, one late log-drum hit]*, *[verse 1 – the groove settles]*, *[final chorus – biggest arrangement]*) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the checkpoint's documented tags exist; anything else is dropped or sung |
| The repeated second chorus and the final chorus written out in full | `(repeat)` in the body would be sung as the word |
| All performance and arrangement direction moved into `caption.txt` | Stage directions in the lyric body get sung |

Kept exactly as written: every lyric line, 108 BPM, F major, the
instrumentation, the five-month mood arc, the running grey cat.

## The story and the hooks

She blocks him in December — no scene, no last speech, just a thumb and a
button — and then does the only thing she can think of with her hands: she
buys a bag of soil. Terracotta pots on a rusty rail, basil in a chipped mug,
cuttings rooting in a jam jar, and a neighbour's grey cat that becomes the
first thing since the breakup that shows up and stays. By March the window
is fully open, bougainvillea is hanging over the road, and when she runs into
his friend at a fruit stand with a fig tree on her hip she has no free hand
to care with. The bridge admits how long it actually took — cereal at the
sink, a dry cracked pot — and points at what was happening under the soil
the whole time. By May the flat is a jungle and she is giving cuttings away.

**The hook:** *"Blocked and blooming, look at me now"* — three words that
work as a caption, a bio and a before-and-after.

**The line for captions:** *"Everything green that I grew out of spite."*

**The knife line:** *"Both hands were full and I liked it like this."*

**The turn:** *"I thought the block button was the end of the story, /
turns out it was only the ground cracking open."*

**Why it can travel:** the plants are literal, not a metaphor she reaches
for, so the video is a genuine five-month before-and-after that anyone with
a windowsill can film. The groove is warm enough for a summer playlist and
the message is growth rather than revenge.

## Lyrics as they will be sung

```
[intro]
December, and my thumb was on your name,
One little button and the noise went away.
No last speech, no argument, no scene,
Just a quiet little room and a girl and a screen.
I didn't cry, I just opened a blind,
And let the cold light in for the first time.

[verse]
Bag of soil on a Saturday morning,
Three flights up with the sun coming warm in.
Terracotta pots and a secondhand rail,
Basil in a mug and a mint that won't fail.
Cuttings in a jam jar, roots like white thread,
Something in this apartment is finally getting fed.
The neighbour's grey cat comes and sits on my chair,
First thing since December that showed up and cared.

[pre-chorus]
They told me give it a season, give it time,
So I gave it water and a place in the light.
Now the balcony's greener than the day that you left,
And nothing out here has asked about you yet.

[chorus]
Blocked and blooming, look at me now,
Dirt on my hands and a sun in the house.
You were a winter I finally survived,
Now every window in here is alive.
Blocked and blooming, I water the light,
Everything green that I grew out of spite.
Call it a garden, call it a crown,
Blocked and blooming, look at me now.

[verse]
March came in and I opened the whole window,
Bougainvillea leaning pink on the road below.
Learned the names from a book at the library,
Learned which ones wilt when you love them too heavy.
Ran into your friend by the fruit stand on Sunday,
Said that you'd been asking how I was doing lately.
I had dirt on my knuckles and a fig on my hip,
Both hands were full and I liked it like this.

[pre-chorus]
They told me give it a season, give it time,
So I gave it water and a place in the light.
Now the whole place smells like something that grew,
And not one single leaf in here is for you.

[chorus]
Blocked and blooming, look at me now,
Dirt on my hands and a sun in the house.
You were a winter I finally survived,
Now every window in here is alive.
Blocked and blooming, I water the light,
Everything green that I grew out of spite.
Call it a garden, call it a crown,
Blocked and blooming, look at me now.

[instrumental]

[bridge]
I thought the block button was the end of the story,
Turns out it was only the ground cracking open.
Some love is a drought that you walk away thirsty,
Some love is the rain that you're owed and get late.
I won't pretend that I did all of it pretty,
There were weeks I ate cereal standing at the sink.
But under the dirt the small roots kept working,
Quiet as anything, further than you think.

[chorus]
Blocked and blooming, look at me now,
Green on the railing and the door swinging out.
You were a winter I finally survived,
Now every window in here is alive.
Blocked and blooming, I water the light,
Everything golden that I grew out of spite.
Call it a garden, call it a crown,
Blocked and blooming, look at me now.

[post-chorus]
Look at me now, look at me now,
Feet on the tile and the speaker turned loud.
Look at me now, look at me now,
Everything I planted in the cold came round.
Look at me now, look at me now,
Blocked and blooming and I'm never coming down.

[outro]
December, and my thumb was on your name,
That one little button and the noise went away.
Now it's May and the balcony's a jungle in the sun,
Blocked and blooming, and the growing's just begun.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 621 at 116 wpm → ~5.4 min, 89% of frame cap |
| Caption + lyrics tokens | 2001 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
