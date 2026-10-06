# Wan 2.2 Shot List — "Your Name in Cursive"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission, plus five shots for the instrumental. Timestamps come from the
rendered WAV; cut on the sung line. At 92 BPM a bar is 2.61 s; the verses
run two bars a line, the short chorus lines one.

## 1. Visual style

Handwriting everywhere, legible nowhere. The single rule of this video is
that **the loops are always shot too close, too soft, too oblique or too
briefly to be read** — the audience must know a name is being written and
never learn it. Every surface in the film is a writing surface:
condensation, flour, chalk dust, wet sand, frost, fog, skin, paper.

Two temperatures. The **private world** is warm and small — desk lamps,
bathroom steam, September afternoon through a high window, everything close
and shallow. The **public world** is grey-blue and wide — winter bus
windows, a library, a street at dusk. The choruses break out of both into
open golden light, and the final chorus goes a full stop brighter on the
modulation. The camera is close and still for the secret, and only starts
moving once she decides.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm dusty September afternoon, flat room behind | Macro on the page, static |
| Verse 1 | Fogged warm bathroom, cool café window, flat silver beach | Close, locked off |
| Pre-chorus 1 | Warm cluttered interior | Handheld, loose |
| Chorus 1 | Golden hour, open, the widest so far | Moving with her, rising |
| Verse 2 | Green library lamps, then grey-blue winter | Over-the-shoulder, then macro |
| Pre-chorus 2 | Warm inside, colder through the window | Locked on her hands only |
| Chorus 2 | Evening streetlights, saturated | Faster tracking |
| Instrumental | One desk lamp, the rest dark; last shot hallway-lit | Slow drift, long holds |
| Bridge | Hallway light, warming as she turns | Static, then a push-in |
| Final chorus | A full stop brighter on the modulation | Wide, moving, released |
| Post-chorus | Bright, clean, high key | Fast cuts, macro |
| Outro | The September afternoon, unchanged | Macro, then the first widen |

## 2. Character bible — paste into every prompt

**Mahima** (the private year — intro, verses, pre-choruses)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair falling forward over one shoulder, no makeup, wearing a soft navy knit jumper with the cuffs pulled over her hands and a canvas satchel, guarded thoughtful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (winter — verse two and chorus two)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair under a knitted hat, no makeup, wearing a long charcoal wool coat over the navy jumper, a blue ink mark on the inside of her wrist, breath visible in the cold, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge, final chorus and outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and pushed back off her face, no makeup, wearing the navy jumper with the sleeves pushed up and the coat open, an open unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the boy — face seen only from the library scene onward)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a dark green corduroy overshirt over a plain grey tee, a paperback in one hand, warm amused expression, realistic cinematic photography, consistent identity

Before the library he is a presence, not a person: a shoulder at the edge of
the classroom frame, a shape across a café, a coat on the back of a chair.
The audience should meet his face at the exact moment she is caught.

**The two friends** — young women her age, animated, ordinary, always
talking over each other. Same two in both pre-choruses; coats on the second
time.

Objects that carry the story: the **blue ballpoint**, the **lined notebook**
and the margin, the **steamed mirror**, the **folded café receipt**, the
**wet sand** at low tide, the **fogged bus window**, the **frosted
windscreen**, the **blue ink on the inside of her wrist**, and finally
**his notebook**, open on a table by a door.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every mark of handwriting in this video is composited in the edit.**
Generate the surface — the steam, the sand, the frost, the page, the wrist —
clean and unmarked, with the hand and the pen or finger moving over it, and
add the loops in post as an animated stroke that matches the movement. The
model cannot write cursive and any attempt produces garbage letterforms that
a viewer will read as a real name. Phone screens and the message she does
not send are composited the same way.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai in his one look with IP-Adapter or a
character LoRA each. Depth for the classroom, the library and the hallway so
the three returns to the September desk match. OpenPose is only needed for
the rooftop and street shots; everything else is hands, and hands are the
risk — every macro of a hand holding a pen, drawing on glass or dragging a
shoe through sand gets a hand check before approval. 16:9 first; 9:16
recomposition for the bus-window hook cut and the post-chorus surface cuts,
which are natural vertical content.

Animate one gesture per clip: a fingertip crossing glass once, one letter of
a loop, steam beading and running, a page turning, a tide edge arriving. The
running condensation in shot 5 and the tide in shot 10 are the two shots
worth generating five times and picking; both are water behaving, which this
model does inconsistently.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; chorus shots 2–3 s.

## 4. Scene per lyric line

### Intro — September, the back row

1. *"First week of September, back row, blue pen,"* — extreme macro on a blue ballpoint moving in the margin of a lined page, the loops composited, the tip of the pen the only thing in focus, warm afternoon light across the paper.
2. *"I wrote it once and then I wrote it again."* — the same framing a beat later: the margin now has the shape twice, then three times, the hand not stopping, macro.
3. *"Little loops in the margin where the notes should be,"* — pull back to the whole page: the lesson notes have stopped halfway down and the margin has taken over, the page tilted away from the aisle, close.
4. *"A secret in my handwriting that only I could read."* — her face, chin on her hand, eyes on something off frame at the front of the room; a private smile arriving and being put away, medium close, the back row in soft focus around her.

### Verse 1 — three private places

5. *"I wrote it in the steam on the bathroom glass,"* — a fingertip drawing across a steamed bathroom mirror, the stroke clearing a line of dark glass behind it, macro, warm and fogged.
6. *"Watched it run before the mirror went clear."* — the drawn line beading and running downward, the shape coming apart, then her own face resolving through the clearing glass behind it, close.
7. *"I wrote it on the back of a café receipt,"* — a café table, a receipt turned over, the pen going down; the window light cool and grey behind, over-the-shoulder macro.
8. *"Folded it in my coat pocket like it was worth something here."* — the receipt folded once, twice, into quarters, and pushed deep into a coat pocket, her hand staying in the pocket a second too long, close-up.
9. *"I dragged it in the sand with the side of my shoe,"* — low and behind her on a flat beach at low tide, the side of a trainer drawing one long looping line in wet sand, tracking backward with her.
10. *"Let the tide come and take it, cause the tide doesn't tell."* — a wide from behind of the whole shape in the sand, out of focus and unreadable, and the first sheet of tide arriving over it, flat silver light.
11. *"Every notebook I own has a page that's just you,"* — her bedroom at night: a stack of notebooks on the bed, each one falling open in her hands to a page that is nothing but the same loops, close, one desk lamp.
12. *"I've been spelling out the thing that I can't say too well."* — her sitting back against the bed with the notebooks around her, looking at the ceiling, one hand still on an open page, wide, lamp only.

### Pre-chorus 1 — the friends

13. *"And my friends all say, just tell him, it's not that deep,"* — two friends in a café booth talking over each other and gesturing, warm cluttered interior, handheld, both of them animated.
14. *"But it's the deepest thing I know how to keep."* — her across the table, half-smiling, not answering, a pen turning over and over in her fingers, close-up.
15. *"I've got a thousand little versions in a thousand little lines,"* — cut fast through six of the surfaces already seen, half a second each: mirror, receipt, sand, notebook, table, napkin.
16. *"And not one of them has ever left this mouth of mine."* — her mouth, closed, in extreme close-up, and then her looking straight to camera for the only time before the bridge, static.

### Chorus 1 — released into the world

17. *"I wrote your name in cursive,"* — her walking out of the café into golden hour, the light climbing her face, tracking from the front, the widest frame so far.
18. *"Now I'm saying it out loud."* — the loops appearing in the pattern of streetlights sliding across a car ceiling above her, composited, her looking up at them.
19. *"Every loop, every letter,"* — flour spilled on a kitchen counter, a finger drawing through it, macro, warm.
20. *"I'm not hiding it now."* — chalk dust on a school step, a shoe scuffing a loop into it, low angle.
21. *"I wrote it small, I wrote it soft,"* — the margin from shot 1 again, now shot from directly above and further away, the whole page a field of loops.
22. *"I wrote it where nobody looks,"* — the inside of a locker door, the underside of a desk, the back page of a library book, three cuts, all macro, all half-lit.
23. *"But you're not a secret anymore,"* — a rooftop at golden hour, her alone, arms loose, head back, the city behind her, wide.
24. *"You're the title of my book."* — a hardback closed in her hands, her thumb over the blank spine where a title would be, the light full on her face, close-up.
25. *"I wrote your name in cursive,"* — her crossing a bridge or an open square in the low sun, moving with purpose for the first time, tracking from the side.
26. *"Now I'm saying it out loud."* — her stopping, breathing out, the golden light going off the buildings behind her, medium, static, held.

### Verse 2 — caught in the library

27. *"You caught me in the library, my hand across the page,"* — a long library table under green lamps, her hand flattening hard over her open notebook as a chair scrapes opposite, deep shadow between the stacks.
28. *"Asked me what I was drawing, I said, nothing, just a shape."* — over-the-shoulder onto Kai's face for the first time in the film, amused, close, leaning in slightly.
29. *"You laughed and said, you're a terrible liar,"* — her covering the page harder with both hands and looking anywhere else, close-up, the green lamp under her chin.
30. *"Then your ears went red and you looked for an escape."* — Kai's ear and jaw in macro, colour rising, and his eyes going back down to his book far too fast, the paperback lifted a fraction too high.
31. *"Now it's fog on the bus window, one finger, one name,"* — a fogged bus window, one finger drawing a loop, the winter city sliding past behind the glass out of focus, macro. **The hook frame.**
32. *"In the frost on the car in the cold morning light,"* — frost on a windscreen at dawn, a bare fingertip cutting a line through it, her breath visible, macro, grey-blue.
33. *"On the inside of my wrist in a blue that stays the same,"* — her wrist under a coat cuff, blue ink on the skin, half rubbed away and redrawn over the old mark, the only warm frame in the winter run.
34. *"I've been carrying you round like a word I can't say right."* — her walking a winter street with her hands in her pockets and her collar up, not looking at anything, tracking from behind, wide and cold.

### Pre-chorus 2 — the hands give her up

35. *"And my friends all say, girl, he can see it on your face,"* — the same booth months later, coats on now, the friends leaning in, but shot from waist height so only their hands and the table are in frame.
36. *"But my face has never been the honest place."* — her hand turning a cup a quarter turn at a time, steady, no face in the shot, close-up.
37. *"It's my hands that give me up, it's my hands that know,"* — her other hand drawing on a napkin without looking at it, the pen moving in the same rhythm as shot 1, macro.
38. *"And my hands have been saying it for months now, so."* — the napkin left on the table as the friends stand and coats come off the back of the chair; the camera stays on the napkin as the light changes.

### Chorus 2 — the loops go public

39. *"I wrote your name in cursive,"* — a bus shelter panel thick with condensation, a hand drawing across it as a bus pulls in behind, evening streetlights, medium.
40. *"Now I'm saying it out loud."* — a fogged shop window from inside the shop, the loops appearing backward from the camera's side, saturated evening colour.
41. *"Every loop, every letter,"* — the misted glass of a corner-shop fridge door, a finger, the drinks glowing cold behind it, macro.
42. *"I'm not hiding it now."* — a dusty car boot in a car park, a finger through the dust, the loop staying this time, low angle.
43. *"I wrote it small, I wrote it soft,"* — reuse shot 21's overhead margin, tighter and moving, the page filling the frame.
44. *"I wrote it where nobody looks,"* — the back page of a returned library book being opened by a stranger's hands, then closed again without noticing, macro.
45. *"But you're not a secret anymore,"* — her walking faster through an evening crowd, people passing in front of the lens, tracking, the first time other people are in frame with her.
46. *"You're the title of my book."* — her stopping outside a lit window, catching her own reflection over the display, medium, saturated.
47. *"I wrote your name in cursive,"* — the fogged bus window from shot 31 again, the old loop still faintly there and a new one drawn over it, macro.
48. *"Now I'm saying it out loud."* — her forehead resting on that window, eyes closed, the city lights sliding over her face, close-up, held.

### Instrumental — the hats drop out

49. Her at her desk at night, one lamp, writing three lines and stopping, the pen lifting and hovering, close on the hand and the page.
50. A slow drift across the open notebooks laid out on the bed, page after page of the same loops, no cuts, the lamp the only light.
51. Rain running down her bedroom window with old loops still faintly on the inside of the glass, the street lights bleeding through, macro.
52. Her hand hovering over her phone on the desk, a message typed and then deleted (composited), the screen going dark, close-up.
53. A hallway: a table by a door, a coat over a chair, and a notebook lying open on the table under a hallway light. Held two seconds longer than expected — the cut into the bridge.

### Bridge — his handwriting

54. *"You left your notebook open on the table by the door,"* — her seeing it from across the room, stopping mid-step, the notebook small and lit in the background, wide, static.
55. *"I wasn't gonna look, but I looked, and there was more."* — her POV coming down over the open page: the same rhythm of loops as her own margins, in a different hand, never legible, composited.
56. *"Little loops in the margin in a hand that wasn't mine,"* — her fingers turning one page, then another, then another, faster, the loops on every one, macro on the hands.
57. *"Mine, in cursive, over and over, every page, every line."* — her hand going to her mouth, the notebook still open under it, close-up, the hallway light hard on one side of her face.
58. *"So I'm done with the pen, I'm done with the glass,"* — she sets her own pen down on the table beside his notebook, deliberately, and takes her hand off it, macro.
59. *"I'm done writing down a thing that I could just ask."* — her straightening up and turning around, the movement in one take, the light beginning to warm.
60. *"You're standing right here and the room's gone still,"* — Kai in the doorway behind her, not moving, the two of them in one frame for the first time, medium wide, everything quiet.
61. *"And if I don't do it now, then I never will."* — push in on her face, the breath before, eyes up, the frame brightening as the modulation arrives.

### Final chorus — said out loud

62. *"I wrote your name in cursive,"* — her mouth moving on the line in close-up; the audio carries it, so the shot needs nothing but her face a stop brighter than any frame before it.
63. *"Now I'm saying it out loud."* — Kai's face receiving it, the paperback forgotten in his hand, close-up.
64. *"Every loop, every letter,"* — the two notebooks side by side on the table, both open, both full of loops, overhead macro.
65. *"Say it back to me now."* — his mouth moving, one line, and her eyes closing for half a beat, two quick close-ups cut hard together. **The turn frame.**
66. *"I wrote it small, I wrote it soft,"* — the two of them walking out of the door into open daylight, wide, following from behind.
67. *"I wrote it where nobody looks,"* — a street in full afternoon, the whole frame open and bright, no macro, no secrets, tracking.
68. *"But you're not a secret anymore,"* — the rooftop from shot 23 in daylight, both of them on it now, wide.
69. *"You're the title of my book."* — her hardback in her hands again, opened this time, his hand coming into frame to hold the other side, close-up.
70. *"I wrote your name in cursive,"* — a wide drone-free pull-back down the street, the two of them small in it, the city ordinary and bright around them.
71. *"Now I'm saying it out loud."* — her face to camera, saying nothing, released, close-up, held one bar.

### Post-chorus — clearing every surface

72. *"Out loud, out loud,"* — the bathroom mirror wiped clear with one flat palm, macro, half a second; the receipt unfolded and dropped, half a second.
73. *"No more margins, no more doubt."* — the tide taking the sand shape completely, the beach smooth; the notebook closed with a hand flat on the cover.
74. *"Out loud, out loud,"* — the bus window cleared by the heater, the frost gone off the windscreen in the sun, two fast cuts.
75. *"Your name, out loud."* — her wrist under running water, the blue ink going, her thumb rubbing it away, macro, bright and clean.

### Outro — the same desk, one year on

76. *"First week of September, back row, blue pen,"* — the identical macro framing as shot 1: a blue ballpoint moving in the margin of a lined page, the same warm afternoon light.
77. *"I wrote it once and then I wrote it again."* — the loops multiplying in the margin exactly as they did in shot 2, matched frame.
78. *"Now it's written on my face where the whole world can see,"* — her face, chin on her hand, the same posture as shot 4, but she is not hiding the smile this time, medium close.
79. *"And you're writing mine in cursive right next to me."* — final shot: the frame widens for the first and only time to reveal two pages, two hands, two pens, side by side at the same desk, both margins full. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first pen stroke, the mirror running in shot 6, the tide in
shot 10, each *"I wrote your name in cursive"*, the library catch in shot 28,
the wrist in shot 33, the instrumental, the open notebook in shot 55, *"say
it back to me now"*, the post-chorus, and the widen in shot 79. At 92 BPM a
bar is 2.61 s; the chorus cuts land on the bar, the post-chorus on the
half-bar.

**The surface challenge.** The shareable cut is shots 31, 32 and 33 —
the bus window, the frost and the wrist — vertical, with *"I wrote your name
in cursive, now I'm saying it out loud"* on screen. Invite people to post
one clip per surface: steam, sand, frost, a receipt, a wrist, and then wipe
it, cut to the post-chorus chant. The second shareable frame is the widen in
shot 79, posted alone with no context. **The caption line:** *"But my face
has never been the honest place."*

## 6. Quality-control checklist

- No handwriting is ever legible in any frame, at any speed, on any surface — every mark is a composited stroke over a clean plate, and any frame where a letterform resolves is rejected
- Three looks in the right sections: the jumper alone until shot 27, the coat and knitted hat from 27 to 48, the coat open and hair back from shot 59 on; the blue wrist mark appears in shot 33 and is gone by shot 75
- Kai has no face before shot 28 — shoulder, coat, shape only — and is present in frame with her from shot 60 onward
- The three returns to the September desk match exactly: shots 1, 21 and 76 are the same lens, height and light; shot 79 is the only widen
- The private world stays close and warm, the winter run stays grey-blue, and shot 62 is measurably a stop brighter than everything before it
- Water behaves: the running mirror in shot 6 and the tide in shot 10 are picked from multiple generations, never accepted first pass
- Hands are the subject of more than thirty shots; every pen, fingertip and page-turn macro gets a finger count before approval
- The last shot is locked-off on the two pages and holds until the piano figure ends
