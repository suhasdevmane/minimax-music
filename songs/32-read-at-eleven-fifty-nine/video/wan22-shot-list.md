# Wan 2.2 Shot List — "Read at Eleven Fifty-Nine"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
90 BPM a bar is 2.67 s in a half-time feel, so verse and chorus shots run
4–6 s while the melodic-rap verse cuts roughly twice as fast.

## 1. Visual style

Two apartments on opposite sides of one city, and the distance between them.
**The split screen is the structure**: from the first pre-chorus onward her
side lives on the left and his side on the right, in identical framing every
time it returns, and it collapses into a single frame exactly once — on the
word *go* in the final chorus. Her side is warm: one lamp, a candle, a
television flicker, city amber through an open window. His side is cooler and
bluer and we never see his face. Between them the city is sodium and headlight
flare.

The rap verse breaks the pattern deliberately: no split screen, a harder
closer key on her, background falling to black, and a cutting rate about twice
everything else in the film.

| Section | Grade | Camera |
|---|---|---|
| Intro | One warm lamp, city amber, slightly too warm | Static, slow, close inserts |
| Verse 1 | Lamp, candle, television flicker, one cold clock | Static objects, close on her |
| Pre-choruses | Warm left, cool blue right, hard split line | Locked-off split screen |
| Chorus 1 | Screen light on her, then amber and blue city | Composited UI, aerial, back seat |
| Verse 2 (rap) | Hard close key, background to black, no split | Long takes to camera, fast inserts |
| Chorus 2 | Warmer and lower on her, colder and faster on the city | Fast object cuts, tracking car |
| Instrumental | Sodium street, headlight flare, one warm window | Locked-off wide, long lens |
| Bridge | Screen light, then hard hallway light only | One long take on her face |
| Final chorus | Headlights sweeping a ceiling, hall warm | Split screen collapsing to one frame |
| Post-chorus | Blue city, green screen glow, warm hall | Fast cuts on the beat |
| Outro | Hall warm, stairwell cold, meeting in a doorway | Static, held open door |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair half-pinned and coming loose, red lipstick still on from earlier and one gold hoop earring in, wearing a silk robe over a vest and shorts, composed knowing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the rap verse, harder key)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair half-pinned and coming loose, red lipstick, one gold hoop earring, wearing the same silk robe, direct challenging expression looking straight into the lens, realistic cinematic photography, consistent identity, natural skin texture

**The man on the other side of the split** — **faceless throughout**. A
shoulder, a forearm, a hand on a phone, a coat being picked up, the back of a
head in a car. He is never identified and never seen above the collar, right
through to the final frame.
> a young man, face out of frame or cropped at the jaw, dark clothing, cool blue room light

**The driver** — the back of a head and two hands on a wheel, nothing more.

There are no exes, rivals or friends on screen; the group chat exists only as
a screen. This is a two-hander in which one of the two has no face.

Objects: the **fan on the dresser**, the **candle burning crooked**, the
**microwave clock**, the **one earring in a dish**, the **door latch**, the
**lamp that keeps getting turned lower**, the **keys**, the **buzzer**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every screen in this video is composited in the edit** — the two drafts, the
read timestamp, the typing dots, the call button, the group chat, the map
route, the address message, the lift indicator and the microwave clock.
Generate phones and clocks as lit blank rectangles and overlay the UI in post.
The read timestamp is the single most important image in the film and must be
typographically exact.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima with IP-Adapter or a character LoRA; keep the male reference
deliberately faceless so the model never volunteers a face. Depth for the two
apartment interiors so the split-screen halves keep consistent geometry every
time they return.

**Build the split screen as two separately generated plates**, composited on a
hard vertical line in the edit. Do not ask the model for a split-screen image;
it will blend the two rooms. Each half must be framed for a nine-by-sixteen
crop of a sixteen-by-nine frame so the halves can also be posted alone.

The rap verse is the one section that needs sustained performance rather than
a moving still: shoot or generate it as two or three long takes at the full
verse length and cut the inserts around them, rather than one clip per bar.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s; the rap-verse inserts are 1–2 s.

## 4. Scene per lyric line

### Intro — eleven fifteen

1. *"Eleven fifteen and this room is too warm"* — a fan on a dresser turning slowly and moving nothing at all, close, warm lamp light, held.
2. *"Fan on the dresser doing nothing at all."* — a window open on a city that is still awake, curtain not moving, amber outside, static.
3. *"Green dot went gray about an hour ago"* — a phone face down on a bedspread, one edge lit by the lamp, macro.
4. *"And I'm not checking, but I know."* — Mahima on the far side of the bed, deliberately not looking at the phone three feet away, medium, static.

### Verse 1 — the message written twice

5. *"I wrote the whole thing twice and I deleted the nice one"* — two drafts on a screen, one long and one short (composited), the long one selected and deleted.
6. *"Sent the flat one instead like it cost me nothing."* — her face as she sends it, entirely composed, close-up, screen light off-frame.
7. *"One earring off, one earring still in, and my lipstick on"* — one gold hoop in a dish beside the bed; the other still in her ear, two inserts on the beat.
8. *"Show I'm not watching and a candle going wrong."* — a television playing to nobody; a candle burning crooked down one side, two static objects.
9. *"I'm not waiting, I'm just up, that's a difference, that's a line"* — her walking across the room doing something entirely unnecessary with a cushion, medium.
10. *"And the clock on the microwave said eleven twenty-nine."* — a green microwave clock reading eleven twenty-nine (composited), the only cold light in the frame, macro.

### Pre-chorus 1 — the stalemate

11. *"Tick, tick, tick, and the room's getting small"* — split screen for the first time: her side left with the lamp, his side right cooler and bluer, both people holding still.
12. *"Tick, tick, tick, and I'm not gonna call."* — the same split, both halves now with a phone in frame, neither being used.
13. *"I could put it down, I could turn off the light"* — her thumb hovering over a call button and not pressing it (composited), full frame, no split.
14. *"But you know what you're doing, and so do I."* — the lamp switch under her other hand, also not pressed, macro; back to the split on the last beat.

### Chorus 1 — the read receipt

15. *"You read it at eleven fifty-nine, and I know you're on your way"* — a read timestamp appearing under a message (composited), held for a full beat, full frame.
16. *"Dots on the screen for a minute and you still didn't say."* — three typing dots appearing, holding, and stopping, macro, no cut for the whole line.
17. *"Nine miles and a river and a driver who don't know"* — aerial of a river with a bridge across it, headlights crossing, night, slow drift.
18. *"But you read it at eleven fifty-nine, and that means go."* — a car back seat, a driver's head and hands on a wheel, a faceless passenger's forearm on the door.
19. *"Don't type it, don't send it, don't call"* — her setting the phone down deliberately screen-up on a table and walking out of frame.
20. *"Door's on the latch and the lamp turned down small."* — a door latch flipped over, close; then a lamp dial turned down two clicks.
21. *"Midnight's a minute and you're wasting my time"* — her at the window with the city behind, not looking down at the street, medium wide.
22. *"You read it at eleven fifty-nine."* — the read timestamp again, tighter, held to the end of the section.

### Verse 2 — the melodic rap

23. *"Eleven forty and I'm not checking, I'm just holding it"* — Mahima sideways in an armchair, phone face down on her knee, straight to camera, hard close key, black behind.
24. *"Screen down on my knee like I'm not the type to notice it."* — the same take continuing, her hand flat on the back of the phone, not turning it over.
25. *"You typed, and you stopped, and you typed, and you stopped again"* — insert: dots appearing and stopping, three times, cut on each stop, one second each.
26. *"Three little dots doing more to me than most men."* — back to the long take, one raised eyebrow, the best single bar in the video, held.
27. *"I know the game, I wrote the second half of the rules"* — insert: a group chat scrolling past too fast to read (composited), one second.
28. *"Taught the whole group chat how to leave a man on cool."* — the long take, her counting something off on two fingers without explaining it.
29. *"But my heart's doing eighty in a thirty-mile zone"* — insert: a speedometer needle climbing in a moving car, one second, then a hard cut back.
30. *"And the loudest thing in this apartment is my phone."* — the phone lighting the whole room for half a second and going dark again, wide.
31. *"So say it or don't, but the minute hand is mine"* — the long take, her leaning forward into the lens for the first time.
32. *"And the minute hand is sitting on eleven fifty-nine."* — the microwave clock again, now reading eleven fifty-nine (composited), macro, held.

### Pre-chorus 2 — the same stalemate, later

33. *"Tick, tick, tick, and the room's getting small"* — reuse shot 11's split-screen framing exactly; only the clocks and the light level have changed.
34. *"Tick, tick, tick, and I'm not gonna call."* — the same split; a coat is now in frame on his side that was not there before.
35. *"I could put it down, I could turn off the light"* — her lamp turned lower again, one click, macro.
36. *"But you know what you're doing, and so do I."* — the split with both sides a stop darker than the first time, held.

### Chorus 2 — quietly getting ready

37. *"You read it at eleven fifty-nine, and I know you're on your way"* — a candle being straightened, fast, and her face denying that she did it.
38. *"Dots on the screen for a minute and you still didn't say."* — a car pulling out of a parking space, wheels turning, night street.
39. *"Nine miles and a river and a driver who don't know"* — a bridge approach seen through a windshield, wipers off, lights streaking.
40. *"But you read it at eleven fifty-nine, and that means go."* — a meter running on a dash (composited), the numbers climbing, macro.
41. *"Don't type it, don't send it, don't call"* — her checking her reflection in a dark window and immediately looking away from it.
42. *"Door's on the latch and the lamp turned down small."* — the latch again and the lamp again, both already done, the frame moving faster than she is.
43. *"Midnight's a minute and you're wasting my time"* — a wide of her whole apartment, warm and low and ready, with her standing in the middle of it doing nothing.
44. *"You read it at eleven fifty-nine."* — the split screen returning for one beat with his side now empty, the coat gone, and holding.

### Instrumental — two cities, one bridge

45. The ticking chop over a locked-off wide of the empty street outside her building, nothing moving, held.
46. A car crossing a bridge on a long lens, headlights flaring into the glass, slow.
47. Her at the window from behind, city beyond, not looking down at the street.
48. The back of the driver's head and two hands on a wheel, close, streetlights passing over them.
49. A hard drop to one bar of black frame with only room tone before the bridge.

### Bridge — the reply that is not words

50. *"Then it came through, and it wasn't even words"* — a phone lighting up on a table with an address and a time on it and nothing else (composited), held long.
51. *"Just a street and a number and a car at the curb."* — her whole face changing in one unbroken take, no cut, the only shot in the film with no camera move at all.
52. *"And I stood in the hallway with my keys in my fist"* — her in the hallway with keys in her fist and nowhere to go, hard overhead hall light, wide.
53. *"And every clever thing I had went off the list."* — her looking at the keys, working out that she is not the one travelling, close.
54. *"So I'm done playing chicken and I'm done playing cool"* — her putting the keys down slowly on a hall table, macro, one beat.
55. *"I'll say the whole thing when I'm looking at you."* — her face in hard hallway light, unflattering and completely honest, the most exposed frame in the video.

### Final chorus — the split collapses

56. *"You read it at eleven fifty-nine, and I know you're on your way"* — split screen, both halves, her left and a car interior right.
57. *"Dots on the screen for a minute and you still didn't say."* — the split still holding, headlights beginning to fill the right half.
58. *"Nine miles and a river and a driver who don't know"* — the split with the right half now almost entirely headlight glare.
59. *"But you read it at eleven fifty-nine, and that means go."* — **the split collapses into one frame on the word go**: headlights arriving in the street four floors below her window, seen from her window, single full frame.
60. *"No more games, no more almost, no more small"* — headlights sweeping across her ceiling as the car stops below, wide, static.
61. *"Just headlights on the street and your hand on my wall."* — a faceless hand flat against the wall of her hallway from the far side of the door, close.
62. *"Midnight came and went and I'm still on the line"* — her back against the inside of the front door, listening to a lift, medium.
63. *"You read it at eleven fifty-nine."* — the read timestamp one last time, full frame, held to the end of the section.

### Post-chorus — the countdown

64. *"Eleven fifty-nine, eleven fifty-nine"* — two headlights crossing a bridge, long lens, one second.
65. *"Two lights on the bridge and a green line."* — a green route line moving on a map (composited), one second.
66. *"Eleven fifty-nine, eleven fifty-nine"* — a lift floor indicator climbing (composited), one second per number.
67. *"Don't say sorry, say you're outside."* — her standing in the middle of her own hallway doing absolutely nothing, wide, held.

### Outro — twelve oh four

68. *"Twelve oh four, and the buzzer goes off"* — an intercom buzzer sounding, close, her hand nowhere near it yet.
69. *"I don't fix my hair and I don't check the clock."* — her hand starting toward her hair and stopping halfway, close.
70. *"I read you, you read me, and neither of us lied"* — the microwave clock reading twelve oh four (composited) with her out of focus behind it, not looking at it.
71. *"Eleven fifty-nine."* — final shot: the front door opening from the inside, warm hall light spilling into a cold stairwell, nobody stepping through it yet. Locked off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first split screen, each read timestamp, the start and end of
the rap verse, the address message, the split collapsing on *go*, the buzzer,
and the open door. At 90 BPM a bar is 2.67 s in half-time; the rap verse cuts
roughly twice as fast as everything around it, which is the whole point of it.

**The split-screen challenge.** Both halves of every split are framed so they
can be posted alone as vertical clips, which makes the duet format native:
post her half of the pre-chorus and invite people to film the other side.
The single shareable frame is shot 15 — a read timestamp appearing and being
held for a full beat — captioned *"and that means go."* The clip is shot 26,
one bar, one long take: *"three little dots doing more to me than most men."*

## 6. Quality-control checklist

- The man is faceless in every frame, including the final one; no shot cheats above his collar
- Split screen is a hard vertical line, identical framing every time it returns, and collapses exactly once, on *go* in shot 59
- Her side is always warmer than his, and her lamp is one click lower in each successive pre-chorus and chorus
- The rap verse has no split screen, a harder key, black falloff and roughly double the cutting rate
- Every screen, clock, timestamp and map is composited; the read timestamp is typographically exact and never model-generated
- The candle is crooked from shot 8 onward and straightened in shot 37; the earring stays single all night
- No image from a night-scrolling heartbreak video: no phone-glow-on-face framing, no story views, no notification lists — this is a flirtation, not a breakup
- The last shot is locked off on an open door with nobody in it and holds through the fade
