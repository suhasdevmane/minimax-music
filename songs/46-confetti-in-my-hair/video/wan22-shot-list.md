# Wan 2.2 Shot List — "Confetti in My Hair"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
126 BPM a bar is 1.9 s, so most shots are 2–4 s and the choruses cut on the
bar.

## 1. Visual style

Two grades and one apartment. The **morning** is flat, hard, unforgiving
daylight — blown-out windows, no fill, everything a little too honest, and it
is where four fifths of the video lives. The **party**, which appears only in
verse two and the second chorus, is warm tungsten and string lights, over-lit
in the middle, dark at the edges, handheld and motion-blurred: the exact
inverse of the morning. Cutting between them should feel like two different
films. The **confetti is the motif** — in her hair, on the tile, in a
dustpan, in a shoe, and finally in a jar — and it is the only thing that
appears in both grades.

| Section | Grade | Camera |
|---|---|---|
| Intro | Hard morning sun, dust in the beam | Slow tilt, then static |
| Verse 1 | Unforgiving daylight, no fill | Locked-off wide, then macro inserts |
| Pre-chorus | Backlit kitchen, faces half silhouette | Slow lateral pan along six faces |
| Choruses | Same daylight, now an asset | Tracking through the flat, slow motion at the window |
| Post-chorus | Bright, punchy, high contrast | Four fast cuts |
| Verse 2 (party) | Warm tungsten, string lights, dark edges | Handheld inside the crowd |
| Instrumental | Late morning, softer | Static objects, one slow push-in |
| Bridge | Cool bathroom light against a warm flat | Static, mirror |
| Final chorus | Full daylight, outside for the first time | Stairwell descent, street |
| Outro | Soft low evening | Locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (morning, the whole video)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair flattened on one side and full of small gold and pink confetti, last night's smudged eye makeup, wearing an oversized black satin shirt over a vest and shorts with one sock, croaky amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the party, verse two and chorus two only)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and moving, sharp eye makeup and gloss, wearing a short green sequined slip dress, laughing open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (outro, Sunday evening)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair washed and tied back, no makeup, wearing a plain grey sweatshirt, calm settled expression, realistic cinematic photography, consistent identity

There is **no romantic male lead in this video** and no Kai. The six people
here are friends and they are shot as a unit.

**The friend who is leaving** — the second lead of the video, present in
almost every group shot and the subject of the ending.
> a young woman in her early twenties, short dark curly hair, small silver nose ring, wearing a red cardigan over a party dress in the night scenes and the same cardigan over a t-shirt with a suitcase in the morning, warm tired expression

**The other four** — a tall young man in a crumpled shirt; a young woman who
never stops tidying; a young man asleep in the bath fully clothed; a
neighbour of about fifty who came up at eleven and never left.

Objects that must stay consistent: the **paper crown** on the kitchen tile,
the **shoe in the plant pot**, the **hat on the lamp**, the **slice of cake
with one bite gone**, the **red suitcase** by the door, the **jam jar** on
the shelf.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, phone UI, the number written on her hand, the ticket and any
luggage tag are composited in the edit.** Generate the hand as clean skin and
the ticket as blank card; the model cannot render legible writing and a
garbled phone number is the first thing a viewer notices in a close-up.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA, and lock
the leaving friend separately — she must be recognisably the same person in
tungsten and in daylight, which is the hardest identity ask in this video.
Keyframes first; OpenPose for the chorus dancing and the stairwell descent
with the suitcase; Depth for the locked-off apartment wides so the depth of
the room reads. Falling confetti is best generated as a short burst and
extended in the edit rather than asked of the model for five seconds. 16:9
first; 9:16 recomposition for the window slow-motion frame and the six-faces
pan, which are the vertical clips.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; post-chorus shots 1–2 s.

## 4. Scene per lyric line

### Intro — the morning

1. *"Morning came in sideways through a curtain nobody closed"* — a slow tilt down a shaft of hard morning light through drifting dust, from the curtain gap to the floor.
2. *"Landed on a room that looks like it went ten rounds"* — the light arriving on a carpet covered in confetti, cups and streamers, static wide.
3. *"I sat up on the carpet and I felt it in my hair"* — Mahima sitting up on the floor between the sofa and the coffee table, blanket half on, hair flat on one side, medium.
4. *"Little gold and pink and silver, still there"* — extreme close-up of her hand going through her hair and coming out with three pieces of confetti on her fingers.

### Verse 1 — the inventory

5. *"Eight in the morning and the living room's a crime scene"* — a locked-off wide of the entire living room, everything visible at once, nobody moving, held.
6. *"There's a sock inside the fruit bowl and I don't know what that means"* — macro insert: a single sock draped over apples in a fruit bowl, absurd and undiscussed.
7. *"The tall one's on the sofa with a cushion on his head"* — the tall friend face-down on the sofa with a cushion over his head, one arm hanging off, static.
8. *"The quiet one is stacking paper plates instead"* — the tidying friend calmly stacking paper plates in total silence while everyone else is still asleep, medium.
9. *"There's a slice of cake with one bite gone beside the chair"* — macro on a slice of cake with a single bite out of it, fork still standing in the frosting.
10. *"And the balloons are half the height they were last night in here"* — balloons hovering at knee level around the room, sagging, drifting slightly, wide.
11. *"My mascara took the pillowcase down with it in the night"* — a black smear on a white pillowcase, macro, then her looking at it.
12. *"And I've never been so glad to see a mess in daylight"* — her face, looking around the room, a real smile arriving, close-up, sun creeping across her.

### Pre-chorus 1 — six faces

13. *"Kettle's on, and nobody is talking"* — a kettle beginning to steam on a counter, backlit by the window, macro.
14. *"Six of us just squinting at the light"* — a slow lateral pan along six faces in a row at the counter, all squinting, all holding mugs, none talking.
15. *"Somebody laughs and then everybody's laughing"* — one person's shoulders starting to shake, then the whole line going, one continuous take.
16. *"Because we all just remembered the same thing"* — a two-second cut to a dark blurred flash of the party, gone before it registers, then back to the kitchen.

### Chorus 1 — the flat starts moving

17. *"Woke up with confetti in my hair, and I don't even care"* — the hero frame: Mahima at the window, backlit, shaking her hair out, confetti coming off it in slow motion.
18. *"Sun through the curtains like it's proud of what went on in here"* — the curtains pulled fully open, the room flooding with hard light, everybody flinching and then laughing, wide.
19. *"There's a shoe in the plant and a hat on the lamp"* — a tracking move that finds a single shoe standing upright in a plant pot, then a party hat on a lampshade.
20. *"And a phone number written up the back of my hand"* — her hand turned over: a number in green felt pen up the back of it (composited), her raising an eyebrow.
21. *"Woke up with confetti in my hair, and I don't even care"* — a tracking move through the flat as all six start dancing badly in yesterday's clothes with mugs in hand.
22. *"Nobody is touching a broom in this apartment soon"* — a broom leaning against a wall, untouched, the dancing happening behind it out of focus.
23. *"Let the floor keep the evidence, let the kitchen keep the proof"* — low along the floor: confetti, a cork, a single earring, feet moving through frame.
24. *"Woke up with confetti in my hair, and I don't even care"* — all six in the middle of the room in one wide, arms up, sunlight full across them.

### Post-chorus 1 — chant

25. *"Confetti in my hair, confetti in my hair"* — confetti pulled out of hair and thrown up again, one second, hard cut.
26. *"Little bit of last night stuck to everywhere"* — the shoe lifted out of the plant pot and turned over, confetti falling out of it.
27. *"Confetti in my hair, confetti in my hair"* — the hat lifted off the lamp and put on the tidying friend's head, one second.
28. *"And I don't even care, no, I don't even care"* — six mugs raised at once in a ragged toast, wide, everybody grinning.

### Verse 2 — the party, and the reason

29. *"Rewind to about eleven when the neighbors came up too"* — hard cut to night: warm tungsten, string lights, a front door opening and neighbours coming in with bottles, handheld.
30. *"And somebody's little brother played a keyboard like he knew"* — a teenage boy at a small keyboard on the kitchen counter, surrounded by people, actually good, medium.
31. *"Someone fired the cannon early, aimed it up into the fan"* — a confetti cannon fired straight up into a spinning ceiling fan, low angle, the moment of impact.
32. *"So it snowed on us for twenty minutes longer than it planned"* — the fan flinging confetti across the whole room, slow motion wide, everyone with their faces turned up.
33. *"She was leaving in the morning for a city ten hours north"* — a red suitcase standing by the front door, half in shadow, the party going on behind it out of focus.
34. *"So we made the whole night bigger than the rest of it was worth"* — the party at its loudest: the whole room jumping, handheld, motion blur, over-lit centre.
35. *"Then we stood there in the kitchen with the big light switched off"* — the kitchen with only hallway light, six people in a circle holding on to each other, from the doorway, held long.
36. *"And nobody said goodbye out loud, we just held on a bit too long"* — the same shot continuing, nobody moving, then one hand tightening on a shoulder, close-up.

### Pre-chorus 2 — laughter and tears

37. *"Kettle's on again, still nobody's talking"* — the kettle again, matched exactly to shot 13, one more mug on the counter than before.
38. *"Six of us, and one of us is packed"* — the same lateral pan as shot 14, matched, except the leaving friend has a coat on and a suitcase at her feet.
39. *"Somebody laughs and then everybody's laughing"* — one face, one continuous take: the laugh, then the face crumpling, then the laugh again.
40. *"Then we're crying, then we're laughing, and that's that"* — the leaving friend wiping her face with the heel of her hand and immediately laughing at herself, close-up.

### Chorus 2 — joy with the clock running

41. *"Woke up with confetti in my hair, and I don't even care"* — the same tracking move as shot 21, re-blocked so the red suitcase is in the background of every part of it.
42. *"Sun through the curtains like it's proud of what went on in here"* — the window again, the light now higher and warmer, the room visibly later.
43. *"There's a shoe in the plant and a hat on the lamp"* — the shoe's owner finally reclaiming it out of the plant pot and hopping to put it on, medium.
44. *"And a phone number written up the back of my hand"* — her photographing the back of her own hand with her phone so she does not lose it (screen composited), close-up.
45. *"Woke up with confetti in my hair, and I don't even care"* — all six dancing around the suitcase rather than moving it, wide.
46. *"Nobody is touching a broom in this apartment soon"* — the dustpan with three pieces of confetti in it, abandoned mid-sweep on the floor, macro.
47. *"Let the floor keep the evidence, let the kitchen keep the proof"* — the paper crown still on the kitchen tile where it fell, feet stepping around it, low angle.
48. *"Woke up with confetti in my hair, and I don't even care"* — the six of them collapsed on and around the sofa, breathing, laughing, wide, the suitcase in frame.

### Instrumental — the clean-up that does not happen

49. The broom leaning untouched against the wall, the room out of focus behind it, static.
50. Two of them lying on the floor on their backs looking up at the ceiling fan, still turning, confetti still on the blades, overhead shot.
51. The friend asleep in the bath fully clothed with a cushion under his head, static, bathroom light.
52. A slow push-in on the red suitcase by the door, ending tight on the handle.
53. The whole living room in one late-morning wide, softer light than the opening, nobody in it.

### Bridge — the mirror

54. *"It was a year that took a lot out of all of us"* — Mahima alone in the bathroom doorway looking at herself in the mirror, confetti still in her hair, not moving, static.
55. *"A bad spring and a worse July"* — her reflection only, held, the flat warm and out of focus behind her in the glass.
56. *"Last night was the first night in a long time"* — over-the-shoulder into the mirror as her expression changes, a small honest smile.
57. *"That nobody in this room had to try"* — through the doorway behind her reflection: the others visible in the flat, moving, unaware.
58. *"So I'm not sweeping yet and I'm not washing out my hair"* — her hand on the tap, not turning it, macro, then pulling away.
59. *"I'll keep the whole night on me for as long as it will stay"* — her walking out of frame and leaving the bathroom light on, the empty mirror held one beat.

### Final chorus — the send-off

60. *"Woke up with confetti in my hair, and I don't even care"* — all six carrying the suitcase down the stairwell together, badly, laughing, camera going down ahead of them.
61. *"Sun through the curtains like it's proud of what went on in here"* — a stairwell window blowing out white as they pass it, silhouettes and confetti in the air.
62. *"There's a shoe in the plant and a hat on the lamp"* — a quick cut back to the empty flat: the shoe and the hat exactly where they were, nobody home.
63. *"And her ticket folded up where her jacket used to hang"* — a folded ticket on the hook by the door where a coat used to be (composited), macro, the hook otherwise empty.
64. *"Woke up with confetti in my hair, and I don't even care"* — the street outside: full daylight for the first time in the video, a car door open, all six on the pavement.
65. *"We will clean it up tomorrow or we won't, and that's the truth"* — a hug that lasts a beat too long, two-shot, confetti coming off a collar onto the pavement.
66. *"Let the floor keep the evidence, let the kitchen keep the proof"* — the car pulling away, five people in the road watching it, wide, held.
67. *"Woke up with confetti in my hair, and I don't even care"* — the five of them turning back toward the building, arms round each other, shot from behind.

### Post-chorus 2 — the stairwell

68. *"Confetti in my hair, confetti in my hair"* — five people chanting on the stairwell, one flight at a time, handheld from below.
69. *"Little bit of last night stuck to everywhere"* — a hand trailing up the bannister, confetti stuck along it, macro.
70. *"Confetti in my hair, confetti in my hair"* — the flat door opening onto the wreckage again, all five in the doorway looking at it.
71. *"And I don't even care, no, I don't even care"* — the five of them walking back in and closing the door, from inside, the room bright behind them.

### Outro — Sunday

72. *"Sweeping up on Sunday and I found one in my shoe"* — a broom finally moving across the floor, evening light, Mahima in the sweatshirt look.
73. *"Little gold circle from a night I'm not gonna lose"* — a shoe turned upside down and one gold disc falling out into her palm, macro.
74. *"Put it in a jar on the shelf beside the door"* — a jam jar on the shelf by the front door, the single piece dropped in, close-up on the jar.
75. *"Woke up with confetti in my hair, and I don't even care"* — final shot: the clean, quiet living room in low evening light with the jar on the shelf, locked-off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first tilt of light, each *"confetti in my hair"*, the hard
cut into the party at shot 29, the cannon into the fan, the kitchen circle,
the matched pan at shot 38, the stairwell descent, and the jar. At 126 BPM a
bar is 1.9 s; the choruses cut on the bar and the post-choruses on the
half-bar.

**The six-faces challenge.** Shots 13–16 are the shareable unit: a line of
friends squinting over mugs, nobody speaking, then all of them laughing at
once. It reads in three seconds and everyone has that photo. Second clip:
shot 17, the slow-motion hair shake at the window, vertical, with the hook on
screen. Third: shots 31–32, the cannon into the ceiling fan.

**Caption:** *"Let the floor keep the evidence, let the kitchen keep the
proof."*

## 6. Quality-control checklist

- Two grades only, and they never blend: morning is hard and flat, the party is warm and dark-edged. Shots 29–36 and 16 are the only night frames.
- Mahima is in the black satin shirt for shots 1–71, the green sequined dress only inside the party, and the grey sweatshirt only for shots 72–75.
- The leaving friend is recognisably the same person in tungsten and in daylight; check her face across shots 30, 35, 38 and 65 side by side.
- The paper crown, the shoe in the plant, the hat on the lamp, the cake with one bite and the red suitcase are identical wherever they recur.
- Shots 13 and 37, and shots 14 and 38, are matched frames; the only differences are the extra mug, the coat and the suitcase.
- No readable text anywhere: the number on her hand, the ticket, the luggage tag and every phone screen are composited.
- Confetti appears in both grades and in every section, and is the subject of the first and last close-ups.
- No distorted hands in the macro inserts, especially the hand with the number on it.
- The last shot is locked-off on the jar and holds until the audio fades.
