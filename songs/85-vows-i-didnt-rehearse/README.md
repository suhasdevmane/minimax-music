# Vows I Didn't Rehearse

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song eighty-five. Female lead **Mahima**, acoustic ballad / modern folk-pop,
a back-garden wedding, US voice. 84 BPM, G major lifting a whole step to A
for the final chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 639 sung words, ballad budget |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 84 BPM, G major with the modulation, one guitar and one piano at the centre, a small string section, and the garden room tone that is never faded out. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 68 entries — with a three-look character bible, Kai as the groom, the paper's whole life as a through-line, the composited-handwriting rule, workflow, the unread-vows challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 85-vows-i-didnt-rehearse
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\85-vows-i-didnt-rehearse\caption.txt `
  --lyrics-file songs\85-vows-i-didnt-rehearse\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\85-vows-i-didnt-rehearse\output\vows_i_didnt_rehearse.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung; the model renders the body literally |
| Digits spelled as words (*three days*, *two miles*, *three drafts*, *twice*) | The model sings digits unpredictably |
| The descriptive tag lines (`[intro – one guitar, room sound, almost spoken]`, `[bridge – guitar and voice alone]`, `[final chorus – modulated, choir, strings]`) reduced to plain tags | Only the checkpoint's plain section tags exist; anything else is dropped or sung |
| Both full choruses written out rather than marked as repeats | A `(repeat)` line would be sung |
| Verse one cut from eight lines to six and verse two from eight to seven | 690 words on the first pass; the ballad budget is 600–640. The aunt's line and the sister's joke went; the hospital hallway and the cold coffee stayed |
| *I have watched him choose me* became *I've watched you choose me* | The verse is addressed to him throughout; the third person broke point of view mid-line |

Kept exactly as written: the hook, the four months of drafts, the paper going
soft, the loose dog, the officiant lowering his script, the bridge's false
version, the drawer, 84 BPM, G major with the lift, the instrumentation and
the mood arc.

## The story and the hooks

She wrote her vows in April and rewrote them in June, read them to a mirror
until the mirror got bored, folded the sheet in fours and slid it into her
sleeve. Then she stands up in a back garden in front of thirty people on
folding chairs and the paper does what paper does in a hand that is shaking:
it goes soft. So she says something else. Not oceans, not time, not the joke
she stole from his sister — the Tuesday the car gave up and he walked two
miles back with a coffee going cold, the thing he said in a hospital hallway
that she refuses to repeat because that one is theirs, the fact that he sings
badly and sings anyway. The officiant lets his script fall to his side. A
stranger at the back cries. The bridge admits there was a perfect version of
the day and that it would have been a lie. The paper stays in the grass, gets
trodden on, and is picked up at the gate that night.

**The hook:** *"These are the vows I didn't rehearse."*

**The line for captions:** *"Every word I wrote down was somebody else's
first."*

**The knife line:** *"Which I'm not repeating, that one's ours to keep."*

**The turn:** *"It would have been beautiful and it would have been a lie,
because nothing about us has ever come out clean."*

**Why it can travel:** the moment a speech goes off-script is the most filmed
thirty seconds at any wedding, and this is a song written to sit under it. The
detail is small enough to be borrowed by anyone — a sink, a name said from
another room, a porch light — and the hook is a caption before it is a lyric.

## Lyrics as they will be sung

```
[intro]
I wrote it out in April, I rewrote it in June,
Read it to the mirror till the mirror got bored.
Folded it in fours and I slid it in my sleeve,
And I never looked at it again.

[verse]
Here's what the paper said, it said that you are kind,
Which is true and useless, everyone's kind on paper.
It said something about oceans, it said something about time,
It was good, it was fine, it would have made them cry.
But my hands went stupid and the paper went soft,
And I looked up and the whole speech left the yard.

[pre-chorus]
So the wind took a folding chair, the dog got loose,
And your mother has a tissue she has not used yet.
Everybody's waiting on the girl with the paper,
And the girl with the paper's got nothing left.

[chorus]
These are the vows I didn't rehearse,
The ones that came sideways, the ones that came first.
You do the dishes when I'm three days low,
You say my name like it's somewhere to go.
I don't have a metaphor, I don't have a line,
I've got a man in a rented suit and the rest of my life.
Every word I wrote down was somebody else's first,
So these are the vows I didn't rehearse.

[verse]
So I told them about the Tuesday the car gave up,
How you walked two miles back with a coffee going cold.
I told them what you said in the hospital hallway,
Which I'm not repeating, that one's ours to keep.
I told them that you sing badly and you sing anyway,
I said I've watched you choose me on days I was hard to choose,
And that's the only promise I know how to make.

[pre-chorus]
The man with the script has let it fall to his side,
And the folding chairs have stopped their little noise.
Somebody's crying in the back who isn't even family,
And you're laughing at me with your whole face.

[chorus]
These are the vows I didn't rehearse,
The ones that came sideways, the ones that came first.
You do the dishes when I'm three days low,
You say my name like it's somewhere to go.
I don't have a metaphor, I don't have a line,
I've got a man in a rented suit and the rest of my life.
Every word I wrote down was somebody else's first,
So these are the vows I didn't rehearse.

[instrumental]

[bridge]
There's a version of today with the paper read out perfect,
Clean and quotable, a good line for a frame.
And it would have been beautiful and it would have been a lie,
Because nothing about us has ever come out clean.
So take the mess, take the sentence that fell over,
Take the girl who lost her place and found it out loud.

[chorus]
These are the vows I didn't rehearse,
The ones that came sideways, the ones that came first.
I will not be easy and I will not be far,
I'll be the light left on when you pull in the yard.
I don't have a metaphor, I don't have a line,
I've got a man in a rented suit and the rest of my life.
For better, for worse, for the paper in the dirt,
These are the vows I didn't rehearse.

[post-chorus]
Not a word of it written, not a word of it wrong,
I found it in my chest where it had been all along.
Not a word of it written, not a word of it wrong,
And the paper's in the grass and I'm still going on.

[outro]
They found it in the grass by the gate,
Three drafts and an arrow and a line crossed out twice.
It lives in a drawer and I've never read it since,
I already said the true one out loud.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 639 at 116 wpm → ~5.5 min, 92% of frame cap |
| Caption + lyrics tokens | 2039 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
