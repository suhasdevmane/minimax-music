# I'll Be There in Every Tomorrow

**Status: written and verified, rendering overnight. Not yet rendered.**

Song 105, the closing song of the family set. A male lead, **Kai**, sings to
his daughter **Ellie** across her whole life: a first heartbeat, a newborn in
his arms, the early years, the grown woman leaving home, the wedding. Orchestral
ballad finale, 74 BPM, E-flat major. Voice lock byte-identical to song 101.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction, as the improved draft.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics: intro, verse, chorus, verse, pre-chorus, chorus, bridge, chorus, outro. 108 sung lines, 633 sung words. No `render.json`: this is a ballad under the 117 BPM line. |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 101 — the voice lock. 74 BPM, E-flat major, the orchestral arrangement per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 108 entries — plus a three-age Kai bible, three Ellie looks, workflow, edit notes and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 105-ill-be-there-in-every-tomorrow
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\105-ill-be-there-in-every-tomorrow\caption.txt `
  --lyrics-file songs\105-ill-be-there-in-every-tomorrow\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\105-ill-be-there-in-every-tomorrow\output\ill_be_there_in_every_tomorrow.wav
```

## What changed from the submission

| Change | Why |
|---|---|
| Sung length | Fitted to the ballad budget of 600 to 640 sung words (633 here); a finale longer than that would rush the model |
| Kept: the promise, the chorus, the bridge's answered-prayer image | They carry the song; everything else is built around them |
| The second memories verse is cut | It repeated the arrival in other words; the grown-daughter verse moves the story forward |
| One repeated chorus is cut | Three full choruses already carry the promise; the length went to the verses |
| Repeats written out in full | The model sings the body literally; `(repeat)` would be sung |
| Section tags reduced to plain tags | Only the eight tags the engine accepts, each alone on its line |
| No quotation marks, em-dashes or digits | The model sings digits unpredictably; numbers are spelled out in words |

Result: 633 sung words, inside the 600–640 budget, at 116 wpm about 5.5 minutes.

## The story and the hooks

A father sings to his daughter from the day she is born to the day she marries.
He starts in a hospital corridor with a first heartbeat he cannot yet hear,
holds her in the delivery room, watches her go to school, lets her leave for
university without stopping her, and walks her to her wedding with silver in
his hair. The song never asks her to stay: it promises he will be there when
she needs him.

**The hook:** *"I'll be there in every tomorrow"* — the title line, sung in
the first chorus and again at the close.

**The line for captions:** *"I cannot promise perfect days, but I can promise you my love will always keep you warm."*

**The turn:** *"My answered prayer come true"* — the bridge's image, the moment the
song stops promising and starts to give thanks.

**Why it can travel:** it is a promise any parent, child or friend can say out
loud. It needs no story to land, and it ends on the first frame it began with.

## Lyrics as they will be sung

```
[intro]
I remember your first heartbeat
Before I knew your face,
A tiny promise growing
In a quiet, sacred place.

[verse]
I wondered who you'd become one day,
What dreams would fill your eyes,
But nothing could prepare me
For the moment you arrived.
They placed you in my waiting arms,
So fragile, warm and new,
The world became a different world
The moment I saw you.
I held my breath and whispered,
I will give you all I can,
And in that very instant, girl,
I became a better man.

[chorus]
I'll be there in every tomorrow,
In the sunshine and the rain.
I'll be there through every victory,
And beside you through the pain.
When you're dancing through your happiest days,
When you're searching for the way,
My love will be a steady light
That never fades away.
You are the dream I never knew
My heart was waiting for,
My precious little daughter,
You are what I'm living for.
And though the years may carry you
To places far from home,
You'll never face this life alone,
You'll never face it alone.

[verse]
When you grow into a young woman
With a world beneath your feet,
When you find the dreams you're meant to chase
And people you will meet,
I won't hold you back from flying,
I won't ask you not to go,
I'll be proud of every distance
That your brave heart dares to know.
But if a dream should break apart,
If someone makes you cry,
If you feel the road is empty
And the stars forget to shine,
You can call the name of Daddy,
And I'll answer where I am,
No matter how old you become,
You'll always be my child.

[pre-chorus]
I cannot promise perfect days,
Or shelter from the storm,
But I can promise you my love
Will always keep you warm.

[chorus]
I'll be there in every tomorrow,
In the sunshine and the rain.
I'll be there through every victory,
And beside you through the pain.
When you're dancing through your happiest days,
When you're searching for the way,
My love will be a steady light
That never fades away.
You are the dream I never knew
My heart was waiting for,
My precious little daughter,
You are what I'm living for.
And though the years may carry you
To places far from home,
You'll never face this life alone,
You'll never face it alone.

[bridge]
And when my hair is silver,
And my footsteps have grown slow,
I'll still see the little girl
Who taught my heart to glow.
I'll still hear your laughter
In the quiet of the night,
And every memory of you
Will make the darkness bright.
You gave me more than happiness,
You gave my life a name,
You took my fear and tiredness
And turned them into flame.
You are my greatest blessing,
My answered prayer come true,
There is no love in all this world
Like the love I have for you.

[chorus]
I'll be there in every tomorrow,
In the sunshine and the rain.
I'll be there through every victory,
And beside you through the pain.
When you're dancing through your happiest days,
When you're searching for the way,
My love will be a steady light
That never fades away.
You are the dream I never knew
My heart was waiting for,
My precious little daughter,
You are what I'm living for.
And though the years may carry you
To places far from home,
You'll never face this life alone,
You'll never face it alone.

[outro]
So close your eyes, my baby girl,
Let tomorrow softly start,
No matter where your journey goes,
You'll always own my heart.
I'll be there in every tomorrow,
As I have been from the start,
My daughter, my joy, my little one,
You are my forever heart.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 633 → ~5.5 min at 116 wpm, 91% of frame cap (8185 of 9000 frames) |
| Caption + lyrics tokens | 1696 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Sonics` vs song 101 | byte-identical |
| `Vocal Details` vs song 101 | all four reference lines present verbatim |
| `[instrumental]` tag | none: the song runs straight through with no lyric-free section |
