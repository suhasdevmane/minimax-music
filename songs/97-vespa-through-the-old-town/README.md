# Vespa Through the Old Town

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninety-seventh song. Female lead **Mahima**, Italian-flavoured Mediterranean
pop with mandolin tremolo, accordion, nylon guitar and handclaps. 112 BPM,
C major. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words, ballad/mid budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 112 BPM, C major, nylon guitar spine, mandolin countermelody, accordion swells, trumpet and tambourine on the last chorus, and the bar, bell, scooter and square-band textures. A `Delivery Note` line fixes the told-not-sung verse tone. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a three-look character bible, the handlebar-mount rule, the taped-mirror motif, the withheld bell tower, the narrow-street challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json`: at 112 BPM this is a ballad/mid song and the length guard's
116 wpm default is the right estimate.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 97-vespa-through-the-old-town
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\97-vespa-through-the-old-town\caption.txt `
  --lyrics-file songs\97-vespa-through-the-old-town\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\97-vespa-through-the-old-town\output\vespa_through_the_old_town.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech in verse one and verse two | Punctuation is not sung and quotation marks confuse the tokenizer |
| Em-dashes replaced with commas throughout | The model sings the lyric body literally |
| `2 euros` → *"Two euros"*; `11` → *"eleven"*; `7` → *"seven numbers"*; `7am` → *"seven"* | The model sings digits unpredictably |
| `[verse 1]` / `[verse 2]` / `[final chorus]` and the descriptive tag lines reduced to plain tags | Only the checkpoint's documented tags exist |
| The final chorus written out in full rather than `(as chorus 1)`, keeping its three varied lines | The verify script flags `(repeat)`, and the model would sing it |
| Trimmed forty-eight words across every section | 687 words overran the 640-word ballad budget by a wide margin; the cuts were articles, auxiliaries and one over-long line, and no image was lost |

Kept exactly as written: every image, 112 BPM, C major, the instrumentation,
the mood arc and the bridge's refusal to make a promise.

## The story and the hooks

She is a bad tourist: a paper map she cannot refold, no sense of direction,
and a week. He drinks his coffee standing up at a bar with no chairs, knows a
guy with a key, and produces a mint-green scooter with a wing mirror taped on
twice. The whole song happens from the back of it — left at the church, right
at the laundry lines, down a street too narrow for a car, waving at a
stranger's grandmother like she lives there. In the evening they split a lemon
ice on a fountain rim and say the thing about kissing to the water instead of
to each other. Then the bridge, which is the whole point: there is a plane on
Sunday, and neither of them is going to ask the other for anything. So they
take the long way back to the harbour instead. The bike goes back on its chain
by the church, the flight goes at seven, and June is left open.

**The hook:** *"On a Vespa through the old town, holding on to you."*

**The line for captions:** *"Half a tank of nowhere and a summer to use."*

**The turn:** *"I won't ask you to wait, you won't ask me to stay / We're
better than a promise we'd break anyway."*

**The image:** *"And a taped-up mirror holding all of that light."*

**Why it can travel:** it is a holiday romance that ends honestly instead of
tragically, and every image in it — the narrow street, the laundry lines, the
grandmother's wave — is something a listener can film on their own trip.

## Lyrics as they will be sung

```
[intro]
Two euros for a coffee at a bar with no chairs,
You drank yours standing up like you were born here.
I had a map that I folded wrong,
A terrible sense of north, and a week.

[verse]
You said no bus comes back here until Thursday,
But you knew a guy with a key and a bike.
It was mint green and older than both of us,
And the mirror was taped back on twice.
Bag on my back and my hands on your jacket,
And the engine sounded like a wasp in a jar.
Then the road tipped down and the town opened,
And I forgot to ask how far.

[pre-chorus]
Left at the church, right at the laundry lines,
Down a street too narrow for a car.
Somebody's grandmother waved from a window,
And I waved back like I lived here.

[chorus]
On a Vespa through the old town, holding on to you,
Cobblestones like a heartbeat coming through my shoes.
Lemon trees and laundry and a bell I cannot see,
And a boy from a town I can't spell in front of me.
On a Vespa through the old town, nothing left to prove,
Half a tank of nowhere and a summer to use.
There's no part of this week that I'd undo,
On a Vespa through the old town, holding on to you.

[verse]
We split a lemon ice on the rim of a fountain
Where the water's been running since before either name.
You said everyone here has kissed somebody on it,
And you said it to the water, and I said the same.
The band in the square only knows seven numbers,
So they played the slow one twice and took their time.
You put your jacket round my shoulders near eleven,
And I decided the night could be mine.

[pre-chorus]
Left at the bakery, right at the harbour,
Down where the boats are all faded blue.
Somebody's radio was playing our nothing,
And I sang it wrong on purpose so you would too.

[chorus]
On a Vespa through the old town, holding on to you,
Cobblestones like a heartbeat coming through my shoes.
Lemon trees and laundry and a bell I cannot see,
And a boy from a town I can't spell in front of me.
On a Vespa through the old town, nothing left to prove,
Half a tank of nowhere and a summer to use.
There's no part of this week that I'd undo,
On a Vespa through the old town, holding on to you.

[instrumental]

[bridge]
Sunday there's a plane with my name on a seat,
And a job and a coat and a grey little street.
I won't ask you to wait, you won't ask me to stay,
We're better than a promise we'd break anyway.
So give me the long way back to the harbour tonight,
And a taped-up mirror holding all of that light.

[chorus]
On a Vespa through the old town, holding on to you,
Cobblestones like a heartbeat coming through my shoes.
Lemon trees and laundry and a bell I finally see,
And a boy who says my name like it belongs to the sea.
On a Vespa through the old town, nothing left to lose,
Half a tank of nowhere and a summer to use.
There's no part of this week that I'd undo,
On a Vespa through the old town, holding on to you.

[post-chorus]
Take the corner wide, let the old town blur,
Every shutter open, every awning in the sun.
Take the corner wide, I'm holding on for good,
And the road keeps going, the summer's not done.

[outro]
The mint green bike is chained by the church again,
My flight goes at seven, and the sea doesn't care.
I'll come back in June when the lemons are heavy,
On a Vespa through the old town, if you're still there.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2142 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
