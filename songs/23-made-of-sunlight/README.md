# Made of Sunlight

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-third song. **Female + male duet** — Mahima on the calling half of
every hook line, Kai answering — Afrobeats-pop with highlife guitar and a
crossover pop chorus. 106 BPM, F major, mid pacing. Same singer as songs 1–8
for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 620 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock — with Singer B added as `Duet Partner` and a line-by-line `Duet Structure`. 106 BPM, F major, log drums, highlife guitar, brass and a talking drum through the break. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look bible for Mahima, Kai's single look, no antagonist, the orange-and-blue rule, the blackout beat and the two-count dance challenge |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 106 BPM this is a mid-tempo song and the verify script's
116 wpm ballad default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 23-made-of-sunlight
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\23-made-of-sunlight\caption.txt `
  --lyrics-file songs\23-made-of-sunlight\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\23-made-of-sunlight\output\made_of_sunlight.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"come on, walk"*, *"what are you made of"* and *"guess"* removed | Punctuation is not sung, and quote marks in the body confuse the phrasing |
| Em-dashes replaced with commas | The model reads them unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines (*"her, teasing"*, *"the power cuts"*) reduced to plain `[verse]` and `[chorus]` | Only the checkpoint's documented tags exist; anything else on a tag line is dropped or sung |
| Every repeated chorus and pre-chorus written out in full | The verify script flags parentheses-only lines, and the model would sing *"repeat"* |
| The call-and-response split moved out of the lyric body into the caption's `Duet Structure` line | The model has no per-line singer control; the split lives in the caption |

Kept exactly as written: every lyric line, 106 BPM, F major with no
modulation, the instrumentation, the blackout bridge, and the arrangement
lift built from brass and group vocals rather than a key change.

## The story and the hooks

Two people in a beach town pass one question back and forth all evening —
what are you made of — and answer it with whatever is nearest: sea glass,
engine oil, salt, sand, mango skin, the drum at the end of the road. Verse
one is her guessing at him in two plastic chairs while the street picks up
his step. Verse two is the next morning, wet market, a fish-stall auntie
telling them they move like one song, and him finally answering. Then the
power cuts in the middle of the party, the drums keep going, and the dance
restarts in lantern light before a generator coughs the bulbs back on. There
is no obstacle in this song and nothing goes wrong in it. That is the point.

**The hook:** *"You're made of sunlight, I'm made of you"* — a call and an
answer, built for two people in one frame.

**The line for captions:** *"Ask me what I'm made of, I will answer again."*

**The turn:** *"So let the generators cough and the lanterns come out / we
were never dancing for the bulbs anyhow."*

**The chant:** *"Oh, the orange and the blue."*

**Why it can travel:** the chorus is an exchange rather than a statement, so
duet clips write themselves; the post-chorus is the easiest choreography in
the catalogue; and the whole record is joy with no complaint in it, which is
rarer than heartbreak and shares harder.

## Lyrics as they will be sung

```
[intro]
Orange on the water and the blue coming down,
Somebody's speaker going wild at the end of the town.
You put your hand out flat and you said, come on, walk,
And the whole evening changed the way it talked.

[verse]
You came down the beach road with your shirt undone,
Two plastic chairs, a cooler and the last of the sun.
The barber's radio was older than the both of us,
But you had the whole street moving with your hands up.
I said, what are you made of, and you laughed and said, guess,
So I started at your hands and I gave it my best.
Sea glass, engine oil, and a laugh like a bell,
And whatever else it is, it wears on you well.

[pre-chorus]
Then the drum comes in and the drum comes in,
And the whole town leans the way the evening leans.
Put your hand in my hand, let the horns begin,
Ask me what I'm made of, I will answer again.

[chorus]
You're made of sunlight, I'm made of you,
Made of the salt and the sand and the blue.
Say it out loud where the whole street hears,
Say it over log drums, say it in my ear.
You're made of sunlight, I'm made of you,
Made of the drum and the dust and the truth.
Whatever I am, I was made in your hands,
So I'm made of you.

[verse]
You came in from the market with the mangoes and the rain,
Orange on your fingers, half the ocean in your hair.
The auntie at the fish stall said we move like one song,
And I have not stopped humming it, so she was not wrong.
You asked me what I'm made of, so I'll answer you now,
Since the night you said my name I have not put it down.
Cold glass, warm asphalt, and the sound of your feet,
And a street that plays your name on every beat.

[pre-chorus]
Then the drum comes in and the drum comes in,
And the whole town leans the way the evening leans.
Put your hand in my hand, let the horns begin,
Ask me what I'm made of, I will answer again.

[chorus]
You're made of sunlight, I'm made of you,
Made of the salt and the sand and the blue.
Say it out loud where the whole street hears,
Say it over log drums, say it in my ear.
You're made of sunlight, I'm made of you,
Made of the drum and the dust and the truth.
Whatever I am, I was made in your hands,
So I'm made of you.

[instrumental]

[bridge]
When the power cuts and the whole street goes dark,
You are still the warmest thing out here in the yard.
I have got you memorised right down to the scar,
I could find you in a blackout by the sound of your heart.
So let the generators cough and the lanterns come out,
We were never dancing for the bulbs anyhow.

[chorus]
You're made of sunlight, I'm made of you,
Made of the salt and the sand and the blue.
Say it to the palms and the plastic chairs,
Say it to the children who are still out there.
You're made of sunlight, I'm made of you,
Made of the drum and the dust and the truth.
Ten thousand mornings and I still choose,
I'm made of you.

[post-chorus]
Oh, the orange and the blue,
Oh, the orange and the blue,
Everything I am, I am made of you.
Oh, the orange and the blue.

[outro]
Sunlight, sunlight, walking down the beach road,
Sunlight, sunlight, and the evening going gold.
Ask me in a hundred years, I will tell you the truth,
I'm made of you.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 620 at 116 wpm → ~5.3 min, 89% of frame cap |
| Caption + lyrics tokens | 2285 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
