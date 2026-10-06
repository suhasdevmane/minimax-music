# Barefoot on the Boulevard

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song fifty-four. Female lead **Mahima**, modern funk with clavinet, slap bass
and a three-piece horn section, with a spoken-then-rapped second verse.
112 BPM, A minor, mid pacing, UK register. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction, lyrics and per-section video direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 619 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1. 112 BPM, A minor, slap bass, clavinet, three-piece horns, and the note that verse two is spoken for two lines then rapped over bass, drums and clavinet only. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 69 entries — with a two-look bible, the faceless-corner-lads rule, the one-direction camera rule, feet-macro guidance, the shoes-off challenge and a QC checklist |
| `source/` · `output/` · `logs/` | Submission; render lands in output/ |

No `render.json` — at 112 BPM this is a mid-tempo song and the verify
script's 116 wpm default is the right guard.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 54-barefoot-on-the-boulevard
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\54-barefoot-on-the-boulevard\caption.txt `
  --lyrics-file songs\54-barefoot-on-the-boulevard\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\54-barefoot-on-the-boulevard\output\barefoot_on_the_boulevard.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung |
| Digits spelled as words (*two in the morning*, *four inches*, *a hundred nights*) | The model sings digits unpredictably |
| Descriptive tag lines (*[intro – clavinet, wet street, no drums]*, *[verse 2 – spoken, then rapped]*) reduced to plain tags | Only the checkpoint's documented tags exist; text on a tag line is dropped |
| The spoken-then-rapped instruction moved out of the lyric body into the caption's `Vocal Style` context and the arrangement blocks | The model sings the lyric body literally |
| Repeated choruses written out in full | The model would sing a repeat marker |
| Two long verse couplets trimmed for the mid-tempo word budget | 619 words sits inside the 600–640 band; the submission ran long |

Kept exactly as written: the hook, the rap cadence, 112 BPM, A minor, the
horn and clavinet arrangement, the UK register, the dawn ending.

## The story and the hooks

Two in the morning, a wide wet northern boulevard, and a pair of four-inch
heels that have stopped being worth it. She sits on a bollard, takes them
off with the straps in her teeth, and the freezing paving turns out to be
the best thing that has happened all night. The second verse walks half a
mile of it — the tram stop, the cabs with their engines running, the lads on
the corner who go quiet, and a young woman walking too fast with her keys
through her fist, who gets a stranger falling into step beside her and a
conversation about nothing until she is past it. Then the bridge stops the
band and admits what the song is about: years of standing very still in
shoes somebody else chose, waiting on a lift, waiting to be asked. By the
last chorus there are six of them in the road and the buses can wait.

**The hook:** *"Barefoot on the boulevard, heels in my hand."*

**The line for captions:** *"Never felt safer than walking alone."*

**The turn:** *"Now the straps are in my fist and the street is in my chest
/ And the walking is the best part, never was the dress."*

**The rap clip:** *"Cobbles like a drum kit and the kerb stones like a snare
/ I am not going home yet, I am going everywhere."*

**Why it can travel:** it is a confidence record that never argues with
anyone. The hook is an image, the challenge is a pair of shoes in your hand,
and the solidarity beat in verse two is the part people will send to each
other.

## Lyrics as they will be sung

```
[intro]
Wet street shining like it's just been laid,
Orange in the puddles where the tram lines fade.
Somebody's boot lid open with the bass turned round,
And I'm undoing buckles, and here comes the sound.

[verse]
Two in the morning and my shoes have gone traitor,
Four inches of glamour and a blister like a saucer.
So I sit on a bollard with the straps in my teeth,
And the paving is freezing and the freezing is relief.
Nobody's watching and the whole street can see,
I stand up and the city rearranges round me.

[pre-chorus]
There's a bassline coming out of a car door,
There's a busker packing up and starting one more.
I take the first step and the cold goes right through,
And I have never in my life felt as good as I do.

[chorus]
Barefoot on the boulevard, heels in my hand,
Wet tram rails and the whole street's a band.
Every shop window's a mirror I can use,
Every kerb is a catwalk and I'm making the news.
Barefoot on the boulevard, two in the morning,
The city is my dance floor and it's only just warming.
Don't need a lift and I don't need a plan,
Barefoot on the boulevard, heels in my hand.

[verse]
Right, shoes in the left hand and the phone in the right,
Half a mile of orange lamps and I am taking the lot tonight.
Past the tram stop, past the cabs with their engines still humming,
Past the lads on the corner who go quiet when they see me coming.
There's a girl walking quick with her keys through her fist,
So I fall in beside her and we chat till the fear is dismissed.
Cobbles like a drum kit and the kerb stones like a snare,
I am not going home yet, I am going everywhere.

[pre-chorus]
I take the next step and the cold's nothing new,
And there's nobody walking this city like I do.

[chorus]
Barefoot on the boulevard, heels in my hand,
Wet tram rails and the whole street's a band.
Every shop window's a mirror I can use,
Every kerb is a catwalk and I'm making the news.
Barefoot on the boulevard, two in the morning,
The city is my dance floor and it's only just warming.
Don't need a lift and I don't need a plan,
Barefoot on the boulevard, heels in my hand.

[instrumental]

[bridge]
I spent years in shoes that somebody else chose,
Standing very still in a corner in a pose.
Held my breath through a hundred nights like this,
Waiting on a lift, waiting to be asked, waiting to be missed.
Now the straps are in my fist and the street is in my chest,
And the walking is the best part, never was the dress.

[chorus]
Barefoot on the boulevard, heels in my hand,
Wet tram rails and the whole street's a band.
Every shop window's a mirror I can use,
Every kerb is a catwalk and I'm making the news.
Barefoot on the boulevard, two in the morning,
The city is my dance floor and it's only just warming.
Six of us laughing with our shoes in our hands,
Owning the middle of the road where the buses ran,
Don't need a lift and I don't need a plan,
Barefoot on the boulevard, heels in my hand.

[post-chorus]
Heels in my hand and the horns coming in,
Cold on the soles and it feels like a win.
Heels in my hand and the long road home,
Never felt safer than walking alone.

[outro]
Sky going pale over the market roof,
Straps in my fist and a mile of proof.
Feet are a state and the morning's begun,
Barefoot on the boulevard, and I'm not done.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 619 → ~5.3 min at 116 wpm, 89% of frame cap |
| Caption + lyrics tokens | 2176 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
