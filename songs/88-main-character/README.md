# Main Character

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song eighty-eight. Female lead **Mahima**, bright cinematic pop with a
widescreen synth-pop lift, 124 BPM, F major, US register. Uptempo, so it
carries a `render.json`. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 755 sung words, inside the uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 124 BPM, F major, the plucked-arpeggio motif, the clapperboard hit and the footstep-clap ear candy. |
| [`render.json`](render.json) | Uptempo pacing for the length guard (`wpm: 140`) |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 96 entries — with a three-look character bible, the rust-orange-coat rule, the faceless-crowd rule, workflow, the wide-shot challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 88-main-character
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\88-main-character\caption.txt `
  --lyrics-file songs\88-main-character\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\88-main-character\output\main_character.wav
```

Expected ~2 h.

## Pacing warning

This is an uptempo song and pacing is estimated, not measured. The lyrics are
**755 words**. Against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 130 wpm | 5.8 min | 97% |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 155 wpm | 4.9 min | 81% |

At 124 BPM with a chanted post-chorus and a conversational verse delivery, a
blended 140–150 wpm is the realistic expectation, which lands near five
minutes. **If the first render truncates the outro, drop the second
post-chorus (39 words, a repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed (`"fine,"` → *fine*, `"sorry"` → *sorry*, `"cut,"` → *cut*) | Punctuation is not sung; quotation marks confuse the phrasing |
| `6:40` and `19th` written as *six forty* and *Nineteenth* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – half-awake, arpeggio only]`, `[chorus 1 – the city as a set]`, `[final chorus – evening, widest]`) reduced to plain `[intro]`, `[chorus]` | Only the plain tag set exists; text on a tag line is dropped |
| The `(repeat)` markers for the second chorus and the second post-chorus written out in full | The model would sing the word *repeat* |
| Performance notes (*arpeggio only*, *piano, near-spoken*, *widest*) moved into the caption | The lyric body is sung literally |
| Verse one and verse two each split into two stanzas in the submission, joined into one `[verse]` each | The engine takes one tag per section |

Kept exactly as written: every lyric line, 124 BPM, F major, the textural
lift instead of a modulation, the instrumentation and the mood arc.

## The story and the hooks

An ordinary Monday. She wakes at six forty in a blue room with a paper cup
that has her name spelled wrong on it, and for ten years she has been very
good at background — holding coats, clapping for other people, third choice,
back of the line. Then the elevator glass catches her and the girl looking
back does not look away. She walks out of the lobby into hard white morning
and the whole commute plays like a title sequence: scaffolding for a key
light, taxis throwing gold out of puddles, the train arriving on the beat.
Upstairs on the nineteenth floor she finally says the sentence she has been
rehearsing in the stairwell all year, deletes the word *sorry* out of an
email, eats lunch alone on a fire escape and is fine. Then the bridge, on a
late train, where she notices a woman in a blue raincoat reading a paperback
and understands that the woman is the lead of a film she will never see —
and that this takes nothing away from her own.

**The hook:** *"Main character, and the city's my set."*

**The line for captions:** *"Nobody yelled cut, and I'm done with the
regret."*

**The turn:** *"She is the lead of a film I will never see, so let me be the
lead of the one in front of me. Everybody gets a set. This one is mine."*

**The knife line:** *"Cut the word sorry and it read just fine."*

**Why it can travel:** it is confidence without a villain. There is no ex,
no revenge and nobody to beat — just a walk to work at chin-up pace, which
is the most filmable and most repeatable thirty seconds anyone owns.

## Lyrics as they will be sung

```
[intro]
Alarm at six forty, blue in the room,
Steam on the window, an unmade bed.
Coffee in a paper cup, my name spelled wrong,
Headphones in and the score comes on.
Roll it.

[verse]
Ten years of standing just outside the frame,
Holding a coat, remembering a name.
I was so good at background, so good at fine,
Second row, third choice, back of the line.
Then the elevator caught me in the glass,
And the girl looking back did not look past.
Something in my shoulders finally set,
And the lobby doors opened like a silhouette.
Wind off the avenue, coat coming loose,
Pigeons hit the sky like they were cued to move.
Somebody's playlist matched my walking speed,
And the whole street turned into an opening scene.

[pre-chorus]
No audition, no note, no callback list,
Nobody is casting this, so I insist.
Light turns green and the crowd divides,
Cue the strings, hit my mark, I rise.
Action.

[chorus]
Main character, and the city's my set,
Best scene of my life and I haven't shot it yet.
Sun through the scaffolding, that is my key light,
Puddles under taxis holding all that bright.
I'm not the friend in the doorway with the one good line,
Not the girl who waits on somebody else's sign.
Nobody yelled cut, and I'm done with the regret,
Main character, and the city's my set.

[post-chorus]
Wide shot, chin up, coat in the wind,
Wide shot, this is where the good part begins.
Steam and the sirens and the crosswalk chime,
Everything out here sounds like a soundtrack of mine.
Doors on the boulevard swing when I pass,
Main character, main character at last.

[verse]
Nineteenth floor, my badge swings on the strap,
Beige on beige and a coffee ring map.
I used to fold my sentences inside a notebook,
Rehearse them in the stairwell where nobody looked.
Today I said the one I had been saving all year,
Table went quiet and I let it stay clear.
Somebody nodded and the meeting moved my way,
That is not a plot twist, that is just a Monday.
Sent the email I rewrote about twelve times,
Cut the word sorry and it read just fine.
Lunch on the fire escape, sun on the brick,
One slice, no company, and I did not feel sick.
Walked home at six with the gold on the glass,
And I never once checked who was watching me pass.

[pre-chorus]
No stand in, no stunt double, no cue,
Nobody is writing this but me and the avenue.
Light turns green and the crowd divides,
Cue the strings, hit my mark, I rise.
Action.

[chorus]
Main character, and the city's my set,
Best scene of my life and I haven't shot it yet.
Sun through the scaffolding, that is my key light,
Puddles under taxis holding all that bright.
I'm not the friend in the doorway with the one good line,
Not the girl who waits on somebody else's sign.
Nobody yelled cut, and I'm done with the regret,
Main character, and the city's my set.

[instrumental]

[bridge]
For years I gave the good lines away for free,
Made myself small so the room could breathe.
Somebody else got the close up, I held the light,
And I called it being humble, and I called it right.
Now look at the woman across the aisle in blue,
Reading her book like the ending is overdue.
She is the lead of a film I will never see,
So let me be the lead of the one in front of me.
Everybody gets a set. This one is mine.

[chorus]
Main character, and the city's my set,
Rain on a windshield is the best shot I'll get.
Sun gone soft on the scaffolding, still my key light,
Neon in the puddles holding all that bright.
I'm not the friend in the doorway with the one good line,
Not the girl who waits on somebody else's sign.
Nobody yelled cut, and I'm done with the regret,
Main character, and the city's my set.

[post-chorus]
Wide shot, chin up, coat in the wind,
Wide shot, this is where the good part begins.
Steam and the sirens and the crosswalk chime,
Everything out here sounds like a soundtrack of mine.
Doors on the boulevard swing when I pass,
Main character, main character at last.

[outro]
Alarm at six forty, blue in the room,
Same cup, same name spelled wrong.
The door swings different when you know it's your scene,
Same old city, brand new song.
Main character, and the city's my set.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 755 at 140 wpm → ~5.4 min, 90% of frame cap |
| Caption + lyrics tokens | 2341 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
