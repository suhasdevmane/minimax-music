# Wan 2.2 Shot List — "Windows Down"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Uptempo: at 128 BPM a bar is 1.88 s, so most shots are 2–4 s and
the choruses cut on every bar. Take timestamps from the rendered WAV; cut on
the sung line.

## 1. Visual style

A one-day road trip, dawn to dark, on a single coast road. The **light
follows the clock**: cool blue dawn in the city, hard clean morning on the
motorway, saturated midday on the cliffs, gold at the petrol station and the
beach, a burning sunset for the final chorus, headlights and stars for the
outro. The **car is the second character**: a cream vintage convertible with
the top down in every shot after the intro. Drone for the road, handheld
inside the car, everything moving.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cool pre-dawn blue, one street | Static close-ups |
| Verse 1 | Pale gold breaking to hard clean morning | Handheld in-car, bonnet cam |
| Pre-chorus | Blown-out sky, first sea | Wide, then in-car push-in |
| Choruses | Saturated blues and whites, lens flare | Drone tracking, lay-by handheld |
| Post-chorus | Bright, punchy, one-second cuts | Ultra-fast inserts |
| Verse 2 | Hard afternoon sun, canopy shade, silver beach | Handheld, low angles |
| Instrumental | Sunset orange to pink, tunnel strobe | Slow motion, bonnet cam |
| Bridge | Dusk blue, last orange line, dash glow | Static, close, then moving |
| Final chorus | Full sunset burning to stars | Drone pull-backs |
| Outro | Deep blue evening, one harbour lamp | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (driving)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and whipping in the wind, light natural makeup, tortoiseshell sunglasses, wearing a white ribbed tank top and faded denim shorts, wide grinning expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (petrol station / beach)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair windblown and salt-textured, no makeup, an oversized faded orange shirt open over the white tank top, barefoot, sun-flushed cheeks, delighted squinting expression, realistic cinematic photography, consistent identity

**Mahima** (sunset / outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied up in a loose knot with strands escaping, light natural makeup, the orange shirt buttoned against the evening, sunglasses pushed up on her head, calm satisfied expression, realistic cinematic photography, consistent identity

**The cashier** — never shown clearly: a pair of hands, an apron, a counter.
> a petrol station attendant, hands and apron only, face out of frame

No male lead in this video. The road is empty apart from the car.

Objects: the **cream vintage convertible** (top down from shot 5 on), the
**paper coffee cup** on the dashboard, the **fuzzy dice** hung from the
mirror in verse 2 and in every in-car shot after, the **unopened map** on
the passenger seat, the **phone** which lives in the glovebox from shot 3
until shot 78.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, road signs, the car's display, the fuel gauge and the
notifications are composited in the edit.** Generate signs as blank boards
and the car screen as a lit blank panel; overlay in post — the model cannot
render legible UI or signage.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
cashier's reference deliberately faceless. Keyframes first; OpenPose for the
standing-in-the-seat shot and the beach; Depth for the in-car compositions.
16:9 first; 9:16 for the post-chorus inserts, which are natural vertical
content. Animate conservatively: hair in wind, a hand out the window, the
dice swinging, road rolling under the bonnet. Drive plates are easiest as a
locked car interior over a moving background.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s; choruses cut every bar.

## 4. Scene per lyric line

### Intro — the street, the keys

1. *"Keys in the cup holder, sunglasses on"* — a quiet residential street before sunrise, a cream vintage convertible at the kerb with the top down, Mahima (driving look) dropping keys into the cup holder, then sunglasses sliding on in the rear-view mirror, close-up, cool blue.
2. *"Half a tank of anything and the whole day gone"* — the fuel gauge (composited at half), then her face in the mirror, a slow grin, static.
3. *"Tell the phone I'm busy, tell the map to guess"* — her thumb flicking the phone to silent (composited) and tossing it into the glovebox, then an unopened folded map dropped on the passenger seat, close-up on hands.
4. *"I'm not lost, I'm just somewhere I haven't been yet"* — her hands on the wheel, one deep breath, the engine turning over, the first sun touching the rooftops behind her, medium.

### Verse 1 — leaving the city

5. *"Left the city sleeping at a quarter past six"* — the convertible pulling away down the empty street past curtained windows and tower blocks, tracking from behind, pale gold.
6. *"Coffee in a paper cup, a playlist of my picks"* — a paper coffee cup wedged on the dashboard with steam curling, her finger scrolling the car screen (UI composited), close-up.
7. *"Took the exit with the funny name because I liked the sound"* — a motorway exit sign flashing past as a blank board, her laughing and swerving late onto the slip road, the indicator ticking, bonnet cam.
8. *"Traded all my deadlines for a road that never ends downtown"* — the city shrinking in the rear-view mirror, her eyes in the mirror not looking back, close-up.
9. *"Elbow out the window and the wind is in my teeth"* — her elbow on the door, hair whipping across her sunglasses, teeth in a grin, profile from the passenger side, hard morning sun.
10. *"Every mile marker is a promise I get to keep"* — the yellow line rolling under the bonnet at speed, mile posts flicking by, low bonnet cam.
11. *"Nobody in the passenger seat telling me to slow"* — the empty passenger seat with only the folded map on it, the seatbelt swaying, static from the driver's side.
12. *"Just the yellow line, the radio, and everywhere to go"* — a wide from a bridge as the car passes beneath and the road opens toward the first hills, drone.

### Pre-chorus 1 — the sea appears

13. *"And the sky is so wide it could swallow me whole"* — the road cresting a hill and the sea appearing for the first time, the car tiny under an enormous blown-out sky, very wide drone.
14. *"And the song that comes on is the one that I know"* — her face as the radio changes, a gasp, a hand to her mouth, close-up handheld.
15. *"Turn it up till the speakers start shaking the door"* — her hand cranking the volume knob, the door speaker grille vibrating, the mirror shaking, extreme close-up.
16. *"This is what a Saturday was invented for"* — her head back, mouth open, singing at the windscreen, the drums dropping out for one beat, then the cut.

### Chorus 1 — the cliffs

17. *"Windows down, volume up, nowhere left to be"* — the coast road proper, cliffs on one side and ocean on the other, the convertible flying along it, drone tracking from the sea side, saturated blue and white.
18. *"Hair a mess, heart a wreck of sunshine and speed"* — her hair completely across her face and sunglasses, laughing and pushing it back with one hand, close-up handheld from the passenger seat.
19. *"Sing it loud to the cliffs, let the ocean sing it back"* — the car stopped at a lay-by, Mahima standing up in the driver's seat singing at the cliffs with both arms out, wide from the front.
20. *"Every wrong turn is right when it's mine, and I'm not turning back"* — the road bending hard and her leaning into it with a grin, bonnet cam, lens flare off the paint.
21. *"Windows down, volume up, nowhere left to be"* — reuse shot 17, closer, the drone dropping to road level beside the car.
22. *"Got a full tank of nothing and I've never felt so free"* — her hand out of the window riding the wind like a wing, slow motion, the sea behind.
23. *"So I'll drive till the coast road runs out of sea"* — the road ahead disappearing into haze along the cliffs, the horizon endless, wide from the driver's shoulder.
24. *"Windows down, volume up, nowhere left to be"* — her singing the hook straight into the rear-view mirror, sunglasses down, the road behind her, close-up.

### Post-chorus 1 — the four inserts (one second each)

25. *"Nowhere left to be, nowhere left to be"* — her bare foot pressing the pedal; the folded-flat roof from behind.
26. *"Foot down, top down, just the road and me"* — the empty road ahead through the windscreen; her hand out of the window.
27. *"Nowhere left to be, nowhere left to be"* — the dice-less mirror with her sunglasses in it; the sea flashing between two cliffs.
28. *"Volume up, windows down, and I'm free"* — her fist punching the air out of the top of the car, low angle from the road.

### Verse 2 — the petrol station, the beach

29. *"Petrol station, sticky counter, sweets I haven't had in years"* — a small coastal petrol station with a faded canopy, Mahima (beach look) barefoot on the forecourt, then a handful of retro sweets on a sticky counter, close-up, hard afternoon sun.
30. *"The cashier asks me where I'm headed and I laugh into my hair"* — the cashier only a pair of hands and an apron across the counter, Mahima laughing and hiding in her hair, over-the-counter shot.
31. *"Bought a map that I won't open and some dice to hang from the mirror"* — her hanging fuzzy dice from the mirror and flicking them, a second folded map tossed onto the first, close-up.
32. *"Filled the tank and filled my lungs, and the picture just got clearer"* — her leaning on the car while the pump runs, eyes closed, breathing the sea air, the canopy shade across her, medium.
33. *"Pulled over where the road bends, kicked my shoes onto the sand"* — the car parked at a bend above a hidden beach, her shoes flying off into the sand, low wide, silver beach light.
34. *"Wrote my name into the tide line, watched it vanish from my hand"* — low shot of her finger dragging a shape into the wet tide line (never legible), a wave sliding in and erasing it, macro.
35. *"Not a single notification worth the view I've got right now"* — the phone in the open glovebox lighting up (composited), then a cut to the horizon she is looking at instead, split by the beat.
36. *"I've got salt inside my eyelashes and I forgot how to frown"* — her face with salt crystals on her lashes, squinting at the sea and laughing, extreme close-up, sea spray.

### Pre-chorus 2 — the sun coming down

37. *"And the sun's getting low like it's coming to sit"* — back in the car, the sun low over the bonnet as if aiming for the passenger seat, wide from the back seat, first gold.
38. *"And the chorus comes round and I know all of it"* — her mouthing the words a beat early, grinning at herself in the mirror, close-up.
39. *"Turn it up till the seagulls are singing along"* — her hand on the volume knob, then a seagull on a fence post as the car passes, tracking.
40. *"This is what a good day sounds like in a song"* — seagulls wheeling above the road ahead, the car beneath them, drone.

### Chorus 2 — golden hour

41. *"Windows down, volume up, nowhere left to be"* — the coast road at golden hour, the drone following the car through a long curve with the sun behind, long shadows, the sea bronze.
42. *"Hair a mess, heart a wreck of sunshine and speed"* — reuse shot 18, gold now, the orange shirt flapping.
43. *"Sing it loud to the cliffs, let the ocean sing it back"* — her singing with one hand on the wheel and the other conducting the sky, medium from the passenger seat.
44. *"Every wrong turn is right when it's mine, and I'm not turning back"* — the dice swinging wildly on a bend, then her grin, two cuts on the beat.
45. *"Windows down, volume up, nowhere left to be"* — a slow-motion pass along a stone wall with the sun strobing through gaps, the car flashing gold, side tracking.
46. *"Got a full tank of nothing and I've never felt so free"* — the fuel gauge now full (composited), then her hand out the window again, warmer, slow motion.
47. *"So I'll drive till the coast road runs out of sea"* — the road ahead turning to a ribbon of gold light between the cliffs and the water, bonnet cam.
48. *"Windows down, volume up, nowhere left to be"* — reuse shot 24, sunglasses pushed up now, the sun in her eyes.

### Instrumental — the solo, the tunnel, the bonnet

49. The car entering a tunnel, the orange tunnel lights strobing across Mahima's face on the beat, close-up.
50. Her hair against the sunset in slow motion from the passenger seat, backlit, strands of gold.
51. The road from the bonnet cam at full speed as the sky turns orange to pink, then the tide line from above, two cuts.
52. A lay-by, her leaning on the warm bonnet with her eyes closed, the engine ticking, the sun almost on the water, wide static.
53. The breakdown: her fingers drumming the wheel on the claps, then the key turning as the band comes back — the cut into the bridge.

### Bridge — the glovebox, the invitation

54. *"I used to think that freedom was a place I had to find"* — the car parked on a cliff lay-by with the engine off, Mahima (sunset look) in the driver's seat with her feet on the dash, talking to the windscreen, close and quiet, dusk blue.
55. *"A city or a person or a sign"* — three soft flashes on the words: the city skyline in the mirror from shot 8, the empty passenger seat, the blank exit sign, then back to her face.
56. *"But it was in the glovebox all along"* — her reaching over and opening the glovebox, the little light inside coming on, close-up.
57. *"Under the receipts and the sunscreen and the songs"* — inside the glovebox: crumpled receipts, a tube of sunscreen, an old cassette, the phone face-down, her hand resting on all of it, macro, warm.
58. *"So if you're stuck on a Tuesday with the week around your neck"* — her turning to the camera as if to a friend in the passenger seat, warm, direct, medium.
59. *"Take the keys, take the coast, take the whole sunset"* — three cuts: the keys lifted from the cup holder; the coast road below the lay-by; the last orange line on the horizon.
60. *"You don't need a reason and you don't need a map"* — her tossing the unopened map into the back seat without looking, a small laugh, close-up.
61. *"You just need the windows down and a road that opens up"* — the key turning, the dashboard lighting, the headlights coming on and throwing light down the road ahead, from the bonnet.
62. *"I'm not running from anything, I'm running with the light"* — the car pulling out of the lay-by into the pink and violet dusk as the drums return, drone rising.
63. *"And the engine's humming something that sounds a lot like mine"* — her hand flat on the dashboard feeling the engine, then her face lit by the dash glow, close-up.

### Final chorus — sunset on the dashboard

64. *"Windows down, volume up, nowhere left to be"* — the sunset filling the whole windscreen and the road turning to gold, from the back seat, the key change hitting.
65. *"Sunset on the dashboard turning everything to gold and me"* — sun on the dashboard, on the coffee cup, on the dice, and on her face, a slow pan across all of it, close.
66. *"Sing it loud to the dark, let the headlights sing it back"* — the headlights cutting into the dusk ahead, her singing into the dark beyond them, wide from the bonnet.
67. *"Every wrong turn was right, it was mine, and I'm not turning back"* — the road behind her in the mirror going dark, her eyes forward, then her hair loosening from the knot in the wind, close-up.
68. *"Windows down, volume up, nowhere left to be"* — a drone pull-back as the car follows the coast into the last light, the cliffs black, the sea burning.
69. *"Got a full tank of nothing and I've never felt so free"* — her arms up out of the top of the car for one beat at speed, silhouetted against the sunset, slow motion, low angle from the road.
70. *"So I'll drive till the stars run out of sea"* — the first stars over the sea as the sky goes deep blue, the car's headlights below, very wide.
71. *"Windows down, volume up, nowhere left to be"* — her face in the dash glow singing the hook, sunglasses on her head, hair everywhere, the happiest frame of the video, close-up.

### Post-chorus 2 — the inserts, at night

72. *"Nowhere left to be, nowhere left to be"* — her foot on the pedal in the dash glow; the roof still down under stars.
73. *"Foot down, top down, just the road and me"* — the road in the headlights; her hand out the window in the dark.
74. *"Nowhere left to be, nowhere left to be"* — the dice swinging in the dark; the sea catching moonlight between cliffs.
75. *"Volume up, windows down, and I'm free"* — her fist punching the air out of the top of the car, low angle, silhouetted against the stars.

### Outro — where the road ends

76. *"Keys in the cup holder, sunglasses off"* — the car stopped where the coast road ends at a small harbour, the engine idling, the keys dropped back into the cup holder and the sunglasses folded on the dash, close-up, deep blue evening.
77. *"The tank says empty but it doesn't say stop"* — the fuel needle on empty (composited), then her shrug and half-smile in the mirror.
78. *"Tell the phone I'm sorry, tell the map I'm home"* — her taking the phone from the glovebox, switching it on, and putting it in her pocket without looking at it, the map left on the seat, close-up on hands.
79. *"Wherever this road ends is wherever I'll go"* — her getting out and walking down toward the harbour wall, the dice still swinging in the empty car behind her, one warm harbour lamp, wide from behind.
80. *"Wherever this road ends is wherever I'll go"* — final shot: her on the harbour wall with the last light on the water and the car small behind her, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the engine turning over, the first drum fill, each "windows
down, volume up", the post-chorus inserts, the tide line, the tunnel, the
glovebox, the key change, and the final "go." At 128 BPM a bar is 1.88 s;
choruses cut every bar, post-chorus inserts every half-bar.

**Windows-down challenge.** The hook is caption-ready. Post the vertical cut
of the four post-chorus inserts (shots 25–28) with *"windows down, volume up,
nowhere left to be"* on screen and invite people to film their own four:
foot down, top down, the road, a hand out the window. The standing-in-the-
seat shot (19) is the hook frame; the tide line (34) is the second shareable
recreate.

## 6. Quality-control checklist

- Three looks in the right sections: white tank and sunglasses for the intro and verse 1, the orange shirt open and barefoot from the petrol station (shot 29) through the instrumental, buttoned with the hair knot from the bridge (shot 54) on
- The light follows the clock: no shot is earlier in the day than the one before it
- The car top is down in every shot from shot 5 on, and the dice are in every in-car shot from shot 31 on
- The cashier never has a visible face; no other people on the road or the beach
- All signs, screens, gauges and notifications composited; no model-generated text; the tide-line word is never legible
- No distorted hands on the wheel, the volume knob or the tide line
- The phone lives in the glovebox from shot 3 until shot 78 and is never in her hand while she drives
- The last shot is locked-off and holds until the audio fades
