# Wan 2.2 Shot List — "Rooftop Radio"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
120 BPM a bar is 2.0 s, so most shots are 2–4 s and the choruses cut on the
bar.

## 1. Visual style

One location, one evening, one roof. The video runs continuously from golden
hour to dawn and **the light is the clock**: gold, then blue hour, then
midnight warm, then grey-gold morning. No shot ever goes back to an earlier
time of day. The only real light sources are practical — the sun, a string of
fairy lights on the water tank, one clamp work lamp, phone torches, and the
city itself. Handheld and inside the crowd for the verses; wide, craned and
drone-scale for the choruses. The **radio is a character**: it is in frame or
audible in every section, and the last shot belongs to it.

| Section | Grade | Camera |
|---|---|---|
| Intro | Dim green stairwell, then blown-out warm gold | Handheld climb, then a wide reveal |
| Verse 1 | Golden hour, hard shadows, warm skin | Handheld, close, working hands |
| Pre-chorus | Blue hour, faces lit by string lights only | Locked-off, comic stillness |
| Choruses | Warm gold against deep blue, dense | Circling handheld, crane and drone |
| Post-chorus | Hard phone-torch flashes, high contrast | Four ultra-fast cuts, one per line |
| Verse 2 | Midnight blue with warm pools | Handheld, portrait-close |
| Instrumental | Blue exterior, one hard practical macro | Drone rise, then a push into the speaker |
| Bridge | String lights only, everything else soft | Static, held portraits |
| Final chorus | Brightest of the video | Crane pull-back, drone |
| Outro | Clean cool dawn, no tricks | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a few strands stuck to her temple from the heat, minimal makeup, wearing a cropped white tank top and high-waisted denim shorts with a thin gold chain, open delighted expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge and outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pushed back off her face, no makeup left, wearing the same cropped white tank top with an oversized denim shirt open over it, tired contented expression, realistic cinematic photography, consistent identity, natural skin texture

There is **no romantic male lead in this video** and no Kai. The people on
the roof are neighbours, and they are shot as a community, not as couples.

**The neighbour** — the third-floor woman, the emotional centre of verse two.
> a woman in her seventies, silver hair pinned up, gold hoop earrings, a loose floral housedress, holding a folding paper fan, warm knowing expression

**The crowd** — twelve to forty people of mixed ages and builds across the
night: a man still in a work shirt with a name tag, two kids of about ten on
the parapet, a young man on the phone, a woman asleep in a folding chair.
Faces are welcome here; nobody is faceless in this song.

Objects that must stay consistent: the **battered silver transistor radio**
with a bent telescopic antenna wrapped in kitchen foil, the **wooden water
tank** with fairy lights tied around its legs, the **orange cooler**, the
stack of **metal folding chairs**, the **upturned crate** the radio stands on.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, phone displays, signage and any readable lettering are
composited in the edit.** Generate phones as lit blank rectangles. The radio
dial must never carry legible station numbers — shoot it as a glowing amber
strip and add nothing.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA; lock the
neighbour separately, she recurs in six shots. Keyframes first; OpenPose for
every dance shot and the water-tank climb; Depth for the wide rooftop
compositions so the skyline sits behind the parapet correctly. 16:9 first;
9:16 recomposition for the pre-chorus freeze and the post-chorus chant, which
are the vertical clips. Animate conservatively: a dial being turned, foil
being adjusted, a cooler dragged one step, hair moving in one gust. Crowd
shots are the hard ones — generate them at 81 frames and cut them short
rather than asking the model for long continuous group motion.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; chorus and post-chorus shots 2 s.

## 4. Scene per lyric line

### Intro — the climb and the hatch

1. *"Six flights up with a radio under my arm"* — Mahima climbing a hot narrow stairwell, the silver radio clamped against her hip, wired-glass window light striping her shoulders, handheld from behind, dim green.
2. *"Tar still soft from the heat of the day"* — extreme close-up of a sneaker pressing into soft black roof tar and leaving a shallow print, macro, gold light.
3. *"Somebody propped the hatch with an empty paint can"* — a rusted roof hatch pushed up from below and wedged with a dented paint can, low angle from inside the stairwell, sky blowing out white above it.
4. *"And the whole sky opened up our way"* — her head and shoulders rising through the hatch into an enormous pink-and-gold sky, wide, the frame resolving from white.
5. *"Nobody called it, nobody planned it"* — the roof as found: vent pipes, laundry line, the water tank, three people already sitting on the parapet, static wide.
6. *"It just started playing and we stayed"* — the radio set down on an upturned crate, her thumb turning it on, the first tinny sound, close-up.

### Verse 1 — building the room

7. *"Landlord's gone to Miami till the end of July"* — a padlock hanging open on the hatch frame, a hand flicking it, then the group walking past it, close then wide.
8. *"Nobody up here's asking who's allowed tonight"* — a low wide from the parapet: the whole roof, the tank, the skyline behind, six people spreading out into it.
9. *"A fresh pack of batteries, a dial that sticks"* — macro on a battery pack being torn open with teeth, two batteries thumbed into the back of the radio.
10. *"One old silver radio and a hundred feet of bricks"* — the radio in the foreground on the crate, rack-focus to the brick parapet and the drop to the street six floors below.
11. *"Girl from the fourth floor hauled a cooler up the stairs"* — the orange cooler dragged up the last flight one step at a time, ice sloshing, her friend laughing and swearing silently, handheld low.
12. *"Somebody's cousin showed up with a stack of folding chairs"* — metal folding chairs opened one after another on the beat, four cuts inside the one shot, gold light.
13. *"We swept the broken glass and strung a line of lights"* — a broom pushing glass into a dustpan, then hands passing fairy lights up the ladder of the water tank.
14. *"And the water tank's a stage if you can climb it right"* — Mahima climbing the tank ladder in three moves and standing up on the platform, shot from below at a wide angle, the sun going down behind her.

### Pre-chorus 1 — the antenna and the freeze

15. *"Antenna wrapped in foil and pointed at the moon"* — extreme close-up: kitchen foil wound around a bent telescopic antenna, fingers adjusting it a millimetre, the moon soft behind.
16. *"Hold it still, hold it still, there it is, that's the tune"* — eight people stood dead still around the radio with their hands half-raised, nobody breathing, locked-off wide, blue hour.
17. *"Everybody freeze, then everybody move"* — the same frame, held one more beat, one person's shoulders starting to shake with laughter.
18. *"On three, on two"* — a fast push-in on the volume wheel, a thumb on it, the string lights coming on in the background on the cut.

### Chorus 1 — the roof goes off

19. *"Rooftop radio, turn it up, let the whole block know"* — the volume wheel cranked and the group breaking into dancing all at once, circling handheld, radio in the middle like a fire.
20. *"We got no permit and we got nowhere else to go"* — a wide from the far corner of the roof: the whole group moving, the dark grid of neighbouring rooftops around them.
21. *"Antenna in the air like a hand in the air"* — a match cut, the foil antenna against the sky, then forty fingers of one raised hand in the same position and light.
22. *"And the city's looking up at us like we put it there"* — Mahima on the water tank, arms open, skyline behind her, very wide low angle, the hero frame of the video.
23. *"Rooftop radio, turn it up, let the whole block know"* — inside the crowd, spinning handheld, faces flashing past, string lights streaking.
24. *"Everybody dancing on a roof that isn't ours"* — feet only on soft tar, twelve pairs, dust lifting, low macro tracking.
25. *"Half the song is static and we sing the rest out loud"* — a two-shot of two friends singing straight into each other's faces, missing a word and shouting through it.
26. *"Six flights over Sunday, and tonight we are the sound"* — drone pull-back: one lit rooftop in a dark grid of rooftops, the city beyond.

### Post-chorus 1 — the chant

27. *"Turn it up, turn it up, let the whole block know"* — a hand cranking the volume wheel, half a second, hard cut.
28. *"Turn it up, turn it up, till the batteries go"* — the radio's battery door with a strip of tape holding it shut, macro, half a second.
29. *"Hands on the water tank and feet down on the tar"* — palms slapping the wooden tank in rhythm, then feet stamping tar, two half-second cuts.
30. *"Turn it up, turn it up, that's how loud we are"* — the whole group jumping on the last beat and landing together, wide, phone torches flaring across the lens.

### Verse 2 — the block arrives

31. *"The lady on the third floor leaned out to complain"* — from the parapet looking down the building's face: a third-floor sash window sliding up, the neighbour leaning out, unimpressed.
32. *"Then she caught the chorus and she asked us for a name"* — her head tilting, her hand going still on the sill, listening, close-up from a floor above.
33. *"Now she's up here with a plate and a folding paper fan"* — the neighbour stepping through the hatch onto the roof, plate in one hand, paper fan in the other, everyone turning.
34. *"Saying she danced to this one back before the block began"* — the neighbour showing two young dancers how the step actually goes, her feet, then her face, the best-lit face in the video.
35. *"The guy from the corner store brought ice up in a crate"* — a crate of bagged ice hoisted through the hatch by two pairs of hands, condensation on the plastic, macro then wide.
36. *"Two kids from the stairwell swore they'd only stay till eight"* — two ten-year-olds sitting on the parapet with ice pops, legs swinging, refusing to go inside, medium.
37. *"At midnight the dial slipped and found a song from way back when"* — a dancing elbow knocking the radio, the dial jogging, a burst of static, then a clean older song, extreme close-up on the amber dial strip.
38. *"And nobody knew how, but every one of us came in"* — the whole roof singing the same line at once, phones down, mouths wide, slow push-in through the crowd.

### Pre-chorus 2 — the squad car

39. *"A squad car turned the corner, slowed down and drove away"* — straight down from the parapet: a patrol car rolling along the street, light bar dark, pausing, then moving on.
40. *"Somebody's grandmother is teaching me to sway"* — the neighbour taking Mahima's hands and moving her feet for her, medium two-shot, everyone else out of focus.
41. *"Everybody freeze, then everybody move"* — the roof genuinely frozen mid-dance, forty people, then collapsing into laughter, locked-off wide.
42. *"On three, on two"* — a red and blue wash crossing the brick wall behind them and vanishing, then the push-in on the volume wheel again, faster.

### Chorus 2 — forty people

43. *"Rooftop radio, turn it up, let the whole block know"* — the same circling handheld as shot 19 but the crowd is now three times bigger and the camera has to fight through it.
44. *"We got no permit and we got nowhere else to go"* — windows opening one after another down the street, people leaning out and staying, from the roof edge.
45. *"Antenna in the air like a hand in the air"* — reuse the antenna macro from shot 21, tighter, with a warm crowd bokeh behind it.
46. *"And the city's looking up at us like we put it there"* — Mahima on the tank again, this time with three others up there with her, wider, arms linked.
47. *"Rooftop radio, turn it up, let the whole block know"* — a static wide of the whole roof from the far parapet, everyone in frame, string lights swinging.
48. *"Everybody dancing on a roof that isn't ours"* — forty pairs of feet on tar, low macro, dust and bottle caps.
49. *"Half the song is static and we sing the rest out loud"* — the neighbour and the two kids singing the same line, three-shot, generations in one frame.
50. *"Six flights over Sunday, and tonight we are the sound"* — a slow drone orbit around the lit roof, the city turning behind it.

### Post-chorus 2 — chant, bigger

51. *"Turn it up, turn it up, let the whole block know"* — forty hands going up in one beat, wide, half a second.
52. *"Turn it up, turn it up, till the batteries go"* — the radio on its crate in the middle of stamping feet, shot from ground level, half a second.
53. *"Hands on the water tank and feet down on the tar"* — a dozen palms hitting the wooden tank in unison, macro, the wood ringing.
54. *"Turn it up, turn it up, that's how loud we are"* — the whole roof jumping and landing, the tank rocking a few inches, everyone laughing at it, wide.

### Instrumental — bass and percussion breakdown

55. A slow drone rise straight up off the roof, the lit rectangle shrinking into a dark grid of blocks, the sound thinning as the camera climbs.
56. Ground level on the street: two strangers walking past stop, look up, and stay looking up, low angle, sodium light.
57. A kid on the parapet hitting a cowbell with a spoon, dead on the beat, macro, string lights behind.
58. A push all the way into the radio's mesh grille until it fills the frame, the mix filtering down to thin mono as it lands.
59. A hard cut back out: the full roof at full width and full stereo again, the crowd hitting the downbeat together.

### Bridge — the quiet middle

60. *"None of us own a window with a view"* — Mahima sitting on the parapet with her back to the city, cup in both hands, catching her breath, static medium, string lights only.
61. *"We split a rent that we can barely do"* — held portrait, two seconds: a man still in his work shirt with the name tag on, smiling at something off frame.
62. *"But nobody lives above the sixth floor sky"* — a straight-up shot from flat on the tar: the string lights, the wires, and the small amount of sky a city gives you.
63. *"And nobody's charging extra for the night"* — held portrait: a woman asleep sitting upright in a folding chair, paper plate on her lap, undisturbed.
64. *"So play it for the ones who worked all week"* — held portrait: a young man on the phone at the far parapet, talking to someone far away, smiling.
65. *"Play it for the ones who couldn't sleep"* — Mahima's hand resting on top of the radio, not turning it, just resting there, macro.
66. *"Play it till the tar goes cool and the east turns gold"* — the eastern sky beginning to lift, the first grey line above the rooftops, wide and still.
67. *"Play it till the batteries go cold"* — her face lit by the amber dial from below, eyes on the horizon, close-up, the last still moment before the lift.

### Final chorus — every window open

68. *"Rooftop radio, turn it up, let the whole block know"* — a crane move starting tight on her on the water tank and beginning to pull back and up.
69. *"We got no permit and we got nowhere else to go"* — the same move continuing until four other rooftops are in frame, each with people on them, all facing this one.
70. *"Antenna in the air like a hand in the air"* — the antenna against a sky that is no longer black, the foil catching first light.
71. *"And the city's looking up at us like we put it there"* — from a neighbouring roof looking back: this roof, lit and full, the only bright thing in the grid.
72. *"Rooftop radio, turn it up, let the whole block know"* — inside the crowd one last time, the neighbour in the middle of it, everyone around her.
73. *"Every window on the street is open now"* — a slow lateral track along the building faces: every window lit, every window open, people in all of them.
74. *"Half the song is static and we sing the rest out loud"* — the group jumping in unison, the tank rocking, shot from the tank platform looking down at them.
75. *"Six flights over Sunday, and tonight we are the sound"* — the widest drone frame of the video, the lit roof and the four lit roofs around it, dawn just starting at the edge.

### Post-chorus 3 — last chant

76. *"Turn it up, turn it up, let the whole block know"* — forty hands, from ground level on the tar, half a second.
77. *"Turn it up, turn it up, till the batteries go"* — the volume wheel already at its stop, a thumb pushing it anyway, macro.
78. *"Hands on the water tank and feet down on the tar"* — palms on wood, feet on tar, two cuts, the light noticeably greyer now.
79. *"Turn it up, turn it up, that's how loud we are"* — the last jump, held a beat longer than the earlier ones, everybody landing tired and grinning.

### Outro — dawn and dead batteries

80. *"Sun coming up behind the tank and the wires"* — grey-gold first light behind the water tank and the overhead wires, the fairy lights still on and now pointless, wide and still.
81. *"Somebody's asleep in a folding chair"* — the sleeping woman again, now in daylight, a jacket over her that wasn't there before, medium.
82. *"The radio is still going on the last of the batteries"* — the radio alone on the crate, volume low, static rising under the song, slow push-in, macro on the dying amber dial.
83. *"And the whole block knows, and the whole block knows"* — final shot: locked-off wide of the empty-ish roof at dawn with the radio still playing, the neighbour's paper fan left on the parapet, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the hatch opening, the first volume crank, each *"rooftop
radio"*, both freeze beats, the dial slip at midnight, the instrumental drone
rise, *"nobody lives above the sixth floor sky"*, the modulation, and the
final static. At 120 BPM a bar is 2.0 s; the choruses cut on the bar and the
post-chorus cuts on the half-bar.

**The freeze challenge.** Shots 15–19 are the shareable unit: a group stands
dead still around a speaker through *"hold it still, hold it still"* and
explodes on *"on three, on two."* Post it vertical with the countdown on
screen and it duets itself. Second clip: shots 31–34, the neighbour arriving
to complain and staying to dance — the emotional cut, captioned *"she danced
to this one before the block began."*

**Caption:** *"We got no permit and we got nowhere else to go."*

## 6. Quality-control checklist

- Time of day only ever moves forward: gold, blue, midnight, grey dawn. No shot is warmer or earlier than the one before it except the two deliberate portrait holds in the bridge.
- Mahima is in the tank-top look until shot 60 and the denim-shirt look from shot 60 on; the shirt never appears earlier.
- The radio is in frame or clearly audible in every section and is the subject of the last shot.
- The foil-wrapped antenna, the fairy-lit water tank, the orange cooler and the upturned crate are identical in every appearance.
- The neighbour recurs in shots 31, 32, 33, 34, 40 and 72 with the same fan and earrings.
- No readable text anywhere: no station numbers on the dial, no signage, no phone screens; all lettering composited in the edit.
- Crowd shots have no duplicated faces and no distorted hands, especially the forty-hands frames.
- The squad car never turns its light bar on and never stops; the video has no antagonist.
- The last shot is locked-off and holds until the audio fades to static.
