# Two Time Zones

**Status: written and verified, NOT rendered. Not yet in the queue — say when.**

Eightieth song. **Female + male duet** — the same female lead as songs 1–79,
with a warm, slightly unpolished male tenor as Singer B. Cinematic pop
ballad, 90 BPM, C major with no modulation. The production decision the
whole arrangement hangs on: **the drums do not arrive until the second
chorus**, so the first chorus lifts on strings and harmony alone and the
second one lifts off the ground.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 613 sung words |
| [`caption.txt`](caption.txt) | Music description. The female lead's `Vocal Details` lines and the `Sonics` block byte-identical to song 1; Singer B added with a section-by-section `Duet Structure`. 90 BPM, C major, the drums-late arrangement and the two-clock ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 81 entries — with a two-lead character bible, the split-screen rule, and the seam as the recurring motif |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

No `render.json` — at 90 BPM this is a ballad and uses the default 116 wpm
length guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 80-two-time-zones
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\80-two-time-zones\caption.txt `
  --lyrics-file songs\80-two-time-zones\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\80-two-time-zones\output\two_time_zones.wav
```

Expected ~2 h.

## One thing to know before rendering

**It's a duet, and the model has no per-line singer control.** Same
situation as songs 4, 9 and 18: the split lives in the caption's
`Duet Structure` line and the model follows it loosely. This song leans on
the split harder than most — the intro and outro trade line by line, and
the second verse belongs entirely to the male lead. Expect the choruses as
two voices; treat the line-by-line trading as the thing to listen for.

## What changed from the submission

| Change | Why |
|---|---|
| Descriptive tag lines — `[intro – piano, pad, clock tick, voices trading lines]` and the rest — reduced to plain `[intro]`, `[verse]`, `[chorus]` etc. | Text on a tag line is silently dropped by the checkpoint, and only the documented tags exist |
| The performance and arrangement direction moved out of the lyric body into the caption's `Arrangement` and `Global Emotional Progression` blocks | The model sings the lyric body literally |
| Quotation marks removed | Punctuation is not sung |

Kept exactly as written: every lyric line, 90 BPM, C major with no
modulation, the drums-late decision, the instrumentation and the energy arc.
The numbers in the lyric were already spelled as words in the submission, so
nothing needed converting.

## The story and the hooks

Two people eight hours apart, living the same day twice. Her morning is his
night. The song is built out of the arithmetic of that gap: two clocks on
one wall, a weather app for a city she has never stood in, a chair nobody
sits in, a voice note recorded at his two in the morning and heard at her
seven. It is not a sad long-distance song — these two are good at this. The
bridge is where being good at it stops being enough, and it ends with an
aisle seat booked for a Tuesday.

**The hook:** *"Two time zones, one heartbeat."*

**The knife line:** *"I don't want to love you in a rectangle of light."*

**The line for captions:** *"There's an hour on the ocean that belongs to
nobody."*

**The quote:** *"Pencil's for the maybes and I'm sure."*

**The turn:** the bridge drops the metaphor entirely and asks for an
argument about who left the door open, and the boring middle bit.

**Why it can travel:** long distance is a huge, under-served lane, and this
one ends with the flight booked rather than the ache. The two-clocks edit is
the challenge: film your wall with a second clock set to someone else's
city, and post it again the day you take it down.

## Lyrics as they will be sung

```
[intro]
It's ten past six and the kettle's going on,
It's ten past two and I'm nowhere near asleep.
I'm watching a sunrise you already had,
I'm holding a night that you don't get to keep.
There's a clock for me and a clock for you,
Hung on the same wall, both of them true.
Same song playing, different light,
Good morning, love. And good night.

[verse]
I keep your city on my weather screen,
A place I've never stood but check for rain.
You send me photos of your street at midnight,
I send you the first bus and the light on the lane.
There's a chair in here that's yours and nobody sits there,
There's a mug in yours that nobody else can use.
We've got the whole round world turning in between us,
And a line that drops out just when I need the news.

[pre-chorus]
So I count the hours out on my hand,
Take away eight and I know where you are.
There's an hour on the ocean that belongs to nobody,
And I think that's the hour that we share.

[chorus]
Two time zones, one heartbeat,
Your midnight leaning on my morning light.
I'll say good night while you say good morning,
And somewhere in the middle we get it right.
Two time zones, one heartbeat,
Eight hours out and still in time.
Set the clocks however you want to,
Two time zones, one heartbeat, one line.

[verse]
You left a voice note at your two in the morning,
I heard it at seven with my coffee going cold.
You sounded tired and honest and unguarded,
And I played it twice again out on the road.
I marked the calendar in pen and not in pencil,
Because pencil's for the maybes and I'm sure.
There's a moon out here that's already been above you,
And it's carrying your evening to my door.

[pre-chorus]
So I count the hours out on my hand,
Take away eight and I'm already there.
There's an hour on the ocean that belongs to nobody,
And I've built a whole house for us in the air.

[chorus]
Two time zones, one heartbeat,
Your midnight leaning on my morning light.
I'll say good night while you say good morning,
And somewhere in the middle we get it right.
Two time zones, one heartbeat,
Eight hours out and still in time.
Set the clocks however you want to,
Two time zones, one heartbeat, one line.

[instrumental]

[bridge]
I don't want to love you in a rectangle of light,
I want to hear you breathing in the same dark room.
I want an argument about who left the door open,
And the boring middle bit, and I want it soon.
So I booked it. Aisle seat. Tuesday. Bag packed.
Your morning and my morning on the same floor.
One more night of two sunrises and never again,
And then it's one time zone, one door.

[chorus]
Two time zones, one heartbeat,
Your midnight leaning on my morning light.
I'll say good night while you say good morning,
And somewhere in the middle we get it right.
Two time zones, one heartbeat,
Eight hours out but not for long.
Set the clocks however you want to,
Two time zones, one heartbeat, one song.

[post-chorus]
Good morning, good night,
Same moon, different light.
Good morning, good night,
Eight hours apart and holding tight.
Good morning, good night,
Two time zones, one heartbeat, one life.

[outro]
It's ten past six and the kettle's going on,
It's ten past two and I'm packing up my room.
Same song playing, same light finally,
No more counting backwards from the moon.
Two time zones closing into one,
Good morning, love. I'll see you soon.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 613 at 116 wpm → ~317 s (5.3 min), 7927/9000 frames (88% of cap) |
| Caption + lyrics tokens | 2356 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
| Duet declared | `Duet Partner` and `Duet Structure` present |
