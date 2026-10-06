# Closure Isn't a Text

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-eight. Female lead **Mahima**, bedroom pop with indie-folk bones
— nylon-string guitar an inch from the microphone, brushed kit, upright bass
and six-deep vocal stacks. 88 BPM, G minor. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words, ballad pacing class, trimmed to fit the budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 88 BPM, G minor, nylon guitar, brushed kit, upright bass, one cello, and the lamp-hum, struck-match, door-latch and kettle ambience per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 77 entries — built from the submission's scene direction, plus a three-look character bible, an ex who never appears in a single frame, the illegible-handwriting rule, workflow, the burn-it challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 78-closure-isnt-a-text
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\78-closure-isnt-a-text\caption.txt `
  --lyrics-file songs\78-closure-isnt-a-text\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\78-closure-isnt-a-text\output\closure_isnt_a_text.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Digits spelled as words (*three in the morning*, *six long pages*, *four walls*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – nylon guitar, room tone, lamp hum, no drums]*, *[verse 2 – guitar and voice, then the kit returns]*, *[final chorus – widest harmonies, released]*) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the checkpoint's documented tags exist; anything else is dropped or sung |
| The repeated second chorus written out in full | `(repeat)` in the body would be sung as the word |
| Several lines shortened by a word each in the choruses and verses | The submission ran 662 sung words, over the 640-word ballad budget; nothing was cut except padding |
| All performance and arrangement direction moved into `caption.txt` | Stage directions in the lyric body get sung |

Kept exactly as written: the story, the letter and the match, 88 BPM, G minor
with no modulation, the instrumentation, the mood arc, the bridge.

## The story and the hooks

She spends a winter waiting for the paragraph that would explain it. She
writes out the questions on the back of an envelope and crosses them out, she
rehearses a level voice she never gets to use, and she keeps the ringer on all
December so that every call that is not him lands a little. Then in April she
sits down with a proper pen and writes him six pages he will never see — the
bathroom light she fixed alone, the friend who said his name and watched her
face — reads it once, and burns it in the sink. The answer she needed turned
out to be the one she wrote. The bridge finds the real definition: closure is
not a confession, it is an ordinary Tuesday when a song comes on and she hums
it and does not go looking. Then a door, closed softly, on purpose, by her.

**The hook:** *"Closure isn't a text, it's a door I close myself"* — the title
opens and closes every chorus.

**The line for captions:** *"It's just the day I stopped needing you to
know."*

**The knife line:** *"And I got the answer that I wrote, not the one you
owe."*

**The turn:** *"It's not a message. It was never going to be a message."*

**Why it can travel:** it names a thing everyone has waited for and then
takes it away gently rather than angrily, and the video gives it two
repeatable formats — one match over a page you were never going to send, and
a montage of doors closed softly instead of slammed. The ex never appears in
a single frame, which is the whole argument made visually.

## Lyrics as they will be sung

```
[intro]
Three in the morning and the ceiling's got nothing,
Same four walls, same question in my throat.
Why is the only thing I ever wanted from you
A couple of sentences you never wrote.
I keep a light on like an answer might arrive,
Like the truth is running late but alive.

[verse]
Wrote it all out on the back of an envelope,
Every question I'd have asked you if you'd stayed.
Rehearsed the level voice, the careful wording,
The version of me that would not be afraid.
Kept the ringer on right through December,
Picked up numbers that I didn't know by name.
Every time it wasn't you, it landed,
And every time I answered I sounded just the same.

[pre-chorus]
I was holding out my hands for something
You were never going to put in them.
Waiting on a knock that isn't coming,
On a night that isn't ever going to end.

[chorus]
Closure isn't a text, it's a door I close myself,
It was never coming from anybody else.
I could wait forever for a page you'll never write,
Or put the pen down and turn out the light.
Closure isn't a text, it's the quiet in my chest,
It's the room I finally leave and let it rest.
No apology arriving, no last word to spell,
Closure isn't a text, it's a door I close myself.

[verse]
Sat down in April with a proper pen and paper,
Six long pages that you're never going to see.
Told you about the bathroom light I fixed alone,
And the friend who said your name and looked at me.
Then I read it once and took it to the sink,
Held a match to the corner, watched it go.
Ash in the basin with the water running over,
And I got the answer that I wrote, not the one you owe.

[pre-chorus]
I stopped holding out my hands for something
You were never going to put in them.
There's no knock coming and I stopped listening,
And the night I thought would never end just did.

[chorus]
Closure isn't a text, it's a door I close myself,
It was never coming from anybody else.
I could wait forever for a page you'll never write,
Or put the pen down and turn out the light.
Closure isn't a text, it's the quiet in my chest,
It's the room I finally leave and let it rest.
No apology arriving, no last word to spell,
Closure isn't a text, it's a door I close myself.

[instrumental]

[bridge]
Turns out closure isn't a confession,
It isn't you explaining what you meant.
It's a Tuesday when I hear a song and hum it,
And I don't go looking for where you went.
It's a name I say out loud without a flinch,
It's an old address I drive past and don't slow.
It's not a message. It was never going to be a message.
It's just the day I stopped needing you to know.

[chorus]
Closure isn't a text, it's a door I close myself,
It was never coming from anybody else.
I'm not waiting on a page you'll never write,
I put the pen down and I turned out the light.
Closure isn't a text, it's the quiet in my chest,
It's the room I finally left and let it rest.
No apology arriving, and there's nothing to tell,
Closure isn't a text, it's a door I close myself.

[post-chorus]
Close it soft, close it slow,
Not a slam and not a show.
Close it soft, close it slow,
Turn the handle, let it go.
Close it soft, close it slow,
And I don't need you to know.

[outro]
There's a light I don't leave on for you now,
And a page in the sink that turned to grey.
Morning at the window, kettle going,
And a door I closed myself, and it stayed.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2095 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
