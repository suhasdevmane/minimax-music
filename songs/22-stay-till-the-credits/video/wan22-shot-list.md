# Wan 2.2 Shot List — "Stay Till the Credits"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission, plus six shots for the instrumental. Timestamps come from the
rendered WAV; cut on the sung line. At 86 BPM a bar is 2.79 s; the verses
run two bars a line and the choruses hold single positions for four.

## 1. Visual style

Three grades, and the argument of the film is which one is beautiful.

The **exes** are shot like film moments: over-lit, over-saturated, staged,
shallow, obviously artificial. Poster light. They look like the trailer.

The **cinema** is grey credit light on two faces with everything else black,
then ugly fluorescent house light as the room comes up. Nothing about it
flatters anybody.

The **flat** is flat: overhead bulbs, a sink, brake lights through a
windscreen, an extractor light over a kitchen floor. No slow motion, no
score-swell in the picture, no golden hour anywhere in this video.

By the bridge the cinema light and the kitchen light have become the same
light, and the last frame is the plainest in the film. The camera is
locked off for every chorus and only moves when she does.

| Section | Grade | Camera |
|---|---|---|
| Intro | Grey credit light, house lights ugly at the edges | Slow wide from the front of the auditorium |
| Verse 1 (exes) | Over-saturated, poster-lit, artificial | Shallow, staged, cut off mid-frame |
| Verse 1 (the back row) | Grey screen light on two faces, black around | Static profiles |
| Pre-chorus | Saturated draining to plain inside the shot | One held move |
| Chorus | Full fluorescent house light, unflattering | Locked-off wide, rows emptying |
| Verse 2 | Flat domestic, overhead bulbs, nothing warm | Handheld, plain |
| Instrumental | Half house lights, dust in the projector beam | Long holds, one tilt |
| Bridge | A moving flashlight beam in a grey room | Static, low |
| Final chorus | Full house lights, the widest frame | Locked off, beside them |
| Post-chorus | Rising to full in four stages | Four cuts, same position |
| Outro | Screen dead, house light plain and clear | Wide, held to the fade |

## 2. Character bible — paste into every prompt

**Mahima** (the cinema, intro through the instrumental)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose over one shoulder, minimal makeup, wearing a dark green satin slip dress with a long camel coat folded across her knees, alert watchful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the flat, verse two)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair scraped into a knot, no makeup, wearing an oversized grey hoodie and pyjama shorts, exhausted unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge, final chorus and outro — the same night as the intro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, minimal makeup, wearing the dark green satin slip dress with the camel coat now over the back of the seat instead of on her knees, settled calm expression, realistic cinematic photography, consistent identity

**Kai** (the man who stays)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a plain navy jumper and dark jeans, no styling, unhurried attentive expression, realistic cinematic photography, consistent identity

Kai's face is lit only ever by whatever is already in the room — the credit
roll, the house lights, an extractor hood. He is never given a hero light.

**The exes** — faceless without exception. A hand pulling away in a taxi
window, a jaw and a shoulder in a poster-lit kiss cropped above the eyes, a
back walking out of a restaurant. Shot beautifully on purpose.
> a young man, face out of frame or cropped above the mouth, dark hair, sharp coat, cinematic over-lit styling

**The usher** — seen from behind or below, a bin bag and a broom and a
flashlight, never a face.

Objects that carry the story: the **camel coat** (on her knees in the intro,
across the seat by the final chorus), the **credit roll** seen only ever
obliquely or as light on a face, the **armrest** between two seats, the
**unclaimed scarf**, the **popcorn on the sloped floor**, the **projector
beam full of dust**, the **blank white screen**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The screen is never shown with legible content.** Every credit roll, poster
and phone screen is composited in the edit as an out-of-focus scroll of
unreadable name-shaped marks, or simply as coloured light thrown onto faces.
The film they are watching is deliberately never identified — no title, no
image, no genre. Generate the auditorium with the screen as a flat grey
luminous rectangle and add the roll in post.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai in his one look with IP-Adapter or a
character LoRA each; keep the ex reference deliberately faceless. Depth is
essential for the auditorium — the sloped floor, the rows and the seat backs
must be the same geometry in every one of the twenty-odd cinema shots, so
build one master plate and generate variations from it rather than
regenerating the room. OpenPose for the crowd standing and filing out.
16:9 throughout; 9:16 recomposition only for the chorus cut.

Animate small: a seat folding up, a coat sliding off a knee, a head turning,
a flashlight beam crossing a row, dust moving in a projector beam. The
emptying-rows chorus is built in the edit from three generated passes of the
same locked-off plate with different numbers of people in it, cross-dissolved
on the bar — do not ask the model to empty a room in one clip. The house
lights coming up in stages is a brightness ramp in the edit over a lit plate.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 5–6 s at this tempo; the chorus positions hold longer.

## 4. Scene per lyric line

### Intro — the room emptying

1. *"Everybody's leaving while the music's still playing,"* — a slow wide from the front of the auditorium looking back up the rows: silhouettes standing, seats folding, the credit light grey across every face.
2. *"Coats on, phones out, halfway up the aisle."* — the aisle at mid-height: coats going on over shoulders, phone screens lighting faces from below, a slow drift up toward the exit.
3. *"But you're still sitting there reading every name,"* — Kai in the back row in profile, lit only by the roll, his eyes moving steadily down the screen, close-up, everything else black.
4. *"Like the people who built it deserve a little while."* — Mahima half out of her seat with the camel coat already on her knees, hesitating, then sitting back down; the seat unfolding under her, medium.

### Verse 1 — the ones who left at the ending

5. *"I've had the kind of love that leaves at the ending,"* — over-lit and over-saturated: a hand pulling away from another hand in the window of a moving taxi, shallow, beautiful, cropped, poster light.
6. *"Kisses at the big scene, gone before the fade."* — a kiss staged exactly like a film poster, cropped above the mouths so neither face reads, rain machine light behind, artificial.
7. *"Loud in the trailer, quiet when it mattered,"* — a phone face-down on a restaurant table going dark, the chair opposite empty, the room still glossy and warm, close-up.
8. *"Every promise in the dark got quietly unmade."* — a back walking out through a doorway into white light, the door closing, the saturation dropping out of the frame as it shuts.
9. *"But you stay in your seat for the names nobody knows,"* — back to the real back row: Kai's face in credit light, absolutely still, close.
10. *"The caterers, the drivers, the second unit crew."* — the roll thrown as moving light across the seat backs in front of them, no legible marks, macro, the light sliding.
11. *"And I'm watching you watch it with my coat still on my knees,"* — her face turned toward him and not the screen, the camel coat folded across her knees with a sleeve trailing on the floor, medium, grey light.
12. *"Thinking, that's the kind of staying that I want from you."* — a two-shot from the row in front, both of them in profile, neither speaking, the whole thesis of the song landing in silence, static.

### Pre-chorus 1 — the good light

13. *"Because anyone can love me in the good light,"* — the poster-lit kiss from shot 6 again, held, the artificial light at its most flattering and most hollow.
14. *"Anyone can hold me when the strings swell high."* — the same frame with the light draining out of it inside the shot until only the plain cinema remains behind it.
15. *"I don't need the hero, I need the one"* — her in the back row, the coat still on her knees, looking straight ahead now, close-up.
16. *"Who's still in his seat when the story's done."* — his hands loose on the armrests, not reaching for a phone, not reaching for her, macro.

### Chorus 1 — the room empties around them

17. *"Stay till the credits, stay till the lights come on,"* — the locked-off wide from behind their shoulders down the length of the auditorium, the rows in front full.
18. *"Stay through the boring part after the ending's gone."* — the same locked-off frame, half the rows now empty, people still moving through it.
19. *"When the crowd walks out and the screen goes grey,"* — the same frame again, three or four people left, the roll ending, the screen going flat grey.
20. *"Be the one in the back row who doesn't walk away."* — the same frame, empty except the two of them, the house lights coming up one stage.
21. *"Stay till the credits, stay till the end of the song,"* — cut round to the front of the auditorium looking back: two people in a room of empty seats under half house light, wide.
22. *"Stay till the lights come on."* — the house lights coming up a second stage, the fluorescent tubes in the ceiling coves visible, unflattering and full, static.

### Verse 2 — three months in

23. *"Three months in, and it's not a movie anymore,"* — a sink full of dishes under an overhead bulb, the tap running on nothing, close, flat.
24. *"It's the dishes and the traffic and my mother on the phone."* — brake lights through a rain-streaked windscreen, wipers, no music in the picture, static from the driver's seat.
25. *"It's me at my worst on a Tuesday in the kitchen,"* — Mahima in the hoodie on the phone to her mother with one hand over her eyes, standing in a kitchen at four in the afternoon, overhead light on, handheld.
26. *"It's the version of me that the trailer never showed."* — her crying without drama, wiping her face with a sleeve and going back to the sink, medium, absolutely plain.
27. *"And you're still here, reading all of my small print,"* — Kai drying the dishes she left, not talking, not making a point of it, close on the hands and the cloth.
28. *"The flaws in the footnotes, the parts I'd cut if I could."* — him in the passenger seat in the traffic, looking out of the window, comfortable in the silence, profile.
29. *"You don't need the montage, you don't need the ending,"* — him sitting on the kitchen floor with his back against a cupboard, opposite her, wide, the extractor light the only light on.
30. *"You just want to sit here, and I never understood."* — the two of them on the floor, a metre apart, neither reaching, held, the same framing as the two-shot in shot 12.

### Pre-chorus 2 — the kitchen floor

31. *"Because anyone can love me in the good light,"* — a slow push in on the two of them on the kitchen floor, the room dark except the extractor.
32. *"Anyone can hold me when the strings swell high."* — the push continuing, her face coming into the light, close.
33. *"I don't need the hero, I need the one"* — his hands on the floor between them, palms up, not doing anything, macro.
34. *"Who's still in his seat when the story's done."* — the two of them from the doorway, small, on the floor of a dark kitchen, wide, static.

### Chorus 2 — the two rooms become one

35. *"Stay till the credits, stay till the lights come on,"* — hard cut pair: the locked-off auditorium wide, then the kitchen floor from the same relative height and distance.
36. *"Stay through the boring part after the ending's gone."* — the emptying rows again; cut to the sink, the drying rack, the same slow nothing.
37. *"When the crowd walks out and the screen goes grey,"* — the grey screen; cut to a dark television in the flat reflecting the room, matched rectangles.
38. *"Be the one in the back row who doesn't walk away."* — two seats in the back row; cut to two people on a kitchen floor, the identical gap between them.
39. *"Stay till the credits, stay till the end of the song,"* — the auditorium from the front, half lit; cut to the kitchen from the doorway, half lit, matched.
40. *"Stay till the lights come on."* — the house lights up another stage in the cinema, and the kitchen strip light flicking on in the flat, one cut, the two rooms now the same colour.

### Instrumental — the room being closed

41. An usher moving down a row with a bin bag, seen from behind and below, no face, half house lights.
42. A single unclaimed scarf left over the back of a seat, still, close-up.
43. The projector beam full of dust, seen from below at the back of the room, the only beautiful shot in the film and it is made of dirt.
44. Popcorn on the sloped floor, kicked by a passing shoe and rolling down toward the front, macro, tracking.
45. The two of them small in a wide empty frame in the back row, nobody else in the room, static, held long.
46. A slow tilt up from the empty seats to the screen: grey, blank, still lit — the cut into the bridge.

### Bridge — the flashlight, then the definition changes

47. *"The usher's got his flashlight out, the popcorn's getting swept,"* — a flashlight beam sweeping along a row of seats and passing over their feet, low and static, the only moving light in the frame.
48. *"The screen's just a rectangle of light."* — the screen straight on: a flat grey luminous rectangle with nothing on it, held four seconds, static.
49. *"I used to think that love was the part with the music,"* — two seconds of the over-lit poster kiss from shot 6, cut hard against the grey.
50. *"The kiss before the black, the walk into the night."* — the ex's back walking out through the white doorway again, then a hard cut back to the empty auditorium, the artificial world used for the last time.
51. *"Now I think it's who's still there when there's nothing left to watch,"* — the two of them from behind, silhouetted against the blank screen, neither moving, wide.
52. *"Who's holding my hand when the story lets go."* — their hands on the armrest between the seats, hers going over his, macro. **The frame that lands.**
53. *"So if this is the after, if this is the rest of it,"* — both of them looking at a blank screen, side on, faces lit by nothing but its grey, medium.
54. *"Then I don't want the movie, I want the after show."* — her turning to look at him and staying turned, close-up, the warmest frame in the video and it is only house light.

### Final chorus — she stops asking

55. *"Stay till the credits, stay till the lights come on,"* — the locked-off wide, but from beside them in the row now rather than behind, the whole auditorium empty in front of them.
56. *"Stay through the boring part, that's where I belong."* — her settling back into the seat and folding the camel coat over the seat back instead of her knees, close-up. **The change.**
57. *"When the crowd walks out and the screen goes grey,"* — the last person in the room passing across the frame and out of it, leaving the two of them, medium wide.
58. *"I'll be the one in the back row who doesn't walk away."* — her face, straight to camera for the only time in the video, full house light, no flattery, close-up.
59. *"Stay till the credits, stay till the end of the song,"* — the widest frame of the film: the two of them from the front of the auditorium, tiny, the room fully lit.
60. *"Stay till the lights come on."* — the house lights reaching full, the whole ceiling of tubes on, the frame at its brightest and plainest, static.

### Post-chorus — the lights in stages

61. *"And the lights come on, and the lights come on,"* — the same two seats, the same two people, one stop brighter.
62. *"And we don't get up, we don't get up."* — the same frame, another stop brighter, neither of them moving.
63. *"And the lights come on, and the lights come on,"* — the same frame, brighter again, every seat in the room visible now.
64. *"And we don't get up, we don't get up."* — the same frame at full house light, everything ordinary and clear, held.

### Outro — the empty room

65. *"Everybody's gone now, the music's still playing,"* — a wide of the auditorium with nobody in it but them, the exit doors propped open on a dark lobby.
66. *"The last name rolls up and the screen goes white."* — the last mark of the roll clearing the top of the frame, then the screen going white and then dead, straight on.
67. *"You turn to me in the empty room and ask me what I thought,"* — Kai turning to her and speaking, unheard, his face plain and warm, close-up.
68. *"And I say, I think I'll stay."* — her face, the smallest real smile, answering a question about the film that neither of them thinks is about the film, close-up.
69. *"I think I'll stay."* — final shot: the two of them from the front of the auditorium, tiny in a wide fully lit empty room, neither of them moving. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the sit-back-down in shot 4, each
*"stay till the credits"*, the last empty row in shot 20, the kitchen floor
in shot 29, the instrumental, the blank screen in shot 48, the hands on the
armrest in shot 52, the coat moving in shot 56, and the last wide. At 86 BPM
a bar is 2.79 s; the chorus positions hold four bars each, which is why the
emptying happens inside the shot rather than between cuts.

**The credits challenge.** The shareable cut is shots 17–22 — the locked-off
wide with the rows emptying across the chorus — vertical, with *"Stay till
the credits, stay till the lights come on"* on screen. Invite people to film
the credits at their next cinema trip and tag whoever stayed with them. The
second shareable frame is shot 52, the hands on the armrest, posted alone.
**The caption line:** *"Anyone can love me in the good light."*

## 6. Quality-control checklist

- Three looks in the right sections: the slip dress and camel coat in the cinema, the hoodie only in verse two and the second pre-chorus, and the coat moves from her knees to the seat back at shot 56 and never moves back
- The exes never have faces and are always the most beautifully lit thing on screen; the cinema and the flat are never flattering
- The screen is never legible — no title, no image, no readable credit roll, in any frame, at any speed
- One auditorium plate: the sloped floor, the row spacing and the seat backs are identical geometry across all twenty-two cinema shots
- The house lights go up in stages and never go back down; shots 60 and 64 are the brightest frames in the film and shot 69 holds that level
- The matched pairs land: shot 12 with shot 30, and the chorus-two cuts in shots 35 to 40
- No slow motion anywhere, no golden hour anywhere, no score-swell in the picture
- The last shot is locked-off, wide, fully lit, with neither person moving, and holds until the piano stops
