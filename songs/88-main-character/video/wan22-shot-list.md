# Wan 2.2 Shot List — "Main Character"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
124 BPM a bar is 1.94 s, so most shots run 2–4 s and the choruses cut close
to every bar.

## 1. Visual style

A commute shot like the opening title sequence of a film. Three passes over
the same city: **morning** (clean gold, high contrast, hard shadows),
**office** (flat unflattering fluorescent, deliberately the least cinematic
place in the video), and **evening** (wet neon, saturated, rain on glass).
The camera grammar is the point — anonymous, waist-level handheld in the
memory flashes; a low ankle-height tracking shot the moment she decides;
long-lens wides for the post-choruses; one completely static locked-off
scene in the bridge. The city is never CGI-enhanced: scaffolding, steam,
puddles, revolving doors and pigeons do all the work.

| Section | Grade | Camera |
|---|---|---|
| Intro | Pre-dawn blue, one warm hallway sliver | Static, extreme close |
| Verse 1 memories | Flat, slightly grey, unflattering | Waist-level handheld |
| Verse 1 street | Blown-out white to clean gold | Low ankle-height tracking |
| Pre-choruses | Silhouette against low sun / headlights | Static on faces, then push-in |
| Chorus 1 & 2 | Golden morning, lens flare through scaffolding | Chest-height tracking |
| Post-choruses | Long morning shadows, warm one side | Long-lens wide, drone |
| Verse 2 | Flat fluorescent, one window shaft, then warm brick | Slow slides, static |
| Instrumental | Tunnel sodium, train fluorescent, first neon | Kinetic, feet and reflections |
| Bridge | Cold carriage fluorescent, tunnel strobe | Locked off, one slow push-in |
| Final chorus | Wet neon, deep saturation, practical only | Crane and drone pull-backs |
| Outro | Pre-dawn blue resolving to clean white | The intro framings, repeated |

## 2. Character bible — paste into every prompt

**Mahima** (morning commute — the primary look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair worn loose over her shoulders, minimal fresh makeup, wearing a long rust-orange wool coat open over a black turtleneck and straight jeans, white sneakers, headphones around her neck, calm focused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (office, verse two)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tucked behind one ear, minimal fresh makeup, wearing a cream knit and dark trousers with a lanyard badge on a navy strap, coat over the back of a chair, guarded then steady expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (evening, final chorus and bridge)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair slightly windblown, minimal fresh makeup, wearing the same long rust-orange wool coat belted, collar up, damp from light rain, open unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**The stranger in blue** (bridge only) — a woman in her fifties in a blue raincoat, reading a paperback on a subway bench seat, never interacting with Mahima, face fully visible and warm.

**Everyone else** — commuters, colleagues, the meeting table. Faceless or turned away: backs of heads, shoulders, hands, figures cropped at the jaw. **No ex, no romantic lead, no male co-star in this video.** Nobody but Mahima and the stranger in blue gets a face.

The **rust-orange coat** is the tracking device: it is the only saturated colour in any wide shot, and it is absent for the whole office sequence so its return at six in the evening reads as a costume change.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, notebooks, badges, name-badge misspellings, email windows,
crosswalk countdowns and shop signage are composited in the edit.** Generate
the laptop as a lit blank panel and the coffee cup as a plain unmarked cup,
then overlay in post — the model cannot render legible text, and the wrong
name on the cup and the deleted word in the email are two of the video's
best beats.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep every
other commuter's reference deliberately faceless. Keyframes first; OpenPose
for the crossing crowds and the two dance steps in chorus two; Depth for the
lobby, the carriage and the deep-perspective avenue shots. 16:9 first; 9:16
recomposition for the walk cuts, which are natural vertical content. Animate
conservatively: a coat catching wind, pigeons lifting, a countdown ticking,
one revolving-door rotation, wipers on the beat.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — blue room, the score starting

1. *"Alarm at six forty, blue in the room"* — extreme close-up of a phone face-down on a nightstand vibrating in a dark blue bedroom, her hand landing flat on it, static, macro.
2. *"Steam on the window, an unmade bed"* — wide of the small bedroom, sheets thrown back, a fogged window with the city grey behind it, nobody in frame for one beat, static.
3. *"Coffee in a paper cup, my name spelled wrong"* — close-up of a plain paper cup being set on a counter, her thumb turning it around (the misspelled name composited), a small unimpressed exhale.
4. *"Headphones in and the score comes on"* — over-the-shoulder as she seats one headphone, the room sound ducking, her eyes lifting to the door, close.
5. *"Roll it"* — hard cut to black for one frame on the wooden clapperboard hit, then her hand on the apartment door handle, static.

### Verse 1 — ten years of background, then the glass

6. *"Ten years of standing just outside the frame"* — memory, flat grey: Mahima at a party holding two other people's coats while a group laughs at the edge of frame, all faces turned away, waist-level handheld.
7. *"Holding a coat, remembering a name"* — memory: her shaking a stranger's hand and repeating a name she is clearly memorising, polite smile, handheld.
8. *"I was so good at background, so good at fine"* — memory: her clapping at somebody else's announcement in an office, third from the edge, half out of the shot, static wide.
9. *"Second row, third choice, back of the line"* — memory: a queue seen from behind, her at the end of it, stepping aside to let two people in front of her, flat light.
10. *"Then the elevator caught me in the glass"* — present: mirrored elevator walls, her reflection multiplied to infinity, doors closing, static, hard clean light.
11. *"And the girl looking back did not look past"* — extreme close-up on her eyes in the mirrored panel, holding her own gaze without blinking, slow push-in.
12. *"Something in my shoulders finally set"* — close on her shoulders dropping and then squaring inside the coat, the collar settling, side angle.
13. *"And the lobby doors opened like a silhouette"* — the lobby doors sliding open into blown-out white morning, her in full silhouette against it, static wide, backlit.
14. *"Wind off the avenue, coat coming loose"* — low ankle-height tracking shot as she steps out, the rust-orange coat catching the wind and flaring, feet in frame.
15. *"Pigeons hit the sky like they were cued to move"* — a plaza flock lifting off in one wave as she walks through, low angle, wings against the sun.
16. *"Somebody's playlist matched my walking speed"* — close-up on her hand adjusting the headphone, then her feet finding the beat exactly, split-second speed ramp.
17. *"And the whole street turned into an opening scene"* — the camera rising from ankle height to chest height as the avenue opens out ahead of her, deep perspective, gold.

### Pre-chorus 1 — the crosswalk

18. *"No audition, no note, no callback list"* — her waiting at the kerb in a packed crowd, everyone else facing forward and faceless, she is the only saturated colour, static.
19. *"Nobody is casting this, so I insist"* — close on the crossing signal counting down (composited numerals), the reflected red on her face.
20. *"Light turns green and the crowd divides"* — the crowd stepping off in both directions at once, a gap opening around her, high angle.
21. *"Cue the strings, hit my mark, I rise"* — her chin lifting, one step forward into the gap, slow-motion for exactly one beat, chest height.
22. *"Action"* — hard snap back to real time on the word, her foot hitting the white line of the crossing, macro on the shoe and the paint.

### Chorus 1 — the city as a set

23. *"Main character, and the city's my set"* — chest-height tracking shot leading her down the avenue, crowd flowing past on both sides, gold morning, lens flare.
24. *"Best scene of my life and I haven't shot it yet"* — a reverse of the same move, camera walking backwards ahead of her, her looking past the lens rather than at it.
25. *"Sun through the scaffolding, that is my key light"* — sun strobing between scaffolding poles across her face as she walks under it, side tracking, hard flicker.
26. *"Puddles under taxis holding all that bright"* — low macro of a taxi wheel rolling through a puddle in slow motion, gold light shattering across the water.
27. *"I'm not the friend in the doorway with the one good line"* — a doorway she passes, a faceless group inside laughing, she does not slow down, a quick pass-by.
28. *"Not the girl who waits on somebody else's sign"* — her reflection travelling across a run of shop windows, one continuous side-tracking move.
29. *"Nobody yelled cut, and I'm done with the regret"* — her descending subway stairs two at a time, the train arriving on the beat behind the pillars, tracking down.
30. *"Main character, and the city's my set"* — carriage doors opening exactly on the word, her stepping in, the doors framing her like a proscenium, static.

### Post-chorus 1 — the wide shot

31. *"Wide shot, chin up, coat in the wind"* — the first true wide: a long-lens shot of one rust-orange coat in a grey crowd on a boulevard, everything else compressed, static.
32. *"Wide shot, this is where the good part begins"* — drone rising above the same block, her a single moving dot of colour on the pavement grid.
33. *"Steam and the sirens and the crosswalk chime"* — steam venting off a grate behind her, an ambulance light passing across the buildings, no siren shown, long lens.
34. *"Everything out here sounds like a soundtrack of mine"* — close-up of her hand tapping the beat against her thigh as she walks, then the same rhythm in a hoarding being hammered.
35. *"Doors on the boulevard swing when I pass"* — a revolving door completing one rotation and throwing a bar of light across her as she passes it, side tracking.
36. *"Main character, main character at last"* — she stops at a corner, looks up the full height of a glass tower, and the camera cranes up with her eyeline, wide.

### Verse 2 — nineteenth floor

37. *"Nineteenth floor, my badge swings on the strap"* — slow-motion close-up of a lanyard badge (blank, composited) swinging against a cream knit as she walks a corridor.
38. *"Beige on beige and a coffee ring map"* — static wide of a beige corridor and a beige meeting room, a desk with overlapping coffee rings on the veneer, macro insert.
39. *"I used to fold my sentences inside a notebook"* — close-up of a notebook page dense with crossed-out lines, her hand closing it, flat fluorescent.
40. *"Rehearse them in the stairwell where nobody looked"* — a concrete fire stairwell, her mouthing words to nobody, hard vertical light from a landing window, static wide.
41. *"Today I said the one I had been saving all year"* — the meeting room, eight faceless colleagues around a table, her speaking, one shaft of window light landing only on her.
42. *"Table went quiet and I let it stay clear"* — the same table in silence, her not filling the gap, hands still, slow push-in on her face.
43. *"Somebody nodded and the meeting moved my way"* — a single nod from across the table, seen only as a shoulder and a chin, then papers turning toward her.
44. *"That is not a plot twist, that is just a Monday"* — a locked-off wide of the ordinary meeting room from the doorway, entirely undramatic, held.
45. *"Sent the email I rewrote about twelve times"* — over-the-shoulder on a lit blank laptop panel (draft composited), her cursor hovering.
46. *"Cut the word sorry and it read just fine"* — extreme close-up: the word deleted from the first line, then the send button pressed (both composited), her finger lifting.
47. *"Lunch on the fire escape, sun on the brick"* — her on a fire escape, shoes off, warm brick behind, a paper plate on her knees, wide from across the alley.
48. *"One slice, no company, and I did not feel sick"* — close-up on her eating, entirely comfortable alone, half a smile at nothing, warm light.
49. *"Walked home at six with the gold on the glass"* — the office door swinging shut behind her, then the rust-orange coat back on, the street ahead lit gold in every window.
50. *"And I never once checked who was watching me pass"* — a long tracking shot from behind, she never turns her head, the crowd irrelevant, golden hour.

### Pre-chorus 2 — the same crosswalk, twelve hours later

51. *"No stand in, no stunt double, no cue"* — the identical framing of shot 18 at dusk, the same kerb, the same crowd, headlight white instead of sun.
52. *"Nobody is writing this but me and the avenue"* — the countdown again (composited), now reflected in wet asphalt at her feet.
53. *"Light turns green and the crowd divides"* — reuse the high angle of shot 20, dusk grade, the gap opening wider.
54. *"Cue the strings, hit my mark, I rise"* — her chin lifting, but this time she is already smiling before she steps, one beat of slow motion.
55. *"Action"* — snap to real time, her shoe hitting the wet white line, the reflection breaking, macro.

### Chorus 2 — the evening version

56. *"Main character, and the city's my set"* — the chest-height tracking shot of shot 23 repeated down the same avenue at dusk, first neon coming on.
57. *"Best scene of my life and I haven't shot it yet"* — reuse the reverse walking move of shot 24, tighter, headlights flaring behind her.
58. *"Sun through the scaffolding, that is my key light"* — the same scaffolding now lit from below by amber work lamps, the flicker pattern inverted.
59. *"Puddles under taxis holding all that bright"* — a taxi through a puddle again, but the light shattering is neon red and green instead of gold.
60. *"I'm not the friend in the doorway with the one good line"* — a lit bar doorway, faceless group, warm spill across the pavement, she passes without slowing.
61. *"Not the girl who waits on somebody else's sign"* — the same run of shop windows as shot 28, her reflection now walking with visible swagger.
62. *"Nobody yelled cut, and I'm done with the regret"* — two actual dance steps on the pavement, unselfconscious, a passer-by glancing and looking away, handheld.
63. *"Main character, and the city's my set"* — she throws her arms wide for one beat under a streetlight, then drops them and walks on, static wide.

### Instrumental — the commute as pure movement

64. Feet on wet pavement in exact rhythm with the claps, macro, neon reflections breaking under each step.
65. A subway carriage window with her reflection strobing past tunnel pillars, the real tunnel and the reflected face fighting for the frame.
66. An escalator handrail from an extreme low angle, her hand riding it up into white light.
67. A revolving door spinning at speed, empty, light bars sweeping the lobby floor, locked off.
68. A crossing crowd in fast motion while she alone moves at normal speed through the middle of it, one long static wide.

### Bridge — the stranger in blue

69. *"For years I gave the good lines away for free"* — a half-empty late carriage, Mahima seated with the coat across her knees, completely still camera, cold fluorescent.
70. *"Made myself small so the room could breathe"* — a memory flash: her physically shifting her chair back from a table to make room, two seconds, grey.
71. *"Somebody else got the close up, I held the light"* — memory: her hands holding a phone up to film somebody else's moment, only her hands in frame.
72. *"And I called it being humble, and I called it right"* — back to the carriage, her looking down at her own hands, unmoving, static.
73. *"Now look at the woman across the aisle in blue"* — a woman in her fifties in a blue raincoat on the opposite bench, reading a paperback, warm and entirely self-contained.
74. *"Reading her book like the ending is overdue"* — slow push-in on the stranger's face as she turns a page, tunnel lights strobing across her.
75. *"She is the lead of a film I will never see"* — a two-shot of both women across the aisle, neither aware of the other, wide, held.
76. *"So let me be the lead of the one in front of me"* — back to Mahima, standing as the train slows, one hand on the pole, the carriage light steadying.
77. *"Everybody gets a set. This one is mine"* — she looks straight down the lens for exactly one beat on the last word, then the doors open behind her and the drums land.

### Final chorus — night, rain, widest

78. *"Main character, and the city's my set"* — she steps up out of the station into light rain and full neon, the widest frame of the video so far, crane rising.
79. *"Rain on a windshield is the best shot I'll get"* — through a bus windshield, wipers sweeping exactly on the beat, the street smearing and clearing.
80. *"Sun gone soft on the scaffolding, still my key light"* — the scaffolding under amber work lamps, rain falling through the light, she walks the length of it.
81. *"Neon in the puddles holding all that bright"* — macro of neon bleeding into a puddle, her boot entering frame and breaking it, slow motion.
82. *"I'm not the friend in the doorway with the one good line"* — she passes the bar doorway of shot 60 one more time and this time glances in and keeps going, easy.
83. *"Not the girl who waits on somebody else's sign"* — her reflection in a dark shop window walking alongside her, both in step, side tracking.
84. *"Nobody yelled cut, and I'm done with the regret"* — laughing, rain in her hair, head tipped back for one beat, chest-height handheld, closest shot of the chorus.
85. *"Main character, and the city's my set"* — drone pulling up and back over the whole block, her the one moving point of colour, rain visible in every streetlight.

### Post-chorus 2 — at crowd scale

86. *"Wide shot, chin up, coat in the wind"* — the long-lens wide of shot 31 at night, the crowd bigger, her coat the only warm colour in the frame.
87. *"Wide shot, this is where the good part begins"* — three strangers who happen to be walking in step with her, none of them looking at each other, wide.
88. *"Steam and the sirens and the crosswalk chime"* — steam and rain together off a grate, backlit into a column, she walks straight through it.
89. *"Everything out here sounds like a soundtrack of mine"* — quick cuts on the beat: a shutter rolling down, a bike bell, a hand on a railing, a heel on a step.
90. *"Doors on the boulevard swing when I pass"* — the revolving door of shot 35 at night, light bars sweeping, her passing without breaking stride.
91. *"Main character, main character at last"* — she stops on the corner, looks back down the avenue she has just walked, and turns forward again, static wide, held.

### Outro — the next morning

92. *"Alarm at six forty, blue in the room"* — the exact framing of shot 1 repeated: the same nightstand, the same hand landing on the same phone, blue.
93. *"Same cup, same name spelled wrong"* — the same paper cup, the same misspelling (composited), but she barely glances at it this time, close.
94. *"The door swings different when you know it's your scene"* — the apartment door opening, her stepping through without pausing at the handle, static.
95. *"Same old city, brand new song"* — the lobby doors of shot 13 opening into clean white morning, silhouette, the light a stop brighter than before.
96. *"Main character, and the city's my set"* — final shot: the low ankle-height tracking shot of shot 14, held long, the rust-orange coat catching the wind as she walks out of frame and the street keeps moving. Locked off through the fade. No text.

## 5. Edit and the challenge

Markers at: the clapperboard on *"roll it"*, the lobby doors, each *"main
character, and the city's my set"*, the crossing snap on *"action"*, the
deleted *"sorry"*, the instrumental, the look down the lens on *"this one is
mine"*, the station exit into the rain, and the final ankle-height walk. At
124 BPM a bar is 1.94 s; the choruses cut near enough every bar and the
post-choruses cut on the two-bar phrase.

**The wide-shot challenge.** The post-chorus is the shareable unit. Post the
vertical cut of shots 31–36 with *"wide shot, chin up, coat in the wind"* on
screen and invite people to film thirty seconds of their own commute at
chin-up walking pace, one coat, one crosswalk, no talking. **The hook
frame** is shot 14: the doors, the light, the coat, the step. **The quote
card** is shot 77.

## 6. Quality-control checklist

- Three looks in the right sections: rust-orange coat for morning and evening, no coat anywhere in the office sequence, coat belted and damp from shot 78 on
- The rust-orange coat is the only saturated colour in every wide shot; grade the crowd down if it competes
- Nobody but Mahima and the stranger in blue has a visible face; no male co-star anywhere in this video
- Every framing in the outro (92, 94, 95, 96) is a deliberate repeat of an intro or verse-one framing, matched to the pixel, one stop brighter
- All text composited: the cup, the badge, the notebook, the countdown, the email, the signage — no model-generated lettering
- Morning is hard gold, the office is flat fluorescent with exactly one window shaft, the evening is practical neon only
- No distorted hands in the macro inserts: the phone, the cup, the headphone, the send button
- The final shot is locked off at ankle height and holds until the audio fades
