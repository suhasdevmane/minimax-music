# Wan 2.2 Shot List — "Pretty When You Laugh"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
90 BPM a bar is 2.67 s, so most shots are 4–6 s and the choruses breathe
rather than cut.

## 1. Visual world

A live-band record filmed like one: warm rooms, practical lamps, real
locations that are deliberately unglamorous — a kitchen table, a bus, a pub,
a supermarket aisle. **Kai is the subject of this video and Mahima is the
camera**: in almost every chorus frame he is lit and centered and she is at
the edge of it, watching. Two sequences break the warmth. The **funeral** is
the coldest, most desaturated footage in the film, and the **stairwell and
bus** in the second pre-chorus are the only fluorescent and gray frames. The
chorus is not a performance — it is a slow-motion portrait of a man laughing,
shot like a love letter.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cool hallway against a warm room beyond | Static, one slow turn |
| Verse 1 | Warm interiors, one bright exterior | Comic cutaways, close-ups |
| Pre-chorus 1 | Warm kitchen, practical lamps | Handheld, loose |
| Choruses | Warm gold, widest and brightest of the film | Slow motion, held portraits |
| Verse 2 | Desaturated February, faces the only color | Static, then near-black |
| Pre-chorus 2 | Fluorescent stairwell, gray bus window | Static, tight |
| Instrumental | Band-room warm, then deliberately mixed | Handheld, archive-feel |
| Bridge | One window, side light, dim room | Locked off, one subject |
| Final chorus | Warmest and busiest frames in the video | Moving, wide, full table |
| Outro | Cool hallway, then one lamp in an empty room | Matched to the intro |

## 2. Character bible — paste into every prompt

**Mahima** (the present day, most of the film)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a center part, warm natural makeup, wearing a mustard-yellow knitted vest over a white long-sleeve shirt and dark jeans, watching amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the funeral, February)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back low, no makeup, wearing a plain black high-neck dress under a heavy dark coat, careful contained expression, realistic cinematic photography, consistent identity

**Kai** (the subject of the film — he is on camera more than she is)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a soft green corduroy overshirt over a white tee and dark jeans, wide open unselfconscious laugh with his eyes shut and his head going back, realistic cinematic photography, consistent identity

**The funeral room** — an older woman in her sixties (his mother), an older
man in his seventies telling the story with his hands, and eight to ten
mourners. His mother and the storyteller get faces; everyone else is turned
away or out of focus.

**The friends and the final table** — a rotating group of six to eight, plus
two children at the last table only. No individual friend is ever the subject
of a shot.

Objects: the **closed door with warm light under it**, the **hand over the
mouth**, the **birds on the wire**, the **phone with the voice note**, the
**too many black coats**, the **kitchen table**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The phone screen, the folder, the audio file and its waveform are
composited in the edit.** Generate the phone as a lit blank slab and overlay
the interface in post — the model cannot render legible UI, and the voice
note is the object the last line of the song turns on.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA, and
build Kai's reference set specifically around **laughing** — eyes shut, head
back, hand over mouth, mid-wheeze, and the still face two seconds before it
starts. That last one matters: shot 22's whole job is the silence before the
laugh. Depth for the funeral room and the final table so ten people hold
their real distances. OpenPose is only needed for the fall into the sofa.
16:9 first; 9:16 for the chorus portraits, which are the natural vertical
content. Animate in short bursts and let the slow-motion chorus shots run
long — 5–6 s each, generated at 24 fps and retimed rather than generated
slow.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s; the chorus portraits are the longest single shots in the film.

## 4. Scene per lyric line

### Intro — the sound through a wall

1. *"I heard you before I saw you, through a wall in someone's house"* — a cool hallway, a closed door with warm light spilling under it, Mahima standing outside it with a drink, not moving, static.
2. *"Some joke I never got the start of, and a sound came out"* — her head turning toward the door on the word, close-up, the room noise blooming through the wall.
3. *"Big and dumb and honest and completely out of key"* — her hand landing on the door frame, macro, the light on her fingers from under the door.
4. *"And I thought, whoever that is, I want to know what's funny"* — the door opening onto a room of people, everyone out of focus, one shape in the middle of it laughing, wide.

### Verse 1 — the catalog

5. *"You laugh like a door coming off its hinge"* — a door swinging badly on one hinge in an empty room, shot beautifully and completely straight, macro.
6. *"Like a kettle, like a seagull, like a bad idea"* — three cuts: a kettle reaching the whistle; a seagull on a railing against a bright sky; a hand knocking over a full glass in slow motion.
7. *"You put your whole hand over your mouth like you're embarrassed"* — Kai's whole hand clamped over his own mouth, eyes streaming, close-up, warm.
8. *"Then it comes out through your fingers anyway"* — the same shot continuing, the sound escaping through his fingers, his shoulders going, extreme close-up.
9. *"It scared the birds up off the wire at the bus stop"* — a line of birds on a wire going up all at once, wide, flat afternoon daylight.
10. *"It made a stranger on the crosstown bus turn around"* — a stranger two rows ahead on a bus turning around, filmed from behind so no face, unbothered, medium.
11. *"You crack before the punchline every single time"* — Kai losing it halfway through telling a story and never reaching the end of it, one continuous take.
12. *"And I have never wanted anything more in my life"* — Mahima watching him do it, an expression that gives her away completely, close-up, the warmest thing in a cool bus.

### Pre-chorus 1 — working for it

13. *"So I say the stupid thing, I do the stupid voice"* — Mahima at a kitchen table doing an extremely bad impression with total commitment, handheld.
14. *"I'd fall down a whole flight of stairs on purpose"* — a very short shot of her deliberately falling backwards into a sofa, arms out, wide.
15. *"I have got no pride, no shame and no material"* — the joke landing nowhere: a table of blank faces, one person checking a phone, her taking it well, wide.
16. *"And I'll take a bad review just to hear it once"* — her shrugging and going again, undeterred, medium, tambourine on the cut.

### Chorus 1 — the portrait

17. *"You're pretty when you laugh"* — slow motion: Kai actually laughing, eyes shut, head going back, the longest held shot so far, warm gold.
18. *"So I'll never stop trying"* — the table around him going up in slow motion, everyone out of focus except him, wide.
19. *"Say something back to me, I'll set you up all night"* — Mahima leaning in and setting up a joke, mouth moving, no sound in the mix, close-up.
20. *"I'll be the worst comedian in town and call it dying"* — the punchline landing on him, his hand going to the table, slow motion.
21. *"Give me the wheeze, give me the eyes going gone"* — extreme close-up on his eyes disappearing into the laugh, held.
22. *"Give me the two seconds of silence before it comes"* — his face completely still, the moment before it starts, held for the whole line with no cut and no sound.
23. *"You're pretty when you laugh"* — Mahima at the edge of the frame, not laughing at the joke at all, laughing at him, medium.
24. *"So I'll never stop trying"* — the whole warm room in one wide, him in the middle of it, her at the edge, slow motion.

### Verse 2 — February

25. *"February, and your uncle's funeral, and the coats"* — a hallway hung with too many black coats on a rail, desaturated, static, held.
26. *"And your mother saying nobody's eaten anything all day"* — a table of untouched food and an older woman standing beside it with her arms folded, medium.
27. *"Then somebody told a story about a boat and a dog"* — an older man beginning a story with his hands, the room around him standing in small silent groups, wide.
28. *"And you went first, and everybody followed you"* — Kai's face breaking first, then the room going one by one behind him, a laugh moving through it like weather, one continuous take.
29. *"I watched a room of people put their shoulders down at once"* — a wide of the whole room from a doorway, every set of shoulders visibly dropping, the coldest frame in the film.
30. *"And I understood what you are actually for"* — Mahima (funeral look) in the doorway, understanding something, close-up, the only warm-toned face in the sequence.
31. *"That night you said, was that alright, and I said, that was the best of you"* — night, a dark bedroom, only the shape of two people lying awake, almost no light at all.
32. *"And you laughed at that as well, quietly, in the dark"* — hold on near-black with only the sound of a quiet laugh, no picture, two full seconds.

### Pre-chorus 2 — the voice note

33. *"So I keep a voice note in a folder on my phone"* — extreme close-up of a phone, a folder, one audio file (UI composited), her thumb above it.
34. *"Fourteen seconds of you losing it at nothing"* — the waveform playing across the screen (composited), macro, the only screen shot in the video.
35. *"On the days I can't reach you and the days I can't reach me"* — Mahima in a fluorescent office stairwell with one earbud in, static, gray-green light.
36. *"I put it on, and the whole place starts to move"* — the smile arriving against her will, close-up, then a gray bus window where it does not fix anything and she plays it again.

### Chorus 2 — the portrait continues

37. *"You're pretty when you laugh"* — Kai laughing in a car, the driver's seat, one hand off the wheel, slow motion.
38. *"So I'll never stop trying"* — Kai laughing in a supermarket aisle at something off-camera, deliberately unglamorous, wide.
39. *"Say something back to me, I'll set you up all night"* — Mahima across a pub table, mid-setup, close-up, horns answering on the cut.
40. *"I'll be the worst comedian in town and call it dying"* — the pub table going up around him, slow motion, warm.
41. *"Give me the wheeze, give me the eyes going gone"* — reuse the eyes close-up, tighter, in a different room and different light.
42. *"Give me the two seconds of silence before it comes"* — a second version of the silent held face, this time in the car, no cut.
43. *"You're pretty when you laugh"* — Mahima at the edge of the pub frame, watching, medium.
44. *"So I'll never stop trying"* — a wide of a kitchen with him at the center of it, her at the edge, both in the same light for once.

### Instrumental — the band and the years

45. A baritone saxophone player in a warm band room actually playing, hands and horn, medium.
46. The horn section as a group in the same room, three players in one frame, wide, low light.
47. A fast run of very short archive-feel clips of Kai laughing across several years — different hair, different seasons, different rooms.
48. The run continuing, deliberately mixed in quality and aspect, like real footage someone kept.
49. Mahima's face at the end of the run, present day, still watching — the cut into the bridge.

### Bridge — direct address

50. *"People say it's the eyes, people say it's the smile"* — Mahima alone at the kitchen table, straight to camera for the only time in the film, one window, side light, locked off.
51. *"People marry a jawline and wonder what went wrong"* — two seconds: a magazine-perfect face on a poster in a bus shelter, deliberately lifeless, static.
52. *"But a face is just a face on a cold gray morning in November"* — two seconds: a cold November street with absolutely nothing happening on it, wide.
53. *"And a laugh is a whole climate, and you brought yours along"* — back to the kitchen table, same framing, no cut from here to the end of the section.
54. *"So keep the eyes, keep the smile, keep whatever they were selling"* — the same unbroken shot, her hands flat on the table.
55. *"I fell for the sound, and I would fall for it again"* — the same shot, held two seconds after the line ends, then a drum fill and a hard cut.

### Final chorus — thirty years on

56. *"You're pretty when you laugh"* — the same kitchen table, now with more chairs, more people, two children among them, wide, the busiest frame in the film.
57. *"So I'll never stop trying"* — Mahima telling a joke to the full table and getting it slightly wrong, handheld.
58. *"Thirty years from now I'll still be working on the timing"* — Kai going anyway, immediately, before she has finished, close-up.
59. *"Still be dying at the table, still be trying"* — the entire table going up, plates and glasses moving, wide, full horns.
60. *"Give me the wheeze, give me the eyes going gone"* — the eyes close-up one last time, the fullest light of any version of it.
61. *"Give me the two seconds of silence before it comes"* — the whole table silent and waiting on him, held, nobody moving.
62. *"You're pretty when you laugh"* — a handclap layer visible around the table, everyone joining in, wide.
63. *"So I'll never stop trying"* — the two of them at the end of the table, the oldest thing in the room being the joke, medium two-shot.

### Post-chorus — call and response

64. *"I'll never stop trying, no I'll never stop trying"* — the table clapping on the beat, hands only, close-up.
65. *"Tell me it's not funny, I'll go get another one"* — a child at the table copying the laugh badly and being copied back, medium.
66. *"I'll never stop trying, no I'll never stop trying"* — Kai's hand over his mouth again, the same gesture as shot 7, thirty years of it.
67. *"You're pretty when you laugh and I am never going to stop"* — Mahima walking out of the room already thinking of the next one, tracking from behind.

### Outro — the bookend

68. *"I heard you before I saw you, through a wall in someone's house"* — the exact hallway and closed door from shot 1, matched framing, the laugh audible through it, static.
69. *"And I've heard it every day since and I still turn around"* — her head turning toward the door exactly as it did in shot 2, matched, close-up.
70. *"If you go before me, leave the fourteen seconds on"* — a quiet room, a phone on a table, the voice note playing to nobody, one warm lamp, static.
71. *"And I'll play it in an empty room and swear you're still in it"* — final shot: the empty room with the sound still in it, the lamp the only light, locked off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the door opening, the hand over the mouth, each *"you're pretty
when you laugh"*, the two seconds of silence, the funeral wide, the near-black
laugh, the voice note, the instrumental, *"I fell for the sound"*, the full
table, and the phone playing to nobody. At 90 BPM a bar is 2.67 s; the
chorus portraits run two bars each and the near-black shot 32 holds with no
cut at all.

**The voice-note challenge.** The shareable cut is the chorus, shots 17–24,
vertical, with the silence in shot 22 landing on the beat. Invite people to
post fourteen seconds of somebody they love laughing at nothing, over the
hook. The second shareable frame is the portrait format itself: a slow-motion
close-up of one person laughing, shot like a love letter, with the caption
line on screen.

## 6. Quality-control checklist

- Two Mahima looks in the right sections: mustard vest everywhere, the black dress and coat only for shots 25–30
- Kai is lit and centered in every chorus frame and Mahima is at the edge of it, watching — if she is ever the center of a chorus shot the film has gone wrong
- The funeral sequence is the only desaturated footage and shot 29 is the coldest frame in the video; shots 35 and 36 are the only fluorescent and gray frames
- Shot 32 holds on near-black with sound only, and nothing is cut into it
- Shot 22 has no sound and no movement for its whole length — it is the hinge of the chorus
- The phone, folder, audio file and waveform composited in the edit; no model-generated text anywhere
- No distorted hands in the hand-over-mouth, thumb, clapping and table close-ups
- Shots 1 and 68, 2 and 69 are exact framing matches; the last shot is locked off, nobody enters it, and it holds until the audio fades
