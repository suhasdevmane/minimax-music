# Wan 2.2 Shot List — "Forever Looks Like Tuesday"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
84 BPM a bar is 2.86 s — the slowest song in this batch — so shots run four to
seven seconds and almost nothing cuts inside a line.

## 1. Visual world

One house, one Tuesday, shot in honest daylight with no grade that could not
have come out of the window. The house is the third character: its dripping
faucet, its dead bulb, its fridge list, its pile of shoes. **Two rules govern the
whole edit.** First, the wedding is shown only in flashes under a second each,
beautifully lit and given no time — the point is that the plain footage is
allowed to breathe and the pretty footage is not. Second, the hospital parking
lot is the only night sequence and the only place the camera stops moving
entirely. Everything else is soft handheld and long holds.

| Section | Grade | Camera |
|---|---|---|
| Intro | Flat honest daylight through net curtain | Macro, locked off |
| Verse 1 | Midday, warm on the sofa, cool on the kitchen floor | Long holds, soft handheld |
| Pre-choruses | Overexposed gold flashes, then plain daylight | Sub-second cuts, then static |
| Choruses | Sun crossing the room, warming through the song | Slow drifts, following moves |
| Verse 2 | Sodium orange through a fogged windshield, night | Completely static |
| Instrumental | Late afternoon, low gold | One long tracking shot |
| Bridge | One warm kitchen light, daylight dying | Held two-shot, then singles |
| Final chorus | Interior lights on for the first time | Moving, wider |
| Post-chorus / outro | Last gold, then one warm lamp | Matched to the intro |

## 2. Character bible — paste into every prompt

**Mahima** (the whole song, one look — this is a one-day film)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pushed up into a loose knot with strands falling out, no makeup, wearing a soft oatmeal sweater with the sleeves pushed up and gray sweatpants and thick socks, reading glasses pushed onto her head, relaxed lived-in expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the hospital parking lot, the only other look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and flat, tired face with no makeup, wearing a navy sweater under a large dark coat that is clearly not hers, exhausted steady expression, realistic cinematic photography, consistent identity

**Kai** (the male lead — he sings verse two, so he is on camera as much as she is)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded green work shirt with the sleeves rolled and dark jeans, forearms wet, holding a wrench, patient good-humored expression, realistic cinematic photography, consistent identity

**The wedding flashes** — the couple are seen only as hands, a shoulder, a
back and rice in the air. No guest gets a face. The woman crying in the
second row is filmed from behind at the shoulder.

There is no third character with lines or a face anywhere in this video.

Objects: the **dripping faucet**, the **wrench**, the **dead bulb above the
stairs**, the **fridge list**, the **shirt dried wrong on the radiator**, the
**laptop and paper form**, the **mug of cold coffee**, the **pile of shoes**,
the **paper cup** in the parking lot, the **stepladder**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The fridge list, the calendar page, the tax form, the laptop screen and any
hospital signage are composited in the edit.** Generate them as blank paper,
blank squares and dark screens, then add the handwriting, the crossed-out
line and the empty Tuesday square in post — the model cannot render legible
writing, and the list losing one line is the video's closing beat.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA; Kai
carries a full verse alone here, so his reference set needs more coverage than
in a solo song — front, three-quarter, lying on his back on the floor, and lit
from below by a flashlight. **Depth is essential on every interior** so the hall,
the kitchen and the stairwell hold their real geometry across forty shots in
the same house. OpenPose for the bad slow dance and for the stepladder. 16:9
throughout; the 9:16 recomposition is the bridge two-shot and the faucet macro.
Animate the smallest possible amount: one drop falling, a wrench turning a
quarter turn, a page lifting, dust in a sunbeam, a shoulder shifting.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–7 s. The wedding flashes are 0.4–0.8 s and are the only fast cuts.

## 4. Scene per lyric line

### Intro — the house

1. *"The faucet in the kitchen has been dripping since the spring"* — macro on a kitchen faucet releasing one slow drop into a steel sink, locked off, flat daylight, held until the second drop.
2. *"You've been meaning to look at it since May"* — a wrench sitting on the windowsill above the sink where it has clearly been for weeks, close-up.
3. *"There's a light bulb out above the stairs we walk around"* — a dark stairwell with one dead bulb in the ceiling fitting, a figure passing through the dark without pausing, static.
4. *"And a list up on the fridge that never gets shorter"* — a fridge door covered in a handwritten list, a takeout menu and a photograph (writing composited), slow push-in.

### Verse 1 — her Tuesday

5. *"It's a Tuesday, and there's nothing on the calendar at all"* — a wall calendar with one conspicuously empty square (composited), locked off.
6. *"Just the trash, and the bank, and a form I have to sign"* — a trash can being wheeled down a path to the curb, seen from a front window, wide.
7. *"You've got the cupboard open and your shoulder in the pipe"* — Kai flat on the kitchen floor with his head and one shoulder inside the sink cupboard, only his legs, a flashlight and one hand visible, low angle.
8. *"I've got the laptop on my knees and I am losing at the taxes"* — Mahima cross-legged on the sofa with a laptop and a paper form, glasses on, completely defeated, medium.
9. *"There's a shirt of yours drying on the radiator wrong"* — a shirt dried into a bad shape over a radiator, macro, backlit by a window.
10. *"And the good scissors are somewhere neither of us can name"* — a drawer opened and closed, then a second drawer, then a third, three cuts, no scissors anywhere.
11. *"Nobody's taking pictures, nobody got dressed up"* — a wide of the whole room with neither of them looking at each other and both entirely at ease, held.
12. *"And I wouldn't trade this afternoon for anything"* — Mahima looking up from the laptop at his legs sticking out of the cupboard and smiling to herself, close-up.

### Pre-chorus 1 — what she was told

13. *"They told me it would look like a church and a dress"* — a 0.6 s flash: a church door standing open, overexposed and golden.
14. *"Rice in my hair and your hand holding mine"* — a 0.6 s flash: rice in the air against the sun, then two hands, cropped at the wrists.
15. *"And it did, for a day. But mostly it looks like this"* — hard cut back to the kitchen floor: the flashlight, the wrench, plain daylight, the flashes over.
16. *"Two people and a Tuesday and a job half done"* — a wide of the kitchen with the cupboard emptied onto the floor around him, static, held.

### Chorus 1 — the house in motion

17. *"Forever looks like Tuesday"* — wet hands under a running faucet, macro, the water loud in the mix.
18. *"And Tuesday looks like you"* — the wrench turning a quarter turn, his forearm and the pipe, close-up.
19. *"Wet hands, a wrench, a radio on low"* — an old radio on a windowsill with the dial lit, dust around it, static.
20. *"And a coffee going cold and a whole afternoon to go"* — a mug of coffee beside the laptop with a skin on the surface, macro, the sun a little further across the table.
21. *"Nobody writes it down, nobody makes a fuss"* — laundry being carried through a doorway, the basket blocking half the frame, following move.
22. *"But the ordinary hours are the best of us"* — the two of them passing in the hall and each moving aside for the other without looking up, wide, one continuous take.
23. *"Forever looks like Tuesday"* — the sun visibly further across the living-room floor than it was in shot 11, same framing, held.
24. *"And Tuesday looks like you"* — Kai's face appearing out of the cupboard for the first time in the video, grinning, close-up.

### Verse 2 — the hospital parking lot

25. *"I thought forever came with fireworks and a plane"* — a framed photograph on a shelf, deliberately out of focus, slow rack that never quite resolves.
26. *"Some big loud proof that you could point to on a wall"* — a picture hook and a bare patch of wall beside the photos, static, two seconds of nothing.
27. *"Then the winter that your father was in the hospital"* — hard cut to night: a hospital parking lot in winter, a car with the engine off among a dozen empty spaces, sodium orange, completely static wide.
28. *"And we ate out in the parking lot and you slept against my coat"* — inside the car: two takeout containers on the dashboard, breath fogging the inside of the windshield, Mahima (parking-lot look) asleep against his shoulder under his coat, static.
29. *"That was a Tuesday too. Nobody sang about it"* — macro on a paper cup held in two hands on her lap, steam almost gone, static.
30. *"You held the paper cup with both your hands and you were fine"* — her face lit white by a vending machine through the windshield, tired and steady, close-up.
31. *"And I knew right then, whatever this thing is"* — Kai's face in the driver's seat watching her and understanding something, close-up, orange light.
32. *"It isn't in the party, it's in getting through the week"* — the two of them walking back toward a lit hospital entrance, small in a very wide static frame, the last night shot in the video.

### Pre-chorus 2 — the second flash

33. *"They told us it would look like a stage and a speech"* — a 0.6 s flash: a microphone on a stand at a reception, warm and overexposed.
34. *"Somebody's mother crying in the second row"* — a 0.6 s flash: a woman filmed from behind at the shoulder, wiping her eyes, no face.
35. *"And it did, for an hour. But mostly it looks like this"* — a 0.6 s flash of a glass being raised, then a hard cut to the kitchen floor and the flashlight, daylight restored.
36. *"Two people and a Tuesday and a job half done"* — reuse shot 16's framing, later in the day, more of the cupboard on the floor, held.

### Chorus 2 — an hour on

37. *"Forever looks like Tuesday"* — wet hands again, the light lower and warmer, macro.
38. *"And Tuesday looks like you"* — the wrench again, further into the job, a pipe section now free in his hand.
39. *"Wet hands, a wrench, a radio on low"* — the radio, the dial the brightest thing in a dimmer room.
40. *"And a coffee going cold and a whole afternoon to go"* — the mug now empty with a ring inside it, pushed to the far side of the table.
41. *"Nobody writes it down, nobody makes a fuss"* — the laundry now folded in a pile nobody has put away, static.
42. *"But the ordinary hours are the best of us"* — the same hall pass as shot 22, but this time one of them puts a hand on the other's back going by.
43. *"Forever looks like Tuesday"* — a long shadow across the living-room floor where the sunbeam was, same framing again.
44. *"And Tuesday looks like you"* — Mahima closing the laptop and putting the form on top of it, done for the day, medium.

### Instrumental — the pedal steel, the house

45. Dust turning in a low sunbeam over the arm of the sofa, macro, very slow, six seconds.
46. The fridge list with one item now struck through (composited), slow push-in.
47. The pile of shoes by the front door, low angle, gold light across them.
48. One long slow tracking shot down the hall from the front door to the kitchen doorway, unbroken, carrying the steel solo.
49. Both of them at the kitchen table with the faucet parts spread out between them, laughing at something that has clearly gone wrong — the cut into the bridge.

### Bridge — a line each, on the floor

50. *"I'll take the faucet that drips, I'll take the burnt-out bulb"* — the held two-shot begins: both of them sitting on the kitchen floor with their backs against the cupboards, side by side, no cut.
51. *"I'll take the taxes and the form you never signed"* — the same two-shot continues, neither of them looking at the other.
52. *"I'll take your terrible singing coming through the wall"* — the same two-shot, her head tipping onto his shoulder for one beat and coming back up.
53. *"I'll take the way you fall asleep in the middle of the film"* — the two-shot ends; the first single: her face in close-up, warm kitchen light.
54. *"I'll take the trash night and the shoes piled by the door"* — single: his face in close-up, the same light, the daylight behind him nearly gone.
55. *"I'll take the way you always buy too many eggs"* — single: her again, laughing before the line is finished.
56. *"And if forever's just a lot of Tuesdays in a row"* — back to the two-shot, both looking straight ahead, wide.
57. *"Then I'll take Tuesday, and I'll take it slow"* — the same two-shot, held four full seconds after the line ends, the softest lighting in the film.

### Final chorus — it works

58. *"Forever looks like Tuesday"* — the faucet turned full on and then off cleanly, no drip, macro, the shot that answers shot 1.
59. *"And Tuesday looks like you"* — a hand at the top of a stepladder seating a bulb, and the stairwell filling with light in one move, wide.
60. *"Wet hands, a wrench, a radio on low"* — the radio turned up, a hand leaving the dial, close-up, interior lights on for the first time.
61. *"And the faucet has stopped its dripping and there's still a night to go"* — the two of them eating standing up at the counter with plates in their hands, wide.
62. *"Nobody writes it down, nobody makes a fuss"* — the wrench going back in a drawer and the drawer closing, macro.
63. *"But the ordinary hours are the best of us"* — a genuinely bad slow dance across the hall that neither of them fully commits to, one continuous handheld take.
64. *"Forever looks like Tuesday"* — the two of them stopping mid-dance because something is boiling over, and both turning for the kitchen, wide.
65. *"And Tuesday looks like you"* — Kai looking back at her over his shoulder from the kitchen doorway, close-up, warm.

### Post-chorus — the week rolls on

66. *"Tuesday, Tuesday, and the week rolling on"* — a calendar page being lifted and turned to the next week, macro, last gold of the day.
67. *"Tuesday, Tuesday, and I want every one"* — the trash cans going back up the path in the dark, seen from the front window, wide.
68. *"Tuesday, Tuesday, and the light turning gold"* — the pile of shoes by the door with two more pairs added, low angle.
69. *"Forever looks like Tuesday, and I'll take it till we're old"* — the two of them on the sofa, one already asleep, the other still watching the screen, wide, one lamp.

### Outro — matching the intro

70. *"The faucet in the kitchen isn't dripping anymore"* — the exact framing of shot 1: the faucet, dry, no drop coming, held five seconds.
71. *"There's a bulb above the stairs and we can see the floor"* — the exact framing of shot 3: the stairwell, now lit, empty.
72. *"The list up on the fridge is one line shorter than it was"* — the exact framing of shot 4: the list with one line struck through (composited), slow push-in.
73. *"And that is what a good life looks like, I suppose"* — final shot: a locked-off wide of the kitchen with both of them just out of frame, one warm lamp on, the light settling, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first drop, the empty calendar square, each *"forever looks
like Tuesday"*, the hard cut to the parking lot, the return to daylight, the
instrumental, the start of the bridge two-shot, the faucet being turned on dry,
and the last framing match. At 84 BPM a bar is 2.86 s; nothing cuts faster
than a bar except the five wedding flashes, which are the only sub-second
shots in the film.

**The ordinary-Tuesday challenge.** The shareable cut is the bridge, shots
50–57, vertical, with the six list lines on screen one at a time. Invite
people to post their own unglamorous Tuesday — the job half done, the thing
they would take, the person they would take it with. The second shareable
cut is shots 1 and 70 back to back: the dripping faucet and the dry one.

## 6. Quality-control checklist

- One Mahima look for the whole day and one for the parking lot only (shots 27–32); Kai wears the same work shirt in every daylight shot with the forearms getting progressively wetter
- Both leads are on camera for a comparable amount of time — this is a duet and he sings a full verse; Kai's face is not shown clearly until shot 24, which is deliberate
- The five wedding flashes are all under a second, all overexposed and golden, and no guest has a face
- The parking lot is the only night sequence and the only completely static camera in the film
- Framing matches exactly between shots 1 and 70, 3 and 71, 4 and 72, and 11, 23 and 43 — the whole ending depends on these
- The fridge list, calendar square, form and laptop screen composited in the edit; no model-generated writing anywhere
- No distorted hands in the wrench, faucet, paper-cup and stepladder close-ups
- The last shot is locked off, nobody re-enters frame, and it holds until the audio fades
