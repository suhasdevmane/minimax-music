# Beach Bonfire Hearts

**Status: written and verified, NOT rendered. Not yet in the queue.**

Forty-seventh song. Female lead **Mahima**, acoustic summer pop / campfire
folk-pop with group harmonies, Australian register, a friends-to-lovers
night on the beach. 102 BPM, D major lifting a key for the final chorus.
Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 102 BPM, D major with the lift, campfire guitar, cajón, group harmonies, slide guitar, waves and fire crackle per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — built from the submission's scene direction, plus a three-look character bible, Kai as the friend, a supporting circle, workflow, bonfire-singalong challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 47-beach-bonfire-hearts
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\47-beach-bonfire-hearts\caption.txt `
  --lyrics-file songs\47-beach-bonfire-hearts\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\47-beach-bonfire-hearts\output\beach_bonfire_hearts.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"nothing"*, *"took you long enough"* and *"finally"* removed | Punctuation is not sung; the lines read as reported speech with commas |
| `[verse 1]`/`[verse 2]`, `[final chorus]` and the descriptive tag lines reduced to plain tags | The model only knows plain section tags |
| *10:30* and *10 summers* spelled out as *half past ten* and *ten summers* | The model sings digits unpredictably |
| The performance notes (one guitar, lifted key, claps and cajón) moved into the caption | The model sings the lyric body literally |

Kept exactly as written: every other line, 102 BPM, D major with the lift,
the instrumentation, the mood arc. No trimming was needed — 616 words fits.

## The story and the hooks

A beach bonfire on the Australian coast. His brother leaves the guitar by
the logs, he tunes it, she sings along and realises she's singing it to
him: the mate she's had since they were ten, beach cricket and peeling
shoulders. One look over the flames. Later the kids are gone, his sister
has the ute headlights on, and he slides across the log to sit beside her;
she fumbles a chord, he laughs the same laugh from a hundred summers, and
she can't say it. So she walks down to the water where the firelight ends,
says all of it, and he says *took you long enough*. They walk back hand in
hand, the brother yells *finally*, the whole beach sings, and at dawn the
two of them are still by the coals playing the same two chords.

**The hook:** *"Beach bonfire hearts, burning slow"* — a caption, a
singalong, a summer.

**The line for captions:** *"Ten summers of almost."*

**The turn:** *"So I say it, I say all of it, I say it low / And you say,
took you long enough, and you kiss me slow."*

**Why it can travel:** it is a group singalong by design, the friends-to-
lovers arc is the most rewatched romance shape there is, and the Australian
detail (esky, servo ice, the ute tray, the southerly) gives it a place
without shutting anyone out.

## Lyrics as they will be sung

```
[intro]
Sun went down behind the dunes an hour ago,
Esky full of servo ice and wood to throw.
Sand's still warm, the southerly's on its way,
You're on the far side of the fire, same as every day.

[verse]
Your brother brought the guitar and he left it by the logs,
You picked it up and tuned it while the others walked the dogs.
Two chords and a shrug, a song we half knew,
And I'm singing at the fire but I'm singing it to you.
Reckon we've been mates since the summer we were ten,
Beach cricket, peeling shoulders, I never looked back then.
But tonight the sparks go up and something in me turns,
Like the wood knows something first, and it's telling me it burns.

[pre-chorus]
Everybody's laughing, passing round the last cold drink,
You look up over the flames and I forget to think.
One look, that's all it takes, I'm caught in it now,
I've been standing in the smoke and I'm working out how.

[chorus]
Beach bonfire hearts, burning slow,
Sparks going up where the stars all go.
I've been keeping my hands in my pockets for years,
Tonight I'm thinking I'll let it show.
Beach bonfire hearts, burning slow,
Salt in your hair and the tide out low.
Pass me the guitar, I'll play it till you know,
Beach bonfire hearts, burning slow.

[verse]
Half past ten and the tide's turned, the little kids are gone,
Your sister's on the ute tray with the headlights on.
You slide across the log and your shoulder's touching mine,
Say, play the one you used to play, and I run out of time.
So I play it and I miss a chord and you laugh out loud,
Same laugh from a hundred summers, but it's different now.
You lean in close and say, you've gone quiet, what's wrong,
And I say, nothing, hey, just listen to the song.

[pre-chorus]
Everybody's singing, nobody's singing in key,
You've stopped singing altogether, you're just looking at me.
One look, that's all it takes, I'm caught in it now,
I've been standing in the smoke and I'm working out how.

[chorus]
Beach bonfire hearts, burning slow,
Sparks going up where the stars all go.
I've been keeping my hands in my pockets for years,
Tonight I'm thinking I'll let it show.
Beach bonfire hearts, burning slow,
Salt in your hair and the tide out low.
Pass me the guitar, I'll play it till you know,
Beach bonfire hearts, burning slow.

[instrumental]

[bridge]
Come down to the water where the firelight ends,
Where I can't hide behind the chords or the friends.
Ten summers of almost, I'm done playing it cool,
If this wrecks us I'm the fool, but I'd rather be the fool.
So I say it, I say all of it, I say it low,
And you say, took you long enough, and you kiss me slow.

[chorus]
Beach bonfire hearts, burning slow,
Sparks going up where the stars all go.
I kept my hands in my pockets for years,
Tonight your hand's in mine and the whole beach knows.
Beach bonfire hearts, burning slow,
Salt in your hair and the tide out low.
Your brother's yelling, finally, from across the glow,
Beach bonfire hearts, burning slow.

[post-chorus]
Burning slow, burning slow,
Ten summers, one spark, and now we know.
Burning slow, burning slow,
Sing it round the fire till the embers go.

[outro]
Sun's coming up behind the dunes, the fire's just coals,
Everyone's asleep in the tray with sand in their clothes.
You've got the guitar and you're playing our song,
Two chords and a shrug, and I sing along,
Sand in the strings and the whole sky gold,
Beach bonfire hearts, burning slow.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 616 → ~5.3 min at 116 wpm, 89% of frame cap |
| Caption + lyrics tokens | 2146 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
