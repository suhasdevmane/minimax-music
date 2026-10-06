# Hey Stranger

**Status: re-render queued** (after song 6) with the character name removed
from the bridge. The first take is archived at
`output/v1-with-name/hey_stranger.wav`; the facts below describe it and will
be replaced when the new take lands.

## Render facts (v1, archived)

| | |
|---|---|
| Seed | 42 |
| Length | 239.63 s (3:59) — the model stopped early; 613 words sang at ~153 wpm. The short, chanted "Hey stranger" lines pace much faster than verse-heavy lyrics, so this song has room for ~150 more words if a longer cut is ever wanted |
| Format | 44.1 kHz stereo, peak 1.000, **6 clipped samples** out of 10.5 million (inaudible; noted for honesty), 0.11% silence |
| Ending | clean fade (last 0.5 s at 0.003) |
| Envelope | 0.10 intro → 0.15–0.17 choruses → 0.18 peak at the final chorus → 0.12 outro; no dead sections |
| Spectral balance vs song 1 | near-identical band ratios — same mix character and voice register |
| Render time | 5595 s generation, 5632 s total (1 h 34 m), peak VRAM 7.2 GB |
| Sidecar | `output/hey_stranger.json` |

Not yet listen-checked: whether "Mahima" is sung clearly once in the bridge, and whether the hook flip ("hasn't learned" → "finally learned") is audible.

Third song. Female lead **Mahima**, modern cinematic pop / dark R&B. Same
voice and sound settings as [Fire in the Rain](../01-fire-in-the-rain/README.md)
and [Someone Else's Forever](../02-someone-elses-forever/README.md).

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` blocks byte-identical to song 1 — the voice lock. Same 96 BPM / F♯ minor and instrument palette as songs 1–2. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | 40 lyric-anchored shots, character bible, ComfyUI workflow, vertical teaser, QC checklist |
| `output/` · `logs/` | Render lands here |

## Render

From the repo root:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\03-hey-stranger\caption.txt `
  --lyrics-file songs\03-hey-stranger\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\03-hey-stranger\output\hey_stranger.wav
```

Verify first:

```powershell
.\.venv\Scripts\python.exe scripts\verify_lyrics.py songs\03-hey-stranger --voice-ref songs\01-fire-in-the-rain
```

Estimated render: **~2 h 15 min** on the RTX 4090 Laptop.

## Why this theme

Songs 1 and 2 both end with Mahima walking away from a man. This one flips
the position: **she was the one who got left**, without a goodbye, at
nineteen — and ten years later she runs into him in aisle seven of a
supermarket on a rainy Tuesday.

"Ran into my ex after ten years" is one of the most-shared personal-story
formats on YouTube and TikTok, because everyone has a version of it. The song
is built to be that story: the rehearsed coldness that collapses the second
she sees him, the realisation in the checkout line that the ache is for
*that time*, not for him, the number on a coffee cup she sets down, and the
walk out into the rain lighter than she walked in.

It is a love song with real pain in it, but the register is different from
the first two — tender rather than defiant, nostalgic rather than
sacrificial. Nobody is a villain. He's just a boy who got scared. That's what
makes it safe to share.

**The hook:** *"Hey stranger"* — two words, sung eight times per chorus and
chanted in the post-chorus. It is the title, the first line of every chorus
line, and the thing people will type in the comments.

**The turn:** chorus 1 ends *"my heart still hasn't learned how to let go"*;
the final chorus ends *"my heart finally learned how to let you go."* Same
melody, one word different, the whole song in that swap.

**The knife line:** *"No goodbye, no reason, just a dial tone / And a girl
who learned to sleep alone."*

**The apology:** *"Then you said, I'm sorry, I'm sorry I never called."* The
character's name is never sung; it lives in the video only (re-rendered
2026-09-03 to remove it; the earlier take is in `output/v1-with-name/`).

**The visual signature:** a mustard-yellow raincoat — the only warm colour in
every cold fluorescent frame. Instantly recognisable in a thumbnail.

## Arc by section

| Section | Feeling | What happens |
|---|---|---|
| Intro | Ordinary night, broken open | Aisle seven; a voice she'd know anywhere |
| Verse 1 | Warm memory → the silence | Nineteen, the old car, the lake; the calls stop; no goodbye |
| Pre-chorus | Rehearsed armour collapses | "I'd be cold, I'd be brief, I'd be right" |
| Chorus | Longing, bittersweet | "Hey stranger, you still say my name the same" |
| Post-chorus | Chant | "Ten years and one hello" |
| Verse 2 | Quiet conversation, the realisation | "Are you happy?" — yes, and it's true; "the ache is not for you, it's for that time" |
| Pre-chorus 2 | Armour to peace | "There's no one to fight" |
| Chorus | Same words, calmer | — |
| Instrumental | Memory montage | Guitar melody, wordless vocal |
| Bridge | Half-time, the coffee cup | He apologises; she sets the cup down |
| Final chorus | Release | "I'm not the girl that you left in the rain" |
| Post-chorus | Flip | "Ten years and one goodbye" |
| Outro | Mirror of the intro | "I didn't feel nineteen anymore" |

## Lyrics

```
[intro]
Tuesday rain, fluorescent light,
Aisle seven on an ordinary night.
Then a voice I'd know in any crowd or storm
Said my name, and ten years came undone.

[verse]
We were nineteen in a car that barely ran,
Windows down, your heartbeat in my hand.
You kissed me by the water, said, wait for me,
The city's just a year, then it's you and me.
The calls got shorter, then the calls got rare,
Then one December there was no one there.
No goodbye, no reason, just a dial tone,
And a girl who learned to sleep alone.

[pre-chorus]
I rehearsed this moment a thousand nights,
I'd be cold, I'd be brief, I'd be right.
But you looked at me like no time had passed,
And every line I practised didn't last.

[chorus]
Hey stranger, you still say my name the same,
Like the years were only weather, like nothing changed.
Hey stranger, I've got somewhere I should be,
But I'm standing in the rain like it's still you and me.
Hey stranger, tell me, did you ever look back?
I built a whole life on the pieces of that.
Hey stranger, it's been ten years and one hello,
And my heart still hasn't learned how to let go.

[post-chorus]
Hey stranger, hey stranger,
Ten years and one hello.
Hey stranger, hey stranger,
Some names you never let go.

[verse]
You asked if I was happy, and I said yes,
And for once it wasn't a lie I had to dress.
You said the city swallowed you, you lost your way,
You dialed my number and had nothing left to say.
Your hands still move the way they did at nineteen,
Your eyes still ask the questions in between.
And I realised, standing in the checkout line,
The ache is not for you, it's for that time.

[pre-chorus]
I rehearsed a war, but there's no one to fight,
You're just a boy who got scared of the night.
And I'm just a girl who survived the fall,
Who isn't waiting by the phone at all.

[chorus]
(repeat)

[instrumental]

[bridge]
You wrote your number on a coffee cup,
Said, call me sometime, if you ever look up.
Then you said, I'm sorry, I'm sorry I never called,
I just didn't know how to come home at all.
And I held that cup like I was nineteen again,
Then I set it down, and I let the moment end.
Maybe I'll call you, maybe I won't,
But I'm not the girl who waits by the phone.

[chorus]
Hey stranger, you still say my name the same,
But I'm not the girl that you left in the rain.
Hey stranger, I've got somewhere I should be,
And this time I'm walking, and it's setting me free.
Hey stranger, yeah, I looked back once or twice,
Then I built a whole life, and the life turned out nice.
Hey stranger, it's been ten years and one hello,
And my heart finally learned how to let you go.

[post-chorus]
Hey stranger, hey stranger,
Ten years and one goodbye.
Hey stranger, hey stranger,
Some names you keep, and that's alright.

[outro]
Tuesday rain, fluorescent light,
Aisle seven on an ordinary night.
I paid for my things, I walked out the door,
And I didn't feel nineteen anymore.
```

## Voice: what's locked, what changed

Byte-identical to song 1: `Sonics & Production Profile`, `Vocal Details`,
96 BPM, F♯ minor, and the palette (piano spine, bass/808s, pads, muted
guitar, strings, finger snaps, handclaps, post-chorus chant, anthemic final
drum lift).

Changed for this song: `Global Emotional Progression`, imagery (supermarket,
yellow raincoat, old car, lake, coffee cup), and textures — the intro carries
a fluorescent hum and a checkout-scanner beep instead of crowd murmur.

Seed stays **42**. New lyrics mean a similar voice, not an identical one.

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 613 → ~5.3 min, 88% of frame cap |
| Caption + lyrics tokens | 1955 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
