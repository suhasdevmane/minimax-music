# Wan 2.2 Shot List — "Mirror, Mirror"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
130 BPM a bar is 1.85 s, so most shots are 2–4 s and the choruses and
post-choruses cut on every bar.

## 1. Visual style

Get-ready-with-me as a coronation. Three worlds: the **bathroom** is warm
bulb light, steam and glitter, tight and intimate; the **ride and the
street** are orange streetlight and passing neon; the **club** is colour,
strobe and a mirrored wall. **The mirror is a character** — every present
shot has a reflective surface in it (the bathroom mirror, a phone, a taxi
window, chrome, the club's mirrored wall), and the reflection is often framed
as if it were a second person. Handheld, playful, close; the choruses are
wide and pulsing.

| Section | Grade | Camera |
|---|---|---|
| Intro / verse 1 | Warm bulbs, steam, glitter sparkle | Close, macro, handheld |
| Pre-chorus | Bulbs dimmed, red lipstick the brightest thing | Slow, static |
| Choruses (bathroom) | Bulbs at max, strobing softly on the kick | Wide, shot-reverse-shot with the reflection |
| Post-chorus | Bulbs steady | Jump cuts on every "say it" |
| Verse 2 | Warm, one cold phone flash, hallway spill, phone-flash pops | Handheld, on the beat |
| Pre-chorus 2 / chorus 2 | Cold memory flash, then street orange and neon | Reflections in every surface |
| Instrumental | Street to mirrored lobby to a strip of club light | Slow motion, low angles |
| Bridge | Green-cool club bathroom, one warm bulb | Extreme close-up, static |
| Final chorus / post-chorus | Club colour, strobes, mirrored wall | Wide reveal, crowd |
| Outro | Club haze, warm bulb, blue street | Slow, calm |

## 2. Character bible — paste into every prompt

**Mahima** (getting ready)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair wrapped in a white towel turban then falling in loose fresh curls, makeup being applied stage by stage, a sharp black eyeliner wing and red lipstick by the pre-chorus, wearing a black silk slip and a white bathrobe off one shoulder, grinning playful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the night out)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in loose glossy curls with a gold hair clip, full glam makeup with a sharp black eyeliner wing and red lipstick, wearing a fitted black mini dress, gold rings on every finger and black strappy heels, confident amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the bad night, memory flash)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and flat, mascara run under the eyes, wearing a grey oversized t-shirt, tired hurt expression, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — never shown at all: he exists only as a lit phone screen on the sink (name composited) and, in the outro, a faceless figure across the bar.
> a young man across a club bar, back to camera or face out of focus, dark jacket, holding a glass

**The three friends** — three young women in going-out looks, one in silver, one in red, one in a white suit, loud and warm, seen in the hallway, the taxi and the club.

The **red lipstick** goes on in the first pre-chorus and stays on to the end,
a little worn in the outro. The **black dress** is on the hook until verse 2
and on her from the zip onward. A **reflective surface** is in every present
frame.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the name on the sink, and any sign or label are
composited in the edit.** Generate the phone as a lit blank screen and
overlay the UI in post — the model cannot render legible UI, and the one
name on that phone is a story beat.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless. Keyframes first; OpenPose for the
bathroom dancing and the club walk-in; Depth for the mirror compositions,
which the model otherwise flattens. 16:9 first; 9:16 for the mirror cuts,
which are natural vertical content. Animate conservatively: a palm wiping
steam, a lipstick stroke, pins dropping, a zip closing, a door opening.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s. Mirror shots: generate the reflection as the subject and
composite her real-side profile only where both must be in frame; the model
handles a single face far better than a face and its mirror image.

## 4. Scene per lyric line

### Intro — steam on the glass

1. *"Lights on, phone down, speakers loud"* — a bathroom light switch flicked on, a phone set face-up on a tiled counter, a small speaker turned up, three quick cuts on the beat, warm bulbs around a fogged mirror.
2. *"Half past nine, I'm a one-woman crowd"* — Mahima (getting-ready look, towel turban, no makeup) stepping into frame in front of the fogged mirror, bathrobe off one shoulder, hips already moving, medium, warm.
3. *"Steam on the glass, I wipe it with my palm"* — extreme close-up of her palm wiping one clean arc through the steam, her face appearing in it, macro.
4. *"There she is. Hey you. Stay calm."* — her eyes meeting her own in the wiped arc, a slow grin, one eyebrow, static close-up.

### Verse 1 — the ritual

5. *"Hair up in a towel and a song I know by heart"* — her singing into a hairbrush at the mirror, towel turban, eyes closed, medium, handheld.
6. *"Every night out is a ritual, and this is the part"* — a slow pan across the counter: brushes, a curling iron, a lipstick, a pot of glitter, laid out like instruments.
7. *"Where the bathroom's a temple and the bulbs are a crown"* — low angle from the counter up: the row of bulbs ringing her head like a crown, her looking down at the lens.
8. *"And nobody gets to tell me to turn it down"* — her reaching over and turning the speaker up one more notch, a wink at the mirror, close-up.
9. *"Eyeliner wing so sharp it could cut"* — extreme close-up of the liner pen drawing one clean wing in a single stroke, macro, steady.
10. *"First try, no shake, that's how I know it's my luck"* — her eye opening, the wing perfect, her mouth dropping open in mock shock at herself, close-up.
11. *"Curls falling out of the pins one by one"* — pins pulled from her hair on the beat, curls dropping one at a time, over-the-shoulder into the mirror.
12. *"I'm not even dressed yet and I'm already the fun"* — her in the bathrobe doing a full spin in the tiny bathroom, arms out, wide, bulbs blurring.
13. *"Gloss on the counter, glitter on the floor"* — the pot of glitter knocked over in slow motion, a sparkle cloud landing on the tiles, macro.
14. *"A dress on the hook that I've been saving for"* — a slow tilt up a black mini dress hanging on the back of the bathroom door, warm light through the fabric.
15. *"Hype on the speaker, I'm singing off-key"* — her belting at the mirror with the curling iron as a microphone, laughing at her own note, medium.
16. *"The mirror's my hype girl, and she's staring at me"* — shot-reverse-shot: her pointing at the mirror, then the reflection filmed as its own person pointing back, cut on the beat.

### Pre-chorus 1 — the red goes on

17. *"Ask the glass, it's never lied"* — the bulbs dim a touch, her picking up the red lipstick, the cap clicking off in extreme close-up.
18. *"It's the only one that's always on my side"* — her eyes to the mirror, steady, the reflection holding her gaze, static.
19. *"One deep breath, the red goes on slow"* — the first stroke of red going on slowly, her breath held, the red the brightest thing in frame, macro.
20. *"Say it with me, mirror, you already know"* — her lips pressing together once, then lifting her eyes to the glass with a dare, close-up, the last beat before the drop.

### Chorus 1 — mirror, mirror

21. *"Mirror, mirror, tell me who's the baddie"* — the drop: the bulbs flare, Mahima (getting-ready look, full face now) dancing at the mirror in the bathrobe, wide, the bulbs pulsing on the kick.
22. *"Don't act shy, you've been looking at me"* — the reflection alone in frame, filmed as a second person, a coy look away and back, close-up.
23. *"Mirror, mirror, say it to my face"* — her leaning in until her nose almost touches the glass, grinning, over-the-shoulder.
24. *"Nobody in this city's gonna take my place"* — a one-second flash of a city skyline at night through a taxi window, then hard back to the bathroom.
25. *"I'm the whole event, I'm the reason they came"* — her climbing onto the edge of the tub to see her whole self in the mirror, arms up, wide, low angle.
26. *"Every bulb around you is spelling my name"* — a rack focus from the ring of bulbs blurred into bokeh to her face sharp in the middle of them.
27. *"Mirror, mirror, tell me who's the baddie"* — her and the reflection singing the line together, split down the frame's centre by the mirror's edge, medium.
28. *"You already know, and baby, so does everybody"* — a one-frame flash of a club door opening onto a crowd, then back to her laughing at the mirror on the last word.

### Post-chorus 1 — say it

29. *"Say it, say it, who's the baddie"* — jump cuts on every "say it": a different pose in the same frame, hands on hips, chin up, a peace sign.
30. *"Say it to my face, say it back at me"* — her cupping a hand to her ear at the mirror, the reflection doing the same a beat late, playful.
31. *"Say it, say it, who's the baddie"* — jump cuts again, faster, the bathrobe slipping off the other shoulder, laughing.
32. *"Lights up, doors up, it's me, it's me"* — her pointing at the reflection on "it's me", the reflection pointing back, then both pointing at the lens, close-up.

### Verse 2 — the wrong name, the dress, the girls

33. *"Phone lights up, it's a name I don't need"* — the phone on the counter lighting up (blank lit screen, name composited), her eyes flicking to it mid-curl, a cold flash on her jaw.
34. *"Someone who used to say I was too much to be seen"* — a slow push-in on her face as she reads it, the grin gone for one breath, close-up.
35. *"Cute. I flip it face down on the sink"* — her hand turning the phone over in one clean motion onto the porcelain, extreme close-up, the glow dying.
36. *"This red on my lips is louder than anything he thinks"* — her reapplying the red straight at the mirror, one stroke, then a smile that shows teeth, close-up.
37. *"Zip on the dress, it's black and it's mean"* — the black dress coming off the hook, the zip closing up her back in extreme close-up on the beat.
38. *"Heels that could walk straight out of a magazine"* — black strappy heels stepping onto the tile one at a time, low angle, glitter on the floor around them.
39. *"Perfume on the wrist, on the neck, in the air"* — perfume misted into the air and her walking through the cloud, backlit by the bulbs, slow motion.
40. *"Rings on every finger and a clip in my hair"* — gold rings sliding on one by one, then the gold clip snapping into her curls, macro, on the beat.
41. *"The girls at the door, all three of them screaming"* — the bathroom door opening from the hallway side: three friends in silver, red and a white suit losing their minds, phone flashes, handheld.
42. *"Phone up, flash on, this is the reveal scene"* — Mahima (night-out look, the full reveal) in the doorway doing a slow turn for their phones, flashes popping on the beat, medium.
43. *"Keys, gloss, one last kiss to the glass"* — her turning back to the mirror, blowing it a kiss, then grabbing keys and gloss off the counter, close-up.
44. *"Don't wish me luck, wish the city luck, I'm out the door at last"* — the four of them piling out of the apartment door into the hallway, her last, the bathroom light clicking off behind her, tracking.

### Pre-chorus 2 — the mirror saw the bad nights too

45. *"Ask the glass, it's never lied"* — her hand on the front door handle, one beat of stillness, the friends' noise behind her, close-up.
46. *"Even on the nights I cried, it stayed on my side"* — a two-second cold flash: Mahima (bad-night look) at the same bathroom mirror, mascara run, the bulbs on, the mirror holding her, then hard back to now.
47. *"One deep breath, the door's about to go"* — her breath in, the door opening onto the street, streetlight orange and a taxi's headlights, medium.
48. *"Say it with me, mirror, you already know"* — her reflection sliding across the taxi's dark window as she walks to it, the city lights over her face, tracking.

### Chorus 2 — every surface in the city

49. *"Mirror, mirror, tell me who's the baddie"* — the taxi, four girls in the back, windows down, Mahima singing the line into the window glass, her reflection singing back, close-up.
50. *"Don't act shy, you've been looking at me"* — the taxi's rear-view mirror with her eyes in it, then the driver's eyes flicking up, amused, extreme close-up.
51. *"Mirror, mirror, say it to my face"* — the wing mirror catching her leaning out of the window, hair in the wind, neon sliding past.
52. *"Nobody in this city's gonna take my place"* — the skyline through the windscreen, the city lights doubled in the glass, wide.
53. *"I'm the whole event, I'm the reason they came"* — the four girls singing at once in the back seat, phones up, flashes, handheld, joy.
54. *"Every bulb around you is spelling my name"* — a shop window at a red light: neon signs (abstract shapes, no text) framing her reflection in the glass, static.
55. *"Mirror, mirror, tell me who's the baddie"* — reuse shot 49, tighter, her grin bigger.
56. *"You already know, and baby, so does everybody"* — the taxi pulling up at a kerb, the club door in the distance with a queue, her stepping out first, heels on wet pavement, wide.

### Instrumental — the walk to the door

57. Heels on wet pavement in slow motion, streetlight orange in the puddles, low angle tracking.
58. The four girls walking in a line, coats open, the club's light ahead, wide from the front, slow motion.
59. A bouncer's rope lifting, her hand brushing it as she passes, close-up.
60. A mirrored lobby wall multiplying Mahima a dozen times as she walks along it, tracking from the side.
61. The club door, still closed, coloured light in a strip beneath it, bass leaking through, static; then a hard cut to black on the pad.

### Bridge — just glass

62. *"Lean in close, I'll tell you the truth"* — the club bathroom, quieter, green-cool light and one warm bulb, Mahima (night-out look) leaning in close to a different mirror, extreme close-up.
63. *"The mirror is just glass, it's got nothing to prove"* — the reflection alone in frame, then her fingertips touching the glass, static.
64. *"It only shows back what I carry inside"* — her eyes in the mirror, steady, a slow push-in, the bass muffled through the wall.
65. *"And I've been carrying it through every bad night"* — a one-second echo of the bad-night mirror flash, then her now, the same eyes, calmer.
66. *"The girl who cried at it, she's still in there"* — her hand flat on the glass over her own reflection's heart, close-up.
67. *"She just learned to walk in like she owns the air"* — her straightening up, fixing one curl, shoulders back, medium, the warm bulb catching the gold clip.
68. *"So when the doors swing open and the whole floor turns"* — her walking toward the bathroom door with her back to camera, the strip of coloured light under it widening, tracking.
69. *"That's not a trick of the light, that's the thing I earned"* — her hand on the door, a breath, the bass swelling, extreme close-up.

### Final chorus — the doors

70. *"Mirror, mirror, tell me who's the baddie"* — the doors swing open onto the floor, Mahima in the frame with light behind her, the whole crowd turning, wide from inside the club, strobe on the kick.
71. *"Don't act shy, you've been looking at me"* — faces in the crowd turning toward her, one after another, handheld.
72. *"Mirror, mirror, I don't need you to say"* — her walking in, the crowd parting, the mirrored wall along the floor catching her from the side, tracking.
73. *"I took your answer with me when I walked away"* — the three friends falling in behind her, the four of them cutting through the floor, wide.
74. *"I'm the whole event, I'm the reason they came"* — her in the middle of the floor, arms up, the strobes on her, low angle, slow motion.
75. *"Every light in this club is spelling my name"* — the lighting rig from below, beams sweeping over the crowd, then down onto her.
76. *"Mirror, mirror, tell me who's the baddie"* — the mirrored wall: her and a hundred reflections dancing, wide.
77. *"You already know, and baby, so does everybody"* — the crowd's hands up around her, her laughing, the friends screaming the line, handheld.

### Post-chorus 2 — the whole floor

78. *"Say it, say it, who's the baddie"* — jump cuts through the crowd on every "say it", hands up, strobing.
79. *"Say it to my face, say it back at me"* — a stranger in the crowd cupping a hand to their ear at her, her cupping hers back, playful.
80. *"Say it, say it, who's the baddie"* — the four friends in a line at the mirrored wall, each striking a pose on a "say it".
81. *"Lights up, doors up, it's me, it's me"* — her pointing at the mirrored wall on "it's me", a hundred reflections pointing back, wide.

### Outro — you were right about me

82. *"Lights low, phone up, the bass in my chest"* — later, the floor in a slower haze, Mahima's phone up filming the room, slow motion, close.
83. *"Half past twelve and I'm still the best dressed"* — a glass on the bar shaking with the bass, then her leaning on the bar, lipstick a little worn, still grinning, medium.
84. *"Somebody's staring, I'll let him stare"* — a faceless figure across the bar (back to camera, out of focus) looking her way, her glancing over and back with a shrug.
85. *"Every mirror in this building knows I'm here"* — the mirrored wall behind the bar with her in it, bottles and light, static.
86. *"Catch me in the window, catch me in the chrome"* — her reflection in the chrome of the bar rail, then in the dark window as the four of them step out onto the street, two quick cuts.
87. *"Every shiny thing in this city's gonna walk me home"* — the street at half past midnight, the four girls walking, heels in hand, her reflection sliding along a dark shop window beside her, tracking from the side.
88. *"Mirror, mirror, you were right about me"* — her stopping at the shop window, tapping the glass twice with a ring, a small nod to herself, close-up.
89. *"You were right about me"* — final shot: the reflection in the shop window as she walks out of frame, the empty glass holding the street lights, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the light switch, the palm wipe, the first lipstick stroke, the
drop, each "mirror, mirror", each "say it", the phone flip, the reveal, the
door onto the street, the instrumental, "just glass", the club doors, and
the last "right about me." At 130 BPM a bar is 1.85 s; choruses and
post-choruses cut every bar, the post-chorus jump cuts every half bar.

**Get-ready-with-me challenge.** The post-chorus is a transition built for
the format. Post the vertical mirror cut of shots 29–32 with *"mirror,
mirror, tell me who's the baddie"* on screen and invite people to film their
own mirror transition: towel and bare face on the first *"say it"*, full look
on *"it's me, it's me."* The palm wiping the steam (shot 3) is the second
shareable frame, and *"don't wish me luck, wish the city luck"* is the
caption.

## 6. Quality-control checklist

- Three looks in the right sections: towel turban and bathrobe through the first post-chorus, the black dress from shot 37 on, the bad-night look only in shots 46 and 65
- The red lipstick goes on in shot 19 and is present in every shot after it, slightly worn from shot 83
- A reflective surface in every present-day frame: bathroom mirror, phone, taxi glass, chrome, the mirrored wall, the shop window
- The ex never appears with a face: a lit phone screen on the sink, and a back at the bar
- All phone UI and the name on the sink composited; neon signs are abstract shapes, no readable text
- Mirror shots generated with the reflection as the subject; no doubled or mismatched faces
- No distorted hands, especially the lipstick, zip, ring and phone close-ups
- The last shot is locked-off on the empty shop window and holds until the audio fades
