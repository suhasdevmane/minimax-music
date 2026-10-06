# Loud Lipstick

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song ninety-two. Female lead **Mahima**, modern British pop-rock with a
chanted chorus, 130 BPM, A major, **UK register** — UK spelling, UK idiom
and Manchester night-out detail. Uptempo, so it carries a `render.json`.
Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 752 sung words, inside the uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 130 BPM, A major, two overdriven guitars, gang vocals, the lipstick-lid click and night-bus ambience. |
| [`render.json`](render.json) | Uptempo pacing for the length guard (`wpm: 140`) |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 91 entries — with a three-look character bible, the stranger in the toilets, the faceless ex, the red-arrives-and-never-leaves colour rule, workflow, the hands-up challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 92-loud-lipstick
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\92-loud-lipstick\caption.txt `
  --lyrics-file songs\92-loud-lipstick\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\92-loud-lipstick\output\loud_lipstick.wav
```

Expected ~2 h.

## Pacing warning

Uptempo, and pacing is estimated rather than measured. The lyrics are **752
words** and the two post-choruses are pure chant, which sings faster than
anything else in the catalogue. Against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 130 wpm | 5.8 min | 96% |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 160 wpm | 4.7 min | 78% |

At 130 BPM with shouted chant sections a blended 145–160 wpm is realistic,
which lands nearer five minutes. **If the first render truncates the outro,
drop the second post-chorus (thirty-four words, a repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech (`"Right then, off we pop."`, `"Your colour is mad."`, `"Alright, mate,"`, `"bring it down,"`, `"too much, too loud"`) | Punctuation is not sung and quotation marks confuse the phrasing |
| Em-dashes replaced with commas throughout | Not sung; they break the phrasing model |
| Descriptive tag lines (`[intro – bathroom reverb, clean arpeggio]`, `[chorus – terrace-sized]`, `[bridge – one clean guitar]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| The `(repeat)` markers for the second chorus, the final chorus and the second post-chorus written out in full | The model would sing the word *repeat* |
| Performance notes (*stomp and clap*, *biggest*, *crowd*) moved into the caption | The lyric body is sung literally |
| Two lines cut from the first verse and two from the second | The submission ran 793 words, over the 781-word uptempo cap |

Kept exactly as written: the hook, the chant, the UK register and every
piece of Manchester detail, 130 BPM, A major, the two-guitar arrangement
and the mood arc.

## The story and the hooks

Half six on a wet evening, a steamed bathroom mirror and a red lipstick she
has not used in two years. Two years of beige: apologising to a chair,
holding doors for people who never look back, keeping her voice at library
volume. Then a text about pre-drinks, the lid coming off with a click, and
the night. The queue in the drizzle, the beige coat handed to the cloakroom
and never mentioned again, the bass through the floor. At half eleven in the
club toilets a stranger says her colour is mad and she gives the lipstick
away for good. Somebody's ex is by the fire door and gets a nod and nothing
else. Then the bridge, on a half-empty stage with the house lights up: it
was never the colour. She was loud at nine in a school hall until an adult
hand came down, and a report card said too much, too loud, and she has been
apologising to a paper crowd ever since. The last chorus is the volume
coming back, and it is not for anyone watching.

**The hook:** *"Loud lipstick, louder me."*

**The chant:** *"Hands up if you've ever been told to calm down / Hands up,
hands up, we are not calming down."*

**The line for captions:** *"It was never the colour, it was never the
shade, it was two years of quiet finally paid."*

**The knife line:** *"They wrote it on a report card, too much, too loud,
and I have been apologising to a paper crowd."*

**The soft moment:** *"I said, take it, go on, do your top lip, she came out
braver, and she kept it, and that's it."*

**Why it can travel:** it is a real night out in real UK detail rather than
a generic club record, the chant is a two-line question millions of people
can answer with one clip, and the emotional payload — being told as a child
to bring it down — lands on an audience far wider than the night-out crowd.

## Lyrics as they will be sung

```
[intro]
Half six, bathroom light, rain down the pane,
Wiped the steam off the mirror with the side of my hand.
One stripe of red and she's back again,
The girl I put in a drawer, and she's turned up with a plan.
Right then.

[verse]
Two years in beige and I called it peace,
Kept my voice at the volume of a library seat.
Said sorry to a chair, said sorry to the rain,
Held the door for people who'd not hold it again.
Then Steph texted, pre-drinks, half seven, her place,
And I found the red at the bottom of a case.
Rolled it in my fingers like a little bit of proof
That I used to be the girl who took up the room.
The lid came off with a click like a lock,
And the one in the mirror said, right then, off we pop.

[pre-chorus]
Cab on the corner, heels on the kerb,
Queue in the drizzle and I don't say a word.
Cloakroom ticket, coat off, hair down,
Bass through the floor coming up through the ground.
Right then. Let's go.

[chorus]
Loud lipstick, louder me,
Kicked the door off the quiet and I set it free.
Two years small, now the whole road knows,
Red on the rim of the glass wherever it goes.
You can hear me in the queue, you can hear me in the cab,
I'm not sorry for the space and I'm not giving it back.
Sing it with your chest till the ceiling agrees,
Loud lipstick, louder me.

[post-chorus]
Louder, louder, louder me,
Louder, louder, let the whole street see.
Red on the rim, red on the rim,
Louder, louder, let the night begin.
Hands up if you've ever been told to calm down,
Hands up, hands up, we are not calming down.

[verse]
Half eleven, toilets, mirror full of us,
One I'd never met said, your colour is mad.
I said, take it, go on, do your top lip,
She came out braver, and she kept it, and that's it.
Somebody's ex was stood by the fire door,
I said alright, mate, and I meant nothing more.
Two years back that would have been my whole night,
Now it's just a face in a bit of red light.
Then the DJ dropped the one we all know,
And the floor came up like it wanted a go.

[pre-chorus]
Sweat on the ceiling, hands in the air,
Somebody starts it and the whole room's there.
Feet on the speaker stack, hair coming down,
Bass through the floor coming up through the ground.
Right then. Let's go.

[chorus]
Loud lipstick, louder me,
Kicked the door off the quiet and I set it free.
Two years small, now the whole road knows,
Red on the rim of the glass wherever it goes.
You can hear me in the queue, you can hear me in the cab,
I'm not sorry for the space and I'm not giving it back.
Sing it with your chest till the ceiling agrees,
Loud lipstick, louder me.

[instrumental]

[bridge]
It was never the colour, it was never the shade,
It was two years of quiet finally paid.
You can take my lipstick, take the whole case,
I would still walk in like I own the place.
I was loud at nine years old in a school hall,
Somebody said bring it down, so I did, that's all.
They wrote it on a report card, too much, too loud,
And I have been apologising to a paper crowd.
Well, the volume is back and it isn't for you,
It's for the girl in the toilets and the nine-year-old too.

[chorus]
Loud lipstick, louder me,
Kicked the door off the quiet and I set it free.
Two years small, now the whole road knows,
Red on the rim of the glass wherever it goes.
You can hear me on the night bus, hear me in the rain,
I'm not sorry for the space, I'm not going back again.
Sing it with your chest till the ceiling agrees,
Loud lipstick, louder me.

[post-chorus]
Louder, louder, louder me,
Louder, louder, let the whole street see.
Red on the rim, red on the rim,
Louder, louder, let the night begin.
Hands up if you've ever been told to calm down,
Hands up, hands up, we are not calming down.

[outro]
Ten past three, night bus, window steamed,
Red on the cup and the chips on my knee.
Lipstick's gone, some girl has got it now,
Louder me, and I'm keeping that somehow.
Loud lipstick, louder me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 752 at 140 wpm → ~5.4 min, 90% of frame cap |
| Caption + lyrics tokens | 2369 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
