# Your Little Book of Life

**Status: written and verified, rendering overnight. Not yet rendered.**

Song 103. Male lead **Kai** (a father, late thirties, warm baritone), gentle folk-pop, a child's everyday wonder, 76 BPM, C major. Single male lead with a low male harmony; no duet.

Source of record: [`source/original-submission.md`](source/original-submission.md) — the song and its scene-by-scene direction, as submitted and improved.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics, 104 sung lines, 631 sung words, no trimming needed beyond the cleanup below |
| [`caption.txt`](caption.txt) | Music description at 76 BPM, C major. `Vocal Details` and `Sonics` byte-identical to song 101 — the voice lock. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 104 entries, numbered 1–104 in lyric order, plus a Kai and Ellie character bible, Wan 2.2 workflow, edit markers and QC checklist. No instrumental shots: the song has no `[instrumental]` tag. |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 103-your-little-book-of-life
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\103-your-little-book-of-life\caption.txt `
  --lyrics-file songs\103-your-little-book-of-life\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\103-your-little-book-of-life\output\your_little_book_of_life.wav
```

## What changed from the submission

| Change | Why |
|---|---|
| Sung length | Fitted to the ballad budget of 600 to 640 sung words, so the song finishes inside the frame cap |
| This version keeps every theme and image and fits the 600–640 sung-word budget | Length came from trimming repeated phrasing, not from cutting the story: the ladybug, the spoon microphone, the blanket fort, the book and the rainbow all stay |
| Repeats written out | The chorus is sung in full four times, so the lyric body carries every repeat literally, as the model sings it |
| Bridge closing | The bridge ends on its plainest line, so the final chorus opens on the song's central image |
| Quotation marks and em-dashes removed; section tags reduced to plain tags | The model sings the lyric body literally and only knows plain section tags |

## The story and the hooks

A father sings to his four-year-old daughter about the small things she does
each day that he would otherwise walk past: a ladybug on a garden wall, a
biscuit shared with it, a spoon held up as a microphone, a blanket fort with
a sign that says knock. He has started to think of her days as a book she is
writing, and he is the reader who keeps every page. The bridge turns to the
pages still to come and the shelf of drawings he keeps, and the final chorus
ends on a rainbow in his heart. The outro goes quiet on the sofa, with her
asleep and the father saying the last line.

**The hook:** *"You're writing your own little book of life."* — the title, sung on the first beat of every chorus.

**The line for captions:** *"Sometimes it's just a blanket fort at the ending of the day."*

**The turn:** *"I learned that joy is not a treasure / Hidden far away"* — the verse where the father stops looking for joy somewhere else.

**Why it can travel:** every parent recognises the moment a child finds something ordinary and makes it a celebration, and the song is about noticing it. It is sung plainly, with no villain and no grief, so it works as a gift to share.

## Lyrics as they will be sung

```
[intro]
Today you found a ladybug
Beside the garden wall,
You watched it climb a blade of grass
And wondered if it'd fall.

[verse]
You gave it half a biscuit,
You gave it room to fly,
Then waved until it disappeared
Like a plane across the sky.
Yesterday you wore your shoes
Upon the wrong two feet,
You marched around the kitchen
To your own imaginary beat.
You called the spoon a microphone,
The blanket was a train,
And suddenly our little home
Was full of sun again.

[chorus]
You're writing your own little book of life,
With every laugh and every surprise.
Every new question, every new day,
You paint a thousand colours my way.
You're my sunrise, my morning light,
The reason my tired heart feels alive.
My beautiful girl, wherever you go,
You make the whole world brighter than you know.

[verse]
You built a castle out of pillows,
A kingdom on the floor,
You pinned a sign upon the chair,
Daddy, knock before the door.
I bowed before the princess
And asked if I could stay,
You said, only if you promise
To be silly every day.
So I became a dancing bear,
A dragon and a king,
And you laughed until your little cheeks
Were brighter than the spring.
I learned that joy is not a treasure
Hidden far away,
Sometimes it's just a blanket fort
At the ending of the day.

[chorus]
You're writing your own little book of life,
With every laugh and every surprise.
Every new question, every new day,
You paint a thousand colours my way.
You're my sunrise, my morning light,
The reason my tired heart feels alive.
My beautiful girl, wherever you go,
You make the whole world brighter than you know.

[verse]
You learned to say the names of things,
Then changed them just for fun.
The fridge became a mountain,
The ceiling was the sun.
You gave a name to every cloud
And every passing plane,
You made a friend of every sound,
The thunder, wind and rain.
You make a celebration
From the smallest thing you find,
A pebble can be precious,
A puddle can be kind.
You show me that the world is new
When seen through loving eyes,
There are miracles in ordinary days
Beneath familiar skies.

[pre-chorus]
I used to chase tomorrow,
Always running toward the next,
You taught me how to hold the moment
And be thankful for the best.

[chorus]
You're writing your own little book of life,
With every laugh and every surprise.
Every new question, every new day,
You paint a thousand colours my way.
You're my sunrise, my morning light,
The reason my tired heart feels alive.
My beautiful girl, wherever you go,
You make the whole world brighter than you know.

[bridge]
One day you'll turn the pages
Far beyond the ones we know,
You'll write about your dreams
And the places you will go.
There may be roads I cannot follow,
There may be skies I cannot see,
But every chapter of your heart
Will always matter to me.
I'll keep the little memories,
Your drawings, words and shoes,
The tiny hands that held mine
When you had the world to choose.
And when you read the story
Of the girl you grew into,
I hope you see between the lines
How proud I am of you.

[chorus]
You're writing your own little book of life,
With every brave and beautiful line.
Every new dream, every new start,
You leave a rainbow in your father's heart.
You're my sunrise, my morning light,
The reason my tired heart feels alive.
My beautiful girl, wherever you go,
You make the whole world brighter than you know.

[outro]
So keep on dancing, keep on dreaming,
Keep your wonder shining through.
Life became a better story
The day it gave me you.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 631 → ~5.4 min at 116 wpm, 91% of frame cap (8159 / 9000 frames) |
| Caption + lyrics tokens | 1676 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 101 | byte-identical |
