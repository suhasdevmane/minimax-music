# Wan 2.2 Shot List — "After Hours"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
132 BPM a bar is 1.82 s, so most shots are 2–4 s and the two-step sections
cut on the off-beat snare rather than the downbeat.

## 1. Visual style

London, half three to half seven, in three rooms and one street. The grade
runs backwards from the usual: the video **starts** under the ugliest light
it will ever have — club strip lights — goes almost completely dark on the
stairwell, spends its warm middle under a single lamp, and ends in flat
honest daylight that is now kind rather than cruel. Handheld, close, cramped
framing: the flat is genuinely too small and the shots should say so.
Practical light only. Slight lens condensation on the bus and balcony shots.

| Section | Grade | Camera |
|---|---|---|
| Intro | Flat white strip light, ugly on purpose | Wide, slow, static |
| Verse 1 (street, bus) | Sodium orange outside, hard fluorescent in | Handheld, cramped |
| Verse 1 (stairwell) | Phone torches only, near black | Following, unstable |
| Pre-choruses | Ceiling light to one warm lamp | Static, close |
| Choruses | Lamp, kitchen strip through a doorway, streetlight | Handheld, in the crowd |
| Post-chorus | Same, four hard cuts | 0.5 s, ultra-fast |
| Verse 2 | Lamp low, faces half-lit, warm | Static, patient, longer takes |
| Instrumental | Warm room against cold hallway | Roaming, one long move |
| MC verse | Half kitchen strip, half lamp | Steady, following him |
| Bridge | First natural light, grey-gold | Still, wide, quiet |
| Final chorus | Daylight winning, lamp still on | Handheld, wide |
| Outro | Flat morning daylight | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (all night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair straightened and starting to fall out of shape, sharp evening makeup, wearing a black slip top and wide-leg trousers with a cropped leather jacket carried over one arm, silver hoops, alert amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (in the flat, from the first pre-chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pushed back off her face, evening makeup slightly worn, wearing a black slip top and wide-leg trousers, no shoes, socks on, holding a mug in both hands, warm relaxed expression, realistic cinematic photography, consistent identity

**Kai** (the MC, whose sister's flat it is)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a plain navy zip-up over a white tee and dark jeans, a tea towel over one shoulder from the second chorus, calm watchful expression, realistic cinematic photography, consistent identity

**The nine** — a real group, faces welcome: a young man who sits on the
floor with a mug in both hands, a young woman leaning in the kitchen
doorframe reading off her phone, a friend still singing on the pavement, two
people crowded into a bathroom mirror, a sleeper in a parka in the hallway.
Nobody here is an ex and nobody needs hiding.

Objects: the **wall switch**, the **single lamp**, the **kettle**, the
**glass of water on the radiator** that trembles with the bassline, the
**pile of coats on the bed**, the **shop shutter**, the **mugs going cold on
the windowsill**, the **parka**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the cooker clock, the out-of-order lift note, the
shopfront and the group-chat notification are composited in the edit.**
Generate phones as lit blank rectangles and shopfronts as unlettered
signage; the model cannot render legible text and this video is full of
small screens.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai in his with IP-Adapter or a character LoRA
each. OpenPose for the two-step shuffle, the dancing in daylight and the
crowded bathroom mirror; Depth for the cramped flat interiors, which the
model otherwise widens into an apartment nobody in this song could afford.
16:9 first; 9:16 for the bus, stairwell and balcony cuts, which are naturally
vertical. Animate conservatively and in short bursts: a switch being hit, a
kettle boiling, a torch beam swinging, a glass trembling, one shuffle cycle.
Low-light shots (stairwell, bridge) need the still to be graded before
animation or the model raises the black level on its own.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — the club emptying

1. *"Strip lights up and the music is gone"* — wide of a small club under flat house strip lights, sticky floor, abandoned cups on a ledge, the room suddenly ugly, static.
2. *"Doorman counting us out one by one"* — a doorman at the exit with a hand out counting people past him, seen from inside, backlit by the street, medium.
3. *"Everybody's got a bed and nobody wants it"* — a slow pan across a group standing in the middle of the emptying floor, nobody moving toward the door, wide.
4. *"Somebody's got a key in their pocket"* — a hand pulling a keyring half out of a jacket pocket and pushing it back, close-up, no faces.
5. *"So the night is only halfway done"* — Mahima in the middle of the room with her jacket over one arm, entirely unbothered by the strip lights, medium, held.

### Verse 1 — pavement, bus, stairwell

6. *"Out on the pavement and my ears are still ringing"* — the group spilling onto a wet pavement under sodium orange, one of them holding both ears, handheld.
7. *"Lost the cloakroom ticket and my mate is still singing"* — a friend patting every pocket while another sings at the sky, medium two-shot, street light.
8. *"Somebody says, my sister's flat, it's two stops on the bus"* — a young woman pointing down the road mid-sentence, the whole group turning to follow the point, wide handheld.
9. *"So we're up on the top deck with the windows full of us"* — the front seats of a night bus top deck, six people across three seats, condensation on the glass, hard fluorescent, static from the stairwell.
10. *"Past the shutter coming down and the fella with the mop"* — a shop shutter rolling down to knee height, a man mopping visible beneath it, low angle from the pavement.
11. *"Two flights up above the fryers where the smell doesn't stop"* — a narrow side door beside the unlettered shopfront, the group going through it, tilt up the building to two lit windows.
12. *"The hallway light's been broken since the year before last"* — a dead bulb in a lino stairwell, a hand flicking a switch twice with nothing happening, close-up, near black.
13. *"So we're going up on phone torch and we're going up fast"* — four phone torch beams swinging up a lino staircase, feet, a hand on a bannister, the darkest shot in the video, following.

### Pre-chorus 1 — the big light goes off

14. *"Big light off and the little lamp on"* — a hand hitting the wall switch, the room dropping from ceiling light to a single lamp in one frame, static, the video's hinge.
15. *"Somebody's playing an old garage song"* — a phone going into a speaker dock (screen composited), a thumb pressing play, close-up.
16. *"The coats are all piled on the end of the bed"* — coats landing one after another on a bed in a small dark bedroom, seen from the doorway.
17. *"And the truth gets a chair and it sits down instead"* — a kitchen chair carried into the front room and set down in the middle of the floor, then nobody sits on it, medium, held.

### Chorus 1 — the flat finds its shape

18. *"After hours, that's when the night gets honest"* — nine people in a front room built for four, all moving slightly, Mahima in socks in the middle with a mug, handheld from inside the crowd.
19. *"Nobody's posing and nobody's promised"* — three faces in close succession, none of them performing, no phones up, close-ups.
20. *"Kettle going and the bassline low"* — a kettle rising to the boil in a tiny kitchen, steam on a window, macro.
21. *"Say the thing that you couldn't say downstairs, then let it go"* — two people talking in a doorway with their heads close together, the room loud around them, medium.
22. *"After hours, when the shutters come down"* — from the flat window, looking down at the shuttered shopfront and the empty street, static.
23. *"Half a flat, half a city, one sound"* — the glass of water on the radiator trembling with the bassline, macro, the city out of focus behind it.
24. *"You can tell me anything, I'm not going home"* — Mahima half-dancing in her socks, mug still in hand, laughing at somebody off frame, medium.
25. *"After hours, that's when the night gets honest"* — a low wide of the whole front room from floor level, legs, socks, the lamp, the doorway light.

### Post-chorus 1 — the chant

26. *"Four in the morning, four in the morning"* — the cooker clock in close-up (composited), 0.5 s.
27. *"Nobody's leaving without saying something"* — socks steaming on a radiator, 0.5 s.
28. *"Four in the morning, four in the morning"* — a mug passed hand to hand across frame, 0.5 s.
29. *"That's when the night gets honest"* — the front door being locked from the inside, the chain going on, close-up.

### Verse 2 — what gets said

30. *"Half four and the tunes have gone soft and gone slow"* — a hand turning a volume knob down two clicks, the room's noise dropping with it, close-up.
31. *"And my mate on the floor says a thing I didn't know"* — a young man sitting on the floor with his back against the sofa, mug in both hands, talking to the carpet, static, long take.
32. *"Says his dad's been ill since the spring and he kept it in"* — Mahima's face listening, not interrupting, not reaching out, close-up.
33. *"Says he couldn't say it sober so he says it with a grin"* — his grin arriving in the wrong place, then the whole room's faces understanding it at once, medium wide.
34. *"The girl in the doorway is handing in her notice"* — a young woman leaning in the kitchen doorframe reading off her phone (screen composited), backlit by the kitchen strip, medium.
35. *"Typing it out on her phone and reading it to all of us"* — a thumb hovering over send, then the room cheering silently, macro then wide.
36. *"I have known this lot for years and I met them all tonight"* — a slow pan of the room's faces from Mahima's eyeline, each one held for half a beat.
37. *"Everything you swallow at the bar comes up in this light"* — the single lamp in frame, everything else falling off into shadow, static, the warmest shot in the video.

### Pre-chorus 2 — the balcony door

38. *"Big light off and the balcony door"* — the balcony door pulled open, cold air visible on the smoke and steam in the room, medium.
39. *"Somebody's crying and laughing at four"* — someone laughing while wiping their eyes with a sleeve, close-up, unembarrassed.
40. *"The coats are all piled and the tea's going cold"* — a row of half-drunk mugs going cold along a windowsill, macro, the blue-grey of the window behind them.
41. *"And nobody's leaving till somebody's told"* — the pile of coats on the bed, undisturbed, seen from the doorway; nobody has touched them.

### Chorus 2 — later and closer

42. *"After hours, that's when the night gets honest"* — the same room, tighter framing, the crowd closer together, handheld.
43. *"Nobody's posing and nobody's promised"* — reuse the three-face cut from shot 19, tighter and slower.
44. *"Kettle going and the bassline low"* — the kettle again, boiled and forgotten, steam gone, macro.
45. *"Say the thing that you couldn't say downstairs, then let it go"* — the man from the floor now standing, part of the room again, medium.
46. *"After hours, when the shutters come down"* — the street below through the blind slats, empty, one taxi passing, static.
47. *"Half a flat, half a city, one sound"* — the glass of water on the radiator, now still; nobody has touched that either.
48. *"You can tell me anything, I'm not going home"* — a whole room singing at a volume that would not wake a neighbour, wide, funny and sincere.
49. *"After hours, that's when the night gets honest"* — Mahima at the window with the first grey behind her, still singing, close-up.

### Instrumental — drum edit, bassline, organ

50. Close-up two-step foot shuffle on kitchen lino, socks, cut on the off-beat snare.
51. A hand riding a fader on a laptop on the kitchen counter (screen composited), the room's volume visibly moving with it.
52. A fridge opened and closed, its light crossing a face in the dark kitchen, twice.
53. Three people crowded into a bathroom mirror laughing, the mirror doing all the work of the shot.
54. One long move down the cold hallway past coats and shoes toward the warm front-room doorway, ending framed in the light.

### MC verse — Kai walks his own party

55. *"Two flights, one lift that has not worked since I moved in"* — a lift door with a laminated notice taped to it (composited), Kai walking straight past it to the stairs, medium.
56. *"Coat on the radiator, kettle doing overtime, tune in"* — his hands spreading a wet coat over a radiator, then filling the kettle again, close-up.
57. *"I do the door, I do the drinks, I do the peace talks"* — three quick cuts on the beat: taking coats at the door; four teas made at once; his hand on two people's shoulders in a doorway.
58. *"I clock who is going to break before he even walks"* — Kai across the room watching the young man on the floor before anything is said, over-the-shoulder, quiet.
59. *"No performance in a room this small and this warm"* — a wide of the front room from Kai's position in the kitchen doorway, everyone slightly too close to everyone.
60. *"You get honest when your back is on the wall by the door"* — two people sitting on the floor with their backs against the hallway wall, mugs on the carpet, medium low.
61. *"I have heard things in this kitchen that a priest would bin"* — Kai alone in the kitchen washing one mug, the party audible off frame, static.
62. *"Grey light through the blind and I am the one who lets it in"* — his two fingers parting a blind slat, grey light landing across the carpet, close-up then the light itself.
63. *"Four in the morning is a country of its own"* — a wide of the whole flat down the hallway, every room lit differently, nobody near the front door.
64. *"Passport is a mug of tea, and nobody goes home"* — a mug pushed across the counter to somebody new, close-up on the hand-off.

### Bridge — the balcony, first light

65. *"Out on the balcony the sky's gone grey and gold"* — Mahima on a small concrete balcony with a mug, low rooftops, a grey-gold sky, wide from behind, the first natural light in the video.
66. *"Bin lorry grinding and a fox crossing the road"* — down in the street: a bin lorry working, then a fox crossing between parked cars, two shots cut as one.
67. *"Somebody's asleep in a parka in the hall"* — back inside: a sleeper sitting upright in a parka against the hallway wall, hood up, static.
68. *"Somebody's playing the first tune of them all"* — a thumb on the speaker, the same track from shot 15 starting again, then a face recognising it, close-up.
69. *"I will keep this hour longer than the club or the queue"* — Mahima's face on the balcony in first light, eyes on the rooftops, close-up, no dialogue movement.
70. *"Nothing happened here, and it's the truest thing I knew"* — a wide of the balcony from across the street: one small lit window, one figure, a whole grey city behind, static, held.

### Final chorus — daylight and the lamp still on

71. *"After hours, that's when the night gets honest"* — the blind fully open, daylight flooding a room where the lamp is still burning, wide handheld.
72. *"Nobody's posing and nobody's promised"* — dancing in flat daylight, which looks absurd and looks great, medium, three people.
73. *"Kettle going and the bassline low"* — the kettle boiling one final time, sunlight through the steam, macro.
74. *"Say the thing that you couldn't say downstairs, then let it go"* — the young man from the floor dancing badly and being cheered, medium.
75. *"After hours, when the shutters come down"* — through the window: the shopfront below, shutter still down, a delivery van pulling up, static.
76. *"Half a flat, half a city, one sound"* — the glass on the radiator trembling again in daylight, macro.
77. *"Sun on the tiles and the tunes running out"* — a rectangle of sun across kitchen lino with feet moving through it, low angle.
78. *"Nobody's sorry and nobody's proud"* — a row of faces in daylight, tired, unmade, entirely fine about it, slow pan.
79. *"You can tell me anything, I'm not going home"* — Kai ad-libbing from the kitchen doorway with the tea towel over his shoulder, medium.
80. *"After hours, that's when the night gets honest"* — the widest frame of the flat: everyone in the front room in full daylight, the lamp still on, handheld, held.

### Post-chorus 2 — daylight chant

81. *"Four in the morning, four in the morning"* — socks on lino, sunlit, 0.5 s.
82. *"Nobody's leaving without saying something"* — mugs stacked in the sink, 0.5 s.
83. *"Four in the morning, four in the morning"* — the lamp finally switched off because it is redundant, close-up on the switch.
84. *"That's when the night gets honest"* — the front door chain coming off and the door opening onto a bright landing.

### Outro — the street, morning

85. *"Bus stop, daylight, jacket in my hand"* — Mahima at a bus stop with her jacket over one arm, flat morning light, wide, the street empty.
86. *"Baker's open and the shutter's going up again"* — a bakery light on and a tray going into the window, then the same shop shutter from shot 10 rolling upward, two shots cut as one.
87. *"Somebody messages, same time next week"* — a group-chat notification on her phone (composited), her thumb not replying yet, close-up.
88. *"And I'm smiling at my phone on an empty street"* — her face, a small private smile, morning light flat and kind on it, close-up.
89. *"After hours, that's when the night gets honest"* — final shot: locked-off wide of the empty street, the shutter fully up, the flat's two windows above it with the curtains still closed, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the doorman's count, the wall switch (shot 14), each "after
hours", every chant, the volume knob (shot 30), the blind slat (shot 62),
the balcony wide (shot 70), the lamp switched off (shot 83) and the final
locked-off street. At 132 BPM a bar is 1.82 s; the two-step sections cut on
the off-grid snare rather than the downbeat, which is what makes the edit
feel like garage rather than house.

**The big-light challenge.** Shots 12–18 recut vertically are the shareable
fifteen seconds: dead stairwell, phone torches, the switch, the lamp, the
first chorus. Invite people to post their own big-light-off moment — the
second a night stops being a night out. The daylight dancing (shot 72) is
the second shareable frame.

**Caption cut:** shots 69–70 with *"Nothing happened here, and it's the
truest thing I knew."*

## 6. Quality-control checklist

- Two looks for Mahima: jacket-over-arm and shoes on outside, socks and mug from shot 14 onward; she is never shod inside the flat
- Kai picks up the tea towel at the second chorus and keeps it until shot 79
- Light runs strip light → near black → one lamp → daylight, and never goes back; no night sky after shot 65
- The lamp stays on through the whole final chorus and is only switched off at shot 83
- The glass of water on the radiator appears trembling (23), still (47) and trembling again (76) — the same glass, same frame
- The shop shutter comes down at shot 10 and goes up at shot 86, matched framing
- All screens, the cooker clock, the lift notice and the shopfront are composited; no model-generated text
- Depth used on every flat interior so the rooms stay genuinely small; no accidental open-plan apartment
- The last shot is locked-off, empty of people, and holds until the audio fades
