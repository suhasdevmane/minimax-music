# Wan 2.2 Shot List — "Wine and Whispers"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. At 92 BPM a bar is 2.61 s and the song is
softly swung, so cuts fall on the end of a sung phrase rather than the beat;
most shots run 4–6 s. Take timestamps from the rendered WAV.

## 1. Visual style

One living room, one night, two people, and a window. **Every frame in this
film is lit by fire or by the street.** Two candles and a lamp with a scarf
over it are the only sources inside; the window is the only cool light and it
is always in the background, never on a face. There is no overhead light in
this video at any point, and the one shot where a hand reaches for a wall
switch is a shot of the hand stopping.

The frames get progressively tighter and the room gets progressively darker.
The film ends darker than it began, which is the point: the last candle goes
out and they are still dancing.

Flirtation here is adult and entirely clothed. The camera holds on mouths,
ears, hands, glasses and the space between two people. Nothing else.

| Section | Grade | Camera |
|---|---|---|
| Intro | Deep amber candlelight, hard falloff to black | Static, macro, one wide |
| Verse 1 | Candle from below, both faces half in shadow | Static two-shot, drifting |
| Pre-chorus 1 | One candle in frame, everything else black | Extreme close-up |
| Chorus 1 | Warmest frame of the film, cool window behind | Overhead, wide |
| Verse 2 | Unchanged light, entirely changed faces | Closest lens in the film |
| Pre-chorus 2 | One new flame, the room fractionally brighter | Macro, very close |
| Chorus 2 | Fuller, closer, the pool of light smaller | Overhead, slow tilt |
| Instrumental | Suspended, no cuts on the beat | Slow drift, macro |
| Bridge | A single candle, most of the frame black | Fragments only |
| Final chorus | The dimmest and warmest the room gets | Standing wides |
| Post-chorus | Unchanged, four repeating beats | Static macro |
| Outro | Window light only after the candle dies | Locked-off, wide |

## 2. Character bible — paste into every prompt

**Mahima** (one look, the whole film)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly undone, soft evening makeup mostly worn off, wearing a deep burgundy silk slip top and wide black trousers, barefoot, open unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a black knitted jumper with the sleeves pushed up and dark trousers, barefoot, a watch he has not taken off, thoughtful guarded expression that opens across the film, realistic cinematic photography, consistent identity

No other people appear in this video. The one figure in a flashback — a man
sitting in a parked car outside a restaurant, not getting out — is Kai seen
from behind through a windscreen, faceless. The empty room in the second
flashback has no one in it at all.

Objects that carry the film and must stay consistent: the **two candles**
burned down to stubs in a saucer, the **open bottle with the cork beside it**
(label always turned away from camera), the **drawer with two dark phones in
it**, the **lamp with a scarf over the shade**, the **two glasses** which are
never both at the same level, the **turntable and the stack of sleeves** in
the corner, seen only in wides, and the **rug that gets rolled back** in the
final chorus.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The bottle label, the record sleeves and any signage on the street outside
the window are composited or turned away in the edit.** Generate them blank
or reversed — the model cannot render legible text, and a readable label
would date the film and break the take.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima and Kai with IP-Adapter or a character LoRA; only two identities
in the whole film. Depth is the critical ControlNet here — one room shot from
a dozen positions, and the geometry has to hold between the doorway wide in
shot 1 and the identical doorway wide in shot 71. Use OpenPose only for the
standing-up sequence and the final slow dance.

Candlelight is the hard part. Generate every plate with a warm practical key
from below at a fixed position and animate the flicker as a brightness
oscillation in the edit rather than asking the model for moving fire — model-
generated flame is where this video will fall apart. The one exception is the
match strike at shot 46, which is worth a dedicated generation.

Animate at a whisper. Nothing in this film moves faster than a head turning:
wax running, a chest rising, a hand setting a glass down, rain on glass, two
people turning very slowly at the end. 16:9 first; 9:16 for the bridge
fragments, which are the natural vertical content.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s.

## 4. Scene per lyric line

### Intro — the room

1. *"Two candles burned to nothing and the wax on the floor"* — macro on two candles burned to stubs in a saucer, wax spilled over the rim onto bare boards, flame low, static.
2. *"The good bottle open that we swore we'd save for more"* — a bottle standing open on the floorboards with the cork beside it, the label turned away from camera, one candle out of focus behind it.
3. *"Phones in a drawer where we can't hear them ring"* — a drawer sliding shut on two dark phone screens, a hand withdrawing, macro.
4. *"And the rain out there doing its own quiet thing"* — the window from inside: rain running down the outside, the street lights broken up in it, the candlelit room reflected faintly in the glass.

### Verse 1 — the safe confessions

5. *"You start with a small one, something safe and half a joke"* — the two of them on the floor with their backs against the sofa, a foot of space between them, Kai talking with a glass on his knee, wide two-shot.
6. *"You say you nearly cancelled, sat outside and never spoke"* — two-second flash: a parked car outside a restaurant at night, a man behind the windscreen not getting out, cold blue, faceless.
7. *"So I tell you that I looked you up before we met"* — Mahima covering her face with one hand, laughing at herself, admitting it anyway, close-up in candlelight.
8. *"Went four years back on a Sunday, not embarrassed yet"* — her hand coming down off her face, entirely unrepentant, a slow shrug, close-up.
9. *"There's a trumpet somewhere low, doing something to the room"* — a wide of the corner with a turntable and a stack of sleeves on the floor beside it, never in macro, the room dark around it.
10. *"Making everything we say sound truer than it should"* — a slow drift across the room past both candles to the two of them, the lens getting tighter as it goes.
11. *"Your glass goes down an inch, my voice goes down a tone"* — two glasses on the boards, one measurably lower than the other, macro, a hand entering to set the second one down.
12. *"And the loudest thing in here is what we haven't shown"* — a held two-shot where neither of them says anything for four bars, both looking at the window, static.

### Pre-chorus 1 — the light stays off

13. *"Don't turn the big light on, leave it where it is"* — a hand reaching toward a wall switch and stopping an inch short, macro, the switch never touched.
14. *"Everything looks kinder at the edge of a wick"* — extreme macro on a candle wick at the moment the flame leans, the wax pooling around it.
15. *"Say the next one closer, say it near my ear"* — Mahima turning her head so her ear is nearer his mouth than her eyes are to his, profile close-up.
16. *"The only thing worth having is the thing you're scared to hear"* — extreme close-up on a mouth moving with nothing audible behind it, one candle's worth of light.

### Chorus 1 — the pool of light

17. *"Wine and whispers, keep the lights down low"* — an overhead of the whole room: the two of them small in a pool of candlelight on a dark floor, everything else black.
18. *"Tell me something true, then something slow"* — the two of them from floor level, the candles between camera and them, both faces warm and half lost.
19. *"The street can have the shouting, the street can have the rain"* — a wide of the window with the wet street beyond, a car passing, a distant figure shouting to someone, all of it outside.
20. *"In here we say it quiet and we say it plain"* — back inside, the same two-shot as shot 5 with the space between them measurably smaller, static.
21. *"Wine and whispers, the hours going soft"* — a candle guttering and being entirely ignored by both of them, macro, the flame recovering.
22. *"Nothing in this room is getting turned off"* — the lamp with the scarf over its shade, glowing dull orange, static, the only manufactured light in the film.
23. *"Move a little closer, let the candles go"* — her foot moving six inches across the boards toward his, macro, the smallest movement in the video.
24. *"Wine and whispers, keep the lights down low"* — the overhead again, tighter, the pool of light smaller, the two of them nearer its centre.

### Verse 2 — the true confessions

25. *"Somewhere past the second glass you stop performing"* — Kai's face with the laughing gone out of it, one candle, closest lens used so far.
26. *"And you tell me about a year you never say aloud"* — two-second flash: an unfamiliar living room floor with a folded blanket on it, cold morning light, nobody in the room.
27. *"How you slept on a friend's floor and called it fine"* — back to his face, telling it flatly, no self-pity, close-up, static.
28. *"And how you still won't sit with your back to a crowd"* — a wide showing where he has chosen to sit: back to the wall, the room in front of him, and her noticing him do it.
29. *"Then you ask me what I'm scared of and I nearly lie"* — Mahima opening her mouth on the easy answer and stopping, a long hold on her face while she decides, extreme close-up.
30. *"And I say the real one and it comes out small"* — the line said very quietly in one unbroken take, no cutaway, candlelight on one side of her face only.
31. *"That I'm easy to leave and I've been left before"* — his face receiving it, not reacting, not looking away, close-up.
32. *"And you set your glass down and don't argue at all"* — his hand setting a glass down on the boards without a sound and staying flat on the wood, macro.

### Pre-chorus 2 — a new flame

33. *"Don't turn the big light on, we're better in the dark"* — the wall switch again from a different angle, this time with nobody near it, static.
34. *"Everything looks braver at the edge of a spark"* — a match struck to relight a candle, the flare filling the frame for one beat, then settling — the only real fire generation in the film.
35. *"Say the next one closer, say it near my ear"* — both of them closer than any previous shot, her ear and his mouth, nothing else in focus.
36. *"The only thing worth having is the thing you're scared to hear"* — reuse shot 16's framing on his mouth instead of hers, the reverse of the first pre-chorus.

### Chorus 2 — closer

37. *"Wine and whispers, keep the lights down low"* — the overhead a third time, the pool smaller again, their shoulders now touching.
38. *"Tell me something true, then something slow"* — a slow tilt across the ceiling with the trumpet countermelody, the candlelight moving on the plaster, no people in frame.
39. *"The street can have the shouting, the street can have the rain"* — the window with the rain harder on it, the street emptier than before, static.
40. *"In here we say it quiet and we say it plain"* — two glasses side by side on the boards, both nearly empty, macro.
41. *"Wine and whispers, the hours going soft"* — wax running down the side of a candle in real time, macro, the pool spreading on the saucer.
42. *"Nothing in this room is getting turned off"* — a wide of the whole flat beyond the doorway, every other room dark, only this one lit.
43. *"Move a little closer, let the candles go"* — her head coming down onto his shoulder, seen from behind them both, wide.
44. *"Wine and whispers, keep the lights down low"* — both of them looking at the window from the floor, the rain on their faces in reflection, static two-shot.

### Instrumental — suspended

45. The muted-trumpet solo carried by the room: a slow drift from the corner turntable across the whole space, no people for eight bars.
46. Wax running down a candle in extreme macro, the flame steady above it.
47. Rain on the glass in extreme macro, the street lights broken into shapes in the drops.
48. A wide of the two of them not talking, her head on his shoulder, both looking at the window, held long.
49. The turntable arm reaching the end of a side and lifting itself, seen once in a wide from across the room — the cut into the bridge.

### Bridge — fragments only

50. *"There's a volume you can only say the big things at"* — extreme close-up: her mouth beside his jaw, the shot cropped so neither face is complete.
51. *"And it's lower than a room, it's lower than that"* — his ear and the edge of her hair, single candle, most of the frame black.
52. *"So I say it to the air beside your jaw"* — the words moving on her lips with nothing audible in the mix, macro, no context in frame.
53. *"The one I've never said to anybody before"* — his eyes closing, extreme close-up, one flame reflected in the lash line.
54. *"You don't answer with a speech, you just breathe out slow"* — his chest rising and falling once, slowly, under the knit of the jumper, macro.
55. *"And you say it back to me at the same level, low"* — his mouth at her ear, answering, and her eyes opening, the first fragment where both of them are in frame at once.

### Final chorus — standing up

56. *"Wine and whispers, keep the lights down low"* — the two of them standing up for the first time in the film, from the floor, wide, slow.
57. *"Tell me something true, then something slow"* — a coffee table being pushed aside with a bare foot, macro, the sound implied.
58. *"The street can have the shouting, the street can have the rain"* — the window one last time, the rain easing, the street entirely empty now.
59. *"We said the whole thing quiet and it came out plain"* — a rug being rolled back with two hands, the bare boards appearing underneath, wide.
60. *"Wine and whispers, the hours going soft"* — the last candle down to a puddle of wax with a flame still standing on it, macro.
61. *"The candle's on its last and we're not moving off"* — both of them standing in the cleared space, not dancing yet, arms at their sides, wide.
62. *"Push the table back and let the small hours go"* — an overhead of the cleared floor with two people standing in the middle of it, the smallest pool of light yet.
63. *"Wine and whispers, keep the lights down low"* — a two-shot at shoulder height, his hand coming up to her back, held.

### Post-chorus — four beats

64. *"Low, low, keep the lights down low"* — the last candle, macro, still burning.
65. *"Nothing in this room has anywhere to go"* — the window, static, rain almost stopped.
66. *"Low, low, keep the lights down low"* — two bare feet on bare boards, close, barely moving.
67. *"Wine and whispers, and the rest of it slow"* — a hand flat on a back, macro, the knit of the jumper under her fingers.

### Outro — the dance with nothing playing

68. *"Sofa pushed back and the rug rolled aside"* — a wide from the doorway, the exact framing of shot 1, the room rearranged and the candle nearly gone.
69. *"Your hand at my back and the last of the wine"* — the two of them turning very slowly in the cleared space with nothing playing on screen, medium.
70. *"No music left but we're still going round"* — the last candle going out on its own, the room dropping to window light in real time, macro into darkness.
71. *"And the loudest thing in here is not a sound"* — final shot: the two of them still turning in near-dark, lit only by the window, barely moving, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first candle frame, each *"keep the lights down low"*, the
match strike at shot 34, the confession at shot 30, the instrumental, the
first bridge fragment at shot 50, the standing-up at shot 56, and the candle
going out. At 92 BPM a bar is 2.61 s, but cut on the end of the sung phrase —
this song has a swung feel and cutting on the beat will fight it.

**The whispered-confession cut.** Post shots 50–55 vertical, the bridge, with
no audio but the piano, and invite people to film the thing they would only
say at that volume — mouth to camera, unheard. The second shareable frame is
shot 17, the overhead of two people in a pool of candlelight, captioned
*"There's a volume you can only say the big things at."*

## 6. Quality-control checklist

- One look for each lead across the whole film; nobody changes clothes and nobody puts shoes on
- No overhead light appears in any frame, and the wall switch is never touched
- The window is the only cool light in the film and it never falls on a face
- Candle flicker is added in the edit as a brightness oscillation, not generated, except the match strike at shot 34
- The pool of light gets measurably smaller at shots 17, 24, 37 and 62, in that order
- The bridge is shot entirely in fragments; no complete face appears in shots 50 to 54
- The bottle label and the record sleeves are turned away or composited; no model-generated text
- Shot 68 matches shot 1 exactly in framing, and the film ends darker than it began
- The last shot is locked-off and holds until the audio fades
