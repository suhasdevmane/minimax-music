# Soft Girl, Steel Spine

**Status: written and verified, NOT rendered. Not yet in the queue.**

Eighty-ninth song. Female lead **Mahima**, trap-pop with a melodic-rap second
verse, 94 BPM, F♯ minor. Ballad/mid pacing class, so no `render.json`. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction exactly as
submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, with the second verse rewritten as real bars (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 94 BPM, F♯ minor, no modulation; felt piano and 808s, with the melodic-rap verse described as a delivery and rhyme-structure change rather than a tag, plus the hand-wrap and coffee-cup textures. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 85 entries — from the submission's scene direction, with a three-look character bible, the pastel/concrete match-cut grammar, the four stairwell women, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 89-soft-girl-steel-spine
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\89-soft-girl-steel-spine\caption.txt `
  --lyrics-file songs\89-soft-girl-steel-spine\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\89-soft-girl-steel-spine\output\soft_girl_steel_spine.wav
```

Expected ~2 h.

## The second verse was rewritten as real bars

The catalogue's *Rap and delivery map* assigns this song **her melodic-rap
second verse**, and the production standard requires real bars — internal
rhyme carrying through the bar, a clear cadence, "not sing-song couplets."
The submission's second verse was six consecutive end-rhyme couplets
(*dark/art, road/code, deal/real, of it/in it, polite/right,
recipe/believe me*) with almost no rhyme anywhere except the line ends. That
is exactly the failure mode the standard names, so the verse was rewritten
in place. Every image and story beat was kept — ballet in the morning and
boxing after dark, the pink on both the pointe shoes and the wraps, the
glittered mouthguard, the cry in the bathroom followed by the closed deal,
the mascara, politeness as a razor — and the rhyme was rebuilt underneath
them:

| Bars | Rhyme |
|---|---|
| pocket / drop it | multisyllabic |
| accident / evidence | multisyllabic slant |
| grin · bring / swing | internal, chained into the end rhyme |
| third stall · at all / whole call | internal, three-way chain across the couplet |
| math / fast | slant |
| quiet · polite / right | internal, then the end rhyme answers it |

Line lengths sit at ten to thirteen syllables, the range the craft standard
gives for rap. The verse ran 107 words before and 119 after; the song moved
from 626 to 640 sung words, still inside the 600–640 ballad budget. The
caption's `Global Emotional Progression` was updated to describe the new
delivery — dry, unhurried, phrases landing just behind the beat, with the
last word of a line answering a word inside the next. **The voice-lock lines
were not touched** and remain byte-identical to song 1.

## What changed from the submission

| Change | Why |
|---|---|
| The second verse rewritten as real bars | The brief assigns a melodic-rap verse; the submission's version was sing-song couplets. See above. |
| `6 a.m.` → *"six a.m."* (twice), `11 minutes` → *"eleven minutes"* | The model sings digits unpredictably |
| Quotation marks removed from the two dialogue lines (*"keep your heart wide open,"* *"keep your guard up"*) | Punctuation is not sung; a quoted phrase can be read as a break in the line |
| Descriptive tag lines — `[intro – felt piano, sub drone, half-whispered]`, `[chorus – big, proud, singable]`, `[verse 2 – melodic rap, dry and pocketed]`, `[bridge – near-spoken, piano and pad, then the kit]`, `[final chorus – fullest arrangement, "say it louder now"]`, `[post-chorus – clipped chant]`, `[outro – felt piano, sub drone, calm]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; there is no `[rap]` tag, so the delivery change lives in the caption |
| The `(repeat)` under the second chorus written out in full | The verify script flags it and the model would sing the word |

Kept exactly as written: every other lyric line, 94 BPM, F♯ minor, the
instrumentation, the mood arc, the six viral moments.

## The story and the hooks

Pink nails, black coffee, six in the morning, and she wraps her hands before
she says amen. She cried in the car, fixed her face in the glass, and walked
in like the whole room asked for her. The song is a correction, not a
complaint: people read the lashes and the pastel set and price her as an
easy bet, and she is not interested in arguing — she is interested in the
fact that feeling everything is the reason she reads a room before its mood
shifts. Her mother told her to keep her heart wide open, her coach told her
to keep her guard up, so she did both, and the lavender candle burns two
feet from the heavy bag. The rap verse is the receipts: studio at six, bag
by the door, pink on the pointe shoes and pink on the wraps because that was
not an accident. Eleven minutes in a bathroom stall with no sound at all,
then blotted, buttoned, back in the room, running the whole call. The
signature went down with a shaking hand and it went down fast. The bridge
widens out to every girl who cried in the stairwell and then walked in and
nailed it, and lands the line the whole song was built to reach.

**The hook:** *"Soft girl, steel spine, don't confuse the two"* — the title
in the first and last line of every chorus.

**The line for captions:** *"Kindness ain't a weakness, kindness is the
proof."*

**The quote:** *"You can be the softest thing in the building, / And still
be the one holding up the ceiling."*

**The rap clip:** *"Cried in the third stall, eleven minutes, no sound at
all, / Blotted, buttoned, walked back in and I ran the whole call."*

**The chant:** the post-chorus — *"Soft, soft, steel, steel, / Cry, then
close the deal"* — is four hard cuts with nothing to learn.

**Why it can travel:** the confidence lane is crowded with songs that win by
putting someone else down, and this one never insults anybody. It is a
two-worlds video with a transition anyone can film — one outfit, one spin,
and you land in the other life — and its central claim, that softness is a
skill rather than a liability, is one a very large audience has been waiting
to hear said plainly.

## Lyrics as they will be sung

```
[intro]
Pink nails, black coffee, six a.m.,
Wrapped my hands before I said amen.
Cried in the car, fixed my face in the glass,
Then I walked in like the whole room asked.

[verse]
They see the lashes and the pastel set,
Think I'm a pushover, easy bet.
Called me sensitive like it's a flaw,
Baby, sensitive is how I saw it all.
I feel everything, that's the gift,
I know the room before the mood shifts.
I'll hold your hand and I'll hold my ground,
Softest voice in here, but I don't back down.
Mom said, keep your heart wide open,
Coach said, keep your guard up, so I did both of them.
Lavender candle next to a heavy bag,
Both of them mine and neither one's an act.

[pre-chorus]
So go ahead, underestimate,
Watch me smile while I take the plate.
Yeah, I cry, and then I win,
Silk on the outside, steel within.

[chorus]
Soft girl, steel spine, don't confuse the two,
I can break down, then break through.
Petal on the outside, iron in the root,
Kindness ain't a weakness, kindness is the proof.
Soft girl, steel spine, say it with me now,
I bend, I bloom, I never bow.
You thought the tears meant I was through,
Soft girl, steel spine, don't confuse the two.

[verse]
Studio at six, bag by the door, gloves in the pocket,
Ballet for the posture, boxing for the way I drop it.
Pointe shoes pink, hand wraps pink, that was not an accident,
Soft is the uniform, the discipline's the evidence.
Glitter on the mouthguard, gloss on the grin I bring,
They saw the sparkle, slept on it, then felt the swing.
Cried in the third stall, eleven minutes, no sound at all,
Blotted, buttoned, walked back in and I ran the whole call.
Mascara did the running, honey, I did the math,
Shook through the signature and still signed it fast.
They asked me for quiet, so I handed them polite,
Politeness is a razor if you angle it right.

[pre-chorus]
So go ahead, read me wrong,
I've been writing the end of this song.
Yeah, I cry, and then I win,
Silk on the outside, steel within.

[chorus]
Soft girl, steel spine, don't confuse the two,
I can break down, then break through.
Petal on the outside, iron in the root,
Kindness ain't a weakness, kindness is the proof.
Soft girl, steel spine, say it with me now,
I bend, I bloom, I never bow.
You thought the tears meant I was through,
Soft girl, steel spine, don't confuse the two.

[instrumental]

[bridge]
To every girl who cried in the stairwell,
Then walked in the room and nailed it,
Who felt every word and still stayed kind,
Who got called weak for a heart that size.
Let them call it soft, let them call it sweet,
Soft is the part they can't defeat.
Cry it out, then stand up straight,
Steel don't bend from a little weight.
You can be the softest thing in the building,
And still be the one holding up the ceiling.

[chorus]
Soft girl, steel spine, don't confuse the two,
I can break down, then break through.
Velvet on the glove, but the punch is true,
Kindness ain't a weakness, kindness is the proof.
Soft girl, steel spine, say it louder now,
I bend, I bloom, I never bow.
You thought the tears meant I was through,
Soft girl, steel spine, don't confuse the two.

[post-chorus]
Soft, soft, steel, steel,
Cry, then close the deal.
Soft, soft, steel, steel,
Pink on the wrap, but the hook is real.

[outro]
Pink nails, black coffee, six a.m.,
Wrap my hands and go again.
Cried in the car and still won the day,
Both of those are me, they're not going away.
Don't confuse the two, don't confuse the two,
Soft girl, steel spine, I'm both, it's true.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2243 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
