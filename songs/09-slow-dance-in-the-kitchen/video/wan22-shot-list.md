# Wan 2.2 Shot List — "Slow Dance in the Kitchen"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
88 BPM a bar is 2.73 s, so most shots run 3–6 s and the choruses cut every
one or two bars.

## 1. Visual style

One location, one evening, two people. A **tiny apartment kitchen** — six
feet by eight, black and white checkered tile, cabinets with a string of
warm fairy lights taped along them from last December, a windowsill radio,
a stove with a pot on it, a wind-up oven timer. The whole video should feel
like a **single continuous night**: the bottle goes down, the pot boils
over, the toast burns, the timer dings, the string lights flicker. Warm
practical light only. Nothing outside the apartment is ever shown except
through the blinds in the intro and in one hallway-mirror memory.

| Section | Grade | Camera |
|---|---|---|
| Intro | Fridge light, one string of fairy lights, blue street light killed by the blinds | Static close-ups |
| Verses | Warm stove lamp and fairy lights, steam haze | Handheld, low angles on the socks |
| Pre-choruses | Warm, steady | Slow push-ins on hands and faces |
| Choruses | Warmest and fullest, all practical lights on | Slow circling, one overhead |
| Instrumental | Fairy lights and stove lamp only, dim | Overhead, extreme close-ups |
| Bridge | Single stove lamp; the hallway memory in cool morning light | Static, close |
| Final chorus / post-chorus | Every light on, then dimming | Circling, then still |
| Outro | Stove lamp, then fridge light, then fade | Locked-off wide |

## 2. Character bible — paste into every prompt

**Mahima** (the whole video, one look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and tucked behind one ear, no makeup, wearing an oversized grey knit cardigan over a white vest and soft black leggings, mismatched socks, one striped and one plain, warm amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the whole video, one look)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded navy t-shirt with a flour handprint on the chest from the final chorus onward and grey joggers, odd socks, one black and one white, sheepish easy smile, realistic cinematic photography, consistent identity

Objects: the **wind-up oven timer** on the counter, the **windowsill radio**
with a glowing dial, the **string of fairy lights** taped along the
cabinets, the **cheap bottle of red** with a screw cap, a **chipped mug and
a jam jar** as the two cups, the **burnt toast**, the **restaurant flyer**
under a magnet on the fridge, the **taped-over smoke alarm**, the
**three-legged chair**, the **ring pull** from a can.

There are no other people in this video. No exes, no friends, no neighbours.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The phone's bank notification in shot 1 and the restaurant flyer are
composited in the edit.** Generate the phone as a lit blank screen and the
flyer as a blank card under a magnet; the model cannot render legible UI or
print, and neither needs to be readable — the flyer only has to look like a
restaurant.

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

For this song specifically: there is one set, so build the kitchen once as
a plate and light it three ways (fridge only, stove lamp and fairy lights,
everything on). Both leads need IP-Adapter or a LoRA each. **OpenPose on
every slow-dance shot** — two bodies in frame in contact is where the model
fuses limbs. Keep the dance to a sway, a turn, one dip and one spin; the
model handles a single slow movement per clip far better than a sequence.
The sock slide in shot 5 and the dip in shot 40 are the only fast
movements. The 9:16 recomposition is for the chorus and the count-of-three.

## 4. Scene per lyric line

### Intro — rent's out, blinds down

1. *"Rent came out on Friday, so we're staying in"* — a tiny kitchen at night lit only by the open fridge, a phone face-up on the counter with a lit blank screen (bank notification composited), Mahima's hand turning it face-down, close-up, static.
2. *"One bottle of the cheap stuff, two mismatched cups"* — a screw-cap bottle of red being opened and poured into a chipped mug and a jam jar, extreme close-up on the pour, warm fridge light.
3. *"You pulled the blinds down on the world outside"* — Kai at the window pulling the blinds down, the blue street light outside cut off slat by slat, medium from behind.
4. *"Now it's just the fridge light and the two of us"* — the fridge door swinging shut and the room dropping to the single string of fairy lights along the cabinets, both of them in it, wide, static.

### Verse 1 — socks on the tile

5. *"Your socks keep sliding on the tile, you almost fall"* — low angle on black and white checkered tile, Kai's odd socks skidding and his hand grabbing the counter edge, handheld.
6. *"I'm laughing so hard I can barely stand"* — Mahima doubled over laughing with her back against the fridge, the jam jar held up out of harm's way, medium close-up, warm.
7. *"The oven timer's ticking like a metronome"* — extreme close-up of a wind-up oven timer on the counter, the dial creeping, the tick audible, stove lamp.
8. *"So you set the bottle down and say, come here"* — Kai setting the bottle on the counter and holding out his hand, the frame on the hand and then up to his face, slow push-in.
9. *"There's string lights on the cabinet we never took down"* — a slow pan along the cabinets following the fairy lights, one strip of tape peeling, warm bokeh.
10. *"There's steam rising off a pot we both forgot"* — a pot boiling over on the stove, steam curling up through the fairy lights, close-up, haze.
11. *"We can't afford the place with the candles and the view"* — a restaurant flyer under a magnet on the fridge door (composited), Mahima's eyes on it for one beat, then moving off it to him, close-up.
12. *"But look at what we've got, look at what we've got"* — Mahima taking his hand and pulling him one step into the middle of the tile, a wide of the whole kitchen with the two of them filling it.

### Pre-chorus 1 — the frame, the count

13. *"Put your hand right here, your chin on my shoulder"* — Mahima placing Kai's hand on her waist and guiding his chin onto her shoulder like a dance teacher, close two-shot.
14. *"I'll count us in, one, two, three, here we go"* — extreme close-up of her mouth counting, then a cut to their socked feet stepping together on the last word.
15. *"The whole world's out there and the rent is still due"* — the closed blinds with the faint city glow behind them, the muffled sound of traffic, then rack focus back to the two of them turning slowly.
16. *"But in here it's slow, in here it's slow"* — the two of them in the first slow turn, her eyes closed, the fairy lights soft behind her, medium, slow circling.

### Chorus 1 — the slow dance

17. *"Turn the radio low, we don't need a floor"* — Kai reaching over to the windowsill radio and turning the glowing dial down without letting go of her waist, close-up on the hand and the dial.
18. *"Slow dance in the kitchen, that's what the kitchen's for"* — the full slow dance in a small circle between the fridge and the sink, wide, the camera circling slowly the opposite way.
19. *"Socks on the tile and the toast gone black"* — the toaster popping two black slices behind them, a small puff of smoke, neither of them looking, medium.
20. *"Spinning by the sink, never going back"* — Kai spinning Mahima once under his arm beside the sink, the tap dripping, her cardigan flaring, slow motion.
21. *"We don't need a ballroom, don't need a band"* — a wide of the whole six-by-eight kitchen with the two of them in the middle of it, the string lights the only decoration, static.
22. *"Just the hum of the fridge and your hand in my hand"* — extreme close-up of their held hands, his thumb moving over her knuckles, the fridge humming.
23. *"Turn the radio low, lock the front door"* — Mahima reaching out with one socked foot to push the apartment door shut, the latch clicking, the hallway light cut off, low angle.
24. *"Slow dance in the kitchen, that's what the kitchen's for"* — the two of them swaying, foreheads nearly touching, both singing the line at each other, close two-shot, warm.

### Verse 2 — Kai, the night out he couldn't afford

25. *"I know I promised you a night out somewhere nice"* — Kai at the counter holding the restaurant flyer (composited), a little embarrassed, stove lamp on his face, medium close-up.
26. *"White tablecloths and a waiter we could tip"* — the flyer close-up, a candle and a skyline on it, then his hand putting it back under the magnet.
27. *"But the toast went black and you laughed till you cried"* — the burnt toast on a plate, then Mahima laughing so hard she slides down the cabinet to sit on the floor, wiping her eyes, handheld.
28. *"Then you turned the music up and said, let's skip it"* — Mahima on the floor reaching up to turn the radio dial up, grinning at him, low angle.
29. *"The smoke alarm's got tape across its mouth"* — a tilt up to a smoke alarm on the ceiling with a strip of masking tape across it, the toast smoke drifting past, static.
30. *"The chair beside the window only stands on three"* — a wooden chair propped against the wall under the window, one leg missing, the fairy lights reflected in the glass, close-up.
31. *"I've got eleven dollars and a feeling in my chest"* — Kai's wallet open on the counter, two notes, then his hand resting flat on his own chest without noticing, medium close-up.
32. *"And the feeling's worth more than anything to me"* — Kai looking across the kitchen at Mahima on the floor, plain and unguarded, slow push-in, warm.

### Pre-chorus 2 — he leads this time

33. *"Put your hand right here, your chin on my shoulder"* — Kai pulling her up off the floor and placing her hand on his shoulder, her chin against his neck, the frame reversed from shot 13, close two-shot.
34. *"I'll count us in, one, two, three, here we go"* — extreme close-up of Kai's mouth counting, Mahima's surprised smile at being led, then the feet stepping.
35. *"The whole world's out there and the rent is still due"* — the phone face-down on the counter in the foreground, the two of them dancing soft in the background, rack focus.
36. *"But in here it's slow, in here it's slow"* — the slow turn again, this time her leading with her eyes open and on him, medium, the fairy lights a touch brighter.

### Chorus 2 — braver

37. *"Turn the radio low, we don't need a floor"* — reuse shot 17, tighter, her hand on top of his on the dial.
38. *"Slow dance in the kitchen, that's what the kitchen's for"* — overhead shot straight down on the checkered tile, the two of them turning in a slow circle, socks on the squares, the camera slowly rotating.
39. *"Socks on the tile and the toast gone black"* — Mahima scraping the black off a slice of toast over the sink with a knife while still swaying against him, close-up, playful.
40. *"Spinning by the sink, never going back"* — Kai dipping her beside the oven, the string lights across her upside-down laughing face, slow motion, low angle.
41. *"We don't need a ballroom, don't need a band"* — the spin knocking a wooden spoon off the counter, neither of them stopping, the spoon bouncing on the tile, medium.
42. *"Just the hum of the fridge and your hand in my hand"* — reuse shot 22, her hand now on top, her thumb moving.
43. *"Turn the radio low, lock the front door"* — the closed door in the background, the two of them in the foreground singing the hook at each other, wide.
44. *"Slow dance in the kitchen, that's what the kitchen's for"* — a slow circle around the two of them at chest height, both faces, the steam and the fairy lights, the warmest frame so far.

### Instrumental — they just dance

45. Overhead, straight down: socked feet on the checkered tile turning in a slow circle, the pattern of the squares, the camera slowly rotating with them, dim.
46. Mahima's forehead on Kai's chest, her eyes closed, his hand on the small of her back, extreme close-up, stove lamp only.
47. The oven timer in extreme close-up, the dial almost at zero, the tick, then the radio dial glowing amber, then the pot lid rattling.
48. A wide of the dim kitchen, the two of them barely moving in the middle, the fairy lights and the stove lamp the only light, locked-off, long.
49. Drop to near-quiet: an extreme close-up of her lips pressing together, holding something in, the cut into the bridge.

### Bridge — the sentence, the count of three

50. *"I've been holding a sentence behind my teeth"* — the dancing stopped but neither letting go, Mahima looking at his collar instead of his face, close-up, single stove lamp, hard shadows.
51. *"Since you burned the toast in the middle of the week"* — the plate of scraped toast on the counter behind her, her eyes flicking to it and back, rack focus.
52. *"I've been practising in the mirror down the hall"* — memory, cool morning light: Kai alone in a hallway mirror mouthing three words to himself, stopping, running a hand over his face, over-the-shoulder into the mirror.
53. *"Every morning, every evening, never said it at all"* — the memory again, a different morning, the same mirror, the same three words not said, then a hard cut back to the kitchen and his face now.
54. *"So let's say it on the count, let's say it on three"* — Mahima saying it to his collar, then lifting her eyes, Kai nodding once, close two-shot.
55. *"One, two, and you said it before me"* — extreme close-up of her mouth on one, two, then a cut to his mouth already moving on two, then her face hearing it.
56. *"I love you, I love you, out loud by the stove"* — both of them saying it over each other and laughing, foreheads together, beside the stove, medium close-up, handheld.
57. *"And the timer went off like it already knows"* — the oven timer on the counter going off with a ding, extreme close-up, then Kai bumping the light switch with his elbow and the fairy lights coming back on across the kitchen, wide.

### Final chorus — flour on his shirt, a ring pull for a ring

58. *"Turn the radio low, we don't need a floor"* — Mahima turning the radio up instead of down, a grin, Kai laughing, close-up on the dial and her face.
59. *"Slow dance in the kitchen, that's what the kitchen's for"* — the dance again, bigger, every light in the kitchen on, the pot finally turned off, wide circling.
60. *"Flour on your shirt and a ring pull for a ring"* — a white flour handprint on the chest of Kai's navy t-shirt, then his fingers twisting the ring pull off a can, close-up.
61. *"Say it one more time, I'll say it back and sing"* — Kai sliding the ring pull onto her finger, half a joke, her holding the hand up to the fairy lights to look at it, extreme close-up, warm.
62. *"We don't need a ballroom, don't need a band"* — the two of them singing the hook at each other, the flyer on the fridge behind them out of focus and ignored, medium.
63. *"Just the hum of the fridge and your hand in my hand"* — their held hands with the ring pull on her finger catching the light, extreme close-up.
64. *"Turn the radio low, lock the front door"* — a wide of the whole lit kitchen from the closed door, the two of them small in the middle of it, dancing, static.
65. *"Slow dance in the kitchen, that's what the kitchen's for"* — the happiest frame: both laughing mid-turn, her hair across her face, his hand in it, slow motion, the string lights streaking.

### Post-chorus — swaying

66. *"That's what the kitchen's for"* — no steps now, just a slow sway, the camera drifting in from the wide, warm.
67. *"Two left feet on a checkered floor"* — overhead: their feet on the tile, out of step and not caring, one of her socks half off, the fairy lights reflected in the tile.
68. *"That's what the kitchen's for"* — her chin on his shoulder, eyes closed, his eyes open on the string lights, close two-shot.
69. *"Every night I'll ask you for one more"* — her mouthing one more against his neck, him nodding, extreme close-up, the fairy lights dimming a touch.

### Outro — the bottle's empty

70. *"The bottle's empty and the song's nearly gone"* — the bottle upside down in the sink, a last drop, the radio dial glowing behind it, close-up, stove lamp only.
71. *"The string lights flicker but you keep on holding on"* — one bulb on the fairy-light string flickering, then her hand still on his shoulder in the soft light, close-up.
72. *"One day we'll have the candles and the view"* — the restaurant flyer on the fridge door, and Mahima's eyes not going to it, staying on him, medium.
73. *"But I'll take the kitchen if the kitchen comes with you"* — final shot: the two of them still swaying in the dim kitchen, the ring pull on her finger, the timer on the counter, the fridge door drifting open and its light spilling across the tile, wide and locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "that's what the kitchen's for",
the count of three in each pre-chorus, the instrumental, the count of three
in the bridge, the timer ding, the ring pull, and the final "you." At 88 BPM
a bar is 2.73 s; choruses cut every one or two bars, verses hold longer.

**Kitchen slow-dance challenge.** The hook is caption-ready. Post the
vertical cut of chorus 1 (shots 17–24) with *"slow dance in the kitchen,
that's what the kitchen's for"* on screen and invite couples to post their
own socks-on-tile slow dance; turning the radio down without letting go
(shot 17) is the opening move. The count of three where he says it before
she gets to three (shots 54–57) is the second shareable frame, and the ring
pull (shot 61) is the third.

## 6. Quality-control checklist

- One look each for the whole video; Kai's flour handprint appears from shot 60 on and never before
- The odd socks are consistent: Mahima one striped and one plain, Kai one black and one white
- OpenPose on every two-body dance shot; no fused arms, no extra hands at the waist
- The flyer and the phone screen are composited; no model-generated print or UI
- Light is practical only: fridge, stove lamp, fairy lights; the hallway memory (shots 52–53) is the only cool frame
- Continuity of the night: pot boiling in the verses, off by the final chorus; timer ticking until shot 57, then silent; bottle full at shot 2, empty at shot 70
- Nobody else ever appears; no window shows anything but blinds
- The last shot is locked-off and holds until the audio fades
