# Wan 2.2 Shot List — "Ring on a Rainy Day"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
82 BPM a bar is 2.93 s, so most shots run one bar and the wide chorus shots
run two.

## 1. Visual style

A wet wedding, shot like a documentary that got lucky. Two timelines: the
**proposal**, one year earlier, is silver and storm-flat on a seafront —
no warm light anywhere in it; the **wedding day** is grey-green garden light
that gets steadily warmer as lamps, bulbs and one nine-second break of gold
take over from the sky. **Water is the co-star**: rain on canvas, standing
water on a dance floor, mud on every hem by the end. Nobody in this video is
unhappy about the rain except the professionals being paid to worry.

Two rules hold the grade together: no shot is dry after shot 5, and the
warmest light in the film is always man-made.

| Section | Grade | Camera |
|---|---|---|
| Intro | Flat overcast, fluorescent shop interior | Static, close |
| Verse 1 (proposal) | Silver storm daylight, no warmth | Wide handheld, then macro |
| Pre-chorus 1 | Grey-green, one warm window | Fast handheld, following staff |
| Choruses | Lifted grey with a rented warm key | Crane, wide, then tracking |
| Verse 2 (his morning) | Warm interior, then flat wet exterior | Static indoors, handheld at the aisle |
| Pre-chorus 2 | The gold seam under the cloud | Slow, patient |
| Instrumental | Late afternoon, lamps taking over | Locked-off details, one slow motion |
| Bridge | Warm lamp on paper, cool grey behind | Static, then silhouette |
| Final chorus | Tent glow against night rain | Handheld, low across water |
| Post-chorus | Night, one work light | Wide, moving with the crowd |
| Outro | Blue dark, one lamp on a pole | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (proposal, one year earlier)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair soaked flat by rain, mascara running, wearing a olive raincoat open over a grey jumper and jeans, overwhelmed laughing-crying expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (wedding day, ceremony)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned in a soft low updo with wet strands loose at the temples, natural bridal makeup, wearing a simple ivory silk slip wedding dress with a heavy wet hem, calm radiant expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (final chorus, barefoot in the garden)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair completely flattened by rain and falling loose, makeup washed soft, wearing the same ivory silk dress now soaked and clinging with mud at the hem, barefoot, open joyful expression, realistic cinematic photography, consistent identity

**Kai** (the groom)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a navy three-piece suit with the jacket off by the second half and a white shirt whose collar has gone soft with rain, tie loosened, warm steady expression, realistic cinematic photography, consistent identity

Supporting people are family, not characters: **his father** (older man, grey
suit, holding his jacket over his wife's hair), **her mother**, **her uncle**
(the striped golf umbrella), **the planner** (clipboard, headset, permanently
damp), **the photographer** (rain cover, crouching), **a grandmother in a
clear plastic rain bonnet**, **a flower girl who stamps in puddles**. Keep
them slightly out of focus or in profile; none of them needs a locked
identity. Anyone from the couple's past is not in this video at all.

Objects that repeat: the **two clear plastic umbrellas** from the intro (they
reappear in the crowd), the **ring box** with the stiff hinge, the **satin
shoes** that get carried and then abandoned, the **paper chain**, the
**old square wedding album**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, signage, the weather app, the order of service and the old
album's printed dates are composited in the edit.** Generate the phone as a
lit blank screen and the album pages as blank square photo frames, and drop
the imagery in afterwards — the model cannot render legible interface or
print, and the forecast screen is the first beat of the story.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai in his one look with IP-Adapter or a
character LoRA each; the wet hair look is a separate reference set, not a
retouch of the dry one. Keyframes first; OpenPose for the kneeling proposal,
the aisle walk and the first dance; Depth for the marquee interiors and the
crane shot over the umbrellas. 16:9 first; 9:16 recomposition for the
umbrella crane and the flooded dance floor, which are the two vertical cuts.
Animate conservatively: falling rain, a hem dragging, a hinge, a laugh, water
spraying off a stamped foot. Rain is easiest added as a real particle pass in
the edit over a plate generated wet rather than asked for as motion.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–6 s.

## 4. Scene per lyric line

### Intro — the forecast

1. *"The forecast said a hundred percent by four,"* — extreme close-up of a phone held in a car, a blank lit screen (weather UI composited), rain hammering the windscreen behind it, static.
2. *"So we bought the cheap umbrellas at the corner store."* — inside a coast-road convenience store, two clear plastic umbrellas pulled off a wire rack, fluorescent light, handheld.
3. *"You said that we could wait for a kinder sky,"* — Kai at the counter looking back over his shoulder at the door and the weather beyond it, medium, flat daylight through wet glass.
4. *"I said the sky has had its whole life to try."* — Mahima pushing the shop door open into the rain with the umbrella still folded, walking out unbothered, tracking from behind.

### Verse 1 — the proposal, one year earlier

5. *"You went down on the wet in a parking lot by the water,"* — very wide: a gravel seafront parking lot, a low grey sea, two tiny figures, Kai going down onto one knee into standing water, locked-off.
6. *"Gray coming sideways off the sea behind your back."* — reverse over Mahima's shoulder, the storm filling the whole background, his silhouette kneeling against it, handheld.
7. *"The box would not open and your hands were shaking,"* — macro on the ring box hinge, his thumbnail slipping twice, rain beading on the velvet, extreme close-up.
8. *"And I was crying before you got the question out."* — her face, hands coming up over her mouth, already gone, close-up, silver light.
9. *"Your knee left a print in the gravel and the rain,"* — insert straight down on wet gravel, a knee-shaped depression slowly filling with water, macro.
10. *"My mascara took a shortcut down my chin."* — extreme close-up of one dark track running from her lashline to her jaw, her laughing through it.
11. *"And you laughed like the weather was a friend of yours."* — Kai's head tipped back, laughing straight up into the rain, low angle, the sky white behind him.

### Pre-chorus 1 — the venue in crisis

12. *"They moved the chairs inside, they moved the flowers twice,"* — two men running a stack of white folding chairs across a lawn, fast handheld, following them.
13. *"The tent man never showed and the aisle turned to clay,"* — the planner on a headset with the clipboard held flat over her hair, then a tilt down to an aisle runner sinking into mud.
14. *"Everyone kept apologizing for the sky,"* — a montage of three people mouthing apologies to camera-left, quick cuts, all of them soaked.
15. *"And the two of us were the only ones okay."* — split action: Mahima perfectly still at an upstairs window; hard cut to Kai perfectly still under an awning. Two static frames in a moving film.

### Chorus 1 — the ceremony under umbrellas

16. *"You gave me a ring on a rainy day,"* — crane rising over the seated guests, every one holding an umbrella, a field of black and clear domes, the couple bare-headed at the centre.
17. *"So let it rain, let it come, let it stay."* — the crane continuing up and back, the umbrellas becoming a pattern, rain in the light, wide.
18. *"Let it soak through the silk and ruin the shoes,"* — low insert of the ivory hem dragging a wet line through cut grass; a bridesmaid behind carrying the satin shoes.
19. *"There is nothing in this garden I would trade for you."* — Mahima's face at the altar, close-up, rain on her cheekbones, looking only at him.
20. *"The band's under the awning and the cake's in the hall,"* — a four-piece band crammed under a stretched awning, cables taped down; cut to two people carrying a cake indoors very carefully.
21. *"And your hand is on my back and I don't care at all."* — close-up of Kai's hand flat against her back as they turn, water beading on the silk under his palm.
22. *"Every good thing I have came the same way,"* — the couple mid-turn, both faces, the umbrella field soft behind them, medium two-shot.
23. *"You gave me a ring on a rainy day."* — pull wide to the whole canopy from outside, rain streaking the lens, warm key light under it.

### Verse 2 — Kai, the morning and the vows

24. *"I ironed a shirt at seven and it lost by ten,"* — an iron hissing on a board in a small rented room, morning window light, static close-up.
25. *"Stood at the end of the aisle with my collar going soft,"* — the same shirt three hours later, collar wilting, shoulders dark with rain, medium on Kai from behind, waiting.
26. *"My father held his jacket like a roof over my mother,"* — an older man holding his suit jacket spread over his wife's hair, both smiling, medium, flat daylight.
27. *"And your uncle raised a golf umbrella like a flag."* — an enormous striped golf umbrella going up in the third row, low angle, the whole row disappearing under it.
28. *"Then the doors came open and none of it mattered,"* — Kai's eyeline: the far garden gate opening, the aisle, a figure at the end of it, slow push-in, everything else falling out of focus.
29. *"Thunder took the second half of what I meant to say,"* — a hard flash across the sky, the guests flinching in unison, the officiant pausing, wide.
30. *"So I said it again louder, and I'd say it in worse."* — extreme close-up of Kai's face saying it again, bigger, the tendons in his neck, rain running off his jaw.

### Pre-chorus 2 — the gold seam

31. *"The photographer kept waiting for a break in it,"* — the photographer crouched under a rain cover, checking the sky every few seconds, medium, patient camera.
32. *"Then the light went strange and gold behind the gray,"* — a low gold seam opening under the cloud, the whole garden changing colour in one shot, wide, slow.
33. *"Everyone kept apologizing for the sky,"* — reuse the apology montage from shot 14, now lit gold, tighter.
34. *"And we were the only two who wanted it this way."* — the couple standing still in the gold, holding hands, unhurried, medium two-shot.

### Chorus 2 — the reception, everyone past caring

35. *"You gave me a ring on a rainy day,"* — guests dancing in their coats inside the marquee, wide handheld into the crowd.
36. *"So let it rain, let it come, let it stay."* — a grandmother in a clear plastic rain bonnet clapping exactly on the beat, close-up, delighted.
37. *"Let it soak through the silk and ruin the shoes,"* — the flower girl stamping in a puddle on purpose, slow motion, spray catching the lamp light.
38. *"There is nothing in this garden I would trade for you."* — Mahima across the room finding Kai in the crowd, one look, over-the-shoulder.
39. *"The band's under the awning and the cake's in the hall,"* — the band from behind, playing out at the marquee mouth, rain falling past the frame edge.
40. *"And your hand is on my back and I don't care at all."* — reuse the hand on the back from shot 21, now with the tent glow behind it, wider.
41. *"Every good thing I have came the same way,"* — the marquee from outside, glowing in a dark wet field, rain streaking the lens, wide.
42. *"You gave me a ring on a rainy day."* — hold on that exterior, the sound of the room carrying, slow drift.

### Instrumental — rain and one violin

43. Water running off a canvas seam in a rope, macro, backlit by the tent.
44. The abandoned aisle runner, mud-tracked and curling at the edge, locked-off.
45. The pair of satin shoes upside down on a folding chair, one lying on its side.
46. The string quartet under the awning, instrument cases held over the instruments between phrases, medium.
47. Slow motion: guests running from the house to the tent with jackets over their heads, laughing, wide.

### Bridge — the album and the answer

48. *"My mother married in a heatwave, not a cloud to spare,"* — an old square wedding album open on a side table, blank photo frames (imagery composited: a cloudless sky, a squinting bride), warm lamp, static.
49. *"An album full of sunshine and a house she had to leave."* — Mahima's hand turning a page, then her face in the present, tender and unsentimental, close-up.
50. *"So keep the painted blue, keep the perfect afternoon,"* — a tilt up from the album to the leaking marquee seam above her, water finding a path down the canvas.
51. *"I will take a roof that leaks above a man who doesn't."* — her closing the album with one hand and standing, medium, cool grey behind and warm lamp in front.
52. *"And I will take the woman who kicked her heels off early,"* — the satin shoes abandoned under the chair, then her bare feet stepping off the boards into wet grass, insert.
53. *"Who never checked her hair and walked out into it."* — Kai watching her walk out into the rain, then following without hesitating, both in silhouette against the tent doorway.

### Final chorus — the first dance in a wet garden

54. *"You gave me a ring on a rainy day,"* — the two of them alone on grass in the dark, the band playing from the tent mouth, rain lit like sparks against the backlight, wide.
55. *"So let it rain, let it come, let it stay."* — close on their hands and her soaked back, turning slowly, handheld.
56. *"Let it flatten every curl that took an hour to do,"* — her hair completely flat, water running from it, her laughing at nothing, close-up.
57. *"There is nothing in this garden I would trade for you."* — his face over her shoulder, eyes closed, close-up, the tent glow behind.
58. *"There's a river running under the floor of the tent,"* — cut inside: a low angle across the wooden dance floor with an inch of water moving over it, bulbs doubled in the reflection.
59. *"And we're barefoot in the middle of it, soaked and content."* — feet stamping and spraying on the beat, low and fast, then a tilt up to the couple still at the centre.
60. *"Every good thing we have came the same way,"* — guests spilling out of the tent into the garden to join them, shoes in hands, wide handheld.
61. *"You gave me a ring on a rainy day."* — a full wide of the garden dance from above, everyone in the rain, the tent behind them, drone or high crane.

### Post-chorus — nobody is going in

62. *"So let it rain, so let it rain,"* — forty people singing straight up at the sky, low angle from the middle of them.
63. *"On the folding chairs and the paper chain,"* — a paper chain sagging and dripping between two poles; folding chairs standing in puddles, two quick inserts.
64. *"So let it rain, so let it rain,"* — the planner putting the clipboard down on a wet table and joining in, medium.
65. *"We are not going in, we are not going in."* — the whole crowd with arms up, one work light on a stand behind them, wide, night.

### Outro — the last of it

66. *"The last song finished and nobody moved,"* — the band packing up while the crowd keeps dancing to nothing, medium, sound of rain only.
67. *"Fifty people dancing in a garden turned to mud."* — a slow pan across mud-covered shoes, hems and trouser cuffs at ankle height.
68. *"The forecast said a hundred percent by four,"* — the two clear plastic umbrellas from the intro, forgotten and unopened on a chair, macro.
69. *"And it kept its word, and so did we."* — final shot: the couple last in the dark garden, the tent unlit behind them, still holding each other and not dancing to anything, rain still falling, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first piano note, the knee hitting the water (shot 5), each
*"you gave me a ring on a rainy day"*, the thunder (shot 29), the gold seam
(shot 32), the instrumental, *"a man who doesn't"* (shot 51), the modulation
into shot 54, and the last frame. At 82 BPM a bar is 2.93 s; the choruses cut
every bar and the pre-choruses cut every half-bar to feel like the panic they
are describing.

**The wet-wedding challenge.** Post the vertical cut of shots 16–19 — the
umbrella crane into the dragging hem — under *"so let it rain"* and invite
couples to post the footage from the day their weather went wrong: mud,
hems, flooded marquees, ruined shoes. The flooded dance floor (shots 58–59)
is the second shareable frame and the better loop.

## 6. Quality-control checklist

- Three Mahima looks in the right sections: raincoat only in the proposal, updo through the ceremony and reception, flat wet hair and bare feet from shot 52 on, never earlier
- Kai's collar is crisp only in shot 24 and soft in every shot after it
- Nothing is dry after shot 5; every exterior plate is generated wet
- The warmest light in any frame is man-made, never the sky, except the nine seconds of gold in shots 32–34
- The weather app, the album prints and all signage are composited; no model-generated text anywhere
- The satin shoes are worn, then carried, then abandoned, in that order, and never worn again
- The two clear umbrellas appear in the intro and return unopened in shot 68
- No guest's face is held long enough to need a locked identity
- The last shot is locked-off, has no dancing in it, and holds until the audio fades
