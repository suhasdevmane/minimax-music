# Wan 2.2 Shot List — "Eyes on Me"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
94 BPM a bar is 2.55 s; most shots run 3–5 s, the choruses hold longer and
cut on the phrase, and the half-rapped verse cuts every half-bar.

## 1. Visual style

One house party, one night, filmed almost entirely in **slow motion**. A
red dress in a room of black, denim and grey; the dress is the only
saturated red in the video apart from the cups. Three spaces: the
**staircase** (where she sees, and where the song ends), the **speaker
corner** (his), and the **window seat** (hers). The camera is low and slow,
crowd shoulders drifting through the foreground out of focus. Warm lamp and
string light with coloured LED spill from the living room; the window is the
one cool source. Kai has a face here and the whole song is about it.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm hallway, staircase in shadow | Steadicam in through the door, then a slow head-turn |
| Verse 1 | Coloured LED on him, warm on her | Long lens across the room, POV swaps |
| Pre-choruses | Warm rooms, getting warmer | Slow-motion tracking through the crowd |
| Choruses | Crowd dark and soft, the two of them lit | One held slow-motion shot per chorus |
| Verse 2 (half-rapped) | Flashback slightly cooler; present warm; window blue | Faster cuts, half-bar, punchy |
| Instrumental | Coloured LED, string lights, red | Overhead, slow motion, one freeze |
| Bridge | Warm, close, party out of focus | Tracking with him, then static two-shot |
| Final chorus / post-chorus | Warmest and widest | Moving, then the staircase from below |
| Outro | Under-cabinet light, hallway lamp | Static, then the door |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and glossy over one shoulder, soft smoky eye makeup and a deep red lip, wearing a fitted knee-length red satin slip dress with thin straps and small gold hoop earrings, confident amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly mussed, soft smoky eye makeup and a deep red lip, wearing the same red satin slip dress with a man's black bomber jacket draped over her bare shoulders, tired satisfied expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the one looking)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a black bomber jacket over a plain white t-shirt and dark jeans, caught-out then warm expression, realistic cinematic photography, consistent identity

**The crowd** — twenty to thirty young adults in black, denim and grey,
never in red, always slightly out of focus, never looking at camera. Kai's
friend at the speaker is seen only from behind or in profile. Mahima's
friend at the window is a young woman in a black top, face soft-focus.

Objects: the **red cup** (hers, full at the door, empty in the outro), the
**speaker stack** (his corner), the **window seat** with a streetlight
outside (hers), the **staircase** with a view of the whole floor, his
**black bomber jacket** (on him until the outro, on her shoulders after).

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The phone in verse 2 is composited in the edit.** Generate it as a lit
blank screen in Kai's hand and overlay an empty lock screen with no
notifications in post — the joke is that nobody is texting him, and the
model cannot render legible UI.

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

Most shots 3–5 s. For this song Mahima has two looks (dress; dress plus
jacket) and Kai is locked with his own LoRA. Depth is essential for the
crowd-through-foreground compositions; render the crowd as a shallow-focus
plate and keep the two leads sharp. Slow motion is done by generating at 24
fps and conforming to half speed in the edit, not by asking the model for
slow motion. The held-look chorus shots (22, 45, 58) are the longest clips
in the video; generate them at 121 frames.

## 4. Scene per lyric line

### Intro — the staircase

1. *"Somebody's playlist, somebody's kitchen, somebody's cousin at the door"* — steadicam in through a front door into a packed hallway, a kitchen full of people to the left, a young man on door duty waving people in, warm lamp light, string lights, the bass thudding.
2. *"Red cup, red dress, I wasn't even gonna come"* — Mahima stepping in from the door in the red dress, the only red in a room of black and denim, a red cup pressed into her hand, medium, slow motion.
3. *"Then I felt it from the staircase like a hand across the room"* — her halfway up the staircase, looking down over the whole floor, and her head turning slowly, in slow motion, toward the far corner, close-up from below.
4. *"Somebody's looking, and I know exactly who"* — her POV over the crowd: Kai by the speaker stack, mid-glance, dropping his eyes; back to her: one eyebrow lifting, extreme close-up.

### Verse 1 — the speaker corner

5. *"You're by the speaker acting like the song is what you're into"* — Kai leaning on the speaker stack nodding to the beat with a friend seen from behind, coloured LED across his face, long lens.
6. *"But your head keeps turning every time I move"* — Mahima taking two steps down the stairs; cut to Kai's head turning toward the staircase; she stops; his eyes drop; slow motion.
7. *"Your boy is talking, and you're nodding, but you're not there"* — Kai nodding at his friend's story, his eyes elsewhere, the friend gesturing in profile, medium.
8. *"You're a satellite tonight, and I'm the view"* — Mahima on the stairs, hand on the banister, looking down at him with a small smile, warm staircase light, close-up.
9. *"I could make it easy, I could walk on over"* — her coming down the last steps, the camera low and slow on her heels and the hem of the red dress.
10. *"Say hey, what's your name, and let it play"* — her reaching the floor, pausing, looking toward the speaker corner, then turning the opposite way, medium, slow motion.
11. *"But where's the fun in easy when you're watching like that?"* — Kai watching her walk away from him, a slightly lost expression, close-up, LED light.
12. *"Baby, I'm gonna make you work for what you're gonna say"* — her walking away into the kitchen crowd, glancing back once over her shoulder, the red dress disappearing between black shirts, tracking from behind.

### Pre-chorus 1 — the long way round

13. *"So I'm gonna take the long way round the room"* — Mahima weaving through the kitchen crowd in slow motion, shoulders drifting past the lens out of focus, tracking alongside.
14. *"Touch my hair, laugh at nothing, take my time"* — her tucking hair behind her ear, then laughing at something a friend says, head back, slow motion, close-up.
15. *"Every step I take is a step you gotta follow"* — Kai at the speaker, his head turning to follow her across the room like it is on a string, the friend still talking, medium.
16. *"Don't you look away, you're doing fine"* — her in the hallway doorway, backlit, looking straight at him across the room for one second, then moving on, medium.

### Chorus 1 — the glance that lasts a whole chorus

17. *"Keep your eyes on me, I know you already do"* — one held slow-motion shot begins: Mahima stops in the middle of the living room, turns, and looks straight at Kai across the crowd, cups and shoulders drifting between them out of focus, long lens.
18. *"I felt it from the staircase, now I'm proving it to you"* — the same shot continues, her weight shifting to one hip, chin up, the look unbroken.
19. *"Keep your eyes on me, don't blink and don't pretend"* — reverse: Kai, not looking away this time, the friend beside him giving up and leaving frame, close-up.
20. *"I'll keep you looking, baby, till the song is at its end"* — back to her, the crowd thickening between them and her not moving, the look still held.
21. *"Eyes on me, eyes on me"* — extreme close-up of her eyes, the coloured LED moving across them, slow motion.
22. *"I know you already do"* — the wide of the whole room with the two of them the only sharp things in it, the crowd a soft blur, hold.

### Verse 2 — half-rapped, reading him (half-bar cuts)

23. *"Look, I saw you clock me when I came in the back"* — flashback, slightly cooler: Kai mid-laugh with three friends by the speaker, his eyes catching the back door as a red dress comes through it, freeze on his face.
24. *"Red dress, no stress, you froze mid-laugh"* — the same frame, his laugh stopping halfway, mouth still open, a friend's hand mid-gesture, extreme close-up.
25. *"Your whole conversation went flat, and I like that"* — the friend's sentence trailing off, looking at Kai, then following his eyes, medium.
26. *"I didn't do a thing yet, I just took off my jacket"* — flashback: Mahima at the back door shrugging a denim jacket off her shoulders and handing it to someone, not looking at anyone, slow motion.
27. *"Now you're doing that thing where you check your phone"* — present: Kai pulling out his phone and staring at it hard, close-up on his face lit by the screen.
28. *"Like you got a text, but I know that you don't"* — the phone screen: a blank lock screen, no notifications (composited), his thumb hovering, macro.
29. *"Nobody's texting you at eleven on a Friday"* — Mahima across the room watching him pretend, a slow grin, chin on her hand, close-up.
30. *"Put it down, look up, we can do this my way"* — Kai pocketing the phone and looking up; she has already looked away, medium two-shot across the room.
31. *"I'm not gonna wave, I'm not gonna call you over"* — her crossing to the window seat and settling in, one arm along the sill, the streetlight blue on that side of her face, medium.
32. *"I'm gonna let the whole room turn in slow motion"* — overhead of the whole party turning in slow motion, the red dress at the window edge, the black jacket at the speaker corner, wide.
33. *"You'll find me by the window when your nerve kicks in"* — her at the window seat watching the room, not him, a friend sitting down beside her, medium.
34. *"Take your time, I got all night, and I already win"* — extreme close-up of her mouth on the last word, the red lip, a slow smile.

### Pre-chorus 2 — from above

35. *"So I'm gonna take the long way round the room"* — the room from the staircase view, slow motion, the camera finding Kai starting to move, then stopping, then moving again, wide.
36. *"Touch my hair, laugh at nothing, take my time"* — reuse shot 14, at the window seat this time, tighter.
37. *"Every step I take is a step you gotta follow"* — Kai taking three steps into the crowd toward the window, then a friend grabbing his shoulder, and him stopping, medium.
38. *"Don't you look away, you're doing fine"* — Mahima at the window, not looking at him, smiling at the glass, the window a cool blue rectangle, close-up.

### Chorus 2 — the glance from the window

39. *"Keep your eyes on me, I know you already do"* — one held slow-motion shot begins: Mahima turning her head from the window to Kai, the streetlight cool on one side of her face and the party warm on the other, long lens.
40. *"I felt it from the staircase, now I'm proving it to you"* — the same shot, her not blinking, the split light, hold.
41. *"Keep your eyes on me, don't blink and don't pretend"* — Kai setting his cup down on the speaker without looking at it, eyes on her, close-up.
42. *"I'll keep you looking, baby, till the song is at its end"* — back to her, the friend beside her whispering in her ear and Mahima laughing without looking away, close-up.
43. *"Eyes on me, eyes on me"* — extreme close-up of her eyes with the blue streetlight and the warm room in each one.
44. *"I know you already do"* — wide of the room from the speaker corner, the window seat lit, the two of them the only sharp things, hold.

### Instrumental — the party in full slow motion

45. The dance floor from directly above, bodies moving in slow motion, the red dress at the edge of frame, coloured LED sweeping.
46. A red cup passed hand to hand down a hallway, macro, slow motion.
47. Mahima's friend whispering something outrageous in her ear, Mahima laughing hard and still not looking away from the speaker corner, close-up.
48. Kai taking a breath, pushing off the speaker stack with his shoulder, and stepping into the crowd, tracking from the front.
49. Drop to near silence: the two of them, the crowd frozen between them, the shot holding — the cut into the bridge.

### Bridge — the crossing, the twist

50. *"When you finally cross the floor, two hundred people in the way"* — Kai moving through the crowd toward the window, people parting slowly, tracking with him, warm.
51. *"I'm gonna act surprised, like I didn't plan the whole thing"* — Mahima arranging her face into surprise a beat too late, eyebrows up, a hand to her chest, close-up.
52. *"You'll say something about the song, I'll say, I know, I picked it"* — the two of them at the window, him gesturing back at the speaker, her mouthing something, close two-shot, the party out of focus.
53. *"Then you'll laugh, and that's the moment, I'll admit it"* — Kai laughing, head down, then looking up at her; her face softening, close-up on each.
54. *"Cause I've been watching you watching me since I walked in"* — Mahima straight to camera for the first time in the video, the confession, streetlight and lamp, extreme close-up, static.
55. *"The eyes on me were mine on you the whole time, that's the twist"* — a quick reprise of shot 4's staircase look, then her face now, the same eyebrow.
56. *"So say it, say the thing you've been rehearsing by the speaker"* — Kai starting a sentence, nervous, hand on the back of his neck, medium.
57. *"I'll say yes before you finish, and we'll take it from there"* — her nodding before he is done, him stopping mid-word and grinning, the drums returning, close two-shot.

### Final chorus — next to him

58. *"Keep your eyes on me, I know you already do"* — one held slow-motion shot: the two of them standing side by side at the window, shoulders touching, the party moving around them.
59. *"I felt it from the staircase, now I'm standing next to you"* — her looking up at him, him looking down at her, both grinning, close two-shot.
60. *"Keep your eyes on me, don't blink and don't pretend"* — the two of them pushing through the crowd together toward the staircase, her hand in his, tracking.
61. *"Turns out I was looking too, so let's call it even then"* — the staircase from below, the two of them climbing it to get away from the noise, her looking back down at the room, wide.
62. *"Eyes on me, eyes on me"* — reuse shot 21's extreme close-up of her eyes, now with him reflected in them.
63. *"I know you already do"* — the wide of the room from the top of the stairs, the party carrying on without them, hold.

### Post-chorus — the stairs

64. *"Eyes on me, don't look away"* — the two of them sitting on the stairs halfway up, facing each other, the party below out of focus, medium.
65. *"I know you already do"* — Kai's face, looking at her, not the room, close-up.
66. *"Eyes on me, it's okay"* — her face, looking at him, the same, close-up.
67. *"Cause my eyes are on you"* — the two-shot on the stairs, her head tipping onto his shoulder, warm below, shadow above.

### Outro — half past two

68. *"Somebody's kitchen, half past two, the music's low"* — the kitchen nearly empty, under-cabinet lights only, cups everywhere, the music muffled through the wall, wide static.
69. *"Red cup empty, red dress, your jacket on my shoulders now"* — Mahima (outro look) leaning on the counter with his black bomber jacket over her bare shoulders, an empty red cup beside her, Kai across the counter in his white t-shirt, medium.
70. *"Yeah, I felt it from the staircase, and I knew exactly who"* — her glancing toward the staircase through the kitchen door, then back at him, a small shrug, close-up.
71. *"Keep your eyes on me, I know you already do"* — final shot: the front door from inside the hallway, the two of them leaving together, the door closing on the low music, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the front door, the staircase head-turn, each "keep your eyes on
me", the half-rapped verse entrance, the phone check, the instrumental
freeze, "that's the twist", "standing next to you", and the door closing.
At 94 BPM a bar is 2.55 s; the rap verse cuts every half-bar.

**The walk-in challenge.** Post the vertical cut of chorus 1 (shots 17–22)
with *"keep your eyes on me"* on screen: a doorway, a cut on the beat, a
slow-motion turn-and-look held straight down the lens. Invite people to post
their own entrance with the head tilt on *"I know you already do."* The rap
clip (shots 27–30, the phone with no notifications) is the second cut, and
*"the eyes on me were mine on you the whole time"* (shot 54) is the quote.

## 6. Quality-control checklist

- The red dress is the only saturated red in every frame apart from the cups; the crowd is black, denim and grey throughout
- Kai is recognisable in every shot: cropped hair, short beard, black bomber jacket until the outro, when the jacket is on her
- The three held-look chorus shots (17–18, 39–40, 58) are single continuous clips, not cut
- Slow motion conformed in the edit from 24 fps; no model-generated slow motion
- The phone lock screen is composited and empty; no readable text anywhere
- Crowd faces always soft-focus and never looking at camera; Kai's friend seen only from behind or in profile
- No distorted hands on the cup pass, the banister and the phone macro
- The last shot is locked-off and holds until the audio fades
