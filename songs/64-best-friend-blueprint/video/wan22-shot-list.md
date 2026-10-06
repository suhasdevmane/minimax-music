# Wan 2.2 Shot List — "Best Friend Blueprint"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Eighty-one entries. Timestamps come from the rendered WAV; cut on
the sung line. This is an uptempo song: at 118 BPM a bar is 2.03 s, so most
shots run 2–3 s, the choruses cut on the bar and the post-chorus cuts every
half bar.

## 1. Visual world

Nine years of one friendship, shot entirely in real rooms and real cars. There
is no glamour grade anywhere: kitchens are lit by the light that is actually in
them, the car is lit by its own dashboard, and the only lighting decision that
repeats is **the open fridge door**, which is the key light for every chorus.
Three recurring set-ups carry the whole video and must be framed identically
every time they appear: the **overhead kitchen table**, the **fridge-light
kitchen dance**, and the **head-on clap routine against a plain wall**. Years
pass by changing hair, phones and clothes inside those same three frames, never
by changing the camera.

| Section | Grade | Camera |
|---|---|---|
| Intro | One warm pendant, blue night beyond | Locked-off overhead |
| Verse 1 | Practical bedroom lamps, warm and messy | Handheld, quick |
| Pre-choruses | Hallway backlight, gold edge, silhouette | Low angle, static |
| Choruses | Open fridge door as the only key | Handheld, wide, in the room |
| Post-choruses | Flat and even, no grade | Head-on locked-off |
| Verse 2 | Sodium parking lot, cold silent days, dash green | Static, then in-car |
| Instrumental | Dashboard green, headlights, one white forecourt | Slow, in-car |
| Bridge | Pre-dawn blue through a windshield | Locked-off two-shot |
| Final chorus | Every light in the apartment on | Handheld, crowded |
| Outro | The same pendant, dimmed, first grey light | Locked-off overhead |

## 2. Character bible — paste into every prompt

**Mahima** (present day)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly unbrushed, minimal makeup, wearing an oversized cream knit and sleep shorts, open unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (out, the chorus and the bar)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair straightened, bold lip and sharp eyeliner, wearing a black slip dress and a leather jacket, bright determined expression, realistic cinematic photography, consistent identity

**Mahima** (nineteen, the earliest clap-routine cuts)
> Same female protagonist Mahima, young woman of about nineteen, expressive dark eyes, oval face, long dark wavy hair with a blunt fringe, heavy eyeliner, wearing a band tee and a zip hoodie, grinning expression, realistic cinematic photography, consistent identity

**Priya** — the best friend, the second lead, on screen almost as much as Mahima.
> Same female character Priya, young woman in her mid-twenties, warm brown eyes, round face, short dark curly hair pushed back with a headscarf, wearing a mustard oversized shirt over a white tee and jeans, calm amused expression that does not change under pressure, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — faceless throughout: a shoulder walking away between two cars, a hand on a car roof, a name lighting a phone. Never a clear face, never in the same frame as Priya.

**The party crowd** (final chorus and last post-chorus) — fifteen friends of
mixed ages, faces allowed, all clearly people who have been in this kitchen
before. Nobody in this video is styled as cool.

Objects that recur: the **single charging cable** between two phones, the
**carrier bags of snacks**, the **sour candy** passed sideways in the car, the
**confiscated phone**, the **foil-covered plate**, and the **small old car**,
which is the same car in every year and visibly worse in each one.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, group chat names, the eleven days of empty notifications,
the fridge photographs and the handwritten card are composited in the edit.**
Generate phones as lit blank rectangles and the card with its writing turned
away from camera. The eleven-day silence is told entirely in composited UI, so
it has to be designed rather than generated.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Priya in one with IP-Adapter or a character
LoRA each; keep the ex's reference deliberately faceless. **OpenPose is
essential for the clap routine**, which appears in nine locations across nine
years and must be the same four moves every time — capture one real reference
performance and pose-condition every version off it. Depth for the kitchen,
which is small, cluttered and reflective. The fridge-light key is easiest done
practically: shoot the plate with a real open fridge rather than asking the
model to invent the falloff. 16:9 first; 9:16 for the kitchen dance and the
clap routine, which are natively vertical. Animate in short bursts: one clap
bar, one bag emptying, one phone sliding across a counter.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–3 s; post-chorus shots 1 s.

## 4. Scene per lyric line

### Intro — one charger

1. *"Nine years, two cities and a group chat with a name"* — locked-off overhead of a kitchen table at night: two phones, two mugs, one charging cable between them, one warm pendant above.
2. *"Three phones, one charger, and a car that barely runs"* — macro on the cable splitting to two phones, both at low battery (composited), a third phone dead beside them.
3. *"I have never had to explain myself to you"* — a two-shot across the table, both of them looking at their phones, neither talking, entirely comfortable.
4. *"Not one time, not once"* — through the window behind them: a small old car on the driveway with its interior light on and one door open.

### Verse 1 — snacks as first aid

5. *"You show up with snacks like it's a medical emergency"* — Priya on a doorstep at night holding two carrier bags up like evidence, deadpan, hard porch light.
6. *"Sour candy and a bag of something fried"* — overhead of a duvet as the bags empty across it in one continuous move, everything landing on the beat.
7. *"You don't ask me if I'm fine, you just start unpacking"* — Priya's hands sorting the snacks into piles without looking up, Mahima out of focus behind her.
8. *"And you put the kettle on and let me cry"* — a kettle switch, steam rising past a window, then Mahima crying and laughing at the same time, close-up.
9. *"You tell me the truth in the exact right order"* — Priya sitting on the end of the bed with both hands out, delivering something carefully, one finger then two.
10. *"The nice part first, then the part I need to hear"* — Mahima's face taking it: relief, then a flinch, then a nod, one continuous close-up.
11. *"You said, that dress is not the problem, and you're right"* — a bedroom mirror, two dresses held up against a body, Priya's single raised eyebrow in the reflection.
12. *"And I put on the other one and we got out of there"* — the front door slamming from outside, both of them already halfway down the path, handheld, fast.

### Pre-chorus 1 — the measuring

13. *"Every friend I've ever made, I measured against you"* — macro on pencil marks up a door frame, the way parents mark height, several low and one much higher, none labelled.
14. *"And every single one of them came up short"* — a hand flattening on top of a head at one of the low marks, then dropping away.
15. *"You're not the bar, you're the whole entire building"* — low angle on Priya standing in a doorway, shot to look enormous, one hand on the frame, backlit gold.
16. *"You're the reason I know what a person's worth"* — Mahima looking up at her from floor level, straight-faced, no joke on her face at all.

### Chorus 1 — fridge light

17. *"You're the blueprint, best friend, everyone else is a copy"* — the kitchen dance: both of them going for it badly in a small kitchen, open fridge door as the only key, socks on linoleum.
18. *"Cheap ink, wrong size, and the second page is gone"* — Priya on a chair with a wooden spoon, Mahima spinning past her, wide, handheld.
19. *"You take my phone at midnight, then the keys, then the wheel"* — a hand lifting a phone off a table and posting it into a coat pocket, macro.
20. *"You tell me what I look like when I won't say how I feel"* — a set of keys sliding the length of a counter into a waiting hand.
21. *"Everybody wants a love song, I'm not writing one"* — a hand on a steering wheel at night, dashboard green, the other hand out the window.
22. *"This one's for the girl who drove four hours in the dark"* — an empty interstate through a windshield at speed, wipers going, nobody else on it.
23. *"Say it in a toast, say it on a card"* — back in the kitchen, both of them shouting the line into each other's faces from six inches away.
24. *"You're the blueprint, best friend, everyone else is a copy"* — a wide of the whole kitchen, fridge open, two people, absolute chaos, held.

### Post-chorus 1 — the routine

25. *"Blueprint, blueprint, everyone else is a copy"* — head-on locked-off two-shot against a plain wall, both doing the four-move clap routine, Priya deliberately one beat behind.
26. *"Blueprint, blueprint, nobody else got it right"* — the same routine on a beach at nineteen, one bar, sunburn and bad hair.
27. *"Blueprint, blueprint, everyone else is a copy"* — the same routine in an elevator, one bar, both in work clothes.
28. *"You're the original, honey, I got the only one"* — the same routine in a parking garage at night, one bar, coats on, breath visible.

### Verse 2 — the fight

29. *"You told me the truth about him in a parking lot"* — two figures between parked cars under sodium light, one of them a faceless shoulder walking away, static wide.
30. *"And I didn't speak to you for eleven days"* — eleven fast cuts of the same phone lock screen with no new messages (composited), one per day, the room light changing behind it.
31. *"You never chased me down, you left the door unlocked"* — a front door pushed and swinging open on its own, nobody there, cold hallway light.
32. *"And you saved me half of everything anyway"* — a foil-covered plate on a counter, the foil peeled back on exactly half a meal, macro.
33. *"Then I called you from a stairwell, you picked up on the first ring"* — a concrete stairwell at night, Mahima sitting three steps up, phone to her ear, wide.
34. *"You didn't say I told you so, you said, I'm in the car"* — Priya already reaching for keys with the phone wedged under her jaw, cut on the first ring.
35. *"Four hours in the dark with a bag of sour candy"* — in-car: a bag of sour candy passed sideways without either of them looking, dashboard green.
36. *"And you never once asked me how I let it get that far"* — a locked-off two-shot of the car interior, both facing forward, neither speaking, held four seconds.

### Pre-chorus 2 — the archive

37. *"Every love I've ever lost, I got over in your kitchen"* — a slow pan across a fridge door covered in nine years of photographs of the two of them (all composited).
38. *"And every version of me, you have kept them all"* — the pan continues and the hair, phones and clothes change left to right across the door.
39. *"You're not a chapter in the book, you're the spine"* — the overhead kitchen table from shot 1, with a different crisis on it in four fast cuts, one bar each.
40. *"And I would sign up for the whole nine years again"* — the same table, present day, empty except for two mugs, static.

### Chorus 2 — the years in one frame

41. *"You're the blueprint, best friend, everyone else is a copy"* — the kitchen dance again, identical framing, and both of them are nineteen.
42. *"Cheap ink, wrong size, and the second page is gone"* — same frame, same position, and they are twenty-two.
43. *"You take my phone at midnight, then the keys, then the wheel"* — a bar sink, hair held back with one hand, a glass of water arriving without being asked for.
44. *"You tell me what I look like when I won't say how I feel"* — a phone taken firmly out of a hand at a table, the hand not resisting, macro.
45. *"Everybody wants a love song, I'm not writing one"* — same kitchen frame, present day, and the two of them are laughing too hard to dance.
46. *"This one's for the girl who drove four hours in the dark"* — reuse shot 22, longer, the sky starting to go grey at the top of the windshield.
47. *"Say it in a toast, say it on a card"* — two glasses knocked together hard enough to spill, close-up, nobody caring.
48. *"You're the blueprint, best friend, everyone else is a copy"* — the full kitchen wide again, fridge open, both of them mid-air.

### Post-chorus 2 — faster

49. *"Blueprint, blueprint, everyone else is a copy"* — the wall routine again, present day, both perfectly in time for the first time.
50. *"Blueprint, blueprint, nobody else got it right"* — the routine in a laundromat, one bar, sitting down.
51. *"Blueprint, blueprint, everyone else is a copy"* — the routine in a supermarket aisle, one bar, one of them still holding a basket.
52. *"You're the original, honey, I got the only one"* — the routine in a hotel corridor at three in the morning, then both collapsing against the wall laughing.

### Instrumental — the drive

53. Wing mirror at speed, an indicator ticking, empty interstate behind, dashboard green.
54. The bag of sour candy passed sideways again, neither of them looking, macro.
55. A service-station forecourt at two in the morning under one brutal white light, the car alone in it.
56. The clap breakdown staged for real: both of them clapping the routine on the hood of the parked car under that light, full body, wide.
57. Hard half-time drop: the car pulling out of the forecourt, taillights, the light going out behind it.

### Bridge — the other way round

58. *"Last year it was your turn and I got to hold the door"* — the exact drive framing from shot 36, reversed: Mahima at the wheel, Priya in the passenger seat.
59. *"I drove the four hours and I didn't say a thing"* — Priya's forehead against the passenger window, eyes open, pre-dawn blue.
60. *"And you looked at me like no one ever did that before"* — Priya turning her head to look at Mahima and holding it, the shot the whole video is built toward.
61. *"And I thought, so that's what she's been doing all along"* — Mahima's eyes flicking sideways and back to the road, close-up, no reaction played.
62. *"If this is the great romance of my life, then fine"* — a wide of the car small on an empty road with the sky going from blue to gold behind it.
63. *"Nine years, no contract, and nobody had to sign"* — the car pulling into a driveway at dawn, both doors opening at the same time.

### Final chorus — the whole room

64. *"You're the blueprint, best friend, everyone else is a copy"* — the kitchen dance frame with fifteen people in it, every light in the apartment on, fridge included.
65. *"Cheap ink, wrong size, and the second page is gone"* — the crowd singing the line straight at the two of them, handheld from inside the group.
66. *"I take your phone at midnight, then the keys, then the wheel"* — Mahima taking Priya's phone this time and pocketing it, the reverse of shot 19, macro.
67. *"I tell you what you look like when you won't say how you feel"* — Mahima holding Priya's face in both hands and saying something we do not hear.
68. *"Everybody wants a love song, so here's the only one"* — a toast raised by fifteen arms at once, glasses everywhere, low wide.
69. *"For the girl who drove four hours and the girl who drove them back"* — a homemade card held up with the writing turned away from camera (composited), Priya's face behind it.
70. *"Say it in a toast, say it on a card"* — the two of them nose to nose in the middle of the crowd, shouting the line, everyone else out of focus.
71. *"You're the blueprint, best friend, everyone else is a copy"* — the widest shot in the video: the whole kitchen, everyone, fridge still open.

### Post-chorus 3 — everybody

72. *"Blueprint, blueprint, everyone else is a copy"* — the head-on wall routine with fifteen people in it, the two originals dead centre and in perfect time.
73. *"Blueprint, blueprint, nobody else got it right"* — one guy getting it completely wrong, one bar, delighted with himself.
74. *"Blueprint, blueprint, everyone else is a copy"* — two people colliding on move three, one bar.
75. *"Blueprint, blueprint, and I'm keeping you for life"* — an older woman doing it perfectly, one bar, nobody more surprised than her.
76. *"You're the original, honey, I got the only one"* — back to the full wall shot, everybody finally in time, the two originals looking at each other.
77. *"Blueprint, blueprint, everyone else is a copy"* — the room breaking apart into noise, handheld, ending on Priya laughing with her head back.

### Outro — the same table

78. *"Nine years, two cities and a group chat with a name"* — the overhead kitchen table from shot 1, matched exactly, the party over, two mugs, one charger.
79. *"Three phones, one charger, and a car that finally died"* — both of them asleep with their heads down on the table, phones dark, cable still connecting them.
80. *"I have never had to explain myself to you"* — the driveway through the window: the same small car with a tarp over it and grass growing round the tires.
81. *"And I'm not about to start tonight"* — final shot: the overhead table again, first grey light at the window, the pendant switching off, both of them still asleep, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first clap, the bags emptying, the fridge opening for chorus
one, each post-chorus routine, the eleven-day cut sequence, the first ring,
the instrumental, the head turn in shot 60, the crowd entering, and the
pendant going out. At 118 BPM a bar is 2.03 s; verses cut on the line,
choruses on the bar, post-choruses every half bar.

**Pacing warning for the edit.** This is an uptempo song at 759 sung words.
If the render paces faster than the 140 words-per-minute guard estimate, the
track will come in nearer five minutes than five and a half and the last
post-chorus will run shorter than the shot count assumes. Cut shots 72–77 to
one bar each and drop shot 74 first if the audio runs short.

**The shareable cut** is shots 17–24, vertical: the fridge-light kitchen dance
with *"everybody wants a love song, I'm not writing one"* on screen.

**The challenge — the routine.** Four moves, one bar, one of you a beat behind
on purpose. Post it with your best friend and caption it with the hook. The
nine-locations montage is the format: film the same four moves everywhere you
two go for a year and cut them together.

## 6. Quality-control checklist

- Three looks for Mahima in the right sections; Priya's look never changes except for hair length across the years, which is how the audience reads time
- The ex is never a face and never appears in a frame with Priya
- The three repeating set-ups — overhead table, fridge-light kitchen, head-on wall — are framed identically every single time, including lens and height
- The clap routine is the same four moves in all nine locations, pose-conditioned off one real reference performance
- The fridge is the only key light in every chorus until the final one, where every light in the apartment is on
- The small old car is the same car in every year and visibly worse each time, ending under a tarp
- All screens, the group chat name, the eleven days of empty notifications, the fridge photographs and the card composited; no model-generated text anywhere
- The last shot is locked-off, matches shot 1 exactly, and the pendant goes out before the audio does
