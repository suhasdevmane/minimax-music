# Wrong Number

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song seventy-two. Female lead **Mahima**, UK pop-rap with live brass, trap
drums and a chanted hook — rapped verses, a sung chorus — 120 BPM, G minor,
UK register with northern city detail. The uptempo pacing class. Same singer
as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 756 sung words, uptempo budget |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock, plus a `Rap and Spoken Delivery` line for the two pop-rap verses. 120 BPM, G minor, live brass and trap drums, the phone-buzz and tram-hum textures, and the beat switch inside the instrumental. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 80 entries — with a three-look character bible, three identity-locked friends, a faceless ex, locked-off rap plates, workflow, four shareable cuts and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 72-wrong-number
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\72-wrong-number\caption.txt `
  --lyrics-file songs\72-wrong-number\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\72-wrong-number\output\wrong_number.wav
```

Expected ~2 h.

## Pacing is the risk here, as it was on song 8

This is an uptempo song with two rapped verses, and rap pacing on this model
is still estimated rather than measured. The lyric is 756 words. What that
means at different pacings against the six-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 125 wpm | 6.0 min | **at the cap** |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 160 wpm | 4.7 min | 79% |
| 180 wpm | 4.2 min | 70% |

The two rap verses are 226 of the 756 words and a pop-rap verse at 120 BPM
typically sits at 160–190 wpm; the two chanted post-choruses are faster still.
A blended estimate of 150–160 wpm lands the record near five minutes. The
guard is set at a deliberately conservative 140. **If the first render
truncates the outro, drop the second post-chorus (twenty-nine words, a
repeat) and re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed, including around his messages and her three-word reply | Punctuation is not sung; the model reads the body literally |
| Digits spelled out — *six months*, *ten to one*, *half a year*, *half past ten*, *second drink* | The model sings digits unpredictably |
| Descriptive tag lines (`[verse 1 — full trap beat…]`, `[post-chorus — crowd chant]`) reduced to plain `[verse]`, `[post-chorus]` | Only the documented plain tags exist; text on a tag line is dropped |
| The rap and chant directions moved out of the lyric body into the caption's `Rap and Spoken Delivery` line and `Duet`-free `Global Emotional Progression` | The model sings the lyric body literally; delivery instructions belong in the caption |
| Both rap verses cut from twelve bars to ten, and the pre-choruses and intro tightened | The submission ran to 841 words, over the uptempo cap; the trims removed repeated ideas, not punchlines |
| Every repeated chorus and post-chorus written out in full; the final chorus given new lines six and eight | The model would sing a `(repeat)` marker, and the final chorus is where the sorry stops being an apology |

Kept exactly as written: the hook, the chant, 120 BPM, G minor, the brass
arrangement, the northern geography and every punchline in the submission.

## The story and the hooks

Six months of nothing, then his name on her screen at ten to one in the
morning, opening with a compliment, with the same three dots he always did
when he was working out a lie. She reads it on a tram coming into Piccadilly
with her own shopping in her hands and her own name on the rent, and she
answers the way a stranger would. He escalates — a laugh, a who is this, a
furious paragraph at two — and she reads it over coffee with her flatmate and
bins it before Monday. She goes to a phone shop on a Saturday and gets a new
number printed on a receipt like a certificate. The bridge gives him exactly
two lines of genuine warmth, and then the argument: she did the whole
rebuild, and he wants the finished flat.

**The hook:** *"Sorry, wrong number, she doesn't live here anymore."*

**The chant:** *"Wrong number, wrong number, wrong girl, wrong year."*

**The rap clip:** *"You want the girl who sat up waiting on a maybe and a
might / She got made redundant, mate, they shut it down one night."*

**The quote:** *"I did the whole rebuild and you want the finished flat."*

**Why it can travel:** it is funny without being a novelty, it is specific to
a real city rather than a generic one, and the chant is four words a room can
shout back. The kitchen chant sequence is the shareable cut and the three
words are the challenge.

## Lyrics as they will be sung

```
[intro]
Six months of nothing, then your name on my screen at ten to one,
Same three dots you always did when you were working out a lie.
I let it sit a minute while the tram went through the dark,
Then I typed three small words and put the whole thing by.

[verse]
You said long time, hope you're keeping well,
Like half a year of silence was a holiday you spent.
I read it on the tram, coming into Piccadilly,
With my own bags in my hands and my own name on the rent.
You got the number off a mate who got it off a mate,
And you opened with a compliment, which is peak, and it's late.
I've moved, I've changed the locks, I've changed the postcode too,
There's a chippy on my corner and it knows my name, not you.
You want the girl who sat up waiting on a maybe and a might,
She got made redundant, mate, they shut it down one night.

[pre-chorus]
So I typed it out slow with a smile on my face,
Read it twice, sent it, put the phone away.
The tram went under the bridge and the signal cut,
And I never checked it once for the rest of the day.

[chorus]
Sorry, wrong number, she doesn't live here anymore,
New city, new keys, new name on the door.
The girl you're texting, mate, moved out in the spring,
She left no forwarding address for anything.
Sorry, wrong number, this is not who you think,
She doesn't wait up and she doesn't lose a wink.
Sorry, wrong number, she doesn't live here anymore,
Try somebody else, like you did before.

[post-chorus]
Wrong number, wrong number, wrong girl, wrong year,
Wrong number, wrong number, she isn't here.
Wrong number, wrong number, wrong girl, wrong year,
Sorry, wrong number, she isn't here.

[verse]
Three dots, then a laugh, then a who's this, are you serious,
Then a paragraph at two in the morning, and it's furious.
I read it with my coffee and my flatmate on the Sunday,
And we laughed like it was telly and I binned it before Monday.
Went down to the phone shop on a Saturday in spring,
Got a number on a receipt and it felt like a new thing.
Same face, same laugh, same ring in the same nose,
Same girl, brand new terms, and the first term is, no.
I'm not angry and I'm not owed and I'm not keeping score,
I just don't answer numbers that I deleted before.

[pre-chorus]
Typed it out again with the very same grin,
Three small words, and I let them do the rest.
The tram came over the bridge with the whole town lit,
And I went to meet the girls in the loud red dress.

[chorus]
Sorry, wrong number, she doesn't live here anymore,
New city, new keys, new name on the door.
The girl you're texting, mate, moved out in the spring,
She left no forwarding address for anything.
Sorry, wrong number, this is not who you think,
She doesn't wait up and she doesn't lose a wink.
Sorry, wrong number, she doesn't live here anymore,
Try somebody else, like you did before.

[instrumental]

[bridge]
For a second I remembered the good version of you,
The one that made me laugh in a kitchen in the rain.
Then I put my coat on and I got the tram again.
It isn't that I hate you, it's that I'm not free labour,
I did the whole rebuild and you want the finished flat.
The girl who lived here loved you and she paid for it in years,
And she's happy, and she's gone, and you cannot have her back.

[chorus]
Sorry, wrong number, she doesn't live here anymore,
New city, new keys, new name on the door.
The girl you're texting, mate, moved out in the spring,
She left no forwarding address for anything.
Sorry, wrong number, this is not who you think,
She's out with her girls and she's on her second drink.
Sorry, wrong number, she doesn't live here anymore,
And I'm not sorry, and I'm not sorry, and I'm sure.

[post-chorus]
Wrong number, wrong number, wrong girl, wrong year,
Wrong number, wrong number, she isn't here.
Wrong number, wrong number, wrong girl, wrong year,
Sorry, wrong number, she isn't here.

[outro]
New flat, new key, new light in the hall,
New number nobody's got but the people that I call.
If it rings after midnight it's my sister or my mate,
And whoever you're texting, she left. It's too late.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 756 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2370 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
