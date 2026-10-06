# Wan 2.2 Shot List — "Beach Bonfire Hearts"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
102 BPM a bar is 2.35 s, so most shots run 3–5 s and the choruses cut every
bar or two.

## 1. Visual style

An Australian beach at night, one long summer night from dusk to dawn.
**The fire is the clock**: it is built in the intro, biggest in the second
chorus, a distant point during the bridge, and coals in the outro. Everything
is lit by fire, headlights, moon or sunrise, never by anything that looks
like a lamp. Warm orange faces against deep blue night, sparks and the Milky
Way. Handheld and close inside the circle, wide and still outside it.

| Section | Grade | Camera |
|---|---|---|
| Intro | Last dusk blue, small new fire, orange faces | Wide, slow |
| Verse 1 / memories | Firelight; the beach-cricket flashback bright, overexposed midday | Handheld close; flashback handheld |
| Pre-choruses | Orange with smoke haze, stars sharp | Over-the-shoulder, push-ins |
| Choruses | Full firelight, sparks, Milky Way | Circling the fire, cutting on the bar |
| Verse 2 | Headlights white from behind, fire orange in front | Close two-shots |
| Instrumental / bridge | Moonlight silver-blue at the water, fire a distant dot | Static wide, silhouettes |
| Final chorus / post-chorus | Fire at full warmth, first grey at the horizon | Fast cuts between faces, stamping feet |
| Outro | Gold dawn, red coals | Locked-off, slow |

## 2. Character bible — paste into every prompt

**Mahima** (the night, at the fire)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and salt-tangled with a few strands across her face, no makeup, sun on her cheeks, wearing an oversized faded navy hoodie over a white singlet and denim shorts, bare feet in the sand, warm open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the beach-cricket flashback, age ten)
> a girl of about ten with dark wavy hair in a messy plait, sunburnt shoulders, a rashie and board shorts, holding a plastic cricket bat on a bright beach at midday, laughing, realistic photography

**Mahima** (dawn)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and salt-tangled, no makeup, wearing the same oversized faded navy hoodie with the sleeves pulled over her hands and a towel round her shoulders, sleepy contented expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the friend who becomes more)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, tanned, wearing a worn grey t-shirt and board shorts, a leather cord bracelet, holding a battered acoustic guitar, easy relaxed grin, realistic cinematic photography, consistent identity

**Kai** (the flashback, age ten)
> a boy of about ten with close-cropped dark hair, bowling a tennis ball on a bright beach, board shorts and no shirt, realistic photography

**The circle** — six to eight friends in their twenties on driftwood logs, hoodies and towels, cans and a guitar; **Kai's brother**, a taller man with the same cropped hair, always in motion; **Kai's sister**, a young woman on the ute tray with a blanket. All friendly, never in sharp focus when the leads are.

Objects: the **battered acoustic guitar** (a sticker on the body, no readable text), the **esky**, the **white ute** on the dune track, the **driftwood logs**, the **fire**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**No screens in this video.** The one thing that could read as text, the
sticker on the guitar, is generated as a blank shape and left blank. Any
on-screen lyric for the challenge cut is composited in the edit.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless. Keyframes first; OpenPose for the dance
and the running shot; Depth for the bedroom compositions. 16:9 first; 9:16 for
the phone-POV cuts, which are natural vertical content. Animate
conservatively: thumb scrolling, screen light flicker, breathing, a hoodie
being pulled on.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s. For this song: lock Kai as well as Mahima, use OpenPose on
every guitar-playing shot (hands on a fretboard are the hardest thing here),
Depth for the wide circle-round-the-fire compositions, and animate the fire,
sparks and wave wash rather than the people wherever possible.

## 4. Scene per lyric line

### Intro — the fire being built

1. *"Sun went down behind the dunes an hour ago"* — wide: an Australian beach below low dunes, the last blue of dusk over the water, a small new fire on the sand with friends arriving carrying driftwood, a white ute parked on the dune track, slow drift.
2. *"Esky full of servo ice and wood to throw"* — close-up of a bag of ice being torn open and tipped into an esky, then a log dropped onto the fire, sparks lifting, handheld.
3. *"Sand's still warm, the southerly's on its way"* — Mahima (night look) sitting on a driftwood log, digging her bare feet into the sand, hair lifting in the first wind, medium, firelight.
4. *"You're on the far side of the fire, same as every day"* — over her shoulder across the flames: Kai on the far log, throwing wood on, grinning at someone off-frame; her looking a beat too long, then down at the fire.

### Verse 1 — the guitar, the ten years

5. *"Your brother brought the guitar and he left it by the logs"* — Kai's brother dropping a battered acoustic guitar against a log and walking off down the beach with two dogs and a couple of the others, wide, firelight fading down the sand.
6. *"You picked it up and tuned it while the others walked the dogs"* — Kai picking the guitar up and tuning it by ear, head tilted, close on his hands on the pegs, the fire behind him.
7. *"Two chords and a shrug, a song we half knew"* — Kai playing two chords with a shrug and a laugh, medium, then Mahima starting to sing along across the fire.
8. *"And I'm singing at the fire but I'm singing it to you"* — Mahima singing, eyes on the fire, then the eyes lifting to Kai who is not looking, close-up, firelight, slow push-in.
9. *"Reckon we've been mates since the summer we were ten"* — flashback, bright overexposed midday: two ten-year-olds playing beach cricket on the same beach, a plastic bat, a tennis ball, handheld.
10. *"Beach cricket, peeling shoulders, I never looked back then"* — flashback: the girl's sunburnt shoulders, the ball going into the water, both kids running after it laughing, then a hard cut back to the fire at night.
11. *"But tonight the sparks go up and something in me turns"* — a log shifting and a column of sparks going straight up, then Mahima's face watching them, her expression changing, close-up.
12. *"Like the wood knows something first, and it's telling me it burns"* — extreme close-up of the fire, wood popping and glowing, then a rack focus to her eyes beyond the flames.

### Pre-chorus 1 — one look

13. *"Everybody's laughing, passing round the last cold drink"* — the circle passing a can from hand to hand, someone telling a story with big gestures, everyone laughing, wide handheld.
14. *"You look up over the flames and I forget to think"* — over Mahima's shoulder: Kai looking up mid-laugh and holding her eyes across the fire for one beat, smoke drifting between them.
15. *"One look, that's all it takes, I'm caught in it now"* — Mahima's face, smoke haze across it, not blinking, extreme close-up, slow push-in.
16. *"I've been standing in the smoke and I'm working out how"* — her standing up and stepping around the smoke to the windward side, wiping her eyes, laughing at herself, medium.

### Chorus 1 — the circle sings

17. *"Beach bonfire hearts, burning slow"* — a slow circle around the fire, every face lit orange, the whole group singing, sparks rising in the middle of the frame.
18. *"Sparks going up where the stars all go"* — tilt up from the sparks to the Milky Way sharp over the beach, wide.
19. *"I've been keeping my hands in my pockets for years"* — close-up of Mahima's hands buried in the pocket of her navy hoodie, then coming out.
20. *"Tonight I'm thinking I'll let it show"* — Kai passing the guitar across the fire and her taking it, both their hands on the neck for a beat, firelit, close.
21. *"Beach bonfire hearts, burning slow"* — Mahima playing, looking straight at Kai, the group singing behind her, medium.
22. *"Salt in your hair and the tide out low"* — Kai's face across the fire, salt-stiff hair, easy grin, then a cut to the wide wet beach and the tide far out under the moon.
23. *"Pass me the guitar, I'll play it till you know"* — her hands on the strings, close-up, the pick catching the light, OpenPose reference for the chord shapes.
24. *"Beach bonfire hearts, burning slow"* — wide from up the dune: the small bright circle on the dark beach, the water beyond, the ute in the foreground.

### Verse 2 — later, the headlights

25. *"Half past ten and the tide's turned, the little kids are gone"* — the beach quieter, towels and buckets gone, small waves closer up the sand, the fire lower and steadier, wide.
26. *"Your sister's on the ute tray with the headlights on"* — Kai's sister sitting on the ute tray with a blanket, the headlights throwing two white beams across the sand toward the fire, wide from the beach.
27. *"You slide across the log and your shoulder's touching mine"* — Kai getting up, walking round the fire and sitting beside Mahima on her log, his shoulder arriving against hers, close two-shot, headlights behind them.
28. *"Say, play the one you used to play, and I run out of time"* — Kai leaning in and asking, easy, her looking down at the guitar and swallowing, close-up.
29. *"So I play it and I miss a chord and you laugh out loud"* — her fingers fumbling a chord, a wrong note, Kai's head going back laughing, medium two-shot.
30. *"Same laugh from a hundred summers, but it's different now"* — a half-second flash of the ten-year-old boy laughing on the bright beach, then Kai laughing now, matched framing.
31. *"You lean in close and say, you've gone quiet, what's wrong"* — Kai's head tilting in close, concerned and fond, his face split between firelight and headlight, close-up.
32. *"And I say, nothing, hey, just listen to the song"* — Mahima's mouth saying it, her eyes saying the opposite, then back to the strings, extreme close-up.

### Pre-chorus 2 — he stops singing

33. *"Everybody's singing, nobody's singing in key"* — the whole circle singing, off-key and happy, arms round shoulders, wide handheld.
34. *"You've stopped singing altogether, you're just looking at me"* — Kai in profile beside her, silent in the middle of the noise, watching her, medium close-up.
35. *"One look, that's all it takes, I'm caught in it now"* — Mahima noticing, turning, the two of them in the middle of the singing not moving, close two-shot.
36. *"I've been standing in the smoke and I'm working out how"* — the headlights switching off behind them, the beach dropping to firelight only, both faces warmer, static.

### Chorus 2 — the fire at its biggest

37. *"Beach bonfire hearts, burning slow"* — the last big log thrown on and the fire roaring up, sparks filling the frame, the group on their feet.
38. *"Sparks going up where the stars all go"* — reuse shot 18, the sparks thicker.
39. *"I've been keeping my hands in my pockets for years"* — Mahima playing the chorus straight at Kai, who is standing now, medium.
40. *"Tonight I'm thinking I'll let it show"* — Kai's sister on the ute tray clocking the two of them and grinning, then pulling the blanket up over her smile.
41. *"Beach bonfire hearts, burning slow"* — a fast cut round the singing faces on the beat, each lit from below.
42. *"Salt in your hair and the tide out low"* — the brother back from the walk with the dogs, dropping onto a log, joining in mid-line.
43. *"Pass me the guitar, I'll play it till you know"* — reuse shot 23, wider, Kai's hand tapping the rhythm on the log beside hers.
44. *"Beach bonfire hearts, burning slow"* — wide from the water's edge looking back: the fire at its brightest, the circle around it, the dunes behind, the brightest frame of the video.

### Instrumental — down to the water

45. The fire settling, Mahima putting the guitar down and standing, looking at Kai once, then walking away from the circle toward the water, her back to camera, out of the firelight.
46. The tide line: small waves, black water, moonlight in a silver line, her footprints filling in the wet sand, tracking low.
47. Kai standing up by the fire, the brother giving him a small shove on the shoulder without looking at him, Kai walking after her.
48. Mahima at the water's edge with her feet in the shallows, arms wrapped round herself, the fire a small orange point far behind her, wide.
49. Kai arriving beside her, both silhouettes against the moonlit water, neither speaking, static wide, the cut into the bridge.

### Bridge — the water, the confession

50. *"Come down to the water where the firelight ends"* — the two silhouettes side by side at the water, the fire far behind, moonlight silver on the wet sand, static wide from the side.
51. *"Where I can't hide behind the chords or the friends"* — Mahima turning to face him, hands moving as she talks, no guitar, medium, blue-silver light.
52. *"Ten summers of almost, I'm done playing it cool"* — her face close, honest, a little scared, the moon on the water behind her, close-up.
53. *"If this wrecks us I'm the fool, but I'd rather be the fool"* — Kai listening, still, his face unreadable, the small waves at their feet, close-up.
54. *"So I say it, I say all of it, I say it low"* — her finishing, looking at the sand, then up, extreme close-up, a long beat.
55. *"And you say, took you long enough, and you kiss me slow"* — Kai's smile breaking, his mouth saying the line, then the kiss, slow, the waves at their feet, a wide two-shot held long.

### Final chorus — back to the fire, the whole beach knows

56. *"Beach bonfire hearts, burning slow"* — the two of them walking back up the beach hand in hand into the firelight, the circle turning and rising, wide from the fire.
57. *"Sparks going up where the stars all go"* — the circle erupting, arms up, someone throwing a handful of sand in the air, sparks and stars behind.
58. *"I kept my hands in my pockets for years"* — close-up of her hand in his, firelit, swinging between them.
59. *"Tonight your hand's in mine and the whole beach knows"* — Mahima laughing and hiding her face in Kai's shoulder as the circle sings at them, medium.
60. *"Beach bonfire hearts, burning slow"* — a fast cut between faces singing the hook at the two of them, on the beat.
61. *"Salt in your hair and the tide out low"* — Kai pulling a strand of her hair out of her face, grinning, close two-shot.
62. *"Your brother's yelling, finally, from across the glow"* — the brother standing on a log on the far side of the fire, arms wide, yelling, the sister on the tray applauding, wide.
63. *"Beach bonfire hearts, burning slow"* — the two of them sitting down on one log with his arm round her, the guitar passed back to her, the circle closing in around them, warm.

### Post-chorus — the singalong

64. *"Burning slow, burning slow"* — feet stamping in the sand, hands clapping, cut on the beat, low angle.
65. *"Ten summers, one spark, and now we know"* — the guitar passing hand to hand across the fire, each pair of hands playing a bar, close.
66. *"Burning slow, burning slow"* — the two of them on the log, her head on his shoulder, singing softly under the chant, close two-shot.
67. *"Sing it round the fire till the embers go"* — the fire visibly lower, the first grey light at the horizon behind the circle, wide, slow.

### Outro — dawn

68. *"Sun's coming up behind the dunes, the fire's just coals"* — wide: the dunes going gold, the fire a ring of red coals, the beach empty and pale, locked-off.
69. *"Everyone's asleep in the tray with sand in their clothes"* — the ute tray: friends asleep under towels and hoodies, sand on their legs, the sister's blanket over two of them, gentle overhead.
70. *"You've got the guitar and you're playing our song"* — Kai by the coals with the guitar, playing the two chords from the start of the night, close on his hands, gold light.
71. *"Two chords and a shrug, and I sing along"* — Mahima (dawn look) with a towel round her shoulders, head on his shoulder, singing softly, close two-shot.
72. *"Sand in the strings and the whole sky gold"* — extreme close-up of sand grains on the guitar's strings and body, then the gold sky over the water.
73. *"Beach bonfire hearts, burning slow"* — final shot: the two of them from behind, sitting by the coals looking at the sunrise over the water, the guitar between them, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first strum, each "beach bonfire hearts", the first look
across the fire (shot 14), the headlights coming on, the instrumental walk
to the water, "took you long enough", the brother's "finally", and the last
strum. At 102 BPM a bar is 2.35 s; choruses cut every bar, verses every two.

**Bonfire singalong challenge.** The chorus is built to be sung badly by a
group. Post the vertical cut of chorus 2 (shots 37–44) with *"beach bonfire
hearts, burning slow"* on screen and invite people to film their own circle
singing it round a fire, sparks in frame, phones up. The second shareable
frame is shot 55, the kiss at the water with *"took you long enough"*.

## 6. Quality-control checklist

- Mahima's night look (navy hoodie, salt-tangled hair, bare feet) from shot 3 to shot 67; the towel and pulled-down sleeves only from shot 71
- Kai recognisable in every shot: cropped hair, short beard, grey t-shirt, the cord bracelet; the ten-year-old flashback pair matched to the adults by hair and build only
- The fire only ever follows the clock: small in the intro, biggest at shot 44, a distant point through shots 45–55, coals from shot 68
- Every guitar shot uses an OpenPose hand reference; no fused fingers on the fretboard
- The brother and sister are supporting faces, never in sharper focus than the leads; the rest of the circle stays soft
- No readable text anywhere: the guitar sticker is a blank shape, the ute has no plates in frame
- Firelight, headlights, moon and sunrise are the only light sources; no lamp-like light on the beach
- The last shot is locked-off and holds until the audio fades
