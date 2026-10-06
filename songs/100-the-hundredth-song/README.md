# The Hundredth Song

**Status: written and verified, NOT rendered. Not yet in the queue.**

The hundredth and final song of the catalogue. **Female + male duet** —
Mahima on the lead, a warm baritone storyteller as Singer B — anthemic
cinematic pop, 98 BPM, F♯ minor lifting to A major, solo piano to full band,
orchestral strings and choir. Same singer as songs 1–99 for the female lead;
Singer B carries verse two and the spoken-word section before the last
chorus. It is the closer, so it is written about all ninety-nine songs before
it and about the people who took them: no titles quoted, no lines borrowed,
only the rooms the songs ended up in.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 636 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock; Singer B added with a section-by-section duet structure that puts the spoken word before the final chorus. 98 BPM, F♯ minor into A major, solo piano, cello, full strings, choir, timpani, with room tone, a piano stool creak and a distant hall crowd as ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 70 entries — the rehearsal room, the growing stage, a closing montage of the catalogue's video worlds, a three-look character bible with Kai, workflow, the hundred challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 98 BPM this is a ballad/mid song and the 600–640 word
budget applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 100-the-hundredth-song
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\100-the-hundredth-song\caption.txt `
  --lyrics-file songs\100-the-hundredth-song\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\100-the-hundredth-song\output\the_hundredth_song.wav
```

Expected ~2 h.

## One thing to know before rendering: the spoken word

Same situation as songs 4, 8 and 9 — the model has no per-line singer
control, so the duet split lives in the caption's `Duet Structure` line and
the model follows it loosely. Two things to check on the first render: the
second verse should come out male, and the seven-line section before the
final chorus should come out spoken rather than sung. The caption removes
the drums under it and says *spoken word with no singing at all* twice, which
is the strongest steer available. If it renders sung, it still works as a
verse; if the outro truncates, the post-chorus is the section to cut.

## What changed from the submission

| Change | Why |
|---|---|
| `99` → *"Ninety-nine"* in the intro and three times in the spoken section | The model sings digits unpredictably |
| Quotation marks around *"that one got me through"* removed | Punctuation is not sung; the comma before it carries the pause |
| `[intro – solo piano, her alone]`, `[verse 1 – her]`, `[spoken – him]`, `[final chorus – both]` and the other descriptive tag lines reduced to plain tags; the her / him / both split moved to the caption's `Duet Structure` line | The model only knows plain section tags and sings the lyric body literally |
| The spoken-word section tagged `[verse]` | `[spoken]` and `[rap]` are not in the permitted tag set; the delivery instruction lives in the caption |
| Repeated pre-chorus and choruses written out in full | The model would sing a `(repeat)` line |
| Verse two, line six: *"the room was full of gold"* → *"the room was gold, and made it true"* | Craft audit. The verses rhyme their even lines in pairs (two with four, six with eight); in verse two, *gold* and *do* left the second pair orphaned. The new line restores the pair on a full rhyme and sets up *"and they do"* two lines later |

Kept exactly as written: every other line, 98 BPM, F♯ minor into A major, the
instrumentation, the mood arc. No trimming was needed — 636 words sits inside
the ballad budget with room to spare.

## The story and the hooks

A woman alone in a rehearsal room with a borrowed microphone, a cable on the
floor and a door that will not close, counting what a hundred songs actually
did. Her verse counts them as people rather than titles: a girl in the first
one learning how to leave, a girl in the fortieth still learning how to stay,
kitchens and taxis and a bus at six. Then the man who came in on one verse
and never left the floor takes his own verse, and gives the record its
thesis from the wrong end of it — a back room above a pub, nine people in the
chairs, and she sang it like the room was gold. The bridge is the smallest
moment: a woman in a hallway after a show says one of them got her through,
and that sentence turns out to be more useful than anything on the record.
He answers it with spoken word, no drums, no singing, doing the arithmetic
of ninety-nine nights out loud. Then the key change, the choir, and the
crowd carrying the hook without her. The last frame is an empty stage with
one microphone still warm.

**The hook:** *"This is the hundredth song, and I'm still singing."*

**The line for captions:** *"A hundred is a doorway, not a wall."*

**The quote:** *"She didn't write a hundred songs. She wrote one song a
hundred times, and everyone who heard it was certain it was theirs."*

**The knife line:** *"Then a woman in a hallway said, that one got me
through."*

**The turn:** *"I used to think the point of this was being heard"* — the
whole record reverses on that line, from being heard to being useful.

**Why it can travel:** it is a closer that refuses to be a farewell. The
spoken section is a forty-second quotable block, the modulation is a
one-second postable frame, and the empty stage with one microphone is an
end-card that works silent, with no text, as the last post of the campaign.

## Lyrics as they will be sung

```
[intro]
It started in a room with a borrowed microphone,
A cable on the floor and a door that wouldn't close.
I had no plan, I had a hundred things to say,
And I've said ninety-nine of them, so here goes.

[verse]
There's a girl in the first one learning how to leave,
And a girl in the fortieth still learning how to stay.
There were kitchens and taxis and a bus at six,
And every one of them was somebody's whole day.
I sang about a summer like it was a person,
I sang about a doorway I was frightened to walk out.
I gave away my worst night so yours would feel smaller,
And that's how you put a heavy thing down.

[pre-chorus]
The last note of a song isn't an ending,
It's the room going quiet enough to hear.
If you came in late, if you only know the one,
Pull a chair to the front, we're nearly there.

[chorus]
This is the hundredth song, and I'm still singing,
Same two hands, same crack in the same high note.
Ninety-nine goodbyes, a hundred ways to begin,
And a voice you carried further than I could alone.
Sing the part you know, I'll hold the rest,
This is the hundredth song, and I'm still singing.

[verse]
I came in on a verse, I was only meant to stay,
Then a hundred rooms went by and I never left the floor.
I've watched a stadium learn a private thing by heart
And hand it back to her a little louder than before.
Some nights the sound was awful and the crowd was nine,
And she sang it like the room was gold, and made it true.
That's the whole trick, if anybody asks,
You sing the small ones like they matter, and they do.

[pre-chorus]
The last note of a song isn't an ending,
It's the sound of a room breathing in the dark.
If you came in late, if you only know the one,
That's enough, that was always enough to start.

[chorus]
This is the hundredth song, and I'm still singing,
Same two hands, same crack in the same high note.
Ninety-nine goodbyes, a hundred ways to begin,
And a voice you carried further than I could alone.
Sing the part you know, I'll hold the rest,
This is the hundredth song, and I'm still singing.

[instrumental]

[bridge]
I used to think the point of this was being heard,
Then a woman in a hallway said, that one got me through.
I've never written anything as useful as that sentence,
So I keep the microphone and I keep making room.

[verse]
Ninety-nine of these. Think about that.
Ninety-nine nights somebody played one on the wrong side of a hard week.
Ninety-nine kitchens, airports, back seats, bus stops.
She didn't write a hundred songs. She wrote one song a hundred times,
And everyone who heard it was certain it was theirs.
That is not a career. That is a promise kept.
So here it is, the last one, which is a funny way of saying the next one.

[chorus]
This is the hundredth song, and I'm still singing,
Same two hands, same crack in the same high note.
A hundred ways of leaving, a hundred coming home,
And a voice that was never only mine to hold.
Take the part you love, leave the rest behind,
This is the hundredth song, and I'm still singing.

[post-chorus]
Still singing, still here, still yours,
Still finding new ways to say the same true thing.
Still singing, still here, still ours,
A hundred is a doorway, not a wall.

[outro]
An empty stage, one light, a microphone still warm,
And a cable on the floor where all of it began.
Whoever picks it up next, I hope the room is loud,
This is the hundredth song, and I'm still singing.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 636 → ~5.5 min at 116 wpm, 91% of frame cap (8224/9000) |
| Caption + lyrics tokens | 2460 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
