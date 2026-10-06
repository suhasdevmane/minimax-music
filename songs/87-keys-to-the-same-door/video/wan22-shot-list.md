# Wan 2.2 Shot List — "Keys to the Same Door"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
104 BPM a bar is 2.31 s, so most shots run 3–5 s and the choruses cut every
one or two bars.

## 1. Visual style

An unglamorous, deeply warm domestic film. Two poles: the **hardware store**
that opens and closes the video is flat overhead retail fluorescent with no
key light and no help from the room, and the **apartment** goes from bare
boards and one bulb to every practical lit at once over the course of the
song. The set is a **one-bedroom walk-up** — a stairwell with a bad turn in
it, a front door with a brass lock, a narrow hallway, a living room that is
empty for half the video. The recurring motif is **the hallway**: the same
locked-off frame returns in every chorus with more in it each time, one pair
of shoes, then three, then a heap, then coats and people. Nothing here is a
grand gesture and the camera never treats anything as one.

| Section | Grade | Camera |
|---|---|---|
| Intro | Flat retail fluorescent, green-grey, no warmth | Extreme close-ups, static |
| Verse 1 | Grey moving-out light; one warm entryway bulb on the buzzer | Handheld, quick cuts |
| Pre-chorus 1 | One bare bulb and a phone torch in a mug | Handheld, low, close |
| Choruses | Warm practicals, a rectangle of daylight through the open door | Locked-off hallway, slow push-ins |
| Verse 2 | Harsh stairwell fluorescent, then low warm lamp on the floor | Long takes, wide, then still |
| Pre-chorus 2 | Near-black, one strip of warm light under a door | Macro, static |
| Instrumental | Daylight crossing bare floor, then a second source | Slow gliding move, one locked-off |
| Bridge | One bedroom lamp; flat morning kitchen light | Low and close, then plain and still |
| Final chorus | Every light in the flat on, warm and a little too bright | Moving, wide, crowded |
| Post-chorus | Dim landing, hard bright rectangle at the door | Four matched locked-off frames |
| Outro | The same flat fluorescent as shot 1, read warm | Slow, calm, held |

## 2. Character bible — paste into every prompt

**Mahima** (moving day, intro through the second chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair scraped back into a messy low bun with strands loose at the temples, no makeup, wearing a faded olive t-shirt with the sleeves rolled and dusty grey cargo trousers, a strip of packing tape stuck to one forearm, tired happy expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge, private, morning)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and unbrushed, no makeup, wearing an oversized cream sweatshirt and soft striped pyjama shorts, bare feet, quiet unguarded expression, realistic cinematic photography, consistent identity

**Mahima** (final chorus and post-chorus, the housewarming)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and freshly washed, light natural makeup, wearing a deep red button-through dress and gold hoop earrings, bright open expression, realistic cinematic photography, consistent identity

**Kai** (the male lead, moving day)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a washed-out navy work shirt with the sleeves pushed up and dark jeans with a dust mark on one knee, a pencil behind one ear, easy patient expression, realistic cinematic photography, consistent identity

**Kai** (final chorus and post-chorus)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a soft charcoal knit over a white t-shirt and dark trousers, sleeves pushed up, warm settled expression, realistic cinematic photography, consistent identity

**The man in the green apron** — the only other face in the video, and only
in the outro. Older, sixties, kind, entirely unsurprised by anything.
> an older man in his sixties behind a hardware store counter, short grey hair, glasses pushed up, wearing a green work apron over a checked shirt, calm knowing expression, realistic cinematic photography

**Housewarming guests** — six to eight people in the final chorus, always in
soft focus or cropped, never given a close-up. No exes, no rivals, nobody
from anyone's past appears in this video at all.

Objects: the **key-cutting machine**, the **two warm brass keys**, the
**buzzer panel card**, the **tape gun**, the **stack of boxes**, the **lamp
still in the car**, the **wooden packing crate** and the pizza box on it, the
**couch** and the **cardboard sign**, the **toothbrush glass**, the **shoe
heap** by the door, the **hall light** nobody turns off, the **welcome mat**,
the **duffel bag** at the back of the closet, the **keyring** with four keys
on it, the **bowl by the door**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The buzzer-panel card, the cardboard sign on the couch and every price
label, aisle marker and shop sign in the hardware store are composited in
the edit.** Generate the buzzer as a blank white slot in a brass plate and
the sign as a blank piece of cardboard; the model cannot render legible
handwriting or print, and the two names in two different handwritings are
the single most important piece of information in verse one.

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

Most shots 3–5 s.

For this song specifically: build the apartment once as a plate and light it
four ways (bare bulb, day empty, evening lived-in, everything on for the
party) so the hallway frame matches exactly across shots 17, 34, 52 and 62 —
that repeated frame is the whole argument of the video and it only works if
it is literally the same lens, height and mark. Both leads need IP-Adapter or
a LoRA each. **OpenPose on every carrying shot** — the couch in the stairwell
(shots 23–24), the boxes up the stairs (shot 7) and anything with two bodies
gripping the same object is where the model fuses arms. Keep each clip to one
movement: a key turning, a bag emptying, a ring letting go of one key. The
key-cutting machine in shots 1 and 63 is the one place to spend a longer
generation and real sparks. The 9:16 recomposition is for the first chorus
and the post-chorus.

## 4. Scene per lyric line

### Intro — aisle four

1. *"The machine at the hardware store screams for eleven seconds"* — extreme close-up of a key-cutting machine, the wheel biting a brass blank, brass dust and a small spray of sparks, the guard vibrating, flat fluorescent, static, held long enough to be unpleasant.
2. *"Then it drops a warm piece of brass in my hand"* — the cut key dropped into an open palm, bright at the cut edge, the fingers closing around it slowly, macro, no warmth in the light at all.
3. *"Two of them, same cuts, same jagged promise"* — two identical keys turned over in her fingers against her thigh, the teeth lining up exactly, extreme close-up, slight handheld drift.
4. *"And I'm standing in aisle four about to cry"* — Mahima (moving-day look) standing in an aisle of paint sample cards holding it together badly, a wall of colour chips behind her, wide and unflattering, static, the ugliest lighting in the film.

### Verse 1 — eight moves, and a card with two names

5. *"I've moved eight times in nine years by myself"* — three fast cuts of the same action in three different empty rooms, a tape gun run across a box lid, different floors and different light in each, handheld, grey.
6. *"I know how to tape a box and lie about the weight"* — Mahima taping a box shut, pressing the seam flat with her thumb, then writing on the side with a marker and not looking up, close-up, deadpan.
7. *"I've handed back a key at the door of every place"* — a box handed up a stairwell to a pair of arms that take it and immediately grimace at the weight, low angle from the flight below, handheld.
8. *"And I've never once been given one back"* — a montage of hands giving keys away: onto a letting-agent's desk, through a letterbox slot, onto a bare kitchen counter, three cuts on the beat, always leaving, never receiving.
9. *"The buzzer downstairs has a slot for two names now"* — a brass buzzer panel beside a front door, one entryway bulb above it, a small blank white card in the slot (composited), close-up, the first warm light in the video.
10. *"Yours in your handwriting and mine underneath in mine"* — extreme close-up on the card, two names in two different hands, one above the other (composited), Mahima's thumb resting on the plate beside it.
11. *"It's the smallest piece of paper in the building"* — a wide pull back from the card to the whole entryway, mailboxes, a radiator, a bicycle chained to the rail, the panel tiny in the frame, static.
12. *"And I keep going down to check it's still there"* — Mahima coming down the stairs barefoot, checking the panel, touching it once, and going back up, a single continuous take from the landing above.

### Pre-chorus 1 — moving night

13. *"Boxes to the ceiling and the lamp's still in the car"* — boxes stacked to the ceiling in one corner of an otherwise empty room, one bare bulb overhead, wide, handheld.
14. *"A pizza on a packing crate and nowhere left to sit"* — an open pizza box on a wooden packing crate, two paper plates, both of them cross-legged on bare boards around it, low angle at floor height.
15. *"The neighbors heard us laughing at eleven"* — the hallway outside the door from the landing, a neighbour's light coming on under a door across the hall, muffled laughing through the wall, static, dim.
16. *"And I don't care, I'm not going anywhere"* — Mahima lying flat on her back on the bare floor laughing at the ceiling, a phone propped torch-up in a mug beside her throwing a hard shadow, overhead.

### Chorus 1 — one pair of shoes

17. *"Two keys to the same door, that's what I've been waiting for"* — **the hallway frame**, locked off from the far end: the front door, the mat, one pair of shoes beside it, a key turning in the lock on the downbeat and the door opening into daylight.
18. *"Not the ring, not the toast, not the ninety second speech"* — three quick cuts of things this song is not: an untouched jewellery-shop window seen from the street, two empty glasses upside down on a shelf, a bare microphone stand in an empty function room, then straight back to the hallway.
19. *"Just a hallway with our shoes in it and a light we both forget"* — the same hallway frame, now with three pairs of shoes, Kai stepping out of his boots without using his hands and walking through, static.
20. *"And a lock that finally knows the two of us"* — extreme close-up of a brass lock from inside, a key entering from the other side and turning, the bolt sliding back, warm.
21. *"Two keys to the same door, one welcome mat, one floor"* — a foot kicking the welcome mat straight, then a slow tilt up the door to the hall light burning in daylight, close.
22. *"That's what I've been waiting for"* — the hall light held in one shot that dissolves from night to daylight, still on, nobody having turned it off, static, warm.

### Verse 2 — the couch

23. *"The couch didn't fit up the stairs and we knew it at the landing"* — a two-seater sofa wedged diagonally in a stairwell at a hopeless angle, both of them on either side of it, red-faced, saying nothing, one long uncut wide take, harsh stairwell fluorescent.
24. *"And neither of us said it for twenty solid minutes"* — a slow push-in on Kai's face over the sofa arm, breathing, jaw set, refusing to be the one who says it, close-up.
25. *"You wanted it against the window, I wanted it against the wall"* — an argument conducted entirely in the empty living room with hand diagrams in the air, both of them drawing rectangles, no sound of the words, medium two-shot.
26. *"So we fought about a couch we couldn't physically get in"* — the sofa still in the stairwell behind them, unmoved, seen past their shoulders through the open flat door, static, the joke played completely straight.
27. *"Then we left it on the sidewalk with a sign and ate on the floor"* — the sofa on the pavement with a blank piece of cardboard on the cushion (composited), shot down from an upstairs window, one passer-by slowing to look.
28. *"First night in a house with nothing in it but us"* — the two of them eating off plates on the bare living-room floor, a lamp on the ground beside them with no shade, the room hollow and echoing, wide, warm and low.
29. *"And I never slept better on a worse mattress"* — a bare mattress on the floor with two people asleep on it, one duvet, no frame, no headboard, shot from floor level, the quietest frame in the film.

### Pre-chorus 2 — two lives merging at night

30. *"Two toothbrushes leaning on each other in a glass"* — macro of two toothbrushes in one glass, leaning together, a bathroom in near-darkness behind them, static.
31. *"My coat on your hook and your book on my side"* — a coat rack with one coat on the wrong hook, then a paperback face down on the wrong side of a bed, two cuts, both close.
32. *"I woke at four and heard you in the kitchen"* — a dark bedroom, Mahima's eyes opening at the sound of a cupboard in another room, a strip of warm kitchen light under the door, extreme close-up.
33. *"And I wasn't scared, I just went back to sleep"* — her eyes closing again, the strip of light going out mid-shot, the frame dropping to black, static, held.

### Chorus 2 — the flat becomes a home

34. *"Two keys to the same door, that's what I've been waiting for"* — the hallway frame again, evening, more practicals lit, six pairs of shoes now, both of them coming through the door together carrying nothing, locked off.
35. *"Not the ring, not the toast, not the ninety second speech"* — a shelf filling across three cuts: his books, her books, then a shelf where there is no telling whose is whose, slow push-in.
36. *"Just a hallway with our shoes in it and a light we both forget"* — the shoe heap now permanent, the two of them stepping over it without looking down while still talking, handheld from behind.
37. *"And a lock that finally knows the two of us"* — reuse shot 20, tighter, evening light on the brass instead of daylight.
38. *"Two keys to the same door, one welcome mat, one floor"* — a fridge door acquiring photographs across cuts, one, then four, then a full door, magnets and a takeaway menu, close.
39. *"That's what I've been waiting for"* — a chair finally arriving to replace the packing crate, carried in and set down, the crate picked up and taken out, one continuous move.

### Instrumental — the empty flat, sixteen bars

40. A slow gliding move down the hallway with nobody in it: the mat, the shoes, the bowl on the shelf by the door, warm daylight from one window crossing bare floor.
41. The move continues into the living room and holds on the couch-shaped absence, a rug and a lamp and nothing between them, dust in the light.
42. Small locked-off details on the piano solo: the toothbrush glass, the buzzer card from outside the door, the hall light on in daylight, three cuts.
43. The four-bar drop to claps and one hum: a single locked-off frame of the front door from inside, closed, absolutely still, held for the whole drop.
44. The rebuild: the door opening and both of them coming through it with grocery bags, the second light source arriving with them, the room finally correct, same locked-off frame.

### Bridge — the bag and the ring

45. *"I kept a bag half packed at the bottom of the closet"* — a closet floor shot from low and close, a duffel bag half packed and pushed to the back behind shoes, lit by one torch, cramped.
46. *"Just in case the room got small, just in case I had to go"* — Mahima (bridge look) crouched in the closet doorway, one lamp behind her, looking at the bag without touching it, still.
47. *"I unpacked it Tuesday, there's nothing left I could run with"* — the bag emptied onto a bed slowly, item by item, a jumper, a charger, a passport wallet, her hands only, close.
48. *"And I had spare keys on my ring for people who moved out"* — the empty bag folded flat and pushed onto a high shelf, then a hard cut to a keyring on a kitchen table with four keys on it, flat morning light.
49. *"I took them off this morning, there is only one now"* — three keys worked off the split ring one at a time and set aside on the table in a small row, extreme close-up on the hands, the plainest and most decisive shot in the video.
50. *"So the door does what a door does, it opens and it holds"* — the front door from inside, opening a few inches on its own weight and stopping, no one in frame, static.
51. *"And we are the two who are allowed in"* — Kai coming into the kitchen behind her, seeing the row of keys on the table, saying nothing, putting a hand flat on her back, medium two-shot, morning.

### Final chorus — the housewarming

52. *"Two keys to the same door, that's what I've been waiting for"* — the hallway frame, every light on, the door standing open, coats over the rail, people coming through continuously, the shoe heap enormous.
53. *"Not the ring, not the toast, not the ninety second speech"* — the crowded room with a guest raising a glass and being cheerfully talked over, nobody making a speech, handheld through the crowd.
54. *"Just your keys in the bowl and mine on top of them"* — the bowl by the door with two keys in it, then a hand adding a set, then a dozen sets, three cuts, close and warm.
55. *"And a lock that finally knows the two of us"* — the lock from inside with the door already open and the key still in it, forgotten, party noise around it, close.
56. *"It's the first place in my life I'm not rehearsing leaving"* — Mahima (housewarming look) alone in the hallway for two seconds with the party behind her, one hand on the door frame, looking down the hall at her own flat, slow push-in — the caption frame.
57. *"Two keys to the same door, one welcome mat, one floor"* — the two of them across a crowded room, one look, nothing said, a rack focus from her to him through moving bodies.
58. *"That's what I've been waiting for"* — the widest and warmest frame in the video: the whole flat lit, full of people, seen from the open front door looking in, slow move forward over the threshold.

### Post-chorus — the door doing its job

59. *"Same door, same door, same little brass and steel"* — four matched locked-off frames of the same lock from the same angle in fast succession: her key, his key, her key with shopping bags on her arm, his key one-handed with a coffee.
60. *"Same door, same door, and I'm still not used to it"* — Mahima stopping for one beat after the lock turns, hand still on the key, a small disbelieving breath, then pushing the door, close.
61. *"Same door, same door, turn it twice and come on in"* — extreme close-up of the key turning twice, two distinct throws of the bolt, the second one landing on the beat.
62. *"Two keys to the same door"* — the door swinging open into the lit hallway, the party noise arriving with it, a hard rectangle of warm light thrown across the dim landing.

### Outro — back to aisle four

63. *"The machine at the hardware store screams for eleven seconds"* — the key cutter again from the exact angle of shot 1, the same eleven seconds, the same sparks, flat fluorescent.
64. *"And a man in a green apron says, good luck to you both"* — a wider shot revealing the older man in the green apron behind the counter, sliding the two keys across to her, medium, static.
65. *"He has no idea what he just handed me"* — his face, kind and completely unsurprised, a small nod, close-up, the only other face given a close-up in the video.
66. *"Or maybe he does, and that's why he said it like that"* — final shot: the two keys on the counter between them, close and warm, her hand arriving to take them, locked off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first piano note, each *"two keys to the same door"*, the
hallway frame in every chorus (shots 17, 34, 52, 62), the instrumental, the
four-bar drop at shot 43, the row of keys on the table at shot 49, the
caption line at shot 56, and the final hold at shot 66. At 104 BPM a bar is
2.31 s; choruses cut every one or two bars, the verses hold three to five
seconds a line, and the couch take at shot 23 deliberately runs over.

**The shoe-pile challenge.** The hook is caption-ready. Post the vertical cut
of chorus one (shots 17–22) with *"two keys to the same door"* on screen and
invite people to post one fixed hallway shot on day one against the same
frame on day one hundred — the shoe heap does all the work, and anyone who
has moved in with anyone can shoot it in ten seconds. The second shareable
cut is the couch wedged in the stairwell with twenty seconds of neither of
them saying a word (shots 23–24); the third is the bowl filling up at
shot 54.

## 6. Quality-control checklist

- Three looks for Mahima and two for Kai, in the right sections: moving-day clothes never appear after shot 39, the housewarming looks never before shot 52
- The hallway frame is literally identical in shots 17, 34, 52 and 62 — same lens, same height, same mark, only the contents and the light change
- The shoe count only ever goes up: one pair at 17, three at 19, six at 34, a heap from 36 on
- The buzzer card, the cardboard sign on the couch and every shop label are composited; no model-generated handwriting or print anywhere
- Nobody from anyone's past appears; the guests are always soft or cropped, and the man in the green apron is the only other face given a close-up
- OpenPose on every two-body carrying shot, especially the sofa in the stairwell — no fused arms and no third hand on the cushion
- The hardware store is graded identically in shots 1–4 and 63–66; nothing about the light changes, only what she brings to it
- The last shot is locked-off and holds until the audio fades
