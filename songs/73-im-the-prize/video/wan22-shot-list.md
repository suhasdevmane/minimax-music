# Wan 2.2 Shot List — "I'm the Prize"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
96 BPM a bar is 2.5 s; the choruses cut once a bar on the streetlamps, the
rapped verses cut on the half-bar where the macro inserts land, and the
post-chorus cuts four times in two bars.

## 1. Visual style

**An ordinary street, lit and cut like a runway.** One location carries the
whole video: a plain residential road after rain, a corner shop with a lit
sign, wheelie bins, a bus stop, shutters. Nothing is dressed up and
everything is lit as if it had been. The grammar is the **retreating
dolly** — the camera walks backwards in front of her at exactly her pace,
and it never once turns to look at what she is walking away from.

Against that runs the **flat**: the window she used to stand in, and the
shelf she calls the trophy room. The flat is deliberately the least
beautiful photography in the film — grey window light, one overhead, no
styling — because the song's claim is that the unglamorous shelf is the real
prize. Gold is a **reflection** in the intro, a **wardrobe** decision in the
pre-choruses, and a **light source** only from the first chorus on.

The men in this video are faceless and always will be. There is no rival
woman scene, no look between women, no slow-motion confrontation; the bridge
depends on that restraint absolutely.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium orange on black wet ground, gold only as reflection | Macro, then ground-level lock-off |
| Verse 1 (rap) | Cold flat interiors, unflattering overhead; pub warm and defocused | Static holds, half-bar macro inserts |
| Pre-choruses | First real gold sources: hallway bulb, then streetlamps | Slow tilts, camera retreating ahead of her |
| Chorus 1 | Streetlamp gold as key, everything else cool | Retreating dolly at walking pace |
| Verse 2 (rap) | Grey morning, no styling, one window | Slow macro pan along the shelf |
| Chorus 2 | More gold sources, headlights and shop windows | Wider, lower retreating dolly |
| Instrumental | Slow motion, then one remaining light | Locked-off, slowed |
| Bridge | Lamps behind her, face half in shadow, then warm frontal | Static, slightly too wide |
| Final chorus | Every lamp at full plus one unmotivated warm key | Widest dolly of the video |
| Post-chorus | Alternating cold street and warm lamp, one per cut | Ultra-fast, half a second each |
| Outro | Intro lighting, one stop warmer | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the waiting look — verse 1, the flat at night)

> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly flattened, no makeup, wearing a dark wool coat still buttoned indoors over a plain grey top, tired patient expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the runway look — pre-choruses, choruses, post-chorus, outro)

> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and full with a deep side parting, warm bronze makeup with a glossy nude lip, wearing a gold-toned longline coat over a black slip dress, large gold hoop earrings and a fine gold chain, calm certain expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the trophy room — verse 2, the flat in the morning)

> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied up in a loose knot, bare face with no makeup, wearing an oversized cream knit and soft grey joggers, one thin gold chain still on from the night before, amused unsentimental expression, realistic cinematic photography, consistent identity, natural skin texture

The **thin gold chain carries across all three looks** — it is on in the
flat at night, it is on in the morning, and it is the one gold object that
never comes off. Keep the neckline in frame wherever the shot allows.

Objects: the **corner shop sign** and its reflection in wet tarmac, the
**door chain** left hanging loose, the **lit window rectangle** seen from
the street, the **gold hoops**, the **shelf** with a rent receipt under a
stone, a leggy houseplant, a chipped mug and a lanyard, and the **low wall**
she sits on in the bridge.

**The ex** — never shown clearly: a shoulder in a pub booth, a hand on a
door, the back of a head at a corner. Never a face, never a reaction shot,
never in the same frame as her after the first verse.
> a young man in his twenties, back to camera or face out of frame, dark jacket, no visible features

**The friends at the pub table** and **the man at the corner in chorus two**
are faceless in the same way. Nobody in this video who is not Mahima gets a
close-up except the two teenage girls on the wall and the woman on the far
pavement in the bridge, who are both filmed plainly and neither of whom is a
rival.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, phone faces, shop signage, the rent receipt and the lanyard
are composited in the edit.** Generate phones as lit blank rectangles and
paper as blank paper, then overlay in post — the model cannot render legible
UI or print, and the receipt on the shelf must read as a receipt for one
second and never be actually readable.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA (front,
three-quarter, profile, walking, seated on a low wall); keep the ex's
reference deliberately faceless. Keyframes first; **OpenPose on every
walking shot** — the retreating dolly is the whole video and a drifting gait
or a swapped leg will show immediately at this pace. Depth for the street so
the vanishing point stays in the same place across the intro, the choruses
and the outro, which are the same plate three times. 16:9 first; 9:16
recomposition for the runway walk, which is the vertical hero. Animate
conservatively: one movement per clip — a hoop swinging, a blind closing, a
foot entering water, a chain settling on a collarbone.

The retreating dolly must be generated at a **fixed pace**. Build the empty
street plate first, light it, and lock the lamp spacing before generating
anything with her in it, because the chorus cuts land on the lamps.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; the rap-verse macro inserts 1.5–2 s; the post-chorus cuts
half a second.

## 4. Scene per lyric line

### Intro — the street, before anything happens

1. *"Gold light on an ordinary street,"* — macro on wet tarmac: the corner shop sign broken up in the water and reassembling as a foot enters frame, static, sodium orange on black.
2. *"Corner shop, wet tarmac, my own two feet."* — tilt up from the boots to the shopfront, the only lit thing on the road, slow.
3. *"You've been running the numbers on me all this time,"* — ground-level wide, the street running to a vanishing point, her small at the far end and not yet moving, locked-off.
4. *"Like the risk is mine."* — her face in the dark between two lamps, unlit and unhurried, close-up, held one beat past comfortable.

### Verse 1 — the shortlist and the dialect of waiting

5. *"You had me on a shortlist with a couple of maybes,"* — the flat at night: her sitting upright on the edge of a sofa in a coat she has not taken off, phone face-up on the table, one hard overhead, static wide.
6. *"Door left on the latch and your cards to your chest."* — a front door standing a hand's width open onto a dark landing, the chain hanging loose, absolutely no movement in frame, held.
7. *"Told your boys you were seeing where it went,"* — a pub table from behind a faceless man's shoulder, three faceless friends laughing, warm and defocused, handheld.
8. *"Told me nothing at all, and I called that respect."* — hard cut back to her flat: the phone screen going dark on the table, her not reaching for it, macro.
9. *"I used to read your silence like it was a language,"* — extreme close-up of a lit blank phone screen (UI composited), her eyes moving across it as if reading a page.
10. *"Learned a dialect of waiting that nobody should learn."* — three half-bar inserts on the beat: the screen dark, lit for something that is not him, dark again, same framing each time.
11. *"Made my whole week a window you could stand at,"* — from the street outside: her standing in a lit window rectangle, the road black around her, static wide.
12. *"And you came when it suited and you left when it turned."* — the same lock-off, three nights cut together: window lit, window empty, window lit, cold exterior, warm interior, and she is always on the wrong side of the glass.
13. *"I'm not doing an interview, I'm not doing a trial,"* — her closing the blind in one movement, the lit rectangle going out, the frame losing its only warm source.
14. *"I'm not auditioning for a part in my own life."* — inside: the door pushed properly shut, the chain lifted off its slot and dropped, macro on the hand, then black for half a beat.

### Pre-chorus 1 — putting the gold on

15. *"So I got up slow and I put the gold on,"* — gold hoops going in one at a time, extreme close-up, a hallway bulb behind her — the first real gold light source of the video.
16. *"Walked out into a night that wasn't yours."* — a fine gold chain settling onto a collarbone, then a gold-toned coat lifted off a hook, two beats, macro.
17. *"Every ordinary street I've been down"* — the front door of her building opening onto the road, seen from outside, the camera already retreating before she is through it.
18. *"Turned into a runway under lamps and open doors."* — her first three steps under the first three lamps, gold crossing her and releasing her in time with the bar, tracking backwards.

### Chorus 1 — the runway

19. *"I'm not the game, baby, I'm the prize,"* — the retreating dolly at walking pace, the whole ordinary street behind her, shutters and a bus stop lit like staging, medium wide.
20. *"Not the maybe, not the almost, not the compromise."* — the same move tighter: waist to head, one lamp passing across her face per phrase, no reaction to the camera.
21. *"I'm not the thing you win for turning up late,"* — low angle from the tarmac, her boots and the wet reflection walking toward and past lens, the shop sign upside down in the water.
22. *"I'm the thing you lose by making somebody wait."* — profile tracking alongside at her exact pace, wheelie bins and a chip shop sliding past behind her, unglamorous and lit beautifully.
23. *"Take your time, take your shot, take your chances elsewhere,"* — two teenage girls sitting on a low wall look up as she passes; one of them straightens without knowing why, handheld from behind them.
24. *"I've got gold light and a street and my own self."* — a wide that includes the whole road and nobody else in it, her dead centre, held for a full bar.
25. *"I'm not the game, baby, I'm the prize,"* — the retreating dolly again, closer than shot 19, the lamps now flaring gently in the lens.
26. *"And I'm done being somebody's nice surprise."* — she passes out of the lamp's pool into the dark between lamps and keeps walking, the frame going almost black on the last word.

### Verse 2 — the trophy room

27. *"There's a shelf in my place that I call the trophy room,"* — the flat in grey morning: one shelf, badly lit, filmed straight on and completely seriously, static wide.
28. *"A rent receipt, a scar, and a plant I didn't kill,"* — a slow macro pan along the shelf in the exact order of the line: a receipt under a stone, a forearm scar as she reaches past, a leggy houseplant that has plainly been kept alive by effort.
29. *"A friendship I nearly wrecked and then repaired,"* — a phone call taken at a kitchen table, answered on the second ring, her shoulders dropping as she starts to laugh; the phone screen composited.
30. *"A job I said yes to before I had the skill."* — a lanyard hanging on the corner of the same shelf, macro, the name never legible.
31. *"None of it is shiny and all of it is mine,"* — her hand straightening a chipped mug on the shelf by a centimetre, then leaving it, close-up.
32. *"And it took a lot of quiet to get here."* — four one-second inserts, one per beat: the same flat in four different years, different curtains, different kettle, same shelf, nobody else in any of them.
33. *"So when you ask me what I bring, I laugh,"* — her sitting on the floor with her back to the shelf, laughing once, small and real, at nothing anyone said. The only laugh in the video.
34. *"Because I'm standing on a decade you weren't near."* — she stands up into frame in front of the shelf, filling it, the window light one stop warmer than shot 27, medium.

### Pre-chorus 2 — the doorways

35. *"So I got up slow and I put the gold on,"* — the hoops again, framing identical to shot 15, but her hands are steadier and the cut is faster.
36. *"Walked past every doorway I used to wait."* — a tracking shot past three doorways in a row: the building's landing, a bar entrance, a car passenger door standing open. She stops at none of them.
37. *"Every ordinary corner in this city"* — a corner taken at speed, the camera swinging round it a half-second ahead of her, streetlight smearing.
38. *"Turned into a runway, and I'm not late."* — doorway light spilling across the pavement and her walking straight through the middle of it without slowing, low wide.

### Chorus 2 — the street catches up

39. *"I'm not the game, baby, I'm the prize,"* — the retreating dolly, further back and lower than chorus one, the road now with real traffic and real people on it.
40. *"Not the maybe, not the almost, not the compromise."* — a bus passes between camera and subject and she is still there, same pace, when it clears.
41. *"I'm not the thing you win for turning up late,"* — taxi headlights sweep across her from the side and pass, the gold moving over her face and off it.
42. *"I'm the thing you lose by making somebody wait."* — a faceless man at a corner half-turns to look; the camera does not, and stays with her, tracking.
43. *"Take your time, take your shot, take your chances elsewhere,"* — a shop window reflection walking alongside her in the glass, two of her, both at the same pace.
44. *"I've got gold light and a street and my own self."* — reuse the framing of shot 24, wider, and now there are four other people on the road who have nothing to do with her.
45. *"I'm not the game, baby, I'm the prize,"* — the two teenage girls again, now walking a few metres behind her, not following, just going the same way.
46. *"And I'm done being somebody's nice surprise."* — the vanishing point of the street with her walking into it, held to the end of the bar, wide and still.

### Instrumental — the half-time switch

47. Slow motion: a gold hoop swinging and coming back to still against her neck, backlit by a lamp, extreme close-up.
48. Slow motion: water thrown up by a passing wheel, lit orange, filling the frame and falling.
49. Her standing completely still in the middle of the empty road, arms down, the street moving around her, wide, no camera move at all.
50. The flat, one insert: a hand on the shelf straightening the plant's pot by a centimetre. Matched framing to shot 31.
51. A bare frame: the corner shop sign switching off, one bank of letters at a time, on the single piano note, then black.

### Bridge — the turn

52. *"Here's the part I didn't understand for years,"* — her sitting on a low wall on the same street, coat open, not performing for anyone, static and slightly too wide.
53. *"A prize is not a thing two women fight about."* — another woman walks past on the far pavement with her own evening going on. No look between them, no slow motion, no music-video beat. Hold the wide.
54. *"It isn't on a shelf and it isn't in a ring,"* — the shelf again, one insert, seen from the doorway of an empty flat, further away than it has ever been shot.
55. *"It's the quiet in my chest when the noise runs out."* — her face on the wall, half in shadow from the lamps behind her, breathing, extreme close-up, no movement.
56. *"I don't need you to lose for me to win,"* — her phone put screen-down on the wall beside her, unhurried, nothing deleted and nobody blocked, close-up on the hand.
57. *"I hope she's kind, I hope you're kind, I hope it's real."* — the other woman turning a corner and gone; the empty far pavement held for the rest of the line.
58. *"And the winning was the part I built alone,"* — the strings and the kit return: her hands on her knees, then pushing off the wall, medium, the first warm frontal light on her face in the whole video.
59. *"I'm the whole of it, and this is how it feels."* — she stands up on the downbeat and squares to the road, low wide, the lamps coming up behind her.

### Final chorus — the widest walk

60. *"I'm not the game, baby, I'm the prize,"* — the widest dolly of the video, the whole road in frame, every lamp at full, her walking dead centre.
61. *"Not the maybe, not the almost, not the compromise."* — the two teenage girls fall in behind her, then three more people, then eight. Not a crowd scene and nobody dances; it is an accumulation.
62. *"I'm not the thing you win for turning up late,"* — low from the tarmac again, matched to shot 21, but now there are a dozen reflections in the water instead of one.
63. *"I'm the thing you lose by making somebody wait."* — profile tracking, the bus stop and the shutters going past, the same ordinary furniture as chorus one lit twice as hard.
64. *"Keep your time, keep your shot, keep your chances elsewhere,"* — a slow push in on her face at walking pace, the background going soft, no smile.
65. *"I've got gold light and a street and my own self."* — she is alone in the frame again; the people are gone from the shot, not from the street, close-up on the coat moving.
66. *"I'm not the game, baby, I'm the prize,"* — the retreating dolly at its closest, gold flaring across the lens on the beat.
67. *"And I've stopped waiting to be recognized."* — she looks into the lens for the first and only time in the video, briefly, then away and on. Do not hold it.

### Post-chorus — the chant

68. *"Slow walk, gold light, chin up, eyes ahead,"* — boots hitting wet tarmac, half a second, macro, cold grade.
69. *"No rush, no proof, no test,"* — a gold hoop catching a lamp, half a second, macro, warm grade.
70. *"I'm not the game, baby, I'm the prize,"* — a chin lifting, half a second, close-up, cold grade.
71. *"And I always was."* — the vanishing point of the street, empty and lit, half a second, warm grade. Alternate the two grades exactly one per cut.

### Outro — the same street

72. *"Corner shop, wet tarmac, gold across the glass,"* — the opening macro of the reflected sign in the tarmac, matched frame for frame to shot 1, one stop warmer.
73. *"Same street I have walked a thousand times."* — the corner shop window with gold across the glass and her reflection standing in it, static.
74. *"Nothing here is new about tonight but me,"* — the ground-level wide from shot 3, same lens, same vanishing point, but she is walking toward camera out of it.
75. *"And that was always it, and that was always mine."* — final shot: she passes camera and out of frame, and the shot holds on the empty gold-lit street. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the foot entering the water in shot 1, the blind closing (shot
13), the first gold hoop (shot 15), each *"I'm not the game, baby, I'm the
prize"*, the shelf pan (shot 28), the shop sign switching off (shot 51), the
woman on the far pavement (shot 53), the look to lens (shot 67), and the
empty street at the end. At 96 BPM a bar is 2.5 s; the choruses cut once a
bar and land on the lamps, the rapped verses cut on the half-bar for the
macro inserts, the bridge holds two bars a shot, and the post-chorus takes
four cuts across two bars.

**The runway challenge.** Cut the vertical hero from shots 19–24 — the
retreating dolly down a road with wheelie bins on it — with *"I'm not the
game, baby, I'm the prize"* on screen, and invite people to film the most
boring street where they live, walk it at half speed after rain, and cut on
the streetlamps. No location, no filter, no budget: the whole point is that
the street is ordinary. The second shareable frame is shot 28, the shelf
pan, captioned with the four things on it; the third is shot 53, the woman
on the far pavement, for *"a prize is not a thing two women fight about."*

## 6. Quality-control checklist

- Three looks in the right sections: the coat-indoors waiting look only in verse 1, the gold runway look from shot 15 onward, the cream-knit morning look only in verse 2 and the two flat inserts
- The thin gold chain is on in all three looks and in every shot a neckline is visible
- The retreating dolly holds one fixed pace in every chorus, and the cuts land on the streetlamps — check chorus one against chorus two against the final chorus on a timeline before locking
- Gold is only a reflection before shot 15 and only a light source after it
- No man in the video ever has a visible face, and the ex is never in frame with her after shot 8
- The bridge has no look, no confrontation and no slow motion between the two women; if the take has a glance in it, use another take
- The flat is the ugliest photography in the film and must stay that way — no styling, no fill, no colour on the shelf
- All screens, signage, the rent receipt and the lanyard are composited, and the receipt is never legible
- Shots 1, 3 and 72, 74 are the same plate and the same lens, one stop apart; the last shot is locked-off on the empty street and holds until the audio fades
