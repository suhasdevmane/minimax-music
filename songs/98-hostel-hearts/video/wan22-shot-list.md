# Wan 2.2 Shot List — "Hostel Hearts"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
106 BPM a bar is 2.26 s, so most shots run 4–6 s; the choruses cut every two
bars and the post-chorus cuts every bar.

## 1. Visual style

Four days and one hostel, shot like a documentary somebody made on the trip
rather than like a music video. **Nobody in this film is styled.** Hair is
unwashed, clothes are the two shirts they packed, and the light is whatever
the building happens to have: one strip light in the kitchen, one working
lamp in the common room, corridor fluorescent, fairy lights on the roof. The
camera is handheld and often slightly late to the moment, as though the
person holding it is also in the conversation. Only four sequences are
locked off, and each of them means something: the ceiling fan, the
noticeboard, the bridge kitchen table, and the last shot.

| Section | Grade | Camera |
|---|---|---|
| Intro | Dorm dim and blue, then one warm lamp | Static, then hard cut handheld |
| Verse 1 | Strip light and candle, steam on the lens | Crowded handheld |
| Pre-chorus | Corridor fluorescent, unflattering | Slow push-in, locked off on the board |
| Choruses | Fairy lights and one orange streetlamp | Wide, roaming, out of time |
| Verse 2 | Market neon and steam; then almost nothing on the roof | One long handheld take |
| Pre-chorus 2 | Flat honest daylight, the least flattering grade | Handheld, low energy |
| Instrumental | Cool — the only cold frames in the film | Slow push, locked off |
| Bridge | Cold northern daylight, one window | Static, the most still shot |
| Final chorus | Six different times of day at once | Six fixed portraits |
| Post-chorus | Corridor fluorescent, unchanged | Cuts, no camera move |
| Outro | Dawn blue, warm lamp beyond a doorway | Static, held |

## 2. Character bible — paste into every prompt

**Mahima** (arriving, days one to two)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied up badly and coming loose, no makeup, wearing a washed-out grey t-shirt and loose linen trousers with a small canvas backpack, tired guarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (days three to four)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and unbrushed, no makeup, wearing a borrowed oversized striped shirt over the same grey t-shirt, open easy expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge, back home)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair washed and tied back, wearing a plain dark jumper, calm certain expression, realistic cinematic photography, consistent identity, natural skin texture

**There is no romantic lead in this film and therefore no Kai, and no ex,
so no faceless figures are needed.** Instead there is an **ensemble of six**,
and every one of them has a face and a consistent look, because the whole
argument of the song is that these people were real:

- **The Dutch cook** — tall woman, late twenties, cropped blonde hair, vest and cargo shorts, always holding a wooden spoon
- **The Argentine** — man, mid twenties, curly dark hair, open shirt, permanently searching a rucksack
- **The German** — man, early twenties, glasses, long hair, a battered nylon guitar he never puts down
- **The traveller from Osaka** — man, thirties, quiet, short hair, carries other people's bags without being asked
- **Two more housemates** — a woman in her thirties on a night-shift schedule and a nineteen-year-old on his first trip

Objects: the **one working pan**, the **lighter** passed hand to hand, the
**candle in a bottle**, the **dying marker**, the **noticeboard** (locked-off,
same angle, four times in the film), the **battered guitar**, the **bare
mattress in bunk nineteen**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every name, date and drawing on the noticeboard, every phone screen and the
group chat are composited in the edit.** Generate the board as a corkboard of
blank paper scraps and tape; the board's content is the emotional payload of
two whole sections and the model cannot write it.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA, and build
a light reference for each of the six ensemble characters — they recur across
nine shots each and a face that drifts will destroy the final chorus, where
all six appear alone in different cities. Depth for the crowded kitchen, which
is the hardest composition in the film. OpenPose for the clapping, the
stairwell suitcase and anyone holding the guitar. 16:9 first; 9:16
recomposition for the noticeboard and the rooftop singalong, which are the
vertical clips. Animate in single gestures: one stir, one lighter passed, one
hand writing, one clap. Groups are the failure mode — generate crowded shots
with fewer bodies than you want and cut faster rather than asking for eight
people in one frame.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s.

## 4. Scene per lyric line

### Intro — arriving

1. *"Bunk nineteen, second floor"* — a hostel dorm at dusk, eight beds, four made, one bare mattress with a stencilled number on the frame, wide static.
2. *"A ceiling fan that only turns one way"* — the ceiling fan from directly beneath, turning slowly, locked off, held.
3. *"I came in tired and I didn't want to talk"* — Mahima dropping her backpack on the bare mattress and standing there, too tired to unpack, medium, dim blue.
4. *"By ten I was laughing in a language I don't speak"* — a hard cut to the same face three hours later, mid-laugh in a crowded common room, one warm lamp, handheld, no explanation.

### Verse 1 — the kitchen

5. *"There's a Dutch girl teaching us all to cook with one pan"* — one pan on one working hob, four people crowded round it, the Dutch cook directing with a wooden spoon, tight handheld.
6. *"An Argentine guy who lost his passport and his mind"* — the Argentine tearing his rucksack apart on the kitchen floor, everyone stepping over him without comment.
7. *"Somebody's playlist, somebody's cheap red wine"* — a phone on a shelf playing music, a wine bottle with a candle jammed in the neck, two quick cuts.
8. *"Somebody's mother on a video call waving at us"* — a phone propped against a sauce bottle with an older woman on a call (composited), the whole table waving at her at once.
9. *"Strangers in a kitchen with one lighter and no plan"* — a lighter passing hand to hand round the table toward the candle, macro on hands only.
10. *"And nobody asks me what I do or where I've been"* — Mahima at the table listening, not talking, unbothered, medium close-up, steam crossing the lens.
11. *"First time all year that nobody wants my history"* — her shoulders dropping half an inch, a small unguarded exhale, close-up.
12. *"Just my half of the table and my name"* — a wide of the whole crowded table from the doorway, plates and elbows, her in it rather than at the edge of it.

### Pre-chorus 1 — the noticeboard

13. *"The door never locks and the kettle never cools"* — the front door swinging open on its own with nobody at it, then a kettle boiling, two cuts.
14. *"The noticeboard is covered in the names of people gone"* — the corkboard, locked off, a slow push-in: layers of paper, tape and marker (all composited).
15. *"Somebody writes mine on it with a dying marker"* — a hand writing into the last free corner with a marker that keeps skipping, macro.
16. *"And that's how you know that you belong"* — Mahima looking at the board from a few feet back, saying nothing, corridor fluorescent, medium.

### Chorus 1 — the roof

17. *"Hostel hearts, strangers for a night, family by the morning"* — the rooftop: fairy lights on a washing line, plastic chairs, the whole group, wide.
18. *"Four days is a lifetime when you're living without warning"* — the group singing badly and enthusiastically, all talking over each other, handheld in among them.
19. *"We don't know each other's last names and we never will"* — hands clapping visibly out of time, four pairs in one frame, close.
20. *"But you sat up when I was sick, and I'd do it again"* — a quieter insert: the Osaka traveller putting a glass of water on the floor beside a bunk, then leaving.
21. *"Hostel hearts, no address and no goodbye that lands"* — one person asleep in a plastic chair through the entire chorus, undisturbed, static.
22. *"A rooftop, a lighter and eleven pairs of hands"* — the lighter again, lighting a candle on the low wall, hands crowding into frame around it.
23. *"Strangers for a night, family by the morning"* — a wide from the far side of the roof: the whole group against the city, the sky still holding a little blue.

### Verse 2 — the market and four in the morning

24. *"Night market, second night, we ate something we couldn't name"* — one long handheld take through a night market: steam, tongs, plastic stools, everyone pointing at food nobody can identify.
25. *"And the Argentine found his passport in his coat"* — the Argentine finding the passport in his own coat pocket and holding it up; the group's unreasonable joy.
26. *"On the roof at four in the morning somebody's crying"* — the roof hours later, most of the fairy lights off, somebody crying quietly, wide, almost no light.
27. *"And nobody makes it weird, we just move closer"* — two people shifting their plastic chairs a few inches, nothing said, nobody performing comfort, static.
28. *"The Dutch girl says she isn't going home in September"* — the Dutch cook talking, animated, hands out; two people laughing at her, close.
29. *"The German plays the only slow song he knows"* — the battered guitar handed across the roof; the German playing, glasses reflecting what light there is.
30. *"And I told a room of strangers what I never told my sister"* — Mahima talking at length, the sound of the song covering it, nobody interrupting, medium close-up.
31. *"And the sky went the colour of a peach and nobody spoke"* — a peach-coloured sky arriving behind the whole silent group, wide, held longer than any other shot so far.

### Pre-chorus 2 — the last morning

32. *"The door never locks and the kettle never cools"* — the same kettle boiling for the last round, flat honest daylight, medium.
33. *"And checkout is at ten and we know what that means"* — beds being stripped, bags on bare mattresses, nobody hurrying, wide.
34. *"Somebody's bus goes first, somebody's on the stairwell"* — a suitcase being dragged down a stairwell badly, somebody sitting on the stairs beside it not helping and not leaving.
35. *"And the marker on the board has run out"* — the dead marker on the noticeboard: tried, shaken, tried again, put down, macro.

### Chorus 2 — the bus station

36. *"Hostel hearts, strangers for a night, family by the morning"* — the bus station under hard morning sun through a canopy, the group in a loose knot, wide.
37. *"Four days is a lifetime when you're living without warning"* — a hug that goes on several seconds too long, static, nobody breaking it.
38. *"We don't know each other's last names and we never will"* — a phone number written on the back of a receipt because somebody's phone is dead, macro.
39. *"But you sat up when I was sick, and I'd do it again"* — cut back to the kitchen from verse one for one beat, then hard back to the station.
40. *"Hostel hearts, no address and no goodbye that lands"* — the bus door closing, seen from outside, faces behind glass.
41. *"A rooftop, a lighter and eleven pairs of hands"* — cut back to the roof at night for one beat, then the station again.
42. *"Strangers for a night, family by the morning"* — the bus pulling out, the remaining four standing there longer than makes sense, wide.

### Instrumental — the building without them

43. A slow push along the empty rooftop, plastic chairs still exactly where they were left, cool grade.
44. The kitchen, cleaned, one pan drying upside down on a rack, locked off.
45. A new group of strangers arriving at the front desk with the same backpacks, handheld, indifferent.
46. The ceiling fan again, same angle as shot 2, still turning one way.
47. The noticeboard from the same angle as shot 14, new names already over the old ones, locked off, held into the bridge.

### Bridge — back home

48. *"People say it wasn't real because it only lasted four days"* — Mahima alone at a kitchen table in a small flat, one mug, a closed laptop, the most static shot in the film.
49. *"As if a thing must be long before it's allowed to be true"* — her face in cold northern daylight from one window, close-up, no reaction shot.
50. *"I've known people ten years who never asked me how I sleep"* — an empty second chair at the table, held, wide.
51. *"And a stranger from Osaka carried my bag up two flights"* — a silent flashback: the Osaka traveller carrying her rucksack up a narrow stairwell, two flights, unasked, no sound.
52. *"So call it what you want, I know what it was"* — her phone face-up on the table with a group chat lighting up (composited), and her smiling at it, macro.
53. *"It was family, and it fit in a room with eight beds"* — her looking straight past the camera at whoever she is arguing with, certain, close-up.

### Final chorus — six cities at once

54. *"Hostel hearts, strangers for a night, family by the morning"* — six fast portraits, each in a different city, each doing something ordinary: a tram, a lecture hall, a kitchen, a beach, a night shift, a bus.
55. *"Four days is a lifetime when you're living without warning"* — the Dutch cook singing it alone in a kitchen that is not the hostel kitchen, fixed frame.
56. *"We won't know each other's last names and we never did"* — the Argentine singing it on a tram, badly, other passengers ignoring him.
57. *"But you sat up when I was sick, and I'd do it again"* — the Osaka traveller singing it very quietly on a night shift, alone in a lit room.
58. *"Hostel hearts, no address and no goodbye that lands"* — the German playing the same guitar in a different room, singing it properly, the only one in tune.
59. *"A rooftop, a lighter and eleven pairs of hands"* — the nineteen-year-old on a beach and the night-shift woman on a bus, split on the cut.
60. *"Strangers for a night, family by the morning"* — Mahima at her kitchen table singing it alone, then all six frames at once in a grid for two beats.

### Post-chorus — the board over months

61. *"Write your name on the board, write your name on the board"* — the noticeboard, same angle: a new name going up, in a new colour, cut on the beat.
62. *"Somebody after you will read it and feel less alone"* — a stranger reading the board and laughing at something written there, medium.
63. *"Write your name on the board, we were here, we were loud"* — layers going up and being covered, five hard cuts on five beats, same frame.
64. *"And a wall in a hallway is the only proof we own"* — the board full, corridor fluorescent, locked off, held.

### Outro — the loop

65. *"The bus pulls out at six, the fan still turns one way"* — a bus pulling out of a station at dawn, seen from inside a hostel window, static.
66. *"And bunk nineteen has a new tired person in it now"* — the same dorm, the same bare mattress, a different woman dropping her bag on it and standing there.
67. *"I hope she doesn't want to talk, and I hope she does by ten"* — the ceiling fan one last time, same angle as shots 2 and 46, turning.
68. *"And I hope somebody hands her half a table and a name"* — final shot: through the kitchen doorway, somebody sliding a chair out for her; hold on the empty half of the table before she sits, then hold two beats after. No text.

## 5. Edit and the challenge

Markers at: the hard cut into the common room, the marker skipping on the
board, each *"Hostel hearts"*, the passport, the peach sky, the bus door
closing, the instrumental fan, *"it fit in a room with eight beds"*, the
six-city grid, and the chair sliding out. At 106 BPM a bar is 2.26 s;
choruses cut every two bars, the post-chorus every bar, and the market take
in shot 24 runs uncut for its whole line.

**The board.** Post the vertical noticeboard sequence (shots 61–64) with
*"write your name on the board"* on screen, and invite people to post the
four-day family they made — the kitchen, the bunk, the goodbye. The rooftop
gang vocal (shots 17–23) is the second shareable frame, and it works better
the worse the singing is.
**Caption:** *"It was family, and it fit in a room with eight beds."*

## 6. Quality-control checklist

- Three looks for Mahima: guarded and tied-up hair for days one and two, the borrowed striped shirt from shot 24 on, the dark jumper only in the bridge and the final chorus
- All six ensemble characters keep a consistent face and wardrobe across their nine appearances; the final chorus falls apart if any of them drifts
- Nobody is styled, nobody is lit flatteringly, and no hair looks washed except in the bridge
- Every name on the noticeboard is composited; the board is shot from the identical angle in shots 14, 47, 61 and 64
- The ceiling fan appears at shots 2, 46 and 67 in the same framing, and always turns the same way
- The comfort in shot 27 is two chairs moving and nothing else — no hugging, no hand on a shoulder
- The instrumental empty-room shots are the only cool-graded frames in the film
- The last shot holds two beats after the chair moves, with no text
