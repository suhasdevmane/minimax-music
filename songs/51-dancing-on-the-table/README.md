# Dancing on the Table

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty-one. **Female + male duet** — Mahima on the lead, Kai on verse two
and the harmony — modern Latin pop with a live horn section, cowbell
percussion and gang-vocal choruses. 128 BPM, D minor, uptempo. Same singer as
songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 742 sung words |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1; Kai added as Singer B with a section-by-section duet structure. 128 BPM, D minor, live brass, cowbell, gang vocals, backyard ambience. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 84 entries — with a two-lead character bible, the family crowd, the light-and-crowd-only-increase rule, OpenPose guidance for every table shot, the challenge cut and a QC checklist |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 51-dancing-on-the-table
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\51-dancing-on-the-table\caption.txt `
  --lyrics-file songs\51-dancing-on-the-table\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\51-dancing-on-the-table\output\dancing_on_the_table.wav
```

Expected ~2 h.

## Pacing note

This is an uptempo song and pacing is a guess until it renders. The lyrics
are 742 words. Against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.4 min | **overrun — outro lost** |
| 125 wpm | 5.9 min | 99% |
| **140 wpm (the guard setting)** | 5.3 min | 88% |
| 155 wpm | 4.8 min | 80% |

Latin pop at 128 BPM with a chanted post-chorus and gang vocals will sit
above 140 in practice, so the guard is deliberately conservative. **If the
first render truncates the outro, drop the second post-chorus (twenty-three
words, a repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung |
| Digits spelled as words | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – cowbell, guitar, backyard ambience]*, *[verse 2 – his side, stripped groove]*) reduced to plain tags | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses, pre-choruses and the post-chorus written out in full | The model would sing a repeat marker |
| Performance direction (who sings which section, the gang vocals, the timbale break) moved into the caption | The model sings the lyric body literally |

Kept exactly as written: every lyric line, 128 BPM, D minor, the brass and
cowbell arrangement, the sunrise ending, the viral moments.

## The story and the hooks

Two people are put at the singles end of a long table at somebody else's
wedding. The caterers leave, the band packs its trumpets at a quarter after
one, a teenage cousin plugs a phone into a speaker, and the cleared table
sits there in the string lights with the whole yard looking at it. She goes
up first. He had his keys in his pocket and a lie about a morning meeting,
and he goes up anyway. By the last chorus a grandmother is up there being
steadied by two cousins. Then the drums fall away, the street is audible,
there is a new scratch in the varnish, and two strangers sit on a back porch
at sunrise under one borrowed suit jacket.

**The hook:** *"We're dancing on the table, let the whole street hear."*

**The line for captions:** *"Two strangers and a hundred years of family
here."*

**The chant:** *"Up, up, higher than the lights / Up, up, this is how we say
goodnight."*

**The turn:** *"There's a scratch in the varnish that the two of us just
made / And every wedding needs two strangers who forgot to be afraid."*

**Why it can travel:** it is a party record with a family in it. The hook is
an instruction, the chant is four words long, and the table climb is a
challenge anyone with a loud relative can film.

## Lyrics as they will be sung

```
[intro]
Caterers gone, and the cake is a crime scene,
String lights still swinging where the big tent had been.
Somebody's cousin took over the sound,
And nobody left in this yard is sitting down.
Forks in the sink and the chairs pushed aside,
And you at the far end, catching my eye.

[verse]
They sat us with the singles where the music didn't go,
Two strangers and a candle that was burning very slow.
You said your mother's cousin married my best friend,
I said we will be family by the time this weekend ends.
I took the last empanada, you took half of mine,
You poured me something red and swore that it was fine.
The band packed up their trumpets at a quarter after one,
And that is the exact minute this party had begun.
The long wood was all empty and the string lights hung low,
And the whole yard was waiting for somebody to go.

[pre-chorus]
One shoe on and one shoe gone,
Cowbell hitting like a countdown song.
Grandmother clapping, the aunties know,
There is only one place left to go.

[chorus]
We're dancing on the table, let the whole street hear,
Plates in the kitchen and the brass in the air.
Hold on to my hand and don't look down,
We are the last two standing in this town.
We're dancing on the table, let the whole street hear,
Two strangers and a hundred years of family here.
Play it again, play it loud, play it till we fall,
We're dancing on the table, or we're not dancing at all.

[post-chorus]
Up, up, higher than the lights,
Up, up, this is how we say goodnight.
Up, up, one more time around,
Nobody in this family sits down.

[verse]
I had my keys in my pocket and a lie about the time,
A meeting in the morning that was never really mine.
Then the lights came up gold over everybody's heads,
And you kicked off your sandals and you climbed on up instead.
You asked me, are you coming, like it wasn't a request,
Like the wood would hold us both and the night would do the rest.
My father's on his feet now with a napkin in the air,
Your grandmother is filming with the phone up in her hair.
I forgot about the morning, I forgot the whole plan,
There is red wine on my collar and I am a happy man.

[pre-chorus]
Two shoes gone and three songs deep,
Cowbell running like a heartbeat.
The aunties clapping, the cousins know,
There is only one place left to go.

[chorus]
We're dancing on the table, let the whole street hear,
Plates in the kitchen and the brass in the air.
Hold on to my hand and don't look down,
We are the last two standing in this town.
We're dancing on the table, let the whole street hear,
Two strangers and a hundred years of family here.
Play it again, play it loud, play it till we fall,
We're dancing on the table, or we're not dancing at all.

[instrumental]

[bridge]
When the brass goes quiet you can hear the whole street,
A radio two doors down and a hundred tired feet.
You said you will remember this in twenty years or so,
I said then help me down and ask me where I go.
There's a scratch in the varnish that the two of us just made,
And every wedding needs two strangers who forgot to be afraid.

[chorus]
We're dancing on the table, let the whole street hear,
Plates in the kitchen and the brass in the air.
Hold on to my hand and don't look down,
We are the last two standing in this town.
We're dancing on the table, let the whole street hear,
Two strangers and a hundred years of family here.
Somebody's mother is up here with us now,
Somebody's father is showing us how.
Play it again, play it loud, play it till we fall,
We're dancing on the table, or we're not dancing at all.

[post-chorus]
Up, up, higher than the lights,
Up, up, this is how we say goodnight.
Up, up, one more time around,
Nobody in this family sits down.

[outro]
Sun coming up on the lights and the chairs,
Your suit jacket over me on the back porch stairs.
Table still standing and the yard is a mess,
We are going to be family, I guess.
We're dancing on the table, let the whole street hear.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 742 at 140 wpm → ~5.3 min, 88% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2530 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
