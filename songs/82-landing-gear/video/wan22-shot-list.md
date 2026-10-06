# Wan 2.2 Shot List — "Landing Gear"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
108 BPM a bar is 2.22 s, so verse shots run one to two bars and the chorus
cuts every bar.

## 1. Visual style

A single continuous ninety minutes, shot like the last reel of a film. Three
light worlds, and the film gets brighter in exactly one direction:
**altitude** is cabin blue with one hard overhead reading light; **the
terminal** is flat unkind fluorescent; **arrivals** is blown-out warm daylight
through a wall of glass. The flashbacks that live inside the choruses are cold
and lamp-lit, always narrower than the shot they cut out of.

Two rules: nothing in the present is ever darker than the shot before it after
the wheels touch, and the male lead's face is not seen anywhere in the video
until shot 58.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cabin blue, one overhead spot | Slow dolly, static close |
| Verse 1 | Cabin blue, single reading light | Static, tight inserts |
| Pre-chorus 1 | Window-lit, cabin lights down | Handheld, then exterior locked-off |
| Choruses | Cold lamp-lit flashbacks against hard sodium and white | Fast cuts, then wide |
| Verse 2 | Flat airport fluorescent | Handheld, walking |
| Pre-chorus 2 | Fluorescent warming toward daylight | Accelerating handheld |
| Instrumental | Cold lamps, then the brightest cut in the film | Locked-off, then running |
| Bridge | Daylight from above, blurred crowd | One locked-off wide |
| Final chorus | Blown-out warm daylight, flares | Tracking, held long |
| Post-chorus | Softened daylight | High wide, pulling back |
| Outro | Cabin blue, then clean white | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (in the air)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slept-on, no makeup, wearing an oversized grey sweatshirt over a white t-shirt and black joggers, a thin blanket across her lap, tired wide-awake expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the terminal and the run)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pushed back off her face, no makeup, wearing the same grey sweatshirt with the sleeves shoved up and a small canvas duffel bag on one shoulder, urgent focused expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the person waiting) — held back deliberately. Until shot 58 he exists only as a phone screen glow, a coat on a chair, a voice. His first real frame is the gap in the crowd.
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a dark green jacket over a plain t-shirt and jeans, standing still, overwhelmed relieved expression, realistic cinematic photography, consistent identity

Everyone else is airport population and stays that way: **the sleeping boy and
his mother** two rows up, **the man with unplugged headphones**, **the woman
with a placard**, **the driver on his phone**, **the couple who collide just
ahead of her**. Keep them in profile, in motion, or slightly out of focus.
None of them needs a locked identity, and none of them is anyone from her
past — there are no exes in this video.

Objects that repeat: the **receipt** with the speech on it (written, read,
hidden in a shoe, never read again), the **canvas duffel** (on her shoulder,
then dropped, then carried by him), the **two wall clocks** set to different
cities, the **seatback map**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, signage, boarding passes, the seatback map, the calendar, the
weather app, the arrivals board and the placard are composited in the edit.**
Generate every screen as a blank lit panel and every sign as a blank
backlit shape. An airport is made of text and the model cannot render a
single word of it legibly; this is the highest-risk video in the batch for
model-generated lettering, so check every frame.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA; build Kai's
reference set but do not use it before shot 58. Keyframes first; OpenPose is
essential for the run through arrivals and the collision, which is the one
shot in the video that will fall apart without a pose reference. Depth for the
cabin interiors and the long corridor. 16:9 first; 9:16 recomposition for the
gear-drop and the run, which are the two vertical cuts.

Animate in short bursts and keep the camera doing the work: reading lights
coming up in sequence, a tray table clicking, a wheel swinging down, a bag
strap slipping off a shoulder. Crowd motion behind a still subject is far
easier as a slow-shutter plate with the subject shot separately and composited
than as a single generation.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–5 s.

## 4. Scene per lyric line

### Intro — altitude

1. *"Cabin lights came up on somewhere dark,"* — the reading lights coming up in sequence down a sleeping wide-body cabin, slow dolly along the ceiling line, cabin blue.
2. *"Four hours left on a little plastic map."* — a seatback screen filling frame, blank and lit (flight map composited: a tiny plane over an ocean), her fingertip resting on the bezel.
3. *"I have been counting this down since a January airport,"* — Mahima's face lit only by the screen, awake among sleeping rows, close-up, static.
4. *"And the whole year folded into one gray seat."* — pull back to a wide of the dim cabin, one overhead spot on her and nothing else lit, locked-off.

### Verse 1 — one row, in detail

5. *"I know this row by heart, I have flown it in my head,"* — the wing outside the window against total black, one strobe pulsing, static.
6. *"Twenty-six A, the wing, the same square of sky."* — over her shoulder out of the window, her reflection ghosted on the glass over the dark, close.
7. *"There's a kid asleep on his mother in the aisle,"* — two rows up, a small boy asleep sideways across his mother, her arm around him, medium, soft focus.
8. *"And a man beside me watching something with the sound off."* — the seat beside her, a blank flickering screen (content composited), his headphones unplugged and lying in his lap, insert.
9. *"I wrote you a speech on the back of a receipt,"* — her hands unfolding a curled receipt covered in tiny handwriting (composited), extreme close-up.
10. *"Then I read it once and I put it in my shoe."* — her bending forward under the seat and tucking the receipt into the side of her sneaker, low insert.
11. *"Because everything I practiced is going to leave my mouth"* — her sitting back up, mouthing something silently, then giving up on it, close-up.
12. *"The second that those doors go the other way."* — a two-second cold flash-forward: blank frosted arrivals doors opening on nobody, then hard cut back to the cabin.

### Pre-chorus 1 — descent

13. *"The seatbelt light, the little chime, the tray table up,"* — three cuts on the beat: a blank lit overhead panel (icon composited), a tray table clicking up, her palm flat on the cabin wall.
14. *"The city coming up like a spilled box of light."* — out of the window: a city rising through cloud, scattered sodium grids, the wing black across the bottom of the frame.
15. *"Something in the floor lets go and starts to lower,"* — exterior, locked-off under the fuselage: the gear doors opening and the wheels swinging down and locking, night, lit by the aircraft's own lights.
16. *"And my whole body knows the sound before I do."* — back inside, her eyes closing for exactly one beat on the sound, extreme close-up, cabin lights now down.

### Chorus 1 — eleven months in eight lines

17. *"Landing gear down, my heart's coming home,"* — the runway lights streaming past under the wing, fast, hard sodium streaks, exterior.
18. *"Eleven months of nothing but a voice on a phone."* — cold flashback: a phone propped against a pillow at three in the morning, a blank lit screen, an empty half of a bed.
19. *"Six thousand miles folding into one hallway,"* — cold flashback: a coat on the back of a chair in an empty apartment, unmoved for months, static.
20. *"And you at the end of it and nothing in the way."* — cold flashback: a suitcase living permanently open on a bedroom floor, half-packed.
21. *"I have been up here so long I forgot the ground,"* — cold flashback: a wall calendar with one square circled (composited), her hand crossing off a day.
22. *"Now the wheels find the runway and the year comes down."* — exterior: the wheels touching, smoke off the tyres, slow motion, the widest shot yet.
23. *"Pull the window shade up, let the morning come on,"* — her hand pushing the window shade up and the frame blowing out to white, close-up.
24. *"Landing gear down, my heart's coming home."* — her face in the new white light, eyes open, the whole cabin behind her lit for the first time.

### Verse 2 — the landing and the walk

25. *"We touched and the whole cabin clapped like we had done it,"* — the cabin applauding, a few people laughing, handheld from the aisle.
26. *"Then we sat on the tarmac for another twenty minutes."* — a wide exterior of the aircraft parked in the middle of nowhere, engines spooling down, nothing happening, locked-off.
27. *"The aisle stood up too early like the aisle always does,"* — the whole aisle standing shoulder to shoulder going nowhere, low angle down the length of it.
28. *"And for once I was standing with them, bag against my chest."* — Mahima in the crush, duffel hugged to her chest, half a smile at herself, close-up.
29. *"A booth, a nod, a corridor with nothing on the walls,"* — three cuts: a passport booth (all screens and stamps composited), an officer's nod, a completely bare corridor.
30. *"A moving floor that I refuse to stand still on."* — a moving walkway from behind, her overtaking every stationary person on it, tracking.
31. *"There's a woman with a placard and a driver on his phone,"* — a woman holding a blank placard (name composited) and a driver scrolling beside her, medium, flat fluorescent.
32. *"And the frosted doors keep opening for other people."* — the frosted arrivals doors from inside, opening and closing on strangers, her not there yet, static.

### Pre-chorus 2 — the last thirty seconds

33. *"The strap in my fist, the escalator taking its time,"* — extreme close-up of her fist white on the bag strap, then an escalator from a low angle, her feet shifting.
34. *"A sign says arrivals like it is a normal word."* — a blank backlit overhead sign (word composited) from below, her walking under it, wide.
35. *"Somebody hugs somebody just ahead of me,"* — a stranger reunion just ahead: two people colliding, out of focus, in the background of her frame.
36. *"And I am running before I decide to run."* — her face changing, then a hard cut to her legs, then she is gone from the frame, handheld.

### Chorus 2 — the run

37. *"Landing gear down, my heart's coming home,"* — tracking with her at full speed down the concourse, the duffel banging her hip, everything else blurring.
38. *"Eleven months of nothing but a voice on a phone."* — cold flashback, one second only: the propped phone from shot 18, now dark.
39. *"Six thousand miles folding into one hallway,"* — a long lens straight down the concourse, the far end compressed and shimmering, her small in it.
40. *"And you at the end of it and nothing in the way."* — the crowd at the barrier ahead, faces scanning, none of them the right one, her point of view.
41. *"I have been up here so long I forgot the ground,"* — slow-motion insert: the bag strap slipping down her shoulder, her catching it without looking.
42. *"Now the wheels find the runway and the year comes down."* — slow-motion insert: one shoe striking tile, the sole flexing, spray of light off the floor polish.
43. *"Pull the window shade up, let the morning come on,"* — the big daylight windows of the arrivals hall coming into frame, flare across the lens, her silhouetted.
44. *"Landing gear down, my heart's coming home."* — her stopping dead, scanning, chest heaving, wide, the crowd moving around her.

### Instrumental — the year, told properly

45. Two clocks side by side on one wall set to different cities, locked-off, cold light.
46. A video call frozen mid-buffer on a laptop, a blank lit screen, a room dark behind it.
47. Her asleep on a couch with a phone still lit on her chest, overhead, one lamp.
48. A small birthday cake on a table with a laptop propped in front of it and one chair pulled up, static, wide.
49. Filtered drop to near-silence on a single held frame of the frosted doors, then a tom rebuild over her running again — the brightest cut in the film.

### Bridge — she stops

50. *"We did it well, we did the calls, we did the time,"* — a locked-off wide: Mahima completely still in the dead centre of a moving hall, bag at her feet, everyone else motion-blurred.
51. *"We split the difference on the hours and the sleep."* — hold the same frame, tighter, her breathing settling.
52. *"I learned your weather and you learned mine,"* — insert: a weather app for a city that is not hers on a blank lit phone (composited), then the phone going into her pocket.
53. *"I fell asleep to your morning more nights than I can count."* — the two clocks again, and a hand lifting one of them off the wall, cold flashback, macro.
54. *"But nobody ever hugged a screen and got it back,"* — her face in the still wide, absolutely level, no self-pity, close-up.
55. *"And I am done being good at missing you."* — she picks the bag back up and walks forward out of frame, the crowd blur resolving behind her.

### Final chorus — the arrival

56. *"Landing gear down, my heart's coming home,"* — the crowd at the barrier, and a gap opening in it, her point of view, blown-out daylight behind.
57. *"No more goodnight at the wrong end of a phone."* — one second of the dark propped phone, then gone for good.
58. *"Six thousand miles folding into one hallway,"* — Kai, seen properly for the first time in the video: standing still in the gap, dark green jacket, not waving, medium.
59. *"And your arms in the doorway and nothing in the way."* — his face, close-up, the moment he sees her, everything else out of focus.
60. *"I dropped the bag before I got to where you stood,"* — the duffel hitting the tile mid-stride and staying there, low insert, her legs continuing past it.
61. *"And the year hit the floor and it broke open good."* — the collision, held long, both of them turning with the momentum, wide, flares across the frame.
62. *"Pull the window shade up, let the morning come on,"* — the abandoned bag alone on the polished floor with people stepping around it, static, five seconds.
63. *"Landing gear down, my heart's coming home."* — back to them, her feet off the ground, his hand on the back of her head, close-up.

### Post-chorus — the hall carries on

64. *"Coming home, coming home,"* — a high wide from the mezzanine: two motionless people in the middle of a moving terminal.
65. *"Feet on the floor and I'm not on my own."* — her feet finding the tile again, insert, his shoes beside hers.
66. *"Coming home, coming home,"* — someone nearby noticing, smiling, and looking away, medium, warm.
67. *"Every mile I flew was a mile of the way home."* — the camera continuing to pull back and up until the two of them are small, wide, daylight softening.

### Outro — over the ocean

68. *"Somewhere over the ocean I stopped being scared,"* — return to the dark cabin, Mahima asleep against the window, cabin blue, static.
69. *"Somewhere over the ocean the year let go."* — the seatback map, the little plane most of the way across (composited), macro.
70. *"The little plane on the little map is gone now,"* — the screen going dark, the map gone, her reflection in the blank panel.
71. *"And I'm standing where the map was trying to go."* — final shot: the two of them walking out of the terminal into clean white daylight, the duffel now on his shoulder, the doors closing behind them, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first reading light, the gear locking down (shot 15), each
*"landing gear down"*, the wheels touching (shot 22), the moment she starts
running (shot 36), the instrumental drop (shot 49), *"done being good at
missing you"* (shot 55), the modulation into shot 56, the bag hitting the
floor (shot 60), and the last frame. At 108 BPM a bar is 2.22 s; the run cuts
every bar and the pre-choruses cut every half-bar.

**The dropped-bag challenge.** Post the vertical cut of shots 36 and 56–61 —
the decision, the gap, the bag, the collision — under *"landing gear down, my
heart's coming home"* and invite long-distance couples to post their own
arrivals footage, phone-shot and shaky and badly framed, cut to the modulated
final chorus. The bridge wide (shot 50) is the second shareable frame and the
better still image.

## 6. Quality-control checklist

- Two Mahima looks in the right sections: blanket and slept-on hair in the air, sleeves shoved up and bag on the shoulder from shot 28 on
- Kai's face does not appear anywhere before shot 58, not even out of focus
- Every screen, sign, stamp, placard and calendar is a blank lit plate with the content composited — no model-generated lettering anywhere in an airport
- Nothing in the present is darker than the shot before it after the wheels touch in shot 22
- Chorus flashbacks are cold, lamp-lit and narrower than the shots they cut out of
- The duffel: on her shoulder, dropped in shot 60, left alone in shot 62, on his shoulder in shot 71 — never carried by her again
- The receipt is written, read once and hidden, and is never seen after shot 10
- OpenPose on the run and the collision; check hands on every close-up of the bag strap
- The last shot is locked-off, has no dialogue and holds until the audio fades
