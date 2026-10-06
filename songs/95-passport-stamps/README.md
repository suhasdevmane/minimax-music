# Passport Stamps

**Status: written and verified, NOT rendered. Not yet in the queue.**

Ninety-fifth song. Female lead **Mahima**, global pop with real world
percussion, travel, US register. 116 BPM, G major, no modulation — the final
chorus widens and swaps the city names in the hook. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission cleaned for the engine and revised at five points (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 116 BPM, G major, nylon-string guitar, djembe and congas, bright synths, and the concourse hum, departure chime and passport-stamp ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 74 entries — built from the submission's scene direction, plus a three-look character bible, Kai as the only recurring face, one fixed light per city, the every-third-cut-is-a-face rule, workflow, the stamp challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json` — 116 BPM sits at the top of the mid band, one below the
uptempo threshold, so the 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 95-passport-stamps
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\95-passport-stamps\caption.txt `
  --lyrics-file songs\95-passport-stamps\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\95-passport-stamps\output\passport_stamps.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech in the first pre-chorus | Punctuation is not sung |
| Descriptive tag lines reduced to plain tags; `[final chorus]` → `[chorus]`; every repeated chorus and pre-chorus written out in full | Only the checkpoint's documented tags exist, and the model would sing the word repeat |
| The intro's last two lines rewritten | Craft pass: *"doesn't look up"* rhymed with *"I showed up"*, which is an identity rhyme on the same word — the one rhyme rule with no exceptions. Now *"never asks me my name"* / *"that says I came"*, a clean rhyme, and it sets up a better payoff |
| The outro's last two lines rewritten to match | The outro repeated the same self-rhyme. *"This time knows my name"* now answers *"never asks me my name"* from the intro: the officer who processed her a year ago recognises her. Same word count, stronger bookend |
| `a grandmother's hands` → `a stranger's hands` in verse one | Originality: songs 59 and 65 both build on a grandmother's hands in a kitchen, and a third use would read as a house habit. A stranger feeding her like family is the sharper version of the line anyway, and it ties into the strangers who stamp the book in the intro and the outro |
| `Coffee in a paper cup` → `Boarding pass in my teeth` in the intro | Originality: songs 45 and 88 both open a line with *coffee in a paper cup*; a third would be a house tic. The replacement is more specific to a departures queue and costs the same nine words |
| The pre-chorus refrain *"I'm not running from anything, I'm running straight to it"* → *"Nothing's chasing me out, I'm chasing every bit of it"* | Originality: song 45 has *"I'm not running from anything, I'm running with the light"*. This song repeats its version twice as a refrain, which makes the collision audible. The replacement keeps the thesis — not fleeing, pursuing — the same word count and the same consonance against *the point* |

Kept exactly as written: the pre-chorus opening couplets and the *nobody
comes back the same* line, all four choruses, verse two, the bridge, the
post-chorus, 116 BPM, G major, the instrumentation and the mood arc. 640
words before and after — every change was word-for-word balanced to hold the
top of the budget.

## The story and the hooks

An airport before sunrise, a stamp coming down, an officer who does not ask
her name. Lisbon was a girl with paint under her nails who taught her how to
fail. Tokyo was a boy at a vending machine and two hot cans and no words.
Oaxaca was a kitchen where a stranger fed her like family in a language she
did not have. Her mother keeps asking when she is going to settle down, and
she keeps saying she is settled, just in a lot of towns. Then Berlin,
Marrakech and two stamps side by side in Istanbul — the same person, three
times — until he flies home in March and she flies on to Peru, cries at the
gate and then laughs at herself. In the bridge there is a shoebox under a
bed at her mother's house with the old full passport in it, and she finally
answers the question: home was never a country.

**The hook:** *"Passport stamps and a heart full of places"* — the title
opens the chorus, opens its second half, and closes it, and the last chorus
swaps the cities in it for the ones the song has since earned.

**The line for captions:** *"I don't count countries, I count who I met."*

**The turn:** *"Home was never a country, it was never a street, / Home is
every person who walked a mile with me."*

**The quote:** *"Some people are a chapter and some are just a line, but
every single one of them is written down my spine."*

**Why it can travel:** it is a travel song that refuses the escapist reading
out loud — *"Nothing's chasing me out, I'm chasing every bit of it"* —
and it gives the edit a percussion instrument, the stamp, that lands on
every downbeat of the post-chorus. The challenge films itself out of one
passport.

## Lyrics as they will be sung

```
[intro]
Ink on the page and an airport at dawn,
Boarding pass in my teeth, half my sleep gone.
A stranger stamps the book, never asks me my name,
One more little square that says I came.

[verse]
Lisbon was a girl with paint under her nails,
Yellow tram at midnight, she taught me how to fail.
Tokyo was a boy by a vending machine,
Two cans of hot coffee, no words in between.
Oaxaca was a kitchen and a stranger's hands,
Feeding me like family in words I couldn't understand.
Every border I crossed, somebody crossed it with me,
I carry all of them like ink you can't see.

[pre-chorus]
My mom keeps asking when I'm gonna settle down,
I said, mama, I'm settled, just in a lot of towns.
Nothing's chasing me out, I'm chasing every bit of it,
Nobody comes back the same, and that's the point.

[chorus]
Passport stamps and a heart full of places,
Every page is a name, every name has a face.
Lisbon in my laugh and Tokyo in my walk,
A little Oaxaca in the way that I talk.
Passport stamps and a heart full of places,
I don't count countries, I count who I met.
Everywhere I land, I leave a piece, take one,
Passport stamps and a heart full of places, I've only just begun.

[verse]
Berlin was a bass line in a basement till four,
Marrakech was the same boy waiting at my door.
We got two stamps side by side in Istanbul,
Window seat and aisle seat, and that was beautiful.
Then he flew home in March and I flew on to Peru,
Cried at the gate, then laughed, cause that's what I do.
Some people are a chapter and some are just a line,
But every single one of them is written down my spine.

[pre-chorus]
Sometimes it's Tuesday and I wake up in a bed,
Don't know the city, or the language in my head.
Nothing's chasing me out, I'm chasing every bit of it,
Nobody comes back the same, and that's the point.

[chorus]
Passport stamps and a heart full of places,
Every page is a name, every name has a face.
Lisbon in my laugh and Tokyo in my walk,
A little Oaxaca in the way that I talk.
Passport stamps and a heart full of places,
I don't count countries, I count who I met.
Everywhere I land, I leave a piece, take one,
Passport stamps and a heart full of places, I've only just begun.

[instrumental]

[bridge]
There's a shoebox under my bed at mama's house,
Boarding passes, ticket stubs, a napkin with a map drawn out.
The old book ran out of pages, they gave me a new one,
But the first one stays in the box, cause that's where I come from.
Home was never a country, it was never a street,
Home is every person who walked a mile with me.
When they ask me where I'm from, I say it's complicated,
I'm from everywhere I've loved and everyone who waited.

[chorus]
Passport stamps and a heart full of places,
Every page is a name, every name has a face.
Berlin in my hips and Istanbul in my eyes,
A little bit of Peru in the way I say goodbye.
Passport stamps and a heart full of places,
I don't count countries, I count who I met.
Everywhere I land, I leave a piece, take one,
Passport stamps and a heart full of places, I've only just begun.

[post-chorus]
Stamp it, one more page,
Every face is a place I'd never trade.
Stamp it, one more page,
Heart full of places, I'm on my way.

[outro]
Ink on the page and an airport at dawn,
Somebody new in the seat where you were gone.
The stranger stamps the book and this time knows my name,
And I smile, cause I came.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2239 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
