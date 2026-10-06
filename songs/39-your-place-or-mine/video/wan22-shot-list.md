# Wan 2.2 Shot List — "Your Place or Mine"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
122 BPM a bar is 1.97 s, so most shots are 2–4 s and the choruses and the
post-chorus chant cut on every bar or faster.

## 1. Visual style

End-of-the-night London. Four worlds: the **club** as the house lights come
up, harsh white on a sticky floor; the **street and the taxi rank**, chicken
shop fluorescent on wet pavement and sodium orange behind, drizzle in every
headlight; the **black cab**, orange interior, neon smearing across wet
glass, the driver's eyes in the mirror; and the **morning kitchen**, clean
gold through blinds. The **coin** is the repeating motif — flicked, spinning,
caught, covered, never looked at until the last shot. The two **front doors**
(red in Dalston, black in Peckham) appear whenever the hook says place.
Handheld and quick in the verses, slow motion and wide on the hook, one
locked-off frame at the end.

| Section | Grade | Camera |
|---|---|---|
| Intro / club lights up | Harsh white, confetti, cloakroom bulb | Slow motion close-ups |
| Verse 1 (the corner) | Chicken-shop white on wet pavement, sodium orange | Handheld two-shots |
| Pre-chorus | Rain light, bar flashback amber, the two doors | Tight, quick |
| Chorus 1 (the rank) | Saturated orange and teal, flare off wet road | Slow motion, wide, drone |
| Post-chorus (chant) | Cab orange, rain on glass | Cut on every phrase |
| Verse 2 (the cab) | Orange interior, phone glow, street lights rolling | Static two-shot, mirror inserts |
| Chorus 2 (the bridge) | River lights, reflections | Drone, interior |
| Instrumental | Deep blue city, orange cab | Slow, pulling back |
| Rap verse | Red light then green on his face | Handheld on him, flash inserts |
| Bridge | Cab light, then one gold flash-forward | Extreme slow motion, still |
| Final chorus / post-chorus | Pre-dawn blue over rooftops, hallway warm | Moving, then the key |
| Outro (kitchen) | Clean morning gold through blinds, steam | Slow pan, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (club and street, intro to final chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly damp from the rain, glossy dark-red lip and a little glitter at the corners of the eyes, wearing a fitted black satin slip dress under an oversized borrowed leather jacket with gold hoop earrings and strappy black heels, amused knowing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (morning outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled up in a loose messy bun, no makeup, wearing an oversized grey t-shirt and shorts, barefoot, holding a mug, soft satisfied smile, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man at the rank, with a face throughout)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a black overshirt open over a white t-shirt and dark jeans with white trainers, a nervous half-laugh and an easy grin, realistic cinematic photography, consistent identity

**The cab driver** — an older man with a grey beard and a flat cap, seen only in the rear-view mirror or from behind through the partition, never a full face.

**The crowd** — club-goers in coats and heels at the rank, a bouncer with his arms out, a chicken-shop counter worker. Never more than a few in focus.

Objects: the **coin**, the **red door** in Dalston and the **black door** in Peckham, the **chicken shop**, the **black cab** with its orange light, his **phone with the map**, the **leather jacket**, the **kettle** and the **two mugs**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the map, the taxi meter, the chicken-shop signage and
any street name are composited in the edit.** Generate the phone as a lit
blank screen in his hand and the meter as a blank glow; overlay the UI in
post — the model cannot render legible UI, and the map and the meter are
story beats.

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

## 4. Scene per lyric line

### Intro — lights up

1. *"Lights up, last tune, the bouncer's calling time"* — a basement club as the harsh house lights snap on, confetti and plastic cups on a sticky floor, a bouncer with his arms out, Mahima (club look) squinting then smiling in slow motion, close-up.
2. *"Coat check queue and you're stood behind me in the line"* — the cloakroom queue, Mahima at the front, the coat-check mirror showing Kai two people behind her, his eyes on her, over-the-shoulder.
3. *"Ears still ringing with the bass from the floor"* — her pressing a finger to one ear and laughing at herself, the cloakroom bulb warm on her face, close-up.
4. *"And you're looking at me like the night wants more"* — Kai caught looking, looking away, looking back; her small knowing smile without turning round, two-shot in the mirror.

### Verse 1 — the corner

5. *"Chicken shop glowing like a chapel on the corner"* — wide of a London corner at four in the morning, a chicken shop lit fluorescent white like a shrine, the crowd spilling out onto wet pavement, drizzle starting.
6. *"Four in the morning and the pavement's getting warmer"* — Mahima walking out under the awning, pulling the leather jacket tighter, Kai half-jogging to catch up behind her, tracking from the front.
7. *"You said, the Tube's shut, and I said, I know"* — two-shot under the awning, Kai pointing vaguely toward a shuttered station, her deadpan nod, handheld.
8. *"You said, where you heading, I said, depends where we go"* — her tilting her head at him, one eyebrow up, the chicken-shop light on half her face, close-up.
9. *"You're proper fit but I'm not saying that out loud"* — her looking him up and down once, slowly, then away at the rank as if bored, medium.
10. *"I let my eyes do the talking while the taxi rank's a crowd"* — the taxi rank, a crowd in coats and heels, black cabs idling, her eyes finding his over the crowd, rack focus.
11. *"You've got that nervous little laugh when I lean in"* — her leaning in to say something we don't hear, his nervous half-laugh, tight two-shot, rain in the headlights behind.
12. *"Boy, I've had you sorted since the second song came in"* — a flash of the dance floor earlier, club colour, her clocking him across the floor on the second song, then back to her face at the rank.

### Pre-chorus 1 — the terms

13. *"Don't act like this is up to you"* — her stepping close, one finger on his chest, laying out the terms, tight two-shot.
14. *"I made my mind up at the bar at half past two"* — flash of the bar at half past two, amber light, her deciding with a slow smile over a drink.
15. *"Two doors in this city and one of them's the answer"* — split image: a red front door in Dalston and a black front door in Peckham, each in its own street light, static.
16. *"You can pick the postcode, I'll be picking everything after"* — Kai nodding like he's been given instructions, her patting his chest once, medium.

### Chorus 1 — the rank, the drop

17. *"Your place or mine, either way, you're mine tonight"* — slow-motion wide of Mahima on the kerb with her arms up, dancing in her heels, cabs sliding past behind her, saturated orange and teal.
18. *"Flip a coin, heads or tails, I win on both sides"* — a coin flicked into the air, spinning, catching the street light, extreme slow motion, macro.
19. *"North of the river or south of the line"* — drone over the Thames at night, the lights of both banks, a bridge between them.
20. *"Call it a cab, call it fate, call it whatever you like"* — Kai putting his hand up for a cab and Mahima pulling it down, laughing, and doing it herself, two-shot.
21. *"You can tell him the street, I'll be telling him drive"* — a black cab pulling in, its orange light reflected in the wet road, her hand on the door handle, low angle.
22. *"Your place or mine, either way, you're mine tonight"* — her turning back to him with the cab door open, a head tilt that means get in, slow motion, flare off the road.

### Post-chorus 1 — the chant

23. *"Your place, my place, your place, my place"* — four cuts on the words: her mouth, his mouth, the crowd at the rank pointing left, then right.
24. *"Either way I'm getting my way"* — her sliding into the back seat first, the cab light orange on her face.
25. *"Your place, my place, your place, my place"* — the crowd pointing again, faster, a bouncer joining in, handheld.
26. *"Either way I'm getting my way"* — Kai getting in after her and the door thumping shut, rain on the window.

### Verse 2 — the cab

27. *"Black cab, light on, orange through the drizzle"* — the cab from outside, its light glowing orange through the drizzle, the meter running, static wide.
28. *"You're checking your phone like the answer's in a riddle"* — two-shot on the back seat, Kai scrolling a blank lit phone (map composited), Mahima watching him with her chin in her hand.
29. *"Your flatmate's in, my flatmate's out, so that's a point to me"* — her counting a point on one finger, the driver's eyes in the rear-view mirror, insert.
30. *"But you've got a rooftop in Peckham with the whole skyline for free"* — a flash of a Peckham rooftop at night, the whole skyline, the two of them leaning on the rail in deep blue.
31. *"I say, you're negotiating, you say, I'm just being fair"* — back in the cab, both talking with their hands, the street lights rolling across their faces, two-shot.
32. *"I say, cute, and I fix the collar on the jacket that you wear"* — her reaching over and fixing his collar, him going completely still, close-up on her hands then his face.
33. *"You say, seriously though, and I say, seriously, hun"* — the driver raising his eyebrows in the mirror, then her taking Kai's phone out of his hand, insert and two-shot.
34. *"You've had one job all night and it's the easy one"* — her putting the phone face-down on the seat between them and patting it, the meter still ticking (composited), close-up.

### Pre-chorus 2 — momentum

35. *"Don't act like this is up to you"* — the cab finally pulling away from the kerb, the city starting to slide past the window, tracking.
36. *"I clocked you at the bar at half past two"* — reuse shot 14, tighter, her eyes over the glass.
37. *"Two doors in this city and one of them's the answer"* — the two doors again, closer, a hand on each handle, split image.
38. *"You can pick the postcode, I'll be picking everything after"* — her leaning toward the driver's partition with a grin, Kai leaning back with his palms up, two-shot.

### Chorus 2 — the bridge over the river

39. *"Your place or mine, either way, you're mine tonight"* — drone over a Thames bridge, the cab a single orange light crossing it, the whole river lit.
40. *"Flip a coin, heads or tails, I win on both sides"* — inside, the coin spinning above her open palm in the cab light, slow motion.
41. *"North of the river or south of the line"* — both banks from the bridge, the cab window framing them, tracking.
42. *"Call it a cab, call it fate, call it whatever you like"* — her singing the hook to him across the back seat, him singing it back with the wrong words, two-shot, laughing.
43. *"You can tell him the street, I'll be telling him drive"* — the driver's hand on the wheel and his grin in the mirror, insert.
44. *"Your place or mine, either way, you're mine tonight"* — her head on the window, the city smearing past in neon, eyes on him, close-up.

### Instrumental — the ride

45. The river from the bridge, slow drone, deep blue.
46. Her hand out of the cab window in the rain, fingers spread, close-up.
47. Kai watching her, caught again, not looking away this time, close-up.
48. The coin on the seat between them, face-down, neither of them looking, macro.
49. A drone pulling back until the cab is a dot on a lit street, the cut into the rap.

### Verse 3 — Kai's rap, the red light

50. *"Cool, cool, I'll admit it, I was done at the door"* — the cab stopped at a red light, red on Kai's face, him turning to camera on the back seat, handheld.
51. *"Had a line rehearsed and I've lost it, what's it for?"* — flash: the club door earlier, his face going blank as she walks past, then back to him shrugging.
52. *"You walked in like the room was a rumour you started"* — flash: the dance floor, the crowd parting a little as she walks in, club colour.
53. *"Now I'm stood at the rank and the whole plan's departed"* — flash: him alone at the rank for one beat, hands in pockets, then back to the cab.
54. *"Dalston or Brixton, honestly, whatever"* — him pointing left, then right, then giving up, hands wide, handheld.
55. *"I'd row across the Thames in a bin bag in this weather"* — a one-beat flash of a black bin bag drifting on the river under the bridge lights, then his grin.
56. *"You say mine and I'm texting my flatmate, get lost"* — his thumbs on a blank lit phone (text composited), fast, close-up.
57. *"You say yours and I'm asking the driver what it costs"* — the driver shrugging in the mirror, palms up off the wheel for a second, insert.
58. *"Not even pretending that I'm the one who decides"* — Kai leaning back with his hands behind his head, surrendered, medium.
59. *"So flip your coin, love, heads or tails, I'll abide"* — Mahima watching him admit it, delighted, chin in hand, close-up.
60. *"Either way, I'm the one who's yours tonight"* — the light going green on his face, the cab moving off, his eyes on her, two-shot.

### Bridge — the coin in the air

61. *"Coin's in the air and the cab's at the kerb"* — the cab stopped at a kerb between two streets, the coin going up in extreme slow motion in the cab light, macro.
62. *"Driver's got his window down, waiting on a word"* — the driver's window down, rain coming in, his hand tapping the door, from behind through the partition.
63. *"Heads is your kitchen, tails is my stairs"* — the coin still turning, the two doors ghosted faintly over it, macro.
64. *"And honestly I'd take the night bus as long as you're there"* — her eyes on him, not on the coin, the softest her face has been, close-up.
65. *"I catch it, I cover it, I don't even look"* — her catching the coin and slapping it onto the back of her hand, covered, and not looking down, close-up on the hands then her face.
66. *"It was never the postcode, it was never the door"* — a flash-forward: a kitchen in clean morning gold, a kettle, two mugs, two seconds.
67. *"It's who's making tea in the morning, and I know that's you, for sure"* — the flash-forward continues: Kai in yesterday's shirt at the table with the mugs, then a hard cut back to her in the cab, decided.

### Final chorus — her street

68. *"Your place or mine, either way, you're mine tonight"* — her leaning forward to the driver's partition and giving her street, her mouth close to the glass, the driver's nod in the mirror.
69. *"Flip a coin, heads or tails, I win on both sides"* — the coin left on the back seat, still covered by nothing, nobody checked, macro.
70. *"North of the river or south of the line"* — the cab pulling off the kerb into an empty pre-dawn road, blue starting over the rooftops, wide.
71. *"Call it a cab, call it fate, call it whatever you like"* — Kai leaning back with both hands up, surrendered and laughing, close-up.
72. *"So I tell the driver my street and you don't even try"* — her turning back from the partition with a grin, him shaking his head, two-shot.
73. *"Your place or mine, either way, you're mine tonight"* — her front door, the red one, her key in the lock, the hallway light coming on, low angle.

### Post-chorus 2 — victory lap

74. *"Your place, my place, your place, my place"* — four cuts: her door, his hands up, the driver's grin, the cab pulling away.
75. *"Either way I'm getting my way"* — the key turning, the door opening, warm hallway light spilling onto the wet step.
76. *"Your place, my place, your place, my place"* — his hand on the door frame, her hand pulling him in by the collar, close-up.
77. *"Either way I'm getting my way"* — the door closing, the street blue and empty, one cab tail-light disappearing, locked-off.

### Outro — the kitchen

78. *"Kettle on, keys on the side, your jacket on my chair"* — morning, a kitchen in gold through blinds, a kettle steaming, her keys on the counter, his black overshirt over a chair, slow pan.
79. *"Sun coming through the blinds and look at that, you're still there"* — the pan lands on Kai at the table in yesterday's white t-shirt with two mugs, Mahima (morning look) in the doorway with her arms folded, smiling, wide.
80. *"Your place or mine, well, I suppose that's decided"* — the coin on the windowsill, heads up, finally seen, macro in the sun.
81. *"Mine, and you're mine, and I'm not even trying to hide it"* — final shot: her walking over and sitting across from him, taking a mug, the sun through the blinds striping the table, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the house lights snapping on, the first "your place or mine",
each chant, the cab door thump, the instrumental, the red light on the rap
entrance, the coin going up, "I know that's you, for sure", her street to the
driver, and the final mug. At 122 BPM a bar is 1.97 s; choruses cut every
bar, the chant every half-bar.

**Coin-flip challenge.** The bridge is the sound: flip a coin on camera,
catch it, cover it, don't look, and cut straight to whoever you were always
going to choose. Post the vertical cut of shots 61–67 with *"Your place or
mine? Either way, you're mine tonight"* on screen. The point-left-point-right
chant (shots 23–26) is the second shareable frame, a group dance for taxi
ranks and kitchens.

## 6. Quality-control checklist

- Two looks in the right sections: slip dress and leather jacket from the club to the front door, grey t-shirt and bun only in the kitchen outro
- Kai's face is visible throughout; he is the romantic lead, not an ex
- The cab driver is only ever the rear-view mirror or the back of his head
- The coin is never seen face-up until shot 80; shots 65 and 69 must show it covered or face-down
- The two doors are always the same red door and the same black door, and it is the red one she opens
- All phone UI, the map, the meter and any signage composited; no model-generated text
- Chant shots 23–26 and 74–77 cut on the words, under a second each
- The last shot is locked-off and holds until the audio fades
