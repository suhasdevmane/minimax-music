# Mango Season

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixty-fifth song. Female lead **Mahima**, Bollywood-folk pop with a modern
kick, memories and childhood, Indian-English register with no slang. 104 BPM,
D major lifting a whole step to E on the final chorus. Same singer as songs
1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 104 BPM, D major with the whole-step lift, dholak and tabla fills, bansuri flute, nylon-string guitar, modern kick, and the train, station bell, ceiling fan, radio crackle and monsoon textures per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 82 entries — built from the submission's scene direction, plus a four-look character bible, seven named children, the train-window bookend rule, workflow, the first-rain challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json` — 104 BPM is mid-pace and the 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 65-mango-season
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\65-mango-season\caption.txt `
  --lyrics-file songs\65-mango-season\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\65-mango-season\output\mango_season.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Descriptive tag lines (`[intro – flute and guitar, the train]`, `[chorus – wide, golden, everything in]`, `[bridge – quiet, near-spoken, then the decision]`, `[final chorus – whole step up, fullest]`, `[post-chorus – chant with claps]`) reduced to plain tags | Only the checkpoint's documented tags exist; anything else in a tag line is dropped or sung |
| `[final chorus]` → `[chorus]`, and both repeated choruses written out in full rather than marked as a repeat | The model sings the body literally and would sing the word repeat |
| The performance notes in the section headings — near-spoken, chant with claps, whole step up — moved into `caption.txt` | Stage directions in the lyric body get sung |

Kept exactly as written: every lyric line, word for word. 104 BPM, D major
with the whole-step lift on *"I am going back"*, the instrumentation, the
mood arc, the plain Indian-English register with no slang, the bookended
station. No trimming was needed — 606 words fits.

## The story and the hooks

A train slowing into a one-lamp station and a grandfather waiting with his
bicycle. A steel trunk on a rickshaw roof, six cousins hanging off the gate,
a grandmother counting heads. A mango tree climbed before anyone could stop
them, raw slices with salt and chilli on a low wall, a ceiling fan that
stops and nobody minds. Then the present — a glass office that shows only
concrete and a mango sealed in plastic that will never be sweet. The second
verse is the grandfather's radio and the cricket score, kites over the roof,
pickle jars drying on the top step, and a grandmother who saved the sweetest
mango because the mangoes know when you are coming. The wind turns, the
crows go quiet, and seven children run the wrong way, out into the first
rain. In the bridge the house is smaller, the bicycle is rusting against the
wall, the cousins are in seven cities — and she buys the ticket. The final
chorus is sung on the train, and the outro is the same platform with nobody
on it and a girl who still knows the way.

**The hook:** *"Take me back to mango season"* — four words, entirely
visual, and it turns into *"I am going back"* on the last chorus, which is
the whole song in one edit.

**The line for captions:** *"She said the mangoes know when you are coming."*

**The turn:** *"So this year I am buying the ticket, / This year I am going
home."* Longing becomes a decision, and the hook changes tense to prove it.

**The chant:** *"Sweet on the tongue, salt on the skin, / Sun on the roof
and the rain coming in."*

**Why it can travel:** every household in the subcontinent and its diaspora
has this summer, and the images are specific enough to be true and common
enough to be shared — a gate, a tree, a terrace, a first rain. The bookend
(a child's hand on the train window bars, then the same hand grown) gives
the video a single frame people will screenshot.

## Lyrics as they will be sung

```
[intro]
The train slows down at a station with one lamp,
My grandfather waiting with his cycle and a smile.
The dust smells sweet and the air is heavy,
I can taste the summer from a mile.

[verse]
Steel trunk tied to the roof of a rickshaw,
Cousins hanging off the gate before we stop.
Grandmother counting heads at the doorway,
Seven children, one house, one water pot.
We climbed the tree before they told us not to,
Raw mango, salt and chilli, sitting on the wall.
The fan went off, the power came and went,
And nobody minded at all.

[pre-chorus]
Now the city keeps me busy, keeps me tired,
Every summer looks the same from here.
The office window only shows me concrete,
A mango in the supermarket, wrapped in plastic, never sweet.
But I close my eyes and I am nine years old,
And the sky is about to break, I can feel it near.

[chorus]
Take me back to mango season,
Yellow hands and a sticky chin.
Take me back to mango season,
Bare feet in the courtyard, let me in.
Cousins on the terrace, cots in a row,
Counting every star we did not know.
The first rain came early that year,
Take me back to mango season, take me there.

[verse]
Grandfather's radio and the cricket score,
The whole street leaning in to hear.
An afternoon so long it had no ending,
Kites above the roof, a string cut, a cheer.
Grandmother's hands and the smell of pickle jars,
Drying in the sun on the top step.
She said the mangoes know when you are coming,
So she saved the sweetest one, a promise that she kept.

[pre-chorus]
Then one evening the wind turned over,
Dust rose up and the crows went quiet.
Grandmother calling from the kitchen doorway,
Bring the clothes in, bring the clothes in, run.
We ran out to the courtyard laughing,
Faces up, we caught the first of it.

[chorus]
Take me back to mango season,
Yellow hands and a sticky chin.
Take me back to mango season,
Bare feet in the courtyard, let me in.
Cousins on the terrace, cots in a row,
Counting every star we did not know.
The first rain came early that year,
Take me back to mango season, take me there.

[instrumental]

[bridge]
The house is smaller now, the tree is taller,
His cycle still leans against the wall.
The cousins live in seven different cities,
Nobody writes a letter, we just call.
But every June when the heat gets heavy,
And the first cloud comes in slow,
I stand out on my balcony in the city,
Face up, and I am nine, and I still know.
So this year I am buying the ticket,
This year I am going home.

[chorus]
I am going back to mango season,
Yellow hands and a sticky chin.
I am going back to mango season,
Bare feet in the courtyard, let me in.
Cousins on the terrace, cots in a row,
Same old stars, I still do not know.
The rain will come early, I can feel it,
I am going back to mango season, back to the beginning.

[post-chorus]
Sweet on the tongue, salt on the skin,
Sun on the roof and the rain coming in.
Sweet on the tongue, salt on the skin,
Take me back, take me back, let me in.

[outro]
The train slows down at a station with one lamp,
Nobody waiting, but I know the way.
I walk the lane with my shoes in my hand,
Somebody's children hanging off the gate.
The dust smells sweet and the air is heavy,
And the mango tree is still there today.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 606 → ~5.2 min at 116 wpm, 87% of frame cap |
| Caption + lyrics tokens | 2330 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
