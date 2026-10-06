# Wan 2.2 Shot List — "Barefoot on the Boulevard"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
112 BPM a bar is 2.14 s, so most shots are 3–4 s and the choruses cut on the
bass hits rather than every bar.

## 1. Visual style

One street, one night, one direction of travel. The camera almost never
turns back: the whole video moves up a wide northern city boulevard from the
club end to the market end, and the grade moves with it — hard sodium orange
and black wet setts at the bottom of the street, then warmer practicals in
the middle, then daylight at the top. Reflections do the work: puddles, tram
rails, dark shop windows. Shot low and level with the road wherever
possible, because this is a video about feet. Handheld for the verses,
smooth backward-tracking for the choruses.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium orange, black wet setts, one security light | Low, static, level with the road |
| Verse 1 | Hard streetlight from above, wet ground bouncing up | Close, handheld, macro inserts |
| Pre-chorus 1 | Warmer — a busker's lamp, a car interior light | Slow push-in |
| Choruses | Orange and wet, one white light crossing frame | Smooth backward tracking at hip height |
| Verse 2 | A run of orange lamps in perspective | Fast handheld, walking pace |
| Pre-chorus 2 | Half-lit, light thrown up off a tram rail | Two static shots only |
| Instrumental | Widest, wettest, most cinematic | Footbridge wide, spins, slow motion |
| Bridge | Flashbacks cold interior white; present warm orange | Static, still, long holds |
| Final chorus | Brightest of the night, every lamp and a shopfront | Wide, road level, moving with the group |
| Post-chorus | Lamps starting to lose to the sky | Following, single figure |
| Outro | Daylight wins, streetlights switch off | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (all night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly damp from rain, evening makeup still sharp, wearing a short bronze sequinned slip dress and a black oversized blazer over it, carrying a pair of black strappy heels by their straps, bare feet, delighted unbothered expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge flashbacks only)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark hair straightened flat, heavy formal makeup, wearing a stiff pale satin dress and high heels, standing very still with her weight on one hip, polite fixed smile, realistic cinematic photography, consistent identity

**The woman with the keys** — a young woman of about the same age walking
too fast, keys laced through her fingers, denim jacket, no face-hiding
needed; she is a person, not a threat. She joins the group in the final
chorus with her hands empty.

**The lads on the corner** — faceless: shot from behind, or as three
silhouettes against a shopfront, never held for more than a beat and never
in focus.

**The busker** — an older man with a small amp, cap on, back mostly to
camera.

Objects: the **black strappy heels** swinging by their straps in every
chorus, the **blister**, the **wet tram rail**, the **car boot lid** with its
speakers turned out, the **keys through the fist**, the **market stall
frames** at dawn.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All shopfront signage, phone screens, tram destination boards and bus
numbers are composited in the edit.** Generate them blank or unlettered; the
model cannot render legible text and a city street is nothing but text.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA; keep the
flashback look visibly stiffer in the reference stills, not just differently
dressed. **OpenPose is essential** for every walking shot — a strut is the
easiest thing in this video to get wrong, and bare feet are the second — plus
the dancing on the crossing and the group walk. Depth for the long
perspective shots down the boulevard. Feet in macro should be generated as
their own stills with a hand or ankle in frame for scale, or the model
produces anatomy that will not survive a close-up. 16:9 first; 9:16 for the
strut and the shoes-off inserts, which are the shareable cuts. Wet ground is
the friend of this render: reflections hide a multitude of small errors.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–4 s.

## 4. Scene per lyric line

### Intro — wet street, buckles

1. *"Wet street shining like it's just been laid"* — low and level with the road: black wet setts and tram rails throwing orange, one puddle taking half the frame, static.
2. *"Orange in the puddles where the tram lines fade"* — a slow drift along a tram rail into the distance where the lamps fall off, the rail as a line of light.
3. *"Somebody's boot lid open with the bass turned round"* — a car with its boot lid up and the speakers turned outward, three figures around it doing nothing, medium wide from across the road.
4. *"And I'm undoing buckles, and here comes the sound"* — Mahima seated, one finger hooked into an ankle strap, working the buckle, extreme close-up on the hands and the shoe.

### Verse 1 — the shoes lose

5. *"Two in the morning and my shoes have gone traitor"* — a black strappy heel held up to the streetlight like evidence, her face soft behind it, close-up.
6. *"Four inches of glamour and a blister like a saucer"* — the blister in unflattering macro, then her expression, entirely unromantic, two-shot cut.
7. *"So I sit on a bollard with the straps in my teeth"* — she sits on a bollard with both straps gripped in her teeth, working the second buckle, medium close-up, funny and real.
8. *"And the paving is freezing and the freezing is relief"* — the first bare sole meeting cold wet paving, macro, water moving around the foot, the hook frame of the video.
9. *"Nobody's watching and the whole street can see"* — a wide of the empty boulevard with one seated figure in it, nobody else in frame, static.
10. *"I stand up and the city rearranges round me"* — slow low push-in as she rises, the camera arcing so the buildings swing behind her, held one beat after she stops moving.

### Pre-chorus 1 — the first step

11. *"There's a bassline coming out of a car door"* — an open car door with the interior lamp on and the stereo audible, seen past her hip, medium.
12. *"There's a busker packing up and starting one more"* — a busker who has already coiled his lead plugging the amp back in, back to camera, warm lamp.
13. *"I take the first step and the cold goes right through"* — her bare foot landing, then the second, low and macro, the shoes already swinging at the edge of frame.
14. *"And I have never in my life felt as good as I do"* — her face in close-up, uncomplicated delight, no irony in it, held.

### Chorus 1 — the strut

15. *"Barefoot on the boulevard, heels in my hand"* — smooth backward tracking ahead of her at hip height down the middle of the empty road, heels swinging by their straps.
16. *"Wet tram rails and the whole street's a band"* — low across the tram rails as she crosses them, orange light running along the metal, her feet in frame.
17. *"Every shop window's a mirror I can use"* — her reflection running along a row of dark shop windows, the real her out of frame for two seconds, tracking.
18. *"Every kerb is a catwalk and I'm making the news"* — a kerb walked heel to toe like a beam, arms out, low angle from the gutter.
19. *"Barefoot on the boulevard, two in the morning"* — a tram passing behind her, empty, its interior white light crossing the frame, static wide.
20. *"The city is my dance floor and it's only just warming"* — a spin in the middle of the road, blazer opening, orange lights streaking, handheld.
21. *"Don't need a lift and I don't need a plan"* — a cab slowing beside her; she waves it on without breaking step; the cab pulls away, medium tracking.
22. *"Barefoot on the boulevard, heels in my hand"* — the heels swinging in close-up against the moving street behind them, macro, cut on the bass.

### Verse 2 — spoken, then rapped

23. *"Right, shoes in the left hand and the phone in the right"* — both hands in one frame, shoes in the left, phone dark in the right, walking, static on the hands.
24. *"Half a mile of orange lamps and I am taking the lot tonight"* — a long perspective shot straight up the boulevard, a run of orange lamps to a vanishing point, her small in the middle of it.
25. *"Past the tram stop, past the cabs with their engines still humming"* — a tram shelter with one person asleep sitting up, then a rank of cabs with fogged windows and engines running, whip pan between them.
26. *"Past the lads on the corner who go quiet when they see me coming"* — three silhouettes against a shopfront who stop talking, shot from behind and never in focus, held for exactly one beat.
27. *"There's a girl walking quick with her keys through her fist"* — a young woman walking too fast, keys laced through her fingers, seen from behind at her own pace, handheld.
28. *"So I fall in beside her and we chat till the fear is dismissed"* — Mahima falling into step beside her and saying something ordinary; both their shoulders drop; two-shot from the side, walking.
29. *"Cobbles like a drum kit and the kerb stones like a snare"* — bare feet on wet setts cut hard on the snare, four quick macro shots inside one lyric line.
30. *"I am not going home yet, I am going everywhere"* — the two of them walking on together into the long orange perspective, wide from behind.

### Pre-chorus 2 — bass and voice

31. *"I take the next step and the cold's nothing new"* — a single bare foot landing squarely on a wet metal tram rail, macro, light thrown up under it.
32. *"And there's nobody walking this city like I do"* — her face in profile crossing frame right to left, static camera, one lamp doing all the work.

### Chorus 2 — wider, busier

33. *"Barefoot on the boulevard, heels in my hand"* — the backward-tracking frame again, but with the street alive behind her and a second figure in step.
34. *"Wet tram rails and the whole street's a band"* — reuse shot 16, wider, both women crossing the rails.
35. *"Every shop window's a mirror I can use"* — the shop-window reflection now containing two of them, tracking.
36. *"Every kerb is a catwalk and I'm making the news"* — the woman with the keys tries the kerb walk and laughs, medium, handheld.
37. *"Barefoot on the boulevard, two in the morning"* — a night bus going past with two passengers looking out at them, static.
38. *"The city is my dance floor and it's only just warming"* — both of them dancing badly at a pedestrian crossing while the light changes twice, wide.
39. *"Don't need a lift and I don't need a plan"* — a phone raised, looked at, and put away without unlocking it, close-up.
40. *"Barefoot on the boulevard, heels in my hand"* — four shoes now swinging, two pairs, one in each woman's hand, macro against the moving road.

### Instrumental — the boulevard as a dance floor

41. Bare feet dancing on a wet zebra crossing, filmed from road level between the stripes, slow motion on the slap-bass hits.
42. A street sweeper's brushes turning in slow motion, water fanning out under a streetlight.
43. The busker playing to nobody, then two of them arriving to dance in front of him; he does not stop, medium.
44. A handheld spin directly under a tram wire, the lights streaking into rings overhead, camera turning with her.
45. A wide from a footbridge over the whole empty boulevard: one small figure dancing in the middle of a mile of orange, the most cinematic frame of the video, held long.

### Bridge — the flashbacks and the fist

46. *"I spent years in shoes that somebody else chose"* — cold interior white: a younger, stiffer version of her standing perfectly still at the edge of a room in a pale satin dress, static, two seconds.
47. *"Standing very still in a corner in a pose"* — the flashback continues: weight on one hip, a polite fixed smile arriving on request, close-up.
48. *"Held my breath through a hundred nights like this"* — a phone in a clutch bag on a table, unanswered, screen dark, macro, cold light.
49. *"Waiting on a lift, waiting to be asked, waiting to be missed"* — a coat held open for her by somebody out of frame; she steps into it; the arms are never given a face.
50. *"Now the straps are in my fist and the street is in my chest"* — hard cut back to warm orange: her fist tightening on the straps, macro, then her chest rising with a breath.
51. *"And the walking is the best part, never was the dress"* — a long still wide of her standing alone in the middle of the road, arms down, nothing moving but her hair, held.

### Final chorus — six of them

52. *"Barefoot on the boulevard, heels in my hand"* — six women walking abreast down the middle of the road, shoes swinging from every hand, road-level wide from behind.
53. *"Wet tram rails and the whole street's a band"* — the group crossing the rails together, twelve bare feet, low macro.
54. *"Every shop window's a mirror I can use"* — the whole group reflected in a lit shopfront, all of them checking themselves at once, tracking.
55. *"Every kerb is a catwalk and I'm making the news"* — the group taking a bus lane like a stage, one after another down the painted line, wide.
56. *"Barefoot on the boulevard, two in the morning"* — the woman with the keys among them, hands now empty and swinging, close-up on the empty hands.
57. *"The city is my dance floor and it's only just warming"* — a jump on the horns' octave lift, all six off the ground at once, freeze for two frames, wide.
58. *"Six of us laughing with our shoes in our hands"* — faces in a row, laughing at something we never hear, tracking along the line.
59. *"Owning the middle of the road where the buses ran"* — a bus waits behind them and nobody hurries; the driver is laughing too, wide from the bus's eyeline.
60. *"Don't need a lift and I don't need a plan"* — the group splitting around a bollard and re-forming without breaking stride, wide.
61. *"Barefoot on the boulevard, heels in my hand"* — the brightest frame of the night: every lamp, a lit shopfront and one set of headlights on six women in the road.

### Post-chorus — the crossroads

62. *"Heels in my hand and the horns coming in"* — a crossroads: the group thinning, everyone taking a different street, wide from above.
63. *"Cold on the soles and it feels like a win"* — hands raised in goodbye without anyone turning round, three quick cuts.
64. *"Heels in my hand and the long road home"* — Mahima alone again on a long straight road, small in frame, walking away from camera.
65. *"Never felt safer than walking alone"* — her face, calm, in step with the horn riff, close-up, the lamps starting to lose to the sky behind her.

### Outro — dawn at the market

66. *"Sky going pale over the market roof"* — a pale sky over a market roof, stall frames going up, crates being wheeled, wide, first daylight.
67. *"Straps in my fist and a mile of proof"* — her fist with the straps still in it, knuckles, the shoes hanging, macro in daylight for the first time.
68. *"Feet are a state and the morning's begun"* — her feet, filthy and unbothered, walking past a stall being built, low tracking.
69. *"Barefoot on the boulevard, and I'm not done"* — final shot: locked-off wide back down the whole boulevard as the streetlights switch off one after another in a run toward camera, her small figure still walking away. Hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first buckle, the first bare sole on paving (shot 8), the
stand-up (shot 10), each "barefoot on the boulevard", the falling-into-step
(shot 28), the footbridge wide (shot 45), the fist (shot 50), the six-abreast
entrance (shot 52) and the streetlights going out. At 112 BPM a bar is
2.14 s; the choruses cut on the slap-bass hits rather than every bar, and the
rap verse cuts on the internal rhymes, not the line ends.

**The shoes-off challenge.** Shots 5–15 recut vertically are the shareable
fifteen seconds: heel, blister, buckle, bare sole, stand-up, strut. Invite
people to post the moment they gave up on their shoes, with the horn riff
over it. The six-abreast walk (shot 52) is the second shareable frame.

**Caption cut:** shots 64–65 with *"Never felt safer than walking alone."*

## 6. Quality-control checklist

- Two looks only: the bronze dress and blazer all night, the stiff pale satin dress in the bridge flashbacks and nowhere else
- She is barefoot from shot 8 to the end and the heels are visible in her hand in every chorus frame
- The camera travels up the street in one direction; no shot looks back down the boulevard until the final locked-off wide, which is the point of it
- The lads on the corner are faceless and out of focus and held for exactly one beat; the woman with the keys has a face and gets more screen time than they do
- The group only grows: one, then two at chorus two, then six at the final chorus, then apart again at the crossroads
- All shopfronts, tram boards, bus numbers and phone screens composited; no model-generated text
- Feet generated as their own stills with ankle or hand in frame for scale; no macro foot shot goes out without a hand check
- The grade moves orange to daylight and never back; the streetlights are off in the last frame
