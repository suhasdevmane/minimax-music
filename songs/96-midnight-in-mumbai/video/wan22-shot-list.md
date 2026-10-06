# Wan 2.2 Shot List — "Midnight in Mumbai"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
110 BPM a bar is 2.18 s, so most shots run 4–6 s and the choruses cut every
two bars — this is a wide, unhurried film, not a fast one.

## 1. Visual world

One night on a sea-facing city at monsoon season, from midnight to the first
ferry. **Every light source in this film is practical and warm**: sodium
lamps, tube lights over shutters, one bulb over a chai burner, headlights,
a lit window three floors up. The sea is the only cool thing in frame, and
it is always in the background of the important shots. Monsoon haze softens
every distant light into a halo. Handheld only when she is moving; locked
off whenever she stops.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium gold, blue-black sea, heavy haze | Wide static, macro inserts |
| Verse 1 | Warm pavement, cool sea, raking headlights | Slow lateral tracking |
| Pre-chorus | Dark street, one tube light per shopfront | Walking away from camera |
| Choruses | Saturated golds and greens, wet tarmac | Drone, roaming handheld |
| Verse 2 (scooter) | Strobing sodium at speed, then moonlit still | Mounted, then locked off |
| Instrumental | Gold, with one cool-graded rain shower | Slow motion, held frames |
| Bridge | Deepest blue, one warm window | Locked-off wide |
| Final chorus | Gold street with first grey entering the sky | Wide, arms-out, moving |
| Outro | Pearl-grey dawn, lamps switching off in sequence | Slow, calm, held |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and moving in the sea wind, minimal natural makeup, wearing a deep green cotton kurta over dark straight trousers with a thin cream scarf, a string of white jasmine round one wrist, calm open expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the stranger)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded blue denim jacket over a plain white t-shirt and dark jeans, scooter keys looped on one finger, easy unhurried expression, realistic cinematic photography, consistent identity

There is no ex and no rival in this film. **Everybody else is a real night
worker**, shot with dignity and never as background colour: the jasmine boy,
the taxi drivers in their yellow-and-black cabs, the chai stall owner, two
delivery riders, an old man with a newspaper, the flower-market traders at
dawn. Faces are fine; nobody is styled.

Objects: the **jasmine string** on her wrist (present from shot 8 to the last
frame), the **small chai glass**, the **cream scarf** (loose at the wall,
straight out behind her on the sea link), the **kettle**, the **scooter**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All signage, shopfront lettering, taxi numbers, phone screens and ferry
markings are composited in the edit.** Generate every plate clean; the model
cannot render legible Devanagari or English signage and one wrong sign
destroys the location.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock both leads with IP-Adapter or a character LoRA each; build Kai's
reference in the denim jacket only, since he never changes. Depth for the
promenade wides and the sea link; OpenPose for the scooter mount and the
arms-out shot in the final chorus. 16:9 first; 9:16 recomposition for the
chai pour and the scarf shot, which are the vertical clips. Animate in single
gestures: one pour, one kick-start, one wave breaking, one curtain moving.
Water, steam and cloth in wind all render better in slow motion than at
speed — shoot the scarf and the pour long and retime in the edit.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s.

## 4. Scene per lyric line

### Intro — the sea wall

1. *"Salt in the air on the wall at Marine Drive"* — wide from behind: Mahima sitting on a sea wall, small against a long curve of streetlamps running away around a dark bay, static, heavy monsoon haze.
2. *"A long curve of lamps like a necklace of light"* — the lamp curve alone, shot long-lens so the lights compress into a single unbroken gold line, slow drift.
3. *"I came out for nothing, with no reason to be here"* — her face in profile at the wall, eyes on the water, no expression to read, close-up.
4. *"And the city said, stay, there is more to the night"* — macro: sea spray hitting the concrete beside her hand, a strand of hair lifting in the salt wind, slow motion.

### Verse 1 — the street empties, the stranger arrives

5. *"The vendors are folding their tables away"* — slow lateral tracking along the promenade past vendors folding trestle tables and stacking crates, her walking the other side of frame.
6. *"The taxis are humming in one yellow line"* — a rank of idling yellow-and-black taxis, headlights raking the wet pavement, low angle.
7. *"A boy sells his jasmine to nobody at all"* — a boy with a tray of white jasmine strings standing at an empty stretch of railing, wide, patient.
8. *"And the smell of it follows me down to the tide"* — macro: her hand taking one jasmine string and looping it round her wrist; the flowers very white against the dark.
9. *"I was not looking for anybody tonight"* — her back at the wall, elbows on the concrete, counting something out on the water, medium.
10. *"I was counting the boats and the lamps on the sea"* — her point of view: three small fishing boats far out, each with one lamp, moving slowly.
11. *"Then a stranger came over and asked for the time"* — Kai arriving beside her at the wall, half a metre of space between them, asking something, two-shot.
12. *"And we laughed, because neither of us cared to know"* — both of them laughing, the first genuine laugh of the film, close two-shot, warm sodium.

### Pre-chorus 1 — the shuttered road

13. *"He said, there is chai at the end of this road"* — Kai pointing inland down a shuttered street, only his hand and the dark road in frame.
14. *"And the kettle sings louder than any radio"* — the far end of the street: a steel kettle at full boil on a stall burner, glowing orange, long lens.
15. *"So I walked with a stranger past the shuttered shops"* — both of them walking away from camera down the middle of the empty road, shutters on either side, one tube light per shopfront.
16. *"And the sea kept the time of the way we would go"* — a look back over her shoulder: the sea still visible at the far end of the street behind them.

### Chorus 1 — the city awake

17. *"Midnight in Mumbai, and the city's wide awake"* — a drone rising over the promenade until the whole bay is one line of gold, the widest shot in the film.
18. *"Every window a lantern, every street a second chance"* — a tower block at night where every third window is still lit, static, long lens.
19. *"Midnight in Mumbai, and the sea will not sleep"* — waves against the sea wall in slow motion, the lamp curve behind them out of focus.
20. *"So I am not sleeping while the whole town wants to dance"* — a night market being folded and restacked for morning, cloth, fruit, hands, roaming handheld.
21. *"Give me chai in a glass and a scooter and sea spray"* — three fast cuts on the beat: a small glass filling, a scooter mirror with the sea in it, spray on the wall.
22. *"Give me warm monsoon air on my face"* — Mahima walking through it all, eyes half closed into the wind, jasmine on her wrist, tracking from the front.
23. *"Midnight in Mumbai, and the city's wide awake"* — two boys playing cricket under a streetlight, a dog asleep across a doorway, quick cuts.
24. *"And a stranger's voice is turning into a place"* — Kai walking a few paces ahead, talking, turning back to check she is following, handheld.

### Verse 2 — the scooter and the sea link

25. *"He wakes up the scooter and I hold on politely"* — a kick-start, the engine catching, low angle on the wheel and the exhaust, then her hand hovering an inch off his jacket.
26. *"Then the road opens out and I hold on for real"* — her hand closing on the denim as the scooter accelerates, macro, motion blur behind.
27. *"The sea link is empty and the wind takes my scarf"* — the empty sea link at speed, cables strobing overhead, her cream scarf pulling straight out behind her, mounted camera.
28. *"And I laugh like a woman with nothing to conceal"* — her face at speed, laughing openly, sodium strobing across it, close-up on the mount.
29. *"He tells me his mother still calls him at midnight"* — the far side, stopped, both leaning on the parapet, Kai talking, a phone lighting in his pocket and being ignored.
30. *"I tell him my flat has one window and a plant"* — her talking now, hands moving, the sea flat and moonlit behind her, medium.
31. *"Two strangers, two histories, one road and one country"* — a wide from far back: two small figures on an enormous empty bridge, static.
32. *"And the city is listening, and the city understands"* — the skyline across the water, every light on, held.

### Pre-chorus 2 — the stall

33. *"He said, there is a stall that stays open till morning"* — the chai stall arriving into frame: one bulb, one burner, four crates, a wall of parked scooters.
34. *"Where the glasses are small and the fire never goes"* — macro on the burner flame under a blackened pot, the bulb flaring in the lens.
35. *"So I sat on a crate with my hands round a tumbler"* — chai poured from a height into a small glass, steam catching the bulb light, slow motion.
36. *"And I stopped making plans for the road leading home"* — her on a crate, both hands wrapped round the glass, shoulders finally down, close-up.

### Chorus 2 — inside it now

37. *"Midnight in Mumbai, and the city's wide awake"* — the whole stall in one frame: a taxi driver, two delivery riders, an old man with a newspaper, her and Kai, wide.
38. *"Every window a lantern, every street a second chance"* — reuse the tower-block framing from shot 18, closer, more windows lit.
39. *"Midnight in Mumbai, and the sea will not sleep"* — the sea heard and not seen: a puddle by the stall holding the reflection of the bulb, macro.
40. *"So I am not sleeping while the whole town wants to dance"* — the stall owner saying something and Mahima laughing hard, handheld, warm.
41. *"Give me chai in a glass and a scooter and sea spray"* — a cat crossing the wall of parked scooters, unhurried, low angle.
42. *"Give me warm monsoon air on my face"* — her stepping out of the bulb's circle of light into the blue night for one breath, then back, medium.
43. *"Midnight in Mumbai, and the city's wide awake"* — the fire under the pot being fed, sparks, macro.
44. *"And a stranger's voice is turning into a place"* — Kai and Mahima on adjacent crates, both looking out at the street rather than at each other, two-shot.

### Instrumental — sitar, strings, bansuri

45. A single slow-motion pour of chai from pot to glass, held for the whole length of the arc.
46. The lamp curve of the promenade from a rooftop, one locked-off frame, no camera move at all.
47. A ten-second monsoon shower starting and stopping; everybody at the stall carries on without reacting; the only cool-graded shot in the sequence.
48. Her walking alone back to the sea wall while Kai pays, the sitar taking the melody, tracking from behind.
49. The bansuri figure over flat black water: an empty frame of sea, no people, no drums, held long.

### Bridge — the wall again

50. *"I have lived in this city for seven long years"* — locked-off wide: the two of them sitting apart on the sea wall, not touching, the whole bay behind them.
51. *"And I never once heard it the way that I do"* — her face, eyes closed, listening rather than looking, close-up.
52. *"The horns are a chorus, the waves keep the measure"* — a distant road with two horns sounding, then a wave breaking exactly on the beat, cut together.
53. *"And a radio upstairs is in tune with them too"* — a lit window three floors up, a curtain moving, a radio just audible, static long lens.
54. *"I do not need an ending, I am here for the middle"* — her opening her eyes and simply looking at the water, medium, no reaction shot from him.
55. *"And the middle is the chai and the sea and you"* — the two of them from far behind, the deepest blue grade in the film, one warm window above them.

### Final chorus — morning refusing to arrive

56. *"Midnight in Mumbai, and the city's wide awake"* — fishing boats coming in at the far end of the bay, lamps still lit, wide.
57. *"Every window a lantern, every stranger a friend"* — everybody from the stall dispersing, each raising a hand as they go, handheld.
58. *"Midnight in Mumbai, and the sea will not sleep"* — the first bus of the day with its interior lights still on, crossing frame, static.
59. *"And I do not want a single thing here to end"* — a flower market being set up in the dark, crates of marigold and jasmine opening, roaming.
60. *"Give me chai in a glass and a scooter and sea spray"* — the three motifs again on the beat, now with the first grey in the sky behind each.
61. *"Give me warm monsoon air on my face"* — Mahima on the promenade with her arms out to the wind, the happiest frame of the film, wide.
62. *"Midnight in Mumbai, and the city's wide awake"* — a crane rise over her and the whole waking bay, the sky greying at the top of frame.
63. *"And a stranger's voice has turned into a place"* — Kai a little way off, hands in pockets, watching the water, not her, medium.

### Post-chorus — four returns

64. *"Awake, awake, the whole of the bay"* — the lamp curve, hard cut, no fade.
65. *"The lights on the water will not look away"* — the kettle, hard cut.
66. *"Awake, awake, and the morning can wait"* — the scooter mirror with the sea in it, hard cut.
67. *"Because midnight in Mumbai is a place I want to stay"* — the jasmine string on her wrist, macro, held two beats longer than the others.

### Outro — the first ferry

68. *"The first ferry moves and the sky turns to pearl"* — the first ferry pulling out, one long horn across the water, wide, pearl-grey sky.
69. *"The vendors come back and the tables unfold"* — the same vendors from shot 5 unfolding the same trestle tables, the loop closing, lateral tracking.
70. *"I am walking home slowly with salt in my hair"* — her walking away unhurried, jasmine still on her wrist, salt-stiff hair, tracking from behind.
71. *"And a city behind me that never went cold"* — final shot: the empty stretch of sea wall where she was sitting in shot 1, locked off, the sea moving, the lamps switching off in sequence down the curve, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first sitar pluck, the laugh in shot 12, each *"Midnight in
Mumbai"*, the kick-start, the pour, the instrumental rain shower, *"I am here
for the middle"*, the final crane, and the ferry horn. At 110 BPM a bar is
2.18 s; choruses cut every two bars, the post-chorus every bar, and the
scooter sequence cuts only on the sodium strobe.

**The pour.** Post the vertical slow-motion chai pour (shot 45) under the
hook and invite people to post their own city at midnight — the stall, the
bridge, the last bus, whatever is still awake where they are. The scarf on
the sea link (shot 27) is the second shareable frame.
**Caption:** *"The city was never the thing that was asleep."*

## 6. Quality-control checklist

- One look each, all night: green kurta and cream scarf for her, denim jacket for him. Nobody changes clothes; it is one night
- The jasmine string is on her wrist from shot 8 to the last frame, and is never lost or swapped
- Every light source is practical and warm; the sea is the only cool element, and the instrumental rain shower is the only cool-graded shot
- No readable signage, taxi number, phone content or ferry marking generated by the model — all composited
- The night workers are shot with dignity, never as texture; no styled extras
- The two leads never touch except her hand on his jacket during the ride; the bridge is deliberately played with space between them
- The outro closes the loop on shot 1 exactly: same framing, same wall, empty
- The last frame is locked off and holds through the fade, with no text
