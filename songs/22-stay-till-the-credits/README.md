# Stay Till the Credits

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-second song. Female lead **Mahima**, cinematic ballad with a modern
low end, romance, US register. 86 BPM, C minor, no modulation — the final
chorus widens instead of lifting and changes one line. Same singer as songs
1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission cleaned for the engine and revised at three points (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 86 BPM, C minor, grand piano and solo cello, sub-bass, strings, and the folding-seats and empty-room ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 69 entries — built from the submission's scene direction, plus a four-look character bible, faceless exes, the three-grade rule, the never-legible-screen rule, workflow, the credits challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json` — 86 BPM is a ballad and the 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 22-stay-till-the-credits
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\22-stay-till-the-credits\caption.txt `
  --lyrics-file songs\22-stay-till-the-credits\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\22-stay-till-the-credits\output\stay_till_the_credits.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Descriptive tag lines reduced to plain tags; `[final chorus]` → `[chorus]`; every repeated chorus and pre-chorus written out in full | Only the checkpoint's documented tags exist, and the model would sing the word repeat |
| The performance notes in the section headings — almost conversational, bare, hushed — moved into `caption.txt` | Stage directions in the lyric body get sung |
| `[verse 1]` lines five and seven rewritten | Craft pass: line five contained *the boring part*, which is the chorus's own phrase, spending the hook a full section before it lands; and line seven's *in the blue* made three consecutive rhymes on *crew / blue / you* with *knows* orphaned, breaking the ballad stanza that verse two holds. The rewrite restores ABCB and replaces both with new material — she stays *for the names nobody knows*, and she is watching him *with my coat still on my knees*, which pays off the *coats on* in the intro: she was one of the leavers |
| `torch` → `flashlight` in the bridge | Song 22 is US register per the catalogue's register map |
| The post-chorus refrain *"And we're still here, we're still here"* → *"And we don't get up, we don't get up"* | Originality: song 04 already chants *"We're still here, we're still here"* in its own post-chorus and again in its outro. The replacement is more specific to this song anyway — it names the physical act the whole record is about, staying in the seat |

Kept exactly as written: the intro, verse two, both pre-choruses, all four
choruses, the rest of the bridge, the outro, 86 BPM, C minor, the
instrumentation and the mood arc. 601 words became 605, inside the ballad
budget.

## The story and the hooks

Everybody is leaving while the music is still playing — coats on, phones
out, halfway up the aisle — and one man is still in the back row reading
every name, because the people who built it deserve a little while. She has
only ever been loved through the exciting part: kisses at the big scene,
gone before the fade, loud in the trailer and quiet when it mattered. Three
months in it stops being a movie and becomes the dishes, the traffic, her
mother on the phone and her at her worst on a Tuesday, and he is still
there, reading all of her small print. In the bridge the usher's flashlight
crosses their feet, the screen is reduced to a rectangle of light, and she
rewrites what love is. The final chorus stops asking him to stay and puts
her in the seat instead.

**The hook:** *"Stay till the credits, stay till the lights come on"* — the
title opens the chorus and closes it, and the whole song is one image
anybody who has ever sat through a credit roll already owns.

**The line for captions:** *"Anyone can love me in the good light."*

**The turn:** *"Now I think it's who's still there when there's nothing left
to watch... Then I don't want the movie, I want the after show."*

**The change:** the last chorus swaps *"Be the one in the back row who
doesn't walk away"* for *"I'll be the one"* — she stops making a request and
makes a promise, and the video moves the coat off her knees to prove it.

**Why it can travel:** the whole idea fits in four words, the challenge
films itself at any cinema, and it argues for the unglamorous half of a
relationship at a moment when everything else is selling the trailer.

## Lyrics as they will be sung

```
[intro]
Everybody's leaving while the music's still playing,
Coats on, phones out, halfway up the aisle.
But you're still sitting there reading every name,
Like the people who built it deserve a little while.

[verse]
I've had the kind of love that leaves at the ending,
Kisses at the big scene, gone before the fade.
Loud in the trailer, quiet when it mattered,
Every promise in the dark got quietly unmade.
But you stay in your seat for the names nobody knows,
The caterers, the drivers, the second unit crew.
And I'm watching you watch it with my coat still on my knees,
Thinking, that's the kind of staying that I want from you.

[pre-chorus]
Because anyone can love me in the good light,
Anyone can hold me when the strings swell high.
I don't need the hero, I need the one
Who's still in his seat when the story's done.

[chorus]
Stay till the credits, stay till the lights come on,
Stay through the boring part after the ending's gone.
When the crowd walks out and the screen goes grey,
Be the one in the back row who doesn't walk away.
Stay till the credits, stay till the end of the song,
Stay till the lights come on.

[verse]
Three months in, and it's not a movie anymore,
It's the dishes and the traffic and my mother on the phone.
It's me at my worst on a Tuesday in the kitchen,
It's the version of me that the trailer never showed.
And you're still here, reading all of my small print,
The flaws in the footnotes, the parts I'd cut if I could.
You don't need the montage, you don't need the ending,
You just want to sit here, and I never understood.

[pre-chorus]
Because anyone can love me in the good light,
Anyone can hold me when the strings swell high.
I don't need the hero, I need the one
Who's still in his seat when the story's done.

[chorus]
Stay till the credits, stay till the lights come on,
Stay through the boring part after the ending's gone.
When the crowd walks out and the screen goes grey,
Be the one in the back row who doesn't walk away.
Stay till the credits, stay till the end of the song,
Stay till the lights come on.

[instrumental]

[bridge]
The usher's got his flashlight out, the popcorn's getting swept,
The screen's just a rectangle of light.
I used to think that love was the part with the music,
The kiss before the black, the walk into the night.
Now I think it's who's still there when there's nothing left to watch,
Who's holding my hand when the story lets go.
So if this is the after, if this is the rest of it,
Then I don't want the movie, I want the after show.

[chorus]
Stay till the credits, stay till the lights come on,
Stay through the boring part, that's where I belong.
When the crowd walks out and the screen goes grey,
I'll be the one in the back row who doesn't walk away.
Stay till the credits, stay till the end of the song,
Stay till the lights come on.

[post-chorus]
And the lights come on, and the lights come on,
And we don't get up, we don't get up.
And the lights come on, and the lights come on,
And we don't get up, we don't get up.

[outro]
Everybody's gone now, the music's still playing,
The last name rolls up and the screen goes white.
You turn to me in the empty room and ask me what I thought,
And I say, I think I'll stay.
I think I'll stay.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 605 → ~5.2 min at 116 wpm, 87% of frame cap |
| Caption + lyrics tokens | 2079 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
