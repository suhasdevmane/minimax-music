# Grandma's Kitchen

**Status: written and verified, NOT rendered. Not yet in the queue.**

Fifty-ninth song. Female lead **Mahima**, soul ballad with a gospel lean,
memories and family, warm and unhurried, US register. 78 BPM, E♭ major
lifting a half step on the final chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 78 BPM, E♭ major with the half-step lift, upright piano, Hammond organ, strings, brushed kit, and the kitchen room tone, AM radio and kettle ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 57 entries — built from the submission's scene direction, plus a two-look character bible, a faceless grandmother, the matched-frame rule between the two kitchens, workflow, the tribute challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json` — 78 BPM is a ballad and the 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 59-grandmas-kitchen
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\59-grandmas-kitchen\caption.txt `
  --lyrics-file songs\59-grandmas-kitchen\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\59-grandmas-kitchen\output\grandmas_kitchen.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Descriptive tag lines (`[intro – hushed, piano, radio and kettle]`, `[chorus – wide, glowing, joyful]`, `[bridge – bare, then building]`, `[final chorus – brighter, choir stack, strings]`) reduced to plain tags | Only the checkpoint's documented tags exist; anything else in a tag line is dropped or sung |
| `[final chorus]` → `[chorus]`, and every repeated chorus written out in full rather than marked as a repeat | The model sings the body literally and would sing the word repeat |
| The performance notes in the section headings — hushed, near-spoken, choir stack — moved into `caption.txt` | Stage directions in the lyric body get sung |

Kept exactly as written: every lyric line, word for word. 78 BPM, E♭ major
with the half-step lift on *"giving it away"*, the instrumentation, the mood
arc, the two-kitchen structure. No trimming was needed — 637 words fits.

## The story and the hooks

An old family kitchen: cardamom in the hall, a radio never turned up, a
grandmother who measured with her hands and told the dough it understood.
A chair pulled to the stove for every scraped knee and bad grade. Then the
present — a small apartment, burnt onions every time, a photograph under a
fridge magnet, and the same radio on a shelf still tuned to the same
station. Her mother tells her she holds the spoon the way her grandmother
did. In the bridge the apron goes on, a friend calls crying, and she hears
herself pull the chair to the stove and say the exact words that were said
to her. The recipe was never lost; it was written into her. By the last
chorus her small apartment is full of people and she leaves the door
unlocked.

**The hook:** *"Everything I know about love, I learned in grandma's
kitchen"* — a tribute template, caption-ready, and it fits over anybody's
home footage.

**The line for captions:** *"She never wrote the recipe, she just lived it
every day."*

**The turn:** *"And I heard her voice come out of me, the same words, the
same key, / Turns out she wrote it down after all, she wrote it into me."*

**The frame that lands:** the chair dragged to the stove in verse one and
again in the bridge, cut against each other — the same move, one generation
on.

**Why it can travel:** grief that has settled into gratitude rather than
sadness, a hook that works as a caption over anyone's family footage, and an
ending that is generous instead of mournful — she gives the love away and
leaves the door open.

## Lyrics as they will be sung

```
[intro]
Cardamom and cinnamon still hanging in the hall,
The radio was always on and never turned up at all.
Flour on the counter, morning sun across the floor,
I could walk that kitchen blindfolded, a thousand times before.

[verse]
She never used a measuring cup, she measured with her hands,
A pinch of this, a little more, she said the dough understands.
She'd hum along to something old while the kettle took the high part,
Pull a chair up by the stove and say, sit, baby, tell me your heart.
I brought her every broken thing, a scraped knee, a bad grade,
She fixed them all with the same two hands and the same thing she made.

[pre-chorus]
She'd say, you don't rush the rising, honey, and you don't skip the salt,
And when somebody leaves the table, that's not always your fault.
She said, you learn it by the feel, girl, you learn it by the smell,
And I'm still learning, standing here, trying to do it half as well.

[chorus]
Everything I know about love, I learned in grandma's kitchen,
Where the door was never locked and nobody went missing.
How to feed a crowd, how to hold a hand, how to let the bread rise slow,
How to leave a light on so the lost ones find their way home.
She never wrote the recipe, she just lived it every day,
Everything I know about love, she taught me anyway.

[verse]
Now it's my apartment, my counter, and the sun still hits the floor,
But I burn the onions every time, and there's no one to ask anymore.
A photo on the fridge, her in that apron, laughing at the lens,
I talk to her while the water boils like the conversation never ends.
Her radio sits on my shelf, still tuned to her old station,
It plays the songs she hummed to teach a hurried girl some patience.

[pre-chorus]
She'd say, you don't rush the rising, honey, and you don't skip the salt,
When the whole thing falls apart, you start again, it's not your fault.
My mother says I've got her hands, the way I hold the spoon,
And I've got her stubborn heart, and I know just what to do.

[chorus]
Everything I know about love, I learned in grandma's kitchen,
Where the door was never locked and nobody went missing.
How to feed a crowd, how to hold a hand, how to let the bread rise slow,
How to leave a light on so the lost ones find their way home.
She never wrote the recipe, she just lived it every day,
Everything I know about love, she taught me anyway.

[instrumental]

[bridge]
So I put on her apron and I set the table for two,
Even though it's only me tonight, that's what she would do.
When my best friend called me crying, I said, come over, don't explain,
I pulled a chair up by the stove and said, sit, baby, tell me your pain.
And I heard her voice come out of me, the same words, the same key,
Turns out she wrote it down after all, she wrote it into me.

[chorus]
Everything I know about love, I learned in grandma's kitchen,
Where the door was never locked and nobody went missing.
How to feed a crowd, how to hold a hand, how to let the bread rise slow,
How to leave a light on so the lost ones find their way home.
She never wrote the recipe, she just lived it every day,
And everything I know about love, I'm giving it away.

[outro]
Cardamom and cinnamon still hanging in the hall,
The radio is always on, I never turn it up at all.
Everything I know about love, I learned it in her kitchen,
And I'll leave the door unlocked in case you need it.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2131 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
