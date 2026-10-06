# Wan 2.2 Shot List — "That Summer Song"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Sixty-eight lyric shots plus five for the instrumental, numbered
continuously. Timestamps come from the rendered WAV; cut on the sung line. At
110 BPM a bar is 2.18 s, so most shots run 3–5 s and the chorus alternates
worlds every bar.

## 1. Visual style

Two worlds, cut against each other inside the same bars. The **present** is a
late-night supermarket: flat fluorescent white with green in the shadows,
hard reflections in freezer glass, still or slow camera. The **summer** is
2.18-seconds-of-heaven overexposed gold, handheld, grainy, with tape flutter
and a slight halation on the highlights. The rule is that the summer never
looks like a filter applied to the present — it is shot wider, moves more,
and always has air in it. The supermarket has no air at all until the last
two shots, when the doors open.

| Section | Grade | Camera |
|---|---|---|
| Intro / the aisle | Flat cold fluorescent, green shadows | Static macro, slow tilt |
| Verse 1 / summer | Overexposed gold, grain, halation | Handheld, moving vehicle |
| Pre-choruses | Cold white, one colour accent | Static, locked wide |
| Choruses | Alternating gold and cold, one bar each | Whip cuts, tracking |
| Verse 2 | Cold inside, warm sodium through glass | Slow push through window |
| Instrumental | Cold, dimming one bank | Long dolly, overhead |
| Bridge | Single overhead bank, hard shadow | Static, half-time |
| Final chorus / post-chorus | Shop light warmed one degree | Tracking backwards, symmetrical |
| Outro | Sodium orange, headlights | Handheld, then locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (present day, twenty-six)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely with strands falling free, minimal natural makeup, wearing a soft cream knit cardigan over a plain white tee and straight-leg jeans, tired warm expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the summer, nineteen)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and wind-blown, sunburnt cheeks and no makeup, wearing a faded yellow tank top and denim cut-offs, open laughing expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man in the parking lot, present day — he has a face)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing an olive canvas jacket over a grey tee, car keys looped on one finger, easy unhurried expression, realistic cinematic photography, consistent identity

**The ex** — never shown clearly. In every summer shot he is a forearm on a
steering wheel, a mouth in close-up, a shoulder in the driver's seat, or a
figure cropped at the jaw.
> a young man in his early twenties, face out of frame or cropped at the jaw, sun-bleached hair, white vest

**The shop worker** — a woman in a green apron restocking the freezer chest.
The green apron is the only saturated colour in the present-day frames until
the final chorus.

Objects that repeat: the **bag of ice** (sweating, then dripping, then
carried out), the **stuck disc** in the car player, the **blue slush cup**,
the **ceiling speaker grille**, the **freezer glass** as a mirror.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, product labels, price signs, shop signage and the wedding post
are composited in the edit.** Generate the phone as a lit blank screen and the
shelves with unbranded packaging; the model cannot render legible text, and
the peas-and-wine gag in shot 40 depends on two readable labels.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA; keep the ex's
reference deliberately faceless. Keyframes first; OpenPose for the dancing
reflection and the walk down the aisle; Depth for the long freezer-aisle
dolly and the through-the-window compositions. 16:9 first; 9:16 for the
freezer-glass reflection cuts, which are the vertical hero shots. Animate
conservatively: condensation running, hair moving in a car window, a trolley
rolling through frame, a thumb scrolling.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the aisle, the ceiling speaker

1. *"Aisle five, quarter past nine,"* — wide static of a long empty supermarket freezer aisle at night, Mahima small at the far end with a basket, fluorescent hum, cold flat light.
2. *"A bag of ice going soft in my hand,"* — extreme macro of a clear bag of ice in her hand, condensation beading and running over her knuckles, shallow focus.
3. *"Four chords come down through the ceiling,"* — slow tilt up from her face to a dusty ceiling speaker grille, held two seconds longer than comfortable, static.
4. *"And the cold floor turns into sand."* — her shoes on shining vinyl floor, then the same framing with the floor now pale sand, one grain-of-sand ripple, match cut.

### Verse 1 — the borrowed car

5. *"That June we had a borrowed car and thirty dollars,"* — summer grade: a battered sedan on a two-lane road seen from a low chase angle, heat shimmer off the tarmac, handheld.
6. *"No air conditioning, so we rode with the windows down,"* — Mahima (nineteen) in the passenger seat, arm out flat riding the airflow, hair everywhere, laughing, handheld from the back seat.
7. *"One disc stuck in the player since the winter before,"* — close-up of a car stereo, a disc jammed half out of the slot, a finger jabbing the eject button and nothing happening.
8. *"Same eleven songs carried us out of that town,"* — the town falling away in a wing mirror, a water tower, a shut-up main street, gold light, handheld.
9. *"You knew the second verse before the radio did,"* — extreme close-up of the ex's mouth, cropped at the nose, shaping words ahead of the song, warm and grainy.
10. *"I learned it off your mouth at dusk."* — Mahima watching him and mouthing the words a half-second behind, forecourt lights coming on behind her, close-up.
11. *"Blue slush on our teeth, sunscreen on the seatbelt,"* — two quick cuts: a blue tongue in a phone-camera selfie framing, then a greasy seatbelt buckle with a thumbprint of sunscreen on it, macro.
12. *"A whole July that nobody could rush."* — wide: the car parked on gravel at dusk, both doors open, two pairs of legs hanging out, nobody moving, static.

### Pre-chorus 1 — the present pulls at her sleeve

13. *"Somebody's cart, somebody's kid asking for cereal,"* — present, locked wide: a trolley wheels through the foreground, a child's arm tugs a sleeve out of focus, Mahima motionless behind it all.
14. *"A green apron stacking bags of ice,"* — the shop worker in the green apron loading ice into the chest freezer behind her, the only colour in the frame, medium.
15. *"I could pay and walk out to the lot,"* — her hand resting on the trolley handle, not moving, then her feet, planted, two static close-ups.
16. *"But I stand in the cold and I don't think twice."* — push-in on her face, breath just visible in the freezer air, eyes closing for one beat.

### Chorus 1 — both times in the same bar

17. *"They're playing that summer song and I'm right back there,"* — whip cut: aisle wide to a full-speed shot down the road from inside the car, both framed identically, gold.
18. *"Salt on the dashboard, wind doing what it wants with my hair,"* — macro of dried salt crust across a black dashboard, then her hair whipping across her face at speed, two beats each.
19. *"Same cheap speakers, same wound-down glass,"* — a blown paper speaker cone in a door panel vibrating, then the glass wound fully down into the door, macro.
20. *"Same three long minutes we thought would last."* — the two of them driving, no dialogue, the ex cropped at the jaw, the road going on, wide handheld.
21. *"Half of me is holding a basket in the light,"* — present, static wide: Mahima alone in the aisle, basket at her side, absolutely still.
22. *"Half of me is nineteen and out of my mind,"* — the hero shot: her reflection in the freezer glass is the nineteen-year-old, dancing, while the real her stands still. Composite in-camera by shooting the reflection plate separately.
23. *"I don't want you back, I want the girl"* — her face in close-up, mouthing the line under her breath, half a smile, cold light.
24. *"Who thought a song could hold the world."* — pull back wide and high, the whole shop from the ceiling, one woman in it, held.

### Verse 2 — the man in the lot, the wedding

25. *"A good man's in the lot with my keys in his hand,"* — shot through the shop window: Kai leaning on a car in the parking lot, keys looped on one finger, warm sodium outside, cold white inside.
26. *"Texting his mother, warm, and nothing at all like you,"* — closer through the glass: Kai thumbing a message and smiling at it, entirely unbothered, slow push.
27. *"He wouldn't know this song if it played all night,"* — Mahima watching him through the window with real affection, her reflection overlaid on him in the glass, medium.
28. *"And I love that about him, and it stings a little too."* — her face only, the smile holding and something moving behind her eyes, close-up, static.
29. *"Somebody posted your wedding last fall and I scrolled it,"* — flashback, months ago, phone glow in a dark bedroom: a wedding post on the screen (composited, no clear faces), her thumb moving.
30. *"Tapped a heart with my thumb and I slept fine."* — the thumb double-taps and keeps scrolling without pausing, then the phone goes face-down on a duvet, macro.
31. *"Funny how a chorus knows where to find me,"* — present, her turning her head slowly toward the ceiling speaker again, low angle.
32. *"Right between the frozen peas and the wine."* — wide, symmetrical: she stands dead centre between a freezer of peas and a shelf of wine bottles, both labels composited and readable, deadpan.

### Pre-chorus 2 — the ice is going

33. *"The ice is going soft and there's water on my sleeve,"* — macro: meltwater running off the bag down her forearm, soaking the cardigan cuff, dripping onto the vinyl.
34. *"The girl in the green apron says the doors close at ten,"* — the shop worker gestures toward a clock (composited) and mouths something, Mahima nodding without moving, medium.
35. *"A whole life waiting under the streetlight,"* — through the automatic doors: Kai under a streetlight in the lot, patient, the brightest thing in the frame, long lens.
36. *"And I'm standing in this aisle being nineteen again."* — her from behind, small, centred in the aisle, static wide, the freezer glass throwing back the yellow tank top for one frame.

### Chorus 2 — deeper in

37. *"They're playing that summer song and I'm right back there,"* — reuse the whip cut from shot 17, but the summer side is now a motel pool at midnight, two people in it, gold.
38. *"Salt on the dashboard, wind doing what it wants with my hair,"* — new summer footage: the two of them asleep in the back seat at a rest stop, dawn coming through the rear window, handheld.
39. *"Same cheap speakers, same wound-down glass,"* — a hand writing on a paper cup on the car roof, sun behind, macro.
40. *"Same three long minutes we thought would last."* — a bonfire on gravel, not sand, sparks going up, the ex only a silhouette, wide.
41. *"Half of me is holding a basket in the light,"* — reuse shot 21, tighter, the basket now heavier.
42. *"Half of me is nineteen and out of my mind,"* — the freezer-glass reflection again, but this time the reflection is spinning and the real her has shifted her weight, one foot moving.
43. *"I don't want you back, I want the girl"* — extreme close-up on her eyes, the summer grade flickering across them for two frames.
44. *"Who thought a song could hold the world."* — she sets the basket down on the floor, framed low, and just stands there.

### Instrumental — the shop empties

45. Long slow dolly down the entire freezer aisle at her walking pace, the glass doors fogging one by one as she passes, cold light, no music-cutting, just motion.
46. The shop worker finishing the ice chest and wheeling the empty pallet away, the aisle now completely empty behind her, wide.
47. Mahima sitting on the edge of a low display, basket on the floor beside her, eyes closed, head tipped back, just listening, medium.
48. Overhead from the ceiling: the whole shop floor, one person in it, the aisles like a circuit board, slow drift.
49. One bar of near silence — the overhead lights drop by one bank, static close-up of her face, only the fluorescent hum audible. The cut into the bridge.

### Bridge — the years of skipping it, then the turn

50. *"For years I skipped it, thumb on the button before the drums,"* — cold present grade, static: a thumb hitting the skip control on a car steering wheel, hard and fast.
51. *"Changed the station, left the room, walked out."* — three half-second cuts: a hand twisting a kitchen radio dial; a door pulled shut; her leaving a bar mid-song with her coat still half on.
52. *"Tonight I stood in the freezer light and let it finish,"* — present, locked wide, she does not move at all for the length of the shot, single overhead bank, hard shadows.
53. *"And nothing broke, and the ice machine hummed some more."* — macro of the ice machine's compressor, vibrating, ordinary, indifferent, held.
54. *"It was never your song, it was never even ours,"* — the freezer-glass reflection: the nineteen-year-old stops dancing and turns to look straight out at her.
55. *"It was cheap gas, long light, the girl I used to be,"* — three summer stills coming alive one at a time: a pump handle, a long shadow across tarmac, her nineteen-year-old face turning to camera.
56. *"And she's not gone, she's only quieter now,"* — back to the glass: the reflection is now simply her, present day, cardigan and all, looking back.
57. *"She's out in the lot with a good man, waiting on me."* — through the doors to the lot, Kai still there, and Mahima already picking up the basket, drums returning.

### Final chorus — walking it out

58. *"They're playing that summer song and I'm right back there,"* — tracking backwards ahead of her as she walks the length of the aisle, ice bag swinging, shop light one degree warmer.
59. *"Salt on the dashboard, wind doing what it wants with my hair,"* — one last summer cut, the shortest of the video, half a second: her arm out the window, then straight back to the shop.
60. *"Same cheap speakers, same wound-down glass,"* — the ceiling speaker again, now shot heroically from below with the light behind it.
61. *"Same three long minutes we thought would last."* — a wide of the aisle with her walking away from camera, unhurried, the freezer doors clear now, not fogged.
62. *"All of me is standing in the freezer light,"* — static wide, she stops, turns to the glass and looks at her own present-day reflection deliberately.
63. *"And the girl I've been missing has been here the whole time,"* — close-up on the reflection and her real face in the same frame, both the same age, both calm.
64. *"I don't want you back, I have got the girl"* — at the checkout, unloading the basket, laughing once at herself, a cashier half in frame.
65. *"Who thought a song could hold the world."* — paying, the ice bag going into a paper sack, warm light, medium.

### Post-chorus — four bars of shop as a stage

66. *"Turn it up, turn it up over the frozen aisles,"* — symmetrical wide, dead centre of the aisle, her walking straight at camera with the paper bag, confident, tracking.
67. *"Let it play, let it play to the end of the line,"* — low angle past the ice chest as she passes, the fluorescents streaking overhead.
68. *"I'm not sad, I'm not sorry, I'm standing here"* — she stops at the end of the aisle, turns her head to the speaker one final time, and gives it the smallest nod.
69. *"With one whole summer of mine."* — the ceiling speaker, the last time, the frame dimming as the shop begins closing down.

### Outro — out through the doors

70. *"Out through the doors with a paper bag on my arm,"* — the automatic doors parting, warm night air hitting her, her hair moving for the first time in the present day, slow motion.
71. *"Humming the second verse under the lot lights,"* — her crossing the lot under sodium lamps, humming, the paper bag on her hip, tracking from the side.
72. *"He asks what took so long, I tell him nothing much,"* — Kai opening the passenger door, saying something, her shrugging and smiling, medium two-shot.
73. *"Just a song I used to know, and I get in."* — final shot: locked-off wide of the lot, the car pulling out, the shop sign receding, a different song faintly on their radio, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the ceiling speaker in shot 3, the sand match cut, each *"that
summer song"*, the freezer-glass reflection at shots 22 and 42, the
instrumental, the silent bar at 49, *"it was never your song"*, the warmed
grade at 58, and the doors opening at 70. At 110 BPM a bar is 2.18 s; the
choruses alternate worlds on the bar line, and shot 59 is a deliberate
half-bar cheat.

**The aisle-freeze challenge.** Post the vertical cut of shots 21–24 with
*"half of me is nineteen and out of my mind"* on screen, and invite people to
film themselves stopping dead wherever they are the second their summer song
comes on, then cutting to a photo from that summer. The freezer-glass double
reflection is the second shareable frame; the peas-and-wine shot is the
comment bait.

## 6. Quality-control checklist

- Two looks in the right worlds: cream cardigan present-day, yellow tank top only in summer footage and reflections — never the reverse
- The ex has no visible face in any frame; Kai has a face in every frame he appears in
- The green apron is the only saturated colour in present-day shots until shot 58, when the whole shop warms one degree
- Summer footage always has moving air in it; present-day footage has none until shot 70
- All labels, screens, clocks and signage composited; no model-generated text anywhere
- The freezer-glass reflection shots are plate composites, not a second generated person in frame — check for duplicated identity artefacts
- The ice bag melts continuously across the video: dry at shot 2, dripping by 33, in a paper sack by 65
- The last shot is locked-off and holds until the audio fades
