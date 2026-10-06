# Someone Else's Forever

**Status: re-render queued** (after song 6) with the character name removed
from the bridge. The first take is archived at
`output/v1-with-name/someone_elses_forever.wav`; the facts below describe it
and will be replaced when the new take lands.

## Render facts (v1, archived)

| | |
|---|---|
| Seed | 42 |
| Length | 290.23 s (4:50) — the model stopped early; 614 words sang at ~127 wpm, faster than the 116 wpm estimate |
| Format | 44.1 kHz stereo, peak 0.984, **0 clipped samples**, 0.14% silence |
| Ending | clean fade (last 0.5 s at 0.003), not a cut-off |
| Envelope | quiet intro (0.04–0.06) → chorus body 0.14–0.17 → bridge dip (0.08) → outro |
| Spectral balance vs song 1 | near-identical band ratios — same mix character and voice register |
| Render time | 7050 s generation, 7098 s total (1 h 58 m), peak VRAM 6.1 GB |
| Sidecar | `output/someone_elses_forever.json` |

Not yet listen-checked: whether "Mahima" is sung clearly once in the bridge, and whether the voice reads as the same singer as song 1 by ear.

Second song. Female lead **Mahima**, modern cinematic pop ballad. Same voice as
[Fire in the Rain](../01-fire-in-the-rain/README.md).

Source of record: [`source/improved-version-perplexity.pdf`](source/improved-version-perplexity.pdf).
Its lyrics, character bible, 35 shots, workflow, teaser and QC checklist are
what the files below carry.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics from the PDF, trimmed to fit the 6-minute cap (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` blocks byte-identical to song 1 — the voice lock. Emotional arc, instrumentation and instrumental-break direction follow the PDF. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | The PDF's 35 lyric-anchored shots, character bible, ComfyUI workflow, vertical teaser and QC checklist, adapted for Wan 2.2 |
| `source/` | The PDF |
| `output/` · `logs/` | Render lands here |

## Render

From the repo root:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\02-someone-elses-forever\caption.txt `
  --lyrics-file songs\02-someone-elses-forever\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\02-someone-elses-forever\output\someone_elses_forever.wav
```

Verify first:

```powershell
.\.venv\Scripts\python.exe scripts\verify_lyrics.py songs\02-someone-elses-forever --voice-ref songs\01-fire-in-the-rain
```

Estimated render: **~2 h 10 min** on the RTX 4090 Laptop.

## Song direction (from the PDF)

- **Genre:** cinematic pop ballad with modern R&B
- **Tempo / key:** 96 BPM, F♯ minor; final chorus lifts toward A major
- **Lead vocal:** young female, intimate and breathy in verses, emotional and powerful in the chorus
- **Instrumentation:** piano, warm bass, atmospheric synths, muted electric guitar, cinematic strings, finger snaps, soft handclaps, restrained 808s, final anthemic drum lift
- **Instrumental break:** piano motif, rain ambience, muted guitar, finger snaps, rising strings, a short wordless female vocal melody
- **Mood arc:** composed heartbreak → nostalgia → wedding-day pain → emotional confrontation → dignity and self-worth
- **The story:** she attends the wedding, relives the relationship, is offered one final escape, refuses to destroy another person's life, and leaves with her identity intact
- **The hook:** *"You're someone else's forever now / And I'm still learning to breathe somehow"* — flips to *"finally learning"* in the last chorus
- **The knife line:** *"I taught your hands how to hold her tight / I taught your eyes how to love her right"*
- **The bridge line:** *"Said, wait, don't go, I can't do this anymore"* — the character's name is never sung; it lives in the video only (re-rendered 2026-09-03 to remove it; the earlier take is in `output/v1-with-name/`)

## What was trimmed to fit, and why

The PDF lyrics are **741 sung words ≈ 6.4 minutes** at this model's measured
116 words/min. The hard cap is **9000 frames = 6.0 minutes**; at 741 words the
render would truncate mid-outro and lose *"And I'm finally mine now."*

Cut to **614 words ≈ 5.3 min (88% of cap)**. Every cut is a repeat or a
restatement — no plot beat, hook, or shot-anchoring line was removed:

| Cut | Words | Why safe |
|---|---|---|
| Intro, second stanza (*"Your eyes found mine… forever can still belong to you"*) | 37 | Pre-empts the reveal; the eye-contact and "she took your hand" beats are fully sung in verse 2 and the chorus. Shot 4 re-anchored to the intro's last line. |
| Chorus 2, second stanza (*"So dance with your forever…"* repeat) | 30 | Identical to chorus 1; the hook + knife lines are kept |
| Post-chorus 2 (after chorus 2) | 22 | Identical to post-chorus 1 |
| Bridge couplet (*"Be the man I loved… let it be good to you"*) | 18 | Sentiment carried by *"I sent you gently through that garden door"* |
| Final chorus, last four short lines (*"Someone else's forever / No longer my goodbye / You were the love I lost / I am the life I find"*) | 16 | The post-chorus that follows delivers the same turn: *"I loved you first, but I choose me now"* |

To restore any of these, paste the lines back and re-run `verify_lyrics.py`;
it fails above 93% of cap.

Two non-lyrical cleanups: quotation marks and em-dashes were removed (the
model does not sing punctuation), and the PDF's `[final chorus]` tag became
`[chorus]` — the checkpoint's documented tag set is intro / verse /
pre-chorus / chorus / post-chorus / bridge / instrumental / solo / outro. The
instrumental's parenthetical direction moved into the caption, since anything
in the lyric body is sung.

## Two conflicts with the PDF, resolved in favour of your standing instructions

1. **Ethnicity.** The PDF's character bible describes Mahima and Aarav as
   South Asian and the genre as "Hindi/English-inspired… Bollywood-pop
   percussion." You had said this character is Western and the song must not
   reference Indian culture. The bible keeps every *identity marker* from the
   PDF (dark wavy hair, dark eyes, silver earrings, deep blue dress; Aarav's
   scar, watch, charcoal suit) and drops only the ethnic descriptors and the
   Bollywood genre line. If you'd rather follow the PDF literally here, it is
   a two-line change in the bible and one in the caption's genre line.
2. **Voice lock.** The PDF's "Song direction" implies a new vocal description.
   The `Vocal Details` block is kept byte-identical to song 1 instead, because
   that block *is* the voice — verified by `verify_lyrics.py --voice-ref`.

## Lyrics as they will be sung

```
[intro]
I wore the colour you once said was mine,
Sat in the third row, three seats from the aisle.
The band played the song we used to hum,
I smiled like a stranger, like we were never one.

[verse]
We were seventeen, with the whole sky to steal,
Carved our names where the old bridge met the field.
You said, one day, they'll understand us too,
I said, I'll wait, and I believed I would for you.

Then the years grew heavy, your father fell ill,
There was a house and a family waiting still.
You came to me crying, I already knew,
I held your face and said, go, I'll be fine without you.

[pre-chorus]
That was the bravest lie I ever told,
Watching you leave with my heart in your hold.
Some love is too bright to survive in the light,
Some love is a candle you carry at night.

[chorus]
You're someone else's forever now,
And I'm still learning to breathe somehow.
I taught your hands how to hold her tight,
I taught your eyes how to love her right.

So dance with your forever, I'll clap along,
I'll be the girl who loved you in a song.
You're someone else's forever now,
And I'm still learning to breathe somehow.

[post-chorus]
Someone else's forever,
Someone else's forever.
I loved you first, but I let you go.
Some hearts stay, some hearts let go.

[verse]
Your mother hugged me, said, you're still our girl,
While I hid a lifetime beneath a little smile.
The bride looked kind beneath her veil of white,
She didn't know she was standing in my goodbye.

You kept looking past her to the third-row seat,
Where I held my heart together underneath.
I wanted to run, but I stayed in place,
Learning how to lose you with a smile upon my face.

[pre-chorus]
Don't look at me, you'll give us away,
Say your vows and mean every word you say.
I'm only a guest, I'm only a friend,
I'm only the girl on the wrong side of the end.

[chorus]
You're someone else's forever now,
And I'm still learning to breathe somehow.
I taught your hands how to hold her tight,
I taught your eyes how to love her right.

[instrumental]

[bridge]
You found me in the rain by the garden door,
Said, wait, don't go, I can't do this anymore.
You said, one word, and I'll leave tonight.
One word, and I'll choose our unfinished life.

I could have said run. I could have said stay.
I could have pulled your future from her hands away.
But I saw your mother smiling through her tears,
And the boy I loved had finally made it here.

So I touched your face like I did before,
Then I sent you gently through that garden door.

And if you ever ask what love looks like,
It's a girl at your wedding letting you go twice.

[chorus]
You're someone else's forever now,
But I'm finally learning to breathe somehow.
I taught your hands how to hold her tight,
Now I'm teaching my heart to survive the night.

So dance with your forever, I'll walk alone,
I'll take every broken piece of me home.
You're someone else's forever now,
But I'm finally learning to breathe somehow.

I gave you my heart, then I gave you away,
And I found my own heart waiting for me today.

[post-chorus]
Someone else's forever,
Someone else's forever.
I loved you first, but I choose me now.
I loved you once, but I'm breathing now.

[outro]
I wore the colour you once said was mine,
I'll wash it clean in the morning light.
Someone else's forever,
Someone else's vow.

You were someone else's forever,
And I'm finally mine now.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 614 → ~5.3 min, 88% of frame cap |
| Caption + lyrics tokens | 1939 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
