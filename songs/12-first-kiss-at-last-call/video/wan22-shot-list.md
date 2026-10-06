# Wan 2.2 Shot List — "First Kiss at Last Call"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
120 BPM a bar is 2.0 s, so most shots are 2–4 s and the choruses cut on the
bar.

## 1. Visual style

One dive bar, one night, told out of order. Three light states and the whole
video is the argument between them. **State one, the bar at full volume:**
warm tungsten, pink neon, hard practical shadows, bodies cutting the frame.
**State two, the alley:** cold blue, one security lamp, breath visible.
**State three, the houselights:** flat green-white fluorescent, no flattery,
every surface honest — and shot like it is the most beautiful light in the
film. Handheld and close in the bar, locked off on the street. The camera
never leaves the building until the final chorus.

| Section | Grade | Camera |
|---|---|---|
| Intro | Pink neon over warm tungsten, deep shadow | Following at head height, handheld |
| Verse 1 | Warm orange, practical only, hard shadows | Fast handheld, cutting on the beat |
| Pre-choruses | Warm dying, cold edges creeping in | Static, longer holds |
| Choruses | Flat green-white fluorescent, wide open | Push-in, then wide |
| Post-choruses | Hard white, high contrast | Half-second impact cuts |
| Verse 2 | Neon sign red-to-blue on skin; alley cold blue | Handheld, then still |
| Instrumental | Fluorescent going down one bank at a time | Slow drifts, rhythmic cuts |
| Bridge | One warm practical, everything else out | Static, single subject |
| Final chorus | Fluorescent inside, sodium orange outside | Tracking out through the door |
| Outro | One sodium lamp on a wet street | Locked off, slow |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night, bar looks)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a slight wave from the humidity, warm smudged eye makeup, wearing a dark red slip top and straight-leg black jeans with scuffed white boots, amused alert expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (from the side door onward, jacket over her shoulders)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, warm smudged eye makeup, wearing a dark red slip top and straight-leg black jeans with an oversized olive canvas jacket draped over her shoulders, open unguarded expression, realistic cinematic photography, consistent identity

**Kai** (the romantic lead, he has a face in this one)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded band t-shirt under an oversized olive canvas jacket and dark jeans, easy grin, slightly nervous hands, realistic cinematic photography, consistent identity

**The bar staff** — a bartender in her forties counting notes, a barback
stacking glasses, a bouncer at the door. Faces allowed, always working,
never reacting to the couple except once (the bouncer holding the door).

**Strangers** — the pool players, the engaged cousin's booth, the crowd. Keep
them out of focus, cropped, or backs to camera. Nobody but Mahima and Kai
gets a lit close-up.

Objects: the **jukebox** with its cracked plastic front, the **dollar taped
to the ceiling**, the **dartboard**, the **beer sign in the window** that
cycles red and blue, the **mop bucket**, the **bank of fluorescent tubes**,
the **olive jacket**, the **bar sign** outside.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All signage, jukebox displays, the beer sign's letters, the bar sign and
any readable lettering are composited in the edit.** Generate the neon and
the sign faces as lit blank shapes and add the letterforms in post — the
model cannot render legible text, and this video is full of signs.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA; keep
the strangers' references deliberately soft so they never sharpen into named
faces. Keyframes first; OpenPose for the bad dancing, the pool shot and the
kiss; Depth for the deep bar interiors so the background bodies stay behind
the leads. 16:9 first; 9:16 for the chorus and post-chorus cuts, which are
the natural vertical content. Animate conservatively: a hand landing on a
waist, chalk on a cue tip, a chair going up on a table, a fluorescent tube
flickering to life. The houselight hit is easiest as a brightness ramp in the
edit over a lit plate, not as a generated lighting change.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; the post-chorus impact shots 0.5 s.

## 4. Scene per lyric line

### Intro — the bar at nine

1. *"Nine o'clock, the door swings, the neon buzzing pink"* — the front door of a dive bar swinging inward, pink neon above the back bar throwing color across a wall of shoulders, handheld push through the doorway.
2. *"You had one job tonight and that job was buying me a drink"* — Mahima at the bar, elbow on the wood, glancing sideways down the room, one eyebrow up, medium close-up, warm tungsten.
3. *"Somebody's racking pool, somebody's playing sad"* — two quick cuts: a rack lifting off a fresh triangle of balls; a man alone at the end of the bar staring at nothing, both out of focus at the edges.
4. *"And I'm already counting up the almosts that we had"* — Mahima's eyes finding Kai across the room over the top of a glass, the crowd sliding between them, slow push-in.

### Verse 1 — the near-misses

5. *"Sticky floor, cheap draft, forty bucks in the jar"* — macro: a glass lifting off the bar and leaving a wet ring, then a tip jar of folded notes, hard warm light.
6. *"A dollar taped to the ceiling with a stranger's name"* — low angle straight up at a ceiling tile with a taped dollar bill on it (lettering composited), the tungsten glare behind it.
7. *"There's a dartboard nobody has hit since the summer"* — a dusty dartboard with one dart lodged near the wire, a hand entering frame and not throwing, close-up.
8. *"You leaned across the jukebox and you played the worst song there"* — Kai leaning on the lit jukebox glass, finger on a blank glowing panel (UI composited), his face uplit, Mahima behind him in soft focus.
9. *"I said that is a crime, you said dance to it anyway"* — the two of them mid-argument and laughing beside the jukebox, her hands up in mock outrage, handheld two-shot.
10. *"So we did it badly, out of time and out of tune"* — them dancing badly in two feet of space, deliberately off the beat, her head thrown back laughing, tight handheld.
11. *"Your friend kept calling and my friend kept a look on you"* — a phone face-up on the bar lighting with a call (UI composited), then a hard cut to her friend across the room watching over the rim of a glass.
12. *"Every time you got close somebody moved the room"* — Kai's hand landing on her waist and a stranger's shoulder immediately cutting through the frame and breaking the contact, close-up on the hands.
13. *"Ten thirty you almost, eleven I almost, and the night was almost through"* — a wall clock at ten thirty, then the same clock at eleven, and between them the same two people standing a metre apart, matched framing.

### Pre-chorus 1 — the room comes down

14. *"The bartender's counting tips, the stools are going up"* — the bartender counting notes onto the bar, then stools going upside down onto the wood in a row behind her, static.
15. *"There's a mop bucket sighing and a last song running out"* — a mop bucket wheeled across the foreground, wheels squealing, the couple small and still behind it.
16. *"I thought we'd lost it somewhere between the pool cue and the door"* — Mahima looking at the pool table, then at the exit, the last customers leaving in a blur behind her, slow pan.
17. *"Then the ceiling opened up and I could not hide anymore"* — a low wide of the ceiling, one fluorescent tube stuttering, her face tipping up into it, static.

### Chorus 1 — the houselights

18. *"First kiss at last call"* — the bank of fluorescent tubes banging on across the ceiling in one hit, the room instantly flat and green-white, wide.
19. *"Lights up and I don't care at all"* — both of them squinting and laughing in the new light, hands half up, close two-shot.
20. *"No candle, no slow song, no dark to hide in"* — a slow pan across the ugly truth of the room: scuffed floor, taped booth seat, dead neon, empty glasses.
21. *"Every ugly bulb in the building coming on"* — the tubes from directly underneath, filling frame, blinding, then the exposure settling.
22. *"You looked at me like I was the one thing worth the wait"* — Kai's face in flat fluorescent, not looking away, close-up, no flattering light at all.
23. *"And I never looked better than I did at half past late"* — Mahima in the same light, smudged makeup, tired eyes, and shot like a portrait, close-up.
24. *"First kiss at last call"* — the kiss, held, a barback carrying a crate of glasses straight past behind them, medium, push-in.
25. *"Lights up and I don't care at all"* — a mop passing across the floor at their feet while they do not move, low angle.

### Post-chorus 1 — chant

26. *"Lights up, lights up, and the whole town saw"* — half-second: a hand slapping a bank of switches on a panel by the cellar door.
27. *"Lights up, lights up, kiss me in the ugly light"* — half-second: the tubes flickering to full.
28. *"Lights up, lights up, and I don't care at all"* — half-second: her face lit flat, grinning straight down the lens.
29. *"Kiss me in the ugly light, kiss me at last call"* — half-second: the bartender pointedly wiping the bar and not looking at them.

### Verse 2 — rewind to the pool table and the alley

30. *"Nine bucks in quarters and a game that we both lost"* — back to warm light: quarters dropping into the pool table slot, balls rumbling down inside the frame, macro.
31. *"You chalked the cue like it mattered and you scratched it on the break"* — blue chalk twisted onto a cue tip in close-up, then the break and the white ball dropping straight into a pocket, Kai's shoulders sagging.
32. *"The beer sign in the window's missing half of its letters"* — the neon beer sign in the window from inside, half its tubes dead (letterforms composited), buzzing.
33. *"So it turned your face red and then it turned your face blue"* — Kai's face in profile with the sign cycling red then blue across it, everything else black, close-up.
34. *"Somebody's cousin got engaged and the corner booth went up"* — a booth of strangers exploding to their feet cheering, a ring lifted, all of them out of focus, wide.
35. *"And we clapped like we knew her, and you looked at me too long"* — the two of them clapping politely, then his applause slowing while he looks at her, tight two-shot.
36. *"Then the side door, and the cold air coming down on my arms"* — the side door pushing open onto a cold blue alley, her bare arms and the change in her breath, handheld from behind.
37. *"You gave me your jacket and you kept your hands in yours"* — the olive jacket going over her shoulders, then his hands going straight back into his own pockets, close-up on the hands.
38. *"I could have kissed you out there in the dark and got away"* — the two of them under one security lamp in the alley, close, and neither moving, static wide, cold blue.
39. *"But the dark is easy, and I wanted you to stay"* — Mahima looking at him one beat too long and then deliberately looking away down the alley, close-up.

### Pre-chorus 2 — the music dies

40. *"The speakers cut to nothing, somebody yells last call"* — a hand pulling a fader down behind the bar, the room's sound dropping out, static close-up.
41. *"The chairs go up like a curtain coming down on us all"* — chairs going up on tables in a fast row across the frame, one after another, tracking sideways.
42. *"I figured we would wave goodbye and let it die out on the street"* — the two of them at the front door about to turn opposite ways, a half-raised hand, medium.
43. *"Then you said my name like a question I already knew"* — Kai stopping and turning back, mouth moving, no sound in the mix, extreme close-up on her reaction.

### Chorus 2 — the same moment, wider

44. *"First kiss at last call"* — reuse the houselight hit, this time from the far end of the bar, the whole room in frame.
45. *"Lights up and I don't care at all"* — wide: chairs up, mop, staff working, two people kissing in the middle of it, slow push-in.
46. *"No candle, no slow song, no dark to hide in"* — the dead jukebox, dark for the first time, in the foreground of the kiss.
47. *"Every ugly bulb in the building coming on"* — reuse shot 21, held two beats longer.
48. *"You looked at me like I was the one thing worth the wait"* — over-the-shoulder from behind Kai, her eyes open in the fluorescent, close.
49. *"And I never looked better than I did at half past late"* — her reflection in the mirrored back bar between the upturned stools, flat and unflattering and lovely.
50. *"First kiss at last call"* — the bartender in the background finally allowing herself half a smile while she counts, medium.
51. *"Lights up and I don't care at all"* — the two of them from above, the emptied room around them, overhead wide.

### Instrumental — closing the bar

52. Bar staff stacking glasses into a crate in strict rhythm, four cuts on the beat, flat fluorescent.
53. A broom sweeping bottle caps and a straw across the floor toward camera, low angle, one long push.
54. The jukebox screen going black, the pool table lamp switching off, two hard cuts.
55. The two of them standing in the middle of the emptying room not moving while everything else moves around them, slow drift, wide.
56. One bank of fluorescents going out, then another, the room stepping down into half-dark — the cut into the bridge.

### Bridge — the honest bit

57. *"Nobody plans it under the bad light"* — Mahima sitting on a barstool that has already been put up on the bar, boots on the rail, one warm practical over her, everything else out, static.
58. *"Everybody's holding out for candles and a perfect night"* — two seconds of an imagined candlelit restaurant table, deliberately flat, lifeless and over-lit, no people in it.
59. *"But you got me under the buzz and the beer and the broom"* — hard cut back to the real bar: a buzzing tube, a beer tap dripping, a broom propped against a wall, three fast macros.
60. *"Cold air in the doorway and a bar going back to a room"* — the propped-open front door with cold air visibly moving through it, the bar behind stripped of everything that made it a bar, wide static.
61. *"It beat every version I rehearsed of how it should have gone"* — two seconds of an imagined rooftop with string lights, equally flat and empty, then a hard cut to her face.
62. *"It beat every slow song I was ever saving for someone"* — Mahima alone, direct to camera for the only time in the video, one warm lamp, close-up.

### Final chorus — leaving

63. *"First kiss at last call"* — the two of them crossing the emptied floor toward the front door hand in hand, tracking backwards, full light.
64. *"Lights up and I don't care at all"* — the bar staff singing the line back without stopping work, the barback with a crate, the bartender with a till drawer, medium.
65. *"No filter, no shadow, no soft place to land"* — flat overhead of the whole bar, every light on, nothing hidden, wide.
66. *"Just a bouncer holding the door and your hand in my hand"* — the bouncer holding the door open with one arm while they duck under it, low angle.
67. *"You looked at me like I was the one thing worth the wait"* — the hard cut from fluorescent white to sodium orange as they step out, on the syllable, matched framing.
68. *"And I never looked better than I did at half past late"* — Mahima on the wet sidewalk under the orange lamp, turning back to look at the bar, medium.
69. *"First kiss at last call"* — the two of them walking backwards down the empty street still talking, tracking from the front.
70. *"Lights up and I don't care at all"* — wide of the street, the bar's windows the only lit thing in the block, slow drift.

### Post-chorus 2 — chant on the street

71. *"Lights up, lights up, and the whole town saw"* — half-second: the bar sign above the door, still lit.
72. *"Lights up, lights up, kiss me in the ugly light"* — half-second: her boots on wet sidewalk, mid-stride.
73. *"Lights up, lights up, and I don't care at all"* — half-second: Kai laughing with his head back.
74. *"Kiss me in the ugly light, kiss me at last call"* — half-second: their hands, fingers already sorted out.

### Outro — the sign goes off

75. *"The bar sign flickers dead behind us on the street"* — the bar sign dying in two stages behind them, the street losing a color, wide static.
76. *"Your jacket on my shoulders and nowhere left to be"* — the olive jacket on her shoulders from behind, his arm just entering frame, tracking slowly.
77. *"Every good light since has come up a little short"* — the two of them getting smaller down the wet street, one working sodium lamp between them and the camera, long lens.
78. *"Worst light in the city and the best night of my life"* — final shot: locked-off wide of the empty wet street, the pair gone out of frame, the single streetlight buzzing, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the door swing, the jukebox, the first clock, the houselight
hit (the loop point), each *"first kiss at last call"*, the alley door, the
fader pull, the instrumental, *"I was ever saving for someone"*, the cut from
white to orange, and the sign going dead. At 120 BPM a bar is 2.0 s; the
choruses cut on the bar and the post-chorus chants cut on the half-bar.

**The ugly-light challenge.** The shareable cut is the vertical chorus, shots
18–25, with the houselight hit on frame one and *"kiss me in the ugly light"*
on screen. Invite people to post their own closing-time frame — phone flash
on, no filter, houselights energy, cut on the flicker. The second shareable
frame is the switch panel in shot 26.

## 6. Quality-control checklist

- Two Mahima looks in the right sections: no jacket until shot 37, jacket on her shoulders from shot 37 to the end and never taken off
- Kai has a face and is lit as clearly as Mahima; every other person in the bar is out of focus, cropped or back-to-camera
- The three light states never blend: warm bar, cold alley, flat fluorescent, with exactly one hard transition between each
- All signage, jukebox panels, phone screens and the beer sign's letters composited in the edit; no model-generated text anywhere
- The houselight hit is the same brightness ramp every time it appears (shots 18, 44, 47) so the loop point is clean
- The imagined candlelit and rooftop shots in the bridge are deliberately flat and empty — they must look worse than the real bar
- No distorted hands in the jukebox, chalk, waist and hand-holding close-ups
- The last shot is locked-off, holds until the audio fades, and no character re-enters frame
