# Wan 2.2 Shot List — "I'll Be There in Every Tomorrow"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. This song has 108 sung lines and 108 entries, numbered in order
from the intro to the last outro line. Timestamps come from the rendered WAV;
cut on the sung line. At 74 BPM a bar is 3.2 s, so most shots run one to two
bars.

## 1. Visual style

A warm, close family-album world that ages with the song. The grade starts
cool and grey at the first dawn, warms through the early years, goes golden
and saturated at the wedding, and ends in clean morning light. The camera
stays patient and close: slow dollies, static frames, handheld only in the
memory montage. Nothing is faked for drama; the light does the work.

| Section | Grade | Camera |
|---|---|---|
| Intro / first heartbeat | Cool grey dawn, one warm practical lamp | Static, slow push in |
| Verse 1 / the arrival | Soft window light, warm, low contrast | Medium, hands and faces |
| Chorus 1 / early years | Warm daylight, slightly washed, rain on glass | Static wide, slow tracking |
| Verse 2 / the grown daughter | Hard late sun, then soft porch light | Two-shot, static wide |
| Pre-chorus / photo wall | Warm hallway lamps, glass glare | Slow dolly along the wall |
| Chorus 2 / graduation | Stage-warm hall, string lights | Orbit, steadicam |
| Bridge / answered prayer | Low golden sun, long shadows, rim light | Slow move in on his face |
| Chorus 3 / wedding | Saturated golden hour, candles | Slow orbit, guest cutaways |
| Outro / morning | Clean warm morning, quiet | Locked-off wide |

## 2. Character bible — paste into every prompt

**Kai, late thirties** (the arrival, the early years)
> Same male character Kai, man in his late thirties, short dark hair neatly cut, light stubble, warm brown eyes, kind tired face, plain navy jumper over a white shirt, realistic cinematic photography, consistent identity, natural skin texture

**Kai, mid-fifties** (grey at the temples)
> Same male character Kai, man in his mid-fifties, dark hair going grey at the temples, short trimmed beard with grey through it, warm lined face, soft gentle eyes, brown wool cardigan over an open-collar shirt, realistic cinematic photography, consistent identity, natural skin texture

**Kai, sixties** (silver, the bridge and the outro)
> Same male character Kai, man in his sixties, silver hair thinning slightly at the crown, neat grey beard, deep smile lines, calm moved expression, linen shirt with sleeves rolled to the forearm, realistic cinematic photography, consistent identity, natural skin texture

**Ellie, baby** (the nursery and the delivery room)
> Same character Ellie, a newborn baby girl, very small, wrapped in a soft white blanket, a little red-faced, dark wisps of hair, eyes half open, realistic cinematic photography, consistent identity, natural skin texture

**Ellie, girl** (toddler, school, teenager at the car)
> Same female character Ellie, young girl and then teenager, bright dark eyes, round face, long brown hair in a loose plait, freckles across the nose, school jumper or a plain t-shirt and jeans, open happy expression, realistic cinematic photography, consistent identity, natural skin texture

**Ellie, grown woman** (the wedding and the grown-woman scenes)
> Same female character Ellie, young woman in her middle twenties, bright dark eyes, round face, long brown hair pinned up with loose strands at the temples, light natural makeup, ivory satin wedding dress or a soft blue dress, calm radiant expression, realistic cinematic photography, consistent identity, natural skin texture

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

Kai's look changes by age, not by wardrobe: the late-thirties look is the
one in the intro and verse 1; the mid-fifties look from verse 2 onward; the
sixties look from the bridge to the end. Ellie's three looks follow her
life: baby in the first two verse shots, girl through chorus 1, grown woman
from verse 2 and at the wedding. Other people (the nurse, the friends, the
guests, the new partner at the wedding) are seen from behind or in soft
focus. No readable faces are needed for anyone outside the family.

All screens, notifications, text, banners, card titles and signage are
composited in the edit. Generate them as blank or unreadable surfaces; the
model cannot render legible text.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Kai in all three ages and Ellie in all three looks with IP-Adapter or a
character LoRA; one reference set per age. Keyframes first; OpenPose for the dance and the porch steps; Depth for the bedroom compositions. 16:9 first; 9:16 for the optional phone-POV cut of chorus 1. Animate conservatively: breathing, hair moving in the light, rain on glass, a hand settling on a shoulder, a door opening slowly.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s. The memory montage in chorus 1 cuts faster, 2–3 s each.

## 4. Scene per lyric line

There is no `[instrumental]` tag in this song: `lyrics.txt` runs straight
from the intro to the outro with no lyric-free section, so no shots are
allocated to an instrumental stretch. Every entry below quotes one sung line.

### Intro — first heartbeat

1. *"I remember your first heartbeat"* — Kai (late thirties) on a plastic chair in a hospital corridor before dawn, hands clasped, a paper cup on the floor, cool grey light, static medium.
2. *"Before I knew your face,"* — the closed door of the room in the corridor, a thin strip of warm lamplight under it, slow push in, static.
3. *"A tiny promise growing"* — his face in profile through the door's narrow window, eyes lowered, listening, warm rim light, slow push in.
4. *"In a quiet, sacred place."* — the nursery window at first light, rows of empty cots, the glass cold and grey, locked-off wide.

### Verse 1 — the arrival

5. *"I wondered who you'd become one day,"* — Kai at a kitchen window at dawn, a mug in both hands, looking out at a grey street, handheld, soft cool light.
6. *"What dreams would fill your eyes,"* — close-up of his reflection in the window glass over the street, a faint warm glow behind it, static.
7. *"But nothing could prepare me"* — the delivery room, a nurse's hands guiding him to sit, Kai's face turning toward the bed, medium, soft window light.
8. *"For the moment you arrived."* — the nurse lifting a bundled newborn toward him, the blanket edge in frame, shallow focus, warm.
9. *"They placed you in my waiting arms,"* — medium close on Kai's hands taking the weight, his fingers spreading under the blanket, slow tilt up.
10. *"So fragile, warm and new,"* — the newborn Ellie in his arms, her small fist against his shirt, extreme close-up, soft warm light.
11. *"The world became a different world"* — a slow pull back from the two of them to the window, the morning light filling the room, wide.
12. *"The moment I saw you."* — Kai looking down, his eyes wet, a short laugh, medium close, locked off.
13. *"I held my breath and whispered,"* — night kitchen, a baby monitor's green light on the table, Kai in the doorway, head bent, still, static medium.
14. *"I will give you all I can,"* — Kai sitting at the table, one hand flat on the wood, the other on his chest, lamp light, slow push in.
15. *"And in that very instant, girl,"* — the monitor's light blinking, cut to the cot, the blanket moving slightly, shallow focus, warm lamp.
16. *"I became a better man."* — Kai lifting his head and standing, shoulders settling, the lamp catching the grey at his temples as a moment of stillness, static wide.

### Chorus 1 — the early years

17. *"I'll be there in every tomorrow,"* — a toddler Ellie on the living-room rug, Kai (late thirties) on his knees beside her, rain on the window behind, static wide.
18. *"In the sunshine and the rain."* — the same window, the rain easing, a shaft of sun across the rug, the two of them in the light, slow tracking.
19. *"I'll be there through every victory,"* — Ellie, six, on a playground frame at the top, arms up, Kai below with his hands out, bright daylight, handheld.
20. *"And beside you through the pain."* — a scraped knee, Kai kneeling on the path, a plaster in his fingers, Ellie's face crumpling then steadying, medium, warm.
21. *"When you're dancing through your happiest days,"* — the kitchen at breakfast, Ellie dancing with a spoon in her hand, Kai laughing in the background, handheld, sun through the window.
22. *"When you're searching for the way,"* — Ellie at the bottom of the stairs with a map of the school, Kai pointing up the street, static wide.
23. *"My love will be a steady light"* — a lamp left on in the hallway at night, the light falling across the stairs, a small figure asleep on the landing, static.
24. *"That never fades away."* — the hallway lamp from the stairs, slow push in along the light, warm, a soft dissolve.
25. *"You are the dream I never knew"* — Kai at the sink looking out, a child's drawing stuck to the window, warm grey light, medium.
26. *"My heart was waiting for,"* — Ellie's first day at school, a school gate in the morning, Kai crouched beside her, her hand in his, slow push in.
27. *"My precious little daughter,"* — Ellie in a yellow raincoat turning back at the gate to wave, bright and wet pavement, medium, handheld.
28. *"You are what I'm living for."* — Kai on the pavement after the gate, watching her go, a hand raised, the street empty behind him, static wide.
29. *"And though the years may carry you"* — a long tracking shot down a school corridor, lockers and light, the corridor lengthening ahead, wide.
30. *"To places far from home,"* — a train platform, a single suitcase set down, Kai at the far end, the train's windows warm, static wide.
31. *"You'll never face this life alone,"* — Kai's hand on the back of a bench, Ellie's shadow beside his on the platform, warm late light, medium.
32. *"You'll never face it alone."* — the two of them walking together on a bridge over a river at dusk, the lights coming on, slow tracking from behind.

### Verse 2 — the grown daughter

33. *"When you grow into a young woman"* — Ellie, seventeen, on the front steps of a house with a bag over her shoulder, Kai in the doorway behind her, warm late afternoon, static medium.
34. *"With a world beneath your feet,"* — low angle on her trainers on the front path, the pavement and the street ahead, sun on the stones.
35. *"When you find the dreams you're meant to chase"* — Ellie at a desk covered in brochures, pen in hand, a window of open sky behind her, handheld.
36. *"And people you will meet,"* — a crowded street of strangers seen through a car window, Ellie's reflection in the glass, shallow focus.
37. *"I won't hold you back from flying,"* — Kai at the car boot lifting a suitcase in, not letting it go, one hand still on the lid, medium two-shot.
38. *"I won't ask you not to go,"* — Kai stepping back from the car with his hands at his sides, open, Ellie in the driver's seat, static.
39. *"I'll be proud of every distance"* — the car pulling away down a long road, the sun low, the frame held wide on the empty drive.
40. *"That your brave heart dares to know."* — Kai on the porch with a hand up, slowly lowering it, a small smile, warm dusk light, locked off.
41. *"But if a dream should break apart,"* — a phone screen lit on a kitchen counter (composited blank), a cup of tea gone cold beside it, cool night light, static.
42. *"If someone makes you cry,"* — Ellie sitting on the back step at night, knees up, the screen light on her face, shallow focus, cool blue.
43. *"If you feel the road is empty"* — a long empty country road, headlights passing and gone, wide, night.
44. *"And the stars forget to shine,"* — a dark sky with a few stars coming through, the porch light at the edge of frame, slow tilt up.
45. *"You can call the name of Daddy,"* — Ellie on the back step, mouth open to speak, her face half in shadow, medium, static.
46. *"And I'll answer where I am,"* — Kai (mid-fifties) in the doorway in a dressing gown, the hallway light behind him, turning toward the step, medium.
47. *"No matter how old you become,"* — Ellie, grown now, sitting beside him on the step as the sun rises over the roofs, a long wide shot.
48. *"You'll always be my child."* — the two of them on the step, his arm around her shoulders, her head on his shoulder, golden dawn, locked off.

### Pre-chorus — the quiet promise

49. *"I cannot promise perfect days,"* — a hallway wall of family photographs, the lamps warm on the glass, Kai (mid-fifties) standing in front of it, slow dolly along the wall.
50. *"Or shelter from the storm,"* — a rain-streaked window in the hallway, the photographs behind the wet glass, rack focus from the window to the frames.
51. *"But I can promise you my love"* — Kai's hand touching one frame, a baby in a christening gown, two fingers on the glass, extreme close-up.
52. *"Will always keep you warm."* — Kai in front of the wall, his hand dropping to his side, the warm light across his shoulders, slow push in.

### Chorus 2 — the graduation

53. *"I'll be there in every tomorrow,"* — a graduation hall, Ellie in a cap and gown walking up the aisle, the crowd rising, stage-warm light, orbit begins.
54. *"In the sunshine and the rain."* — the hall's tall windows, a light rain outside, sun breaking through over the rooftops, the crowd turned toward the stage.
55. *"I'll be there through every victory,"* — Ellie receiving her certificate, the stage lights on her face, the hall applauding, steadicam push in.
56. *"And beside you through the pain."* — reuse shot 20 with the scrape replaced by a bandaged hand on a dinner table, Kai's hand over hers, tighter.
57. *"When you're dancing through your happiest days,"* — a dance floor in a warm room, string lights overhead, Ellie in a long dress turning with friends, steadicam pass.
58. *"When you're searching for the way,"* — Ellie at a table with a notebook and a map, looking up at the ceiling, Kai in the corner of the room watching, static wide.
59. *"My love will be a steady light"* — a single lantern on a windowsill outside the hall, the glow in the glass, slow push in.
60. *"That never fades away."* — reuse shot 24, the hallway lamp, now the lamp on the table in the dance room, warmer, tighter.
61. *"You are the dream I never knew"* — Kai in the crowd at the dance, watching her, a glass in his hand he forgets to drink from, medium.
62. *"My heart was waiting for,"* — Kai's hand over his mouth in the crowd, his eyes bright, steadicam orbit closing on his face, close.
63. *"My precious little daughter,"* — Ellie turning from the dance floor to look back at him, a laugh on her face, warm light, medium close.
64. *"You are what I'm living for."* — Kai and Ellie in a quiet corner of the dance room, forehead to forehead for one beat, static, warm.
65. *"And though the years may carry you"* — a slow dolly down the empty corridor of the hall, the doors at the end open to a bright night, wide.
66. *"To places far from home,"* — a taxi's lights on a dark road at night, the back window with a face in it, distant, wide.
67. *"You'll never face this life alone,"* — Kai on a bench in the hall's courtyard, the lantern lit beside him, a second place on the bench left free, static.
68. *"You'll never face it alone."* — the courtyard gate swinging shut in the breeze, the bench and the lantern in the foreground, locked off.

### Bridge — the answered prayer

69. *"And when my hair is silver,"* — Kai (sixties, silver) on a porch at sunset, the light catching his hair, a slow move in, golden.
70. *"And my footsteps have grown slow,"* — his shoes on the porch boards, slow steps across the wood to the rail, low angle, long shadows.
71. *"I'll still see the little girl"* — a flash of the school gate from shot 26, grainy and warm, then back to the porch.
72. *"Who taught my heart to glow."* — Kai at the rail, the sun on his face, eyes closing for one breath, rim light, medium close.
73. *"I'll still hear your laughter"* — Ellie (grown) on the porch steps, laughing at something off-frame, her head thrown back, warm, medium.
74. *"In the quiet of the night,"* — the porch at night, the light on, the sky going deep blue, one moth at the lamp, static wide.
75. *"And every memory of you"* — a montage of three still-warm frames (the rug, the school gate, the car), each held two beats, dissolving.
76. *"Will make the darkness bright."* — the porch light coming on as the frame darkens around it, Kai's silver hair catching the lamp, locked off.
77. *"You gave me more than happiness,"* — Ellie walking up the porch steps with a small child on her hip, Kai reaching for the child's hand, warm late sun.
78. *"You gave my life a name,"* — a close-up of Kai's hand taking the child's small hand, the two hands together, shallow focus, golden.
79. *"You took my fear and tiredness"* — the brass comes in here: Kai's face shifting from tired to open as the frame tilts up to the sky, slow move in.
80. *"And turned them into flame."* — the sun flaring low across the porch, the frame almost white at the edge, warm, held.
81. *"You are my greatest blessing,"* — Kai and Ellie in a two-shot at the top of the steps, her hand on his arm, the child in her other arm, wide golden frame.
82. *"My answered prayer come true,"* — extreme close-up of Kai's face, his eyes open and bright, the grey at his temples lit by the sun.
83. *"There is no love in all this world"* — a wide shot of the porch from the garden, the house and the family in the frame, the sun going down behind the roof.
84. *"Like the love I have for you."* — Kai looking to the camera, the smallest smile, the sun gone, the porch light the only light, locked off.

### Chorus 3 — the wedding

85. *"I'll be there in every tomorrow,"* — Ellie in white at the top of an aisle, a tent wall glowing gold, the guests turning, slow orbit begins.
86. *"In the sunshine and the rain."* — a tent wall with rain streaking the canvas, the warm light inside, the bride's veil lifting in a breeze, wide.
87. *"I'll be there through every victory,"* — the first dance begins, Kai (sixties) taking her hand, the floor opening around them, steadicam.
88. *"And beside you through the pain."* — reuse shot 62 with the wedding guests' faces in soft focus, Kai's hand on her back, tighter.
89. *"When you're dancing through your happiest days,"* — the wide dance floor under string lights, the two of them turning slowly, wide orbit, saturated gold.
90. *"When you're searching for the way,"* — a close-up of Kai's shoes on the floor keeping time with hers, a slow step each beat, static, low.
91. *"My love will be a steady light"* — the candle on the long table, its flame steady, the room softer behind it, slow push in.
92. *"That never fades away."* — a long table of guests laughing, candlelight on the cloths, a child's hand reaching for a sugared almond, wide.
93. *"You are the dream I never knew"* — Kai (sixties) at the edge of the floor, looking at her, a glass in one hand, the other resting on the rail, medium.
94. *"My heart was waiting for,"* — Ellie turning in her dress, her face bright, catching his eyes across the floor, steadicam closes in.
95. *"My precious little daughter,"* — the father of the bride's hand on her shoulder as they dance, the two faces in soft focus, close and warm.
96. *"You are what I'm living for."* — Kai and Ellie in a clean two-shot, both smiling, the light full on them, held for two beats.
97. *"And though the years may carry you"* — a slow dolly out of the tent through the open flap into the evening garden, lanterns in the trees, wide.
98. *"To places far from home,"* — a car's headlights in a long drive at dusk, the wedding car leaving the gate, the frame held wide.
99. *"You'll never face this life alone,"* — the gate of the garden, Kai standing by it with a hand on the post, the lanterns behind him, medium.
100. *"You'll never face it alone."* — Kai and Ellie's silhouettes against the tent's gold glow, side by side in the frame, a last slow push in.

### Outro — the morning

101. *"So close your eyes, my baby girl,"* — Kai (sixties) in a rocking chair by a nursery window at dawn, a folded blanket on the chair arm, the cot gone, locked-off wide.
102. *"Let tomorrow softly start,"* — Ellie, grown, walks in and sits down on the floor against the chair, her head coming to rest on his knee, medium.
103. *"No matter where your journey goes,"* — dawn light moving slowly across the bare floorboards toward the two of them, a slow pan, quiet.
104. *"You'll always own my heart."* — Kai's hand settling on her hair, his eyes closing, extreme close-up of the hand and the silver at his wrist.
105. *"I'll be there in every tomorrow,"* — a slow dissolve through the years in the same window light: the rug, the school gate, the car, the porch, the wedding gold, each held one beat.
106. *"As I have been from the start,"* — the first intro frame returns, the nursery window at dawn, cold and grey, then warming as the light takes it.
107. *"My daughter, my joy, my little one,"* — a close-up of Ellie's hand taken into his, the two hands in the warm light, shallow focus.
108. *"You are my forever heart."* — the final locked-off wide: the window, the rocking chair, two silhouettes, held through the fade; no text.

## 5. Edit and the challenge

Bar length is 3.2 s at 74 BPM. Markers at: the first vocal entrance (shot 1),
the first chorus (17), the first "I'll be there in every tomorrow" in the
wedding (85), the bridge's brass entry on "You took my fear and tiredness"
(79), "My answered prayer come true" (82), and the final outro line (108).
No instrumental break: the cut between chorus and bridge is on the orchestra
opening, not on a lyric-free gap, so mark it on the brass swell.

**Shareable cut.** The bridge's porch frames (shots 69–84) cut together as a
vertical 9:16 piece with the line *"My answered prayer come true"* on screen,
no music swap, the sung lines underneath. The grey-haired hand taking the
small hand (shot 78) is the still.

**The challenge.** Post a short family-album clip: a photo of you with someone
you love at one age, then the same person at another, with *"I'll be there in
every tomorrow"* over it. Invite people to post their own before-and-after
family photo with the same line. Keep it simple; the song carries the feeling.

## 6. Quality-control checklist

- Kai's three ages in the right sections: late thirties through verse 1 and the first chorus; mid-fifties from verse 2 to chorus 2; sixties from the bridge to the outro; silver only from the bridge on
- Ellie's looks in order: baby in the arrival and the nursery, girl through chorus 1 and the graduation, grown woman from verse 2 and at the wedding
- The grade warms steadily from the cool dawn intro to the golden wedding, then clean morning in the outro; no cold frames after the bridge
- The bridge's silver-haired porch shots (69–84) are the warmest frames of the porch sequence; the outro returns to the intro window
- No readable faces for anyone outside the family; the nurse, friends and guests are seen from behind or in soft focus
- All UI, banners, card titles and signage composited; no model-generated text
- No distorted hands, especially the newborn's hands and the hand-on-hand shots (78, 104, 107)
- The last shot (108) is locked-off and holds through the fade
