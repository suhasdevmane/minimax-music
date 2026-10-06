# Wan 2.2 Shot List — "Kids on Bicycles"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
92 BPM a bar is 2.6 s, so most shots are 4–6 s — this video holds shots far
longer than the uptempo songs in the catalogue, and should.

## 1. Visual style

One suburban dead-end street across one summer, shot on the assumption that
the camera is a kid: knee height, close to the tarmac, always slightly
behind the action. The summer is hard sun, deep green, blown highlights and
real lens flare — no filter, no haze, nothing that looks like a memory
effect. The **one** exception is the bridge, which is present-day grey spring
rain seen through a windscreen, and it must look like a completely different
film. The final chorus returns to the summer without apologising for it and
is the warmest gold in the video. Nothing is slowed down except two shots in
the instrumental.

| Section | Grade | Camera |
|---|---|---|
| Intro | Hard early sun, deep green, blown tar highlights | Macro and one wide, static |
| Verse 1 | Overhead midday, short shadows, concrete glare | Knee height, handheld |
| Pre-chorus 1 | Late afternoon, long shadows, gold beginning | Handheld, following |
| Choruses | Golden hour into blue, streetlights just coming on | Front-facing knee height, tracking |
| Verse 2 (plan) | Warm, low, backlit | Static, kerb level |
| Verse 2 (truck) | Overcast, then dusk — the only unsunlit summer scene | Static, patient, wide |
| Pre-chorus 2 | Flat grey, wet concrete, warm windows | Static |
| Instrumental | Flare, spokes, overhead | Slow motion on two shots only |
| Bridge | Grey spring daylight, rain on glass, cold white LED | Static, in-car, long holds |
| Final chorus | Brightest warmest gold of the video | Crane and tracking, wide |
| Post-chorus | Gold into blue | Fast cuts |
| Outro | Last gold of the day, long shadows | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (present day, bridge only)
> Same female protagonist Mahima, young woman in her late twenties, expressive dark eyes, oval face, long dark wavy hair tied back, no makeup, wearing a plain olive jacket over a t-shirt, sitting in a parked car with both hands still on the wheel, quiet unreadable expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima at nine** (the whole summer)
> Same protagonist as a nine-year-old girl, the same expressive dark eyes and oval face aged down, dark wavy hair in a high ponytail with a fringe, a graze on one knee, wearing a faded red t-shirt, cut-off denim shorts and scuffed trainers, sunburnt nose, wide open expression, realistic cinematic photography, consistent identity, natural skin texture

Build the child look from the adult reference stills aged down, not from a
generic child face — the audience has to recognise them as the same person
in the bridge without being told.

**The other three** — a boy with a shaved head and a too-big BMX, a girl with
glasses taped at one hinge and the best bike, and a smaller boy who is
always last. They have faces; they are friends, not exes, and the video
belongs to all four of them.

**The parents** — never a full face: a man in a doorway from the chest down
whistling, a mother's arm holding a screen door, a hand on a car window from
the inside. They are the boundary of the world, not characters in it.

Objects, and they carry the video: the **playing card clipped to a fork with
a clothes peg**, the **plank-and-brick ramp**, the **garden hose**, the
**chalk**, the **corner streetlight** (warm orange in the summer, cold white
LED in the bridge), the **removal truck**, the **fourth bike**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All house numbers, street signs, the removal truck's livery, chalk writing
and any screen are composited or left blank in the edit.** Generate the truck
unlettered and the chalk as drawings rather than words; the model cannot
render legible text, and legible text would date and place a street that
should belong to everybody.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock the adult Mahima with IP-Adapter or a character LoRA, then build a
second LoRA for the nine-year-old from aged-down stills of the same face; the
identity match between shot 60 and the summer is the single most important
technical job in this video. Lock the other three children too — a video
about four friends fails instantly if one of them changes face between
shots. **OpenPose is essential** for every riding shot: children on bicycles
are the hardest thing here, and hands on and off handlebars need a pose
reference or the model produces four-armed riders. Depth for the
front-facing four-abreast frame and the overhead. 16:9 first; 9:16 for the
card-in-the-spoke macro and the four-abreast ride, which are the shareable
cuts. Keep clips short: one pedal cycle, one ramp attempt, one sprinkler
pass. Riding sequences are more reliable assembled from three two-second
clips than generated as one long move.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s.

## 4. Scene per lyric line

### Intro — the street wakes up

1. *"Cut grass and hot tar and a hose in the sun"* — a sprinkler ticking across a lawn in macro, then heat shimmer over black tar, two cuts, hard early sun.
2. *"Screen door banging and the day just begun"* — a screen door swinging shut on its spring, a mother's arm withdrawing, static, no face.
3. *"Somebody's mother calling somebody in"* — a wide of the empty street with four bikes leaning on four different fences, a voice off frame, nobody in shot.
4. *"And the whole street waking up again"* — four front doors opening at almost the same moment in one wide frame, four kids coming out, static.

### Verse 1 — the ramp

5. *"We built a ramp from a plank and a brick"* — a plank being balanced on a stack of bricks on a driveway, four pairs of hands, knee height.
6. *"Argued an hour over who would go quick"* — four nine-year-olds arguing with their entire bodies, medium wide, handheld, nobody backing down.
7. *"I went last and I went too slow"* — Mahima at nine setting off toward the ramp with visible reluctance, tracking from behind.
8. *"Took the gravel on the drive below"* — the front wheel stalling halfway up the plank, then a knee and gravel in macro, two cuts, unglamorous.
9. *"Nobody cried and nobody told"* — her face doing an excellent job of not crying, close-up, held longer than comfortable.
10. *"Ran it under the hose and called it cold"* — the knee held under a running garden hose, sun through the spray, a small rainbow, macro.
11. *"The dog two doors down knew all four of us by sound"* — a dog behind a chain-link fence going off at a specific freewheel sound, medium, funny.
12. *"And the ice cream truck was the only clock in town"* — four heads turning in unison at a chime two streets away, then four bikes leaving frame at speed, two cuts.

### Pre-chorus 1 — chalk, sprinkler, the whistle

13. *"Chalk on the driveway and a sprinkler on the lawn"* — chalk drawings on concrete and filthy hands, macro; then four kids running fully dressed through a sprinkler, wide.
14. *"Two dollars between four of us and the whole day long"* — coins counted out on a kerb, four heads bent over them, overhead close.
15. *"Somebody's father whistling at the door"* — a man in a doorway from the chest down, two fingers in his mouth, whistling, static.
16. *"And we knew what it meant and we rode one more"* — four kids hearing it, looking at each other, and deliberately setting off for one more lap, medium wide.

### Chorus 1 — the ride

17. *"We were kids on bicycles, racing the streetlights home"* — four bikes abreast down the middle of an empty road at dusk, filmed from the front at knee height, tracking backwards, the frame of the video.
18. *"Handlebars and hollering, and nobody rode alone"* — four faces mid-shout, filmed one after another in a single pan across the line.
19. *"Cards in the spokes making engines out of air"* — a playing card clipped to a fork with a clothes peg, macro, ticking against the spokes.
20. *"Nine years old and the whole wide world was four streets square"* — an overhead of the four streets, the whole world, four small riders crossing it.
21. *"We were kids on bicycles, and the only rule we knew"* — the corner streetlight beginning to warm from dull orange toward full, macro, the light itself.
22. *"Was be up on the porch by the time the yellow came through"* — four bikes dropped on a lawn and four kids hitting a porch at a dead run, wide, comic urgency.
23. *"We didn't know it was the best of it, we just knew it was ours"* — the four of them on the porch steps out of breath, looking back at the street, medium.
24. *"We were kids on bicycles, racing the streetlights home"* — hands off handlebars for exactly two seconds, arms out, front-facing knee height, the shot everyone will screenshot.

### Verse 2 — the plan, and the truck

25. *"We swore we'd buy four houses in a row"* — four kids sitting on a kerb pointing at four different houses, static, kerb level, backlit.
26. *"Cut a gate in every fence so we could go"* — a finger drawing a gate in the air against a fence panel, then chalk marking the exact spot, two cuts.
27. *"Through each other's back yards for the rest of our lives"* — a low tracking shot through three connected back gardens, washing lines, a paddling pool, a shed.
28. *"And nobody laughed at it, nobody thought twice"* — four faces in a row, all of them entirely serious, slow pan, held.
29. *"Then a moving truck came in the last week of June"* — a removal truck on the street with its ramp down, unlettered, overcast light, static wide, the grade change lands here.
30. *"And a bike went in the back of it too soon"* — a small bike lifted into the truck and laid on its side among boxes, close-up, no faces.
31. *"We rode three abreast and the gap was loud"* — the front-facing knee-height frame again with three riders and an obvious empty space on the left, tracking, silent.
32. *"And nobody said it, and we rode round and round"* — the same corner taken again and again as the light fails, three or four repetitions cut together, wide.

### Pre-chorus 2 — the first rain

33. *"Chalk washing off in the rain on the lawn"* — chalk drawings running in rainwater down a driveway, macro, the colours going into the gutter.
34. *"Three bikes on the corner and a fourth one gone"* — three bikes leaning on a wet corner with a clear space beside them, static, flat grey.
35. *"Somebody's father whistling at the door"* — the same man, same doorway, same whistle, framed identically to shot 15.
36. *"And we came in early and we didn't know what for"* — three kids going straight inside without arguing, which has never happened, wide, warm windows behind grey.

### Chorus 2 — the ride with the space in it

37. *"We were kids on bicycles, racing the streetlights home"* — the four-abreast frame reused with three riders, dusk, cooler than chorus one.
38. *"Handlebars and hollering, and nobody rode alone"* — three faces mid-shout in the same pan as shot 18, and the pan continues past an empty lane.
39. *"Cards in the spokes making engines out of air"* — reuse shot 19, tighter, the card frayed now.
40. *"Nine years old and the whole wide world was four streets square"* — the overhead again, three riders, the same four streets.
41. *"We were kids on bicycles, and the only rule we knew"* — the streetlight coming on, this time already lit when the shot begins.
42. *"Was be up on the porch by the time the yellow came through"* — three pairs of shoes on a porch, static, the fourth space in frame.
43. *"We didn't know it was the best of it, we just knew it was ours"* — the three of them on the steps, nobody talking, medium, held long.
44. *"We were kids on bicycles, racing the streetlights home"* — three riders, hands still on the handlebars this time, front-facing knee height.

### Instrumental — spokes and the overhead

45. A bike wheel spinning upside down on the grass, slow motion, glockenspiel on every rotation.
46. A bicycle bell struck twice, extreme close-up, the thumb and the dome.
47. Sun flaring directly through a spinning spoke pattern, slow motion, the most beautiful frame in the video.
48. An overhead of the street with four bikes lying on their sides in a rough circle on a lawn, nobody in frame, static.
49. Everything drops: a single wide of the empty road at dusk, held on one sustained note, no movement at all.

### Bridge — present day, rain

50. *"I drove down that street in the spring, in the rain"* — a windscreen with a wiper crossing it, the street beyond in soft focus, static, grey spring daylight.
51. *"Slowed to a crawl and I sat there again"* — adult Mahima in the driver's seat, engine off, both hands still on the wheel, profile, held very long.
52. *"The ramp is long gone and the fences came down"* — the driveway where the ramp was, plain empty concrete; then one continuous lawn where four gardens used to be fenced, two static shots.
53. *"And the streetlight is white and it burns all night now"* — the corner streetlight replaced with a cold white LED, on in daylight, matched framing to shot 21.
54. *"But I know the sound of a card in a spoke"* — a single flash frame of the card in the spoke from shot 19, two frames only, then back to the rain on the glass.
55. *"And a part of me is nine, and she never came in"* — through the wet windscreen, far down the road, a small figure on a bike at the edge of resolution — deliberately ambiguous, never brought into focus. Static, held to the end of the line.

### Final chorus — all four, and then everybody

56. *"We were kids on bicycles, racing the streetlights home"* — hard cut to full golden hour: the four-abreast frame restored, all four riders, brightest gold of the video.
57. *"Handlebars and hollering, and nobody rode alone"* — four faces mid-shout in the pan, the fourth face back in it.
58. *"Cards in the spokes making engines out of air"* — the card, new and clean, macro.
59. *"Nine years old and the whole wide world was four streets square"* — the overhead, and more bikes joining from side streets, ten of them.
60. *"We were kids on bicycles, and I hope that somewhere still"* — a crane-style wide of the road filling with children on bicycles, twenty of them, wide and rising.
61. *"There are four of them out late at the top of the hill"* — four silhouettes at the top of a rise against the last of the sun, small in frame, static.
62. *"We didn't know it was the best of it, we just knew it was ours"* — the streetlight coming on over the whole crowd of riders, low angle from beneath it.
63. *"We were kids on bicycles, racing the streetlights home"* — the widest frame of the video: the full street, full gold, full of bikes.

### Post-chorus — the chant

64. *"Ride till the yellow comes on"* — feet on pedals, macro, cut on the beat.
65. *"Ride till somebody calls"* — a bicycle bell, close-up.
66. *"Ride like the summer is long"* — a card in a spoke, close-up, ticking fast.
67. *"Ride like it never ends at all"* — a porch light coming on and a screen door held open, wide.

### Outro — the street at the end of the day

68. *"Cut grass and hot tar and a hose in the sun"* — the sprinkler from shot 1 again, identical framing, late gold instead of early hard light.
69. *"Four bikes on their sides where the pavement runs"* — four bikes lying on their sides on a grass verge, one front wheel still turning slightly, low and close.
70. *"The light on the corner is warming to gold"* — the warm orange corner streetlight coming up to full, macro, the same lamp as shot 21 and the opposite of shot 53.
71. *"And nobody's going in, and nobody's old"* — final shot: a locked-off wide of the empty street in the last gold of the day with the four bikes in it and children's voices audible off frame. Hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the four front doors (shot 4), each "kids on bicycles", the card
in the spoke, the truck ramp (shot 29), the three-abreast frame (shot 31),
the spoke flare (shot 47), the cut to rain (shot 50), the flash frame (shot
54), the hard cut back to gold (shot 56) and the final locked-off street. At
92 BPM a bar is 2.6 s; this edit holds shots for two bars where the uptempo
songs hold for one, and the bridge holds two shots for four bars each.

**The card-in-the-spoke challenge.** Shots 17–24 recut vertically are the
shareable fifteen seconds: four abreast, four faces, the card, the
streetlight, the porch, hands off the bars. Invite people to post the street
they grew up on, or the sound of a card ticking in a wheel. The spoke flare
(shot 47) and the overhead of four fallen bikes (shot 48) are the two frames
that will travel on their own.

**Caption cut:** shots 31–32 with *"We rode three abreast and the gap was
loud."*

## 6. Quality-control checklist

- The nine-year-old is unmistakably the same face as the adult in shot 51; build the child LoRA from aged-down adult stills, and check the match before any other shot is approved
- All four children keep the same faces and the same bikes across the whole summer; the girl with the taped glasses has the best bike from first frame to last
- Parents are never shown above the chest; the world's boundary is a whistle and an arm
- The summer has no memory effect on it — no haze, no grain, no vignette; the bridge is the only visually different section and it must look like another film
- The streetlight is warm orange everywhere except shot 53, where it is cold white in daylight; shots 21, 53 and 70 use matched framing
- The rider count is the story: four, then three from shot 31 to 44, four again at 56, then twenty by shot 60
- All house numbers, street signs, truck livery and chalk writing composited or left blank; no model-generated text
- Every riding shot posed with OpenPose; the hands-off-handlebars shot (24) checked frame by frame for arm count
- The last shot is locked-off, empty of people, with voices off frame, and holds until the audio fades
