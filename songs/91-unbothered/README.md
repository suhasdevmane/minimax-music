# Unbothered

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song ninety-one. Female lead **Mahima**, Afrobeats with a warm pop sheen,
108 BPM, E major, US register. Mid pacing class, so no `render.json`. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 633 sung words, inside the ballad and mid budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 108 BPM, E major, log drum and palm-muted guitar, the rooftop and market ambience. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 81 entries — with a three-look character bible, the aunties and the pepper trader, the never-shown doorway figure, workflow, the shoulders-down challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 91-unbothered
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\91-unbothered\caption.txt `
  --lyrics-file songs\91-unbothered\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\91-unbothered\output\unbothered.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech (`"Aren't you gonna reply?"`, `"You look light today,"`, `"hey"`) | Punctuation is not sung and quotation marks confuse the phrasing |
| Em-dashes and question marks replaced with commas | Not sung; they break the phrasing model |
| Descriptive tag lines (`[intro – rooftop, guitar and shaker]`, `[chorus – the widest, warmest groove]`, `[bridge – drums out, honest]`) reduced to plain `[intro]`, `[chorus]`, `[bridge]` | Only the plain tag set exists; text on a tag line is dropped |
| The `(repeat)` markers for the second pre-chorus, the second chorus and the second post-chorus written out in full | The model would sing the word *repeat* |
| Performance notes (*drums out*, *everyone*, *night on the rooftop*) moved into the caption | The lyric body is sung literally |

Kept exactly as written: every lyric line, 108 BPM, E major, the log-drum
and guitar instrumentation, the market and rooftop imagery and the mood arc.
No trimming was needed — 633 words fits.

## The story and the hooks

Somebody sends her a screenshot at ten in the morning: three paragraphs
about her, no warning. She reads it, laughs, makes coffee and puts a song
on. Her cousin asks whether she is going to reply and she says: to what, a
stranger having a hard July? The rest of the day is the answer. A Saturday
market, flowers she buys for herself, a pepper trader who tells her she
looks light today and gets told that some heavy things went down along the
way. A hibiscus drink, the long block home on purpose. Then at nine the
person who wrote the paragraphs walks into the party, the whole room turns
waiting for a story, and she says hey, makes room and goes back to the beat.
The bridge is the only still moment in the song: she did feel it, on a
Tuesday, with the curtains shut. She just stopped performing it.

**The hook:** *"Unbothered, untouchable, in my lane."*

**The chant:** *"Shoulders down, shoulders down / Nothing in this city gonna
hold me down."*

**The line for captions:** *"Unbothered is not a wall I built, it's a door I
close without the guilt."*

**The quote:** *"To what, a stranger having a hard July?"*

**The soft moment:** *"You look light today. I put some heavy things down
along the way."*

**Why it can travel:** the chant is a four-count move anyone can do in a
kitchen or a market aisle, the record is a real Afrobeats groove rather than
a pop song with a log drum on it, and nobody gets dragged — the person who
started it is never even shown.

## Lyrics as they will be sung

```
[intro]
Rooftop speaker, six o'clock gold,
Ice in a glass and a story I've been told.
Somebody's typing something long about me,
And the log drum came on, so I let it be.

[verse]
They sent me a screenshot at ten in the morning,
Three paragraphs deep with no kind of warning.
I read it, I laughed, I went and made my coffee,
Then I put on the song that gets my hips talking to me.
My cousin said, aren't you gonna reply?
I said, to what, a stranger having a hard July?
They want me in the comments, want me in the fight,
But my afternoon is booked and my chest is light.
Some things are weather, they pass over the roof,
I'm not gonna argue with a cloud about proof.

[pre-chorus]
Peace is a muscle and I work it every week,
Learned it from my aunties in the kitchen when they speak.
When the noise gets loud I turn the bass up higher,
Let them run their mouth, I am not lending them a fire.

[chorus]
Unbothered, untouchable, in my lane,
Sun on the back of my neck, I'm not complaining.
Say what you want, put it in a frame,
I'll be right here moving just the same.
Low stress, light feet, easy on my mind,
Whatever you're carrying, leave it behind.
Unbothered, untouchable, in my lane,
Look at me dancing while you're saying my name.

[post-chorus]
Shoulders down, shoulders down,
Nothing in this city gonna hold me down.
In my lane, in my lane,
Unbothered, untouchable, in my lane.

[verse]
Market on a Saturday, colours in a row,
Bought myself the flowers, nobody had to know.
The auntie with the peppers said, you look light today,
I said, I put some heavy things down along the way.
Cold drink after, hibiscus and lime,
Walked the long block home because the day was mine.
Then at nine that same person walked into the party,
Whole room turning, waiting on a story.
I said hey, made room, went back to the beat,
And the floor stayed hot underneath my feet.

[pre-chorus]
Peace is a muscle and I work it every week,
Learned it from my aunties in the kitchen when they speak.
When the noise gets loud I turn the bass up higher,
Let them run their mouth, I am not lending them a fire.

[chorus]
Unbothered, untouchable, in my lane,
Sun on the back of my neck, I'm not complaining.
Say what you want, put it in a frame,
I'll be right here moving just the same.
Low stress, light feet, easy on my mind,
Whatever you're carrying, leave it behind.
Unbothered, untouchable, in my lane,
Look at me dancing while you're saying my name.

[instrumental]

[bridge]
Don't get it twisted, I feel it all,
I just stopped performing it for people in the hall.
I let it hurt on a Tuesday with the curtains closed,
Then I woke up Wednesday and I picked the good clothes.
They call it cold, I call it a choice,
I gave my best years to the loudest voice.
Unbothered is not a wall I built,
It's a door I close without the guilt.

[chorus]
Unbothered, untouchable, in my lane,
Moon on the rooftop and I'm still not complaining.
Say what you want, put it in a frame,
I'll be right here moving just the same.
Low stress, light feet, easy on my mind,
Whatever you're carrying, leave it behind.
Unbothered, untouchable, in my lane,
Look at me dancing while you're saying my name.

[post-chorus]
Shoulders down, shoulders down,
Nothing in this city gonna hold me down.
In my lane, in my lane,
Unbothered, untouchable, in my lane.

[outro]
Rooftop speaker, midnight gold,
Ice in the glass and a story getting old.
Somebody's typing, I will never even see,
The log drum's playing, so I let it be.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 633 → ~5.5 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2120 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
