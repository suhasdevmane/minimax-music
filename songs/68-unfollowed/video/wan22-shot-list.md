# Wan 2.2 Shot List — "Unfollowed"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-two lyric shots plus five for the instrumental, numbered
continuously. Timestamps come from the rendered WAV; cut on the sung line. At
100 BPM a bar is 2.4 s, so most shots run 3–5 s and the half-rapped bridge
cuts on the half-bar.

## 1. Visual style

Deliberately unglamorous. The whole video is shot in flat honest daylight
with almost no fill, in one small flat, one park, one salon, one street — the
argument being that nothing cinematic happens on the day you finally do the
thing. Frames get wider as the song goes: the verses are tight and slightly
claustrophobic, the choruses open out, and the final chorus is the only
sequence with air moving through it. The one stylised sequence in the piece
is the bridge, and it is stylised on purpose so that the cut back to the
kitchen lands.

| Section | Grade | Camera |
|---|---|---|
| Intro | Flat kitchen daylight, no fill | Locked-off, long holds |
| Verse 1 / the failed attempts | Cold blue night, one warm lamp | Static, repeated framings |
| Pre-choruses | Unchanged from the intro on purpose | Static |
| Choruses | Bright unglamorous afternoon | Wider, slow handheld |
| Verse 2 | Park gold, salon tungsten, candlelight | Handheld, loose |
| Instrumental | Late golden hour across the floor | Slow pan, dolly |
| Bridge | Hard pools of light in black | Tracking, then to camera |
| Final chorus | Dawn blue to gold, curtains moving | Moving, widest of the video |
| Post-chorus | One frame, a whole day | Locked-off time-lapse |
| Outro | The intro's light, exactly | Locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the flat, present)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair unstyled and pushed behind one ear, no makeup, wearing a grey marl sweatshirt and soft navy joggers, unreadable calm expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (after the haircut — the loud dress)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair cut with a blunt fringe, warm natural makeup, wearing a deep tangerine slip dress, amused settled expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the bridge, the gallery)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pushed back, minimal makeup, wearing a long black wool coat over the grey sweatshirt, direct level expression, realistic cinematic photography, consistent identity

**The ex** — never appears as a person, in any frame, in any form. He exists
only as a folded photograph, an unlit exhibit on a gallery wall, and a name
said at a dinner table by someone else. Do not generate him even faceless.

**Her sister** — a woman a few years older, on a video call and later at the
dinner table, warm, dry, impatient in a loving way.

Objects that repeat: the **mug of cold coffee**, the **kettle**, the **tote
bag**, the **folded photograph**, the **picture light** in the gallery, the
**tangerine dress** on its hanger.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every phone screen, notes app, bus indicator board and gallery label is
composited in the edit.** Generate the phone as a lit blank rectangle in her
hand; the model cannot render legible UI, and in this video the UI is
deliberately never the point — it is always cut away from before it can be
read.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA, paying
attention to the fringe continuity — the blunt fringe exists only from shot
30 onward and must never appear before it. Keyframes first; OpenPose for the
walk down the gallery and the street walk in the final chorus; Depth for the
kitchen and the gallery interiors. 16:9 first; 9:16 for the locked-off face
shot and the bridge, which are the vertical hero cuts. Animate
conservatively: steam leaving a mug, a kettle switch popping, a curtain
lifting, a fringe being touched.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — a Tuesday

1. *"Tuesday, nothing special, coffee going cold,"* — macro of a mug on a kitchen table, a skin forming on the surface of the coffee, no steam, flat daylight, static.
2. *"My thumb above your name in the usual place,"* — her thumb hovering a centimetre above a lit blank phone screen (UI composited), held far too long, extreme close-up.
3. *"One small button and one small sound,"* — the thumb comes down once. Cut to the mug, which does not move.
4. *"And nothing at all happened to my face."* — the hero shot: a locked-off close-up of her face for the entire line, in which she does nothing at all. Hold two beats past comfortable.

### Verse 1 — the season of not doing it

5. *"I rehearsed it for a season like a speech,"* — her sitting on the edge of a bed at night mouthing something to herself, phone face-down beside her, one warm lamp.
6. *"Told my sister I would do it in the spring."* — her sister on a video call mid-sentence, unimpressed and fond (screen composited), Mahima nodding and not meaning it.
7. *"Then I'd sit up past midnight with my thumb above the glass,"* — the identical framing as shot 2, but at night, in different pyjamas, thumb hovering.
8. *"And put the phone back down and not do a thing."* — the same framing again, three quick variations with different weather in the window behind her, the phone going face-down each time.
9. *"You were never even cruel, that was the worst of it,"* — a wide of the flat at night, everything tidy, nothing broken, nobody in the frame for two seconds.
10. *"You just got quieter until the quiet was the norm."* — her at the kitchen table with a meal for one, chewing, the room silent, static medium.
11. *"I kept your tab open like a window in a storm,"* — a real window left open in heavy rain, curtain soaked and slapping the frame, nobody closing it, static.
12. *"Let the cold come in and I called that keeping warm."* — her asleep on the sofa under a coat with the window still open behind her, blue light, wide.

### Pre-chorus 1 — the unsent paragraphs

13. *"No speech today, no closing line,"* — a notes app scrolling through long unsent paragraphs (composited), moving too fast to read, macro.
14. *"No paragraph I wrote and never sent,"* — her selecting all of it and then putting the phone down without deleting anything, close-up on the hand.
15. *"Just a thumb, a quiet little sound,"* — return to the intro's kitchen framing, identical, her hand flat on the table.
16. *"And a whole year finally spent."* — a slow push on the mug, the coffee completely cold now, the light unchanged.

### Chorus 1 — the world stubbornly continues

17. *"Unfollowed, unbothered, un-yours,"* — her stepping out of her front door into an ordinary afternoon street, wide, the first exterior of the video.
18. *"And the sky did not fall down on me,"* — a plain shot of the sky above the terrace: grey-blue, uneventful, a single plane trail, static tilt up.
19. *"The kettle clicked, the bus came on time,"* — a kettle switch popping up on its own, macro, then a bus pulling in at a stop dead on the minute (board composited).
20. *"The dog next door barked at the tree."* — a small dog in a neighbouring yard barking with total conviction at a tree containing nothing, handheld, held slightly too long.
21. *"I thought that it would feel like losing,"* — her walking with a heavy tote cutting into her shoulder, tracking from the side.
22. *"It feels like setting a heavy bag down."* — she sets the tote on a low wall, rolls her shoulder once, and picks it up noticeably lighter, medium.
23. *"Unfollowed, unbothered, un-yours,"* — her walking on down the pavement, unhurried, the frame wider than any verse shot.
24. *"And nothing in the world made a sound."* — a wide of the whole street with her small in it and traffic moving normally, static, no drama.

### Verse 2 — the ordinary week

25. *"I took my coffee to the park at half past one,"* — her on a park bench with a takeaway cup, coat on, handheld, gold afternoon.
26. *"Watched a kid start a war with a pigeon and win."* — a toddler charging a pigeon across gravel and the pigeon giving ground, low angle, comic timing.
27. *"Sat there till the light went orange on the water,"* — the boating lake going amber, her out of focus in the foreground, long lens.
28. *"And nobody came to ask me where I'd been."* — her alone on the bench in a wide, people passing behind her, nobody stopping, static.
29. *"Bought a dress in a colour you would call a lot,"* — a changing-room mirror, the tangerine slip dress, her looking at it and deciding, over-the-shoulder.
30. *"Cut a fringe I am going to have to live with for a while."* — a salon chair, scissors, hair falling, then her seeing the blunt fringe and laughing once at herself, tungsten light.
31. *"Somebody said your name at dinner on the Friday,"* — a candlelit dinner table, her sister mid-sentence, the table carrying on around her.
32. *"I passed the bread and answered with a stranger's smile."* — close-up: she passes the bread, says one short sentence, smiles politely, and the conversation moves on without her.

### Pre-chorus 2 — the folded photograph

33. *"No paragraph, no closing line,"* — her at the dinner table after, coat on, phone in her lap, not looking at it.
34. *"No last look at a face I know by heart,"* — a printed photograph in her hands, the far half out of frame, only her own half visible to camera.
35. *"Just the same small sound in a different week,"* — the intro's kitchen framing once more, the same hand, the same table, a week's worth of post on it.
36. *"And a photograph with your half torn apart."* — she folds the photo in half so only she is showing and stands it on a shelf that way, macro.

### Chorus 2 — she is inside the shots now

37. *"Unfollowed, unbothered, un-yours,"* — her in the kitchen actually making the tea rather than watching the kettle, handheld, warmer.
38. *"And the sky did not fall down on me,"* — the same patch of sky as shot 18, now with her at the window in the bottom of frame.
39. *"The kettle clicked, the bus came on time,"* — her on the bus by the window, forehead not touching the glass, just sitting, medium.
40. *"The dog next door barked at the tree."* — she crouches at the fence and greets the dog, which stops barking, handheld.
41. *"I thought that it would feel like losing,"* — the tangerine dress on a hanger on a door frame, catching afternoon light, static.
42. *"It feels like setting a heavy bag down."* — her dropping the tote by the door and kicking her shoes off, wide, unposed.
43. *"Unfollowed, unbothered, un-yours,"* — her lying on the floor of the flat looking at the ceiling, arms out, entirely relaxed, overhead.
44. *"And nothing in the world made a sound."* — the flat from the hallway, her in the far room, ordinary sounds only, static wide.

### Instrumental — the flat, quietly reorganised

45. A slow pan across a shelf: the folded photograph now sits between other objects, neither hidden nor featured, and the pan does not stop on it.
46. Her moving a chair to a different wall, standing back, and leaving it there.
47. Her opening the window on purpose this time, then closing it after a minute — the answer to shot 11.
48. Fast cuts of ordinary noise: a hairdryer, a laugh at something off-camera, a phone face-up on the arm of the sofa being ignored.
49. One full bar of silence: a static wide of the empty kitchen, late golden hour crossing the floor, nobody in frame. The cut into the bridge.

### Bridge — the museum, half-rapped

50. *"Let me be honest, I was running a museum,"* — hard cut: an empty white gallery at night, Mahima in the long black coat walking in from the dark, tracking.
51. *"One exhibit, one man, and the only guide was me."* — a single framed piece on the far wall under one picture light, deliberately unreadable from this distance, wide.
52. *"Every post became a plaque, every photo a display,"* — a row of small brass plaques along an empty wall (composited), her walking past them without looking.
53. *"And I gave myself the tour at one and two and three."* — the same gallery, three times, with the light through the high windows changing to show three different nights.
54. *"I called it keeping up, I called it being kind,"* — her stopping at the exhibit, hands in coat pockets, looking up at it, from behind.
55. *"It was homework on a person who had already resigned."* — a hard tracking shot the length of the gallery ending on the picture light itself, glare.
56. *"And the truth is not dramatic, it is boring and it's plain,"* — cut to the real kitchen for one beat only: the mug, the table, nothing happening. Then back.
57. *"You don't get a lightning bolt, you get a Tuesday and some rain."* — rain on the gallery skylight, ordinary and grey, low angle.
58. *"So I didn't write a paragraph, I didn't make a scene,"* — her reaching up and switching the picture light off. The wall goes black. Static.
59. *"I just took my name off a room I'd been cleaning."* — a wide of the whole gallery in darkness, her the only thing lit, from a doorway behind her.
60. *"Not a punishment, no flex, not a quiet little war,"* — a heavy gallery door she has been holding open with her back; she steps through and lets it swing shut.
61. *"Just a door I had been holding, and I'm not holding it anymore."* — straight to camera, no transition, back in the kitchen in the grey sweatshirt, delivering the line level and unbothered as the strings arrive.

### Final chorus — the first good morning

62. *"Unfollowed, unbothered, un-yours,"* — dawn: every window in the flat open, curtains lifting, the first moving air in the video, wide.
63. *"And the sky did not fall down on me,"* — the sky again, third time, now blue-going-gold, filmed from the fire escape, tilt.
64. *"The kettle clicked, the bus came on time,"* — the kettle, the bus, the dog, three half-second reprises in daylight, all warmer than before.
65. *"The dog next door barked at the tree."* — the dog asleep in the sun instead, and she notices and smiles, handheld.
66. *"I thought that it would feel like losing,"* — her barefoot in the tangerine dress with the new fringe, crossing the flat with a coffee, tracking.
67. *"It feels like the first clean morning in a year."* — her leaning in the doorway with the light on her face and her eyes closed, medium close-up.
68. *"Unfollowed, unbothered, un-yours,"* — her walking a street she has been avoiding, past whatever used to be a landmark, without slowing down, tracking from the front.
69. *"And the quiet is not empty, it is clear."* — the widest shot of the video: the street, the sky, her small and moving through it at normal speed.

### Post-chorus — one day in one frame

70. *"Unfollowed in the morning, unbothered by the night,"* — a locked-off frame of the kitchen window from the inside, time-lapsing from early light forward.
71. *"Un-yours by the time the streetlights came on,"* — the same frame continuing, her passing through it four times doing four ordinary things.
72. *"Unfollowed, unbothered, un-yours,"* — the same frame as the streetlights outside come on, the room going amber.
73. *"And the day just carried on."* — the same frame, night, the room lit only from the street, her sitting down in the chair by the window.

### Outro — the intro, exactly

74. *"Coffee going cold on a table by the window,"* — the identical framing as shot 1: same mug, same table, same light. The phone is not in the shot.
75. *"A fringe I'm still getting used to in the glass,"* — her reflection in the dark window, touching the fringe, mildly amused by it, close-up.
76. *"Somebody will ask me and I'll tell them it went fine,"* — her looking off-camera and saying two words to someone we never see, medium.
77. *"And it will be the truth, at last."* — final shot: the mug, the table, the empty chair opposite, held until the piano stops. No text.

## 5. Edit and the challenge

Markers at: the button press in shot 3, the held face in shot 4, each
*"unfollowed, unbothered, un-yours"*, the open window in shot 11 and its
answer in shot 47, the silent bar at 49, the picture light going out at 58,
the door in 60, dawn at 62, and the last piano note. At 100 BPM a bar is
2.4 s; the bridge cuts on the half-bar to sit with the half-rapped cadence.

**The anticlimax challenge.** Post the vertical cut of shots 1–4 with
*"and nothing at all happened to my face"* on screen, and invite people to
film the two unedited seconds after they finally do the small thing they have
been putting off for a year. The bridge to-camera line in shot 61 is the
second shareable frame, and the folded photograph in shot 36 is the comment
bait.

## 6. Quality-control checklist

- Three looks in the right sections: grey sweatshirt until shot 29, tangerine dress and fringe only from shot 30 on, black coat only in the bridge
- The blunt fringe never appears before shot 30 — the single hardest continuity risk in this video
- The ex is never generated in any form, faceless or otherwise; he exists only as a folded photo, an unlit exhibit and a name said by somebody else
- The gallery is the only stylised sequence; every other frame is flat honest daylight with no fill
- Frames widen monotonically from intro to final chorus, and only the final chorus has moving air in it
- All screens, plaques and boards composited; the UI is always cut away from before it can be read
- The mug of cold coffee opens and closes the video in identical framing, with the phone present in one and absent in the other
- The last shot is locked-off and holds until the piano stops
