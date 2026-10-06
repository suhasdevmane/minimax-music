# Wan 2.2 Shot List — "Trouble Looks Cute on You"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. At 105 BPM a bar is 2.29 s, so most shots
run 3–5 s and the choruses cut on the bar. Take timestamps from the rendered
WAV and cut on the sung line.

## 1. Visual style

A humid salsa bar at one in the morning and the roof above it at four. Two
worlds and one rule: **the red light is the lie and the daylight is the
truth.** Everything inside the bar is lit by a single red bulb over the bar
and warm amber spill from the small stage — saturated, sweaty, gorgeous, and
deliberately flattering. From the bridge onward the red is gone entirely and
never comes back: grey-blue pre-dawn, then flat gold sunrise, then plain
morning street. The camera is close and handheld inside, still and wide
outside. Skin, sweat and brass are the textures.

| Section | Grade | Camera |
|---|---|---|
| Intro | Deep red key, amber stage spill, black surround | Slow push through dancers |
| Verse 1 | Red and amber, hard shadow, macro detail | Static close-ups, macro |
| Pre-chorus 1 | Sweeping stage lights across both faces | Handheld, following |
| Chorus 1 | Fully saturated red and gold, blurred room | Circling, on the bar |
| Verse 2 | House lights half up, unflattering and honest | Static two-shot, booth |
| Pre-chorus 2 | Red returning as the band retakes the stage | Handheld |
| Chorus 2 | Richer red, more of the room watching | Wider, circling |
| Instrumental | Stage-only light, everything else silhouette | Fast cuts, macro |
| Bridge | Grey-blue pre-dawn, city glow from below, no red | Locked-off, wide |
| Final chorus | First gold sunrise, long shadows, no artificial colour | Slow circling |
| Post-chorus | Alternating red and gold flashes on the beat | Ultra-fast |
| Outro | Flat grey morning, one warm shop light | Slow tracking |

## 2. Character bible — paste into every prompt

**Mahima** (the bar)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly damp at the temples, warm bronze makeup with a deep red lip, wearing a black slip dress with thin straps and gold hoop earrings, amused knowing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the roof and the morning)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pushed back off her face, makeup worn down to almost nothing, wearing the same black slip dress under an oversized men's charcoal jacket, barefoot, calm open expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a charcoal jacket over an open white shirt with the collar loose, a plain silver ring on a chain at his throat, a small white scar across the knuckle of his right hand, easy unguarded expression, realistic cinematic photography, consistent identity

**The band** — five players on a small stage: a nylon-string guitarist, a
conga player, a timbale player, a trumpet and a trombone. Faces are fine;
they are witnesses, not characters. Keep them working, never posing.

**The woman at the end of the bar** — faceless. Seen once, over Kai's
shoulder, turning her head at the sound of his laugh, soft-focused and never
held for more than a second.

**Her two friends** — two young women at a table, warm and protective, seen
mouthing a warning and later collecting their coats.

Objects that must stay consistent: the **red bulb** over the bar, the **ring
on the chain**, the **scar on his knuckle**, her **coat check ticket**, her
**shoes carried in one hand** from the bridge on, his **charcoal jacket**,
which moves onto her shoulders in the outro and never leaves.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, signage, the bar clock and the coat check ticket are
composited in the edit.** Generate them blank — the model cannot render
legible text, and any readable sign will break the take.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA; keep
the woman at the end of the bar deliberately faceless. Keyframes first;
OpenPose for the dance shots, the spin and the catch; Depth for the bar
interiors so the crowd behind them holds its distance. 16:9 first; 9:16 for
the chorus dance cuts, which are the natural vertical content. Animate
conservatively: one spin per clip, one turn of the head, sweat catching a
light, a hand closing on a waist. Split any dance sequence into two-to-three
second pieces rather than asking for a full phrase.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the red bulb

1. *"Red bulb over the bar and the brass coming down"* — macro on a single bare red bulb over a crowded bar, then a rack focus past it to the small stage where a trombone slide is dropping on the last phrase, handheld.
2. *"Somebody says your name like a warning to me"* — a friend leaning to Mahima's ear at a packed table, her mouth moving, Mahima's eyebrows lifting one millimetre, close two-shot, red key.
3. *"The congas keep going, nobody's sitting"* — low wide of a packed floor from hip height, legs and skirts moving, the conga player's hands in the background, nobody at the tables.
4. *"And you cross the whole room way too easy"* — Kai moving through the crowd toward camera, the dancers parting without him asking, slow push-in from Mahima's eyeline.

### Verse 1 — three things she notices

5. *"Your friends won't meet my eyes, that's the first thing I clock"* — over Mahima's shoulder: two men at the bar looking anywhere but at her, one finding something urgent in his glass, static.
6. *"Second, the barman pours before you talk"* — the barman setting a glass down in front of Kai before his mouth opens, macro on the pour, red light through the liquid.
7. *"Third, you don't lie about a single part"* — Kai's shrug in close-up, palms turning up, an honest man admitting he is not a safe one, no smile.
8. *"You just say it plain and let me choose my heart"* — Mahima's face, entirely still, taking it in, chin lifting, the red bulb reflected in one eye, close-up.
9. *"There's a nick on your knuckle from a bad last spring"* — macro on the small white scar across his right knuckle as he lifts the glass, the tendon moving under the skin.
10. *"And a chain at your collar holding somebody's ring"* — macro on a plain silver ring hanging on a fine chain at his open collar, rising and falling with his breath, red rim light.
11. *"I should be saying goodnight, I should be gone"* — her hand in the pocket of a coat on the back of a stool, finding a coat check ticket, turning it over between two fingers.
12. *"But the nylon guitar keeps talking me on"* — the guitarist's hands on nylon strings on the small stage, macro, then the ticket going back in the pocket.

### Pre-chorus 1 — the warnings stack

13. *"Every warning that they gave me had your name inside"* — the two friends at their table, both talking at once, urgent and fond, seen from Mahima's seat, slightly out of focus.
14. *"Every one of them was right, and I decide"* — Mahima nodding, yes, I heard you, then setting her glass down on the bar with a small deliberate click, close-up on the glass and her hand.
15. *"Keep your hand right where it is, don't lose the beat"* — Kai's hand arriving at her waist and stopping exactly where it lands, her hand covering it, waist-level close-up.
16. *"I'm not looking for the door, I'm looking at your feet"* — low shot on four feet on a scuffed floor finding the same count, the timbales entering, handheld.

### Chorus 1 — the floor

17. *"Trouble looks cute on you, so I'll take my chances"* — the two of them dancing properly, close and unpolished and laughing, circling camera, the room a red blur behind them.
18. *"Red light, wrong man, right song, two dances"* — four fast beats: the red bulb, his face, the trumpet bell, their joined hands raised on the count.
19. *"I know how this ends, I've been told twice tonight"* — Mahima's face over his shoulder mid-turn, eyes open and clear, not lost at all, close-up.
20. *"And I'd still pick the floor over doing it right"* — a wide of the floor from the stage, the two of them at the centre of it, the bar door small and open behind them.
21. *"Trouble looks cute on you, you wear it like linen"* — his open collar and loose shoulder in close-up as he moves, the shirt soft and damp, the chain swinging.
22. *"Loose at the shoulder and the whole room is in it"* — the whole floor moving in the same direction on the beat, wide, the horn section standing up.
23. *"Call it a mistake, I'll call it mine"* — a spin and a catch, his hand at the small of her back, her hair coming loose, slow motion for one beat only.
24. *"Trouble looks cute on you, and I've got time"* — the two of them stopped dead in the middle of the moving floor, looking at each other, everything else motion-blurred around them.

### Verse 2 — the confession

25. *"Two in the morning and the band takes a break"* — the small stage empty, instruments on stands, the room suddenly quieter and uglier, wide static.
26. *"You give me the version your mother would hate"* — a corner booth, Kai talking with his hands, telling it straight, Mahima's shoulder in the foreground, house lights half up.
27. *"A job that you walked out of, a bridge that you burned"* — two-second flash cut: an office lobby at night, cold fluorescent, one man walking out through the turnstile, back to camera.
28. *"A girl at the end of the bar who still turns"* — over Kai's shoulder, a woman at the far end of the bar turning her head at the sound of his laugh, faceless and soft-focused, held one second only.
29. *"I'm nodding along like I'm reading a menu"* — Mahima with her chin on her hand, completely calm, listening the way you read a menu, a slow blink, close-up.
30. *"Choosing the one thing I know will undo me"* — macro on her finger tracing a wet ring on the table, then stopping.
31. *"You say, you can still leave, the door is right there"* — a wide two-shot with the bar's front door propped open behind her, a cold blue rectangle in the warm red room. She does not look at it.
32. *"And I say, I've counted every step, I don't care"* — her face, straight to him, entirely unbothered, the smallest smile arriving at the end of the line, close-up.

### Pre-chorus 2 — the room clears

33. *"Every red flag in this room is doing a slow wave"* — the band coming back on, a hanging red pennant near the stage moving in the fan draught, then the room refilling around it.
34. *"Every single one is right, and I stay"* — her two friends collecting their coats and giving her the look; she waves them off, warm, no drama, medium shot.
35. *"Keep your hand right where it is, don't lose the beat"* — Kai's open hand held out and waiting, held one beat longer than comfortable, then hers landing in it.
36. *"I'm not looking for the door, I'm looking at your feet"* — reuse the low four-feet framing from shot 16, tighter and faster, the timbales louder.

### Chorus 2 — more of the room watching

37. *"Trouble looks cute on you, so I'll take my chances"* — the floor giving the two of them space, other dancers glancing over, circling camera at a wider radius.
38. *"Red light, wrong man, right song, two dances"* — the trumpet player leaning into a counter-line, bell up into the red, low angle from the floor.
39. *"I know how this ends, I've been told twice tonight"* — Mahima's head going back as she laughs, throat and jaw in the red light, close-up.
40. *"And I'd still pick the floor over doing it right"* — a long lens down the length of the bar, the two of them at the far end, everything between them out of focus.
41. *"Trouble looks cute on you, you wear it like linen"* — his jacket coming off and going over a chair back, the white shirt sticking between his shoulders, medium.
42. *"Loose at the shoulder and the whole room is in it"* — an overhead of the whole floor turning on the same beat, the red bulb dead centre of the frame.
43. *"Call it a mistake, I'll call it mine"* — their fingers laced and lifted on the beat, macro, the ring on his chain swinging into the bottom of frame.
44. *"Trouble looks cute on you, and I've got time"* — the bar clock on the wall reading past three (composited), then Mahima looking at it and not caring, medium close-up.

### Instrumental — the band takes over

45. Macro on the guitarist's right hand on nylon strings, the solo, the red bulb burning out of focus behind it.
46. The brass section trading phrases, trumpet then trombone, bells up, low angle, cut on each answer.
47. The percussion breakdown — congas, bongos, timbales, a cowbell — cut fast on the pattern, hands only, four angles.
48. The two of them dancing in silhouette against the stage lights, no faces, just shape and motion, wide.
49. A slow drift up from the floor to the fire door at the back of the bar, grey light showing under it — the cut into the bridge.

### Bridge — the roof, no red anywhere

50. *"Up on the roof there's no red light to hide in"* — the fire door pushing open onto grey-blue air, the music dropping away behind it, from inside looking out, locked-off.
51. *"Just the city on its four in the morning hum"* — a wide of the city from the gravel roof, a few lit windows, one distant siren's worth of movement, static.
52. *"You go quiet, and you tell me one true thing"* — the two of them on the ledge with a metre of space between them, Kai looking at the city and not at her, wide two-shot.
53. *"Not the dangerous kind, the kind that's hard to say"* — his profile in close-up, the easy expression gone, the ring on the chain still against his shirt.
54. *"And trouble looks different when it's cold and it's honest"* — Mahima's face, the amusement going out of it and something steadier arriving, close-up in flat blue light.
55. *"It looks like a man who might actually stay"* — a wide of the two of them on the ledge, the gap between them now half what it was, first light on the far buildings.

### Final chorus — daylight

56. *"Trouble looks cute on you, so I took my chances"* — Mahima (roof look, his jacket, barefoot) dancing on gravel to the music leaking up through the floor, slow circling.
57. *"Dawn light, same man, one more of those dances"* — Kai's hand finding her waist again in flat gold light, the same gesture as shot 15 with nothing hidden.
58. *"I knew how this ends, they told me twice that night"* — her shoes standing side by side on the gravel where she left them, macro, sunrise behind.
59. *"And I'd pick this roof again and call it right"* — a wide from behind them both, facing the skyline, arms loose, the whole city going gold.
60. *"Trouble looks cute on you, you wear it like linen"* — his open collar again, this time in daylight, the shirt creased and honest, close-up.
61. *"Loose at the shoulder with the sun coming in it"* — the sun edging over a building and catching the silver chain, lens flare across his throat, macro.
62. *"Call it a mistake, I'll call it mine"* — the two of them laughing at how ridiculous the whole thing is, foreheads almost touching, handheld.
63. *"Trouble looks cute on you, and I've got time"* — a slow spin with the skyline behind her, jacket sleeves past her hands, wide, gold.

### Post-chorus — the chant

64. *"So I'll take my chances, so I'll take my chances"* — four ultra-fast flashes: the red bulb, his hand at her waist, the trumpet bell, her shoes in her hand.
65. *"Red light, wrong man, right song, two dances"* — reuse shot 18's four beats, cut twice as fast, alternating red and gold frames.
66. *"So I'll take my chances, so I'll take my chances"* — her face in the red bar and her face on the gold roof, hard cut between them on the beat, four times.
67. *"Trouble looks cute on you"* — the roof, both of them still, the chant dropping out, a held wide.

### Outro — the street

68. *"Bar is shut, the brass is packed away"* — street level, the bar shuttered, the trombone player loading a case into a car boot, flat grey morning.
69. *"Your jacket on my shoulders and the street is grey"* — Mahima walking with the charcoal jacket around her, sleeves well past her hands, tracking from the side.
70. *"Somebody's going to say your name like a warning"* — a shopkeeper rolling up a shutter and glancing at the two of them, incurious, wide.
71. *"And I'll smile and I'll say, I know, and I'll stay"* — final shot: she glances back once at the dark bar door, then turns and keeps walking beside him, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each *"trouble looks cute on you"*, the
band break at shot 25, the instrumental, the fire door at shot 50, the first
gold frame at shot 56, and the last look back. At 105 BPM a bar is 2.29 s;
the choruses cut on the bar and the post-chorus cuts on the half-bar.

**The two-dance cut.** Post shots 17–24 vertical with the hook on screen —
the spin and catch at shot 23 is the single frame that travels. The
challenge: film the moment you knew a night was going to be a story, cut on
*"right song, two dances."* The second shareable frame is shot 58, her shoes
on the gravel at sunrise, captioned *"I read every warning. I stayed for the
second dance."*

## 6. Quality-control checklist

- Two looks, cleanly divided: bar look with the red lip until shot 49, roof look with his jacket and bare feet from shot 56 on
- No red light appears in any frame from shot 50 onward, and no artificial colour at all after shot 55
- The woman at the end of the bar is faceless and on screen for one second only
- The ring on the chain and the scar on his knuckle are visible in at least one shot per section he appears in
- The bar clock, the coat check ticket and any signage are composited; no model-generated text anywhere
- Dance shots are one movement per clip, OpenPose-referenced, with real weight — no floating feet or impossible spins
- His jacket travels: on him to shot 41, over a chair, on her from shot 56 to the end
- The last shot is locked-off and holds until the audio fades
