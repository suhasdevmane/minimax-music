# Wan 2.2 Shot List — "Cry in the Uber"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Sixty-three lyric shots plus five for the instrumental, numbered
continuously. Timestamps come from the rendered WAV; cut on the sung line. At
90 BPM a bar is 2.67 s, so shots are long — most 4–6 s — and several are
deliberately held past the cut.

## 1. Visual world

One night, one car, one city, in the rain. Roughly two thirds of the video
happens inside a moving vehicle, and the camera stays inside it even when the
song does not — the memories are seen as if remembered from the back seat.
Everything outside the window is abstract: brake lights, wet neon, a bus, a
bridge, none of it in focus. The glass is the canvas. The only warm light in
the piece belongs to doorways, and the last one is hers.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium orange, rain in the beams | Static, from behind |
| Verse 1 | Dashboard green, strobing streetlights | Locked interior, fragments |
| Pre-choruses | Warm domestic behind, cold blue in front | Static, rewound |
| Choruses | Every colour, smeared on wet glass | Long holds, slow push |
| Verse 2 | Red light flooding the car, then flat bulb | Static, over the seat |
| Instrumental | Gold on black, the river | Exterior, above, wide |
| Bridge | Streetlight through a wet windscreen | Slowing, settling |
| Final chorus | Warmest of the video, her own hall | Tracking from behind |
| Outro | Hall light only | Static, held |

## 2. Character bible — paste into every prompt

**Mahima** (the whole video)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair damp from rain and pushed back from her forehead, makeup slightly worn through, wearing a dark green wool coat over a black jumper, composed expression that keeps failing, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the hallway, final two shots)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and drying, no makeup left, wearing a black jumper with the coat removed, spent and settled expression, realistic cinematic photography, consistent identity, natural skin texture

**The driver** — a man in his fifties, never given a full face. Generate him
only in fragments: a hand on the wheel, a shoulder, an ear, a strip of eyes
in the rear-view mirror, a forearm reaching back between the seats.
> a man in his fifties, seen only as hands, shoulder or a narrow strip of eyes in a rear-view mirror, dark jacket, wedding ring

**The ex** — faceless in every frame. In the kitchen memory he is a pair of
hands on a counter, a mouth in close-up, a shape at the edge of the frame.
> a young man in his late twenties, face out of frame or cropped at the jaw, dark jumper

Objects that repeat: the **cardboard pine tree** turning on the mirror, the
**bottle of water** in the door pocket, the **packet of tissues**, the **wet
window**, the **hall light** — his at the start, hers at the end.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the map, the arrival card, the tip and the rating are
composited in the edit.** Generate the phone as a lit blank rectangle; the
model cannot render legible UI, and the blue dot crawling round the block in
shot 2 has to read instantly.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA; keep the
driver's and the ex's references deliberately faceless. Keyframes first;
OpenPose for the walk up the path in the final chorus and the stair sit in
the outro; Depth for the car interiors, which are the hardest compositions in
the piece. Shoot the through-glass city as separate plates and composite —
asking the model for a sharp face and a smeared city in one generation fails.
16:9 first; 9:16 for the window-profile shots, which are the vertical hero
cuts. Animate conservatively: rain running down glass, wipers, a turning air
freshener, a head against a window.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s.

## 4. Scene per lyric line

### Intro — the pavement

1. *"On the pavement in the rain outside your door,"* — Mahima from behind on a wet residential street at night, coat undone, rain visible in the sodium beams, a front door with a warm hall light behind her, static.
2. *"Watching a small blue dot come crawling round the block,"* — the phone screen filling frame, a blue dot crawling a map (composited), rain landing on the glass and blurring it.
3. *"Three minutes, then two, then none,"* — three cuts of the same wide, each one wetter and each one with her a little more still; headlights sweeping into the last.
4. *"And I hold it in until the door clicks shut."* — the car door closing from inside, the sound of the street cutting off, her face lit for one second by the interior lamp before it fades.

### Verse 1 — the car, and the driver

5. *"He says you alright, love, is it Peckham, is that right,"* — the driver's eyes in a narrow strip of rear-view mirror, nothing else of him, the car pulling out.
6. *"I say yes, and my voice comes out in bits."* — her in the back seat, jaw set, the first crack in her face, close-up, dashboard green.
7. *"A bottle of water in the door, a charger on the seat,"* — macro pan across the door pocket and the seat beside her, the small furniture of a stranger's kindness.
8. *"A cardboard pine tree turning where the mirror sits."* — the air freshener turning slowly on its string in front of the smeared windscreen, shallow focus, held.
9. *"He turns the radio down before I have to ask,"* — his hand reaching for the volume dial without looking, from her point of view over the seat.
10. *"Puts the heating on my side and doesn't say a word."* — a vent flexing open, then her hands in her lap unclenching very slightly, two macros.
11. *"The wipers keep a rhythm that my ribs are trying to match,"* — the windscreen from inside, wipers sweeping, the city ahead unreadable, static, on the beat.
12. *"And the whole of south London goes by, blurred."* — her profile against the side window with the city running behind her out of focus, long lens, held.

### Pre-chorus 1 — the eleven minutes

13. *"Not on your stairs, not in your street,"* — memory: her in his kitchen with her coat already on, standing very straight, his hands on the counter, his face out of frame.
14. *"Not while your kitchen light was still on."* — memory: the kitchen from outside through a window, the light on, two shapes not moving.
15. *"I kept my face together for eleven minutes,"* — memory: her going down a communal staircase holding the rail, perfectly composed, tracking from below.
16. *"And now the door is shut and you're gone."* — the kitchen light going off behind the window; hard cut back to the car and her face in the dark.

### Chorus 1 — permission

17. *"Let me cry in the Uber, I'll be fine by my door,"* — the hero shot: her face in profile against the window, streetlights running down the glass and across her skin, held for the whole line.
18. *"Half an hour, that's all, I won't ask for more."* — the same framing, her eyes closing, the first tear not wiped away.
19. *"Let the streetlights run like water down the glass,"* — pure glass: rain and light with no face at all, abstract, a bus going past as a smear of yellow.
20. *"Let a kind man with the heating on let it pass."* — the driver's hand on the wheel, steady, and nothing else in the frame.
21. *"Let me cry in the Uber all the way through town,"* — the car from outside on a wet road, seen from another lane, her a shape in the back window.
22. *"I'll be fine by my door, I just can't be fine now."* — back inside, her hand flat against the window, the city behind it, slow push.

### Verse 2 — the tissues

23. *"At the lights he passes back a packet of tissues,"* — a red light flooding the car, his forearm coming back between the seats holding a packet, his eyes forward.
24. *"Doesn't look in the mirror, keeps his eyes on the road ahead."* — the mirror strip, deliberately empty of eye contact, the light still red.
25. *"Says the traffic's proper bad round Elephant and Castle,"* — the windscreen: a wet junction, buses, a roundabout, everything stopped, wide.
26. *"Which is the kindest thing that anyone has said."* — her taking the tissues, a small nod, and completely losing it, close-up.
27. *"And I think about your kitchen and how you said it,"* — memory: the kitchen bulb, a carrier bag of shopping still on the counter, unpacked.
28. *"Like a thing that you'd rehearsed on the way back from the shop."* — memory: his mouth in close-up saying a short sentence, calm, cropped at the nose.
29. *"No shout, no slammed door, no reason I can hold,"* — memory: a wide of the kitchen with both of them in it, nobody moving, held far too long.
30. *"Just a quiet, I think that we should stop."* — hard cut to the car, her face, no memory left, the red light turning green off-frame.

### Pre-chorus 2 — the road takes it

31. *"Not in your hallway, not on your stairs,"* — memory: a communal hallway, neighbours shaking out umbrellas, her walking past them with her face perfect.
32. *"Not with your neighbours coming in from the rain."* — memory: the front door closing behind her from inside, warm light narrowing to nothing.
33. *"I held it through the goodbye and the going,"* — her in the car with her hand over her mouth, back to the present, tight.
34. *"And now the New Cross Road can take the strain."* — the car at speed on a long wet arterial road, filmed from outside, spray and tail lights, wide.

### Chorus 2 — the bottom of it

35. *"Let me cry in the Uber, I'll be fine by my door,"* — a very slow push from the front footwell up to her face, the city passing behind her the whole way.
36. *"Half an hour, that's all, I won't ask for more."* — the push continues and settles, her fully crying now, no performance in it.
37. *"Let the streetlights run like water down the glass,"* — a long unlit stretch: no streetlights at all, her face almost gone in the dark, only the dashboard on her chin.
38. *"Let a kind man with the heating on let it pass."* — the driver's shoulder and the back of his headrest, the radio still low, the wipers still going.
39. *"Let me cry in the Uber all the way through town,"* — her hands in her lap holding the unopened tissue packet, the water bottle untouched beside her.
40. *"I'll be fine by my door, I just can't be fine now."* — her forehead against the window, eyes open, watching nothing, held.

### Instrumental — the river

41. The car crossing a bridge, filmed from outside and above, wide, the water black beneath it.
42. The bridge lights coming off the water in a long gold line, no car in frame, the first warm exterior of the video.
43. Her face turning to look at it properly, the first time she has looked out rather than at the glass, close-up.
44. The driver's eyes in the mirror strip, noticing that she has stopped, and looking away again.
45. One bar where only rain is audible: a static shot of the windscreen at a red light, the wipers stopping mid-sweep. The cut into the bridge.

### Bridge — arrival

46. *"Near the bridge the crying stops of its own accord,"* — her face, dry, not repaired, just finished, static, the passing lights slowing.
47. *"The way rain does, without deciding to."* — the windscreen: rain thinning to nothing, the wipers still going out of habit over dry glass.
48. *"The lights come off the water in a long gold line,"* — reuse shot 42 from inside the car instead, framed through her window past her shoulder.
49. *"And the city carries on without you."* — a night bus pulling away, a man locking up a shop, two people laughing under an awning — the world, indifferent.
50. *"He says, that's you there, love, mind how you go,"* — the car pulling in at a kerb, the mirror strip, a hand gesturing at a house.
51. *"And I tip him more than I have and tell him so."* — the phone screen, a tip being added (composited), then her leaning forward to say thank you properly.
52. *"The rain has come to nothing by the time I reach my floor,"* — the door opening onto a street where the rain has stopped and everything is dripping and lit.
53. *"And I'm not fine, but I'm fine enough to open my door."* — her standing on the kerb as the car pulls away, alone, upright, the strings arriving.

### Final chorus — the walk to the door

54. *"Let me cry in the Uber, I'll be fine by my door,"* — tracking behind her up a wet garden path, keys already in her hand, the tail lights leaving frame behind her.
55. *"Half an hour, that's all, I won't ask for more."* — her boots on wet paving, puddles carrying the streetlight, low and close.
56. *"Let the streetlights run like water down the glass,"* — a last look back at the empty street where the car was, over her shoulder.
57. *"Let a kind man with the heating on let it pass."* — the empty road, one set of tail lights turning a corner and gone.
58. *"I didn't text you, I didn't ring, I didn't say a thing,"* — her phone in her hand, screen dark, going into her coat pocket without being unlocked.
59. *"I cried in the Uber all the way through town,"* — the key going into her own lock, macro, her breath visible in the cold.
60. *"And I'm fine by my door, I'm fine, I'm fine now."* — the door opening onto her own hall light, seen from outside, the warmest frame in the video.

### Post-chorus — five stars

61. *"Five stars for the man who let me be a mess,"* — a phone on a hall table, a rating being given (composited), her thumb steady.
62. *"Five stars for the rain on the glass,"* — a half-second reprise of shot 19, warmer than it was.
63. *"Five stars for the key and the hall light on,"* — the key still in the door, the hall light above it, macro.
64. *"And a girl who got herself home at last."* — her closing the front door behind her from inside, the street sealed out.

### Outro — the hallway

65. *"Kettle on, coat on the floor, phone face down,"* — three static macros: a kettle beginning to steam, the wet coat dropped on the floor, the phone going face-down.
66. *"Tomorrow I'll be someone who cried in a car and lived."* — her sitting down on the bottom stair with her shoes still on, wide, hall light above her.
67. *"Tonight I'm a woman in a hallway with her shoes still on,"* — close-up of her face, no makeup left, calm, breathing normally for the first time.
68. *"And the hall light's on, and the worst of it has gone."* — final shot: her from behind on the stair under the hall light, held until the piano stops and the kettle clicks off. No text.

## 5. Edit and the challenge

Markers at: the door click in shot 4, the tissues at 23, each *"cry in the
Uber"*, the bridge crossing at 41–42, the silent rain bar at 45, the tip at
51, the key at 59, and the kettle at the very end. At 90 BPM a bar is 2.67 s;
the choruses hold across two bars per shot, which is why they play slower
than the verses even though the cut rate is the same.

**The window challenge.** Post the vertical cut of shots 17–19 with *"let me
cry in the Uber, I'll be fine by my door"* on screen, and invite people to
post their own window-on-the-way-home footage: no face, no words, just the
glass and the city. The tissues shot is the second shareable frame, and the
five-stars post-chorus is the caption people will steal.

## 6. Quality-control checklist

- The driver never has a full face in any frame — hands, shoulder, ear, mirror strip only
- The ex is faceless in every memory; no full-face generation of him exists in this video
- Two looks: green coat for the entire journey, coat removed only from shot 65 on
- All through-glass city is a composited plate; never ask for a sharp face and a smeared city in one generation
- The rain decreases monotonically from shot 1 to shot 52 and never comes back
- All screens, maps, tips and ratings composited; no model-generated text anywhere
- Doorways are the only warm light in the video: his at shot 1, hers from shot 60 on
- The last shot is static and holds until the kettle clicks off
