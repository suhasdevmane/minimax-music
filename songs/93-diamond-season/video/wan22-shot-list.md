# Wan 2.2 Shot List — "Diamond Season"

**One shot per lyric line**, built from the submission's per-section video
direction. At 126 BPM a bar is 1.9 s, so the choruses cut on the bar and the
drop cuts on the half-bar. Take timestamps from the rendered WAV.

## 1. Visual world

Four worlds and one physical idea: **light through glass**. A **jewellery
shop after closing** in green-white fluorescent, a **dark seam of rock** lit
by a single work lamp, a **workshop and vault** of steel and desk lamps, and
a **black-marble gala** under chandeliers. Every colour in the video except
skin tone comes from real refraction — prisms, cut glass, chandelier drops,
a champagne flute — never from gels. The bridge is the only sequence with no
refraction at all, and that absence is the point.

| Section | Grade | Camera |
|---|---|---|
| Intro | Fluorescent white, slightly green, one warm case light | Macro, static |
| Verse 1 | Staff-room fluorescent, dawn bus window, then near-black | Handheld, plain |
| Pre-choruses | Near-black, one work lamp, one white point | Tight, compressed |
| Choruses | Hard white key, real prism colour, deep black surround | Slow turns, push-ins |
| Post-chorus drop | Each cut a stop brighter than the last | Hard match cuts on the beat |
| Verse 2 (rap) | Single desk lamp, hard shadow, steel and glass | Static, exact, cold |
| Instrumental | Pure white through prism, then black, then everything | Locked off, then faces |
| Bridge | One fluorescent strip and the case light, no refraction | Still, wide, unglamorous |
| Final chorus | Every prism firing, chandelier white on black marble | Widest of the video |
| Outro | Fluorescent white and one warm case light | The intro framings repeated |

## 2. Character bible — paste into every prompt

**Mahima** (the shop and the seam — night shift)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back in a practical low ponytail, no makeup, wearing a plain navy staff polo shirt and dark trousers with a name badge, a soft cloth in one hand, tired steady expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (workshop and vault, the rapped verse)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled into a sleek low knot, sharp minimal makeup, wearing a charcoal tailored suit with a white shirt open at the collar, a jeweller's loupe in one hand, cool exact expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (gala, choruses and bridge)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and glossy with a deep side part, luminous makeup, wearing a floor-length black column gown with no jewellery at all, bare shoulders, composed radiant expression, realistic cinematic photography, consistent identity, natural skin texture

**The new girl** (outro) — a young woman in the same navy staff polo behind the glass case, face visible, seventeen or eighteen, unimpressed until she looks up.

**The colleague in the doorway** (intro) — faceless: a shoulder and a bag, backlit in a half-closed shutter, never a reverse angle.

**The gala crowd** — faces visible but never featured; they exist to turn their heads. **There is no male lead in this video and no romantic thread at all.**

Objects: the **soft cloth**, the **four-Cs poster** with curling corners, the
**work lamp** in the seam, the **jeweller's loupe**, the **velvet tray**, the
**empty glass case**, the **prism**. She wears **no jewellery in any shot** —
the whole video is about the stone and she is never wearing one.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All lettering is composited in the edit** — the four-Cs poster, the name
badge, the price tickets in the case, the vault drawer labels. Generate a
blank laminated poster and blank tickets, then overlay in post; the model
cannot render legible lettering, and the four words on that poster are the
spine of both verses.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; the polo
look and the gown look must read as unmistakably the same face, because the
drop's match cuts depend on it. **Refraction is the hardest thing here**:
generate the prism, chandelier and cut-glass passes as separate real plates
and composite the spectrum in the edit rather than asking the model to
invent caustics, which it does badly. OpenPose for the staircase walk and
the slow turn under the light. Depth for the vault corridor and the rock
seam. 16:9 first; 9:16 recomposition for the drop cuts, which are the
shareable unit. Animate in short bursts: one cloth pass, one lid rising, one
tray sliding, one turn, one door opening.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — the shop after closing

1. *"Night shift, glass case, cloth in my hand"* — macro of a soft cloth moving across a glass case, the reflection of a lit ring travelling under it, fluorescent white, static.
2. *"Wiping other people's diamonds off the stand"* — a wider shot of the same case: a row of rings on stands, her hand and the cloth the only things moving, everything else still.
3. *"Somebody said, that's as close as you get"* — a faceless colleague backlit in a half-closed shutter, bag over the shoulder, saying it on the way out, never a reverse angle.
4. *"I said, give it ten years, and I'll take that bet"* — her face reflected in the case glass over the rings, entirely unbothered, one small nod, close-up.

### Verse 1 — twenty-two, two jobs

5. *"Twenty-two, two jobs and a folding bed"* — a folding bed against a bare wall in a rented room, a second uniform on a hanger behind it, flat daylight, static wide.
6. *"Four Cs on a poster and they lived in my head"* — a laminated poster taped to a staff-room wall, corners curling, blank in-camera (composited), her looking up at it while eating.
7. *"Cut, colour, clarity, carat, in that order"* — four macro inserts on the beat: a bevelled edge, a lamp through glass, a flawless surface, a set of tiny scales.
8. *"Said them like a prayer while I locked the door"* — her mouthing the four words while pulling a shutter down from the outside, hands above her head, street dark.
9. *"Everybody's diamond came out of the dark"* — the first glimpse of the seam: a black rock face, one work lamp, a figure very far away in it, wide.
10. *"Nobody asks a stone what it cost to start"* — a stone in a display setting in extreme macro, perfect and silent, then a cut to raw rock at the same scale.
11. *"They only see the setting, they never see the mine"* — a customer's hand in the shop, faceless, being shown a ring; behind the glass her hands wait with the tray.
12. *"Never see the hands that put the shine on the shine"* — extreme close-up of her hands, dry knuckles, cloth wound round two fingers, polishing.
13. *"So I kept my head down and I let it press"* — a six-in-the-morning bus window with her asleep against it, city grey sliding past, static.
14. *"Diamonds don't get made out of comfort and rest"* — back to the seam: her palm flat against the rock face, dust falling on her forearm, one lamp, near-black.

### Pre-chorus 1 — a mile of stone

15. *"Two thousand degrees and a mile of stone"* — a tight tunnel of rock lit by one lamp, the walls close enough to touch on both sides, slow push-in.
16. *"Nobody heard a thing, I was down there alone"* — her face lit only by the lamp, no expression, dust in the beam, static close.
17. *"Now the lid comes off and the room goes still"* — a hairline crack opening in the rock, a single point of white light coming through it, macro.
18. *"Count it down and let the light spill"* — the crack widening, the white light flooding the lens and blowing the frame out entirely.
19. *"Here we go"* — one dead-stop frame of pure white, held for the silent bar.

### Chorus 1 — the case opens

20. *"Pressure made me, now it's diamond season"* — a glass case lid rising on a hydraulic hinge, the light changing as it opens, low angle, hard white key.
21. *"You can hate the way I shine, you don't get a reason"* — a velvet tray sliding into a spotlight, empty except for one stone, macro, deep black surround.
22. *"I was carbon in the dark with a weight on my chest"* — a half-second cut back to the rock seam, the same composition as shot 14, then straight back to white.
23. *"Now the light goes right through me and comes out the best"* — a prism throwing bands of real colour across a white wall and then across her face, slow track.
24. *"Turn me, turn me, catch the edge"* — her turning slowly under a hard key light, the refraction crawling over her shoulders and jaw, locked off.
25. *"Every cut you ever gave me is a facet in the end"* — extreme macro of a stone rotating, each facet catching the light in turn, one per beat.
26. *"Pressure made me, now it's diamond season"* — a wide of her alone in a black space with a single beam and the prism pattern all around her.
27. *"Diamond season, diamond season"* — the pattern accelerating across the wall, then a hard cut to black on the last word.

### Post-chorus 1 — the drop, four match cuts

28. *"Carbon, carbon, hold the line"* — cloth on glass, cut on the beat to a loupe against an eye, the same framing exactly.
29. *"Carbon, carbon, give it time"* — the navy polo, cut on the beat to the black gown, identical posture and identical frame.
30. *"Pressure, pressure, hold me down"* — the staff-room fluorescent, cut on the beat to a gala spotlight, the same overhead angle.
31. *"That is how a diamond gets its crown"* — the rock face, cut on the beat to a black marble staircase, the same lines and the same lens.
32. *"Diamond season, diamond season"* — a wide of her at the top of the black staircase, alone, chandelier above, held.
33. *"Ten years cooking, here's the reason"* — the four cuts replayed at double speed as one flurry, ending on her face at the top of the stairs.

### Verse 2 — the rap, workshop and vault

34. *"Ten years pressing, ten years quiet, ten years carbon in the seam"* — her at a jeweller's bench under a single desk lamp, suit look, loupe up, static and exact.
35. *"Every no was a hundred atmospheres, every knockback was a squeeze"* — a hydraulic press closing slowly on a piece of metal, macro, hard shadow, no faces.
36. *"They said the girl with the cloth ain't the girl on the tray"* — a split composition: the polo look reflected in one pane of glass, the suit look in the next.
37. *"Now the girl with the cloth got the loupe and the say"* — her magnified iris filling the frame through the loupe, unblinking, extreme macro.
38. *"Cut me at an angle where the light has to bend"* — a stone in tweezers turned exactly one degree under a lamp until the light bends, macro.
39. *"That is not luck, that's geometry, friend"* — a technical drawing of facet angles on a lightbox (composited), her finger tracing one line.
40. *"Clarity is nothing but the flaws I outgrew"* — a wall of tiny drawers, one pulled open, the light finding what is inside, static.
41. *"Colour is the temper that the fire ran through"* — a jeweller's torch flame passing across metal in slow motion, the colour changing, macro.
42. *"Carat is the years, so go on, count the weight"* — a set of small brass scales settling, the pans coming level, one hand steadying them.
43. *"I don't shine for a room, the room can catch up late"* — her walking a steel vault corridor in the suit, lights coming on ahead of her, tracking.
44. *"Put a hand on the velvet, but don't touch the glass"* — a stranger's hand approaching the glass and her own hand stopping it an inch short, close.
45. *"Everything I am I made out of the past"* — she sets the loupe down on the bench and the desk lamp clicks off, hard cut to black.

### Pre-chorus 2 — the gala doors

46. *"Two thousand degrees and a mile of stone"* — two heavy doors seen from the inside, her silhouette against them, backlit white, static.
47. *"Nobody heard a thing, I was down there alone"* — a half-second flash of the rock tunnel at the same framing, then back to the doors.
48. *"Now the doors come off and the whole room turns"* — the doors opening and every head in the gala turning at once, wide, one continuous move.
49. *"Count it down and let it burn"* — the chandelier above coming into focus over her shoulder, the drops firing their spectrum.
50. *"Here we go"* — one dead-stop frame of her in the doorway, held for the silent bar.

### Chorus 2 — the gala

51. *"Pressure made me, now it's diamond season"* — her descending the black marble staircase, chandelier light crawling over the gown, tracking.
52. *"You can hate the way I shine, you don't get a reason"* — the gala crowd turning as she passes, faces visible but never held, over the shoulder.
53. *"I was carbon in the dark with a weight on my chest"* — a half-second cut to the shop case, empty and lit, then straight back.
54. *"Now the light goes right through me and comes out the best"* — chandelier drops throwing exactly the pattern of the shop case prism onto black marble.
55. *"Turn me, turn me, catch the edge"* — a champagne flute rotating in slow motion, refracting light identically to a cut stone, macro.
56. *"Every cut you ever gave me is a facet in the end"* — the facet macro of shot 25 repeated, faster, one per beat, brighter.
57. *"Pressure made me, now it's diamond season"* — a wide of the whole gala room from above, her the only still figure in it.
58. *"Diamond season, diamond season"* — the spectrum sweeping across the marble floor, then a hard cut to black.

### Instrumental — light itself

59. A prism rotating on a black background, the spectrum crawling slowly across the whole frame, no people, locked off.
60. A long corridor with the arpeggio visualised as light travelling down it, one lamp igniting per note, slow track.
61. The drums-out drop played on one held wide of the empty gala staircase, nobody on it, everything lit.
62. The snare-roll build cut entirely on faces from the room, one per beat, accelerating.
63. The shop's glass case, empty, one light still on, the cloth folded on top of it, static.

### Bridge — no refraction

64. *"Do not get it wrong, I would not wish the weight"* — her sitting on the floor of the empty shop in the gown with her shoes off, case light above, completely still.
65. *"I am not the girl who says the dark was great"* — a close-up of her face under a single fluorescent strip, unflattering and honest, no prism anywhere.
66. *"Nobody needs a mile of stone on their chest"* — a wide of the shop with the shutters down, small and ordinary, her tiny in the corner of it.
67. *"To be worth the velvet, to be worth the rest"* — an empty velvet tray on the counter beside her, nothing on it, macro.
68. *"I did not need the pressure to be worth the light"* — the four-Cs poster still taped to the staff-room wall, her looking at it from the doorway.
69. *"But the pressure came, and I did not break, and that is mine"* — her taking the poster down carefully and rolling it, close on the hands.
70. *"So I will take the season and I will take the shine"* — she stands, gown gathered in one hand, the rolled poster in the other, static.
71. *"And I'll leave the door open for the next one in line"* — a foot propping the shop door open, the street light coming in, the arpeggio returning on the frame.

### Final chorus — both worlds at once

72. *"Pressure made me, now it's diamond season"* — the gala staircase and the shop floor intercut on the bar, matched camera moves in both.
73. *"You can hate the way I shine, you don't get a reason"* — every prism in the video firing at once across a black wall, the widest refraction shot.
74. *"I was cloth on a glass case, closing up alone"* — the polo look and the cloth, one clean shot, no irony in the framing.
75. *"Now the case is open and the light is my own"* — the case lid up, nothing inside it, the light spilling out over her hands, macro.
76. *"Turn me, turn me, catch the edge"* — her turning under the chandelier as the refraction lands across her, the biggest version of shot 24.
77. *"Every cut you ever gave me is a facet in the end"* — facet macros and chandelier drops cut together, one per beat, indistinguishable.
78. *"Pressure made me, now it's diamond season"* — the widest shot of the video: the entire gala room, every light on, her at the centre of the floor.
79. *"Diamond season, diamond season"* — the room holding, the spectrum still moving across the marble, then black.

### Post-chorus 2 — the drop reversed

80. *"Carbon, carbon, hold the line"* — gown cut to polo cut to gown on consecutive beats, the same frame each time.
81. *"Carbon, carbon, give it time"* — staircase cut to rock face cut to staircase, matched lines and lens.
82. *"Pressure, pressure, hold me down"* — the loupe cut to the cloth cut to the loupe, identical macro framing.
83. *"That is how a diamond gets its crown"* — spotlight cut to fluorescent cut to spotlight, the same overhead angle.
84. *"Diamond season, diamond season"* — a close-up of her hand, open, with no jewellery on it at all, held.
85. *"Ten years cooking, here's the reason"* — hard cut to the shop fluorescent coming on with a flicker, the drop stopping dead.

### Outro — the new girl

86. *"Night shift, glass case, cloth in her hand"* — macro of a cloth on glass exactly as shot 1, but a different, younger hand doing it.
87. *"Somebody's wiping the glass where I stand"* — the new girl in the navy polo behind the case, unimpressed, mid-shift, static.
88. *"I told her, ten years, and I meant every one"* — Mahima on the other side of the glass in the gown, saying the line; the new girl looking up.
89. *"Diamond season, and it's only begun"* — final shot: the two of them either side of the case, the reflection placing them in the same frame, the shop lights going down to one, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the bet in shot 4, the crack of light on *"let the light spill"*,
the case lid on the first chorus, all four drop cuts, the loupe close-up,
the doors opening, the poster coming off the wall, and the last case light.
At 126 BPM a bar is 1.9 s; choruses cut on the bar, the drop cuts on the
half-bar, and the four match cuts land exactly on *"carbon"*, *"carbon"*,
*"pressure"*, *"pressure"*.

**The transformation challenge.** The drop is the shareable unit: post shots
28–33 vertically and invite people to film themselves in their work clothes,
cut on the first *"carbon, carbon"*, and land on the version of themselves
that took ten years. **The hook frame** is shot 31, the rock face cutting to
the marble staircase. **The rap clip** is shot 39. **The quote card** is shot
69.

## 6. Quality-control checklist

- Three looks in the right sections: navy polo for the shop and the seam, charcoal suit only for the rapped verse, black gown for the choruses, bridge and outro
- The polo look and the gown look must read as unmistakably the same face; every match cut in the drop depends on it
- She wears no jewellery in any shot of the video, including the gala
- Every colour except skin tone comes from real refraction plates composited in the edit; no gels, no CGI caustics
- The bridge has no refraction anywhere in it, and that absence must be obvious
- The four drop cuts use identical framing, lens and posture on both sides of each cut
- All lettering composited: the four-Cs poster, the name badge, the price tickets, the vault drawers, the facet drawing
- The colleague in the intro doorway has no face and no reverse angle; there is no male lead in this video
- The last four shots repeat the first two framings with a different hand, and the final two-shot holds until the audio fades
