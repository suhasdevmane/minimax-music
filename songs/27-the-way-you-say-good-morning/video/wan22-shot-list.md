# Wan 2.2 Shot List — "The Way You Say Good Morning"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
92 BPM a bar is 2.61 s and this video cuts slowly — most shots run 4–7 s and
several hold longer.

## 1. Visual style

One bedroom, one morning, one window. The only clock in this video is the
light: it starts gray-blue at the top of the frame and climbs the wall stripe
by stripe until it is almost off the bed, and every section can be placed in
time by where the stripes are. Everything is motivated by that window — no
lamps, no practicals, no fill except a single bounce card. The camera moves
slowly or not at all. Skin texture, creased sheets, dust in the beams and
real shadow are the whole visual language; there is no diffusion and no glow.

**Sensual, never explicit.** Framing stays above the shoulder, or on hands,
sheets, light and texture. Nothing in this video would be cut by a platform.

| Section | Grade | Camera |
|---|---|---|
| Intro | Gray-blue warming to gold at the top of frame | Locked-off wide, static inserts |
| Verse 1 | Single hard window source, deep shadow | Extreme close-ups |
| Pre-choruses | Gold dominant, blue only in corners | Tight two-shot on one pillow |
| Chorus 1 | Full gold through blinds, dust in beams | Slow lateral dolly |
| Verse 2 | Fully warm, one empty room | Static, out-of-focus foregrounds |
| Chorus 2 | Gold and white, blown window highlights | Overhead, slow motion |
| Instrumental | Pure window light, no fill | Locked-off objects |
| Bridge | Cold gray flat inserts against the warm room | Static, evenly lit inserts |
| Final chorus | Fullest light of the video | Reverse lateral dolly, wider |
| Post-chorus | Dimming as the blinds close, warm-dark | Four tight cutaways |
| Outro | Warm stripes, soft shadow | Locked-off wide, then close |

## 2. Character bible — paste into every prompt

**Mahima** (the whole morning)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slept-in across the pillow, no makeup at all, wearing an oversized white cotton shirt, bare shoulders, warm relaxed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge inserts, the colder past)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled back tight, no makeup, wearing a plain gray sweatshirt and already fully dressed for work, exhausted flat expression, realistic cinematic photography, consistent identity

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, bare shoulders under a white sheet, eyes closed for almost the entire video, soft half-asleep expression, realistic cinematic photography, consistent identity

There are no exes, rivals or third characters in this video, and nobody
outside this apartment is ever seen. The flash-forward in the final chorus is
**two older hands only** — no faces, no attempt at aged versions of either
lead, because the model cannot hold identity across an age jump and the shot
does not need it.

Objects: the **blinds and the blind cord**, the **ceiling fan**, the **phone
face-up on the nightstand**, the **two mugs**, the **full mug going cold on
the kitchen counter**, **his shirt over the back of a chair**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The phone screen, the six stacked alarms in the bridge and any calendar or
notification are composited in the edit.** Generate the phone as a lit blank
rectangle on the nightstand and overlay the UI in post.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai in his single look with IP-Adapter or a
character LoRA each. Depth for the bedroom compositions so the bed geometry
and the light stripes stay consistent shot to shot. OpenPose is barely needed
here — there is almost no gross movement — but it is worth using on the two
shots where somebody reaches up to the blind cord.

**The hardest thing in this video is the light continuity.** Build the room
once as a set of stills at five light positions (opening blue, first gold,
mid-wall, high-wall, blinds closed) and generate every shot from the still
that matches its section. Animate small: breathing, the fan, dust drifting, a
hand arriving, sheets settling. Nothing needs to travel across the room.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–7 s; the instrumental object shots hold to 8 s.

## 4. Scene per lyric line

### Intro — ten to seven

1. *"Ten to seven and the room goes gray to gold"* — locked-off wide from the foot of the bed, the room still mostly blue, the top of the frame beginning to warm, held long.
2. *"Blinds laying stripes across the both of us."* — hard stripes of window light lying across a shoulder and a forearm on the bed, static, macro.
3. *"The fan is turning slow, your arm across my back"* — the ceiling fan turning slowly against a blue ceiling, then a tilt down to his arm across her back.
4. *"You say two words and I lose the whole day to that."* — her face on the pillow, eyes open, entirely still, the first gold arriving on one cheek, close-up.

### Verse 1 — his voice, her list

5. *"There's a strip of light across the ceiling and your jaw"* — one hard stripe running across the ceiling and continuing down across his jaw, static, wide-ish then push.
6. *"And your voice comes out like it's been dragged across a floor."* — extreme close-up of his mouth and beard, eyes closed, barely moving, the shot held on the sound.
7. *"You say it into my shoulder with your eyes still shut"* — his face against her shoulder, both in the stripe, neither looking at anything, tight.
8. *"Like the day is a rumor that you haven't heard about."* — her eyes in the half-dark, one slow blink, deep shadow either side of the light stripe.
9. *"I have got a whole list of things I meant to be"* — a phone on the nightstand out of focus with a long notes list on it (composited), her hand nowhere near it.
10. *"And not one of them is stronger than you saying it to me."* — back to her face, the amusement going out of it and something softer arriving, close-up, static.

### Pre-chorus 1 — say it again

11. *"So say it slow, say it into the pillow"* — both faces on one pillow framed tight, neither looking at the other, her eyes closed now too.
12. *"Say it before the room gets any older."* — the light on the wall visibly climbing one stripe, timelapse-slow, no people in frame.
13. *"Two words, no rush, don't clear your throat"* — her mouth close to his ear, speaking, barely moving, extreme close-up.
14. *"Say it like you mean the whole day that you wrote."* — his eyebrow moving without his eyes opening, the smallest possible performance, macro.

### Chorus 1 — the day loses

15. *"The way you say good morning makes me wanna stay in bed"* — slow lateral dolly along the length of the bed, sheets and light and two people passing the lens in one unbroken move.
16. *"Half a word, all gravel, and it goes right through my head."* — the dolly continuing, now on her face at the end of the move, gold across it.
17. *"You haven't opened both eyes and you've already won"* — his face, one eye opening halfway and closing again, close-up.
18. *"Say it one more time and the day can come undone."* — a hand pulling the blind cord and the stripes widening across the bed all at once, on the downbeat.
19. *"The way you say good morning, low and slow and rough"* — dust drifting through the widened beams over the bed, macro, backlit.
20. *"Sunday doesn't start until you say enough."* — both of them under the sheet from the side, laughing at nothing, medium.
21. *"Pull the blinds, let the light come down in lines"* — the blinds themselves filling the frame, gold pouring through them, static.
22. *"The way you say good morning makes the morning mine."* — a wide of the whole room fully lit for the first time, the bed in the middle of it.

### Verse 2 — the world pulls, and loses

23. *"There's a meeting at nine and a car that needs the shop"* — the phone face-up on the nightstand lighting and going dark (composited), the room out of focus behind it.
24. *"And a phone on the nightstand that has buzzed and will not stop."* — the same phone buzzing itself half an inch across the wood, macro, nobody reaching for it.
25. *"Your hand finds the small of my back like it knows the way"* — his hand arriving at the small of her back under the sheet, deliberate and slow, close, framed as texture.
26. *"And the outside world can take a number and wait."* — a car on the driveway with a flat tire seen through the window, badly out of focus, the window frame sharp.
27. *"Coffee went cold on the counter, that's twice this week"* — a full mug on a kitchen counter with nobody in the room, the only frame in the video without a person, static, held.
28. *"And I'd let it go cold again for the sound of you half asleep."* — back to the bed: her face, decision made, a small private smile, close-up.

### Pre-chorus 2 — awake this time

29. *"So say it slow, say it into the pillow"* — reuse shot 11's framing exactly; her eyes are open now and on him.
30. *"Say it before the room gets any older."* — the stripes now high on the wall, almost off the bed, no people.
31. *"Two words, no rush, don't clear your throat"* — her fingers on his jaw turning his face toward her, close.
32. *"Say it like you mean the whole day that you wrote."* — his eyes opening properly for the first time in the video, extreme close-up.

### Chorus 2 — wider

33. *"The way you say good morning makes me wanna stay in bed"* — overhead from directly above the bed, both on their backs, sheets and light making the whole composition.
34. *"Half a word, all gravel, and it goes right through my head."* — the overhead holding, one of them turning their head, the light stripes crossing both bodies.
35. *"You haven't opened both eyes and you've already won"* — slow motion of a sheet lifting and settling, ninety-six frames, no faces.
36. *"Say it one more time and the day can come undone."* — her laughing at something the audience does not hear, medium, real time.
37. *"The way you say good morning, low and slow and rough"* — his hand and her hand on the sheet, fingers overlapping, static macro.
38. *"Sunday doesn't start until you say enough."* — a wide with a lot of air in it, both awake, neither getting up.
39. *"Pull the blinds, let the light come down in lines"* — reuse shot 21, the light harder and whiter, highlights blown at the window.
40. *"The way you say good morning makes the morning mine."* — the room wide, both small in the middle of a very bright frame, held to the drop.

### Instrumental — the room, no talking

41. The ceiling fan alone against the ceiling, held eight seconds, the light on the wall behind it visibly moving.
42. Dust in the light beams over the bed, macro, backlit, nothing else in frame.
43. Two mugs on the nightstand, one full and one empty, and the phone dark beside them.
44. His shirt over the back of a chair with a stripe of light across it, static.
45. Her hand flat on the sheet and his fingers arriving on top of it, no faces, held to the end of the break.

### Bridge — who she was before

46. *"I used to hate the morning, set six alarms in a row"* — cold insert: an old phone screen with six alarms stacked on it (composited), flat gray light, lifeless.
47. *"Wake up already tired with nowhere good to go."* — cold insert: a bare mattress in a smaller, colder apartment, gray window, no warmth anywhere.
48. *"Then a Sunday in the spring and a voice in the dark"* — cold insert: Mahima (bridge look) sitting on the edge of that bed fully dressed at six in the morning, head down.
49. *"And the first thing in the world stopped being the worst part."* — hard cut back to the warm room: her awake in the dark, watching the window for the light to start.
50. *"Now I wake before the sun just to be early to you"* — her profile against a window with no light in it yet, only the shape of the blinds, close.
51. *"And I lie here in the quiet till you move."* — the first gold hitting the wall behind her as she waits, and his shoulder shifting in the foreground, static.

### Final chorus — the widest light

52. *"The way you say good morning makes me wanna stay in bed"* — the chorus-one lateral dolly repeated in the opposite direction, wider, the room at its brightest.
53. *"Half a word, all gravel, and it goes right through my head."* — the dolly ending on him this time, eyes open, saying it properly, close.
54. *"Forty years of mornings and I'd take every one"* — flash-forward: two older hands on the same sheet in the same light, no faces, two seconds.
55. *"If it starts with your voice and it ends with the sun."* — hard back to the present, her face, the flash-forward not explained, close-up.
56. *"The way you say good morning, low and slow and rough"* — both of them sitting up against the headboard for the first time, still not leaving, medium wide.
57. *"Sunday doesn't start until you say enough."* — the light stripes now at the very top of the wall, the whole room warm, static wide.
58. *"Pull the blinds, let the light come down in lines"* — a hand reaching up to the blind cord again, this time to close it, macro.
59. *"The way you say good morning makes the morning mine."* — the stripes narrowing as the blinds tilt, the room dimming warm, wide.

### Post-chorus — the two words

60. *"Good morning, good morning"* — tight cutaway one: his mouth, saying it, cut on the beat.
61. *"Say it low, say it slow, say it just to me."* — tight cutaway two: her eyes, closing on the last word.
62. *"Good morning, good morning"* — tight cutaway three: the fan, slower now that the room is dim.
63. *"And the rest of the day can be what it wants to be."* — tight cutaway four: the last stripe of light on the wall, thin and warm.

### Outro — the day cancelled

64. *"Blinds down, light in lines across the sheet"* — the locked-off wide that opened the video, identical framing, warm now instead of blue.
65. *"Your voice in the dark before the day begins."* — the same wide, both of them lying back down, the sheet moving once.
66. *"Don't get up yet, don't say anything else"* — her face turning into his shoulder, close, almost dark.
67. *"Just say it to me one more time."* — final shot: her eyes closing, one held breath on the soundtrack, the frame holding warm and still through the fade. No text.

## 5. Edit and the challenge

Markers at: the first gold on her cheek, each *"good morning"*, the blind cord
pull in shot 18, the empty kitchen counter, the first cold bridge insert, the
flash-forward, and the last breath. At 92 BPM a bar is 2.61 s; this edit
deliberately cuts slower than the music, often holding two bars per shot, so
that the four post-chorus cutaways landing on the beat feel like a change of
gear.

**The audio clip.** The post-chorus (shots 60–63) exists to be lifted as a
sound: two words over a bare snap groove, four cuts, four seconds. Post it
vertically with the blind-cord pull from shot 18 as the opening frame,
captioned *"you haven't opened both eyes and you've already won."* The second
shareable frame is the flash-forward at shot 54 — two older hands, two
seconds, no explanation.

## 6. Quality-control checklist

- The light climbs the wall in one direction only, section by section, until shot 58 closes the blinds; no shot's light position contradicts its place in the song
- Every frame is window-motivated: no lamps, no practicals, no fill beyond one bounce
- Framing stays above the shoulder or on hands, sheets and texture — nothing that a platform would cut
- Kai's eyes stay closed until shot 32 and are open from there on
- The bridge inserts (46–48) are the only cold, flat, evenly lit frames in the film
- The flash-forward is hands only; no aged faces are attempted anywhere
- Phone screen and the six alarms composited; no model-generated text
- The last shot is locked off and holds through the fade with the fan still turning
