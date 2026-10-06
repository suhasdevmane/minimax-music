# Keys to the Same Door

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song 87. **Female + male duet** — Mahima on the lead, a plain-spoken male
tenor as Singer B — warm contemporary pop with a live-room feel, 104 BPM,
C major, upright piano, layered handclaps and a very large singalong chorus.
Same singer as songs 1–8 for the female lead; the male voice modelled on
song 4's Singer B. US register.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock; Singer B added with a section-by-section duet structure. 104 BPM, C major, room-miked upright piano, four or five layers of claps, warm synth bass, muted acoustic and ringing electric, a group vocal on the last chorus, and the key cutter and door buzzer as ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 66 entries — one apartment across its first months, a two-lead character bible with Kai, the repeating hallway frame, the composited buzzer-card note, workflow, the shoe-pile challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 104 BPM this is the ballad/mid pacing class, so the
verify script uses the 116 wpm default.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 87-keys-to-the-same-door
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\87-keys-to-the-same-door\caption.txt `
  --lyrics-file songs\87-keys-to-the-same-door\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\87-keys-to-the-same-door\output\keys_to_the_same_door.wav
```

Expected ~2 h.

## One thing to know before rendering: it's a duet

Same situation as songs 4, 8 and 9: the model has no per-line singer control,
so the split lives in the caption's `Duet Structure` line and the model
follows it loosely. Expect the choruses as two voices in unison rather than
in harmony — the hook is written to be shouted together, not traded. The
second verse is the one that should come out male, and the couch story only
works if it does. Treat the first render as a test of that.

## What changed from the submission

| Change | Why |
|---|---|
| `[intro – piano and a key cutter]`, `[verse 2 – male lead]`, `[chorus – claps, piano, both voices in unison]`, `[final chorus – modulated, group vocal]`, `[post-chorus – chanted call and response]` and `[bridge – piano and voice, no percussion]` reduced to plain tags | The model only knows the eight plain section tags and drops or sings anything else on a tag line |
| The her / him / both split and the modulation note moved out of the tag lines into the caption's `Duet Structure` and `Global Emotional Progression` | Stage directions in the lyric body get sung |
| `[verse 1]` / `[verse 2]` and `[pre-chorus 2]` / `[chorus 2]` renumbered to plain `[verse]`, `[pre-chorus]`, `[chorus]` | Same rule; numbering is not an allowed tag |
| The repeated pre-chorus and all three choruses written out in full | The model would sing a `(repeat)` line |

Kept exactly as written: every lyric line, 104 BPM, C major, the whole-step
lift into the final chorus, the instrumentation and the mood arc. The
submission already spelled every number as a word (*eleven seconds*, *aisle
four*, *eight times in nine years*, *twenty solid minutes*, *ninety second
speech*) and used no quotation marks or em-dashes, so nothing was cleaned
there. No trimming was needed — 640 words sits at the top of the ballad
budget.

**Craft check:** the twelve-point check in
[`docs/LYRIC_CRAFT.md`](../../docs/LYRIC_CRAFT.md), including the
verse-chorus echo check at all four transitions, was run against the
existing `lyrics.txt` and found nothing to fix. Verse two moves the story to
a new voice and a new day rather than rephrasing verse one; no verse or
bridge closes on the chorus's opening phrase, rhyme word or signature image;
every section sits inside the guide lengths; the hook carries the title in
the first and last line of every chorus and returns in the post-chorus. The
lyrics are unchanged from the file as delivered.

## The story and the hooks

Two keys get cut from one blank in aisle four of a hardware store, and the
noise of the machine is the loudest sound in the song. She has moved eight
times in nine years, handed a key back at the door of every one of them, and
never once been given one. Now there is a buzzer card downstairs with two
names on it in two different handwritings and she keeps going down to check
it is still there. Moving night is boxes to the ceiling, a lamp still in the
car and pizza on a packing crate. His verse is the couch that does not fit
up the stairs, twenty silent minutes on the landing, an argument about a
wall versus a window conducted about furniture they cannot physically get
inside, and the best night's sleep of his life on a bare mattress. Then the
bridge, which is the private part: a duffel bag half packed at the back of a
closet for years, emptied out on a Tuesday, and three spare keys worked off
a ring at a kitchen table one morning until only one is left. The last
chorus is a housewarming with a bowl of keys by the door, and the outro goes
back to the counter, where a man in a green apron says good luck to you both
and has no idea, or every idea, what he just handed her.

**The hook:** *"Two keys to the same door, that's what I've been waiting
for"* — domestic, singable, and the whole argument of the song in nine
words.

**The line for captions:** *"It's the first place in my life I'm not
rehearsing leaving."*

**The turn:** *"I took them off this morning, there is only one now."*

**The quote:** *"I've handed back a key at the door of every place, and I've
never once been given one back."*

**Why it can travel:** it gives moving in together the weight the culture
saves for a proposal, and the video's repeated hallway frame — one pair of
shoes on day one, a heap on day one hundred — is a challenge anyone who has
ever shared an address can shoot in ten seconds.

## Lyrics as they will be sung

```
[intro]
The machine at the hardware store screams for eleven seconds,
Then it drops a warm piece of brass in my hand.
Two of them, same cuts, same jagged promise,
And I'm standing in aisle four about to cry.

[verse]
I've moved eight times in nine years by myself,
I know how to tape a box and lie about the weight.
I've handed back a key at the door of every place,
And I've never once been given one back.
The buzzer downstairs has a slot for two names now,
Yours in your handwriting and mine underneath in mine.
It's the smallest piece of paper in the building,
And I keep going down to check it's still there.

[pre-chorus]
Boxes to the ceiling and the lamp's still in the car,
A pizza on a packing crate and nowhere left to sit.
The neighbors heard us laughing at eleven,
And I don't care, I'm not going anywhere.

[chorus]
Two keys to the same door, that's what I've been waiting for,
Not the ring, not the toast, not the ninety second speech.
Just a hallway with our shoes in it and a light we both forget,
And a lock that finally knows the two of us.
Two keys to the same door, one welcome mat, one floor,
That's what I've been waiting for.

[verse]
The couch didn't fit up the stairs and we knew it at the landing,
And neither of us said it for twenty solid minutes.
You wanted it against the window, I wanted it against the wall,
So we fought about a couch we couldn't physically get in.
Then we left it on the sidewalk with a sign and ate on the floor,
First night in a house with nothing in it but us,
And I never slept better on a worse mattress.

[pre-chorus]
Two toothbrushes leaning on each other in a glass,
My coat on your hook and your book on my side.
I woke at four and heard you in the kitchen,
And I wasn't scared, I just went back to sleep.

[chorus]
Two keys to the same door, that's what I've been waiting for,
Not the ring, not the toast, not the ninety second speech.
Just a hallway with our shoes in it and a light we both forget,
And a lock that finally knows the two of us.
Two keys to the same door, one welcome mat, one floor,
That's what I've been waiting for.

[instrumental]

[bridge]
I kept a bag half packed at the bottom of the closet,
Just in case the room got small, just in case I had to go.
I unpacked it Tuesday, there's nothing left I could run with,
And I had spare keys on my ring for people who moved out.
I took them off this morning, there is only one now.
So the door does what a door does, it opens and it holds,
And we are the two who are allowed in.

[chorus]
Two keys to the same door, that's what I've been waiting for,
Not the ring, not the toast, not the ninety second speech.
Just your keys in the bowl and mine on top of them,
And a lock that finally knows the two of us.
It's the first place in my life I'm not rehearsing leaving,
Two keys to the same door, one welcome mat, one floor,
That's what I've been waiting for.

[post-chorus]
Same door, same door, same little brass and steel,
Same door, same door, and I'm still not used to it.
Same door, same door, turn it twice and come on in,
Two keys to the same door.

[outro]
The machine at the hardware store screams for eleven seconds,
And a man in a green apron says, good luck to you both.
He has no idea what he just handed me,
Or maybe he does, and that's why he said it like that.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2358 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
