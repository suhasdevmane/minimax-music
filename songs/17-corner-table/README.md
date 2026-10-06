# Corner Table

**Status: written and verified, NOT rendered. Not yet in the queue.**

Seventeenth song. Female lead **Mahima**, understated indie-pop with a warm
live-band feel, a café love story told across four seasons through one
corner table. 110 BPM, C major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 629 sung words, every repeat written out |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 110 BPM, C major, warm electric guitar, upright piano, soft kick, restrained strings in the last chorus only, the café textures and the shop bell. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 65 entries — one café across a year, a three-look character bible, Kai as the man two tables over, the barista as a silent witness, the year-in-a-window push-in, the same-seat challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 17-corner-table
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\17-corner-table\caption.txt `
  --lyrics-file songs\17-corner-table\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\17-corner-table\output\corner_table.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung; commas carry the phrasing |
| Descriptive tag lines (*[intro – guitar figure...]*, *[final chorus – strings enter...]*) reduced to plain tags | The model only knows plain section tags |
| Every repeated chorus and pre-chorus written out in full | The model would sing "(repeat)" literally |
| Performance notes (near-spoken bridge, strings entering) moved to the caption | Anything in the lyric body gets sung |

Kept exactly as written: every lyric line, 110 BPM, C major, the
instrumentation, the four-season structure, the barista.

## The story and the hooks

September, she pretends to read a paperback so she has an excuse to sit at
the corner table while he works two tables over; she never gets past the
first line. November, he orders her oat latte before she reaches the
counter. December, the street lights go up and they share the table.
January, the door keeps opening and it's never him, and the barista wipes
his side of the table twice. March, the window's open, she's stopped
bringing the book, and he walks in with a reason: his dad got sick, he went
home, and in a year of ten o'clocks they never swapped numbers. She pushes
the sugar over and says sit down. The barista brings two leaves in the foam.

**The hook:** *"Same corner table, different me, and you still sat down."*

**The line for captions:** *"It was never the table. It's who keeps showing
up."*

**The turn:** *"You say, my dad got sick, I went home, I didn't have your
number / And I laugh, because a year of ten o'clocks and I never gave it to
you."*

**Why it can travel:** the whole story fits in one locked-off frame with
jump cuts, which is a format people already make; the hook is a caption;
and the wit (a year of coffees and no phone number) is the kind of detail
that gets quoted.

## Lyrics as they will be sung

```
[intro]
Same chair, same window, same wobble in the leg,
Same latte going cold beside a book I never read.
The girl behind the counter draws a leaf into the foam,
She's watched this whole thing happen and she's never said a word.

[verse]
September, I was hiding in a paperback,
Same page for an hour, eyes on the door instead.
You came in shaking rain out of your jacket,
Sat two tables over and I lost my place.
I pretended I was reading, you pretended you were working,
Both of us just stealing looks across the room.
Then you asked me what the book was, and I couldn't tell you,
Because I'd never made it past the first line.

[pre-chorus]
And every week I told myself, this isn't anything,
Just coffee and a window and a habit I can't kick.
But I kept coming back at ten, and you kept coming in at ten,
And the girl behind the counter kept on smiling like she knew.

[chorus]
Same corner table, different me, and you still sat down,
Watched a whole year through that window, and you're still around.
I came in pretending, now I'm not pretending anymore,
Same corner table, and I'm not who I was before.
Same corner table, different me, and you still sat down.

[verse]
November, you got to the counter before I did,
Said, oat milk, extra hot, and turned around and grinned.
I didn't know you'd been paying attention,
I'd been so careful to look like I wasn't.
By the time the lights went up along the street outside,
We were sharing one table and pretending it was small.
Then January, the door kept opening and it was never you,
And she wiped your side of the table twice and didn't say a thing.

[pre-chorus]
And every week I told myself, it wasn't anything,
Just coffee and a window and a chair across from mine.
But I kept coming back at ten, and the door stayed shut at ten,
And the foam went flat, and I let it, and I stayed.

[chorus]
Same corner table, different me, and you still sat down,
Watched a whole year through that window, and you're still around.
I came in pretending, now I'm not pretending anymore,
Same corner table, and I'm not who I was before.
Same corner table, different me, and you still sat down.

[instrumental]

[bridge]
March, and the window's open, there's blossom on the street,
I stopped bringing the book, I stopped saving you the seat.
Then the bell above the door, and the rain-shaken jacket,
And you say, it's a long story, is anybody sitting here.
You say, my dad got sick, I went home, I didn't have your number,
And I laugh, because a year of ten o'clocks and I never gave it to you.
I could say a hundred things about the winter,
But I push the sugar over and I say, sit down.

[chorus]
Same corner table, different me, and you still sat down,
Watched a whole year through that window, and you're still around.
I came in pretending, now I'm not pretending anymore,
Here's my number on a napkin, should have done it long before.
Same corner table, different me, and you still sat down.
Same corner table, different me, and you still sat down.

[post-chorus]
The girl behind the counter draws two leaves into the foam,
Sets them down between us, doesn't say a word, and goes.
She's watched the whole thing happen from the first page to the last,
She never had to read it, she was always there.

[outro]
Same chair, same window, same wobble in the leg,
Two coffees going warm beside a book I'll never read.
It was never the table, it was never this street,
It's who keeps showing up, it's who keeps showing up.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 629 → ~5.4 min at 116 wpm, 90% of frame cap |
| Caption + lyrics tokens | 2222 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
