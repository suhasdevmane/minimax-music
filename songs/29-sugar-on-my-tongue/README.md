# Sugar on My Tongue

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-ninth song. Female lead **Mahima**, bouncy dance-pop with a
retro-diner twist, kiss-sound percussion and bass drops, flirty and
PG-13. 118 BPM, C minor lifting to E♭ major, the catalogue's uptempo class.
Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 118 BPM, C minor lifting to E♭, the bouncing bass, kiss-sound percussion, the diner ear candy and the bass-drop break. |
| [`render.json`](render.json) | Uptempo pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 91 entries — built from the submission's scene direction, plus a two-look character bible, Kai as the boy, the waitress and cook as a comic pair, the cherry motif, workflow, count-to-three challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 29-sugar-on-my-tongue
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\29-sugar-on-my-tongue\caption.txt `
  --lyrics-file songs\29-sugar-on-my-tongue\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\29-sugar-on-my-tongue\output\sugar_on_my_tongue.wav
```

Expected ~2 h.

## Pacing is unmeasured

Every ballad so far sang at 116–153 words per minute. This one is 118 BPM
with a chant post-chorus, so it will pace faster, but by how much is a
guess until it renders. The lyrics are 730 words. Against the model's
6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.3 min | **overrun — outro lost** |
| 125 wpm | 5.8 min | 97% |
| **140 wpm (the guard setting)** | 5.2 min | 87% |
| 153 wpm (song 3's measured pace) | 4.8 min | 80% |
| 160 wpm | 4.6 min | 76% |

The guard is set at a deliberately conservative 140. **If the first render
truncates the outro, the fix is to drop the second post-chorus (28 words, a
repeat) and re-render.** The measured pacing goes into
`docs/VOICE_RECIPE.md` either way.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around the diner signs and the count removed; no em-dashes | The model sings the lyric body literally |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines reduced to plain tags | Only the checkpoint's documented tags exist |
| Repeated choruses, pre-choruses and the post-chorus written out in full | A `(repeat)` line would be sung |
| The count *"one, two"* is spelled out as words | Digits are sung unpredictably |
| Performance notes (half-spoken bridge, the bar of silence on the count, the kiss-sound hits) moved into the caption | Stage directions in the body would be sung |

Kept exactly as written: every lyric line, 118 BPM, C minor with the lift to
E♭, the instrumentation, the mood arc.

## The story and the hooks

A candy-pink diner after closing. He walks in with his collar up and
pretends he doesn't do dessert; she catches him eyeing the cherry. She
counts to three and stops at two. He slides closer, steals a fry, writes his
number on a napkin; she folds it and says *we'll see*. The cook kills the
kitchen lights, the sign flips, and she wipes the cream off his lip with her
thumb. In the parking lot she reads out the scorecard — he held the door, he
didn't rush, he let her have the last sip — and decides he's earned it. The
sign blazes back on, the cherry goes into his hand, and the last frame is
the cherry alone on the counter as the neon dims.

**The hook:** *"You're like sugar on my tongue, and I've got a sweet tooth
tonight."*

**The line for captions:** *"I don't give it away, I decide."*

**The chant:** *"Sweet tooth, sweet tooth, honey, don't rush."*

**The turn:** *"Okay, okay, you passed the test / You held the door, you
didn't rush, you did your best."*

**Why it can travel:** it is a flirt where she holds every card and enjoys
it, the count-to-three is a ready-made transition for creators, and the
cherry pull-away is a gesture anyone can copy.

## Lyrics as they will be sung

```
[intro]
Cherry on the counter, neon in the glass,
Jukebox humming something slow and I'm not gonna ask.
You walked in like Friday with your collar turned up,
Sit down, honey, I'm about to fill your cup.

[verse]
I got a booth in the corner and a straw with your name,
Vanilla on my lips and you're looking the same.
You're talking about traffic like it's something I need,
I'm watching your mouth and I'm not listening, believe me.
Milkshake sweating on the table between us,
Two spoons and one glass and the whole diner sees us.
You said you don't do dessert, that's a lie and you know it,
Cause you keep sneaking looks at the cherry, don't blow it.
Pink light on the chrome, the cook's playing our song,
And I'm stirring the whipped cream real slow, real long.

[pre-chorus]
Don't act like you're bitter, don't act like you're cool,
I can see the sugar high all over you.
Lean in a little, the waitress won't mind,
I'll count to three, honey, and you'll cross that line.
One, two, and I'm looking at you.

[chorus]
You're like sugar on my tongue,
And I've got a sweet tooth tonight.
One taste and I'm gone, one look and you're done,
Come here, honey, take a bite.
You're like sugar on my tongue,
Sweeter than the syrup on the side.
But sugar, you gotta earn it, come on, learn it,
I don't give it away, I decide.
Sugar, sugar, sugar on my tongue,
Sugar, sugar, sweet tooth tonight.

[post-chorus]
Sweet tooth, sweet tooth, honey, don't rush,
Sweet tooth, sweet tooth, I can see you blush.
Sweet tooth, sweet tooth, sugar on my tongue,
Sweet tooth, sweet tooth, and the night is young.

[verse]
Now you're sliding in closer, your knee against mine,
Stealing fries off my plate like a crime, that's fine.
You wrote your number on a napkin, drew a heart on the end,
I folded it twice, said, we'll see, my friend.
The clock on the wall says the kitchen's closing,
The cook flips the sign but I'm still dosing.
You're sweet like the frosting, but I want the cake,
So show me you're patient for goodness sake.
Wipe that cream off your lip, no, let me do it,
See, that's the kind of slow that I'm into.

[pre-chorus]
Don't act like you're bitter, don't act like you're cool,
I can see the sugar high all over you.
Lean in a little, the jukebox won't mind,
I'll count to three, honey, and you'll cross that line.
One, two, and I'm looking at you.

[chorus]
You're like sugar on my tongue,
And I've got a sweet tooth tonight.
One taste and I'm gone, one look and you're done,
Come here, honey, take a bite.
You're like sugar on my tongue,
Sweeter than the syrup on the side.
But sugar, you gotta earn it, come on, learn it,
I don't give it away, I decide.
Sugar, sugar, sugar on my tongue,
Sugar, sugar, sweet tooth tonight.

[instrumental]

[bridge]
Okay, okay, you passed the test,
You held the door, you didn't rush, you did your best.
You let me have the cherry, let me have the last sip,
You laughed at my jokes and you didn't get slick.
The parking lot's empty and the sign's turning off,
The last song is playing and I'm done playing tough.
Come here, sugar, and I'll say it slow,
You earned it, so now you get to know.

[chorus]
You're like sugar on my tongue,
And I've got a sweet tooth tonight.
One taste and I'm gone, one look and you're done,
Come here, honey, take a bite.
You're like sugar on my tongue,
Sweeter than the syrup on the side.
And sugar, you earned it, look at you, you learned it,
Now I'm giving it away, I decide.
Sugar, sugar, sugar on my tongue,
Sugar, sugar, sweet tooth tonight.

[post-chorus]
Sweet tooth, sweet tooth, honey, don't rush,
Sweet tooth, sweet tooth, I can see you blush.
Sweet tooth, sweet tooth, sugar on my tongue,
Sweet tooth, sweet tooth, and the night is young.

[outro]
Cherry on the counter, neon going dim,
Jukebox playing our song now, and I'm walking out with him.
He's got my number and I've got his hand,
Sweetest thing I ever ordered, and I didn't even plan.
Sugar on my tongue, honey, sugar on my tongue,
Sweet tooth tonight, and the night is young.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 730 at 140 wpm → ~5.2 min, 87% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2424 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
