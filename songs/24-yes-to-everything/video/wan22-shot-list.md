# Wan 2.2 Shot List — "Yes to Everything"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Uptempo: at 124 BPM a bar is 1.94 s, so most shots are 2–4 s
and the choruses and post-choruses cut on every bar or half-bar. Timestamps
come from the rendered WAV; cut on the sung line.

## 1. Visual style

One night, seven o'clock to sunrise, told in order. Three worlds: the
**planned evening** (bar patio, restaurant, the cab) is warm tungsten and
tidy framing; the **night of yeses** (karaoke, the fair, the wheel, the
diner) is saturated neon, strobe and handheld; the **sunrise** (the empty
lot, the wheel in daylight) is pale gold and wide. **Every yes is a new
location** — the choruses jump-cut on the word. The **ferris wheel** is the
motif: unlit in the intro, lit on the first ask, dark in the bridge, turning
in daylight at the end. Her **heels** come off at the diner and never go
back on.

| Section | Grade | Camera |
|---|---|---|
| Intro / verse 1 | Warm patio and restaurant tungsten, dusk blue | Static two-shots, close on the phone |
| Pre-choruses | Passing neon, diner warmth | Push-ins, handheld |
| Choruses | Saturated neon, strobe, the wheel's white bulbs | Jump cuts on every yes, whip pans |
| Post-choruses | Strobe, four fast inserts | Ultra-fast jump cuts |
| Verse 2 | Bar neon, street, fair half-dimmed, diner fluorescent | Handheld, tracking, then still at the top |
| Instrumental | Most saturated section, long exposures | Slow-mo and impact cuts |
| Rap verse | Blue pre-dawn, a bakery's warm window | One steadicam tracking shot, inserts |
| Bridge | Pale gold sunrise, long shadows, the wheel dark | Wide static, slow push-in |
| Final chorus / post-chorus / outro | Full golden morning | Crane up, gondola two-shots |

## 2. Character bible — paste into every prompt

**Mahima** (the plan — intro, verse 1, pre-chorus 1)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned up neatly, light polished makeup, wearing a fitted emerald satin mini dress under a cropped black leather jacket with black heels and a small black bag, polite contained expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the night of yeses — choruses, verse 2, instrumental)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and windblown, makeup slightly softened, wearing the emerald satin mini dress with the leather jacket tied at her waist, a paper fairground wristband on her wrist, heels in one hand from the diner on, wide-open laughing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (sunrise — rap verse, bridge, final chorus, outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and a little flattened, makeup worn soft, wearing an oversized light-wash denim jacket over the emerald dress, barefoot, heels carried or set beside her, tired glowing expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the date)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a white t-shirt under an oversized light-wash denim jacket and dark jeans, a paper fairground wristband, easy grinning expression, hands often open as if offering something, realistic cinematic photography, consistent identity

From the rap verse on, **his denim jacket is on her**; he is in the white
t-shirt.

**The girls** — never seen in person: a group chat on her phone (composited), and one voice note. **The cab driver**, **the ticket-booth man**, **the ride operator** and **the diner waitress** are single-shot supporting faces who never pull focus.

Objects: the **ferris wheel** (unlit, lit, dark, turning in daylight), the
**karaoke mic**, the **paper wristband**, the **yellow cab** and its meter,
the **stack of pancakes** and the syrup on his sleeve, her **heels**, one
**balloon** in the empty lot.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the group chat, the ride app, the two-percent battery,
the cab meter digits, the karaoke lyric screen, the clock faces and the bar
sign are composited in the edit.** Generate the phone as a lit blank screen
in her hand, the karaoke screen as a glowing blank, the meter as a soft red
glow, and overlay the UI in post — the model cannot render legible UI.

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

Most shots 2–4 s. For this song: Kai locked with his own LoRA; OpenPose on
the karaoke stage, the run for the gate and every dance shot; Depth for the
wheel gondola and the wide fairground plates. The ferris wheel is best a
single lit plate with a brightness ramp in the edit; do not ask the model
to switch it on.

## 4. Scene per lyric line

### Intro — seven o'clock, the plan

1. *"Seven o'clock, I told my girls I'd be home by ten"* — a bar patio at dusk, Mahima (plan look) at a table with one drink, her phone in her lap under the table, a group chat lit on it (composited), her thumb typing, close-up, warm patio bulbs.
2. *"Told myself, one drink, then leave"* — a medium two-shot from the side: her sitting very upright with the drink, Kai leaning back easy, an unlit ferris wheel over the rooftops behind his shoulder.
3. *"You said, you ever been up a ferris wheel at night"* — the ferris wheel's lights switching on in the distance behind him as he asks, rack focus from his grin to the wheel.
4. *"And I heard my own mouth go, yeah, why not, let's see"* — her face: a beat of absolutely not, then her mouth saying yes before her brain does, extreme close-up, dusk blue.

### Verse 1 — the planner, the dare, the cab

5. *"I'm the girl with the plan, with the list, with the alarm"* — a restaurant table, her phone face-up beside her plate with a ride app countdown (composited), her eyes flicking to it, close-up, candle light.
6. *"Ride booked home before I even sit down"* — her sliding into the booth while already tapping the phone, Kai watching with an eyebrow up, over-the-shoulder.
7. *"You ordered the thing on the menu that I couldn't say"* — a small plate arriving, Kai sliding it across the table with two fingers, macro on the plate then his face.
8. *"Then you dared me to try it, and I didn't back down"* — her fork hovering, then eating it and refusing to react, his laugh, then her thumb cancelling the ride on the phone without looking at it (composited), close-up.
9. *"Now there's a cab outside and the meter's running slow"* — a yellow cab at the kerb, the meter a soft red glow (digits composited), Kai half in the door holding it open, wide, street sodium.
10. *"And you said, there's a bar with a mic and a bad crowd"* — Kai leaning out of the cab door asking, pointing down the street, the dome light on his face, medium.
11. *"Every sensible cell in my body said no"* — a slow push-in on Mahima on the pavement with her arms crossed, every no lining up behind her eyes.
12. *"But the word that came out of me was pretty loud"* — her saying yes so loudly the cab driver looks round in the mirror, then her getting in, handheld.

### Pre-chorus 1 — okay, okay

13. *"Okay, okay, I know how this goes"* — the back of the cab, city lights sliding across both faces, her talking to the window, medium two-shot.
14. *"I'm the one who says maybe, I'm the one who says no"* — her counting her own rules off on her fingers, Kai's grin in the window's reflection, close-up.
15. *"But you've got a grin like you already know"* — the cab pulling up outside a karaoke bar with a buzzing sign (abstract glow, no text), his grin in profile, pink and green spill.
16. *"And I'm so tired of maybe, so here we go"* — her hand on the bar's door handle, a held beat as the kick drops out, then pushing it open on the last word, the light flooding out.

### Chorus 1 — the drop, every yes a new place

17. *"Tonight I'm saying yes to everything"* — the drop: Mahima (night look, jacket off, hair down for the first time) on the karaoke stage with the mic in a bad crowd, the whole room bouncing, wide, strobe.
18. *"Yes to the wheel, yes to the lights, yes to the spin"* — three jump cuts on the beat: the lit ferris wheel from below; a ride's lights streaking; a spinning ride with her hair flying.
19. *"Yes to the mic, yes to the song I don't know"* — her with the mic, eyes on the blank glowing karaoke screen (lyrics composited), singing the wrong words with total commitment, close-up.
20. *"Yes to the worst idea you've got, let's go"* — Kai pointing at something off-frame with a terrible-idea grin, her grabbing his hand and going, tracking.
21. *"Tonight I'm saying yes to everything"* — the two of them bursting out of the bar door onto the street, the crowd's cheer behind them, wide, neon.
22. *"No to the plan, no to the clock, no to the ten"* — three inserts on the beat: her list crumpled in a fist; a wall clock (face composited); a phone alarm dismissed with a swipe (composited).
23. *"Ask me again, ask me anything"* — her walking backwards in front of him down the street, arms out, asking for the next dare, handheld.
24. *"Tonight I'm saying yes, yes, yes to everything"* — three jump cuts of her nodding yes in three places: the bar, the street, the fair gate, then a whip pan to the wheel.

### Post-chorus 1 — the yes chant

25. *"Yes, yes, yes, yes, say it again"* — jump cuts on every yes: the same frame of her at camera in a different pose, hands up, chin down, a wink, a point.
26. *"Yes, yes, yes, yes, where have you been"* — four inserts: the crowd's hands up; a paper wristband snapped onto her wrist; a coin into a ride slot; his open hand.
27. *"Yes, yes, yes, yes, to everything"* — the two of them on a spinning ride with no one else on it, the operator bored, strobing lights, wide.
28. *"Ask me, ask me, yes to everything"* — her face to camera nodding yes, extreme close-up, the wheel's bulbs behind her.

### Verse 2 — karaoke, the gate, the wheel, the diner

29. *"You picked the worst song on the whole machine"* — back at the bar: Kai scrolling the karaoke machine to the worst possible song (screen composited), her groaning with her whole body, medium.
30. *"I knew half the words and the bar knew the rest"* — her belting on the stage, the whole bar taking the chorus for her, hands up, handheld in the crowd.
31. *"We ran for the gate when the fair was closing"* — a tracking shot of the two of them running hand in hand down a street toward the fairground gate as its lights start going off, her heels in her hand for the first time.
32. *"The guy in the booth just laughed, said, you two are a mess"* — the ticket booth, an older man laughing and waving them through anyway, snapping a wristband on her wrist, close-up on the hands.
33. *"Top of the wheel, the whole city went still"* — a wide from outside the gondola: the wheel stopped, the two of them tiny at the top, the city spread out, the wind, static.
34. *"You said, don't look down, so I looked at you instead"* — inside the gondola, a close two-shot: Kai saying it with a small grin, her already looking at him, the city's glow below.
35. *"Three a.m. diner, a stack I didn't need"* — a diner booth, a stack of pancakes set down, her bare feet up on the seat, warm fluorescent, medium.
36. *"Syrup on your sleeve and my heels under the seat"* — macro of syrup on his denim sleeve, then a low angle under the table: her heels kicked off, her bare feet.

### Pre-chorus 2 — two percent

37. *"Okay, okay, I know how this goes"* — the diner booth, her phone on the table showing two percent (composited), a stack of missed messages, her shrug, close-up.
38. *"I had a curfew, I had a cab, I had a no"* — three quick inserts: the alarm she dismissed; the cab; her own no face from the pavement earlier, then her laughing at all three.
39. *"But my phone's at two percent and I don't even know"* — her turning the phone face down with one finger, looking at him, medium.
40. *"What time it is, and I don't wanna know, so here we go"* — both of them sliding out of the booth, her carrying her heels, Kai leaving cash on the table, the door chiming, blue pre-dawn through the glass.

### Chorus 2 — the night as a playground

41. *"Tonight I'm saying yes to everything"* — the ferris wheel from below at full light, the two of them in a gondola rising, wide, the brightest frame so far.
42. *"Yes to the wheel, yes to the lights, yes to the spin"* — reuse shot 18, three new angles, tighter on her hair flying.
43. *"Yes to the mic, yes to the song I don't know"* — her dancing in the diner aisle with a fork as a mic, the waitress deadpan, medium.
44. *"Yes to the worst idea you've got, let's go"* — Kai at a ring-toss stall with the last stall-keeper, missing every throw, her laughing, then winning a tiny prize, handheld.
45. *"Tonight I'm saying yes to everything"* — the two of them at the top of a slide on the fairground, her in his lap, going down, slow motion.
46. *"No to the plan, no to the clock, no to the ten"* — reuse shot 22, the clock now reading much later (composited).
47. *"Ask me again, ask me anything"* — her spinning under his arm on the empty fairground midway, the leather jacket tied at her waist flaring, tracking.
48. *"Tonight I'm saying yes, yes, yes to everything"* — the two of them back to back on the midway, arms folded, mock-serious, then cracking up, wide.

### Instrumental — the drop extended

49. The ferris wheel spinning in a long exposure, bulbs streaking into rings, static.
50. Coins into ride slots and a wristband on a wrist, four impact cuts on the beat.
51. Mahima's hair in slow motion at the top of the wheel, the city behind her.
52. The karaoke crowd's hands, the cab meter's red glow, the diner's neon, a whip pan through all three.
53. The yes vocal chop matched to her mouth saying it in five different places, on the beat.
54. The filter sweep down: a single street lamp on an empty pre-dawn street, the cut into the rap verse.

### Verse 3 — Kai's verse, the list

55. *"Look, I got a list and we ain't even halfway"* — a steadicam tracking shot: Kai (white t-shirt, his jacket now on her) walking backwards in front of Mahima (sunrise look) through the empty pre-dawn city, counting on his fingers, to camera.
56. *"Rooftop, sunrise, a bakery that opens by five, hey"* — three inserts on the beat: a rooftop edge; a pale sky; a bakery's window lights coming on with a baker inside.
57. *"There's a bridge with a view and a bench with our name on it"* — Kai pointing at a bridge, then slapping the back of a bench as they pass, the tracking shot continuing.
58. *"No name yet, give me a week and a pen and I'll claim it"* — him miming writing on the bench with an invisible pen, her rolling her eyes and laughing, medium.
59. *"You said one drink, that was six hours back"* — a flash insert: her asleep for thirty seconds on his shoulder in the cab, his jacket over her, then back to the walk.
60. *"Heels in my hand, head on my jacket, that's facts"* — Kai holding up her heels in one hand as evidence, her snatching them back, close-up on the hands.
61. *"I know you've got rules, I know you've got a plan"* — him walking beside her now, hands in the air in surrender, her list of rules mimed on her fingers, two-shot.
62. *"But you laughed at the top of that wheel and I'm a fan"* — a flash insert of her laugh in the gondola from shot 34, then his face, sincere for one beat.
63. *"So one more yes, that's all I'm asking, one more"* — Kai stopping, turning to her, one finger up, hands open, the first street lamps switching off behind him.
64. *"Say yes to the second date, I'll be at your door"* — a close two-shot: him actually asking, her not answering yet, the bakery's warm window behind them.

### Bridge — sunrise on the lot

65. *"Sun coming up on the fairground lot"* — the fairground car park at sunrise, empty, the wheel dark and still, a single balloon drifting, wide static, pale gold.
66. *"The wheel's gone dark and the diner's closed"* — Mahima (sunrise look) sitting on a kerb in his denim jacket, barefoot, the heels beside her, the diner's sign off in the background, medium.
67. *"I said yes all night to the dumb stuff"* — Kai standing a little way off, waiting, hands in his pockets, out of focus behind her, her face sharp.
68. *"And it took me till sunrise to know"* — a slow push-in on her face as she gets it, the sun clearing the wheel behind her.
69. *"That it wasn't the wheel, it wasn't the song"* — two flash inserts: the wheel lit; the karaoke mic; then hard back to her.
70. *"It wasn't the syrup at three"* — a flash of the syrup on his sleeve, then her hand touching that same sleeve on the jacket she's wearing, macro.
71. *"Every yes I said was a yes to you"* — her looking up at him for the first time in the bridge, close-up, gold light on her face.
72. *"So go on, ask me"* — Kai crouching down in front of her, about to ask, the balloon crossing the frame behind him, held on the silence.

### Final chorus — the wheel in daylight

73. *"Tonight I'm saying yes to everything"* — she stands up and the two of them dance in the empty lot in the sunrise, wide, a crane beginning to rise.
74. *"Yes to the wheel, yes to the lights, yes to the spin"* — the fair's rides switching on one by one as the morning crew arrives, the wheel starting to turn, crane rising.
75. *"Yes to the mic, yes to the song I don't know"* — a morning-crew worker at the karaoke bar's open door across the street, Mahima singing at him from the lot, him applauding, medium.
76. *"Yes to the worst idea you've got, let's go"* — the two of them running for the wheel, her barefoot, the operator shaking his head and opening the gondola anyway, tracking.
77. *"And I'm saying yes to the second date"* — a close two-shot in the gondola in morning light, her saying it straight to him, no hesitation.
78. *"Yes to the third, and no, I don't wanna wait"* — her holding up three fingers, laughing; him holding up four; her pushing his hand down, close-up.
79. *"Ask me again, ask me anything"* — the gondola rising, the city waking below, the two of them leaning out to look, wide from outside.
80. *"Tonight I'm saying yes, yes, yes to everything"* — the wheel turning in full daylight with just the two of them on it, the crane at its highest, wide.

### Post-chorus 2 — the chant, in daylight

81. *"Yes, yes, yes, yes, say it again"* — jump cuts of her nodding yes at camera in the gondola, four poses, morning light.
82. *"Yes, yes, yes, yes, where have you been"* — four inserts: the wristband on her wrist; the balloon let go; his hand and hers; the wheel's pale bulbs against the sky.
83. *"Yes, yes, yes, yes, to everything"* — Kai at camera in the gondola mouthing yes with her, both grinning, close two-shot.
84. *"Ask me, ask me, yes to everything"* — her head on his shoulder in the gondola, her heels on the seat opposite, medium.

### Outro — ten o'clock came and went

85. *"Ten o'clock came and went, and I'm still here"* — the gondola at the top in daylight, the city awake below, her dead phone in her lap, her bare feet up, wide two-shot.
86. *"Phone's dead, feet hurt, I'm not going anywhere"* — her stretching her feet out and wincing, then settling deeper into his jacket, close-up, calm.
87. *"You said, so, what do you say"* — Kai asking, close-up on his face, the wind moving his hair, unhurried.
88. *"I said, what do you think, yes, yes, yes"* — final shot: the wheel from the ground, wide, the two of them small at the top, the sun full up, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the wheel lighting up (shot 3), the loud yes (shot 12), the
door on "here we go", the first drop, each "yes to everything", each
post-chorus chant, the top of the wheel (shot 33), the instrumental, the
start of the rap, "so go on, ask me", the final drop and the last "yes." At
124 BPM a bar is 1.94 s; the choruses cut on every bar, the post-chorus
jump cuts on every half-bar.

**Yes-to-everything challenge.** The post-chorus chant is a built-in
jump-cut format. Post the vertical cut of shots 25–28 with *"tonight I'm
saying yes to everything"* on screen and invite people to cut their own
night of yeses on every "yes" — a new place, a new dare, a new plate. The
pavement yes (shot 12) is the second shareable frame; the wheel at sunrise
(shot 88) is the quote card, with *"every yes I said was a yes to you."*

## 6. Quality-control checklist

- Three looks in the right sections: hair pinned and jacket on through pre-chorus 1; hair down and jacket tied at the waist from shot 17; his denim jacket on her from shot 55 to the end, and Kai in the white t-shirt from then on
- The heels come off in shot 31 and are never on her feet again
- The wheel's four states in order: unlit (2), lit (3 on), dark (65–72), turning in daylight (74 on)
- Kai's identity locked in every shot; the driver, the booth man, the operator and the waitress never pull focus
- All phone UI, the meter digits, the karaoke screen, the clocks and the bar sign composited; no model-generated text
- OpenPose on the karaoke stage, the run for the gate and every dance; Depth on the gondola shots
- No distorted hands on the fork, the wristband, the coins or the three-and-four fingers
- The last shot is locked-off from the ground and holds until the audio fades
