# Wan 2.2 Shot List — "City Lights Don't Sleep"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
114 BPM a bar is 2.11 s, so most shots run 4–6 s, the choruses cut every two
bars, and the spoken bridge is a single continuous take that ignores the grid
entirely.

## 1. Visual style

A northern English city between three and half past five in the morning.
Brick, iron, wet ground with no rain falling, and **one dominant light source
per frame, a different colour every time**: sodium orange, a green shop sign,
tungsten in a cafe, orange beacons on a gritter, blue on a wall two streets
away. Nothing is graded to look sad — the palette is saturated and calm,
closer to a night-drive photograph than to a breakup video. The camera is
locked off or slow-drifting for the whole first half; it only starts moving
in chorus two, and it stops completely for the bridge.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium through a curtain, deep blue room | Overhead locked off, POV |
| Verse 1 | Sodium, brick red, one green sign, wet ground | Fixed positions, long holds |
| Pre-chorus | One dominant colour per shot, six different | Four-second static portraits |
| Chorus 1 | Neon and sodium at full saturation | Wide, long lens, slow drone |
| Verse 2 | Interior tungsten, condensation, blue outside | Handheld, close, warm |
| Pre-chorus 2 | Sodium losing to grey at the top of frame | Static portraits again |
| Chorus 2 | More saturated, more sources, everything moving | Tracking, bridge drone |
| Instrumental | Full colour, then near black, then fast returns | Slow drift, then hard cuts |
| Bridge | Underlit from a road, pale grey behind | One locked-off continuous take |
| Final chorus | Last neon against first daylight, both at once | Separate frames, drone rise |
| Post-chorus | One light in a dark frame, each time | Hard cuts, no movement |
| Outro | Purple-grey into flat morning, no warm source | Static, one long uncut take |

## 2. Character bible — paste into every prompt

**Mahima** (the whole night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose under the hood of a coat, no makeup, wearing a heavy oversized navy parka over a plain black jumper and jeans, calm alert expression, not tired, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge and outro, hood down)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and pushed back, no makeup, wearing the same navy parka with the hood down, direct settled expression, realistic cinematic photography, consistent identity, natural skin texture

**There is no romantic lead in this film and therefore no Kai, and no ex, so
no faceless figures are needed.** The supporting cast is the night shift, and
every one of them recurs, so each needs a light reference:

- **The cafe woman** — fifties, apron, pours before she is asked
- **The cleaner** — sixties, wheeling a trolley out of an office lobby
- **Two chefs** — twenties, whites, sitting on a step
- **The nurse** — forties, lanyard, walking to a car park
- **The security guard** — thirties, behind lobby glass
- **The gritter driver** and **the baker** — both seen only in pre-chorus two
- **The lad hosing the takeaway front** — twenties, waders, steam

Objects and motifs: the **fox** on the empty road, the **empty tram with
every light on**, the **canal holding the orange**, the **one green window**
in a dark tower, the **radio with a bent aerial**, the **nod** — four seconds,
no dialogue, six times in the film.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All shop signage, tram destination boards, the cafe menu, phone screens and
any street name are composited in the edit.** Generate every plate clean; a
wrong English word on a northern high street is instantly visible and this
film's whole claim is that the place is real.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA, and build a
light reference for each of the seven night workers, since all of them return
in the final chorus. Depth for the skyline and ring-road wides. OpenPose only
where a body moves through frame — most of this film is held. **The fox is
the hardest shot in the video**: generate it as a still with the animal
already standing centre-road and animate only ear and breath movement; do not
ask the model for a walking fox. The streetlights-cutting-out shot in the
outro is a lighting change on a locked plate, done in the edit, not generated.
16:9 first; 9:16 recomposition for the post-chorus single-light cuts.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s. The bridge is one continuous take with two cutaways.

## 4. Scene per lyric line

### Intro — the flat

1. *"Three in the morning and my ceiling knows my face"* — overhead locked off: Mahima on top of the covers fully awake, hands behind her head, entirely calm, deep blue room.
2. *"Not sad, just wired, just awake"* — her point of view of the ceiling: a water stain, a lampshade, a passing headlight crossing it.
3. *"I take my coat off the back of the door"* — her hand taking the navy parka off a hook, macro, sodium through a thin curtain behind.
4. *"And go and see who else is still here"* — the flat door swinging shut on a dark hallway, static, held one beat after it closes.

### Verse 1 — the walk out

5. *"The tram goes past empty with its lights all on"* — a tram passing with every interior light on and nobody inside, fixed position from the far pavement.
6. *"Like it's doing somebody a favour for nothing"* — the tram receding down the line, its lights getting smaller, held long.
7. *"There's a lad hosing down the front of a chip shop"* — a young man in waders hosing a tiled takeaway front, steam coming off the pavement, medium.
8. *"And a fox on the corner that won't move for me"* — a fox standing dead centre of an empty road looking straight at the lens, refusing to move, held four seconds.
9. *"The canal holds the orange of all of Ancoats"* — a canal at night holding a whole district's orange light on a flat unbroken surface, wide, static.
10. *"And the water doesn't shiver, it just carries it"* — macro on the water: no wind, no ripple, the reflection perfectly intact.
11. *"Everybody I know is asleep in a postcode"* — a terrace of dark windows, one after another, slow lateral drift, not a light in any of them.
12. *"And I've never in my life felt less alone"* — Mahima walking into the frame at the end of that terrace, hood up, small, unhurried, tracking from behind.

### Pre-chorus 1 — the nod

13. *"The night shift and the sleepless and the lads just clocking off"* — a cleaner wheeling a trolley out of an office lobby into the street, one white lobby light.
14. *"We nod like a handover, we don't ask a thing"* — two chefs in whites on a step, one green sign above them; each gives a four-second nod.
15. *"There's nothing to explain at half past three"* — a nurse with a lanyard walking to a car park, one column of blue-white light.
16. *"And the ring road hums a note I can sing"* — a security guard behind lobby glass, lit only by his own screens, raising a hand.

### Chorus 1 — the skyline

17. *"City lights don't sleep, and neither do we"* — Mahima on a footbridge with the whole city in front of her, wide, neon and sodium at full saturation.
18. *"Sodium gold and a window still green"* — long-lens compression on a tower with a scatter of lit windows, one of them unmistakably green.
19. *"Not lonely, just running on a different clock"* — her face in profile against the skyline, calm, not wistful, close-up.
20. *"And the whole of the skyline is up with me"* — a slow drone drift across the ring road, headlights streaming in both directions.
21. *"City lights don't sleep, they just turn themselves down"* — a single office floor, fully lit, absolutely empty, seen from across the street.
22. *"They keep one eye open for whoever's around"* — one desk lamp still on inside that floor, long lens, nobody at the desk.
23. *"Put your hand on the glass and count them with me"* — her hand flat against a window with the lit city beyond it, macro, breath on the glass.
24. *"City lights don't sleep, and neither do we"* — the widest frame yet: the whole grid, wet, reflective, deep blue sky above it.

### Verse 2 — the cafe

25. *"There's a caff on Oldham Street that opens at four"* — the cafe door opening from inside, her coming in with cold on her coat, handheld.
26. *"And the woman on the counter knows I take it strong"* — the cafe woman already pouring before anything is said, close on the pour and her face.
27. *"Two builders, a driver, a girl in last night's dress"* — three separate table portraits cut fast: two builders sharing a plate, a taxi driver with his phone face-down, a young woman in last night's dress and somebody else's jacket.
28. *"And a radio that only plays songs nobody wants"* — an old radio with a bent aerial on a shelf above the counter, macro, tungsten warm.
29. *"Nobody here is anybody's problem"* — a wide of the whole room: five people, five tables, nobody looking at anybody, all completely at ease.
30. *"Nobody here is going to ask how I've been"* — Mahima in a corner seat with both hands round a mug, shoulders down, medium.
31. *"We're just the people that the daylight hasn't counted"* — condensation on the cafe window with the blue night pressing on the other side, macro.
32. *"And I like the arithmetic that leaves us in between"* — a wall clock at ten past four, then her face, faintly amused, two cuts.

### Pre-chorus 2 — the handover

33. *"The gritters and the bakers and the ones who cannot stop"* — a gritter lorry with orange beacons going past a shut pub, static, the beacons the only movement.
34. *"We nod like a handover, we don't ask a thing"* — a bakery back door open with flour-lit air spilling out, trays going in, a four-second nod.
35. *"There's nothing to explain when the sky goes grey"* — a window cleaner setting his ladder at half four, the sky greying at the top of frame.
36. *"And the ring road hums a note I can sing"* — the ring road from below, one sustained frame, headlights, the first grey above it.

### Chorus 2 — the city moving

37. *"City lights don't sleep, and neither do we"* — the ring road from a bridge, long-exposure feel, headlights as continuous lines, static.
38. *"Sodium gold and a window still green"* — the green window again, closer, the surrounding tower now half-lit.
39. *"Not lonely, just running on a different clock"* — a car park roof with the whole grid below it, Mahima small at the edge, wide.
40. *"And the whole of the skyline is up with me"* — a drone lifting off the car park roof, faster than the chorus-one move.
41. *"City lights don't sleep, they just turn themselves down"* — the canal again, the reflection now broken by a passing barge, static.
42. *"They keep one eye open for whoever's around"* — a bus depot with rows of buses lit and empty, wide.
43. *"Put your hand on the glass and count them with me"* — her walking a footbridge with the skyline behind her, tracking from the side, the first real camera move of the film.
44. *"City lights don't sleep, and neither do we"* — a hard cut to the fox's empty corner, now with a bin lorry passing through it.

### Instrumental — the guitar, the dark, the return

45. A long slow drift along an empty motorway slip road, sodium lamps passing in rhythm.
46. The green window, closer than ever: a single lamp on a desk with nobody at it, long lens.
47. The filter-down: near black, one blue light crossing a brick wall two streets away, the only dark frame in the film.
48. Five fast returns on the build: the fox, the tram, the canal, the cafe window, the lit empty office floor.
49. A gated-snare hit landing on a wide of the footbridge with Mahima already sitting on the low wall, held into the bridge.

### Bridge — spoken word, one take

50. *"People say get some rest, like rest is somewhere you drive to"* — Mahima sitting on a low wall on a footbridge over the ring road, facing camera, city behind her, talking. Locked off. **This shot does not cut for the whole passage except twice, as noted.**
51. *"I've tried. I've laid there and listened to my own blood"* — the same take continuing; she does not gesture and the camera does not move.
52. *"Out here the city is doing the same thing I am"* — same take; traffic passing beneath her in the lower third of frame.
53. *"Holding a light up because somebody has to"* — same take; the pale grey rising behind her head, the first non-artificial light in the film.
54. *"The offices are empty and the windows are still on"* — same take.
55. *"Which is either a waste or a kindness, and I've decided it's kindness"* — **cutaway one:** the lit empty office floor, held two seconds, then straight back to the take.
56. *"So no, I'm not broken because I'm awake at four"* — **cutaway two:** her own dark bedroom window seen from the street, two seconds, then back.
57. *"I'm just keeping the same hours as everything I love"* — the take, final line, straight to camera, then she looks away at the city and the arpeggio starts.

### Final chorus — everyone, at dawn

58. *"City lights don't sleep, and neither do we"* — the cleaner finishing, taking her gloves off outside the lobby, her own frame.
59. *"Sodium gold and a window still green"* — the two chefs standing up off the step and going back inside, their own frame.
60. *"Not lonely, just running on a different clock"* — the nurse pulling out of the car park, the security guard being relieved at the desk, cut together.
61. *"And the whole of the skyline is up with me"* — the gritter driver and the baker, each finishing, each in their own frame.
62. *"City lights don't sleep, they just turn themselves down"* — the cafe woman turning a chair the right way up as light comes through the condensation.
63. *"They kept one eye open till the morning came round"* — the tram again, the same fixed position as shot 5, now with three people on it.
64. *"Put your hand on the glass, you were counting with me"* — Mahima's hand leaving the footbridge rail; the last neon and the first daylight both in frame.
65. *"City lights don't sleep, and neither do we"* — a drone rising off the footbridge until the whole grid is visible under a pale sky.

### Post-chorus — one light at a time

66. *"Leave it on, leave it on, out to the ring road"* — a single tower window in a dark frame, hard cut on the beat.
67. *"Leave it on, leave it on, till the morning takes over"* — a shop sign, same size in frame, hard cut.
68. *"Somebody out there is watching the same light"* — a bedroom lamp behind a curtain, hard cut.
69. *"Leave it on, leave it on, we'll get there together"* — a phone screen face-up on a windowsill, the least necessary light of the four, held.

### Outro — the streetlights go out

70. *"Half five and the sky turns the colour of a bruise"* — the sky over a terrace going deep purple-grey, static wide, held.
71. *"Then it fades like a dimmer and the streetlights go out"* — a whole street of lamps cutting out at once, in one uncut take, no camera move.
72. *"I'll sleep when the buses are full and the city has company"* — Mahima walking home with the light behind her, hood down, tracking from the front.
73. *"City lights don't sleep, and neither do we"* — final shot: her flat window from the street, the curtain drawing closed, the sodium already off, held as the first full bus crosses the foreground. No text.

## 5. Edit and the challenge

Markers at: the coat off the hook, the fox, each *"city lights don't sleep"*,
the cafe door, the filter-down in the instrumental, the first word of the
spoken bridge, both bridge cutaways, the drone rise, and the streetlights
going out. At 114 BPM a bar is 2.11 s; choruses cut every two bars, the
post-chorus every bar, and the bridge deliberately abandons the grid.

**The streetlights.** Post the uncut shot of a whole street's lamps cutting
out at once (shot 71) with the outro line on screen — it is the rarest image
in the film and nobody films it. Then the challenge: post the view from
wherever you are at three in the morning, cut to the post-chorus chant. One
light, one window, one caption. The fox (shot 8) is the second shareable
frame.
**Caption:** *"I'm not lonely, I'm just on a different clock."*

## 6. Quality-control checklist

- Exactly one dominant light source per frame, and a different colour in each of the six pre-chorus portraits
- The film is never graded to look sad; no desaturation, no cold blue on her face, no crying
- The nod is four seconds, wordless, and appears exactly six times
- All seven night workers keep a consistent face and wardrobe, because all seven return in the final chorus
- The bridge is one locked-off continuous take with exactly two cutaways, on *kindness* and on *awake at four*, and nowhere else
- The camera does not move at all until shot 43; the drift in shots 11 and 45 is the only exception and it is slow
- Ground is wet in every exterior and rain never falls in any frame
- No readable signage, tram board, menu or phone content generated by the model — all composited
- The streetlights in shot 71 go out in one take with no cut, and the last frame holds until the pad decays. No text
