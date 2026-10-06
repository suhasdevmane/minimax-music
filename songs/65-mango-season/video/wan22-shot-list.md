# Wan 2.2 Shot List — "Mango Season"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission, plus six shots for the instrumental. Timestamps come from the
rendered WAV; cut on the sung line. At 104 BPM a bar is 2.31 s, so the
choruses cut roughly every bar and the verses every two.

## 1. Visual world

A small-town Indian summer, remembered at full saturation, cut against a
present-day city that has had the colour taken out of it. The **memory** is
saffron, leaf-green, whitewash gone chalky, dust hanging in low afternoon
sun, then rain-dark grey and silver when the monsoon arrives. The
**present** is flat office white, supermarket fluorescent and hazy city
heat, cool and even, until the bridge decision when warmth starts leaking
back in. The film is bookended by the same one-lamp railway station, and
the **child's hand on the train window bars** in shot 1 is answered by the
**adult's hand in the same place** in shot 65 — the single most important
match in the edit.

Nothing is stylised. Real practical light: the platform lamp, the bare bulb
on the verandah, a lantern on the terrace, the doorway glow during the rain.
Handheld for the children, steady and still for the present day.

| Section | Grade | Camera |
|---|---|---|
| Intro | Amber platform lamp against a violet sky; the city train cold and fluorescent | Slow, from inside the carriage |
| Verse 1 | Late afternoon saffron and green, dust in the air | Handheld, chasing the children |
| Pre-chorus 1 | Flat office white, supermarket fluorescent, one warm overcast flash | Locked off, still |
| Chorus 1 | Golden courtyard, deep blue terrace night with a warm lantern | Wide, generous, drifting |
| Verse 2 | Harsh bleached afternoon, then soft morning on the step | Steady, low, at child height |
| Pre-chorus 2 | Slate grey with the last sun cutting under the cloud | Rising wind, handheld |
| Chorus 2 | Rain-dark grey with warm light from the doorway | Slow motion on the rain only |
| Instrumental | Silver-grey rain light, then the first clearing | Long holds, water everywhere |
| Bridge | Hazy city heat, a shadow crossing as the cloud arrives | Static, quiet |
| Final chorus | Golden late afternoon through a train window | Moving with the train |
| Post-chorus | Saturated saffron, green, grey-blue | Fast cuts, textures only |
| Outro | The amber lamp, then the last violet light in the courtyard | Slow walking, then a hold |

## 2. Character bible — paste into every prompt

**Mahima** (present day, the city)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back low, minimal makeup, wearing a plain cream cotton kurta with the sleeves pushed up, tired thoughtful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the journey home, final chorus and outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and lifted by the train window air, no makeup, wearing a soft green cotton kurta, a small canvas bag beside her, calm anticipating expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima at nine** — the child in every memory. Cast one child and keep her
across the whole summer; same dark wavy hair, two plaits, the same yellow
cotton frock, bare feet, mango juice to the elbows from chorus one on.
> a young girl of about nine, dark wavy hair in two plaits, expressive dark eyes, a yellow cotton frock, bare feet, realistic cinematic photography, consistent identity

**The grandfather** — a man in his seventies, thin, white kurta, a black
bicycle he never rides fast. His face is seen and warm; he is the one adult
the camera looks at directly.
> an older man in his seventies, thin build, white cotton kurta and dhoti, close-cropped white hair, wire-framed glasses, standing beside a black bicycle, warm open expression, realistic cinematic photography, consistent identity

**The grandmother** — a woman in her seventies in a cotton sari, seen mostly
as hands and a doorway silhouette. Her hands are a character: counting
heads, spooning pickle, pressing a mango into a child's palms.
> an older woman in her seventies, silver hair in a low bun, a soft cotton sari, seen from behind or in soft three-quarter, hands wrinkled and quick, warm afternoon light

**The cousins** — six children between six and twelve, mixed ages, no
individual styling, always a group and always moving. Seven children total
with Mahima, and the count must hold in every wide: the gate, the tree, the
terrace cots, the rain.

Objects that carry the story: the **one-lamp station** and its unlit name
board (never legible), the **black bicycle**, the **steel trunk**, the
**iron gate**, the **mango tree** in the courtyard, the **low wall** where
the salt-and-chilli slices are eaten, the **ceiling fan** that stops, the
**transistor radio** on its stool, the **glass pickle jars** on the top
step, the **cots in a row** on the terrace, the **supermarket mango sealed
in plastic**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, signage, station name boards and price labels are composited
in the edit.** The group chat in the bridge, the photograph on her phone and
the supermarket label are overlays. The station board and the shop signs
stay out of focus or out of frame — the model cannot render a legible
Devanagari or Latin sign and a wrong one would break the location instantly.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both adult looks and the child in her one look with
IP-Adapter or a character LoRA each; lock the grandfather too, since his
face is seen repeatedly. Keep the grandmother's reference face-light,
three-quarter and from behind. Depth for the courtyard, the verandah and the
terrace so the house stays the same house across twelve minutes of
generation. **OpenPose is essential for the children** — climbing the tree,
hanging off the gate, running into the rain and spinning with arms out all
invent anatomy without a pose reference. 16:9 first; 9:16 recomposition for
the mango hook cut and the first-rain cut.

Animate in single actions: one child dropping from a branch, one kite string
going slack, one dial turn, one sari coming off the line, one face turning
up. Rain is generated as a lit plate with real movement in it and layered in
the edit rather than asked for as a whole scene — sheeting rain plus seven
running children in one generation will fail. The flooded-courtyard stamping
shot is the one exception and should be generated several times and picked.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the one-lamp station

1. *"The train slows down at a station with one lamp,"* — a child's hand gripping the window bars of a slowing train carriage, the platform sliding into frame behind it, one amber lamp, violet sky. **The bookend frame — answered in shot 65.**
2. *"My grandfather waiting with his cycle and a smile."* — the grandfather on the empty platform beside his black bicycle, raising one hand as the carriage passes, medium, the lamp behind him.
3. *"The dust smells sweet and the air is heavy,"* — the platform surface in the last light, dust lifting where the train stops, a stray dog moving out of the way, low and close.
4. *"I can taste the summer from a mile."* — cut to the present: adult Mahima on a city train at night, forehead against cold glass, eyes closed, fluorescent light overhead, her reflection doubled in the window.

### Verse 1 — the house, the tree, the fan

5. *"Steel trunk tied to the roof of a rickshaw,"* — a cycle rickshaw coming up a narrow lane, a steel trunk roped to the roof, dust behind the wheels, tracking from the front.
6. *"Cousins hanging off the gate before we stop."* — six children hanging off an iron gate, shouting and waving, the gate swinging under their weight, handheld, saffron light.
7. *"Grandmother counting heads at the doorway,"* — the grandmother in the doorway counting with one finger, laughing, seen in soft three-quarter, the children streaming past her in blur.
8. *"Seven children, one house, one water pot."* — an earthenware water pot in the corner of the courtyard with seven children queueing at it, the smallest last, wide, static.
9. *"We climbed the tree before they told us not to,"* — children in the branches of the courtyard mango tree, one hanging by the knees, dappled leaf light on their faces, low angle from below.
10. *"Raw mango, salt and chilli, sitting on the wall."* — small hands passing slices of raw mango sprinkled with salt and red chilli along a low sun-warmed wall, mouths puckering, macro then medium.
11. *"The fan went off, the power came and went,"* — a ceiling fan slowing to a stop, the blades coming into focus one by one, the room going hot and dim, static, looking straight up.
12. *"And nobody minded at all."* — the children on the floor under the stopped fan, sprawled and unbothered, then all of them laughing at something off frame, overhead wide.

### Pre-chorus 1 — the city, the plastic mango

13. *"Now the city keeps me busy, keeps me tired,"* — adult Mahima at a desk in a glass office at dusk, the last one on the floor, flat white light, static wide.
14. *"Every summer looks the same from here."* — the office window showing only the next building's windows, no sky, a slow push toward the glass.
15. *"The office window only shows me concrete,"* — her reflection in that window over the concrete, faint, the two images overlapping, close-up.
16. *"A mango in the supermarket, wrapped in plastic, never sweet."* — her hand lifting a single mango sealed in plastic off a fluorescent shelf, turning it over, setting it back down, macro.
17. *"But I close my eyes and I am nine years old,"* — her eyes closing in the supermarket aisle, the fluorescent hum, everything still, close-up.
18. *"And the sky is about to break, I can feel it near."* — a warm overcast flash: the courtyard sky going dark with cloud, one held second, then back to her face.

### Chorus 1 — the best of the summer

19. *"Take me back to mango season,"* — child Mahima with a ripe mango in both hands, juice running to her elbows, grinning straight down the lens, golden hour. **The hook frame.**
20. *"Yellow hands and a sticky chin."* — macro on yellow-stained fingers, then a sticky chin being wiped with the back of a wrist and made worse.
21. *"Take me back to mango season,"* — the courtyard from the terrace above, children scattered across it, the mango tree throwing a long shadow, wide drift.
22. *"Bare feet in the courtyard, let me in."* — bare feet running fast across hot stone, the camera low and level with them, dust kicking up, tracking.
23. *"Cousins on the terrace, cots in a row,"* — seven cots lined up on the terrace at night, seven children lying on them, a lantern at one end, wide and still.
24. *"Counting every star we did not know."* — one child pointing up, the others following the finger, a deep blue sky thick with stars, looking up over their heads.
25. *"The first rain came early that year,"* — a single fat drop hitting hot dust and vanishing into a dark coin, macro, one second.
26. *"Take me back to mango season, take me there."* — the whole courtyard from the gate, everyone in it, the tree, the wall, the doorway, the widest golden frame of the film.

### Verse 2 — the radio, the kites, the pickle jars

27. *"Grandfather's radio and the cricket score,"* — the transistor radio on a stool on the verandah, the grandfather's fingers on the dial, close-up, harsh bright afternoon.
28. *"The whole street leaning in to hear."* — neighbours and children gathered around the stool, all leaning the same way, a cheer breaking out at a boundary, medium wide, handheld.
29. *"An afternoon so long it had no ending,"* — a bleached white sky over the roofline, nothing moving, held four seconds longer than feels comfortable, static.
30. *"Kites above the roof, a string cut, a cheer."* — kites high in the white sky, one string going slack, children running to the roof edge to watch it fall, low angle then a whip to the edge.
31. *"Grandmother's hands and the smell of pickle jars,"* — the grandmother's hands spooning mango pickle into a glass jar and wiping the rim clean with a thumb, macro, soft morning light.
32. *"Drying in the sun on the top step."* — a row of glass jars on the top step catching the light, the courtyard out of focus beyond, close-up.
33. *"She said the mangoes know when you are coming,"* — the grandmother's hands pressing one perfect ripe mango into child Mahima's palms, a finger to her lips, their secret, close on the hands.
34. *"So she saved the sweetest one, a promise that she kept."* — the child holding the mango against her chest and looking up at her, the grandmother in soft three-quarter above, warm.

### Pre-chorus 2 — the wind turns

35. *"Then one evening the wind turned over,"* — the courtyard at dusk, dust lifting off the ground in a low spiral, the light changing colour inside the shot, handheld.
36. *"Dust rose up and the crows went quiet."* — the mango leaves turning silver-side up all at once, then crows leaving a wire in one movement, two cuts, slate grey sky.
37. *"Grandmother calling from the kitchen doorway,"* — her silhouette in the lit kitchen doorway, one arm out, calling, the wind pulling at her sari, medium.
38. *"Bring the clothes in, bring the clothes in, run."* — saris being hauled off a washing line at speed, the fabric snapping in the wind, handheld and fast.
39. *"We ran out to the courtyard laughing,"* — the children running the opposite way, out into the open instead of in, seen from the doorway, the last sun cutting under the cloud.
40. *"Faces up, we caught the first of it."* — seven faces turned up as the first drops land, slow motion on the rain only while the children move at speed, wide. **The first-rain shot.**

### Chorus 2 — the rain in the courtyard

41. *"Take me back to mango season,"* — rain hitting hot dust across the whole courtyard in slow motion, steam coming off the stone, wide.
42. *"Yellow hands and a sticky chin."* — a child's face in the rain with mango juice still on her chin, rinsing clean as we watch, close-up.
43. *"Take me back to mango season,"* — a child spinning with arms out in the downpour, the camera turning with her, medium.
44. *"Bare feet in the courtyard, let me in."* — bare feet stamping into a puddle forming across the stone, water flying, low and close.
45. *"Cousins on the terrace, cots in a row,"* — the cots on the terrace being dragged in fast under the rain, sheets over heads, laughing, wide from the stairs.
46. *"Counting every star we did not know."* — the terrace sky now solid cloud with no stars in it at all, the empty cot frames in the rain, static.
47. *"The first rain came early that year,"* — the grandfather under the verandah roof, watching them, smiling, not calling them in, medium, warm doorway light behind.
48. *"Take me back to mango season, take me there."* — the whole courtyard again from the gate, matched to shot 26, now dark and streaming with rain and better for it.

### Instrumental — the monsoon proper

49. Rain sheeting off the edge of a tin roof in an unbroken curtain, the courtyard behind it out of focus, long hold, silver-grey.
50. The courtyard flooded an inch deep, children stamping through it in a line, water thrown chest high, handheld, the only fully chaotic shot in the film.
51. The mango tree shaking under the weight of the rain, leaves dumping water, low angle looking up through the branches.
52. A paper boat riding the gutter along the side of the lane, a child's hand following it, then losing it, macro tracking.
53. The grandmother in the kitchen doorway with a steel cup of chai, watching, not saying anything, the rain between her and the camera, medium.
54. The rain thinning, then a single drop hanging on the underside of a leaf and letting go — the cut into the bridge, macro, first clearing light.

### Bridge — the house is smaller now

55. *"The house is smaller now, the tree is taller,"* — adult Mahima on a small city balcony in June, a photograph of the house open on her phone (composited), the heat visible in the air behind her, static.
56. *"His cycle still leans against the wall."* — the photograph fills the frame: the black bicycle against the courtyard wall, rust on the frame, the tyres flat, a still image held.
57. *"The cousins live in seven different cities,"* — a group chat lighting up on her phone (composited), seven names, the messages piling up, over-the-shoulder.
58. *"Nobody writes a letter, we just call."* — her thumb hovering over the chat, not typing, then the phone screen going dark in her hand, close-up.
59. *"But every June when the heat gets heavy,"* — her on the balcony rail, the city hazy and colourless behind her, a fan turning uselessly in the room through the door, wide.
60. *"And the first cloud comes in slow,"* — a single dark cloud crossing over the city rooftops, its shadow moving across her face, the first cool frame of the present day.
61. *"I stand out on my balcony in the city,"* — her turning her face up to it, exactly the posture of the children in shot 40, matched framing, close-up.
62. *"Face up, and I am nine, and I still know."* — a two-second transparent overlay of the child's face in the courtyard rain over the adult's face, then the adult alone, eyes still closed.
63. *"So this year I am buying the ticket,"* — her hands on her phone booking a train (screen composited), decided, no hesitation, close-up on the hands only.
64. *"This year I am going home."* — her stepping back inside off the balcony and starting to pack a small canvas bag, warmth coming back into the grade, medium.

### Final chorus — the train back

65. *"I am going back to mango season,"* — adult Mahima's hand on the window bars of a moving train, the same bars and the same grip as shot 1, matched frame. **The bookend.**
66. *"Yellow hands and a sticky chin."* — her face at the window, hair lifting in the air, golden late afternoon light moving across it, close-up.
67. *"I am going back to mango season,"* — fields running past the window, green then dry then green, the shadow of the train on the embankment, tracking.
68. *"Bare feet in the courtyard, let me in."* — intercut: the child running across the courtyard, and the adult's feet in sandals on the carriage floor, tapping.
69. *"Cousins on the terrace, cots in a row,"* — the terrace at night from the memory, then a beat of empty carriage seats opposite her, the same row shape, matched.
70. *"Same old stars, I still do not know."* — the sky through the train window as evening comes on, the first stars over the fields, her looking up at them.
71. *"The rain will come early, I can feel it,"* — cloud building on the horizon ahead of the train, the light going grey-gold, wide through the door of the carriage.
72. *"I am going back to mango season, back to the beginning."* — the outskirts of the town coming into frame, the water tank, the low roofs, her sitting forward, medium.

### Post-chorus — the textures

73. *"Sweet on the tongue, salt on the skin,"* — fast cuts on the beat: mango juice on a chin; a pinch of salt on a raw slice; a wet forearm.
74. *"Sun on the roof and the rain coming in."* — a hot tin roof in white sun; the same roof under rain; steam between them.
75. *"Sweet on the tongue, salt on the skin,"* — a mango stone stripped bare; yellow fingers spread; a red chilli flake on a thumb.
76. *"Take me back, take me back, let me in."* — the iron gate swinging open on an empty courtyard, held one beat longer, saturated saffron and green.

### Outro — nobody waiting

77. *"The train slows down at a station with one lamp,"* — the same one-lamp platform at dusk, empty now, the train pulling in, the lamp coming on as we watch, wide.
78. *"Nobody waiting, but I know the way."* — adult Mahima stepping down with the canvas bag, looking at the spot where the bicycle used to stand, then walking on, medium.
79. *"I walk the lane with my shoes in my hand,"* — her sandals hooked on two fingers, bare feet on the warm lane, tracking low behind her.
80. *"Somebody's children hanging off the gate."* — a new set of children on the same iron gate, shouting at something else entirely, not at her, medium.
81. *"The dust smells sweet and the air is heavy,"* — the courtyard as she comes through the gate, the last violet light in it, the low wall, the top step, nobody there.
82. *"And the mango tree is still there today."* — final shot: the mango tree, taller than it was, in the middle of the empty courtyard, one green mango on a low branch at the height a nine-year-old could reach. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first flute entrance, the arrival at the gate, each *"take me
back to mango season"*, the supermarket mango, the wind turning in shot 35,
the first rain in shot 40, the instrumental, *"this year I am going home"*,
the modulated *"I am going back"*, the post-chorus chant, and the last frame
on the tree. At 104 BPM a bar is 2.31 s; choruses cut on the bar, the
post-chorus on the half-bar, the outro two bars at a time.

**The mango hook.** The shareable cut is shots 19–22, vertical, with *"Take
me back to mango season"* on screen — child Mahima with a mango in both
hands is the frame that gets screenshotted. **The first-rain cut** is shots
39–41 with the seven faces turning up, and it is the one people will duet.
**The challenge:** post your own grandparents'-house summer — a gate, a
tree, a terrace, a first rain — to the post-chorus chant *"sweet on the
tongue, salt on the skin."* **The caption line:** *"She said the mangoes
know when you are coming."*

## 6. Quality-control checklist

- Seven children in every group wide — the gate, the water pot, the tree, the terrace cots, the rain — and the same seven faces throughout
- The child and the two adult looks are locked; the grandfather's face is seen and consistent, the grandmother's is not generated in close-up
- The bookend lands: the child's hand on the window bars in shot 1 and the adult's hand in the identical grip and framing in shot 65
- Shot 26 and shot 48 are the same camera position on the courtyard, golden and then rain-dark; shot 40 and shot 61 are the same face-up posture, child and adult
- No readable text anywhere — the station name board, shop signage, the supermarket label, the phone and the group chat are all composited or out of focus
- The present day is colourless until the cloud in shot 60, and warmth returns only from shot 64 onward
- Rain is a layered plate everywhere except the flooded-courtyard stamping shot; no CGI water on skin
- The last shot is locked-off on the tree with the single low mango and holds until the flute note ends
