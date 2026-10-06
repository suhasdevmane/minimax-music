# Wan 2.2 Shot List — "Small Hands, Big World"

**One shot per lyric line**, 114 entries, built from the scene-by-scene
direction in [`source/original-submission.md`](../source/original-submission.md).
Timestamps come from the rendered WAV; cut on the sung line. At 70 BPM a bar
is 3.43 s, so most shots run one to two bars.

## 1. Visual style

Warm, unhurried family realism. Two worlds that share one house: the **day** is
honest, natural window light, a kitchen table, a playground, a porch; the
**night** is a single warm lamp against deep blue. The camera is close and
human, at the child's eye level whenever possible, and it holds still more
often than it moves. The house with seven windows is the motif that returns:
it is drawn on paper, seen from the street, and lit at the end. Stars and a
rainbow are the second motif. Nothing is glossy. Skin, wool, wet tarmac and
denim should look like themselves.

| Section | Grade | Camera |
|---|---|---|
| Intro / kitchen table | Warm window light, soft dust in the air | Overhead, slow push |
| Verse 1 / rug and kitchen | Warm, soft daylight | Medium two-shots, close inserts |
| Chorus 1 / porch at dusk | Blue-hour to first stars, warm porch lamp | Wide, slow push on hands |
| Verse 2 / hallway | Soft ceiling light, warm pool on the floor | Low static wide, slow tracking |
| Verse 3 / playground | Overcast, then a break of low sun through rain | Handheld tracking, medium |
| Pre-chorus / kitchen sink | Warm, window going dark | Medium two-shot |
| Chorus 2 / porch at night | Deep blue, stars, one warm lamp | Static wide, close on hands |
| Bridge / bedroom floor | One bedside lamp, hard warm shadows | Static low two-shot, slow drift |
| Chorus 3 / the day in montage | Bright, golden, full | Quick cuts, one per phrase |
| Outro / porch | Last blue of dusk | Locked-off wide |

## 2. Character bible — paste into every prompt

**Kai** (look 1: kitchen, playground, porch at dusk)
> Same male character Kai, man in his late thirties, short beard with a little grey at the chin, warm brown eyes, denim jacket over a plain grey t-shirt, kind tired face, relaxed listening expression, kneeling to his daughter's height, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (look 2: bedroom, porch at night)
> Same male character Kai, man in his late thirties, short beard with a little grey at the chin, warm brown eyes, the same denim jacket open over a dark henley with the sleeves pushed up, soft tired gentle expression, realistic cinematic photography, consistent identity, natural skin texture

**Ellie** (look 1: kitchen, rug, hallway, porch)
> Same female character Ellie, girl about six years old, light brown hair in two pigtails, a bright red knitted jumper, a yellow pencil tucked behind one ear, a few freckles, focused and serious expression, realistic cinematic photography, consistent identity, natural skin texture

**Ellie** (look 2: playground, the scraped knee)
> Same female character Ellie, girl about six years old, light brown hair in two pigtails with one coming loose, the same bright red knitted jumper with dust on the sleeves, a scraped knee with a small graze, wet and determined expression, realistic cinematic photography, consistent identity, natural skin texture

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

There is no screen, phone or app in this video. Any words on paper, chalk or
the drawings are added in the edit, never generated, because the model cannot
render legible writing. The pencil behind Ellie's ear and the red jumper are
props that must stay consistent in every frame where she appears.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Kai and Ellie in their looks with IP-Adapter or a character LoRA, and
check the child's likeness against her approved keyframe before animating
any close-up. Keyframes first; OpenPose for the kneeling and the stair and
playground shots; Depth for the hallway and kitchen compositions. 16:9 for the
whole video. Animate conservatively: breathing, hair moving in a draft, a
pencil moving across paper, a hand reaching, water running, rain falling.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the pencil

1. *"You hold a pencil like a captain"* — Ellie at the kitchen table, close-up on her small fist gripping a pencil hard like a steering wheel, Kai's hand out of focus at the edge of frame, warm window light, static close.
2. *"Gripping hard the wheel,"* — tight on her knuckles and the pencil moving across the paper, a slow tilt up to the drawing, the pencil scratch audible under the line.
3. *"You draw a house with seven windows"* — overhead of the paper, the seven windows drawn one at a time as the pencil moves, locked-off overhead, warm.
4. *"And a garden of a field."* — Ellie sitting back, pencil tucked behind her ear, looking down at the drawing with quiet pride, a small smile, medium close, slow push.

### Verse 1 — the drawing and the puzzles

5. *"You say, this one is for Daddy,"* — Ellie slides the drawing across the table toward Kai, medium two-shot, Kai kneeling beside her chair so their eyes are level.
6. *"This one's where the flowers grow,"* — extreme close-up of her finger pointing at a row of crayon flowers, Kai's hand reaching in from the edge.
7. *"Then you add a little rainbow"* — her crayon arcing a rainbow over a yellow sun, close on the paper, warm.
8. *"To a sky I used to know."* — Kai watching the drawing, a private smile, medium close, slight rack focus from the paper to his eyes.
9. *"You solve your tiny puzzles"* — on the rug, Ellie's hands sorting wooden jigsaw pieces, low overhead, soft daylight from the window.
10. *"With a focus fierce and bright,"* — her face close, lips pressed together, eyes narrowed, the room soft and out of focus behind her.
11. *"You turn the pieces over"* — insert of her small hands turning a piece face up, then a second, quick fingers, the picture starting to show.
12. *"Till the picture comes to light."* — the puzzle completed, a tabby cat in a tree, wide shot with Kai's hand flat on the rug beside her, daylight across the floor.
13. *"You may be small enough to fit"* — Kai lifting her onto his knee at the kitchen table, her small frame against his chest, medium two-shot, warm.
14. *"Inside my waiting arms,"* — the hug, camera circling slowly once around them, his arms closed around her, her face against his shoulder, soft.
15. *"But there is something powerful"* — Ellie pulling back to look at him, serious, chin up, pencil still behind her ear, medium close, low angle.
16. *"In all your little charms."* — her grin with a gap where a front tooth is missing, her head tilted to one side, close, warm, a slight handheld drift.

### Chorus 1 — the porch

17. *"Small hands, big world,"* — wide shot of Kai and Ellie walking out of the front door onto the porch, her hand held in his, the brush kit entering, locked wide, dusk beginning.
18. *"Big dreams in a little girl."* — close on their joined hands as they go down the porch steps, her fingers wrapped around two of his, slow push-in.
19. *"You carry more light"* — Ellie with a rolled drawing under one arm, the porch lamp switching on behind them with a warm glow across the boards.
20. *"Than the stars in the night."* — a slow tilt up to the first star over the rooftop, Ellie's face turned up toward it, deep blue sky, static.
21. *"You teach my heart to see"* — Kai's profile looking down at her, the steel guitar line rising, medium close, his eyes bright.
22. *"Who I was and who I can be."* — a two-second cutaway to a faceless memory of a porch step, cropped at the shoulders, then back to Ellie's face in the lamp light.
23. *"Small hands, big world,"* — the porch rail, her small hand resting on it next to his big hand, both in frame, a slow dolly along the rail.
24. *"You are my precious girl."* — Kai crouched on the step, hands on her shoulders, looking at her, medium two-shot, warm porch light.
25. *"You make me laugh,"* — Ellie laughing with her mouth open, Kai laughing with her, handheld close, warm and unposed.
26. *"You make me strong,"* — Kai standing up and pulling her up with him, both on the step, medium shot, his shoulders squaring.
27. *"You show me where my heart belongs."* — a slow push onto their hands clasped on the rail again, the house lit behind them through the front window.
28. *"And every day I understand"* — Kai's eyes closing for one beat in the lamp light, medium close, held.
29. *"A better life begins"* — the front door opening onto a warm hallway, Ellie running in ahead of him, the frame filling with interior light.
30. *"With your small hands in my hands."* — back on the porch: his hands around hers, both held together at the height of their chests, close, static, locked.

### Verse 2 — the hallway and the animals

31. *"You lined your animals up"* — the hallway, plush animals in a row across the floorboards, wide static low angle from the doorway, ceiling lamp.
32. *"Across the hallway floor,"* — Ellie on her knees placing a stuffed rabbit at the end of the line, slow tracking along the row.
33. *"The lion was the teacher,"* — Ellie holding the lion up in front of Kai, who is crouched in the doorway, close, his face listening.
34. *"The rabbit guarded the door."* — the rabbit propped against a shoebox that serves as the door, Kai's hand touching the box while she explains, medium.
35. *"The little bear was sleeping,"* — the bear under a folded blanket, Ellie tucking the corner in with a serious face, close insert, soft.
36. *"The elephant was late,"* — Ellie holding a toy clock up beside the elephant, a comic-serious beat, medium close, ambient room sound.
37. *"And you explained the whole plan to me"* — Ellie with hands on her hips, explaining, Kai nodding, medium two-shot, the corridor in soft shadow.
38. *"With a serious little face."* — tight close-up on Ellie's face, eyebrows drawn together, earnest, static.
39. *"You organise the whole world"* — wide shot of the hallway with the animals and both of them, Ellie spreading her arms to take in the whole row, slow push-in.
40. *"In your wonderfully bright way,"* — a close on her bright eyes, a smile starting, warm lamp, very slight handheld.
41. *"You make a home from anything,"* — she builds a den from couch cushions and a sheet in the living room, Kai peeking in at the entrance, wide static.
42. *"A game from any day."* — inside the den: Kai crawling in beside her, a torch in her hand, low angle, the sheet glowing warm.
43. *"Your mind is full of questions,"* — Ellie asking something, Kai's head tilted, close on his face as he thinks, a soft chuckle.
44. *"Your spirit full of flight,"* — Ellie jumping off the bottom stair with her arms out, slow motion, a wide frame, daylight from the front door.
45. *"You find a hundred possibilities"* — three quick cuts, each held a beat: a cardboard box turned into a boat, a wooden spoon as a microphone, a sock puppet on her hand. Close, bright.
46. *"Inside a single night."* — the den at night, the torch beam making a circle on the sheet ceiling, her shadow and Kai's shadow side by side, warm.

### Verse 3 — the falls and the courage

47. *"Sometimes you fall and scrape your knee"* — the playground in late afternoon, Ellie running and tripping, a medium tracking shot as she goes down on the wet tarmac.
48. *"And tears begin to rise,"* — extreme close on her knee, a small graze, her lower lip beginning to shake, soft focus.
49. *"You look at me, then stand again"* — her face turning toward the bench where Kai sits, a wide shot over the distance, him half-rising from the bench.
50. *"With courage in your eyes."* — extreme close on her eyes, wet, then steadying, the playground blurred behind her.
51. *"I kiss the place that hurts you,"* — Kai kneeling on the tarmac, bending to her knee, close on his face and the scrape, soft.
52. *"But you're stronger than the pain,"* — Ellie standing up on her own, wiping her face with the back of her hand, low angle, sunlight on her.
53. *"You take a breath and run again"* — Ellie running back across the playground, handheld tracking from the side, her breath visible in the cool air.
54. *"Into the sun and rain."* — low sun breaking through the rain, a rainbow arching over the slide, she runs straight into the light, wide.
55. *"I wish I could protect you"* — Kai on the bench, elbows on his knees and hands clasped, a slow push onto his face in the dusk light, quiet.
56. *"From every difficult road,"* — a tight insert on the cracked tarmac path, puddles holding the sky, static, slow.
57. *"Carry every burden"* — Kai lifting Ellie onto his shoulders on the walk home, medium shot from behind, both walking away down the path.
58. *"And lighten every load."* — the two of them crossing a footbridge, a shopping bag swinging between them, wide, warm, soft.
59. *"But life will have its lessons,"* — the kitchen table, Ellie colouring a hard page with her tongue out, Kai beside her, overhead.
60. *"And you'll learn them as you grow,"* — a door frame with pencil height marks, Ellie standing against it, Kai's hand flat on her head measuring, close.
61. *"I'll be beside you, cheering"* — Kai at the playground fence with both arms up, cheering as Ellie climbs the frame, medium wide, bright.
62. *"Every step you choose to go."* — Ellie at the top of the climbing frame looking down, choosing her next handhold, Kai's hands out below her, static wide.

### Pre-chorus — the sink

63. *"You don't know it, little darling,"* — the kitchen sink, Kai washing dishes, Ellie drying a cup on a step stool beside him, medium two-shot, the window dark behind them.
64. *"But you rescue me each day,"* — close on Kai's hands in the water, then tilting up to his face as he turns toward her.
65. *"You bring my tired heart back home"* — Ellie reaching up to hug his soapy wet arm, close, soft.
66. *"In your own special way."* — Kai laughing, lifting her up and setting her on the counter beside the sink, medium, warm.

### Chorus 2 — the porch at night

67. *"Small hands, big world,"* — the porch in full night, Ellie asleep on a blanket on the swing with her drawing on her chest, wide static.
68. *"Big dreams in a little girl."* — Kai sitting beside her on the swing, one hand on the chain, the other resting on the blanket, medium.
69. *"You carry more light"* — the porch lamp behind them, a thin line of light across the blanket, close on her sleeping face.
70. *"Than the stars in the night."* — the stars coming out one at a time, a slow tilt up, the frame brightening gradually.
71. *"You teach my heart to see"* — Kai looking up at the sky, his face lit by the stars, close profile, slow.
72. *"Who I was and who I can be."* — a two-second faceless cutaway to an old porch in memory, then back to the swing in blue night.
73. *"Small hands, big world,"* — a close on the blanket: her small hand and his big hand, the swing creaking faintly, static close.
74. *"You are my precious girl."* — Kai leaning down to kiss the top of her head, eyes closed, soft lamp light, medium close.
75. *"You make me laugh,"* — Ellie stirring in her sleep and smiling, Kai smiling back at her, two-shot in the lamp light.
76. *"You make me strong,"* — Kai standing and carrying her inside, her head on his shoulder, medium shot from the porch door.
77. *"You show me where my heart belongs."* — the hallway, Kai carrying her past the line of animals on the floor, slow tracking, warm.
78. *"And every day I understand"* — Kai stopping in the bedroom doorway, the nightlight on, looking at her in the bed, medium, the room dim and blue.
79. *"A better life begins"* — Kai tucking the blanket in, a small drawing pinned above the bed showing seven windows, close on the drawing.
80. *"With your small hands in my hands."* — his hand in hers on the duvet, both still, the nightlight glow, locked close.

### Bridge — the bedroom floor

81. *"If the world tells you you're too small,"* — the bedroom floor after bedtime, Kai sitting beside her bed, the wall of drawings behind, a low lamp, medium two-shot.
82. *"Remember what I know,"* — Kai speaking close to the lens, slow, a quiet face, locked close, a hard lamp shadow across him.
83. *"The strongest rivers start as drops,"* — insert: a crayon drawing of a river with raindrops falling into it, held on the wall, slow push.
84. *"The tallest trees once grew low."* — insert: a drawn tree with a small figure beside it, pencil marks, lamp light across the paper.
85. *"A seed can split the earth apart,"* — a macro of a seed cracking dark soil in a jar on the windowsill, slow, close.
86. *"A spark can light the sky,"* — a single lit birthday candle, the flame reflected in Ellie's eyes, close, warm.
87. *"And you have more inside your heart"* — Ellie's hand flat on her chest, Kai's hand over hers, close, slight rack focus.
88. *"Than you can see tonight."* — the window: a dark sky with the first star, a slow tilt across the glass, a faint reflection of them both.
89. *"So dream as wide as oceans,"* — Ellie lying on the floor and drawing a long crayon line across the paper, arms wide, wide shot, lamp glow.
90. *"Walk as far as you can see,"* — a cutaway to a beach at dusk, tiny figures walking into the distance, slow, wide.
91. *"Be gentle with the world, my child,"* — Kai's hand brushing Ellie's hair back from her forehead, medium close, soft, slow.
92. *"But never hide your wings."* — Ellie standing on the bed with a cotton cape tied at her shoulders, arms lifted, silhouetted by the nightlight, wide low.
93. *"And if you ever lose your way,"* — slow close on Kai's face, the lamp half-lighting him, serious and tender, his lips barely moving.
94. *"I'll help you understand,"* — Kai and Ellie side by side on the floor, backs against the bed, both looking at the same drawing, medium two-shot.
95. *"You'll always have your father's voice"* — close on Kai speaking, his voice near the lens, the drawing behind him soft in focus, locked.
96. *"And a place within his hands."* — Ellie's small hand pressed into the middle of his big palm, extreme close, held, the lamp warm.

### Chorus 3 — the day in one montage

97. *"Small hands, big world,"* — quick cut: Ellie on the swing in morning light, legs pumping, wide and bright.
98. *"Brave heart in a little girl."* — Ellie climbing to the top rung of a climbing frame, low angle, sky behind her, bright.
99. *"You carry more hope"* — Ellie carrying a watering can across the garden, a small figure under a huge sky, wide.
100. *"Than the wildest wind can blow."* — the paper kite she is flying on the field, held wide with the wind pulling it, bright sky.
101. *"You teach my heart to see"* — Kai at the garden gate watching her, his face opening up in the sunlight, medium close.
102. *"The best that life can be."* — Ellie sitting on the grass with a drawing of the house with seven windows, extended wide, golden light.
103. *"Small hands, big world,"* — Ellie at the foot of the stairs with her shoes on the wrong feet, Kai kneeling in front of her with his hands ready, static, warm.
104. *"You are my precious girl."* — Kai tying her laces in a double knot, close on his hands and her small shoe pulled tight, warm.
105. *"You make me laugh,"* — Ellie wiggling her toes and giggling, Kai pulling a silly face, medium two-shot in sunlight.
106. *"You make me strong,"* — Kai standing up, Ellie grabbing his hand and running for the front door, his back to camera, handheld.
107. *"You are the reason I belong."* — the front door opening onto a bright street, the two of them stepping out together, wide, morning.
108. *"And every day I understand"* — Kai pausing on the path, looking back at the house and then at her, eyes soft, medium close, slow.
109. *"A better life begins"* — the house from the street in the early evening, every window lit, the seven windows of the drawing echoed in the frame, wide static.
110. *"With your small hands in my hands."* — their hands swinging between them as they walk down the path, close, bright, tracking.

### Outro — the porch, last light

111. *"Small hands, big world,"* — the porch at dusk, locked-off wide, Ellie on the top step with her drawing, Kai sitting beside her, the last blue light.
112. *"My forever little girl."* — Ellie leaning her back against Kai's knee, her head turned up toward him, close, soft.
113. *"No matter where you stand,"* — a slow pull-back, the two of them small against the porch and the open sky, locked off.
114. *"You'll always hold my hand."* — extreme close on their hands on the step, held, then black on the last guitar note.

**Instrumental:** none. This song has no instrumental section; every
lyric line is sung, and the bridge is sung throughout.

## 5. Edit and the challenge

Bar length at 70 BPM is 3.43 s. Markers at: the first vocal entrance (shot 1);
each "small hands, big world" (shots 17, 23, 67, 73, 97, 103, 111); the bridge
entrance and the promise, "I'll help you understand" (shot 94); the drawn house
with seven windows as the last image of the day (shot 109); and the final
"hand" (shot 114). The outro holds on the last guitar note with no fade to
text.

**The shareable cut.** A vertical 9:16 crop of the chorus 1 porch sequence
(shots 17–30) with the caption *"small hands, big world"* on screen, is the
short that travels: a father's hand around a child's hand, in one held frame.

**The challenge.** "Draw your house with the most windows." People post a
child's drawing of their own house, tag a parent, and play the chorus under
it. The pencil and the seven windows are the shareable frame.

## 6. Quality-control checklist

- Kai's denim jacket is present in every father shot of look 1; the dark henley with sleeves pushed up is used only in the night shots (look 2)
- Ellie's pencil is behind her ear in every drawing and kitchen shot (1–4, 5–16, 59, 102); the red jumper is worn in every shot of Ellie awake, and the night shots 78–80 and 92 use the same red jumper under a blanket or cape
- The house with seven windows is correct in shots 3, 79, 102 and 109: seven windows, no more, no fewer
- Hands are checked on every close: the joined hands (18, 23, 30, 73, 80, 96, 110, 114) are the emotional center and must not warp
- No legible writing is generated; drawn words and the outro title, if any, are composited in post
- Every face of a child is consistent with the approved keyframe; the faceless memory shots (22, 72) stay cropped
- The bridge stays indoors and in lamp light; the porch and the playground never appear in it
- The last shot (114) is locked and holds until the final guitar note decays
