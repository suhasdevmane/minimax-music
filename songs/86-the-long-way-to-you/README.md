# The Long Way to You

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song eighty-six. Female lead **Mahima**, modern country-pop, a decade of wrong
towns reframed as one route, US voice. 100 BPM, A major lifting a whole step
to B for the final chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 637 sung words, mid-tempo ballad budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 100 BPM, A major with the modulation, capoed acoustic and pedal-steel-style electric as the two voices, fiddle from the first pre-chorus, and porch ambience under the intro, bridge and outro. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 64 entries — with a three-look character bible, Kai in the parking lot, the faceless-ex rule, the map's whole life as a through-line, workflow, the pin-map challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 86-the-long-way-to-you
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\86-the-long-way-to-you\caption.txt `
  --lyrics-file songs\86-the-long-way-to-you\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\86-the-long-way-to-you\output\the_long_way_to_you.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung; the model renders the body literally |
| Digits spelled as words (*nineteen*, *twenty-three*, *nine*, *three staircases*, *a hundred times*) | The model sings digits unpredictably |
| The descriptive tag lines (`[intro – acoustic and one steel bend]`, `[bridge – acoustic, organ, no drums]`, `[final chorus – modulated, harmony stack]`) reduced to plain tags | Only the checkpoint's plain section tags exist; anything else is dropped or sung |
| All three choruses written out in full rather than marked as repeats | A `(repeat)` line would be sung |
| Choruses cut from eight lines to six; the *halfway built / calling her a gift* couplet dropped | 718 words on the first pass. The bridge already carries that idea in *somebody's almost*, so the couplet was the redundant one |
| Verse two cut from eight lines to seven (*I had a speech about how I don't do this any more*) | Budget, and the apartment line says it better in one image |

Kept exactly as written: the hook, the map and its pins, the nine towns, the
box that never got unpacked, the parking lot at a quarter after eight, the
exit never taken, the nail hole, 100 BPM, A major with the lift, the
instrumentation and the mood arc.

## The story and the hooks

There is a paper map on her hallway wall with a pin in every town and a length
of thread between them. Nine of the pins are cities; the rest are people. At
nineteen she moved for a boy with a good car and broke the lease in a season.
At twenty-three she took the job because he took the job and learned a whole
city she never learned to like. One never got her coffee order right; one
called her difficult and meant it as a fact. She hauled the same box up three
staircases and never unpacked it. Then the man arrives, and he is deliberately
nobody's idea of a lightning strike: a dead battery in a parking lot at a
quarter after eight, jumper cables, a man who asks a question twice and waits.
The bridge is the exit she passed a hundred times and never took, and the
pleasant, wrong life that was down it. By the last chorus the porch light is
on, the screen door does not latch, and the map is coming off the wall.

**The hook:** *"I took the long way, but the long way led to you."*

**The line for captions:** *"Every year I called a loss was a mile."*

**The knife line:** *"There was one who called me difficult and meant it as a
fact."*

**The turn:** *"If I'd turned there at twenty I'd be somebody's almost, with a
life I'd have to like instead of one I get to love."*

**Why it can travel:** everyone has a version of that map, and the song refuses
to be bitter about a single pin on it. The love interest is ordinary on
purpose, which is what makes the arrival believable, and the pin-map format is
a ready-made video anybody can shoot in their own hallway.

## Lyrics as they will be sung

```
[intro]
There's a map in the hallway with a pin in every town,
Nine of them for cities and the rest for someone's name.
I used to see that thread and call it wasted mileage,
Now I trace it with my finger and it ends up here.

[verse]
At nineteen I moved for a boy with a good car,
Broke the lease in a season, drove back home in the dark.
At twenty-three I took the job because he took the job,
And I learned a whole new city that I never learned to like.
There was one who never once got my coffee order right,
There was one who called me difficult and meant it as a fact.
I kept a box of somebody in the back of every closet,
Hauled it up three staircases and I never once unpacked.

[pre-chorus]
And I asked the road why it kept on bending,
Why the exits showed up early or too late.
Turns out the road was never confused,
The road was taking its time.

[chorus]
I took the long way, but the long way led to you,
Every wrong turn was a road I had to lose.
Every town I couldn't stay in, every name I couldn't keep,
Was a mile of the highway running down to your street.
So here's to every detour, every year I called a loss,
I took the long way, but the long way led to you.

[verse]
And you were not a lightning strike, you were a Wednesday,
A dead battery, a parking lot, a quarter after eight.
You had jumper cables and you knew how not to hurry,
And you asked me twice about the thing I said the first time.
I had an apartment set up not to need a second key.
But you made coffee in the morning like you'd made it here for years,
And the map on the wall went quiet for the first time.

[pre-chorus]
So I stopped asking the road where it was going,
Stopped counting all the mile markers behind.
Turns out the road was never lost,
The road was bringing me home.

[chorus]
I took the long way, but the long way led to you,
Every wrong turn was a road I had to lose.
Every town I couldn't stay in, every name I couldn't keep,
Was a mile of the highway running down to your street.
So here's to every detour, every year I called a loss,
I took the long way, but the long way led to you.

[instrumental]

[bridge]
There's a sign I passed a hundred times and never took,
Somewhere past a town with a diner and a church.
If I'd turned there at twenty I'd be somebody's almost,
With a life I'd have to like instead of one I get to love.
So I'm grateful for the bad ones, I'm grateful for the slow,
I'm grateful for the girl who kept on driving in the dark.

[chorus]
I took the long way, but the long way led to you,
Every wrong turn was a road I had to lose.
Now the porch light's on at midnight and the screen door doesn't latch,
And the map comes down tomorrow, there's a nail hole where it was.
So here's to every detour, every year I called a loss,
I took the long way, but the long way led to you.

[post-chorus]
The long way, the long way,
Nine wrong towns and a right one, all the same.
The long way, the long way,
I would drive every mile of it again.

[outro]
There's a map in the hallway with a pin in every town,
And a pin in this one, and this one's staying in.
I used to call it wasted, all that thread across the country,
Now I call it the long way, and the long way led to you.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2044 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
