# No Plans, No Problem

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty-four. Female lead **Mahima**, Afrobeats with Afroswing rap-sung
verses, 104 BPM, E major, mid pacing, UK register throughout. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 637 sung words, every repeated section written out in full |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 104 BPM, E major, log drums, round moving bass, whistle synth on the hook, and the rap-sung verse delivery specified in the emotional progression. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 69 entries — with a two-look character bible, the three friends, the market auntie, the chain-reaction sequence, workflow, the chain challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 104 BPM this is a mid-tempo song and the verify script's
116 wpm ballad default is the right guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 44-no-plans-no-problem
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\44-no-plans-no-problem\caption.txt `
  --lyrics-file songs\44-no-plans-no-problem\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\44-no-plans-no-problem\output\no_plans_no_problem.wav
```

Expected ~2 h.

## One thing to watch: the rap-sung verses

The catalogue's rap map assigns this song *her Afroswing rap-sung verses*.
There is no `[rap]` tag in this engine, so both verses are plain `[verse]`
sections and the flow lives entirely in the caption's emotional progression,
which specifies conversational rap-sung delivery sitting behind the beat with
melody returning only in the last two bars. The lyric itself is written for
that cadence — ten to thirteen syllables a line, internal rhymes carrying
through each bar (*half eleven, curtains drawn, no alarm, no shame*) — so it
will still scan if the model sings it straight. The verses are the part of
this render to judge by ear.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads the body literally |
| Digits spelled as words (*half eleven*, *ten percent*, *two o'clock*, *four percent*) | The model sings digits unpredictably |
| Descriptive tag lines (*[verse 1 — log drums, rap-sung flow]*) reduced to plain `[verse]` etc. | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| Repeated choruses and post-choruses written out in full instead of *(repeat)* | The model would sing the word |
| The submission's bridge trimmed from six lines to four | Word budget: the mid-tempo class caps at 640 sung words and the rap-sung verses are dense |

Kept exactly as written: the hook, both verses, 104 BPM, E major, the
instrumentation, the UK register and the mood arc.

## The story and the hooks

A Saturday with nothing in it. She wakes at half eleven with the curtains
still shut and a group chat asking what the plan is; there is no plan, and
that is the plan. They miss a train on purpose, take the bus instead and
ride the top deck up Kingsland Road. At two they are in a market full of
grill smoke, where an auntie takes a fiver, gives back change and calls her
daughter. By late afternoon there is a speaker bungee-corded to a bicycle on
the canal towpath, and a boy starts dancing, then his mum, then the barber
from the shop, and the towpath is a dance floor. The bridge is the only quiet
moment: she has had a whole year of colour-coded weeks and none of them
turned out like this one.

**The hook:** *"No plans, no problem, just vibes and my people"* — four
stresses, a chant, and a caption that writes itself.

**The line for captions:** *"Nothing in the diary, so tell me what we do."*

**The turn:** *"But today was never written down and look at what it gave /
The best ones don't get booked, they only find you on the way."*

**The heart line:** *"Takes the fiver, gives me change, and then she calls me
daughter."*

**Why it can travel:** the chain reaction on the towpath is a ready-made
challenge, the flow is current UK, and the message — that the good day is the
one you did not schedule — is the most repostable feeling there is in a
summer record.

## Lyrics as they will be sung

```
[intro]
No alarm, no reason, just a Saturday,
Sunlight on the wall and the curtains still drawn.
Somebody is typing in the group chat asking what we're doing,
And the honest answer is, we haven't got a plan at all.

[verse]
Half eleven, curtains drawn, no alarm, no shame,
Group chat asking what's the plan, there ain't one, that's the game.
Meet me by the station, bring your appetite and time,
We're not booking, we're not queueing, we're just letting the day decide.
Missed the train on purpose so we took the bus instead,
Top deck, front seat, all of Kingsland Road ahead.
Somebody's shoes are brand new, somebody's aunt is on the phone,
Somebody swears they know a spot, they don't, but we go on.

[pre-chorus]
No reservation, no itinerary, no rush,
Phone on ten percent and I am not topping up.
Wherever we end up is exactly where we should be,
Turn it up a little bit and drop that beat on me.

[chorus]
No plans, no problem, just vibes and my people,
Nowhere to be by nine and nothing to prove.
No plans, no problem, no map and no timing,
Just a speaker, a pavement and a reason to move.
Feet doing something that could pass for a dance,
Best day of the summer and it came by chance.
No plans, no problem, just vibes and my people,
Nothing in the diary, so tell me what we do.

[post-chorus]
No plans, no problem, no plans, no problem,
Just vibes and my people and a whole day free.

[verse]
Two o'clock, we hit the market and the street is full of smoke,
Jerk chicken, roti, plantain and a mango for the road.
Auntie on the corner says she'll do it for a fiver,
Takes the fiver, gives me change, and then she calls me daughter.
Down beside the water there's a speaker on a bike,
Playing something old enough that everybody likes.
Kid starts moving, then his mum, then the barber from the shop,
Now the towpath is a dance floor and there's nobody to stop us.

[pre-chorus]
It's proper warm, the ice cream queue is halfway round the block,
Phone on four percent and I am not topping up.
Wherever we end up is exactly where we should be,
Turn it up a little bit and drop that beat on me.

[chorus]
No plans, no problem, just vibes and my people,
Nowhere to be by nine and nothing to prove.
No plans, no problem, no map and no timing,
Just a speaker, a pavement and a reason to move.
Feet doing something that could pass for a dance,
Best day of the summer and it came by chance.
No plans, no problem, just vibes and my people,
Nothing in the diary, so tell me what we do.

[instrumental]

[bridge]
I had a whole year of calendars and colour-coded weeks,
Alarms to go to the gym and reminders to eat.
But today was never written down and look at what it gave,
The best ones don't get booked, they only find you on the way.

[chorus]
No plans, no problem, just vibes and my people,
Nowhere to be by nine and nothing to prove.
No plans, no problem, no map and no timing,
Just a speaker, a pavement and a reason to move.
Half of the towpath in a kind of a dance,
Best day of the summer and it came by chance.
No plans, no problem, just vibes and my people,
Nothing in the diary, so tell me what we do.

[post-chorus]
No plans, no problem, no plans, no problem,
Just vibes and my people and a whole day free.

[outro]
Half eleven tomorrow and the curtains will be drawn,
Group chat will be asking me the same.
And I'll tell them what I told them here today,
No plans, no problem, come and find me anyway.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2104 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
