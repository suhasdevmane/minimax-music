# High Heels on Concrete

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninety-fourth song. Female lead **Mahima**, drill-pop with a widescreen
cinematic chorus, UK register, both verses rapped in a London drill cadence.
140 BPM, D minor. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 746 sung words, uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 140 BPM, D minor, sliding 808s, triplet hi-hat rolls, dark cathedral keys, and the heel-strike sample that is the signature percussion of the record. A `Delivery Note` line carries the rap cadence. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 83 entries — with a two-look character bible, a faceless doubter, the heel-strike rule, the tunnel set piece, the walk-out challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 94-high-heels-on-concrete
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\94-high-heels-on-concrete\caption.txt `
  --lyrics-file songs\94-high-heels-on-concrete\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\94-high-heels-on-concrete\output\high_heels_on_concrete.wav
```

Expected ~2 h.

## Pacing: uptempo, and the verses are rapped

At 746 sung words this is an uptempo song and the length guard uses
`render.json`'s conservative 140 wpm rather than the 116 wpm ballad default.
That lands it at 5.3 minutes, 89% of the six-minute frame cap. The real
figure will almost certainly be faster: a drill verse at 140 BPM typically
paces 170–200 wpm, and the two rapped verses are 217 of the 746 words, with
two chant post-choruses on top. A blended estimate of 155–165 wpm puts the
track nearer 4.6 minutes.

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| **140 wpm (the guard setting)** | 5.3 min | 89% |
| 160 wpm | 4.7 min | 78% |
| 185 wpm | 4.0 min | 67% |

**If the first render truncates the outro, drop the second post-chorus (33
words, a repeat) and re-render.** If it comes in short instead, that is the
better failure: the outro is written to hold on an empty street.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech (*stay small*, *love, where you going*, *hope you're doing well*) | Punctuation is not sung and quotation marks confuse the tokenizer |
| Em-dashes replaced with commas throughout | The model sings the lyric body literally |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines reduced to plain tags | Only the checkpoint's documented tags exist; anything else is dropped or sung |
| The rap-cadence direction moved out of the lyric body into the caption as a `Delivery Note` line | Stage directions in the body get sung |
| Both repeated choruses and both post-choruses written out in full | The verify script flags `(repeat)`, and the model would sing it |

Kept exactly as written: every line, 140 BPM, D minor, the instrumentation,
the heel-strike motif and the mood arc. No trimming was needed — 746 words
sits inside the uptempo budget.

## The story and the hooks

Half past midnight on a London high road. She comes off the last Overground
with her collar up and two years of keeping quiet behind her, and the sound
of her own heels on wet concrete turns into a drumline — the pavement
talking, the cracks keeping time. A railway tunnel does the mixing. A black
cab slows and gets waved on. A lad who once told her she was dreaming keeps
his head down. Then the bridge admits what the whole song has been dancing
around: there was a year she walked this fast because she was frightened,
keys laced between her fingers. Same street, same shoes, same stride — she
just stopped asking the dark for somewhere to hide. By the last chorus the
crowd is walking in time with her, and by half three the road is empty again
and hers.

**The hook:** *"High heels on concrete, that's my drumbeat."*

**The line for captions:** *"No apology, no permission, no disguise."*

**The chant:** *"Listen to the concrete, listen how it rings."*

**The turn:** *"There was a year I walked this fast because I was frightened
/ Keys between my fingers and my shoulders always tightened."*

**Why it can travel:** the hook is a sound before it is a sentence, so the
video edits itself — a heel, a beat, a wet pavement. And the bridge says the
quiet thing out loud without ever making the song sad.

## Lyrics as they will be sung

```
[intro]
Half past midnight and the high road's humming,
You can hear me on the pavement before you see me coming.
Steel on wet stone, that's the only sound,
London, hold your breath, I am coming round.

[verse]
Off the last Overground with my collar to my chin,
Two years keeping quiet was a habit that I binned.
They said stay small, keep the volume low,
Now the whole road turns when I take it slow.
Kick, snare, kick, that's the pavement talking,
Every crack in the concrete keeping time while I am walking.
No entourage, no ring light, no crew,
Just a coat, a key and a couple of things to prove.
I was bare polite the whole time they took the mick,
Learned to keep receipts and let the silence stick.
Now the same lot slide in, saying hope you're doing well,
I read it on the escalator, kept the story to myself.

[pre-chorus]
Feel that in the tarmac, that's a shoulder squaring up,
Hear that in the doorway, that's a woman had enough.
Give me one dark mile with a bassline underneath,
And I'll turn two leather soles into a full percussion piece.

[chorus]
High heels on concrete, that's my drumbeat,
Every step a snare going down an empty street.
Lamp light, long shadow, nothing in my lane,
The city hears me coming and it learns to say my name.
Click, clack, hear it ricochet and rise,
No apology, no permission, no disguise.
High heels on concrete, that's my drumbeat,
And the whole of London moves in time with my feet.

[post-chorus]
Listen to the concrete, listen how it rings,
Leather, steel and pavement, that's the only drum I bring.
Listen to the concrete, hear it under me,
I don't need a stage tonight, I've got a whole street.

[verse]
Tunnel under the arches and the echo does the mixing,
Bassline off the brickwork and the ceiling does the lifting.
Black cab slows beside me, says, love, where you going,
Nah mate, I'm still working, and the working's in the walking.
There's a lad on the corner who once told me I was dreaming,
Head down now, phone out, pretending he's not seeing.
I don't want the last word, I would rather have the sound,
Every door I got shut out of, I just laid it in the ground.
Puddle catching neon and it doubles up the light,
Two of me now walking and the both of us alright.
Nobody left a lane for me, so I poured one out of nothing,
Took the long way past the river just to hear the bridges drumming.

[pre-chorus]
Feel that in the railings, that's the iron keeping score,
Hear that in the stairwell, that's a nobody no more.
Give me one wet mile with a chorus in my chest,
And I'll turn a bad address into a name you won't forget.

[chorus]
High heels on concrete, that's my drumbeat,
Every step a snare going down an empty street.
Lamp light, long shadow, nothing in my lane,
The city hears me coming and it learns to say my name.
Click, clack, hear it ricochet and rise,
No apology, no permission, no disguise.
High heels on concrete, that's my drumbeat,
And the whole of London moves in time with my feet.

[instrumental]

[bridge]
There was a year I walked this fast because I was frightened,
Keys between my fingers and my shoulders always tightened.
Same street, same shoes, same length of stride,
I just stopped asking the dark for a place to hide.
So if you hear me late and you wonder what it is,
That's not running, that's a rhythm, that's a business.

[chorus]
High heels on concrete, that's my drumbeat,
Every step a snare and now there's hundreds on the street.
Lamp light, long shadow, and they're falling into line,
The city hears me coming and the city knows it's mine.
Click, clack, hear it ricochet and rise,
No apology, no permission, no disguise.
High heels on concrete, that's my drumbeat,
And the whole of London moves in time with my feet.

[post-chorus]
Listen to the concrete, listen how it rings,
Leather, steel and pavement, that's the only drum I bring.
Listen to the concrete, hear it under me,
I don't need a stage tonight, I've got a whole street.

[outro]
Half past three and the high road's gone quiet,
Nothing left but me and the noise I made of it.
High heels on concrete, that's my drumbeat,
Let it ring out down the middle of the street.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 746 at 140 wpm → ~5.3 min, 89% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2387 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
