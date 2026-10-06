# Wan 2.2 Shot List — "Your Little Book of Life"

**One shot per lyric line.** This song has 104 lyric lines in `lyrics.txt`
(section tags excluded), so there are 104 numbered shots, numbered
continuously from 1 to 104 in lyric order, including the repeated choruses.
The song has **no `[instrumental]` tag**, so there are no instrumental shots
in this list; the music under the bridge and the outro is covered by the
lyric shots that sit on either side of it. Timestamps come from the rendered
WAV; cut on the sung line. At 76 BPM a 4/4 bar is 3.16 s.

## 1. Visual style

A gentle, sunlit family world, shot as if the camera is in the room with
them. Warm daylight and lamp light dominate; the grade stays natural with a
soft, slightly golden warmth. The garden, the kitchen and the living room
are the three homes of the song, and the bookshelf and the sign are the
motifs that carry the book-of-life idea. The ladybug is the first and last
image of the story. Handheld and close in the verses, steadier in the
bridge, wide and open in the final chorus. No phones, no screens, no text
inside the frame.

| Section | Grade | Camera |
|---|---|---|
| Intro / garden morning | Soft early sun, cool shadows, faint mist | Macro, then slow pull back |
| Verse 1 / kitchen | Warm kitchen light, bright and playful | Handheld, low-angle tracking |
| Chorus 1 / living room | Full golden afternoon, soft and open | Wide, push-in |
| Verse 2 / blanket fort | Amber lamp light through fabric, cosy | Overhead, close |
| Chorus 2 / garden lawn | Warm afternoon, long shadows | Tracking |
| Verse 3 / discovery | Clean bright daylight, sparkle on water | Mixed, low-angle, macro |
| Pre-chorus / kitchen table | Single warm lamp, dim room | Static close, slow push-in |
| Chorus 3 / bedroom | Small warm bedside lamp, low glow | Medium close, slow |
| Bridge / hallway shelf | One hall lamp, hard shadows | Static, close |
| Final chorus / garden | Golden hour, full colour, rainbow | Wide, crane up |
| Outro / night sofa | Kitchen lamp spill, dark blue garden | Slow static wide |

## 2. Character bible — paste into every prompt

**Kai** (the father, every shot he is in)
> Same male character Kai, man in his late thirties, short dark hair, warm tired face, wearing a cardigan, holding a mug of tea, realistic cinematic photography, consistent identity, natural skin texture

**Ellie** (the daughter, every shot she is in)
> Same young girl Ellie, about four years old, wavy dark hair, round face, bright eyes, wearing a yellow raincoat, holding a plush bear, realistic cinematic photography, consistent identity, natural skin texture

**Kai's cardigan and mug** are constants. The **yellow raincoat** is Ellie's
daytime look and is worn in the garden and the kitchen; in the final chorus
and the outro she wears it over her pyjamas. The **plush bear** is in her
hand or under her arm in every shot after the intro. Friends and neighbours
are seen only at a distance or from behind; no face is generated for them.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

All signs, the chalk drawing, the bookshelf labels and any on-screen words
are composited in the edit or kept out of frame. The hand-lettered sign on
the fort chair is a physical prop, so keep its lettering out of focus; do
not ask the model to render legible words.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Kai and Ellie with IP-Adapter or a character LoRA, one reference per
character, approved on a daytime still and a warm-lamp still. Keyframes
first; Depth for the kitchen and bedroom compositions; OpenPose for the
spinning and the bowing shots. 16:9 throughout; 9:16 only for the optional
challenge cut. Animate conservatively: breathing, a sleeve moving, a page
turning, water and bubbles drifting, leaves in a breeze.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — a small morning

1. *"Today you found a ladybug"* — Ellie in the yellow raincoat crouched by a low garden wall in early sun, plush bear under one arm, looking down at the wall; medium close, soft mist, static.
2. *"Beside the garden wall,"* — the wall and wet grass in macro, a ladybug on a stone at the bottom of the frame, shallow focus, slow pull back to show Ellie's hands on her knees.
3. *"You watched it climb a blade of grass"* — macro: the ladybug climbing a blade of grass, cool morning light, Ellie's eyes just in the top of frame watching it.
4. *"And wondered if it'd fall."* — Ellie's face close-up, eyes wide, breath visible in the cool air, then Kai in the back doorway with his mug of tea, smiling and not interrupting.

### Verse 1 — the biscuit, the spoon, the kitchen

5. *"You gave it half a biscuit,"* — Ellie in the garden holding a half biscuit out toward the wall, the bear propped beside her, warm early light, handheld, medium close.
6. *"You gave it room to fly,"* — Ellie standing back with both arms open, the wall and the garden behind her, the ladybug lifting off in a soft blur, wide shot.
7. *"Then waved until it disappeared"* — Ellie waving at the sky with her whole arm, a small wide shot, the frame tilting up after the speck.
8. *"Like a plane across the sky."* — the sky in a slow tilt, a plane's contrail on a pale blue, Ellie's raised hand in the bottom corner, static wide.
9. *"Yesterday you wore your shoes"* — the kitchen, warm light: Ellie on the floor pulling on her shoes, one foot already in the wrong shoe, medium close, handheld.
10. *"Upon the wrong two feet,"* — low-angle close-up of two small feet in shoes on the wrong feet, Kai's slippers at the edge of frame, warm lamp.
11. *"You marched around the kitchen"* — Ellie marching in a wide circle past the counter, arms swinging, the camera tracking low in front of her, cheerful and steady.
12. *"To your own imaginary beat."* — Ellie stamping on the beat with the bear raised over her head, Kai at the counter tapping his mug in time, wide, lively.
13. *"You called the spoon a microphone,"* — Ellie holding a wooden spoon to her lips like a microphone, close-up on her mouth, eyes sideways toward Kai.
14. *"The blanket was a train,"* — a blanket draped over two kitchen chairs becoming a tunnel, Ellie crawling through it with the bear, medium overhead, warm.
15. *"And suddenly our little home"* — a wide shot of the whole kitchen, every surface lit, Kai at the counter looking up from his mug with a grin.
16. *"Was full of sun again."* — the window full of morning sun, a sunbeam across the kitchen floor, Ellie stepping into it, wide and warm, static.

### Chorus 1 — the title line

17. *"You're writing your own little book of life,"* — the living room in golden afternoon, Ellie spinning in the centre with her arms out, the bear in one hand; wide shot, slow push in.
18. *"With every laugh and every surprise."* — Ellie's head thrown back laughing mid-spin, sunlight in her wavy hair, close medium, handheld.
19. *"Every new question, every new day,"* — Ellie pointing at the window, her mouth open mid-question, Kai on the arm of the sofa with his cardigan sleeve pushed up, medium two-shot.
20. *"You paint a thousand colours my way."* — a close-up of Ellie's hands with bright paint on her fingers pressed to the window glass, warm sun behind, shallow focus.
21. *"You're my sunrise, my morning light,"* — Kai on the sofa arm, eyes closed, singing, the late afternoon sun on his face, slow push-in, warm.
22. *"The reason my tired heart feels alive."* — a close-up of Kai's tired, warm face opening into a smile, a crease at the eyes, steady light.
23. *"My beautiful girl, wherever you go,"* — Ellie running across the rug toward the camera with the bear held high, handheld tracking from the front, the room behind her bright.
24. *"You make the whole world brighter than you know."* — Ellie stopping dizzy, laughing, pointing at the bright window; close-up of her face in full sun, a lens flare at the edge.

### Verse 2 — the castle, the princess, the blanket fort

25. *"You built a castle out of pillows,"* — overhead shot of a fort made from sofa cushions on the living room floor, Ellie inside arranging the last pillow, warm lamp.
26. *"A kingdom on the floor,"* — the wide overhead view of the whole fort and rug as a kingdom, two toy animals on the walls, static, warm.
27. *"You pinned a sign upon the chair,"* — close-up of a hand-lettered card pinned to a dining chair, the lettering kept out of focus, Ellie's small hand adjusting the pin.
28. *"Daddy, knock before the door."* — Kai, at the fort's entrance, his knuckles raised toward the chair, a close-up on his hand and the cardigan sleeve, warm.
29. *"I bowed before the princess"* — Kai kneeling and bowing low as a dancing bear at the fort entrance, the cardigan and the mug on the floor, medium wide, handheld.
30. *"And asked if I could stay,"* — Kai's face peering in at the fort entrance with a hopeful look, Ellie's face at the gap in the blanket, soft lamp glow, close two-shot.
31. *"You said, only if you promise"* — Ellie inside the fort, one finger raised as if making a rule, the amber light on her face, close-up.
32. *"To be silly every day."* — Kai inside the fort on his back with the bear on his chest, both of them laughing up at the ceiling of blankets, wide, static.
33. *"So I became a dancing bear,"* — Kai on all fours in the living room, arms out like a bear, Ellie clapping in front of him, handheld tracking, playful.
34. *"A dragon and a king,"* — Kai wearing a cardboard crown from the kitchen drawer, roaring softly, Ellie's delighted face at the edge of the frame, medium.
35. *"And you laughed until your little cheeks"* — a close-up of Ellie laughing with her cheeks pushed up, eyes squeezed, amber light, handheld.
36. *"Were brighter than the spring."* — a tight close-up of the cheeks in warm light, a single soft flare, held one beat, shallow focus.
37. *"I learned that joy is not a treasure"* — Kai sitting alone on the sofa, mug in both hands, looking across at the fort, the lamp behind him, static medium.
38. *"Hidden far away,"* — the fort from the window at dusk, the amber glow through the blanket walls, the garden dark outside, wide static.
39. *"Sometimes it's just a blanket fort"* — Ellie and Kai inside the fort with a torch lit under the blanket, the bear between them, overhead close.
40. *"At the ending of the day."* — the fort glowing from inside, a slow pull back out of the window, the room going soft and dim, wide.

### Chorus 2 — the hook returns on the lawn

41. *"You're writing your own little book of life,"* — the back garden in afternoon, Ellie running in a circle on the lawn with the bear held up, Kai walking after her with his tea; wide, tracking.
42. *"With every laugh and every surprise."* — Ellie mid-run, her wavy hair flying, the bear's ear bouncing, handheld close from the side. Reuse shot 18 with a fresh angle and the garden behind her.
43. *"Every new question, every new day,"* — Ellie stopping by the garden wall and pointing at the same blade of grass, a call-back to shot 3, the camera low.
44. *"You paint a thousand colours my way."* — a close-up of a chalk drawing on the paving slab in bright colours, Ellie's knees in the frame, warm sun.
45. *"You're my sunrise, my morning light,"* — Kai on the garden path, cardigan open in the warm air, a wide shot with the back door and kitchen light behind him.
46. *"The reason my tired heart feels alive."* — a close-up of Kai's face in the sun, his eyes lit, a soft lens glow, static.
47. *"My beautiful girl, wherever you go,"* — Ellie walking backward along the path, looking back at Kai, the bear waving, a steady tracking shot from the front.
48. *"You make the whole world brighter than you know."* — the lawn in full afternoon light, Ellie and the bear in the middle of it, a wide shot tilting up to the sky.

### Verse 3 — names, clouds, pebbles

49. *"You learned to say the names of things,"* — Ellie in the kitchen naming the objects on the counter, her finger pointing at each in turn, close medium, bright.
50. *"Then changed them just for fun."* — Ellie grinning at the toaster and calling it a loud dog, Kai's face at the side of frame smiling, handheld.
51. *"The fridge became a mountain,"* — Ellie climbing a kitchen chair toward the fridge door, low angle, the fridge door filling the frame like a cliff.
52. *"The ceiling was the sun."* — Ellie lying on the floor looking up at the kitchen ceiling light, arms out, the bulb a warm glow above, overhead.
53. *"You gave a name to every cloud"* — Ellie and Kai on the lawn lying on their backs, pointing at clouds, a wide sky shot with two small figures in the bottom corner.
54. *"And every passing plane,"* — a plane across the sky, Ellie's arm pointing up at it, the contrail a soft line, wide static.
55. *"You made a friend of every sound,"* — Ellie with her hands cupped to her ears on the lawn, the open window and birds in the background, close medium.
56. *"The thunder, wind and rain."* — a light rain beginning on the window glass, Ellie at the window with her palm against it, the grey light soft, close.
57. *"You make a celebration"* — Ellie splashing in the puddle in her yellow raincoat, arms up, water spraying up in the sun, handheld wide.
58. *"From the smallest thing you find,"* — a macro shot of a small pebble in Ellie's open palm, wet and bright, her fingers curled around it.
59. *"A pebble can be precious,"* — the same pebble held up to the light, a sparkle on its edge, Ellie's eyes focused on it, close and shallow.
60. *"A puddle can be kind."* — the puddle from above reflecting the sky, Ellie's boot stamping into it and the water rippling, overhead close.
61. *"You show me that the world is new"* — Kai crouched beside her at the puddle looking at the sky reflected in it, the camera low between them, wide and soft.
62. *"When seen through loving eyes,"* — a close-up of Kai's face in profile, looking at Ellie with his tired eyes softened, a sunbeam across his cheek.
63. *"There are miracles in ordinary days"* — a wide shot of the ordinary street and garden gate, Ellie skipping through it with the bear, the light warm after the rain.
64. *"Beneath familiar skies."* — the sky after the rain, a faint rainbow at the edge, a slow tilt up, wide and open, static at the end.

### Pre-chorus — a small reflective pause

65. *"I used to chase tomorrow,"* — Kai alone at the kitchen table after bedtime, the tea gone cold, the hallway light a thin line at the frame edge; static close on his hands on the mug.
66. *"Always running toward the next,"* — a slow push-in on Kai's face as he looks toward the hallway and the light under her door, soft, unhurried.
67. *"You taught me how to hold the moment"* — Ellie's drawing of a ladybug and a sun on the table, held up to the lamp light by Kai's hand, close and warm.
68. *"And be thankful for the best."* — Kai setting the mug down and leaning back, eyes closed, a small breath out, the lamp behind him; medium static.

### Chorus 3 — the hook, intimate

69. *"You're writing your own little book of life,"* — Ellie's bedroom at night, the bear in her arms and a row of plush toys on the shelf; medium close, Kai sitting on the edge of the bed.
70. *"With every laugh and every surprise."* — Ellie in bed under a blanket, a sleepy smile, the bedside lamp warm on her face, close.
71. *"Every new question, every new day,"* — Ellie asking Kai a question with her eyes, Kai leaning in to answer, a close two-shot in the lamp light.
72. *"You paint a thousand colours my way."* — a close-up of a crayon drawing taped to the bedroom wall, bright colours, the lamp light moving across it; slow.
73. *"You're my sunrise, my morning light,"* — Kai's hand resting on the blanket beside her hand, both in the lamp glow, a close-up on the hands, static.
74. *"The reason my tired heart feels alive."* — Kai's face close, the tired lines in his face softened by the lamp, a slow push-in, warm.
75. *"My beautiful girl, wherever you go,"* — the bedroom door half open to the hallway, a soft slice of light, Ellie's shape in the bed in the frame, a long static shot.
76. *"You make the whole world brighter than you know."* — Ellie's eyes closing slowly, the lamp dimming, a soft close-up on her face with the bear under her chin.

### Bridge — the pages to come

77. *"One day you'll turn the pages"* — the hallway bookshelf in hard single-lamp light, a battered picture book and a stack of drawings tied with string, static close.
78. *"Far beyond the ones we know,"* — a close-up of a page turning under Kai's thumb, the paper lifting in the lamp light, shallow focus.
79. *"You'll write about your dreams"* — a fresh blank page in a notebook, a child's pencil resting on it, the lamp casting a long shadow, close.
80. *"And the places you will go."* — the two small shoes by the front door, one pair on the wrong feet, the door mat and a bit of morning sun through the window, static.
81. *"There may be roads I cannot follow,"* — a close-up of Kai's face in the hall, looking at the open front door, the dark street beyond it, medium close.
82. *"There may be skies I cannot see,"* — a wide shot through the open front door of the street at dusk, a single streetlamp on, Kai's silhouette in the frame.
83. *"But every chapter of your heart"* — Ellie's small hand pressed to a drawing of a house with a sun above it, held by Kai's hand, close and warm.
84. *"Will always matter to me."* — Kai's eyes in close-up, wet at the edges but steady, the cardigan collar in frame, the hall lamp soft behind.
85. *"I'll keep the little memories,"* — a shelf of small keepsakes: a jar of pebbles, a tin of drawings, a row of tiny shoes; slow pan along the shelf.
86. *"Your drawings, words and shoes,"* — close-up on a pair of small yellow wellington boots on the bottom shelf, a little mud still on the sole, warm.
87. *"The tiny hands that held mine"* — Ellie's small hand in Kai's large one, a close-up of the two hands across the frame, warm and soft-focus.
88. *"When you had the world to choose."* — Ellie at the window with a row of picture books in front of her, choosing one, the morning light on her face, medium.
89. *"And when you read the story"* — Kai and Ellie reading side by side on the sofa, the book open between them, the lamp warm over the pages, static two-shot.
90. *"Of the girl you grew into,"* — a slow push-in over the book's open page, the picture of a girl older than Ellie drawn in the margin, hard to see, shallow focus.
91. *"I hope you see between the lines"* — a close-up of Kai's finger tracing under a line of text, shallow focus, the lamp light catching the paper's edge.
92. *"How proud I am of you."* — Kai looking up from the book at Ellie, his tired face soft and open, a close-up at the bridge's end, the lamp glow holding.

### Chorus 4 — the final chorus, every layer

93. *"You're writing your own little book of life,"* — the family in the garden at golden hour: Ellie in the yellow raincoat over her pyjamas with the bear on her shoulder, Kai at the path, bubbles drifting; wide sweeping shot, crane up over the wall.
94. *"With every brave and beautiful line."* — Ellie reaching up to catch a bubble, her face lit by the sun, a close-up with a soft rim light, handheld, bright.
95. *"Every new dream, every new start,"* — a wide shot of the garden with the neighbour's child running in the background, the lawn in full colour, the camera moving slow and open.
96. *"You leave a rainbow in your father's heart."* — a rainbow arc in the spray from the garden hose, Kai watching it with his cardigan open, a close-up on his face as the light hits, warm and bright.
97. *"You're my sunrise, my morning light,"* — Kai in the sun with Ellie on his shoulders, both laughing up at the sky, the camera low behind them, wide and warm.
98. *"The reason my tired heart feels alive."* — a close-up of Kai's face with Ellie's hand on his cheek, the golden light across both faces, soft and clean.
99. *"My beautiful girl, wherever you go,"* — Ellie running across the grass in the raincoat with the bear held high, the garden behind her, a tracking shot from the front.
100. *"You make the whole world brighter than you know."* — the garden and the rainbow in one wide frame, Ellie small in the middle with arms wide, the crane rising slowly above the wall.

### Outro — guitar and voice

101. *"So keep on dancing, keep on dreaming,"* — night: Ellie asleep on the sofa in the yellow raincoat with the bear under her arm, Kai beside her with the last of the tea; slow static wide.
102. *"Keep your wonder shining through."* — close-up of Ellie's sleeping face, a small smile, the kitchen lamp spilling soft light across the sofa.
103. *"Life became a better story"* — Kai's hand resting on the raincoat sleeve, close, warm amber light, the garden dark blue through the open back door.
104. *"The day it gave me you."* — the garden wall in the dark, one blade of grass moving in the breeze, the ladybug's stone in the frame, the frame fades to black on the last note.

## 5. Edit and the challenge

Markers at: the first vocal entrance (shot 1), the first "You're writing your
own little book of life" (shot 17), the verse-2 "Daddy, knock before the
door" (shot 28), the bridge's first page turn (shot 78), the final chorus's
"rainbow" (shot 96), and the last note (shot 104). The instrumental work is
carried by the transitions between these markers; there is no
instrumental-tagged section to cut to. At 76 BPM a bar is 3.16 s.

**Shareable cut.** Post the vertical cut of chorus 1 (shots 17–24) with the
caption *"You're writing your own little book of life"* on screen and invite
people to post a short clip of their own child doing one small ordinary
thing, with the chorus over it. The ladybug and the puddle are the two
shareable frames.

## 6. Quality-control checklist

- Kai in cardigan and mug in every shot he appears in, late-thirties look held across the whole song
- Ellie in the yellow raincoat for the garden and kitchen, with the plush bear in hand from shot 5 on; the raincoat over pyjamas in shots 93–101
- Friends and neighbours never show a generated face; they are seen at distance or from behind
- No legible text in any frame; signs and drawings are out of focus or composited
- The ladybug appears in shot 1 and returns as the stone in shot 104
- Hands and small fingers checked on the pebble, the crayon drawing and the bubble shots
- The final shot is locked-off, holds on the dark garden, and fades with the last note
