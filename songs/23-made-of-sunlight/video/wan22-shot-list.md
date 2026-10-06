# Wan 2.2 Shot List — "Made of Sunlight"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
106 BPM a bar is 2.26 s, so most shots run 2–5 s and the choruses cut on the
half-bar where the call and the answer alternate.

## 1. Visual style

A beach town on one road, filmed across one evening, one morning and one
evening again. **The grade is the story: orange and blue.** Every frame holds
warm practical light — bulbs, lanterns, headlights, low sun — against deep
blue sea and sky. Nothing is cool and grey anywhere in this video. Cameras
stay at human height and move with people rather than around them; the only
drone moves are the two crowd rises. Skin stays warm and real, never plastic.

| Section | Grade | Camera |
|---|---|---|
| Intro | Full golden hour, deep blue on the sea side | Wide, low, slow drift |
| Verse 1 | Sun behind, faces bounced, long shadows | Tracking and close two-shots |
| Pre-chorus | Last light, first bulb strings | Whip-pans, low hand inserts |
| Choruses | Bulbs and headlights over deep blue sky | Circling handheld, one drone rise |
| Verse 2 | Flat bright morning, wet ground, saturated | Static and doorway framings |
| Instrumental | Bulbs, brake lights, blue leaving the sky | Rooftop wide, loose handheld |
| Bridge | Black, then one lantern, hard falloff | Static, then handheld through the crowd |
| Final chorus | Every practical on, widest frames | Drone climb, slow push |
| Post-chorus | Orange lights, blue sky, flat and clean | Locked-off wide |
| Outro | Last blue, one warm bulb behind | Long lens, held |

## 2. Character bible — paste into every prompt

**Mahima** (evening, the dance)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and moving, light natural makeup with a warm gloss, wearing a burnt-orange wrap dress and bare feet with sandals carried in one hand, open delighted expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (morning, the market)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair damp from rain and pushed back, no makeup, wearing a pale blue cotton shirt over a vest and cut-off shorts, a canvas market bag on her hip, easy amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead, both days)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing an open short-sleeved shirt in faded orange and blue over a white vest and loose trousers, sun-worn skin and working hands, relaxed smiling expression, realistic cinematic photography, consistent identity

No exes and no rivals appear in this video; there is no antagonist. The
crowd is a real crowd — the barber and the two old men outside his shop, the
auntie at the fish stall, the drummers, the brass players, the children, the
boy with two crates of bottles, and one older couple at the edge of the final
chorus. Keep every extra warm, ordinary and specific; nobody is styled.

Objects: the **two plastic chairs** and the **cooler**, the **barber's
radio**, a piece of **sea glass**, the **mangoes**, the **cold bottle**, the
**lantern**, the **string of bulbs**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All shop signage, radio dials, market prices and any lettering are
composited in the edit** — or simply avoided by framing. The model cannot
render legible text and this town would be full of it.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai in his single look with IP-Adapter or a
character LoRA each. **OpenPose is essential for every dance shot** — the
post-chorus step, the crowd in the choruses and the drummers' hands all need
a pose reference or the model invents limbs. Depth for the road wides and the
market. 16:9 first; 9:16 recomposition for the dance-challenge cut. Animate
conservatively and in short bursts: one two-count step per clip, one drum
strike per clip, cloth and hair movement rather than whole-body travel.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; the instrumental shots run longer.

## 4. Scene per lyric line

### Intro — the road at golden hour

1. *"Orange on the water and the blue coming down"* — wide, low, the main road of a beach town running straight down to the sea, the sun sitting on the water, everything orange, slow drift forward.
2. *"Somebody's speaker going wild at the end of the town"* — a speaker on a plastic crate outside a shop, the cone visibly moving, dust jumping on the crate beside it, macro, static.
3. *"You put your hand out flat and you said, come on, walk"* — Kai's open hand entering frame from the right into low sun, held flat and still, extreme close-up, shallow.
4. *"And the whole evening changed the way it talked"* — Mahima (evening look) stepping off a kerb into the road, sandals in one hand, the street ahead of her already moving, tracking from behind at hip height.

### Verse 1 — her, teasing

5. *"You came down the beach road with your shirt undone"* — Kai walking down the centre of the road toward camera, shirt open over a white vest, sun directly behind him, long lens, heat shimmer.
6. *"Two plastic chairs, a cooler and the last of the sun"* — the same walk from the side: two stacked plastic chairs under one arm, a cooler swinging in the other hand, tracking parallel.
7. *"The barber's radio was older than the both of us"* — a barber shop doorway, a battered radio on a shelf, two old men nodding on a bench beside it, static, warm interior light.
8. *"But you had the whole street moving with your hands up"* — Kai's hands going up over his head mid-walk and four or five people in the background picking up the step without stopping what they were doing, medium wide.
9. *"I said, what are you made of, and you laughed and said, guess"* — the two of them dropped into the plastic chairs at the edge of the sand, close two-shot, her turned toward him, his head going back laughing.
10. *"So I started at your hands and I gave it my best"* — her eyes going down to his hands resting on his knees, then a matched insert of the hands themselves, working hands, scarred and oil-marked.
11. *"Sea glass, engine oil, and a laugh like a bell"* — three fast inserts on the beat: a piece of green sea glass turned in her fingers, an oil-dark knuckle, his open laughing mouth in profile.
12. *"And whatever else it is, it wears on you well"* — back to the two-shot, her looking at him a beat too long, the sun almost gone behind them, slow push.

### Pre-chorus 1 — the drum arrives

13. *"Then the drum comes in and the drum comes in"* — a drummer's hands landing on a log drum, extreme close-up, the skin visibly moving, two strikes.
14. *"And the whole town leans the way the evening leans"* — whip-pan off the drum to the road filling with people, everyone moving on the same count, medium wide, handheld.
15. *"Put your hand in my hand, let the horns begin"* — her hand going into his, low frame at waist height, both stepping off the sand into the road, the brass entering behind them out of focus.
16. *"Ask me what I'm made of, I will answer again"* — Mahima looking straight at Kai as the first bulb string comes on above the road, her face lit warm from above, close-up, static.

### Chorus 1 — call and response

17. *"You're made of sunlight, I'm made of you"* — circling handheld around the two of them in the middle of the dance, the crowd blurred orange behind, one full revolution.
18. *"Made of the salt and the sand and the blue"* — tight single on Mahima on the call, matched framing, then the same framing on Kai for the answer, cut on the half-bar.
19. *"Say it out loud where the whole street hears"* — a wide of the road from head height, forty people moving on the same two-count, bulb strings crossing overhead.
20. *"Say it over log drums, say it in my ear"* — her mouth close to his ear mid-step, both still dancing, extreme close-up, the crowd out of focus.
21. *"You're made of sunlight, I'm made of you"* — drone rising slowly from head height to roof height, the road a river of movement, sea beyond.
22. *"Made of the drum and the dust and the truth"* — low shot of bare feet and sandals in sand, dust lifting through a warm light beam, ground level.
23. *"Whatever I am, I was made in your hands"* — his hands at her waist, her hands over his, both moving, tight and unhurried, warm key.
24. *"So I'm made of you"* — the two of them stopped still for one beat while the crowd keeps moving around them, medium, slight slow motion.

### Verse 2 — him, the morning after

25. *"You came in from the market with the mangoes and the rain"* — morning, a short warm shower: Mahima (market look) walking in from a doorway, hair wet, a canvas bag on her hip, static wide.
26. *"Orange on your fingers, half the ocean in your hair"* — close-up of her fingers wet with mango, then her pushing her damp hair back off her face, natural bright light.
27. *"The auntie at the fish stall said we move like one song"* — a fish stall under a tarpaulin, an older woman laughing and pointing at the two of them, over-the-shoulder from Kai's position.
28. *"And I have not stopped humming it, so she was not wrong"* — Kai walking away from the stall shaking his head and grinning, medium, wet ground reflecting the sky.
29. *"You asked me what I'm made of, so I'll answer you now"* — Kai in a doorway with a cold bottle against his neck, looking straight down the lens, the only direct address in the video, static close-up.
30. *"Since the night you said my name I have not put it down"* — his hand turning the bottle, condensation running, then his eyes lifting back to her off camera, tight.
31. *"Cold glass, warm asphalt, and the sound of your feet"* — three fast inserts on the beat: condensation running down glass, bare feet crossing hot wet road, a speaker cone pulsing.
32. *"And a street that plays your name on every beat"* — a wide of the morning road, the same road as the dance, empty except for market traffic, held two beats.

### Pre-chorus 2 — evening again

33. *"Then the drum comes in and the drum comes in"* — match cut from the empty morning road to the same framing at dusk with the drummers already set up in it, static.
34. *"And the whole town leans the way the evening leans"* — the crowd assembling faster than the first time, people arriving from three directions at once, medium wide, handheld.
35. *"Put your hand in my hand, let the horns begin"* — the three brass players walking into shot mid-phrase, instruments up, tracking backwards ahead of them.
36. *"Ask me what I'm made of, I will answer again"* — Kai finding Mahima in the crowd, her hand already out, low frame on the two hands meeting.

### Chorus 2 — the dance at full size

37. *"You're made of sunlight, I'm made of you"* — long steadicam push straight down the centre of the crowd, people parting, the two leads at the end of it.
38. *"Made of the salt and the sand and the blue"* — reuse the matched singles from shot 18, tighter, sweat and bulb light on both faces.
39. *"Say it out loud where the whole street hears"* — four faces in the crowd singing the answer half, cut fast, ordinary people, no styling.
40. *"Say it over log drums, say it in my ear"* — the drummers from behind, the crowd beyond them, the whole frame moving on the beat, low wide.
41. *"You're made of sunlight, I'm made of you"* — the two leads at the centre, everyone around them in motion, ninety-six frames slow motion on this line only.
42. *"Made of the drum and the dust and the truth"* — dust and bulb light, a wide low frame of legs and sand, real time again.
43. *"Whatever I am, I was made in your hands"* — her hands on his shoulders, crowd out of focus behind, tight two-shot, blue rim light from the sea side.
44. *"So I'm made of you"* — a blue neon over a shop reflected in a puddle with dancing legs crossing it, static, held to the section end.

### Instrumental — the street dance

45. A talking drum answering the log drums, the drummer's hands and then his face, close and loose.
46. The three brass players turned toward each other rather than the crowd, playing a call and answer, medium.
47. Rooftop wide of the whole road, the dance filling it end to end, the sea black beyond, slow drift.
48. Children at the front doing the two-count step better than the adults, low angle, handheld.
49. A boy carrying two crates of bottles straight through the middle of the dance without spilling one, tracking, the crowd folding around him.

### Bridge — the power cuts

50. *"When the power cuts and the whole street goes dark"* — hard cut to black on the downbeat, two seconds of near-black with only silhouettes and the drums continuing, static.
51. *"You are still the warmest thing out here in the yard"* — one lantern coming up under Mahima's face, held low, everything past her in blackness, close-up, hard falloff.
52. *"I have got you memorised right down to the scar"* — her fingers finding a small scar on his forearm in the dark, lantern light only, extreme close-up.
53. *"I could find you in a blackout by the sound of your heart"* — her forehead against his chest, both still, the crowd's phone torches drifting behind them out of focus.
54. *"So let the generators cough and the lanterns come out"* — a generator being kicked awake, a cough of smoke, a man's hand on the pull cord, hard practical light from a torch.
55. *"We were never dancing for the bulbs anyhow"* — handheld low through the crowd with lanterns passing the lens, the dance already restarted in the dark, one string of bulbs stuttering back on at the top of frame.

### Final chorus — full power, both in harmony

56. *"You're made of sunlight, I'm made of you"* — every practical back on at once, the whole road lit, drone climbing from inside the crowd to above the roofline.
57. *"Made of the salt and the sand and the blue"* — the sea behind the roofline at the top of the drone move, deep blue against the orange road, held.
58. *"Say it to the palms and the plastic chairs"* — the two plastic chairs from verse one, empty in the sand, the two leads dancing past them, medium.
59. *"Say it to the children who are still out there"* — the children still dancing at the edge of the road well past bedtime, an adult giving up on collecting them, wide.
60. *"You're made of sunlight, I'm made of you"* — slow push to a tight two-shot, both singing the hook to each other rather than to camera.
61. *"Made of the drum and the dust and the truth"* — the drummers seen past the two leads' shoulders, the whole band lit warm, medium.
62. *"Ten thousand mornings and I still choose"* — an older couple at the edge of the dance doing exactly the same two-count step, forty years on, held just under two seconds.
63. *"I'm made of you"* — back to the leads, both still, the crowd moving, her hand flat on his chest, close.

### Post-chorus — the chant

64. *"Oh, the orange and the blue"* — locked-off wide of the road, everyone on the same two-count step, arms up, the simplest possible choreography.
65. *"Oh, the orange and the blue"* — same locked-off wide, one bar later, more people in frame, identical framing so the repetition reads.
66. *"Everything I am, I am made of you"* — three tight cutaways of individual faces singing the chant, cut on the beat.
67. *"Oh, the orange and the blue"* — the locked-off wide a third time, the two leads walking backwards out of frame while the crowd keeps going.

### Outro — two voices, one guitar

68. *"Sunlight, sunlight, walking down the beach road"* — long lens from far ahead, both walking toward camera down the empty end of the road, the dance a warm blur far behind them.
69. *"Sunlight, sunlight, and the evening going gold"* — the same walk from the side, low, the last blue in the sky above the water.
70. *"Ask me in a hundred years, I will tell you the truth"* — the two of them stopping, her looking at him, no dialogue, no kiss, medium two-shot.
71. *"I'm made of you"* — final shot: the two plastic chairs and the cooler left in the sand, the sea beyond, one warm bulb still burning behind, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first hand entering frame, the first log-drum strike, each
*"you're made of sunlight"*, the morning cut, the blackout downbeat, the
power returning, and the final chair frame. At 106 BPM a bar is 2.26 s; the
choruses cut on the half-bar so the call and the answer each get their own
image.

**The two-count challenge.** The post-chorus (shots 64–67) is deliberately
the easiest choreography in the catalogue: one step, two counts, arms up.
Post it as a vertical locked-off wide so the whole move is learnable from a
single clip, captioned *"orange and the blue."* The second shareable cut is
the call-and-answer pair from shots 17–18, made for two people lip-syncing
the two halves of the hook in one frame.

## 6. Quality-control checklist

- Two looks for Mahima only: burnt orange for both evenings, pale blue for the morning, never mixed inside a section
- Orange and blue in every single frame — no grey, no cool daylight, no desaturated shot anywhere
- Kai looks directly at the lens exactly once, on shot 29, and never again
- No shop signage, price boards or radio dials legible; all lettering composited or framed out
- OpenPose on every dance shot; the two-count step is identical in shots 64–67
- The blackout at shot 50 is the only near-black frame in the video, and the drums never stop through it
- Light only returns in stages after shot 55; no shot after it is darker than the one before
- The final frame is locked off on the empty chairs and holds until the audio fades
