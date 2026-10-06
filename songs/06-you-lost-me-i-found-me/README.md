# You Lost Me, I Found Me

**Status: rendered 2026-09-03.** → [`output/you_lost_me_i_found_me.wav`](output/you_lost_me_i_found_me.wav)

## Render facts

| | |
|---|---|
| Seed | 42 |
| Length | 292.18 s (4:52) — 607 words at ~125 wpm |
| Format | 44.1 kHz stereo, peak 0.950, **0 clipped samples** — first render with peak-normalisation (the raw output peaked at 0.996 and was scaled to 0.95), 0.18% silence |
| Ending | fade (last 0.5 s at 0.013) |
| Envelope | 0.04 intro → 0.15 first chorus → 0.10 bridge → 0.15 final chorus → 0.07 outro; the cold-to-warm arc |
| Spectral balance vs song 1 | sub-bass lower (10.8 vs 17.8), mids a touch fuller — consistent with a bright A-major anthem rather than dark R&B; voice register the same |
| Render time | 7226 s generation, 7256 s total (2 h 01 m), peak VRAM 6.1 GB. A first attempt was aborted at 10 min to remove the character name from the lyrics |
| Sidecar | `output/you_lost_me_i_found_me.json` |

Not yet listen-checked: whether the key lift into the final chorus is
audible, and whether *"girl, you've been worth it all along"* lands in the
mirror moment.

Sixth song. Female lead **Mahima**, inspirational pop / empowerment anthem
with cinematic build. Same voice as songs 1–5.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics (one chorus repeat removed to fit — see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` blocks byte-identical to song 1 — the voice lock. 96 BPM, A major lifting toward B, instrumentation and the instrumental-break ad-lib per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 79 entries — plus the three-look character bible, colour arc, workflow, before/after challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render

Launched via the queue runner; to re-run identically from the repo root:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\06-you-lost-me-i-found-me\caption.txt `
  --lyrics-file songs\06-you-lost-me-i-found-me\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\06-you-lost-me-i-found-me\output\you_lost_me_i_found_me.wav
```

Expected ~2 h. This is the first render with peak-normalisation in
`generate.py` (scales to 0.95 only if the model's output exceeds it), added
after the clipped-sample count trended upward across the last batch.

## What changed from the submission, and why

| Change | Why |
|---|---|
| Final chorus: dropped the first 8 lines (the third identical repeat of the main chorus), kept the two new stanzas *"I'm not the girl who begs for love…"* and *"…never going back"* | The full text is ~690 words, right at the 6-minute hard cap. Removing the third verbatim repeat is the only cut that loses no new words; the hook still lands four times in the final chorus and twice more in the outro |
| Quotation marks and em-dashes removed; the descriptive tag lines (`[intro – soft…]`, `[chorus – big…]`, `[final chorus – …]`, `[bridge – raw…]`, `[outro – …]`) reduced to plain tags; the instrumental's parenthetical moved into the caption | The model sings the lyric body literally and only knows plain section tags. The ad-lib *"I found me… I found me…"* is described in the caption as a wordless vocal on the hook |

Kept exactly as written: 96 BPM, A major with the lift, the instrumentation,
the mood arc, the layered harmonies (song 1's `Harmony` line already
provides them), and every other line.

## The story and the hook

She broke on a bathroom floor. She packed a bag at night, left the keys on
the table, and walked out quiet. Weeks of crying in the car, then saying no,
locking her own door, buying herself flowers. Nights she almost hit send —
and remembered the girl on the floor, and put the phone down. Then daylight,
a city street, head up.

**The hook:** *"You lost me, but I found me."* Six words, sung eight times.

**The mirror line:** *"And said, girl, you've been worth it all along."* (The
character's name is not sung in this song — it belongs to the video only.)

**The knife line:** *"Telling me I was too much, not enough, not right."*

**The turn:** *"But then I remembered the girl in the bathroom / The one who
cried till she couldn't breathe / And I promised her I wouldn't go back."*

**Why it can travel:** not bitter, not revenge — calm. And the before/after
format is built in: shot 1 is the floor, shot 79 is her looking into the
camera.

## Lyrics as they will be sung

```
[intro]
I still remember the night I fell apart,
Sitting on the bathroom floor in the dark.
Your voice on repeat in my head like a knife,
Telling me I was too much, not enough, not right.
I cried till my chest felt empty and cold,
Wondering if I'd ever feel whole.
But somewhere between the tears and the silence,
A new version of me started to rise.

[verse]
You said I was dramatic for needing more,
For wanting love that didn't keep score.
You called it too much when I asked to be seen,
Then acted surprised when I stopped playing small in your scene.
I packed my bags in the middle of the night,
Left your keys on the table, turned off the light.
I didn't slam doors, I didn't scream loud,
Just walked out quiet, head held proud.

[pre-chorus]
That was the night I stopped begging for love,
Stopped shrinking myself to fit in your world.
I looked in the mirror, eyes red from the rain,
And whispered, we're not doing this again.

[chorus]
You lost me, but I found me,
In the pieces you left on the floor.
You walked out, but I stayed true,
And built something stronger than before.
You thought I'd break, I'd fall apart,
But you gave me back my own heart.
Now I'm standing here, finally free,
You lost me, but I found me.

[verse]
The first few weeks, I cried in the car,
Replayed every fight, every scar.
Wondered if maybe I was the problem,
If love was supposed to feel this wrong.
But then I started saying no more,
Started locking my own front door.
Started sleeping through the night,
Started believing I deserved light.
I bought myself flowers, took myself out,
Learned what peace feels like without doubt.
I stopped checking your stories, stopped waiting by the phone,
Started building a life that felt like my own.

[pre-chorus]
That was the moment I stopped looking back,
Stopped tracing your name in the dust on my glass.
I looked in the mirror, this time with a smile,
And said, girl, you've been worth it all along.

[chorus]
(repeat)

[instrumental]

[bridge]
There were nights I almost called you,
Almost typed I miss you and hit send.
Almost believed your version of me,
Almost forgot who I was again.
But then I remembered the girl in the bathroom,
The one who cried till she couldn't breathe.
And I promised her I wouldn't go back,
I promised her I'd choose me.
So I turned off the light, put the phone down,
Lay in the dark and just breathed.
And for the first time, the silence felt safe,
Like my own heart was enough to keep me.

[chorus]
I'm not the girl who begs for love,
Not the one who hides who she is.
I'm the one who walked through fire,
And came out whole in the end of it.
You lost me, but I found me,
And I'm never giving that back.
You lost me, but I found me,
And I'm never going back.

[outro]
Sometimes I pass that old street,
Where I cried and couldn't breathe.
Now I walk with my head up high,
No longer asking why.
You lost me, but I found me,
In the quiet after the storm.
You lost me, but I found me,
And this time, I'm finally home.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 607 → ~5.2 min at 116 wpm, 87% of frame cap |
| Caption + lyrics tokens | 1923 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
