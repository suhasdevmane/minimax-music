# Polaroids in My Pocket

**Status: rendered 2026-09-03.** → [`output/polaroids_in_my_pocket.wav`](output/polaroids_in_my_pocket.wav)

## Render facts

| | |
|---|---|
| Seed | 42 |
| Length | 312.69 s (5:13) — 632 words at ~121 wpm, close to the estimate |
| Format | 44.1 kHz stereo, peak 1.000, **33 clipped samples** out of 13.8 million (inaudible; the most of the batch so far), 0.12% silence |
| Ending | clean fade (last 0.5 s at 0.004) |
| Envelope | 0.07 intro → 0.12–0.15 verses/chorus → 0.10 dip at the fight verse → 0.17 peak at the final chorus → 0.08 outro; the arc the caption asked for |
| Render time | 7426 s generation, 7458 s total (2 h 04 m), peak VRAM 6.2 GB |
| Sidecar | `output/polaroids_in_my_pocket.json` |

**Did the duet happen? Unverified — needs a listen.** A pitch-tracking proxy
put 67% of analysed windows below 150 Hz, versus 43–57% for the three
female-only songs. That is higher, but inside the spread of the female-only
control, and the proxy is contaminated by bass and 808s even after filtering.
Signal analysis cannot confirm a male voice here. First thing to check by ear:
verse 2 (*"Next one, you asleep on my shoulder"*) and the fight verse, which
the caption assigned to the male lead.

Fourth song. **A duet** — Mahima and a male lead — modern acoustic-pop /
indie-pop with a cinematic build. Mahima's voice is the same as songs 1–3.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, trimmed to fit the 6-minute cap (see below) |
| [`caption.txt`](caption.txt) | Music description. Mahima's four `Vocal Details` lines and the `Sonics` block are byte-identical to song 1; a second singer is added for the duet. Tempo, key and instrumentation follow the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | 43 lyric-anchored shots, character bible (Mahima + Noah), polaroid/phone/split-screen motifs, workflow, teaser, duet challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render

From the repo root:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\04-polaroids-in-my-pocket\caption.txt `
  --lyrics-file songs\04-polaroids-in-my-pocket\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\04-polaroids-in-my-pocket\output\polaroids_in_my_pocket.wav
```

Verify first:

```powershell
.\.venv\Scripts\python.exe scripts\verify_lyrics.py songs\04-polaroids-in-my-pocket --voice-ref songs\01-fire-in-the-rain
```

Estimated render: **~2 h 15 min** on the RTX 4090 Laptop.

## Three things to know before rendering

**1. It's a duet, and the model has no per-line singer control.** The
checkpoint's lyric tags are section tags only — there is no documented way
to mark a line as "male" or "female". The submission's `[verse 1 – Female]`
style tags aren't valid and would be dropped. So the duet structure lives
entirely in the caption: a `Duet Partner` line describing the male voice and
a `Duet Structure` line saying which sections belong to which singer. The
model will follow that loosely, not exactly. Expect the choruses to come out
as two voices in harmony; expect the verse alternation to be approximate.
This is the first duet through this pipeline — treat the render as a test of
what the model does with two singers.

**2. Mahima's voice is locked; the song's key and tempo are not.** The
submission specifies 92 BPM in G major with a lift to A major, and the caption
follows it. Songs 1–3 are 96 BPM in F♯ minor. This is deliberate — a major-key
duet should feel brighter — but it means the singer sits in a different range
than before, so the timbre may read slightly differently even with the same
`Vocal Details`. If it drifts too far, the fallback is to re-render at
F♯ minor / 96 BPM.

**3. The `Sonics` block is still the dark-R&B production profile** from song
1, kept byte-identical for consistency. The acoustic-pop palette is carried in
the `Arrangement` section (fingerstyle and strummed guitar, piano, warm bass,
shaker/kick/snare/snaps, pads and strings in the choruses, the ambient ear
candy — room noise, a laugh, a phone chime on the "good morning" line, a door
closing in the instrumental).

## What was trimmed to fit, and why

The submission is **~880 sung words ≈ 7.6 minutes** at this model's measured
116 words/min. The hard cap is 6.0 minutes. Cut to **632 words ≈ 5.4 min
(91% of cap)**. Everything kept is verbatim.

| Cut | Words | Why safe |
|---|---|---|
| Intro, male stanza (*"We look so young in half of these…"*) | 30 | The male voice now enters in verse 2; the intro is Mahima alone finding the box |
| Pre-chorus 2 (*"learning a new language…"*) | 40 | The second chorus follows the reconciliation verse directly; the sentiment is carried by *"I don't wanna win, I just want us"* |
| Chorus 2, trimmed to 4 lines | 55 | Kept the hook and *"Every stay when we could've gone"*; full 12-line chorus returns for the finale |
| Bridge, two couplets (*"We cried through the whole damn thing…"* and *"We didn't fix everything in one night…"*) | 33 | Kept the packed bag, *"stop being almost"*, the list on the wall, and *"that choice, again and again"* |
| Post-chorus, first 4 of 8 lines | 22 | Kept the *"we're still here"* half, which pays off the outro |
| Outro, *"We're still writing our story / Not perfect, but real, and it's ours / In polaroids and phone screens"* | 17 | Ends on *"We're still here / We're still here"*, which is the stronger last line |

Restored after the first pass left headroom: the verse-2 stanza *"We were
scared of saying I love you… your favourite shade"* and the fight-verse
couplet *"I was scared that if I knocked too loud…"* — both anchor shots.

Non-lyrical cleanups: all singer/performance directions in parentheses and
in the tag lines were removed from the lyric body (they would be sung) and
moved into the caption; quotation marks and em-dashes were removed; the
instrumental's parenthetical went into the caption's arrangement.

## The story and the hook

A couple on the bedroom floor with a shoebox of polaroids: the café where he
tried not to stare, the night train where he watched her breathe, the kitchen
at 3 a.m. where they almost broke, the night he packed a bag and sat back
down, the list they wrote on the living room wall. It starts cute, goes
through real pain, and ends grateful.

**The hook:** *"We're still writing our story / In polaroids and phone
screens."* Visual, modern, and made for couples to overlay their own photos.

**The line people will caption:** *"Every stay when we could've gone."*

**The knife line:** *"We almost broke. We didn't die."*

**The turn:** the bridge — *"Then let's stop being almost / And start being
honest, even if it's scary."*

**Why it can travel:** the duet format is a ready-made couples' duet
template; the specific details (grey hoodie, night train, list on the wall)
are precise enough to feel real and general enough to be anyone's.

## Lyrics as they will be sung

```
[intro]
I found a box beneath our bed,
Full of polaroids we never framed.
Your handwriting on every back,
Little dates and silly names.

[verse]
First photo, you in that old grey hoodie,
Coffee in your hand, trying not to stare.
I was pretending I didn't notice,
But I noticed everything about you there.
Rain on the window, cheap earphones sharing,
Your playlist full of songs I didn't know.
You said, this one feels like how you laugh,
And I fell a little, slow and low.

[verse]
Next one, you asleep on my shoulder,
On that night train to nowhere special.
I didn't sleep, I just watched you breathe,
Thinking, please let this be real, not accidental.
We were scared of saying I love you,
So we said it in the way we stayed.
In the way you saved my side of the sofa,
In the way I learned your favourite shade.

[pre-chorus]
We didn't know we were building a forever,
We were just trying to get through today.
But every little good morning text
Was a brick in the house where our hearts could stay.

[chorus]
We're still writing our story
In polaroids and phone screens,
In late-night talks and are you okay,
In I'm here and please don't go away.
We're still writing our story
Through the mess and the in-betweens,
Every fight, every I was wrong,
Every stay when we could've gone.
If love is a film, then we're the slow scene,
Not the highlight, just the parts in between.
We're still writing our story,
In polaroids and phone screens.

[verse]
Remember that kitchen at 3 a.m.,
When we fought about nothing and everything?
You said, maybe we're just not enough,
I said nothing, let the silence sing.
You cried in the bathroom, I sat on the floor,
Holding a mug I didn't drink.
I was scared that if I knocked too loud,
You'd say, this is it, this is the end.

[verse]
But then you came out with your eyes all red,
Said, I don't wanna win, I just want us.
I dropped every argument I had,
And held you through the shaking and the dust.
That photo's blurry, taken next day,
Both of us laughing, puffy-eyed.
Caption on the back just says,
We almost broke. We didn't die.

[chorus]
We're still writing our story
In polaroids and phone screens,
Every fight, every I was wrong,
Every stay when we could've gone.

[instrumental]

[bridge]
There's one I haven't shown you yet,
Taken the night you almost left.
You packed a bag, then sat back down,
Said, I don't know if I can do this again.
I said, I love you, but I'm tired
Of the distance, of the almosts, of the maybes.
You said, then let's stop being almost,
And start being honest, even if it's scary.
So we wrote a list on the living room wall,
What we're scared of, what we need, what we'll change.
And that choice, again and again,
Is the reason we're still here today.

[chorus]
We're still writing our story
In polaroids and phone screens,
In I'm proud of you and I messed up,
In let's talk and give me space, please.
We're still writing our story
Through the mess and the in-betweens,
Every scar, every we survived,
Every us when it could've been me.
If love is a film, then we're the long cut,
Not the trailer, just the parts no one sees.
We're still writing our story,
In polaroids and phone screens.

[post-chorus]
Polaroids and phone screens,
Polaroids and phone screens.
We're still here, we're still here,
In polaroids and phone screens.

[outro]
I put the box back under the bed,
But I kept a few in my pocket today.
Just in case we forget who we are,
When the world gets loud and the colours fade.
We're still here.
We're still here.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 632 → ~5.4 min, 91% of frame cap |
| Caption + lyrics tokens | 2186 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
