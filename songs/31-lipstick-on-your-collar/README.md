# Lipstick on Your Collar

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirty-first song. Female lead **Mahima**, retro doo-wop modernised into
pop-R&B — finger snaps, baritone sax and trap hats — 108 BPM, F major with a
semitone lift into the final chorus. Mid pacing class, so no `render.json`.
Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 108 BPM swung, F major lifting a semitone to F♯; walking bass, dry snaps, baritone sax, doo-wop triplet piano over trap hats and an 808, with the lipstick-cap click as ear candy. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — from the submission's scene direction, with a three-look sixties character bible, Kai as the boyfriend with the print on his collar, faceless colleagues, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 31-lipstick-on-your-collar
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\31-lipstick-on-your-collar\caption.txt `
  --lyrics-file songs\31-lipstick-on-your-collar\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\31-lipstick-on-your-collar\output\lipstick_on_your_collar.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| `7:45` → *"Seven forty-five"* (twice), `12:15` → *"Twelve fifteen"* | The model sings digits unpredictably, and a colon between two numbers is worse than either alone |
| Quotation marks removed from the dialogue lines and the air-quoted *"work wife"* (*"wow, she's bold,"* *"yeah, she is,"* *"honestly, I kind of like it,"* *"now it's only fair,"* *"do it again"*) | Punctuation is not sung; a quoted phrase can be read as a break in the line |
| Descriptive tag lines — `[intro – snaps and bass, a kiss at the door]`, `[chorus – big, bright, girl-group harmonies]`, `[bridge – half-time, honest, then the flower]`, `[post-chorus – call and response]`, `[outro – snaps and bass, the same morning again]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[verse 1]` / `[verse 2]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; the final chorus's swapped third and fourth lines carry the change instead |

Kept exactly as written: every lyric line, 108 BPM swung, F major with the
semitone lift, the instrumentation, the mood arc, the six viral moments. No
trimming was needed — 637 words fits.

## The story and the hooks

Seven forty-five, he is buttoning up, his coffee going cold in his favourite
cup, and she leaves a cherry-red print just below his left collar edge on
purpose. Not jealousy — she says so outright, twice — but pride played as a
game. Everybody's got a work wife, someone by the printer laughing at his
jokes all day, and she is not the jealous type, she is the creative kind. By
twelve fifteen he is texting her what happened in the meeting: the front
desk did a double take, the intern stopped breathing, marketing said she is
bold, and he wrote back *yeah, she is.* He gives up scrubbing it by noon and
admits he likes it. The bridge drops the game and says the real thing: it
was never about them, it is about him catching his reflection in the lobby
door and smiling because he remembered who he is going home for. Then he
comes home with a flower from the shop downstairs and tucks it behind her
ear — *now it's only fair* — and the last chorus has both marks in it. The
outro is the same doorway, the same cold coffee, and a request for a
brighter red.

**The hook:** *"Lipstick on your collar, so they know you're mine"* — the
title in the first line of every chorus, and again halfway through.

**The line for captions:** *"I don't need a ring to make it official."*

**The quote:** *"You smile like you just remembered who you're going home
for."*

**The turn:** the flower behind her ear — *"now it's only fair"* — which
makes the claim run both ways and turns a possessive joke into a mutual one.

**The loop:** the outro returns to the opening frame, so the video cuts back
to its own first shot cleanly.

**Why it can travel:** the collar-print reveal is a two-person format that
takes ten seconds to film, and the elevator-mirror shot is the second frame
people will copy. The sixties styling with a phone in hand gives editors a
look that is not currently everywhere.

## Lyrics as they will be sung

```
[intro]
Seven forty-five, you're buttoning up,
Coffee going cold in your favourite cup.
One kiss at the door before you go,
I left a little something you don't even know.

[verse]
Everybody's got a work wife, that's what they say,
Someone by the printer laughing at your jokes all day.
I'm not the jealous type, I'm the creative kind,
So I write in cherry red and leave it where they'll find.
One press on your collar, right below the ear,
You'll be halfway to the lobby before it's clear.
I hope the whole floor takes a real good look,
Baby, you're the headline, I'm the one who wrote the hook.

[pre-chorus]
Go on, take the elevator, act like you don't know,
Ten floors of mirror and a little red glow.
Straighten up your tie, keep that blushing low,
I'm two miles away and I can feel it show.

[chorus]
Lipstick on your collar, so they know you're mine,
Red on cotton white, they can read between the lines.
Give the office something for the group chat, honey,
Let them lean and whisper, let them think it's funny.
Lipstick on your collar, wear it like a sign,
Every desk on every floor can tell you're doing fine.
I don't need a ring to make it official,
Just a kiss of red on you, and baby, that's a signal.

[verse]
Twelve fifteen, you text me, they saw it in the meeting,
Front desk did a double take, the intern stopped breathing.
Somebody from marketing said, wow, she's bold,
You wrote back, yeah, she is, and that's the story told.
Tried to scrub it in the bathroom, gave up by noon,
Said, honestly, I kind of like it, then a heart, then a moon.
So tomorrow don't reach for the darker shirt,
I'll go a shade brighter, just to watch it work.

[pre-chorus]
Go on, walk the corridor, let them all stare,
Tell them it's a new brand, tell them you don't care.
Loosen up your tie, let that blushing show,
I'm two miles away and I already know.

[chorus]
Lipstick on your collar, so they know you're mine,
Red on cotton white, they can read between the lines.
Give the office something for the group chat, honey,
Let them lean and whisper, let them think it's funny.
Lipstick on your collar, wear it like a sign,
Every desk on every floor can tell you're doing fine.
I don't need a ring to make it official,
Just a kiss of red on you, and baby, that's a signal.

[instrumental]

[bridge]
It was never about them, I trust you with my life,
You could work in a room of pretty and be fine.
It's the way you catch your reflection in the lobby door
And you smile like you just remembered who you're going home for.
So keep it on, keep it on, don't wipe it away,
Let it be the loudest thing you say all day.
Then you came home with a flower from downstairs,
Tucked it behind my ear, said, now it's only fair.

[chorus]
Lipstick on your collar, so they know you're mine,
Red on cotton white, they can read between the lines.
Flower in my hair now, so they know I'm yours,
Two of us walking in like we own the whole floor.
Lipstick on your collar, wear it like a sign,
Every desk on every floor can tell you're doing fine.
I don't need a ring to make it official,
Just a kiss of red on you, and baby, that's a signal.

[post-chorus]
Red on your collar, ooh,
Everybody knows, everybody knows.
Red on your collar, ooh,
That's how it goes, that's how it goes.

[outro]
Seven forty-five, you're buttoning up,
Same cold coffee in your favourite cup.
You lean in at the door, you tilt your head,
Say, do it again, and make it a brighter red.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 637 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2256 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
