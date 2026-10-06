# Wan 2.2 Shot List — "Sugar on My Tongue"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Uptempo: at 118 BPM a bar is 2.03 s, so most shots are 2–4 s
and the choruses cut on every bar or half-bar. Timestamps come from the
rendered WAV; cut on the sung line.

## 1. Visual style

A candy-coloured American-style diner after hours, chrome and chequered
floor, pink and teal neon, one lit jukebox. **The cherry is the motif** — on
the counter in the intro, held out and pulled back in every chorus, finally
placed in his hand in the last chorus, alone on the counter at the end. The
game is hers: she leads every frame, he reacts. Playful, saturated, PG-13;
the kiss is seen once, wide, from across the lot.

| Section | Grade | Camera |
|---|---|---|
| Intro / outro | Pink and teal neon, warm counter tungsten, dim room | Static, mirror shots |
| Verses (booth) | Warm booth lamp, neon rim light | Close, over-the-shoulder, handheld |
| Pre-choruses | Neon flicker on the count | Push-ins |
| Choruses | Full neon, pink and teal strobe on the beat, chrome glare | Tracking, whip pans, on the beat |
| Post-choruses | Strobing, four fast inserts | Ultra-fast cuts |
| Instrumental | Most saturated section, slow-mo and impact cuts | Slider along the counter |
| Bridge (parking lot) | Pink sign, then sodium orange, cold breath | Static two-shots |
| Final chorus | Brightest pink of the video, whole lot lit | Wide, moving, a spin |

## 2. Character bible — paste into every prompt

**Mahima** (diner look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a red ribbon tied at the crown, glossy cherry-red lips and winged liner, wearing a fitted red knit top and a high-waisted black skirt with red heels, teasing confident expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (parking lot / outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a red ribbon, glossy cherry-red lips, wearing the red knit top under his oversized dark jacket, heels carried in one hand, satisfied soft expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the boy)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a dark denim jacket with the collar turned up over a white t-shirt, slightly flustered charming expression, realistic cinematic photography, consistent identity

**The waitress and the cook** — supporting comic pair, seen at the counter and the kitchen pass. Waitress: a woman in her forties in a pink diner uniform and apron, deadpan. Cook: a large man in a white t-shirt and paper hat, seen mostly from the pass. They never pull focus.

Objects: the **maraschino cherry** (single, on a stem), the **milkshake** with two straws, the **napkin** (its writing composited as a blur), the **jukebox**, the **open/closed sign**, the diner's **pink neon sign** outside.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All signs, the napkin's writing, the jukebox display, the clock face and
the waitress's phone screen are composited in the edit.** Generate the
diner sign as a glowing abstract shape and the napkin as blank; overlay
anything that must read as text in post — the model cannot render legible
UI or lettering.

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

Most shots 3–5 s. For this song: OpenPose on every dance shot and the spin;
Depth for the long counter compositions; the cherry hand-offs need a hand
reference or the fingers drift. Kai's identity locked with his own LoRA.

## 4. Scene per lyric line

### Intro — after hours, the door chime

1. *"Cherry on the counter, neon in the glass"* — macro of a single maraschino cherry on the chrome counter, pink neon reflected in a tall glass beside it, static.
2. *"Jukebox humming something slow and I'm not gonna ask"* — Mahima (diner look) alone at the counter, twirling the cherry stem, the lit jukebox glowing behind her, the waitress wiping down far off, medium, static.
3. *"You walked in like Friday with your collar turned up"* — the door chime: Kai stepping in with his collar up, shaking off the cold, seen in the mirror behind the counter over Mahima's shoulder, she does not turn.
4. *"Sit down, honey, I'm about to fill your cup"* — her hand tapping the stool beside her without looking, then her slow smile at the mirror, close-up.

### Verse 1 — the booth, the milkshake

5. *"I got a booth in the corner and a straw with your name"* — the corner booth, a milkshake with two straws, Mahima sliding one straw toward him across the table, over-the-shoulder, booth lamp warm.
6. *"Vanilla on my lips and you're looking the same"* — close-up of her taking a sip, cherry-red lips on the straw, eyes on him, neon rim light in her hair.
7. *"You're talking about traffic like it's something I need"* — Kai talking, hands moving, animated about nothing, medium, handheld.
8. *"I'm watching your mouth and I'm not listening, believe me"* — her face, chin on her hand, nodding along with zero attention, eyes fixed on his mouth, close-up.
9. *"Milkshake sweating on the table between us"* — macro of condensation running down the glass, two straws, two spoons, the booth lamp in the drops.
10. *"Two spoons and one glass and the whole diner sees us"* — the waitress and the cook at the pass, glancing over, unimpressed and amused, then back to work, wide from the booth.
11. *"You said you don't do dessert, that's a lie and you know it"* — Kai shaking his head no at the offered spoon, and his eyes flicking down to the cherry, close-up on the eye-flick.
12. *"Cause you keep sneaking looks at the cherry, don't blow it"* — her catching it, one eyebrow up, a slow grin, extreme close-up.
13. *"Pink light on the chrome, the cook's playing our song"* — the jukebox lights changing as a new song starts, pink on the chrome edges of the booth, the cook nodding at the pass, medium wide.
14. *"And I'm stirring the whipped cream real slow, real long"* — her spoon stirring the whipped cream slowly, holding his eyes over it, over-the-shoulder from behind him.

### Pre-chorus 1 — the count

15. *"Don't act like you're bitter, don't act like you're cool"* — Kai leaning back trying to look cool, arm along the booth, Mahima leaning in, two-shot.
16. *"I can see the sugar high all over you"* — his face, a flush rising, close-up, the neon flickering once.
17. *"Lean in a little, the waitress won't mind"* — behind them, the waitress flipping the door sign from open to closed (sign composited) and rolling her eyes, rack focus from the booth.
18. *"I'll count to three, honey, and you'll cross that line"* — her fingers on the table, one, two, close-up on the hand, the neon buzzing.
19. *"One, two, and I'm looking at you"* — she stops at two and just looks at him, the band drops out, a held close-up on her eyes, then a hard cut on the drop.

### Chorus 1 — sugar rush on the chequered floor

20. *"You're like sugar on my tongue"* — the drop: Mahima out of the booth and onto the chequered floor, milkshake in hand, the jukebox lights strobing, wide, whip pan.
21. *"And I've got a sweet tooth tonight"* — her dancing between the chrome stools, a kiss blown at camera on the kiss-sound hit, tracking.
22. *"One taste and I'm gone, one look and you're done"* — two cuts on the beat: her lips on the straw; Kai in the booth, done for, staring.
23. *"Come here, honey, take a bite"* — her curling a finger at him from the floor, pink and teal strobe, medium.
24. *"You're like sugar on my tongue"* — her sliding along the counter on a stool, heels up, the chrome catching the neon, slider.
25. *"Sweeter than the syrup on the side"* — a syrup bottle on the counter squeezed onto a plate on the beat, macro, then her grin.
26. *"But sugar, you gotta earn it, come on, learn it"* — the cherry held up between two fingers toward Kai and pulled away at the last second, close-up, slow motion.
27. *"I don't give it away, I decide"* — her pointing at herself with the cherry hand, chin up, straight to camera, medium close-up.
28. *"Sugar, sugar, sugar on my tongue"* — the cook and the waitress bobbing at the counter despite themselves, the cook with a spatula, wide.
29. *"Sugar, sugar, sweet tooth tonight"* — Mahima spinning once on the floor, skirt flaring, neon strobing, wide.

### Post-chorus 1 — the chant

30. *"Sweet tooth, sweet tooth, honey, don't rush"* — her lips on the words, extreme close-up, then a flat palm toward Kai: slow down.
31. *"Sweet tooth, sweet tooth, I can see you blush"* — Kai's cheeks actually red, close-up, the booth lamp.
32. *"Sweet tooth, sweet tooth, sugar on my tongue"* — the cherry stem tied in a knot and shown on the tip of her tongue to camera, macro.
33. *"Sweet tooth, sweet tooth, and the night is young"* — the diner clock on the wall (face composited), then a whip pan back to the booth.

### Verse 2 — closer, the napkin, the closing sign

34. *"Now you're sliding in closer, your knee against mine"* — the booth, Kai on her side now, under the table his knee touching hers, low angle, warm.
35. *"Stealing fries off my plate like a crime, that's fine"* — his hand sneaking a fry off her plate, her hand slapping it, then letting him, close-up on the hands.
36. *"You wrote your number on a napkin, drew a heart on the end"* — a napkin slid across the table toward her (writing composited as a soft blur), his pen still in hand, over-the-shoulder.
37. *"I folded it twice, said, we'll see, my friend"* — her folding the napkin twice and tucking it into the pocket of her top with a shrug, close-up, a half smile.
38. *"The clock on the wall says the kitchen's closing"* — the cook killing the kitchen lights one bank at a time behind the pass, the diner shrinking toward the booth, wide.
39. *"The cook flips the sign but I'm still dosing"* — the cook flipping a second sign in the kitchen window (composited), Mahima not moving, sipping, medium.
40. *"You're sweet like the frosting, but I want the cake"* — a slice of layered cake on a plate between them, her fork taking the tip, then her eyes on him, close.
41. *"So show me you're patient for goodness sake"* — Kai with his hands folded on the table like a schoolboy, waiting, her nodding approval, two-shot.
42. *"Wipe that cream off your lip, no, let me do it"* — a dab of cream on his lip, his hand going to wipe it, her catching his wrist and wiping it with her thumb, slowly, extreme close-up.
43. *"See, that's the kind of slow that I'm into"* — his face, forgetting how to breathe; her smallest nod, as if ticking a box, close-up on each.

### Pre-chorus 2 — the jukebox

44. *"Don't act like you're bitter, don't act like you're cool"* — Mahima taking his hand and pulling him out of the booth toward the jukebox, tracking from behind.
45. *"I can see the sugar high all over you"* — the jukebox glow on both faces, his eyes on her, not the machine, close two-shot.
46. *"Lean in a little, the jukebox won't mind"* — her finger pressing a jukebox button (display composited), the lights inside racing, macro.
47. *"I'll count to three, honey, and you'll cross that line"* — her two fingers counting on his chest, one, two, close-up.
48. *"One, two, and I'm looking at you"* — she stops at two, looks up at him, silence, then the bass drop sweeps and the frame whips away.

### Chorus 2 — the whole diner is theirs

49. *"You're like sugar on my tongue"* — both of them dancing on the chequered floor now, the diner empty and completely theirs, wide, moving.
50. *"And I've got a sweet tooth tonight"* — a spin: her spinning under his arm, skirt flaring, the jukebox strobing, tracking.
51. *"One taste and I'm gone, one look and you're done"* — reuse shot 22, tighter, both now on the floor.
52. *"Come here, honey, take a bite"* — the cherry passed from her fingers toward his mouth and pulled back at the last second, slow motion, close.
53. *"You're like sugar on my tongue"* — the waitress at the counter filming them on her phone (screen composited), deadpan, then a tiny smile, medium.
54. *"Sweeter than the syrup on the side"* — reuse shot 25, the syrup on a stack of pancakes on the pass.
55. *"But sugar, you gotta earn it, come on, learn it"* — him reaching for the cherry, her holding it above her head, him not reaching further, a laugh, medium.
56. *"I don't give it away, I decide"* — her to camera again, cherry in hand, this time with him blurred behind her, medium close-up.
57. *"Sugar, sugar, sugar on my tongue"* — the two of them back-to-back on the floor, arms folded, mock-cool, then breaking into laughter, wide.
58. *"Sugar, sugar, sweet tooth tonight"* — her red heels on the chequered floor cut on the beat, low angle, strobe.

### Instrumental — the dance break

59. A slow-motion slider pass along the chrome counter, Mahima sliding stool to stool with the milkshake, neon streaking.
60. Kiss-sound hits matched to blown kisses at camera, four in a row, each a different angle, on the beat.
61. The jukebox lights racing, extreme close-up, then a whip to her heels on the floor.
62. The cook and the waitress finally dancing behind the counter, the cook with the spatula, the waitress deadpan but moving, wide.
63. Mahima's clap build to camera, hands filling the frame, then a hard cut to black on the silence.

### Bridge — the parking lot, the verdict

64. *"Okay, okay, you passed the test"* — the parking lot outside, the pink diner sign buzzing (an abstract glowing shape, no text), Mahima (parking-lot look) leaning on Kai's car, mock-serious, wide static.
65. *"You held the door, you didn't rush, you did your best"* — a quick flashback insert: Kai holding the diner door for her earlier, then back to her counting one finger, close-up.
66. *"You let me have the cherry, let me have the last sip"* — insert: Kai pushing the last of the milkshake across to her; then two fingers counted.
67. *"You laughed at my jokes and you didn't get slick"* — insert: Kai laughing with his whole face at something she said in the booth; then three fingers, her nod.
68. *"The parking lot's empty and the sign's turning off"* — the diner sign flicking off, the lot dropping to one sodium lamp, breath in the cold air, wide.
69. *"The last song is playing and I'm done playing tough"* — the jukebox's last song faint through the glass, her face softening for the first time, close-up, orange lamp.
70. *"Come here, sugar, and I'll say it slow"* — her curling one finger: come here, and Kai crossing the lot, tracking from behind him.
71. *"You earned it, so now you get to know"* — her hand on his collar, pulling him in, the frame cutting away just before the kiss, extreme close-up on the hand.

### Final chorus — the lift, the lot lit pink

72. *"You're like sugar on my tongue"* — the diner sign blazing back on behind them on the lift, the whole lot going pink, wide from across the lot.
73. *"And I've got a sweet tooth tonight"* — the two of them dancing in the empty lot, her heels off and in her hand, tracking.
74. *"One taste and I'm gone, one look and you're done"* — her spinning under his arm in the lot, his jacket on her shoulders flaring, slow motion.
75. *"Come here, honey, take a bite"* — the cherry finally placed in his open palm, close-up on the hands, held.
76. *"You're like sugar on my tongue"* — the kiss, seen once, wide from across the lot, the two of them small in a pink frame, static.
77. *"Sweeter than the syrup on the side"* — the waitress locking the diner door behind the glass and pretending not to watch, a smile she can't hide, medium.
78. *"And sugar, you earned it, look at you, you learned it"* — Kai holding up the cherry like a trophy, grinning, her rolling her eyes and laughing, two-shot.
79. *"Now I'm giving it away, I decide"* — her to camera one last time, no cherry in hand now, a shrug and a smile, medium close-up.
80. *"Sugar, sugar, sugar on my tongue"* — both of them on the bonnet of his car under the pink sign, feet swinging, the milkshake glass between them, wide.
81. *"Sugar, sugar, sweet tooth tonight"* — her head on his shoulder, the sign buzzing, a slow push-in.

### Post-chorus 2 — chant in the lot

82. *"Sweet tooth, sweet tooth, honey, don't rush"* — her lips, pink light, extreme close-up.
83. *"Sweet tooth, sweet tooth, I can see you blush"* — Kai's blush again, sodium and pink, close-up.
84. *"Sweet tooth, sweet tooth, sugar on my tongue"* — the knotted cherry stem in her open palm, macro.
85. *"Sweet tooth, sweet tooth, and the night is young"* — the diner clock through the window reading late (composited), the lot behind it.

### Outro — the cherry on the counter

86. *"Cherry on the counter, neon going dim"* — back inside, the mirror of shot 1: a cherry on the counter, the neon starting to dim, macro, static.
87. *"Jukebox playing our song now, and I'm walking out with him"* — through the diner window, the two of them walking away across the lot hand in hand, her heels in her other hand, wide.
88. *"He's got my number and I've got his hand"* — their hands, his thumb over the folded napkin in her fingers, close-up, tracking beside them.
89. *"Sweetest thing I ever ordered, and I didn't even plan"* — her glancing back at the diner once, a small satisfied smile, then forward, medium.
90. *"Sugar on my tongue, honey, sugar on my tongue"* — the jukebox lights cycling down inside the empty diner, the last song ending, wide.
91. *"Sweet tooth tonight, and the night is young"* — final shot: the cherry alone on the counter, the neon buzzing down to one warm bulb, then dark, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the door chime, each "one, two" count and its drop, each "you
gotta earn it", the kiss-sound hits, the instrumental, "you passed the
test", the sign flicking off, the lift into the final chorus, and the last
neon buzz. At 118 BPM a bar is 2.03 s; choruses cut on the bar, the
post-chorus chant on the half-bar.

**Count-to-three challenge.** The pre-chorus ending is a built-in
transition: *"one, two, and I'm looking at you"* into the drop. Post the
vertical cut of shots 15–23 with the hook on screen and invite people to
count on their fingers, hold on two, and cut to their own reveal on the
drop — an outfit, a partner, a dessert. The cherry pull-away (shot 26) is
the second shareable frame; the thumb on his lip (shot 42) is the third.

## 6. Quality-control checklist

- Two looks in the right places: the diner look inside until the instrumental; his jacket over her shoulders from the bridge on; heels in hand from the final chorus on
- Kai's identity locked in every shot; the waitress and cook never pull focus
- The cherry is in every chorus and is only placed in his hand once, in shot 75
- The kiss is seen once, wide, in shot 76; the bridge cuts away before it
- All signs, the napkin's writing, the jukebox display, the clock and the waitress's phone are composited; no model-generated text
- Kiss-sound hits land on a blown kiss or a lip close-up every time
- No distorted hands on the cherry hand-offs, the thumb wipe or the napkin
- The last shot is locked-off and holds until the audio fades
