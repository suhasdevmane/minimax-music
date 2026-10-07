# Wan 2.2 Shot List — "Power Back On"

**One scene per lyric line**, built from the submission's per-section video
direction. This is the first uptempo song: at 136 BPM a bar is 1.76 s, so
most shots are 2–4 s and the choruses cut on every bar. Take timestamps
from the rendered WAV.

## 1. Visual world

A rain-soaked, near-future city before dawn, most tower windows dark. A vast
abandoned power station. **Light is the story**: every effort switches
something on — one lamp, one floor, one block — until the roof opens and the
city glows. The repeating motif is real practical light (strip lights,
neon, sodium, sunrise), not CGI. Effects stay minimal.

| Section | Light | Camera |
|---|---|---|
| Intro | Cold blue, rain, one flicker under her palm | Slow, wide, static |
| Rap verse 1 | Dark hall, strip lights igniting on the beat | Fast handheld, on the beat |
| Female verse | Cracked mirror, warm gold growing | Push-ins, stairwell tracking |
| Pre-chorus | Cold blue → electric blue and amber, rotating ring | Circling |
| Chorus | Full station lit, roof panels opening, first light | Sprint tracking, match cuts to city |
| Post-chorus | Four 0.5 s impact shots | Ultra-fast |
| Rap verse 2 | Lit station, moving lights, intercut mini-stories | Confident handheld |
| Female verse 2 | Calm, neon repaired, rain stopping, rooftop dawn | Steady |
| Bridge | Rooftop dawn, no gym, transparent flashback overlays | Still, wide |
| Final chorus | Sunrise, crowds of people moving, bridge, aerial | Drone pull-backs |
| Outro | The neon wall lit, morning, calm breath | Slow, fade |

## 2. Character bible — paste into every prompt

**Mahima**
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair pulled into a tight high ponytail, athletic build, wearing a black training jacket with reflective silver detailing over a black sports top and leggings, focused determined expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic muscular build, wearing a charcoal sleeveless training hoodie and dark joggers, a rusted old metal key on a cord around his neck, grounded intense expression, realistic cinematic photography, consistent identity

Objects: her **broken neon sign** (an abstract glowing symbol once repaired,
never text), his **rusted key**, the **dead neon wall**, the **glowing floor
ring** in the generator room, the **main power lever**.

Mini-story extras (rap verse 2, final chorus): a young woman doing her first
pull-up; an older male runner with a knee brace; a student at a laptop who
then runs at night; a shy teenage boy adding a plate to a barbell. Keep
technique realistic and emotion grounded — self-improvement, never defeating
someone else.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

Timers, screens and any sign that would read as text: composite in the edit.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock both leads (front, three-quarter, profile, full body, resting and
exerting) with IP-Adapter or a character LoRA each. **OpenPose is essential
here** — pull-ups, sled pulls, rope slams, sprints and box jumps all need a
pose reference or the model invents anatomy. Depth for the big industrial
interiors. 16:9 first; 9:16 recomposition for the gym-hook cut.

Animate in short bursts: one rep per clip. Sprints and slams split into
2–3 s pieces; the model handles a single explosive movement far better than
a sequence. Light "switching on" is easiest done as a brightness ramp in the
edit over a still-lit plate.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

## 4. Scene per lyric line

### Intro — low battery

1. *"City went quiet, lights went thin"* — wide aerial of a rain-soaked near-future city before dawn, most tower windows dark, a few dim, slow drift, cold blue.
2. *"I heard my own heart booting again"* — Mahima walking alone across a wet forecourt toward the vast dark power station, a broken neon sign tucked under her arm, the reflective silver on her jacket catching what little light there is, tracking from behind, rain.
3. *"No rescue. No shortcut."* — Kai at a second entrance, pulling the rusted key from around his neck and fitting it to a heavy steel door, close-up on the key and his hands, cold light.
4. *"Just one more breath"* — extreme close-up of Mahima's palm pressed flat against a dead neon wall inside, then a thin line of blue electricity flickering beneath it, macro, one breath audible.
5. *"Power back on"* — the flicker running along the wall for one beat and dying, her eyes lifting, static.

### Verse 1 — Kai's rap, first spark

6. *"Came in with the weight of a week on my chest"* — Kai stepping into a dark turbine hall, shoulders heavy, breath visible, one shaft of cold light, wide.
7. *"No sleep, no peace, still I showed up dressed"* — close-up of him lacing trainers on a steel step, then standing, handheld on the beat.
8. *"World said, slow down, doubt said, sit down"* — him shadow-boxing in the dark, fast combinations, the punches cut on the beat, handheld.
9. *"I put both feet on the ground, said, watch this now"* — his feet landing flat on the concrete, a strip light overhead flickering on, low angle.
10. *"No silver spoon, no perfect plan"* — chalked hands clapping a cloud of chalk, extreme close-up, strobing under the new light.
11. *"Just scars on my hands and a fire I understand"* — close-up of scarred knuckles gripping an exposed steel beam overhead.
12. *"Every bad day got a lesson inside"* — an explosive pull-up on the beam, chin over the bar, another strip light igniting behind him on the rep.
13. *"Every closed door taught me how to build my side"* — a second and third pull-up, a light for each, the hall brightening in bands, medium wide.
14. *"I was running on empty, but empty ain't done"* — heavy battle-rope slams, the ropes whipping up on the beat, sweat flying, handheld.
15. *"Battery low, still I'm chasing the sun"* — a timer on a wall counting upward (composited), then his face, jaw set, sweat on his forehead.
16. *"They only see the glow when the whole thing's lit"* — him stepping back to look at the half-lit hall, breathing hard, the lit strips reflected in his eyes.
17. *"They never see the dark where you learn not to quit"* — a box jump, landing hard, and a line of sparks racing away from his feet across the floor toward a doorway, slow motion.

### Verse 2 — Mahima, quiet strength

18. *"I used to wait for the perfect day"* — the sparks arriving under a door into a dim changing room where Mahima stands before a cracked mirror, her reflection tired, static.
19. *"For all my fear to fade away"* — close-up of her reflection in the cracked glass, eyes on herself, then the eyes changing, focusing.
20. *"But the mirror said, girl, you're still here"* — her tying her hair into the tight ponytail in the mirror, over-the-shoulder.
21. *"So I tied my hair and faced the year"* — her pulling off the outer jacket and hanging it on a hook, turning from the mirror, medium.
22. *"I had a storm behind my eyes"* — a treadmill in the dark room, her sprinting, one warm gold lamp coming on above it, side tracking.
23. *"A hundred reasons to compromise"* — kettlebell swings, each swing on the beat, a second gold lamp igniting, medium.
24. *"Then I learned that strength is quiet too"* — battle ropes, her face calm and controlled rather than strained, close-up, gold light growing.
25. *"It starts when nobody's clapping for you"* — shadow boxing that is almost dance, fluid, alone in the room, wide, the room now warm.
26. *"One step, one breath, one more round"* — her at the foot of a long concrete stairwell, one breath, then starting up, low angle.
27. *"I found my rhythm in the underground"* — her running up the stairwell as lights ignite behind her one landing at a time, tracking from above.
28. *"No crown, no crowd, no finish line"* — her reaching the top landing without slowing, the whole stairwell lit below her, wide from above.
29. *"Just me becoming more than mine"* — her pushing through a door at the top into a vast dark circular room, the door light spilling in, static.

### Pre-chorus 1 — the generator room

30. *"Feel that pulse beneath the pain"* — the giant circular generator room, Mahima at one end and Kai entering at the far end, a dim ring on the floor between them, wide.
31. *"That's not weakness, that's your name"* — the floor ring beginning to glow and rotate slowly, overhead shot.
32. *"If the night says, you can't go on"* — the camera circling Mahima as she takes a deep breath, cold blue shifting to electric blue.
33. *"Turn your hurt into a power song"* — the camera circling Kai as he breathes, then both of them locking eyes across the room, a nod, amber entering the light.
34. *"Breathe in. Lock in. Rise up."* — three cuts on the words: her inhale, his fists closing, both of them stepping onto the ring.

### Chorus 1 — power surge

35. *"Power back on, power back on"* — the generator activating on the drop, light blasting outward through the whole room in a ring, wide, both leads lit from below.
36. *"I was down, but I was never gone"* — Mahima launching into a sprint down a long industrial corridor as its lights come on ahead of her, tracking from the front.
37. *"Turn the pressure into pulse"* — Kai hauling a huge weighted sled across the turbine hall floor, chains taut, veins standing, side tracking.
38. *"Turn the fear into muscle"* — his final, enormous rope slam, the ropes hitting the floor on the downbeat, slow motion.
39. *"I don't need luck, I don't need saving"* — Mahima mid-sprint, ponytail flying, face fierce and joyful, close-up, slow motion.
40. *"I've got a heart that keeps creating"* — match cut to the city outside: a whole block of tower windows switching on, aerial.
41. *"Power back on, power back on"* — match cut again: another district lighting up as Kai stands over the ropes, alternating on the bar.
42. *"When the world goes dark, I become the dawn"* — the station's roof panels grinding open and golden first light flooding down onto both of them, wide, slow.
43. *"One more rep, one more run"* — Mahima bursting out of the corridor into the golden light, Kai turning toward her, medium.
44. *"Power back on, I'm not done"* — both of them stopped in the light, breathing hard, looking up, wide.

### Post-chorus 1 — the chant (0.5 s impact shots)

45. *"Not done. Not done."* — a fist closing; a running shoe striking the floor.
46. *"Still here. Still strong."* — sweat flying off a face in slow motion; city lights switching on.
47. *"Power back on."* — the two leads standing back-to-back beneath the bright generator, low angle.
48. *"Power back on."* — hold, the ring rotating fast around them.

### Verse 3 — Kai's rap, the lit station

49. *"No fake flex, I got proof in the pace"* — Kai performing in the centre of the fully lit station, rhythmic moving lights sweeping, confident handheld.
50. *"Every time I lost, I rebuilt the base"* — intercut: a young woman straining through her first pull-up in a small gym, and getting her chin over, close-up.
51. *"No someday talk, I'm here right now"* — Kai to camera, pointing at the floor, handheld on the beat.
52. *"Sweat on the floor, got dirt on my crown"* — a drop of sweat hitting the concrete, extreme close-up, then his grin.
53. *"This for the kid who got laughed out the room"* — intercut: a shy teenage boy alone in a gym adding a small plate to a barbell, checking no one is watching.
54. *"For the girl who was told she was taking up room"* — intercut: the young woman from shot 50 chalking up for a second attempt, shoulders back.
55. *"For the one who got tired but never got weak"* — intercut: an older runner with a knee brace tying his shoes at a track at dawn, then starting slow.
56. *"For the voice in your head that you're learning to beat"* — intercut: a student closing a laptop at night, pulling on trainers, and stepping out into the street to run.
57. *"I don't chase perfect, I chase progress"* — Kai, straight to camera, still, the moving lights pausing on him, close-up.
58. *"Small wins stack till they look like a process"* — quick stack of the four mini-story people each finishing their small win, on the beat.
59. *"Mind on calm, but the engine on loud"* — Kai's face calm while the lights strobe around him, contrast, medium.
60. *"I don't need a stage, I can light up a crowd"* — pull back to reveal the whole lit hall around him, wide.

### Verse 4 — Mahima, recovery is strength

61. *"I don't need to outrun my past"* — Mahima walking, not collapsing, after the sprint, hands on her head, breathing steadily, calm light, tracking.
62. *"I let it teach me how to last"* — her drinking water, looking around the lit station, small satisfied nod, close-up.
63. *"Every version that broke before"* — her picking up the broken neon sign from where she left it at the start, close-up on her hands and the cracked tubes.
64. *"Built the girl who walks through this door"* — her reconnecting the sign's cable, and it lighting as an abstract glowing symbol, no text, macro.
65. *"I can rest without giving in"* — her sitting on a crate with the glowing sign beside her, eyes closed, breathing, medium, calm gold.
66. *"I can heal and still want to win"* — her standing, jacket back over her shoulder, walking toward a stairwell marked by daylight, medium.
67. *"Soft heart, strong mind, steady feet"* — her climbing to the rooftop as the rain stops, the last drops on her face, close-up.
68. *"Peace in my head with a fire in my beat"* — the rooftop at dawn, the city half-lit below, her at the edge, wide, brightening sky.

### Pre-chorus 2 — the lever

69. *"Feel that pulse beneath the pain"* — Mahima and Kai standing together at a huge main power switch in the station's control room, hands on the lever, medium two-shot.
70. *"That's not weakness, that's your name"* — close-up of her hand on the lever, then his beside it.
71. *"If the night says, you can't go on"* — her controlled breath, then his, alternating close-ups.
72. *"Turn your hurt into a power song"* — both looking up at the control room window toward the dark skyline.
73. *"Breathe in. Lock in. Rise up."* — on "rise up," both pulling the lever together and the entire skyline lighting up through the window, wide.

### Chorus 2 — into the city

74. *"Power back on, power back on"* — the station's great doors opening and Mahima running out through them into sunrise, Kai following, wide from outside.
75. *"I was down, but I was never gone"* — the two of them running into the city streets, now alive and bright, tracking.
76. *"Turn the pressure into pulse"* — other runners joining from side streets, not racing, moving together, wide.
77. *"Turn the fear into muscle"* — cyclists and a group of dancers joining the wave of motion at an intersection, drone.
78. *"I don't need luck, I don't need saving"* — Mahima at the head of the run, laughing, sun on her face, close-up tracking.
79. *"I've got a heart that keeps creating"* — Kai beside her, glancing over, a grin, close-up tracking.
80. *"Power back on, power back on"* — the whole moving crowd on a long bridge, drone pull-back beginning.
81. *"When the world goes dark, I become the dawn"* — the sun clearing the skyline ahead of them, lens flare, drone.
82. *"One more rep, one more run"* — a lifter on a rooftop gym pausing to watch the runners pass below, then going back to the bar.
83. *"Power back on, I'm not done"* — the drone pull-back continuing until the bridge and the lit city fill the frame.

### Instrumental — training montage (0.5 s impact / 2 s slow-motion alternating)

84. Sprint starts from blocks. 85. A barbell lift, bar bending. 86. Jump rope, fast. 87. Mountain climbers. 88. Sled pull. 89. Boxing bag strikes. 90. A yoga stretch on the rooftop, slow. 91. Laughter after a brutal set, two people on the floor. 92. A filtered flash of the generator ring, on the vocal chop.

### Bridge — rooftop, no pressure

93. *"If today is all you can carry"* — the rooftop at dawn, Mahima sitting on the ledge breathing slowly, Kai arriving with two water bottles and sitting beside her, wide, still.
94. *"Carry today and let it be"* — her taking the bottle, a small thanks, both looking out at the waking city, medium.
95. *"You don't have to be fearless"* — a transparent overlay: Mahima's tired reflection in the cracked mirror, ghosted over her calm face now.
96. *"You just have to move your feet"* — a transparent overlay: Kai alone in the dark hall at the start, over him now in the light.
97. *"You can pause. You can breathe. You can start again."* — three quiet cuts: his hands resting; his breath; his eyes on the horizon.
98. *"The strongest thing you'll ever do"* — Kai speaking, then singing, to no one in particular, close-up, warm dawn.
99. *"Is believe you're not at the end"* — Mahima looking at him, then back at the city, a nod.
100. *"We don't break, we bend, then grow"* — both rising from the ledge, wide.
101. *"We don't wait, we make the road"* — both walking toward the rooftop stairs and a bright open street beyond, tracking from behind.

### Final chorus — full release

102. *"Power back on, power back on"* — the power station now a vibrant sunrise workout space full of people training, dancing, running, wide crane.
103. *"I was down, but I was never gone"* — Mahima leading a run through the city, a crowd behind her, tracking from the front.
104. *"Turn the pressure into pulse"* — Kai in one final training sequence in the station, a clean heavy lift, slow motion.
105. *"Turn the fear into muscle"* — the four mini-story people celebrating their own progress, quick cuts.
106. *"I don't need luck, I don't need saving"* — Mahima close-up mid-run, no strain, joy.
107. *"I've got a heart that keeps creating"* — the neon symbol glowing in the lit station, then the city.
108. *"No quit! No fear! New day, new gear!"* — Kai shouting the ad-libs to the crowd in the station, handheld, energy.
109. *"Stand tall, breathe deep, your future starts here!"* — the crowd's hands up, then Kai's calm face, contrast.
110. *"Power back on, power back on"* — both leads arriving on the bridge and stopping, the crowd flowing past them.
111. *"When the world goes dark, I become the dawn"* — both looking at the sun, then turning to face camera with relaxed confidence, not aggression, medium two-shot.
112. *"One more rep, one more run"* — hold on the two-shot, breathing settling.
113. *"Power back on, I'm not done"* — cut to a very wide aerial: the once-dark city glowing in full sunrise.

### Outro — the wall, lit

114. *"I was down"* — return to the opening close-up: the neon wall, now fully illuminated, Mahima's palm lifting away from it, macro.
115. *"But I was never gone"* — her turning and walking away into morning light through the open doors, wide.
116. *"Take your time."* — Kai following at a distance, unhurried, the key swinging on its cord.
117. *"Then turn your power back on."* — both joining the wider group outside in the sun, medium.
118. *"Power back on."* — the powered city skyline at sunrise, slow drift.
119. *"Power back on."* — fade out on the skyline, the sound of one steady calm breath. No text.

## 5. Edit and the cuts

Markers at: the first whisper, the rap entrance, the generator drop, each
"power back on", the post-chorus chants, "I don't chase perfect", the lever
pull, the instrumental, "you just have to move your feet", the modulated
final chorus, and the final breath. At 136 BPM a bar is 1.76 s; choruses cut
every bar, rap verses every half-bar where the mini-story intercuts land.

**15-second gym hook** — shots 35–38, vertical, with the four hook lines on
screen. **Recovery quote** — shots 93–96 with *"You don't have to be
fearless; you just have to move your feet."* **Rap clip** — shots 57–58.
**Caption** — *"I was down, but I was never gone."*

## 6. Quality-control checklist

- Both leads recognisable in every shot; her ponytail and silver-detail jacket, his key on the cord
- Every exercise anatomically real (OpenPose on all lifts, pulls, slams, jumps)
- Light only ever increases — no shot is darker than the one before it except the bridge overlays
- The neon sign is an abstract symbol, never text; no readable signage anywhere
- Mini-story extras are self-improvement moments, never competing against anyone
- The final two-shot to camera is relaxed, not aggressive
- Impact shots ≤0.5 s, slow-motion shots ≈2 s in the montage
- Ends on the aerial and the breath, no text
