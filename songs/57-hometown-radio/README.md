# Hometown Radio

**Status: written and verified, NOT rendered. Not yet in the queue.**

Fifty-seventh song. Female lead **Mahima**, country-pop with a modern rhythm
section, memories, US register. 96 BPM, G major lifting a whole step to A on
the final chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — the submission cleaned for the engine, extended by a third verse and revised at four points (see below) |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 96 BPM, G major with the whole-step lift, acoustic guitar, banjo-style plucks, pedal-steel, fiddle, family harmonies, and the car ambience, AM static and diner textures per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 81 entries — built from the submission's scene direction, plus a four-look character bible, a completely unseen ex, the one-way light schedule, the chorus-one to final-chorus location matches, workflow, the hometown challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

No `render.json` — 96 BPM is mid-pace and the 116 wpm default applies.

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 57-hometown-radio
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\57-hometown-radio\caption.txt `
  --lyrics-file songs\57-hometown-radio\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\57-hometown-radio\output\hometown_radio.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks removed from the reported speech in the intro, both verses and the outro | Punctuation is not sung |
| Descriptive tag lines reduced to plain tags; `[verse 3]` → `[verse]`; `[final chorus]` → `[chorus]`; every repeated chorus and pre-chorus written out in full | Only the checkpoint's documented tags exist, and the model would sing the word repeat |
| **A third verse added after the instrumental** | The submission came in at 576 sung words, twenty-four under the ballad floor. Rather than padding the existing sections, the arc gained the beat it was missing: she drives out to her mother's porch. It pays off *"Mama kept my room like I'd be back by June"* from verse one, and it hands the bridge its turn — the mother's aside, *"you can love a town and still drive on"*, is the thing the bridge then finishes. The verse is six lines in the same AABB couplets as verses one and two, and it develops rather than restates: a new place, a new person, and the one character in the song who never mentions him |
| Verse one, line two rewritten | Craft pass: *mine / them* was an orphan in a verse otherwise built entirely of couplets. Now *"but I know every line"* — same image, same word count, clean rhyme |
| Verse two, the last two lines rewritten | Craft pass: *winces / change* did not rhyme, and *loads our number* is not how anybody describes a jukebox. Now *"catches my eye"* / *"some things don't die"*, which keeps the friend's knowing beat and rhymes |
| Pre-chorus two, line three rewritten | Craft pass: *through / you / too* made three consecutive identical rhymes and left *door* orphaned, where pre-chorus one is a clean AABB. Now *"she turns the speaker up and she's out on the floor"* — it rhymes, and it gives the diner dance an action instead of a description |
| The outro's third line rewritten | Craft pass: *off / song* did not rhyme. *"I keep the window down and I sing along"* rhymes and closes the loop with the chorus's own *sing along* |
| The bridge's last line: `the girl I used to be` → `the kid it let me be` | Originality: songs 56 and 67 both close a nostalgic line on *the girl I used to be*, and a third would be a house habit. The replacement keeps the rhyme, and it hands the credit to the town rather than to her, which is what the bridge is arguing |

Kept exactly as written: the intro, both choruses one and two, the third
chorus, the bridge, the post-chorus, the rest of both verses, 96 BPM, G
major with the whole-step lift on *let it heal*, the instrumentation and the
mood arc. 576 words became 638.

## The story and the hooks

Two hours out the static clears and it is the same voice on the dial. The
water tower still has the initials, faded to a whisper. The Dairy Barn is a
vape shop, the church is untouched, the field where they parked has a
subdivision name, and her mother has kept her room like she would be back by
June. She swore she would just drive through — gas, a coffee, past you — and
then the dial lands on the opening chord and she is seventeen with her hand
out of the window. At the diner her old best friend comes out from behind
the counter, tells her he moved to Dallas and married a nurse, says it like
it is good news, and it is, and it is worse. Then she drives out to her
mother's porch, where nobody asks about him at all, and gets handed the
sentence that finishes the song. By the time the sun goes down behind the
silo she knows the song was never theirs.

**The hook:** *"Hometown radio still plays our song"* — the title opens and
closes every chorus, and by the final one the line around it has changed
from *let it hurt* to *let it heal*.

**The line for captions:** *"Everything changed and nothing did."*

**The turn:** *"Maybe it never was ours, maybe it was mine, / You were only
ever riding on the passenger side."*

**The quote:** *"This town didn't miss you, it kept the porch light on for
me."*

**The knife line:** *"Says it like it's good news, and it is, and it's
worse."*

**Why it can travel:** everybody has a station that never updated and a
building that used to be something else, the diner dance is a clip that
posts itself, and the resolution is about the town rather than about him —
she is not over the place, she is just done being hurt by it.

## Lyrics as they will be sung

```
[intro]
Two hours out and the static clears,
Same voice on the dial I haven't heard in years.
He says it's a warm one, folks, drive safe tonight,
And I roll the window down and let it back inside.

[verse]
Water tower's still got your letters and mine,
Faded to a whisper, but I know every line.
The Dairy Barn's a vape shop, the church is the same,
And the field where we parked has a subdivision name.
Mama kept my room like I'd be back by June,
Posters on the wall, glow stars, crooked moon.
Passed your old truck at the light on Main,
Different plates, but my chest didn't get the memo, same old lane.

[pre-chorus]
I swore to myself I'd just drive through,
Gas and a coffee and I'm past you.
But the dial lands right on that opening chord,
And I'm seventeen with my hand out the door.

[chorus]
Hometown radio still plays our song,
Like nobody told it that we moved on.
Every streetlight's humming the words we knew,
Every mile of this town is a mile of you.
Everything changed and nothing did,
I'm a grown woman feeling like a kid.
Turn it up, let it hurt, sing along,
Hometown radio still plays our song.

[verse]
Slid in the booth at the diner on Fifth,
Cracked red vinyl, sugar packets, the whole gift.
My old best friend behind the counter, she screams,
Says girl, you look expensive, but you still look sixteen.
She says he moved to Dallas, married a nurse,
Says it like it's good news, and it is, and it's worse.
Then that song comes on the speaker and she catches my eye,
Tops my coffee off and says, honey, some things don't die.

[pre-chorus]
I told her I'd only stop on through,
Hug and a refill and I'm past you.
But she turns the speaker up and she's out on the floor,
Two girls in a diner, seventeen, hands out the door.

[chorus]
Hometown radio still plays our song,
Like nobody told it that we moved on.
Every streetlight's humming the words we knew,
Every mile of this town is a mile of you.
Everything changed and nothing did,
I'm a grown woman feeling like a kid.
Turn it up, let it hurt, sing along,
Hometown radio still plays our song.

[instrumental]

[verse]
Drove out to Mama's the long way, took it slow,
Screen door, sweet tea, and the dog I used to know.
She didn't ask about him once, she asked about my week,
Asked about my sister, asked if I still eat.
She said, you can love a town and still drive on,
And she hummed the harmony to that same old song.

[bridge]
Sun going down behind the silo, gold,
The whole sky the color of a story I've told.
I'm parked in the lot with the engine still on,
Waiting on the second verse to come along.
Maybe it never was ours, maybe it was mine,
You were only ever riding on the passenger side.
This town didn't miss you, it kept the porch light on for me,
Water tower, diner, and the kid it let me be.

[chorus]
Hometown radio still plays our song,
And I'm finally okay that we moved on.
Every streetlight's humming the words I knew,
Every mile of this town is a mile I grew.
Everything changed and nothing did,
I'm a grown woman, still that kid.
Turn it up, let it heal, sing along,
Hometown radio still plays our song.

[post-chorus]
Same three chords, same four streets,
Same girl behind the wheel, different heartbeat.
Same three chords, same four streets,
Ooh, I'm home, I'm home, I'm home.

[outro]
Signal's fading out past the county sign,
DJ says goodnight, folks, says take your time.
I keep the window down and I sing along,
Hometown radio, still playing our song.
Still playing our song.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 638 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2306 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
