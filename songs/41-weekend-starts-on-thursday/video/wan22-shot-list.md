# Wan 2.2 Shot List — "Weekend Starts on Thursday"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
124 BPM a bar is 1.94 s, so most shots are 2–4 s and the choruses and
countdown chants cut on every bar or faster.

## 1. Visual style

Office-to-rooftop disco. Three worlds in one night: the **office** is flat,
fluorescent and slightly green, until one slice of evening sun crosses the
carpet; the **rooftop and the taxi** are golden hour into magenta into neon,
string lights and lens flare; the **dawn** is clean sunrise gold on an empty
rooftop. The **countdown fingers** are the repeating motif, five to one, in
the lift, at the bar, in the club and at sunrise. Handheld and quick in the
verses, slow motion and wide on the hook, locked-off on the Monday tag.

| Section | Grade | Camera |
|---|---|---|
| Intro / office | Flat fluorescent, faint green, one warm sun slice | Static, then quick cuts |
| Verse 1 (the week) | Each day flatter and greyer; the text brings the sun | Time-lapse, deadpan static |
| Pre-chorus (elevator) | Warm gold lift light, doors open on orange | Handheld, packed |
| Chorus 1 (rooftop sunset) | Golden hour to magenta, string lights on | Slow motion, wide |
| Post-chorus (countdown) | Magenta, flare | Cut on every number |
| Verse 2 (bar, taxi) | Blue hour, pink neon, taxi interior light | Handheld, funny |
| Chorus 2 (club, night rooftop) | Club colour, then night skyline | Tracking, wider |
| Instrumental | Sodium and neon, then pre-dawn grey-blue | Aerial, walking tracking |
| Bridge | Pre-dawn blue, one string of lights | Still two-shot |
| Final chorus / post-chorus | Sunrise gold flooding the rooftop | Slow motion, crane |
| Outro (Monday) | Warm lift, grey office, her smile | Locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (office, intro to pre-chorus 1)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back in a low ponytail, light office makeup, wearing a cream silk blouse tucked into high-waisted black trousers and flat shoes, bored then brightening expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (rooftop and taxi, chorus 1 to final chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and falling over one shoulder, glossy lips and a little sparkle on the cheekbones, wearing the same cream silk blouse untucked over the black trousers with gold heels and a fitted black blazer swung over one shoulder, laughing open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (Monday outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in a loose bun, minimal makeup, wearing large dark sunglasses, a grey knit sweater and black trousers, holding a takeaway coffee, small private smile, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man she texts, seen with a face from the rooftop on)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a white shirt with the sleeves rolled and a loosened navy tie, later the tie worn around his forehead, easy warm grin, realistic cinematic photography, consistent identity

**The crew** — two female friends from the office (one with a short bob and a red lip, one with braids and big hoops) and two male colleagues, all in end-of-work-day office clothes progressively undone. They are always a group; never more than six in the taxi.

**The taxi driver** — an older man, grey moustache, seen only in the rear-view mirror, deadpan then laughing.

Objects: the **wall clock** stuck at four fifty-nine, the **desk plant**, the **seven paper cups**, the **gold heels** swapped for flats, the **tie headband**, the **sharing plate**, the **taxi**, the **sunglasses**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the wall clock face, elevator floor numbers, the taxi
meter and the alarm screen are composited in the edit.** Generate the phone
as a lit blank screen and the clock as a blank dial; overlay the UI and the
numbers in post — the model cannot render legible UI, and the one-word text
and the countdown numbers are story beats.

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

Most shots 3–5 s.

For this song specifically: lock Kai with his own reference set (front,
three-quarter, with and without the tie headband). OpenPose for the rooftop
dance, the finger countdowns and the taxi squeeze; Depth for the open-plan
office and the rooftop wide shots. The countdown shots are 9:16 native.

## 4. Scene per lyric line

### Intro — the office at four fifty-nine

1. *"Four fifty-nine and the clock is stuck"* — Mahima (office look) at her desk, chin on her hand, lit by a monitor, eyes on a wall clock (blank dial, composited), the second hand seeming to hesitate, close-up, flat fluorescent light, static.
2. *"Fluorescent lights and I'm out of luck"* — a slow tilt up from her face to the ceiling grid of fluorescent tubes, one of them flickering, faint green cast.
3. *"Then a laptop shuts across the room"* — across the open-plan floor, one laptop lid snapping shut, heads lifting over the partitions like meerkats, wide.
4. *"And the whole floor starts to hum"* — her eyebrows lifting, the tiniest smile, and behind her two chairs rolling back at once, medium.
5. *"Somebody's phone lights up with a plan"* — a phone on a neighbouring desk buzzing and lighting (screen composited), a hand snatching it, close-up on the claps.
6. *"Somebody's already got a drink in hand"* — a colleague pulling a can from a mini fridge under a desk and cracking it, deadpan, medium.
7. *"Printer's jammed and I don't even care"* — the office printer flashing red, a stack of paper half out, Mahima walking past it without looking, tracking.
8. *"I can hear the weekend on the stairs"* — the stairwell door swinging open, laughter echoing up, a slice of warm evening sun falling across the grey carpet for the first time, wide.

### Verse 1 — the week, then the text

9. *"Monday was a marathon, Tuesday was a blur"* — Monday: Mahima jogging between glass meeting rooms with a stack of folders, then Tuesday: a time-lapse of her at the desk with the window light sweeping across the wall, two quick cuts, grey.
10. *"Wednesday I was talking to a plant that didn't care"* — her talking earnestly to a small desk plant that leans slightly away from her, deadpan close-up, flat light.
11. *"Coffee number seven going cold beside my screen"* — seven paper cups in a row beside the monitor, a slow pan along them, the last one steaming faintly.
12. *"Spreadsheet in my eyeballs, I forgot what colours mean"* — her face reflected in the monitor with a grid of cells ghosted over her eyes (composited), extreme close-up, everything grey.
13. *"Then a text from you, one word, out, no question mark"* — the phone on the desk lighting up (one-word message composited), her eyes dropping to it, the sun slice reaching her desk exactly on the cut, close-up.
14. *"And my heart does a drum roll like the party's about to start"* — her face changing, a grin breaking, a hand pressed to her chest, then a glance across the floor, medium close-up, warmer.
15. *"Heels under the desk, I'm swapping out my flats"* — under the desk: flats kicked off, gold heels pulled from a drawer and slipped on in one fluid move, low angle close-up.
16. *"Grab my jacket, grab the girls, and we are not coming back"* — her standing, black blazer swung over one shoulder, pointing at the two friends across the floor who are already standing, wide, the office suddenly full of movement.

### Pre-chorus 1 — the elevator

17. *"Lock the screen, kill the lights, let the inbox wait"* — three cuts on the claps: a screen locking, a hand slapping the light switch, a row of monitors going dark behind them, handheld.
18. *"Everybody grab a hand, we are not gonna be late"* — a chain of hands pulling each other into a packed elevator, the crew and Mahima squeezing in, the doors closing on a laughing face, medium.
19. *"Elevator going down, counting every floor"* — inside the lift, faces squashed together, everyone looking up at the floor numbers (composited), warm gold lift light, close handheld.
20. *"Ten, nine, eight, seven, we're already out the door"* — the crew shouting the numbers at the display, then the doors opening onto orange evening light and all of them spilling out, wide from outside.

### Chorus 1 — the rooftop at sunset

21. *"Weekend starts on Thursday when I'm with you"* — a cheat cut: the lift doors open straight onto a rooftop bar at sunset, the city orange and pink behind, Kai at the bar turning with two drinks, wide slow motion.
22. *"Friday is a rumour, Saturday can wait too"* — Mahima (rooftop look) walking toward him across the rooftop, heels clicking, the sun behind her head, tracking from the front.
23. *"First drink on the rooftop, sunset bleeding through"* — the first sip, the sunset seen through the glass, her eyes on Kai over the rim, close-up, flare.
24. *"Weekend starts on Thursday when I'm with you"* — her singing the hook straight to him, one hand on his tie, string lights along the bar switching on behind them, medium close-up.
25. *"Tell the boss I'm sorry, tell the week we're through"* — her blowing a kiss at the office towers on the skyline, then turning her back on them, medium.
26. *"Clocking out my worries, got better things to do"* — the crew arriving around them, a blazer thrown over a chair, a phone dropped face-down on the bar, quick cuts.
27. *"Glasses up, glasses up, one more for the crew"* — a slow-motion wide of the whole crew raising glasses against the magenta sky, the glasses catching the last sun.
28. *"Weekend starts on Thursday when I'm with you"* — Kai and Mahima clinking glasses, her laugh, the city lights beginning to come on below, medium two-shot.

### Post-chorus 1 — the countdown

29. *"Five, four, three, two, one"* — five hands, then four, three, two, one finger, straight at camera, cut on each number, magenta and flare, 9:16 native.
30. *"Thursday night, here we come"* — the crew jumping on the beat with the skyline behind, wide.
31. *"Five, four, three, two, one"* — Mahima alone doing the finger countdown to camera with a grin, close-up.
32. *"The week is done, the week is done"* — a glass slammed down on the bar on the last word, the drink jumping, extreme close-up.

### Verse 2 — the bar, the tie, the taxi

33. *"Rooftop bar and the speakers play a song from when we were seventeen"* — the rooftop an hour later, packed, deep blue sky, a speaker on a pole, the crew's faces lighting up at the first notes, wide.
34. *"You know every word, you sing it wrong, it's the best thing I have ever seen"* — Kai singing at the top of his lungs with the wrong words, Mahima filming him on her phone and laughing so hard she can't hold it steady, handheld.
35. *"Somebody ordered the sharing plate, nobody's sharing, it's a war"* — a sharing plate in the middle of the table, five forks fencing over the last piece, top-down.
36. *"Your tie is now a headband and I'm not sure what the tie was for"* — Kai with the navy tie knotted around his forehead, striking a serious pose, Mahima's hand covering her face, medium.
37. *"Taxi waiting with the meter on, six of us in a car for four"* — the street outside, a taxi at the kerb with the meter glowing (composited), six people trying to fit through two doors, wide.
38. *"Driver says he's seen it all, then he says he hasn't seen this before"* — the driver's face in the rear-view mirror, deadpan, then a small laugh, close-up.
39. *"Neon on your cheekbones, my mascara's holding on for dear life"* — the back seat, Mahima on Kai's lap, pink and blue neon sliding across his face, then an extreme close-up of her eye with mascara smudged, still laughing.
40. *"This is the night we'll be quoting back every time that Monday picks a fight"* — the taxi pulling away from the kerb into the neon street, the crew's hands out of the windows, tracking from behind.

### Pre-chorus 2 — the taxi countdown

41. *"Lock the screen, kill the lights, let the inbox wait"* — inside the moving taxi, Mahima turning her phone face-down on her knee, then the whole car swaying to the beat, handheld.
42. *"Everybody grab a hand, we are not gonna be late"* — six hands piled together on the middle of the back seat, close-up.
43. *"Next stop is downtown, driver, drop us at the door"* — the taxi pulling up outside a club door with a queue and a doorman, the crew spilling out, wide.
44. *"Ten, nine, eight, seven, we're already wanting more"* — the crew shouting the countdown at the street numbers above the door as they pass the queue, low angle.

### Chorus 2 — the club and the night rooftop

45. *"Weekend starts on Thursday when I'm with you"* — the club dance floor, the crew in the middle, Kai pulling Mahima into the light, wide with colour strobes.
46. *"Friday is a rumour, Saturday can wait too"* — reuse shot 22, now under club light, tighter.
47. *"First drink on the rooftop, sunset bleeding through"* — a fire escape outside the club, Mahima and Kai catching their breath, the city noise below, medium.
48. *"Weekend starts on Thursday when I'm with you"* — a second rooftop, a night one, the whole skyline lit, the crew arriving up a metal stair, wide crane.
49. *"Tell the boss I'm sorry, tell the week we're through"* — Mahima on the night rooftop pointing at the one dark office tower on the skyline and laughing, medium.
50. *"Clocking out my worries, got better things to do"* — her dancing with the two friends, heels in one hand, string lights overhead, handheld.
51. *"Glasses up, glasses up, one more for the crew"* — a bigger glasses-up on the night rooftop with the skyline behind, slow motion, more people than before.
52. *"Weekend starts on Thursday when I'm with you"* — Kai spinning her once under the lights, her hair flying, close tracking.

### Post-chorus 2 — the countdown, hands in the air

53. *"Five, four, three, two, one"* — the crew doing the finger countdown on the night rooftop, cut on each number, strobes.
54. *"Thursday night, here we come"* — a crowd behind them joining in, hands up, wide.
55. *"Five, four, three, two, one"* — Kai doing the countdown with the tie headband, deadly serious, close-up.
56. *"The week is done, the week is done"* — Mahima and the two friends collapsing into each other laughing, medium.

### Instrumental — the night in motion

57. An aerial of the taxi driving through a lit grid of city streets, sodium and neon, slow drift.
58. Mahima's gold heels in her hand, her bare feet on the pavement, tracking low.
59. A late food stop, chips shared out of one paper bag between six hands, close-up, steam.
60. The crew walking in a line down the middle of an empty street, arms linked, wide from the front.
61. The clap breakdown: the crew clapping on the rooftop against the first grey-blue of pre-dawn, then a filter sweep and the frame settling on Mahima and Kai alone at the edge — the cut into the bridge.

### Bridge — the alarm, the turn

62. *"There's an alarm set for seven, there's a meeting I forgot"* — the night rooftop almost empty, Mahima's phone showing an alarm set for seven (composited), pre-dawn blue, close-up.
63. *"There's a version of tomorrow where I'm paying for this a lot"* — her turning the phone face-down on the ledge with a shrug and a wince, medium.
64. *"But it was never about the calendar, never about the day"* — Kai looking at her, a long two-shot on the rooftop edge, the city going quiet below, still.
65. *"Every hour feels like the weekend when you're looking at me that way"* — his face, then hers, the smallest smile, one string of lights still on behind them, close-ups.
66. *"So I'll take the Monday headache, I'll take the Tuesday blues"* — her head on his shoulder, the horizon beginning to lighten, wide static.
67. *"As long as every Thursday is a Thursday spent with you"* — her lifting her head and saying it to him, close two-shot, warmer.
68. *"The week can have my mornings, it can have my nine to five"* — both standing as the claps return, the crew reappearing one by one behind them with the last drinks, medium.
69. *"But the nights belong to us and that's the part where I'm alive"* — the first orange line on the horizon behind the whole group, a slow push-in on Mahima's face lit by it.

### Final chorus — the last dance at sunrise

70. *"Weekend starts on Thursday when I'm with you"* — Mahima and Kai dancing in the middle of the empty rooftop as the sun clears the towers, crane pulling back, gold flooding in.
71. *"Friday is a rumour, Saturday can wait too"* — the two friends dancing barefoot with their shoes in their hands, sunrise behind, slow motion.
72. *"Last dance on the rooftop, morning coming through"* — Kai dipping her, the sun directly behind them, silhouette then flare, wide.
73. *"Weekend starts on Thursday when I'm with you"* — her singing the hook to him with the whole sky behind, close-up, gold.
74. *"Tell the boss I'm sorry, tell the week we're through"* — the office towers on the skyline now catching the sunrise, her looking at them without any fear, medium.
75. *"Clocking out my worries, got better things to do"* — the crew in a loose circle, arms around shoulders, swaying, wide.
76. *"Glasses up, glasses up, one more for the crew"* — the final glasses-up with the sunrise inside the glasses, slow motion, extreme close-up on the glass, then the faces.
77. *"Weekend starts on Thursday when I'm with you"* — Kai's forehead against hers, both laughing, the tie headband finally slipping off, close two-shot.

### Post-chorus 3 — the countdown, tired and happy

78. *"Five, four, three, two, one"* — the finger countdown done slowly and sleepily, sunrise behind, cut on each number.
79. *"Thursday night, here we come"* — Mahima mouthing it with her eyes closed, grinning, close-up.
80. *"Five, four, three, two, one"* — the crew's hands, then the empty glasses lined up on the ledge, top-down.
81. *"The week is done, the week is done"* — Mahima collapsing into a rooftop chair with a grin on the last word, full morning light, medium.

### Outro — Monday, sunglasses on

82. *"Monday's gonna find me with my sunglasses on"* — the office elevator on Monday morning, Mahima (Monday look) in dark sunglasses holding a coffee, the same crew faces around her also in sunglasses, warm lift light, locked-off.
83. *"Humming in the elevator, playing this song"* — her humming, a slight sway, the floor numbers going up (composited), the others trying not to laugh, medium.
84. *"Counting down the hours, counting down to you"* — a glance at her phone: one word from Kai (composited), her thumb hovering, then the sunglasses pushed up, close-up.
85. *"Weekend starts on Thursday, and Thursday starts with you"* — final shot: the doors opening onto the grey office and her walking in with a smile the office doesn't deserve, the wall clock behind her, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the laptop-shut click, the one-word text, the elevator doors
opening, each "weekend starts on Thursday", each countdown chant, the
instrumental, "never about the calendar", the sunrise dance and the final
"Thursday starts with you." At 124 BPM a bar is 1.94 s; the countdown
chants cut on every beat.

**The countdown challenge.** Post the vertical cut of shots 29–32 with
*"five, four, three, two, one"* and invite people to film their own
four-fifty-nine countdown: fingers at the clock, laptop shut on "done,"
lift doors opening on whatever their Thursday is. The lift-doors-to-rooftop
cheat cut (shot 21) is the hook frame, and *"Friday is a rumour, Saturday
can wait too"* is the caption line.

## 6. Quality-control checklist

- Three looks in the right sections: office ponytail and flats until shot 15, gold heels and loose hair from shot 16, sunglasses and bun only in the outro
- Kai's tie goes from loosened (chorus 1) to headband (shot 36 on) to off (shot 77); never on his neck again after shot 36
- The finger countdown is exact and cut on the numbers every time; no extra fingers in any countdown shot
- Never more than six people in the taxi and never fewer than four on the rooftop
- All screens, the wall clock, the lift numbers, the meter and the alarm composited; no model-generated text or digits
- The office is the only flat-lit world; every rooftop shot has practical string lights or real sun
- The sunrise only appears from shot 69 on; the bridge stays pre-dawn blue
- The last shot is locked-off in the grey office and holds until the audio fades
