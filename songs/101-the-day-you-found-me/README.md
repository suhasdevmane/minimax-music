# The Day You Found Me

**Status: written and verified, rendering overnight. Not yet rendered.**

Song 101. Male lead, a father singing to his young daughter: the father is the
on-screen male lead **Kai**, and the daughter, about four, is **Ellie**, the
child who finds him. Acoustic folk-pop ballad at 72 BPM in G major. Warm and
heartfelt, never sentimental-sounding, never explicit. This song is the voice
reference for its family: its `Vocal Details` and `Sonics` blocks are the lock
that other songs in the family are checked against.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted, before the improved
version.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics: the improved version, trimmed to the 600–640 sung-word ballad budget |
| [`caption.txt`](caption.txt) | Music description. 72 BPM, G major, fingerpicked guitar and upright piano, the `Vocal Details` and `Sonics` blocks as the voice lock. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 76 numbered shots, plus 5 unnumbered instrumental shots — with the Kai and Ellie character bible, workflow, edit notes and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 101-the-day-you-found-me
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\101-the-day-you-found-me\caption.txt `
  --lyrics-file songs\101-the-day-you-found-me\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\101-the-day-you-found-me\output\the_day_you_found_me.wav
```

No `render.json` is needed: the song sets its own pace at the default ballad
rate of 116 wpm.

## What changed from the submission

| Change | Why |
|---|---|
| Sung length | Fitted to the ballad budget of 600 to 640 sung words, keeping the theme and the central images |
| Repeated sections written out in full | The model sings the lyric body literally and cannot read "(repeat)" |
| One bridge line rewritten to avoid a forced rhyme | Meaning outranks the rhyme; a slant rhyme carries it instead |
| One line added to the outro | The outro needed a final line that lands the father's promise to the child |


## The story and the hooks

A father has been getting by on quiet and endurance. One ordinary morning,
before the light is up, his four-year-old daughter comes running down a cold
hallway in her bare feet and climbs onto the kitchen counter, telling him it
is going to be a good one. She gives him a crayon drawing of their house with
seven windows and a yellow sun, and he folds it into his coat and carries it
through the whole hard day. The song is his admission that the thing he thought
he was doing for her, she was doing for him. He is not going back to the place
he was, because she keeps saying his name.

**The hook:** *"Everybody thinks I saved you, but I've got it upside down."*
The chorus turns the usual story round, in one line.

**The line for captions:** *"You found me in the hallway, and you don't even know."*

**The turn:** *"Then you found me in the hallway, and you find me every day."*
The final chorus states the reversal in the present tense.

**Why it can travel:** it is a domestic picture every parent recognises, the
kitchen before school, a child's drawing in a pocket, and it resolves in the
simplest possible image: a kettle, grey light, a child walking in.

## Lyrics as they will be sung

```
[intro]
The kettle clicks at ten past six,
The window's holding grey,
I'm counting up the things to fix
Before I drive away.

[verse]
I used to carry mornings like a crate I couldn't set down,
Keys in one hand, trouble in the other, both my shoulders down.
I kept a running total of the ways I came up short,
And I called that being careful, and I called that being tough.
Then a door came open slowly at the far end of the hall,
And two bare feet went running on a floor that's always cold.
You had your hair gone sideways and one sock up to your knee,
And you asked me if the morning had a plan for you and me.
You climbed up on the counter where you're never let to climb,
And you told me it was going to be a good one, this time.

[pre-chorus]
I had been hunting for my reasons
In the hardest hour of day,
Then a small voice in a doorway
Took the heavy part away.

[chorus]
Everybody thinks I saved you,
But I've got it upside down.
I was the one who went missing,
Standing right here, not around.
I was tired and I was quiet
And I called it getting by,
Till you found me in the hallway
At ten past six one day.

[verse]
You drew a house with seven windows and a door too small to use,
And a yellow sun above the roof the sky could never lose.
You gave the clouds a purple edge, you put a fence around the lawn,
And a man beside a little girl, and the man was holding on.
You held it up and waited there and watched me while I read,
And you said that I could keep it if I kept it by my bed.
So I folded up your masterpiece and slid it in my coat,
And it rode there through the whole long day, a small and folded note.
Nobody in that building knew the reason I could stand,
There was paper in my pocket with a sun you drew by hand.

[pre-chorus]
I had been hunting for my reasons
In the hardest hour of day,
Then a small voice in a doorway
Took the heavy part away.

[chorus]
Everybody thinks I saved you,
But I've got it upside down.
I was the one who went missing,
Standing right here, not around.
I was tired and I was quiet
And I called it getting by,
Till you found me in the hallway
At ten past six one day.

[instrumental]

[bridge]
One day this hall will be a city
And the door you open, yours alone,
And the feet that came out running to me
Will be running down a road of your own.
I'll be glad. I'll carry boxes.
I'll stand waving at the kerb.
And I'll keep a folded drawing
In my coat, the way I learned.
You won't know you ever did it,
You'll just think you grew up fine.

[chorus]
Everybody thinks I saved you,
But I've got it upside down.
You're the one who came and got me,
You're the reason I'm around.
I was tired and I was quiet
And I called it getting by,
Then you found me in the hallway,
And you find me every day.

[post-chorus]
Ten past six, the kettle clicking,
Grey light coming through the floor,
You found me in the hallway
And you don't even know.

[outro]
So sleep now, there's no hurry,
Let the morning do the rest.
You found a man who'd gone missing
And you walked him to the step.
And he isn't going back there,
Not while you still say his name.
```

## Budget (verified)

Produced by `scripts/verify_lyrics.py songs/101-the-day-you-found-me --voice-ref songs/101-the-day-you-found-me`.

| Check | Result |
|---|---|
| Sung words | 610 → ~316 s (5.3 min) at 116 wpm, 7888 of 9000 frames, 88% of frame cap |
| Caption + lyrics tokens | 2010 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| Voice lock: `Sonics` | byte-identical to song 101 (this song is the reference for its family) |
| Voice lock: `Vocal Details` | all reference lines present verbatim |
| Result | PASS |
