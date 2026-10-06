# Wan 2.2 Shot List — "Photo Booth Strip"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. Timestamps come from the rendered WAV; cut
on the sung line. At 108 BPM a bar is 2.22 s, so verse shots run 2–4 s and the
post-chorus cuts on the word.

## 1. Visual style

Three worlds and one object. **The booth** is warm tungsten with a hard
on-axis flash, slightly too bright, shot mostly from where the lens is. **The
mall** around it is cold fluorescent going to green emergency lighting as the
building shuts down. **The present day** is flat blue-grey winter daylight
with no warmth in it at all, so that the tungsten inside the paper strip is
the only warm thing in every present-day frame. The strip is the hero object
and appears in twenty-two shots; it must be the same physical prop, same
crease, same torn edge, every time. Handheld inside the booth, static
everywhere else.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cold fluorescent concourse, one warm booth | Macro, then locked-off wide |
| Verse 1 | Warm tungsten with hard flash punctuation | Lens-POV and curtain-gap profile |
| Pre-choruses | Booth tungsten, flash lamp cycling | Macro, tight |
| Choruses | Paper lit like a museum object | Static overhead, then match cuts |
| Verse 2 | Overexposed on the blur, then green emergency | Handheld, then wide |
| Instrumental | Green low light, one warm rectangle | Slow, observational |
| Bridge | Flat blue-grey winter daylight | Close on hands, static |
| Final chorus | First warm domestic light in the present | Steady, medium |
| Post-chorus | Booth tungsten, black between cuts | One word, one cut |
| Outro | Grey daylight through concrete | Slow drift, held wide |

## 2. Character bible — paste into every prompt

**Mahima** (the night, aged about nineteen)
> Same female protagonist Mahima, young woman of about nineteen, expressive dark eyes, oval face, long dark wavy hair loose with one side tucked behind her ear, light natural makeup with a glossy lip, wearing a cropped black cardigan over a striped tee and a corduroy skirt, bright nervous expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (present day)
> Same female protagonist Mahima, woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair pushed back, no makeup, wearing a heavy charcoal wool coat and a grey scarf, composed unhurried expression, realistic cinematic photography, consistent identity

**Kai** — the boy in the booth, and the only male lead with a face.
> Same male character Kai, man in his late teens, close-cropped dark hair, faint stubble, wearing a green corduroy jacket over a plain white tee, warm amused expression, realistic cinematic photography, consistent identity

**The mall guard** — a flashlight beam, a shoulder, a set of keys. Never a face, never a full body.

**The mother on the bench** — an out-of-focus figure with shopping bags in the far background of one shot only.

Objects that recur: the **red velvet curtain**, the **quarters**, the
**metal delivery tray**, the **paper strip** with its four frames, the
**torn edge** down the middle of it from shot 32 onward, and the **wool coat**
with the receipt in the pocket.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All booth numerals, countdown displays, mall signage, store names, the bus
pass and the receipt are composited in the edit.** Generate every panel and
label as a blank lit surface. The four photographs inside the strip are also
composited: shoot each frame as its own live plate, grade it to booth
tungsten, then place it into the paper in post so the strip is identical in
every one of its twenty-two appearances.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA each.
**The booth is a hard set for the model** — it is tiny, symmetrical and
mirror-heavy, so build the interior as a Depth reference and reuse it for
every booth shot rather than regenerating the space. OpenPose for the chin
turn in shot 9 and the laugh in shot 26, both of which are the kind of
specific human movement the model smooths into nothing without a reference.
The blur in shot 27 is deliberately a bad photograph: shoot it as a real long
exposure plate, do not ask the model for motion smear. 16:9 first; 9:16 for
the strip and the post-chorus, which are natively vertical. Animate small: a
curtain falling, a coin dropping, a paper strip curling.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — closing time

1. *"Curtain the color of a cheap red wine"* — macro on red velvet curtain nap, one hand pulling it back an inch and letting it fall closed, static.
2. *"Two dollars in quarters and a boy with a plan"* — macro on a palm of quarters, then one going into the slot, the mechanism swallowing it.
3. *"The mall is closing, the escalator's stopped"* — wide of an empty concourse, shutters half down, a still escalator, the lit booth tiny at the far end.
4. *"And we're the only ones still standing where we stand"* — the two of them small in that wide, standing at the curtain, nobody else in the building, locked-off.

### Verse 1 — frames one and two

5. *"Frame one, I'm looking at the lens like I'm supposed to"* — lens-POV: Mahima seated square to camera, polite photo face, hands visible in her lap, warm tungsten.
6. *"Hair behind my ear and my hands in my lap"* — close-up of her tucking one side of her hair back, the gesture she will repeat in the bridge.
7. *"You're half a second late and your eyes are on me"* — lens-POV: Kai dropping into frame a beat late, already turned toward her instead of the camera.
8. *"So the first of the four is already a trap"* — the flash fires: two frames of pure white, then the pair blinking, close two-shot.
9. *"Frame two, you turn my face with two fingers"* — profile through the curtain gap: two fingers turning her chin, held slow, the most deliberate movement in the video.
10. *"And the flash catches the second I say okay"* — extreme close-up of her mouth on the word, the flash blowing out mid-syllable.
11. *"Somebody's mom is waiting on the bench outside"* — a wide of the concourse bench, an out-of-focus woman with shopping bags checking a watch, the booth curtain twitching behind her.
12. *"And I forget my own name in the easiest way"* — lens-POV: both of them looking at each other and not at the camera as the flash goes, the frame that becomes the kiss.

### Pre-chorus 1 — the countdown

13. *"The machine counts down in a voice like a school bell"* — macro on the booth countdown lamp cycling (numerals composited), a mechanical clunk, the iris moving.
14. *"Four little squares and no way to choose"* — the four exposure windows in the machine face, blank and lit, static macro.
15. *"No take it again, no do it better"* — both of them frozen mid-adjustment, waiting, breathing, tight from the side.
16. *"Just whatever we were, and then the proof"* — the delivery tray, empty, lit from inside, the developing sound audible, macro.

### Chorus 1 — the strip

17. *"Four frames, one night, photo booth strip of my life"* — the wet strip sliding into the metal tray, four squares in a vertical column, lit from above, static.
18. *"A smile, a kiss, a laugh and a blur on the right"* — the strip picked up by two fingers at the edge, turned toward the light, water still on it.
19. *"Two dollars, a curtain, and a flash in the dark"* — frame one expands to fill the screen and becomes live for one bar: her polite smile, then it snaps back to paper.
20. *"Cut it down the middle, you still can't tell us apart"* — frame two expands and becomes live: the chin turn and the kiss, then it snaps back.
21. *"Everybody gets a wall, a shoebox, a shelf"* — a fridge door covered in other people's photographs, none of them hers, slow pan.
22. *"I got four inches of paper that I keep to myself"* — the strip laid flat on a palm, actual scale, next to a house key for reference, macro.
23. *"In a wallet, in a coat pocket, out of the light"* — three fast cuts: a wallet behind a bus pass, an inside coat pocket, a drawer closing.
24. *"Four frames, one night, photo booth strip of my life"* — the strip alone on black, lit like a museum object, held.

### Verse 2 — frames three and four

25. *"Frame three, you say the thing about the sandwich"* — lens-POV: Kai mid-sentence, gesturing with both hands, entirely unbothered about the camera.
26. *"And I'm laughing with my whole face, eyes gone"* — lens-POV: her head back, eyes screwed shut, laughing so hard the booth shakes, the best frame in the video.
27. *"Frame four is a blur, you turn to tell me something"* — a real long-exposure plate: Kai turning toward her as pure motion smear, her half a ghost beside him.
28. *"And the flash gets the motion and none of the sound"* — the same plate held on screen with the audio dropping out entirely for one beat.
29. *"I still don't know the end of that sentence"* — present-day insert, two seconds: her face at a window, unreadable, cold daylight, the only present-day shot before the bridge.
30. *"The mall guy kills the lights and rolls the gate"* — a flashlight beam sweeping the concourse, shutters coming down in sequence, the fluorescents going to green.
31. *"We tear it down the middle on the escalator"* — the strip against a thumb at the top of the still escalator, torn in one motion, macro, no ceremony.
32. *"And you get the frames where I look great"* — his half going into a corduroy jacket pocket, hers hanging from her fingers, the two halves parting frame in opposite directions.

### Pre-chorus 2 — nobody on the stool

33. *"The machine counts down in a voice like a school bell"* — the same countdown lamp from shot 13, cycling, with nobody on the stool.
34. *"Four little squares and no way to choose"* — the four exposure windows again, dark now, one flickering.
35. *"Nobody tells you when you're in the last one"* — the booth seat, worn through in the middle, the curtain moving slightly with no reason given.
36. *"You find that out later, and it lands like news"* — a single quarter on the tiles under the seat, macro, the concourse black beyond it.

### Chorus 2 — where it lived

37. *"Four frames, one night, photo booth strip of my life"* — the half-strip in a wallet behind a bus pass, the wallet opening and closing, macro.
38. *"A smile, a kiss, a laugh and a blur on the right"* — taped inside a locker door, corners curling, fluorescent light, a hand closing the door on it.
39. *"Two dollars, a curtain, and a flash in the dark"* — between the pages of a paperback, the book snapping shut, dust in the light.
40. *"Cut it down the middle, you still can't tell us apart"* — face-down in a drawer under a handful of batteries, the drawer closing, black.
41. *"Everybody gets a wall, a shoebox, a shelf"* — frame three expands and becomes live for one bar: the laugh, slower than before.
42. *"I got four inches of paper that I keep to myself"* — frame four expands and becomes live: the blur, held two frames longer than it wants to be.
43. *"In a wallet, in a coat pocket, out of the light"* — the strip in each of the four hiding places in four fast cuts, the light around it different every time, the tungsten inside it identical.
44. *"Four frames, one night, photo booth strip of my life"* — the strip alone on black again, now visibly torn down one side, held.

### Instrumental — the mall, empty

45. The concourse in green emergency lighting, shutters fully down, absolutely still, wide.
46. The stopped escalator seen from directly above, the handrail catching one strip light.
47. The booth still lit and glowing, the only warm rectangle in the building, slow push-in.
48. The curtain moving with no wind reason, macro, unsettling.
49. A single quarter spinning to rest on the tiles, close-up, then black.

### Bridge — the coat pocket

50. *"Found it in a coat in November with a receipt"* — a wool coat on a hook in flat winter light, a hand going into the inside pocket, close on the hands.
51. *"Half a strip, three good frames and one that came out wrong"* — the half-strip and a folded receipt coming out together, the receipt dropped, the paper kept.
52. *"Everybody wants the kiss, everybody wants the laugh"* — the strip held up against the window, all frames backlit, her face out of focus behind it.
53. *"But the wrong one is the one I've kept this long"* — her thumb settling deliberately over the blur frame and staying there, macro.
54. *"We were both already moving when the last flash went"* — present-day Mahima tucking one side of her hair back, the same gesture as shot 6, in a different life.
55. *"And I'd rather have a blur than a night I never spent"* — a locked-off medium of her at the window, one breath she does not quite control, no music cue on her face.

### Final chorus — where it lives now

56. *"Four frames, one night, photo booth strip of my life"* — the fridge door from shot 21, her hand hovering with the strip and a magnet, warm domestic light for the first time.
57. *"A smile, a kiss, a laugh and a blur on the right"* — she does not do it. The hand comes down. Static, held one beat too long.
58. *"Two dollars, a curtain, and a flash in the dark"* — an empty picture frame opened, considered, closed and put back in a drawer.
59. *"Cut it down the middle, you still can't tell us apart"* — the two torn halves laid edge to edge on a table, the tear line invisible from a distance, overhead.
60. *"Everybody gets a wall, a shoebox, a shelf"* — a slow pan across her actual shelves: books, a plant, other people's photographs, no strip anywhere.
61. *"I got four inches of paper that I keep to myself"* — the strip going into the inside coat pocket, deliberately, one pat over the outside of it.
62. *"Not on the fridge, not in a frame, just out of sight"* — the coat going onto the hook, the pocket flat, the hallway empty, wide.
63. *"Four frames, one night, photo booth strip of my life"* — her walking out of frame without looking back at the coat, warm light, static.

### Post-chorus — one word, one cut

64. *"A smile, a kiss, a laugh, a blur"* — the four live frames for exactly one word each, in order, booth tungsten, black between cuts.
65. *"A smile, a kiss, a laugh, a blur"* — the same four, faster, the blur held one beat longer at the end.
66. *"Four frames, one night"* — the whole strip on black, all four squares at once, two beats.
67. *"A smile, a kiss, a laugh, a blur"* — the four again, fastest, ending on the blur alone, held into silence.

### Outro — the site

68. *"The mall came down the summer after"* — a slow drift across a concrete parking structure deck, numbered bays, strip lights, nobody, grey daylight.
69. *"There's a parking structure where the booth used to stand"* — Mahima standing roughly where the booth was, hands in coat pockets, working out the geometry.
70. *"I've still got four inches of a Tuesday"* — her hand inside the coat pocket, not taking anything out, close-up.
71. *"And a laugh with my eyes gone and your hand"* — final shot: the laugh frame from shot 26 filling the screen, live, held silent, then fading to the paper version of it and out. No text.

## 5. Edit and the challenge

Markers at: the coin drop, the first flash, the chin turn in shot 9, the
strip landing in the tray, the long-exposure blur, the tear at the top of the
escalator, the instrumental, the thumb over the blur, the hand that does not
put it on the fridge, and the final laugh. At 108 BPM a bar is 2.22 s;
choruses cut on the bar, the post-chorus cuts on every word.

**The shareable cut** is shots 17–20, vertical: the wet strip in the tray and
the first two frames expanding into live action, with *"cut it down the
middle, you still can't tell us apart"* on screen.

**The challenge — frame four.** Post your own photo booth strip and caption
the fourth frame, the bad one, with what was actually happening in it. The
post-chorus is built to be lip-synced at one cut per word and is the second
shareable moment.

## 6. Quality-control checklist

- Two looks for Mahima, strictly separated: the booth night through shot 32, present day from shot 50, with the single deliberate exception of the two-second insert at shot 29
- Kai never appears in a present-day shot, and never after shot 32 except inside a photograph
- The mall guard is a flashlight beam and a shoulder only
- The paper strip is one physical prop with the same crease and the same torn edge in all twenty-two of its appearances, and the tear exists from shot 31 onward and never before
- The four photographs are composited from graded live plates, not model-generated; the blur is a real long-exposure plate
- All numerals, signage, the bus pass and the receipt composited; no model-generated text anywhere
- Every present-day frame is cold except the last chorus, and the tungsten in the paper is the only warm light in the bridge
- The last shot is the laugh, held silent, and fades to paper rather than to black
