# Wan 2.2 Shot List — "Festival Season"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Uptempo: at 128 BPM a bar is 1.875 s, so most shots are 2–4 s
and the choruses cut on every bar. Take timestamps from the rendered WAV.

## 1. Visual world

One festival weekend, Friday noon to Sunday afternoon, told in order. The
**field is the set**: tents, mud, flags on poles, the ferris wheel on the far
edge of the sky. Three light worlds: **Friday day** is flat bright and
dusty; **the nights** are stage rig, lasers, phone lights, confetti; **the
sunrise set** is pink-to-gold and the softest frames in the video. The two
crew flags (one yellow, one pink) are the recurring landmark, and the
**wristband** is on her wrist from shot 1 to the last frame. Glitter and
mud accumulate on her across the weekend and are never cleaned off.

| Section | Grade | Camera |
|---|---|---|
| Intro / Friday | Flat bright noon, dust, overexposed sky | Handheld, quick |
| Verse 1 | Rain grey turning gold, then golden hour | Handheld, wide field shots |
| Pre-choruses | Blackout, phone glow, one beam | Slow push-ins, then still |
| Choruses (night) | Full rig, strobes, lasers, confetti | Aerial + rail handheld, cut every bar |
| Post-choruses | Strobe on the claps, white wash | Ultra-fast, on the beat |
| Verse 2 | Saturday sun, then night from a stranger's shoulders | Handheld, high POV |
| Instrumental | Darkest and brightest frames side by side | Slow motion + drone |
| Bridge | Pre-dawn navy to pink, string bulbs | Still, wide, tender |
| Final chorus | Full sunrise gold, lens flare | Drone rising with the sun |
| Outro | Overcast Sunday softness, bus glass | Slow, calm |

## 2. Character bible — paste into every prompt

**Mahima** (Friday)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose under a straw bucket hat, glitter pressed onto her cheekbones, wearing a white cropped vest, denim shorts and white trainers already muddy, a fabric festival wristband on her left wrist, wide open grin, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (Saturday night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in two loose braids with glitter through them, sunburnt shoulders, wearing a mesh long-sleeve over a black bralette, denim shorts, mud to the ankles, the festival wristband on her left wrist, ecstatic screaming-the-words expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (sunrise / Sunday)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and tangled with glitter still in it, no makeup left but glitter traces, wearing an oversized grey hoodie over the same shorts, barefoot on wet grass, the festival wristband on her left wrist, tired peaceful expression, realistic cinematic photography, consistent identity, natural skin texture

**The crew** — four friends, two women and two men, early twenties, always as a group, always under or near the yellow and pink flags. Casual festival wear, glitter, ponchos in the rain. Warm, never posed.

**The stranger in the bucket hat** — never shown clearly: a shoulder, the back of a bucket hat, hands holding her ankles as she sits on his shoulders. Face out of frame or turned to the stage.
> a young man in a khaki bucket hat, back to camera or face turned away toward the stage, dark t-shirt

**The DJs** — silhouettes on a stage against the rig, never a face.

Objects: the **two flags** (one yellow, one pink, on long poles), the
**wristband**, the **paper cup**, the **ferris wheel**, the **hay bale**
outside the sunrise tent.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the two-percent battery, stage LED walls and any
signage are composited in the edit.** Generate the phone as a lit blank
screen and the stage screens as abstract colour washes; the model cannot
render legible UI or lettering, and festival stages are covered in both.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; the
glitter and mud must persist look to look, so approve the stills in weekend
order. Keyframes first; OpenPose for the jumping, the shoulders lift and the
rail conducting shot; Depth for the wide field and drone compositions.
16:9 first; 9:16 for the chant cut and the shoulders POV, which are natural
vertical content. Crowds are the hard part: generate the crowd plates wide
and slow, and keep the hero shots to Mahima plus the four crew members;
the negative prompt's "many people in the background" is relaxed only for
the explicit crowd plates. Animate conservatively: hands rising, confetti
falling, flags moving, the wheel turning, mud spray in slow motion.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s; the chant impact shots 0.5 s.

## 4. Scene per lyric line

### Intro — Friday noon, the wristband

1. *"Wristband on and the tent's half up"* — extreme close-up of a fabric festival wristband being snapped shut on Mahima's wrist (Friday look), then a rack focus past her to a half-collapsed tent with two crew members fighting the poles, flat bright noon, handheld.
2. *"Warm cider in a paper cup"* — a paper cup lifted into the sun, condensation and dust, her face behind it squinting and grinning, close-up, overexposed sky.
3. *"Bass in the ground before we see the stage"* — her bare feet on the grass, then a low shot across the campsite field with the far stage rig as a shape on the horizon, the grass vibrating in macro, wide.
4. *"Three days off from acting my age"* — Mahima spinning once with her arms out in the middle of the campsite, hat coming off, the crew laughing behind her, medium, dust in the light.

### Verse 1 — mud, glitter, flags

5. *"Parked in a field in the wrong kind of shoes"* — rows of cars on a grass car park, Mahima climbing out in white trainers and looking down at them, then at the mud, comic resignation, medium.
6. *"Glitter on my cheekbones and nothing to lose"* — a crew member's thumb pressing glitter onto Mahima's cheekbone, extreme close-up, her eyes closed and smiling, warm light.
7. *"Rain came down at four and nobody ran"* — a downpour arriving over the crowd, everyone looking up, and then a wave of arms rising instead of anyone running, wide, grey light.
8. *"Mud to the ankles, we danced where we stand"* — feet stamping in mud to the ankles in a circle, the crew dancing exactly where they stood, rain on their shoulders, low angle, slow motion.
9. *"Flags on long poles so the lost ones can find us"* — two flags on long poles going up above the crowd, one yellow and one pink, seen from a distance through heads, the rain passing and gold light breaking through, wide.
10. *"A yellow one, a pink one, the whole crew behind us"* — the crew gathered under the flags, five of them in a row, Mahima in the middle, arms around shoulders, medium, washed gold.
11. *"Someone's got a speaker, someone's got a drum"* — a portable speaker carried on a shoulder, a hand drum being slapped, quick cuts on the beat, handheld.
12. *"Someone's mom packed sandwiches enough for everyone"* — a cool box opening on foil-wrapped sandwiches, hands reaching in, Mahima with a sandwich in one hand and a cup in the other, laughing, close-up.
13. *"Phone at two percent and I'm not gonna charge it"* — her phone screen (blank lit, battery composited) in her hand, then her sliding it into her back pocket and leaving it, close-up on the hands.
14. *"Whatever this weekend is, I don't wanna watch it"* — her looking straight ahead at the field with nothing in her hands, the crew moving past her, slow push-in on her face, golden hour.
15. *"Walk through the gate like we've done it a hundred times"* — the crew walking through the main gate in a line, wristbands raised, a security guard nodding them in, tracking from the front.
16. *"Big wheel turning slowly on the far end of the sky"* — the ferris wheel on the far edge of the site, lights just coming on, turning slowly against the last of the sun, wide, static, hold.

### Pre-chorus 1 — the low end rolls in

17. *"Hear that low end rolling in over the hill"* — the main stage crowd at dusk, a bass note visible as every head turning toward the stage at once, wide from behind.
18. *"Ten thousand strangers going quiet and still"* — the crowd going still, hands rising, the stage lights cutting to black, wide, the last of the sky.
19. *"Hands up, lights out, one breath, then the drop"* — Mahima's face in the dark lit only by phone glow around her, eyes closed, one breath, extreme close-up, slow push-in.
20. *"Somebody count me in, I'm never gonna stop"* — her eyes opening, a single beam from the stage cutting across the crowd toward her, still.

### Chorus 1 — the drop

21. *"It's festival season, and we're not going home"* — the drop: the full rig blasting on, lasers, confetti cannons, the entire field jumping, aerial, wide.
22. *"Glitter in the mud and my voice is gone"* — Mahima mid-jump at the rail screaming the line, glitter streaked, mud on her legs, handheld, strobe.
23. *"Sing it with the stranger on your left and your right"* — her with her arms over the shoulders of two strangers (faces turned to the stage), all three singing, medium, lasers behind.
24. *"We came for the weekend, we're staying for the light"* — a laser sweep across ten thousand raised hands, then confetti falling through the beams, wide.
25. *"It's festival season, and the field's on fire"* — the crowd from above as one moving surface, the flags scattered across it like landmarks, drone.
26. *"Every flag's a friend and every song's a choir"* — the yellow and pink flags waving in the middle of the crowd, the crew beneath them, lit by the rig, medium wide.
27. *"Hands up high, it's festival season"* — Mahima's hands up, glitter on her palms catching a strobe, low angle, slow motion.
28. *"And we're not going home, no, we're not going home"* — her turning to a crew member beside her and shouting the line into their face, both laughing, handheld, close.

### Post-chorus 1 — the chant (0.5 s impact shots)

29. *"Not going home, not going home"* — rows of raised hands clapping on the beat; a confetti cannon firing.
30. *"Oh oh, oh oh oh, we're not going home"* — the DJ silhouette with both hands up; the crowd's phone lights swaying.
31. *"Not going home, not going home"* — the yellow flag whipping; mud spraying off a jumping boot.
32. *"Oh oh, oh oh oh, we're not going home"* — Mahima's face in a strobe, mouth open on the chant, hold for the bar.

### Verse 2 — Saturday, the shoulders

33. *"Saturday, sunburnt shoulders and a borrowed hat"* — Saturday afternoon, Mahima (Saturday look) with pink sunburnt shoulders pulling a borrowed straw hat down, squinting, close-up, hard sun.
34. *"Lost the crew by the food trucks, found them just like that"* — her alone in a food-truck queue scanning the crowd, then spotting the yellow flag over the heads and breaking into a run toward it, tracking.
35. *"A boy in a bucket hat said, can you see from there"* — night, the second stage, a stranger in a khaki bucket hat (face turned to the stage) crouching and offering his shoulders, her hesitating for one beat, medium.
36. *"Then he lifted me up and I was waving in the air"* — her rising above the crowd on his shoulders, arms out, the stage wash from below, low angle, slow motion.
37. *"Ten thousand phone lights like a low-hung sky"* — her POV from above the crowd: ten thousand phone lights spread to the horizon, the real stars faint above, wide.
38. *"Confetti cannons and the drummer up high"* — confetti cannons firing, a drummer on a riser above the stage lit in silhouette, the confetti falling past her face, close-up.
39. *"I don't know his name and I don't need to know it"* — her sliding down off his shoulders, a hand on his shoulder for a thanks, his face never in frame, medium.
40. *"Some nights you get a moment and you don't have to own it"* — her walking back through the crowd toward the pink flag without looking back, a small private smile, tracking from the front.

### Pre-chorus 2 — the front rail

41. *"Hear that low end rolling in over the hill"* — Saturday night, the main stage, Mahima at the front rail, both hands on it, the crowd behind her turning as one, medium from the stage side.
42. *"Ten thousand strangers going quiet and still"* — reuse shot 18, from the rail this time, the stillness closer.
43. *"Hands up, lights out, one breath, then the drop"* — her face at the rail in blackout, glitter in her braids catching a phone glow, one breath, close-up.
44. *"Somebody count me in, I'm never gonna stop"* — the single beam landing directly on her at the rail, her grin, still.

### Chorus 2 — Saturday's peak

45. *"It's festival season, and we're not going home"* — the bigger drop, fireworks over the stage, the whole crew at the rail together, wide from behind them.
46. *"Glitter in the mud and my voice is gone"* — the crew's faces in a row at the rail, each singing, mouths open, glitter streaked, tracking along the line.
47. *"Sing it with the stranger on your left and your right"* — reuse shot 23, fireworks reflected in the strangers' eyes.
48. *"We came for the weekend, we're staying for the light"* — a drone rising over the field, flags and lights and fireworks to the horizon.
49. *"It's festival season, and the field's on fire"* — the field from above lit red by the fireworks, every hand up, drone.
50. *"Every flag's a friend and every song's a choir"* — a slow pan across dozens of flags in the crowd, each one moving, the pink and yellow among them, medium wide.
51. *"Hands up high, it's festival season"* — reuse shot 27, fireworks behind her hands.
52. *"And we're not going home, no, we're not going home"* — Mahima on the rail turned around to face the crowd, conducting them with both arms, the crowd shouting back, wide from the stage.

### Post-chorus 2 — the chant, louder

53. *"Not going home, not going home"* — the clap, wider, more hands; a firework bursting.
54. *"Oh oh, oh oh oh, we're not going home"* — the crew jumping in unison at the rail, strobe.
55. *"Not going home, not going home"* — the pink flag; a boot in the mud.
56. *"Oh oh, oh oh oh, we're not going home"* — Mahima's face, hoarse, still shouting, hold.

### Instrumental — the drop stripped, the build, the breakdown, the drop

57. The crowd jumping in slow motion, mud spraying up in sheets, lasers overhead, low angle.
58. A laser sweep over ten thousand hands, seen from the stage, the beams cutting through smoke.
59. The crew running between stages through the dark campsite paths, flags on poles bouncing above them, tracking.
60. The ferris wheel spinning lit from directly below, the sky black behind it, slow.
61. The riff drop: a hard cut back to the rail, everyone jumping, the biggest strobe of the video, then a filtered flash of Mahima's face on the vocal chop, into the bridge.

### Bridge — four a.m., the sunrise set

62. *"Four a.m., the main stage dark, the small tent's still going"* — the main stage as a dark shape in a blue pre-dawn, and at the edge of frame a small tent glowing with a string of bulbs, wide, still.
63. *"Sunrise set, the sky turns pink and nobody is slowing"* — inside the tent, a small crowd swaying to a soft set, the sky through the open side going navy to pink, medium wide.
64. *"My legs are gone, my voice is gone, there's glitter in my hair for weeks"* — Mahima (sunrise look, hoodie, barefoot) sitting on a hay bale outside the tent, trainers beside her, glitter in her tangled hair, close-up, pink light.
65. *"But I found a girl I really like, and she looks a lot like me"* — her catching her reflection in a puddle in the wet grass, glitter and mud and a tired smile looking back, overhead, still.
66. *"Monday's got a train and a desk and a boss who knows my name"* — a two-second flash of an empty office desk under fluorescent light, then back to her face in the pink field, the contrast.
67. *"But right now I'm the girl in the field who danced through all the rain"* — her standing up from the hay bale in the wet grass, arms out, a slow turn, the sky going gold, wide.
68. *"The sun climbs up the ferris wheel, the last DJ takes a bow"* — the sun rising through the spokes of the ferris wheel, lens flare, and the DJ silhouette in the tent raising a hand and bowing, two shots.
69. *"And ten thousand people whisper, we're not going anywhere now"* — the small tent crowd spilling out into the sunrise, quiet, faces to the light, Mahima among them, wide, slow push-in.

### Final chorus — sunrise drop

70. *"It's festival season, and we're not going home"* — the sunrise drop: the small crowd and the crew dancing in full daylight in the mud, the sun behind them, wide, gold.
71. *"The sun's coming up and my voice is gone"* — Mahima singing the line with no voice left, laughing at herself, hoodie sleeves over her hands, close-up, sun flare.
72. *"Sing it with the stranger on your left and your right"* — her arms around two strangers from the sunrise tent, faces to the sun, medium.
73. *"We came for the weekend, we're leaving with the light"* — the yellow and pink flags going up one more time against the morning sky, low angle.
74. *"It's festival season, and the field's still on fire"* — a drone rising with the sun over the field, tents and flattened grass and the small tent's crowd dancing, gold.
75. *"Every flag's a friend and every song's a choir"* — the crew in a line with their arms linked, jumping in the wet grass, tracking along them.
76. *"Hands up high, it's festival season"* — her hands up in the sunrise, glitter on her palms catching the sun instead of a strobe, slow motion, low angle.
77. *"And we're not going home, no, we're not going home"* — her collapsing backward onto the hay bale laughing, the crew piling on, handheld, warm.

### Post-chorus 3 — the last chant

78. *"Not going home, not going home"* — a few hundred people clapping in daylight, hoarse; the sun through the wheel.
79. *"Oh oh, oh oh oh, we're not going home"* — the crew's faces in the sun, eyes closed, still singing.
80. *"Not going home, not going home"* — the flags; muddy bare feet in wet grass.
81. *"Oh oh, oh oh oh, we're not going home"* — Mahima's face in the morning light, singing softly now, hold.

### Outro — Sunday, the bus

82. *"Sunday, tent down, mud on my knees"* — Sunday, overcast, Mahima on her knees in the mud folding a tent, the field emptying around her, wide.
83. *"Wristband stays on till it falls off me"* — extreme close-up of the wristband on her wrist as she pulls her hoodie sleeve down over it and leaves it on.
84. *"Bus back to the city with my head on the glass"* — the bus: her forehead against the window, the field sliding past, the crew asleep around her, close-up, soft light.
85. *"Still hear the drop, still feel the bass"* — her eyes closed against the glass, a small smile, a two-second flash of the drop from shot 21, then back to the bus.
86. *"Same field next year, same crew, same song"* — the crew asleep across the bus seats, the yellow flag rolled up on the rack above them, medium.
87. *"It's festival season, and we're not going home"* — final shot: the empty field from above, flattened grass squares where the tents were, the ferris wheel still turning, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the wristband click, each "festival season", the first drop,
every chant, the shoulders lift, the instrumental, "she looks a lot like
me", the sunrise drop and the final wheel. At 128 BPM a bar is 1.875 s;
choruses cut every bar, chants every half-bar.

**Recap challenge.** The post-chorus chant is the challenge: post your own
festival recap cut to *"not going home, not going home"* with the clap on
the beat. The vertical cut is shots 29–32 with the chant on screen. The
second shareable frame is the shoulders POV (shots 36–37), and the caption
line is *"Some nights you get a moment and you don't have to own it."* The
wristband shot (83) is the post-festival-blues clip.

## 6. Quality-control checklist

- Three looks in weekend order: Friday hat and white vest; Saturday braids and mesh; sunrise hoodie and bare feet from shot 62 on
- Glitter and mud only ever accumulate; nothing is cleaned off between sections
- The wristband is on her left wrist in every shot from 1 to 87
- The bucket-hat stranger and the DJs never have a visible face
- The yellow and pink flags appear in every chorus and the outro bus rack
- All phone screens, battery UI and stage LED walls composited; no model-generated text
- Crowd plates generated wide and slow; hero shots limited to Mahima plus the four crew
- The last shot is locked-off from above and holds until the audio fades
