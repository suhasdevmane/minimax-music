# Wan 2.2 Shot List — "Ride or Die"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
120 BPM a bar is 2.0 s, so most shots are 2–4 s and the chants cut on every
half-bar.

## 1. Visual style

Four friends, one apartment and one car, over ten years. The video moves
between **four kinds of light**, and each one means a different kind of
showing up: motorway sodium (the drive), hospital fluorescent (the wait),
airport fluorescent into dawn (the collection), and warm domestic kitchen
light (the ordinary years). Memories are warm, grainy and slightly
over-exposed; the present is clean and bright. Handheld and close for the
verses, wider and steadier for the choruses. Nothing here is glamorous and
nothing is sad — the register is loud, funny and unembarrassed.

| Section | Grade | Camera |
|---|---|---|
| Intro | Streetlight through a blind, one hall lamp, headlights | Close, dark, handheld |
| Verse 1 (origin) | Warm, grainy, blown highlights | Handheld, memory feel |
| Verse 1 (receipts) | Sodium, fluorescent, stairwell bulb, daylight | Static, one per light source |
| Pre-choruses | Cool blue into warm domestic | Fast cuts, close |
| Choruses | Streetlights strobing, dashboard glow, forecourt | In-car and tracking |
| Post-chorus | Hard, bright, high contrast | 0.5 s, ultra-fast |
| Verse 2 (rap) | Airport fluorescent, dawn terminal, kerbside | Fast handheld montage |
| Instrumental | Bright interior, then kerbside streetlight | Roaming, circle shots |
| Bridge | One streetlight, cold blue sky starting | Static, long holds |
| Final chorus | Every light in the house, then a bright garden | Wide, moving with the crowd |
| Outro | Flat kind daylight | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (present day)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely, minimal makeup, wearing a grey sweatshirt and jeans with a denim jacket over the top, trainers, open unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (memories, nineteen)
> Same female protagonist Mahima, young woman in her late teens, expressive dark eyes, oval face, long dark wavy hair straightened, heavy eyeliner and a fringe, wearing a cropped band t-shirt and a leather jacket too big for her, delighted mischievous expression, realistic cinematic photography, consistent identity

**Mahima** (the flash-forward only, two seconds)
> Same female protagonist Mahima, woman in her sixties, the same expressive dark eyes and oval face, silver-grey hair cut short, deep laugh lines, wearing a linen shirt and gardening trousers, sitting in a folding chair, laughing, realistic cinematic photography, consistent identity

**The best friend** — a young woman of the same age with a face, in every
section: short bleached hair, a nose ring, an oversized denim shirt, a
crooked grin. She is the co-lead of this video and must be as recognisable
as Mahima. She appears at nineteen with longer dark hair, and in the
flash-forward in her sixties with the same crooked grin.

**The other two** — a young man and a young woman who make up the four in
the car and the kitchen. Faces welcome, no arcs of their own.

**The guy** — the ex mentioned in verse one is **never shown**: a doorway, a
shoulder leaving frame, a mattress being carried away from a flat. No face,
ever.

Objects: the **two identical spare keys** on two different keyrings, the
**cardboard arrivals sign** with a printed photo taped to it, the **curling
photograph on the fridge** under a magnet, the **plastic hospital chair**,
the **phone on the kitchen table** in the outro.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the group chat, the arrivals board, the deleted message, the
cardboard sign's photo and the voice-note waveform are composited in the
edit.** Generate phones as lit blank rectangles, the arrivals board as a
blank light box and the cardboard sign as a blank card with a taped
rectangle on it; the model cannot render legible text and this video's
comedy lives in that text.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima across three ages and the best friend across three ages with
IP-Adapter or a character LoRA each — the aged flash-forward is the hardest
identity job in the video and needs its own reference set built from the
present-day stills, not a generic older face. OpenPose for the in-car shots,
the kitchen dancing and the clap circle. Depth for the hallway push and the
arrivals hall. 16:9 first; 9:16 for the car-window chant and the arrivals-sign
cut, which are the shareable ones. Animate in short bursts: one hug, one
clap cycle, one hand out of one window. Car interiors are more reliable
generated as a still with the car parked and the movement added as a
lighting pass in the edit — streetlights strobing across faces sells motion
better than the model's attempt at a moving background.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — the three a.m. call

1. *"Three in the morning and the ringtone is yours"* — a phone face-down on a wooden chair buzzing itself in a slow circle in a dark bedroom, macro, streetlight through a blind.
2. *"I'm out of the bed and I'm into my shoes"* — a hand out of a duvet, then two feet finding trainers on a dark floor without a light being turned on, two cuts, low.
3. *"No question, no why, no what did you do"* — Mahima pulling a coat on over pyjamas in a hallway, phone against her ear, saying nothing, medium.
4. *"Just send me a pin and I'm coming to you"* — a front door left on the latch, then headlights swinging across a bedroom ceiling behind her, two cuts.
5. *"Ride or die"* — her face in a car, engine on, seatbelt going across, held one beat in silence before the drums.

### Verse 1 — the origin and the receipts

6. *"We met in a kitchen at a party neither of us knew"* — memory, warm and grainy: two nineteen-year-olds pressed against a kitchen counter at a crowded house party, both clearly wanting to leave, handheld.
7. *"I said, I hate it here, you said, thank God, me too"* — the two of them recognising each other mid-sentence, then both laughing, close two-shot, blown highlights.
8. *"Ten years and eleven addresses down the line"* — a fast montage of eleven front doors and eleven sets of keys, one per beat, static frames.
9. *"You still know my order and I still know your sign"* — two paper cups set down on a table without either of them asking, close-up on the hands.
10. *"You drove four hours in a car that barely ran"* — a tired car on a motorway at night with one headlight dimmer than the other, static wide from a bridge, sodium light.
11. *"Slept in a plastic hospital chair and held my hand"* — a plastic hospital chair with a coat over its back and two hands joined on the armrest, static, fluorescent, held long.
12. *"You never said, I told you so, about the guy"* — a mattress being carried out of a flat past a doorway where a shoulder leaves frame, the ex never seen, medium.
13. *"You just brought up the mattress and you never asked me why"* — the same mattress going up a narrow staircase carried by two people who cannot see each other, stairwell bulb, handheld and funny.
14. *"There's a photo on your fridge of us at nineteen"* — a fridge door with one curling photograph under a magnet, slow push-in until the faces are clear, kitchen daylight.
15. *"Two idiots in a garden with the whole thing still to see"* — the photograph itself, filling frame, then a slow pull back to the whole kitchen around it.

### Pre-chorus 1 — two-word portraits

16. *"Ambulance friend, airport friend"* — blue light moving across a wall, then an arrivals board (blank light box, composited), two cuts on the beat.
17. *"The one who reads the message that I didn't send"* — a typed message deleted character by character before sending (composited), macro on the screen.
18. *"If the world ends on a Wednesday afternoon"* — a completely ordinary weekday street in flat afternoon light, static wide, deliberately unremarkable.
19. *"I'm not calling anybody, I'm just calling you"* — Mahima looking at a phone, putting it face-down, and it ringing anyway, close-up.

### Chorus 1 — four in a car

20. *"You're my ride or die, and I'd ride for you"* — four friends in one car at night, windows down, all singing the same wrong words, from the front seat looking back.
21. *"Say the word and I'm outside, no questions, no excuse"* — the car pulling up outside a building and one of them already coming out of the door before it stops, wide.
22. *"Ride or die, ride or die"* — the driver's hand on the wheel with the indicator ticking, macro, streetlights strobing across it.
23. *"I'll be the phone call that you never have to try"* — a phone screen lighting the whole car interior for one second (composited), then dark, then faces.
24. *"Nobody's coming, so we came for each other"* — the back seat filmed from the front: three of them wedged in, laughing, medium.
25. *"Nobody chose us, so we chose one another"* — a petrol station forecourt at night, all four out of the car doing nothing useful, wide, hard overhead light.
26. *"Whatever the year does, whatever it puts us through"* — the car moving through a tunnel, lights running over four faces in sequence, tracking.
27. *"You're my ride or die, and I'd ride for you"* — a wide from outside: one car on an empty road at night with its windows down and noise coming out of it.

### Post-chorus 1 — the chant

28. *"Hey, ride or die, ride or die"* — four hands out of four car windows, one per window, 0.5 s.
29. *"Hands up if you've got one, hands up high"* — a kitchen with four people dancing badly, hands up, 0.5 s.
30. *"Ride or die, ride or die"* — a hand slapping a car roof twice, macro, 0.5 s.
31. *"That's my people, that's my ride"* — a fist meeting a fist, then both hands opening, close-up.

### Verse 2 — the rap

32. *"Group chat got a name that we can never say out loud"* — a group chat scrolling at speed on a phone (composited), thumb flicking, macro.
33. *"Four hundred unread and a blurry photo of a crowd"* — a genuinely blurry photo of four people at a gig filling the frame, held for exactly one beat.
34. *"You got a spare key, I got the same"* — two identical keys on two different keyrings held side by side, macro.
35. *"You know the exact wrong thing to say to make me okay"* — the best friend saying something clearly inappropriate across a table and Mahima laughing against her will, two-shot.
36. *"Arrivals hall at a quarter to five"* — an arrivals hall at dawn, almost empty, a cleaner working, wide, fluorescent against a blue window.
37. *"Cardboard sign with my worst photo on the side"* — the best friend holding a badly made cardboard sign with a printed photo taped to it (composited), grinning, medium.
38. *"I flew in a wreck and I walked out a joke"* — Mahima coming through the arrivals gate looking destroyed, seeing the sign, and losing it completely, handheld.
39. *"You had gum and a coffee and you didn't make me talk"* — a paper coffee cup and a packet of gum handed over without a word, close-up on the exchange, then two people walking in silence.
40. *"Held my hair and my secret on the very same night"* — a hand gathering hair back at a kerbside, filmed from behind, gentle and not comic, streetlight above.
41. *"Then buried it deeper than the reason for the flight"* — the next day: the two of them on a sofa in daylight watching something, neither of them mentioning it, wide static.
42. *"You are the reason that I know I'm not too much"* — Mahima mid-story with both arms out, taking up the whole frame, and nobody asking her to be smaller.
43. *"You call me on my nonsense and it still feels like love"* — the best friend cutting her off with one raised eyebrow, then both of them laughing, close two-shot.

### Pre-chorus 2 — funnier portraits

44. *"Bail money friend, bad haircut friend"* — a cash machine at night, then a bathroom mirror with a genuinely bad home haircut being surveyed, two cuts.
45. *"The one who says the true thing and then stays till the end"* — someone saying something hard across a kitchen table, then not getting up, static, long hold.
46. *"If the world ends on a Wednesday afternoon"* — reuse shot 18, now with four people walking through the same ordinary street.
47. *"I'm not calling anybody, I'm just calling you"* — a phone already ringing before it is picked up, macro.

### Chorus 2 — the house fills up

48. *"You're my ride or die, and I'd ride for you"* — the same car, different season, rain on the windows, four of them singing, from the front.
49. *"Say the word and I'm outside, no questions, no excuse"* — a kitchen with more people in it than chorus one, handheld through the crowd.
50. *"Ride or die, ride or die"* — the indicator again, daylight this time, macro.
51. *"I'll be the phone call that you never have to try"* — four phones face-down in a row on a table, nobody looking at any of them, static.
52. *"Nobody's coming, so we came for each other"* — the four of them at a table singing with the brass playing off a stereo, wide.
53. *"Nobody chose us, so we chose one another"* — a door opening and two more people arriving with bags of food, medium.
54. *"Whatever the year does, whatever it puts us through"* — a slow pan of the kitchen: every surface covered, everyone talking at once.
55. *"You're my ride or die, and I'd ride for you"* — the two leads in the middle of the crowded kitchen, foreheads almost touching, shouting the line at each other, close.

### Instrumental — brass in the front room

56. A real brass section playing in somebody's front room, plainly too big for it, the trombone slide nearly hitting a lamp, wide and funny.
57. The clap breakdown as four pairs of hands in a circle, filmed from directly above, cutting on every clap.
58. A slow push down a hallway lined with photographs from every year, ending on the most recent one.
59. The four of them on a kerb at four in the morning eating chips with their feet in the gutter, wide, streetlight.
60. A single held frame of the two leads sitting slightly apart from the others, saying nothing, as the build starts.

### Bridge — the vow

61. *"Nobody hands you a certificate for this"* — the two of them on the kerb with a bag of chips between them, not looking at each other, static, one streetlight.
62. *"No aisle, no ring, no photograph, no priest"* — a wide of an empty road with the two of them very small in the bottom of the frame, held.
63. *"But if there were vows then I'd say them in the road"* — Mahima standing up into the middle of the empty road, arms out, saying it to nobody, wide.
64. *"I'd say them in the group chat, I'd say them in the cold"* — a phone typing something long and then just being put down without sending, macro.
65. *"For better, for worse, for whatever we go through"* — a hand landing on a shoulder and staying there, held four full seconds without a cut.
66. *"You were never plan B, it was always me and you"* — both of them on the kerb from behind, the cold blue sky beginning above the rooftops, static, the quietest frame in the video.

### Final chorus — everybody

67. *"You're my ride or die, and I'd ride for you"* — a packed kitchen singing the hook at full volume, every light in the house on, wide handheld.
68. *"Say the word and I'm outside, no questions, no excuse"* — the brass section jammed into the kitchen doorway playing over everyone's heads, low angle.
69. *"Ride or die, ride or die"* — a room of raised hands, whip pan across them.
70. *"I'll be the phone call that you never have to try"* — the two leads pulled together by other people's arms, laughing, medium.
71. *"Nobody's coming, so we came for each other"* — a chair stood on, then thought better of, then stood on anyway, wide.
72. *"Nobody chose us, so we chose one another"* — the four originals in a line with their arms round each other, static, the anchor frame.
73. *"Forty years from now with a garden and a chair"* — two seconds of flash-forward: two women in their sixties in folding chairs in a garden, mid-laugh, bright daylight.
74. *"Same two idiots and the same bad hair"* — the older pair reaching for the same thing at the same time, then a hard cut back to the kitchen.
75. *"Whatever the year does, whatever it puts us through"* — the crowded kitchen from the doorway, everyone singing, nobody looking at camera.
76. *"You're my ride or die, and I'd ride for you"* — the two leads in the centre of it, the widest and warmest frame of the video.

### Post-chorus 2 — hands up

77. *"Hey, ride or die, ride or die"* — a room of raised hands from floor level, 0.5 s.
78. *"Hands up if you've got one, hands up high"* — a car roof slapped twice in daylight, 0.5 s.
79. *"Ride or die, ride or die"* — the fridge photograph, now with a second photo taped beside it, macro.
80. *"That's my people, that's my ride"* — the front door of the flat standing open with noise coming out of it, static, from the landing.

### Outro — the voice note

81. *"Voice note at midnight, three minutes long"* — a phone lying flat on a kitchen table playing a voice note, waveform composited, macro, quiet room.
82. *"Half of it laughing and the rest of it wrong"* — Mahima listening while doing something else entirely, washing a mug, half-smiling, medium.
83. *"Nothing important, and I play it twice"* — her thumb pressing play a second time without looking, close-up.
84. *"That's the whole thing, that is the whole of my life"* — her sitting down at the table with the phone still playing, chin on her hand, static.
85. *"You're my ride or die, and I'd ride for you"* — final shot: she walks out of frame and the camera does not follow; the phone on the table in a sunlit empty kitchen, the note still playing, a laugh in it. Hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the seatbelt (shot 5), the fridge photograph (shot 14), each
"ride or die", every chant, the arrivals sign (shot 37), the clap circle
(shot 57), the shoulder hold (shot 65), the flash-forward (shot 73) and the
final locked-off kitchen. At 120 BPM a bar is 2.0 s; the choruses cut every
bar and the chants cut on every half-bar.

**The arrivals-sign challenge.** Shots 36–39 recut vertically are the
shareable fifteen seconds: empty dawn terminal, the terrible cardboard sign,
the collapse, the coffee handed over in silence. Invite people to post the
worst photo of a friend they have ever held up at an airport, with the chant
over it. The four-hands-out-of-four-windows frame (shot 28) is the second
shareable cut.

**Caption cut:** shots 61–62 with *"Nobody hands you a certificate for
this."*

## 6. Quality-control checklist

- Three ages for both leads: nineteen in the memories, present day throughout, sixties for exactly two seconds at shots 73–74 and nowhere else
- The best friend is as recognisable as Mahima in every section; she is a co-lead, not an extra
- The ex has no face at any point — doorway, shoulder, or absent
- Four light worlds stay separate: motorway sodium, hospital fluorescent, airport fluorescent into dawn, warm kitchen; no shot mixes two
- The kerbside hair shot (40) is filmed from behind, gentle, and never played for comedy
- All screens, the arrivals board, the cardboard sign's photo, the group chat and the waveform are composited; no model-generated text
- The crowd only grows across the choruses: four, then a kitchen, then a full house
- The last shot holds on an empty kitchen with the voice note still playing and does not cut when she leaves frame
