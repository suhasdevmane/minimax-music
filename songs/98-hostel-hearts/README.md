# Hostel Hearts

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninety-eighth song. Female lead **Mahima**, warm indie pop with a mixed
gang-vocal chorus recorded live and left untuned on purpose. 106 BPM,
D major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words, ballad/mid budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 106 BPM, D major, two acoustic guitars, room-recorded stairwell claps, whistling in the break, and the fan, kettle, lighter, market and bus textures. A `Delivery Note` line fixes the deliberately untrained gang vocal. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 68 entries — with a three-look character bible, a six-person ensemble bible, the no-styling rule, the noticeboard motif, the write-your-name challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 106 BPM this is a ballad/mid song and the length guard's
116 wpm default is the right estimate.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 98-hostel-hearts
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\98-hostel-hearts\caption.txt `
  --lyrics-file songs\98-hostel-hearts\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\98-hostel-hearts\output\hostel_hearts.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | The model sings the lyric body literally and punctuation is not sung |
| `bunk 19` → *"Bunk nineteen"*; `4 days` → *"Four days"*; `4am` → *"four in the morning"*; `8 beds` → *"eight beds"* | The model sings digits unpredictably |
| The gang-vocal direction moved out of the lyric body into the caption as a `Delivery Note` line | Stage directions in the body get sung |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines reduced to plain tags | Only the checkpoint's documented tags exist |
| The final chorus written out in full rather than `(as chorus 1)`, keeping its past-tense variant line | The verify script flags `(repeat)`, and the model would sing it |
| Trimmed thirty words across the choruses, verses and pre-choruses | 669 words overran the 640-word ballad budget; the cuts were auxiliaries and articles, and no image or joke was lost |

Kept exactly as written: every character, 106 BPM, D major, the
instrumentation, the untuned gang vocal, and the mood arc.

## The story and the hooks

She arrives at bunk nineteen too tired to unpack and does not want to talk to
anybody. Three hours later she is laughing in a language she does not speak.
There is a Dutch woman running the only working pan, an Argentine who has lost
his passport, somebody's mother waving at the whole table from a video call,
and a noticeboard in the corridor covered in the names of everyone who has
already gone. Somebody writes hers on it with a marker that is dying, and that
is the moment. Four days: a night market, a passport found in a coat pocket, a
roof at four in the morning where somebody cries and nobody makes it weird,
and a thing she says out loud to people she met on Tuesday that she has never
told her sister. Then checkout at ten. The bridge is the argument she has with
everybody afterwards: four days is not too short to be real, and she has known
people for ten years who never asked her how she sleeps. The last shot is a
new tired person on the same bare mattress and somebody sliding a chair out
for her.

**The hook:** *"Hostel hearts, strangers for a night, family by the morning."*

**The line for captions:** *"It was family, and it fit in a room with eight
beds."*

**The chant:** *"Write your name on the board, write your name on the board."*

**The turn:** *"I've known people ten years who never asked me how I sleep /
And a stranger from Osaka carried my bag up two flights."*

**Why it can travel:** every person who has ever travelled alone has this
exact four days, and nobody has written the song about it that takes it
seriously. The gang vocal is designed to be sung badly by a group on a roof,
which is also the challenge.

## Lyrics as they will be sung

```
[intro]
Bunk nineteen, second floor,
A ceiling fan that only turns one way.
I came in tired and I didn't want to talk,
By ten I was laughing in a language I don't speak.

[verse]
There's a Dutch girl teaching us all to cook with one pan,
An Argentine guy who lost his passport and his mind.
Somebody's playlist, somebody's cheap red wine,
Somebody's mother on a video call waving at us.
Strangers in a kitchen with one lighter and no plan,
And nobody asks me what I do or where I've been.
First time all year that nobody wants my history,
Just my half of the table and my name.

[pre-chorus]
The door never locks and the kettle never cools,
The noticeboard is covered in the names of people gone.
Somebody writes mine on it with a dying marker,
And that's how you know that you belong.

[chorus]
Hostel hearts, strangers for a night, family by the morning,
Four days is a lifetime when you're living without warning.
We don't know each other's last names and we never will,
But you sat up when I was sick, and I'd do it again.
Hostel hearts, no address and no goodbye that lands,
A rooftop, a lighter and eleven pairs of hands.
Strangers for a night, family by the morning.

[verse]
Night market, second night, we ate something we couldn't name,
And the Argentine found his passport in his coat.
On the roof at four in the morning somebody's crying,
And nobody makes it weird, we just move closer.
The Dutch girl says she isn't going home in September,
The German plays the only slow song he knows.
And I told a room of strangers what I never told my sister,
And the sky went the colour of a peach and nobody spoke.

[pre-chorus]
The door never locks and the kettle never cools,
And checkout is at ten and we know what that means.
Somebody's bus goes first, somebody's on the stairwell,
And the marker on the board has run out.

[chorus]
Hostel hearts, strangers for a night, family by the morning,
Four days is a lifetime when you're living without warning.
We don't know each other's last names and we never will,
But you sat up when I was sick, and I'd do it again.
Hostel hearts, no address and no goodbye that lands,
A rooftop, a lighter and eleven pairs of hands.
Strangers for a night, family by the morning.

[instrumental]

[bridge]
People say it wasn't real because it only lasted four days,
As if a thing must be long before it's allowed to be true.
I've known people ten years who never asked me how I sleep,
And a stranger from Osaka carried my bag up two flights.
So call it what you want, I know what it was,
It was family, and it fit in a room with eight beds.

[chorus]
Hostel hearts, strangers for a night, family by the morning,
Four days is a lifetime when you're living without warning.
We won't know each other's last names and we never did,
But you sat up when I was sick, and I'd do it again.
Hostel hearts, no address and no goodbye that lands,
A rooftop, a lighter and eleven pairs of hands.
Strangers for a night, family by the morning.

[post-chorus]
Write your name on the board, write your name on the board,
Somebody after you will read it and feel less alone.
Write your name on the board, we were here, we were loud,
And a wall in a hallway is the only proof we own.

[outro]
The bus pulls out at six, the fan still turns one way,
And bunk nineteen has a new tired person in it now.
I hope she doesn't want to talk, and I hope she does by ten,
And I hope somebody hands her half a table and a name.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2120 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
