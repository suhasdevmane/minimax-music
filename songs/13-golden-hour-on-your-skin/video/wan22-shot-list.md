# Wan 2.2 Shot List — "Golden Hour on Your Skin"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
96 BPM a bar is 2.5 s; most shots hold for one or two bars.

## 1. Visual style

Golden hour, always. Three locations — a **rooftop car park**, a **field of
long grass**, and a **car bonnet on the shoulder of a back road** — and all
three are shot in the same twenty minutes before sunset, so the whole video
lives in one colour: honey, amber, a little red at the end. Lens flare on
every hook, heavy film grain throughout, dust and pollen in the air. The
only breaks from gold are deliberate: two quick flashes of *dark* and
*noon* inside each chorus, a grey imagined winter in the bridge, and blue
hour for the outro. The **phone she doesn't use** is a motif — she raises
it and lowers it until the post-chorus, when she finally takes the photo.

| Section | Grade | Camera |
|---|---|---|
| Intro / verse 1 | Full gold, long shadows, flare, grain | Static wides, slow push-ins |
| Pre-choruses | Sun on the horizon, flare at its strongest | Slow, at the edge |
| Choruses | Gold with two hard flashes (dark kitchen, flat noon) | Handheld, cut on the beat |
| Verse 2 | Lower, redder, grass glowing, gravel road | Moving, wind, windows down |
| Instrumental | Last gold, then a beat of blue | Slow motion, macro |
| Bridge (winter) | Desaturated grey, flat light | Locked-off |
| Bridge (turn) / final chorus | Warmest frames in the video | Moving, wider |
| Post-chorus | The very last gold | Close, then a held still |
| Outro | Blue hour, streetlights, one gold phone screen | Slow, calm |

## 2. Character bible — paste into every prompt

**Mahima** (rooftop, intro through chorus 1, bridge turn, final chorus, outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and lifted by a light breeze, light natural makeup with a warm glow, wearing a cream ribbed tank top and faded high-waisted jeans, gold hoop earrings, soft amazed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (field and back road, verse 2 through instrumental)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and windblown, a small crown of dandelions on her head, light natural makeup, wearing a loose white linen shirt open over a yellow sundress, barefoot, laughing open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (imagined winter, bridge first half only)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely, no makeup, wearing an oversized grey knit jumper, quiet wistful expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead, on screen in every gold section)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, light freckles across his cheeks and forearms, wearing a faded olive t-shirt and dark jeans, relaxed easy grin, lit from the side by low sun, realistic cinematic photography, consistent identity

Objects: the **dusty old car** (a boxy, sun-faded estate, warm grey), the
**can of lemonade**, the **dandelion crown**, the **phone** she keeps not
using.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The phone screen and the final photo are composited in the edit.**
Generate the phone as a lit blank screen in her hand and overlay the still
in post — the model cannot render a clean legible photo-on-a-screen, and the
outro's last frame depends on it.

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

Most shots 3–5 s. For this video specifically: lock Kai too (front,
three-quarter, profile, lit from the left and from the right), because he is
on screen for almost every line; generate the sun as a practical flare in
the still and let the model animate grain, dust, hair and grass, not the
light itself.

## 4. Scene per lyric line

### Intro — twenty minutes to go

1. *"Twenty minutes till the sun goes down"* — a wide of the sky above a city rooftop car park, the sun low and huge between two towers, honey and orange, heavy grain, static.
2. *"The whole sky turning honey brown"* — tilt down from the sky to the roof: a dusty grey estate car parked alone, long shadows across the concrete, flare across the lens.
3. *"You're leaning on the car with your eyes half closed"* — Kai leaning back against the bonnet, eyes half closed, sun on the side of his face, medium, slow push-in.
4. *"And I swear the light knows something I don't know"* — Mahima (rooftop look) a few steps away, watching him with a small unhidden smile, the low sun behind her hair, close-up.

### Verse 1 — the rooftop, the lemonade, the freckles

5. *"Seven forty on a Thursday, rooftop, no plans"* — the two of them sitting on the bonnet with their feet on the bumper, the city below, wide from the side, gold.
6. *"Warm can of lemonade sweating in your hands"* — extreme close-up of a sweating lemonade can in Kai's hands, condensation catching the sun, macro.
7. *"You're telling me a story that you've told before"* — Kai mid-story, gesturing with the can, laughing at his own joke, medium close-up, handheld.
8. *"But the way the sun hits your jaw, I want to hear it more"* — his jawline lit from the side, then rack focus to Mahima not listening, just looking, over her shoulder.
9. *"Dust in the air like it's floating on purpose"* — a shaft of low sun full of floating dust between them, backlit, macro, slow.
10. *"Every little freckle coming up to the surface"* — extreme close-up of the freckles on Kai's cheek and forearm in the direct light, his eyes crinkling.
11. *"I've got a hundred pictures that I never take"* — Mahima raising her phone toward him, framing, then lowering it without taking the shot, close-up on her hands and face.
12. *"Cause a camera never gets you the way I do, babe"* — her eyes on him instead, the phone face-down on the bonnet beside her, close-up, warm.

### Pre-chorus 1 — the edge of the roof

13. *"And I know it only lasts a little while"* — the sun visibly lower now, sitting between the two towers, wide, flare at full strength.
14. *"The light, the heat, the way you smile"* — three quick cuts on the beat: the sun; heat haze off the car roof; Kai's smile.
15. *"But if this is all I ever get to keep"* — Mahima stepping up beside him at the rooftop edge, their shoulders touching, medium from behind.
16. *"Then let me stand here till it sinks beneath the street"* — their two shadows stretched all the way back across the roof, the sun half behind the skyline, wide, static.

### Chorus 1 — the photograph being taken

17. *"Golden hour on your skin"* — Kai's bare forearm in the sun, her hand resting on it, macro, flare.
18. *"And I'm falling all over again"* — Mahima falling back onto the bonnet laughing, hair spreading, overhead, slow motion.
19. *"Every day the sun comes down"* — the field at golden hour: long grass leaning in the wind, lit from behind, wide.
20. *"And every day you pull me in"* — Kai pulling Mahima in by the hand on the back road, her stumbling into him laughing, handheld.
21. *"Golden hour on your skin"* — the back of his neck and shoulder in the light as she rests her chin on it, close-up.
22. *"Like the light was made to fit you in"* — a hard one-second flash: the two of them in a dark kitchen at night, then a flat fluorescent flash of them in a supermarket aisle, both fine, both plain, then back to gold.
23. *"I've loved you in the dark, I've loved you in the noon"* — Kai turning toward her on the rooftop, the flare crossing his face, slow motion, medium close-up.
24. *"But nothing hits like you at half past seven in June"* — the hook frame: the slow-motion turn completing, his grin arriving, the flare swallowing the edge of frame, hold.
25. *"Golden hour on your skin"* — the two of them on the rooftop edge, foreheads almost touching, wide, backlit.
26. *"And I'm falling all over again"* — Mahima's face, eyes closed, sun on her lashes, close-up, warm.

### Verse 2 — the field, the back road, the bonnet

27. *"Sunday in the field where the long grass leans"* — Mahima (field look, no crown yet) walking into long grass at golden hour, the grass leaning in a wind, tracking from behind.
28. *"You made a crown of dandelions, said, here, my queen"* — Kai's hands weaving dandelion stems, then placing the crown on her head with an exaggerated bow, medium, handheld.
29. *"We drove the back roads with the windows wide"* — the estate car on a back road with every window down, Mahima's hair everywhere, her hand out riding the air, tracking alongside.
30. *"Pulled over on the shoulder just to catch the light"* — the car pulling onto a gravel shoulder, dust rising gold behind it, fields either side, wide.
31. *"You sat up on the bonnet with your shoes kicked off"* — Kai's bare feet on the bumper, his trainers dropped in the gravel, low angle, sun on the road behind.
32. *"Talking about nothing till the nothing felt like love"* — both of them up on the bonnet talking, her knees pulled up, the sun sitting on the road at the horizon, wide static.
33. *"And I thought, this is it, this is the frame"* — Mahima looking at Kai instead of the sunset, the dandelion crown catching the light, close-up.
34. *"The one I'd hang above the door if a day could stay the same"* — a held, still, locked-off frame from behind the car: the two of them on the bonnet, the road running straight into the sun. Hold a full bar.

### Pre-chorus 2 — let it leave slow

35. *"And I know the sun's already on its way"* — the sun sliding down the road toward the horizon, time-lapse feel, wide.
36. *"It's got a whole other side of the world to save"* — the top of the frame going blue while the bottom stays amber, the field between, wide.
37. *"But if it's leaving, let it leave me slow"* — Mahima's hand on Kai's forearm, studying the colour of his skin in the last light, macro.
38. *"Let me memorise the colour of your skin before it goes"* — her eyes closing for a beat, as if saving it, close-up, deep amber.

### Chorus 2 — bigger, closer

39. *"Golden hour on your skin"* — Mahima spinning in the field with the dandelion crown, slow motion, sun behind her, wide.
40. *"And I'm falling all over again"* — Kai lifting her off the bonnet and setting her down, her feet leaving the ground, handheld.
41. *"Every day the sun comes down"* — reuse shot 19, tighter, more wind.
42. *"And every day you pull me in"* — the two of them running across the rooftop car park toward the edge, hand in hand, tracking, gold.
43. *"Golden hour on your skin"* — reuse shot 21, tighter.
44. *"Like the light was made to fit you in"* — the dark kitchen flash and the noon supermarket flash again, half a second each, then gold.
45. *"I've loved you in the dark, I've loved you in the noon"* — Kai carrying her on his back through the long grass, both laughing, tracking.
46. *"But nothing hits like you at half past seven in June"* — the lens flare swallowing the whole frame on the hook, then resolving on his face, slow motion.
47. *"Golden hour on your skin"* — a wide of the field with the two of them tiny in it, the sun a red disc, static.
48. *"And I'm falling all over again"* — Mahima's face against his shoulder, eyes open this time, looking at the camera, close-up.

### Instrumental — the lens-flare montage

49. Long grass in extreme slow motion, backlit, pollen drifting, macro.
50. Mahima's hair filling a car window, the sun strobing through it, slow motion.
51. A hand out of the car window riding the air, the road blurring gold below, tracking.
52. Kai holding his hand up to the sun, the flare breaking between his fingers, extreme close-up.
53. Mahima's face lit from the side, eyes closed, the crown slightly crooked, slow motion; then the sun dropping behind the skyline and the frame going briefly blue and quiet for the cut into the bridge.

### Bridge — the imagined winter, then the turn

54. *"And when the winter comes and the sky goes grey at four"* — a grey flat, Mahima (winter look) at a window, the light flat and colourless, locked-off, desaturated.
55. *"And the light's a cold thing coming through the door"* — a cold slab of grey light on a wooden floor through an open door, static, empty.
56. *"I'll close my eyes and it's July again"* — her closing her eyes at the window, then a warm one-second flash of the rooftop cutting in, close-up.
57. *"Rooftop, back road, you and the honey light, and then"* — three warm flashes on the words: the rooftop edge, the gravel shoulder, Kai in the honey light, then the grey again.
58. *"You'll look at me the way you're looking now"* — hard cut to the present: the rooftop, gold, Kai looking at her, the look held, medium close-up.
59. *"And I'll fall, I don't know how, but I'll fall somehow"* — Mahima's face changing as she understands it, a laugh that's almost a breath, close-up.
60. *"Cause it was never really the sun, it was you"* — the turn: she turns her back on the sunset to face him, the flare now behind her head, medium.
61. *"Golden hour's just the hour I remember to look at you"* — the two of them face to face at the edge, the strings entering, wide, the warmest frame so far.

### Final chorus — every location, the best frames

62. *"Golden hour on your skin"* — the rooftop, the field, the bonnet, three cuts on the beat, each on Kai in the light.
63. *"And I'm falling all over again"* — the two of them dancing badly on the rooftop, arms out, handheld, wide.
64. *"Every day the sun goes down"* — the sun a red half-disc on the skyline, wide, static.
65. *"And every day I let you in"* — Kai spinning her under his arm on the roof, the car behind, slow motion.
66. *"Golden hour on your skin"* — reuse shot 17, the hand on the forearm, warmer.
67. *"Every line and every grin"* — Mahima raising her phone and, for the first time, taking the photo on purpose, the shutter, close-up on her thumb.
68. *"I've loved you in the dark, I've loved you in the noon"* — a quick warm stack: the kitchen at night and the supermarket at noon, but this time she's looking at him in both, then gold.
69. *"But nothing hits like you at half past seven in June"* — Kai's grin at the camera she's holding, straight down the lens, the flare, slow motion.
70. *"Golden hour on your skin"* — a wide from behind of both of them at the rooftop edge, the sun going, their shadows long.
71. *"And I'm falling all over again"* — Mahima leaning her head on his shoulder, eyes closed, the very last gold on her face, close-up.

### Post-chorus — the photo

72. *"Falling, falling, all over again"* — Mahima directing Kai into the light with her hands, him obeying and laughing, medium, handheld.
73. *"Falling, falling, all over again"* — him standing still where she put him, chin up, grinning, the sun square on his face, medium.
74. *"Turn your face into the light, don't move"* — her holding the phone up, framing him, extreme close-up on her eye past the phone.
75. *"Let me keep this one of you"* — the photo taken: a held still of Kai in the light (composited onto the phone screen in the edit), then cut to the real him, blinking, laughing. Hold.

### Outro — blue hour

76. *"The sun's gone under, the sky's gone blue"* — the rooftop after sunset, the sky gone blue, the skyline dark, wide, slow drift.
77. *"Streetlights blinking on, nothing left to do"* — the streetlights in the city below blinking on one by one, the two of them sitting on the bonnet with his arm around her, wide from behind.
78. *"But you're still glowing like the sun forgot to leave"* — a close-up of Kai's face in the blue, still warm, as if lit from inside, slow push-in.
79. *"Guess I carry golden hour with me"* — final shot: Mahima's phone in her lap showing the golden photo (composited), the only gold left in the frame, then her looking up from it at the real him and smiling, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "golden hour on your skin", the
two flashes inside each chorus, the instrumental, the grey-to-gold cut in
the bridge, the shutter on shot 67, and the final "with me." At 96 BPM a
bar is 2.5 s; the choruses cut on the bar, the verses hold two.

**The golden-hour challenge.** Post the vertical cut of chorus 1 (shots
17–26) with *"golden hour on your skin"* on screen and invite people to
film the person they love at the same twenty minutes every day for a week,
cut on the hook. The post-chorus photo (shot 75) is the second shareable
frame, and *"golden hour's just the hour I remember to look at you"* is the
caption.

## 6. Quality-control checklist

- Three looks in the right sections: rooftop look for intro, verse 1, chorus 1, the bridge turn, final chorus and outro; field look with the dandelion crown from shot 27 to shot 53; grey jumper only in shots 54–57
- Kai's freckles and side-lighting consistent in every gold shot; he is never lit flat except in the two deliberate flashes
- The whole video is golden except the four allowed breaks: the dark/noon flashes, the grey winter, and blue hour from shot 76
- The phone is raised and lowered without a photo until shot 67; the photo exists only from shot 67 on
- The phone screen and the final photo are composited; no model-generated text or UI
- Lens flare on every hook line, film grain on every frame, no clean digital-looking shot anywhere
- No distorted hands, especially the dandelion weaving and the phone close-ups
- The last shot is locked-off and holds until the audio fades
