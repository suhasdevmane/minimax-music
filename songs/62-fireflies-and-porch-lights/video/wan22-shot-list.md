# Wan 2.2 Shot List — "Fireflies and Porch Lights"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. Timestamps come from the rendered WAV; cut
on the sung line. At 94 BPM a bar is 2.55 s, so verse shots run 3–5 s and the
choruses cut roughly on the bar.

## 1. Visual style

Two porches, one lawn, three summers. The whole video is built out of **one
light source at a time**: a tungsten porch bulb, a bug light, a kitchen window
through a screen, headlights on a packed truck, and finally a second porch
that is hers. Fireflies are always practical points of light in frame, never
a particle effect — generate them as small warm bokeh and add motion in the
edit. The matched crane off the lawn recurs three times with identical framing
and grade so the audience notices what changed rather than how it was shot.
Handheld only for the kids running; everything with an adult in it is on
sticks.

| Section | Grade | Camera |
|---|---|---|
| Intro | Blue dusk lawn, one warm bulb | Macro, then locked-off wide |
| Verse 1 | Deep blue with a warm halo behind | Handheld, low, kid height |
| Pre-chorus 1 | Warm interior spill through screen mesh | Static through the mesh |
| Choruses | Warmest and widest, lawn lit as well as porch | Matched crane, slow rise |
| Verse 2 | Same bulb, cold lawn, distant lightning | Sticks, still, wider spacing |
| Pre-chorus 2 | Porch bulb only, hard falloff to black | Static, mirrors pre-chorus 1 |
| Instrumental | Bulb alone, no fill, black beyond the boards | Slow, observational |
| Bridge | Softer, more sources, present-day warmth | Locked-off from the rail |
| Final chorus | Fullest grade, lawn and sky lit together | Matched crane, third pass |
| Post-chorus | Sprinkler mist, hard backlight, sparkle | Handheld, low, fast |
| Outro | One bulb in a black frame | Held wide |

## 2. Character bible — paste into every prompt

**Mahima** (fourteen, the first summer)
> Same female protagonist Mahima, girl of about fourteen, expressive dark eyes, oval face, long dark wavy hair in a loose ponytail with strands stuck to her neck, no makeup, wearing a faded yellow tank top and denim cutoffs, barefoot with grass on her shins, open delighted expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (seventeen, the last August)
> Same female protagonist Mahima, young woman of about seventeen, expressive dark eyes, oval face, long dark wavy hair down, light natural makeup, wearing an oversized plaid overshirt over a white tank and shorts, guarded quiet expression, realistic cinematic photography, consistent identity

**Mahima** (present day, her own porch)
> Same female protagonist Mahima, woman in her late twenties, expressive dark eyes, oval face, long dark wavy hair tied up loosely, no makeup, wearing a soft grey sweatshirt and linen trousers, bare feet on painted boards, settled unhurried expression, realistic cinematic photography, consistent identity

**Kai** — the boy from two houses down, the one male lead with a face.
> Same male character Kai, boy of about fourteen and later seventeen, close-cropped dark hair, wearing a plain white t-shirt and basketball shorts, later a work shirt and jeans, easy grinning expression, realistic cinematic photography, consistent identity

**Her mother** — a silhouette at the kitchen sink seen through screen mesh only, never a clear face, never outside the house.

**The two kids** (bridge and post-chorus) — a boy and a girl of about nine,
new faces, never resembling the leads. They carry the jar in the present day.

Objects that recur: the **mason jar** with six nail-punched holes, the
**screen-door hinge** thick with paint, the **bug light**, the **low
chain-link fence**, and the **second, working hinge** on her own porch.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All house numbers, street signs, truck lettering and any label on the jar
are composited or removed in the edit.** Generate surfaces blank — the model
cannot render legible text, and a nonsense street sign breaks the illusion
that this is somebody's real childhood.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three ages with a character LoRA per age plus IP-Adapter
for the eyes; Kai gets one LoRA covering both ages. **The firefly work is the
hard part** — generate plates with the lawn empty and add fireflies as tracked
warm bokeh in the edit, because the model will otherwise produce floating
white blobs that flicker inconsistently between frames. OpenPose for the
running and the fence vault. Depth for the porch interiors, which are shallow
and read flat without it. 16:9 first; 9:16 for the jar release and the
sprinkler run. Animate small: a hinge spring letting go, a moth at a bulb, a
lid turning back, grass moving under a sprinkler.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the porch at dusk

1. *"Screen door banging on a hinge that never got fixed"* — macro on a paint-thick screen-door hinge, the spring stretching and letting go, the door slapping twice and settling, static.
2. *"Cut grass and citronella in the air"* — macro on a citronella candle on the rail, smoke curling through the porch bulb's beam, a mown lawn out of focus behind it.
3. *"Somebody's sprinkler ticking two yards over"* — a long lens down the row of back yards, one sprinkler arm ticking across in silhouette, blue dusk.
4. *"And the light comes on before we know it's there"* — locked-off wide of the porch from the lawn, two chairs, nobody in frame, and the bulb flicking on by itself as the sky drops a stop.

### Verse 1 — fourteen

5. *"We had a jar with a lid my dad punched with a nail"* — macro on a nail going through a metal lid from underneath, the burr of the hole, a hand steadying it.
6. *"Six holes and a blade of grass for a bed"* — the jar held up, six punched holes throwing six dots of light on a cheek, a blade of grass curled inside.
7. *"You'd come across the fence at half past eight"* — Kai swinging a leg over a low chain-link fence and landing badly, laughing, handheld at kid height.
8. *"With grass stains and whatever your mother said"* — close-up of a green-smeared knee and a hand brushing at it, his shrug in the background out of focus.
9. *"We were bad at catching, better at the chasing"* — the two of them running the lawn barefoot at half speed, arms out, hands closing on nothing, tracking alongside.
10. *"Barefoot on a lawn that hadn't cooled off yet"* — low macro on bare feet in warm grass, the blades springing back, dust rising in the porch light.
11. *"My knees in the dirt and your hand in the dark"* — Mahima kneeling in a flower bed with her hands cupped, his hand entering frame to cup them from the other side.
12. *"Two kids and a hundred nights we hadn't spent"* — a wide from the far end of the lawn, both of them small, both porch lights on behind them, sky still blue at the top.

### Pre-chorus 1 — ten more minutes

13. *"Mama's voice through the screen saying, ten more minutes"* — shot from outside through the mesh: a mother's silhouette at the kitchen sink, distorted, calling without turning round.
14. *"Ten more minutes, and then ten more again"* — the same frame twice with the light behind her dimming between takes, a hard cut on the repeat.
15. *"Porch light doing that thing where it hums"* — macro on the bug light, moths against the glass, the filament flickering, sound-led.
16. *"And neither of us ever going in"* — two pairs of bare feet on the porch boards, not moving toward the door, the screen door out of focus behind them.

### Chorus 1 — the whole summer at once

17. *"Fireflies and porch lights, you and me and July"* — the matched crane: a slow rise off the grass to a wide of both houses, both porch lights on, the fence between them.
18. *"Two houses and a fence and a whole lot of sky"* — the crane completes, holding on the sky above the two roofs, blue at the top of frame, the lawn small at the bottom.
19. *"We caught them in a jar and we let them go at nine"* — the jar on the grass between them, both faces lit from inside it, close two-shot.
20. *"Because a light that small is only borrowed for a time"* — the lid turned back and everything inside going up at once past two faces, shot at high frame rate.
21. *"I can still hear the hinge, I can still smell the grass"* — hard cut to the hinge from shot 1, then to grass in a fist, two macro shots on the beat.
22. *"I can still feel fourteen when the summer gets like this"* — Mahima at fourteen flat on her back on the lawn, arms out, looking straight up, overhead.
23. *"Nothing ever happened and it changed my whole life"* — the two of them side by side on the porch steps, a full foot of space between them, neither looking over, static wide.
24. *"Fireflies and porch lights, you and me and July"* — a wide of the lawn with the fireflies at their thickest, both kids running through them, the porch behind, tracking.

### Verse 2 — the last August

25. *"Last August you were taller and you drove"* — Kai at seventeen leaning on a truck door at the curb, keys in hand, taller in the same frame composition as shot 7.
26. *"And I had a summer job and plans for the fall"* — Mahima at seventeen pulling a name badge off a work shirt on the porch steps and dropping it beside her.
27. *"You knocked on the screen at half past eight anyway"* — a knuckle on the screen door in close-up, the same hinge, the same double slap, matched to shot 1.
28. *"And we sat on the steps and hardly talked at all"* — the same two-shot as shot 23, same spacing, three years older, both looking at the lawn.
29. *"Then you kissed me by the gate like it was nothing"* — at the gate, a kiss held for under two seconds, shot wide from the porch so it reads small.
30. *"And your dad's truck was already packed to leave"* — the truck at the curb with a tarp roped over the bed, engine running, exhaust in the headlights.
31. *"I let the last one out of the jar that night"* — the jar opened at arm's length, one point of light leaving it, nothing else inside, close-up on the glass.
32. *"And I stood in the yard till there was nothing to see"* — a long static wide of her alone mid-lawn with the empty jar hanging from one hand, held five seconds, distant lightning once.

### Pre-chorus 2 — nobody counting

33. *"No voice through the screen now, nobody counting"* — the kitchen window from outside, dark, no silhouette at the sink, matched exactly to shot 13.
34. *"Ten more minutes and the whole house still"* — the interior beyond the mesh, one chair pushed in, nothing moving, static.
35. *"Porch light doing that thing where it hums"* — the bug light again in macro, one moth, then none, matched to shot 15.
36. *"And neither of us saying what we feel"* — two pairs of feet on the boards, one pair in driving shoes now, matched to shot 16.

### Chorus 2 — the missing light

37. *"Fireflies and porch lights, you and me and July"* — the matched crane a second time, identical framing and grade, and one of the two porch lights is off.
38. *"Two houses and a fence and a whole lot of sky"* — the crane completes as before, but the fence now has one new bright panel in it.
39. *"We caught them in a jar and we let them go at nine"* — fast intercut of four summers on the same square of grass, both kids getting taller, one cut per bar.
40. *"Because a light that small is only borrowed for a time"* — reuse shot 20 tighter and slower, the release at half speed.
41. *"I can still hear the hinge, I can still smell the grass"* — the hinge and the grass again, but the grass is dry and cut short now, two macro shots.
42. *"I can still feel fourteen when the summer gets like this"* — the seventeen-year-old lying in the same spot as shot 22, same overhead framing, alone.
43. *"Nothing ever happened and it changed my whole life"* — the empty porch steps in the same wide as shots 23 and 28, nobody on them, held.
44. *"Fireflies and porch lights, you and me and July"* — the lawn with almost no fireflies left, the one lit porch behind it, slow drift.

### Instrumental — nobody on the porch

45. The two empty chairs, one rocking slightly, no wind explanation offered, static.
46. The mason jar upside down on the rail with the lid lying beside it, macro, dust visible.
47. The hinge, still, no movement at all, the longest static shot in the video.
48. A spider working in the corner of the bug light, moths gone, macro.
49. The lawn seen from an upstairs window, mown short, no fireflies, a sprinkler ticking across it in the dark.

### Bridge — her own porch

50. *"I've got a porch of my own on a street you never knew"* — a different porch, wider boards, better paint, present-day Mahima sitting with her feet up, locked-off from the rail.
51. *"Two chairs and a bulb I leave on after dark"* — two chairs, one clearly used, a mug on the rail, the bulb already on in daylight, static.
52. *"When the heat leaves the grass I still go out at eight"* — the screen door opening on a hinge that works, no slap, her stepping out with the mug, medium.
53. *"And let the evening take its time to start"* — a slow wide of her lawn going from gold to blue in one shot, her small on the porch, time-lapse feel.
54. *"Some kids came through with a jar and a nail-punched lid"* — two kids of about nine cutting across her lawn with a jar, freezing when they see her, handheld.
55. *"And I let them have the yard, the way somebody did"* — she lifts one hand off the rail, they carry on, and she watches them without saying anything, over-the-shoulder.

### Final chorus — both porches

56. *"Fireflies and porch lights, you and me and July"* — the matched crane a third time, and now both lights are on again because one of them is hers.
57. *"Two houses and a fence and a whole lot of sky"* — the crane completes and match-cuts to her own lawn on the rise, the two skies continuous.
58. *"I don't need it in a jar, I don't need it to stay"* — the kids opening their jar on her lawn, shot from her eyeline at the rail, everything going up at once.
59. *"A light like that was only ever passing anyway"* — her face at the rail watching it, warm light from below, a real unforced smile, close-up.
60. *"I can still hear the hinge, I can still smell the grass"* — the old hinge and the new hinge cut back to back, matched framing, one paint-thick and one clean.
61. *"I can still feel fourteen when the summer gets like this"* — the fourteen-year-old on the lawn from shot 22 and the adult on the porch in the same composition, cut on the beat.
62. *"Nothing ever happened and it changed my whole life"* — the empty steps from shot 43 cut to her own steps with the two kids sitting on them, the frame no longer empty.
63. *"Fireflies and porch lights, you and me and July"* — the widest shot in the video: her lawn, the kids, the fireflies and the sky, all lit together for the first time.

### Post-chorus — the kids

64. *"You and me and July"* — handheld low on the grass, the two kids running through a sprinkler, hands opening, water everywhere.
65. *"Two kids and a jar and a sky"* — the jar abandoned on its side in the grass, lid off, sprinkler mist crossing it, macro.
66. *"You and me and July"* — her clapping the rhythm once on the porch rail with one hand, half-smiling, not singing, close-up.
67. *"Let it go, let it go, let it fly"* — the kids' hands opening upward in slow motion against hard sprinkler backlight, everything sparkling.

### Outro — the light left on

68. *"Screen door banging on a hinge that never got fixed"* — the old hinge from shot 1 one last time, macro, no movement, then a slow fade to the new one.
69. *"Somebody out there is fourteen tonight"* — a long lens down her present-day street: three porch lights on, one of them with two kids under it.
70. *"I'll leave it on, I'll leave it on till the morning"* — her going in, the screen door slapping twice behind her, the porch empty, static.
71. *"Fireflies and porch lights, you and me and July"* — final shot: one warm bulb over two empty chairs in a black frame, one moth crossing it, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the hinge in shot 1, the fence vault, the jar release in shot 20,
the truck at the curb, the second crane where the light is missing, the
instrumental, the first frame of her own porch, the third crane, and the
final bulb. At 94 BPM a bar is 2.55 s; verses cut on the line, choruses on the
bar, the post-chorus every half bar.

**The shareable cut** is shots 17–20, vertical: the crane off the lawn into
the jar release, with *"a light that small is only borrowed for a time"* on
screen.

**The challenge — leave the light on.** Film your own porch, stoop, balcony
or window at dusk and cut on *"you and me and July"*, then tag the neighbour
you spent those summers with. The three matched cranes are the second
shareable idea: post them as a triptych and let people find the missing light
themselves.

## 6. Quality-control checklist

- Three ages of Mahima in the right sections: fourteen through chorus one, seventeen from shot 25, present day from shot 50 and never before it
- Kai never appears after shot 30, and never on her present-day street
- Her mother is only ever a silhouette behind screen mesh
- The three cranes are identical in framing, lens and grade; only the porch lights and the fence panel change
- Fireflies are tracked warm bokeh added in the edit, never model-generated floating blobs
- One light source per shot; no shot has both the porch bulb and the kitchen window as keys
- All house numbers, signs and truck lettering blanked or composited; no model-generated text
- The last shot is locked-off, holds through the fade, and the bulb never goes out
