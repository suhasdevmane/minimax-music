# Fire in the Rain

**Status: rendered.** First song. Female lead, modern cinematic pop / dark R&B.

## Files

| File | Purpose |
|---|---|
| [`caption.txt`](caption.txt) | Music description fed to the model. Its `Vocal Details` block defines the voice reused by every later song. |
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics as sung in the full render (500 words, trimmed from the original) |
| [`lyrics_sample.txt`](lyrics_sample.txt) | Intro + chorus used for the 60 s voice test |
| [`source/original-submission.md`](source/original-submission.md) | The complete lyrics and style direction as originally written, before trimming |
| `output/fire_in_the_rain_full.wav` | **The song.** 4:18, 44.1 kHz stereo, no clipping |
| `output/fire_in_the_rain_full.mp3` | Compressed copy |
| `output/fire_in_the_rain_full.json` | Reproducibility sidecar: seed, caption, lyrics, versions |
| `output/sample_fire_in_the_rain.wav` + `.json` | The 58 s test render that approved the voice |
| `logs/` | Raw render logs |

## Render facts

| | |
|---|---|
| Seed | 42 |
| Requested / actual length | 350 s cap → 257.97 s (model emitted end-of-audio) |
| Render time | 6041 s (1 h 41 m) on RTX 4090 Laptop 16 GB |
| Peak VRAM | 7.3 GB with `leaf_level` LM streaming |
| Measured pacing | 500 sung words → 258 s = **116 words/min** |

To re-render identically (same seed, caption and lyrics reproduce exactly):

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\01-fire-in-the-rain\caption.txt `
  --lyrics-file songs\01-fire-in-the-rain\lyrics.txt `
  --duration 350 --seed 42 `
  --out songs\01-fire-in-the-rain\output\fire_in_the_rain_full.wav
```

## The story

Secretive attraction → passionate romance → betrayal and confusion →
emotional revelation → self-respect and liberation. A phone lights up at a
quarter past two with a stranger's name; a jacket by the door holds a train
ticket back to where they met; under the station clock the truth comes out —
the name was his sister's last call, and he was never running from her, he
was running from himself. She chooses herself anyway.

**The hook:** *"Now I miss you, but I choose me / No more chains where my
wings should be."*

## What was trimmed and why

The original submission (see `source/`) ran ~1,567 words — about 17 minutes at
the pacing this model sings, against a 6-minute hard cap. It was cut to 500
words keeping the full narrative spine. Removed: the third verse's
"I knew all along" counter-twist and the letter-burning, two chorus repeats,
and the longer bridge.

The submission also had stage directions inside the lyric body — e.g.
`*(16–24 bars: pulsing bass, atmospheric synths...)*`. The model sings the
lyric body literally, so these were moved into the caption's `Arrangement`
section where they function as direction.

With the measured 116 wpm there is room for ~190 more words; the cut third
verse would fit if a longer version is ever wanted.

## Lyrics as rendered

```
[intro]
I saw your name in the rain on my window,
Like a secret the night wouldn't let go.
You walked in wearing the scent of goodbye,
With a little bit of heaven and a dangerous lie.

[verse]
We met where the city turns gold after dark,
Under neon stars in an old train park.
You had silver rings and a runaway smile,
I had a suitcase full of reasons to stay awhile.
You laughed at my scars, I danced with your doubt,
We kissed like the world was running out.
But your phone lit up at a quarter past two,
A name I didn't know, with a heart next to you.

[pre-chorus]
You were my high, you were my warning,
My midnight truth and my Sunday morning.
Every don't go sounded like goodbye,
Every kiss had a question hiding in its eyes.

[chorus]
We were fire in the rain,
Sweetest love and sharpest pain.
You said forever, then you vanished overnight,
Left your shadow dancing in my headlights.
Now I hate you, but I miss you,
I forgive you, then I curse you.
You're the song I can't delete from my phone,
The kind of love that breaks you beautifully alone.

[verse]
I found your jacket hanging by my door,
Still carrying the perfume I was addicted to before.
In the pocket, one train ticket folded in two,
Destination: the town where I first met you.
There you were beneath the station clock,
Like the final scene in a film that forgot to stop.
That name on my phone was my sister's last call,
You weren't running from me. You were running from you.

[pre-chorus]
You were my wound, you were my healing,
I wanted revenge, I wanted truth,
But the hardest enemy was the love we never knew.

[chorus]
We were fire in the rain,
Sweetest love and sharpest pain.
You said forever, then you vanished overnight,
Left your shadow dancing in my headlights.
Now I hate you, but I miss you,
I forgive you, then I curse you.
You're the song I can't delete from my phone,
The kind of love that breaks you beautifully alone.

[instrumental]

[bridge]
Maybe love is not the person who stays,
Maybe love is the courage to walk away.
Maybe hate is grief wearing a crown,
Maybe healing is putting that crown down.
So here's to the heart that was shattered but grew,
I lost you, found me, and that was the truth.

[chorus]
Fire in the rain,
Love that left a scar-shaped stain.
You were the storm, I became the sky,
You were the question, I became the why.
Now I miss you, but I choose me,
No more chains where my wings should be.
If you're poison, I turned it into light,
If you're gone, I'm still dancing tonight.
We were young under city lights,
You and me, a beautiful ending in disguise.

[outro]
I saw your name in the rain on my window,
But it doesn't hurt like it did long ago.
Fire in the rain,
I choose me tonight.
```
