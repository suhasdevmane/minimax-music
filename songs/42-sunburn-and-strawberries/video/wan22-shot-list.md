# Wan 2.2 Shot List — "Sunburn and Strawberries"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Eighty-three entries. This is an uptempo song: at 118 BPM a bar
is 2.03 s, so most shots run 2–4 s, the choruses cut on the bar and the
post-chorus chant cuts on the clap. Take timestamps from the rendered WAV.

## 1. Visual style

One Australian beach day from half five in the morning to headlights on the
coast road, shot as saturated film: blown highlights, deep blue water, white
sand, halation on every bright edge, visible grain. **The sun is the clock**
— blue pre-dawn, hard flat morning, brutal midday, then the good light from
verse two onward, then last light and headlights. Nothing is graded backwards
and no shot pretends to be a different hour than the one before it.

Handheld and close for the people, wide and still for the beach. Nobody in
this film is styled: the towels are old, the car is small, the esky-sized
cooler in the boot is somebody's dad's.

| Section | Grade | Camera |
|---|---|---|
| Intro | Blue pre-dawn into first orange on a windscreen | Static, then in-car |
| Verse 1 | Hard flat morning, blown highlights, sun down the lens | Handheld, fast |
| Pre-chorus 1 | Brutal high sun, high contrast | Faster handheld |
| Chorus 1 | Most saturated grade in the film | Running tracking, wides |
| Post-chorus | Same grade, hard cuts on the clap | Static macro |
| Verse 2 | Light going gold, shadows lengthening | Handheld, warmer |
| Pre-chorus 2 | Low sun, everything backlit | Handheld |
| Chorus 2 | Gold, glowing, long shadows | Wider, slower |
| Instrumental | Peak gold into one still frame | Fast cuts, then locked |
| Bridge | Same gold held longer, plus one cold flash | Static, unmoving |
| Final chorus | Sunset, the last of the gold, drone | Pull-backs |
| Outro | Last light and headlights, saturation dropping | In-car, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the whole day — one look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied up in a messy knot and salt-stiff by afternoon, no makeup, wearing a black one-piece swimsuit under an oversized faded blue shirt worn open, bare feet, sunburnt shoulders that deepen across the day, laughing open expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing green board shorts and a white t-shirt that comes off after the first chorus, a stripe of white zinc across his nose from the first verse onward, sunglasses pushed up on his head, easy grinning expression, realistic cinematic photography, consistent identity

**The group** — four more, all with faces, all specific and none styled: Kai's
younger brother who launches the footy into the water; a friend who sleeps
under a towel for most of the film; a friend who counts down the jetty queue;
a friend who is on their phone exactly once and gets shouted at for it.

**The seagull** is a character. It appears three times — sizing up the chips,
mid-theft, and unbothered on a bollard at sunset — and it should be the same
bird each time.

Objects that carry the film and must stay consistent: the **punnet of
strawberries** (six left by the outro), the **stripe of white zinc** on Kai's
nose, the **rubber thongs** abandoned in a line on hot sand, the **footy**,
the **ice-cream van** with the queue at its window, and the **shoe with sand
still in it** in the bridge.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The roadside stall sign, the car stereo display, the ice-cream van livery,
the phone screen in the bridge and every piece of beach signage are
composited in the edit.** Generate them blank or turned away — the model
cannot render legible text, and an unreadable half-formed sign is the fastest
way to make a saturated film look cheap.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and Kai with IP-Adapter or a character LoRA, and give the four
friends a lighter reference each — they recur across the whole day and the
group has to read as the same group at sunset as at eight in the morning.
**OpenPose for everything with water in it**: the run into the surf, the
jetty jump, the football throw, the chest-deep ice-cream shot. Depth for the
in-car interiors and the car park wide.

Water is the hard part. Generate surf and splash as short bursts of two to
three seconds and never ask for a continuous swimming shot; the jetty jump is
three separate clips — the countdown, the bodies in the air, the impact —
cut together. Sunburn deepening across the day is a grade decision in the
edit, not a prompt: shoot the same skin and warm and redden it progressively.

16:9 first; 9:16 for the chorus run and the jetty jump, which are the natural
vertical content.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — before dawn

1. *"Alarm at half five and the kettle's not on"* — a dark suburban street before dawn with one kitchen light on in one house, wide, static, blue.
2. *"Four of us awake and the boot's already done"* — a car boot slamming shut on towels, a footy and a folded chair, close, the interior light dying.
3. *"Punnet of strawberries from a stall on the road"* — a roadside stall with a hand-painted sign turned away from camera, a punnet passing through a car window into a hand, macro.
4. *"And a whole day in front of us and nowhere to go"* — the first orange light hitting a windscreen on an empty highway, from inside the car, low.

### Verse 1 — the drive and the arrival

5. *"The back window's stuck so we cop it all the way"* — a rear window jammed half open, the wind tearing through the back seat, hair everywhere, handheld.
6. *"Radio's cactus so we sing to fill the day"* — a car stereo with a dead blank display (composited), a hand slapping it once, then four mouths singing badly at once.
7. *"Sunnies on your head and your feet up on the dash"* — bare feet up on a dashboard with sunglasses pushed onto a forehead beside them, wide-lens interior.
8. *"And a bag of hot chips going cold in the back"* — a paper bag of chips on a back seat, a hand reaching into it without looking, macro.
9. *"Car park's full by eight and the sand is already hot"* — a beach car park completely full at eight in the morning, a slow pan across it, hard flat light.
10. *"Thongs off, straight in, and we don't check the spot"* — rubber thongs abandoned in a line on burning sand, then bare feet doing a fast painful run across it, low.
11. *"Your brother's launched the footy and it's landed in the drink"* — a football sailing out over the shallows and everybody on the sand watching it land, wide.
12. *"And a seagull's got a plan and it's closer than you think"* — a seagull in profile sidling up to an unattended bag, entirely unhurried, macro, static.
13. *"I put zinc across your nose and you just let me do it"* — Mahima drawing a stripe of white zinc across Kai's nose with one finger, extreme close-up, both of them still.
14. *"You don't say a word about it, but I know that you knew it"* — Kai not looking away, the smallest smile, her hand still up, close two-shot — the first flirt beat, entirely wordless.

### Pre-chorus 1 — the small chaos

15. *"Salt in everything, sand in the bread"* — a sandwich unwrapped and visibly full of sand, inspected for one beat, eaten anyway, macro.
16. *"Somebody's towel is on somebody's head"* — a friend asleep flat on their back with a towel over their entire head, static, held.
17. *"The jetty's got a queue and the queue's got a dare"* — a queue of teenagers along a wooden jetty rail, one of them counting down with a hand, from below.
18. *"And the whole day's going nowhere and I don't care"* — a wide from out in the water looking back at the beach, everything small and bright and loud.

### Chorus 1 — into the water

19. *"Sunburn and strawberries, that's my kind of summer"* — Mahima and the whole group running into the water, filmed from behind at knee height, spray everywhere.
20. *"Red on my shoulders and red on the back of my hands"* — red shoulders in close-up with a strap line already showing, salt drying white on the skin.
21. *"There's an ice-cream van doing the same eight bars"* — an ice-cream van parked on the grass above the sand with a queue at the window, wide, heat shimmer.
22. *"And a mile of nothing but water and sand"* — a very wide of a long empty beach with six tiny figures in it, locked-off.
23. *"Sunburn and strawberries, that's my kind of summer"* — strawberry-stained fingers held up to camera, red juice in the creases, macro.
24. *"Salt in my hair and my thongs going west"* — a single rubber thong floating out on the shallows, nobody chasing it, low on the water.
25. *"I'll be peeling by Wednesday and I'd do it all again"* — Mahima going under a wave and coming up laughing, filmed from the water, two beats.
26. *"Sunburn and strawberries, and today was the best"* — the six of them standing waist-deep in a rough line, all facing the horizon, wide from behind.

### Post-chorus 1 — the chant

27. *"Sunburn and strawberries, sunburn and strawberries"* — feet hitting wet sand, macro, hard cut on the clap.
28. *"That's my kind, that's my kind of summer"* — a strawberry going into a mouth, macro.
29. *"Sunburn and strawberries, sunburn and strawberries"* — a football spinning in the air against the sun, low.
30. *"Salt on my mouth and the sun going under"* — the ice-cream van window with a hand coming out of it, static.

### Verse 2 — the day refusing to end

31. *"Two o'clock and the tide has come a long way in"* — a tide line visibly halfway up a pile of belongings, the water arriving under a towel, macro.
32. *"Half our stuff is floating and we're laughing at the win"* — a bag, a hat and a book floating in six inches of water, nobody moving to save them, wide.
33. *"Your mum's on the phone about coming back for tea"* — Kai on the phone with one hand over his other ear, turned away from the noise, medium.
34. *"And you say, maybe, in a voice that means, not me"* — his face saying maybe in a way that means no, close-up, the grin arriving after.
35. *"Ice-cream van rolls up and plays the same eight bars"* — the van's roof speaker in macro, paint peeling, the sound implied.
36. *"Eleven of us queue with the coins we found in cars"* — a palm full of coins scraped out of a car cup holder, then a queue of eleven people with wet hair.
37. *"You take the one with bubblegum stuck on its nose"* — a gaudy ice-cream with a bubblegum nose held up against the sun, macro, backlit.
38. *"And you eat it in the water and you don't come in close"* — Kai chest-deep in the water twenty metres out, eating it, grinning back at shore, long lens.
39. *"Four o'clock, the good light, and nobody has moved"* — a wide of the whole group in exactly the same positions as an earlier wide, four hours of light later.
40. *"And a nothing sort of Saturday has got something to prove"* — Mahima's face in the low sun with her eyes closed, salt-stiff hair, close-up.

### Pre-chorus 2 — the dare

41. *"Salt in everything, sand in the cake"* — a supermarket cake, sandy, being cut with a car key, macro, absurd and correct.
42. *"Half the arvo gone and nobody's awake"* — three people asleep on towels at odd angles, one still with the towel over their head, wide.
43. *"The jetty's got a queue and the queue's got a dare"* — the jetty rail again, low sun through the boards, the queue shorter and braver now.
44. *"And I'm up on the rail and I'm already there"* — Mahima on the rail with her toes over the edge, arms out for balance, from below in the water.

### Chorus 2 — gold

45. *"Sunburn and strawberries, that's my kind of summer"* — the group in the water in low gold light, everything backlit, wide.
46. *"Red on my shoulders and red on the back of my hands"* — her shoulders again, visibly redder than shot 20, the same framing exactly.
47. *"There's an ice-cream van doing the same eight bars"* — the van from the beach side with the sun behind it, a queue of two now.
48. *"And a mile of nothing but water and sand"* — the same very wide as shot 22, four hours later, longer shadows, same frame.
49. *"Sunburn and strawberries, that's my kind of summer"* — the punnet on a towel with half the strawberries gone, macro, gold light.
50. *"Salt in my hair and my thongs going west"* — Mahima wringing her hair out with both hands, sun straight through it, close-up.
51. *"I'll be peeling by Wednesday and I'd do it all again"* — Kai carrying his brother on his shoulders into the shallows, both going over, wide.
52. *"Sunburn and strawberries, and today was the best"* — the six of them sitting in a line on the wet sand facing the sun, backs to camera, wide.

### Post-chorus 2 — same beats, later hour

53. *"Sunburn and strawberries, sunburn and strawberries"* — feet on wet sand again, gold light, same framing as shot 27.
54. *"That's my kind, that's my kind of summer"* — a strawberry going into a mouth, gold light, same framing as shot 28.
55. *"Sunburn and strawberries, sunburn and strawberries"* — the footy spinning against a low sun instead of a high one.
56. *"Salt on my mouth and the sun going under"* — the seagull on a bollard at sunset, entirely unbothered, static.

### Instrumental — the solo and the jump

57. A long slow track along the water line past everybody's abandoned stuff — towels, thongs, a book, the punnet — nobody in frame.
58. The jetty countdown: a hand going three, two, one, from below in the water.
59. The jump itself: three bodies in the air at once against the sky, shot from the water, slow motion for one beat.
60. The impact: three separate splashes, cut fast, water filling the lens.
61. A whistling group walking back up the sand in silhouette, then a hard drop to one very long still wide of the empty beach with the tide fully in.

### Bridge — the only cold frame in the film

62. *"You don't get told which day it is until it's done"* — two-second flash: a cold grey April street, a coat, a bus stop, no beach, desaturated — the only cold frame in the video.
63. *"You just wake up in April and you know that it's gone"* — hard cut back to the beach, gold, Mahima sitting on a towel with her arms around her knees, watching the others.
64. *"So I'm keeping the sand in my shoe and the strawberry stain"* — a canvas shoe on its side with sand still in it, macro, then a red stain on a shirt hem.
65. *"And the photo where your eyes are shut and mine are the same"* — a phone held up for a group photo (composited screen), at least three people with their eyes shut in it.
66. *"We'll be telling this one wrong for the next twenty years"* — the group already arguing about what just happened, all talking over each other, medium, funny and warm.
67. *"And nobody will fix it, and nobody cares"* — Mahima's face watching them argue, entirely content, the camera not moving for the first time in the film.

### Final chorus — sunset

68. *"Sunburn and strawberries, that's my kind of summer"* — a last run into the water fully clothed, all six, sunset behind, wide tracking.
69. *"Red on my shoulders and red on the back of my hands"* — her shoulders a third time, reddest, the same framing as shots 20 and 46.
70. *"Ice-cream van's gone and the car park's clear"* — the empty car park with one small car left in it, long shadows, static.
71. *"And a mile of nothing but water and sand"* — the same very wide a third time, sunset, the beach entirely theirs.
72. *"Sunburn and strawberries, that's my kind of summer"* — the whole group carrying everything up the sand at once, badly, dropping things, wide.
73. *"Salt in my hair and my sunnies gone west"* — a pair of sunglasses lying on the sand, forgotten, macro, a foot stepping past them.
74. *"I'll be peeling by Wednesday and I'd do it all again"* — Mahima and Kai last up the beach, not holding hands, walking close, from behind.
75. *"Sunburn and strawberries, and today was the best"* — a drone pull-back from six figures on an empty beach at sunset, rising and rising.

### Post-chorus 3 — the last chant

76. *"Sunburn and strawberries, sunburn and strawberries"* — feet on sand a third time, last light.
77. *"That's my kind, that's my kind of summer"* — the last strawberry going into a mouth.
78. *"Sunburn and strawberries, sunburn and strawberries"* — the footy going into the boot instead of the air.
79. *"Salt on my mouth and the sun going under"* — the sun actually going under the water line, locked-off, held.

### Outro — the coast road

80. *"Headlights on the coast road and the seats are all wet"* — headlights on a coast road at dusk, the ocean going dark on one side, from a following car.
81. *"Somebody's asleep with a towel on their head"* — the car interior: wet seats, sandy footwells, one person asleep under a towel exactly as in shot 16.
82. *"Half a punnet left and it's going hand to hand"* — the punnet with six strawberries in it being passed forward between seats, macro, dashboard light only.
83. *"Sunburn and strawberries, and a whole lot of sand"* — final shot: the car's tail lights going round a headland and out of frame, the empty beach behind it, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first surf-guitar note, the zinc stripe at shot 13, each
*"sunburn and strawberries"*, every post-chorus chant, the jetty jump at shot
59, the cold April flash at shot 62, the drone pull-back at shot 75, and the
tail lights. At 118 BPM a bar is 2.03 s; choruses cut on the bar, the chant
cuts on the clap, and the bridge holds each shot for two full bars.

**The zinc cut.** Post shots 13 and 14 vertical — the stripe going across the
nose and the not-looking-away — and invite people to film the moment they
knew a day was going to be the one. The second shareable frame is shot 59,
three bodies in the air off the jetty, captioned *"You don't get told which
day it is until it's gone."*

## 6. Quality-control checklist

- One look each for Mahima and Kai across the whole day; only the sunburn, the salt in the hair and the light change
- Sunburn deepens progressively and is checked at shots 20, 46 and 69, which share an identical framing
- The three matched wides — shots 22, 48 and 71 — are the same frame at three different hours and must line up exactly
- The seagull is the same bird in shots 12, 30 and 56
- The zinc stripe is on Kai's nose in every shot from 13 to the end
- Water shots are two-to-three-second bursts with OpenPose; the jetty jump is three clips, never one
- The roadside stall sign, stereo display, van livery and phone screen are composited; no model-generated text
- Australian detail stays real and unforced: thongs, a footy, a punnet, an ice-cream van, a jetty — no koalas, no postcards, no cliché
- The last shot is locked-off and holds until the audio fades
