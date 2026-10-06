# Wan 2.2 Shot List — "Fireworks in February"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
112 BPM a bar is 2.14 s, so most shots run 2–4 s and the choruses cut on the
bar with the black-to-gold flashes landing on the downbeat.

## 1. Visual style

One night, one empty retail parking lot, two people and a security guard.
**The entire video has two light states: black and gold.** Before the first
firework there is nothing but a single working lot light, headlights and
breath. After it, everything in frame — carts, painted lines, puddles,
faces — is lit by fireworks and goes dark again between shells. Cold is a
texture, not a grade: visible breath, thin shoes on frozen asphalt, smoke
sitting low. The three bridge inserts are the only clean, bright, lifeless
images in the film and they are deliberately ugly.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium orange street, one cold interior lamp | Static wide, slow |
| Verse 1 | Headlights and one lot light, everything else black | Passenger profile, handheld |
| Pre-choruses | One point source on the ground, smoke in the beam | Feet-to-face tilt |
| Choruses | Black to gold on the downbeat, gold on wet asphalt | Wide low, one under-shot, drone |
| Verse 2 | Flashlight beam, then firework gold across his face | Close, static |
| Instrumental | Fireworks only, lot light constant | Long lens, tall frames |
| Bridge | Clean lifeless inserts against the warm dark lot | Locked-off, then curb-level |
| Final chorus | Full gold, silhouettes against the last shell | Drone rise, held silhouette |
| Post-chorus | Lot light and headlights only, sky black again | Locked-off wide |
| Outro | Dash glow, heater warmth, blue-black outside | Interior close, rear window |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose under a knitted beanie, no makeup, wearing an oversized dark green wool coat over a sweater and thin canvas shoes, breath visible, curious amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (final chorus flash-forward, a later February)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose under a knitted beanie, no makeup, wearing the same oversized dark green wool coat, carrying a builder's bucket of sand, calm knowing expression, realistic cinematic photography, consistent identity

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a navy work jacket over a hooded sweatshirt and jeans, cold-reddened hands with no gloves, delighted nervous expression, realistic cinematic photography, consistent identity

**The security guard** — a man in his fifties in a padded uniform jacket, face allowed and warm; the third character in the video and never a threat.
> a man in his fifties in a padded navy security uniform jacket, tired kind face, arms folded

There are no exes and no rivals in this video. Nobody else appears at all —
the town is empty on purpose.

Objects: the **two flat fireworks boxes**, the **lighter**, the **builder's
bucket of sand**, the **crumpled receipt**, the **sparkler**, the **shared
coat**, the **corral of shopping carts**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All store signage, the receipt total, the phone's paused safety video, the
calendar date and the shop window in the bridge are composited in the
edit.** The model cannot render legible text, and the receipt and the
calendar are two of the three most important close-ups in the film.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and Kai with IP-Adapter or a character LoRA each; the guard needs
only a consistent reference image since he is always mid-shot or wider.
Depth for the big lot wides so the geometry of the painted lines holds.
OpenPose for the spin in chorus one and for the two of them getting onto the
car hood. 16:9 first; 9:16 recomposition for the black-to-gold hook cut.

**Fireworks are the one thing not to generate.** Shoot or license real
pyrotechnic plates and composite them, then let Wan animate the people under
a matching brightness ramp. Generated fireworks read as smeared light and
will sink the whole video. The same applies to the sparkler: real plate,
composited, with the model animating only her arm and the smoke.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; the instrumental long-lens shots run to 8 s.

## 4. Scene per lyric line

### Intro — a dead month

1. *"Second week of February and the whole town's asleep"* — static wide of a wet main street with every window dark, one traffic light cycling to nobody, sodium orange, slow.
2. *"Nothing on the calendar and nothing left to keep"* — a kitchen wall calendar with no marks on it at all (composited), one cold overhead lamp, static close.
3. *"You said, wear the big coat, and you wouldn't tell me why"* — Mahima pulling the green wool coat off a hook by the door, reading a phone she doesn't answer, medium.
4. *"Half past ten on a Tuesday in the deadest month alive"* — her stepping out of the front door, breath white the instant she's outside, headlights waiting at the curb, static wide.

### Verse 1 — the drive and the trunk

5. *"We drove past the strip mall and the shuttered garden store"* — passenger-side profile through the windshield, a dark strip mall sliding past, reflections crossing her face.
6. *"Parked between the carts where the lot light doesn't go anymore"* — high wide of a huge empty lot, one car alone beside a corral of shopping carts, one broken lot light overhead, static.
7. *"I said, is this a kidnapping, you said, more or less"* — interior two-shot, engine off, both still belted in, her turned toward him, dash glow only.
8. *"And your breath came out white and you laughed at my face"* — Kai laughing outside the car with his breath fully white in the cold, close-up, headlights side-on.
9. *"You popped the trunk open and I stood there in the wind"* — the trunk lifting from her point of view, her coat moving in the wind, low handheld.
10. *"Two flat boxes, a lighter, and a bucket of sand"* — three inserts on the beat: two flat fireworks boxes, a lighter in a cold-red hand, a builder's bucket of sand.
11. *"You said, on a bus in November I had mentioned it once"* — a two-second warm flash: the two of them on a bus at night months earlier, her mid-sentence, him listening, out-of-focus city behind.
12. *"That I'd never seen one close, and you'd been holding that since"* — hard cut back to the lot, her face, the realisation arriving, close-up, one lot light.

### Pre-chorus 1 — before the first one

13. *"And the cold got into my shoes and I didn't care"* — her feet in thin canvas shoes on frozen asphalt, then a slow tilt beginning upward.
14. *"And the smoke came down slow through the frozen air"* — the tilt continuing to her face through low drifting smoke lit by the lot light.
15. *"Something in my chest went off before the first one flew"* — the first fuse catching, sparking on the ground, extreme close-up.
16. *"I have never been the kind of girl this happens to"* — Kai walking backwards fast toward her, both bracing, wide low, the frame still dark.

### Chorus 1 — the sky

17. *"Fireworks in February, just because you could"* — hard black-to-gold on the downbeat: the whole lot lit, both of them tiny under an enormous sky, wide low from the far side.
18. *"No birthday, no reason, no occasion, nothing owed"* — from directly beneath, gold falling toward the lens, the two of them at the bottom of a very tall frame.
19. *"You lit up an empty parking lot like a town square"* — the lot in full gold light — carts, painted lines, puddles all readable — slow drift, wide.
20. *"And I finally know what people mean by care"* — Mahima's face turned up, gold flashing across it, going dark and gold again on the beat, close-up.
21. *"Fireworks in February and the sky went gold"* — her spinning once with her arms out, coat flaring, medium, real time.
22. *"Twenty-eight days of nothing and you made one hold"* — Kai watching her instead of the sky, hands in pockets, medium, gold on one side of his face.
23. *"Anybody can do December, baby, anyone would"* — a whole shell reflected end to end in a puddle between two painted lines, macro, static.
24. *"You did fireworks in February, just because you could"* — both of them in one wide, the lot going black between shells and gold again on the last word.

### Verse 2 — the receipt, the guard, his face

25. *"There was a receipt in the glove box for a hundred and ten"* — the glove box open, a crumpled receipt on top of the manual (total composited), interior light, static close.
26. *"More than your insurance will forgive you again"* — the same glove box closing, her hand pulling back, a small guilty smile off frame edge.
27. *"You had watched a whole video on where to stand back"* — his phone face-up on the dash with a paused safety video (composited), the screen the only light in the frame.
28. *"And you made me hold the sparkler while you lit the first pack"* — a sparkler in her fist held out at full arm's length, her face leaning away from it, close.
29. *"The security guard came out and then he just stayed"* — a service door opening across the lot, the guard with a flashlight, the beam swinging over and then dropping, wide.
30. *"Arms folded on the curb like a kid at a parade"* — the guard sitting down on the curb, arms folded, looking up, medium, gold across his face.
31. *"And I didn't look up once at the sky going white"* — the sky going white out of focus in the background while her eyes stay level, close-up on her, shallow.
32. *"I was watching your face turning gold in the light"* — the reverse: Kai's face in full firework gold, her out of focus in the foreground, held two beats.

### Pre-chorus 2 — later and colder

33. *"And the cold got into my shoes and I didn't care"* — reuse shot 13's framing exactly, more smoke, wet asphalt now.
34. *"And the smoke came down slow through the frozen air"* — the same tilt to her face, the lot-light beams now fully visible through the smoke.
35. *"Something in my chest went off before the first one flew"* — the guard on the curb now holding a sparkler too, not making eye contact with anyone, medium.
36. *"I have never been the kind of girl this happens to"* — Kai crouched over the second box with the lighter, the flame the only light in frame, close.

### Chorus 2 — bigger

37. *"Fireworks in February, just because you could"* — the two of them getting up onto the car hood, one coat pulled over both shoulders, medium wide.
38. *"No birthday, no reason, no occasion, nothing owed"* — ninety-six frames slow motion of both on the hood looking up, gold moving across them.
39. *"You lit up an empty parking lot like a town square"* — the whole display in the windshield reflection with their faces behind the glass, static.
40. *"And I finally know what people mean by care"* — reuse shot 20, tighter, her eyes wet from cold rather than crying.
41. *"Fireworks in February and the sky went gold"* — drone hovering just above the car, the two on the hood, the lot geometry all around them.
42. *"Twenty-eight days of nothing and you made one hold"* — a long lens on one shell going up alone and opening, the sky filling.
43. *"Anybody can do December, baby, anyone would"* — the empty shopping carts lit gold and then going dark, static, no people.
44. *"You did fireworks in February, just because you could"* — both silhouetted on the hood against the last gold of the section, held to the drop.

### Instrumental — the display gets the screen

45. Long lens, a single shell rising, the fuse trail crossing the whole frame, then opening at the top, eight seconds.
46. The guard walking back toward the service door, stopping, and turning around to watch one more, wide.
47. Her sparkler burning down to the glove, sparks landing on the wool and going out, macro.
48. The two of them very small at the bottom of a very tall frame, the sky doing all the work above them.
49. The lot from above with only the lot light on between shells, smoke drifting across the painted lines, drone, held.

### Bridge — everybody else's version

50. *"People wait for a reason, they save it for a date"* — clean cold insert: a wall calendar with one date circled hard in red (composited), flat lit, lifeless.
51. *"Put a circle in red on a square on a page"* — the same calendar, a hand pinning it back to the wall, no faces, static.
52. *"Wrap it in ribbon and they leave it by the tree"* — a wrapped box under a dry, dropping tree in an empty room, clean bright light, static.
53. *"And forget halfway through what the whole thing should mean"* — a jewellery case opening in a lit shop window with nobody in front of it, reflection of an empty street.
54. *"So don't buy me diamonds and don't book me a flight"* — hard cut back to the lot: the three of them sitting on the curb, the guard on the end, all quiet, last smoke drifting, wide.
55. *"Just tell me to get in the car on a nothing kind of night"* — Mahima looking sideways at Kai on the curb, saying it to him and not to camera, close two-shot, warm dark.

### Final chorus — the widest, and the flash-forward

56. *"Fireworks in February, just because you could"* — the biggest volley of the night, the lot brighter than it has been, wide low.
57. *"No birthday, no reason, no occasion, nothing owed"* — drone rising from the lot until the car is a dot and the display is level with the lens.
58. *"You lit up an empty parking lot like a town square"* — the top of the drone move: the lot, the dead strip mall, the empty town, one bright point in it.
59. *"And now every February I know what's coming there"* — two-second flash-forward: the same lot in a later February, Mahima arriving first, carrying the bucket of sand.
60. *"Fireworks in February and the sky went gold"* — back to the night, her face gold, laughing with her head back, close.
61. *"Twenty-eight days of nothing and you made one hold"* — Kai lighting the last one and running, seen from behind, gold catching the back of his jacket.
62. *"I'd trade every New Year's for the way you stood"* — the two of them standing shoulder to shoulder, no coat shared now, both just watching, medium.
63. *"Doing fireworks in February, just because you could"* — held silhouette: both of them black against the last shell, no movement, two full seconds.

### Post-chorus — the lot empties

64. *"February, February"* — locked-off wide of the lot with heavy smoke drifting across it, sky black again, only the lot light.
65. *"Nothing on the calendar and everything in the sky"* — the two of them walking back to the car through the smoke, small in the frame, same locked-off wide.
66. *"February, February"* — the guard raising one hand without turning around as he goes back through the service door.
67. *"Twenty-eight days and you picked the coldest night"* — the empty curb where the three of them sat, one spent sparkler on it, static close.

### Outro — the drive home

68. *"Ash on the windshield and the heater coming on"* — ash settling on the windshield from inside the car, the wipers clearing it in one pass, interior.
69. *"Your hand on the gearshift and the radio off"* — his hand on the gearshift, the radio dark, dash glow, close.
70. *"Nine more Februaries and I still know the sound"* — her face in the passenger seat, heater warmth on it, looking straight ahead, close.
71. *"Of the first one going up over an empty lot"* — final shot: the empty lot through the rear window, one working light, smoke still in the air, holding as the car pulls away and the frame darkens. No text.

## 5. Edit and the challenge

Markers at: the first breath outside, the trunk opening, the first fuse, each
black-to-gold downbeat, the guard sitting down, the bridge inserts, the
flash-forward, and the last silhouette. At 112 BPM a bar is 2.14 s; every
gold flash in the choruses lands on a downbeat and every black frame between
shells lands on beat three.

**The black-to-gold challenge.** Shot 16 into shot 17 — a completely dark
frame cutting to a whole parking lot in gold on the word *"fireworks"* — is
the cut to post vertically, captioned *"anybody can do December."* Invite
people to post the smallest thing somebody did for them for no reason at
all, cut on the same downbeat. The second shareable frame is shot 32, his
face going gold while she isn't looking at the sky.

## 6. Quality-control checklist

- One look for each lead across the whole night; the flash-forward is the same coat, a different mood, and must not read as a new character
- Every firework and every sparkler is a real composited plate; nothing pyrotechnic is generated
- Visible breath in every exterior shot before the fireworks start, and in most after
- Two light states only: black and gold. No shot invents a third source except the lot light, the headlights and the flashlight
- The bridge inserts (50–53) are the only clean bright images in the film and contain no faces
- The guard is warm and never a threat; he ends the video with a raised hand, not a confrontation
- Receipt, calendar, safety video and shop window all composited; no model-generated text anywhere
- The last shot is locked off through the rear window and holds until the audio fades
