# Wan 2.2 Shot List — "Lipstick on Your Collar"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
108 BPM a bar is 2.2 s, so most shots are 3–4 s and the choruses cut on
every bar.

## 1. Visual style

Sixties styling with a smartphone in hand: winged liner, a silk robe, a
mustard kitchen, a mirrored elevator, a glass-walled open-plan office that
looks like a modern building dressed by a period costume department. **Red is
the only saturated colour** — the lip print, the lipstick, the flower — and
everything else sits in cream, mustard, chrome and pale blue. Two worlds:
the **apartment** (warm gold morning sun, cosy, hers) and the **office**
(bright, cool, glass, his) — and the video ends the moment the two merge in
the lobby. Slow motion for the walks, static for the jokes, macro for the
print.

| Section | Grade | Camera |
|---|---|---|
| Intro / outro | Warm gold morning, cream and mustard | Static, matched framing |
| Verse 1 | Vanity bulbs, warm; street daylight | Close-ups to camera |
| Pre-choruses | Cool elevator chrome, red reflected | Locked-off in the mirror |
| Choruses (office) | Bright office daylight, red on white | Front tracking, heads turn on the beat |
| Verse 2 | Warm café; cool bathroom fluorescents | Handheld over the shoulder |
| Instrumental | Golden hour, lens flare | Slow-motion strut, tracking |
| Bridge | One warm kitchen lamp; open door on blue evening | Static, close |
| Final chorus / post-chorus | Most saturated frames, bright morning lobby | Slow-motion walk-in, mirrored elevator |

## 2. Character bible — paste into every prompt

**Mahima** (morning, apartment)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair set in soft rollers under a silk headscarf, winged black eyeliner and a bold cherry-red lip, wearing a cream silk robe with a mustard trim, amused knowing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (out, café and street)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in a sixties half-up bouffant with a red ribbon, winged black eyeliner and a bold cherry-red lip, wearing a fitted cream sixties swing coat over a black polo neck and cigarette trousers, cat-eye sunglasses on her head, confident playful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (final chorus, the lobby)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in a sixties half-up bouffant with a single red flower tucked behind her left ear, winged black eyeliner and a bold cherry-red lip, wearing the cream swing coat open over a black dress, radiant confident expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the boyfriend)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a crisp white cotton shirt with a red lipstick print just below the left collar edge, a slim navy tie and grey trousers, embarrassed then proud expression, realistic cinematic photography, consistent identity

**Colleagues** — never a clear face: the back of a head at a printer, a hand on a phone, a receptionist seen from behind the desk, an intern cropped at the jaw. The "work wife" is a faceless figure by the printer, once, seen from behind.
> office workers in smart sixties-styled clothes, faces turned away or out of frame, glass-walled open-plan office

**The sax player** — a street-corner musician, older man, back or profile only, brass catching the sun.

The **lip print** is the motif: it appears in the first minute and in the
last frame, and it is never wiped off. The **red flower** appears in the
bridge and stays in her hair to the end.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, texts, group chats and elevator floor numbers are
composited in the edit.** Generate the phone as a lit blank screen and the
elevator panel as unlit buttons; overlay the UI in post — the model cannot
render legible UI, and the texts are the second verse's storytelling.

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

Most shots 3–5 s. For this song, lock Kai too (front, three-quarter, the
collar in every angle); OpenPose for the corridor strut and the lobby walk-in;
Depth for the mirrored elevator, which the model will otherwise fill with
duplicate people.

## 4. Scene per lyric line

### Intro — the doorway, the secret

1. *"Seven forty-five, you're buttoning up"* — a sunlit sixties apartment hallway, Kai buttoning a white shirt in the hallway mirror, Mahima (morning look) leaning in the kitchen doorway behind him in the silk robe, wide static, warm gold.
2. *"Coffee going cold in your favourite cup"* — a mustard kitchen counter, a chipped favourite mug steaming less and less, a smartphone beside a rotary phone, close-up.
3. *"One kiss at the door before you go"* — the kiss at the open front door, her hand sliding to his collar, medium close-up, morning sun behind them.
4. *"I left a little something you don't even know"* — macro of the cherry-red lip print pressed just below the collar edge on white cotton, then her satisfied smile at the closing door.

### Verse 1 — the plan

5. *"Everybody's got a work wife, that's what they say"* — Mahima at a round-bulb vanity mirror talking straight to camera as if to a friend, one eyebrow up, close-up, warm bulbs.
6. *"Someone by the printer laughing at your jokes all day"* — a flash of the glass-walled office, a faceless colleague by a printer laughing, seen from behind, cool daylight.
7. *"I'm not the jealous type, I'm the creative kind"* — her applying the red lipstick in the mirror, blotting on a tissue, looking up at the lens, extreme close-up.
8. *"So I write in cherry red and leave it where they'll find"* — the lipstick capped with a click, then a slow-motion replay of her hand on his collar at the door, close.
9. *"One press on your collar, right below the ear"* — macro of the print, the fibres of the cotton, the perfect red edge, static.
10. *"You'll be halfway to the lobby before it's clear"* — Kai on a bright street with a coffee, unaware, two passers-by glancing at his collar, tracking from the front.
11. *"I hope the whole floor takes a real good look"* — the office lobby doors ahead of him, the building's glass front, low angle, clean daylight.
12. *"Baby, you're the headline, I'm the one who wrote the hook"* — Mahima at home on the sofa, feet up, phone in hand, grinning at the ceiling, medium, warm.

### Pre-chorus 1 — the elevator

13. *"Go on, take the elevator, act like you don't know"* — Kai stepping into a mirrored elevator with two faceless colleagues, the doors closing, locked-off from inside.
14. *"Ten floors of mirror and a little red glow"* — the mirrored walls reflecting him ten times, the red print visible in every reflection, static, cool chrome.
15. *"Straighten up your tie, keep that blushing low"* — he straightens his tie in the mirror, freezes as he catches the print, a colleague's eyes flicking to it and away, close-up.
16. *"I'm two miles away and I can feel it show"* — split screen: Mahima at home checking her watch with a knowing smile; Kai in the elevator going red, the floor panel climbing (composited).

### Chorus 1 — the whole floor looks

17. *"Lipstick on your collar, so they know you're mine"* — Kai walking onto the open-plan floor, tracking from the front, the first head turning on the downbeat, bright daylight.
18. *"Red on cotton white, they can read between the lines"* — heads turning one after another along a row of desks on each bar, faces turned away, medium wide.
19. *"Give the office something for the group chat, honey"* — phones lighting up along the row, a group chat blowing up (composited), quick cuts.
20. *"Let them lean and whisper, let them think it's funny"* — two colleagues leaning together to whisper, seen from behind, the collar in soft focus beyond them.
21. *"Lipstick on your collar, wear it like a sign"* — Mahima in the kitchen doorway singing to camera, one hand on her hip, the other holding the phone, medium, warm.
22. *"Every desk on every floor can tell you're doing fine"* — Kai sitting at his desk, touching the collar, thinking, then leaving it, close-up.
23. *"I don't need a ring to make it official"* — Mahima's bare ring finger tapping the doorframe, then her wink to camera, extreme close-up.
24. *"Just a kiss of red on you, and baby, that's a signal"* — the print again from across the office, a slow zoom on the collar between monitors, the only red in frame.

### Verse 2 — the texts

25. *"Twelve fifteen, you text me, they saw it in the meeting"* — a café table, Mahima (out look) with a coffee, the phone buzzing face-up, over the shoulder, warm daylight.
26. *"Front desk did a double take, the intern stopped breathing"* — flashes of the meeting room: a receptionist from behind doing a double take, an intern frozen mid-sip cropped at the jaw.
27. *"Somebody from marketing said, wow, she's bold"* — the phone screen with the messages arriving (composited), her laugh, covering her mouth, close-up.
28. *"You wrote back, yeah, she is, and that's the story told"* — her typing a reply, then setting the phone down and looking out of the café window, pleased, medium.
29. *"Tried to scrub it in the bathroom, gave up by noon"* — Kai at an office bathroom sink dabbing the collar with a paper towel, making it worse, laughing at himself in the mirror, cool fluorescents.
30. *"Said, honestly, I kind of like it, then a heart, then a moon"* — his text on her screen with a heart and a moon (composited), her thumb hovering, then her smile.
31. *"So tomorrow don't reach for the darker shirt"* — a row of his shirts on a rail in the apartment wardrobe, her hand pushing a navy one aside for a white one, close-up.
32. *"I'll go a shade brighter, just to watch it work"* — four lipstick shades lined up on the café table, her picking the brightest and uncapping it, macro.

### Pre-chorus 2 — the corridor

33. *"Go on, walk the corridor, let them all stare"* — Kai walking a long glass corridor in slow motion, chin up now, colleagues staring through the glass, tracking from the front, afternoon sun.
34. *"Tell them it's a new brand, tell them you don't care"* — a faceless colleague pointing at the collar, Kai shrugging and grinning, medium.
35. *"Loosen up your tie, let that blushing show"* — his hand loosening the tie one notch, then his face, proud and pink, close-up.
36. *"I'm two miles away and I already know"* — Mahima at home not even checking the phone, smiling to herself while watering a plant, wide, warm.

### Chorus 2 — bigger, then together

37. *"Lipstick on your collar, so they know you're mine"* — a whole row of colleagues leaning in to whisper, phones up, from behind, the collar the focus across the floor.
38. *"Red on cotton white, they can read between the lines"* — reuse shot 24, the zoom tighter.
39. *"Give the office something for the group chat, honey"* — the group chat again with a photo of the collar in it (composited), someone's thumb reacting.
40. *"Let them lean and whisper, let them think it's funny"* — the front desk from behind, the receptionist turning to a colleague, a hand over a mouth.
41. *"Lipstick on your collar, wear it like a sign"* — evening, the lobby: Mahima (out look) waiting by the glass in the swing coat, golden light through the doors, wide.
42. *"Every desk on every floor can tell you're doing fine"* — the elevator opening and Kai stepping out, the print still on, seeing her, medium.
43. *"I don't need a ring to make it official"* — she reaches for his collar and straightens it instead of wiping it, close on her hands.
44. *"Just a kiss of red on you, and baby, that's a signal"* — the two of them walking out through the revolving doors into golden light, tracking from behind.

### Instrumental — the sax strut

45. Mahima walking down the street at golden hour in the swing coat, cat-eye sunglasses down, slow-motion tracking from the front.
46. A baritone sax player on a street corner, brass catching the sun, profile only, lens flare.
47. Kai leaving the building and falling into step beside her, matching stride, tracking from the side.
48. The two of them reflected in a long shop window, walking in sync, the red print and the red lip the only colour.
49. A stop on a single snap: her hand on his collar, freeze frame, then black for one beat into the bridge.

### Bridge — honest, then the flower

50. *"It was never about them, I trust you with my life"* — night, the apartment, Mahima (morning look, rollers out, hair down) sitting on the kitchen counter in his suit jacket, talking straight to him, one warm lamp, static.
51. *"You could work in a room of pretty and be fine"* — Kai across the kitchen, leaning on the fridge, listening, close-up, lamp light.
52. *"It's the way you catch your reflection in the lobby door"* — a replay of him in the lobby door glass that morning, catching his reflection and the print, medium.
53. *"And you smile like you just remembered who you're going home for"* — his small private smile in the glass, then a match cut to his face now in the kitchen, the same smile.
54. *"So keep it on, keep it on, don't wipe it away"* — her fingertip touching the print on the collar, gentle, extreme close-up.
55. *"Let it be the loudest thing you say all day"* — her hands on his lapels, foreheads close, the lamp behind them, close two-shot.
56. *"Then you came home with a flower from downstairs"* — the front door opening earlier that evening, Kai coming in with a single red flower from the stand by the entrance, the door open on blue evening, medium.
57. *"Tucked it behind my ear, said, now it's only fair"* — his hand tucking the flower behind her ear, then her face, surprised for the first time in the video, close-up, warm.

### Final chorus — both marks, the walk-in

58. *"Lipstick on your collar, so they know you're mine"* — next morning, the two of them walking into the office lobby together through the revolving doors in slow motion, Mahima (lobby look) with the flower, Kai with a fresh print, wide, bright.
59. *"Red on cotton white, they can read between the lines"* — the whole lobby turning: a security guard from behind, a courier, a receptionist, on the beat.
60. *"Flower in my hair now, so they know I'm yours"* — close-up of the red flower behind her ear, then her eyes to camera.
61. *"Two of us walking in like we own the whole floor"* — the mirrored elevator with both of them inside, ten reflections each, the red doubled, locked-off.
62. *"Lipstick on your collar, wear it like a sign"* — the elevator doors opening onto the floor and both stepping out, heads turning down the row, tracking from the front.
63. *"Every desk on every floor can tell you're doing fine"* — Kai at his desk with the flower's twin in a glass of water beside his monitor, close-up.
64. *"I don't need a ring to make it official"* — her bare ring finger resting on his collar as she leans down to say goodbye at his desk, extreme close-up.
65. *"Just a kiss of red on you, and baby, that's a signal"* — she walks back to the elevator alone, the whole floor watching her go, her wink over her shoulder, tracking.

### Post-chorus — the floor sings along

66. *"Red on your collar, ooh"* — the office from above, colleagues swaying at their desks on the beat, faces down or away, wide overhead.
67. *"Everybody knows, everybody knows"* — the front desk clapping on two and four, hands only, close-up.
68. *"Red on your collar, ooh"* — the elevator doors closing on Mahima's smile, medium.
69. *"That's how it goes, that's how it goes"* — the group chat one more time, a row of red heart reactions (composited), then Kai's grin at his screen.

### Outro — the same morning again

70. *"Seven forty-five, you're buttoning up"* — the apartment hallway a week later in the exact framing of shot 1, Kai buttoning the shirt, Mahima in the doorway with a brighter red lip already on, wide static, warm gold.
71. *"Same cold coffee in your favourite cup"* — the same mug on the same counter, the steam gone, close-up, matched to shot 2.
72. *"You lean in at the door, you tilt your head"* — at the door, he leans in and tilts his head to offer the collar himself, medium close-up.
73. *"Say, do it again, and make it a brighter red"* — she presses the print, a lipstick cap clicks, she laughs, the door closes on her satisfied face, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the lipstick cap click, the first "so they know you're mine",
the elevator freeze, the group chat, the sax entrance, "now it's only fair",
the walk-in, and the final click. At 108 BPM a bar is 2.2 s; choruses cut
on every bar, the heads turning on the downbeats.

**Collar-print challenge.** The hook is caption-ready. Post the vertical cut
of shots 3–4 into 13–16 (the kiss, the print, the elevator mirror) with
*"lipstick on your collar, so they know you're mine"* on screen and invite
couples to film the doorway kiss, the collar, and the partner's reaction at
work. The elevator freeze (shot 15) is the second shareable frame; the
outro's "do it again" (shot 73) loops straight back to shot 1.

## 6. Quality-control checklist

- Three looks in the right sections: rollers and robe for the apartment, swing coat and bouffant for the café and street, the flower from shot 57 on and never before
- Kai's lip print is on the left collar in every office shot and is never wiped off; it is fresh, not faded, in the final chorus and outro
- Red is the only saturated colour in the grade; no other red props in frame
- Colleagues never have a visible face; the work wife is seen once, from behind
- All texts, group chats and elevator floor numbers composited; no model-generated text
- The mirrored elevator has no duplicate people beyond the true reflections (Depth control)
- Shots 70–71 match shots 1–2 exactly in framing and light so the video loops
- The last shot is locked-off and holds until the audio fades