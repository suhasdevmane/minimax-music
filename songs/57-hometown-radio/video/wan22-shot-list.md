# Wan 2.2 Shot List — "Hometown Radio"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission, plus six shots for the instrumental. Timestamps come from the
rendered WAV; cut on the sung line. At 96 BPM a bar is 2.5 s; the verses run
two bars a line and the choruses one and a half.

## 1. Visual world

One small American town, one evening, filmed as it actually looks. The film
runs on a single unbroken light schedule — **late gold, then blue hour, then
full night, then the last blue at the county line** — and no shot ever goes
backwards in that schedule. That constraint is the whole visual design: the
audience should feel the day ending underneath the song without ever being
told.

Three grades inside it. The **present** is dry and plain: low sun through a
driver's window, sodium streetlights, diner fluorescent, headlights. The
**memory flashes** are two seconds each, over-bright and grainy, blown out
at the edges, always a summer. Her mother's **porch** is the only frame in
the film with soft light in it, and it is the only place the camera looks a
second person full in the face.

Half of this video is shot from inside a car.

| Section | Grade | Camera |
|---|---|---|
| Intro | Late gold, sun low through the driver's window | Inside the car, low, from the footwell up |
| Verse 1 | Long shadows, hard bright street, dim warm bedroom | Passenger-window drive-bys, one interior |
| Pre-chorus 1 | Forecourt fluorescent against dusk | Static, then a two-second over-bright flash |
| Chorus 1 | Blue hour, sodium, headlights | Tracking the car, streetlights coming on |
| Verse 2 | Warm diner interior, night in the window | Handheld booth-height |
| Pre-chorus 2 | Diner warm, memory over-bright | Handheld between tables |
| Chorus 2 | Full night, headlights, lit windows | Two in the car, faster cuts |
| Instrumental | Sodium and the last blue in the west | Long static holds, one drive-out |
| Verse 3 | The only soft light in the film, kitchen glow behind | Still, close, faces seen directly |
| Bridge | Black silo against gold, then warm returns | Locked off, held long |
| Final chorus | Night, but brighter, everything lit | The chorus-one route, re-driven |
| Post-chorus | Headlights and streetlights, high contrast | Four hard cuts on the claps |
| Outro | Tail lights and one reflector, otherwise dark | Wide, receding, held |

## 2. Character bible — paste into every prompt

**Mahima** (present day, the whole drive)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and moving in the open window air, minimal makeup, wearing a fitted black tee, a good tan suede jacket and gold hoops that read as money in a town that has none, composed guarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima at seventeen** — the memory flashes only. Same face, cheaper
clothes, no jacket.
> Same female protagonist Mahima at seventeen, dark wavy hair, expressive dark eyes, a faded band tee and cut-off shorts, no makeup, sunburned shoulders, open unguarded expression, realistic cinematic photography, consistent identity

**The mother** — a woman in her fifties, grey coming in at the front, a
cardigan over a work shirt, reading glasses pushed up. **She is the only
other person in this film the camera looks at directly and holds on.** Her
face and hands are fully seen, warmly and without softening.
> an older woman in her fifties, grey at the temples, hair tied back, a cardigan over a plain work shirt, reading glasses pushed up on her head, warm plain unsentimental expression, realistic cinematic photography, consistent identity

**The best friend** — a woman the same age, apron, ponytail, a coffee pot in
one hand for most of her screen time. Face fully seen. Loud, delighted,
completely unstyled.

**The ex** — never seen, ever. He exists as a truck the same make and colour
at a red light, an empty passenger seat, and a name nobody says. Do not
generate him in any frame, including the memory flashes: in the seventeen
flashes she is alone in the car or with the friend.

Objects that carry the story: the **car radio display** (composited, never
legible), the **water tower** with initials weathered almost to nothing, the
**vape shop in the old dairy stand**, the **glow stars on a bedroom
ceiling** with one crooked, the **cracked red vinyl booth** and the sugar
caddy, the **coffee pot**, the **screen door** and the **old dog**, the two
**sweet tea glasses sweating on a porch rail**, the **silo**, and the
**empty passenger seat**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every sign, dial, menu, plate and screen is composited or kept illegible.**
The water tower initials, the subdivision entrance sign, the diner menu, the
county sign, the truck plates and the radio display are all overlays or
deliberately out of focus. A wrong small-town sign reads as fake instantly,
and the water tower initials must never resolve into letters — the whole
point of the line is that they are faded to a whisper.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks, the mother and the friend with IP-Adapter or a
character LoRA each. Depth for the diner and the porch. The drive-by plates
are the workhorse of this film: build one master car-interior plate for the
driver's side and one for the passenger window, and generate the passing
world as separate motion layers rather than asking for a full driving shot
each time — the model invents geometry through side windows.

OpenPose for the diner dance and for the hug that knocks the napkin
dispenser over. Animate single actions: a dial turning, a window going down,
a screen door swinging, a dog standing up slowly, a coffee pot tipping,
streetlights coming on. The streetlights-coming-on sequence in shot 17 is a
brightness ramp in the edit over a lit plate. 16:9 first; 9:16
recomposition for the diner dance and the radio-dial hook cut.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–5 s; the memory flashes exactly two.

## 4. Scene per lyric line

### Intro — two hours out

1. *"Two hours out and the static clears,"* — from the passenger footwell up to her hand on the wheel, a two-lane highway and fields through the windscreen, late gold sun, low and wide.
2. *"Same voice on the dial I haven't heard in years."* — macro on the car radio display (composited) as the numbers settle and the static resolves, her thumb still on the dial.
3. *"He says it's a warm one, folks, drive safe tonight,"* — her face in the rear-view mirror, listening, the smallest reaction she does not intend to have, close-up.
4. *"And I roll the window down and let it back inside."* — the driver's window going down and the air taking her hair, the field noise arriving, medium, sun directly across her face.

### Verse 1 — the inventory

5. *"Water tower's still got your letters and mine,"* — a water tower against a low sun, initials painted decades ago and weathered almost to nothing, never legible, low angle from the car.
6. *"Faded to a whisper, but I know every line."* — closer on the paint, the shapes barely there under the rust, macro, held.
7. *"The Dairy Barn's a vape shop, the church is the same,"* — a drive-by pair: a closed dairy stand with a bright new shopfront inside it, then a white clapboard church untouched, both from the passenger window.
8. *"And the field where we parked has a subdivision name."* — a field's worth of identical new houses with an entrance sign we never read, the same drive-by move, long shadows.
9. *"Mama kept my room like I'd be back by June,"* — a bedroom door opening on a room that stopped in a particular year, curtains closed, dim and warm, static wide.
10. *"Posters on the wall, glow stars, crooked moon."* — the ceiling from the bed: glow-in-the-dark stars, one of them crooked, macro, the room dim around it.
11. *"Passed your old truck at the light on Main,"* — back in the car: a truck the same make and colour two cars ahead at a red light on Main Street, hard bright street light, her hands tightening on the wheel.
12. *"Different plates, but my chest didn't get the memo, same old lane."* — the plates (composited, illegible) resolving as different, her exhaling, the light going green and the truck pulling away, close then wide.

### Pre-chorus 1 — she swore she'd drive through

13. *"I swore to myself I'd just drive through,"* — a gas station forecourt at the edge of town, her filling the tank, looking down the road out, forecourt fluorescent against dusk.
14. *"Gas and a coffee and I'm past you."* — her back in the driver's seat with a paper cup, key in the ignition, decided, medium.
15. *"But the dial lands right on that opening chord,"* — her hand going still on the key as the song starts on the car speakers, close on the hand, then her face.
16. *"And I'm seventeen with my hand out the door."* — two seconds, over-bright and grainy: Mahima at seventeen with her hand out of a moving car window in a rushing summer, alone in the frame.

### Chorus 1 — driving the town

17. *"Hometown radio still plays our song,"* — streetlights coming on one after another down a long road ahead of the car, blue hour, tracking from inside.
18. *"Like nobody told it that we moved on."* — the high-school parking lot, empty, one light on a pole, the car crossing it, wide.
19. *"Every streetlight's humming the words we knew,"* — the bleachers from below, sodium light through the boards, static.
20. *"Every mile of this town is a mile of you."* — a railway crossing with the lights flashing and no train, the car waiting, medium wide.
21. *"Everything changed and nothing did,"* — a drive-by of Main Street with half the shopfronts new and half the same, one continuous pass.
22. *"I'm a grown woman feeling like a kid."* — her singing along without meaning to, her face doing something she does not intend, close-up, dashboard light.
23. *"Turn it up, let it hurt, sing along,"* — her hand reaching to the volume and turning it up, then going back to the wheel, macro.
24. *"Hometown radio still plays our song."* — the car from outside, a single pair of tail lights going down a street of streetlights, static wide, blue hour ending.

### Verse 2 — the diner

25. *"Slid in the booth at the diner on Fifth,"* — a cracked red vinyl booth from the seat opposite, her sliding in, night in the window behind her, warm interior.
26. *"Cracked red vinyl, sugar packets, the whole gift."* — macro across the tabletop: the split vinyl, a caddy of sugar packets, a laminated menu kept out of focus.
27. *"My old best friend behind the counter, she screams,"* — the friend seeing her from behind the counter and shrieking, coffee pot still in her hand, handheld, delighted.
28. *"Says girl, you look expensive, but you still look sixteen."* — the friend coming out around the counter and hugging her hard enough to knock a napkin dispenser over, one continuous handheld take.
29. *"She says he moved to Dallas, married a nurse,"* — the friend sitting down opposite with the pot still in her hand, talking, seen over Mahima's shoulder.
30. *"Says it like it's good news, and it is, and it's worse."* — Mahima taking it well on the outside, her hands going around the mug, close-up, nothing in the room reacting.
31. *"Then that song comes on the speaker and she catches my eye,"* — the corner speaker, then the friend's eyes coming up across the table and not saying the obvious thing, two cuts.
32. *"Tops my coffee off and says, honey, some things don't die."* — the pot tipping and the coffee going in, steam, the friend's hand on Mahima's wrist for one second, macro.

### Pre-chorus 2 — the diner dance

33. *"I told her I'd only stop on through,"* — Mahima gesturing at the door with her thumb, half standing, not standing, medium.
34. *"Hug and a refill and I'm past you."* — her coat back on the hook, sitting down again, the friend already walking away with the pot, medium.
35. *"But she turns the speaker up and she's out on the floor,"* — the friend reaching up to the corner speaker and turning it up, then coming out between the tables with her arms already going, handheld.
36. *"Two girls in a diner, seventeen, hands out the door."* — the two of them dancing badly between the tables, two customers watching, the cook unimpressed in the hatch; cut two seconds of the same two girls at seventeen doing it in the same room, over-bright and grainy.

### Chorus 2 — with the friend in the car

37. *"Hometown radio still plays our song,"* — the two of them in the car with the windows down, the friend still in her apron, full night, headlights.
38. *"Like nobody told it that we moved on."* — the water tower again from directly below, floodlit from the ground, both of them looking up through the windscreen.
39. *"Every streetlight's humming the words we knew,"* — the subdivision at night, every window lit, the car going slowly past, drive-by.
40. *"Every mile of this town is a mile of you."* — the empty high-school field with the lights on for nobody, wide, the car parked at the fence.
41. *"Everything changed and nothing did,"* — the two of them singing at each other rather than at the road, handheld from the back seat.
42. *"I'm a grown woman feeling like a kid."* — the friend's face mid-laugh, then Mahima's, two close-ups cut hard.
43. *"Turn it up, let it hurt, sing along,"* — both their hands going to the volume at the same time, macro.
44. *"Hometown radio still plays our song."* — the car pulling up outside the diner again and the friend getting out, waving without turning round, medium wide.

### Instrumental — the town at night

45. The diner sign going off, the window going dark from the inside, static, held.
46. A dog crossing an empty Main Street unhurried, sodium light, wide.
47. The high-school field with the floodlights on for nobody, from the far end, long hold.
48. A porch swing moving on its own in the wind on a dark porch, close.
49. A grain elevator black against the last blue in the west, wide, still.
50. The car pulling out of town and taking the other turn, away from the highway — the cut into verse three.

### Verse 3 — her mother's porch

51. *"Drove out to Mama's the long way, took it slow,"* — a farmhouse at the end of a dirt drive, one porch light on, the car's headlights swinging across it, wide.
52. *"Screen door, sweet tea, and the dog I used to know."* — a screen door on its spring, then two glasses of sweet tea sweating on the porch rail, then an old dog getting up slowly, three cuts, soft light.
53. *"She didn't ask about him once, she asked about my week,"* — her mother's face, fully seen and held longer than any other face in the film, talking, kitchen light behind her through the screen.
54. *"Asked about my sister, asked if I still eat."* — her mother's hands around a glass, then Mahima laughing properly for the first time in the video, two-shot on the porch step.
55. *"She said, you can love a town and still drive on,"* — her mother saying it as an aside, not a lesson, looking out at the yard rather than at her daughter, close-up.
56. *"And she hummed the harmony to that same old song."* — the radio audible through the kitchen window, her mother humming under it without noticing, both of them on the step, wide, the last of the day going.

### Bridge — the silo, the empty seat

57. *"Sun going down behind the silo, gold,"* — an empty lot at the edge of town, the car facing a silo, the silo black against gold, locked off, held. **The most beautiful frame in the film, and it is a parking lot.**
58. *"The whole sky the color of a story I've told."* — the sky above the silo alone, no ground in frame, the colour changing inside the shot.
59. *"I'm parked in the lot with the engine still on,"* — her hands coming off the wheel and going into her lap, the engine vibration visible in the mirror, close.
60. *"Waiting on the second verse to come along."* — the radio display (composited) and the dashboard clock, macro, nothing happening.
61. *"Maybe it never was ours, maybe it was mine,"* — the empty passenger seat, held four seconds, the seatbelt still buckled from nobody.
62. *"You were only ever riding on the passenger side."* — the same seat, the camera not moving, then her looking across at it once and looking away.
63. *"This town didn't miss you, it kept the porch light on for me,"* — three warm returns on the line: the water tower, the diner window, her mother's porch light, one second each.
64. *"Water tower, diner, and the kid it let me be."* — her own face in the rear-view mirror, and for one frame the seventeen-year-old's in the same mirror, then back, close-up.

### Final chorus — the same roads, driven differently

65. *"Hometown radio still plays our song,"* — the long road of streetlights from shot 17, all of them already on now, the car moving faster.
66. *"And I'm finally okay that we moved on."* — the high-school lot from shot 18, her driving straight through it without slowing.
67. *"Every streetlight's humming the words I knew,"* — the bleachers from shot 19, headlights sweeping across them as she turns.
68. *"Every mile of this town is a mile I grew."* — the railway crossing from shot 20, the lights flashing, and this time she does not stop because there is nothing coming.
69. *"Everything changed and nothing did,"* — Main Street re-driven, faster, the new shopfronts and the old ones the same length of pass.
70. *"I'm a grown woman, still that kid."* — her singing on purpose this time, wide open, close-up, dashboard light.
71. *"Turn it up, let it heal, sing along,"* — her hand out of the driver's window at exactly the angle the seventeen-year-old's was in shot 16, macro. **The payoff frame.**
72. *"Hometown radio still plays our song."* — the car from outside on the same street as shot 24, more windows lit, headlights on full, wide.

### Post-chorus — four streets

73. *"Same three chords, same four streets,"* — Main Street on the clap, hard cut.
74. *"Same girl behind the wheel, different heartbeat."* — the road past the school, hard cut.
75. *"Same three chords, same four streets,"* — the road out to her mother's, hard cut.
76. *"Ooh, I'm home, I'm home, I'm home."* — the highway out of town, then her face driving, saying the last line, close.

### Outro — past the county line

77. *"Signal's fading out past the county sign,"* — a county sign passing in the headlights, never legible, low angle from the car.
78. *"DJ says goodnight, folks, says take your time."* — the radio display degrading back into static, macro, the numbers drifting.
79. *"I keep the window down and I sing along,"* — her singing along to something she can barely hear any more, window still down, close-up, dark.
80. *"Hometown radio, still playing our song."* — the car from outside on a straight dark road, one pair of tail lights, wide, receding.
81. *"Still playing our song."* — final shot: the tail lights going away down a straight dark road, the window still down, one reflector catching the light and going out. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the dial clearing in shot 2, each *"hometown radio still plays
our song"*, the truck at the light in shot 11, the diner hug in shot 28, the
diner dance in shot 36, the instrumental, the porch line in shot 55, the
empty passenger seat in shot 61, the hand out of the window in shot 71, the
post-chorus claps, and the last tail lights. At 96 BPM a bar is 2.5 s; the
choruses cut every bar and a half, the post-chorus on each clap.

**The hometown challenge.** The shareable cut is shots 1–4 and 17 — the dial
pulling out of static and the streetlights coming on — vertical, with
*"Hometown radio still plays our song"* on screen. Invite people to post the
song their hometown station will not stop playing, or the building that used
to be something else. The second shareable clip is the diner dance, shot 36,
posted whole with no context. **The caption line:** *"Everything changed and
nothing did."*

## 6. Quality-control checklist

- The light schedule never runs backwards: late gold through verse one, dusk at the forecourt, blue hour in chorus one, full night from verse two, the last of the day only on the porch and the silo, then full dark to the end
- The ex is not generated in any frame of the film, including the seventeen flashes; he is a truck, an empty seat and a name nobody says
- The memory flashes are exactly two seconds, over-bright and grainy, and there are only three of them: shots 16, 36 and one frame inside shot 64
- Her mother is the only second face the camera holds on, and the porch is the only soft light in the video
- Nothing is legible: the water tower initials, the subdivision sign, the diner menu, the truck plates, the radio display, the county sign
- The chorus-one and final-chorus locations match one for one — shots 17 with 65, 18 with 66, 19 with 67, 20 with 68, 21 with 69, 24 with 72
- Shot 71 reproduces the arm angle of shot 16 exactly; if it does not match, reshoot the plate rather than cutting around it
- The last shot is locked-off on the receding tail lights and holds until the station dissolves into static
