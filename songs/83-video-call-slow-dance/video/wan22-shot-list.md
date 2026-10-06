# Wan 2.2 Shot List — "Video Call Slow Dance"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
94 BPM a bar is 2.55 s, so most shots run 3–5 s and the choruses cut every
one or two bars.

## 1. Visual world

Two bedrooms, two time zones, one song. The whole video lives inside a
**vertical split screen** and the split is the story: it starts as a wall,
learns to behave like one room, drifts off-centre when one of them moves
more, and physically closes in the final chorus until the two halves are one
frame. The only light in either room is practical — one lamp each, plus the
laptop. **Her room is amber and his is cooler blue**, and the two
temperatures converge across the song until they match on the first chorus
and never separate again. No exteriors until the post-chorus. Everything is
intimate, handheld only where a real hand would hold it.

| Section | Grade | Camera |
|---|---|---|
| Intro | Her amber, his cool blue, two clocks | Static, matched pairs |
| Verse 1 | Warm lamp, screen glow arriving | Close, handheld |
| Pre-chorus 1 | Both rooms dimming | Matched low angles |
| Chorus 1 | Laptop light only, colours matched | Slow circling, split aligned |
| Verse 2 | Desk lamp, dying window light | Static, close on hands |
| Chorus 2 | Fully matched amber, wider | Looser handheld, split drifting |
| Instrumental | Warm, then one side drains to flat blue | Slow push-ins, wide |
| Bridge | Cold frozen blue meeting warm lamp | Static, then live motion |
| Final chorus | Fullest warm light, string lights on | Moving, split closing |
| Post-chorus | Harsh public airport light | Fast cuts, no split |
| Outro | Lamp only, falling to black | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (her room, the whole song)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair twisted up and pinned with loose strands at the temples, soft natural makeup with a warm red lip, wearing an oversized cream ribbed knit jumper over black shorts, bare feet in white socks, small gold studs, warm amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge and outro, hair down)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly fallen out of its pins, makeup softened, wearing the same oversized cream ribbed knit jumper, bare feet in white socks, tender open expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (his room, the whole song)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a heather-grey button-down shirt with the collar bent up on one side over a white t-shirt and dark joggers, bare feet, warm unhurried expression, realistic cinematic photography, consistent identity

Objects, and they carry the story: her **lamp on a long cord** (she drags it
in verse 1 and the light on her face changes in shot), his **stack of
hardback books** under the laptop, his **wall calendar with a red pen** and
its circled date, **her** calendar which is only revealed in the final
chorus, the **ceiling fan** behind him, the two **laptops** (hers silver,
his black, so the split is readable in a thumbnail), her **white socks** on
floorboards, his **bare feet** on carpet.

Nobody else appears in this video at any point. No flatmates, no street, no
window with a person in it. The airport shots in the post-chorus are empty.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, video-call windows, clock faces, the calendar's numbers, the
battery indicator, the spinning buffer wheel and the airport gate signage
are composited in the edit.** Generate every laptop as a lit blank panel and
overlay the picture in post. The model cannot render a legible interface,
and the interface is doing half the storytelling here — including the
freeze, which is a post effect over a live plate, not a generated glitch.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock both leads with IP-Adapter or a character LoRA each (front,
three-quarter, profile, seated at a desk, standing holding a laptop). Depth
for the two bedroom interiors so the rooms stay dimensionally consistent
across forty shots. **OpenPose for every dance shot** — a person turning
slowly while holding a laptop flat against the chest is exactly the pose the
model invents extra arms for. Shoot the two halves as separate 16:9 plates
and compose the split in the edit rather than generating a split frame; 9:16
recomposition for the palms-meeting cut, which is the vertical hero.

Animate conservatively and in short bursts: one turn per clip, one lamp
move, one hand rising to the screen. The split-screen line moving in the
final chorus is an edit animation over static plates, not a generation.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — two clocks, press play

1. *"Nine your time and midnight mine"* — vertical split: left, her bedroom at midnight, curtains closed, one amber lamp; right, his bedroom, blue still in the window. A clock face composited on each side, static wide.
2. *"Same song queued up, we press play on three"* — matched close-ups of two hands hitting a space bar at the same instant, cut so both land on the same frame.
3. *"Pick the laptop up and hold it to your chest"* — Kai lifting the laptop off the desk and pressing it flat to his chest, the screen light climbing his jaw, medium close-up, static.
4. *"Tonight the distance don't get to me"* — Mahima doing the same on her side, a small laugh she turns away from the camera, matched framing to shot 3.
5. *"Two lamps, two rooms, one slow groove"* — both sides wide at once: two people, two lamps, two rooms, standing in the same posture, the split line dead centre and hard.
6. *"Baby, don't blink, and don't you move"* — extreme close-up of her eyes on the screen, then his, cut on the beat, screen glow as key light.

### Verse 1 — her, getting ready for a laptop

7. *"I put my hair up like it's a real date"* — her room twenty minutes earlier: close-up of her twisting her hair up and pinning it, lamp light, handheld.
8. *"Lipstick for a camera, that's how far gone I am"* — a warm red lip drawn in a small hand mirror, macro, then her pressing her lips together and checking the laptop preview.
9. *"Moved the lamp so the light hits right"* — her dragging the lamp across the floorboards by its cord, the light on her face visibly changing inside the shot, medium wide.
10. *"Cleared the laundry off the bed like you'd notice, damn"* — a fast sweep of clothes off the bed into a basket, then a held beat on the empty made bed, static.
11. *"You're in that grey shirt with the collar bent"* — what she sees: him on her screen, framed slightly too low, her own face reflected faintly in the monitor glass, over-the-shoulder.
12. *"Ceiling fan turning slow behind your head"* — macro on his bent collar, then the fan blades turning behind him, shallow focus, slow.
13. *"Two thousand miles of signal and delay"* — a wide of her alone in the amber room with the cool screen light on one side of her face, static, the first shot where the two colours meet.
14. *"And you freeze on the frame where you're smiling my way"* — the picture stuttering and holding on his smile (composited); her finger reaching out and touching the frozen frame, extreme close-up.

### Pre-chorus 1 — the count-in

15. *"So put the laptop on your palm, lift it slow"* — matched pair, one per side, both from the same low angle: a laptop balanced flat on one open palm like a tray.
16. *"Count me in, one, two, here we go"* — extreme close-up of her mouth counting, then his feet stepping on the count, cut on the number.
17. *"Sway to the left when I sway to the right"* — both sides at once, both leaning, the split line between them reading for the first time like a wall rather than a frame.
18. *"Mirror me, baby, we can get it right tonight"* — both rooms dimming as each of them reaches off-frame to a lamp, the laptops becoming the only light source, wide.

### Chorus 1 — the dance

19. *"Video call slow dance, hold your screen like it's me"* — the dance proper: both of them turning slowly, each holding a laptop against the chest, the two halves aligned so the movement reads as one, slow circling camera.
20. *"Two bedrooms, one song, closest we can be"* — pull back on both sides simultaneously to reveal how much empty room is around each of them, matched wides.
21. *"Turn down the lights, I'll turn up the sound"* — his hand on a volume key, her hand on a lamp switch, cut together on the beat, macro.
22. *"Spin me on the carpet, I'll spin you around"* — a slow spin, hers clockwise on floorboards, his anticlockwise on carpet, so the split reads as a single turn.
23. *"Video call slow dance, cheek against the glass"* — her cheek resting against the edge of the screen, eyes closed, the light on her skin, extreme close-up.
24. *"Buffering forever, I don't need it fast"* — his palm flat on his own screen, the picture soft and slightly behind, close-up through the glass.
25. *"If a signal is all we get tonight"* — both sides, hands raised toward the split line, almost meeting across it, static and symmetrical.
26. *"Hold your screen like it's me, and hold it tight"* — both of them pulling the laptop in tighter to the chest, chins down, the first shot where both rooms are the same colour.

### Verse 2 — him, the stack of books and the red pen

27. *"I put the laptop on a stack of books"* — his room earlier: close-up of his hands stacking hardbacks under the laptop, three, then four, static.
28. *"So your eyes line up with mine and stay"* — him checking the preview, removing one book, checking again, the small engineering of a good angle, medium.
29. *"Marked the calendar with a red pen, look"* — macro on a red pen crossing today's square on a wall calendar.
30. *"Twenty-two more squares and I'm on my way"* — pull back on the calendar: a block of crossed squares and one circled date; he taps it twice with the pen cap and turns the calendar toward the camera.
31. *"You do that thing where you say you're fine"* — her on his screen saying it, framed small in the middle of his monitor, his room dark around it.
32. *"Then you look off frame and your voice goes thin"* — her eyes going off to the left of frame; hold on his face watching her do it, close-up, no reaction yet.
33. *"So I press my hand up flat to the screen"* — his hand rising into his own shot and pressing flat against the monitor, screen glow through the gaps between his fingers, extreme close-up.
34. *"Put yours on mine, baby, let me in"* — her hand rising to meet it, the two palms aligned exactly across the split-screen line, both sides at once, static, held.

### Pre-chorus 2 — no laughing this time

35. *"So put the laptop on your palm, lift it slow"* — both already standing when the section starts, laptops already up, no hesitation, matched medium shots.
36. *"Count me in, one, two, here we go"* — the counting mouths again, but now cut in sync to the frame rather than a beat apart.
37. *"Sway to the left when I sway to the right"* — reuse the framing of shot 17, closer, both leaning further, the split line softer.
38. *"Mirror me, baby, we're dancing tonight"* — both rooms warmer; the temperature difference between the two halves has closed to almost nothing, wide.

### Chorus 2 — comfortable now

39. *"Video call slow dance, hold your screen like it's me"* — the dance wider and looser, more floor used on both sides, handheld.
40. *"Two bedrooms, one song, closest we can be"* — the split line drifting off-centre for the first time, giving whichever of them is moving more the bigger half.
41. *"Turn down the lights, I'll turn up the sound"* — he knocks his lamp with an elbow and catches it without stopping the dance, single take, medium.
42. *"Spin me on the carpet, I'll spin you around"* — she nearly drops the laptop, catches it, laughs into the screen, handheld close.
43. *"Video call slow dance, cheek against the glass"* — both of them mouthing the hook at each other rather than singing it, the guitar line answering, two-shot across the split.
44. *"Buffering forever, I don't need it fast"* — a slow drift of the picture on her side, half a second behind his movement, nobody caring.
45. *"If a signal is all we get tonight"* — reuse the hands-toward-the-line framing of shot 25, tighter and warmer.
46. *"Hold your screen like it's me, and hold it tight"* — both rooms fully matched amber, both laptops held tight, the widest symmetrical frame so far.

### Instrumental — the guitar, then the freeze

47. Wide of her alone on floorboards in white socks, dancing in a room that suddenly looks too large, slow push-in from behind.
48. Wide of him alone, his shadow thrown across a bare wall by the lamp, matched push-in.
49. A slow push in on each laptop from behind, so we see the back of the screen and the person beyond it, cut together.
50. The picture stutters, blocks up, and the sound drops out — one side of the frame going flat blue.
51. Black frame, one beat, then her face in the lamplight breathing — the cut into the bridge.

### Bridge — she dances to a frozen picture

52. *"Then the picture froze with your hand on your heart"* — her side only; his half is a frozen blocky still with a spinning wheel composited over it, static wide.
53. *"That little wheel spinning, my screen went dark"* — she stops moving, looks at the frozen frame, waits, close-up, the cold blue and the warm lamp meeting on her face.
54. *"I could've hung up, could've called it a night"* — her hand on the trackpad hovering over the end-call button and not pressing it, macro.
55. *"But I kept on swaying in the lamplight"* — her feet starting to sway again with nothing live on the other side of the screen, low angle, held long.
56. *"And when you came back you were laughing at me"* — the frozen frame snapping back to live motion on a beat: he is already dancing, badly, half a bar behind.
57. *"Cause you never stopped either, out of time, out of key"* — both of them laughing, a two-shot where the split line is barely visible, handheld.
58. *"So it's not the signal, and it's not the screen"* — matched close-ups of both faces, the strings entering, both rooms brightening together.
59. *"It's that you keep dancing when you can't see me"* — the widest two-sided frame of the video so far, both dancing, the split line beginning to move inward.

### Final chorus — the split closes

60. *"Video call slow dance, hold your screen like it's me"* — the biggest version of the dance, both rooms at their fullest warm light, string lights that were always there now switched on.
61. *"Two bedrooms, one song, closest we can be"* — the dividing line narrowing, not a wipe but a physical squeeze, until the two rooms are two halves of one frame.
62. *"Turn down the lights, I'll turn up the sound"* — his hand and her hand on their two lamps at once, both dimming together, macro pair.
63. *"Spin me on the carpet, I'll spin you around"* — a full spin each, the two turns reading as one continuous rotation across the closing gap.
64. *"Video call slow dance, cheek against the glass"* — both cheeks against both screens, mirrored, the split now a hairline.
65. *"Twenty-two more squares and this screen is the past"* — her red pen crossing a square on her own calendar, revealed for the first time — she has been counting too, macro then wide.
66. *"If a signal is all we get tonight"* — both calendars in one frame across the vanishing split, his circled date and hers matching.
67. *"Hold your screen like it's me, and hold it tight"* — the two of them holding the laptops tight, eyes closed, one frame, no visible divide, static and held.

### Post-chorus — the gate

68. *"Hold it like it's me, hold it like it's me"* — the split breaks for the first time: a full-frame airport gate sign (composited), harsh public light, one and a half seconds.
69. *"Till the airport, till the gate, till it's really me"* — an empty arrivals rail, no people, cold overhead light, static.
70. *"Hold it like it's me, hold it like it's me"* — a suitcase standing by a door in a dark hallway, one lamp behind it, low angle.
71. *"Same song, same sway, till it's really me"* — a hand on a boarding pass (composited), then a hard cut back to the bedroom light.

### Outro — three percent

72. *"Nine your time and midnight mine"* — back to the opening framing, two clocks, two lamps, but the split is now a soft seam rather than a wall.
73. *"Battery blinking, three percent"* — the low-battery indicator on her machine (composited), her looking at it and not doing anything about it, close-up.
74. *"Say goodnight slow, then say it again"* — two goodnights overlapping, his and hers, matched close-ups cut on the overlap.
75. *"I'll still be dancing when the call has ended"* — the screen going black; her room lit only by the lamp again; she keeps swaying, alone, in silence, medium wide.
76. *"Twenty-two squares, then no more screen"* — her calendar on the wall behind her, the circled date, her still moving in the foreground out of focus.
77. *"Till then, baby, hold it like it's me"* — final shot: the split closes completely and holds on one frame — her room, one lamp, one person still dancing, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the two space bars in shot 2, each *"video call slow dance"*,
the palms meeting (shot 34), the instrumental, the freeze (shot 52), the
snap back to live (shot 56), the split beginning to close (shot 59), the
gate cut (shot 68), and the final seam. At 94 BPM a bar is 2.55 s; choruses
cut every one or two bars, verses hold two bars or longer.

**The press-play-on-three challenge.** Long-distance couples queue the same
song on both machines, count down, and post the split screen. Cut the
vertical hero from shots 33–34 — the two palms meeting across the divide —
with *"hold your screen like it's me"* on screen. The second shareable frame
is shot 55, dancing to a frozen picture; the third is shot 77, the split
closing to one room.

## 6. Quality-control checklist

- Her room is amber and his is cool blue until shot 26, matched from there on, and they never separate again
- The split line does exactly one thing per section: hard and central through the intro, aligned through chorus 1, drifting in chorus 2, closing from shot 59, gone by shot 67
- Nobody but the two leads appears anywhere, and the airport shots are completely empty
- Every screen, clock, calendar number, battery indicator, buffer wheel and gate sign is composited; no model-generated interface or text
- The freeze in shots 52–55 is a post effect over a live plate, never a generated glitch
- OpenPose on every shot where someone turns while holding a laptop; check for extra hands at the chest and fused fingers on the screen presses
- Continuity: her hair is pinned up until the bridge and down from shot 52 on; his collar is bent on the same side in every shot; the book stack under his laptop stays at three
- The last shot is locked-off and holds until the audio fades
