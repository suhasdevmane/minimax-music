# Wan 2.2 Shot List — "The Long Way to You"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
100 BPM a bar is 2.4 s, so verse shots run one bar each through the montage
and the choruses hold two bars per shot.

## 1. Visual style

Ten years of roads, told from inside one car and one hallway. The film has
three registers. The **past** — nine apartments, nine towns — is flat, evenly
lit and slightly cool, no home in any of it, and it cuts fast. The **road** is
golden-hour warm with the sun directly ahead and flare across the windscreen.
The **house at the end** is warm interior practicals against a blue rural
night, and it is the only place in the film where the camera stops moving.

Two rules. The most romantic moment in the video is lit by a grocery-store
parking lot, deliberately, and the almost-life in the bridge is the only
footage graded cleaner than the real one.

| Section | Grade | Camera |
|---|---|---|
| Intro | One warm hallway bulb, everything else dark | Macro on the map, static |
| Verse 1 | Flat, cool, nine different rooms that rhyme | Fast cuts, locked-off |
| Pre-choruses | Low sun ahead, dashboard glow | Long lens down a bend |
| Choruses | Golden hour, flare across the windscreen | Continuous tracking drive |
| Verse 2 | Sodium parking-lot light, unflattering and honest | Static, patient, wide |
| Instrumental | Flat bedroom daylight, then bright driveway | Locked-off, ordinary |
| Bridge | Dusty warm road, the almost-life cooler and cleaner | Passing, never slowing |
| Final chorus | Warm practicals against blue night | Static, the camera finally stops |
| Post-chorus | Plain daylight for the nine, dusk for the tenth | One-second locked-off cuts |
| Outro | Table lamp, then porch light | Macro, then locked-off wide |

## 2. Character bible — paste into every prompt

**Mahima** (the past, nineteen to twenty-six)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and unstyled, no makeup, wearing a plain grey t-shirt and jeans with a flannel shirt tied at the waist, guarded tired expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the parking lot and the road, present)
> Same female protagonist Mahima, woman in her late twenties, expressive dark eyes, oval face, long dark wavy hair pushed back and tucked behind one ear, no makeup, wearing a denim jacket over a white tank top and jeans, arms folded, unimpressed then unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the house)
> Same female protagonist Mahima, woman in her late twenties, expressive dark eyes, oval face, long dark wavy hair loose, wearing an oversized flannel shirt over a t-shirt, barefoot, settled easy expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man in the parking lot)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a canvas work jacket over a t-shirt and jeans, unhurried patient expression, realistic cinematic photography, consistent identity

**The exes are faceless and always have been.** In verse one they are a hand
on a steering wheel, a shoulder in a doorway, a voice with no sound, the back
of a head at a kitchen table. Never a face, never a name, never a locked
identity. The woman on the porch in the bridge's almost-life is framed from
behind and stays that way.

Objects that repeat: the **paper road map** with pins and thread — on a wall,
lit from behind, lifted down, flat on a table, one new pin — the **cardboard
box** that gets carried up three staircases and is finally opened and thrown
out, the **jumper cables**, the **porch light**, the **screen door that will
not latch**, the **nail hole**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every road sign, exit sign, town name, coffee-cup order, job lanyard and the
place names printed on the map are composited in the edit.** Generate the map
as a blank paper texture with pins and thread and lay the cartography over it;
generate all signage as blank backlit shapes. A road video is nothing but
text and the model can render none of it — this and the map are the two
highest-risk assets in the film.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai in his one look with IP-Adapter or a
character LoRA each. The exes need no reference at all — build them as crops
and shoulders and keep them that way.

Keyframes first. The nine-apartment montage is the technical problem here:
generate one kitchen plate and re-dress it nine ways rather than generating
nine kitchens, or the model will drift the architecture and the montage will
stop rhyming. Depth for the hallway and the car interiors; OpenPose only for
the jumper-cable shots, where hands and cables together will otherwise fuse.
16:9 first; 9:16 recomposition for the map macros and the parking-lot meeting.

Animate small and let the car do the moving: thread pulling taut, a pin going
in, a screen door swinging and not latching, moths at a porch light, a hood
being lowered. Driving plates are far more reliable generated as a moving
background with the interior shot separately and composited.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–5 s.

## 4. Scene per lyric line

### Intro — the map

1. *"There's a map in the hallway with a pin in every town,"* — a large paper road map pinned flat to a narrow hallway wall, coloured pins and thread between them, one warm bulb above it, static.
2. *"Nine of them for cities and the rest for someone's name."* — macro along the thread, pin to pin, the cartography composited, shallow focus.
3. *"I used to see that thread and call it wasted mileage,"* — her hand entering frame and tracing one thread slowly across the whole map, close-up.
4. *"Now I trace it with my finger and it ends up here."* — her fingertip stopping on the last pin, held, then her face out of focus behind it.

### Verse 1 — nine towns, one box

5. *"At nineteen I moved for a boy with a good car,"* — a car packed to the roof pulling away from a curb at dusk, a faceless hand on the wheel, locked-off, flat light.
6. *"Broke the lease in a season, drove back home in the dark."* — the same car on a night road going the other way, one occupant, dashboard glow, static from the back seat.
7. *"At twenty-three I took the job because he took the job,"* — a job lanyard on a hook by a front door (blank, composited), the door clearly hated, close-up.
8. *"And I learned a whole new city that I never learned to like."* — Mahima at a kitchen sink in an apartment with nothing on the walls, wide, flat.
9. *"There was one who never once got my coffee order right,"* — a takeaway cup with a wrong order written on the side (composited), set down in front of her, macro.
10. *"There was one who called me difficult and meant it as a fact."* — a doorway argument seen from a hallway, no sound, no faces, only a shoulder and her back, static.
11. *"I kept a box of somebody in the back of every closet,"* — a closet door opening on a taped cardboard box shoved to the back, torch-lit, close.
12. *"Hauled it up three staircases and I never once unpacked."* — the same box carried up a narrow staircase, three quick match cuts in three different stairwells, the box identical each time.

### Pre-chorus 1 — asking the road

13. *"And I asked the road why it kept on bending,"* — a long lens straight down a two-lane road that bends out of sight, last light, locked-off.
14. *"Why the exits showed up early or too late."* — blank exit signs going past a passenger window, blurred (all signage composited), handheld.
15. *"Turns out the road was never confused,"* — Mahima at the wheel, one hand, no radio, no urgency, close-up, dashboard glow starting to matter.
16. *"The road was taking its time."* — the road ahead through the windscreen, the sun going down directly in line with it, wide.

### Chorus 1 — the reframe

17. *"I took the long way, but the long way led to you,"* — a continuous tracking drive alongside the car on a wide open road, golden hour, flare across the frame.
18. *"Every wrong turn was a road I had to lose."* — one of the towns from verse one passing on the left, held exactly one line, seen from the moving car.
19. *"Every town I couldn't stay in, every name I couldn't keep,"* — another town passing on the right, matched framing, matched speed.
20. *"Was a mile of the highway running down to your street."* — a long straight of empty highway from a high angle, the car small in it, drone or crane.
21. *"So here's to every detour, every year I called a loss,"* — the map again, but from behind the wall: pins pushed through, thread taut, light coming through the pinholes, macro.
22. *"I took the long way, but the long way led to you."* — back to the drive, her face lit by the low sun, one hand out of the window, close-up.

### Verse 2 — a Wednesday

23. *"And you were not a lightning strike, you were a Wednesday,"* — a grocery-store parking lot after dark, half empty, sodium light, static wide.
24. *"A dead battery, a parking lot, a quarter after eight."* — a hood up, Mahima standing beside it with her arms folded, medium, unflattering overhead light.
25. *"You had jumper cables and you knew how not to hurry,"* — a pickup pulling in beside her without ceremony, then jumper cables clipped on in close-up.
26. *"And you asked me twice about the thing I said the first time."* — the two of them waiting by the running engine, talking, Kai asking something a second time and waiting, medium two-shot.
27. *"I had an apartment set up not to need a second key."* — a single key on a hook by a door, and one empty hook beside it, insert, flat apartment light.
28. *"But you made coffee in the morning like you'd made it here for years,"* — a small kitchen the next morning, him finding the mugs without asking, her watching from the doorway, warm, handheld.
29. *"And the map on the wall went quiet for the first time."* — the hallway map, unlit, nobody looking at it, static, held two seconds longer than it needs.

### Pre-chorus 2 — the same road, different driver

30. *"So I stopped asking the road where it was going,"* — the same long-lens bend from shot 13, now in morning light with two people in the car.
31. *"Stopped counting all the mile markers behind."* — her feet up on the dash, mile markers going past and nobody looking at them, insert.
32. *"Turns out the road was never lost,"* — the rear-view mirror with the road emptying out behind, macro.
33. *"The road was bringing me home."* — the windscreen ahead, the light now coming from behind the car, wide.

### Chorus 2 — arriving

34. *"I took the long way, but the long way led to you,"* — the car leaving the highway for a county road, tracking from outside, late afternoon dust in the light.
35. *"Every wrong turn was a road I had to lose."* — the county road becoming a gravel road, the turn on the line, from inside over her shoulder.
36. *"Every town I couldn't stay in, every name I couldn't keep,"* — dust rising behind the car on gravel, seen from behind, backlit.
37. *"Was a mile of the highway running down to your street."* — the gravel road becoming a driveway, the turn on the line.
38. *"So here's to every detour, every year I called a loss,"* — a small house with a porch coming into frame at the end of the driveway, seen through a dusty windscreen.
39. *"I took the long way, but the long way led to you."* — the car stopping, the engine off, the dust settling around it, locked-off, held.

### Instrumental — the box

40. The taped cardboard box from verse one on a bedroom floor, finally being cut open, flat daylight, locked-off.
41. What is inside: photographs face down, a hoodie, a set of keys to a door that no longer exists, macro on each.
42. The four-bar drop: the box taped shut again, one quiet unremarkable shot, no music but brushes and acoustic.
43. Her carrying it down a driveway in bright daylight and setting it beside a trash can, wide, ordinary.
44. The empty patch of closet floor where it lived, static, and a door closing on it.

### Bridge — the exit she never took

45. *"There's a sign I passed a hundred times and never took,"* — a blank highway exit sign at dusk (composited), seen from a car that does not slow down, passing.
46. *"Somewhere past a town with a diner and a church."* — a small town glimpsed past the exit: a diner, a church, a water tower, all in one wide pass.
47. *"If I'd turned there at twenty I'd be somebody's almost,"* — a two-second insert of the almost-life: a woman on a porch in that town, framed from behind, never a face, graded cooler and cleaner than everything around it.
48. *"With a life I'd have to like instead of one I get to love."* — the almost-life continuing: a tidy kitchen, a set table, absolutely nothing wrong with it, static.
49. *"So I'm grateful for the bad ones, I'm grateful for the slow,"* — hard cut back to the real road, warm and dusty, her at the wheel, close-up.
50. *"I'm grateful for the girl who kept on driving in the dark."* — a night-driving shot from the back seat, only her silhouette and the road, held to the end of the line.

### Final chorus — the house

51. *"I took the long way, but the long way led to you,"* — a porch light on at midnight with moths at it, static, the brightest thing in frame.
52. *"Every wrong turn was a road I had to lose."* — a screen door swinging and not latching, twice, and nobody getting up to fix it, locked-off.
53. *"Now the porch light's on at midnight and the screen door doesn't latch,"* — the two of them inside seen through the screen from the porch, warm practicals, blue night in the foreground.
54. *"And the map comes down tomorrow, there's a nail hole where it was."* — the hallway map being lifted off the wall in one piece, medium.
55. *"So here's to every detour, every year I called a loss,"* — the bare patch of paint behind it, and a single nail hole, her thumb going over it, macro.
56. *"I took the long way, but the long way led to you."* — the empty hallway wall with the bulb still on above nothing, wide, held.

### Post-chorus — the nine towns, given back

57. *"The long way, the long way,"* — three one-second cuts: three of the verse-one towns, now in plain daylight and looking ordinary rather than sad.
58. *"Nine wrong towns and a right one, all the same."* — three more one-second cuts, matched, same treatment.
59. *"The long way, the long way,"* — the last three towns, one second each, the montage deliberately unremarkable.
60. *"I would drive every mile of it again."* — the tenth cut, held four times as long: the driveway, the porch, the light on, warm dusk.

### Outro — one new pin

61. *"There's a map in the hallway with a pin in every town,"* — the same map now flat on a kitchen table rather than a wall, being smoothed out under a table lamp, wide.
62. *"And a pin in this one, and this one's staying in."* — one new pin pushed into it, extreme close-up, the sound of it going through paper.
63. *"I used to call it wasted, all that thread across the country,"* — the whole map from directly above, every pin and thread visible at once, static.
64. *"Now I call it the long way, and the long way led to you."* — final shot: the two of them on the porch steps at night, the map rolled up beside them, the screen door open behind, locked-off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first acoustic figure, the box's first staircase (shot 12),
each *"the long way led to you"*, the parking lot (shot 23), the box being
thrown out (shot 43), the almost-life insert (shots 47–48), the modulation
into shot 51, the map coming off the wall (shot 54), the new pin (shot 62),
and the last frame. At 100 BPM a bar is 2.4 s; the verse-one montage cuts
every bar, the post-chorus cuts every second, and the choruses hold two bars.

**The pin-map challenge.** Post the vertical cut of shots 1–4 and 54–55 — the
map traced, then lifted off the wall with the nail hole behind it — under
*"the map comes down tomorrow"* and invite people to film their own map,
corkboard or photo wall of everywhere they lived and everyone they moved for.
The parking-lot meeting (shots 23–26) is the second shareable cut and the one
that will get quoted, precisely because nothing happens in it.

## 6. Quality-control checklist

- Three Mahima looks in the right sections: flannel-at-the-waist only in verse one, denim jacket for the parking lot and the road, oversized flannel and bare feet only at the house
- No ex ever has a face, in any shot; the almost-life woman is framed from behind and stays there
- The nine-apartment montage is one re-dressed plate, not nine generated rooms — check the architecture matches across all cuts
- All signage, the coffee-cup order, the lanyard and the map's cartography are composited; no model-generated lettering anywhere
- The parking-lot scene stays under sodium light and gets no warm key and no music swell
- The almost-life insert is the only footage in the film graded cooler and cleaner than the present
- The box: closed in shot 11, carried in shot 12, opened in shot 40, thrown out in shot 43, and never seen again
- Hands checked on every jumper-cable and pin close-up
- The camera stops moving from shot 51 onward and does not move again; the last shot is locked-off and holds until the audio fades
