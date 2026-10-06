# Wan 2.2 Shot List — "Dating Myself"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
94 BPM a bar is 2.55 s, so most shots run 3–5 s and the choruses cut on the
snap.

## 1. Visual style

Shoot a solo date exactly the way a romance is shot. Every grammar cue of a
love scene is used honestly and only one person is in the frame: the
across-the-table two-shot, the reverse angle, the candle between them, the
slow push on a face reacting to something the other person said. **The
reverse angle is on an empty, beautifully lit chair**, and the video never
winks at it. Warm, low, film-grain, shallow focus. Interiors carry the whole
piece; the only exteriors are the walk over, one rainy street and the walk
home.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cool blue street into warm pooled window light | Slow handheld, following |
| Verse 1 | Candle-warm booth, deep shadow, shallow focus | Static across-the-table setups |
| Pre-choruses | Memory flat grey-blue, present warm and low | Hard cut between two locked frames |
| Choruses | Golden, soft, romantic-comedy warm | Classic coverage, gentle push-ins |
| Verse 2 | Overcast daylight, then screen light | Handheld outside, static inside |
| Instrumental | Wet street, neon reflections, one shop window | Slow tracking and one long wide |
| Bridge | One lamp, deep shadow, deliberately unromantic | Static, wider than comfortable |
| Final chorus / post-chorus | Widest and warmest in the video | Full coverage, fast rhythmic cuts |
| Outro | Night street into one warm lamp | Slow, calm, holding |

## 2. Character bible — paste into every prompt

**Mahima** (the date — intro, verse 1, all choruses, post-chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and glossy with a side part, warm evening makeup with a soft brown lip, gold drop earrings, wearing a deep green satin slip dress with thin straps, relaxed amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (daytime — verse 2, pre-chorus two, instrumental)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely, no makeup, wearing a cream knit jumper and wide dark trousers with a long camel coat, calm open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the memory flash in pre-chorus one, cooler and younger)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark hair flat and unstyled, no makeup, wearing a work shirt and a coat still on indoors, tired closed expression, realistic cinematic photography, consistent identity, natural skin texture

**The waiter** — a warm, ordinary presence, face fine, seen four times: the
menu, the olives, the dessert, the two desserts. Same person every time. He
is on her side and never patronising.

**The man in the lobby** (verse 2) — faceless. Shot from behind his shoulder
or cropped at the chin.
> a young man in his twenties, back to camera or face out of frame, dark overcoat, holding a folded cinema ticket

**No ex appears in this video at all.** There is no antagonist. The only
opposition is the woman in the pre-chorus memory, and she is the same person.

Objects that must stay continuous: the **gold drop earrings**, the **single
candle** (burning lower across the night), the **corner booth**, the **small
glass of red**, the **phone face-down in the bag**, the **peonies wrapped in
paper**, the **record sleeve**, the **lamp left on**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the booking confirmation, the menu, the receipt, the cinema
listings and the record label are composited in the edit.** Generate menus
and phones as blank lit surfaces and overlay in post — the model cannot
render legible text, and a misspelled menu will pull a viewer straight out of
an otherwise beautiful frame.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
lobby man's reference deliberately faceless. Keyframes first; Depth for the
booth and the cinema interiors, which the model flattens badly in low light;
OpenPose only for the walking shots. 16:9 first; 9:16 for the chorus and
post-chorus cuts, which are the shareable ones. Animate conservatively:
candle flicker, wine tilting in a glass, a spoon going down, hair moving as
she turns, rain on a window. Avoid animating the waiter's hands near plates —
generate the plate landed rather than being placed.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s. The empty-chair reverse angles must be generated from the
same plate as the matching across-the-table shot so the booth, candle height
and background extras line up exactly.

## 4. Scene per lyric line

### Intro — the booking and the walk

1. *"Made the reservation under my own name"* — extreme close-up of her thumb on a phone, a booking screen composited, one tap, warm bathroom light off frame.
2. *"Table for one, and the host didn't blink"* — a host stand, her mouthing two words, the host nodding and picking up exactly one menu, medium, warm pooled light.
3. *"Gold earrings out for an ordinary Tuesday"* — a bathroom mirror, gold drop earrings going in one at a time, her watching herself do it, close-up.
4. *"Walked the long way over just to think"* — Mahima (date look) walking a long blue evening block, coat open, hands in pockets, tracking from the front.
5. *"Nobody's evening to carry but my own"* — she takes a corner she did not need to take, slowing rather than hurrying, wide from across the street.
6. *"Nobody waiting on me at the door"* — the restaurant door from outside, warm light spilling, her reflection arriving in the glass, static.

### Verse 1 — the meal

7. *"Ordered the one thing I'd never get for two"* — a menu (blank, composited) closing decisively in her hands, the waiter's pencil moving, close-up.
8. *"Olives on the side and a small glass of red"* — a small plate of olives landing and a glass of red poured, the candle behind the glass, macro.
9. *"Waiter came around and asked me if I was waiting"* — the waiter's open hand gesturing at the empty seat opposite, over her shoulder, shallow focus.
10. *"I said, no, I'm all here, go ahead"* — her shaking her head once with a small smile and moving her glass to the centre, close-up.
11. *"Phone in my bag with the screen facing down"* — the phone sliding face-down into a bag on the seat beside her, the screen light dying, close-up.
12. *"No proof required and no one to impress"* — a slow pan of the restaurant in shallow focus: a couple arguing softly, a birthday candle, a waiter with four plates.
13. *"Watched the whole room like the opening of a movie"* — her face watching all of it with unhurried open attention, slow push-in, candle light.
14. *"And I liked the girl who came in that dress"* — her reflection in the dark window over the booth, holding her own eye contact, close-up, the first hook beat.

### Pre-chorus 1 — then and now

15. *"Used to think a Friday on my own was a loss"* — two seconds, cool flat grade: Mahima (memory look) eating standing up over a sink with the TV on and her coat still on, static.
16. *"Something you survive, something you hide"* — the memory continuing, her closing a curtain in daylight, then a hard cut to black.
17. *"Now I light the candle and I take my time"* — back in the booth: her hand cupping the candle flame, warm, macro, the temperature jump is the point.
18. *"And I don't leave until I decide"* — her settling back into the booth, one arm along the top of the bench, taking up the whole seat, medium.

### Chorus 1 — the date, shot like a romance

19. *"I'm dating myself, and honestly it's going great"* — the classic across-the-table two-shot framing, her in the near seat, warm gold, gentle push-in.
20. *"She shows up on time and she never makes me wait"* — **the reverse angle: an empty, beautifully lit chair**, candle in the foreground, coverage identical to shot 19. **The hook frame.**
21. *"Reservation for one, and I said it out loud"* — her saying something and laughing at her own answer, alone, entirely natural, close-up.
22. *"Corner booth, candle lit, and I'm proud"* — a wide of the booth from across the restaurant, one person in a pool of gold, everyone else out of focus.
23. *"I'm dating myself, no notes and no complaints"* — her tipping her glass at nothing in particular and drinking, medium.
24. *"Nobody's bad mood that I have to translate"* — the couple at the next table mid-tension in shallow focus behind her calm face, single frame, no cut.
25. *"Ordered the dessert and I finished the plate"* — dessert landing with one spoon, the waiter grinning, close-up.
26. *"I'm dating myself, and honestly it's going great"* — the spoon going down on a clean plate, her leaning back satisfied, macro then medium.

### Verse 2 — flowers, a matinee, a polite no

27. *"Peonies on a Wednesday, no occasion"* — Mahima (daytime look) pointing at peonies through a florist's window, overcast daylight, medium.
28. *"Paid the full price and I carried them home"* — paper being wrapped and taped around the stems, hands only, macro.
29. *"Put them where the sofa sees them in the morning"* — her setting the flowers on a low table opposite the sofa, wide, warm lamp.
30. *"Not the hall where they'd be blooming for someone unknown"* — she moves the vase two inches so it lines up with where she actually sits, then checks from the sofa, close-up. **The two-inch adjustment is the shot.**
31. *"Matinee at four, back row, lights low"* — a wide of an almost-empty cinema auditorium with one person in the back row, screen light only.
32. *"Both of the armrests mine and I cried at the end"* — both her elbows spreading onto both armrests, then her face lit by the screen, tears she does not wipe, close-up.
33. *"Somebody kind asked me out in the lobby"* — a flat-lit lobby, a faceless man in an overcoat saying something warm, shot from behind his shoulder.
34. *"I said, I'm seeing someone, and I'm loyal, my friend"* — her smiling, saying a short sentence, and walking on, genuinely kind, tracking as she goes.

### Pre-chorus 2 — the quiet

35. *"Used to call it lonely when the place went quiet"* — the flat from the hallway, empty, everything still, static wide, late daylight.
36. *"Used to fill it up with anyone I could find"* — a two-second cool flash: the memory look answering the door to nobody she cares about, then black.
37. *"Now the quiet is the part I look forward to"* — a record going on and a bath running in the next room, two cuts, warm.
38. *"And I don't rush a single thing that's mine"* — her sitting on the floor with her back against the sofa doing nothing at all, the peonies behind her, wide.

### Chorus 2 — fuller

39. *"I'm dating myself, and honestly it's going great"* — reuse the across-the-table framing of shot 19, another night, the candle burned lower.
40. *"She shows up on time and she never makes me wait"* — reuse the empty-chair reverse of shot 20, candle lower, the room behind fuller.
41. *"Reservation for one, and I said it out loud"* — the host stand again, a longer queue behind her, one menu again, medium.
42. *"Corner booth, candle lit, and I'm proud"* — her hand smoothing the tablecloth flat, a small ritual, macro.
43. *"I'm dating myself, no notes and no complaints"* — her tipping generously, notes going under the edge of a plate, close-up.
44. *"Nobody's bad mood that I have to translate"* — the arguing couple leaving in silence behind her while she orders more, single wide.
45. *"Ordered the dessert and I finished the plate"* — reuse shot 25 tighter, a different dessert, the same waiter grin.
46. *"I'm dating myself, and honestly it's going great"* — her walking out past a full restaurant with her coat over her arm, everyone else in pairs, tracking backwards.

### Instrumental — the rain, no lyrics

47. Rain starting hard on the pavement outside the restaurant, macro on a puddle taking the first drops, neon reflections breaking up.
48. Her under an awning, coat over her shoulders, entirely content to wait it out, medium, wet neon.
49. The electric piano solo over her walking, a bus passing, her reflection sliding across its lit windows, slow tracking.
50. A receipt being folded and pushed into a coat pocket, hands only, macro, streetlight.
51. One held wide of an empty city crossing in the rain, the light changing with nobody there — the cut into the bridge.

### Bridge — the honest part

52. *"This is not a speech about not needing nobody"* — her sitting on the edge of the bath with her shoes off, still in the dress, one lamp, static, unglamorous.
53. *"I would love a hand to hold when the winter comes"* — a close-up of her own hands, one holding the other, resting on her knees.
54. *"But I'm not going hungry at a table for two"* — a two-second cool flash: a restaurant table for two with two full plates and no conversation at all, faceless, then black.
55. *"Just to say that I wasn't the only one"* — back to the bathroom, her looking at nothing, breathing, medium.
56. *"So whoever you are, you can take your sweet time"* — a wide of the flat with one lamp and the front door standing open onto a dark hallway, nobody in it.
57. *"I'm not standing at the window keeping score"* — she walks past the window without looking out of it, deliberately, medium.
58. *"I'm not waiting to start, I already started"* — her pulling the duvet across the empty half of the bed herself, no drama, close-up.
59. *"And you'd be joining something good, not fixing something poor"* — her switching the lamp to its lowest setting and settling, the room warm — the cut into the final chorus.

### Final chorus — two desserts

60. *"I'm dating myself, and honestly it's going great"* — the booth again, the widest and warmest lighting in the video, across-the-table framing, slow push.
61. *"She shows up on time and she's never running late"* — the empty-chair reverse a third time, now with her coat draped over it like it belongs to somebody, close-up.
62. *"Reservation for one, and I said it out loud"* — her saying it to the host clearly, chin up, no apology in the delivery, medium.
63. *"Corner booth, candle lit, and I'm proud"* — a fresh candle lit at the table, the flame catching, macro.
64. *"I'm dating myself and I'm easy to date"* — her laughing properly at something off frame, head back, unposed, close-up.
65. *"Nobody's silence that I have to translate"* — the whole restaurant in one wide, her booth the brightest thing in it, static.
66. *"Ordered two desserts and I finished them straight"* — two desserts landing at one place setting, the waiter openly delighted, medium.
67. *"I'm dating myself, and honestly it's going great"* — her raising her glass to the empty chair, unembarrassed, holding it there, close-up.

### Post-chorus — the rituals, cut on the snaps

68. *"Going great, going great"* — earrings in, one cut per snap, macro.
69. *"Table for one and I'm never running late"* — the candle lit, macro, one cut.
70. *"Going great, going great"* — olives, then the glass of red, two fast cuts.
71. *"Flowers on a Wednesday and nothing to celebrate"* — paper folding around peony stems, macro, one cut.
72. *"Going great, going great"* — both armrests, then a record sleeve sliding out, two fast cuts.
73. *"Nobody to answer to and nobody to wait"* — a bath tap running, then a lamp switching on, two cuts.
74. *"Going great, going great"* — the phone face-down in the bag, held longer than the rest, macro.
75. *"I'm dating myself and it's going great"* — a fast rhythmic assembly of all eight ritual frames on the snaps, ending on the clean dessert plate.

### Outro — home

76. *"Walked home slow with the peonies wrapped in paper"* — her walking a night street with the flowers in the crook of her arm, tracking from the side, warm shop windows.
77. *"Keys in the door and the lamp already on"* — the door opening onto a room where the lamp is already burning because she left it on for herself that morning, from the hallway.
78. *"Poured one glass and I put on a record"* — one glass poured, a needle dropping, two cuts, macro, warm.
79. *"And I stayed up late with the best company I've known"* — final shot: her on the sofa with her feet up, the peonies in frame, eyes closing, a small private smile, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the single tap in shot 1, the first empty-chair reverse, each
*"I'm dating myself"*, the two-inch flower adjustment, the lobby no, the
instrumental, *"I'm not waiting to start"*, the two desserts, and the final
smile. At 94 BPM a bar is 2.55 s; the choruses cut on the snap and the
post-chorus cuts on every snap without exception.

**The solo-date challenge.** Post the vertical cut of chorus one (shots
19–26) with *"table for one"* on screen and invite people to film their own
reservation-for-one — one shot per ritual, ending on the dessert plate. The
empty-chair reverse (shot 20) is the still that will get screenshotted; keep
it beautiful enough to stand alone.

## 6. Quality-control checklist

- Three looks in the right sections: green satin only on date nights, cream knit and camel coat in daylight, the memory look only in shots 15, 16 and 36
- No ex appears anywhere; the only faceless man is the one in the cinema lobby, and he is kind
- The empty-chair reverse angles (20, 40, 61) are generated from the same plate as their matching across-the-table shot, with the candle a step lower each time
- The waiter is the same person in all four appearances and is never patronising
- All menus, screens, receipts and record labels composited; no model-generated text anywhere
- The bridge is the only deliberately unflattering lighting in the video
- No distorted hands in the candle, glass, spoon and flower-wrapping macros, which carry a third of the shots
- The last shot is locked-off and holds until the audio fades
