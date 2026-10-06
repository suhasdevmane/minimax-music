# Windows Down

**Status: written and verified, NOT rendered. Not yet in the queue.**

Forty-fifth song. Female lead **Mahima**, pop-rock road anthem with driving
guitars and big floor toms, 128 BPM, E major lifting a whole step for the
final chorus. Uptempo, solo. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, cleaned for the model |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 128 BPM, E major with the whole-step lift, driving guitars, floor toms, the gang-chant post-chorus, tyre hiss and engine textures. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 80 entries — built from the submission's scene direction, plus a three-look character bible, a faceless cashier, the car and its objects, workflow, the four-insert challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 45-windows-down
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\45-windows-down\caption.txt `
  --lyrics-file songs\45-windows-down\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\45-windows-down\output\windows_down.wav
```

Expected ~2 h.

## Pacing note before rendering

**Pacing is estimated, not measured.** The ballads in this catalogue sang at
116–153 words per minute. This one is 128 BPM with a chant post-chorus, which
will pace faster. The lyrics are 756 words. At the guard setting of 140 wpm
that is ~5.4 minutes, 90% of the model's 6-minute cap; at 116 wpm it would
overrun and lose the outro, at 160 wpm it lands near 4.7 minutes. The two
post-chorus chants are fast, so a blended 145–155 wpm is the reasonable
guess. **If the first render truncates the outro, drop the second
post-chorus (28 words, a repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| `6:15` → *"a quarter past six"* | The model sings digits unpredictably |
| Quotation marks around *busy* removed | Punctuation is not sung |
| `[verse 1]`/`[verse 2]`, `[final chorus]` and the descriptive tag lines reduced to plain tags | The model only knows plain section tags |
| The second chorus written out in full instead of `(repeat)` | The model would sing the word repeat |

Kept exactly as written: every lyric line, 128 BPM, E major with the lift,
the instrumentation, the mood arc. 756 words fits the uptempo budget.

## The story and the hooks

She takes a car and a coast road on a Saturday with nowhere to be. Out of the
sleeping city at a quarter past six, the exit with the funny name, elbow out
the window, the sea appearing over a hill. A petrol station with sticky
sweets and fuzzy dice, a hidden beach where she writes her name in the tide
line and lets a wave take it. The sun comes down, the glovebox turns out to
be where freedom was all along, and she hands the feeling to whoever is
stuck on a Tuesday. The final chorus is sunset on the dashboard; the outro is
an empty tank at a harbour wall and no intention of stopping.

**The hook:** *"Windows down, volume up, nowhere left to be"* — a caption, a
chant, and the whole song in seven words.

**The line for captions:** *"Got a full tank of nothing and I've never felt
so free."*

**The turn:** *"I used to think that freedom was a place I had to find / But
it was in the glovebox all along."*

**The quote:** *"You don't need a reason and you don't need a map."*

**Why it can travel:** it is built for driving playlists and road-trip
reels at a tempo they actually use, the post-chorus is a four-shot template
anyone can film from a car, and it is joyful without needing a heartbreak
behind it.

## Lyrics as they will be sung

```
[intro]
Keys in the cup holder, sunglasses on,
Half a tank of anything and the whole day gone.
Tell the phone I'm busy, tell the map to guess,
I'm not lost, I'm just somewhere I haven't been yet.

[verse]
Left the city sleeping at a quarter past six,
Coffee in a paper cup, a playlist of my picks.
Took the exit with the funny name because I liked the sound,
Traded all my deadlines for a road that never ends downtown.
Elbow out the window and the wind is in my teeth,
Every mile marker is a promise I get to keep.
Nobody in the passenger seat telling me to slow,
Just the yellow line, the radio, and everywhere to go.

[pre-chorus]
And the sky is so wide it could swallow me whole,
And the song that comes on is the one that I know.
Turn it up till the speakers start shaking the door,
This is what a Saturday was invented for.

[chorus]
Windows down, volume up, nowhere left to be,
Hair a mess, heart a wreck of sunshine and speed.
Sing it loud to the cliffs, let the ocean sing it back,
Every wrong turn is right when it's mine, and I'm not turning back.
Windows down, volume up, nowhere left to be,
Got a full tank of nothing and I've never felt so free.
So I'll drive till the coast road runs out of sea,
Windows down, volume up, nowhere left to be.

[post-chorus]
Nowhere left to be, nowhere left to be,
Foot down, top down, just the road and me.
Nowhere left to be, nowhere left to be,
Volume up, windows down, and I'm free.

[verse]
Petrol station, sticky counter, sweets I haven't had in years,
The cashier asks me where I'm headed and I laugh into my hair.
Bought a map that I won't open and some dice to hang from the mirror,
Filled the tank and filled my lungs, and the picture just got clearer.
Pulled over where the road bends, kicked my shoes onto the sand,
Wrote my name into the tide line, watched it vanish from my hand.
Not a single notification worth the view I've got right now,
I've got salt inside my eyelashes and I forgot how to frown.

[pre-chorus]
And the sun's getting low like it's coming to sit,
And the chorus comes round and I know all of it.
Turn it up till the seagulls are singing along,
This is what a good day sounds like in a song.

[chorus]
Windows down, volume up, nowhere left to be,
Hair a mess, heart a wreck of sunshine and speed.
Sing it loud to the cliffs, let the ocean sing it back,
Every wrong turn is right when it's mine, and I'm not turning back.
Windows down, volume up, nowhere left to be,
Got a full tank of nothing and I've never felt so free.
So I'll drive till the coast road runs out of sea,
Windows down, volume up, nowhere left to be.

[instrumental]

[bridge]
I used to think that freedom was a place I had to find,
A city or a person or a sign.
But it was in the glovebox all along,
Under the receipts and the sunscreen and the songs.
So if you're stuck on a Tuesday with the week around your neck,
Take the keys, take the coast, take the whole sunset,
You don't need a reason and you don't need a map,
You just need the windows down and a road that opens up.
I'm not running from anything, I'm running with the light,
And the engine's humming something that sounds a lot like mine.

[chorus]
Windows down, volume up, nowhere left to be,
Sunset on the dashboard turning everything to gold and me.
Sing it loud to the dark, let the headlights sing it back,
Every wrong turn was right, it was mine, and I'm not turning back.
Windows down, volume up, nowhere left to be,
Got a full tank of nothing and I've never felt so free.
So I'll drive till the stars run out of sea,
Windows down, volume up, nowhere left to be.

[post-chorus]
Nowhere left to be, nowhere left to be,
Foot down, top down, just the road and me.
Nowhere left to be, nowhere left to be,
Volume up, windows down, and I'm free.

[outro]
Keys in the cup holder, sunglasses off,
The tank says empty but it doesn't say stop.
Tell the phone I'm sorry, tell the map I'm home,
Wherever this road ends is wherever I'll go.
Wherever this road ends is wherever I'll go.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 756 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing note above) |
| Caption + lyrics tokens | 2400 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
