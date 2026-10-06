# Video Call Slow Dance

**Status: written and verified, NOT rendered. Not yet in the queue.**

Eighty-third song. **Female + male duet** — Mahima and a male R&B tenor,
trading verses and singing every chorus in close harmony — modern R&B /
slow-jam pop, 94 BPM, A♭ major. Same singer as songs 1–8 for the female
lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction exactly as
submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock. A male R&B tenor added as Singer B with a section-by-section `Duet Structure`. 94 BPM, A♭ major, no key change; electric piano spine, snaps, deep bass, and the call-connecting chime, laptop fan and buffering-glitch textures. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 77 entries — from the submission's scene direction, with a two-lead character bible, the split-screen rule, the two-room colour rule, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 83-video-call-slow-dance
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\83-video-call-slow-dance\caption.txt `
  --lyrics-file songs\83-video-call-slow-dance\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\83-video-call-slow-dance\output\video_call_slow_dance.wav
```

Expected ~2 h.

## One thing to know before rendering

**It's a duet, and the model has no per-line singer control.** Same
situation as songs 4, 8 and 9: the split lives in the caption's
`Duet Structure` line, and the model follows it loosely. This one asks for
more than most — an alternating pre-chorus, a male-only second verse and
close two-part harmony on every chorus. Expect the choruses to arrive as two
voices; expect the male-only second verse to be the part that needs
checking by ear.

## What changed from the submission

| Change | Why |
|---|---|
| `9 your time` → *"Nine your time"* (twice), `press play on 3` → *"press play on three"*, `1, 2, here we go` → *"one, two, here we go"* (twice), `2,000 miles` → *"Two thousand miles"*, `22 more squares` / `22 squares` → *"Twenty-two more squares"* / *"Twenty-two squares"* (three times), `3%` → *"three percent"* | The model sings digits unpredictably, and a comma inside a number or a percent sign is worse still |
| Descriptive tag lines — `[intro – electric piano, pad, room tone, a call connecting]`, `[verse 1 – her]`, `[pre-chorus – both, alternating lines]`, `[chorus – both, wide and warm]`, `[verse 2 – him]`, `[bridge – electric piano, her alone, then both]`, `[final chorus – fullest harmonies, strings, the countdown line]`, `[outro – electric piano, two voices trading goodnights]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; which voice takes which section is carried by the caption's `Duet Structure`, not by a tag |
| The `(repeat)` under the second chorus written out in full | The verify script flags it and the model would sing the word |

Kept exactly as written: every lyric line, 94 BPM, A♭ major, the
instrumentation, the mood arc, the six viral moments. No trimming was
needed — 623 words fits.

## The story and the hooks

Nine in the evening where he is, midnight where she is. Same song queued on
both machines, press play on three, pick the laptop up and hold it flat
against your chest, and slow dance in two separate bedrooms at the same
time. She does her hair for it. She puts lipstick on for a camera and says
so, out loud, because that is how far gone she is. She moves the lamp. He
stacks hardbacks under his laptop so their eyes line up, and marks the
calendar with a red pen — twenty-two more squares. It is ridiculous and they
both know it. Then the picture freezes with his hand on his heart, the
little wheel spins, and she could hang up. She keeps swaying instead. When
he comes back he is laughing, because he never stopped either, out of time
and out of key. That is the whole song: it is not the signal and it is not
the screen, it is that he keeps dancing when he cannot see her.

**The hook:** *"Video call slow dance, hold your screen like it's me"* — the
title in the first line of every chorus and again halfway through.

**The line for captions:** *"Two bedrooms, one song, closest we can be."*

**The turn:** *"So it's not the signal, and it's not the screen, / It's that
you keep dancing when you can't see me."*

**The countdown:** the red pen and the crossed squares. It shows up in his
verse, replaces the buffering line in the final chorus, and closes the outro
— a ready-made format for anyone counting down to a flight.

**Why it can travel:** long distance is enormous and almost nothing is
written about the *effort* of it — the lamp moved for better light, the
stack of books, the hair done for a webcam. The dance is a two-person format
anyone can film with two phones and one song, and the split screen closing
at the end is a single visual idea people will copy immediately.

## Lyrics as they will be sung

```
[intro]
Nine your time and midnight mine,
Same song queued up, we press play on three.
Pick the laptop up and hold it to your chest,
Tonight the distance don't get to me.
Two lamps, two rooms, one slow groove,
Baby, don't blink, and don't you move.

[verse]
I put my hair up like it's a real date,
Lipstick for a camera, that's how far gone I am.
Moved the lamp so the light hits right,
Cleared the laundry off the bed like you'd notice, damn.
You're in that grey shirt with the collar bent,
Ceiling fan turning slow behind your head.
Two thousand miles of signal and delay,
And you freeze on the frame where you're smiling my way.

[pre-chorus]
So put the laptop on your palm, lift it slow,
Count me in, one, two, here we go.
Sway to the left when I sway to the right,
Mirror me, baby, we can get it right tonight.

[chorus]
Video call slow dance, hold your screen like it's me,
Two bedrooms, one song, closest we can be.
Turn down the lights, I'll turn up the sound,
Spin me on the carpet, I'll spin you around.
Video call slow dance, cheek against the glass,
Buffering forever, I don't need it fast.
If a signal is all we get tonight,
Hold your screen like it's me, and hold it tight.

[verse]
I put the laptop on a stack of books
So your eyes line up with mine and stay.
Marked the calendar with a red pen, look,
Twenty-two more squares and I'm on my way.
You do that thing where you say you're fine,
Then you look off frame and your voice goes thin.
So I press my hand up flat to the screen,
Put yours on mine, baby, let me in.

[pre-chorus]
So put the laptop on your palm, lift it slow,
Count me in, one, two, here we go.
Sway to the left when I sway to the right,
Mirror me, baby, we're dancing tonight.

[chorus]
Video call slow dance, hold your screen like it's me,
Two bedrooms, one song, closest we can be.
Turn down the lights, I'll turn up the sound,
Spin me on the carpet, I'll spin you around.
Video call slow dance, cheek against the glass,
Buffering forever, I don't need it fast.
If a signal is all we get tonight,
Hold your screen like it's me, and hold it tight.

[instrumental]

[bridge]
Then the picture froze with your hand on your heart,
That little wheel spinning, my screen went dark.
I could've hung up, could've called it a night,
But I kept on swaying in the lamplight.
And when you came back you were laughing at me,
Cause you never stopped either, out of time, out of key.
So it's not the signal, and it's not the screen,
It's that you keep dancing when you can't see me.

[chorus]
Video call slow dance, hold your screen like it's me,
Two bedrooms, one song, closest we can be.
Turn down the lights, I'll turn up the sound,
Spin me on the carpet, I'll spin you around.
Video call slow dance, cheek against the glass,
Twenty-two more squares and this screen is the past.
If a signal is all we get tonight,
Hold your screen like it's me, and hold it tight.

[post-chorus]
Hold it like it's me, hold it like it's me,
Till the airport, till the gate, till it's really me.
Hold it like it's me, hold it like it's me,
Same song, same sway, till it's really me.

[outro]
Nine your time and midnight mine,
Battery blinking, three percent.
Say goodnight slow, then say it again,
I'll still be dancing when the call has ended.
Twenty-two squares, then no more screen,
Till then, baby, hold it like it's me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 623 → ~5.4 min at 116 wpm, 90% of frame cap |
| Caption + lyrics tokens | 2388 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
