# Cry in the Uber

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song sixty-nine. Female lead **Mahima**, sad pop and cinematic downtempo,
piano, sub-bass and real rain, 90 BPM, F minor, UK register with London
detail. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, ballad budget, no `render.json` |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 90 BPM, F minor, felt piano and deep sub, the rain, wet-road hiss, indicator and siren textures, and the bar of rain alone inside the instrumental. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 68 entries — with a two-look character bible, a driver seen only in fragments, a faceless ex, through-glass plate guidance, workflow, the window challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 69-cry-in-the-uber
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\69-cry-in-the-uber\caption.txt `
  --lyrics-file songs\69-cry-in-the-uber\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\69-cry-in-the-uber\output\cry_in_the_uber.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed, including around the driver's and the ex's spoken lines | Punctuation is not sung; the model reads the body literally |
| Digits spelled out — *three minutes*, *eleven minutes*, *half an hour*, *five stars* | The model sings digits unpredictably |
| Descriptive tag lines (`[chorus 1 — strings swell, no drop]`, `[bridge — close voice…]`) reduced to plain `[chorus]`, `[bridge]` | Only the documented plain tags exist; text on a tag line is dropped |
| Every repeated chorus written out in full; the final chorus given a new fifth line and a past-tense close | The model would sing a `(repeat)` marker, and the tense change is the whole resolution |
| Chorus trimmed from eight lines to six | At 90 BPM an eight-line chorus repeated three times pushed the sung-word count past the ballad budget; six lines keeps the hook twice per chorus and the song inside 5.5 minutes |

Kept exactly as written: the hook, 90 BPM, F minor, the arrangement list,
the London geography and every image in the submission.

## The story and the hooks

She holds her face together through a goodbye in his kitchen, down his
stairs, past his neighbours coming in out of the rain, and onto a wet
pavement where she watches a small blue dot crawl round the block towards
her. Then she gets into a stranger's car and gives herself exactly one
journey. The driver turns the radio down without being asked, puts the
heating on her side, says nothing, and at a red light passes back a packet
of tissues without looking in the mirror — which is the kindest thing
anybody has said to her all week. The thing that ended it was not a shout or
a slammed door; it was a quiet sentence he had clearly rehearsed on the walk
back from the shop. Somewhere near the bridge the crying stops on its own,
the way rain does. She tips him more than she has, finds her keys, and opens
her own door.

**The hook:** *"Let me cry in the Uber, I'll be fine by my door."*

**The line for captions:** *"I'm not fine, but I'm fine enough to open my
door."*

**The knife line:** *"No shout, no slammed door, no reason I can hold / Just
a quiet, I think that we should stop."*

**The turn:** *"Near the bridge the crying stops of its own accord / The way
rain does, without deciding to."*

**Why it can travel:** everyone has had the ride home, and the small kindness
of a stranger who says nothing is one of the most under-written moments in
pop. The five-stars post-chorus is a ready-made caption, and the
streetlights-on-glass frame is a single shareable image.

## Lyrics as they will be sung

```
[intro]
On the pavement in the rain outside your door,
Watching a small blue dot come crawling round the block,
Three minutes, then two, then none,
And I hold it in until the door clicks shut.

[verse]
He says you alright, love, is it Peckham, is that right,
I say yes, and my voice comes out in bits.
A bottle of water in the door, a charger on the seat,
A cardboard pine tree turning where the mirror sits.
He turns the radio down before I have to ask,
Puts the heating on my side and doesn't say a word.
The wipers keep a rhythm that my ribs are trying to match,
And the whole of south London goes by, blurred.

[pre-chorus]
Not on your stairs, not in your street,
Not while your kitchen light was still on.
I kept my face together for eleven minutes,
And now the door is shut and you're gone.

[chorus]
Let me cry in the Uber, I'll be fine by my door,
Half an hour, that's all, I won't ask for more.
Let the streetlights run like water down the glass,
Let a kind man with the heating on let it pass.
Let me cry in the Uber all the way through town,
I'll be fine by my door, I just can't be fine now.

[verse]
At the lights he passes back a packet of tissues,
Doesn't look in the mirror, keeps his eyes on the road ahead.
Says the traffic's proper bad round Elephant and Castle,
Which is the kindest thing that anyone has said.
And I think about your kitchen and how you said it,
Like a thing that you'd rehearsed on the way back from the shop.
No shout, no slammed door, no reason I can hold,
Just a quiet, I think that we should stop.

[pre-chorus]
Not in your hallway, not on your stairs,
Not with your neighbours coming in from the rain.
I held it through the goodbye and the going,
And now the New Cross Road can take the strain.

[chorus]
Let me cry in the Uber, I'll be fine by my door,
Half an hour, that's all, I won't ask for more.
Let the streetlights run like water down the glass,
Let a kind man with the heating on let it pass.
Let me cry in the Uber all the way through town,
I'll be fine by my door, I just can't be fine now.

[instrumental]

[bridge]
Near the bridge the crying stops of its own accord,
The way rain does, without deciding to.
The lights come off the water in a long gold line,
And the city carries on without you.
He says, that's you there, love, mind how you go,
And I tip him more than I have and tell him so.
The rain has come to nothing by the time I reach my floor,
And I'm not fine, but I'm fine enough to open my door.

[chorus]
Let me cry in the Uber, I'll be fine by my door,
Half an hour, that's all, I won't ask for more.
Let the streetlights run like water down the glass,
Let a kind man with the heating on let it pass.
I didn't text you, I didn't ring, I didn't say a thing,
I cried in the Uber all the way through town,
And I'm fine by my door, I'm fine, I'm fine now.

[post-chorus]
Five stars for the man who let me be a mess,
Five stars for the rain on the glass,
Five stars for the key and the hall light on,
And a girl who got herself home at last.

[outro]
Kettle on, coat on the floor, phone face down,
Tomorrow I'll be someone who cried in a car and lived.
Tonight I'm a woman in a hallway with her shoes still on,
And the hall light's on, and the worst of it has gone.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2037 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
