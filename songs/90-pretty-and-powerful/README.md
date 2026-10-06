# Pretty and Powerful

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song ninety. **Female + male duet with rap** — Mahima on the melodic lead,
a male rapper as Singer B on both rap verses — hip-hop pop with cinematic
brass and a stadium chant, 100 BPM, G minor, US register. Uptempo class
because of the raps, so it carries a `render.json`. Same singer as songs 1–8
for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 756 sung words, inside the uptempo budget |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1; a rapper added as Singer B with a section-by-section duet structure. 100 BPM, G minor, the brass and 808 spine, the heel-strike percussion. |
| [`render.json`](render.json) | Uptempo pacing for the length guard (`wpm: 140`) |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 90 entries — with a three-look Mahima bible, Kai as the rapper, the faceless-boardroom rule, the gold-and-black palette lock, workflow, the chant challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 90-pretty-and-powerful
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\90-pretty-and-powerful\caption.txt `
  --lyrics-file songs\90-pretty-and-powerful\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\90-pretty-and-powerful\output\pretty_and_powerful.wav
```

Expected ~2 h.

## Pacing warning

Uptempo class, and pacing is estimated rather than measured. The lyrics are
**756 words**, of which 138 are in the two male rap verses. Against the
model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 130 wpm | 5.8 min | 97% |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 160 wpm | 4.7 min | 79% |

A rap verse at 100 BPM runs 150–190 wpm while the sung sections sit nearer
120, so a blended 140–150 is the realistic expectation. **If the first
render truncates the outro, drop the second post-chorus (twenty-two words, a
repeat) and re-render.**

Second thing to know: **the model has no per-line singer control.** As with
songs 4 and 8, the split lives entirely in the caption's `Duet Structure`
line and the model follows it loosely. Expect the choruses as two voices;
the two rap verses are the real test.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and question marks removed from the sung lines (`"Which salon, which shade…"`, `"too much"`, `"Hey, don't lower the light"`) | Punctuation is not sung and quotation marks confuse the phrasing |
| Em-dashes replaced with commas or full stops throughout | Not sung; they break the phrasing model |
| Descriptive tag lines (`[verse 1 – her, dry and melodic]`, `[verse 2 – his rap, beat drops]`, `[post-chorus – crowd chant]`) reduced to plain `[verse]`, `[post-chorus]` | Only the plain tag set exists; text on a tag line is dropped, and there is no `[rap]` tag |
| The `(repeat)` markers for the second chorus, the final chorus and the second post-chorus written out in full | The model would sing the word *repeat* |
| Performance notes (*near-spoken*, *both voices*, *brass an octave up*) moved into the caption | The lyric body is sung literally |
| Two lines cut from the third verse and two from the bridge | The submission ran 853 words, over the 781-word uptempo cap |

Kept exactly as written: the hook, both rap verses in full, 100 BPM, G minor,
the brass and 808 instrumentation, the gold-and-black world and the mood arc.

## The story and the hooks

She is asked the wrong question in every room she walks into. Her face is on
the cover of the pitch deck and her name is missing from the credits line;
the forecast question goes to the man at the far end of the table and she
gets asked which salon. So she answers the question nobody asked her, names
the margin first, and keeps walking. He takes the second verse and vouches
without explaining: she is not a muse, she is the architect, and you built a
hallway she simply widened. By verse three her name is on the glass, she has
stopped shrinking her laugh, and she hires the woman they called too much.
His second verse is the honest one — he was raised on the same false choice
and had to unlearn it, and he tells his little sister not to lower the
light. Then the bridge, on the floor in front of a mirror, where she names
the years she spent cutting herself in half and stops.

**The hook:** *"Pretty and powerful, don't make me choose."*

**The chant:** *"Gold and black, gold and black / Front of the room and I'm
not moving back."*

**The line for captions:** *"Pretty was never a place I was hiding, it's the
door I walk through, it is not the building."*

**The rap clip:** *"Y'all built a hallway, she just widened up the line."*

**The turn:** *"Beauty is not the rent I pay to keep the skill. Both of them
mine, and I'm not choosing. I never will."*

**Why it can travel:** it declines a question millions of women get asked
weekly, it has a stamping four-beat chant built for outfit-change
transitions, and the male feature is a co-signer rather than a love
interest, which is a role this catalogue has not used yet.

## Lyrics as they will be sung

```
[intro]
Warehouse mirror, cold floor, gold light,
Heels in one hand, a contract in the other.
They keep asking me which one is the real one.
Both of them. Run it up.

[verse]
They put my face on the cover of the deck,
Left my name off the line where the credit gets checked.
He got the forecast question, I got the small talk,
Which salon, which shade, which designer, which walk.
So I named the margin before they could ask,
And I let the number do the talking, then I laughed.
Pretty was never a place I was hiding,
It's the door I walk through, it is not the building.

[verse]
Watch her walk in the warehouse, whole room recalibrate,
Gold on the collar, but the mind is what intimidates.
They clocked the glow and they slept on the resume,
Now they in the back row taking notes on how she runs the day.
She ain't a muse, she the architect, she drafted the design,
Y'all built a hallway, she just widened up the line.
Call her pretty, cool, but say the whole sentence,
Pretty and the payroll and the plan and the presence.

[pre-chorus]
Two things are true at once, they always were,
Don't hand me a mirror and call it a career.
I can be the picture and the one who takes it,
I can be the plan and the one who makes it.

[chorus]
Pretty and powerful, don't make me choose,
I'll take the heels and the hard-earned bruise.
Gold in my ears and the numbers in my hand,
Look good, close it out, that was always the plan.
You want the gloss or you want the grind,
Both of them living in the same mind.
Pick a lane for me, but I already do,
Pretty and powerful, don't make me choose.

[post-chorus]
Gold and black, gold and black,
Front of the room and I'm not moving back.
Pretty. Powerful. Both at once.
Don't make me choose.

[verse]
Fifth floor glass and my name on the wall,
Same faces, same questions, different tone in the call.
I do not owe this table a plainer face,
And I don't shrink my laugh to fit a smaller space.
They said pick one, so I picked the two,
Then I hired the girl they said was too much too.

[verse]
I'll be honest, I was taught that a woman had to trade,
Look good or get respected, only one of them pays.
Then I sat in the back while she carried a whole floor,
Charts up the wall and a warehouse on tour.
Told my little sister, hey, don't lower the light,
Nobody dims the sun to make the moon look right.
So say it all together, don't split it in two,
Pretty and powerful, that is just her, that's the truth.

[pre-chorus]
Two things are true at once, they always could,
Don't call it a lucky face, it was hours and good.
I can be the picture and the one who takes it,
I can be the plan and the one who makes it.

[chorus]
Pretty and powerful, don't make me choose,
I'll take the heels and the hard-earned bruise.
Gold in my ears and the numbers in my hand,
Look good, close it out, that was always the plan.
You want the gloss or you want the grind,
Both of them living in the same mind.
Pick a lane for me, but I already do,
Pretty and powerful, don't make me choose.

[instrumental]

[bridge]
For years I cut myself in half to fit the room,
Wore the quiet one to work, saved the loud one for the moon.
Grew up on lip gloss and long division,
Nobody told me I had to pick a religion.
Beauty is not the rent I pay to keep the skill,
Both of them mine, and I'm not choosing. I never will.

[chorus]
Pretty and powerful, don't make me choose,
I'll take the heels and the hard-earned bruise.
Gold in my ears and the room in my hand,
Look good, close it out, that was always the plan.
You want the gloss or you want the grind,
Both of them living in the same mind.
Two of us saying it, so you say it too,
Pretty and powerful, don't make me choose.

[post-chorus]
Gold and black, gold and black,
Front of the room and I'm not moving back.
Pretty. Powerful. Both at once.
Don't make me choose.

[outro]
Warehouse mirror, cold floor, gold light,
Heels on, folder closed, both of them right.
Don't make me choose.
Never had to choose.
Pretty and powerful.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 756 at 140 wpm → ~5.4 min, 90% of frame cap |
| Caption + lyrics tokens | 2540 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
