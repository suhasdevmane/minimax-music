# Fireworks in February

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-sixth song. Female lead **Mahima**, modern radio pop with bright synth
bells and punchy drums, US register. 112 BPM, G major, mid pacing. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 637 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 112 BPM, G major with no modulation, synth bells stacking an octave per chorus, a drumless piano bridge, and the lot ambience and lighter-click ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a one-look bible for each lead, the security guard as the third character, the two-light-state rule, the real-pyro compositing note and the black-to-gold challenge |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 112 BPM this is a mid-tempo song and the verify script's
116 wpm ballad default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 26-fireworks-in-february
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\26-fireworks-in-february\caption.txt `
  --lyrics-file songs\26-fireworks-in-february\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\26-fireworks-in-february\output\fireworks_in_february.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"wear the big coat"*, *"is this a kidnapping"* and *"more or less"* removed | Punctuation is not sung, and quote marks in the body confuse the phrasing |
| Em-dashes replaced with commas | The model reads them unpredictably |
| Digits spelled out: *a hundred and ten*, *twenty-eight days*, *nine more Februaries* | The model sings digits unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines (*"before the first one"*, *"piano and voice, no drums"*) reduced to plain `[verse]`, `[chorus]` and `[bridge]` | Only the checkpoint's documented tags exist; anything else on a tag line is dropped or sung |
| Every repeated chorus and pre-chorus written out in full | The verify script flags parentheses-only lines, and the model would sing *"repeat"* |
| Three words trimmed in the second verse, bridge and final chorus | The submission ran to 641 sung words, four over the ballad-class budget |

Kept exactly as written: every other line, 112 BPM, G major with no
modulation, the instrumentation, the arrangement-only lift, and the ending
on the drive home.

## The story and the hooks

He texted her at half past ten on a February Tuesday and told her to wear the
big coat. They parked in an empty retail lot between a corral of shopping
carts and one broken light, and he opened the trunk on two flat boxes, a
lighter and a bucket of sand, because months earlier on a bus she had said
she had never seen fireworks up close. Verse two is the evidence of how much
this cost him: a receipt in the glove box for a hundred and ten, a safety
video paused on the dash, a security guard who came out to stop it and sat
down on the curb instead. The bridge is the argument — everybody else circles
a date in red and forgets what it was for. The last chorus is a trade: every
New Year's for one February Tuesday.

**The hook:** *"Fireworks in February, just because you could."*

**The line for captions:** *"Anybody can do December, baby, anyone would."*

**The knife line:** *"And I didn't look up once at the sky going white / I was
watching your face turning gold in the light."*

**The turn:** *"So don't buy me diamonds and don't book me a flight / just
tell me to get in the car on a nothing kind of night."*

**Why it can travel:** it is an anti-occasion love song in a calendar full of
occasions, it has a single cinematic image — an empty parking lot going gold
— and its argument fits in one caption.

## Lyrics as they will be sung

```
[intro]
Second week of February and the whole town's asleep,
Nothing on the calendar and nothing left to keep.
You said, wear the big coat, and you wouldn't tell me why,
Half past ten on a Tuesday in the deadest month alive.

[verse]
We drove past the strip mall and the shuttered garden store,
Parked between the carts where the lot light doesn't go anymore.
I said, is this a kidnapping, you said, more or less,
And your breath came out white and you laughed at my face.
You popped the trunk open and I stood there in the wind,
Two flat boxes, a lighter, and a bucket of sand.
You said, on a bus in November I had mentioned it once,
That I'd never seen one close, and you'd been holding that since.

[pre-chorus]
And the cold got into my shoes and I didn't care,
And the smoke came down slow through the frozen air.
Something in my chest went off before the first one flew,
I have never been the kind of girl this happens to.

[chorus]
Fireworks in February, just because you could,
No birthday, no reason, no occasion, nothing owed.
You lit up an empty parking lot like a town square,
And I finally know what people mean by care.
Fireworks in February and the sky went gold,
Twenty-eight days of nothing and you made one hold.
Anybody can do December, baby, anyone would,
You did fireworks in February, just because you could.

[verse]
There was a receipt in the glove box for a hundred and ten,
More than your insurance will forgive you again.
You had watched a whole video on where to stand back,
And you made me hold the sparkler while you lit the first pack.
The security guard came out and then he just stayed,
Arms folded on the curb like a kid at a parade.
And I didn't look up once at the sky going white,
I was watching your face turning gold in the light.

[pre-chorus]
And the cold got into my shoes and I didn't care,
And the smoke came down slow through the frozen air.
Something in my chest went off before the first one flew,
I have never been the kind of girl this happens to.

[chorus]
Fireworks in February, just because you could,
No birthday, no reason, no occasion, nothing owed.
You lit up an empty parking lot like a town square,
And I finally know what people mean by care.
Fireworks in February and the sky went gold,
Twenty-eight days of nothing and you made one hold.
Anybody can do December, baby, anyone would,
You did fireworks in February, just because you could.

[instrumental]

[bridge]
People wait for a reason, they save it for a date,
Put a circle in red on a square on a page.
Wrap it in ribbon and they leave it by the tree,
And forget halfway through what the whole thing should mean.
So don't buy me diamonds and don't book me a flight,
Just tell me to get in the car on a nothing kind of night.

[chorus]
Fireworks in February, just because you could,
No birthday, no reason, no occasion, nothing owed.
You lit up an empty parking lot like a town square,
And now every February I know what's coming there.
Fireworks in February and the sky went gold,
Twenty-eight days of nothing and you made one hold.
I'd trade every New Year's for the way you stood,
Doing fireworks in February, just because you could.

[post-chorus]
February, February,
Nothing on the calendar and everything in the sky.
February, February,
Twenty-eight days and you picked the coldest night.

[outro]
Ash on the windshield and the heater coming on,
Your hand on the gearshift and the radio off.
Nine more Februaries and I still know the sound
Of the first one going up over an empty lot.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2024 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
