# Wan 2.2 Shot List — "Two Time Zones"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
90 BPM a bar is 2.67 s, so most shots run 4–6 s. Many shots here are split
screen and are generated as **two plates composited in the edit**, never as
one generation.

## 1. Visual style

Two flats, eight hours apart, on one screen. **The split line is the story**:
it starts as a hard vertical wall in the intro, becomes a seam by the second
chorus, slides across the frame during the final chorus as her side takes
more of it, and is gone entirely at the meeting. Her side is cold blue
turning gold; his side is warm lamp against black. Every matched pair —
curtains, hands on windows, coats, doors, stairs, the moon — is framed
identically on both sides so the composite reads as one action.

| Section | Grade | Camera |
|---|---|---|
| Intro | Left cold blue pre-dawn, right warm lamp on black | Static split screen, locked-off |
| Verse 1 | Blue hour going warm, real streetlight | Handheld on her side, static on his |
| Pre-choruses | Flat daylight, then vast open sea | Static, then one aerial |
| Chorus 1 | Left gold sunrise, right deep blue midnight, matched exposure | Locked-off split, no camera move |
| Verse 2 | His warm and low, hers bright and cold | Static interiors, walking handheld |
| Chorus 2 | Both sides warmer, energy visibly up | Moving, matched motion both sides |
| Instrumental | Gold left, blue right, meeting at the seam | Macro clocks, one very high aerial |
| Bridge | One dark room lit by a laptop, then nothing | Static, close, the laptop light dying |
| Final chorus | Above cloud, hard airport light, daylight | Moving, the split line sliding |
| Post-chorus / outro | One light source for both, clean morning | Single frame, no split at all |

## 2. Character bible — paste into every prompt

**Mahima** (her side — intro through the flight)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slept-on, no makeup, wearing a chunky oatmeal jumper over striped pyjama trousers and thick socks, soft awake expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (travelling and the meeting — final chorus, post-chorus, outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back, light natural makeup, wearing a soft grey sweatshirt under a long camel coat with a backpack, tired excited expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead — his side throughout)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded navy t-shirt and a soft open flannel shirt, bare feet, warm sleepy expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the barrier and the outro)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a dark jacket over the same navy t-shirt, awake and searching expression, realistic cinematic photography, consistent identity

**No ex, no rival, no third character.** The only other people in this video
are anonymous commuters, an anonymous cabin, and an arrivals crowd — all
background, none held for more than a beat.

Objects that must stay continuous: the **two clocks on one wall** (her side,
seen in shots 5, 49, 79 and 81), **his lamp** (on at two in the morning,
still on in the bridge, off in the outro), the **coat on the empty chair**,
**his spare mug**, the **wall map with two pins**, the **wall calendar marked
in pen**, the **backpack**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the weather app, the two-city lock screen, the calendar marks,
the departures board and the boarding pass are composited in the edit.**
Generate phones and boards as lit blank surfaces. **Clock faces are the one
exception worth care**: generate real analogue clock faces with no numerals
visible, and set the hands in the edit — the two clocks reading the same time
in the final shot is the whole ending, and the model will not place hands
reliably.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai in both looks with IP-Adapter or a
character LoRA each. **Every split-screen shot is two separate generations
composited in the edit** — never prompt for a split screen, the model will
produce one incoherent room. Generate each side at full 16:9 and crop, so the
two halves match on lens height and eye line. Depth for the interiors;
OpenPose for the matched-motion pairs in chorus two, where both sides must
perform the same action on the same beat.

Animate conservatively: steam off a kettle, a curtain opening, a hand
flattening on glass, a second hand moving, breath in cold air. The three-second
hug in shot 77 should be generated as one continuous take at 121 frames rather
than assembled — it is the payoff and a cut inside it will kill it.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

## 4. Scene per lyric line

### Intro — two rooms, two clocks

1. *"It's ten past six and the kettle's going on"* — left frame only: a kettle switched on in cold blue pre-dawn, Mahima in a jumper over pyjamas, static.
2. *"It's ten past two and I'm nowhere near asleep"* — right frame only: Kai at a kitchen table under a single lamp, black window behind him, static.
3. *"I'm watching a sunrise you already had"* — full split screen for the first time: her at her window with the first gold on her face, his window black.
4. *"I'm holding a night that you don't get to keep"* — the split holds, he tips his chair back and looks at the ceiling, she pours water, both in their own halves.
5. *"There's a clock for me and a clock for you"* — her side: two analogue clocks side by side on one wall, both second hands moving, macro. **The motif.**
6. *"Hung on the same wall, both of them true"* — pull back to show the clocks over her kitchen table, the coat still on the spare chair, wide.
7. *"Same song playing, different light"* — tight two-shot across the split line, their heads either side of the seam, both listening to something.
8. *"Good morning, love. And good night."* — both of them saying it, matched framing, the seam between them dead centre, held.

### Verse 1 — her side

9. *"I keep your city on my weather screen"* — a phone lock screen with two cities and two temperatures (composited), her thumb resting on it, macro.
10. *"A place I've never stood but check for rain"* — her at a bus stop in first light, breath visible, checking the phone again, medium.
11. *"You send me photos of your street at midnight"* — a photo arriving of an empty street at midnight, filling the frame, then her face looking at it too long.
12. *"I send you the first bus and the light on the lane"* — her raising the phone to photograph a bus arriving in blue light, over-the-shoulder.
13. *"There's a chair in here that's yours and nobody sits there"* — the chair at her table with a coat still hanging on it, static, warm interior.
14. *"There's a mug in yours that nobody else can use"* — his side: he reaches past one mug for another and puts the first back where it was, close-up.
15. *"We've got the whole round world turning in between us"* — a departures board or a slowly turning globe, macro, no legible text.
16. *"And a line that drops out just when I need the news"* — both frames freeze mid-call at the same instant, the split screen going still, held two seconds.

### Pre-chorus 1 — the arithmetic

17. *"So I count the hours out on my hand"* — her counting on her fingers under a desk in the middle of a working day, close-up, flat daylight.
18. *"Take away eight and I know where you are"* — a wall map with two pins in it, macro, one hand touching the second pin.
19. *"There's an hour on the ocean that belongs to nobody"* — a very high aerial of open ocean at the hour that is neither of their days, slow drift.
20. *"And I think that's the hour that we share"* — the ocean holding, the light indeterminate, no cut, the last shot before the chorus.

### Chorus 1 — split screen, no drums

21. *"Two time zones, one heartbeat"* — both lying down with their heads at the split line so they appear to share a pillow across two cities, locked-off. **The hook frame.**
22. *"Your midnight leaning on my morning light"* — left gold sunrise on her face, right deep blue midnight on his, matched exposure, held.
23. *"I'll say good night while you say good morning"* — two curtains opening and closing in perfect sync either side of the seam.
24. *"And somewhere in the middle we get it right"* — two hands flat against two windows, palms meeting across the split line, macro.
25. *"Two time zones, one heartbeat"* — both of them turning over in their beds at the same moment, mirrored, wide.
26. *"Eight hours out and still in time"* — two kettles, two lamps, two chairs, three fast matched pairs across the seam.
27. *"Set the clocks however you want to"* — the two clocks from shot 5 again, the second hands now visibly out of phase, macro.
28. *"Two time zones, one heartbeat, one line"* — both frames holding, both people still, the seam the brightest thing in the picture.

### Verse 2 — his side

29. *"You left a voice note at your two in the morning"* — Kai recording a voice note at a dark kitchen table, talking too long, one lamp, static.
30. *"I heard it at seven with my coffee going cold"* — her at seven with headphones in, walking, a coffee going cold in the other hand, tracking.
31. *"You sounded tired and honest and unguarded"* — his face in the lamp light mid-sentence, unguarded, close-up.
32. *"And I played it twice again out on the road"* — her stopping dead on a pavement to play it again, commuters going round her, wide.
33. *"I marked the calendar in pen and not in pencil"* — a pen pressing hard on a wall calendar, a date circled twice (marks composited), macro.
34. *"Because pencil's for the maybes and I'm sure"* — a pencil set down beside it and deliberately not picked up, macro.
35. *"There's a moon out here that's already been above you"* — the same moon shot from his city, matched in size and frame position.
36. *"And it's carrying your evening to my door"* — the same moon from her city, cut back to back with shot 35, identical framing.

### Pre-chorus 2 — his arithmetic

37. *"So I count the hours out on my hand"* — Kai counting on his fingers on a night bus, sodium light across his face, close-up.
38. *"Take away eight and I'm already there"* — the wall map again, a thread now running between the two pins, macro.
39. *"There's an hour on the ocean that belongs to nobody"* — the open ocean again, this time with first light on it, high aerial.
40. *"And I've built a whole house for us in the air"* — a contrail crossing the dawn sky over the water, slow, wide.

### Chorus 2 — the drums arrive

41. *"Two time zones, one heartbeat"* — two coats going on either side of the seam on the same beat, matched motion, split screen.
42. *"Your midnight leaning on my morning light"* — two doors closing on the same beat, matched, split.
43. *"I'll say good night while you say good morning"* — two sets of stairs taken at the same pace, matched, split.
44. *"And somewhere in the middle we get it right"* — two streets walked in opposite directions across the seam, tracking both sides.
45. *"Two time zones, one heartbeat"* — the seam narrowing very slightly for the first time, both frames still equal, wide.
46. *"Eight hours out and still in time"* — her buying two coffees out of habit and looking at the second one, close-up.
47. *"Set the clocks however you want to"* — his hand adjusting one of two clocks on his own wall, macro.
48. *"Two time zones, one heartbeat, one line"* — both of them arriving home at their own ends of the day, matched, split, holding into the break.

### Instrumental — the world between, no lyrics

49. The two clocks on one wall, both second hands moving, drifting slowly out of sync, macro, held long.
50. An empty aeroplane cabin at night, one reading light on, nobody in the seats, slow track down the aisle.
51. A departures board flicking over row by row, macro, letters deliberately unreadable.
52. The dawn side and the night side of the planet from very high up, the terminator line crossing the frame.
53. One held bar of silence: the split screen with both frames empty, both rooms lit, nobody in either — the cut into the bridge.

### Bridge — the decision

54. *"I don't want to love you in a rectangle of light"* — her face lit only by a laptop screen in a dark room, close-up, static.
55. *"I want to hear you breathing in the same dark room"* — she closes the laptop mid-call, deliberately, and the room goes black except for a window.
56. *"I want an argument about who left the door open"* — her sitting in that dark with the closed laptop on her knees, wide, barely lit.
57. *"And the boring middle bit, and I want it soon"* — her thumb on a phone, one tap, a booking confirmed (composited), macro.
58. *"So I booked it. Aisle seat. Tuesday. Bag packed."* — the phone going face-down on the bed and a bag being pulled out of a wardrobe, two cuts.
59. *"Your morning and my morning on the same floor"* — his side: Kai asleep at the table with the lamp still on, not knowing yet, static.
60. *"One more night of two sunrises and never again"* — a passport going into a coat pocket, macro, one lamp.
61. *"And then it's one time zone, one door"* — the bag zipped closed by the door, wide — the cut into the final chorus.

### Final chorus — travelling, the split sliding

62. *"Two time zones, one heartbeat"* — an aisle seat from above, her sitting down, the cabin filling around her, medium.
63. *"Your midnight leaning on my morning light"* — a cabin window going light, the wing over cloud, the split line sliding to give her side more of the frame.
64. *"I'll say good night while you say good morning"* — his side, now the narrower half: Kai awake, checking a phone, not knowing.
65. *"And somewhere in the middle we get it right"* — the terminator line seen from the window at altitude, day meeting night out of the glass.
66. *"Two time zones, one heartbeat"* — the split line sliding further, her side almost the whole frame, hard airport light arriving.
67. *"Eight hours out but not for long"* — arrivals doors from inside, luggage, movement, handheld.
68. *"Set the clocks however you want to"* — a row of airport clocks on a wall showing different cities, macro, hands set in the edit.
69. *"Two time zones, one heartbeat, one song"* — Kai at the arrivals barrier checking his phone, still not looking up, the split line one thin strip.

### Post-chorus — the meeting, no split

70. *"Good morning, good night"* — he looks up, single frame, no split at all for the first time in the video, medium.
71. *"Same moon, different light"* — her seeing him from thirty feet away and starting to walk faster, tracking.
72. *"Good morning, good night"* — the backpack coming off her shoulder and hitting the floor, close-up.
73. *"Eight hours apart and holding tight"* — the hug beginning, wide, arrivals crowd blurred around them.
74. *"Good morning, good night"* — the hug continuing, one continuous take, close, three full seconds, no cut.
75. *"Two time zones, one heartbeat, one life"* — the bag still on the floor where she dropped it and nobody picking it up, macro, warm.

### Outro — one kitchen, one morning

76. *"It's ten past six and the kettle's going on"* — a kettle switched on, filmed exactly like shot 1, one light source, no split.
77. *"It's ten past two and I'm packing up my room"* — two mugs coming down from a shelf instead of one, close-up.
78. *"Same song playing, same light finally"* — both of them in one frame in one kitchen, out of focus in the background, warm.
79. *"No more counting backwards from the moon"* — the two clocks on the wall, still set to different times, a hand reaching up toward one.
80. *"Two time zones closing into one"* — the clock being taken down off the wall and held, macro, the wall behind it lighter where it hung.
81. *"Good morning, love. I'll see you soon."* — final shot: one clock on the wall, one pale rectangle beside it, the two of them out of focus behind, the kettle steaming, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first split, the two clocks, each *"two time zones, one
heartbeat"*, the frozen dropped call, the drums arriving in chorus two, the
instrumental, the laptop closing, the split line beginning to slide, the hug,
and the clock coming down. At 90 BPM a bar is 2.67 s; chorus one holds a shot
per bar with no camera movement at all, and chorus two moves on every bar
because the drums are finally there.

**The two-clocks challenge.** Post the vertical cut of chorus one (shots
21–28) with *"two time zones, one heartbeat"* on screen and invite people to
film the second clock on their wall set to somebody else's city — and to post
the day they take it down. The shared-pillow split (shot 21) is the still
that gets screenshotted.

## 6. Quality-control checklist

- Both leads recognisable in every shot; her oatmeal jumper on her side, his flannel and bare feet on his, the travel looks only from shot 62 on
- Every split-screen frame is two separate generations composited in the edit; nothing is prompted as a split screen
- The two halves match on lens height and eye line so the shared-pillow and hands-on-glass shots read as one action
- The split line is a hard wall in the intro, a seam by chorus two, sliding through the final chorus, and completely gone from shot 70 onward
- The drums arriving in chorus two must be visible in the cutting: no shot in chorus one moves the camera, every shot in chorus two does
- Clock hands are set in the edit, never model-generated; the ending depends on them
- All screens, boards and calendar marks composited; no model-generated text anywhere
- The hug in shot 74 is one continuous generation with no cut inside it
- The last shot is locked-off and holds until the audio fades
