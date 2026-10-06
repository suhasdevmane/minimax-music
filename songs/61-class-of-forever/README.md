# Class of Forever

**Status: written and verified, NOT rendered. Not yet in the queue.**

Sixty-first song. Female lead **Mahima**, anthemic pop-rock / heartland
alternative, US register, 116 BPM, B♭ major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 630 sung words, mid class |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 116 BPM, B♭ major, two ringing guitars, dry punchy kit, Hammond-style organ, a real gang vocal on the last chorus. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 75 entries — with a three-look character bible, Kai as the friend who stays, a faceless coach, the fluorescent-to-dawn light rule, workflow, the ten-year challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 61-class-of-forever
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\61-class-of-forever\caption.txt `
  --lyrics-file songs\61-class-of-forever\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\61-class-of-forever\output\class_of_forever.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung, and the model reads em-dashes unpredictably |
| Every number spelled as a word — *four years*, *fifty caps*, *five-year plan*, *ten years* | The model sings digits unpredictably |
| Descriptive tag lines (`[intro — school bell, chiming guitar, low tom]`, `[verse 1]`, `[final chorus]`) reduced to plain `[intro]` `[verse]` `[chorus]` | Only the documented plain tags exist; anything else is dropped or sung |
| Every repeated chorus written out in full rather than marked as a repeat | A repeat marker would be sung as a lyric |
| Performance directions (the drumless bridge, the gang vocal, the stomp under the post-chorus) moved into `caption.txt` | The model sings the lyric body literally |
| Two lines added to the intro and two to the post-chorus chant | The submission came in at 600 words, the floor of the mid budget; the additions raise it to 630 without touching a verse or the hook |

Kept exactly as written: every other lyric line, 116 BPM, B♭ major, the
instrumentation, the light-order video concept and the mood arc.

## The story and the hooks

The last bell rings and nobody moves. She scrapes a sticker off a locker and
finds four years of glue in the shape of it, the coach holds the gym door open
and pretends he is not crying, and the whole class stands in a parking lot at
golden hour holding car keys nobody uses. Then the field: caps in the
floodlights, sprinklers at midnight nobody runs from, one boy enlisting, one
girl flying out Tuesday, and a promise sworn on a stolen helmet. The bridge is
the turn, and it is not a triumphant one — she knows the group chat goes quiet
by the second fall and half of them will never drive back, so she asks for
nothing except the rest of the night. Dawn comes up on empty bleachers, one
pair of sneakers on the fifty and one car left in the lot.

**The hook:** *"We're the class of forever, no goodbye's gonna stick."*

**The line for captions:** *"We've got no five-year plan, we've got the whole
of the night."*

**The turn:** *"So I won't ask you for a decade or a vow / Just stay out on
this field with me right now."*

**The chant:** *"Hands up if you're never getting over it."*

**Why it can travel:** graduation is an annual, global, self-renewing occasion
with an enormous amount of user footage attached to it, and this is the rare
graduation song that admits most of the promises will not be kept and stays
joyful anyway.

## Lyrics as they will be sung

```
[intro]
Last bell rang and nobody moved,
Half of us just stood there in the hall.
Somebody's speaker in the parking lot,
Playing the same four chords for us all.
Nothing but floor wax and fluorescent light,
And now they want the keys and the building back.

[verse]
I scrape a sticker off the locker door,
It leaves the shape of it, four years of glue.
Coach is holding the gym doors open,
Saying, go on, get out, like he isn't crying too.
There's a dent in the trophy case from sophomore year,
Nobody ever said whose fault it was.
I put my hand flat on the cold glass,
And I say thank you to a building, just because.

[pre-chorus]
Nobody's engine is actually running,
Everybody's keys are in their hand.
We keep saying that we're gonna go now,
Then nobody goes. I think we understand.

[chorus]
We're the class of forever, no goodbye's gonna stick,
Throw it up, let it fall, we were here and it was quick.
Fifty caps in the floodlights, half of them come down wrong,
Somebody's crying, somebody's laughing, somebody starts the song.
We've got no five-year plan, we've got the whole of the night,
And a field full of people I will know for life.
Turn the headlights on the grass, take one more pic,
We're the class of forever, no goodbye's gonna stick.

[verse]
Midnight on the fifty and the sprinklers kick on,
Nobody runs for it, we let it soak us through.
He's enlisting in the fall, she's flying out on Tuesday,
And I'm staying right here, and that's alright too.
We swear on a helmet somebody stole from the shed,
Same spot, ten years, whoever can come.
Then we sit in the wet grass till the sky goes gray,
And nobody says the word done.

[pre-chorus]
Somebody's mom keeps flashing headlights at the gate,
Somebody's brother says he'll drive us all around.
We keep saying that we're gonna go now,
And then nobody goes. Nobody makes a sound.

[chorus]
We're the class of forever, no goodbye's gonna stick,
Throw it up, let it fall, we were here and it was quick.
Fifty caps in the floodlights, half of them come down wrong,
Somebody's crying, somebody's laughing, somebody starts the song.
We've got no five-year plan, we've got the whole of the night,
And a field full of people I will know for life.
Turn the headlights on the grass, take one more pic,
We're the class of forever, no goodbye's gonna stick.

[instrumental]

[bridge]
I know how this goes, I have watched it before,
The group chat goes quiet by the second fall.
Half of us won't drive back when the ten years land,
And half of us will, and half is not that small.
So I won't ask you for a decade or a vow,
Just stay out on this field with me right now.

[chorus]
We're the class of forever, no goodbye's gonna stick,
Throw it up, let it fall, we were here and it was quick.
Fifty caps in the wet grass, we can leave them where they land,
Somebody's crying, somebody's laughing, somebody takes my hand.
We've got no five-year plan, we've got the rest of the night,
And a field full of people I will know for life.
Kill the headlights, one more song before we split,
We're the class of forever, no goodbye's gonna stick.

[post-chorus]
Oh, no goodbye's gonna stick,
Oh, we were here and it was quick.
Same spot, same gate, same ten years,
Oh, no goodbye's gonna stick.
Hands up if you're never getting over it,
Oh, no goodbye's gonna stick.

[outro]
Sun's coming up on the empty bleachers,
Somebody's shoes still out on the grass.
I'm the last one in the parking lot,
And I'm not in a hurry, and I'm not sad.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 630 → ~5.4 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2121 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
