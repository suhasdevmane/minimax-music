# That Summer Song

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song sixty-seven. Female lead **Mahima**, nostalgia pop with bright chorused
guitars, claps and wide synth pads, 110 BPM, C major, US register. Same
singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 636 sung words, mid-tempo budget, no `render.json` |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 110 BPM, C major, the guitar-and-claps arrangement, the fluorescent-hum and trolley-wheel textures, and the one silent bar inside the instrumental. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 73 entries — with a two-look character bible, Kai as the present-day partner, a faceless ex, the freezer-glass reflection plate, workflow, the aisle-freeze challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 67-that-summer-song
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\67-that-summer-song\caption.txt `
  --lyrics-file songs\67-that-summer-song\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\67-that-summer-song\output\that_summer_song.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed | Punctuation is not sung; the model reads the body literally |
| Digits spelled out — *quarter past nine*, *thirty dollars*, *eleven songs*, *nineteen*, *ten* | The model sings digits unpredictably |
| Descriptive tag lines (`[verse 1 — warm, the borrowed car]`, `[bridge — half-time…]`) reduced to plain `[verse]`, `[bridge]` | Only the documented plain tags exist; text on a tag line is dropped |
| Every repeated chorus written out in full, and the final chorus given its own varied last four lines | The model would sing a `(repeat)` marker, and the varied final chorus is where the story resolves |
| The instrumental placed after the second chorus, before the bridge | The shot list needs the no-lyrics stretch for the empty-shop sequence |

Kept exactly as written: the hook, 110 BPM, C major, the arrangement list,
the mood arc and every image in the submission.

## The story and the hooks

She is in a supermarket freezer aisle at nine at night with a bag of ice
going soft in her hand when four chords come down through the ceiling
speaker, and the floor turns into sand. One summer, one borrowed car with
thirty dollars in it and a disc jammed in the player, blue slush and
sunscreen on the seatbelt, a boy whose mouth she learned the words from.
Now there is a good man in the parking lot with her keys, texting his
mother, who would not know this song if it played all night. She scrolled
past the ex's wedding last autumn and slept fine. She has skipped this song
for years; tonight she stands in the freezer light and lets it finish, and
nothing breaks. The turn is that the girl she has been missing is not
missing — she is the one holding the basket.

**The hook:** *"They're playing that summer song and I'm right back there."*

**The line for captions:** *"I don't want you back, I want the girl who
thought a song could hold the world."*

**The knife line:** *"Funny how a chorus knows where to find me, right
between the frozen peas and the wine."*

**The turn:** *"It was never your song, it was never even ours / It was cheap
gas, long light, the girl I used to be."*

**Why it can travel:** everybody has one of these songs and a shop it
ambushed them in. The video's freezer-glass double reflection is a single
shareable frame, and the aisle-freeze challenge writes itself.

## Lyrics as they will be sung

```
[intro]
Aisle five, quarter past nine,
A bag of ice going soft in my hand,
Four chords come down through the ceiling,
And the cold floor turns into sand.

[verse]
That June we had a borrowed car and thirty dollars,
No air conditioning, so we rode with the windows down.
One disc stuck in the player since the winter before,
Same eleven songs carried us out of that town.
You knew the second verse before the radio did,
I learned it off your mouth at dusk.
Blue slush on our teeth, sunscreen on the seatbelt,
A whole July that nobody could rush.

[pre-chorus]
Somebody's cart, somebody's kid asking for cereal,
A green apron stacking bags of ice.
I could pay and walk out to the lot,
But I stand in the cold and I don't think twice.

[chorus]
They're playing that summer song and I'm right back there,
Salt on the dashboard, wind doing what it wants with my hair,
Same cheap speakers, same wound-down glass,
Same three long minutes we thought would last.
Half of me is holding a basket in the light,
Half of me is nineteen and out of my mind,
I don't want you back, I want the girl
Who thought a song could hold the world.

[verse]
A good man's in the lot with my keys in his hand,
Texting his mother, warm, and nothing at all like you.
He wouldn't know this song if it played all night,
And I love that about him, and it stings a little too.
Somebody posted your wedding last fall and I scrolled it,
Tapped a heart with my thumb and I slept fine.
Funny how a chorus knows where to find me,
Right between the frozen peas and the wine.

[pre-chorus]
The ice is going soft and there's water on my sleeve,
The girl in the green apron says the doors close at ten.
A whole life waiting under the streetlight,
And I'm standing in this aisle being nineteen again.

[chorus]
They're playing that summer song and I'm right back there,
Salt on the dashboard, wind doing what it wants with my hair,
Same cheap speakers, same wound-down glass,
Same three long minutes we thought would last.
Half of me is holding a basket in the light,
Half of me is nineteen and out of my mind,
I don't want you back, I want the girl
Who thought a song could hold the world.

[instrumental]

[bridge]
For years I skipped it, thumb on the button before the drums,
Changed the station, left the room, walked out.
Tonight I stood in the freezer light and let it finish,
And nothing broke, and the ice machine hummed some more.
It was never your song, it was never even ours,
It was cheap gas, long light, the girl I used to be,
And she's not gone, she's only quieter now,
She's out in the lot with a good man, waiting on me.

[chorus]
They're playing that summer song and I'm right back there,
Salt on the dashboard, wind doing what it wants with my hair,
Same cheap speakers, same wound-down glass,
Same three long minutes we thought would last.
All of me is standing in the freezer light,
And the girl I've been missing has been here the whole time,
I don't want you back, I have got the girl
Who thought a song could hold the world.

[post-chorus]
Turn it up, turn it up over the frozen aisles,
Let it play, let it play to the end of the line,
I'm not sad, I'm not sorry, I'm standing here
With one whole summer of mine.

[outro]
Out through the doors with a paper bag on my arm,
Humming the second verse under the lot lights,
He asks what took so long, I tell him nothing much,
Just a song I used to know, and I get in.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 636 → ~5.5 min at 116 wpm, 91% of frame cap |
| Caption + lyrics tokens | 2101 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
