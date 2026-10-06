# Ghost in My DMs

**Status: written and verified, NOT rendered. Not yet in the queue — say when.**

Seventh song. Female lead **Mahima**, emotional pop / bedroom pop with
cinematic touches, late-night, Western Gen-Z voice. Same singer as songs 1–6.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 92 BPM, F♯ minor lifting toward A, instrumentation and the low notification-chime ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — built from the submission's scene direction, plus a three-look character bible, a faceless ex, a screen-only new girl, workflow, phone-POV challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 07-ghost-in-my-dms
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\07-ghost-in-my-dms\caption.txt `
  --lyrics-file songs\07-ghost-in-my-dms\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\07-ghost-in-my-dms\output\ghost_in_my_dms.wav
```

Expected ~2 h.

## Resolved: the stanza shared with song 6

**Fixed 2026-09-04. The bridge is now this song's own.**

As submitted, the second half of this bridge was word-for-word identical to
song 6's bridge — six lines in all, once `scripts/audit_catalogue.py` was
pointed at the whole catalogue and compared every song against every other.
It arrived that way because the submission's bridge direction, a flashback
to her crying on the bathroom floor, is also song 6's intro. Two songs in
one catalogue sharing a verbatim stanza is the kind of thing listeners
notice, and the catalogue-wide rule is that no song repeats another's lines.

Song 6 is already rendered and song 7 is not, so song 7 changed. The new
lines keep the meter, the rhyme positions and the same turn — the near-relapse,
the memory that stops it, the promise — but carry it in this song's own
imagery: the story frame still lit on the phone, the handset turned face down
on the tiles. The last line now lands on choosing herself in this song's
words rather than song 6's, which also sets up the outro's *"keep choosing
me over the pain."*

The change touched `lyrics.txt`, this README's lyrics block, and shot list
entries 52–57 plus the edit-marker list. Nothing else in the lyrics moved.

## What changed from the submission

| Change | Why |
|---|---|
| `2 a.m.` → *"Two a.m."* | The model sings digits unpredictably |
| The 4-line "ad-lib/variation over last 4 lines" after the final chorus is its own `[post-chorus]` section | The model can't layer an ad-lib over a chorus; as a post-chorus it is sung after it, which is what the video direction (do-not-disturb, lights off) wants anyway |
| Quotation marks and em-dashes removed; `[verse 1]`/`[verse 2]` and the descriptive tag lines reduced to plain tags | The model sings the lyric body literally and only knows plain section tags |

Kept exactly as written: every other line, 92 BPM, F♯ minor with the lift,
the instrumentation, the mood arc. No trimming was needed — 602 words fits.

## The story and the hook

She's fine, mostly. Then his story pops up at two a.m. and she's not. His
hoodie in a drawer. His name lighting up her phone at a café. His song in a
shop. His new girl with her pose. His mum viewing her story. The nights she
almost typed *I miss you* and almost drove to his street. Then the bathroom
floor, the promise, the block button, do not disturb, and a morning where
the phone stays in the bag.

**The hook:** *"You're a ghost in my DMs"* — visual, meme-able, caption-ready.

**The line for captions:** *"I know I should block, delete, set me free."*

**The knife line:** *"Then your mum likes my post and I lose my mind."*

**The turn:** *"You can haunt my past, but not my future / I'm blocking the
ghost, I'm closing the door for sure."*

**Why it can travel:** it's how breakups actually feel now — DMs, story
views, likes — in native slang, and it ends with the phone face-down.

## Lyrics as they will be sung

```
[intro]
Two a.m., phone glow on my face,
Your story popped up, same old place.
You're laughing with them like nothing changed,
While I'm here stuck, feeling deranged.

[verse]
We said we'd be different, not like the rest,
No games, no lies, just put us to the test.
You called me babe, said I was your safe place,
Now I'm just a name you erase from your trace.
I still got your hoodie, smells like your smoke,
I wear it when I'm sad, like a joke.
My girls say, burn it, he's toxic, babe,
But it's the closest I get to the way you stayed.

[pre-chorus]
I swear I'm doing better, most of the time,
Then your name lights up and I lose my mind.
I tell myself, don't look, don't care,
But I'm already stalking your air.

[chorus]
You're a ghost in my DMs, haunting my nights,
Every like, every view, feels like a fight.
I try to move on, but you're everywhere,
In my playlist, my streets, in the clothes that I wear.
You're the what if I can't let go,
The high I miss, even though it broke me slow.
I know I should block, delete, set me free,
But you're a ghost in my DMs, and you're still haunting me.

[verse]
Remember that night on the roof, just us two,
Said you'd never leave, said I was your truth.
Now you're out there living your best life,
While I'm here Googling how to cut ties.
I see your new fit, she's got my vibe,
Same pose, same smile, same late-night drive.
I hate that I care, but I zoom right in,
Then close the app, pretend I didn't.

[pre-chorus]
I swear I'm doing better, most of the time,
Then your mum likes my post and I lose my mind.
Even your family won't let me go,
Like they're keeping tabs on the girl you chose to know.

[chorus]
(repeat)

[instrumental]

[bridge]
There were nights I almost texted I miss you,
Almost drove to your street, almost broke through.
Almost let your story rewrite what I knew,
Almost lost the girl I built without you.
But then I thought of her on the bathroom tiles,
Phone face down, counting breaths through the tears.
And I swore to her I would not go back there,
I swore that this time I choose me.

[chorus]
(repeat)

[post-chorus]
But tonight I'm turning off the screen,
Putting my phone on do not disturb, letting me be me.
You can haunt my past, but not my future,
I'm blocking the ghost, I'm closing the door for sure.

[outro]
One day I'll wake and you won't be the first thought,
One day your name won't make my chest lock.
Till then I'll keep choosing me over the pain,
Even if you're a ghost, I won't let you stay.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 602 → ~5.2 min at 116 wpm, 86% of frame cap |
| Caption + lyrics tokens | 1995 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
