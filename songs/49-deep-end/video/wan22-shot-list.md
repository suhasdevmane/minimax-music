# Wan 2.2 Shot List — "Deep End"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
124 BPM a bar is 1.94 s, so most shots are 2–4 s, the choruses cut on the bar
and the post-choruses cut on the chopped vocal.

## 1. Visual style

One rooftop pool, one evening, and the light changes hands exactly once. The
first third is **gold**: low direct sun sliding down a glass tower, hot tile,
long shadows, everything above the water lit. Then the underwater lights come
on in the first pre-chorus and from that moment **the pool is the only light
source in the video** — faces lit from below, neon on the parapet, the sky
violet and then black. Half the shots after the dive are underwater. The
water is the subject, not the backdrop.

| Section | Grade | Camera |
|---|---|---|
| Intro | Hard gold on water, deep shadow on tile | Slow drift, static wides |
| Verse 1 | Gold going amber, lit from above | Lateral track at chest height, drone straight down |
| Pre-chorus | The switch: everything above the water drops out | Static, macro on hands and feet |
| Choruses | Pool blue, pink and blue neon, violet sky | Wide on the drop, water-level slow motion |
| Post-chorus | Hard neon, high contrast, wet skin | Four rhythmic cuts |
| Verse 2 | Neon from the side, blue from below | Close two-shot, macro objects |
| Instrumental | Blue and bubbles, then one wide city frame | Underwater, then a drone rise |
| Bridge | Pool light only, her face the brightest thing | Overhead, floating, static |
| Final chorus | Peak neon, the brightest frame | Wide of a full pool, treading-water two-shot |
| Outro | Neon switching off in sections | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (before the dive)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned up immaculately with gold pins, polished makeup and gold hoop earrings, wearing a black one-piece swimsuit under an open silk shirt and gold sandals, composed watchful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (after the dive)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wet hair pushed straight back off her face, makeup gone, wearing a black one-piece swimsuit, neon reflecting on wet skin, open alive expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing dark swim shorts with a white towel over one shoulder, calm unhurried expression, realistic cinematic photography, consistent identity

**The party** — forty people of mixed ages in swimwear and party clothes,
clustered in the shallow third of the pool for the first half of the video and
in all of it by the last chorus. Faces are fine; nobody here is an ex and
nobody is faceless.

Objects that must stay consistent: her **gold hair pins**, the **gold hoop
earrings** dropped into a folded towel, the **glass set down on hot tile**
with its condensation ring, the **white towel** over Kai's shoulder and later
round her own, the **row of abandoned phones** along the pool edge.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the neon signage on the parapet and any hotel or bar
lettering are composited in the edit.** Generate phones as lit blank
rectangles and the neon as abstract shapes and lines with no readable words.

Keep this PG-13 throughout: swimwear is ordinary and unfussy, framing is never
leering, and the two leads never get closer than treading water an arm's
length apart. The charge of this video is the decision, not the contact.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA — the wet look
is the harder one and needs its own reference set — and lock Kai separately.
**Water is the technical risk in this video.** Generate splashes, the dive and
the surfacing as short bursts of 2 s and extend them in the edit; do not ask
for five seconds of continuous water. Underwater shots want soft caustic light
baked into the still before animation, and hair underwater should be generated
in a floating pose rather than animated into one. OpenPose for the dive, the
surfacing and the floating overhead shot. Depth for the wides so the deep end
reads as deeper. 16:9 first; 9:16 recomposition for the dive and the chopped
post-chorus, which are the vertical clips.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–4 s; post-chorus shots 1–2 s; the dive is 2 s generated and
retimed to 4 s in the edit.

## 4. Scene per lyric line

### Intro — gold hour

1. *"Sun coming down the side of the building like it's pouring"* — the sun sliding down the face of a glass tower and hitting the pool surface, the whole thing going gold, slow drift.
2. *"Turning the whole pool the color of a coin"* — the water surface filling the frame, hammered gold, one leaf turning on it, macro.
3. *"Everybody's on the edge with their feet in and their phones out"* — a row of feet along the pool edge at ankle depth, phones up above them, lateral track.
4. *"Nobody in past the second step"* — a drone straight down: bodies clustered in the shallow third, the deep end empty and a darker blue.
5. *"I've been the queen of the second step"* — Mahima on a sun lounger at the edge, immaculate, phone face-down, glass in hand, not in the water, medium.

### Verse 1 — the party, catalogued

6. *"Seven o'clock and the tiles are still warm from the sun"* — bare feet crossing hot tile, heat shimmer just above it, low macro.
7. *"Half the city down below us and the evening just begun"* — from the parapet: the city grid far below, sun low across it, wide.
8. *"Forty people in the shallow end with glasses at their chins"* — a slow lateral track along the shallow end at chest height, every glass held above the waterline.
9. *"Nobody's hair is wet, and nobody goes in"* — a static wide of the pool: the shallow end crowded, the deep end perfectly still and untouched.
10. *"I have been that girl for two whole summers, careful, dry"* — Mahima adjusting a gold pin in her hair with two fingers, macro on the pins, precise.
11. *"Perfect hair, perfect distance, perfect lie"* — her reflection in the still water at the edge, composed, then a ripple crossing it.
12. *"Then you came up the steps at the far end of the blue"* — Kai coming up the roof stairs at the far end, towel over one shoulder, backlit by the last of the sun.
13. *"And you didn't look away, and neither did I"* — a shot-reverse across the length of the pool, both of them holding it, the water between them.

### Pre-chorus 1 — the lights come on

14. *"Somebody turned the lights on underneath the water"* — the underwater pool lights coming on all at once, the surface going electric blue, everything above it dropping into shadow.
15. *"The whole roof went quiet and the whole pool went blue"* — a wide of the whole roof in the new light: forty faces lit from below, nobody talking.
16. *"I've got one shoe off and one hand on the rail"* — one gold sandal pushed off a heel; a hand closing on the pool rail, two macro cuts.
17. *"And the drop is only six feet, so"* — her point of view straight down into the deep end, the tiled bottom visible through blue, no motion at all in the frame.

### Chorus 1 — the drop

18. *"Meet me at the deep end, I'm done with wading in"* — the drop lands on a wide of the whole roof: neon on the parapet coming up, everyone turning toward the water.
19. *"Standing in the shallow with a glass up to my chin"* — one glass held at chin height in the shallow end, lowered slowly out of frame, macro.
20. *"Six feet of nothing underneath and neon on the blue"* — underwater, looking up at the surface from six feet down, legs and neon and city glow above it.
21. *"Count me down from three and I'll come up looking at you"* — Kai in the deep end already, treading water, looking back at the edge, medium.
22. *"Meet me at the deep end, I'm done with wading in"* — the party starting to move: people setting drinks down along the edge, from a low angle.
23. *"Everybody's careful, I've been careful for a while"* — a row of abandoned phones and glasses along the tile, macro tracking along them.
24. *"So kick the whole year off and let it sink under the tile"* — a gold sandal kicked away across the tile, spinning, landing on its side.
25. *"Meet me at the deep end, I'm going in"* — her at the deep end edge, toes over it, arms loose, the neon behind her, wide, held.

### Post-chorus 1 — chopped hook

26. *"Deep end, deep end, water going gold to blue"* — a hair tie pulled out and hair dropping, one second.
27. *"Deep end, deep end, I am not staying dry for you"* — a flat palm hitting the water surface, macro, the splash frozen at its peak.
28. *"Deep end, deep end, hair down and hands up high"* — the underwater light strobing through moving water, abstract, one second.
29. *"Deep end, deep end, meet me at the deep end"* — a wide of the pool with the whole crowd's hands up, neon at full.

### Verse 2 — the conversation

30. *"You asked me what I'm waiting for, I said I've got a fear"* — the two of them at the rail with the city behind, close two-shot, party out of focus.
31. *"The last one left me sitting on an edge for half a year"* — her alone in the frame now, arms folded, looking at the water rather than at him.
32. *"You said the shallow end is where the loud ones stay"* — Kai, close, saying it lightly, no weight on it, then looking away first.
33. *"Then you turned around and walked the other way"* — Kai walking away along the pool edge toward the deep end, unhurried, not looking back, tracking behind.
34. *"Somebody laughed and somebody held a phone up in the air"* — the crowd noticing something is happening, phones going up, from her point of view.
35. *"I put my glass down on the tile and pulled the pins out of my hair"* — a glass set down on hot tile, condensation ring spreading, then pins coming out one at a time.
36. *"Two whole summers keeping every single thing in reach"* — gold earrings dropped into a folded white towel, macro, deliberate.
37. *"Gone in about the time it takes to breathe"* — her face, one breath in, eyes closing, close-up, pool light from below.

### Pre-chorus 2 — the whole roof watching

38. *"Everybody's phone is up, the underwater lights are on"* — forty phones up in a ring around the pool, small lights, from her position at the deep end.
39. *"The whole roof went quiet and the whole pool went blue"* — a static wide of the entire roof holding still, nobody moving, the water flat.
40. *"I've got both shoes off now and no hand on the rail"* — her feet on the tile edge, toes over it, nothing in her hands, low macro.
41. *"And the drop is only six feet, so"* — her face, straight to camera height, no music left in the mix, absolutely still, held to the last frame.

### Chorus 2 — the dive

42. *"Meet me at the deep end, I'm done with wading in"* — the dive: one slow-motion shot from water level, the surface breaking, neon shattering across it.
43. *"Standing in the shallow with a glass up to my chin"* — underwater, following her down, hair up around her, bubbles trailing.
44. *"Six feet of nothing underneath and neon on the blue"* — the tiled bottom from very close, her hand touching it and pushing off.
45. *"Count me down from three and I'll come up looking at you"* — her turning back toward the light and rising, shot from above the surface looking down.
46. *"Meet me at the deep end, I'm done with wading in"* — the surface breaking as she comes up, hair pushed back with both hands, water off her face, slow motion.
47. *"Everybody's careful, I've been careful for a while"* — the crowd at the edge reacting, phones and open mouths, wide.
48. *"So kick the whole year off and let it sink under the tile"* — a sunk gold pin lying on the tiled floor of the pool, macro, light moving over it.
49. *"Meet me at the deep end, I'm going in"* — her treading water in the middle of the deep end, alone in the frame, neon behind, wide.

### Instrumental — everyone in

50. The rest of the party going in after her, one at a time and then all at once, wide from the far end.
51. Legs and bubbles from directly below, twenty bodies entering the water, abstract and blue.
52. Two people helping an older guest down the steps into the water, laughing, medium.
53. A slow drone rise off the roof: one lit blue rectangle in an enormous dark city, the only wide of the city in the video.
54. Back down through the build to a tight shot of her face at the surface, breathing, waiting for the drop.

### Bridge — floating

55. *"I've spent a long time with my feet on solid ground"* — her floating on her back in the middle of the pool, ears under, shot from directly above, the party gone from the sound.
56. *"Reading every room before I ever made a sound"* — the same overhead, wider, the crowd visible only as movement at the edges of the frame.
57. *"The shallow end is safe and it is boring and it's small"* — the shallow end from underwater, feet standing still on tile, nothing happening.
58. *"And I have been so careful that I hardly lived at all"* — her face at water level in profile, ear submerged, one eye open, extreme close-up.
59. *"So if this is a mistake, then it's a mistake I choose"* — her righting herself in the water and standing where she can, water to her shoulders, looking up.
60. *"And I'd rather be the girl who jumped than the girl who didn't move"* — the deep end from her eyeline, neon reflecting, and she pushes off toward it.

### Final chorus — the whole roof in the water

61. *"Meet me at the deep end, I'm done with wading in"* — a wide of a pool with forty people in it, every phone abandoned along the edge.
62. *"Hair already ruined and there's neon on my skin"* — her face and shoulders, wet, neon across them, close-up, the brightest frame of the video.
63. *"Six feet of nothing underneath and neon on the blue"* — underwater again, the crowd's legs and light, alive and chaotic.
64. *"Count me down from three and I'll come up looking at you"* — the two of them treading water an arm's length apart, talking, the party going on around them.
65. *"Meet me at the deep end, I'm done with wading in"* — a lateral track along the pool edge past abandoned shoes, glasses and phones, all of it left behind.
66. *"Everybody's in the water and there's nobody left dry"* — a drone straight down on a full pool, the reverse of shot 4, the deep end the busiest part.
67. *"The whole roof going under and the whole year going by"* — forty people going under at the same time on the beat, wide, then the surface closing.
68. *"Meet me at the deep end, I'm going in"* — her in the middle of it all, arms out, head back, neon and water, the hero frame.

### Post-chorus 2 — filtering away

69. *"Deep end, deep end, water going gold to blue"* — the pool from the far corner, half as many people, softer light.
70. *"Deep end, deep end, I am not staying dry for you"* — someone getting out and wrapping up in a towel, steam off shoulders, medium.
71. *"Deep end, deep end, hair down and hands up high"* — the neon on the parapet switching off one section at a time, wide.
72. *"Deep end, deep end, meet me at the deep end"* — the water surface settling, the movement going out of it, macro.

### Outro — the end of the night

73. *"Wet hair on a rooftop with a towel round my shoulders"* — her on a lounger with the white towel round her shoulders, hair flat and wet, no makeup left, medium.
74. *"City carrying on below us like it always does"* — the city grid below, indifferent and enormous, from her eyeline, wide.
75. *"You said, what took you so long, and I said, nothing, I'm here"* — Kai sitting down on the next lounger, a metre away, both looking out rather than at each other, two-shot.
76. *"Meet me at the deep end, I'm already in"* — final shot: the empty pool still lit, the surface flat, one towel and one glass at the edge, locked-off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the underwater lights coming on, each *"meet me at the deep end"*,
the drop at shot 18, the silent last bar of the second pre-chorus, the dive at
shot 42, the drone rise, *"the girl who didn't move"*, the final drop, and the
last neon switching off. At 124 BPM a bar is 1.94 s; the choruses cut on the
bar and the chopped post-choruses cut on the vocal stutters.

**The dive clip.** Shots 41–46 are the shareable unit: the silent held frame,
then the dive at water level with the neon shattering, then the surfacing.
Vertical, hook on screen at the drop. Second clip: shots 8–9, the whole party
holding glasses at their chins with nobody's hair wet — the joke reads in two
seconds and everyone recognises the room. Third: shots 4 and 66 back to back,
the same drone frame empty and full.

**Caption:** *"I'd rather be the girl who jumped than the girl who didn't
move."*

## 6. Quality-control checklist

- The light hands over exactly once, at shot 14, and never goes back: gold above the water before it, pool-blue from below after it.
- Mahima is in the pinned-hair look for shots 1–41 and the wet look from shot 42 on; the two never appear in the same section.
- Kai is present but never crowding: he and Mahima are never closer than an arm's length, and there is no kiss in this video.
- The gold pins, the hoop earrings in the folded towel, the glass with its condensation ring and the white towel are identical wherever they recur.
- Shots 4 and 66 are the same drone framing, empty deep end and full, and must match exactly.
- Water shots are generated as short bursts and retimed; no shot asks the model for more than two seconds of continuous water motion.
- No readable text anywhere: phone screens and all neon signage are composited as abstract shapes.
- Swimwear and framing stay ordinary and unleering throughout; the charge is in the decision.
- The last shot is locked-off on the empty lit pool and holds until the audio fades.
