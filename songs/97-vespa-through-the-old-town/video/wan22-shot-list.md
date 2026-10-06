# Wan 2.2 Shot List — "Vespa Through the Old Town"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
112 BPM a bar is 2.14 s, so most shots run 4–5 s and the choruses cut every
two bars, except the post-chorus, which cuts on every stomp.

## 1. Visual style

One Mediterranean old town over one week, in three passes: **full sun**
(chorus one), **string-light evening** (verse two and the harbour), and
**night into blue dawn** (chorus two, bridge and the last ride). The
apricot and ochre walls do the colour grading for us — every daylight shot
gets warm bounce onto both faces off a wall. **The handlebar mount is the
signature camera**: at least one mounted shot per section, so the audience
rides the whole film rather than watching it. Nothing is shot on a long lens
except the bell tower, which is deliberately withheld until the final chorus.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cool dark interior, one hard bar of sun | Static, counter-level |
| Verse 1 | Deep courtyard shade cutting to full sun | Slow pan, then mounted |
| Pre-chorus | Strobing hard sun and deep shade | Handlebar mount |
| Chorus 1 | Full midday, slightly overexposed, apricot bounce | Tracking car, drone |
| Verse 2 | Blue hour into warm string-light gold | Locked-off, single close-ups |
| Pre-chorus 2 | Harbour sodium, one floodlight, black water | Mount, slower |
| Chorus 2 | One headlight, sodium, moon on water | Mounted, aerial |
| Instrumental | Warm, plus one cool-graded dawn swim | Slow motion, observational |
| Bridge | Darkest in the film, warm from below only | Locked-off wide, macro |
| Final chorus | Deep night into the first blue of morning | Continuous ride, drone pull-back |
| Post-chorus | Full sun, saturated, hard cuts | Whip pans, no fades |
| Outro | Clean flat morning, no drama | Static, held |

## 2. Character bible — paste into every prompt

**Mahima** (daytime)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and wind-blown, no makeup, wearing a faded yellow cotton sundress and white canvas trainers with a small canvas backpack, delighted open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (evening and night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, light natural makeup, wearing a faded yellow cotton sundress under an oversized man's denim jacket, calm warm expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the local, all week)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a worn denim jacket over a plain white t-shirt and dark work trousers, scuffed leather boots, easy unhurried expression, realistic cinematic photography, consistent identity

There is no ex and no rival in this film. Everyone else is a resident of the
town, shot as themselves: the grandmother at the first-floor window, the
five-piece square band, the man mending net at the harbour, the card players
outside the bar at seven in the morning. Faces are fine; nobody is styled.

Objects: the **mint-green scooter**, the **wing mirror wrapped twice in
silver tape** (the emotional object of the film — it appears in the courtyard,
the bridge and the outro), the **badly folded paper map**, the **paper cup of
lemon ice with one spoon**, the **denim jacket** (his, from shot 31 to the
end), the **bell tower**, withheld until shot 58.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All signage, shop lettering, the map, the boarding pass and any menu are
composited in the edit.** Generate the map as a blank folded paper and the
phone as a lit blank screen; the model cannot render legible European
signage and one wrong word breaks the location.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock both leads with IP-Adapter or a character LoRA each; build Mahima's
daytime and evening looks as separate references since the denim jacket
changes the silhouette. **OpenPose for every shot with the scooter** — a
pillion passenger's leg and arm geometry is exactly what the model invents,
and a bad mount ruins the signature camera. Depth for the narrow-street
mounted shots, where the walls are a hand's width from the lens. 16:9 first;
9:16 recomposition for the handlebar shots and the laundry sheets, which are
the vertical clips. Animate in single gestures: one kick-start, one sheet
filling with wind, one wave from a window, one branch touched. Cloth in wind
and water render better in slow motion — shoot the sheets and the dawn swim
long and retime in the edit.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–5 s. Post-chorus cuts 1 s.

## 4. Scene per lyric line

### Intro — the bar with no chairs

1. *"Two euros for a coffee at a bar with no chairs"* — two small white cups on a zinc counter, one hand each, the square visible through the open doorway behind, static, counter-level.
2. *"You drank yours standing up like you were born here"* — Kai draining his cup in one movement and setting it down, entirely at home, medium.
3. *"I had a map that I folded wrong"* — Mahima wrestling a paper map that will not fold back the way it came, defeated by it, close-up on hands and face.
4. *"A terrible sense of north, and a week"* — both of them looking at the map, then at the square, then at each other; the hard bar of morning sun across the counter between them.

### Verse 1 — the borrowed bike

5. *"You said no bus comes back here until Thursday"* — an empty bus stop on the edge of town with nothing at it, wide, dry.
6. *"But you knew a guy with a key and a bike"* — a garage courtyard in deep shade, a shape under a tarpaulin, Kai with a key in his hand.
7. *"It was mint green and older than both of us"* — the tarpaulin coming off in one movement, then a slow pan the length of the mint-green scooter.
8. *"And the mirror was taped back on twice"* — macro: the wing mirror wrapped twice in silver tape, the first appearance of the film's key object.
9. *"Bag on my back and my hands on your jacket"* — her small canvas backpack going on, then her hand hovering an inch off his denim jacket and closing on it.
10. *"And the engine sounded like a wasp in a jar"* — the kick-start, the engine catching badly then holding, low angle on the exhaust and the wheel.
11. *"Then the road tipped down and the town opened"* — a hard cut from courtyard shade into full sun as they clear an archway, the road tipping downhill.
12. *"And I forgot to ask how far"* — the whole town opening out below: rooftops, the sea beyond, no bell tower yet, wide.

### Pre-chorus 1 — streets too narrow

13. *"Left at the church, right at the laundry lines"* — handlebar mount: a church corner taken tight, the wall sliding past a hand's width from the mirror.
14. *"Down a street too narrow for a car"* — mount continuing: laundry lines strung overhead, white sheets flaring as they pass beneath.
15. *"Somebody's grandmother waved from a window"* — an old woman at a first-floor window raising one hand, low angle up, warm shutter green behind her.
16. *"And I waved back like I lived here"* — Mahima waving back with both hands, over-committed and delighted, from the pillion, tracking.

### Chorus 1 — full sun

17. *"On a Vespa through the old town, holding on to you"* — a long tracking car alongside the scooter on a coast road, both of them laughing, sea on the far side.
18. *"Cobblestones like a heartbeat coming through my shoes"* — her feet on the footboard vibrating with the cobbles, macro, the stones blurring beneath.
19. *"Lemon trees and laundry and a bell I cannot see"* — a lemon tree branch hanging low enough that she reaches up and touches it going past, slow motion.
20. *"And a boy from a town I can't spell in front of me"* — from directly behind her: Kai's shoulders and the road ahead over them, her point of view held.
21. *"On a Vespa through the old town, nothing left to prove"* — a drone lifting off them as they come out of a short tunnel into light.
22. *"Half a tank of nowhere and a summer to use"* — the fuel gauge and the two of them reflected in the taped mirror, macro.
23. *"There's no part of this week that I'd undo"* — her face in profile at speed, eyes closed into the wind for one beat, apricot bounce off a wall.
24. *"On a Vespa through the old town, holding on to you"* — a wide from a hillside: the scooter as one small mint-green dot on a road above the sea.

### Verse 2 — the fountain and the band

25. *"We split a lemon ice on the rim of a fountain"* — the two of them from behind on a stone fountain rim, one paper cup and one spoon between them, the square busy behind.
26. *"Where the water's been running since before either name"* — macro: the fountain spout, the water lit from beneath, carved stone worn smooth.
27. *"You said everyone here has kissed somebody on it"* — Kai in single close-up, talking to the water rather than to her.
28. *"And you said it to the water, and I said the same"* — Mahima in single close-up, also talking to the water. Never a two-shot in this exchange.
29. *"The band in the square only knows seven numbers"* — a five-piece square band on a low platform, accordion, guitars, a small drum, wide.
30. *"So they played the slow one twice and took their time"* — couples of every age dancing badly in the square, one very old pair dancing well, handheld.
31. *"You put your jacket round my shoulders near eleven"* — his denim jacket going round her shoulders; she does not comment on it, close two-shot.
32. *"And I decided the night could be mine"* — her face lit by string lights, a decision arriving behind the eyes, close-up.

### Pre-chorus 2 — the harbour

33. *"Left at the bakery, right at the harbour"* — handlebar mount, night, empty streets, slower than the daytime mount, a lit bakery window passing.
34. *"Down where the boats are all faded blue"* — a working harbour, not a marina: nets, crates, faded blue hulls, one floodlight, wide.
35. *"Somebody's radio was playing our nothing"* — a small radio on a crate beside a man mending net, macro, the black water moving behind.
36. *"And I sang it wrong on purpose so you would too"* — both of them singing a song neither knows, badly, on the harbour wall, handheld.

### Chorus 2 — the same roads at night

37. *"On a Vespa through the old town, holding on to you"* — the coast road with no other traffic, the single headlight throwing forward, tracking car.
38. *"Cobblestones like a heartbeat coming through my shoes"* — reuse the footboard framing from shot 18, now in headlight spill and sodium.
39. *"Lemon trees and laundry and a bell I cannot see"* — the same lemon tree in the dark, the branch out of reach now, static.
40. *"And a boy from a town I can't spell in front of me"* — her arms out sideways for two seconds, then back onto his jacket, from behind.
41. *"On a Vespa through the old town, nothing left to prove"* — the whole town from above at night, all lit, drone, slow.
42. *"Half a tank of nowhere and a summer to use"* — the taped mirror again, now holding sodium and a moon, macro.
43. *"There's no part of this week that I'd undo"* — the moon on the water at speed, the road edge in the near frame, mounted.
44. *"On a Vespa through the old town, holding on to you"* — the scooter as one headlight on a dark coast road, very wide, hillside.

### Instrumental — accordion, then the stomp break

45. Slow-motion pass of white sheets on a laundry line, filling and emptying, backlit.
46. The square band packing up: instruments into cases, the platform cleared, chairs stacked.
47. A dawn swim — both of them going into flat grey sea fully awake and shouting; the only cool-graded shot in the film.
48. Old men playing cards outside a bar at seven in the morning, entirely unimpressed by the two of them going past dripping.
49. The scooter parked against a wall, the mirror tape catching the first light, locked off, held into the bridge.

### Bridge — the wall above the harbour

50. *"Sunday there's a plane with my name on a seat"* — locked-off wide: both sitting on a stone wall above the harbour with a gap between them, lights below.
51. *"And a job and a coat and a grey little street"* — her phone face-down on the wall with a boarding pass on it (composited), unlooked at, macro.
52. *"I won't ask you to wait, you won't ask me to stay"* — Kai in close-up, saying nothing, looking at the harbour.
53. *"We're better than a promise we'd break anyway"* — Mahima in close-up, saying it, clear-eyed, no tears.
54. *"So give me the long way back to the harbour tonight"* — both standing, the scooter behind them, the gap between them closing to nothing, medium.
55. *"And a taped-up mirror holding all of that light"* — macro of the taped mirror with the whole harbour in it, the shot the film has been building toward.

### Final chorus — the long way back

56. *"On a Vespa through the old town, holding on to you"* — the archway from shot 11, now at night, taken at speed, mounted.
57. *"Cobblestones like a heartbeat coming through my shoes"* — the laundry street, sheets down, lines bare, mounted.
58. *"Lemon trees and laundry and a bell I finally see"* — the bell tower, shown for the first time in the film, full frame, lit, long lens.
59. *"And a boy who says my name like it belongs to the sea"* — Kai turning his head slightly to speak over his shoulder as they ride, close from the pillion.
60. *"On a Vespa through the old town, nothing left to lose"* — the grandmother's window, shutter closed now, passing, mounted.
61. *"Half a tank of nowhere and a summer to use"* — the piazza empty, the fountain running to nobody, wide, night.
62. *"There's no part of this week that I'd undo"* — a drone pulling up and back until the whole old town and the sea are in one frame.
63. *"On a Vespa through the old town, holding on to you"* — the drone holding as the first blue of morning comes into the sky behind the town.

### Post-chorus — clap and stomp

64. *"Take the corner wide, let the old town blur"* — full sun again: a corner taken wide, the whole street smearing, whip pan, one second.
65. *"Every shutter open, every awning in the sun"* — shutters banging open along one apricot wall, hard cut.
66. *"Take the corner wide, I'm holding on for good"* — an awning cranked out over a doorway, hard cut.
67. *"And the road keeps going, the summer's not done"* — the coast road ahead with nothing on it at all, held two beats longer than the others.

### Outro — the bike chained up

68. *"The mint green bike is chained by the church again"* — morning: a chain going round the scooter frame at a railing by the church, macro.
69. *"My flight goes at seven, and the sea doesn't care"* — the sea from the road, flat and completely indifferent, static wide.
70. *"I'll come back in June when the lemons are heavy"* — a hand on the taped mirror for one second, then gone; her walking away with the backpack, not looking back.
71. *"On a Vespa through the old town, if you're still there"* — final shot: the mint-green scooter alone against the church wall, the bell sounding once, locked off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the tarpaulin coming off, the kick-start, the cut into sun at the
archway, each *"On a Vespa through the old town"*, the jacket going round her
shoulders, the instrumental stomp break, *"a taped-up mirror"*, the bell tower
reveal, and the final bell. At 112 BPM a bar is 2.14 s; choruses cut every two
bars, the post-chorus every bar, and the mounted shots run long and uncut on
purpose.

**The narrow-street mount.** Post the vertical handlebar shot from shots
13–14, walls a hand's width from each mirror, with the hook on screen. Then
the challenge: film your own left-at-the-church, right-at-the-laundry-lines
directions on any bike in any town and cut it to the clap-and-stomp
post-chorus. The grandmother's wave (shots 15–16) is the second shareable
frame.
**Caption:** *"Half a tank of nowhere and a summer to use."*

## 6. Quality-control checklist

- Two looks for her, one for him: the denim jacket moves from his shoulders to hers at shot 31 and stays there until the outro
- One mounted handlebar shot minimum per section; the mount is the film's signature camera
- The taped mirror appears in exactly three places — shot 8, shot 22 and 42, and shots 55 and 70 — and is never cleaned up or replaced
- The bell tower is never visible before shot 58, in any frame, including backgrounds
- The verse-two fountain exchange is single close-ups only; no two-shot until shot 31
- Every daylight shot carries warm apricot bounce off a wall onto both faces; the dawn swim is the only cool-graded shot
- No readable signage, map, menu or boarding pass generated by the model — all composited
- Scooter and pillion geometry checked on every riding shot (OpenPose); no floating feet, no impossible lean
- The last frame is locked off, the bell sounds once, and it holds through the fade with no text
