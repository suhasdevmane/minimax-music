# Wan 2.2 Shot List — "Dance Like Nobody's Sober"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Eighty-three entries. This is an uptempo song: at 126 BPM a bar
is 1.90 s, so most shots run 2–4 s, the choruses cut on the bar and the
post-chorus chant cuts on the half-bar. Take timestamps from the rendered
WAV.

## 1. Visual style

One reception hall and the car park outside it, across a single night that
ends at half five in the morning. **The room is real and the light is
practical**: tungsten uplighters up the walls, a disco ball throwing moving
dots, one strobe on the DJ rig, a fire door leaking amber into a blue car
park. No CGI, no colour that a wedding hall could not actually produce.
Everything is handheld and inside the crowd — this video has no clean wide
until the bridge, and no beautiful shot until the last one.

The people are the point. Every extra is a specific person with a history,
not a background dancer, and nobody in this video dances well.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cool blue car park against a hot amber doorway | Slow push, then handheld |
| Verse 1 | Warm tungsten, disco dots, honest and slightly ugly | Handheld, close, fast |
| Pre-chorus 1 | Lights starting to strobe on the snare roll | Handheld, building |
| Chorus 1 | Saturated amber and magenta, strobe on the brass | Inside the crowd, moving |
| Post-chorus | Hard strobe, four repeating frames | Ultra-fast, locked |
| Verse 2 | Warm and close, each face held long enough to read | Handheld portraits |
| Pre-chorus 2 | Building again, more people in frame | Handheld |
| Chorus 2 | Fuller, hotter, faster strobe, confetti underfoot | Overhead and inside |
| Instrumental | Full colour into sudden darkness | Fast cuts, then still |
| Bridge | One warm wash, everything else shadow, room slowed | Slow pan, still |
| Final chorus | House lights up, full colour, no shadows left | Wide and moving |
| Outro | Flat dawn grey, one warm doorway | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night — one look, degrading beautifully)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned up at the start and coming loose through the night, evening makeup slightly worn, wearing an emerald green satin midi dress, barefoot from the first chorus onward, laughing open expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** is not in this video. There is no romantic lead. The song is about a
room, and the only person the camera loves more than once is Mahima.

**The grandmother** — the anchor character, seen four times: on a plastic
chair by the door in the intro, at the front of the conga line, back at the
front in the final chorus, and on the kerb at dawn.
> an older woman in her late seventies, silver hair set for an occasion, a good navy coat over a floral dress, absolutely delighted expression, realistic cinematic photography, consistent identity

**The bride** — dress bunched in one fist, veil still on, dancing properly.
**The groom** — shirtsleeves, no jacket, one shoe, by verse two.
**The two aunties** — women in their sixties holding both hands, howling the
same chorus at each other, one of them crying and grinning at once.
**The uncle** — a man in a waistcoat with one specific shoulder move.
**The photographer** — a woman who gives up and sits on the edge of the
stage with the camera in her lap.
**The kids** — two children in socks, skidding, and later one asleep on
coats.

Nobody here is faceless; this is the one video in the catalogue where the
crowd is the co-star. Keep every extra plausibly related to somebody else in
frame.

Objects that recur: the **heels standing upright in a potted ficus**, the
**napkin in the punch bowl**, the **fork on the carpet**, **table nine empty
with nine full drinks on it**, the **disco ball**, the **confetti**, and
**cake wrapped in a napkin** at dawn.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The DJ rig displays, the seating plan, the table numbers and any signage
are composited in the edit.** Generate them blank. The model cannot render
legible text and a readable table card will break the take.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and the grandmother with IP-Adapter or a character LoRA; lock the
bride, groom and the two aunties with a lighter reference each, since they
recur but only in one or two shots per section. **OpenPose is essential
here** — the conga line, the uncle's shoulder move, the kids skidding in
socks and every hands-up chorus frame need a pose reference or the model
invents limbs. Depth for the hall interiors so the crowd holds its depth
behind the foreground.

Crowd shots are the hard part. Generate them as smaller groups against a
matched background and layer two or three passes in the edit rather than
asking the model for forty people in one frame; the negative prompt already
fights many-people-in-the-background for good reason. 16:9 first; 9:16 for
the chorus and the chant, which are the natural vertical content.

Animate in short bursts: one movement per clip. A conga line is three clips,
not one. The light "strobing" is safest done as a brightness cut in the edit
over an evenly lit plate.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — outside, then the door opens

1. *"String lights over the parking lot, band's loading in"* — a slow push across a parking lot at night under string lights strung between poles, a van with its back doors open, cool blue.
2. *"Somebody's grandma's already three glasses in"* — the grandmother on a plastic chair by the fire door in her good navy coat, glass in hand, entirely delighted, medium.
3. *"The DJ says, one more, and the whole room roars"* — the fire door swinging open from inside, sound and hot amber light spilling into the blue, from outside looking in.
4. *"And a hundred pairs of shoes hit the floor"* — low and inside now: forty pairs of feet hitting parquet on the downbeat, hip height, handheld.

### Verse 1 — the room coming apart

5. *"There's a napkin in the punch bowl and a fork on the floor"* — macro on a napkin sagging into a punch bowl, then a fork lying on patterned carpet that nobody picks up.
6. *"The best man ran eleven minutes, then he ran some more"* — a man at a microphone with three cue cards and no plan, the room's polite faces holding on behind him, wide.
7. *"Cousins from three time zones that nobody has seen"* — three people colliding in a hug by the bar, all talking at once, handheld and close.
8. *"Since the summer that we all turned seventeen"* — a two-second flash of the same three as teenagers in a garden, warm and overexposed, then hard cut back.
9. *"Table nine has given up on ever sitting down"* — an entirely empty round table with nine full drinks still on it, a blank table card (composited), static.
10. *"And the kids in socks go skidding past the sound"* — two children in socks skidding the length of the parquet and crashing softly into a curtain, low tracking.
11. *"My shoes are in a plant pot and I'm leaving them right there"* — a pair of heels standing upright in a potted ficus, macro, then Mahima's bare feet walking away from them.
12. *"There's frosting on my elbow and I'm past the point of care"* — close on a smear of white frosting on her elbow and her entirely not noticing it, handheld.
13. *"Somebody's uncle does the shoulder thing he does"* — a man in a waistcoat doing one very specific shoulder move, medium, held long enough to be funny.
14. *"And the whole room comes apart, and I'm in love with us"* — the ring of people around him losing it, then Mahima's face in the middle of them, lit up.

### Pre-chorus 1 — the request

15. *"The DJ takes a request from a woman in a hat"* — a woman in an enormous hat leaning over the DJ booth, shouting, the DJ leaning in to hear, medium.
16. *"Plays it twice in a row and nobody minds that"* — the DJ nodding and reaching for the fader, blank screens on the rig (composited), close on the hand.
17. *"Bass in the folding chairs, the ceiling's coming loose"* — macro on a folding chair leg buzzing against parquet, then a ceiling tile visibly shifting in its frame.
18. *"Grab a hand, any hand, we've got nothing left to lose"* — hands finding hands across the floor, nobody checking whose, waist height, the lights starting to strobe.

### Chorus 1 — the floor

19. *"Dance like nobody's sober, sing like nobody's home"* — a wide from inside the crowd: forty people all doing something different at the same tempo, handheld.
20. *"Left foot, wrong foot, doesn't matter, it's our own"* — low on a dozen pairs of feet, none of them in step, all of them on the beat, tracking.
21. *"Hands up, ceiling down, throw the whole night over"* — every hand in the room up on the downbeat, shot from the floor looking up, disco dots crossing the ceiling.
22. *"Nobody's watching, and nobody's sober"* — three faces in a row, mid-shout, none of them aware of the camera, fast cuts.
23. *"Dance like nobody's sober, sing like nobody's home"* — Mahima at the centre with the bride, both singing the line straight at each other, close two-shot.
24. *"Every song's our song when the speakers get blown"* — a speaker stack visibly moving, then the bride's veil in motion across the frame.
25. *"Turn it up, hold on, this is what we came for"* — a slow-motion beat of confetti firing out of a cannon nobody was licensed to use, one second only.
26. *"Dance like nobody's sober till they throw us out the door"* — the whole floor from the DJ's position, everyone in frame, everyone moving, wide.

### Post-chorus 1 — the chant

27. *"Left foot, wrong foot, doesn't matter, doesn't matter"* — feet in socks on parquet, hard strobe, locked-off.
28. *"Left foot, wrong foot, let the whole floor shatter"* — one hand hitting the air, macro, strobe.
29. *"Left foot, wrong foot, doesn't matter, doesn't matter"* — a tray of drinks going past at speed, low, strobe.
30. *"Dance like nobody's sober, and nobody's sober"* — the disco ball itself, dead centre, turning, strobe.

### Verse 2 — the people

31. *"The bride has got her dress hitched up above her knees"* — the bride with her dress bunched in one fist, dancing properly, medium, warm.
32. *"Her mother's on the floor and her father's on his feet"* — an older woman on the parquet doing something from decades ago, entirely unbothered, handheld.
33. *"Two aunties who have not spoken since a funeral in June"* — two women in their sixties finding each other across the floor and stopping, one beat of hesitation, medium.
34. *"Are holding both hands, screaming out the same tune"* — the same two holding both hands and howling the chorus at each other, one crying and grinning at once, close.
35. *"The groom has lost his jacket and I think he's lost a shoe"* — the groom in shirtsleeves with one shoe on, being carried sideways by three friends, wide.
36. *"The photographer gave up an hour or two ago too"* — a woman sitting on the edge of the stage with a camera in her lap, watching instead of shooting, smiling.
37. *"There's a cousin on a chair who should not be on a chair"* — a young man standing on a folding chair with both arms up and visibly no plan for getting down, low angle.
38. *"And a conga line has started and I don't know where"* — a line forming out of nothing near the cake table, three people becoming eight, tracking.
39. *"The waiters have stopped pretending, they are in it now"* — two waiters setting down a tray and joining the line, one still holding a cloth over his arm.
40. *"And somebody's grandma's leading it, don't ask me how"* — the front of the line: the grandmother, coat off, leading twenty people, absolutely in charge, wide tracking all the way round the room.

### Pre-chorus 2 — the queue at the booth

41. *"The DJ's taking requests from a queue outside the booth"* — six people queuing at the DJ booth, patient and serious, like it is a bank, wide.
42. *"The bride says, play it one more time, and that's the truth"* — the bride arriving at the front and being waved straight in, the queue accepting this without complaint.
43. *"Bass in the folding chairs, the ceiling's coming loose"* — reuse shot 17's chair-leg macro, tighter and faster, the buzz stronger.
44. *"Grab a hand, any hand, we've got nothing left to lose"* — the room reacting before the drop lands, thirty faces turning toward the booth at once, handheld.

### Chorus 2 — bigger

45. *"Dance like nobody's sober, sing like nobody's home"* — an overhead of the entire floor from a balcony or a ladder, the whole room turning, wide.
46. *"Left foot, wrong foot, doesn't matter, it's our own"* — two guests miming the brass counter-melody with imaginary trumpets, entirely committed, medium.
47. *"Hands up, ceiling down, throw the whole night over"* — reuse shot 21's floor-up framing, more hands, more confetti falling into it.
48. *"Nobody's watching, and nobody's sober"* — the uncle again, now with a circle of six copying his shoulder move badly, handheld.
49. *"Dance like nobody's sober, sing like nobody's home"* — Mahima in the middle, arms up, head back, hair fully loose now, close-up.
50. *"Every song's our song when the speakers get blown"* — confetti already ankle-deep on the parquet, feet moving through it, low.
51. *"Turn it up, hold on, this is what we came for"* — the grandmother and the bride dancing together, both laughing, medium.
52. *"Dance like nobody's sober till they throw us out the door"* — the hall from the doorway, every person in frame, the widest shot so far, static.

### Post-chorus 2 — faster

53. *"Left foot, wrong foot, doesn't matter, doesn't matter"* — reuse shot 27, cut twice as fast.
54. *"Left foot, wrong foot, let the whole floor shatter"* — reuse shot 28, a different hand, same framing.
55. *"Left foot, wrong foot, doesn't matter, doesn't matter"* — the drinks tray again, this time nearly empty, low.
56. *"Dance like nobody's sober, and nobody's sober"* — the disco ball, hard strobe, the last frame before the break.

### Instrumental — the band breakdown, then the drop

57. A drummer and a percussionist trading fills with the whole room clapping on the two and four, from behind the kit, fast cuts.
58. The synth lead over an overhead of the floor, everyone in a loose ring, arms up.
59. Two guests attempting a lift and abandoning it halfway, both laughing, handheld, one take.
60. The cake table with one slice left on it and forks everywhere, macro, oddly still.
61. The hard drop: the room lights cutting to near-black, the crowd noise falling away, one child asleep face-down on a mountain of coats across two pushed-together chairs — the cut into the bridge.

### Bridge — the one still moment

62. *"Half past one, and the room goes soft for a beat"* — Mahima stopped dead in the middle of a moving room, everything around her very slightly slowed, one warm wash of light.
63. *"There's a kid asleep on a mountain of coats by our feet"* — the sleeping child on the coats, held longer than any shot so far, static, quiet.
64. *"And I look at every face that I grew up beside"* — a slow pan across faces, each held for a beat: the two aunties, the uncle, her mother, the bride.
65. *"And I know that this exact room will not happen twice"* — Mahima's eyes going wet and her deciding not to let it happen, extreme close-up.
66. *"So I take the nearest hand and I lift it in the air"* — her hand finding another hand at her side without looking, both going up, macro.
67. *"While the song is still playing and the floor is still there"* — the room coming back to full speed and full light around her in one continuous take, medium into wide.

### Final chorus — house lights up

68. *"Dance like nobody's sober, sing like nobody's home"* — the house lights coming up on a floor that flatly refuses to clear, wide, everything visible and nobody caring.
69. *"Left foot, wrong foot, doesn't matter, it's our own"* — feet again, this time in full white light, confetti and cake and one lost shoe on the parquet.
70. *"Hands up, lights up, last ones on the floor"* — every hand up under house lights, the ugliest and best-lit frame in the video, wide.
71. *"Nobody's leaving, and nobody's sober"* — a venue staff member gesturing at the door and being absorbed into the crowd, medium.
72. *"Dance like nobody's sober, sing like nobody's home"* — the bride and groom being carried, badly, by six people, handheld and low.
73. *"Every song's our song and the speakers have blown"* — confetti in the air a second time, this time falling under white light, slow motion for one beat.
74. *"Turn it up, hold on, this is what we came for"* — the grandmother back at the front of a new line, coat still off, leading it again.
75. *"Dance like nobody's sober till they throw us out the door"* — a wide of the whole hall from the doorway with every person in frame and moving, hold.

### Post-chorus 3 — out the door

76. *"Left foot, wrong foot, doesn't matter, doesn't matter"* — feet on parquet under house lights, no strobe left, locked-off.
77. *"Left foot, wrong foot, let the whole floor shatter"* — a hand in the air, the last one, macro.
78. *"Left foot, wrong foot, doesn't matter, doesn't matter"* — the empty drinks tray on a table, still.
79. *"Dance like nobody's sober, and nobody's sober"* — the disco ball stopping, the motor off, the dots going still on the wall.

### Outro — the car park at half five

80. *"Car park, half five, and the sky is going grey"* — the parking lot in flat grey dawn light, the string lights still on and now pointless, wide, static.
81. *"Shoes in one hand, cake in a napkin, on our way"* — six people in evening wear sitting on a kerb, shoes in hands, cake in napkins, the grandmother among them.
82. *"Somebody starts the chorus in the taxi line once more"* — the taxi queue, one person starting the hook and four ragged unaccompanied voices joining, medium.
83. *"Dance like nobody's sober till they throw us out the door"* — final shot: the fire door swinging shut on an empty hall, confetti all over the floor, one uplighter still on, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the fire door at shot 3, each *"dance like nobody's sober"*, every
post-chorus chant, the conga line at shot 40, the hard drop at shot 61, the
sleeping child at shot 63, the house lights at shot 68, and the door closing.
At 126 BPM a bar is 1.90 s; choruses cut on the bar, the chant cuts on the
half-bar, and the bridge holds for four full bars per shot.

**The wrong-foot cut.** Post shots 27–30 vertical with the chant on screen
and invite people to film the worst dancer at the best wedding they have ever
been to. The second shareable frame is shot 40, the grandmother leading the
conga line, captioned *"This exact room will not happen twice."*

## 6. Quality-control checklist

- One look for Mahima across the whole night, degrading correctly: hair pinned at shot 4, half loose by shot 24, fully loose from shot 49, barefoot from shot 11 onward
- The grandmother appears exactly four times — shots 2, 40, 74 and 81 — and is the same person each time
- Nobody in this video dances well, and nobody looks like a professional dancer
- Every extra reads as somebody's relative; no styled background models
- Crowd frames are layered from smaller passes, never one forty-person generation
- All table cards, DJ screens and signage composited; no model-generated text
- The light only ever gets brighter after the bridge, ending in flat dawn grey
- The last shot is locked-off and holds until the audio fades
