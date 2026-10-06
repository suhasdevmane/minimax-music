# Wan 2.2 Shot List — "Under the Same Umbrella"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
98 BPM a bar is 2.45 s, so most shots run 3–5 s and the choruses cut every
bar or two.

## 1. Visual world

A rain-soaked Indian city market street at dusk, and only that street. The
monsoon is a character: rain in every frame, gutters running gold with neon,
tarps and awnings and the banyan tree where the rickshaws hide. **The
umbrella is the frame**: one black umbrella, two people under it, everyone
else running. Colour everywhere: marigold, saffron, the blue tarp, the blue
dupatta bleeding onto a white shirt. Warm and saturated throughout; the only
cold light in the video is the inside of the bus.

| Section | Grade | Camera |
|---|---|---|
| Intro | Blue-grey rain light, neon just switching on | Static under the awning, then a slow tilt up to the umbrella |
| Verse 1 (her) | Gold gutters, red and green neon, warm stall bulb | Two-shot tracking from the front |
| Pre-choruses | Neon reflections underfoot | Low angles on feet, shoulders |
| Choruses | Fully saturated, rain backlit gold | Slow-motion wides, overhead of the umbrella |
| Verse 2 (him) | Warm stall bulb, steam, neon on wet cotton | Handheld, close, playful |
| Instrumental | Golden, slow, then bus headlights sweeping | Slow motion, macro |
| Bridge | Harsh cold bus interior light against warm street | Static, held |
| Final chorus / post-chorus | Brightest, most colourful frames | Moving, spinning, overhead |
| Outro | One warm bulb, blue rain, quiet | Static, slow push-in |

## 2. Character bible — paste into every prompt

**Mahima** (the whole video, one look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and rain-damp at the ends, light natural makeup with a small bindi, wearing a mustard-yellow kurta with a bright blue dupatta over one shoulder, a canvas tote bag, bright amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the stranger with the umbrella)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a plain white cotton shirt with the sleeves rolled, dark trousers, carrying a black umbrella, one shoulder and sleeve soaked dark with rain, warm easy smile, realistic cinematic photography, consistent identity

**The chai wallah** — an older man under a blue tarp, a flat cap, a steaming pot. Seen from the side or over the counter, a warm silent narrator; never a hero close-up.

**The bus driver** — only ever an arm on a horn and a shrug through a rain-streaked windscreen. Faceless.

Objects: the **black umbrella** (in every shot from shot 4 to the end), the **blue dupatta** and the **blue stain** it leaves on his shirt from verse 2 on, the **two chai glasses**, the **banyan tree** with the rickshaws under it, the **bus** and its empty window seat.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All shop signs, the bus route board, the wristwatch face and the wall
clock are composited in the edit.** Generate signage as lit colour blocks
and overlay any lettering in post — the model cannot render legible
script, and this street is covered in it.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and Kai with IP-Adapter or a character LoRA each, front,
three-quarter and profile, dry and rain-damp; keep the chai wallah and the
driver deliberately generic. Keyframes first; OpenPose for the walking
two-shots and the post-chorus spin; Depth for the crowded market wides and
the bus stop. 16:9 first; 9:16 for the overhead umbrella shots, which are
natural vertical content. Animate conservatively: rain falling, steam
rising, an umbrella tilting, feet splashing, a dupatta lifting in the wind.
Rain is easiest added as a particle layer in the edit over a wet plate.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the sky opens

1. *"The sky cracked open right over the market"* — a wide of a crowded market street at dusk, the first fat drops hitting, then the downpour arriving like a wall, vendors grabbing tarps, blue-grey light, static.
2. *"Every rickshaw ran for the shade of a tree"* — three auto-rickshaws swerving under a huge banyan tree, their drivers ducking, rain bouncing off the roofs, medium wide.
3. *"I was counting how far I would have to run"* — Mahima under a shop awning, dupatta pulled over her head, eyes counting the street ahead, weight on her toes, close-up, neon flickering on.
4. *"When a stranger held a black umbrella over me"* — a black umbrella opening beside her and tilting over her head, then a tilt up to Kai holding it, a half-laugh from her, medium.

### Verse 1 — her, the first block

5. *"You said, which way, and I pointed anywhere"* — two-shot from the front, walking, Kai glancing at her, Mahima pointing vaguely down the street, tracking.
6. *"The gutters running gold with the light from the signs"* — low angle on the gutter, water running gold and red with neon, their feet stepping over it, close.
7. *"Your left sleeve was soaking on the side that wasn't covered"* — close-up of Kai's left shoulder and sleeve dark with rain, the umbrella clearly tilted her way, her side dry.
8. *"And you smiled like you didn't even mind"* — her looking at the sleeve, then up at his face, him shrugging with a grin, close-up on him.
9. *"Six blocks to the bus stop, one bus every hour"* — Mahima holding up six fingers and pointing down the long neon street, the bus stop somewhere in the rain, medium.
10. *"The chai stall's got a tarp and a pot that never sleeps"* — the chai stall under a blue tarp, steam rising off a boiling pot, the chai wallah stirring, rain sheeting off the tarp edge, warm bulb.
11. *"You asked me for my name, I said, ask me at the corner"* — Kai asking, Mahima tilting her head and nodding toward the next corner, a small smile, two-shot.
12. *"Some things go better slow when the whole street's running deep"* — a wide of the flooded street, the two of them walking slowly while everyone else runs, the umbrella steady, slow motion.

### Pre-chorus 1 — puddles, shoulders

13. *"Every step, the puddles clap under our feet"* — low angle on four feet splashing through a puddle in rhythm, neon in the water, on the beat.
14. *"Every step, your shoulder gets closer to mine"* — close-up on two shoulders under the umbrella, the gap between them closing, from behind.
15. *"Don't look at the sky, don't look at the time"* — Mahima covering her wristwatch with her other hand (face composited), Kai looking pointedly at the ground, medium.
16. *"Just walk, just walk, just walk"* — three cuts on the words: feet, feet, the umbrella from behind moving into the neon.

### Chorus 1 — the only ones dry

17. *"Under the same umbrella, we're the only ones dry"* — slow-motion wide, the crowd streaking past in the rain, the black umbrella still and calm in the middle, both faces lit and laughing.
18. *"Two strangers in a monsoon, let the whole town go by"* — overhead of the black umbrella moving through a sea of colourful tarps and running people, drone.
19. *"The rain's got the city, the city's got us"* — a flooded crossing, a wedding band caught in the rain still playing, the umbrella passing them, wide.
20. *"Six blocks is a lifetime when you're waiting on a bus"* — a bus stop sign far down the street (composited), the two of them in no hurry, tracking from behind.
21. *"Under the same umbrella, count the corners, one, two"* — Mahima counting on her fingers as they pass a corner, then a second corner, quick cuts on the beat.
22. *"I'm halfway to the bus stop, and I'm halfway to you"* — close two-shot, her looking at him a beat too long, rain backlit gold behind them, slow push-in.

### Verse 2 — him, the chai stall

23. *"I only had the one umbrella, I was headed the other way"* — flashback, thirty seconds before the intro: Kai walking the opposite direction under the umbrella, passing the awning where she stands, tracking.
24. *"But you looked like you'd run for it, and I couldn't watch that"* — his point of view of Mahima under the awning about to bolt, then his feet stopping and turning around on the wet pavement.
25. *"The chai wallah gave us two cups for the price of one"* — present: the chai wallah handing two small glasses across the counter and holding up one finger, over-the-shoulder, warm bulb.
26. *"Said the rain does this to strangers, and he tipped his cap"* — the chai wallah tipping his flat cap with a knowing look, then the two of them clinking glasses, close.
27. *"Your dupatta's dripping blue all down my white shirt"* — close-up of the wet blue dupatta against Kai's shoulder and the blue bleeding into his white shirt.
28. *"It's the best that shirt has ever looked, I swear"* — Kai looking down at the blue stain and grinning, Mahima covering her mouth, medium two-shot.
29. *"Three blocks in, you've stopped checking where the bus stop is"* — Mahima not looking down the street at all anymore, just at him, chai in hand, close-up.
30. *"And I'm walking slower, like I don't want to get there"* — low angle on Kai's feet slowing almost to a stop, the umbrella drifting, tracking.

### Pre-chorus 2 — no gap now

31. *"Every step, the puddles clap under our feet"* — reuse shot 13, closer, the feet now side by side.
32. *"Every step, your shoulder gets closer to mine"* — the two shoulders now touching, the umbrella tilting so the rain hits them both a little, from behind.
33. *"Don't look at the sky, don't look at the time"* — a wall clock on a shop front (composited), both of them looking anywhere but at it, medium.
34. *"Just walk, just walk, just walk"* — the umbrella from the front, both faces under it, neon streaking past behind them, tracking.

### Chorus 2 — the city as a party

35. *"Under the same umbrella, we're the only ones dry"* — a temple bell ringing in the rain, kids jumping in puddles, the umbrella passing through, wide, saturated.
36. *"Two strangers in a monsoon, let the whole town go by"* — reuse shot 18, the overhead, now passing a shop front strung with lights.
37. *"The rain's got the city, the city's got us"* — a rickshaw sending up a wave that soaks everyone but them, the umbrella catching it, slow motion.
38. *"Six blocks is a lifetime when you're waiting on a bus"* — Mahima and Kai laughing hard at the wave, leaning into each other, close two-shot.
39. *"Under the same umbrella, count the corners, one, two"* — corner four, corner five, her fingers, quick cuts.
40. *"I'm halfway to the bus stop, and I'm halfway to you"* — the bus stop shelter now visible at the end of the street, her face falling a little at the sight of it, close-up.

### Instrumental — the last block, no lyrics

41. A street dog shaking off rain under a doorway, slow motion, gold.
42. A bicycle bell, a cyclist passing in a plastic poncho, the umbrella turning to follow him, medium.
43. Kai spinning the umbrella once so the rain flies off in a ring, Mahima's eyes following it, slow motion, backlit.
44. Macro: one raindrop on Mahima's eyelash, her blinking, the neon in the drop.
45. The bus stop shelter in the rain, headlights sweeping over the two of them from the left, the music dropping to rain alone, the cut into the bridge.

### Bridge — the bus

46. *"There's the bus stop, there's the bus, there's the door swinging wide"* — a bus pulling in, its door folding open, harsh white interior light spilling onto the wet kerb, static.
47. *"And the driver's on the horn like he's got somewhere to be"* — the driver's arm on the horn through a rain-streaked windscreen, faceless, then Mahima flinching at the sound.
48. *"You could keep the umbrella, I could walk home in the rain"* — Kai holding the umbrella handle out to her, rain starting to hit his head, close-up on the handle between them.
49. *"Or the next one's in an hour, and the chai is still on me"* — him nodding back down the street toward the blue tarp, a hopeful half-smile, medium.
50. *"Say the word and I'll stay, say the word and I'll stay"* — extreme close-up of Mahima's mouth about to speak, then her eyes, the bus door light on one side of her face.
51. *"I don't know your name, but I know I don't want to go"* — her hand not taking the handle, her feet not moving toward the door, low angle, held.
52. *"So the bus pulls away with an empty seat by the window"* — the door folding shut, the bus pulling out, an empty window seat sliding past with rain on the glass, tracking with the bus.
53. *"And we're standing in the flood, and I've never felt less alone"* — the two of them alone on the kerb under the umbrella, red tail lights fading on the wet road, then a laugh breaking out of both of them, wide.

### Final chorus — the wrong way

54. *"Under the same umbrella, let the bus roll on by"* — the bus disappearing into the rain in the background, the umbrella in the foreground turning around, wide.
55. *"Two strangers in a monsoon, and neither says goodbye"* — the two of them walking back the way they came, the wrong way, laughing, tracking from behind.
56. *"The rain's got the city, the city's got us"* — the flooded street opening up ahead of them, neon on the water, the brightest wide of the video.
57. *"Who needs a lifetime when you're missing every bus"* — a second bus passing them going the other way, Mahima waving it off without looking, close-up.
58. *"Under the same umbrella, count the corners, one, two"* — the corners going past in reverse now, her counting backwards on her fingers, quick cuts.
59. *"I'm not going to the bus stop, I'm just going with you"* — the chai wallah seeing them coming back and already pouring two more glasses, then the two of them arriving under the tarp, warm.

### Post-chorus — let it pour

60. *"Let it pour, let it pour, we're not going anywhere"* — the two of them spinning under the umbrella in a flooded square, overhead, rain lit like sparks.
61. *"Let it pour, let it pour, there's a whole night to spare"* — low angle on their feet splashing in a circle, people clapping from doorways behind them.
62. *"Let it pour, let it pour, on the market, on the street"* — both lifting the umbrella away and letting the rain hit their faces for one second, eyes closed, laughing, slow motion.
63. *"The only ones dry from our heads to our feet"* — the umbrella coming back down over both of them, soaked now and not caring, close two-shot.

### Outro — the bench

64. *"The sky's still open right over the market"* — late, the market quieter, the same rain, the same banyan tree, wide, static.
65. *"The rickshaws are still hiding under the tree"* — the three rickshaws still parked under the banyan, a driver asleep in one, medium.
66. *"I never did tell you my name at the corner"* — the two of them on the chai stall bench under the tarp, Kai asking again with his eyebrows, Mahima shaking her head and smiling, two-shot.
67. *"You just kept the umbrella over me"* — the black umbrella still open over her head even under the tarp, his hand on the handle, close-up on the hand.
68. *"You just kept the umbrella over me"* — final shot: overhead of the umbrella from above the tarp, two heads beneath it, the rain, the last neon sign switching off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the umbrella opening (shot 4), each
"under the same umbrella", the male verse entrance, the instrumental, the
bus horn (shot 47), the bus pulling away (shot 52), "I'm just going with
you", and the final "over me." At 98 BPM a bar is 2.45 s.

**The umbrella-share challenge.** Post the vertical overhead cut of chorus 1
(shots 17–22) with *"under the same umbrella, we're the only ones dry"* on
screen and invite people to film their own two-under-one-umbrella walk, the
rule being that whoever is on the wet side has to keep smiling. The bus
door standoff (shots 46–53) is the second shareable cut, made for a
slow-zoom edit with *"say the word and I'll stay."*

## 6. Quality-control checklist

- One look each for the whole video: Mahima in the mustard kurta and blue dupatta, Kai in the white shirt with one soaked sleeve; the blue stain on his shirt appears at shot 27 and stays for the rest of the video
- The black umbrella is in every frame from shot 4 to shot 68, and it is always tilted her way
- The chai wallah never gets a hero close-up; the bus driver is only an arm and a windscreen
- All signage, the bus board, the watch and the wall clock composited; no model-generated script
- Rain in every exterior frame; the only cold light in the video is the bus interior in the bridge
- Everyone else in the street is running or sheltering; the two leads are the only people walking slowly
- No distorted hands on the umbrella handle or the chai glasses
- The last shot is the overhead and holds until the audio fades
