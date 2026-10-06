# Wan 2.2 Shot List — "Passport Stamps"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission, plus six shots for the instrumental. Timestamps come from the
rendered WAV; cut on the sung line. At 116 BPM a bar is 2.07 s, so the
verses cut every bar and the post-chorus lands a stamp on every downbeat.

## 1. Visual world

A travel film in which **every third cut is a face, not a place**. That is
the rule the whole edit is built on, and it is the argument of the song: the
stamps are an index of people. If a sequence runs three landscape or transit
shots without a person in it, one of them gets replaced.

Each city has one light and keeps it, so a two-second return later in the
film is instantly recognisable: **Lisbon** warm sodium and yellow tram
paint; **Tokyo** cold neon on wet tarmac; **Oaxaca** warm afternoon through
a doorway with smoke and steam in the beam; **Berlin** red and dark and low;
**Marrakech** dusty pink at dusk; **Istanbul** flat airport white; **Peru**
high, thin, bright. Against all of them sit the two framing worlds: the
**airport** at pre-dawn, cold blue through glass under hard fluorescent, and
her mother's house, one bedside lamp and nothing else on.

Nothing is graded like a tourism advert. Real sun, real fluorescent, one
unflattering gate lounge, and a crying shot that is allowed to be ugly.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cold pre-dawn blue, hard fluorescent | Macro, then a still queue wide |
| Verse 1 | One fixed light per city | Handheld, close to people |
| Pre-chorus 1 | Whatever light she is in — a bunk lamp, a strip light | Static, phone-height |
| Chorus 1 | Real sun, the brightest and widest so far | Moving in every frame |
| Verse 2 | Berlin red, Marrakech pink, Istanbul white | Handheld, then locked at the counter |
| Pre-chorus 2 | An unfamiliar curtain, unidentifiable | Static, low, waking up |
| Chorus 2 | Saturated afternoon into evening | Faster, more people in frame |
| Instrumental | Six different lights cut hard together | Feet, hands, one slow-motion stamp |
| Bridge | One bedside lamp, everything else off | Still, close, the quietest run |
| Final chorus | Full daylight throughout | Cut on the beat, everything at once |
| Post-chorus | Hard flat counter light, high contrast | Four stamps, four faces |
| Outro | The same cold pre-dawn blue as the intro | Locked off, held |

## 2. Character bible — paste into every prompt

**Mahima** (the whole film — one look, deliberately)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose or pushed back off her face, no makeup, wearing a faded olive utility jacket over a plain white tee and dark jeans, a small worn canvas backpack on one shoulder, open curious expression, realistic cinematic photography, consistent identity, natural skin texture

She wears the same jacket in every city. It is the only continuity object
the audience is given, and it gets visibly more worn as the film goes on —
build three versions of the plate texture, clean, faded and frayed, and use
them in order.

**Mahima** (bridge, her mother's house)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, no makeup, wearing an old grey sweatshirt she clearly owned as a teenager, sitting on the floor of a childhood bedroom, soft settled expression, realistic cinematic photography, consistent identity

**Kai** (the recurring one — Tokyo, Berlin, Marrakech, Istanbul, the gate)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a dark wool overcoat over a grey crewneck, a canvas duffel over one shoulder, easy unhurried expression, realistic cinematic photography, consistent identity

He is the only person in the film who appears more than once, and the
audience should not be told he is recurring — they should notice.

**The Lisbon girl** — a young woman with paint under her nails and on her
forearms, denim shirt, laughing, seen on the step of a yellow tram at night.
Face fully seen; she is a friend, not a rival.

**The Oaxaca family** — a courtyard kitchen full of people of three
generations, talking over her head, none of them singled out and none of
them a grandmother. The woman who feeds her is seen from the chest down and
by her hands, putting a plate in front of the camera.

**Her mother** — only ever on a phone screen, warm and unconvinced.

Objects that carry the story: the **passport** and the **stamp coming down**
(the film's percussion), the **paper coffee cup**, the **two hot cans from
the vending machine**, the **two boarding passes in one hand**, the
**shoebox under the bed**, the **napkin with a map drawn on it**, and the
**two passports side by side** — one battered and full, one new and empty.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every passport page, stamp, boarding pass, departure board, street sign
and phone screen is composited in the edit.** Generate blank documents and
blank boards; the model produces garbage country names and nonsense scripts,
and a wrong stamp in a travel video is the one mistake the audience will
catch. The napkin map in the bridge is drawn in post and never legible. No
real airline or country marks anywhere.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in her two looks and Kai in his one look with IP-Adapter or a
character LoRA each; the Lisbon girl and the Oaxaca kitchen need their own
references too, since both return in the bridge and must match. Depth for
the market, the club and the courtyard. OpenPose for the dance she gets
pulled into and for the crowd shots. 16:9 first; 9:16 recomposition for the
stamp macros and the post-chorus, both of which are natural vertical
content.

Animate one movement per clip: a stamp coming down, a tram pulling away, a
can dropping into a vending-machine tray, a plate being set down, a
departure board flipping, a face turning. The two chorus montages are cut
from many short generations rather than long ones — nothing in this film
needs to run more than three seconds except the bridge and the last shot.
The crying shot in shot 30 should be generated several times and picked for
the one where the laugh actually arrives.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–3 s; the bridge runs 4–5 s.

## 4. Scene per lyric line

### Intro — departures before sunrise

1. *"Ink on the page and an airport at dawn,"* — macro on a passport open on a counter and a stamp coming down hard, the ink square landing among others, cold overhead light.
2. *"Boarding pass in my teeth, half my sleep gone."* — her in the queue with a boarding pass held in her teeth while she gets the passport out, the backpack on one shoulder, half the concourse lights still off behind her, medium.
3. *"A stranger stamps the book, never asks me my name,"* — the officer at the desk, seen past her shoulder, working without looking up, the book pushed back across the counter.
4. *"One more little square that says I came."* — her picking the passport up and turning away, the counter empty behind her, cold blue through the glass, medium, static.

### Verse 1 — three cities, three people

5. *"Lisbon was a girl with paint under her nails,"* — the Lisbon girl laughing on the step of a yellow tram at night, paint on her hands and forearms, warm sodium light, handheld and close.
6. *"Yellow tram at midnight, she taught me how to fail."* — the tram pulling away with the girl on the step still waving, Mahima left on the cobbles laughing, the tram light sliding off the buildings.
7. *"Tokyo was a boy by a vending machine,"* — Kai in a dark overcoat by a lit vending machine on an empty wet street, cold neon on the tarmac, wide, still. **First appearance — do not flag it.**
8. *"Two cans of hot coffee, no words in between."* — two hot cans dropping into the tray, one handed across, neither of them speaking, both of them holding the cans for the warmth, close two-shot.
9. *"Oaxaca was a kitchen and a stranger's hands,"* — a plate set down in front of the camera by a woman seen only from the chest down, a courtyard kitchen busy behind her, warm doorway light with steam in it.
10. *"Feeding me like family in words I couldn't understand."* — the room talking over her head, three generations at one table, nobody explaining anything to her, her laughing anyway, handheld from her seat.
11. *"Every border I crossed, somebody crossed it with me,"* — a border queue at a land crossing, her and somebody she has clearly just met sharing a look about the wait, medium.
12. *"I carry all of them like ink you can't see."* — a slow tilt across her own forearms and open hands, unmarked, in the same warm light as the kitchen, macro.

### Pre-chorus 1 — the phone call

13. *"My mom keeps asking when I'm gonna settle down,"* — her on a hostel bunk with a phone propped against a bag, her mother's face on the screen (composited), affectionate and unconvinced, static.
14. *"I said, mama, I'm settled, just in a lot of towns."* — her laughing and shaking her head at the screen, the bunk lamp the only light, close-up.
15. *"Nothing's chasing me out, I'm chasing every bit of it,"* — her walking fast down a station platform toward something out of frame, tracking from the front.
16. *"Nobody comes back the same, and that's the point."* — her stopping at the platform edge as a train arrives, the wind of it in her hair, medium, held one beat.

### Chorus 1 — the daylight montage

17. *"Passport stamps and a heart full of places,"* — a train window with a whole country going past it, her reflection faint in the glass, real sun.
18. *"Every page is a name, every name has a face."* — the Lisbon girl's face, the Tokyo boy's face, a bus driver's face, three cuts on the beat, all looking at camera.
19. *"Lisbon in my laugh and Tokyo in my walk,"* — her laughing in a market at full noon with somebody's hand on her arm, handheld, crowded.
20. *"A little Oaxaca in the way that I talk."* — her mid-sentence with her hands moving, talking to two people whose backs are to camera, warm afternoon.
21. *"Passport stamps and a heart full of places,"* — a mountain road from the back of a moving truck, three other people's legs hanging off the tailgate with hers, wide.
22. *"I don't count countries, I count who I met."* — a hostel receptionist mid-laugh behind a desk, then a stranger on a bus asleep against her shoulder, two cuts. **The caption frame.**
23. *"Everywhere I land, I leave a piece, take one,"* — a beach at the wrong end of the day, grey-gold, her sitting with two other people, nobody in swimwear, real.
24. *"Passport stamps and a heart full of places, I've only just begun."* — her walking away from camera down a wide bright street with the backpack on, the frame at its widest and brightest so far.

### Verse 2 — the recurring one

25. *"Berlin was a bass line in a basement till four,"* — a low-ceilinged basement club, a bass bin, red light, the two of them standing in the crowd rather than dancing, handheld, dark.
26. *"Marrakech was the same boy waiting at my door."* — a riad doorway at dusk, dusty pink light, Kai already there with the duffel down at his feet, her arriving and stopping. **The reveal — the audience should recognise him from shot 7 without help.**
27. *"We got two stamps side by side in Istanbul,"* — a counter in flat airport white, two passports handed over together, two stamps landing one after the other, macro, locked off.
28. *"Window seat and aisle seat, and that was beautiful."* — the two of them in a row of two on a plane, her at the window, him on the aisle, both asleep, overhead.
29. *"Then he flew home in March and I flew on to Peru,"* — two boarding passes in one hand, then one of them going across to him, a gate lounge behind, close on the hands.
30. *"Cried at the gate, then laughed, cause that's what I do."* — her crying properly and unattractively in a gate seat, then laughing at herself and wiping her face with a sleeve, unflattering fluorescent, medium, held.
31. *"Some people are a chapter and some are just a line,"* — a departure board flipping over above her, the destinations composited and unreadable, her looking up at it.
32. *"But every single one of them is written down my spine."* — her walking to her own gate alone with the jacket visibly more worn than it was in Lisbon, tracking from behind, high, thin Peruvian light waiting past the glass.

### Pre-chorus 2 — a room she doesn't know

33. *"Sometimes it's Tuesday and I wake up in a bed,"* — a ceiling she does not recognise, filmed from her pillow, an unfamiliar light fitting, static.
34. *"Don't know the city, or the language in my head."* — a window, then a street sign out of focus that she cannot read (composited), then her sitting up on the edge of the bed and laughing at herself, three cuts.
35. *"Nothing's chasing me out, I'm chasing every bit of it,"* — her lacing a boot on the edge of the bed, decided, close-up.
36. *"Nobody comes back the same, and that's the point."* — her opening a door onto a street she has never seen, the light hitting her face, medium, held.

### Chorus 2 — with people in it

37. *"Passport stamps and a heart full of places,"* — a train window again, but this time somebody else is in the seat opposite her, talking, saturated afternoon.
38. *"Every page is a name, every name has a face."* — three more faces on the beat: the Oaxaca woman's, a market seller's, Kai's from Berlin, all looking at camera.
39. *"Lisbon in my laugh and Tokyo in my walk,"* — somebody else's hands taking her phone to take her picture, her posing badly and laughing, handheld.
40. *"A little Oaxaca in the way that I talk."* — her at a long table in the middle of a group, arguing about something with her hands, warm evening.
41. *"Passport stamps and a heart full of places,"* — her being pulled into a dance she does not know by two people who do, wide, evening.
42. *"I don't count countries, I count who I met."* — her failing the dance and being laughed at kindly, close.
43. *"Everywhere I land, I leave a piece, take one,"* — a rooftop at dusk with six people on it and her among them, nobody looking at the view, wide.
44. *"Passport stamps and a heart full of places, I've only just begun."* — her walking away down another street, the jacket more worn again, evening this time, matched to shot 24.

### Instrumental — the percussion break

45. Feet on six surfaces cut on the drums, half a second each: cobbles, sand, a tiled station floor, a metal gangway, a dirt road, an escalator.
46. Hands on a drum in a street band, macro, the skin of the drum moving.
47. A stamp coming down in slow motion, the ink spreading into the paper, macro, the loudest image in the film.
48. A window seat: a wing and cloud, unmoving, held longer than anything around it.
49. Her back on a night bus with her head against the glass, a road going past, the only quiet shot in the break.
50. A door opening onto a room she has never seen, the light arriving — the cut into the bridge.

### Bridge — the shoebox

51. *"There's a shoebox under my bed at mama's house,"* — a childhood bedroom, one bedside lamp, a shoebox being pulled out from under a bed, her on the floor in the old sweatshirt, wide, still.
52. *"Boarding passes, ticket stubs, a napkin with a map drawn out."* — the contents spread on the carpet: passes, stubs, a napkin with a biro map on it (composited, never legible), macro over her hands.
53. *"The old book ran out of pages, they gave me a new one,"* — two passports side by side on the carpet, one battered and swollen with stamps, one flat and empty, close-up.
54. *"But the first one stays in the box, cause that's where I come from."* — the old one going back in the box and the lid going on, her hand staying on the lid, macro.
55. *"Home was never a country, it was never a street,"* — the Lisbon girl and the Oaxaca kitchen returning for two seconds each, each held a beat longer than the first time.
56. *"Home is every person who walked a mile with me."* — Kai at the gate, and her mother on the phone screen, two more returns, same treatment.
57. *"When they ask me where I'm from, I say it's complicated,"* — her face on the bedroom floor in lamp light, thinking about it, close-up, the quietest frame in the film.
58. *"I'm from everywhere I've loved and everyone who waited."* — her mother in the bedroom doorway behind her, not saying anything, the lamp between them, medium, the drums returning.

### Final chorus — everything at once

59. *"Passport stamps and a heart full of places,"* — full daylight, a wide of her walking into a departures hall with the new passport in her hand, the widest frame of the film.
60. *"Every page is a name, every name has a face."* — six faces from the whole video on six beats, faster than either previous chorus.
61. *"Berlin in my hips and Istanbul in my eyes,"* — the basement club and the Istanbul counter cut against each other on the bar, red then white.
62. *"A little bit of Peru in the way I say goodbye."* — high thin bright light, a bus pulling out of a mountain town, her waving from the road, wide.
63. *"Passport stamps and a heart full of places,"* — every mode of transport in the film on the beat: tram, train, plane, truck, bus, escalator.
64. *"I don't count countries, I count who I met."* — a single long lens on a crowded street, her in the middle of it, indistinguishable from everyone else for one beat.
65. *"Everywhere I land, I leave a piece, take one,"* — her hugging somebody hard at a station, both of them holding on a beat too long, medium.
66. *"Passport stamps and a heart full of places, I've only just begun."* — her at a gate window with a plane on the stand beyond it, the sun full on her face, medium wide.

### Post-chorus — a stamp on every downbeat

67. *"Stamp it, one more page,"* — a stamp coming down on a downbeat, a hand, a counter, hard flat light.
68. *"Every face is a place I'd never trade."* — a face between the stamps: the Lisbon girl, straight to camera, half a second.
69. *"Stamp it, one more page,"* — a second stamp, a different desk, a different hand, on the beat.
70. *"Heart full of places, I'm on my way."* — two more stamps and two more faces alternating on the downbeats, ending on the passport closing.

### Outro — the same counter, a year on

71. *"Ink on the page and an airport at dawn,"* — the same departures hall at the same hour, matched exactly to shot 1, cold blue through the glass.
72. *"Somebody new in the seat where you were gone."* — a stranger asleep in the gate seat where Kai sat in shot 29, the same seat, the same angle, medium.
73. *"The stranger stamps the book and this time knows my name,"* — the officer from shot 3 looking up and saying something to her, her surprised and pleased, over-the-shoulder.
74. *"And I smile, cause I came."* — final shot: the new passport closing on the counter, her hand taking it, and her walking out of frame toward the gates, leaving the counter empty. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first stamp, each *"passport stamps and a heart full of
places"*, the vending machine in shot 7, the reveal in shot 26, the gate in
shot 30, the instrumental, the shoebox in shot 51, the mother in the doorway
in shot 58, the post-chorus stamps, and the empty counter. At 116 BPM a bar
is 2.07 s; the choruses cut on the bar, the post-chorus on the downbeat with
a stamp landing on each one.

**The stamp challenge.** The shareable cut is shots 67–70 — four stamps and
four faces, vertical, with the chant on it. Invite people to post their own
passport spread or one face from every trip, one per beat. The second
shareable frame is shot 22 with *"I don't count countries, I count who I
met."* **The quote:** *"Some people are a chapter and some are just a line,
but every single one of them is written down my spine."*

## 6. Quality-control checklist

- The rule holds: no run of three consecutive shots without a person's face in it, anywhere in the film
- One jacket, three wear states, in order — clean through Lisbon and Tokyo, faded from Berlin, frayed from shot 32 on; the old sweatshirt appears only in the bridge
- Kai appears in shots 7, 8, 25, 26, 27, 28, 29, 38 and 56 and nowhere else, and shot 7 gives away nothing
- Every city keeps its single light: Lisbon sodium, Tokyo neon, Oaxaca doorway warm, Berlin red, Marrakech pink, Istanbul white, Peru high and thin
- No document is legible in any frame — no stamps with country names, no boarding passes, no departure boards, no street signs, no napkin map
- Nobody who feeds her in Oaxaca is framed as a grandmother, and no face there is singled out
- Shot 30 is allowed to be unflattering; if the laugh does not land in the take, regenerate rather than cut around it
- Shots 1 and 71 are the same lens, height and light; shot 74 holds on the empty counter until the guitar stops
