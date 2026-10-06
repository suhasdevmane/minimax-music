# Landing Gear

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song eighty-two. Female lead **Mahima**, widescreen pop with rock guitars,
long-distance reunion, US voice. 108 BPM, D major lifting a whole step to E
for the final chorus. Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
concept, sound direction and the scene-by-scene video notes as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 632 sung words, mid-tempo ballad budget, no trimming needed at render time |
| [`caption.txt`](caption.txt) | Music description. `Sonics` and the four `Vocal Details` lines byte-identical to song 1 — the voice lock. 108 BPM, D major with the modulation, two-guitar arrangement, and the cabin-air, seatbelt-chime and landing-gear textures written into the bed. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look character bible, Kai withheld until shot 58, the composited-signage rule, workflow, the dropped-bag challenge and a QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 82-landing-gear
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\82-landing-gear\caption.txt `
  --lyrics-file songs\82-landing-gear\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\82-landing-gear\output\landing_gear.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout the lyric body | Punctuation is not sung; the model renders the body literally |
| Digits spelled as words (*twenty-six A*, *eleven months*, *six thousand miles*, *four hours*, *twenty minutes*) | The model sings digits unpredictably |
| The descriptive tag lines (`[intro – pad, one piano note, cabin air]`, `[bridge – piano and voice, half-time]`, `[final chorus – modulated]`) reduced to plain `[intro]`, `[bridge]`, `[chorus]` | Only the checkpoint's plain section tags exist; anything else is dropped or sung |
| Both full choruses written out rather than marked as repeats | A `(repeat)` line would be sung |
| *Seatbelt sign* became *seatbelt light* and *practised* became *practiced* | US register, and the sung line scans a syllable better |

Kept exactly as written: the hook, the speech in the shoe, the gear dropping,
the tarmac wait, the run, the dropped bag, 108 BPM, D major with the lift, the
instrumentation and the mood arc. No trimming was needed — 632 words fits.

## The story and the hooks

Eleven months, one night flight, and ninety minutes of song. She is on the
plane, not at the gate: seat twenty-six A, a kid asleep two rows up, a man
watching something with the sound off, a speech she wrote on a receipt and
then hid in her shoe because she knows it will not survive the doors. Then the
descent, the city coming up like a spilled box of light, and the mechanical
thump under the floor that her body understands before she does. She lands.
The cabin claps. They sit on the tarmac for twenty more minutes, which is the
joke the song needed. Then a booth, a corridor, a moving walkway she refuses
to stand still on, and a set of frosted doors that keep opening for other
people. She stops once, dead centre of the hall, to say the truest thing in
the song out loud, and then she runs.

**The hook:** *"Landing gear down, my heart's coming home."*

**The line for captions:** *"I am done being good at missing you."*

**The knife line:** *"Nobody ever hugged a screen and got it back."*

**The turn:** *"I dropped the bag before I got to where you stood, and the
year hit the floor and it broke open good."*

**Why it can travel:** the arrivals-hall run is the most filmed thirty seconds
in ordinary life, and this is a song built to sit under everyone's shaky phone
footage of it. The gear-drop sound is a hook you can hear before the vocal
arrives.

## Lyrics as they will be sung

```
[intro]
Cabin lights came up on somewhere dark,
Four hours left on a little plastic map.
I have been counting this down since a January airport,
And the whole year folded into one gray seat.

[verse]
I know this row by heart, I have flown it in my head,
Twenty-six A, the wing, the same square of sky.
There's a kid asleep on his mother in the aisle,
And a man beside me watching something with the sound off.
I wrote you a speech on the back of a receipt,
Then I read it once and I put it in my shoe.
Because everything I practiced is going to leave my mouth
The second that those doors go the other way.

[pre-chorus]
The seatbelt light, the little chime, the tray table up,
The city coming up like a spilled box of light.
Something in the floor lets go and starts to lower,
And my whole body knows the sound before I do.

[chorus]
Landing gear down, my heart's coming home,
Eleven months of nothing but a voice on a phone.
Six thousand miles folding into one hallway,
And you at the end of it and nothing in the way.
I have been up here so long I forgot the ground,
Now the wheels find the runway and the year comes down.
Pull the window shade up, let the morning come on,
Landing gear down, my heart's coming home.

[verse]
We touched and the whole cabin clapped like we had done it,
Then we sat on the tarmac for another twenty minutes.
The aisle stood up too early like the aisle always does,
And for once I was standing with them, bag against my chest.
A booth, a nod, a corridor with nothing on the walls,
A moving floor that I refuse to stand still on.
There's a woman with a placard and a driver on his phone,
And the frosted doors keep opening for other people.

[pre-chorus]
The strap in my fist, the escalator taking its time,
A sign says arrivals like it is a normal word.
Somebody hugs somebody just ahead of me,
And I am running before I decide to run.

[chorus]
Landing gear down, my heart's coming home,
Eleven months of nothing but a voice on a phone.
Six thousand miles folding into one hallway,
And you at the end of it and nothing in the way.
I have been up here so long I forgot the ground,
Now the wheels find the runway and the year comes down.
Pull the window shade up, let the morning come on,
Landing gear down, my heart's coming home.

[instrumental]

[bridge]
We did it well, we did the calls, we did the time,
We split the difference on the hours and the sleep.
I learned your weather and you learned mine,
I fell asleep to your morning more nights than I can count.
But nobody ever hugged a screen and got it back,
And I am done being good at missing you.

[chorus]
Landing gear down, my heart's coming home,
No more goodnight at the wrong end of a phone.
Six thousand miles folding into one hallway,
And your arms in the doorway and nothing in the way.
I dropped the bag before I got to where you stood,
And the year hit the floor and it broke open good.
Pull the window shade up, let the morning come on,
Landing gear down, my heart's coming home.

[post-chorus]
Coming home, coming home,
Feet on the floor and I'm not on my own.
Coming home, coming home,
Every mile I flew was a mile of the way home.

[outro]
Somewhere over the ocean I stopped being scared,
Somewhere over the ocean the year let go.
The little plane on the little map is gone now,
And I'm standing where the map was trying to go.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 632 at 116 wpm → ~5.4 min, 91% of frame cap |
| Caption + lyrics tokens | 2077 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
