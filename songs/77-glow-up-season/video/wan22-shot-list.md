# Wan 2.2 Shot List — "Glow Up Season"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
122 BPM a bar is 1.97 s, so most shots are 2–4 s and the choruses and
post-choruses cut on every bar.

## 1. Visual style

Sunlit dance-pop. One rule: **the light only gets warmer.** The intro
starts in pre-dawn blue and the video climbs through morning white, hard
afternoon sun, golden hour, blue hour with string lights, and ends on a
lamp. The **montage of small wins** is the engine — the salon, the river,
the gym, the red dress, the paint roller, the rooftop — each one short,
specific and cut on the beat. The ex is a back walking out of a door, never
more. Saturated, clean, glossy, handheld in the verses and wide on the
drops.

| Section | Grade | Camera |
|---|---|---|
| Intro | Pre-dawn blue to gold in one cut | Close-ups, static |
| Verse 1 | Clean white salon, cold-to-gold river, bright gym | Handheld, tracking |
| Pre-choruses | Warm interior, blown-out door | Beat-synced close-ups |
| Choruses | Saturated full sun, then golden hour, then string lights | Wide tracking, drone |
| Post-choruses | High-contrast impact frames | Ultra-fast, 0.5 s each |
| Verse 2 | Warm brunch, patio sun, big daylight in the new flat | Handheld |
| Instrumental | All the day's lights in sequence | Fast cuts, then one wide |
| Bridge (rap) | Blue hour arriving, string lights on | Kai to camera, cutaways |
| Final chorus | String lights and last pink sky | Drone, slow motion |
| Outro | Last light, then a lamp, then dark | Slow push-in, static |

## 2. Character bible — paste into every prompt

**Mahima** (dawn / gym / river)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled into a high ponytail, no makeup, wearing a white cropped hoodie, black leggings and clean white trainers, sleepy then determined expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the new cut / day)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, dark wavy hair freshly cut to a shoulder-length bob, light natural makeup, wearing a cream ribbed top and high-waisted light-blue jeans with gold hoop earrings, bright amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the red dress / rooftop)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, dark wavy shoulder-length bob, glowing makeup with a soft red lip, wearing a fitted red satin slip dress and gold hoop earrings, radiant confident expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the rapper, a friend-of-a-friend at the rooftop party, bridge and final chorus only)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing an open camel overshirt over a white t-shirt and dark trousers, a drink in hand, relaxed admiring expression, realistic cinematic photography, consistent identity

**The ex** — never shown clearly: a back walking away down a corridor, a hand on a door, a figure leaving through a doorway. No face, ever.
> a young man in his mid twenties, back to camera, walking away through a doorway, dark jacket

**Friends** — two young women, one with braids and one with a blonde crop, warm, loud, always laughing; a rooftop crowd of twelve to twenty in the last third.

**Objects that recur:** the **white trainers** (intro and outro, by the door), the **red dress** (cart, hanger, booth, rooftop), the **new keys**, the **paint roller**, the **plants on the sill**, the **mirror by the door**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the group chat, the shopping cart, the saved contact,
the alarm and the lease are composited in the edit.** Generate the phone as
a lit blank screen and overlay the UI in post — the model cannot render
legible UI.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless. Keyframes first; OpenPose for the dance
and the running shot; Depth for the bedroom compositions. 16:9 first; 9:16 for
the phone-POV cuts, which are natural vertical content. Animate
conservatively: thumb scrolling, screen light flicker, breathing, a hoodie
being pulled on.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s. Hair falling, a paint roller and a spin in a dress are
the three motions the model handles best here; the run and the crowd dance
need OpenPose.

## 4. Scene per lyric line

### Intro — six a.m.

1. *"Six a.m. and I didn't hit snooze"* — Mahima (dawn look) in bed in pre-dawn blue, her hand reaching for the buzzing phone on the nightstand and switching the alarm off instead of snoozing, then sitting up, close-up, static.
2. *"Laced up the white ones, got nothing to lose"* — extreme close-up of white trainers by the door being laced fast, her fingers quick, cool light.
3. *"Playlist loud and the blinds pulled wide"* — her yanking the blinds open, warm dawn light hitting the room on the beat, medium shot from behind.
4. *"This is the year I stop hiding the light"* — her face in the new light, eyes closed for one beat, then a small private grin, close-up.

### Verse 1 — small wins

5. *"Booked the salon on a Tuesday afternoon"* — a bright, almost-empty salon, Mahima (dawn look, long hair down) in the chair with a cape on, the stylist behind her, wide, clean white light.
6. *"Told her, take it shorter, I've got somewhere to be soon"* — the stylist holding up a length of hair with a questioning look, Mahima nodding bigger than expected, over-the-shoulder into the mirror.
7. *"Watched the old length fall like it was never mine"* — the first cut, a long length of dark hair falling to the floor in slow motion, macro.
8. *"Walked out lighter with the sun on my mind"* — Mahima (new cut look) stepping out of the salon onto the street, shaking out the bob, hard afternoon sun on her face, tracking from the front.
9. *"Group chat blowing up, they said, who is she"* — a phone on a café table lighting up with a flood of reactions (composited), her hand covering her laugh, close-up.
10. *"Same girl, new light, that's the whole story"* — her looking up from the phone straight into the camera with a shrug and a grin, medium close-up, café daylight.
11. *"Ran the long loop by the river, lungs on fire"* — a river path at dawn, Mahima (dawn look) running, breath visible, white trainers hitting the path, long side-tracking shot, cold blue turning gold.
12. *"Every mile a little further from the liar"* — a faceless figure in a dark jacket, back to camera, walking away down a corridor in a two-second memory flash, then hard cut back to her running past the camera and out of frame.
13. *"Gym at seven, I was scared of the room"* — a one-second flash of her hesitating at a gym door with her hand on the handle, then present day: pushing through it, medium, bright morning.
14. *"Now the room knows my name and my favourite tune"* — a nod from the front desk, a fist bump from a regular on the way past, her song visibly landing on her face, handheld.
15. *"Little wins stacking like a tower of gold"* — four fast cuts on the beat: a set finished in the gym mirror with a small nod, a plant on a counter, a bill paid on a laptop (composited), a stretch in a window.
16. *"I'm twenty-four and I've never felt this bold"* — her in the gym mirror, hands on hips, breathing hard, looking herself in the eye, over-the-shoulder into the mirror.

### Pre-chorus 1 — the mirror by the door

17. *"He said I'd never shine without him"* — Mahima (new cut look) in her hallway mirror mouthing the line at her reflection with one eyebrow up, mock-serious, close-up, warm lamp.
18. *"Look who's lighting up the room"* — claps on the beat: lipstick, earring, hair, keys, four extreme close-ups.
19. *"Don't need a reason, don't need a witness"* — her turning from the mirror and walking to the front door, tracking from behind, the light around the door frame growing.
20. *"Sunrise came early and it's coming through"* — the front door opening onto a street flooded with golden light, the frame blowing out, wide.

### Chorus 1 — the drop, the crosswalk

21. *"It's glow up season, and I'm the sun"* — Mahima (new cut look) in the middle of a city crosswalk with the sun directly behind her, lens flare on the drop, wide tracking from the front.
22. *"Look at me shining, yeah, look what I've become"* — her arms opening wide as she walks, cars stopped, sun through her hair, slow motion.
23. *"New hair, new dress, new door, new number"* — four cuts on the four beats: the bob shaken out, the red dress on a hanger, a new front door with new keys turning, a phone screen saving a new number (composited).
24. *"Turned my whole winter into a summer"* — a split second of her in a grey winter coat on a grey street dissolving into the same street in full sun and the cream top, match cut.
25. *"It's glow up season, and I'm the sun"* — her friends catching up to her on the pavement, arms around her shoulders, all three walking toward camera, wide.
26. *"Nobody's shadow, I'm the only one"* — low angle: her shadow long on the pavement ahead of her, only one shadow, then tilting up to her face.
27. *"Watch me rise, watch me run"* — her breaking into a run down the sunlit street, friends laughing behind her, tracking.
28. *"It's glow up season, and I'm the sun"* — her stopping and spinning once with her face to the sun, eyes closed, medium, saturated.

### Post-chorus 1 — impact frames

29. *"Shine, shine, that's the season"* — sunlight through her spread fingers, macro, 0.5 s; a spin in the red dress, 0.5 s.
30. *"Glow, glow, I don't need a reason"* — water splashed from a bottle in the gym, slow motion, 0.5 s; her laughing straight to camera, 0.5 s.
31. *"Shine, shine, that's the season"* — reuse shot 29, tighter.
32. *"It's glow up season"* — her face to camera, a wink, freeze for one beat.

### Verse 2 — the red dress, the lease

33. *"Bought the red dress that I saved in the cart"* — a phone screen with a shopping cart holding one red dress, saved since winter (composited), her thumb pressing buy with exaggerated ceremony, close-up.
34. *"Six months waiting for the nerve to start"* — a boutique bag on the bed, the dress coming out of tissue paper, her holding it up against herself in the mirror, warm daylight.
35. *"Wore it to brunch with nowhere special to be"* — Mahima (red dress look) sliding into a corner booth at brunch, a mimosa, sunlight through the window, medium.
36. *"Corner booth, sunlight, the whole place looking at me"* — a stranger at the next table glancing over, a waiter smiling, her pretending not to notice and failing, over-the-shoulder.
37. *"Laughing so loud with my girls on the patio"* — a patio table with the two friends, all three laughing so hard one of them is wiping her eyes, wide, patio sun.
38. *"Haven't checked his page in weeks, and I don't know"* — one friend picking up Mahima's phone and miming a scroll of his page, Mahima shrugging, genuinely uninterested, medium close-up.
39. *"What he's up to, and that's the sweetest part"* — her taking the phone back, dropping it face-down on the table without looking, and reaching for her drink, close-up on the hands.
40. *"Sleeping through the night is a work of art"* — night, a soft bedroom, her asleep and peaceful, the phone face-down and dark on the nightstand, overhead, slow.
41. *"Signed the lease on a place with a view"* — a bright empty apartment, boxes, a big window with the city beyond, her signing a document on the counter (composited), wide.
42. *"Painted every wall a colour he'd have hated too"* — a roller of warm terracotta paint going up a white wall in one long stroke, her in an old shirt with paint on her cheek, close-up.
43. *"Plants on the sill and a mirror by the door"* — plants being lined up on the window sill one by one on the beat, then a full-length mirror being hung by the door, two cuts.
44. *"And the girl in it is somebody I'm rooting for"* — her catching her reflection in the newly hung mirror, paint on her cheek, and giving it a small firm nod, over-the-shoulder.

### Pre-chorus 2 — the rooftop fills

45. *"He said I'd fall apart without him"* — the rooftop of the new building at late golden hour, Mahima (red dress look) at the centre of a circle of friends telling a story, everyone leaning in, wide.
46. *"Look who's holding the whole room"* — claps on the beat: a bottle opened, a string of lights switched on, a hug, a toast, four close-ups.
47. *"Don't need a reason, don't need a witness"* — her laughing mid-story with the sun on her hair, people arriving behind her through the roof door, medium.
48. *"Sunrise came early and it's coming through"* — a slow push-in on her face as the golden light peaks, then a drone lift off the roof edge.

### Chorus 2 — golden hour on the roof

49. *"It's glow up season, and I'm the sun"* — the rooftop from the drone, twenty people dancing, Mahima in red at the centre, the city gold behind, wide.
50. *"Look at me shining, yeah, look what I've become"* — a friend filming her on a phone as she dances, her playing to it, handheld.
51. *"New hair, new dress, new door, new number"* — the four objects again, now at home: the bob in the mirror by the door, the red dress in motion, the new keys on a hook, the phone on the counter (composited).
52. *"Turned my whole winter into a summer"* — a two-second flash of the empty white apartment with boxes, dissolving into the same room painted terracotta and full of plants and people.
53. *"It's glow up season, and I'm the sun"* — reuse shot 49, closer, the drone dropping toward her.
54. *"Nobody's shadow, I'm the only one"* — the low sun throwing every dancer's shadow across the roof, hers in the middle, overhead.
55. *"Watch me rise, watch me run"* — the drone pull-back rising over the roof and the gold city.
56. *"It's glow up season, and I'm the sun"* — her arms up at the centre, the sun sitting on the skyline directly behind her, wide.

### Post-chorus 2 — party impact frames

57. *"Shine, shine, that's the season"* — a shower of petals from a plant she shakes, slow motion; a spin in the red dress.
58. *"Glow, glow, I don't need a reason"* — a cheers of four glasses, close; a burst of laughter.
59. *"Shine, shine, that's the season"* — reuse shot 57, tighter.
60. *"It's glow up season"* — her face lit gold, a wink, freeze.

### Instrumental — the day's montage, then the door

61. The drop instrumental: the salon cut, the river run, the gym nod, the paint roller, the rooftop spin, cut to the vocal chop, one shot per bar.
62. The snare build: the cuts get faster, half-bar, quarter-bar, the same shots tighter and tighter.
63. The filter sweep: one long wide shot of Mahima alone at the roof edge with the gold city behind her, breathing, still, the party soft-focus behind.
64. The breakdown: the roof door opens and Kai walks in late, a drink handed to him, blue hour arriving, the string lights on.
65. Kai spotting her across the roof, a slow half-smile, the beat dropping to claps and bass — the cut into the bridge.

### Bridge — Kai's rap, from across the room

66. *"Saw her cross the room and the whole vibe shifted"* — Kai to camera at the edge of the party, a drink in hand, low-key, the string lights behind him, medium close-up, blue hour.
67. *"Not the dress, not the hair, it's the way she's lifted"* — cutaway: Mahima laughing in the middle of the crowd, the red dress, the last sun on her, slow motion, then back to Kai.
68. *"Heard some guy walked out, thought he took the light"* — a two-second flash of the faceless ex walking out of a door, back to camera, then Kai shaking his head.
69. *"Now she's running every morning, sleeping every night"* — two quick cuts: the river run at dawn, the peaceful sleep, then Kai.
70. *"Main character energy, no script, no cue"* — Mahima holding court in the crowd, a friend handing her a sparkler, wide from Kai's side of the roof.
71. *"She don't need a co-star, she's the whole view"* — Kai gesturing at her with his drink, then the camera racking focus from him to her, she's the view, medium.
72. *"Every L he handed her, she flipped to a lesson"* — a flash of the gym mirror nod, the paint roller, the lease, on the beat, then Kai nodding.
73. *"Every door he slammed became a door to a blessing"* — the ex's door closing, hard cut to her new front door opening onto the sunlit street, match cut on the door.
74. *"So if you see her shining, don't ask who she's with"* — Kai turning to the friend next to him, a shrug, handheld.
75. *"She's with herself, and honestly, that's the gift"* — Mahima alone for one beat in the crowd, sparkler in hand, eyes closed, content, close-up.
76. *"Glow up season, tell your friends"* — Kai pointing her out to the friend beside him, then Mahima catching it across the roof and laughing, unbothered, two-shot across the party.
77. *"Once the sun comes out, it doesn't set again"* — the beat rebuilding: the whole crowd turning toward the skyline where the last pink is holding, string lights brightening, wide, drone starting to lift.

### Final chorus — key change, string lights

78. *"It's glow up season, and I'm the sun"* — the drone over the roof at blue hour, string lights, the whole party dancing, Mahima in red at the centre, wide.
79. *"Look at me shining, yeah, look what I've become"* — a slow-motion turn in the red dress with sparklers around her, close.
80. *"New hair, new dress, new door, new number"* — the four cuts one last time, all four from the rooftop: the bob, the dress, the keys in her hand, her phone handed to a friend to film (composited).
81. *"Turned my whole winter into a summer"* — a friend spraying a bottle of something fizzy, the spray catching the string lights, slow motion.
82. *"It's glow up season, and I'm the sun"* — Kai in the crowd singing the harmony, then Mahima beside her friends, the whole crowd singing, handheld.
83. *"Never was his shadow, I was always the one"* — her alone in a pool of string light, arms out, no shadow at all now, medium.
84. *"Hands up higher, here it comes"* — every hand on the roof going up on the beat, drone lifting fast.
85. *"It's glow up season, and I'm the sun"* — the drone pull-back over the roof and the lit city, her small and bright at the centre, wide.

### Post-chorus 3 — last impact frames

86. *"Shine, shine, that's the season"* — a sparkler tracing a circle, macro; a hug from both friends at once.
87. *"Glow, glow, I don't need a reason"* — her face lit by the string lights, laughing; the lit city.
88. *"Shine, shine, that's the season"* — reuse shot 86, tighter.
89. *"It's glow up season"* — her to camera, a wink, freeze, the crowd blurred behind.

### Outro — alone on the roof, then the lamp

90. *"Rooftop, last light, still warm on my face"* — the party gone in, Mahima alone at the roof edge wrapped in a blanket over the red dress, the last light on her face, slow push-in.
91. *"Didn't need him back, I just needed the space"* — her phone beside her on the ledge, screen dark, her hand resting next to it and not picking it up, close-up.
92. *"Tomorrow's a Monday and I'm up at six"* — a wide shot of her small against the darkening sky and the city lights, static.
93. *"Glow up season, and this is just the start of it"* — inside, the bedroom: the alarm being set for six (composited), the white trainers by the door, close-up.
94. *"No countdown, no comeback, nothing to prove"* — her sitting on the bed in the lamp light, hair damp, a small tired smile, medium.
95. *"Just a girl and a sky and a whole lot of room"* — the window beside the bed, the city lights beyond, the plants on the sill in silhouette, static.
96. *"It's glow up season, and I'm the sun"* — final shot: her reaching over and turning off the lamp, the room going dark except the window, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the alarm, the first salon cut, the crosswalk drop, each "I'm
the sun", the four-cut "new hair, new dress, new door, new number" every
time it lands, the instrumental, Kai's first line, "hands up higher", and
the lamp. At 122 BPM a bar is 1.97 s; choruses and post-choruses cut every
bar, the four-cut line every beat.

**The four-frame challenge.** Post the vertical cut of chorus 1 (shots
21–28) with *"it's glow up season, and I'm the sun"* on screen. The
challenge is the four-beat line: people post their own *new hair, new
dress, new door, new number* on the four beats. The crosswalk shot (21) is
the hook frame; Kai's *"she's the whole view"* (shot 71) is the second
shareable clip.

## 6. Quality-control checklist

- Three looks in the right sections: dawn look for the intro, the river and the gym; the bob and cream top from shot 8 to shot 44; the red dress from shot 35 (brunch) and every rooftop shot after
- The light only gets warmer; no shot is colder than the one before it except the two-second ex flashes
- The ex never has a visible face; he is a back walking out of a door
- Kai appears only from shot 64 on, always with the drink, never as a love interest — admiring, not pursuing
- The four-cut line lands as four distinct frames on four beats every time it appears
- All phone UI, the cart, the group chat, the lease and the alarm are composited; no model-generated text
- OpenPose on the river run and every crowd-dance shot; hands checked on every sparkler shot
- The last shot is locked-off and holds until the audio fades
