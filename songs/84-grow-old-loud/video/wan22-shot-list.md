# Wan 2.2 Shot List — "Grow Old Loud"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
118 BPM a bar is 2.03 s, so choruses cut every bar and the post-chorus chant
cuts on the half-bar.

## 1. Visual style

One kitchen, sixty years. The film ages two people forward through makeup,
costume and grade while the room stays recognisably the same — the doorway
never moves, the practical over the sink is in shot one and shot seventy-nine.
Three worlds share the frame: the **real timeline**, warm, messy and
over-lit; the **ghost timeline** in verse one, a flat shadowless catalogue
photograph of the careful life they refuse; and the **decades**, each graded
to its own era.

Two rules. The camera never gets more polite as the couple get older — the
handheld gets *worse*. And the ghost timeline is the only place in the film
with no practical light source visible in frame.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm overheads, hard practical over the sink | Handheld, close, one to lens |
| Verse 1 (ghost timeline) | Flat, shadowless, desaturated | Locked-off, symmetrical, still |
| Pre-choruses | One porch light, one street lamp, headlights | Two-shot, static, then handheld |
| Choruses | Warm, bright, saturated, practicals everywhere | Wide handheld, fast |
| Post-choruses | Day, dusk, night across matched car cuts | Locked-off, identical framing |
| Verse 2 | Kitchen daylight, concert lighting, road daylight | Handheld, warm |
| Instrumental | Tungsten, eighties fluorescent, nineties daylight, modern LED | One fixed doorway frame |
| Bridge | One lamp, deep shadow, least saturated in the film | Static, quiet |
| Final chorus | Ugly house lights up full | Wide, unglamorous |
| Outro | Warm, single overhead, the sink practical | Locked-off, held |

## 2. Character bible — paste into every prompt

**Mahima** (early twenties, the real timeline)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly messy, light natural makeup, wearing a red slip dress under an oversized denim jacket, delighted unrepentant expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the ghost timeline, forties)
> Same female protagonist Mahima, woman in her forties, expressive dark eyes, oval face, dark wavy hair cut to a neat shoulder-length bob, minimal makeup, wearing a beige knit cardigan over a plain blouse, polite closed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (seventies and eighties, the real timeline)
> Same female protagonist Mahima, woman in her late seventies, the same expressive dark eyes and oval face now deeply lined, thick silver-grey hair worn loose to the shoulder, bright red lipstick, wearing a loud patterned jacket over a plain tee, wide open laughing expression, realistic cinematic photography, consistent identity, natural aged skin texture

**Kai** (early twenties)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a plain white t-shirt and dark jeans, grinning expression, realistic cinematic photography, consistent identity

**Kai** (ghost timeline, and again at eighty)
> Same male character Kai, in the ghost timeline a man in his forties with the same close-cropped hair going grey and a neat trimmed beard, wearing a beige zip fleece and chinos, mild neutral expression; in the real timeline at eighty the same face heavily lined with full white hair and beard, wearing a loud patterned jacket matching hers, delighted expression, realistic cinematic photography, consistent identity, natural aged skin texture

**The grandmother** — the only other named presence, seen twice: in the intro
doorway and alone in the outro flashback. Late eighties, cardigan, hand up,
mock-stern, and then dancing on her own.

Everyone else is family and party population — three generations at the
gathering, grandchildren with phones, an aunt laughing, wedding staff stacking
chairs, a band packing up. Keep them in motion or in profile; none needs a
locked identity. There are no exes and no rivals in this video.

Objects that repeat: the **framed picture** that walks itself off the nail,
the **volume dial**, the **thermostat**, the **matching loud jackets**, the
**car with the windows down**, the **bench with the plaque**, the **practical
light over the sink**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the wall calendar, the bench plaque, the speaker-box sticker,
the thermostat display and any signage are composited in the edit.** Generate
them as blank surfaces and drop the content in afterwards — the model cannot
render legible text, and the bench plaque is a punchline that has to be
readable.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
This video needs **five locked identities, not two**: Mahima at twenty-two, at
forty in the ghost timeline and at seventy-plus, and Kai at twenty-two and at
eighty. Build a separate IP-Adapter or LoRA reference set for each age — do
not try to age a young reference with a prompt, it will drift between shots
and the whole conceit collapses. Shoot the reference stills for each age in
the same doorway and the same three-quarter angle so the match cuts land.

Keyframes first; OpenPose is essential for every dance shot, especially the
older couple, where the model will otherwise invent joints. Depth for the
fixed kitchen doorway frame that carries the instrumental. 16:9 first; 9:16
recomposition for the car match cuts and the emptied function room.

Animate in short bursts: one dance move, one picture falling, one hand on a
dial. The decade montage in the instrumental is a single locked-off plate
regenerated per era, not a moving camera.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — told to keep it down

1. *"Somebody's grandmother told us to keep it down,"* — an older woman in a kitchen doorway, hand up, mock-stern, mouthing something lost under the room noise, medium, warm overheads.
2. *"We were twenty-two and wrong about everything but this."* — Mahima and Kai at the counter caught mid-laugh, drinks in hand, entirely unrepentant, handheld two-shot.
3. *"So here's a promise with my whole chest in it,"* — Mahima turning to the lens, the only direct address in the video until the last shot, close-up.
4. *"We are going to be the loudest old people in this town."* — both of them to camera now, Kai's hand on her shoulder, the party blurring behind them, medium.

### Verse 1 — the ghost timeline

5. *"There's a version of us that goes quiet at forty,"* — hard cut to the ghost timeline: the pair in their forties at a kitchen table, beige, still, symmetrical, locked-off, flat shadowless light.
6. *"Beige and careful with a lawn and a schedule."* — a perfect empty lawn, mown in stripes, nobody on it, static wide.
7. *"Sits at the back at the wedding with a plate on their knees,"* — the ghost pair at the back of a wedding with plates balanced on their knees, watching other people dance, locked-off.
8. *"Says we used to, we used to, and never says we will."* — the ghost Mahima mid-sentence, gesturing at something offscreen and behind her, close-up, no light in her eyes.
9. *"I have met them, I have sat across from them at dinner,"* — a restaurant table shot straight down the middle, the ghost pair opposite each other, neither speaking.
10. *"They ordered the same thing they have ordered for a decade."* — two identical plates arriving, neither of them looking at the menu, overhead insert.
11. *"And I love a routine, I do, I will take the Tuesday,"* — a wall calendar with every square filled in identical handwriting (composited), macro, then a soft pull back.
12. *"But do not let me die of being sensible."* — hard cut back to the real timeline: young Mahima at the kitchen table looking slightly sick, handheld, warm and messy.

### Pre-chorus 1 — the swearing-in

13. *"So swear it on the driveway, swear it on the porch,"* — the two of them facing each other on cracked concrete outside, hands gripping each other's forearms like a real oath, static two-shot.
14. *"Swear it on whatever we still own at ninety."* — a porch light with moths battering it, low angle, night.
15. *"No inside voice, no sitting one out,"* — a neighbour's curtain twitching across the street, seen over their shoulders, medium.
16. *"No wondering what the neighbors think."* — the two of them noticing the curtain and deliberately getting louder, handheld, headlights sweeping across them.

### Chorus 1 — the first age jump

17. *"Let's grow old loud, baby, never grow old quiet,"* — smash cut: Mahima and Kai in their seventies dancing hard in the same kitchen, wide handheld, saturated and bright.
18. *"Turn it up in the kitchen till the pictures leave the wall."* — a framed picture actually walking itself off its nail and hitting the floor, slow motion, macro on the glass.
19. *"Let's be the ones they talk about at every family thing,"* — the older pair on a wedding dance floor, front and centre among people fifty years younger, wide.
20. *"The two at the front of the dance floor who should not be there at all."* — a ring of younger guests filming them on phones, delighted, low angle from the middle of the floor.
21. *"Gray hair, bad knees, brand new speakers,"* — a brand new speaker box with the sticker still on it standing next to a walking frame, static insert.
22. *"Same fight about the thermostat for sixty years."* — a hand adjusting a thermostat and a second hand adjusting it straight back, twice, on the beat, extreme close-up.
23. *"Let's grow old loud, baby, never grow old quiet,"* — the older pair back in the kitchen, arms up, the volume visibly too high, handheld wide.
24. *"I'll be the one still shouting when you can't hear."* — Mahima at seventy shouting cheerfully into Kai's ear at point-blank range, both laughing, close two-shot.

### Post-chorus 1 — the car, three ages

25. *"Loud, loud, never grow old quiet,"* — locked-off through a car windscreen: the pair at twenty-two, windows down, both shouting along, day.
26. *"Loud, loud, we are not going to try it."* — identical framing, same car older, the pair at fifty, dusk.
27. *"Loud, loud, put the windows down,"* — identical framing, the car visibly ancient, the pair at eighty, night.
28. *"We're the loudest old people in this town."* — a wide of a suburban street with one car in it and lights coming on down the whole street, locked-off.

### Verse 2 — Kai's picture of eighty

29. *"I looked at you today across a sink of dishes,"* — present day: Kai at twenty-two watching Mahima across a sink full of dishes, kitchen daylight, handheld.
30. *"And I saw the whole thing, eighty and still ridiculous."* — a slow push toward her face that resolves, mid-move, on her face at eighty in the same position.
31. *"Matching jackets that nobody on earth asked us to wear,"* — the aged-up pair in identical loud patterned jackets, standing in a hallway mirror, delighted with themselves.
32. *"Front row at a show for a band that we outlived."* — the front row of a rock show, the two of them the only people over sixty in frame, hands up, concert lighting.
33. *"You singing the wrong words with total confidence,"* — Mahima at eighty singing loudly and confidently wrong, close-up, stage light across her face.
34. *"Me swearing that the wrong words are the right ones."* — Kai at eighty nodding along and joining in with the same wrong words, close-up.
35. *"A camper van, a bad map and an argument at lunch,"* — a camper van pulled onto a verge with a paper map spread on the hood, a full argument in progress, wide, road daylight.
36. *"And a bench with our names on it that we're never sitting on."* — a park bench with a small engraved plaque (composited), the two of them walking straight past it without stopping, static.

### Pre-chorus 2 — the oath, decades on

37. *"So swear it in the driveway, swear it in the car,"* — the same cracked driveway sixty years later, the same grip on each other's forearms, the porch light newer, static two-shot.
38. *"Swear it on the day a doctor says take it easy."* — a consulting room, an unheard sentence from off-frame, both of them nodding politely, clinical white, locked-off.
39. *"No inside voice, no sitting one out,"* — the two of them in the parking lot outside, getting into the car, medium.
40. *"No dying with a good song left unplayed."* — a hand turning the car stereo up hard, extreme close-up, warm evening light through the windscreen.

### Chorus 2 — the family thing

41. *"Let's grow old loud, baby, never grow old quiet,"* — a large family gathering across three generations, the oldest two people in the room obviously the loudest, wide handheld.
42. *"Turn it up in the kitchen till the pictures leave the wall."* — reuse shot 18, tighter, the picture already on the floor and nobody picking it up.
43. *"Let's be the ones they talk about at every family thing,"* — grandchildren filming them on phones, laughing, over-the-shoulder.
44. *"The two at the front of the dance floor who should not be there at all."* — an aunt covering her face and laughing, then dropping her hands and joining in, medium.
45. *"Gray hair, bad knees, brand new speakers,"* — Kai at eighty lowering himself into a dance move his knees clearly disagree with, low angle, and doing it anyway.
46. *"Same fight about the thermostat for sixty years."* — reuse shot 22, now with a third and fourth hand joining the argument, wider.
47. *"Let's grow old loud, baby, never grow old quiet,"* — the whole room dancing, three generations in one wide handheld frame, night through the windows.
48. *"I'll be the one still shouting when you can't hear."* — Mahima at eighty shouting into his ear again, and this time he shouts back, close two-shot.

### Instrumental — the decades, one doorway

49. Fixed locked-off frame on the kitchen doorway, warm tungsten, wallpaper one: the couple at twenty-five crossing it.
50. Identical frame, cool eighties fluorescent, wallpaper two: the same two at forty, crossing faster, a child following.
51. Identical frame, flat nineties daylight, wallpaper three: the same two at sixty, one of them carrying a speaker.
52. Identical frame, modern warm LED, wallpaper four: the same two at eighty, dancing across it instead of walking.
53. The false ending: everything drops to a bare clap track and the same frame with nobody in it, two seconds, absolutely still — then the tom rebuild and they come back through it mid-dance.

### Bridge — his father

54. *"My father went out whispering, he was polite about it,"* — an old man in a chair by a window seen from behind, one lamp, deep shadow, static.
55. *"Held the door for everybody right up to the end."* — a hand holding a door open for someone off-frame, held too long, close-up.
56. *"And I loved him and I am not doing that,"* — a room with a television on mute, blue light, nobody watching it, wide.
57. *"I want the neighbors calling and the ceiling coming down."* — Kai at eighty, close-up, saying it flatly, no performance in it.
58. *"So if we get the forty years, let's spend them like they're stolen,"* — the aged-up pair sitting on the edge of a bed at night, not performing for anyone, talking quietly, wide, one lamp.
59. *"Let's be embarrassing in every photograph."* — a shoebox of photographs on the bed between them, every one of them badly posed, macro.
60. *"And when they turn the volume on the world down for us,"* — her hand finding his on the bedspread, extreme close-up.
61. *"Let's find the dial and break it off."* — a volume dial turned all the way up, macro, and held one beat too long into the modulation.

### Final chorus — nobody leaving

62. *"Let's grow old loud, baby, never grow old quiet,"* — house lights coming up full on an emptying function room, the ugliest light in the film, wide.
63. *"Turn it up in the kitchen till the pictures leave the wall."* — staff stacking chairs along one wall, the sound of it, medium.
64. *"Let's be the ones they talk about at every family thing,"* — a caterer sweeping around the feet of two people in their eighties who are still dancing, low angle.
65. *"The two at the front of the dance floor who should not be there at all."* — a full wide of the cleared room with two figures in the middle of it and nothing else.
66. *"Gray hair, bad knees, brand new speakers,"* — the band packing up, and one of them stopping, looking at the couple, and plugging back in.
67. *"Same fight about the thermostat for sixty years."* — the band starting again for two people, medium on the guitarist grinning.
68. *"No last dance, no lights up, no thank you for coming,"* — the couple dancing under full house lights with no one else in frame, wide, unglamorous, held.
69. *"We are staying till they stack the chairs and sweep the floor."* — the last chairs going up, the broom, and the two of them still going, tracking past.
70. *"Let's grow old loud, baby, never grow old quiet,"* — a high wide of the whole empty room from the balcony, two people at the centre of it.
71. *"I'll be the one still shouting when you can't hear."* — close two-shot, both shouting the line at each other and neither of them hearing it, laughing.

### Post-chorus 2 — the car, four ages

72. *"Loud, loud, never grow old quiet,"* — the car frame at twenty-two again, day.
73. *"Loud, loud, we are not going to try it."* — the car frame at fifty, dusk.
74. *"Loud, loud, put the windows down,"* — the car frame at eighty, night, and a hand coming out of the window to wave.
75. *"We're the loudest old people in this town."* — the suburban street, every light on, the car pulling away, locked-off.

### Outro — the grandmother

76. *"Somebody's grandmother told us to keep it down,"* — the grandmother from shot 1 in the doorway again, hand up, the same frame.
77. *"And she was the last one standing at eleven."* — flashback to the same night: the emptied kitchen, the grandmother alone, dancing to the radio, wide, warm.
78. *"So here's to the noise and the knees and the years,"* — the practical over the sink from shot 1, still on, macro, then a slow pull back.
79. *"Let's grow old loud and let them hear."* — final shot: Mahima and Kai at eighty in the same kitchen doorway, one of them reaching for the volume, both looking straight down the lens for the first time since shot 4, holding it, locked-off, through the fade. No text.

## 5. Edit and the challenge

Markers at: the first stomp, the smash cut into the ghost timeline (shot 5),
*"do not let me die of being sensible"* (shot 12), each *"grow old loud"*, the
picture hitting the floor (shot 18), the false ending (shot 53), *"break it
off"* (shot 61), the modulation into shot 62, and the last frame. At 118 BPM a
bar is 2.03 s; choruses cut every bar, the post-chorus cuts on the half-bar,
and the ghost-timeline verse deliberately cuts slower than everything around
it.

**The age-jump challenge.** Post the vertical cut of the car match cuts
(shots 25–28) — one framing, windows down, three decades — and invite couples
and families to post their own version with a parent or grandparent in the
passenger seat, cut on *"loud, loud, put the windows down."* The picture
falling off the wall (shot 18) is the loop, and the emptied function room
(shots 62–65) is the still image that carries the caption.

## 6. Quality-control checklist

- Five locked identities, each with its own reference set: Mahima at twenty-two, at forty in the ghost timeline and at seventy-plus; Kai at twenty-two and at eighty. No prompt-only ageing anywhere
- The kitchen doorway framing is pixel-identical in shots 49–53 and 79; the practical over the sink appears in shot 1 and shot 78
- The ghost timeline is the only part of the film with no visible practical light source, and the only part cut slower than the music
- Every dance shot has an OpenPose reference, especially the older couple; no invented joints, no floating feet
- The bench plaque, the calendar, the thermostat display and the speaker sticker are composited; no model-generated text
- Direct address to the lens happens exactly twice, in shots 3–4 and shot 79, and nowhere else
- Matching jackets appear only from shot 31 onward, and on both of them
- The car match cuts share one framing and one lens; only the grade, the car and the ages change
- The last shot is locked-off, holds after the volume hand moves, and runs until the audio fades
