# Wan 2.2 Shot List — "Loud Lipstick"

**One shot per lyric line**, built from the submission's per-section video
direction. At 130 BPM a bar is 1.85 s, so the choruses cut on the bar and
the post-chorus stomp cuts on the half-bar. Take timestamps from the
rendered WAV.

## 1. Visual world

A wet Manchester night, shot like a gig rather than a fashion film.
**Colour is the story**: the first third of the video is near-monochrome
beige and grey, and red arrives with the lipstick and never leaves. Three
places — a small flat bathroom, a club (queue, toilets, floor, small stage)
and the top deck of a night bus — plus a flat-daylight school hall for the
bridge. Everything practical: sodium street light, club red and white,
toilet fluorescent, bus strip light. Strobe used twice and never on the last
eight bars of a chorus. Handheld, in the crowd, sweat on the lens.

| Section | Grade | Camera |
|---|---|---|
| Intro | Harsh bathroom white, black rain window, one red | Macro, static |
| Verse 1 flashbacks | Desaturated to nearly monochrome | Flat, locked off, unflattering |
| Verse 1 present | Warm lamp-lit flat | Handheld, close |
| Pre-choruses | Sodium orange, red spill from a doorway | Tracking, low |
| Choruses | Red and white club light, hard shadows | Handheld in the crowd |
| Post-chorus | House lights half up, faces visible | Floor level, wide |
| Verse 2 | Toilet fluorescent, green exit light at the fire door | Close, crowded |
| Instrumental | Red wash to one white key, then everything | Silhouette and faces |
| Bridge | Flat house lights; school hall in flat daylight | Static, wide, still |
| Final chorus | Full red and white, no strobe | Stage and crowd wides |
| Outro | Bus fluorescent, orange light passing in bars | Static, close |

## 2. Character bible — paste into every prompt

**Mahima** (the beige two years — flashbacks only)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled back flat into a low tie, no makeup, wearing an oversized oatmeal jumper and grey trousers, shoulders rounded, apologetic closed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the night — the primary look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with volume and a slight wave, sharp eyeliner and a matte pillar-box red lip, wearing a black leather jacket over a red slip dress and heavy boots, gold hoops, bright fearless expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (night bus, outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair flattened by sweat and rain, red lip worn away to a stain, wearing the black leather jacket zipped over the red dress, tired contented expression, realistic cinematic photography, consistent identity, natural skin texture

**The stranger in the toilets** — a woman in her twenties at the mirror, face fully visible, initially unsure and then transformed by the borrowed lipstick. She reappears in the front row of the final chorus wearing it.

**Steph and the friends** — two women, faces visible, warm and loud, present from pre-drinks to the speaker stack.

**Somebody's ex** (verse two) — faceless. A shoulder and a jaw in green exit light, out of focus, never a reverse angle, never a reaction shot. **There is no male romantic lead in this video.**

**The nine-year-old** (bridge) — a child in a school hall singing far too loudly; only an adult's hand, palm down, lowering in frame. The adult is never shown.

Objects: the **red lipstick** (wound up, the lid clicking, handed away and
never returned), the **beige coat** given to the cloakroom and never seen
again, the **cloakroom ticket**, the **glass with a red mark on the rim**,
the **report card in a drawer**, the **bag of chips**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, tickets and paperwork are composited in the edit** — the group
chat lighting up the phone, the cloakroom ticket number, the report card and
its two words. Generate blank paper, a blank ticket and a lit blank phone,
then overlay in post; the model cannot render legible lettering and the two
words on the report card are the emotional hinge of the bridge.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA, and note
that the beige look and the night look must read as the same face — that
contrast only works if the identity is stable. **OpenPose for every crowd
shot**, the jump on the chorus, the stomp-and-clap block and the climb onto
the speaker stack; a room of people jumping on one beat is where this model
falls apart without pose references. Depth for the club interiors and the
bus. 16:9 first; 9:16 recomposition for the mirror, the stomp block and the
stage cuts. Animate in short bursts: one lipstick stroke, one lid click, one
jump, one hand going up, condensation running down a window.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s.

## 4. Scene per lyric line

### Intro — the steamed mirror

1. *"Half six, bathroom light, rain down the pane"* — a small flat bathroom, harsh white light, the window black and streaming with rain, nobody in frame, static wide.
2. *"Wiped the steam off the mirror with the side of my hand"* — her hand dragging across the steamed mirror in one stroke, the streak revealing one eye, macro.
3. *"One stripe of red and she's back again"* — extreme macro of a red lipstick being wound up, then one stripe drawn across the bottom lip, no other colour in frame.
4. *"The girl I put in a drawer, and she's turned up with a plan"* — she presses her lips together and looks up into the cleared streak, meeting her own eye, static close.
5. *"Right then"* — the lipstick lid pushed on with an audible click; hard cut to black on the click, then the stick count into the verse.

### Verse 1 — two years of beige

6. *"Two years in beige and I called it peace"* — flashback, near-monochrome: her in an oatmeal jumper in a grey meeting room, saying nothing, locked off and unflattering.
7. *"Kept my voice at the volume of a library seat"* — the same room, someone speaking over her; she stops mid-sentence and lets it go, static.
8. *"Said sorry to a chair, said sorry to the rain"* — she walks into a chair leg and apologises to it, then apologises to the sky under a bus shelter, two quick cuts.
9. *"Held the door for people who'd not hold it again"* — her holding a door for three people who do not look at her, held two beats too long, wide.
10. *"Then Steph texted, pre-drinks, half seven, her place"* — present, warm lamp light: a phone lighting up face-up on a duvet with a group chat (composited), her hand reaching for it.
11. *"And I found the red at the bottom of a case"* — a make-up case upended onto the duvet, everything grey and beige, the red rolling out and stopping, macro.
12. *"Rolled it in my fingers like a little bit of proof"* — the lipstick turning slowly between her fingers, close-up, the only saturated object in the frame.
13. *"That I used to be the girl who took up the room"* — a two-second flash of a much younger version of her mid-laugh in a crowded kitchen, colour, then back to the duvet.
14. *"The lid came off with a click like a lock"* — the lid coming off in macro with the click, matched exactly to shot 5 in reverse, hard light.
15. *"And the one in the mirror said, right then, off we pop"* — her in the bedroom mirror in the leather jacket and the red, grabbing keys, out of frame before the line ends.

### Pre-chorus 1 — the queue

16. *"Cab on the corner, heels on the kerb"* — a boot landing in a puddle on the kerb, sodium orange, macro, the cab door closing behind it.
17. *"Queue in the drizzle and I don't say a word"* — the queue under fine rain outside a club door, breath visible, her in the middle of it, static wide.
18. *"Cloakroom ticket, coat off, hair down"* — the beige coat handed through a cloakroom hatch and taken away, a paper ticket pressed into her palm (composited).
19. *"Bass through the floor coming up through the ground"* — low angle on the floor of the corridor, dust jumping with the bass, red spill from the doorway ahead.
20. *"Right then. Let's go"* — a held cymbal, her hand on the door, one beat of stillness, then the door swinging in.

### Chorus 1 — the floor

21. *"Loud lipstick, louder me"* — she walks into the room on the crash and the whole floor jumps, handheld from inside the crowd.
22. *"Kicked the door off the quiet and I set it free"* — the club door swinging back and hitting the wall, red light flooding the corridor behind it, low angle.
23. *"Two years small, now the whole road knows"* — a hard cut to a flat, near-monochrome flashback frame for half a second, then straight back to red.
24. *"Red on the rim of the glass wherever it goes"* — macro of a red lipstick mark on a glass rim, the glass lifted out of frame.
25. *"You can hear me in the queue, you can hear me in the cab"* — the crowd shouting the hook straight at camera, sweat on the lens, handheld and close.
26. *"I'm not sorry for the space and I'm not giving it back"* — her with her arms wide in the middle of the floor, people moving around her, slow-motion for one bar.
27. *"Sing it with your chest till the ceiling agrees"* — a low angle up at the ceiling with condensation on it and a hundred hands below, wide.
28. *"Loud lipstick, louder me"* — the room landing on the downbeat together and freezing for half a second, locked off.

### Post-chorus 1 — stomp and clap

29. *"Louder, louder, louder me"* — floor level: forty feet stomping on a wooden floor on the beat, house lights half up.
30. *"Louder, louder, let the whole street see"* — the same stomp from a high wide, the whole room in the pattern.
31. *"Red on the rim, red on the rim"* — a row of glasses on a bar shelf, every one with a red mark, slow lateral track.
32. *"Louder, louder, let the night begin"* — hands clapping above heads in a wave across the room, tracking.
33. *"Hands up if you've ever been told to calm down"* — hands going up one after another across the frame, faces visible and laughing, wide.
34. *"Hands up, hands up, we are not calming down"* — her at the front with the whole crowd behind her, all shouting it, house lights up, static.

### Verse 2 — the toilets and the fire door

35. *"Half eleven, toilets, mirror full of us"* — six women crammed at a club toilet mirror, fluorescent light, everyone talking at once, wide.
36. *"One I'd never met said, your colour is mad"* — the stranger leaning in, pointing at Mahima's mouth in the mirror, both faces in the glass.
37. *"I said, take it, go on, do your top lip"* — the lipstick handed over, close-up on the exchange of hands, the fluorescent flattening everything but the red.
38. *"She came out braver, and she kept it, and that's it"* — the stranger looking at herself differently, then dropping the lipstick into her own bag; Mahima sees and does not ask for it.
39. *"Somebody's ex was stood by the fire door"* — a propped fire door in green exit light, a faceless shoulder and jaw out of focus in the gap.
40. *"I said alright, mate, and I meant nothing more"* — a two-second nod from her, then she turns back into the room before the shot has finished with him.
41. *"Two years back that would have been my whole night"* — a half-second flash of the beige look standing alone at the edge of a room, then gone.
42. *"Now it's just a face in a bit of red light"* — the fire door out of focus in the far background behind a foreground of dancers, the depth doing the argument.
43. *"Then the DJ dropped the one we all know"* — the DJ booth from below, a hand on a fader, the whole room's arms going up behind it.
44. *"And the floor came up like it wanted a go"* — floor level looking up as the crowd jumps, the boards flexing, dust and steam in the light.

### Pre-chorus 2 — maximum heat

45. *"Sweat on the ceiling, hands in the air"* — condensation actually dripping from a low ceiling onto upturned faces, macro then wide.
46. *"Somebody starts it and the whole room's there"* — one person starting the chant at the back, the room joining in a visible wave toward camera.
47. *"Feet on the speaker stack, hair coming down"* — Steph and a friend holding her ankles as she climbs onto a speaker stack, low angle.
48. *"Bass through the floor coming up through the ground"* — from up on the stack, looking down: the whole floor moving as one, wide.
49. *"Right then. Let's go"* — a held cymbal, everyone frozen mid-motion, her at the top of the stack, one beat.

### Chorus 2 — from the stack and the stage

50. *"Loud lipstick, louder me"* — her eyeline over the entire room from the speaker stack, arms out, handheld.
51. *"Kicked the door off the quiet and I set it free"* — over her shoulder into the crowd, every face shouting the same words.
52. *"Two years small, now the whole road knows"* — a hard cut to a small stage at the end of the room with a mic stand under a red wash, empty.
53. *"Red on the rim of the glass wherever it goes"* — a bar towel wiping a glass and failing to remove the red mark, macro, funny.
54. *"You can hear me in the queue, you can hear me in the cab"* — quick intercut: the queue outside in the rain still hearing the bass through the wall.
55. *"I'm not sorry for the space and I'm not giving it back"* — the beige coat visible on a rail in the cloakroom, alone, in the background of a passing shot.
56. *"Sing it with your chest till the ceiling agrees"* — a wide from the back of the room over every raised hand toward the red stage.
57. *"Loud lipstick, louder me"* — she steps onto the stage on the last word, backlit white, the crowd going up.

### Instrumental — solo, breakdown, build

58. A guitarist in silhouette against the red wash, only the neck of the guitar catching white light.
59. The crowd in half-time slow motion, faces mid-shout, sweat and steam, one long move through them.
60. A stack of glasses behind the bar, every rim marked red, a spilled drink running across the counter.
61. Everything drops to one white key light and a single figure on the floor keeping the stomp going alone.
62. The snare-roll build shot entirely on faces, one per beat, accelerating until the whole room is in frame.

### Bridge — the school hall

63. *"It was never the colour, it was never the shade"* — house lights up, the room half empty, her alone on the small stage with the mic, static wide, unflattering.
64. *"It was two years of quiet finally paid"* — a close-up of her face with the club lights off, the red lip the only thing left of the night.
65. *"You can take my lipstick, take the whole case"* — the stranger from the toilets applying it in the background of the frame, out of focus, unbothered.
66. *"I would still walk in like I own the place"* — her walking the length of the empty floor in house light, no music-video lighting at all, tracking.
67. *"I was loud at nine years old in a school hall"* — flat daylight: a nine-year-old singing far too loudly in a school hall, arms out, entirely certain.
68. *"Somebody said bring it down, so I did, that's all"* — an adult hand entering frame, palm down, lowering; the child's volume visibly dropping; the adult never shown.
69. *"They wrote it on a report card, too much, too loud"* — a report card in a drawer with two words underlined (composited), macro, flat light.
70. *"And I have been apologising to a paper crowd"* — the drawer closing slowly on it, then a cut to her adult hand still resting on the handle.
71. *"Well, the volume is back and it isn't for you"* — back on the stage, she lifts the mic off the stand as the band slams in and the red returns in one frame.
72. *"It's for the girl in the toilets and the nine-year-old too"* — a two-shot in her eyeline: the stranger in the crowd, then a flash of the child, then the crowd again.

### Final chorus — the stage

73. *"Loud lipstick, louder me"* — her on the stage with the mic, the crowd packed to the front, full red and white, no strobe.
74. *"Kicked the door off the quiet and I set it free"* — the crowd shouting every word back, shot from beside her at the mic.
75. *"Two years small, now the whole road knows"* — a wide from the very back of the room over every raised hand.
76. *"Red on the rim of the glass wherever it goes"* — the stranger from the toilets in the front row wearing the lipstick, singing, close-up.
77. *"You can hear me on the night bus, hear me in the rain"* — a cut outside: the queue and the wet street, bass still coming through the wall, static.
78. *"I'm not sorry for the space, I'm not going back again"* — back inside, her taking up the whole stage, arms wide, low angle.
79. *"Sing it with your chest till the ceiling agrees"* — light confetti of nothing but beams and steam over the crowd, wide.
80. *"Loud lipstick, louder me"* — the whole room and the stage landing together on the last word, held, locked off.

### Post-chorus 2 — handed to the room

81. *"Louder, louder, louder me"* — floor level stomp again, now with the front rows and the stage in the same frame.
82. *"Louder, louder, let the whole street see"* — she stops singing for two bars and just watches them do it, close on her face.
83. *"Red on the rim, red on the rim"* — the marked glasses again, this time being collected in a crate, still marked.
84. *"Louder, louder, let the night begin"* — hands up in a wave from the back of the room to the front, tracking.
85. *"Hands up if you've ever been told to calm down"* — individual faces, one per beat, all shouting the line, house lights half up.
86. *"Hands up, hands up, we are not calming down"* — the whole room with hands up, her at the side of the stage rather than the centre, wide, held.

### Outro — night bus

87. *"Ten past three, night bus, window steamed"* — the top deck of a night bus, empty except for her, a steamed window with the city smeared behind it.
88. *"Red on the cup and the chips on my knee"* — a paper cup with a red mark on the rim and a bag of chips balanced on her knee, macro, bus fluorescent.
89. *"Lipstick's gone, some girl has got it now"* — her checking an empty jacket pocket, finding nothing, and being entirely fine about it, close.
90. *"Louder me, and I'm keeping that somehow"* — she draws one short line in the steam with a finger and leaves it there, macro on the glass.
91. *"Loud lipstick, louder me"* — final shot: her face in profile against the steamed window, orange street light passing across it in bars, the stain of the red still on her mouth, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the lid click in the intro, the first crash, every *"louder
me"*, the lipstick changing hands in shot 38, the fire-door nod, the house
lights coming up for the bridge, the band slamming back in on *"the volume
is back"*, and the last steamed-window frame. At 130 BPM a bar is 1.85 s;
choruses cut on the bar, the stomp block cuts on the half-bar.

**The hands-up challenge.** The post-chorus is the shareable unit: post
shots 33–34 vertically with *"hands up if you've ever been told to calm
down"* on screen and invite people to film the two-line stomp-and-clap with
their own answer. **The hook frame** is shot 5 into shot 21 — the lid click
cut hard to the room jumping. **The caption card** is shot 69, the report
card. **The soft moment** is shot 38, the lipstick going into somebody
else's bag.

## 6. Quality-control checklist

- Three looks in the right sections: oatmeal and low tie only in flashbacks, leather and red for the whole night, jacket zipped and the lip worn to a stain on the bus
- The beige look and the night look must read as unmistakably the same face; that is the entire trick
- Red does not appear anywhere in the frame before shot 3, and never leaves after it
- The ex by the fire door has no face, no reverse angle and no reaction shot; there is no romantic lead in this video
- The lipstick is given away in shot 38 and never comes back; the stranger wears it in shot 76
- All lettering composited: the group chat, the cloakroom ticket, the report card
- Strobe appears at most twice and never in the last eight bars of a chorus; the bridge is lit by unflattering house light on purpose
- Crowd jumps and the stomp block are pose-referenced; no floating feet, no invented hands
- The final shot holds on the steamed window until the audio fades
