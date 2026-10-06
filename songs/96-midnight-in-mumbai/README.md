# Midnight in Mumbai

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninety-sixth song. Female lead **Mahima**, Bollywood-fusion pop with tabla,
sitar, bansuri and full Hindi-film strings, sung in neutral Indian English
with no slang. 110 BPM, B minor. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 638 sung words, ballad/mid budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 110 BPM, B minor opening toward its relative major, tabla and dholak, sitar answers, bansuri, tanpura drone and the sea, kettle and scooter textures. A `Delivery Note` line fixes the neutral Indian English register. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-lead character bible, the practical-light rule, the jasmine-string continuity motif, the chai-pour challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 110 BPM this is a ballad/mid song and the length guard's
116 wpm default is the right estimate.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 96-midnight-in-mumbai
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\96-midnight-in-mumbai\caption.txt `
  --lyrics-file songs\96-midnight-in-mumbai\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\96-midnight-in-mumbai\output\midnight_in_mumbai.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the stranger's two lines in the pre-choruses | Punctuation is not sung and quotation marks confuse the tokenizer |
| Em-dashes replaced with commas throughout | The model sings the lyric body literally |
| `7 years` → *"seven long years"*; no digits anywhere in the body | The model sings digits unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines reduced to plain tags | Only the checkpoint's documented tags exist |
| The final chorus written out in full rather than `(as chorus 1)`, keeping its two varied lines | The verify script flags `(repeat)`, and the model would sing it |
| Trimmed nine words across the intro, verses and choruses | 649 words overran the 640-word ballad budget; the cuts were all filler articles, not images |

Kept exactly as written: every image, 110 BPM, B minor, the instrumentation,
the neutral register with no slang, and the mood arc.

## The story and the hooks

She has lived in this city long enough to stop noticing it. One night she
walks out to the sea wall with no reason, and the city refuses to let her go
home: a boy selling jasmine to an empty railing, a rank of idling taxis, a
stranger who asks her the time as a joke. He knows a stall where the kettle
is louder than a radio. They cross an empty sea link on a scooter with her
scarf pulling straight out behind her, and she tells him about her one window
and her one plant. Then the bridge, which is the whole song: seven years here
and she has never once heard the place until tonight. She stops wanting the
night to become something. The first ferry moves, the vendors unfold the same
tables, and she walks home with salt in her hair.

**The hook:** *"Midnight in Mumbai, and the city's wide awake."*

**The line for captions:** *"I do not need an ending, I am here for the
middle."*

**The turn:** *"I have lived in this city for seven long years / And I never
once heard it the way that I do."*

**The image:** *"The sea link is empty and the wind takes my scarf."*

**Why it can travel:** it is a love song to a city rather than to a person,
which means every listener can swap the city and keep the song. And the last
line refuses the romance ending on purpose — she goes home alone and happy.

## Lyrics as they will be sung

```
[intro]
Salt in the air on the wall at Marine Drive,
A long curve of lamps like a necklace of light.
I came out for nothing, with no reason to be here,
And the city said, stay, there is more to the night.

[verse]
The vendors are folding their tables away,
The taxis are humming in one yellow line.
A boy sells his jasmine to nobody at all,
And the smell of it follows me down to the tide.
I was not looking for anybody tonight,
I was counting the boats and the lamps on the sea.
Then a stranger came over and asked for the time,
And we laughed, because neither of us cared to know.

[pre-chorus]
He said, there is chai at the end of this road,
And the kettle sings louder than any radio.
So I walked with a stranger past the shuttered shops,
And the sea kept the time of the way we would go.

[chorus]
Midnight in Mumbai, and the city's wide awake,
Every window a lantern, every street a second chance.
Midnight in Mumbai, and the sea will not sleep,
So I am not sleeping while the whole town wants to dance.
Give me chai in a glass and a scooter and sea spray,
Give me warm monsoon air on my face.
Midnight in Mumbai, and the city's wide awake,
And a stranger's voice is turning into a place.

[verse]
He wakes up the scooter and I hold on politely,
Then the road opens out and I hold on for real.
The sea link is empty and the wind takes my scarf,
And I laugh like a woman with nothing to conceal.
He tells me his mother still calls him at midnight,
I tell him my flat has one window and a plant.
Two strangers, two histories, one road and one country,
And the city is listening, and the city understands.

[pre-chorus]
He said, there is a stall that stays open till morning,
Where the glasses are small and the fire never goes.
So I sat on a crate with my hands round a tumbler,
And I stopped making plans for the road leading home.

[chorus]
Midnight in Mumbai, and the city's wide awake,
Every window a lantern, every street a second chance.
Midnight in Mumbai, and the sea will not sleep,
So I am not sleeping while the whole town wants to dance.
Give me chai in a glass and a scooter and sea spray,
Give me warm monsoon air on my face.
Midnight in Mumbai, and the city's wide awake,
And a stranger's voice is turning into a place.

[instrumental]

[bridge]
I have lived in this city for seven long years,
And I never once heard it the way that I do.
The horns are a chorus, the waves keep the measure,
And a radio upstairs is in tune with them too.
I do not need an ending, I am here for the middle,
And the middle is the chai and the sea and you.

[chorus]
Midnight in Mumbai, and the city's wide awake,
Every window a lantern, every stranger a friend.
Midnight in Mumbai, and the sea will not sleep,
And I do not want a single thing here to end.
Give me chai in a glass and a scooter and sea spray,
Give me warm monsoon air on my face.
Midnight in Mumbai, and the city's wide awake,
And a stranger's voice has turned into a place.

[post-chorus]
Awake, awake, the whole of the bay,
The lights on the water will not look away.
Awake, awake, and the morning can wait,
Because midnight in Mumbai is a place I want to stay.

[outro]
The first ferry moves and the sky turns to pearl,
The vendors come back and the tables unfold.
I am walking home slowly with salt in my hair,
And a city behind me that never went cold.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2145 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
