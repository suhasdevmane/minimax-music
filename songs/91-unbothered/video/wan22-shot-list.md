# Wan 2.2 Shot List — "Unbothered"

**One shot per lyric line**, built from the submission's per-section video
direction. At 108 BPM a bar is 2.22 s, so verse shots run 3–5 s and the
choruses cut roughly every bar with the dance shots held longer. Take
timestamps from the rendered WAV.

## 1. Visual style

Sunlight is the whole grade. No filters, no colour gels, no night-blue
correction: real midday sun on painted walls, real gold at six, real string
lights at midnight. The video is built out of four places — a **rooftop**, a
**kitchen**, a **street**, a **Saturday market** — plus one dim bedroom for
the bridge, which is the only shot in the film where she does not move. The
camera is loose and human: handheld at chest height, low angles on feet,
and one drone move reserved entirely for the last chorus. Nobody is
humiliated on screen; the person who wrote the paragraphs is never shown
clearly and never reacted to.

| Section | Grade | Camera |
|---|---|---|
| Intro | Low gold, long shadows, warm skin | Static macro, then overhead |
| Verse 1 | Hard morning sun through a window | Handheld, kitchen-height |
| Pre-choruses | Memory shot warmer and softer than present | Low, child's eyeline |
| Choruses | Full midday sun, saturated, no shadow drama | Tracking with the dance |
| Post-chorus chant | Flat bright sun | Locked off, four-count wide |
| Verse 2 | Market daylight, then lamp and one red bulb | Handheld among people |
| Instrumental | Party warm cut against one hard window shaft | Close on hands and feet |
| Bridge | Curtain dark, then full daylight in one cut | Completely still |
| Final chorus | Moonlight, string lights, deep blue | Wide, then the single drone move |
| Outro | String lights, one warm lamp | Static, the intro framings repeated |

## 2. Character bible — paste into every prompt

**Mahima** (daytime — the primary look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair worn loose with a centre part, minimal glowy makeup, wearing a bright coral wrap top and wide cream linen trousers, gold hoops, flat sandals, easy amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (party and final chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled up into a high loose bun with strands down, glowy makeup with gold on the eyelids, wearing a fitted black slip dress and gold hoops, bare feet, open joyful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and unstyled, no makeup, wearing an old grey t-shirt and shorts, sitting still with a plain unperformed expression, realistic cinematic photography, consistent identity, natural skin texture

**The aunties** (pre-chorus memory) — three women in their fifties and sixties at a kitchen table, faces fully visible, mid-laugh, entirely at ease. Warm, real, not stylised.

**The pepper auntie** (verse two) — a market trader in her sixties behind a stall of chillies and tomatoes, face visible, knowing and kind.

**The neighbours and dancers** — real-looking people of all ages on a residential street and a rooftop, faces visible, joining the dance for two beats each.

**The person who wrote the paragraphs** — never shown clearly. A silhouette in a doorway, a shoulder at the edge of frame, a figure out of focus behind dancers. No face, no reaction shot, no confrontation. **There is no male romantic lead in this video.**

Objects: the **glass of ice**, the **phone face-down**, the **portable
speaker**, the **bunch of flowers she buys herself**, the **hibiscus drink**,
the **curtains**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens are composited in the edit** — the wall of paragraph text, the
video call with her cousin, the glowing phone under her hand on the ledge.
Generate the phone as a lit blank rectangle and overlay in post; the model
cannot render legible messages, and the sheer visual length of the paragraphs
is the joke in verse one.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA. **OpenPose
is essential for every dance shot** — the street chorus, the four-count chant
and the party floor all need pose references or the model will invent joints;
build the four-count move once as a pose sequence and reuse it across shots
19–26, 27–30, 45–52, 66–73 and 74–77 so the choreography stays identical.
Depth for the market and the crowded front room. 16:9 first; 9:16
recomposition for the dance and chant cuts, which are the shareable unit.
Animate in short bursts: one move per clip, one drum strike, ice shifting in
a glass, a curtain opening.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — rooftop, six o'clock gold

1. *"Rooftop speaker, six o'clock gold"* — a portable speaker on a warm concrete ledge with washing lines and rooftops behind it, low gold sun straight into the lens, static wide.
2. *"Ice in a glass and a story I've been told"* — extreme macro of ice shifting in a glass, condensation running down, gold light refracting through it.
3. *"Somebody's typing something long about me"* — overhead shot of her lying back on the warm roof, phone face-down on her stomach, screen light leaking around it (composited), eyes closed.
4. *"And the log drum came on, so I let it be"* — her hand reaching sideways and tapping the speaker once as the log drum lands, close-up on the hand, everything else still.

### Verse 1 — the screenshot and the coffee

5. *"They sent me a screenshot at ten in the morning"* — a phone lighting up on a cluttered kitchen counter, a comically long wall of text scrolling (composited), hard morning sun across it.
6. *"Three paragraphs deep with no kind of warning"* — her reading it, one eyebrow lifting, thumb scrolling and scrolling and still not reaching the end, close-up.
7. *"I read it, I laughed, I went and made my coffee"* — a single genuine laugh, then she puts the phone face-down and turns to the kettle in one move, medium handheld.
8. *"Then I put on the song that gets my hips talking to me"* — two small dance steps at the counter while the coffee brews, seen from the hip down, sun on the floor tiles.
9. *"My cousin said, aren't you gonna reply?"* — a phone propped against a sugar tin on a video call (composited), her cousin mid-question, Mahima out of focus behind it.
10. *"I said, to what, a stranger having a hard July?"* — her shrugging with both hands full, cup in one and a spoon in the other, direct to the propped phone, close.
11. *"They want me in the comments, want me in the fight"* — the phone face-down on the counter buzzing three times, unattended, macro, her hand not moving toward it.
12. *"But my afternoon is booked and my chest is light"* — her walking out of the kitchen into a bright hallway, coffee in hand, a fan turning behind her, tracking.
13. *"Some things are weather, they pass over the roof"* — a fast cloud shadow crossing a painted wall and moving on, no people, static wide, two seconds.
14. *"I'm not gonna argue with a cloud about proof"* — her on the front step in full sun, cup down, looking up at the sky and shaking her head once, low angle.

### Pre-chorus 1 — peace as a muscle

15. *"Peace is a muscle and I work it every week"* — a memory shot from a child's eyeline: three older women at a kitchen table, mid-laugh, warm and soft.
16. *"Learned it from my aunties in the kitchen when they speak"* — the same table, one auntie waving a hand dismissively at something being said, the others laughing harder.
17. *"When the noise gets loud I turn the bass up higher"* — back to the present: her hand on the speaker dial, turning it, extreme close-up, sun on her knuckles.
18. *"Let them run their mouth, I am not lending them a fire"* — the kick drops out; her still on the step with the sun behind her, held on one frame for two bars.

### Chorus 1 — the street

19. *"Unbothered, untouchable, in my lane"* — she starts dancing down the middle of a quiet residential street in full sun, tracking backwards ahead of her.
20. *"Sun on the back of my neck, I'm not complaining"* — a close-up from behind, sun on her neck and shoulders, hair moving, hand-held.
21. *"Say what you want, put it in a frame"* — a neighbour on a step joins the move for exactly two beats and sits back down, wide.
22. *"I'll be right here moving just the same"* — low angle on feet and shadow, sandals on warm tarmac, the shadow doing the same dance.
23. *"Low stress, light feet, easy on my mind"* — a wide with washing lines and painted walls, four people dancing at different distances down the street.
24. *"Whatever you're carrying, leave it behind"* — a man setting down two shopping bags to do the move and picking them back up, comic timing, static.
25. *"Unbothered, untouchable, in my lane"* — tracking with her again, faster, the whole street now moving behind her.
26. *"Look at me dancing while you're saying my name"* — she stops dead centre of the street on the downbeat, arms out, grinning, locked-off wide.

### Post-chorus 1 — the four-count chant

27. *"Shoulders down, shoulders down"* — four dancers in a line dropping their shoulders on the beat, locked off, flat bright sun.
28. *"Nothing in this city gonna hold me down"* — the same move with her in front and the line behind her, mirrored framing.
29. *"In my lane, in my lane"* — the move at half speed, close on shoulders and hands, deliberately teachable.
30. *"Unbothered, untouchable, in my lane"* — the full line hitting the last count together and freezing, wide, two seconds of stillness.

### Verse 2 — market, flowers, party

31. *"Market on a Saturday, colours in a row"* — a slow lateral track along stacked market stalls, chillies and tomatoes and fabric, no people in focus.
32. *"Bought myself the flowers, nobody had to know"* — her paying for a bunch of flowers with both hands, close on the exchange, sun through the awning.
33. *"The auntie with the peppers said, you look light today"* — the pepper auntie's face, warm and knowing, speaking directly to camera height, static close.
34. *"I said, I put some heavy things down along the way"* — Mahima's reply, a small shrug and a real smile, matched framing to shot 33.
35. *"Cold drink after, hibiscus and lime"* — a deep red hibiscus drink held up against the sun, macro, the lime wedge and the light through the glass.
36. *"Walked the long block home because the day was mine"* — a long tracking shot from the side, flowers under one arm, walking deliberately slowly past painted shutters.
37. *"Then at nine that same person walked into the party"* — night, a crowded front room; a silhouette entering the doorway, backlit, face never visible.
38. *"Whole room turning, waiting on a story"* — heads turning in one wave, the music continuing, the room holding a breath, wide.
39. *"I said hey, made room, went back to the beat"* — her glancing over, nodding once, stepping half a pace sideways to make room, then turning back, one continuous take.
40. *"And the floor stayed hot underneath my feet"* — low angle on bare feet and the floor, the party resuming above frame, red bulb light.

### Pre-chorus 2 — the party version

41. *"Peace is a muscle and I work it every week"* — her hand on the speaker dial again, this time at the party, lamp warm, close-up.
42. *"Learned it from my aunties in the kitchen when they speak"* — a two-second flash of the auntie memory, same framing as shot 15, warmer.
43. *"When the noise gets loud I turn the bass up higher"* — two friends closing ranks around her without being asked, none of them looking at the doorway.
44. *"Let them run their mouth, I am not lending them a fire"* — the kick drops again; a held frame of the three of them laughing, the doorway out of focus behind.

### Chorus 2 — the party floor

45. *"Unbothered, untouchable, in my lane"* — the street choreography recreated indoors with more people and less space, handheld in the middle of it.
46. *"Sun on the back of my neck, I'm not complaining"* — a red bulb standing in for the sun on the same shoulder framing as shot 20.
47. *"Say what you want, put it in a frame"* — a slow-motion insert of the flowers in a jar on a table behind the dancers, untouched.
48. *"I'll be right here moving just the same"* — feet on a wooden floor, the same low angle as shot 22, night version.
49. *"Low stress, light feet, easy on my mind"* — a wide of the whole room hitting the same beat, one lamp and one red bulb.
50. *"Whatever you're carrying, leave it behind"* — someone's jacket sliding off a chair unnoticed as the room moves, small and funny, static.
51. *"Unbothered, untouchable, in my lane"* — her spinning once, hair going, the room blurring, handheld push-in.
52. *"Look at me dancing while you're saying my name"* — she lands the beat facing away from the doorway entirely, locked off.

### Instrumental — percussion conversation

53. Hands on a log drum in extreme close-up, the whole frame the wood and the palm, warm lamp light.
54. A talking drum squeezed under an arm and struck, the pitch bending, close on the tension cords.
55. Bare feet on a wooden floor keeping the pattern, floor level, dust and light.
56. A shaker in silhouette against a bright window, the only hard shaft in the sequence.
57. A wide of the whole room landing on one beat together, then everyone laughing, held.

### Bridge — the still room

58. *"Don't get it twisted, I feel it all"* — her sitting on the end of a bed in a dim room, curtains closed, completely still, static.
59. *"I just stopped performing it for people in the hall"* — a close-up of her face doing nothing at all, no acting, held longer than is comfortable.
60. *"I let it hurt on a Tuesday with the curtains closed"* — a wide of the dim room, one line of daylight at the curtain edge, her small in the frame.
61. *"Then I woke up Wednesday and I picked the good clothes"* — a hard cut: her pulling the curtains open and the room flooding with daylight, same framing as 60.
62. *"They call it cold, I call it a choice"* — her hand moving along a clothes rail and stopping on the coral top from the daytime look, close.
63. *"I gave my best years to the loudest voice"* — a two-second flash of an old kitchen at night with a raised voice implied and no one in frame, then back.
64. *"Unbothered is not a wall I built"* — a bare wall in full daylight, nothing on it, one second, deliberately literal and empty.
65. *"It's a door I close without the guilt"* — a real door closing gently on its own weight, her hand leaving the handle, the drums coming back on the click.

### Final chorus — the rooftop at night

66. *"Unbothered, untouchable, in my lane"* — the intro rooftop at night with string lights up and twenty people dancing, wide, deep blue sky.
67. *"Moon on the rooftop and I'm still not complaining"* — the moon over the water tanks and the same ledge from shot 1, static, two seconds.
68. *"Say what you want, put it in a frame"* — the four-count move done by the whole roof, handheld among them.
69. *"I'll be right here moving just the same"* — the same low feet-and-shadow angle as shot 22, now lit by string lights.
70. *"Low stress, light feet, easy on my mind"* — a close-up on her face mid-dance, eyes closed, entirely unselfconscious.
71. *"Whatever you're carrying, leave it behind"* — an older neighbour joining at the edge of the roof, doing the move badly and delightedly.
72. *"Unbothered, untouchable, in my lane"* — the single drone move of the video: rising off the roof, the dance getting smaller, the neighbourhood opening out.
73. *"Look at me dancing while you're saying my name"* — the drone holding high over the lit roof in a dark block, the music carrying, wide.

### Post-chorus 2 — handed around

74. *"Shoulders down, shoulders down"* — the four-count move from three angles cut on the beat, the whole roof doing it.
75. *"Nothing in this city gonna hold me down"* — a child on the edge of frame doing the move half a beat late, nobody correcting them.
76. *"In my lane, in my lane"* — her not at the front for the first time, somewhere in the middle of the group, wide.
77. *"Unbothered, untouchable, in my lane"* — everyone landing the last count together and holding, string lights swinging, locked off.

### Outro — one glass again

78. *"Rooftop speaker, midnight gold"* — the same speaker on the same ledge from shot 1, string lights instead of sun, the roof emptying behind it.
79. *"Ice in the glass and a story getting old"* — the macro of shot 2 repeated: the ice almost melted, warm lamp light instead of gold.
80. *"Somebody's typing, I will never even see"* — her phone face-down on the ledge, the screen glowing faintly under it (composited), her hand resting on top of it.
81. *"The log drum's playing, so I let it be"* — final shot: the overhead of shot 3 repeated, her lying back on the roof at night, eyes closed, one hand keeping time on her stomach, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the log drum landing on *"so I let it be"*, both kick-drops in
the pre-choruses, the first street step, every *"in my lane"*, the doorway
in verse two, the curtain cut in the bridge, the door closing on *"without
the guilt"*, and the drone lift. At 108 BPM a bar is 2.22 s; the choruses
cut roughly on the bar, and the chant cuts on the count.

**The shoulders-down challenge.** The post-chorus is the shareable unit: a
four-count move you can do in a kitchen, a lift or a market aisle. Post
shots 27–30 vertically, including the half-speed teaching shot, with
*"shoulders down, shoulders down"* on screen. **The hook frame** is shot 26,
her stopped dead centre of the street with the whole block moving behind
her. **The caption card** is shot 65, the door closing.

## 6. Quality-control checklist

- Three looks in the right sections: coral and linen for daytime, black slip and high bun from shot 37 on, grey t-shirt only in the bridge
- The four-count choreography is identical in every chant and chorus shot; build it once as a pose sequence and reuse it
- The person from the doorway is never shown clearly, never confronted and never reacted to after shot 39
- No male romantic lead anywhere in this video; the aunties, the pepper trader and the neighbours all have faces
- Sunlight is real: no gels, no blue night correction, no filters; the only artificial light is the string lights and one red bulb
- All screens composited; the paragraph wall must look absurdly long, which is the joke
- The bridge is the only sequence in which she does not move, and it must be allowed to sit uncomfortably long on shot 59
- The last four shots are exact repeats of the first four framings, and the final overhead holds until the log drum fades
