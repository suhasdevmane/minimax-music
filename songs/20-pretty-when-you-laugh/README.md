# Pretty When You Laugh

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twentieth song. Female lead **Mahima**, warm pop-soul with a live horn
section and gospel-tinged backing vocals, 90 BPM, A flat major, US register.
Ballad pacing, no `render.json`. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 638 sung words, ballad budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 90 BPM, A flat major, Rhodes and a live horn section, with a wide-open room mic and a muffled laugh through a wall as the opening and closing texture. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look character bible, Kai as the subject of the film rather than the co-star, the funeral grade rule, the composited-UI note, workflow, the voice-note challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 20-pretty-when-you-laugh
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\20-pretty-when-you-laugh\caption.txt `
  --lyrics-file songs\20-pretty-when-you-laugh\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\20-pretty-when-you-laugh\output\pretty_when_you_laugh.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Digits spelled out throughout — *two seconds*, *fourteen seconds*, *thirty years* | The model sings digits unpredictably |
| Quotation marks removed from the reported speech in verse two (*was that alright*, *that was the best of you*) and em-dashes removed everywhere | Punctuation is not sung; the model sings the lyric body literally |
| Descriptive tag lines (*intro – Rhodes alone*, *bridge – Rhodes and voice, one low string*, *final chorus – whole horn section*) reduced to plain `[intro]`, `[bridge]`, `[chorus]`; all performance direction moved into the caption | Only the checkpoint’s documented tags exist, and anything left in the body gets sung |
| The repeated chorus written out in full instead of marked as a repeat | The verify script flags parentheses-only lines and the model would sing them |
| No `render.json` | At 90 BPM this is a ballad; the verify script’s 116 wpm default is the right guard |

Kept exactly as written: every image, 90 BPM, A flat major, the horn-and-Rhodes
production list, the funeral verse, the fourteen-second voice note and the six
viral moments. Ten words were trimmed by contraction across the choruses and
verses to bring the count inside the ballad budget; no line was cut.

## The story and the hooks

She heard him through a wall at somebody's party before she ever saw his
face, and went to find out what was funny. He laughs like a door coming off
its hinge. He puts his whole hand over his mouth like he is embarrassed and
it comes out through his fingers anyway. It has scared birds off a wire and
made a stranger on a bus turn around. Then February: his uncle's funeral, too
many coats, nobody eating, and somebody tells a story about a boat and a dog
— and he goes first, and the whole room follows him, and she watches a room
of people put their shoulders down at once and understands what he is
actually for. She keeps fourteen seconds of him losing it at nothing in a
folder on her phone. The bridge is the argument: everyone else fell for a
face. The last line is what she wants done with the recording.

**The hook:** *"You're pretty when you laugh, so I'll never stop trying."*

**The line for captions:** *"A face is just a face on a cold gray morning in
November, and a laugh is a whole climate."*

**The turn:** *"I watched a room of people put their shoulders down at once,
and I understood what you are actually for."*

**The knife line:** *"If you go before me, leave the fourteen seconds on."*

**Why it can travel:** it is a wedding-speech song and a best-friend song at
once, the funeral verse gives a funny record real weight, and the video's
format — a slow-motion portrait of one person laughing — is something anyone
can shoot on a phone.

## Lyrics as they will be sung

```
[intro]
I heard you before I saw you, through a wall in someone's house,
Some joke I never got the start of, and a sound came out.
Big and dumb and honest and completely out of key,
And I thought, whoever that is, I want to know what's funny.

[verse]
You laugh like a door coming off its hinge,
Like a kettle, like a seagull, like a bad idea.
You put your whole hand over your mouth like you're embarrassed,
Then it comes out through your fingers anyway.
It scared the birds up off the wire at the bus stop,
It made a stranger on the crosstown bus turn around.
You crack before the punchline every single time,
And I have never wanted anything more in my life.

[pre-chorus]
So I say the stupid thing, I do the stupid voice,
I'd fall down a whole flight of stairs on purpose.
I have got no pride, no shame and no material,
And I'll take a bad review just to hear it once.

[chorus]
You're pretty when you laugh,
So I'll never stop trying.
Say something back to me, I'll set you up all night,
I'll be the worst comedian in town and call it dying.
Give me the wheeze, give me the eyes going gone,
Give me the two seconds of silence before it comes.
You're pretty when you laugh,
So I'll never stop trying.

[verse]
February, and your uncle's funeral, and the coats,
And your mother saying nobody's eaten anything all day.
Then somebody told a story about a boat and a dog,
And you went first, and everybody followed you.
I watched a room of people put their shoulders down at once,
And I understood what you are actually for.
That night you said, was that alright, and I said, that was the best of you,
And you laughed at that as well, quietly, in the dark.

[pre-chorus]
So I keep a voice note in a folder on my phone,
Fourteen seconds of you losing it at nothing.
On the days I can't reach you and the days I can't reach me,
I put it on, and the whole place starts to move.

[chorus]
You're pretty when you laugh,
So I'll never stop trying.
Say something back to me, I'll set you up all night,
I'll be the worst comedian in town and call it dying.
Give me the wheeze, give me the eyes going gone,
Give me the two seconds of silence before it comes.
You're pretty when you laugh,
So I'll never stop trying.

[instrumental]

[bridge]
People say it's the eyes, people say it's the smile,
People marry a jawline and wonder what went wrong.
But a face is just a face on a cold gray morning in November,
And a laugh is a whole climate, and you brought yours along.
So keep the eyes, keep the smile, keep whatever they were selling,
I fell for the sound, and I would fall for it again.

[chorus]
You're pretty when you laugh,
So I'll never stop trying.
Thirty years from now I'll still be working on the timing,
Still be dying at the table, still be trying.
Give me the wheeze, give me the eyes going gone,
Give me the two seconds of silence before it comes.
You're pretty when you laugh,
So I'll never stop trying.

[post-chorus]
I'll never stop trying, no I'll never stop trying,
Tell me it's not funny, I'll go get another one.
I'll never stop trying, no I'll never stop trying,
You're pretty when you laugh and I am never going to stop.

[outro]
I heard you before I saw you, through a wall in someone's house,
And I've heard it every day since and I still turn around.
If you go before me, leave the fourteen seconds on,
And I'll play it in an empty room and swear you're still in it.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2169 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
