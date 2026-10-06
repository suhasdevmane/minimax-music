# Don't Tell the Neighbours

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirtieth song. Female lead **Mahima**, reggaeton-pop with a soft dembow and
plucked synths, **UK register** — south London flat, UK spelling and idiom.
100 BPM, A minor, ballad/mid pacing. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 624 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 100 BPM, A minor, dembow mixed as if heard through a wall, a drumless nylon-guitar bridge, and the knuckle-knock percussion and alarm-through-a-wall ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 69 entries — with a two-look bible for Mahima, Kai's single look, Number Twenty-Four as the third character, the under-exposure rule, the migrating-sofa running gag and the "shh" challenge |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 100 BPM this is a ballad/mid song and the verify script's
116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 30-dont-tell-the-neighbours
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\30-dont-tell-the-neighbours\caption.txt `
  --lyrics-file songs\30-dont-tell-the-neighbours\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\30-dont-tell-the-neighbours\output\dont_tell_the_neighbours.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"right"*, *"some of us have work"*, *"sorry about the noise, mate"* and *"no bother, love"* removed | Punctuation is not sung, and quote marks in the body confuse the phrasing |
| Em-dashes replaced with commas | The model reads them unpredictably |
| Digits spelled out: *half eleven*, *half twelve*, *three knocks*, *Number Twenty-Four*, *four in the morning* | The model sings digits unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines (*"plucked synth, room tone, no drums"*, *"the hook inverted"*) reduced to plain tags | Only the checkpoint's documented tags exist; anything else on a tag line is dropped or sung |
| Every repeated chorus and pre-chorus written out in full | The verify script flags parentheses-only lines, and the model would sing *"repeat"* |
| The last couplet of verse one cut, plus small trims across the choruses, pre-choruses and post-chorus | The submission ran to 658 sung words, well over the budget. The cut couplet introduced a downstairs neighbour who then never returned; the song is better with one neighbour. |

Kept exactly as written: every other line, 100 BPM, A minor, the
instrumentation, the mixed-through-a-wall production note, the hook inverting
in the final chorus, and the UK register throughout.

## The story and the hooks

Half eleven on a Tuesday, chain across the door, curtains pulled, one lamp on,
and a sofa shoved back with a bare foot to make about two square metres of
dance floor. She spends the first verse on her toes in thick socks trying to
be quiet and losing. At half twelve the party wall goes bang three times, a
note comes under the door in beautiful joined-up handwriting saying that some
of us have work, and they laugh and do it again. The next morning she
apologises to Number Twenty-Four on the stairs and does not mean a word of it,
and he says no bother, love, presses the lift call and smiles at the floor
like he remembers being twenty-three. Then the bridge stops the joke: she has
spent her whole life keeping the volume down, small in corridors, holding half
her laugh in her throat so nobody would complain. The last chorus turns the
dial the other way and opens the curtains.

**The hook:** *"Turn it down, don't tell the neighbours what we do."*

**The line for captions:** *"Nothing that happens in this flat leaves this
flat."*

**The turn:** *"I've spent my whole life keeping the volume down / small in
the corridor and small in a crowd."*

**The inversion:** *"Turn it up, let the neighbours hear it too."*

**Why it can travel:** it is a party song that fits in one room, so it costs
nothing to recreate; the "shh" post-chorus is a two-count step anybody can
copy from one clip; and it earns its ending by turning a comic neighbour into
the reason the song means something.

## Lyrics as they will be sung

```
[intro]
Half eleven and the block has gone quiet,
One lamp on and the curtains pulled tight.
Nothing that happens in this flat leaves this flat,
So put your phone face down and come here for that.

[verse]
Chain across the door and my shoes in the hall,
Curtains doing shapes on the back of the wall.
You pushed the sofa with your foot and you said, right,
And the floorboards in this flat haven't settled since eight.
Up on my toes trying to keep the noise low,
And you're doing that thing with your shoulders, and I go.

[pre-chorus]
Keep it low, keep it slow, keep it under the beat,
Whisper it, don't shout it, put your hand on the heat.
If the ceiling starts shaking then we've gone too far,
And I don't want to stop, and you know what you are.

[chorus]
Turn it down, don't tell the neighbours what we do,
Thin walls, low lamp, half eleven, me and you.
One more song and I promise we're through,
Turn it down, don't tell the neighbours what we do.
Palm across my mouth and my back against the door,
Bass through the boards and I'm not stopping anymore.
Number Twenty-Four is banging on the wall again,
Turn it down, don't tell the neighbours where we've been.

[verse]
Half twelve, three knocks, and the wall goes bang bang bang,
And we froze like two kids caught halfway through a plan.
A note under the door in proper joined-up pen,
Saying, some of us have work, and we laughed and did it again.
Saw him on the stairs this morning with his bin bag and cap,
Said, sorry about the noise, mate, and I did not mean that.
He said, no bother, love, and he pressed the lift call,
Then he smiled at the floor like he remembered it all.

[pre-chorus]
Keep it low, keep it slow, keep it under the beat,
Whisper it, don't shout it, put your hand on the heat.
If the ceiling starts shaking then we've gone too far,
And I don't want to stop, and you know what you are.

[chorus]
Turn it down, don't tell the neighbours what we do,
Thin walls, low lamp, half eleven, me and you.
One more song and I promise we're through,
Turn it down, don't tell the neighbours what we do.
Palm across my mouth and my back against the door,
Bass through the boards and I'm not stopping anymore.
Number Twenty-Four is banging on the wall again,
Turn it down, don't tell the neighbours where we've been.

[instrumental]

[bridge]
I've spent my whole life keeping the volume down,
Small in the corridor and small in a crowd.
Made myself easy so nobody complained,
Kept half of my laugh in the back of my throat and stayed.
Then you came round on a Tuesday with a bag and a plan,
And I haven't been quiet since, and I don't think I can.

[chorus]
Turn it down, don't tell the neighbours what we do,
Thin walls, low lamp, half eleven, me and you.
One more song, and I'm not promising we're through,
Turn it up, let the neighbours hear it too.
Palm across my mouth and my back against the door,
Bass through the boards and I'm not stopping anymore.
Number Twenty-Four can put the kettle on again,
Turn it up, let the neighbours know where we've been.

[post-chorus]
Shh, shh, don't tell the neighbours,
Shh, shh, thin walls, low lamp.
Shh, shh, don't tell the neighbours,
One more song and then we'll stop, I promise.

[outro]
Four in the morning and the buzzer's gone still,
Two glasses in the sink and the lamp on the sill.
Somebody's alarm going off through the wall,
And we're still up, and I'm not sorry at all.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 624 at 116 wpm → ~5.4 min, 90% of frame cap |
| Caption + lyrics tokens | 2144 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
