# Yes to Everything

**Status: written and verified, NOT rendered. Not yet in the queue.**

Twenty-fourth song. Female lead **Mahima** with a male pop-rap feature
(Singer B) on the third verse — dance-pop / festival pop with a drop chorus,
124 BPM, B major. Uptempo class, so it carries a `render.json`. Same singer
as songs 1–8 for the female lead.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission complete, nothing trimmed |
| [`caption.txt`](caption.txt) | Music description. Mahima's `Vocal Details` lines and the `Sonics` block byte-identical to song 1 — the voice lock. A male pop-rapper added as Singer B with a section-by-section `Duet Structure`. 124 BPM, B major, sidechained supersaws, the drop chorus, the fairground-organ and cab-meter textures. |
| [`render.json`](render.json) | Per-song pacing for the length guard (`wpm: 140`) — see the pacing note below |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 88 entries — from the submission's scene direction, with a three-look character bible, Kai as the date, the yes-cut jump-cut rule, workflow and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 24-yes-to-everything
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\24-yes-to-everything\caption.txt `
  --lyrics-file songs\24-yes-to-everything\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\24-yes-to-everything\output\yes_to_everything.wav
```

Expected ~2 h.

## Pacing is estimated, not measured

Uptempo song, same open question as song 8. The lyrics are **758 words**.
What that means at different pacings against the model's 6-minute hard cap:

| If it sings at | Length | Of cap |
|---|---|---|
| 116 wpm (ballad default) | 6.5 min | **overrun — outro lost** |
| 125 wpm | 6.1 min | **overrun** |
| **140 wpm (the guard setting)** | 5.4 min | 90% |
| 160 wpm | 4.7 min | 79% |
| 180 wpm | 4.2 min | 70% |

The chorus and the two post-chorus chants are word-dense and will run fast,
and the male rap verse (111 of the 758 words) at 124 BPM is typically
170–200 wpm; a blended estimate is 145–155 wpm, landing near 5.2 minutes.
The guard is set at a deliberately conservative 140. **If the first render
truncates the outro, drop the second post-chorus (28 words, a repeat) and
re-render.**

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the dialogue lines (*"You ever been up a ferris wheel at night?"*, *"You two are a mess,"* *"So, what do you say?"*) and the question marks with them | Punctuation is not sung; a quoted phrase can be read as a break in the line |
| Descriptive tag lines — `[chorus – the drop, full supersaws, hands up]`, `[post-chorus – the yes chant]`, `[instrumental – the drop extended, DJ section]`, `[verse 3 – male pop-rap feature (Singer B)]`, `[bridge – pad, piano, near-spoken]` — reduced to plain tags | The model only knows the eight plain section tags; text on a tag line is dropped |
| `[verse 1]` / `[verse 2]` / `[verse 3]` → `[verse]`, `[final chorus]` → `[chorus]` | Same reason; the third verse being the male feature is carried by the caption's `Duet Structure`, not by a tag |
| The `(repeat)` under the second chorus written out in full | The verify script flags it and the model would sing the word |

The submission's lyric body already spelled its numbers as words (*three
a.m.*, *two percent*, *home by ten*), so no digit cleanup was needed — the
only digits in the file are in the prose scene direction.

Kept exactly as written: every lyric line, 124 BPM, B major, the
instrumentation, the mood arc, the six viral moments. No trimming was
needed — 758 words fits the uptempo budget.

## The story and the hooks

She is the girl with the plan, the list and the alarm, and a ride home
booked before she sits down. He is the one who suggests things. One drink,
home by ten — then a menu dare, a karaoke bar with a bad crowd, a fair as it
is closing, the top of the wheel where the whole city goes still, a three
a.m. diner with syrup on his sleeve and her heels under the seat. The male
feature answers from the sunrise car park with the rest of the list:
rooftop, bakery, a bench with their name on it, and one more ask. Then the
bridge lands the realisation — it was never the wheel, the song or the
syrup. Every yes she said all night was a yes to him.

**The hook:** *"Tonight I'm saying yes to everything."*

**The line for captions:** *"No to the plan, no to the clock, no to the
ten."*

**The rap clip:** *"You said one drink, that was six hours back / Heels in
my hand, head on my jacket, that's facts."*

**The turn:** *"Every yes I said was a yes to you, / So go on, ask me."*

**The chant:** the post-chorus — *"Yes, yes, yes, yes, say it again"* — is a
ready-made jump-cut structure, one yes per location.

**Why it can travel:** it is a night that keeps opening another door, and
the chant gives editors a beat to cut on. Everyone has a friend who plans
everything, and this is the night she stopped.

## Lyrics as they will be sung

```
[intro]
Seven o'clock, I told my girls I'd be home by ten,
Told myself, one drink, then leave.
You said, you ever been up a ferris wheel at night,
And I heard my own mouth go, yeah, why not, let's see.

[verse]
I'm the girl with the plan, with the list, with the alarm,
Ride booked home before I even sit down.
You ordered the thing on the menu that I couldn't say,
Then you dared me to try it, and I didn't back down.
Now there's a cab outside and the meter's running slow,
And you said, there's a bar with a mic and a bad crowd.
Every sensible cell in my body said no,
But the word that came out of me was pretty loud.

[pre-chorus]
Okay, okay, I know how this goes,
I'm the one who says maybe, I'm the one who says no.
But you've got a grin like you already know,
And I'm so tired of maybe, so here we go.

[chorus]
Tonight I'm saying yes to everything,
Yes to the wheel, yes to the lights, yes to the spin.
Yes to the mic, yes to the song I don't know,
Yes to the worst idea you've got, let's go.
Tonight I'm saying yes to everything,
No to the plan, no to the clock, no to the ten.
Ask me again, ask me anything,
Tonight I'm saying yes, yes, yes to everything.

[post-chorus]
Yes, yes, yes, yes, say it again,
Yes, yes, yes, yes, where have you been,
Yes, yes, yes, yes, to everything,
Ask me, ask me, yes to everything.

[verse]
You picked the worst song on the whole machine,
I knew half the words and the bar knew the rest.
We ran for the gate when the fair was closing,
The guy in the booth just laughed, said, you two are a mess.
Top of the wheel, the whole city went still,
You said, don't look down, so I looked at you instead.
Three a.m. diner, a stack I didn't need,
Syrup on your sleeve and my heels under the seat.

[pre-chorus]
Okay, okay, I know how this goes,
I had a curfew, I had a cab, I had a no.
But my phone's at two percent and I don't even know
What time it is, and I don't wanna know, so here we go.

[chorus]
Tonight I'm saying yes to everything,
Yes to the wheel, yes to the lights, yes to the spin.
Yes to the mic, yes to the song I don't know,
Yes to the worst idea you've got, let's go.
Tonight I'm saying yes to everything,
No to the plan, no to the clock, no to the ten.
Ask me again, ask me anything,
Tonight I'm saying yes, yes, yes to everything.

[instrumental]

[verse]
Look, I got a list and we ain't even halfway,
Rooftop, sunrise, a bakery that opens by five, hey.
There's a bridge with a view and a bench with our name on it,
No name yet, give me a week and a pen and I'll claim it.
You said one drink, that was six hours back,
Heels in my hand, head on my jacket, that's facts.
I know you've got rules, I know you've got a plan,
But you laughed at the top of that wheel and I'm a fan.
So one more yes, that's all I'm asking, one more,
Say yes to the second date, I'll be at your door.

[bridge]
Sun coming up on the fairground lot,
The wheel's gone dark and the diner's closed.
I said yes all night to the dumb stuff,
And it took me till sunrise to know
That it wasn't the wheel, it wasn't the song,
It wasn't the syrup at three.
Every yes I said was a yes to you,
So go on, ask me.

[chorus]
Tonight I'm saying yes to everything,
Yes to the wheel, yes to the lights, yes to the spin.
Yes to the mic, yes to the song I don't know,
Yes to the worst idea you've got, let's go.
And I'm saying yes to the second date,
Yes to the third, and no, I don't wanna wait.
Ask me again, ask me anything,
Tonight I'm saying yes, yes, yes to everything.

[post-chorus]
Yes, yes, yes, yes, say it again,
Yes, yes, yes, yes, where have you been,
Yes, yes, yes, yes, to everything,
Ask me, ask me, yes to everything.

[outro]
Ten o'clock came and went, and I'm still here,
Phone's dead, feet hurt, I'm not going anywhere.
You said, so, what do you say,
I said, what do you think, yes, yes, yes.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 758 at 140 wpm → ~5.4 min, 90% of frame cap (see the pacing table above) |
| Caption + lyrics tokens | 2919 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Mahima's `Vocal Details` lines / `Sonics` vs song 1 | present verbatim / byte-identical |
