# Wan 2.2 Shot List — "Closure Isn't a Text"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
88 BPM a bar is 2.73 s, so most shots run 4–6 s; this is a slow, patient
video and nothing except the post-chorus cuts on the beat.

## 1. Visual style

One flat, one winter into one spring. **The door is the protagonist.** It is
shot the way a face is shot: from her eye level on the hallway floor, from
outside as it closes, in macro on the handle, latched, still, sunlit. The
video's two halves are separated by nothing but light — the winter half is
lit by a single lamp at three in the morning, the spring half by open windows
and no lamps at all. Grain, soft focus falloff, handheld only when she is
waiting. Nothing here is glamorous.

| Section | Grade | Camera |
|---|---|---|
| Intro | One warm lamp, deep shadow, blue window | Overhead and static, very close |
| Verse 1 | Harsh overhead kitchen light, then cold winter daylight | Static interiors, handheld outside |
| Pre-chorus 1 | A strip of landing light under a dark door | Locked-off at floor level |
| Choruses | Warm interior against cool hallway, the closing gap of light | Slow, deliberate, one move per shot |
| Verse 2 | Flat bright April daylight, plus the match flare | Static, macro-heavy |
| Instrumental | Daylight only, no lamp in frame | Macro and one long still wide |
| Bridge | Flat ordinary daylight, deliberately uncinematic | Handheld, loose, unstyled |
| Final chorus / post-chorus | Brightest in the video, all natural | Wide, then one-beat hand inserts |
| Outro | Clean morning, no lamps anywhere | Slow, still, holding |

## 2. Character bible — paste into every prompt

**Mahima** (winter, waiting — intro, verse 1, pre-chorus one, chorus one)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slept-on, no makeup, wearing a washed-out grey long-sleeved thermal top and flannel pyjama trousers with thick socks, awake and hollow expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (April, the letter — verse 2, pre-chorus two, chorus two)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back off her face, no makeup, wearing a faded blue denim shirt over a white vest with the sleeves pushed up, focused settled expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the ordinary Tuesday and after — bridge, final chorus, outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down with a middle part, light natural makeup, wearing a soft oatmeal jumper and straight jeans, easy unbothered expression, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — never appears. Not a hand, not a shoulder, not a voice, not a
photograph. He is present only as an absence: an unanswered door, a page that
never arrives, a name said out loud in shot 56 that the audience does not
hear. **Do not generate him in any frame.**

**The friend** (verse 2) — one young woman across a kitchen table, face fine,
warm, seen once for two seconds.

**The delivery driver** (verse 1) — faceless, cropped at the chest, seen
once at a doorway in winter.

Objects that must stay continuous: the **lamp** (on in the intro, off in the
instrumental, off and daylit in the outro), the **envelope covered in
crossed-out questions**, the **six handwritten pages**, the **single match**,
the **white ceramic basin**, the **front door and its handle**, the **phone**
(face-up and out of reach in shot 4, in a drawer by shot 42, never again).

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All handwriting, screens and the ceiling music are composited or implied in
the edit.** Generate the envelope and the pages as blank paper with pen
movement and overlay illegible cursive in post — the words must never be
readable, because the whole point is that nobody reads them. The phone screen
stays dark in every shot it appears in.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA. There is
no second character to lock, which makes this the simplest bible in the
catalogue and the hardest video to keep interesting — lean on the macro work.
Keyframes first; Depth for the hallway and the door shots, which are the
video's spine and must feel like the same real space every time; OpenPose
only for the step-ladder shot. 16:9 first; 9:16 for the chorus and
post-chorus cuts. Animate conservatively: a pen moving, a flame taking a
corner, ash under running water, a door swinging the last few inches, steam
off a kettle.

**The match burn (shots 31–34) is the one shot to over-cover.** Generate at
least six variants; fire is where the model most often produces something
that reads as fake, and this is the emotional centre of the video.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s. The three door frames (shots 17, 21, 77) are generated from
the same plate at different times of day so the closing match cut reads.

## 4. Scene per lyric line

### Intro — three in the morning

1. *"Three in the morning and the ceiling's got nothing"* — directly overhead on Mahima (winter look) lying awake, blanket to her chin, eyes open, static, one lamp.
2. *"Same four walls, same question in my throat"* — her point of view: a flat, empty ceiling, held long enough to be uncomfortable, no movement at all.
3. *"Why is the only thing I ever wanted from you"* — her face turned toward the lamp, close-up, the light on one side only.
4. *"A couple of sentences you never wrote"* — the phone face-up on the far side of the room, screen dark, deliberately out of reach, static wide.
5. *"I keep a light on like an answer might arrive"* — the lamp burning in the corner of the dark room, macro on the filament, nothing else in frame.
6. *"Like the truth is running late but alive"* — her turning over away from the phone and not sleeping, medium, held.

### Verse 1 — the rehearsal and the ringer

7. *"Wrote it all out on the back of an envelope"* — a pen working down the back of an envelope, questions numbered then crossed out (handwriting composited, illegible), macro, harsh overhead light.
8. *"Every question I'd have asked you if you'd stayed"* — her mouthing a sentence to herself at the kitchen table, trying a different emphasis, close-up.
9. *"Rehearsed the level voice, the careful wording"* — her sitting up straighter and starting the sentence again, practising calm, medium, static.
10. *"The version of me that would not be afraid"* — her reflection in the dark kitchen window, the version she is rehearsing, close-up.
11. *"Kept the ringer on right through December"* — the phone on a café table, ringer visibly on, winter light through the window, macro.
12. *"Picked up numbers that I didn't know by name"* — her answering at a doorway to a faceless delivery driver, bright and polite, medium, cold daylight.
13. *"Every time it wasn't you, it landed"* — the tiny drop in her face after she closes the door, held two seconds longer than comfortable, close-up.
14. *"And every time I answered I sounded just the same"* — her walking a winter street with the phone in her hand, breath visible, tracking, low sun.

### Pre-chorus 1 — the waiting posture

15. *"I was holding out my hands for something"* — her sitting on the hallway floor with her back to the wall, facing the front door, wide, floor level.
16. *"You were never going to put in them"* — her hands open on her knees, palms up, macro, the only light a strip under the door.
17. *"Waiting on a knock that isn't coming"* — the front door from her eye level, closed, filling the frame, locked-off. **The door's first portrait.**
18. *"On a night that isn't ever going to end"* — the strip of landing light under the door, someone's shadow passing on the landing and going by, macro.

### Chorus 1 — the door

19. *"Closure isn't a text, it's a door I close myself"* — her hand landing on the inside handle of the front door, close-up, warm interior light.
20. *"It was never coming from anybody else"* — she pushes it, and from outside the gap of warm light narrows toward nothing, slow, static. **The hook frame.**
21. *"I could wait forever for a page you'll never write"* — the door closed from outside, the light gone, the street cold and blue, wide.
22. *"Or put the pen down and turn out the light"* — her back against the closed door on the inside, eyes shut, breathing out, medium.
23. *"Closure isn't a text, it's the quiet in my chest"* — a wide of the whole flat with every internal door standing open except one, static.
24. *"It's the room I finally leave and let it rest"* — her walking out of a room and pulling its door softly to behind her without looking back.
25. *"No apology arriving, no last word to spell"* — the empty hallway floor where she was sitting in shot 15, nobody in it, static.
26. *"Closure isn't a text, it's a door I close myself"* — the lamp switched off, the flat going dark, one frame held after the click.

### Verse 2 — April, six pages, the match

27. *"Sat down in April with a proper pen and paper"* — Mahima (April look) at the kitchen table in flat daylight, good paper, a real pen, writing fast, medium.
28. *"Six long pages that you're never going to see"* — pages accumulating face-down in a pile beside her hand, macro, the handwriting never visible.
29. *"Told you about the bathroom light I fixed alone"* — a two-second cut: her on a step ladder fitting a bathroom light on her own, the fitting coming good.
30. *"And the friend who said your name and looked at me"* — a two-second cut: a friend across a kitchen table saying something and watching her face carefully.
31. *"Then I read it once and took it to the sink"* — her standing, reading the pages once through, then carrying them to the sink, tracking.
32. *"Held a match to the corner, watched it go"* — a match struck and held to a corner, the flame taking, macro, the warmest light in the video.
33. *"Ash in the basin with the water running over"* — the pages curling in a white ceramic basin, then the tap running and the ash going grey, macro.
34. *"And I got the answer that I wrote, not the one you owe"* — her hands under the running water afterwards, washing them, close-up, held.

### Pre-chorus 2 — the hallway, changed

35. *"I stopped holding out my hands for something"* — the same hallway floor as shot 15, empty, sunlight lying across it, identical framing.
36. *"You were never going to put in them"* — her hands, now busy: carrying a laundry basket past the door without a glance, close-up.
37. *"There's no knock coming and I stopped listening"* — the front door from the same eye level as shot 17, in daylight, unremarkable, locked-off.
38. *"And the night I thought would never end just did"* — daylight where the strip of landing light was, the gap under the door bright, macro.

### Chorus 2 — routine

39. *"Closure isn't a text, it's a door I close myself"* — her closing an internal door softly with both hands, unhurried, medium.
40. *"It was never coming from anybody else"* — a key turning in the front door without any drama, macro.
41. *"I could wait forever for a page you'll never write"* — the flat seen from the front doorway, tidy, lived-in, warm afternoon, wide.
42. *"Or put the pen down and turn out the light"* — the phone going into a drawer and the drawer sliding shut, close-up. **The phone is not seen again.**
43. *"Closure isn't a text, it's the quiet in my chest"* — her sitting on the sofa doing nothing at all, calm, wide, late gold.
44. *"It's the room I finally leave and let it rest"* — the bedroom from the intro, made, empty, daylit, static.
45. *"No apology arriving, no last word to spell"* — the envelope from shot 7 dropping into a bin without ceremony, macro.
46. *"Closure isn't a text, it's a door I close myself"* — the front door in afternoon light, closed, still, holding into the break.

### Instrumental — the ash and the empty room, no lyrics

47. Macro on wet grey ash swirling down a plughole, the last of it going, water running clear.
48. Her lying on the floor of the front room with her feet up the wall, listening to nothing, wide, daylight.
49. The lamp from the intro switched off in broad daylight, her hand leaving the switch, close-up.
50. A slow pan across the flat with every window open and the curtains moving, no lamp in frame anywhere.
51. Two bars of pure room tone: the still, empty, sunlit hallway, nothing moving — the cut into the bridge.

### Bridge — an ordinary Tuesday

52. *"Turns out closure isn't a confession"* — Mahima (Tuesday look) in a supermarket aisle, handheld, flat overhead light, deliberately uncinematic.
53. *"It isn't you explaining what you meant"* — her humming along to the ceiling music without noticing she is doing it, close-up, loose handheld.
54. *"It's a Tuesday when I hear a song and hum it"* — her hand putting something ordinary in a basket, still humming, macro.
55. *"And I don't go looking for where you went"* — her at a checkout, phone nowhere, paying and talking to the cashier, medium.
56. *"It's a name I say out loud without a flinch"* — her mid-sentence in conversation outside, saying a name easily, her face not changing at all, close-up.
57. *"It's an old address I drive past and don't slow"* — from inside a car: a familiar turning going past at unchanged speed, her hands steady on the wheel.
58. *"It's not a message. It was never going to be a message."* — her face driving, entirely ordinary, no music-video emotion, close-up, held.
59. *"It's just the day I stopped needing you to know"* — the car indicator not going on, the turning disappearing in the mirror — the cut into the final chorus.

### Final chorus — light everywhere

60. *"Closure isn't a text, it's a door I close myself"* — every window in the flat open at once, curtains moving, brightest frame in the video, wide.
61. *"It was never coming from anybody else"* — her walking room to room switching lamps off in daylight, tracking.
62. *"I'm not waiting on a page you'll never write"* — a blank pad on the kitchen table with the pen capped beside it, macro.
63. *"I put the pen down and I turned out the light"* — the last lamp switched off, the room not getting any darker, close-up.
64. *"Closure isn't a text, it's the quiet in my chest"* — her standing in the middle of the flat with her eyes closed for one beat, wide, calm.
65. *"It's the room I finally left and let it rest"* — the bedroom door pulled softly to from the hallway side, macro on the latch.
66. *"No apology arriving, and there's nothing to tell"* — from outside the building: a closed front door in a sunlit street, wide, nobody around.
67. *"Closure isn't a text, it's a door I close myself"* — her hand leaving the handle on the inside, the latch settling, macro, held.

### Post-chorus — doors, in rhythm

68. *"Close it soft, close it slow"* — a wardrobe door closing gently, hands only, one beat.
69. *"Not a slam and not a show"* — a kitchen cupboard closing gently, one beat.
70. *"Close it soft, close it slow"* — a car door pushed to rather than swung, one beat.
71. *"Turn the handle, let it go"* — a bedroom door, the handle turned first so the latch does not click, one beat. **The technique shot.**
72. *"Close it soft, close it slow"* — a garden gate easing shut, one beat, daylight.
73. *"And I don't need you to know"* — the front door, closed softly, the hand leaving, two beats, held.

### Outro — morning

74. *"There's a light I don't leave on for you now"* — the lamp from the intro, off, in full daylight, macro, the same angle as shot 5.
75. *"And a page in the sink that turned to grey"* — the white basin, clean and dry, one drop of water in it, macro.
76. *"Morning at the window, kettle going"* — a kettle beginning to steam by a bright window, her hand reaching for a mug, medium.
77. *"And a door I closed myself, and it stayed"* — final shot: the front door from inside, closed, still, morning sunlight moving slowly across it, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the overhead in shot 1, the phone out of reach, each *"closure
isn't a text"*, the match, the ash going down the plughole, the instrumental,
*"it's just the day I stopped needing you to know"*, the phone going in the
drawer, and the final door. At 88 BPM a bar is 2.73 s; nothing in this video
cuts on the beat except the post-chorus, which is why the post-chorus feels
like a decision.

**The burn-it challenge.** Post the vertical cut of verse two (shots 31–34)
with *"closure isn't a text"* on screen and invite people to write the thing
they would have sent and film one match. The soft-close door montage (shots
68–73) is the second format and the more repeatable one.

## 6. Quality-control checklist

- Three looks in the right sections: grey thermal only in the winter half, denim shirt only in April, oatmeal jumper from the bridge on
- The ex never appears in any frame in any form; the name in shot 56 is never audible or legible
- The phone is dark in every shot, out of reach in shot 4, in the drawer by shot 42, and never seen again
- All handwriting is illegible in every frame — the pages must never be readable
- The three door portraits (17, 37, 77) match on lens, height and angle, and differ only in light
- Lamps appear only in the winter half and in shots 49, 61 and 63 being switched off; there is no lamp on after shot 63
- The match burn is over-covered with at least six variants; discard any take where the flame reads as synthetic
- No door in the video is ever slammed, in any shot, including the post-chorus
- The last shot is locked-off and holds until the audio fades
