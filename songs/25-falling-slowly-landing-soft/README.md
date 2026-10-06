# Falling Slowly, Landing Soft

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-fifth song. Female lead **Mahima**, piano ballad / cinematic pop with
strings and minimal drums, 80 BPM, E♭ major. The slowest song in the
catalogue so far. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 80 BPM, E♭ major with no modulation; the final chorus widens dynamically instead. Piano spine, cello doubling the bass, harp arpeggios, brushed kit. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — from the submission's scene direction, with a three-look character bible, Kai as the man who waits, a faceless ex, the coat and feather motifs, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 25-falling-slowly-landing-soft
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\25-falling-slowly-landing-soft\caption.txt `
  --lyrics-file songs\25-falling-slowly-landing-soft\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\25-falling-slowly-landing-soft\output\falling_slowly_landing_soft.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the dialogue lines (*"I don't do the falling anymore,"* *"That's fine, I'll wait while you breathe,"* *"We've got time, there's no rush,"* *"more"*) | Punctuation is not sung; a quoted phrase can be read as a break in the line |
| Descriptive tag lines — `[intro – hushed, piano and a faint string pad]`, `[chorus – wide, tender, singable]`, `[bridge – bare piano, then building]`, `[final chorus – fullest strings, layered harmonies, still soft]`, `[outro – piano and one held string]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; the variation lives in the words, not the tag |
| The `(repeat)` under the second chorus written out in full | The verify script flags it and the model would sing the word |

Kept exactly as written: every lyric line, 80 BPM, E♭ major, the
instrumentation, the mood arc, the six viral moments. The lyric body already
spelled its numbers as words, so no digit cleanup was needed. No trimming
either — 639 words fits.

## The story and the hooks

The last one dropped her from a height she cannot name, so she keeps her
coat on for the first three dates and a hand on the door in case she has to
leave. He never pushes. He brings tea and sits a little further off. He
learns the way she goes quiet when she is scared, and gets quiet too, until
the quiet stops being hard. She has a hundred exits drawn in her head, each
door with a plan and each plan with a name. Then one morning she looks down
and her feet are not touching the ground, and she realises she has been
falling the whole time — and that he caught her so slowly she never felt it
land. The bridge is where she stops bracing: not scared of the height, not
scared of the drop, because she knows the way he catches.

**The hook:** *"I was falling slowly, you made me land soft"* — the title in
the first line of every chorus.

**The line for captions:** *"I was falling slowly, you made me land soft."*

**The quote:** *"You don't try to fix me, you just stand closer, / And the
closer you stand, the further I can fall."*

**The turn:** *"If I'm falling for you, then I'm falling for good."*

**The image that carries it:** the coat. It is buttoned to the collar in the
intro, still on through the first verse, off at the door by the first
chorus, and left hanging on a bench by the second. The video never has to
explain it.

**Why it can travel:** the trust fall is a ready-made couples format, and
the song is written for the ones who flinch — a much larger audience than
the ones who fall easily.

## Lyrics as they will be sung

```
[intro]
I kept my coat on for the first three dates,
Hand on the door in case I had to leave.
I said, I don't do the falling anymore,
You said, that's fine, I'll wait while you breathe.

[verse]
The last one dropped me from a height I can't name,
I hit so hard I learned to walk on glass.
When you reached for me, I flinched before you touched,
You smiled and said, we've got time, there's no rush.
You never asked why my back's against the wall,
You brought me tea and sat a little further off.
You learned the way I go quiet when I'm scared,
You got quiet too, till the quiet wasn't hard.

[pre-chorus]
I built a hundred exits, drew them in my head,
Every door had a plan, every plan had a name.
Then I looked down one morning, feet not touching ground,
And I realised I'd been falling all along.

[chorus]
I was falling slowly, you made me land soft,
Feather on a pillow, coat I finally took off.
Braced for the crash, braced for the drop,
I was falling slowly, you made me land soft.
No sirens, no shatter, no sorry on the floor,
Just your hand in my hair, your voice saying, more.
I was falling slowly, but I never felt the ground,
You made me land soft, you caught me coming down.

[verse]
You memorised my coffee, then you memorised my fears,
Don't take it personal when I need a night alone.
Porch light on like a question I can answer
Any hour I decide to come home.
I still check the exits, only out of habit,
Like reaching for a wall in a room full of light.
You don't try to fix me, you just stand closer,
And the closer you stand, the further I can fall.

[pre-chorus]
So I stopped counting doorways, stopped rehearsing goodbye,
Let the hundred exits blur into one open sky.
I looked down this morning, feet not touching ground,
And I laughed, cause I'd been falling all along.

[chorus]
I was falling slowly, you made me land soft,
Feather on a pillow, coat I finally took off.
Braced for the crash, braced for the drop,
I was falling slowly, you made me land soft.
No sirens, no shatter, no sorry on the floor,
Just your hand in my hair, your voice saying, more.
I was falling slowly, but I never felt the ground,
You made me land soft, you caught me coming down.

[instrumental]

[bridge]
I used to think love meant bracing for the fall,
Arms crossed over my chest, waiting for the sound.
You never let me hit, you never let me break,
You kept your arms wide open till I came down.
Here's the thing I never said to anyone before,
Not scared of the height, not scared of the drop.
If I'm falling for you, then I'm falling for good,
I know the way you catch, I'll land soft.

[chorus]
I was falling slowly, you made me land soft,
Feather on a pillow, coat I finally took off.
No bracing for the crash, no bracing for the drop,
I was falling slowly, you made me land soft.
No sirens, no shatter, no sorry on the floor,
Just your hand in my hair, your voice saying, more.
I was falling slowly, now I'm lying on the ground,
You made me land soft, and I'm staying where I'm found.

[post-chorus]
Land soft, land soft, you made me land soft,
Coat off at the door, both hands off the lock.
Land soft, land soft, you made me land soft,
Never felt the ground, only felt you catch.

[outro]
If you see me falling, don't run, don't shout,
Don't bring a net, don't brace, don't work it out.
Just be exactly where you've been this whole time,
Cause I was falling slowly, and I landed soft.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2262 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
