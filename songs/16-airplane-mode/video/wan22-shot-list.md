# Wan 2.2 Shot List — "Airplane Mode"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
98 BPM a bar is 2.45 s, so shots run long — four to seven seconds — and the
edit almost never cuts inside a line.

## 1. Visual style

Real light, real places, no grade that could not have come out of the camera.
The film is built on **the two phones lying flat on a wooden table**, which
appear in every act, always from the same height and angle, always untouched.
Nothing dramatic happens in this video and it must never try to make
something happen: the camera holds, people finish their sentences, water
keeps moving. Three light worlds — the road, the cabin interior, the lake —
and one deliberately ugly frame, the city insert in the second pre-chorus,
which is the only cold, lit-from-above shot in the film.

| Section | Grade | Camera |
|---|---|---|
| Intro | Late sun through a dirty windshield, real | Windshield POV, static |
| Verse 1 | Low golden side light, dust in the air | Slow drifts, macro inserts |
| Pre-choruses | Golden hour, long shadows | Static, long holds |
| Choruses | Sunset to blue hour to firelight, all practical | Slow drifts, wide |
| Verse 2 | Hard midday sun off water, real flare | Handheld, then locked wide |
| City insert | Cold, overhead, unappealing | Static, two seconds |
| Instrumental | Blue hour into full dark, one lit window | Locked off, very slow |
| Bridge | Firelight and one lamp; the ridge cold | Static, single subject |
| Final chorus | Starlight and embers, then clean dawn | Slow tilt, wide |
| Outro | Flat morning light, no grade | Windshield POV, locked |

## 2. Character bible — paste into every prompt

**Mahima** (arrival and evenings)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly windblown, no makeup, wearing a cream cable-knit sweater and dark straight jeans with thick socks and no shoes, relaxed unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the lake, day two)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair wet and pushed back off her face, no makeup, wearing a dark green swimsuit under an open flannel shirt with a towel around her shoulders, bright open expression, realistic cinematic photography, consistent identity

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded brown work jacket over a grey thermal and canvas trousers, then swim shorts and a towel at the lake, easy quiet expression, realistic cinematic photography, consistent identity

There is no third character in this video. No neighbors, no strangers, no
faces on the ridge. The only other presence is the person who left the
postcards, and they are never shown.

Objects: **the key under the flat rock**, **the two phones flat on the wooden
table**, **the old whistling kettle**, **the drawer of postcards**, **the deck
of cards with two missing and two hand-drawn replacements**, **the woodstove**,
**the screen door**, **the dock**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every phone screen, the signal bars, the map and the postcards' handwriting
are composited in the edit.** Generate phones as dark or faintly lit blank
slabs and the postcards as blank card stock, then add the bars, the greying
map and the handwriting in post — the model cannot render legible interfaces
or script, and the bars dropping in the intro is the shot the whole song
hangs on.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA. This
video needs almost no pose control — OpenPose only for the lake entry and the
dive — but it needs **Depth on every cabin interior** so the small windows,
the table and the far wall keep their real distances. 16:9 throughout; the
9:16 recomposition is the table shot and the lake, both of which crop
vertically without losing anything. Animate the smallest possible amount:
steam off a mug, a curtain moving, water against a piling, firelight on a
ceiling, one shoulder roll. Resist the urge to add camera motion — half the
shots in this list are locked off on purpose.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–7 s. This is the longest average shot length in the catalogue.

## 4. Scene per lyric line

### Intro — losing the signal

1. *"Two hours out of the city and the bars start dropping"* — windshield POV from inside a car on a two-lane road, the last suburbs sliding past into trees, late sun, static.
2. *"One, then none, and the little map goes plain"* — the phone in the dashboard cradle losing bars one at a time and the map fading to blank grey (UI composited), extreme close-up.
3. *"You said we could turn back, I said keep driving"* — Kai at the wheel glancing across, Mahima in the passenger seat shaking her head once, medium two-shot, handheld.
4. *"And the radio gave up somewhere past the county line"* — a hand turning the radio dial through static and then off, then the road ahead with no sound cue at all, close-up to wide.

### Verse 1 — the cabin, and the table

5. *"The key was under a rock exactly where they said it was"* — a hand tipping a flat rock and lifting a key out of the dirt underneath, macro, low golden light.
6. *"The kettle's older than the both of us and whistles like a train"* — a battered enamel kettle going onto a stove ring, the burner catching, close-up.
7. *"There's a drawer of someone's postcards and a deck with two cards missing"* — a drawer pulled open and postcards fanned across it with a hand (handwriting composited), then a card deck with obvious gaps.
8. *"And a window with nothing in it but the water and the pines"* — a small cabin window filling the frame, the lake and pine treeline outside it, locked off, held.
9. *"You put your phone down on the table, screen flat, and slid it over"* — Kai's hand placing a phone screen-down on a wooden table and pushing it toward the middle, macro, the definitive angle for this shot.
10. *"I put mine beside it and we never said a word"* — Mahima's hand setting hers beside his, then both hands leaving frame, same angle, held two beats after they go.
11. *"Two whole days and nobody needs us, nobody knows"* — a wide of the table from above with the two phones and nothing else on it, the room around it empty.
12. *"And the quiet came in through the screen door like a guest"* — the screen door standing open onto the lake, light moving across the floorboards, no people, locked off.

### Pre-chorus 1 — putting the week down

13. *"There's a whole week in my shoulders that I'm setting on the floor"* — Mahima sitting on the porch steps and rolling her shoulders once, from behind, golden hour.
14. *"There's a hundred things unanswered and they'll all still be there"* — a bag dropped in a corner and conspicuously not unpacked, static, long shadow across it.
15. *"Let them wait, let them wonder where I've gone"* — her shoes coming off and being left by the door, macro, sunlight on the boards.
16. *"I have got somewhere better to be and it is right here"* — Mahima looking at the water for a long, uncut beat, profile, low sun.

### Chorus 1 — the evening

17. *"Put the world on airplane mode"* — the two of them on the porch with mugs, steam rising, wide, sunset behind them.
18. *"It's just you and me tonight"* — Kai building a fire in the woodstove badly, then better, close-up on hands and the first catch of flame.
19. *"No little lights, no half a conversation"* — the lake going flat and silver as the wind drops, locked-off wide, no people.
20. *"Nobody pulling on my sleeve to be somewhere else"* — a slow drift across the table: the two phones exactly where they were left, now with fire moving on their backs.
21. *"Let the sky keep whatever it was going to say"* — a tilt up from the porch rail to a sky going from orange to blue, held.
22. *"I am not taking anything today"* — Mahima laughing hard at something off-camera, unposed, close-up, firelight.
23. *"Put the world on airplane mode"* — the two of them side by side on the porch in blue hour, seen from behind, wide.
24. *"It's just you and me tonight"* — the cabin from outside with one window lit, the lake in the foreground, locked off, held.

### Verse 2 — the lake and the cards

25. *"Saturday the lake was cold enough to make me shout"* — Mahima (lake look) wading in to her waist and shouting at the cold, handheld, hard midday flare.
26. *"You went in like a lunatic and stayed in twice as long"* — Kai running past her down the dock and diving, one continuous shot, water everywhere.
27. *"We played that broken deck all afternoon and made the missing up"* — the incomplete deck laid out on the porch boards with two obviously hand-drawn replacement cards among them, macro.
28. *"You cheated, badly, and I let you have it anyway"* — Kai palming a card with no skill whatsoever, then Mahima seeing it and saying nothing, two-shot.
29. *"Then you asked me something small that I had spent a year avoiding"* — a wide two-shot from behind, both of them sitting on the dock with their legs in the water, no cut for the whole line.
30. *"And I answered it out loud because there was nowhere else to look"* — her face in profile, thinking longer than a music video usually allows, then speaking, close-up.
31. *"Turns out I have plenty to say when nothing interrupts"* — his face listening, not reacting, just listening, close-up.
32. *"Turns out I was never tired, I was only being reached"* — the same wide from behind, the two of them now sitting closer together than they were, held.

### Pre-chorus 2 — the boundary

33. *"There's a whole year in my jaw that I am putting down as well"* — Mahima alone at the window at dusk, unclenching, close-up, blue interior light.
34. *"There's a version of me answering at midnight in my head"* — the only city insert: a lit desk at midnight, a hand on a keyboard, shot cold and overhead and deliberately unappealing, two seconds.
35. *"She can wait, she can sit outside the door"* — hard cut back to the cabin: her hand closing the inner door on the porch, macro.
36. *"I'm not letting her back in until the drive home instead"* — Mahima turning back into the warm room, one lamp on, wide.

### Chorus 2 — night two

37. *"Put the world on airplane mode"* — firelight moving across the ceiling boards, locked off, no people, held.
38. *"It's just you and me tonight"* — reuse the table angle, night version: the two phones with the stove light on them.
39. *"No little lights, no half a conversation"* — Mahima's feet across Kai's lap on the couch, both of them reading, wide.
40. *"Nobody pulling on my sleeve to be somewhere else"* — the postcards spread on the floor between them, a hand sorting them, macro.
41. *"Let the sky keep whatever it was going to say"* — a slow push out through the screen door to the black lake, one lamp behind the camera.
42. *"I am not taking anything today"* — the stove door open, the fire down to bright coals, close-up.
43. *"Put the world on airplane mode"* — the two of them asleep in chairs with a blanket half over both, wide, one lamp.
44. *"It's just you and me tonight"* — the cabin from the water again, the same framing as shot 24, one window lit, locked off.

### Instrumental — outdoors, no people at first

45. Water moving against the dock pilings, macro, very slow, blue hour.
46. Wind moving through the tops of the pines, tilt up, no cut, held six seconds.
47. A bird crossing the frame left to right over the flat lake, wide, locked off.
48. The kettle beginning to steam on the stove, no whistle yet, close-up, warm.
49. A single long wide of the cabin from the water in full dark with one lit window — the cut into the bridge.

### Bridge — the ridge, and the refusal

50. *"Monday's coming for us both with all its little teeth"* — Mahima at the dark window with the fire behind her, static, her reflection faint in the glass.
51. *"There's a signal on the ridge if we walk up and let it in"* — the ridge above the cabin at night with one distant cold light on it, the only cold frame in the sequence, long lens.
52. *"But the fire's going and the kettle's going and you're reading me the postcards"* — Kai reading a postcard aloud with the stove behind him, warm, medium.
53. *"From people we will never meet, from summers we were not in"* — macro on a postcard held in his fingers, blank card stock with handwriting composited, out of focus behind it his mouth moving.
54. *"So the ridge can keep its one bar and the week can hold its breath"* — Mahima turning away from the window and sitting back down, one continuous move, wide.
55. *"I'll take the last of the quiet and I'll take it here with you"* — a hand putting another log into the stove and the door closing on it, macro, the fire flaring.

### Final chorus — the last night into dawn

56. *"Put the world on airplane mode"* — the two of them outside in blankets with the entire sky above them, very wide, starlight.
57. *"It's just you and me tonight"* — a slow tilt up from the porch rail to the stars, unbroken, six seconds.
58. *"No little lights, no half a conversation"* — the fire going down to embers, macro, the last orange in the frame.
59. *"Nobody pulling on my sleeve to be somewhere else"* — the two of them close under one blanket, seen from the side, quiet, medium.
60. *"Let the sky keep whatever it was going to say"* — first light: mist coming off the lake in sheets, locked-off wide, cold and clean.
61. *"I'll pick it up on Monday, not today"* — the table in daylight, the two phones untouched, same angle as shots 9, 11, 20 and 38, held longest here.
62. *"Put the world on airplane mode"* — Mahima on the porch in the cold dawn with a blanket around her and a mug, wide, breath visible.
63. *"It's just you and me tonight"* — Kai coming out with a second mug and sitting down beside her without speaking, wide, held.

### Post-chorus — four slow images

64. *"Airplane mode, airplane mode"* — the lake surface at dawn, macro, almost still water.
65. *"Nothing coming in and nothing going out"* — smoke leaving the chimney into a grey sky, tilt up, slow.
66. *"Airplane mode, airplane mode"* — the two phones, one last time, being picked up off the table at last, macro.
67. *"Just the water and the woodsmoke and your mouth"* — the two of them close in the open doorway, backlit by the lake, medium, the only kiss in the video.

### Outro — the drive down

68. *"We drove back down on Sunday and the bars came back like weather"* — the cabin door being locked and the key going back under the flat rock, macro, flat morning light.
69. *"Three at once, then a hundred, then a hum"* — the phone in the dashboard cradle lighting up as the signal returns, bars filling, notifications stacking (UI composited), extreme close-up.
70. *"You reached over and you slid my phone beneath the seat"* — Kai's hand reaching across, lifting the phone out of the cradle and sliding it under the passenger seat, one continuous move, macro.
71. *"And said not yet, and I said not yet, and we drove on"* — final shot: windshield POV of the road ahead, both of them quiet in frame edges, locked off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the bars dropping, the two phones going down (the loop point),
each *"put the world on airplane mode"*, the dock conversation, the
instrumental, the ridge light, the dawn mist, and the phone going under the
seat. At 98 BPM a bar is 2.45 s; nothing in this edit cuts faster than one
bar and most shots hold for two or three.

**The airplane-mode challenge.** The shareable cut is shots 9–12 and 61 back
to back: two phones going flat on a table, then the same table two days later
in daylight, with *"put the world on airplane mode"* on screen. Invite people
to post their own two-frame version — the phone going down and the signal
coming back. The second shareable frame is shot 70, the phone going under the
seat instead of being answered.

## 6. Quality-control checklist

- Two Mahima looks in the right sections: cable-knit for arrival and every evening, swimsuit and flannel only for shots 25–32
- The table shot is the same height, lens and angle every single time it appears (shots 9, 10, 11, 20, 38, 61, 66) — this is the spine of the video and any drift kills it
- The two phones are untouched and screen-down in every frame from shot 10 to shot 66, with no exceptions and no reflections that could read as a lit screen
- Exactly one cold, overhead, unappealing frame in the film (shot 34) and exactly one cold night frame (shot 51); everything else is warm or natural
- No third person anywhere, indoors or out; the ridge light has no figure in it
- All signal bars, maps, notifications and postcard handwriting composited in the edit; no model-generated text
- Camera motion stays minimal — if a shot can be locked off, lock it off; no shot cuts inside a sung line
- The last shot is locked off, nobody reaches for anything, and it holds until the audio fades
