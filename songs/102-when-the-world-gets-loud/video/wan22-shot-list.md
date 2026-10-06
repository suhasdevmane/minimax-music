# Wan 2.2 Shot List — "When the World Gets Loud"

**One shot per lyric line**, 80 numbered entries in lyrics order, plus five unnumbered instrumental shots for the sixteen-bar piano break. Timestamps come from the rendered WAV; cut on the sung line. At 68 BPM a bar is 3.5 s, so each four-line stanza runs about 14 s and the whole song runs close to 5 minutes and 55 seconds.

## 1. Visual style

Warm domestic realism with a grey working day around it. The **day** is cold, grey and desaturated; the **home** is amber, low and close. The house is the emotional centre: the kitchen, the hallway, the window with the glass of water on the sill. Nothing is glamorous. Handheld where the day is loud, static and slow where the house is quiet, and a slow orbit reserved for the hand-spinning in the hallway.

| Section | Grade | Camera |
|---|---|---|
| Intro / dawn | Cold grey, one warm kitchen light | Static, through glass |
| Verse 1 / the day | Desaturated, cool, fluorescent | Handheld, quick cuts |
| Front door and hallway | Amber from the kitchen, cool street outside | Static wide, then slow push |
| Pre-chorus | Warm hallway, soft and gold | Slow orbit around the pair |
| Chorus (kitchen) | Low warm lamp, rest of house dim | Slow push-in, reverse on the sink |
| Verse 2 (flower) | Soft morning window light, early dawn close-up | Macro, time-lapse feel |
| Instrumental | Cold blue, one lamp | Slow, unhurried, mostly static |
| Bridge | Cold blue window light, hard shadows | Static medium, held |
| Final chorus / porch | Blue wet street, warm porch light | Wide two-shot, then close hands |
| Post-chorus | Warm amber, hallway lamp | Slow track along the hall |
| Outro | Clear early sunlight, golden and even | Slow wide, then locked close |

## 2. Character bible — paste into every prompt

**Kai** (the father, one look throughout; his grey work coat comes off in the hallway and does not come back on)
> Same male character Kai, man in his late thirties, short dark hair, warm tired face with laughter lines, plain grey work coat over a dark shirt, slightly rumpled, expression worn but kind, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (indoors, coat off)
> Same male character Kai, man in his late thirties, short dark hair, warm tired face with laughter lines, dark shirt with sleeves pushed up, no coat, relaxed shoulders, expression soft and present, realistic cinematic photography, consistent identity, natural skin texture

**Ellie** (the daughter, about four; yellow cardigan in every shot)
> Same young girl Ellie, about four years old, wavy dark hair falling past her shoulders, bright brown eyes, round soft face, wearing a yellow cardigan over a white top, open and playful expression, realistic cinematic photography, consistent identity, natural skin texture

**The flower** — a single stem in a clear glass of water, bent and torn at first, then upright and fresh. Keep the same glass, the same window sill and the same stem in every flower shot.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, notifications, radio displays and any on-screen clock or message are composited in the edit.** Generate phones as lit blank screens and overlay any UI in post. The phone on the counter is face down in most shots and is never the focus.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate. Lock Kai and Ellie with IP-Adapter or a character LoRA each, one reference per look. Keyframes first; OpenPose for the hallway walk and the dance in the kitchen; Depth for the interiors. 16:9 throughout, since this is a family film, not a phone-POV edit. Animate conservatively: a kettle steaming, a flower in a glass turning towards the light, breathing, a coat being hung.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — dawn, one chord

1. *"Some days start with thunder"* — Kai (coat on) at the kitchen window at grey dawn, phone face down on the counter behind him, rain on the glass, static medium close-up, cold light.
2. *"Before the sun is high,"* — the window glass, rain streaking, Kai's reflection faint in it, his hand flattening on the sill, close-up, cold grey.
3. *"A hundred voices asking"* — the phone face down on the counter, a faint glow leaking from under it, a mug going cold beside it, static, slow.
4. *"And no good way to reply."* — Kai picking up his bag and pausing, not looking at the phone, one warm kitchen light switching on behind him, medium wide.

### Verse 1 — the day, then the front door

5. *"The phone goes off at seven with a problem I can't name,"* — a fluorescent office corridor, Kai walking fast with the phone at his ear, handheld, desaturated.
6. *"The traffic sits and doesn't move and then it moves again."* — a car interior at a jam, Kai's hands on the wheel, the windscreen full of red brake lights, slow handheld.
7. *"There's a man who wants an answer and a number that won't close,"* — a laptop on a desk, a spreadsheet of red figures, Kai rubbing his eyes, over-the-shoulder, cold light.
8. *"And a meeting in an hour where I'll say that it's all fine."* — a conference room, Kai smiling a practiced smile at people off-frame, the smile not reaching his eyes, medium close-up.
9. *"I keep a face for all of it, I've worn it till it fits,"* — Kai in the car park, alone, dropping the smile in the car mirror, then putting it back on, tight close-up.
10. *"I can carry a whole bad week and never let it slip."* — Kai carrying a briefcase across a wet car park, shoulders braced against the wind, wide and handheld.
11. *"Then I come in through the front door, drop my bag against the wall,"* — the front door opening onto the dark hallway, Kai stepping in, dropping the bag, the street light behind him, static wide.
12. *"And there's music in the kitchen and you dancing in the hall."* — Ellie barefoot in the yellow cardigan in the kitchen doorway, dancing to a radio on the counter, amber light spilling down the hall.
13. *"You don't stop to look at me, you're too far into the song,"* — Ellie dancing with her eyes shut, not looking up, the radio's glow on her face, medium shot, warm.
14. *"You just reach out for my hand and pull me where you are."* — Ellie's small hand reaching back toward Kai in the hall, his hand taking it, the grey coat half off his arm, close on the two hands.

### Pre-chorus 1 — the thread

15. *"You don't ask me how it went,"* — Ellie in the hallway, holding Kai's hand and looking up at him with no question on her face, medium two-shot, warm.
16. *"You don't need the whole report,"* — the grey coat dropped on the hall chair, Ellie's cardigan sleeve swinging into frame, close on her hands, amber light.
17. *"You just take my hand and spin me"* — the slow orbit begins around the pair in the hallway, Kai's coat over his arm, the kitchen blurred gold behind.
18. *"Till I've lost the thread of it."* — Kai's face mid-turn, eyes half closed, a breath going out of him, the shoulders dropping an inch, close-up.

### Chorus 1 — the quiet I come back to

19. *"When the world gets loud,"* — Kai leaning in the kitchen doorway, arms folded, Ellie at the sink on a step stool, slow push-in on Kai's face, warm low light.
20. *"You're the quiet I come back to."* — reverse on Ellie at the sink, rinsing a cup under the running tap, her humming, the radio turned low.
21. *"When I can't hear myself,"* — Kai's face in the doorway, the sound of the room going soft around him, a slight soft-focus pull, close-up.
22. *"I just stand here and I watch you."* — Ellie turning round with the cup, a wet smile for him, the kitchen light on her cardigan, medium shot.
23. *"You don't fix a single thing,"* — the counter, untouched: bills in a pile, a half-eaten sandwich, Ellie's crayon drawing on the fridge, static wide, no one fixing anything.
24. *"You don't know there's any weight,"* — Ellie climbing onto the step stool to reach a high cupboard, her face pure concentration, low angle, warm light.
25. *"You just put your hand in mine"* — their hands joined over the counter, the cup between them, close on the two hands, warm.
26. *"And the shouting goes away."* — the kitchen held still, the radio's music softening, the window dark behind them, a long static hold on the pair, low lamp.

### Verse 2 — the flower in the glass

27. *"You brought a flower in to me from somewhere near the fence,"* — Ellie at the back door holding up a bent flower from the garden fence, petals torn, Kai in the kitchen light, medium two-shot.
28. *"The stem was bent, the petals torn, it didn't make much sense."* — macro on the broken stem and torn petals in Ellie's small fist, soft daylight, shallow focus.
29. *"You said that it was only tired and wanted somewhere small,"* — Ellie speaking to the flower, face very serious, the sill of the window in soft focus behind her, medium close-up.
30. *"So we filled a glass with water and we set it by the wall."* — Kai pouring water into a clear glass at the counter, Ellie holding the flower steady, the glass set on the sill, hands in frame, warm.
31. *"You checked on it at bedtime and you checked on it at dawn,"* — night, a single lamp in the kitchen, Ellie in her pyjamas tilting her head at the glass, a dawn cut to the same window, time-lapse feel.
32. *"You turned it to the window so it knew which way was warm."* — Ellie's small hands turning the glass a quarter turn toward the window light, close on her hands and the glass, morning sun.
33. *"By Thursday it was standing and you never said a thing,"* — the stem upright in the glass on the sill, petals open, wide static shot of the window, golden light, no one in frame.
34. *"You just carried on with breakfast like it's normal to be mending."* — Kai at the table over cereal and toast, Ellie not looking up, the glass visible on the sill behind them, medium two-shot, warm morning.
35. *"I have spent my whole life hammering at problems till they break,"* — Kai alone in the car at a red light, hands tight on the wheel, the windscreen grey, cold light, medium close-up.
36. *"And you fixed a broken flower with a glass and three days' faith."* — the flower in the glass, petals standing, Kai's reflection faint in the window beside it, close-up on the glass, morning light.

### Pre-chorus 2 — the thread, again

37. *"You don't ask me how it went,"* — the hallway again, evening: Ellie looking up at Kai with an easy grin, no question, medium, warm.
38. *"You don't need the whole report,"* — reuse shot 16, tighter, the grey coat on the chair, cardigan sleeve, deeper gold light.
39. *"You just take my hand and spin me"* — reuse shot 17 with the flower glass visible on the sill in the background of the orbit.
40. *"Till I've lost the thread of it."* — Kai laughing quietly with his eyes closed, the window behind them a deep blue dusk, close-up, warm.

### Chorus 2 — the quiet, again

41. *"When the world gets loud,"* — living room, Ellie building a small tower of blocks on the rug, Kai on the sofa with his eyes half closed, wide static shot.
42. *"You're the quiet I come back to."* — reverse from the sofa: Ellie in the foreground, Kai soft in the background, the flower glass on the low table between them.
43. *"When I can't hear myself,"* — Kai's face, eyes opening slowly, the room's sounds softening, a soft-focus pull, close-up.
44. *"I just stand here and I watch you."* — Ellie stacking the last block on the tower, looking across at him with delight, medium close-up, lamp light.
45. *"You don't fix a single thing,"* — the blocks falling over in a small crash, Ellie giggling, Kai not moving to fix it, static wide.
46. *"You don't know there's any weight,"* — Ellie climbing up onto the sofa beside him, her small weight against his arm, low angle, warm lamp.
47. *"You just put your hand in mine"* — Ellie reaching up, her small hand finding his, his hand closing around it, close on the two hands on the cushion.
48. *"And the shouting goes away."* — the room quiet, the window dark, the two of them still, a long static hold, lamp light, the tower on the rug.

### Instrumental — sixteen bars, piano and strings

- Kai in the kitchen at night, standing at the sink with both hands on the edge, head down, the tap dripping, a single cold blue light, close and still.
- The hallway at night, the front door shut and bolted, Kai's grey coat on its hook, the light from the lamp falling across the floorboards, slow dolly down the hall.
- Ellie asleep in her small bed, the yellow cardigan folded on the chair, the flower glass on the windowsill, moonlight, wide and very quiet.
- Kai sitting on the edge of the bath with a towel over his shoulder, drying his face slowly, cool blue light from the frosted window, close.
- A slow pull back from the kitchen window at night, the street light outside and the glass with the flower reflected faintly in it, the house dark except one lamp.

### Bridge — the men who never learned to care

49. *"I don't know how to tell you"* — Kai in the doorway of Ellie's room in the dark, his mouth just opening on a word he does not finish, static medium, cold window light.
50. *"That the thing you do is rare,"* — Ellie asleep under her blanket, the flower glass on the sill in the window light, slow tilt from the sill to her face.
51. *"That there are grown men twice your size"* — a wide shot of a hallway with an older man in a suit walking past a closed door, out of focus, the hallway cold and empty, static.
52. *"Who have never learned to care"* — a loose montage of hard shadows: a laptop screen dark on a desk, a closed car door, Kai's own face in a dark window, cold light, quick.
53. *"The way you cared about a flower"* — macro on the glass of water on the sill, the stem standing up, Kai's fingers touching the glass rim, soft focus.
54. *"With a stem that wouldn't hold."* — Ellie's hand curling round the glass in the dark, the flower steady, close on her small fingers, cold blue light.
55. *"So if anybody ever says"* — Kai standing up slowly from the bed edge, hand on the wall, looking back at Ellie, a long breath, medium, cold.
56. *"Your softness makes you small,"* — Kai's face in the window glass, eyes wet but steady, the reflection of the street below, close-up, one hard shadow.
57. *"They have never been the broken thing"* — the hallway, Kai walking towards the kitchen, past the flower glass, hard shadows across the walls, static wide.
58. *"You carried down the hall."* — Ellie's small silhouette at the top of the stairs with the flower glass in both hands, carefully carrying it down, cold light, two-shot.
59. *"They have never been the tired man"* — Kai at the kitchen table, head in his hands, the phone face down beside him, a single lamp, close and still.
60. *"You turned towards the sun."* — Kai lifting his head as Ellie sets the glass down in front of him on the table, turning it toward the warm window light, close on the glass and his face, the first warm frame of the bridge.

### Chorus 3 — the shelter, lifted

61. *"When the world gets loud,"* — the front step of the house in soft rain, Kai under the porch light with an umbrella, wide two-shot from across the path.
62. *"You're the quiet I come back to."* — Ellie beside him holding the glass with the flower in both hands, carefully, rain falling into the porch light, medium two-shot.
63. *"When I can't hear myself,"* — close on Kai's face under the umbrella, the rain falling past him, the sound of the street softened, shallow focus.
64. *"I just stand here and I watch you."* — Ellie laughing up at him through the rain, the yellow cardigan bright against the blue wet street, medium close.
65. *"I came here to be the shelter,"* — Kai holding the umbrella steady over Ellie's head, his shoulder getting soaked, wide static under the porch light.
66. *"To stand between you and the rain,"* — the umbrella held over the glass in Ellie's hands, rain beading on the umbrella's edge, close on the glass and her fingers.
67. *"And you've been the one who's quietly"* — Kai lowering the umbrella and letting the rain fall on his shoulders, Ellie laughing at him, medium, porch light.
68. *"Been taking it away."* — Ellie holding the umbrella up for him now, on tiptoe, the rain still falling, a wide shot of the two of them under the one small umbrella, warm porch light, the street blue.

### Post-chorus — the glass by the window

69. *"The world can keep on shouting,"* — the grey coat hung on the hook by the front door, the door swinging shut on the rain, the street sound cut off, static close on the coat.
70. *"The night can rise and fall,"* — the hallway at night, Ellie spinning in the middle of the frame in the yellow cardigan, arms out, slow tracking shot from the front door.
71. *"There's a glass beside the window"* — the kitchen window, the glass with the flower on the sill in warm lamp light, a slow rack focus from the glass to Ellie's spinning shape behind it.
72. *"And you dancing in the hall."* — Kai leaning on the hallway doorframe, smiling properly for the first time in the film, Ellie dancing past him, medium, warm amber.

### Outro — the flower standing up

73. *"So let it all get louder,"* — the kitchen at sunrise, the phone face down on the counter buzzing and then falling still, Kai and Ellie at the sink, wide static, golden light.
74. *"Let the thunder do its worst."* — a window with rain outside, the sky grey and then breaking, the glass on the sill catching the first light, close.
75. *"There's a flower on the windowsill"* — macro on the glass, the stem upright, the petals open and bright, the light moving across the water, very slow push.
76. *"And it is standing up."* — Ellie's finger touching a petal gently, Kai's hand resting on her head, close on the two hands and the flower, warm.
77. *"So let the phone keep ringing,"* — the phone on the counter lighting up with a call (composited), Kai and Ellie not turning to look, their backs to camera at the sink, static.
78. *"Let the traffic have its say,"* — a window view of a traffic queue in the sun, far away, muffled, the house kitchen in soft focus in the foreground.
79. *"I've got a little hand to hold"* — Kai's hand around Ellie's small hand on the glass, his grey coat on the back of a chair, close on the two hands.
80. *"And a whole hall left to play."* — Ellie running down the hallway into the sunlight at the front door, the flower glass safe on the sill behind her, the frame held on the open doorway; the piano decays into room tone under the last held shot. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the first "when the world gets loud", the pre-chorus hallway spin, "the flower in the glass" at the start of verse 2, the instrumental, "the way you cared about a flower", the porch umbrella line "to stand between you and the rain", "and it is standing up", and the final "play". At 68 BPM a bar is 3.5 s, so the instrumental's sixteen bars cover about 56 s of the edit.

**Shareable cut.** Cut chorus 1 (shots 19–26) as a 9:16 clip with the lines "when the world gets loud, you're the quiet I come back to" on screen, and the hallway spin (shots 15–18) as a second cut. The two together show the whole idea in under thirty seconds.

**Challenge.** Ask viewers to film their own come-home moment with no words: one minute, a hand, the door, the thing they do first when they get in. The prompt on screen is "you don't ask me how it went."

## 6. Quality-control checklist

- Kai's grey work coat is on in the intro and the first verse, off from the hallway spin onward, and is never back on for the rest of the song
- Ellie's yellow cardigan is in every Ellie shot; no other colour of cardigan appears
- The flower in the clear glass is the same glass and the same stem throughout, bent in shots 27–29, upright from shot 33 and in every frame after it
- The sill and the window are the same set in every flower shot, so the stem's change reads as one plant, not three
- No one in the film has a visible phone screen; all UI, call screens and the radio display are composited in the edit
- The day scenes are cold and desaturated, the home scenes warm; the bridge's cold blue is the one place the home goes cold on purpose
- Hands and small fingers are clean in every close-up, especially the flower and the two-hand shots (shots 25, 47, 76, 79)
- The last shot holds on the open doorway until the piano decays to room tone, and nothing is added to it
