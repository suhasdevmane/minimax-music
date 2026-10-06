# Wan 2.2 Shot List — "Blocked and Blooming"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
108 BPM a bar is 2.22 s, so most shots run 3–5 s and the choruses cut on the
half-bar where the log drums land.

## 1. Visual style

One small apartment across five months. **The room is the calendar**: in
December it is grey, bare and cold-lit with the blinds down; by May it is a
jungle with every window open. Nothing in the video announces the passage of
time except the amount of green in frame and how high the sun sits on the
wall. Shoot it like a real flat — practical light, a rusty balcony rail,
mismatched pots, one bad chair. Handheld and close in the verses, wider and
freer in the choruses.

| Section | Grade | Camera |
|---|---|---|
| Intro (December) | Flat blue-grey, low winter sun, desaturated | Static, close |
| Verse 1 | Cold daylight with one warm interior lamp | Handheld, working close-ups |
| Pre-choruses | Each cut a step warmer than the last | Locked-off match cuts |
| Choruses | Full warm gold and saturated green | Loose handheld, moving with her |
| Verse 2 (March) | Bright spring daylight, high contrast | Handheld, street energy |
| Instrumental | Golden into blue hour and back | Macro and slow wides |
| Bridge | One lamp, deep shadow, fridge light | Static, unflattering, honest |
| Final chorus / post-chorus | Brightest in the video, doors open | Wide, moving, people in frame |
| Outro (May) | Clean May morning, no filter | Slow, calm, mirrored to the intro |

## 2. Character bible — paste into every prompt

**Mahima** (December)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and unbrushed, no makeup, wearing a grey oversized cardigan over a plain white t-shirt and thick socks, tired flat expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the growing months, verses and choruses)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied up in a messy knot with a scarf, no makeup, wearing a faded olive work shirt with rolled sleeves and denim shorts, soil on her hands and forearms, absorbed focused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (final chorus and outro, May)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and shining, light natural makeup, wearing a soft yellow linen dress and bare feet, open relaxed expression, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — never seen at all in this video, not even as a hand. He exists
only as a name on a locked phone screen in shot 1, and the screen is
composited.

**His friend** (verse 2) — faceless. Shot from behind, or cropped at the
chin, or in soft focus over her shoulder.
> a young man in his twenties, back to camera or face out of frame, dark jacket, holding a paper bag of fruit

**The two friends** (final chorus) — two young women, casual spring clothes,
carrying plant pots. Faces fine, they are on her side.

**The grey cat** — the same short-haired grey cat every time: verse 1 on the
balcony chair, the second chorus asleep in a sunbeam, and the last shot. It
is the running joke; keep it consistent.

Objects that must stay continuous: the **rusty balcony rail**, the **basil in
a chipped mug**, the **jam jar of cuttings** on the sill, the **library
book**, the **young fig tree in a plastic nursery pot**, the **watering can**,
the **one bad balcony chair**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the block confirmation, the library book's printed page and
any shop signage are composited in the edit.** Generate the phone as a lit
blank rectangle and the book as an open blank spread, then overlay in post —
the model cannot render legible text, and the one screen in this video has to
read cleanly in half a second.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
friend's reference deliberately faceless. Keyframes first; OpenPose for the
dancing and the carrying shots; Depth for the balcony and the crowded
interiors, which the model otherwise flattens. 16:9 first; 9:16 for the
chorus and post-chorus cuts, which are the shareable ones. Animate
conservatively: water pouring, leaves moving in a draught, a hand pressing
soil, hair lifting when the window opens.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s. Growth is achieved in the edit by cutting between separately
dressed set states, never by generative morphing — the model will not grow a
plant convincingly.

## 4. Scene per lyric line

### Intro — December

1. *"December, and my thumb was on your name"* — extreme macro of a thumb resting motionless on a phone screen (UI composited: a contact card), the skin cold-lit, no movement for two full seconds, static.
2. *"One little button and the noise went away"* — the thumb presses once, the screen dims, and the room tone drops out; pull back to reveal the phone face-down on a bare table, static.
3. *"No last speech, no argument, no scene"* — wide of the whole grey apartment, blinds down, one chair, nothing on the walls, Mahima (December look) small in the frame, locked-off.
4. *"Just a quiet little room and a girl and a screen"* — her sitting on the edge of the bed with her hands in her lap, not looking at the phone, medium, flat cold light.
5. *"I didn't cry, I just opened a blind"* — her hand pulling a blind cord, the slats tilting, a hard bar of winter light crossing the room, close-up.
6. *"And let the cold light in for the first time"* — her face in that bar of light, eyes closing once against the brightness, close-up, blue-grey grade.

### Verse 1 — soil, pots, the first thing that stays

7. *"Bag of soil on a Saturday morning"* — a garden shop counter, her shouldering a heavy bag of compost, the weight visible in her shoulder, medium, cold daylight.
8. *"Three flights up with the sun coming warm in"* — a stairwell, her climbing with the bag, stopping on a landing to breathe and laughing at herself, handheld from above.
9. *"Terracotta pots and a secondhand rail"* — mismatched terracotta pots being wedged onto a rusty balcony rail, her hands testing that they hold, close-up.
10. *"Basil in a mug and a mint that won't fail"* — a chipped mug of basil and a tin of mint set on the windowsill, she turns them both to face the light, close-up.
11. *"Cuttings in a jam jar, roots like white thread"* — macro through the glass of a jam jar, white roots suspended in water, light refracting, almost still.
12. *"Something in this apartment is finally getting fed"* — her filling a watering can at the kitchen sink, the tap loud, steam on the window, medium.
13. *"The neighbour's grey cat comes and sits on my chair"* — the grey cat jumping onto the one balcony chair and settling like it owns it, static wide from inside through the glass.
14. *"First thing since December that showed up and cared"* — her watching the cat for a long beat, then quietly moving her cup so it can stay, close-up, the first small real smile of the video.

### Pre-chorus 1 — a season, and what she did with it

15. *"They told me give it a season, give it time"* — a locked-off frame of one pot on the sill, three quick match cuts on the beat: January bare, February a shoot, March four leaves.
16. *"So I gave it water and a place in the light"* — her hand lifting a pot out of shade and setting it in the sun, the light climbing her forearm, close-up.
17. *"Now the balcony's greener than the day that you left"* — the balcony from outside, pulling back: the rail now half covered, a step warmer in grade than shot 9.
18. *"And nothing out here has asked about you yet"* — her at the balcony door with a mug, looking out, entirely unbothered, medium, warm.

### Chorus 1 — the hook

19. *"Blocked and blooming, look at me now"* — Mahima (growing look) barefoot between pots with the watering can, walking straight at camera, handheld, saturated gold and green.
20. *"Dirt on my hands and a sun in the house"* — her hands held open to camera, soil in every crease, sun across the palms, extreme close-up. **The hook frame.**
21. *"You were a winter I finally survived"* — a fast flash of the grey December wide (shot 3), then a hard cut back to the green room, the same angle.
22. *"Now every window in here is alive"* — a slow pan across every windowsill in the flat, each one crowded, curtains moving, wide.
23. *"Blocked and blooming, I water the light"* — water arcing from the can into a pot, catching the sun, slow motion for one beat, macro.
24. *"Everything green that I grew out of spite"* — her looking straight down the lens with one eyebrow up, a plant filling the frame beside her face, medium close-up.
25. *"Call it a garden, call it a crown"* — low angle from the floor looking up: leaves arching over her head like a headdress, her chin lifting.
26. *"Blocked and blooming, look at me now"* — wide from outside the building: the whole balcony green, one woman in the middle of it, arms loose, drone-style slow pull back.

### Verse 2 — March, the window open, his friend

27. *"March came in and I opened the whole window"* — both window panels pushed wide at once, curtains and her hair lifting in the draught, medium, bright.
28. *"Bougainvillea leaning pink on the road below"* — from the street looking up: pink bougainvillea spilling over the rail toward the pavement, low angle, high contrast.
29. *"Learned the names from a book at the library"* — her cross-legged on the floor with an open book (blank spread, text composited), mouthing a long name, close-up.
30. *"Learned which ones wilt when you love them too heavy"* — a yellowed leaf lifted off a stem, then her tipping standing water out of a saucer, a small frown, macro.
31. *"Ran into your friend by the fruit stand on Sunday"* — a Sunday market, her at a fruit stall with a fig tree in a nursery pot on her hip, handheld.
32. *"Said that you'd been asking how I was doing lately"* — the faceless friend stopping in front of her mid-sentence, shot from behind his shoulder, her face open and polite.
33. *"I had dirt on my knuckles and a fig on my hip"* — extreme close-up of her knuckles gripping the pot, dirt in the creases, the fig leaves brushing her jaw.
34. *"Both hands were full and I liked it like this"* — she shifts the tree, says something short, and walks out of frame before he has finished, tracking, market colour everywhere.

### Pre-chorus 2 — the flat is hers

35. *"They told me give it a season, give it time"* — the same locked-off sill frame from shot 15, now overflowing, one hard cut, no montage.
36. *"So I gave it water and a place in the light"* — her carrying the fig tree in through the front door and setting it down where the sun lands, wide.
37. *"Now the whole place smells like something that grew"* — crushed mint between her fingers held up near the lens, her eyes closing, macro.
38. *"And not one single leaf in here is for you"* — slow pan across the room: every surface growing something, ending on her looking back at camera, late gold.

### Chorus 2 — fuller

39. *"Blocked and blooming, look at me now"* — reuse the walk-at-camera framing of shot 19, now with the window open and street sound in, busier background.
40. *"Dirt on my hands and a sun in the house"* — reuse shot 20, tighter, one hand only, a ring back on her finger that was bare in December.
41. *"You were a winter I finally survived"* — the grey cat asleep in a sunbeam among the pots, one ear flicking, static macro.
42. *"Now every window in here is alive"* — from outside on the street at eye level: the open window above, leaves moving, her passing across it once.
43. *"Blocked and blooming, I water the light"* — her feet on the tile between pots, moving on the beat, water spots drying on the floor, low static.
44. *"Everything green that I grew out of spite"* — her spinning a pot to show its best side and setting it front and centre, close-up, small satisfied nod.
45. *"Call it a garden, call it a crown"* — reuse shot 25's low angle, wider, more leaves, string lights now strung across the balcony unlit.
46. *"Blocked and blooming, look at me now"* — she pulls the balcony door shut behind her from the inside and leans on it, framed by green, medium, holding into the break.

### Instrumental — the growing montage, no lyrics

47. Macro: a seedling breaking the surface of dark soil, the crust lifting, almost still, golden light.
48. Water hitting dry earth and darkening it in a spreading ring, macro, slow motion.
49. Her repotting something outgrown, both hands deep in compost, pushing soil down around the root ball, close-up, forearms working.
50. Her asleep on the sofa in daylight, the library book face-down on her chest, plants all around, slow wide, dust in the light.
51. The balcony at dusk from the street, pots silhouetted, one string light coming on — the cut into the bridge.

### Bridge — the honest part

52. *"I thought the block button was the end of the story"* — night, her sitting on the kitchen counter, one lamp, deep shadow, static, unflattering.
53. *"Turns out it was only the ground cracking open"* — macro of soil in a glass-sided pot, roots visibly threading down through the layers, lamp light only.
54. *"Some love is a drought that you walk away thirsty"* — a cracked dry pot on the floor with nothing in it, dust, close-up, the coldest frame since the intro.
55. *"Some love is the rain that you're owed and get late"* — rain starting on the balcony behind glass, the pots taking it, her silhouette watching, static wide.
56. *"I won't pretend that I did all of it pretty"* — her eating cereal out of the box lit by the open fridge, no makeup, flat expression, medium.
57. *"There were weeks I ate cereal standing at the sink"* — the same, from behind, her shoulders low, the sink full of unwashed mugs, static.
58. *"But under the dirt the small roots kept working"* — back to the glass-sided pot, push in until the roots fill the frame, macro, warm.
59. *"Quiet as anything, further than you think"* — her hand pressing flat onto the surface of the soil, holding, then lifting away — the cut into the final chorus.

### Final chorus — doors open, people arriving

60. *"Blocked and blooming, look at me now"* — Mahima (May look, yellow linen, hair down) opening the front door to two friends carrying more pots, bright, wide.
61. *"Green on the railing and the door swinging out"* — the balcony door swinging fully open on its own weight, green flooding into the frame, low angle.
62. *"You were a winter I finally survived"* — a last two-second flash of the December wide, then the same angle now unrecognisable, hard match cut.
63. *"Now every window in here is alive"* — every window in the flat open at once, curtains and leaves all moving, slow pan, brightest grade in the video.
64. *"Blocked and blooming, I water the light"* — one friend watering while Mahima directs her, both laughing, handheld, natural.
65. *"Everything golden that I grew out of spite"* — her handing over a jam jar of rooted cuttings for a friend to take home, close-up on the exchange.
66. *"Call it a garden, call it a crown"* — the low angle again, this time with all three women under the arching leaves, wide.
67. *"Blocked and blooming, look at me now"* — from the hallway looking in through the open front door: green, light, people, music — she glances back at camera once.

### Post-chorus — the kitchen party

68. *"Look at me now, look at me now"* — bare feet on tile between pots, moving on the beat, cut on every clap, low static.
69. *"Feet on the tile and the speaker turned loud"* — a small speaker on the counter beside the basil mug, the mug visibly buzzing, macro.
70. *"Look at me now, look at me now"* — three pairs of hands clapping in the green room, mid-shot, motion blur.
71. *"Everything I planted in the cold came round"* — her spinning once with her arms out and knocking a hanging plant, everyone laughing, handheld.
72. *"Look at me now, look at me now"* — the balcony from outside at night, string lights lit, silhouettes moving among the leaves, static wide.
73. *"Blocked and blooming and I'm never coming down"* — her leaning on the rail with a drink, city behind, looking up rather than out, medium.

### Outro — May morning

74. *"December, and my thumb was on your name"* — the exact frame of shot 1 recreated: the same table, the same phone, face-down, untouched, now with leaves crowding the edges, macro.
75. *"That one little button and the noise went away"* — her hand entering frame, picking the phone up without looking at it, and dropping it in a bag, close-up.
76. *"Now it's May and the balcony's a jungle in the sun"* — the exact frame of shot 5 recreated: the same blind, the same window, now blazing green — her hand opening it wider, close-up.
77. *"Blocked and blooming, and the growing's just begun"* — final shot: the balcony from outside, overgrown, the grey cat on the chair, Mahima stepping out with a coffee and sitting down beside it, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the button press, the first log-drum entry in verse 1, each
*"blocked and blooming"*, the fig-tree walk-off, the instrumental, *"under the
dirt the small roots kept working"*, the door swinging open, and the final
sit-down. At 108 BPM a bar is 2.22 s; the choruses cut on the half-bar where
the log drums land, the post-chorus cuts on every clap.

**The December-to-May challenge.** Shots 3, 5, 62 and 76 are built as exact
frame pairs. Post the vertical cut of chorus one (shots 19–26) with
*"blocked and blooming"* on screen and invite people to film the same corner
of their own room the week they blocked someone and again five months later,
cutting on the hook. The hands-full-of-soil frame (shot 20) is the second
shareable still.

## 6. Quality-control checklist

- Three looks in the right sections: grey cardigan only in the intro, olive work shirt through the verses and choruses, yellow linen from shot 60 on
- The ex is never shown, not even a hand — the only trace of him is the composited contact card in shot 1
- His friend at the market has no visible face
- The grey cat appears exactly three times: shots 13, 41 and 77, and is the same cat
- Green increases monotonically: no shot after the intro has fewer plants than the shot before it, except the two deliberate December flashbacks and the dry pot in the bridge
- The four mirrored frame pairs match on lens, height and angle: 1/74, 3/62, 5/76, 9/17
- All screens and printed pages composited; no model-generated text anywhere
- No distorted hands in the soil and watering close-ups, which are half the video
- The last shot is locked-off and holds until the audio fades
