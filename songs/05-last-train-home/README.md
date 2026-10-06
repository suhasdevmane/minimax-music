# Last Train Home

**Status: re-render queued** (after song 6) with the character name removed
from the bridge. The first take is archived at
`output/v1-with-name/last_train_home.wav`; the facts below describe it and
will be replaced when the new take lands.

## Render facts (v1, archived)

| | |
|---|---|
| Seed | 42 |
| Length | 311.12 s (5:11) — 626 words at ~121 wpm, close to the estimate |
| Format | 44.1 kHz stereo, peak 1.000, **278 clipped samples** out of 13.7 million (0.002%, inaudible, but the most of the batch — see note), 0.18% silence |
| Ending | clean fade (last 0.5 s at 0.004) |
| Envelope | 0.11 intro → 0.14–0.18 choruses → 0.09 dip at the bridge absence → 0.16 final chorus; matches the arc |
| Spectral balance vs song 1 | sub-bass band lower (12.5 vs 17.8) — consistent with the caption's "soft 808s" and lighter electronic production; mids and highs match |
| Render time | 7393 s generation, 7423 s total (2 h 04 m), peak VRAM 6.2 GB |
| Sidecar | `output/last_train_home.json` |

Clipping note: the model's output peaks at exactly 1.0 and the WAV writer
hard-clips anything above it. Counts across the batch were 0 / 6 / 33 / 278
samples — all inaudible, but the trend suggests adding a peak-normalise
step (scale to −1 dBFS) in `generate.py` before the next batch.

Not yet listen-checked: whether "Mahima" is sung clearly once in the bridge,
and whether the hard cut in mood at *"seven p.m."* comes through.

Fifth song. Female lead **Mahima**, cinematic indie-pop / soft electronic
ballad, nocturnal. Same voice as songs 1–4.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission nearly complete, one stanza cut (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` blocks byte-identical to song 1 — the voice lock. Tempo, key, instrumentation and the train-sound ear candy follow the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | 43 lyric-anchored shots, character bible (Mahima + Theo), workflow, teaser, the note as UGC hook, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render

From the repo root:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\05-last-train-home\caption.txt `
  --lyrics-file songs\05-last-train-home\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\05-last-train-home\output\last_train_home.wav
```

Verify first:

```powershell
.\.venv\Scripts\python.exe scripts\verify_lyrics.py songs\05-last-train-home --voice-ref songs\01-fire-in-the-rain
```

Estimated render: **~2 h 15 min** on the RTX 4090 Laptop.

## What changed from the submission, and why

This one fit almost as written. **626 words ≈ 5.4 min, 90% of cap.**

| Change | Why |
|---|---|
| Cut verse 2, stanza 2 (*"I started saving them in a box… when my week got weak"*, 30 words) | Only cut needed to stay under the safety line. It also repeats the shoebox-of-keepsakes image that is the whole premise of song 4, so losing it keeps the two songs distinct. Everything else is verbatim. |
| `2:13` → *"two-thirteen"*, `7 p.m.` → *"seven p.m."*, `2 a.m.` → *"two a.m."* | The model sings digits unpredictably; spelled-out numbers are safe |
| *"That the director forgot to **mass**"* → *"That the **film** forgot to **cast**"* | "mass" reads as a typo and has no meaning in the line; "cast" keeps the sense and a slant rhyme with "glass" |
| Quotation marks and em-dashes removed; `[final chorus – bigger, fuller]` and the `[intro – …]` / `[outro – …]` tags reduced to `[chorus]`, `[intro]`, `[outro]`; the instrumental's parenthetical moved into the caption | The model sings the lyric body literally and only knows the plain section tags |

Kept exactly as written: the key and tempo (98 BPM, E minor, lifting toward
G major for the final chorus), the instrumentation, the mood arc, the
optional second voice on the final hook (song 1's `Harmony` line already
provides it), and the station announcement as very low ear candy.

## The story and the hook

Two strangers on the last train, night after night, 2:13 a.m., platform
three. A dropped pen. A note in a seat pocket: *"Long days, longer nights,
but somehow I'm still here. Are you?"* Song titles on receipts. A question
they never answer. Then one night he isn't there, and she rides the whole
line and back, watching every face. Weeks. Then a Tuesday at seven p.m., in
daylight, on the platform, not the train — and he tells her he stopped
taking the last train. (The character's name is never sung; it lives in the
video only. Re-rendered 2026-09-03 to remove it; the earlier take is in
`output/v1-with-name/`.)

**The hook:** *"On the last train home / We built a world no one knows."*

**The line for the note, and the UGC prompt:** *"Still here. Still tired.
Still trying."*

**The turn:** *"Got tired of almosts and maybes / Wanted a start, not an
in-between."*

**The last line:** *"A first step, not a last one."*

**Why it can travel:** it isn't a together-song or a breakup-song. It's the
almost — and then the choice. The visual world is one location and two
props, which makes it cheap to shoot and instantly recognisable.

## Lyrics as they will be sung

```
[intro]
Two-thirteen a.m., platform three,
Same train, same seat, same view.
You always stand by the second door,
Headphones on, looking at the floor.
I never say hi, you never do,
But sometimes our eyes meet through the glass.
And for one stop, the whole ride feels
Like it's only us, and everyone else is past.

[verse]
First week, you wore that black hoodie,
Scrolling through songs I couldn't hear.
I wondered what you were listening to,
If your day was heavy, if you were ok here.
Second week, you dropped a pen,
I picked it up, you said thanks so low.
Your voice was softer than I imagined,
And I pretended I didn't watch you go.
Third week, you left a note
In the pocket of the seat in front,
Long days, longer nights, but somehow
I'm still here. Are you? in your font.
I wrote back underneath in pencil,
Still here. Still tired. Still trying.
Folded it small, left it for you,
Heart beating loud as the train lights died.

[pre-chorus]
We never said names, never asked why,
Just two strangers sharing the same sky.
But every night at two-thirteen,
I started living for that seat.

[chorus]
On the last train home,
We built a world no one knows.
In the space between stations,
We said everything without words.
On the last train home,
I almost told you I'm not okay alone.
But the doors opened, you stepped out,
And I stayed quiet with my almost-love.

[verse]
You started leaving song titles,
Little scribbles on old receipts,
Listen to this when you're feeling small,
Play this when the city sleeps.
One night you wrote, what if we
Got off at the same stop someday?
Not by accident, not by habit,
But because we chose to stay.
I stared at those words till my stop came,
Walked out with your note in my hand.
That night I didn't sleep at all,
Just rehearsing what I'd say if you asked.

[pre-chorus]
But you never asked, I never said,
We kept dancing around what we felt.
Two ghosts on the last train home,
Afraid to be real, afraid to melt.

[chorus]
(repeat)

[instrumental]

[bridge]
Then one night you weren't there.
Same time, same seat, same door.
I sat down, tried to pretend
You were just late, not gone for good.
I rode the whole line and back,
Watching every face through the glass.
Hoping you'd appear like a scene
That the film forgot to cast.
Weeks passed. I kept the notes,
Kept riding, kept checking the door.
The train felt longer, quieter,
Like a story missing its core.
Then last Tuesday, seven p.m.,
Not two a.m., not the last ride.
I saw you standing on the platform,
Same hoodie, but different eyes.
You looked up, saw me, smiled,
Said, I stopped taking the last train.
Got tired of almosts and maybes,
Wanted a start, not an in-between.

[chorus]
So I stepped off the last train home,
Walked toward you through the crowd.
No more notes, no more stations,
Just your name, finally loud.
We didn't need the last train now,
To say what we couldn't before.
You said, let's go somewhere else,
And I said, yes. Let's walk out that door.

[outro]
Now when I think of two-thirteen,
I don't see the train or the seat.
I see your hand in mine,
Walking away from the almost-we.
On the last train home,
We were a beautiful almost-love.
But now we're something better,
A first step, not a last one.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 626 → ~5.4 min, 90% of frame cap |
| Caption + lyrics tokens | 1993 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
