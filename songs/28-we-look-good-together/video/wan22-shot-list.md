# Wan 2.2 Shot List — "We Look Good Together"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
116 BPM a bar is 2.07 s, so most shots run 2–4 s and the choruses cut on the
bar with every strut step landing on a downbeat.

## 1. Visual style

A color-blocked city at gold hour, then a gelled party, then one flat
overhead kitchen light. **Reflection is the motif**: shop glass, a bus
window, a car door, a puddle, a mirror by the front door, a phone screen.
Almost every chorus shot contains the two of them twice. The camera moves
with them and never above them — tracking, backwards dollies, ground-level
feet — and the only locked-off framings in the film are the crosswalk plate
used for the outfit transitions and the very last shot.

The bridge deliberately breaks every rule of the grade: no gold, no neon, no
gels, one flat overhead kitchen light, and it is the best they look.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm interior lamp, hard sun in the doorway | Static mirror frame, inserts |
| Verse 1 | Hard low sun through apartment windows | Handheld, close |
| Pre-choruses | Long shadows down the crosswalk | Ground-level feet, sideways glances |
| Chorus 1 | Full gold hour, city color-blocked behind | Backwards tracking at waist height |
| Verse 2 | Saturated party gels, one hard key | Slow motion, deadpan singles |
| Chorus 2 | Party gels cutting hard to wet neon | Circling, hard match cut |
| Instrumental | Gold, neon, then one overcast frame | Locked-off crosswalk plate |
| Bridge | One flat overhead kitchen light, no gels | Static, close, unglamorous |
| Final chorus | Rain reflections, flat sun, airport fluorescents, gold | Tracking, wider each time |
| Post-chorus | Last gold, everything reflective | Fast reflection cuts |
| Outro | One warm hallway lamp, dark around it | Static, then held close |

## 2. Character bible — paste into every prompt

**Mahima** (the going-out look, intro through the post-chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair blown out and moving, bold red lip and sharp liner, wearing a tailored scarlet blazer over a black slip dress and gold hoops, amused confident expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the bridge and outro, Tuesday)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair scraped into a messy knot, no makeup, wearing a faded oversized sweatshirt with flour on one sleeve, flour dusted in her hair, unguarded soft expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the going-out look)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a scarlet-lined charcoal suit jacket over a black tee, gold chain, white trainers, dry deadpan expression with a smile behind it, realistic cinematic photography, consistent identity

**Kai** (the bridge and outro, Tuesday)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a plain gray t-shirt and track pants, bare feet, quietly delighted expression, realistic cinematic photography, consistent identity

**The doorman** — a man in his forties in a long coat, face allowed, warm, in on the joke by the end of his shot.

**Somebody's ex** — faceless. Seen only as a shoulder, a turned back, and a hand setting a glass down too hard.

**The imitators at the bar** — a group of three, faces out of focus or cropped, never mocked by the camera; the joke is that they are trying, not that they fail.

Objects: the **scarlet and charcoal color pairing** (worn by both, every
going-out shot), the **mirror by the front door**, the **corner shop window**,
the **two coffees with one straw**, the **good coat on the chair**, the
**flour**, the **photo that never gets posted**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All shop signage, the crosswalk countdown, the phone screens and the final
photo are composited in the edit.** The last shot in particular is a
composited image on a phone screen and must not be model-generated text or UI.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai in both looks with IP-Adapter or a character
LoRA each — four references total, and the Tuesday looks must still read as
the same two people, which is the single hardest continuity job in this video.
**OpenPose is essential for the strut**: the walk, the step off the curb, the
spin in verse one and the dance circle in chorus two all need pose references
or the model will invent gait. Depth for the street wides so the crosswalk
geometry holds across the three outfit-transition plates.

Reflections are the one thing to plan rather than generate: shoot or build the
reflective surface plate first, then composite the pair into the glass, rather
than asking the model for a person and a matching reflection in one frame. It
gets one of the two wrong almost every time.

16:9 first; 9:16 recomposition for the crosswalk transition cut, which is the
main vertical deliverable.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s; the instrumental transition plates are 3 s each.

## 4. Scene per lyric line

### Intro — the last ten seconds inside

1. *"Mirror by the door and the keys in my hand"* — a full-length mirror by the front door with both of them in it, each checking the other rather than themselves, static.
2. *"Green light on the corner, whole block understands."* — a crosswalk signal going green at the end of the block, seen from the open doorway, long lens, gold beyond.
3. *"Turn the collar up, do the thing with the shades"* — his collar turning up in one move, then her sunglasses going on, two inserts cut on the beat.
4. *"Baby, look at what we made."* — both of them in the mirror, still, looking at the reflection and not at each other, held one beat past comfortable.

### Verse 1 — her, getting dressed

5. *"I picked the jacket and you picked the shoes"* — a bed covered in rejected clothes, one scarlet jacket held up over it, handheld.
6. *"We argued for an hour and the argument was the truth."* — her holding two jackets against his chest in turn, him saying nothing, medium two-shot.
7. *"You came out the bedroom doing that stupid little spin"* — Kai executing an entirely unnecessary spin in a doorway, full body, one take.
8. *"And I said, absolutely not, then I let you win."* — her face, flat, unimpressed, then breaking into a laugh she tries to stop, close-up.
9. *"There's a window on the corner where the light hits right"* — a corner shop front used as a mirror, gold bouncing off the glass, both reflected in it, static.
10. *"And we take the same photo there every Friday night."* — a phone held up in the same framing they use every week, the screen composited, over-the-shoulder.
11. *"Two coffees, one straw, and a plan we didn't make"* — two coffees with one straw between them on a low wall, both hands in frame, macro.
12. *"And the afternoon's a scene we didn't have to stage."* — a wide of the two of them sitting on that wall doing nothing at all, gold hour, people passing.

### Pre-chorus 1 — counting in

13. *"Count it in, one, two, hit the corner clean"* — two pairs of feet stopping at a curb in step, ground level, long shadows.
14. *"Bass in the chest and the whole street lean."* — a crosswalk countdown ticking (composited), the street beyond it color-blocked, static.
15. *"Are you ready, are you ready, don't break stride"* — both of them looking at each other sideways without turning their heads, tight two-shot.
16. *"Chin up, shoulders back, and glide."* — the first step off the curb landing exactly on the downbeat, ground level, hard shadow.

### Chorus 1 — the strut

17. *"Baby, we look good together, and we know it"* — tracking backwards ahead of both of them at waist height, the block passing behind, everyone else slightly slower.
18. *"Every window in the city is a stage and we show it."* — their reflection running along a row of shop windows, the camera moving with it, no faces in the real plane.
19. *"Green light, gold hour, and the whole block slows"* — a bus passing and both of them appearing in its glass for one frame, then gone, static.
20. *"We didn't come to the party, we're the reason it goes."* — a stranger on the sidewalk visibly turning around after they pass, medium, real time.
21. *"Baby, we look good together, say it with your chest"* — Mahima alone in the tracking shot, chin up, delivering the line straight to the lens for two seconds.
22. *"Two of us on one sidewalk and the sidewalk is a set."* — Kai alone in the matching framing, deadpan, not smiling until the last word.
23. *"You can look, you can love it, you can put it on your screen"* — a phone filming them from the crowd, the screen showing them, both reflections and both realities in one frame.
24. *"Baby, we look good together, and we know it."* — a wide of the whole block at gold hour with the two of them dead centre and laughing between lines.

### Verse 2 — him, the party

25. *"Doorman did a double take and held the door too long"* — a doorman's face doing a small double take, close, warm, then the door held open two beats past necessary.
26. *"Somebody's ex went quiet in the middle of a song."* — a faceless figure at the bar setting a glass down too hard, shoulder and hand only, party gels.
27. *"You walked in like the floor was on your payroll"* — Mahima crossing the room in slow motion, one hard key on her, the crowd blurred and slower.
28. *"And I held both the drinks and let the whole room go slow."* — Kai standing completely still holding two drinks, watching her, everything else in slow motion around him.
29. *"They can copy the fit, they can borrow the pose"* — a group of three at the bar looking at a phone, then looking up, faces out of focus.
30. *"Take it frame for frame off a picture that we posted."* — the same three trying the corner-window pose badly, held just long enough to be funny and not long enough to be cruel.
31. *"But they can't get the part where you laugh at my joke"* — Kai saying something inaudible close to her ear, medium, party light.
32. *"The one that isn't funny and you laugh at it the most."* — her laughing far harder than the joke deserves, head back, the only unposed frame of the party, close.

### Pre-chorus 2 — the second count

33. *"Count it in, one, two, hit the corner clean"* — reuse shot 13's ground-level framing on a polished party floor, other shoes around them.
34. *"Bass in the chest and the whole street lean."* — a mirror ball throwing spots across both faces, static, no movement but the light.
35. *"Are you ready, are you ready, don't break stride"* — both counting each other in with a look and nothing else, tight two-shot.
36. *"Chin up, shoulders back, and glide."* — the first step onto the dance floor landing on the downbeat, ground level.

### Chorus 2 — the party version

37. *"Baby, we look good together, and we know it"* — the two of them dancing in a small clear circle the room makes without being asked, circling handheld.
38. *"Every window in the city is a stage and we show it."* — the circle seen from above through a mirrored ceiling panel, both of them and both reflections.
39. *"Green light, gold hour, and the whole block slows"* — six phones up around the circle, screens composited, all showing the same two people.
40. *"We didn't come to the party, we're the reason it goes."* — the whole room moving with them by the end of the line, wide.
41. *"Baby, we look good together, say it with your chest"* — Mahima's single from shot 21 repeated under party gels, harder light, same delivery.
42. *"Two of us on one sidewalk and the sidewalk is a set."* — Kai's matching single, gels, still deadpan.
43. *"You can look, you can love it, you can put it on your screen"* — hard match cut from the party floor to the same two steps on the crosswalk at night, neon replacing gold.
44. *"Baby, we look good together, and we know it."* — the two of them mid-stride on wet neon street, reflections under their feet, tracking.

### Instrumental — the walk as a set piece

45. Locked-off wide of the empty crosswalk over the slap-bass break, nobody in it, three seconds.
46. The same locked-off plate: both of them crossing it in the scarlet-and-charcoal fits, gold hour.
47. The same plate again: both crossing in a second pairing of outfits, night neon.
48. The same plate a third time: both crossing in a third pairing, flat overcast daylight.
49. The corner shop window from directly opposite, their reflections arriving and leaving the frame, nobody else in it.
50. Four fast reflection cuts on the brass shout chorus — glass, a car door, a puddle, a phone screen — half a second each.

### Bridge — Tuesday, no filter

51. *"Take the gold off, hang the good coat on the chair"* — gold hoops and a chain dropped into a dish, macro; then the good coat going over the back of a chair and staying there.
52. *"Tuesday, no filter, and there's flour in your hair."* — Mahima (Tuesday look) at a kitchen counter with flour on it, flour in her hair, not knowing, flat overhead light.
53. *"Nobody's watching and there's nothing to prove"* — a wide of the kitchen with both of them in old clothes, no styling, the worst light in the video, static.
54. *"And I still catch myself just looking at you."* — Kai (Tuesday look) leaning in a doorway watching her and saying nothing, medium, held.
55. *"That's when we look the best, with the lights off the floor"* — the two of them sitting on the kitchen floor with their backs to the cabinets, one plate between them.
56. *"Don't tell the internet, but I like this version more."* — her looking up at him and him shrugging, both faces fully lit and completely unglamorous, close two-shot.

### Final chorus — four unglamorous places

57. *"Baby, we look good together, and we know it"* — the crosswalk in the rain under one umbrella, both still in step, wet reflections everywhere.
58. *"Every window in the city is a stage and we show it."* — the rain version of the shop-window reflection, distorted by water on the glass.
59. *"Green light, gold hour, and the whole block slows"* — the same crosswalk in flat unflattering midday sun, no shadows, both unbothered.
60. *"We didn't come to the party, we're the reason it goes."* — a bus shelter, both squashed under it out of the rain, still posing, medium.
61. *"Baby, we look good together, in the rain, in the sun"* — an airport line under fluorescents, both exhausted, bags at their feet, still finding the light.
62. *"In the line at the airport at a quarter past one."* — a departures board out of focus behind them (composited), her asleep on his shoulder standing up.
63. *"You can look, you can love it, you can put it on your screen"* — hard cut back to gold: the last full strut down the block, brass at its widest, everyone else out of focus.
64. *"Baby, we look good together, and we know it."* — the widest frame in the video, the whole block, gold, both of them dead centre.

### Post-chorus — the chant

65. *"Look at us, look at us"* — reflection in shop glass, half a second; a car window, half a second, cut on the beat.
66. *"Every shop window agrees with us."* — a puddle, a shop mirror, a phone screen, three fast cuts.
67. *"Look at us, look at us"* — the two of them walking away from camera down the block, still in step, long lens.
68. *"Nobody had to tell us, we just knew."* — their shadows on the sidewalk, long and side by side, ground level, the sun almost gone.

### Outro — the door closes on the performance

69. *"Turn the lock, kick the shoes down the hall"* — a lock turning from inside, then two pairs of good shoes kicked down a hallway, one after the other.
70. *"Take the picture, don't post it, this one isn't theirs."* — both on the sofa in Tuesday clothes, a phone held out at arm's length, the flash of the shutter.
71. *"Baby, we look good together,"* — the phone screen showing the photo they just took, both of them in it in old clothes, laughing, macro on the screen.
72. *"And we know it."* — final shot: a thumb hovering over the share button and not pressing it, the screen going dark, the room going with it. Locked-off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the mirror frame in shot 4, the first step off the curb, each
*"we look good together"*, the party match cut at shot 43, the three
crosswalk transition plates, the flour, and the thumb not pressing. The final two lines get their own shots, 71 and 72. At 116
BPM a bar is 2.07 s; every strut step in the choruses lands on a downbeat and
the post-chorus reflections cut on the eighth.

**The crosswalk transition.** Shots 45–48 are the same locked-off plate with
three different outfit pairings crossing it — the outfit-transition format
built into the video rather than added to it. Post it vertically with the
chant over it. The second shareable cut is the bridge, shots 51–56, captioned
*"don't tell the internet, but I like this version more"* — the getting-ready
video's opposite, and the reason the song is not just a flex.

## 6. Quality-control checklist

- Scarlet and charcoal in every going-out frame for both leads; the Tuesday looks share no color with them at all
- The two Tuesday looks must still read as the same two people — check identity on every bridge shot before approving
- Almost every chorus frame contains the pair twice: once real, once reflected. Reflections are composited plates, never generated in the same pass
- The ex is faceless throughout; the imitators are out of focus and the camera never mocks them
- The bridge is the only section with no gold, no neon and no gels, and it is lit flat from overhead on purpose
- OpenPose on the strut, the spin, the step off the curb and the dance circle
- The three crosswalk transition plates are identical framing, focal length and camera height
- The last shot is a composited phone screen going dark, locked off, holding through the fade
