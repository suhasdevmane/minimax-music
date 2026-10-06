# I'm the Prize

**Status: written and verified, NOT rendered. Not yet in the queue.**

Seventy-third song. Female lead **Mahima**, trap-pop with melodic-rap verses
and a fully sung chorus, 96 BPM, B minor. Ballad/mid pacing class, so no
`render.json`. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction exactly as
submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, with one bridge line rewritten (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 96 BPM, B minor, no modulation; 808s, a slightly detuned upright piano and rolling hats, with both rapped verses described as a delivery and rhyme-structure change rather than a tag, plus the wet-street and shop-sign textures. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 75 entries — from the submission's scene direction, with a three-look character bible, the retreating-dolly runway grammar, the faceless-men rule, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 73-im-the-prize
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\73-im-the-prize\caption.txt `
  --lyrics-file songs\73-im-the-prize\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\73-im-the-prize\output\im_the_prize.wav
```

Expected ~2 h.

## One line changed for the verse-chorus echo rule

`docs/LYRIC_CRAFT.md` requires the echo check at every transition, **bridge
included**: the last two lines before a chorus must not paraphrase the hook
before the hook lands, and must not reuse the chorus's rhetorical figure.
The bridge as submitted ended:

> I'm not the consolation, I'm not the runner-up,
> I'm the whole of it, and this is how it feels.

That first line is a three-beat list of near-miss nouns in a *not the X, not
the Y* construction, sitting immediately before a chorus whose second line
is *"Not the maybe, not the almost, not the compromise"* — the same device,
the same semantic field and the same position, two beats before the hook.
It flattened the biggest chorus in the song. The line was replaced with
*"And the winning was the part I built alone,"* which keeps the bridge's own
argument moving (the prize is what she built, not what he withheld), calls
back to the trophy shelf in verse two, and answers *"I don't need you to
lose for me to win"* three lines earlier. Nothing else in the lyric was
touched: the rhyme position is unrhymed in both versions, the bridge's
`xAxA xBxB` scheme is unchanged, and the song moved from 638 to 639 sung
words, still inside the 600–640 ballad budget. **The voice-lock lines were
not touched** and remain byte-identical to song 1.

Everything else passed the twelve-point check as written: no self-rhymes and
no repeated end pairs, one point of view held throughout, verse two develops
rather than restates verse one (verse one is his shortlist, verse two is her
shelf), section lengths inside the guide limits for a song with rapped
verses, and no clichés, digits, quotation marks, em-dashes or stage
directions in the body.

## What changed from the submission

| Change | Why |
|---|---|
| The bridge's seventh line rewritten | Verse-chorus echo rule; see above |
| Em-dash removed from the intro (*"Corner shop, wet tarmac—my own two feet"* → a comma) | Punctuation is not sung, and an em-dash can be read as a break in the line |
| Quotation marks removed from *"seeing where it went"* in verse one | Same reason; a quoted phrase inside a sung line reads as a stop |
| Descriptive tag lines — `[intro – piano and sub drone, street ambience, close and unhurried]`, `[verse 1 – melodic rap, dry and pocketed]`, `[chorus – sung, wide, no insult in it]`, `[verse 2 – melodic rap, warmer, the hats halved]`, `[bridge – near-spoken, piano and pad, then the kit]`, `[final chorus – fullest arrangement, last line rewritten]`, `[post-chorus – clipped chant]`, `[outro – piano and drone, calm, resolved]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped or sung |
| `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; there is no `[rap]` tag, so the delivery change lives in the caption's `Global Emotional Progression` |
| The `(repeat)` under the second chorus written out in full | The verify script flags it and the model would sing the word |

Kept exactly as written: every other lyric line, 96 BPM, B minor, the
instrumentation, the mood arc, the six viral moments. No trimming was needed
— 639 words fits.

## The story and the hooks

She was on a shortlist. The door was left on the latch, his cards stayed at
his chest, he told his friends he was seeing where it went and told her
nothing at all, and she filed that under respect. She learned to read his
silence as if it were a language, which is a skill nobody should have to
acquire, and she made a whole week into a window he could stand at whenever
it suited him. Then she stops. She puts the gold on, walks out onto the most
ordinary road in the city and treats it like a runway, and the chorus is not
an insult — it is a correction, sung rather than spat. Verse two is the
evidence: a shelf she calls the trophy room, holding a rent receipt, a scar,
a plant she managed not to kill, a friendship she nearly wrecked and
repaired, and a job she said yes to before she had the skill. None of it is
shiny and all of it is hers. The bridge is where the song stops being about
him at all: a prize is not a thing two women fight over, it isn't on a shelf
and it isn't in a ring, and she does not need him to lose in order to win.
She hopes the other woman is kind. She hopes he is. Then the last chorus,
the same walk, and the outro puts her back on the exact street she started
on, where nothing has changed except her — which, the song says, was always
the only thing that was going to.

**The hook:** *"I'm not the game, baby, I'm the prize"* — the title in the
first and seventh line of every chorus and again in the post-chorus.

**The line for captions:** *"I'm the thing you lose by making somebody
wait."*

**The turn:** *"A prize is not a thing two women fight about. / It isn't on
a shelf and it isn't in a ring, / It's the quiet in my chest when the noise
runs out."*

**The rap clip:** *"I used to read your silence like it was a language, /
Learned a dialect of waiting that nobody should learn."*

**The chant:** the post-chorus — *"Slow walk, gold light, chin up, eyes
ahead"* — is four half-second cuts and nothing to memorise.

**Why it can travel:** the self-worth lane is full of songs that win by
humiliating the ex, and this one never raises its voice or names a rival —
the bridge explicitly refuses the catfight the genre usually reaches for,
which is the part people quote. The video costs nothing: one wet residential
street, one coat, and a camera walking backwards, so the challenge is
literally *film your most boring road and walk it like a runway*. And the
trophy-shelf verse gives the song a second life outside the breakup context
entirely, as a list anyone can make of the unglamorous things they survived.

## Lyrics as they will be sung

```
[intro]
Gold light on an ordinary street,
Corner shop, wet tarmac, my own two feet.
You've been running the numbers on me all this time,
Like the risk is mine.

[verse]
You had me on a shortlist with a couple of maybes,
Door left on the latch and your cards to your chest.
Told your boys you were seeing where it went,
Told me nothing at all, and I called that respect.
I used to read your silence like it was a language,
Learned a dialect of waiting that nobody should learn.
Made my whole week a window you could stand at,
And you came when it suited and you left when it turned.
I'm not doing an interview, I'm not doing a trial,
I'm not auditioning for a part in my own life.

[pre-chorus]
So I got up slow and I put the gold on,
Walked out into a night that wasn't yours.
Every ordinary street I've been down
Turned into a runway under lamps and open doors.

[chorus]
I'm not the game, baby, I'm the prize,
Not the maybe, not the almost, not the compromise.
I'm not the thing you win for turning up late,
I'm the thing you lose by making somebody wait.
Take your time, take your shot, take your chances elsewhere,
I've got gold light and a street and my own self.
I'm not the game, baby, I'm the prize,
And I'm done being somebody's nice surprise.

[verse]
There's a shelf in my place that I call the trophy room,
A rent receipt, a scar, and a plant I didn't kill,
A friendship I nearly wrecked and then repaired,
A job I said yes to before I had the skill.
None of it is shiny and all of it is mine,
And it took a lot of quiet to get here.
So when you ask me what I bring, I laugh,
Because I'm standing on a decade you weren't near.

[pre-chorus]
So I got up slow and I put the gold on,
Walked past every doorway I used to wait.
Every ordinary corner in this city
Turned into a runway, and I'm not late.

[chorus]
I'm not the game, baby, I'm the prize,
Not the maybe, not the almost, not the compromise.
I'm not the thing you win for turning up late,
I'm the thing you lose by making somebody wait.
Take your time, take your shot, take your chances elsewhere,
I've got gold light and a street and my own self.
I'm not the game, baby, I'm the prize,
And I'm done being somebody's nice surprise.

[instrumental]

[bridge]
Here's the part I didn't understand for years,
A prize is not a thing two women fight about.
It isn't on a shelf and it isn't in a ring,
It's the quiet in my chest when the noise runs out.
I don't need you to lose for me to win,
I hope she's kind, I hope you're kind, I hope it's real.
And the winning was the part I built alone,
I'm the whole of it, and this is how it feels.

[chorus]
I'm not the game, baby, I'm the prize,
Not the maybe, not the almost, not the compromise.
I'm not the thing you win for turning up late,
I'm the thing you lose by making somebody wait.
Keep your time, keep your shot, keep your chances elsewhere,
I've got gold light and a street and my own self.
I'm not the game, baby, I'm the prize,
And I've stopped waiting to be recognized.

[post-chorus]
Slow walk, gold light, chin up, eyes ahead,
No rush, no proof, no test,
I'm not the game, baby, I'm the prize,
And I always was.

[outro]
Corner shop, wet tarmac, gold across the glass,
Same street I have walked a thousand times.
Nothing here is new about tonight but me,
And that was always it, and that was always mine.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2261 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
