# First Kiss at Last Call

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twelfth song. Female lead **Mahima**, anthemic pop-rock with gang vocals,
120 BPM, A major, US register. The catalogue's second uptempo song. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 745 sung words, uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 120 BPM, A major, driving guitars, big room snare, gang vocals, bar-room ambience and a closing door as the last sound. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo song, see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 78 entries — with a two-look character bible, Kai as the male lead, the three-light-state rule, the composited-signage note, workflow, the ugly-light challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 12-first-kiss-at-last-call
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\12-first-kiss-at-last-call\caption.txt `
  --lyrics-file songs\12-first-kiss-at-last-call\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\12-first-kiss-at-last-call\output\first_kiss_at_last_call.wav
```

Expected ~2 h.

## Pacing: uptempo, and the length is an estimate

This is a 120 BPM pop-rock song, not a ballad. Every measured song in the
catalogue so far paced between 116 and 153 words per minute, all of them at
84–98 BPM. At 120 BPM with a driving backbeat the vocal will pace faster, but
by how much is a guess until it renders. The lyrics are **745 words**. What
that means against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| 130 wpm | 5.7 min | 96% |
| **140 wpm (the guard setting)** | 5.3 min | 89% |
| 155 wpm | 4.8 min | 80% |

The chorus and the post-chorus chant are short-lined and will run well above
the average; the verses are conversational and will run below it. A blended
estimate of 140–150 wpm lands between 5.0 and 5.3 minutes. The guard in
`render.json` is set at a conservative 140. **If the first render truncates
the outro, drop the second post-chorus (twenty-eight words, an exact repeat)
and re-render.** The measured pacing goes into `docs/VOICE_RECIPE.md` either
way.

## What changed from the submission

| Change | Why |
|---|---|
| Digits spelled out throughout — *nine o'clock*, *forty bucks*, *ten thirty*, *eleven*, *nine bucks* | The model sings digits unpredictably |
| Quotation marks and em-dashes removed from the sung lines | Punctuation is not sung; the model sings the lyric body literally |
| Descriptive tag lines (*intro – bar at full volume*, *bridge – one clean guitar*) reduced to plain `[intro]`, `[bridge]` and so on; performance directions moved into the caption | Only the checkpoint's documented tags exist, and anything left in the body gets sung |
| The verse-2 rewind and the two chant sections written out in full instead of marked as repeats | The verify script flags parentheses-only lines and the model would sing them |
| The submission's single post-chorus placed after chorus one as well as after the final chorus | The uptempo word budget is met by adding sections, not by inflating verses |

Kept exactly as written: every image, 120 BPM, A major, the guitar and gang-vocal
production list, the three-light-state video logic and the six viral moments.

## The story and the hooks

A whole night in a dive bar that is nothing but near-misses. He plays the
wrong song on the jukebox, they dance badly, his friend keeps calling, her
friend keeps watching, and every time he gets close somebody moves through
the room. Ten thirty he almost, eleven she almost. Out the side door in the
cold he gives her his jacket and puts his hands straight back in his own
pockets, and she could have kissed him in the dark and got away with it, and
she doesn't, because the dark is easy. Then the speakers cut, the chairs go
up, and the houselights bang on across the whole ceiling — green, flat, awful
— and that is where it finally happens.

**The hook:** *"First kiss at last call, lights up and I don't care at all."*

**The line for captions:** *"I never looked better than I did at half past
late."*

**The chant:** *"Kiss me in the ugly light, kiss me at last call."*

**The turn:** *"It beat every version I rehearsed of how it should have gone,
it beat every slow song I was ever saving for someone."*

**Why it can travel:** everybody has had the night of almosts, the houselight
hit is one of the most recognizable images in nightlife, and the song argues
for the unflattering version of a moment over the planned one — which is
exactly the register of a phone-flash, no-filter clip.

## Lyrics as they will be sung

```
[intro]
Nine o'clock, the door swings, the neon buzzing pink,
You had one job tonight and that job was buying me a drink.
Somebody's racking pool, somebody's playing sad,
And I'm already counting up the almosts that we had.

[verse]
Sticky floor, cheap draft, forty bucks in the jar,
A dollar taped to the ceiling with a stranger's name.
There's a dartboard nobody has hit since the summer,
You leaned across the jukebox and you played the worst song there.
I said that is a crime, you said dance to it anyway,
So we did it badly, out of time and out of tune.
Your friend kept calling and my friend kept a look on you,
Every time you got close somebody moved the room.
Ten thirty you almost, eleven I almost, and the night was almost through.

[pre-chorus]
The bartender's counting tips, the stools are going up,
There's a mop bucket sighing and a last song running out.
I thought we'd lost it somewhere between the pool cue and the door,
Then the ceiling opened up and I could not hide anymore.

[chorus]
First kiss at last call,
Lights up and I don't care at all.
No candle, no slow song, no dark to hide in,
Every ugly bulb in the building coming on.
You looked at me like I was the one thing worth the wait,
And I never looked better than I did at half past late.
First kiss at last call,
Lights up and I don't care at all.

[post-chorus]
Lights up, lights up, and the whole town saw,
Lights up, lights up, kiss me in the ugly light.
Lights up, lights up, and I don't care at all,
Kiss me in the ugly light, kiss me at last call.

[verse]
Nine bucks in quarters and a game that we both lost,
You chalked the cue like it mattered and you scratched it on the break.
The beer sign in the window's missing half of its letters,
So it turned your face red and then it turned your face blue.
Somebody's cousin got engaged and the corner booth went up,
And we clapped like we knew her, and you looked at me too long.
Then the side door, and the cold air coming down on my arms,
You gave me your jacket and you kept your hands in yours.
I could have kissed you out there in the dark and got away,
But the dark is easy, and I wanted you to stay.

[pre-chorus]
The speakers cut to nothing, somebody yells last call,
The chairs go up like a curtain coming down on us all.
I figured we would wave goodbye and let it die out on the street,
Then you said my name like a question I already knew.

[chorus]
First kiss at last call,
Lights up and I don't care at all.
No candle, no slow song, no dark to hide in,
Every ugly bulb in the building coming on.
You looked at me like I was the one thing worth the wait,
And I never looked better than I did at half past late.
First kiss at last call,
Lights up and I don't care at all.

[instrumental]

[bridge]
Nobody plans it under the bad light,
Everybody's holding out for candles and a perfect night.
But you got me under the buzz and the beer and the broom,
Cold air in the doorway and a bar going back to a room.
It beat every version I rehearsed of how it should have gone,
It beat every slow song I was ever saving for someone.

[chorus]
First kiss at last call,
Lights up and I don't care at all.
No filter, no shadow, no soft place to land,
Just a bouncer holding the door and your hand in my hand.
You looked at me like I was the one thing worth the wait,
And I never looked better than I did at half past late.
First kiss at last call,
Lights up and I don't care at all.

[post-chorus]
Lights up, lights up, and the whole town saw,
Lights up, lights up, kiss me in the ugly light.
Lights up, lights up, and I don't care at all,
Kiss me in the ugly light, kiss me at last call.

[outro]
The bar sign flickers dead behind us on the street,
Your jacket on my shoulders and nowhere left to be.
Every good light since has come up a little short,
Worst light in the city and the best night of my life.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 745 at 140 wpm → ~5.3 min, 89% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2197 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
