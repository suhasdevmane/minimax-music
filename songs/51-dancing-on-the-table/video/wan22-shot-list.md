# Wan 2.2 Shot List — "Dancing on the Table"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
128 BPM a bar is 1.88 s, so most shots are 2–4 s and the choruses cut close
to every bar.

## 1. Visual style

One backyard, one night, one table. The whole video is a **single continuous
party** from two in the morning to sunrise, and the only progression is how
many people are up on the wood. Practical light only: string lights strung
from fence to fig tree, an open kitchen door, a couple of phone torches, then
daylight. Warm, saturated, hand-held, slightly over-exposed on the highlights.
No CGI, no colour-grade tricks beyond a warm film curve. Motion blur and
imperfect framing are wanted — this should look shot by somebody who was
also at the party.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm string lights, deep blue sky, kitchen window glow | Slow drift, wide |
| Verse 1 | Candle plus one light run, the far end darker | Static two-shots, close |
| Pre-chorus | Warm, faces lit from behind | Fast handheld, short lens |
| Choruses | Brightest practicals, every bulb, kitchen door open | Low angles up the table, circling |
| Post-chorus | Same, flared by a phone torch | Ultra-fast cuts, 0.5 s |
| Verse 2 | Cooler at his seat, warming as the lights come up | Handheld, POV-leaning |
| Instrumental | Warm, hazy, kitchen smoke | Inside-the-circle, roaming |
| Bridge | Half the lights off, first blue of dawn | Static, wide, quiet |
| Final chorus | Widest and warmest frame of the video | Crane-style wide, sweeping |
| Outro | First sun, long shadows, string lights redundant | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (through the night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned up with strands falling loose, warm evening makeup slightly worn off, wearing a deep red satin wedding-guest slip dress, bare feet, delighted breathless expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (outro, sunrise)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair fully down and messy, makeup worn away, wearing a deep red satin slip dress with an oversized charcoal suit jacket over her shoulders, bare feet, tired contented expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a white dress shirt with the sleeves rolled and the collar open, a charcoal suit jacket that later comes off, no tie, warm open expression, realistic cinematic photography, consistent identity

**The family** — a real crowd, not extras: a grandmother in a folding chair
with a phone held level with her hairline, three aunts, a teenage cousin on
the speaker, an uncle with a cowbell, a father spinning a napkin, a
twelve-year-old drumming an upturned bucket, the newly married couple
watching from the porch steps. Faces welcome; they are family, not exes.

Objects: the **long trestle table**, the **cowbell**, **two sandals in the
grass**, the **collapsed cake**, the **red splash on a white collar**, the
**fresh scratch in the varnish**, the **charcoal suit jacket**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, phone displays, seating cards and any signage are composited
in the edit.** Generate the grandmother's phone as a lit blank rectangle and
overlay the vertical-video UI in post; the model cannot render legible text
and a wedding is full of it.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock both leads with IP-Adapter or a character LoRA each, referenced front,
three-quarter, profile and full body, seated and mid-dance. **OpenPose is
essential** for every shot on the table — climbing up, the hand-off, the
spin, the crowd's raised arms — or the model invents limbs. Depth for the
long-table compositions and the crane-style wides. 16:9 first; 9:16
recomposition for the table-climb hook cut. Animate in short bursts: one
step up, one spin, one clap cycle per clip; a crowd dancing for four seconds
is more reliable as three two-second pieces cut together than one long
generation.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — the leftovers

1. *"Caterers gone, and the cake is a crime scene"* — slow drift across a backyard at two in the morning, a half-collapsed wedding cake on a side table with a knife still in it, warm string lights, deep blue sky, wide.
2. *"String lights still swinging where the big tent had been"* — the marquee half down, poles leaning, string lights swinging gently on their own, low angle into the sky, static.
3. *"Somebody's cousin took over the sound"* — a teenage cousin crouched over a borrowed speaker with a phone cable (screen composited), the first beat landing, close-up.
4. *"And nobody left in this yard is sitting down"* — a slow pan across folding chairs, all empty, all pushed back at angles, people standing beyond them, wide.
5. *"Forks in the sink and the chairs pushed aside"* — through the open kitchen door: a sink stacked with forks and plates, one aunt drying her hands and heading back out, warm interior light.
6. *"And you at the far end, catching my eye"* — the length of the long trestle table in one shot: Mahima at the near end with her shoes in her hand, Kai at the far end, both looking, shallow focus racking from her to him.

### Verse 1 — the singles table

7. *"They sat us with the singles where the music didn't go"* — two-shot across a guttering candle at the dark end of the table, both angled away from the empty dance floor, static.
8. *"Two strangers and a candle that was burning very slow"* — macro of the candle, wax down the side, one moth, the two of them soft behind it.
9. *"You said your mother's cousin married my best friend"* — Kai talking with his hand doing the family-tree gesture, Mahima following it with her eyes, medium close-up.
10. *"I said we will be family by the time this weekend ends"* — Mahima flicking a seating card over between her fingers (blank card, UI composited if needed), a dry smile, close-up on hands then face.
11. *"I took the last empanada, you took half of mine"* — both hands arriving at the same plate, a half taken, an eyebrow, close-up on the plate.
12. *"You poured me something red and swore that it was fine"* — a bottle poured into a plastic cup past the sensible line, her looking at it, his shrug, close two-shot.
13. *"The band packed up their trumpets at a quarter after one"* — two musicians zipping instrument cases by the fence, the last brass note dying, medium wide.
14. *"And that is the exact minute this party had begun"* — the speaker kicking in over the band's silence, heads turning across the yard, wide handheld.
15. *"The long wood was all empty and the string lights hung low"* — a clean wide of the cleared table, nobody on it, lights sagging above it, static, held one beat longer than the others.
16. *"And the whole yard was waiting for somebody to go"* — a slow pan of faces all pointed at the same empty table, nobody moving, medium wide.

### Pre-chorus 1 — the countdown

17. *"One shoe on and one shoe gone"* — one sandal dropping into the grass in slow motion, her other foot still in its shoe, macro.
18. *"Cowbell hitting like a countdown song"* — an uncle striking a hand-held cowbell on the beat, close-up on the metal and his grin.
19. *"Grandmother clapping, the aunties know"* — the grandmother in a folding chair starting a slow clap on the two and the four, three aunts turning to each other behind her, medium.
20. *"There is only one place left to go"* — Mahima's bare foot arriving on a chair seat, the table edge above it, low angle, held.

### Chorus 1 — the table becomes the stage

21. *"We're dancing on the table, let the whole street hear"* — she steps from the chair onto the wood as the horns hit, low angle straight up the length of the table, string lights overhead, tracking backwards.
22. *"Plates in the kitchen and the brass in the air"* — quick cut pair: the stacked sink through the kitchen door, then a trumpet raised and blown by the fence, the musician back out of the van.
23. *"Hold on to my hand and don't look down"* — her hand down, his hand up, the pull, close-up on the grip then the two of them rising into frame.
24. *"We are the last two standing in this town"* — both upright on the table, the family standing up around them in a ring, wide from the porch steps.
25. *"We're dancing on the table, let the whole street hear"* — circling low shot around the table as they dance, faces of the family sweeping past behind them.
26. *"Two strangers and a hundred years of family here"* — a slow rack across three generations at the table's edge, grandmother to aunts to cousins to a toddler on a hip.
27. *"Play it again, play it loud, play it till we fall"* — the teenage cousin's thumb on the volume, then the whole yard's arms going up on the beat, handheld from inside the crowd.
28. *"We're dancing on the table, or we're not dancing at all"* — both leads mid-spin on the wood, motion blur, string lights streaking, wide.

### Post-chorus 1 — the chant

29. *"Up, up, higher than the lights"* — bare feet landing on wood, macro, 0.5 s.
30. *"Up, up, this is how we say goodnight"* — the cowbell struck, extreme close-up, 0.5 s.
31. *"Up, up, one more time around"* — a ring of clapping hands filmed from inside the ring, whip pan, 0.5 s.
32. *"Nobody in this family sits down"* — the bride herself climbing onto the table in her dress, two cousins steadying her, medium.

### Verse 2 — Kai's twenty minutes earlier

33. *"I had my keys in my pocket and a lie about the time"* — flashback, cooler grade: Kai at the table, thumb turning a car key over in his jacket pocket, close-up on the hand.
34. *"A meeting in the morning that was never really mine"* — his eyes going to the side gate, then back to the table, medium close-up, the party soft behind him.
35. *"Then the lights came up gold over everybody's heads"* — the string lights coming on in a run down the whole garden, seen from his seat, the grade warming inside the shot.
36. *"And you kicked off your sandals and you climbed on up instead"* — from his eyeline: her sandals hitting the grass, then her legs stepping up onto the chair, low and partial.
37. *"You asked me, are you coming, like it wasn't a request"* — reverse: Mahima above him on the table, hand out, eyebrows up, low angle from his chair.
38. *"Like the wood would hold us both and the night would do the rest"* — his hands flat on the table edge, weight going on, the boards taking it, close-up.
39. *"My father's on his feet now with a napkin in the air"* — an older man spinning a napkin overhead by the fence, whooping, medium, handheld.
40. *"Your grandmother is filming with the phone up in her hair"* — the grandmother filming vertically, the phone held level with her hairline, screen composited, close-up, funny and fond.
41. *"I forgot about the morning, I forgot the whole plan"* — the car key dropped into a jacket pocket that is then thrown over a chair back, close-up.
42. *"There is red wine on my collar and I am a happy man"* — a red splash across a white collar in macro, then his face, entirely unbothered.

### Pre-chorus 2 — deeper in

43. *"Two shoes gone and three songs deep"* — both pairs of shoes now in the grass side by side, dew on them, macro.
44. *"Cowbell running like a heartbeat"* — the cowbell again, faster, the uncle's whole arm in it now, close-up.
45. *"The aunties clapping, the cousins know"* — the three aunts up out of their chairs clapping over their heads, cousins pulling more people off seats behind them, medium wide.
46. *"There is only one place left to go"* — a wide of the yard with a queue of people at the chairs, waiting to climb, static.

### Chorus 2 — the table is crowded

47. *"We're dancing on the table, let the whole street hear"* — reuse the low tracking shot up the table, but the wood is crowded now and the camera has to push through legs.
48. *"Plates in the kitchen and the brass in the air"* — both trumpets and the trombone playing together by the fence, brass catching the string lights, medium.
49. *"Hold on to my hand and don't look down"* — the two of them holding both hands and leaning back against each other's weight, spinning, close.
50. *"We are the last two standing in this town"* — a plate sliding off the table end and smashing, nobody looking at it, macro then wide.
51. *"We're dancing on the table, let the whole street hear"* — over the fence: the neighbour's dark house and a light coming on upstairs, then back to the yard.
52. *"Two strangers and a hundred years of family here"* — the newly married couple watching from the porch steps, laughing, veil across her knees, medium two-shot.
53. *"Play it again, play it loud, play it till we fall"* — the whole crowd jumping on the beat, the camera low and jumping with them.
54. *"We're dancing on the table, or we're not dancing at all"* — an overhead of the full table from the fig tree, bodies and lights, the widest frame so far.

### Instrumental — brass and the timbale break

55. Two musicians back out of the van, trumpet and trombone trading four bars at each other across the lawn, handheld between them.
56. The percussion duel: an uncle on timbales against a twelve-year-old on an upturned plastic bucket, cut on every hit.
57. A ring of clapping hands filmed from inside the ring, the camera turning a full three hundred and sixty degrees.
58. Kitchen doorway: someone carrying out a tray of plastic cups over their head through the dancing, tracking behind them.
59. Both leads at the far end of the table catching their breath, laughing, not talking, hands on knees, the party roaring out of focus behind them.

### Bridge — the quiet inside the loud night

60. *"When the brass goes quiet you can hear the whole street"* — the music down, the two of them sitting on the table edge with their feet swinging, half the string lights switched off, static wide.
61. *"A radio two doors down and a hundred tired feet"* — over the fence: a neighbour's lit kitchen window with a radio on the sill, the first blue of dawn in the sky above it.
62. *"You said you will remember this in twenty years or so"* — Kai in profile, talking to the yard rather than to her, close-up, one lamp on his face.
63. *"I said then help me down and ask me where I go"* — her hand out to him for the first time reversed, his hand taking it, close on the two hands and the drop to the grass.
64. *"There's a scratch in the varnish that the two of us just made"* — macro of a fresh pale scratch in the table varnish, a thumb running along it.
65. *"And every wedding needs two strangers who forgot to be afraid"* — the two of them standing beside the table looking at it, from behind, the yard beyond, wide and still.

### Final chorus — three generations up

66. *"We're dancing on the table, let the whole street hear"* — the horns return and the whole family climbs: cousins, aunts, the father with his napkin, crane-style wide of the lit yard.
67. *"Plates in the kitchen and the brass in the air"* — the trombone player standing on a chair to reach over the crowd, medium low.
68. *"Hold on to my hand and don't look down"* — a mother and a father being helped up by four hands, close on the hands.
69. *"We are the last two standing in this town"* — the two leads in the middle of a crowded table not looking at anyone but each other, medium two-shot, bodies moving past frame.
70. *"We're dancing on the table, let the whole street hear"* — the grandmother finally helped up by two cousins, phone still in her hand, medium, the biggest cheer of the video.
71. *"Two strangers and a hundred years of family here"* — a slow tilt from the grandmother's bare feet on the wood up to her face, delighted.
72. *"Somebody's mother is up here with us now"* — an older woman dancing properly, arms up, the crowd giving her room, medium.
73. *"Somebody's father is showing us how"* — the napkin father doing a step nobody else knows, everyone copying it badly, wide handheld.
74. *"Play it again, play it loud, play it till we fall"* — the teenage cousin on the speaker with both thumbs up, then a hard cut to the crowd's arms.
75. *"We're dancing on the table, or we're not dancing at all"* — the widest crane frame of the video: the whole lit backyard, the loaded table, a greying sky above.

### Post-chorus 2 — the chant, sky greying

76. *"Up, up, higher than the lights"* — bare feet on wood again, dew and grass on them now, macro, 0.5 s.
77. *"Up, up, this is how we say goodnight"* — the cowbell, one last strike, 0.5 s.
78. *"Up, up, one more time around"* — the bride swinging her veil overhead like a flag, whip pan.
79. *"Nobody in this family sits down"* — every folding chair in the yard empty, seen in a slow pan, the noise still going off frame.

### Outro — sunrise on the back porch

80. *"Sun coming up on the lights and the chairs"* — first daylight, string lights pale and still burning, chairs scattered, slow drift, wide.
81. *"Your suit jacket over me on the back porch stairs"* — the charcoal jacket going over her shoulders, the two of them sitting on the steps with plastic cups, medium from behind.
82. *"Table still standing and the yard is a mess"* — the long table alone in a field of paper napkins and one broken plate, static wide, morning light along the wood.
83. *"We are going to be family, I guess"* — the two of them on the steps, shoulders touching, both looking at the table rather than at each other, close two-shot.
84. *"We're dancing on the table, let the whole street hear"* — final shot: locked-off wide of the whole yard in early sun with the string lights still on, nobody in frame for the last two seconds, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first cowbell, the speaker kicking in over the band's
silence (shot 14), the table climb on the first chorus hit (shot 21), each
"dancing on the table", every chant, the timbale break, "help me down"
(shot 63), the grandmother's climb (shot 70) and the final locked-off wide.
At 128 BPM a bar is 1.88 s; the choruses cut close to every bar and the
post-chorus chants cut on every half-bar.

**The table-climb challenge.** Shots 17–24 recut vertically are the
shareable fifteen seconds: sandal, cowbell, clap, climb, hand, horns. Invite
people to post the moment somebody at their family party got up on the
furniture, with the chant underneath. The grandmother's climb (shot 70) is
the second shareable frame and the one most likely to travel on its own.

**Caption cut:** shots 25–26 with *"Two strangers and a hundred years of
family here."*

## 6. Quality-control checklist

- Two looks for Mahima only: red slip dress through the night, the same dress plus the charcoal jacket from shot 81; bare feet from shot 17 onward and never shod again
- Kai loses the jacket at shot 41 and it reappears only on her shoulders in shot 81
- The number of people on the table only ever increases: two, then a handful, then three generations; no chorus is emptier than the one before it
- All practical light: string lights, kitchen door, phone torches, then daylight — no cinematic key that could not exist in the yard
- Every table shot posed with OpenPose; no invented limbs in the crowd, no duplicate faces in the ring
- The grandmother's phone screen and any seating card are composited; no model-generated text anywhere
- The sky greys progressively from shot 60 and is fully lit by shot 80 — no night sky after the bridge
- The last shot is locked-off, empty of people, and holds until the audio fades
