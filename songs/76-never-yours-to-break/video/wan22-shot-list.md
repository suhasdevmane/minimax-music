# Wan 2.2 Shot List — "Never Yours to Break"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
92 BPM a bar is 2.61 s, so most shots run 4–6 s — this is a slow, held video
and the cutting rate is the lowest in the catalogue.

## 1. Visual style

One glass house on a bare hill, one storm, one night into one morning.
**Stillness is the performance**: she barely moves in the entire video, and
every bit of motion is given to the weather, the light and the camera. The
architecture is the antagonist's answer — steel frame, full-height panes, a
roof beam, a junction box, all repeatedly shown intact. Wide, symmetrical,
composed. No handheld anywhere except the two flashbacks, which are
deliberately ugly.

| Section | Grade | Camera |
|---|---|---|
| Intro | Blue-black exterior, warm low interior, lightning frames | Extreme wides, locked-off |
| Verse 1 | Flat overcast daylight, one pointless warm lamp | Static, architectural |
| Pre-choruses | Storm light in, warm light behind camera | Slow corridor tracks |
| Choruses | Blazing interior gold against black exterior | Long lens from the valley, slow drifts |
| Verse 2 | Hard winter daylight, then warm crowded interiors | Static, then one gentle push |
| Instrumental | Blue-black with white strobe, then one lamp | Macro and one held wide |
| Bridge | Flashback sodium orange, handheld; present one lamp | Handheld once, then locked-off |
| Final chorus / post-chorus | First warm exterior light in the video | Drone rise, then one-beat cuts |
| Outro | Low gold morning, long shadows | Slow, still, mirrored to the intro |

## 2. Character bible — paste into every prompt

**Mahima** (the house, storm night — intro, verse 1, pre-choruses, choruses)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and perfectly still, no makeup, wearing a floor-length charcoal knit dress with long sleeves and bare feet, calm unflinching expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (winter, out in the world — verse 2)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down under a dark wool coat, light natural makeup and a deep red lip, wearing a black polo neck and a long dark wool coat, bright animated expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the flashback in the bridge — deliberately unglamorous)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark hair scraped back, no makeup, wearing a zipped hoodie in a parked car at night, exhausted hollow expression, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — never shown above the shoulders and never in the house. He
exists twice, both times as a storyteller elsewhere: gesturing hands at a
table, and a smaller group the second time.
> a young man in his twenties, cropped at the chin or shot from behind, dark jacket, hands gesturing while he talks

**The town** — a row of lit windows in a valley below the house, curtains
open at night, curtains closing at dawn. No individual faces; the town is a
single character seen only as light.

Objects that must stay continuous: the **pale rectangle** where a mirror
hung, the **ring in the dust** where a bowl of salt stood, the **old repaired
hairline crack** in one pane (visible in shots 12 and 74), the **empty
hanger**, the **steel frame**, the **roof beam**, the **one tree that goes
down** on the hill.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Any screen, car dashboard readout, street sign or house number is
composited in the edit.** There is very little UI in this video by design —
the only screens are a car stereo skipping a track in shot 32 and the
dashboard clock in the bridge flashback, and both are overlaid in post.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless. Depth is essential throughout — glass
interiors with a lit valley behind them collapse without it, and the model
will otherwise put the reflections in the wrong plane. Keyframes first;
OpenPose only for the walking-the-length-of-the-house shots. 16:9 first; 9:16
for the chorus cut, which is the shareable one. Animate conservatively: rain
sheeting down glass, a curtain of light moving across a floor, hair barely
lifting, one branch strike. **Lightning is done in the edit as a two-frame
white flash on a lit plate, never generatively.**

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s. The three extreme wides of the house (shots 1, 21, 75) are
generated from the same plate with different skies so the match cut reads.

## 4. Scene per lyric line

### Intro — the storm arrives

1. *"A house of glass at the edge of the hill"* — extreme wide from the valley: a single-storey glass house alone on a bare hill, lit from inside, black sky above, locked-off.
2. *"And the town waited to hear it come down"* — a row of lit windows in the town below, curtains open, silhouettes standing in them watching uphill, long lens.
3. *"Thunder came in like it had something to prove"* — the sky over the hill, cloud stacking fast, one lightning flash filling the frame for two frames, wide.
4. *"Wind on the panes, rattling the ground"* — rain hitting full-height glass in sheets from outside, the interior warm and blurred behind it, macro.
5. *"I stood in the middle, hands at my sides"* — interior: Mahima (storm look) standing dead centre in an empty room, hands loose, symmetrical wide, locked-off.
6. *"And let the sky throw all that it had"* — the same frame, a white lightning flash filling the room, her not flinching, hold two seconds after the flash.

### Verse 1 — the inventory and the story

7. *"You came in like a season, you left like a bill"* — daylight, flat and overcast: a pale rectangle on a wall where a mirror hung, static, centred.
8. *"Took the mirror off the wall, the salt off the sill"* — a windowsill with a clean ring in the dust where a bowl stood, macro, grey light.
9. *"Told your friends a version where I came apart"* — elsewhere: a table of three people leaning in, a man's gesturing hands cropped at the chin, warm pub light.
10. *"Where you did the holding and I did the harm"* — the listeners' faces reacting, sympathetic, one of them shaking their head, medium.
11. *"I was never once the thing that you dropped"* — back in the house: low angle along the floorboards toward her bare feet, wide.
12. *"I was the floor you stood on while you talked"* — the same low angle, pushing slowly along the floor to the wall, the whole span solid, static.
13. *"Every crack you point at, I put there myself"* — a hairline crack in one pane, clearly an old filled repair, macro, hard light raking across it.
14. *"Long before I heard your name from someone else"* — her thumb running along the repair once, then leaving, close-up.

### Pre-chorus 1 — the invitation

15. *"You tell it like a rescue that went wrong"* — the pub table again, the story getting bigger, hands wider, cropped at the chin.
16. *"Like the roof caved in the second you left"* — the roof beam of the glass house from directly beneath, absolutely intact, static, symmetrical.
17. *"Come and see it then, come stand in my doorway"* — the front door standing wide open onto the storm, rain coming in across the threshold, nobody there.
18. *"There's nothing on this floor to sweep up yet"* — a slow track down the corridor toward that open doorway across a completely clean floor.

### Chorus 1 — the house holds

19. *"You call it a wreckage, I call it a home"* — extreme wide from the valley: the glass house blazing with light in the worst of the storm, locked-off.
20. *"Windows intact and the lights still on"* — her walking the length of the house past every window, turning lamps on as she goes, long tracking from outside.
21. *"Say that you broke me if it helps you sleep"* — the same extreme wide as shot 1, now with every light on, the sky worse, the house brighter.
22. *"You never held a key, never held the deed"* — a close-up of the front door lock from inside, the key in it, her hand turning it once.
23. *"I was standing here before you learned my name"* — her standing at the largest pane with the storm inches away on the other side, from behind, wide.
24. *"Still in the storm, and I'm not the one who changed"* — the same frame reversed: her face through the wet glass from outside, unmoved, rain distorting.
25. *"Say it loud, say it twice, whatever it takes"* — a branch driven against a pane by the wind, the glass flexing and holding, slow motion. **The hook frame.**
26. *"My heart was never yours to break"* — pull back through the glass to the full interior, every light on, one still figure in the middle.

### Verse 2 — winter, elsewhere

27. *"Heard you tell it a different way this winter"* — the same pub table, a smaller group now, two people rather than three, cropped at the chin.
28. *"That the girl in your version got quieter each year"* — one listener checking the time and not really listening, medium, warm light going cold.
29. *"Funny, I've been loud in every room I walk in"* — Mahima (winter look, red lip, wool coat) walking into a full room and the room turning toward her, gentle push-in.
30. *"And none of them has watched me disappear"* — her mid-laugh at a long crowded table, entirely present, warm, medium.
31. *"You took a jacket and a playlist and a Sunday"* — an empty hanger swinging on a rail in an otherwise full wardrobe, macro.
32. *"And a couple of the words I don't say the same"* — a car stereo skipping a track (readout composited), her face not flickering at all, close-up.
33. *"You never took the roof, never touched the wiring"* — hard architectural cut: the roof beam, then a junction box, two static frames, cool light.
34. *"Never had a hand on the frame"* — the steel frame of the glass house from outside in winter light, snow on the hill, wide.

### Pre-chorus 2 — after the weather

35. *"You tell it like a rescue that went wrong"* — a knuckle rapping once on a pane from outside, nobody visible behind it, macro.
36. *"Like the ceiling came down when you were gone"* — the ceiling from directly below, intact, static, the same composition as shot 16.
37. *"Come and see it then, come knock on the glass"* — the open doorway again, this time with the storm pulling back and the floor dry, wide.
38. *"Same house, still standing, the storm already passed"* — the clouds moving off over the hill, first cold light at the horizon, long lens.

### Chorus 2 — settled

39. *"You call it a wreckage, I call it a home"* — from directly above: the house as a lit rectangle on a dark hill, drone, slow drift.
40. *"Windows intact and the lights still on"* — reuse the walking-the-length framing of shot 20, later, fewer lamps left to turn on.
41. *"Say that you broke me if it helps you sleep"* — the town's lit windows again, most of them dark now, people gone to bed, long lens.
42. *"You never held a key, never held the deed"* — the key coming out of the lock and going into her pocket, close-up.
43. *"I was standing here before you learned my name"* — her sitting down on the floor in the middle of the empty room, unhurried, wide.
44. *"Still in the storm, and I'm not the one who changed"* — her face in profile against the wet glass, absolutely still, close-up.
45. *"Say it loud, say it twice, whatever it takes"* — a second branch strike on a different pane, flex and hold, slow motion, tighter than shot 25.
46. *"My heart was never yours to break"* — the extreme valley wide again, dawn just starting at the edge of frame, locked-off, holding into the break.

### Instrumental — the storm peaks, no lyrics

47. Rain running down full-height glass in macro, the valley lights distorted and swimming behind it.
48. Lightning lighting the entire interior white for a single frame, her silhouette dead centre, then two seconds of darkness.
49. A tree going over on the hill outside, roots lifting, seen through glass from inside, wide.
50. Her still sitting on the floor while the storm peaks around the house, one lamp, static wide, no reaction at all.
51. One bar of near-silence: the room, water running off the roofline outside the frame, nothing moving — the cut into the bridge.

### Bridge — the admission

52. *"I won't pretend it didn't hurt, because it did"* — her sitting with her back against the glass, knees up, one lamp, close-up, the first vulnerable frame.
53. *"Months I couldn't hear your name out loud"* — flashback, handheld and ugly: her in a parked car at night, engine running, hands on the wheel, sodium orange.
54. *"Lost the sleep, lost the weight, lost a friend or two"* — the flashback continues: a dashboard clock (composited) reading late, an untouched takeaway bag on the passenger seat.
55. *"Sat outside a house I don't drive to now"* — an ordinary suburban house across the road from the car, one upstairs light on, seen through a rain-blurred windscreen.
56. *"But hurting isn't ruin, a bruise is not a wound"* — hard cut back to the present, locked-off, composed, her face lit by one lamp.
57. *"And nothing you carried out of here was mine"* — the empty hanger from shot 31 again, still swinging, macro, warm now.
58. *"You were weather. I have lived through harder weather."* — through the glass from outside: the storm on this side, her on that side, one frame, both in focus.
59. *"The lights are on in every window down the line"* — she stands, and lamps come up one after another down the length of the house — the cut into the final chorus.

### Final chorus — sunrise, modulation

60. *"You call it a wreckage, I call it a home"* — drone rise from the valley to the house as the sun comes over the hill, the first warm exterior light in the video.
61. *"Every light in every window, and I turned them on"* — her walking through the house switching the lamps off one at a time because she no longer needs them.
62. *"Say that you broke me if it helps you sleep"* — the town below, curtains closing, people going back to bed, long lens, gold.
63. *"You never held a key, never held the deed"* — her hand flat on the doorframe, the steel warm in the sun, macro.
64. *"I was standing here before you learned my name"* — the hill in gold with one tree down beside an untouched house, extreme wide.
65. *"Still in the sunrise, and I'm not the one who changed"* — her standing in the same dead-centre position as shot 5, now in sunlight, identical framing.
66. *"Say it loud, say it twice, whatever it takes"* — the pane that took the branch strike, unmarked, sun coming through it, macro.
67. *"My heart was never yours to break"* — a wide of the whole interior in morning light, one figure, nothing broken, slow push.

### Post-chorus — the list, one beat each

68. *"Never yours, never yours"* — a window, then a wall, two frames, one beat each, clean morning light.
69. *"Not the windows, not the walls, not the doors"* — a door handle, then a floorboard, then the roofline, three frames on the beat.
70. *"Never yours, never yours to take"* — the steel frame from outside, then the old repaired crack, two frames.
71. *"Never yours, and it never was yours to break"* — her hand closing the front door from the inside, one beat, then held.

### Outro — morning

72. *"A house of glass at the edge of the hill"* — the fallen tree on the hill in low gold light, being what it is, wide.
73. *"And the town got tired of waiting for the fall"* — the last open curtain in the town closing, long lens, warm.
74. *"Morning came in gold on the floor of the hall"* — gold light moving across the floorboards of the hall in real time, macro, the repaired crack catching it.
75. *"And it never was your house at all"* — final shot: the exact opening extreme wide from shot 1, now in sunlight, one tree down beside it, everything else identical, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first lightning flash, the mirror rectangle, each *"my heart
was never yours to break"*, the branch strike, the instrumental, the car
flashback, the sunrise drone rise, and the final wide. At 92 BPM a bar is
2.61 s; the choruses hold four to six seconds a shot and only the
post-chorus cuts on the beat, which is why the post-chorus lands as hard as
it does.

**The standing-still challenge.** Post the vertical cut of chorus one (shots
19–26) with *"my heart was never yours to break"* on screen and invite
people to post a single locked-off shot where the weather, the traffic or the
crowd does everything and they do nothing. The branch-strike frame (shot 25)
is the second shareable still.

## 6. Quality-control checklist

- Three looks in the right sections: charcoal knit and bare feet in the house, wool coat and red lip only in verse two, the hoodie only in the bridge flashback
- The ex is never shown above the shoulders and is never inside the house
- She moves as little as possible: no gesture larger than a hand on glass except the two walking shots and standing up in shot 59
- The four mirrored frame pairs match on lens, height and angle: 1/21/46/75, 5/65, 16/36, 31/57
- Lightning is a two-frame white flash added in the edit, never generated
- The glass never breaks, in any shot, at any point — the whole video is that promise
- All screens and readouts composited; no model-generated text anywhere
- Depth pass on every interior with the valley visible behind the glass, or the reflections land in the wrong plane
- The last shot is locked-off and holds until the audio fades
