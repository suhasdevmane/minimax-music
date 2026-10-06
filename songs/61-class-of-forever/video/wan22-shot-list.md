# Wan 2.2 Shot List — "Class of Forever"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-five entries. Timestamps come from the rendered WAV; cut
on the sung line. At 116 BPM a bar is 2.07 s, so verse shots run 3–4 s and
the choruses cut on the bar.

## 1. Visual world

One school, one night, one field, told in three light sources in strict
order: **institutional fluorescent** in the building, **sodium floodlight**
on the field, then **headlights and phone screens** when the school switches
off, and finally **dawn**, which is the only warm light in the video and
arrives from the horizon rather than from anything the school owns. The
building is deliberately unbeautiful — polished floors, taped-over notices,
scuffed lockers — so that the field reads as an escape. Handheld inside the
crowd, locked-off whenever she is alone.

| Section | Grade | Camera |
|---|---|---|
| Intro | Flat fluorescent, one blade of daylight | Long lens, static |
| Verse 1 | Fluorescent, cool, unromantic | Macro and slow push-ins |
| Pre-chorus 1 | Low gold sun down a row of cars | Slow lateral track |
| Choruses | Sodium floodlights, deep blue sky | Handheld inside the crowd |
| Verse 2 | Scoreboard glow, phone torches, first gray | Low and still |
| Pre-chorus 2 | Two hard headlight beams, black surround | Locked-off |
| Instrumental | Streetlight strobe through car interiors | Fast, in-car |
| Bridge | Blue pre-dawn, scoreboard off mid-line | Locked-off wide |
| Final chorus | Headlights killed, dawn from the horizon | Drone rise |
| Post-chorus | First direct sun across the bleachers | Handheld, chest height |
| Outro | Clean gold morning, sprinkler mist | Slow pan, held wide |

## 2. Character bible — paste into every prompt

**Mahima** (ceremony)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair half pinned up under a graduation cap, light natural makeup, wearing an open navy graduation gown over a white tee and jeans, bright overwhelmed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (midnight on the field)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and damp from sprinklers, makeup worn off, wearing a soaked white tee and jeans with the gown tied round her waist, barefoot, calm tired expression, realistic cinematic photography, consistent identity

**Mahima** (outro, morning)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair dried messy, no makeup, wearing an oversized varsity jacket over the same white tee, settled unhurried expression, realistic cinematic photography, consistent identity

**Kai** — the friend staying in town, the only male lead with a face.
> Same male character Kai, man in his early twenties, close-cropped dark hair, short beard, athletic build, wearing a navy graduation gown over a football practice shirt and shorts, open easy expression, realistic cinematic photography, consistent identity

**The coach** — seen only from the chest down and in silhouette in the gym doorway, never a clear face.

**The class** — a crowd of fifteen to twenty young people in navy gowns, faces
allowed and repeated across the night so the group reads as one class, not as
extras. Two are named by the lyric and must be castable at a glance: a boy
enlisting in the fall and a girl with an airline tag already on her bag.

Objects that recur: the **sticker shadow** on the locker door, the **cracked
trophy case**, the **stolen helmet**, a **keyring** turned over and over, and
the **white sneakers** left on the fifty-yard line.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All signage, scoreboards, school names, phone screens and the airline tag
are composited in the edit.** Generate boards and screens as blank lit
surfaces — the model cannot render legible text, and a misspelled school
banner in a graduation video is fatal.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai with IP-Adapter or a character LoRA
each; keep the coach's reference cropped so no face is ever generated.
**OpenPose is essential for the cap throw and the crowd choruses** — fifty
arms going up at once is exactly where the model invents limbs, so shoot the
throw as three separate plates of six to eight people and composite. Depth
for the corridor, which is long, symmetrical and confuses the model without
it. 16:9 first; 9:16 for the cap-throw and headlight cuts. Animate in short
bursts: one throw, one sprinkler sweep, one hand finding another hand.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–4 s; chorus shots 2 s.

## 4. Scene per lyric line

### Intro — the last bell

1. *"Last bell rang and nobody moved"* — long lens straight down an empty corridor, fluorescent tubes overhead, a dozen students standing still in it and not talking, static, flat light.
2. *"Half of us just stood there in the hall"* — a slow pan across four of them against the lockers, none of them looking at each other, hands in pockets.
3. *"Somebody's speaker in the parking lot"* — the propped-open double doors at the end of the corridor as a rectangle of hot daylight, a car stereo audible beyond it, static.
4. *"Playing the same four chords for us all"* — outside now: a boot on a car sill, a phone on a dashboard, the lot shimmering, low angle.
5. *"Nothing but floor wax and fluorescent light"* — macro on the polished floor doubling the tubes overhead, one sneaker stepping into frame and stopping.
6. *"And now they want the keys and the building back"* — a caretaker's hand hanging a bunch of keys on a hook by the office door, close-up, unglamorous.

### Verse 1 — the building, item by item

7. *"I scrape a sticker off the locker door"* — macro on a thumbnail working under the edge of a sticker, paint flaking, her breath fogging the metal.
8. *"It leaves the shape of it, four years of glue"* — the ghost of the sticker left in adhesive, a perfect outline, her thumb resting on it, held.
9. *"Coach is holding the gym doors open"* — the gym doorway in silhouette, a big man holding one door with an outstretched arm, seen from behind Mahima, chest down only.
10. *"Saying, go on, get out, like he isn't crying too"* — reverse: the coach's jaw and shoulder in the corner of frame, looking hard at the floor, students filing past him into the daylight.
11. *"There's a dent in the trophy case from sophomore year"* — a spidered crack low in the trophy case glass, dusty medals behind it, slow push-in.
12. *"Nobody ever said whose fault it was"* — three of them glancing at each other in the reflection of the same glass, one small guilty grin, over-the-shoulder.
13. *"I put my hand flat on the cold glass"* — her palm flat against the case, the corridor reflected behind her hand, macro.
14. *"And I say thank you to a building, just because"* — a wide of her alone in the corridor with her hand still on the glass, the fluorescents buzzing, locked-off, held four seconds.

### Pre-chorus 1 — nobody starts a car

15. *"Nobody's engine is actually running"* — slow lateral track along a row of open car doors, kids sitting sideways in driver's seats with their feet on the tarmac, gold sun straight down the row.
16. *"Everybody's keys are in their hand"* — close-up of a hand turning a keyring over and over, never putting the key anywhere.
17. *"We keep saying that we're gonna go now"* — Kai leaning on a hood mid-sentence, pointing vaguely at the road, nobody moving, medium.
18. *"Then nobody goes. I think we understand"* — a high wide of the whole lot: twenty cars, doors open, nobody in motion, long shadows, static.

### Chorus 1 — caps up

19. *"We're the class of forever, no goodbye's gonna stick"* — low and wide from the grass under the floodlights, the class in gowns, arms coming back, the field enormous behind them.
20. *"Throw it up, let it fall, we were here and it was quick"* — fifty mortarboards leave frame at once; hold on empty sky one full beat; they come back down badly and everyone ducks.
21. *"Fifty caps in the floodlights, half of them come down wrong"* — slow motion of caps tumbling through the sodium beams, one bouncing off a shoulder.
22. *"Somebody's crying, somebody's laughing, somebody starts the song"* — handheld inside the crowd at head height, spinning through three faces: crying, laughing, singing.
23. *"We've got no five-year plan, we've got the whole of the night"* — Mahima with her cap gone, head back, eyes shut, laughing at the floodlights, close-up.
24. *"And a field full of people I will know for life"* — a slow arc around a knot of eight of them with arms round shoulders, the crowd holding steady around the lens.
25. *"Turn the headlights on the grass, take one more pic"* — a phone held up for a group photo, everyone piling in, one boy sprinting in late from the left.
26. *"We're the class of forever, no goodbye's gonna stick"* — wide from behind the group toward the goalposts, caps scattered at their feet, floodlights flaring the lens.

### Verse 2 — midnight on the fifty

27. *"Midnight on the fifty and the sprinklers kick on"* — the sprinklers coming up in sequence across the fifty-yard line, seen at grass height, water crossing the frame in slow motion.
28. *"Nobody runs for it, we let it soak us through"* — the group standing in it with their arms out, gowns tied round waists, soaked through, wide.
29. *"He's enlisting in the fall, she's flying out on Tuesday"* — two close-ups back to back: a boy sitting on a helmet with his forearms on his knees; a girl with an airline tag already looped on her bag strap (composited).
30. *"And I'm staying right here, and that's alright too"* — Mahima flat on her back in the wet grass looking up, overhead shot, sprinkler mist above her.
31. *"We swear on a helmet somebody stole from the shed"* — the stolen helmet upside down in the grass, four hands laid on it one at a time, macro.
32. *"Same spot, ten years, whoever can come"* — a tight circle of faces from inside the huddle, lit by phone torches from below, nobody grinning.
33. *"Then we sit in the wet grass till the sky goes gray"* — a long static wide of six of them sitting in a rough line on the fifty, the sky visibly lightening behind them.
34. *"And nobody says the word done"* — Kai and Mahima side by side in profile, neither speaking, the scoreboard glow on their faces.

### Pre-chorus 2 — the gate

35. *"Somebody's mom keeps flashing headlights at the gate"* — headlights flashing twice through chain-link, seen from the field, hard beams through the fence diamonds.
36. *"Somebody's brother says he'll drive us all around"* — a boy walking backwards across the grass toward the gate, arms wide, still talking, wide.
37. *"We keep saying that we're gonna go now"* — nobody stands up. A locked-off wide of the seated group with the gate lights behind them.
38. *"And then nobody goes. Nobody makes a sound"* — a girl waving at the gate without turning her head, close-up, everything else black.

### Chorus 2 — headlights on the grass

39. *"We're the class of forever, no goodbye's gonna stick"* — six cars reversed onto the running track, headlights aimed at the field, engines running, wide from behind the cars.
40. *"Throw it up, let it fall, we were here and it was quick"* — the class dancing in the beams, silhouettes thrown fifty feet across the grass, handheld low.
41. *"Fifty caps in the floodlights, half of them come down wrong"* — reuse shot 21 as a two-second flashback insert, colder, then hard cut back to the headlights.
42. *"Somebody's crying, somebody's laughing, somebody starts the song"* — three faces again but lit hard white by headlights now, black surround, cut on the beat.
43. *"We've got no five-year plan, we've got the whole of the night"* — Mahima standing directly in a headlight beam, arms out, her shadow enormous behind her.
44. *"And a field full of people I will know for life"* — a low shot along the grass with twenty pairs of bare feet and a hundred long shadows crossing.
45. *"Turn the headlights on the grass, take one more pic"* — the group photo again, this time lit only by phone flashes, everyone blinking through it.
46. *"We're the class of forever, no goodbye's gonna stick"* — high wide from the bleachers looking down on the lit field, the whole class in one frame, tiny.

### Instrumental — school to field

47. Five cars pulling out of the school lot in a line, seen from the sidewalk, gowns hanging out of the windows.
48. A trunk full of shoes, gowns and one football helmet, lid slamming, macro.
49. Bare feet out of a rear window against streetlight strobe, in-car, fast.
50. The school sign shrinking in a wing mirror (blank board, composited), rack focus to a laughing face in the back seat.
51. Hard cut: the corridor from shot 1, now dark, one caretaker's light on, the floor still shining, nobody in it. Two seconds of silence.

### Bridge — the honest part

52. *"I know how this goes, I have watched it before"* — locked-off wide, Mahima sitting up alone at the fifty in blue pre-dawn, the others out of focus behind her.
53. *"The group chat goes quiet by the second fall"* — a phone face-up in the grass, screen dark, dew on it, macro.
54. *"Half of us won't drive back when the ten years land"* — four faces in close-up, one at a time, listening and not answering, cut evenly.
55. *"And half of us will, and half is not that small"* — Kai's face, the only one that reacts, a slow nod, close-up.
56. *"So I won't ask you for a decade or a vow"* — the scoreboard switching off mid-line, the field dropping a full stop of light, wide.
57. *"Just stay out on this field with me right now"* — Mahima lying back down in the grass, and one by one the others do the same around her, overhead, rising.

### Final chorus — dawn from the horizon

58. *"We're the class of forever, no goodbye's gonna stick"* — everyone up, a ragged line across the fifty facing the sunrise, seen from behind, wide.
59. *"Throw it up, let it fall, we were here and it was quick"* — arms round shoulders, the line rocking, singing at the sky, handheld from inside it.
60. *"Fifty caps in the wet grass, we can leave them where they land"* — a slow track across abandoned caps lying in the wet grass, sprinkler mist over them, dawn light.
61. *"Somebody's crying, somebody's laughing, somebody takes my hand"* — macro: a hand finding hers in the middle of the line, no faces, held.
62. *"We've got no five-year plan, we've got the rest of the night"* — Mahima's face in first sun, eyes closed, mouth open on the note, close-up.
63. *"And a field full of people I will know for life"* — drone begins to rise off the field: a ring of people, caps scattered, cars around the track.
64. *"Kill the headlights, one more song before we split"* — the headlights go out in pairs as the drone climbs, the field returning to natural light.
65. *"We're the class of forever, no goodbye's gonna stick"* — the drone at height, the whole field and the dark school beyond it, the sun clearing the bleachers.

### Post-chorus — the chant

66. *"Oh, no goodbye's gonna stick"* — handheld at chest height inside the group, faces above the lens, everyone shouting down at the camera.
67. *"Oh, we were here and it was quick"* — feet stomping in wet grass, water jumping, macro on the beat.
68. *"Same spot, same gate, same ten years"* — the stolen helmet upside down in the grass with car keys thrown into it, one more set landing.
69. *"Oh, no goodbye's gonna stick"* — a boy on someone's shoulders with both arms up, silhouetted against the sunrise.
70. *"Hands up if you're never getting over it"* — every hand in the group going up at once, shot from below, first direct sun through the fingers.
71. *"Oh, no goodbye's gonna stick"* — the group breaking apart in four directions across the field, wide, held.

### Outro — one car left

72. *"Sun's coming up on the empty bleachers"* — empty bleachers in full morning light, rows of aluminium, absolutely still, wide.
73. *"Somebody's shoes still out on the grass"* — a single pair of white sneakers on the fifty-yard line, sprinkler mist still hanging, macro.
74. *"I'm the last one in the parking lot"* — slow pan from the field to the lot: one car, doors shut, everything else gone.
75. *"And I'm not in a hurry, and I'm not sad"* — final shot: Mahima sitting on the hood in the varsity jacket, gown folded on her lap, not looking at her phone, morning sun on her face, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the bell decay, the first downbeat of verse one, the cap throw in
shot 20, the sprinklers in shot 27, the headlights in shot 39, the
instrumental, the scoreboard switching off, the drone rise, the hands going
up, and the final hold. At 116 BPM a bar is 2.07 s; choruses cut on the bar,
the post-chorus cuts every half bar.

**The shareable cut** is shots 19–22, vertical: the cap throw with the beat
held on the empty sky and *"we were here and it was quick"* on screen.

**The challenge — same spot, ten years.** Post your own last-day frame, then
duet it with the friend you swore it with and hold up the year you graduated.
The headlights-on-the-grass shot (39–44) is the second shareable moment, and
it is the easiest thing in the video for a real class to recreate.

## 6. Quality-control checklist

- Three looks in the right sections: gown and cap through the first chorus, soaked and barefoot from shot 27, varsity jacket only in the outro
- The coach is never seen above the chest; every other class face is repeated across the night so the group reads as one class
- Light runs in strict order — fluorescent, floodlight, headlight, dawn — and dawn never arrives early
- The cap throw is composited from three plates of six to eight people; no single generation of fifty airborne caps
- All boards, signs, screens and the airline tag composited; no model-generated text anywhere
- The helmet, the keyring, the sticker shadow and the white sneakers all appear at least twice
- No shot in the bridge is handheld; the honesty of that section is carried by stillness
- The last shot is locked-off, holds through the fade, and her phone stays face-down
