# The Old Playlist

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixtieth song. Female lead **Mahima**, lo-fi pop / nostalgia pop with a
full-fidelity cinematic chorus, US register, 88 BPM, D major. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 637 sung words, ballad class |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 88 BPM, D major, Rhodes spine, dusty sampled kit, vinyl crackle that ducks away in the choruses. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a three-look character bible, a faceless ex, the aisle-of-rooms device, workflow, the old-playlist challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 60-the-old-playlist
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\60-the-old-playlist\caption.txt `
  --lyrics-file songs\60-the-old-playlist\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\60-the-old-playlist\output\the_old_playlist.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads em-dashes unpredictably |
| Every number spelled as a word — *twelve percent*, *three years*, *track eleven*, *thirty tracks*, *five minutes*, *nineteen* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro — bus ambience, vinyl, Rhodes, no drums]`, `[verse 1]`, `[final chorus]`) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the documented plain tags exist; anything else is dropped or sung |
| Every repeated chorus written out in full rather than marked as a repeat | A repeat marker would be sung as a lyric |
| Performance directions (half-time bridge, the vinyl ducking, the tape-stop between sections) moved into `caption.txt` | The model sings the lyric body literally |

Kept exactly as written: every lyric line, 88 BPM, D major, the instrumentation,
the aisle-of-rooms video concept and the mood arc. No trimming of content was
needed beyond tightening three chorus lines to land inside the word budget.

## The story and the hooks

Last bus of the night, twelve percent of battery, and a playlist she built at
nineteen and has not opened in three years. She hits shuffle. A summer of
double shifts, a car with four people shouting one line, a blue kitchen table
and a boy with a rucksack already by the door. Then the track she always
skipped, which turns out to be only a good song, and a voice memo she recorded
by accident and cannot explain any more. The bus goes past her stop. The turn
is that she does not want the year back: she wants five minutes in the seat
beside the girl who made the playlist, long enough to tell her it costs more
than she has planned and she still gets there. Then the battery dies, the doors
open, and she adds one new song to the bottom of the list.

**The hook:** *"Hit shuffle on the old playlist and I'm nineteen again."*

**The line for captions:** *"I know how it ends, and I still want it back."*

**The turn:** *"I only want five minutes on this bus beside her / Just enough
to tell her what's ahead."*

**The last line that lands:** *"Hit shuffle on the old playlist and I get to
be her friend."*

**Why it can travel:** everybody has a dead playlist with a name they would
not say out loud now. The video device is free to copy — a screen recording
of your own oldest playlist — and the ending is generous rather than sad.

## Lyrics as they will be sung

```
[intro]
Last bus out and the windows are sweating,
Twelve percent of battery to spare.
I push the old white earbuds in and settle,
And a name I stopped saying is there.

[verse]
Track one is a summer of working the doubles,
Grease on my sleeve and the walk home at three.
Track two is a back seat with somebody's cousin,
All of us shouting the part we can't reach.
Skip, and it lands on a blue kitchen table,
A boy who was leaving before the leaves turned.
I made this in a bedroom with a map on the ceiling
And a whole lot of nerve I hadn't earned.

[pre-chorus]
I only meant to check the time and get home,
I did not mean to open up a door.
But the first four seconds hit me like a hallway
I have not walked down in three years or more.

[chorus]
Hit shuffle on the old playlist and I'm nineteen again,
Cheap perfume, borrowed denim, the whole night to spend.
Every song is a door I never got around to closing,
Every chorus is a room with all the lights still glowing.
Nothing bad has happened yet inside a three-minute track,
I know how it ends, and I still want it back.
So let the window fog, let the long way be the plan,
Hit shuffle on the old playlist and I'm nineteen again.

[verse]
Track eleven is the one I always used to skip,
He was the only reason it was ever on the list.
Tonight I let it play the whole way to the ending,
And it's only a good song. That's the whole of what I missed.
There's a voice memo buried near the bottom of the album,
Somebody laughing, half a sentence, then it's gone.
I can't tell you what was funny anymore,
But I can tell you who I was when I put it on.

[pre-chorus]
I only meant to ride until my stop,
I did not mean to fall through thirty tracks.
But a bassline from a song I half remember
Hands me that whole summer, all of it, right back.

[chorus]
Hit shuffle on the old playlist and I'm nineteen again,
Cheap perfume, borrowed denim, the whole night to spend.
Every song is a door I never got around to closing,
Every chorus is a room with all the lights still glowing.
Nothing bad has happened yet inside a three-minute track,
I know how it ends, and I still want it back.
So let the window fog, let the long way be the plan,
Hit shuffle on the old playlist and I'm nineteen again.

[instrumental]

[bridge]
I wouldn't go back, and I want that on the record,
I like my life, I like my quiet, I like my bed.
I only want five minutes on this bus beside her,
Just enough to tell her what's ahead.
That it's going to cost her more than she has planned,
And she still gets there. Tired, but she lands.

[chorus]
Hit shuffle on the old playlist and I'm nineteen again,
Cheap perfume, borrowed denim, the whole night to spend.
Every song is a door I never got around to closing,
Every chorus is a room with all the lights still glowing.
Nothing bad has happened yet inside a three-minute track,
I know how it ends, and I don't need it back.
So let the window fog, let the driver make the bend,
Hit shuffle on the old playlist and I get to be her friend.

[post-chorus]
Nineteen again, nineteen again,
Two stops out and the battery's at one.
Nineteen again, nineteen again,
Let it play, let it play till it's done.

[outro]
Doors hiss open and the cold comes in,
Earbuds out, I put the old thing away.
But I added one more song before I stood up,
Something from tonight, for whoever's listening one day.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2079 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
