# Wine and Whispers

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song thirty-eight. Female lead **Mahima**, jazz-pop lounge with a small-room
trio feel — upright bass, brushed kit, muted trumpet — flirty and intimate,
US register. 92 BPM, E♭ major, softly swung, ballad pacing. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 92 BPM, E♭ major, the brushes-only kit, the muted-trumpet solo and the drumless bridge. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a single-look character bible, Kai as the man, the fire-and-street-only lighting rule, the fragments-only bridge, workflow and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 38-wine-and-whispers
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\38-wine-and-whispers\caption.txt `
  --lyrics-file songs\38-wine-and-whispers\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\38-wine-and-whispers\output\wine_and_whispers.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | Punctuation is not sung; the model reads the lyric body literally |
| Digits spelled as words (*four years back*, *the second glass*) | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – bass alone, brushes after a bar…]`, `[chorus – harmony opens, volume does not]`, `[verse 2]`, `[pre-chorus 2]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| Every repeated section written out in full — both pre-choruses, all three choruses | `(repeat)` would be sung as the word |
| Eleven lines tightened by a word or two each | 664 words fell to 639, inside the 600–640 ballad band |

Kept exactly as written: every image, 92 BPM, E♭ major, the instrumentation,
the mood arc, the bridge turn, the dance in the outro.

## The story and the hooks

Two candles burned to stubs, a bottle they had been saving for an occasion
that never arrived, and both phones shut in a drawer. It starts as a game:
he admits he nearly cancelled and sat outside in the car; she admits she went
four years back through his photos on a Sunday before they ever met. Then the
second glass, and it stops being charming. He tells her about a year he never
mentions and why he still won't sit with his back to a crowd. She is asked
what she is afraid of, nearly lies, and says the real one instead: that she
is easy to leave, and has been. He puts his glass down and doesn't argue. The
bridge finds the volume that big things have to be said at, which is lower
than a room — and he says it back at the same level. Then the table goes
back, the rug rolls aside, and they dance with nothing playing.

**The hook:** *"Wine and whispers, keep the lights down low"* — first and
last line of every chorus, with the title word landing on a long held note.

**The line for captions:** *"There's a volume you can only say the big things
at."*

**The knife line:** *"That I'm easy to leave and I've been left before / And
you set your glass down and don't argue at all."*

**The turn:** *"You don't answer with a speech, you just breathe out slow /
And you say it back to me at the same level, low."*

**Why it can travel:** it is a grown-up record in a catalogue full of nights
out, and it does the rarest thing a flirty song can do — it makes being known
sound more dangerous than being wanted. The bridge is a ready-made silent
vertical edit: a mouth moving with no audio.

## Lyrics as they will be sung

```
[intro]
Two candles burned to nothing and the wax on the floor,
The good bottle open that we swore we'd save for more.
Phones in a drawer where we can't hear them ring,
And the rain out there doing its own quiet thing.

[verse]
You start with a small one, something safe and half a joke,
You say you nearly cancelled, sat outside and never spoke.
So I tell you that I looked you up before we met,
Went four years back on a Sunday, not embarrassed yet.
There's a trumpet somewhere low, doing something to the room,
Making everything we say sound truer than it should.
Your glass goes down an inch, my voice goes down a tone,
And the loudest thing in here is what we haven't shown.

[pre-chorus]
Don't turn the big light on, leave it where it is,
Everything looks kinder at the edge of a wick.
Say the next one closer, say it near my ear,
The only thing worth having is the thing you're scared to hear.

[chorus]
Wine and whispers, keep the lights down low,
Tell me something true, then something slow.
The street can have the shouting, the street can have the rain,
In here we say it quiet and we say it plain.
Wine and whispers, the hours going soft,
Nothing in this room is getting turned off.
Move a little closer, let the candles go,
Wine and whispers, keep the lights down low.

[verse]
Somewhere past the second glass you stop performing,
And you tell me about a year you never say aloud,
How you slept on a friend's floor and called it fine,
And how you still won't sit with your back to a crowd.
Then you ask me what I'm scared of and I nearly lie,
And I say the real one and it comes out small,
That I'm easy to leave and I've been left before,
And you set your glass down and don't argue at all.

[pre-chorus]
Don't turn the big light on, we're better in the dark,
Everything looks braver at the edge of a spark.
Say the next one closer, say it near my ear,
The only thing worth having is the thing you're scared to hear.

[chorus]
Wine and whispers, keep the lights down low,
Tell me something true, then something slow.
The street can have the shouting, the street can have the rain,
In here we say it quiet and we say it plain.
Wine and whispers, the hours going soft,
Nothing in this room is getting turned off.
Move a little closer, let the candles go,
Wine and whispers, keep the lights down low.

[instrumental]

[bridge]
There's a volume you can only say the big things at,
And it's lower than a room, it's lower than that.
So I say it to the air beside your jaw,
The one I've never said to anybody before.
You don't answer with a speech, you just breathe out slow,
And you say it back to me at the same level, low.

[chorus]
Wine and whispers, keep the lights down low,
Tell me something true, then something slow.
The street can have the shouting, the street can have the rain,
We said the whole thing quiet and it came out plain.
Wine and whispers, the hours going soft,
The candle's on its last and we're not moving off.
Push the table back and let the small hours go,
Wine and whispers, keep the lights down low.

[post-chorus]
Low, low, keep the lights down low,
Nothing in this room has anywhere to go.
Low, low, keep the lights down low,
Wine and whispers, and the rest of it slow.

[outro]
Sofa pushed back and the rug rolled aside,
Your hand at my back and the last of the wine.
No music left but we're still going round,
And the loudest thing in here is not a sound.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2019 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
