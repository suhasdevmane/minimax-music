# Wan 2.2 Shot List — "Bad Idea, Good Night"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. This is a fast one: at 150 BPM a bar is 1.6 s, so most shots
are 2–3 s and the choruses cut on every bar. Take timestamps from the
rendered WAV; cut on the sung line.

## 1. Visual style

One night, start to finish, shot like a friend's phone that happens to be
very good. **The red light is the motif** — every chorus ends on a traffic
light, red, and them running it. Three places: the **skate park** (cold
floodlights, warm faces), the **basement gig** (one red bulb, phone
torches, sweat) and the **scooter** (sodium streaks, the amber roundabout).
The ending is the only still, gold frame in the video. Handheld, fast,
chaotic, fun; nothing is composed except the red lights and the last shot.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm bedroom lamp, cool phone glow | Static close-ups |
| Verse 1 | Blue dusk, one sodium light warming up | Handheld, on the beat |
| Pre-choruses | Harsh white car-park floodlight | Quick cuts |
| Choruses | Neon and sodium streaks, saturated red | Scooter-mounted, whip pans |
| Verse 2 | Skate park cold floodlights; basement one red bulb | Handheld, in the pit |
| Instrumental | Streaks, then black | Fast, then a hard stop |
| Bridge | Amber blink, a passing blue, otherwise dark | Slow, circling |
| Final chorus / post-chorus | Most saturated frames, first grey of dawn | Fastest cuts |
| Outro | Clean gold sunrise | Locked-off, still |

## 2. Character bible — paste into every prompt

**Mahima** (night-out look, intro through chorus 1)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a few strands tucked behind one ear, smudged black eyeliner, wearing a cropped black band t-shirt, baggy dark cargo jeans and scuffed white sneakers, grinning mischievous expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (skate park and basement, verse 2 through final chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and wind-tangled, smudged black eyeliner, wearing a grey oversized zip hoodie open over a cropped black band t-shirt and baggy dark cargo jeans, a scraped knee visible through a rip, a marker scrawl on her forearm, laughing exhilarated expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (sunrise, post-chorus and outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and messy, eyeliner smudged from the night, wearing a man's oversized faded denim jacket with patches over the cropped black band t-shirt, blue-stained tongue and lips from a slushie, tired happy expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the bad idea)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, a small pale scar cutting through his left eyebrow, chipped black nail polish, wearing a faded denim jacket with patches over a white t-shirt and black jeans, a worn skateboard under one arm, easy crooked grin, realistic cinematic photography, consistent identity

Kai's **scooter** is a battered small-engine scooter with one cracked,
flickering headlight. His **board** has trucks visibly worn thin. From the
post-chorus on his **denim jacket** is on Mahima.

**The friends, the sister, the group chat** — only ever on a phone screen,
never in the real world. The **one-star girls** in the car park are
faceless: backs turned, or cropped at the shoulder.
> a young woman with her back to camera in a car park, dark jacket, face never visible

**The basement band** — four musicians, faces in shadow or turned away,
lit by one red bulb.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the group chat, the poll, the spreadsheet, the
notifications and the star ratings are composited in the edit.** Generate
the phone as a lit blank screen and overlay the UI in post — the model
cannot render legible UI. The marker on their forearms is an abstract
scrawl, never a readable word.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless. Keyframes first; OpenPose for the dance
and the running shot; Depth for the bedroom compositions. 16:9 first; 9:16 for
the phone-POV cuts, which are natural vertical content. Animate
conservatively: thumb scrolling, screen light flicker, breathing, a hoodie
being pulled on.

For this song specifically: OpenPose on the drop-in, the fall and every pit
shot; a plate of the empty skate park and the empty roundabout for the
scooter passes, then animate 2 s bursts of motion; the red-light shots are
locked-off stills with only the light and the exhaust animated.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–3 s.

## 4. Scene per lyric line

### Intro — the vote

1. *"My best friend texted, do not do it"* — Mahima (night-out look) at her dresser mirror doing eyeliner, a phone propped against the mirror lighting up (message composited), close-up on her reflection, warm lamp.
2. *"My sister sent a warning too"* — the phone screen filling the frame, a second message landing (composited), her eyes flicking to it in the mirror, still grinning.
3. *"The group chat voted, seven to nothing"* — extreme close-up of a poll result bar on the phone (composited), her thumb scrolling the pile-on, a laugh escaping.
4. *"Every single one of them said you"* — her tossing the phone onto the bed behind her and finishing the last flick of eyeliner, a look to camera in the mirror.

### Verse 1 — the inventory

5. *"You got a scar above your eyebrow and a story to go with it"* — blue dusk street corner, Kai leaning on a wall with his board under one foot, extreme close-up of the pale scar through his eyebrow as he turns, sodium light warming up.
6. *"Chipped black polish and a board with the trucks worn thin"* — his chipped black nails tapping the board's edge, then the worn trucks, macro, on the beat.
7. *"You said, I know what they say, and I said, yeah, so do I"* — Mahima arriving, the two of them a metre apart, both talking, both shrugging, medium two-shot handheld.
8. *"Then you held out your hand and I said, let's begin"* — his hand held out, hers taking it, a shrug to camera from her, close-up on the hands then her face.
9. *"You showed up on a scooter with a cracked headlight"* — the battered scooter at the kerb, one headlight cracked and flickering, low angle, Kai swinging onto it.
10. *"Said, hop on, and I looked at the sky like, really?"* — Mahima looking straight up at the sky, exasperated and amused, then swinging a leg over the seat, medium.
11. *"Everyone I love has got a spreadsheet of your damage"* — a fast flash of a phone showing rows and a red column (composited, no readable text), then her face over it, deadpan.
12. *"And I'm about to put my name on it, honestly"* — her thumb tapping the screen once, decisive, then pocketing the phone and wrapping her arms round his jacket.
13. *"Your jacket smells like a gas station slushie"* — the scooter moving, her face pressed to his denim shoulder, nose wrinkling then smiling, close-up, passing streetlights.
14. *"Your playlist is loud and it's ninety percent screaming"* — a tinny speaker in his jacket pocket, her wincing and laughing, a whip pan to the road ahead.
15. *"You laugh at your own jokes before you finish them"* — Kai half-turning to shout a joke and cracking up before the end, her not hearing a word, close-up from her side.
16. *"And somehow every red flag has me leaning in"* — her leaning further in, chin on his shoulder, the streetlights strobing across both faces, tracking alongside.

### Pre-chorus 1 — the reviews

17. *"Yeah I read the reviews, one star, one star"* — a car park behind a strip of shops under harsh white floodlight, three faceless girls with their backs turned, one raised finger each (a single star composited over each), quick cuts.
18. *"Every girl you dated left a warning in the parking lot"* — Mahima walking straight past the turned backs toward the scooter, long shadows, tracking from the front.
19. *"I know exactly what this is"* — her stopping and looking at camera, a knowing raised eyebrow, close-up, floodlight.
20. *"And I'm doing it anyway, ready or not"* — her breaking into a run for the scooter, the stutter build, handheld chasing her.

### Chorus 1 — red light

21. *"You're a bad idea, but a good night"* — the scooter tearing through the city at night, Mahima on the back with both arms out, screaming the hook into the wind, scooter-mounted camera, neon streaks.
22. *"Wrong on paper, but the timing's right"* — a crumpled sheet of paper flying out of her hand and tumbling behind them on the road, slow motion, sodium light.
23. *"I'll regret you in the morning, that's the deal"* — her face over his shoulder, hair everywhere, mouthing the line at camera, close-up on the move.
24. *"But tonight I'm gonna feel what I feel"* — a whip pan from her face to the road ahead, lights smearing, then back.
25. *"Whoa oh, tell my friends I'm sorry"* — punch-in on her mouth wide open on the shout, then a phone in her pocket lighting up, ignored.
26. *"Whoa oh, tell my mum don't worry"* — punch-in on Kai's grin over his shoulder shouting the answer, then both of them.
27. *"You're a bad idea, but a good night"* — the scooter slowing to an empty junction, a traffic light overhead turning red, both of them lit red, locked-off.
28. *"And the best ones always start with a red light"* — a beat of stillness under the red, a look between them, then the scooter launching through the red light and out of frame.

### Verse 2 — skate park, basement, chips

29. *"Skate park after dark, you're teaching me to drop in"* — an empty concrete skate park under cold floodlights, Mahima (hoodie look) at the lip of a small ramp on his board, terrified and laughing, Kai below with his arms up, wide.
30. *"I'm screaming on the ramp and you're screaming louder"* — her dropping in and wobbling down the ramp screaming, Kai screaming louder beside her, handheld tracking.
31. *"Concrete kissed my knee, you kissed it better"* — the fall, then the scraped knee through the rip in her cargos, then Kai crouching and kissing the graze theatrically, close-up.
32. *"Then you laughed and said, I told you I was trouble"* — Kai laughing up at her from the crouch, her shoving his shoulder, both on the concrete, warm faces under cold light.
33. *"Basement gig at midnight, your friend's band is terrible"* — a packed low-ceilinged basement lit by one red bulb, a four-piece band in shadow playing badly, phone torches up, wide from the back.
34. *"The ceiling's dripping and the amp keeps cutting out"* — a drip falling from the ceiling in slow motion, then the amp cutting out mid-riff and the crowd cheering anyway, quick cuts.
35. *"You pulled me in the pit and held onto my hoodie"* — Kai dragging Mahima into the pit by the hoodie sleeve and keeping a fist in the back of it as bodies crash around them, handheld inside the pit.
36. *"And I sang words I didn't know at the top of my mouth"* — her eyes shut, shouting lyrics she doesn't know, sweat shining, red bulb, close-up.
37. *"Chips from the van with your last four coins"* — outside, a chip van's fluorescent strip, four coins counted one by one onto the counter, macro, breath in the cold.
38. *"You said, I'm broke, I said, I noticed, I don't care"* — one paper cone of chips shared between them on a wall, her stealing the last one, medium two-shot.
39. *"Your friend's band's name in marker on my forearm"* — an abstract marker scrawl on her forearm (no readable text), her holding it up to the van light, close-up.
40. *"Your number on yours, and half of it isn't there"* — a half-rubbed-off scrawl on his forearm held next to hers, both laughing at it, close-up on the two arms.

### Pre-chorus 2 — the way you laugh

41. *"Yeah I read the reviews, one star, one star"* — the one-star fingers from shot 17 in three quick flashes, harsher and faster.
42. *"But the reviews never mentioned the way you laugh"* — Kai laughing unguarded on the wall, head thrown back, chips in hand, close-up, then Mahima watching him.
43. *"I know exactly what this is"* — her looking from him to camera, the knowing eyebrow again, softer this time.
44. *"And I'm doing it anyway, don't do the math"* — her shaking her head at an imaginary sum and pulling him up off the wall toward the scooter.

### Chorus 2 — the night in motion

45. *"You're a bad idea, but a good night"* — the board sliding across the skate park concrete on the downbeat, then the pit jumping, two shots cut on the bar.
46. *"Wrong on paper, but the timing's right"* — reuse shot 22, the paper tumbling, tighter.
47. *"I'll regret you in the morning, that's the deal"* — Mahima at the top of the ramp again, this time pushing off without hesitating, wide.
48. *"But tonight I'm gonna feel what I feel"* — her landing the drop-in and rolling out with both fists up, Kai chasing her across the park, tracking.
49. *"Whoa oh, tell my friends I'm sorry"* — the whole basement crowd's hands up on the shout, phone torches swinging, wide from the stage.
50. *"Whoa oh, tell my mum don't worry"* — Mahima on Kai's shoulders in the pit for one bar, arms up, red bulb, low angle.
51. *"You're a bad idea, but a good night"* — another empty junction, another red light, the scooter idling under it, both lit red, locked-off.
52. *"And the best ones always start with a red light"* — the launch through the red, the camera left behind under the light as they shrink down the road.

### Instrumental — full speed, then the stop

53. The scooter flying down an empty dual carriageway, sodium lights smearing into lines, scooter-mounted camera looking back at Mahima's face, lead guitar melody.
54. The basement crowd clapping in unison on the drum breakdown, phone torches on the beat, wide, red bulb.
55. The crowd whoa oh: the whole basement with hands and torches up, Mahima and Kai in the middle looking at each other, slow motion.
56. Kai kick-flipping the board under the skate park floodlights, slow motion, the wheels catching the light.
57. The sudden stop: a black frame, then the two of them frozen at a red light, engine idling, silence, the cut into the bridge.

### Bridge — the roundabout at two

58. *"Two on a scooter, no helmets, sorry mother"* — an empty roundabout at two in the morning, the lights switched to blinking amber, the scooter circling it slowly, wide from the centre island.
59. *"Doing thirty through the roundabout at two"* — the scooter going round a second time for no reason, Mahima's chin on Kai's shoulder, a mock-apologetic look to camera, tracking.
60. *"The streetlights blinking orange like they're judging us"* — the amber lights blinking over both of them, low angle looking up as they pass under.
61. *"And I'm holding on and laughing, and so are you"* — both laughing, her arms tight round him, his hand briefly over hers on his jacket, close-up on the hands.
62. *"Maybe you'll ghost me by Thursday"* — her eyes closed, hair whipping, the amber blink on her face, extreme close-up.
63. *"Maybe you'll forget my name"* — a distant siren passing on the ring road, blue light flickering on the underpass wall behind the roundabout, wide.
64. *"But I'll have this, the wind and the sirens"* — her opening her eyes and smiling anyway, the blue fading, amber returning, close-up.
65. *"And the night I said yes to the flame"* — the cracked headlight flickering against the dark road ahead, macro, then her face lit by it.
66. *"They'll say, you should've known better, and I did"* — Mahima mouthing I know at camera over his shoulder, deadpan, the toms building.
67. *"I knew better and I did it anyway"* — Kai turning back with the scar and the grin, the scooter leaving the roundabout onto the exit.
68. *"Better never made me laugh until I couldn't breathe"* — her laughing so hard she has to hide her face in his jacket, the guitars roaring back, tracking.
69. *"Better never had a scar and a story to say"* — the scooter accelerating down the exit under the sodium lights picking up speed, camera falling behind.

### Final chorus — every red light

70. *"You're a bad idea, but a good night"* — every red light of the night cut on the beat, four junctions, four reds, four launches.
71. *"Wrong on paper, but the timing's right"* — the paper from shot 22 landing in a gutter, then a kid's foot kicking it, dawn grey beginning.
72. *"I'll regret you in the morning, if I do"* — Mahima on the ramp landing it clean and rolling to Kai, taking a bow, wide.
73. *"But right now the only plan I've got is you"* — her hand tightening on the front of his denim jacket, pulling him in, close-up.
74. *"Whoa oh, tell my friends I'm sorry"* — the basement crowd's hands up again, then Mahima's own hands up on the back of the scooter.
75. *"Whoa oh, tell my mum don't worry"* — her and Kai shouting the line at each other nose to nose in the car park, laughing.
76. *"You're a bad idea, but a good night"* — the last red light, the sky behind it going from black to grey, both lit red, locked-off, the longest hold.
77. *"And the best ones always start with a red light"* — the launch, the camera staying, the red light turning green a second too late.

### Post-chorus — seven to nothing

78. *"Bad idea, bad idea, good night"* — the phone on the scooter seat, a wall of unread messages (composited), the first grey light on the screen.
79. *"Bad idea, bad idea, good night"* — her flipping the phone face-down on the seat, close-up on the hand.
80. *"Seven to nothing, they were right"* — the poll result on the phone in a flash (composited), then her shrug to camera, conceding.
81. *"Bad idea, but a good night"* — her and Kai shouting the chant at each other on the forecourt, nose to nose, then breaking into laughter, medium.

### Outro — gas station curb

82. *"Sun's coming up on a gas station curb"* — a gas station forecourt at sunrise, Mahima (sunrise look, his denim jacket) and Kai sitting on the kerb, small in a wide frame, gold light.
83. *"Slushie for breakfast, blue tongue, no sleep"* — a blue slushie shared with two straws, her sticking out a blue tongue at him, close-up.
84. *"Your board under my feet, your jacket on my shoulders"* — his board under her sneakers rolling an inch back and forth, the patched denim jacket on her shoulders, medium.
85. *"Forty messages waiting and I'm not gonna read"* — the phone lit with a stack of notifications (composited) placed screen-down on the concrete, close-up on the hand.
86. *"You said, so was it worth it, and I said, ask me tomorrow"* — Kai asking, her tired shrug and smile, medium two-shot, the sun clearing the forecourt roof.
87. *"Then I kissed you like a secret I don't plan to keep"* — final shot: the kiss on the kerb, the board rolling away a foot on its own, the sun full on the forecourt, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the count-in, the first band hit, every red light, each "whoa
oh", the drum breakdown, the full stop, "I knew better and I did it
anyway", the post-chorus chant, and the last kiss. At 150 BPM a bar is
1.6 s; choruses cut every bar, the red-light holds are the only shots
longer than two bars.

**The seven-to-nothing challenge.** The hook is caption-ready. Post the
vertical cut of chorus 1 (shots 21–28) with *"you're a bad idea, but a good
night"* on screen and invite people to post the group-chat vote their
friends held about someone, then the night they had anyway. The blue-tongue
kiss (shot 87) is the second shareable frame.

## 6. Quality-control checklist

- Three looks in the right sections: band tee through chorus 1, grey hoodie with the scraped knee and marker scrawl from shot 29, his denim jacket on her from shot 78 on and never before
- Kai's scar through the left eyebrow and chipped black polish visible in every close-up; the same scooter and board throughout
- The friends, the sister and the group chat exist only on a screen; the one-star girls never show a face
- Every chorus ends on a red light and them running it; the final one (shot 76) holds longest and the sky is grey behind it
- All UI composited; the marker scrawls are abstract, never words
- OpenPose on the drop-in, the fall and every pit shot; no invented anatomy on the scooter two-up
- Everything before the outro is handheld and moving; the outro is the only locked-off gold frame
- The last shot holds until the audio fades, no text
