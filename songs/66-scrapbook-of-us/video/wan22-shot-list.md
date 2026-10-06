# Wan 2.2 Shot List — "Scrapbook of Us"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. Timestamps come from the rendered WAV; cut
on the sung line. At 86 BPM a bar is 2.79 s, so most shots run 4–6 s and the
post-chorus is the only fast passage in the video.

## 1. Visual style

One kitchen table, one night, and eleven years falling out of a book. The
**present** is lit by nine tea lights and one warm bulb over the counter,
nothing else, and it gets measurably darker as the candles burn down until
the final chorus, when every light in the room comes on for the only time.
The **memories** are never graded to match each other: each live insert keeps
the real light of the year it came from, so the video is a collection of
mismatched lights held together by one candlelit table. The recurring device
is the **locked-off overhead of the open book** with exactly one page turn per
lyric line. Everything with paper in it is macro; everything with a person in
it is on sticks.

| Section | Grade | Camera |
|---|---|---|
| Intro | Nine candle flames, one counter bulb, deep black | Macro, then locked-off wide |
| Verse 1 | Candlelight present; sodium bar and hard diner fluorescent | Push-in through paper into scene |
| Pre-chorus 1 | Each year's own real light | Four one-bar inserts, handheld |
| Choruses | Candlelight only, exposure shifting on every turn | Locked-off overhead of the book |
| Verse 2 | Noticeably darker, candles burned down, nothing relit | Macro, still, no movement |
| Pre-chorus 2 | Two candles, her face half in shadow | Locked-off two-shot |
| Instrumental | Candles plus a hallway pool of light | Long close-ups on hands |
| Bridge | The darkest frame in the video, lit by the page | Macro, then a face |
| Final chorus | Every light in the apartment on | Steady, wide |
| Post-chorus | Sixteen mismatched years, half a second each | Ultra-fast |
| Outro | Candle stubs, first hallway light, a bright blank page | Macro, then a held wide |

## 2. Character bible — paste into every prompt

**Mahima** (the present, the whole night)
> Same female protagonist Mahima, woman in her early thirties, expressive dark eyes, oval face, long dark wavy hair tied back loosely with strands loose at the front, no makeup, wearing a soft oatmeal jumper with the sleeves pushed up and glue dried on her fingertips, nervous open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the earliest memories, aged about twenty)
> Same female protagonist Mahima, young woman of about twenty, expressive dark eyes, oval face, long dark wavy hair down and glossy, bold lip and sharp eyeliner, wearing a red satin slip dress and a denim jacket, bright quick expression, realistic cinematic photography, consistent identity

**Kai** — the partner, present in almost every shot from the other side of the table.
> Same male character Kai, man in his early thirties, close-cropped dark hair going grey at the temples, short beard, wearing a washed-out navy shirt with the cuffs undone, quiet attentive expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the earliest memories)
> Same male character Kai, man in his early twenties, close-cropped dark hair, no beard, wearing a plain grey tee and an open flannel shirt, easy grinning expression, realistic cinematic photography, consistent identity

No other faces. Extras in the bar, the diner and the hospital corridor are
out of focus or cropped, and no third person is ever in the same frame as the
book.

Objects that recur: the **shoebox**, the **bar napkin** with ink bled into the
fibre, the **circled diner receipt**, the **hospital wristband** with the
misspelled name, the **folded note glued at one edge**, the **two nearly
identical green paint swatches**, and the **blank last page** with one line of
dried glue across it.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every piece of writing in this video is composited in the edit.** The phone
number on the napkin, the circled diner total, the misspelled name on the
wristband, the lease, the paint swatch labels and the note in the corner of
the blank year are all overlaid in post onto model-generated blank paper. This
is a video about handwriting, and the model cannot produce a single legible
character — so it produces none of them.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and Kai in both ages with a character LoRA per person plus
IP-Adapter for identity across the age gap; grey at the temples is the only
ageing cue on Kai and it must be consistent. **Hands are the lead actor here**
— roughly half the shots are macro on fingers, paper edges and page turns,
which is the single worst case for this model. Shoot every page turn as its
own short clip with an OpenPose or reference hand plate, keep the motion to
one continuous action, and reject anything with a sixth finger rather than
trying to fix it. Depth for the candlelit interior, which has almost no fill
and confuses the model. 16:9 first; 9:16 for the overhead book shot, which is
natively vertical. Animate small: a page lifting, a flame moving, a thumb
sliding into a gap.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s; post-chorus shots 0.5 s.

## 4. Scene per lyric line

### Intro — the table, set

1. *"Glue on my fingers, a shoebox on the floor"* — macro on fingertips tacky with dried glue, pressing together and coming apart with a thread of it between them.
2. *"Nine tea lights and a table set for two"* — the nine flames in a row across the table at flame height, long lens, everything behind them black.
3. *"I have been hiding this since February"* — the shoebox on the floor beside a chair, lid half off, paper visible, her foot beside it.
4. *"And tonight I'm handing it to you"* — locked-off wide of the whole table from the doorway, two plates, nine candles, both chairs occupied, the book still under her hands.

### Verse 1 — the napkin and the receipt

5. *"Page one is a napkin from a bar on Delancey"* — the book opened on Kai's knee, page one: a bar napkin glued flat, ink bled into the fibre (composited), macro.
6. *"Your number in a pen that hardly worked at all"* — the frame pushes into the napkin until the paper texture becomes a bar counter and we are eleven years back.
7. *"You wrote it upside down so I would have to turn it"* — the bar: young Kai testing a pen three times against a beer mat, then writing, sodium and neon spill.
8. *"And I've turned it over ever since that fall"* — the napkin slid across the counter upside down, young Mahima turning it the right way round, close-up on her hand and her face.
9. *"Page two is a receipt from a diner at three"* — back to the book, page two, a curled thermal receipt glued at the top, hard shadow across it.
10. *"Two coffees and a plate of fries we didn't share"* — the diner at three in the morning, hard fluorescent, two coffees and one plate between them, neither eating.
11. *"I circled the total and wrote the date beside it"* — her hand circling a total with a borrowed pen (composited), the pen dragging on the thermal paper.
12. *"Because I knew already I'd want the proof somewhere"* — young Mahima folding the receipt into her jacket pocket while young Kai is looking out the window.

### Pre-chorus 1 — the quiet stealing

13. *"You never saw me keep them, you were watching me"* — a cinema seat, a ticket stub palmed off the armrest, Kai in the next seat looking at the screen, one bar.
14. *"A ticket in my pocket, a stub up my sleeve"* — a bar coaster going into a coat pocket; a luggage tag pulled off a handle and folded away, two half-bar inserts.
15. *"Eleven years of small and careful stealing"* — a receipt folded into a back pocket at a supermarket checkout, Kai two feet away loading a bag.
16. *"From every single room that we would leave"* — present day: Kai looking up from the book straight at her, catching on, the first eye contact in the video.

### Chorus 1 — the book

17. *"Every page in the scrapbook of us, I'd live again"* — locked-off overhead of the open book, hands entering from the bottom of frame, one page lifting into candlelight.
18. *"Soft ones, sharp ones, and the ones that left a stain"* — the next turn, and a page with a ring-shaped coffee stain across the corner of it, macro.
19. *"A napkin, a wristband, a flower pressed to dust"* — a pressed flower gone to paper, disintegrating slightly as the page moves, one bar.
20. *"A ticket to a movie we walked out of, and us"* — the cinema again for one bar: two seats empty in a full row, the film still running.
21. *"I never called it saving, I just never threw it out"* — the shoebox on the floor from directly above, still half full of unused paper.
22. *"And a box you never empty is a love song"* — her face across the table watching him read, chin on her hand, candlelight, held.
23. *"Take your time, there's a page for every when"* — three page turns in one shot, each one changing the exposure slightly, nobody correcting it.
24. *"Every page in the scrapbook of us, I'd live again"* — the overhead again, both his hands flat on the open spread, not turning, wide.

### Verse 2 — the hard pages

25. *"Page nine is a wristband from a hospital in April"* — a plastic hospital wristband glued across a page, name misspelled (composited), his thumb entering frame and stopping on it.
26. *"Your name typed wrong, and I never got it changed"* — a hospital corridor at night in cold green light, two seconds, a chair and a coat, nobody's face.
27. *"Page ten is only a folded piece of paper"* — a folded square glued at one edge so it can still be opened, macro, neither of them opening it.
28. *"With the thing I would have said if you had stayed"* — Kai's face looking at the folded square, and deciding not to. Locked-off, held.
29. *"Page eleven is a lease with both our names"* — a lease document glued across two pages (all text composited), a coffee ring on the corner.
30. *"Page twelve is mostly empty, and we know why"* — a page that is almost entirely blank with one small note in the corner, a long static macro.
31. *"A swatch of the wall we painted twice"* — two nearly identical green paint swatches side by side, the difference almost invisible in candlelight.
32. *"And a note that I have read a hundred times"* — the note's corner, worn soft and rounded from handling, the only piece of paper in the book that is not flat.

### Pre-chorus 2 — the explanation

33. *"I didn't keep the bad ones to make a point"* — locked-off two-shot across the table, her talking with her hands, him listening with the book open on his knee.
34. *"I kept them because they belong to us the same"* — her face half in shadow with only two candles left, close-up, no movement.
35. *"Eleven years of getting half of it right"* — macro on the mostly blank page from shot 30, her hand covering it, then deliberately uncovering it again.
36. *"And I wouldn't give a single Tuesday away"* — Kai reaching across and putting one hand flat on top of hers on the page, both hands only.

### Chorus 2 — the good and bad, alternating

37. *"Every page in the scrapbook of us, I'd live again"* — the locked-off overhead repeated exactly, one page turn per line, the turns slower than in chorus one.
38. *"Soft ones, sharp ones, and the ones that left a stain"* — the bar from shot 7 and the hospital corridor from shot 26 cut back to back, one bar each.
39. *"A napkin, a wristband, a flower pressed to dust"* — a turn that stops halfway, the page standing on its edge, held, then falling.
40. *"A ticket to a movie we walked out of, and us"* — the diner from shot 10 and the lease signing cut back to back, one bar each.
41. *"I never called it saving, I just never threw it out"* — Kai gets up mid-chorus and lights three more candles without the shot cutting, the frame brightening as he does.
42. *"And a box you never empty is a love song"* — the table with the new light on it, both of them, the book between them, wide.
43. *"Take your time, there's a page for every when"* — the overhead again, brighter now, four pages turning in sequence.
44. *"Every page in the scrapbook of us, I'd live again"* — her watching him, the same framing as shot 22, but she is smiling this time.

### Instrumental — nobody speaks

45. His hands on the pages in a long unbroken close-up: a thumb under a corner, a page lifted and settled.
46. A page held up to a candle to see the writing through it from the back, the flame visible through the paper.
47. Kai laughing with no sound at something on a page, close-up on his face, candlelight, held long.
48. Her face across the table watching him read, chin on her hand, not saying anything, the longest static shot in the video.
49. The shoebox on the floor with the lid off, still half full of blank paper, and one hand reaching down to touch the edge of it.

### Bridge — the last page

50. *"The last page is empty and I left it that way"* — the book turned to the final spread: one clean page with a single line of dried glue across it and nothing else.
51. *"A line of dried glue and a space for a date"* — extreme macro on the glue line, ridged and shiny, catching two flames.
52. *"There's no question in this, there's nothing to say"* — Kai's face taking a second longer than expected to understand it, close-up, no cut.
53. *"I'm telling you I'm nowhere near done, and I'll wait"* — her face, waiting, not helping him, the darkest frame in the video.
54. *"Keep your thumb in the gap and hold our place"* — his thumb sliding into the gap between the last two pages and staying there, macro.
55. *"And we'll fill it the slow way, at the pace we make"* — the book closing on his thumb, the two of them and the closed book in one wide, held.

### Final chorus — every light on

56. *"Every page in the scrapbook of us, I'd live again"* — the whole book resting on one open palm, actual size and weight, candlelight raking across the cover.
57. *"Soft ones, sharp ones, and the ones that left a stain"* — the cover in macro: cloth tape, uneven corners, obviously handmade.
58. *"A napkin, a wristband, a flower pressed to dust"* — three of the objects on the bare table beside the book, unglued spares, arranged and not styled.
59. *"A ticket to a movie we walked out of, and us"* — both of them standing on either side of the table, the book between them, medium two-shot.
60. *"You're holding eleven years in the palm of one hand"* — every light in the apartment comes on: the wide of the kitchen fully lit for the only time, glue, scissors, shoebox, both of them.
61. *"And the box is only half full, which was more or less the plan"* — the shoebox in full light, the unused paper in it obvious for the first time.
62. *"Take your time and turn them, then hand me back the pen"* — a pen on the table between them, neither hand on it yet, macro.
63. *"Every page in the scrapbook of us, I'd live again"* — the two of them in the lit kitchen, not embracing, just standing there, wide, held.

### Post-chorus — sixteen years in eight seconds

64. *"I'd live it again, I'd live it again"* — four half-second cuts: the bar, the napkin, the diner, the receipt.
65. *"Every wrong turn, every long way round"* — four half-second cuts: the cinema, an airport gate, the hospital corridor, the lease.
66. *"I'd live it again, I'd live it again"* — four half-second cuts: the two greens on the wall, the folded note, the shoebox, the blank page.
67. *"Turn the page, I'm not putting it down"* — the book open on the table with nobody holding it, pages moving slightly in a draught, static.

### Outro — the pen

68. *"Glue on your fingers now, the shoebox on the floor"* — macro on Kai's fingertips, now tacky with the same glue, matched exactly to shot 1.
69. *"The candles are down to nothing, the tea's gone cold"* — two candle stubs guttering and two cold mugs, macro, the wax pooled on the table.
70. *"You've got one page left and a pen in your hand"* — the pen going from her hand into his, one continuous move, no faces in frame.
71. *"And I'm not saying anything. Go on. Write."* — final shot: the wide of the table from the doorway matched to shot 4, the book open at the blank page, Kai leaning over it with the pen, the blank page the brightest thing in the frame, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first page turn, the push through the napkin into the bar, the
eye contact in shot 16, the wristband, the mostly blank page, the
instrumental, the glue line in shot 51, the thumb going into the gap, the
lights coming on in shot 60, and the pen changing hands. At 86 BPM a bar is
2.79 s; the choruses cut one page turn per line and the post-chorus cuts every
half beat.

**The shareable cut** is shots 17–24, vertical: the locked-off overhead of the
book with one page turn per line, with *"a box you never empty is a love
song"* on screen.

**The challenge — page one.** Show the oldest piece of paper you kept from
somebody and say what page it would be: a ticket, a receipt, a wristband, a
napkin. The blank last page (shots 50–54) is the second shareable moment and
the one that will get reposted at anniversaries.

## 6. Quality-control checklist

- Two ages each for Mahima and Kai, cleanly separated; grey at the temples is the only ageing cue on Kai and must be present in every present-day shot
- No third face anywhere in the video; extras in the bar, diner and hospital are out of focus or cropped
- Every piece of writing composited onto blank model-generated paper — the napkin number, the circled total, the misspelled wristband, the lease, the swatch labels, the note
- Hands are checked frame by frame; any macro shot with a malformed hand is regenerated, not retouched
- The present-day frame gets progressively darker from shot 1 to shot 53, brightens by three candles at shot 41, and is fully lit only from shot 60
- Memory inserts are never graded to match each other; each keeps the real light of its own year
- The book is one physical prop with the same cloth-tape spine and the same uneven corners in all of its appearances
- The last shot matches shot 4 exactly in lens and position, and the blank page is the brightest thing in it
