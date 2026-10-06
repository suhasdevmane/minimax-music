# Cassette Tape Heart

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty-six. Female lead **Mahima**, synthwave with analogue polysynths,
gated-reverb drums and a modern pop vocal. 100 BPM, A minor, ballad/mid
pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 638 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1. 100 BPM, A minor, detuned polysynth pad, octave analogue bass, gated snare, the always-ticking arpeggio, and the tape hiss / lid clunk / tape-stop / drawer textures. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 67 entries — with a three-look bible, the hands-only rule for the boy, three separated colour worlds, the un-gelled bridge, macro-generation guidance and a QC checklist |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

No `render.json` — at 100 BPM this is a ballad/mid song and the verify
script's 116 wpm default is the right guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 56-cassette-tape-heart
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\56-cassette-tape-heart\caption.txt `
  --lyrics-file songs\56-cassette-tape-heart\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\56-cassette-tape-heart\output\cassette_tape_heart.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung |
| Digits spelled as words (*track four*, *nineteen*, *four beats*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – hiss, pad, no drums]*, *[bridge – no drums, one pad]*) reduced to plain tags | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| The tape-stop, rewind and hiss direction moved out of the lyric body into the caption | The model sings the lyric body literally |
| Repeated choruses and pre-choruses written out in full | The model would sing a repeat marker |
| Two verse couplets trimmed for the ballad word budget | 638 words sits inside the 600–640 band; the submission ran long |

Kept exactly as written: the hook, 100 BPM, A minor, the synthwave
arrangement, the bridge turn, the drawer ending, the viral moments.

## The story and the hooks

She finds a mixtape in a drawer with dead batteries in the player beside it,
and the handwriting on the card does the rest. He made it in a bedroom with
one finger on a record button, caught the DJ talking at the top of track
four and left it in. She played it until the ribbon went thin and the fourth
song always skipped and she loved the skip. There was a car with a tape deck
and a heater that lied, frost on the inside of the glass, and the click at
the end of the side that was the loudest sound of that winter. She never
taped over side A. Then the bridge takes every colour out of the video and
the song stops being about him at all: she does not want him back, she wants
the girl who thought a tape was a promise. The last frame is a drawer
closing on a cassette lying flat, not buried.

**The hook:** *"I've got a cassette tape heart, and you're on side A."*

**The line for captions:** *"Recorded over you, and you still bleed through
the seams."*

**The turn:** *"I don't want you back, I want the girl that I was / The one
who thought a tape was a promise you could hold."*

**The knife line:** *"And the fourth song always skipped and I loved it
instead."*

**Why it can travel:** the object does the work. Every macro shot — the lid,
the spools, the pencil in the spool, the drawer — is a fifteen-second clip on
its own, and the bridge gives the nostalgia a spine so it does not curdle
into a mood board.

## Lyrics as they will be sung

```
[intro]
Found it in a drawer with the batteries dead,
Your handwriting sloping across the white card.
A breath of static before anything starts,
And a girl I used to be sits down in the dark.

[verse]
You made it in a bedroom with the radio on,
One finger on the button, waiting hours for a song.
You caught the deejay talking at the top of track four,
You swore, and you kept it, and I loved you all the more.
I played it till the ribbon wore as thin as a thread,
And the fourth song always skipped and I loved it instead.

[pre-chorus]
New batteries out of the back of the clock,
The lid clicks down and the motor kicks up.
Four beats of a drum that I'd know anywhere,
And I'm nineteen again and you're still standing there.

[chorus]
I've got a cassette tape heart, and you're on side A,
Wound tight in a drawer where I left you that day.
Everyone after you got put down on side B,
Recorded over you, and you still bleed through the seams.
Press rewind, press rewind, let the spools start to turn,
There's a hiss in the silence I could never unlearn.
I know how it ends and I press play anyway,
I've got a cassette tape heart, and you're on side A.

[verse]
A car with a tape deck and a heater that lied,
Frost on the inside of the glass and your hand on the dial.
We drove past the water till the second side ran out,
And the click at the end of it was the loudest sound.
I never taped over side A and I don't know why,
I just wound it to the front and I put it back inside.

[pre-chorus]
Thumb on the button, and I know I should stop,
The lid clicks down and the motor kicks up.
Four beats of a drum that I'd know anywhere,
And I'm nineteen again and you're still standing there.

[chorus]
I've got a cassette tape heart, and you're on side A,
Wound tight in a drawer where I left you that day.
Everyone after you got put down on side B,
Recorded over you, and you still bleed through the seams.
Press rewind, press rewind, let the spools start to turn,
There's a hiss in the silence I could never unlearn.
I know how it ends and I press play anyway,
I've got a cassette tape heart, and you're on side A.

[instrumental]

[bridge]
I don't want you back, I want the girl that I was,
The one who thought a tape was a promise you could hold.
I want the bedroom carpet and the waiting and the hiss,
I want an afternoon spent making one thing good.
You were never the point, though I let you be for years,
You're just the sound of the last time that I was new.

[chorus]
I've got a cassette tape heart, and you're on side A,
Wound tight in a drawer, and that's exactly where you stay.
Everyone after you got put down on side B,
And the bleed is getting quieter, and that is alright with me.
Press rewind, press rewind, let the spools start to turn,
There's a hiss in the silence I could never unlearn.
I know how it ends and I press play anyway,
I've got a cassette tape heart, and you're on side A.

[post-chorus]
Side A, side B, and the click at the end,
Side A, side B, and I wind it again.
All that hiss, all that hope, that afternoon,
Side A, side B, and I let it run through.

[outro]
Batteries out and the drawer slides away,
Card in the case with the crease and the fray.
I won't wind you back for a long time, but stay,
I've got a cassette tape heart, and you're on side A.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2134 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
