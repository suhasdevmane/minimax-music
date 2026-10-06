# Wan 2.2 Shot List — "Pretty and Powerful"

**One shot per lyric line**, built from the submission's per-section video
direction. At 100 BPM a bar is 2.4 s, so verse shots run 3–5 s and the
choruses cut roughly every bar. Take timestamps from the rendered WAV.

## 1. Visual world

Three rooms, one palette. A **concrete warehouse** with a lit runway down
the middle, a **black glass boardroom** on the fifth floor, and an **empty
boxing ring** under a single work lamp. Everything is gold and black:
practical tungsten lamps, brass-coloured light, black floors, black
tailoring, no other saturated colour except one bright coat in verse three.
Over the course of the video the three rooms bleed into each other — a
runway light rig above the boardroom table, a boardroom chair on the runway,
the ring ropes lit gold — until the final chorus, where they are one space.

| Section | Light | Camera |
|---|---|---|
| Intro | Cold concrete, one gold shaft from a high window | Static, low, wide |
| Verse 1 (her) | Hard boardroom daylight through black glass | Slow push-ins |
| Verse 2 (his rap) | Gold work lamps, hard shadows, black floor | Handheld to camera, on the beat |
| Pre-choruses | Gold key, deep black fill, one held still frame | Locked off |
| Choruses | Overhead lamps igniting on the brass hits | Runway tracking, hard cuts |
| Post-chorus chant | All lamps up, dust in the beams | Floor-level, wide |
| Verse 3 (her) | Late-afternoon gold through black glass | Steady, warm |
| Verse 4 (his rap) | One work lamp, everything else dark | Static, seated, honest |
| Instrumental | Gold reducing to a single lamp, then a rise | Floor level, slow motion |
| Bridge | One lamp, long shadow, warm | Completely still |
| Final chorus | Every lamp lit, gold saturating | Crane and runway tracking |
| Outro | Cold concrete, one gold shaft, then black | The intro framings repeated |

## 2. Character bible — paste into every prompt

**Mahima** (the runway and chorus look — primary)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair straightened and worn sleek behind the shoulders, defined brow and a clean gold-toned makeup, wearing a sharply tailored black blazer over a black top and wide black trousers, large gold hoop earrings, black heels, level confident expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (boardroom, verses one and three)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied low at the nape, minimal gold-toned makeup, wearing a black high-neck knit and tailored trousers with a slim gold chain, a black folder under one arm, composed alert expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge and outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly undone, makeup softened, wearing the black blazer over her shoulders like a coat and bare feet on concrete, unguarded open expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (Singer B, the rapper — the only male character with a face)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing an unstructured black jacket over a black tee and dark trousers, a thin gold chain, relaxed grounded expression, realistic cinematic photography, consistent identity

**The boardroom** — every colleague is faceless: backs of heads, shoulders, hands on a table, figures cropped at the jaw. Nobody is ever the villain on camera; they are simply not the subject.

**The younger woman** (verse three) — a woman in her early twenties in a bright cobalt coat, the only non-gold colour in the video, face visible and nervous then delighted.

**The crowd** (chant and final chorus) — twelve people in black, all ages, faces visible, stamping heel patterns on concrete.

Objects: the **propped full-length mirror**, the **black folder**, the
**heels carried in one hand**, the **tripod camera** she turns to face the
mirror, the **roll of architect's drawings**, the **skipping rope** in the
empty ring.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All text is composited in the edit** — the pitch-deck cover and its credits
line, the name being painted on the glass door, the contract, the charts on
the warehouse wall. Generate blank paper, blank glass and blank boards, then
overlay in post; the model cannot render legible lettering and the missing
name on the credits line is the whole point of verse one.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock both leads with IP-Adapter or a character LoRA each (front, three-quarter,
profile, seated, walking); keep every boardroom reference deliberately
faceless. **OpenPose is essential** for the runway walks, the heel-stamp chant
and the rope turn in the ring — a walk cycle in heels is where this model
invents anatomy. Depth for the warehouse and the black-glass boardroom, both
of which are big reflective spaces. 16:9 first; 9:16 recomposition for the
runway and chant cuts. Animate in short bursts: two strides per clip, one
lamp igniting, one stamp, one page turning.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — cold room, one brass swell

1. *"Warehouse mirror, cold floor, gold light"* — a full-length mirror propped against a concrete pillar in an empty warehouse, one gold shaft from a high window crossing it, nobody in frame, static wide.
2. *"Heels in one hand, a contract in the other"* — her bare feet walking across cold concrete, heels hooked on two fingers in one hand, a black folder in the other, low tracking at ankle height.
3. *"They keep asking me which one is the real one"* — her face in the propped mirror, half in the gold shaft, half in shadow, static close.
4. *"Both of them. Run it up"* — Kai in the far doorway, backlit, not moving, delivering the last two words; the brass swell lands and the frame cuts to black.

### Verse 1 — her, the boardroom

5. *"They put my face on the cover of the deck"* — a printed pitch deck sliding across a black glass table, her photograph on the cover (composited), a faceless hand pushing it, macro.
6. *"Left my name off the line where the credit gets checked"* — extreme close-up of the credits line on the back page (composited), her thumb resting just below where her name is not, held.
7. *"He got the forecast question, I got the small talk"* — a wide of the boardroom, every head turning away from her toward a faceless man at the far end, her the only face in frame.
8. *"Which salon, which shade, which designer, which walk"* — four fast cuts on the beat: a hand gesturing at her sleeve, at her earring, at her hair, at her shoes, all faceless, all from her eyeline.
9. *"So I named the margin before they could ask"* — her standing and speaking, one hand flat on the glass, the room reflected upside down beneath it, slow push-in.
10. *"And I let the number do the talking, then I laughed"* — the table recalculating, pens moving, then a single genuine laugh from her, close-up, the first warm frame of the video.
11. *"Pretty was never a place I was hiding"* — her walking the corridor outside, folder under one arm, black glass on both sides doubling her, tracking from behind.
12. *"It's the door I walk through, it is not the building"* — she pushes a heavy glass door open and the corridor behind her goes dark as the warehouse ahead lights up, match cut on the door.

### Verse 2 — Kai's rap, the runway lights

13. *"Watch her walk in the warehouse, whole room recalibrate"* — Kai at the head of the lit runway, hands loose, delivering straight to the lens, crew building lighting track behind him, handheld.
14. *"Gold on the collar, but the mind is what intimidates"* — a macro of a gold hoop and a jaw line, then a hard cut to the same framing on a page of figures, both lit the same.
15. *"They clocked the glow and they slept on the resume"* — the faceless boardroom seen from the runway's far end, tiny and far away, Kai walking toward camera in the foreground.
16. *"Now they in the back row taking notes on how she runs the day"* — folding chairs at the edge of the runway, faceless figures writing, her passing in the opposite direction without looking.
17. *"She ain't a muse, she the architect, she drafted the design"* — a roll of architect's drawings unrolled on a trestle table, her hand flattening it, gold work lamp above, macro.
18. *"Y'all built a hallway, she just widened up the line"* — a narrow corridor of lighting stands, crew pulling them wider apart on the beat, the runway visibly widening, low wide.
19. *"Call her pretty, cool, but say the whole sentence"* — Kai stopping dead centre of the runway, pointing past the lens, static, one lamp igniting behind him.
20. *"Pretty and the payroll and the plan and the presence"* — four lamps igniting on the four nouns, one per beat, the runway fully lit by the end of the line, locked off wide.

### Pre-chorus 1 — the mirror and the tripod

21. *"Two things are true at once, they always were"* — her standing in front of the now-upright mirror, blazer on, seen only as a reflection, static.
22. *"Don't hand me a mirror and call it a career"* — her hand turning a tripod camera beside the mirror so the lens and the reflection face each other, close-up.
23. *"I can be the picture and the one who takes it"* — the frame she is composing: her reflection, the camera, and her hand on the shutter release, all in one shot.
24. *"I can be the plan and the one who makes it"* — the drums drop out; one completely still frame, her looking directly into the mirror, held for the silent bar.

### Chorus 1 — the runway at full power

25. *"Pretty and powerful, don't make me choose"* — the runway walk, tracking backwards ahead of her, overhead lamps igniting in sequence on the brass hits.
26. *"I'll take the heels and the hard-earned bruise"* — split-second cuts: a heel landing on the runway, then the same rhythm on the canvas of the empty boxing ring.
27. *"Gold in my ears and the numbers in my hand"* — macro of a gold hoop swinging, then the black folder in her grip, matched framing.
28. *"Look good, close it out, that was always the plan"* — the boardroom walk in the same body language as the runway walk, hard cut between the two on the beat.
29. *"You want the gloss or you want the grind"* — a two-shot cut: the runway lit like a fashion show, then the ring lit by one bare bulb, identical composition.
30. *"Both of them living in the same mind"* — her stopped in the exact centre of the runway with the ring behind her and the boardroom ahead, deep-focus wide.
31. *"Pick a lane for me, but I already do"* — the crew laying a second lighting track alongside the first, doubling the runway, low angle on the beat.
32. *"Pretty and powerful, don't make me choose"* — she reaches the end of the runway and stops on the downbeat, every lamp lit behind her, locked off wide.

### Post-chorus 1 — the chant

33. *"Gold and black, gold and black"* — floor-level shot of twelve pairs of feet in black stamping the chant pattern on concrete, heels only.
34. *"Front of the room and I'm not moving back"* — her at the front of the group, dead still while everyone behind her stamps, wide, lamps swinging slightly.
35. *"Pretty. Powerful. Both at once."* — three hard cuts on the three phrases: her face, the crowd's feet, Kai's raised arm at the edge of frame.
36. *"Don't make me choose"* — the whole group freezing on the last word, dust hanging in the lamp beams, held one extra beat.

### Verse 3 — her name on the glass

37. *"Fifth floor glass and my name on the wall"* — a signwriter's hand finishing lettering on a glass door (composited), her reflection watching from the corridor.
38. *"Same faces, same questions, different tone in the call"* — the same boardroom composition as shot 7, but every faceless figure is now leaning toward her instead of away.
39. *"I do not owe this table a plainer face"* — her at the head of the table, gold hoops on, entirely at home, slow push-in, late-afternoon gold.
40. *"And I don't shrink my laugh to fit a smaller space"* — her laughing at full volume, head back, and nobody at the table flinching, handheld, warm.
41. *"They said pick one, so I picked the two"* — her sliding two chairs out from the table instead of one, close on the hands, deliberate.
42. *"Then I hired the girl they said was too much too"* — the younger woman in the cobalt coat shown to the second chair, the two shaking hands, the only non-gold colour in the video.

### Verse 4 — Kai's second rap, stripped

43. *"I'll be honest, I was taught that a woman had to trade"* — Kai alone on a flight case in the emptied warehouse, jacket off, one work lamp, talking straight to camera, static.
44. *"Look good or get respected, only one of them pays"* — the same shot, no cut, he simply looks away and back; the honesty is in the stillness.
45. *"Then I sat in the back while she carried a whole floor"* — a wide from the very back of the warehouse, him small in the frame, the wall of charts lit behind her at the far end.
46. *"Charts up the wall and a warehouse on tour"* — a slow lateral track along the wall of blank boards (charts composited), gold lamp light raking across them.
47. *"Told my little sister, hey, don't lower the light"* — a warm cutaway with no music-video gloss: Kai on a doorstep with a teenage girl, both sitting, ordinary daylight.
48. *"Nobody dims the sun to make the moon look right"* — the same doorstep, the girl looking up, a lamp behind her in the hallway staying bright, close two-shot.
49. *"So say it all together, don't split it in two"* — back to the flight case, him standing, the lamps of the warehouse coming up one at a time behind him.
50. *"Pretty and powerful, that is just her, that's the truth"* — he turns and walks out of frame toward the runway, leaving the lamp swinging, static.

### Pre-chorus 2 — the mirror, with everyone behind her

51. *"Two things are true at once, they always could"* — the mirror shot of 21 repeated, but the reflection now has the whole crowd standing behind her.
52. *"Don't call it a lucky face, it was hours and good"* — the tripod camera again, her hand on it, the shutter firing once, the flash lighting the whole group.
53. *"I can be the picture and the one who takes it"* — the composed frame from shot 23, now wide enough to contain twelve people, all still.
54. *"I can be the plan and the one who makes it"* — the silent bar again on one held frame, wider, the choir entering, lights up one stop.

### Chorus 2 — the rooms bleed together

55. *"Pretty and powerful, don't make me choose"* — a runway lighting rig hanging above the boardroom table, her walking the length of the table like a runway, tracking.
56. *"I'll take the heels and the hard-earned bruise"* — the boardroom chair now standing on the runway, empty, lit like a monument, static.
57. *"Gold in my ears and the numbers in my hand"* — reuse the macro pairing of shot 27, tighter and faster, gold hoop then folder.
58. *"Look good, close it out, that was always the plan"* — her signing the contract on the runway floor, kneeling, lamps overhead, high angle.
59. *"You want the gloss or you want the grind"* — the ring ropes lit gold with the runway visible through them, deep focus, no people.
60. *"Both of them living in the same mind"* — a single continuous-feeling move that carries her from ring to runway to boardroom, three spaces, one walk.
61. *"Pick a lane for me, but I already do"* — the crowd forming two lines on either side of the runway, her walking between them, backwards tracking.
62. *"Pretty and powerful, don't make me choose"* — a brass hit on the word choose, every lamp in all three rooms igniting at once, locked-off wide.

### Instrumental — brass riff, heel-strike breakdown, rise

63. Twelve pairs of heels stamping in unison on concrete, shot from floor level, dust lifting with each strike, slow motion into real time.
64. A skipping rope turning in slow motion in the empty boxing ring, nobody holding it in frame, single bare bulb above.
65. Brass players in silhouette in a far corner of the warehouse, only the bells of the instruments catching gold.
66. Her hand flattening the contract on the trestle table, one slow pass, macro, no face.
67. The lamps killing one by one until only the propped mirror is lit, then a filtered rise as every lamp snaps back on together.

### Bridge — the mirror, alone

68. *"For years I cut myself in half to fit the room"* — her sitting on the floor in front of the mirror, blazer over her shoulders, bare feet, completely still camera.
69. *"Wore the quiet one to work, saved the loud one for the moon"* — her reflection and her real profile in one frame, the reflection lit warmer than she is.
70. *"Grew up on lip gloss and long division"* — an insert on a childhood desk: an open exercise book of long division beside an open lip gloss, one lamp, macro.
71. *"Nobody told me I had to pick a religion"* — back to the floor, her turning the blazer right way round and putting one arm in, unhurried.
72. *"Beauty is not the rent I pay to keep the skill"* — Kai off to the side, out of focus, saying his answering line; she does not turn to him.
73. *"Both of them mine, and I'm not choosing. I never will"* — she looks directly into the lens on the last word, the drums land, hard cut to white lamp glare.

### Final chorus — everything at once

74. *"Pretty and powerful, don't make me choose"* — the runway packed on both sides, her walking its full length, crane rising with her.
75. *"I'll take the heels and the hard-earned bruise"* — the crew carrying the boardroom table onto the runway and setting it down on the beat, wide.
76. *"Gold in my ears and the room in my hand"* — her stepping up onto the table, gold hoops catching every lamp, low angle.
77. *"Look good, close it out, that was always the plan"* — the crowd's faces from her eyeline on the table, a slow pan across all of them.
78. *"You want the gloss or you want the grind"* — Kai on the ropes of the ring, one arm up, the chant behind him, matched height to her on the table.
79. *"Both of them living in the same mind"* — a two-shot with the whole warehouse between them, both raised, both lit the same, wide.
80. *"Two of us saying it, so you say it too"* — the crowd shouting the line to camera, faces visible, dust in the beams, handheld among them.
81. *"Pretty and powerful, don't make me choose"* — a crane pulling up and back over the entire warehouse with every lamp lit, the runway a bar of gold.

### Post-chorus 2 — handed over

82. *"Gold and black, gold and black"* — floor-level stamping again, now with the whole crowd and both leads in the pattern, not leading it.
83. *"Front of the room and I'm not moving back"* — the younger woman in the cobalt coat at the very front of the group, stamping, grinning.
84. *"Pretty. Powerful. Both at once."* — three cuts across three faces from the crowd, none of them the leads, one per phrase.
85. *"Don't make me choose"* — the whole group facing camera and freezing, the two leads at the edges of frame rather than the centre, held.

### Outro — the empty room again

86. *"Warehouse mirror, cold floor, gold light"* — the exact framing of shot 1: the propped mirror, the gold shaft, the warehouse empty again, static.
87. *"Heels on, folder closed, both of them right"* — her sitting on the floor putting the heels on, then closing the black folder on her knees, close.
88. *"Don't make me choose"* — she stands into frame and the mirror holds her reflection alone, nobody else in the room, static wide.
89. *"Never had to choose"* — a last look at the mirror, no expression to camera, just checking, then turning away.
90. *"Pretty and powerful"* — final shot: the ankle-height tracking shot of shot 2 reversed, heels on now, walking out through the gold shaft, the lamp dying behind her, locked off through the fade. No text.

## 5. Edit and the challenge

Markers at: the brass swell after *"run it up"*, the door match cut on
*"it is not the building"*, the four lamps on *"pretty and the payroll and
the plan and the presence"*, every *"don't make me choose"*, both silent
bars in the pre-choruses, the doorstep cutaway, the look to lens on *"I
never will"*, and the final gold shaft. At 100 BPM a bar is 2.4 s; the
choruses cut roughly on the bar and the chant cuts on the half-bar.

**The gold-and-black challenge.** The chant is the shareable unit: post the
vertical cut of shots 33–36 with *"gold and black, gold and black"* on
screen and invite people to film four seconds of the heel-stamp pattern and
cut on the fourth beat, which works as a transition into any outfit change.
**The hook frame** is shot 20, four lamps igniting on four nouns. **The rap
clip** is shots 18 and 48. **The quote card** is shot 73.

## 6. Quality-control checklist

- Three Mahima looks in the right sections: blazer and hoops for the runway and choruses, low-tied hair and folder for the boardroom verses, blazer over the shoulders and bare feet for the bridge and outro
- Kai has a face and is never posed as her boss, her rescuer or her partner; his second verse is delivered seated and still, with no swagger
- Every boardroom colleague is faceless; the cobalt coat is the only non-gold colour in the entire video
- Light is gold and practical only; no coloured gels, no CGI beams, no lens effects beyond real flare
- All lettering composited: the deck cover and its credits line, the glass door, the contract, the charts
- The three rooms bleed together progressively — no cross-room prop appears before chorus two
- Heel and stamp shots pose-referenced; no invented ankles, no floating feet
- The last two shots are exact reversals of the first two, and the final one holds until the audio fades
