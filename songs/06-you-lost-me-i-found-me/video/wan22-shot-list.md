# Wan 2.2 Shot List — "You Lost Me, I Found Me"

**One shot per lyric line**, as requested. Each entry is the line as sung and
the scene for it. Timestamps come from the rendered WAV; cut on the sung
line, not on a clock.

## 1. Visual arc

The whole video is one colour journey: **cold and dim** (bathroom floor,
night street, car) → **neutral** (mirror, kitchen, first solo coffee) →
**warm and bright** (flowers, dancing, daylight city, final look to camera).
Grade every shot to where it sits on that line. The ex is **never shown
clearly** — a silhouette, a hand, a voice on a phone, keys on a table.

| Section | Grade | Camera |
|---|---|---|
| Intro / Verse 1 | Cold blue-grey, single practical light | Static, close, low |
| Pre-chorus 1 | Cold, one warm bulb entering | Slow push-in |
| Chorus 1 | Neutral, morning | Handheld montage on the beat |
| Verse 2 | Neutral → warming | Handheld, closer |
| Pre-chorus 2 | Warm | Slow push-in, mirror |
| Instrumental | Warm, saturated | Fast cuts |
| Bridge | Night again, but warm lamp not cold bulb | Static, still |
| Final chorus | Bright daylight, golden | Wide tracking, moving |
| Outro | Golden hour, calm | Slow, ends on a locked-off close-up |

## 2. Character bible — paste into every prompt

**Mahima** (early scenes)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair loose and unkempt, no makeup, tear-streaked, wearing an oversized grey t-shirt and black leggings, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (healing scenes)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair tied back, minimal natural makeup, wearing a soft cream cardigan over a white top and blue jeans, calm open expression, realistic cinematic photography, consistent identity

**Mahima** (final chorus / outro)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair freshly cut to the collarbone and loose, light natural makeup, wearing a rust-orange blazer over a white top and wide-leg trousers, confident easy smile, realistic cinematic photography, consistent identity

The **haircut** is the visible turn: long and unkempt until pre-chorus 2,
collarbone-length from the instrumental on. The **rust-orange blazer** is the
final-act colour, the first warm thing she wears.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

Phone screens and handwritten text: composite in the edit, never leave to
the model.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks (front, three-quarter, profile, full body,
neutral and emotional) with IP-Adapter or a character LoRA. Keyframes first;
OpenPose for the dance and the city walk; Depth for the bathroom and mirror
compositions. 16:9 first; 9:16 for the before/after challenge cuts. Animate
conservatively: breathing, tears, hair, a hand closing a phone, rain.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Lines are short, so most shots are 3–5 s. Where two consecutive lines are
one image, the second entry says *hold*.

## 4. Scene per lyric line

### Intro — cold, dim, static

1. *"I still remember the night I fell apart"* — Mahima (early look) sitting on a bathroom floor at night with her back against the tub, knees up, one dim bulb over the mirror, cold blue-grey, static wide, very still.
2. *"Sitting on the bathroom floor in the dark"* — hold, slow push-in on her face, eyes open and empty, tear tracks catching the light.
3. *"Your voice on repeat in my head like a knife"* — extreme close-up of a phone on the tiles beside her, screen lit with a voice-message waveform playing, her hand not reaching for it.
4. *"Telling me I was too much, not enough, not right"* — her flinching slightly with each phrase as if hearing it, jaw tight, close-up, static.
5. *"I cried till my chest felt empty and cold"* — her curling forward over her knees, shoulders shaking once, then still, medium shot, cold light.
6. *"Wondering if I'd ever feel whole"* — her looking up at the dark ceiling, breath visible in the cold, the bulb flickering once.
7. *"But somewhere between the tears and the silence"* — the phone screen going dark on the tiles, the room quieter, her hand flattening on the floor.
8. *"A new version of me started to rise"* — her pushing herself up off the floor by the tub edge, rising into frame, the camera tilting up with her, still cold but her spine straight.

### Verse 1

9. *"You said I was dramatic for needing more"* — a kitchen at night, a man's silhouette in the doorway with his back to camera, Mahima at the table small in the frame, one overhead light, static.
10. *"For wanting love that didn't keep score"* — close-up of her hands on the table, a cold mug, her thumb rubbing the rim, his shadow across the table.
11. *"You called it too much when I asked to be seen"* — her looking up at the silhouette and speaking, then looking down again, medium close-up, the silhouette unmoving.
12. *"Then acted surprised when I stopped playing small in your scene"* — her standing up from the table, chair scraping, his silhouette turning slightly, her face set, static.
13. *"I packed my bags in the middle of the night"* — a bedroom lit by a phone torch, Mahima folding clothes into a duffel bag fast and quiet, handheld, cold.
14. *"Left your keys on the table, turned off the light"* — extreme close-up of her hand setting a set of keys on the kitchen table, then the overhead light switching off, the keys the last thing lit.
15. *"I didn't slam doors, I didn't scream loud"* — her closing the apartment door behind her with two hands, slowly, no sound, the hallway light on her back.
16. *"Just walked out quiet, head held proud"* — her walking down a rain-wet street at night with the duffel bag, streetlights haloed, chin up, tracking from the side, cold blue with orange sodium light.

### Pre-chorus 1 — one warm bulb enters

17. *"That was the night I stopped begging for love"* — a small cheap hotel room, Mahima sitting on the edge of the bed with the bag at her feet, one warm bedside lamp, the first warm light of the video, static.
18. *"Stopped shrinking myself to fit in your world"* — her taking a breath and sitting up straighter, shoulders back, close-up, lamp light.
19. *"I looked in the mirror, eyes red from the rain"* — her standing at a bathroom mirror, hair wet from rain, eyes red, looking at herself directly, over-the-shoulder into the mirror, slow push-in.
20. *"And whispered, we're not doing this again"* — extreme close-up of her mouth forming the words to her reflection, then her eyes, a small decision landing in them.

### Chorus 1 — morning, neutral, montage on the beat

21. *"You lost me, but I found me"* — morning light, Mahima (healing look) at a window with coffee, the first daylight in the video, medium shot, soft.
22. *"In the pieces you left on the floor"* — close-up of her hands gathering a few of his things from a floor into a box: a photo frame face-down, a hoodie, a charger.
23. *"You walked out, but I stayed true"* — her carrying the box out to a hallway and setting it down without ceremony, then walking back in and shutting the door.
24. *"And built something stronger than before"* — her phone in hand: a chat thread being deleted, a contact being blocked, each on the beat, then the phone set face-down.
25. *"You thought I'd break, I'd fall apart"* — her at a café counter alone ordering, a tiny nervous smile at the barista, handheld.
26. *"But you gave me back my own heart"* — her sitting at a café window alone with the coffee, watching the street, not checking her phone, warm neutral light.
27. *"Now I'm standing here, finally free"* — her walking alone through a park in daylight, hands in pockets, first solo walk, tracking from the front.
28. *"You lost me, but I found me"* — close-up of her first real smile, small and surprised at itself, daylight on her face.

### Verse 2 — neutral warming to gold

29. *"The first few weeks, I cried in the car"* — Mahima in a parked car at night in a supermarket lot, forehead on the steering wheel, dashboard light, static.
30. *"Replayed every fight, every scar"* — her staring through the windshield, rain on the glass, her reflection in it, close-up.
31. *"Wondered if maybe I was the problem"* — her hands gripping the wheel, then letting go, medium shot inside the car.
32. *"If love was supposed to feel this wrong"* — her wiping her face with her sleeve and starting the car, the headlights coming on and lighting the frame.
33. *"But then I started saying no more"* — daytime, her on the phone at a kitchen counter shaking her head with a calm firm expression, then hanging up, neutral light.
34. *"Started locking my own front door"* — extreme close-up of her hand turning a new deadbolt on her own front door, a fresh brass lock, warm hallway light.
35. *"Started sleeping through the night"* — her asleep in a bed with morning light arriving across the pillow, peaceful, overhead shot, slow.
36. *"Started believing I deserved light"* — her opening bedroom curtains and sunlight flooding the room and her face, medium shot from behind, warm.
37. *"I bought myself flowers, took myself out"* — her at a flower stall choosing a bouquet for herself, then walking with it down a sunny street, handheld, warm.
38. *"Learned what peace feels like without doubt"* — her cooking for one in a small kitchen, music on, the flowers in a jar on the counter, golden evening light.
39. *"I stopped checking your stories, stopped waiting by the phone"* — her phone on the counter lighting up and her not looking at it, continuing to stir a pan, close-up on the phone then on her.
40. *"Started building a life that felt like my own"* — her dancing alone in the living room in socks, badly and happily, the flowers behind her, wide handheld, warm.

### Pre-chorus 2 — the mirror, warm

41. *"That was the moment I stopped looking back"* — her at a hair salon chair as long hair falls to the floor, seen from behind, warm light, the haircut.
42. *"Stopped tracing your name in the dust on my glass"* — close-up of her wiping a dusty windowpane clean with her sleeve, the street outside coming into focus.
43. *"I looked in the mirror, this time with a smile"* — the same mirror composition as shot 19, but daylight, hair at her collarbone, and she is smiling at herself, slow push-in.
44. *"And said, girl, you've been worth it all along"* — extreme close-up of her mouth saying the words to her reflection, then her eyes, steady and kind. The one moment she addresses herself directly.

### Chorus 2

Reuse shots 21–28 with a warmer grade and slightly wider framing. Chorus 1
was relief; chorus 2 is confidence.

### Instrumental — fast cuts, saturated warm

45. Gym, early morning, Mahima on a treadmill, headphones, sweat, focused.
46. A journal open on a bed, her writing fast, a mug beside it, lamp light.
47. Her at a laptop late at night, working, a small smile at the screen.
48. Her laughing hard with two friends at a bar table, head thrown back.
49. Her alone at an airport gate with a small suitcase, looking out at the planes, calm.
50. Her on a balcony at sunset with a glass of wine, hair blowing, eyes closed.
51. Brief drop: a black frame, then her face in the dark, breathing — the cut into the bridge.

### Bridge — night again, but a warm lamp

52. *"There were nights I almost called you"* — Mahima (healing look) sitting up in bed at night, phone in hand, his name on the screen, thumb hovering, warm lamp light, static.
53. *"Almost typed I miss you and hit send"* — extreme close-up of the phone screen with three words typed in a message box and the send arrow, her thumb over it. (Composite the text in post.)
54. *"Almost believed your version of me"* — her face in the lamp light, doubt crossing it, her looking at the ceiling, close-up.
55. *"Almost forgot who I was again"* — her thumb moving toward send, then stopping, the screen light on her face, static.
56. *"But then I remembered the girl in the bathroom"* — a two-second flash of shot 1, the bathroom floor, cold, then back to the bed.
57. *"The one who cried till she couldn't breathe"* — her eyes closing, one slow breath, the lamp light steady.
58. *"And I promised her I wouldn't go back"* — her deleting the typed words one letter at a time, close-up on the screen and her thumb.
59. *"I promised her I'd choose me"* — her looking up from the phone with a settled expression, close-up, warm.
60. *"So I turned off the light, put the phone down"* — her placing the phone face-down on the nightstand and switching off the lamp, the frame going to near-black.
61. *"Lay in the dark and just breathed"* — her lying back in the dark, only a little window light on her face, a long exhale, overhead shot.
62. *"And for the first time, the silence felt safe"* — the still dark room, her eyes open and calm, static, very quiet.
63. *"Like my own heart was enough to keep me"* — her hand resting flat on her own chest in the dark, the smallest smile, extreme close-up.

### Final chorus — daylight, golden, moving

64. *"I'm not the girl who begs for love"* — hard cut to bright daylight, Mahima (final look) in the rust-orange blazer stepping out of her front door onto a sunny street, wide, the first fully bright frame.
65. *"Not the one who hides who she is"* — her walking down the city street with her hair loose and her head up, tracking from the front, golden.
66. *"I'm the one who walked through fire"* — her crossing a busy crossing with the crowd, unhurried, sun flare, slow motion.
67. *"And came out whole in the end of it"* — her meeting two friends on the pavement, a hug, laughing, handheld, warm.
68. *"You lost me, but I found me"* — the three of them walking together, Mahima in the middle singing the line out loud, the friends joining in.
69. *"And I'm never giving that back"* — her spinning once on the pavement with her arms out, blazer flaring, sun behind her, slow motion.
70. *"You lost me, but I found me"* — close-up of her singing to camera mid-walk, no fear, golden light.
71. *"And I'm never going back"* — her stopping at a corner, looking back over her shoulder down the street for one beat, then turning forward and walking on.

### Outro — golden hour, calm, ends locked-off

72. *"Sometimes I pass that old street"* — Mahima (final look) walking alone at golden hour and slowing as she reaches a familiar apartment building, wide, warm.
73. *"Where I cried and couldn't breathe"* — her looking up at a dark window on the second floor, a two-second flash of the bathroom, then back to her face in the gold light.
74. *"Now I walk with my head up high"* — her walking on past the building without stopping, chin up, tracking from the side.
75. *"No longer asking why"* — close-up of her face in profile, peaceful, the building sliding out of frame behind her.
76. *"You lost me, but I found me"* — her turning a corner into full sunset light, the street opening up ahead, wide.
77. *"In the quiet after the storm"* — a still shot of the rain-washed street behind her, empty, golden, puddles reflecting the sky.
78. *"You lost me, but I found me"* — her slowing to a stop and turning toward the camera, locked-off medium shot.
79. *"And this time, I'm finally home"* — final locked-off close-up: Mahima looking straight into the camera, calm, sure, the smallest smile, holding it through the fade. No text.

## 5. Edit and the challenge

Add markers at: the first vocal entrance, "we're not doing this again", each
"You lost me, but I found me", the instrumental, the word "Mahima", "put the
phone down", the hard cut to daylight at "I'm not the girl", and the final
"home." At 96 BPM a bar is 2.5 s.

**Before/after challenge.** Shot 1 (bathroom floor) and shot 79 (final look
to camera) are the two frames. Post them as a split with *"You lost me, but I
found me"* on screen and invite before/after transformation clips on the
hook — breakup → glow-up, sadness → confidence. The name line (shot 44) is
the second shareable moment: people saying their own name to a mirror.

## 6. Quality-control checklist

- Three looks in the right sections: unkempt/grey until pre-chorus 2, tied-back cardigan through verse 2, collarbone hair + rust blazer from the instrumental on
- The ex never has a visible face
- Colour temperature only ever moves cold → warm, never back (the bathroom flashes in the bridge and outro are the only exceptions, and they are two seconds)
- The two mirror shots (19 and 43) match framing exactly
- Phone screens composited; no model-generated text
- No distorted hands, especially the keys, the phone, and the deadbolt close-ups
- The final shot is locked-off and holds until the audio fades
