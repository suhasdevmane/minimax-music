# Wan 2.2 Shot List — "Call Me After Midnight"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. At 96 BPM a bar is 2.50 s; the choruses cut
on the gated snare and the verses cut on the phrase, so shots run 3–5 s. Take
timestamps from the rendered WAV.

## 1. Visual style

Two grades and a hard rule between them. The **day** is flat, colourless
office light — desaturated, wide-lensed, competent and completely empty. The
**night** is a bedroom lit magenta and cyan by a window sign across the
street, with no white light anywhere in it, ever. Verse one is the only
sustained daylight in the video and the last daylight frame is the hallway
light switching off; after that the neon does not leave until dawn.

The **corded landline** is the co-star. It is a deliberate anachronism and it
is in almost every night frame: the handset, the cradle, the coiled cord
stretching across a duvet, across a floor, out of a doorway. A mobile phone
appears exactly twice, both times being pushed away.

| Section | Grade | Camera |
|---|---|---|
| Intro | Magenta key, cyan fill, one degree darker per shot | Static, medium |
| Verse 1 (day) | Flat desaturated office daylight, no colour | Wide, locked-off |
| Pre-chorus 1 | Neon starting to pulse with the arpeggio | Macro, static |
| Chorus 1 | Deep magenta and cyan, warmest frames of the film | Cutting on the snare |
| Verse 2 (stairwell) | One warm shaft through wired glass, afternoon | Handheld, close |
| Pre-chorus 2 | Neon pulsing harder, room darker | Held statics |
| Chorus 2 | Same palette pushed harder | Longer, wider moves |
| Instrumental | Near-black with only the sign on | Slow drift, macro |
| Bridge | The two grades alternating side by side | Static, cutting |
| Final chorus | Brightest neon, window open, city cold outside | Rising crane |
| Post-chorus | Hard cuts on the gated snare | Static macro |
| Outro | Grey-blue first light killing the neon | Locked-off, low |

## 2. Character bible — paste into every prompt

**Mahima** (day)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled back neatly, careful daytime makeup, wearing a stone-grey blazer over a white shirt with a plain lanyard badge, composed professional expression that never reaches her eyes, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and loose, makeup washed off, wearing an oversized cream ribbed vest and soft grey shorts, bare feet, relaxed amused expression, realistic cinematic photography, consistent identity, natural skin texture

**The man is never seen and never heard.** He exists entirely as a voice on a
line — no face, no hand, no cutaway to his room, no flashback. Resist the
temptation: the whole video is one woman alone in a room, and that is why it
works.

**The office extras** — four people in an elevator, three people in meeting
rooms, all faceless or in profile, none held for more than a beat. Nobody in
the daytime section is a character.

Objects that carry the film and must stay consistent: the **corded landline**
in cream plastic with a coiled cord, the **window sign** across the street
that supplies the magenta, the **cold mug of tea** on the desk, the **blank
lanyard badge**, and the **second pillow**, which the handset ends up lying
on in the final chorus.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The window sign, the lanyard badge, the world clock faces, the phone
screens and every piece of office signage are composited in the edit.**
Generate the sign as a coloured light source with no readable characters —
its job is the magenta, not the message.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA — the day and
night looks are the same face under completely different light, and the
bridge cuts between them four times, so the identity has to hold across a
grade change. There is only one character to lock, which makes this the
simplest bible in the set. Depth for the bedroom, which is shot from a dozen
positions; OpenPose only for the slow dance in the final chorus and the
feet-up-the-wall shot.

Animate small and animate the cord. The single most useful motion in this
video is a coiled telephone cord swinging, stretching and dragging — it
carries rhythm without needing a body to move. Neon pulse is safest done as a
brightness oscillation in the edit over an evenly lit plate, matched to the
arpeggio. 16:9 first; 9:16 for the chorus and the bridge alternation, which
are the natural vertical content.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — putting the day down

1. *"Twelve o'clock, and the city drops a gear"* — a wide of the bedroom lit magenta from a window sign across the street, curtains open, nobody in frame yet, static.
2. *"Laptop shut, kettle cold, nobody here"* — a laptop lid closing under one hand and the room dropping one degree darker, then a mug of untouched tea on a desk, macro.
3. *"Everybody had a piece of me today"* — Mahima (night look) sitting on the end of the bed still in half of her work clothes, doing nothing at all, medium.
4. *"Now the light goes low and I'm not giving it away"* — her pulling the last of the work clothes off over the back of a chair, the neon on her shoulders, medium, slow.

### Verse 1 — the daytime self

5. *"From nine to six I'm a name on somebody's list"* — flat office daylight, the only sustained daylight in the film: a blank lanyard badge against a white shirt (composited), macro.
6. *"Nodding in an elevator where the signal won't stick"* — an elevator interior with four faceless people, Mahima nodding at somebody talking, a phone in her hand with no bars (composited), locked-off.
7. *"Six voices in my ear and a badge on a string"* — a meeting room seen through glass, her mouth moving, no sound design behind it, wide.
8. *"And a daytime voice that doesn't mean a thing"* — her professional smile in close-up, held two beats too long so it stops reading as a smile.
9. *"By eleven I've said yes about a hundred times"* — the same nod in four different rooms, cut fast on the beat, identical framing each time.
10. *"By half past I've run out of the good kind"* — her alone in a stairwell for two seconds with her eyes shut and her head back against the wall, static.
11. *"Then the hall light goes off and the day lets go"* — a corridor light switching off at the far end, the frame going dark from the back forward — the last daylight frame in the video.
12. *"And my shoulders come down and my voice goes low"* — back in the neon bedroom: her shoulders dropping visibly on the beat, one long breath out, close-up.

### Pre-chorus 1 — the rule

13. *"Don't text me, I don't want it typed"* — a mobile phone face-up on the duvet with a blank message screen (composited), her thumb hovering and then pushing it away across the sheet.
14. *"I want the low and lazy sound of you alive"* — the cream corded landline on the bedside table, the coiled cord curling across the duvet, macro, deliberate.
15. *"Let it ring twice, I'll get it on the third"* — her hand resting flat on the cradle, not lifting it, the neon pulsing twice on the light change.
16. *"Nothing in the world I'd rather have than your word"* — her face lit magenta, looking at the phone and not at the camera, close-up, the arpeggio arriving.

### Chorus 1 — the line opens

17. *"Call me after midnight, that's when I'm all yours"* — the handset lifted and brought to her ear, the coiled cord swinging under it, close, cut on the gated snare.
18. *"When the office goes dark and they lock all the doors"* — the window: an office tower across the city going out floor by floor, wide, static.
19. *"Nobody wants a thing from me at half past two"* — her lying back across the bed with the phone on her chest, the ceiling magenta above her, overhead.
20. *"Nothing left to give, and I'm giving it to you"* — her mouth close to the receiver, smiling at something we do not hear, extreme close-up.
21. *"Call me after midnight, let the line run long"* — the cord stretched taut from cradle to hand across the width of the frame, macro.
22. *"Say it slow, say it wrong, keep the talking on"* — her laughing with no sound, head turning away from the receiver, close-up.
23. *"Every hour before this one was the world's, not ours"* — a two-second flash of the office corridor in flat grey, then a hard cut back to magenta.
24. *"Call me after midnight, that's when I'm all yours"* — a wide of the whole room with her small in it and the window sign huge behind her.

### Verse 2 — the rule breaks

25. *"Tuesday you were three time zones out of line"* — a world clock on an office wall with blank faces (composited), static, flat light.
26. *"And your midnight came down sideways into mine"* — the same clock from an angle, the second hand moving, her reflection faint in the glass over it.
27. *"So I broke my own rule in a stairwell at four"* — a fire-escape stairwell, one warm shaft of afternoon light through wired glass, her sitting three steps up with the phone to her ear.
28. *"Whispered like a thief with my back to the door"* — her back against the door, phone cupped in one hand, whispering, handheld, close.
29. *"You said, that's the day voice, and I said, it's not"* — somebody pushing the stairwell door from the other side, her going instantly silent, then carrying on.
30. *"Then I dropped it half an octave and proved your point"* — extreme close-up of her mouth, chin dropping, one hand cupped around the receiver, the smile arriving as she is caught out.
31. *"So the rule's got a hole in the shape of you"* — back in the neon bedroom that night, her grinning at the ceiling with nothing in her hands, medium.
32. *"And I'm in no hurry to make it new"* — the landline on the table, untouched, the room dark around it, static, held.

### Pre-chorus 2 — already awake

33. *"Don't text me, I don't want it typed"* — the mobile phone face-down in a drawer, the drawer closing, macro.
34. *"I want the low and lazy sound of you alive"* — the landline in the dark before it rings, held for four full seconds with nothing happening, locked-off.
35. *"Let it ring once this time, I'm already awake"* — her already sitting up in the dark, already looking at it, wide.
36. *"Been holding my real voice back for your sake"* — her hand on the handset before the first ring finishes, macro, the neon pulsing hard.

### Chorus 2 — the cord goes everywhere

37. *"Call me after midnight, that's when I'm all yours"* — her walking the flat with the cord stretched to its limit behind her, tracking from the front.
38. *"When the office goes dark and they lock all the doors"* — the window sign buzzing and flickering, macro, the source of every colour in the film.
39. *"Nobody wants a thing from me at half past two"* — her feet up the wall, upside down on the bed, handset at her ear, wide.
40. *"Nothing left to give, and I'm giving it to you"* — the cord hanging vertically from the bed edge and swinging, macro, slow.
41. *"Call me after midnight, let the line run long"* — a long slow camera move around the bed with her at the centre, the widest move so far.
42. *"Say it slow, say it wrong, keep the talking on"* — her laughing with no sound again, a different laugh, close-up.
43. *"Every hour before this one was the world's, not ours"* — the kitchen of the flat, dark, the cord running through the doorway from the bedroom, static.
44. *"Call me after midnight, that's when I'm all yours"* — her framed in the bedroom doorway with the cord across the frame, medium.

### Instrumental — suspended

45. The synth lead over the city: a slow pan across a skyline with almost every window dark, one plane light crossing.
46. The coiled cord in extreme macro, swinging, the neon moving through the plastic.
47. A bedside table with only the landline on it, nothing else, static, oddly formal.
48. Her half asleep on top of the covers, eyes almost shut, handset still at her ear, overhead, held long.
49. A drop to near-black with only the window sign lit — the cut into the bridge.

### Bridge — the two of her

50. *"The girl at noon is a highlight reel and a good coat"* — day grade: Mahima (day look) walking a corridor in the stone-grey blazer, flat light, professional smile, wide.
51. *"She says the right thing twice and never the rest"* — day grade: her saying the same sentence to two different people, identical delivery, cut together.
52. *"The one at two in the morning has a rougher throat"* — night grade: her in the magenta, hair down, no makeup, handset at her ear, close-up.
53. *"And she'll tell you the whole thing straight from her chest"* — night grade, closer: her actually saying something hard, no smile, one long take.
54. *"So if you want the real one, you know when to call"* — day and night cut against each other four times, each cut longer than the last, ending on night.
55. *"And nobody in daylight ever gets her at all"* — the night version held for eight full seconds without a cut, the longest single shot in the video.

### Final chorus — the window open

56. *"Call me after midnight, that's when I'm all yours"* — the window thrown open, the city cold and blue outside, the room hot magenta inside, wide.
57. *"When the office goes dark and they lock all the doors"* — the last lit office tower going dark across the skyline, seen from the open window.
58. *"Nobody wants a thing from me at half past two"* — her dancing slowly on her own with the handset at her ear, cord fully extended, medium, rising crane.
59. *"Nothing left to give, and I'm giving it to you"* — her spinning once and the cord wrapping around her, then unwrapping, wide.
60. *"Call me after midnight, let the line run long"* — the bed with the handset lying on the second pillow, nobody in the shot, static.
61. *"We can fall asleep together with the phone on"* — her lying down beside the handset on the pillow, facing it, close two-shot of a woman and a telephone.
62. *"Every hour before this one was the world's, not ours"* — the widest frame in the film: the whole bedroom, the open window, the city, the cord across the floor.
63. *"Call me after midnight, that's when I'm all yours"* — her face on the pillow in magenta, eyes open, listening, extreme close-up.

### Post-chorus — four beats

64. *"After midnight, after midnight, that's when I'm all yours"* — the handset, macro, hard cut on the gated snare.
65. *"Let it ring, let it ring, till the morning is ours"* — the window sign, macro, buzzing.
66. *"After midnight, after midnight, that's when I'm all yours"* — her mouth at the receiver, macro.
67. *"Call me, call me, the whole night is ours"* — the coiled cord, macro, still.

### Outro — dawn

68. *"Six in the morning and the line is still on"* — grey-blue first light arriving through the open window and beginning to kill the magenta, wide, slow.
69. *"You fell asleep first and I let it run long"* — Mahima on the floor with her back against the bed, handset at her ear, eyes closed, listening to breathing, medium.
70. *"The city's coming up and I'm still on the floor"* — the window sign switching itself off, the room going entirely neutral for the first time since shot 11.
71. *"Call me after midnight, and I'll answer once more"* — final shot: the handset lying on the carpet beside her, the cord running out of frame, the line still open, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the laptop closing, the hallway light at shot 11, each *"call me
after midnight"*, the stairwell at shot 27, the instrumental, the first day-
night cut at shot 50, the window opening at shot 56, and the sign going out.
At 96 BPM a bar is 2.50 s; choruses cut on the gated snare, the post-chorus
cuts on every snare, and the bridge alternation lengthens each time.

**The two-voices cut.** Post shots 50–55 vertical and invite people to film
their noon voice and their two-in-the-morning voice back to back, same
sentence, same camera. The second shareable frame is shot 17, the handset
coming up with the cord swinging, captioned *"Everybody gets the daylight.
You get the rest."*

## 6. Quality-control checklist

- Two looks, cleanly divided by shot 11: no neon in the daytime section and no white light in the night section, ever
- The man is never seen, never heard and never cut to; the video is one woman alone in a room
- The corded landline appears in every night frame from shot 14 onward; the mobile phone appears exactly twice, both times being pushed away
- The cord is the motion in this video — it swings, stretches or drags in at least one shot per section
- The window sign is a coloured light source with no readable characters; all badges, screens and clock faces composited
- The bridge alternation is four cuts, each longer than the last, ending on the night version held for eight seconds
- Neon pulse is a brightness oscillation added in the edit, matched to the arpeggio, not generated
- The last shot is locked-off and holds until the audio fades
