# Ride or Die

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty-five. Female lead **Mahima**, anthemic pop with punchy live drums,
a brass section, a chant chorus and a fully rapped second verse. 120 BPM,
E flat major, uptempo. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 734 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1. 120 BPM, E flat major, live drums, brass section, gang vocals, and the note that verse two is rapped over drums, sub-bass and muted guitar with brass stabs. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — uptempo |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 85 entries — with a three-age bible for both leads, the faceless-ex rule, four separated light worlds, the two-second flash-forward, the arrivals-sign challenge and a QC checklist |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 55-ride-or-die
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\55-ride-or-die\caption.txt `
  --lyrics-file songs\55-ride-or-die\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\55-ride-or-die\output\ride_or_die.wav
```

Expected ~2 h.

## Pacing note

This is an uptempo song and pacing is a guess until it renders. The lyrics
are 734 words, of which the rap verse is about a hundred and twenty and the
two chants another forty. Against the model's six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.3 min | **overrun — outro lost** |
| 125 wpm | 5.9 min | 98% |
| **140 wpm (the guard setting)** | 5.2 min | 87% |
| 155 wpm | 4.7 min | 79% |

A rap verse at 120 BPM typically runs 170–200 wpm and the chants are faster
still, so the guard is deliberately conservative. **If the first render
truncates the outro, drop the second post-chorus (twenty-two words, a
repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung |
| Digits spelled as words (*three in the morning*, *ten years*, *four hundred unread*, *forty years*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – phone tone, slow kick, no groove]*, *[verse 2 – the rap]*) reduced to plain tags | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| The rap instruction and the gang-vocal and crowd-chant direction moved into the caption | The model sings the lyric body literally |
| Repeated choruses, pre-choruses and the post-chorus written out in full | The model would sing a repeat marker |

Kept exactly as written: every lyric line, 120 BPM, E flat major, the brass
and live-drum arrangement, the vow bridge, the voice-note ending, the viral
moments.

## The story and the hooks

Two people met in somebody else's kitchen at a party neither of them wanted
to be at, and eleven addresses later one of them still knows the other's
order. The verse keeps the receipts: four hours in a car with one headlight
out, a plastic hospital chair, a mattress carried up a narrow staircase, and
not one I told you so. The rap verse is the fast version — a group chat with
a name that cannot be said out loud, two identical spare keys, an arrivals
hall at a quarter to five and the worst possible photograph taped to a piece
of cardboard, a hand gathering hair back at a kerb and a secret buried the
next morning. Then the band stops and the vow gets said in an empty road.
The last shot is a three-minute voice note playing to an empty kitchen.

**The hook:** *"You're my ride or die, and I'd ride for you."*

**The line for captions:** *"Nobody's coming, so we came for each other."*

**The chant:** *"Hands up if you've got one, hands up high."*

**The rap clip:** *"You know the exact wrong thing to say to make me okay."*

**The turn:** *"Nobody hands you a certificate for this / No aisle, no ring,
no photograph, no priest."*

**Why it can travel:** it is a wedding song for a friendship, at a tempo
built for a room shouting it. The receipts in verse one are specific enough
that everybody swaps in their own, and the arrivals-hall sign is a challenge
that already exists — this just gives it a soundtrack.

## Lyrics as they will be sung

```
[intro]
Three in the morning and the ringtone is yours,
I'm out of the bed and I'm into my shoes.
No question, no why, no what did you do,
Just send me a pin and I'm coming to you.
Ride or die.

[verse]
We met in a kitchen at a party neither of us knew,
I said, I hate it here, you said, thank God, me too.
Ten years and eleven addresses down the line,
You still know my order and I still know your sign.
You drove four hours in a car that barely ran,
Slept in a plastic hospital chair and held my hand.
You never said, I told you so, about the guy,
You just brought up the mattress and you never asked me why.
There's a photo on your fridge of us at nineteen,
Two idiots in a garden with the whole thing still to see.

[pre-chorus]
Ambulance friend, airport friend,
The one who reads the message that I didn't send.
If the world ends on a Wednesday afternoon,
I'm not calling anybody, I'm just calling you.

[chorus]
You're my ride or die, and I'd ride for you,
Say the word and I'm outside, no questions, no excuse.
Ride or die, ride or die,
I'll be the phone call that you never have to try.
Nobody's coming, so we came for each other,
Nobody chose us, so we chose one another.
Whatever the year does, whatever it puts us through,
You're my ride or die, and I'd ride for you.

[post-chorus]
Hey, ride or die, ride or die,
Hands up if you've got one, hands up high.
Ride or die, ride or die,
That's my people, that's my ride.

[verse]
Group chat got a name that we can never say out loud,
Four hundred unread and a blurry photo of a crowd.
You got a spare key, I got the same,
You know the exact wrong thing to say to make me okay.
Arrivals hall at a quarter to five,
Cardboard sign with my worst photo on the side.
I flew in a wreck and I walked out a joke,
You had gum and a coffee and you didn't make me talk.
Held my hair and my secret on the very same night,
Then buried it deeper than the reason for the flight.
You are the reason that I know I'm not too much,
You call me on my nonsense and it still feels like love.

[pre-chorus]
Bail money friend, bad haircut friend,
The one who says the true thing and then stays till the end.
If the world ends on a Wednesday afternoon,
I'm not calling anybody, I'm just calling you.

[chorus]
You're my ride or die, and I'd ride for you,
Say the word and I'm outside, no questions, no excuse.
Ride or die, ride or die,
I'll be the phone call that you never have to try.
Nobody's coming, so we came for each other,
Nobody chose us, so we chose one another.
Whatever the year does, whatever it puts us through,
You're my ride or die, and I'd ride for you.

[instrumental]

[bridge]
Nobody hands you a certificate for this,
No aisle, no ring, no photograph, no priest.
But if there were vows then I'd say them in the road,
I'd say them in the group chat, I'd say them in the cold.
For better, for worse, for whatever we go through,
You were never plan B, it was always me and you.

[chorus]
You're my ride or die, and I'd ride for you,
Say the word and I'm outside, no questions, no excuse.
Ride or die, ride or die,
I'll be the phone call that you never have to try.
Nobody's coming, so we came for each other,
Nobody chose us, so we chose one another.
Forty years from now with a garden and a chair,
Same two idiots and the same bad hair.
Whatever the year does, whatever it puts us through,
You're my ride or die, and I'd ride for you.

[post-chorus]
Hey, ride or die, ride or die,
Hands up if you've got one, hands up high.
Ride or die, ride or die,
That's my people, that's my ride.

[outro]
Voice note at midnight, three minutes long,
Half of it laughing and the rest of it wrong.
Nothing important, and I play it twice,
That's the whole thing, that is the whole of my life.
You're my ride or die, and I'd ride for you.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 734 at 140 wpm → ~5.2 min, 87% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2327 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
