# Wan 2.2 Shot List — "Borrowed Shirt"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. At 84 BPM a bar is 2.86 s, so shots run long
here — four to seven seconds — and the cuts fall on the phrase rather than
the beat. Take timestamps from the rendered WAV.

## 1. Visual style

One apartment, one morning, no cutaways to anywhere else and no other
people. The whole film is domestic macro and slow drifting wides: skin,
cotton, steam, dust in a sunbeam, the grain of a floorboard. **The light is
the clock** — it starts low and raking through a half-drawn curtain, climbs
across the boards through the choruses, and by the final chorus the room is
flat and bright and even. Nothing is styled; the flat looks lived in, the bed
stays unmade, the washing-up is real. Shallow focus almost throughout, so the
background is always a warm blur.

Tasteful is a hard rule: she is in his shirt with the sleeves rolled and it
is never a lingerie shoot. The camera stays at face, hands and feet. The most
intimate frame in the film is a kiss on a shoulder through cotton.

| Section | Grade | Camera |
|---|---|---|
| Intro | Low raking sun, deep shadow, dust in the beam | Macro, static |
| Verse 1 | Bright kitchen against a dark bedroom doorway | Static, shallow |
| Pre-chorus 1 | Even warm interior, object by object | One slow track |
| Chorus 1 | Golden, wide, no cool tones anywhere | Slow drifting, wide |
| Verse 2 | Warm, one shaft of light per object | Macro, static |
| Pre-chorus 2 | Flat kitchen light, fridge-door reflection | Handheld, close |
| Chorus 2 | Sun higher, room brighter, fuller | Drifting, wider |
| Instrumental | Grainy, warm, pure texture | Slow drift, no cuts on beat |
| Bridge | Curtains half drawn again, softest light of the film | Static, close |
| Final chorus | Brightest and flattest, midday coming | Pull-backs |
| Post-chorus | Unchanged golden, four repeating beats | Static macro |
| Outro | Late-morning light gone soft and even | Locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the whole film — one look only)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slept-in, no makeup at all, wearing an oversized pale blue men's oxford shirt with the sleeves rolled twice and the top three buttons open, bare legs and bare feet, relaxed unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, bare-chested under a grey open cardigan or in a plain white t-shirt and dark pyjama trousers, hair wrecked from sleeping, sleepy easy expression, a thin black hair tie around his right wrist, realistic cinematic photography, consistent identity

There is no third character. No exes, no friends, no phone calls, nobody at
the door. If a living thing is needed in a frame, use a plant on the sill or
a cat asleep on a chair; the location decides.

Objects that carry the story and must stay consistent: the **pale blue
oxford shirt**, the **chipped mug** on a shelf of matching ones, the
**turntable and the record on its run-out groove**, the **watch face down on
the windowsill**, the **single kicked-off shoe by the door**, the **hair tie
on his wrist**, the **bedside drawer** with a charger, a lip balm and a
dog-eared paperback, and the **shopping list on the fridge in two
handwritings**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The wall calendar, the shopping list and the two handwritings on it are
composited in the edit.** Generate the fridge door and the calendar blank —
the model cannot render handwriting, and the second handwriting being hers
is the whole point of that shot.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and Kai with IP-Adapter or a character LoRA; only two identities
in the entire film, so the references can be small and exact. Depth is the
key ControlNet here rather than OpenPose — the story is spatial, one flat
seen from a dozen angles, and the doorway compositions need consistent
geometry. Use OpenPose only for the two dancing shots and the counter-sit.
16:9 first; 9:16 for the chorus turns and the shoulder kiss, which are the
natural vertical content.

Animate very conservatively. This song is slow and the model rewards small
motion: steam rising, a curtain breathing, a cuff being rolled, a needle
riding a groove, a chest rising in sleep. Anything faster than a walk across
a room should be split into two clips.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–7 s.

## 4. Scene per lyric line

### Intro — the run-out groove

1. *"Needle at the end of the record, going round"* — extreme macro on a turntable, the needle riding the run-out groove, the platter turning, dust visible on the vinyl, static.
2. *"Making that soft little scratch instead of sound"* — the tonearm from above, the counterweight steady, the record label a soft blur (blank, composited later if needed), macro.
3. *"Curtains half open on a street still asleep"* — a half-drawn curtain with low raking sun behind it, an empty street visible through the gap, one parked car, slow drift.
4. *"And your shirt on my shoulders, three buttons deep"* — bare feet crossing a wooden floor, then a slow pan up to the open collar of the pale blue shirt, her chin, her sleep-flattened hair.

### Verse 1 — the kitchen and the doorway

5. *"The kettle's doing that thing where it rattles the lid"* — macro on a kettle lid shivering on the boil, steam catching the window light, static.
6. *"You're still under the blanket, doing what you did"* — a wide from the kitchen through an open doorway into the dark bedroom, a shape under a blanket, one arm hanging off the mattress.
7. *"Which is nothing, beautifully, one arm hanging loose"* — closer on that arm and the hair tie on his wrist, the fingers slack, the duvet rising and falling, macro.
8. *"Face down in the pillow like you've got no excuse"* — Kai face down in the pillow, hair wrecked, one eye barely opening and closing again, close-up in soft shadow.
9. *"I roll the sleeves up twice and they swallow my hands"* — macro on her rolling a cuff twice; the sleeve still finishing past her knuckles, hard morning light across the counter.
10. *"Smells like cedar and the rain that we walked in"* — her pulling the shirt collar to her face for exactly one breath, eyes closing, close-up.
11. *"I take the ugly mug, the one with the chip"* — a hand reaching into a cupboard past four matching mugs to take the chipped one, macro.
12. *"Make the coffee far too sweet so you'll steal a sip"* — two heaped spoons of sugar going in, deliberately, then her small private smile over the rim, close-up.

### Pre-chorus 1 — the inventory

13. *"There's a watch face down on the windowsill"* — a man's watch lying face down on a sill beside a plant, the strap curled, morning light across the glass, macro static.
14. *"There's a shoe by the door lying where it fell"* — one shoe on its side by the front door where it was kicked off, the other nowhere in frame, low angle.
15. *"Nothing here is tidy, nothing here is planned"* — one continuous slow track through the flat: a towel over a chair back, a book face down, two glasses on the floor by the sofa.
16. *"And I've never felt this easy standing where I stand"* — the track ending on her stopped in the middle of the room, eyes closed, arms loose, just standing in it, medium wide.

### Chorus 1 — the morning at its widest

17. *"I'm wearing your shirt and nothing else is on my mind"* — Mahima turning slowly on the floorboards, shirt tails moving with her, the sun behind her, wide, golden.
18. *"No plans, no phone, no reason to be on time"* — her phone face-down and forgotten on the arm of the sofa, the screen dark, dust settling on it, macro.
19. *"The sunlight's doing slow laps across the floor"* — a short time-lapse of the sunbeam moving across the boards, dust turning in it, locked-off.
20. *"And I'm not thinking past the kitchen door"* — a wide framed through the kitchen doorway, her in the middle of it, the rest of the world not in the film.
21. *"Small and ordinary and holy as it gets"* — butter going onto hot toast and melting into it, macro, ridiculous and beautiful.
22. *"Toast and butter, two spoons, and the radio set"* — two teaspoons side by side on a saucer and a small kitchen radio with a blank dial (composited), her hand adjusting it.
23. *"Say my name low, say it one more time"* — Kai appearing in the bedroom doorway with his hair wrecked, saying something we do not hear, her turning at the sound.
24. *"I'm wearing your shirt and nothing else is on my mind"* — the two of them across the room from each other, neither moving, both grinning, wide static.

### Verse 2 — the fourth Sunday

25. *"Fourth Sunday in a row that I've woken up here"* — a wall calendar with four small pencil marks in a column (composited), her hand not quite touching it, close-up.
26. *"Which is not an accident, let's be clear"* — her face in a hallway mirror, caught working something out, a very small smile arriving, close-up.
27. *"There's a hair tie on your wrist that is not yours"* — macro on the black hair tie around his wrist as he reaches for the chipped mug, the shirt cuff of his sleeve in frame.
28. *"And my charger's got a home in your bedside drawer"* — a bedside drawer sliding open on a charger coiled neatly, a lip balm and a paperback with a folded corner, macro.
29. *"I nearly ask the question at the counter, then I don't"* — her mouth opening to speak and closing again, a held beat of silence, close-up, shallow focus.
30. *"I ask about the toast instead and you say, sure, both"* — two slices dropping into a toaster and the lever going down, macro, the tension released.
31. *"You come in half asleep and you kiss my shoulder"* — Kai crossing behind her, one hand on her hip in passing, a kiss on her shoulder through the shirt fabric, medium close-up.
32. *"Not my mouth, my shoulder, and somehow that's bolder"* — her eyes closing for exactly one beat and opening again, extreme close-up, the most intimate frame in the film.

### Pre-chorus 2 — the fridge door

33. *"There's a watch lying face down where you left it"* — the same sill and the same watch, this time with his hand reaching past it to open the window latch, macro.
34. *"There's a list on the fridge and my milk is on it"* — a magnet-pinned shopping list in two different handwritings (composited), her finger stopping under the second one.
35. *"Nothing here is tidy, nothing here is planned"* — a wide of the kitchen as an honest mess: the board, the crumbs, the open butter, two mugs, both of them in it.
36. *"And I've stopped counting mornings on one hand"* — her reflection in the fridge door, warm and distorted, looking at the list rather than at herself.

### Chorus 2 — more lived-in

37. *"I'm wearing your shirt and nothing else is on my mind"* — the two of them eating toast standing up at the counter, shoulder to shoulder, wide, brighter than chorus one.
38. *"No plans, no phone, no reason to be on time"* — a clock on the wall with blank hands (composited), then her turning it face-down on the shelf, close-up.
39. *"The sunlight's doing slow laps across the floor"* — the sunbeam further along the boards than shot 19, the same locked-off frame, a visible time jump.
40. *"And I'm not thinking past the kitchen door"* — a record being lifted, flipped and set down, macro, the needle lowering.
41. *"Small and ordinary and holy as it gets"* — her sitting up on the counter, feet swinging, both hands around the chipped mug, medium.
42. *"Toast and butter, two spoons, and the radio set"* — him standing between her knees at the counter, foreheads touching, both fully dressed, both laughing, close two-shot.
43. *"Say my name low, say it one more time"* — extreme close-up on his mouth saying something short and her whole face changing, no sound needed.
44. *"I'm wearing your shirt and nothing else is on my mind"* — a wide of the kitchen with both of them small in it and the light huge, static.

### Instrumental — the flat doing nothing

45. The record turning, macro, the arm tracking slowly inward across the side.
46. Steam rising off two mugs left side by side on the windowsill, backlit, no people, slow drift.
47. The shirt on her in a long bedroom mirror seen from behind, her tugging the collar straight, her face only in reflection.
48. A plant on the sill, or a cat asleep on a chair, entirely ignored by both of them, static macro.
49. Her bare feet and his socks side by side on the floorboards, a slow drift up to the unmade bed behind them — the cut into the bridge.

### Bridge — the shirt folded, and given back

50. *"I fold it on the bed like I'm handing it back"* — Mahima on the edge of the unmade bed folding the shirt with real care across the duvet, in a t-shirt of her own, static, soft.
51. *"Sleeves squared and the collar smoothed flat"* — macro on her hands squaring the sleeves and smoothing the collar flat, slower than the moment needs.
52. *"You look at the shirt and you look at my face"* — the folded shirt held out on two flat palms, Kai in the doorway, his eyes going from the shirt to her, medium.
53. *"And you say, that one is yours now, it lives at your place"* — close-up on him shaking his head once and saying it, entirely unbothered, the smallest shrug.
54. *"So I don't make a speech and I don't ask for proof"* — her face doing something complicated and warm and choosing not to say any of it, extreme close-up.
55. *"I just put it back on, and that's the whole truth"* — her buttoning the shirt back on, one button at a time, from the bottom, unhurried, medium close-up.

### Final chorus — the best part of the day, still indoors

56. *"I'm wearing your shirt and nothing else is on my mind"* — the two of them dancing badly and barely in the kitchen with no music playing on screen, wide, bright.
57. *"No plans, no phone, no reason to be on time"* — the shirt in motion as she turns, the tails lifting, shot from the hip up, midday light.
58. *"The sunlight's doing slow laps across the floor"* — the same locked-off floor frame a third time, the beam now almost gone from the boards.
59. *"And I'm not thinking past the kitchen door"* — a slow pull-back through the kitchen doorway leaving them dancing in the far room, framed small.
60. *"It's not a big love song, it's a Sunday and a shine"* — her laughing with her head right back, throat and open collar in the light, close-up.
61. *"Your shirt, my coffee, and the rest of it is fine"* — the chipped mug in her hand and his hand closing over hers around it, macro.
62. *"Say my name low, say it one more time"* — his mouth at her ear, her eyes closing, a two-shot that stays at shoulder height and above.
63. *"I'm wearing your shirt and nothing else is on my mind"* — the widest shot of the film: the whole flat, both of them small, light everywhere, locked-off.

### Post-chorus — four repeating beats

64. *"Nothing else, nothing else, nothing else is on my mind"* — the kettle, macro, still faintly steaming.
65. *"Just the kettle and the light and you taking your time"* — the light on the floorboards, macro, unchanged.
66. *"Nothing else, nothing else, nothing else is on my mind"* — his hand around the chipped mug, macro, the hair tie still on his wrist.
67. *"Your shirt on my shoulders and the whole day mine"* — her open collar, macro, the same framing as shot 4, closing the loop.

### Outro — nobody gets up

68. *"Needle at the end of the record, going round"* — back to the first frame exactly: the needle in the run-out groove, still turning.
69. *"Neither of us getting up to fix the sound"* — a wide of the two of them on the sofa, her legs across his lap, both looking at the turntable, neither moving.
70. *"Your shirt on my shoulders, three buttons deep"* — close on the open collar and her collarbone, her chest rising slowly, eyes shut.
71. *"And the best part of Sunday is the part we don't speak"* — final shot: the wide of the sofa, both of them still, the record scratching softly, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first needle frame, each *"nothing else is on my mind"*, the
shoulder kiss at shot 31, the instrumental, the shirt held out at shot 52,
the first dancing frame at shot 56, and the last wide. At 84 BPM a bar is
2.86 s; cut on the end of the sung phrase, never mid-line — this song falls
apart if it is cut fast.

**The borrowed-shirt cut.** Post shots 17, 31 and 55 as a vertical
twenty-second edit with the hook on screen, and invite people to film the one
item of clothing they never gave back. The second shareable frame is shot 52,
the folded shirt held out on two palms, captioned *"He said keep it. That was
the whole conversation."*

## 6. Quality-control checklist

- One look for each lead across the whole film; the shirt is the costume and it never changes
- The camera stays at face, hands and feet: nothing in this video is a lingerie shot, and the most intimate frame is a kiss on a shoulder through cotton
- The light only ever advances: the sunbeam in shots 19, 39 and 58 must be measurably further along the boards each time
- Only two people appear in the entire video; no third face, no phone call, no exterior scene
- The calendar, the shopping list, the radio dial and the clock face are composited; no model-generated handwriting or text
- The chipped mug, the watch on the sill, the hair tie and the single shoe recur exactly as placed
- The final wide matches the intro's framing so the film closes its loop
- The last shot is locked-off and holds until the audio fades
