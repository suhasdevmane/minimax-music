# Wan 2.2 Shot List — "Thank You for Leaving"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
84 BPM a bar is 2.86 s, so most shots run 3–6 s and the choruses cut every
bar or two.

## 1. Visual style

A gratitude ballad in daylight. Two worlds: the **memory** is one winter
night on a train platform, cold sodium orange and blue, steam and hard
shadow; the **present** is a small apartment and a city in clean, warm
daylight that gets brighter as the year passes. The **plant is the clock**:
it sits on the same windowsill in every apartment shot and is visibly
bigger each time we return, from half-dead to touching the ceiling. No
tears anywhere in the video. Handheld and close in the apartment, tracking
and wide in the city.

| Section | Grade | Camera |
|---|---|---|
| Intro / the box | Soft daylight, one window, clean | Overhead, close, static |
| Platform memories | Cold sodium orange and blue, steam | Wide, static, from behind her |
| Early apartment | Grey daylight, one streetlight at night | Slow pans |
| Pre-choruses (months) | Grey to gold across the cuts | Locked-off windowsill, jump cuts |
| Choruses (city) | Full morning sun, slightly overexposed | Tracking from the front |
| Verse 2 / supermarket | Bright afternoon; flat white made warm | Handheld, intimate |
| Instrumental | Every season, ending gold | Time-lapse and slow motion |
| Bridge | Warm lamp, soft shadows; one cold flash | Static close, straight to camera |
| Final chorus / post-chorus | Golden, wide, warm | Moving, wider |
| Outro | Clear morning light, white and warm | Slow, calm, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (platform memory, winter)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose under a dark wool beanie, no makeup, wearing a long camel winter coat with the sleeves pulled over her hands and a grey scarf, hurt frozen expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (early apartment, the first months)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely, no makeup, wearing an oversized grey sweatshirt and black leggings, tired quiet expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (present, arrived)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and glossy, light natural makeup, wearing a cream linen shirt tucked into high-waisted rust-coloured trousers and small gold hoops, calm open smiling expression, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — never shown clearly: a back walking away down a platform, a shoulder in a carriage doorway, a hand on a bag strap. Never a face.
> a man in his twenties, back to camera or face out of frame, dark coat, holdall over one shoulder

**The sister** — warm, a little older than Mahima, seen once in the supermarket. Give her a face; she is kind.
> a woman in her late twenties, dark hair in a low bun, denim jacket, warm open face

**The friend with a key** — one young woman, casual, seen in the second pre-chorus and the instrumental.

Objects: the **cardboard box** (his things), the **plant** (a pothos or monstera; half-dead in the first apartment shot and visibly larger every time it appears, brushing the ceiling by the final chorus), the **crack in the wall** (painted over in the pre-chorus), the **spare chair**, the **two coffees**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the tutorial video, the radio display and any signage are
composited in the edit.** Generate screens as lit blank panels and overlay
the UI in post — the model cannot render legible UI or text, and platform
signs and departure boards must never be readable.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless. Keyframes first; OpenPose for the
running shot and the spin on the rug; Depth for the apartment compositions
and the platform wides. 16:9 first; 9:16 for the windowsill time-lapse and
the walk-out-into-sun cut, which are natural vertical content. Animate
conservatively: breath in cold air, a leaf unfurling, a curtain moving,
water from a can, a hug.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–6 s.

## 4. Scene per lyric line

### Intro — the box on the floor

1. *"I found the box of your things last week"* — overhead: Mahima (present look) sitting cross-legged on bare floorboards in a small bright apartment with an open cardboard box, soft window light, static.
2. *"Sat on the floor and I didn't even weep"* — her face, dry-eyed, curious, looking into the box like it belongs to a stranger, close-up, warm daylight.
3. *"Just a jacket, a charger, a ticket stub"* — three cuts on the beat: her hands lifting a dark jacket, a coiled phone charger, a folded train ticket, macro.
4. *"And a version of me I've stopped dreaming of"* — her setting the ticket down and looking up at the window, the plant huge in the corner of frame, slow push-in.

### Verse 1 — the platform, the bare apartment

5. *"The night you left, the platform was cold"* — memory: a near-empty night train platform in winter, Mahima (winter look) small in a wide frame, breath in the air, cold sodium light, static.
6. *"You didn't look back, and I didn't hold"* — from behind her: the ex walking away down the platform toward a carriage door, holdall on his shoulder, never turning, his face never shown.
7. *"I stood there shaking with my hands in my sleeves"* — close-up of her hands pulled up inside her coat sleeves, shaking, the scarf, steam drifting past.
8. *"Thinking nobody survives when the whole train leaves"* — the train pulling out, its lights sliding across her face, then the platform empty around her, wide, slow.
9. *"I moved to a place with a crack in the wall"* — the new apartment, almost empty: a slow pan across a crack running up a bare wall, grey daylight.
10. *"One chair, one plate, one mattress, that's all"* — three cuts on the beat: one chair, one plate on a counter, a mattress on the floor, static.
11. *"Bought a plant from the corner store, half dead"* — a corner-shop bucket of drooping plants, Mahima (early look) picking the saddest one, close-up on her hand and the wilted leaves.
12. *"Put it by the window and I went to bed"* — her setting the plant on the windowsill, then lying down on the mattress in her coat, a single streetlight through the glass, wide, night.

### Pre-chorus 1 — the months

13. *"I hated you in March, I'll be honest, it was rough"* — the locked-off windowsill: the plant with one new leaf; then Mahima on the floor beside it with her head in her hands, grey light.
14. *"By June I was running, and by August I was up"* — jump cuts on the same frame: her lacing running shoes at dawn by the window; her dancing while cooking, the plant bigger each time, light going gold.
15. *"Turns out the silence you left me had room"* — her rolling paint over the crack in the wall, the wall going clean, medium.
16. *"For all of the things I never got to bloom"* — the windowsill again, the plant now clearly alive and green, morning sun through the leaves, macro.

### Chorus 1 — out into the light

17. *"Thank you for leaving, I finally arrived"* — Mahima (present look) pushing through the building's front door and coming down the steps into full morning sun, tracking from the front, slightly overexposed.
18. *"You closed a door and I walked out into the light"* — the door swinging shut behind her, her not looking back, sun flare, medium.
19. *"You took the girl who waited by the phone"* — a two-second cold flash of the winter platform, her small and still, then back to the bright street.
20. *"And left me with a woman who can make it on her own"* — her crossing a wide street alone, head up, shoulders easy, wide tracking.
21. *"Thank you for leaving, I mean it, no spite"* — her face close, a real smile, no edge in it, handheld.
22. *"I'd shake your hand on that platform tonight"* — her hand extended forward as if for a handshake, then dropping as she laughs at herself, medium.
23. *"You thought you were the ending, you were only the ride"* — a train crossing a bridge in the distance behind her as she walks, unbothered, wide.
24. *"Thank you for leaving, I finally arrived"* — her stopping at a corner, closing her eyes in the sun for one beat, close-up.

### Verse 2 — the leaf, the sink, the sister

25. *"The plant grew a leaf in the middle of May"* — macro of a new leaf unfurling on the sill in time-lapse, bright afternoon.
26. *"Said, look at you, out loud, to a plant, okay"* — Mahima talking to the plant, catching herself, shrugging at nobody, medium, warm.
27. *"Learned to fix the sink from a video"* — her under the kitchen sink with a wrench, a phone propped against a cupboard playing a tutorial (screen composited), water spraying, her laughing.
28. *"Learned to fall asleep with the radio low"* — night: a small radio glowing on the floor by the mattress, her asleep, calm, one warm lamp.
29. *"Ran into your sister at the grocery store"* — a supermarket aisle by the fruit, the sister turning and her face lighting up, a surprised real hug, handheld.
30. *"She hugged me and said, you seem lighter than before"* — the sister holding her at arm's length, saying something kind, Mahima's eyes shining but dry, two-shot.
31. *"I said, I am, and I didn't have to try"* — Mahima nodding, meaning it, a small shrug, close-up, the flat white light made warm by her face.
32. *"I didn't ask about you, and she didn't say why"* — a beat where the question hangs and isn't asked; they part with a wave down the aisle, wide.

### Pre-chorus 2 — the place fills up

33. *"I hated you in March, I'll be honest, it was rough"* — the apartment now: a rug, a lamp, books, a second chair, the same windowsill frame, golden late afternoon.
34. *"By June I was running, and by August I was up"* — the friend letting herself in with her own key, holding takeaway bags, Mahima looking up and grinning, medium.
35. *"Now my place has got a rug and a friend with a key"* — the two of them on the rug with the food, laughing, the key tossed onto the table, handheld.
36. *"And a window full of green that's growing just for me"* — the window crowded with plants, the first one tallest in the middle, sun through the leaves, slow push-in.

### Chorus 2 — the city, alone and not lonely

37. *"Thank you for leaving, I finally arrived"* — Mahima walking through a park in full sun, headphones in, tracking from the side.
38. *"You closed a door and I walked out into the light"* — reuse shot 18, tighter on the door closing.
39. *"You took the girl who waited by the phone"* — her at a coffee window ordering for one, easy, not checking a phone, medium.
40. *"And left me with a woman who can make it on her own"* — her carrying a bag of groceries up her building's stairs two at a time, low angle.
41. *"Thank you for leaving, I mean it, no spite"* — reuse shot 21, a little wider, the street behind her alive.
42. *"I'd shake your hand on that platform tonight"* — the platform seen from a bridge above in daylight, empty and harmless, a train sliding through, wide.
43. *"You thought you were the ending, you were only the ride"* — her on the bridge above the platform looking down, then walking on, tracking from behind.
44. *"Thank you for leaving, I finally arrived"* — her face turned up to the sun on the bridge, eyes closed, a breath, close-up.

### Instrumental — the year, wordless

45. The windowsill in time-lapse: the plant across four seasons, fast, the light changing behind it.
46. Mahima painting the whole wall now, sleeves rolled, music on, wide.
47. Her running along a river path at dawn, breath steady, tracking from the side, gold.
48. The spare chair being carried up the stairs by Mahima and the friend, laughing, handheld.
49. Dinner at the table, two chairs, two plates, the friend mid-story, warm lamp.
50. A pause: Mahima alone at the window watering the plant, calm, slow push-in — the cut into the bridge.

### Bridge — honest, then the release

51. *"If you're wondering if I'm bitter, come and see"* — Mahima at the kitchen table at evening, talking almost straight to camera, warm lamp, static close.
52. *"There's a spare chair at my table that wasn't there for me"* — her hand resting on the back of the second chair, close-up on the hand and the chair.
53. *"I don't play our song, I don't drive down your street"* — two quick cuts: a car passing a street sign without turning (sign unreadable); a thumb skipping a track on a phone without a flinch (screen composited).
54. *"I don't wish you badly, I wish you well, and I mean it"* — her face, steady and kind, a small nod, close-up.
55. *"Some people are a home, and some people are a train"* — cold flash: the winter platform, the train pulling away, her standing there, wide.
56. *"You pull out of the station and don't come back again"* — match cut: the same spot on the platform in summer, Mahima (present look) walking past it without stopping, wide.
57. *"I'd have waited on that platform till my hair turned grey"* — the winter her on the bench, alone, small, the frame holding, then a slow dissolve.
58. *"So thank God, thank you, thank the day you pulled away"* — the present her at the table, eyes closed, a breath, then a laugh breaking out, close-up, the cut landing on the word thank.

### Final chorus — the plant touches the ceiling

59. *"Thank you for leaving, I finally arrived"* — wide from the apartment door: the whole room alive, rug and books and lamp, the plant's leaves brushing the ceiling, Mahima in the middle of it, golden.
60. *"The plant's touching the ceiling and I'm doing alright"* — her reaching up to touch the highest leaf, then the ceiling, laughing, low angle.
61. *"You took the girl who waited by the phone"* — reuse shot 19, the flash even shorter, the return to gold faster.
62. *"And left me with a woman who can make it on her own"* — her at the stove, dancing a little, the friend arriving behind her, wide handheld.
63. *"Thank you for leaving, I mean it, no spite"* — night: Mahima on the platform bench with two takeaway coffees, calm, medium.
64. *"I'd buy you a coffee on that platform tonight"* — her setting one coffee down on the bench and standing, keeping the other, close-up on the cup.
65. *"You thought you were the ending, you were only the ride"* — her walking away up the platform stairs with her coffee as a train arrives behind her, wide, warm platform light.
66. *"Thank you for leaving, I finally arrived"* — her at the top of the stairs stepping out into a bright night street, city lights, a small smile, tracking.

### Post-chorus — watered

67. *"I arrived, I arrived"* — morning: her watering the plant, the can, the soil, water catching the light, macro.
68. *"Watered myself and I came back alive"* — her drinking a glass of water at the window, sun on her face, eyes closed, close-up.
69. *"I arrived, I arrived"* — her spinning once on the rug, arms out, the room going by, wide handheld.
70. *"Thank you for leaving, look at me thrive"* — her landing the spin facing the window, the plant filling the frame beside her, hold.

### Outro — the box on the bench

71. *"I found the box of your things last week"* — daylight platform: Mahima (present look) walking along it carrying the cardboard box, calm, tracking from the side.
72. *"Left it on the platform for the city to keep"* — her setting the box down on the bench, straightening, one hand resting on it for a second, medium.
73. *"Kept the plant, kept the place, kept the sky"* — the windowsill, the plant in full sun, the curtain moving in a breeze, static, clean.
74. *"Thank you for leaving, I finally arrived"* — final shot: her walking away up the platform stairs into white morning light without looking back, the box small on the bench behind her, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the train pulling out, each "I finally
arrived", the paint roller over the crack, the supermarket hug, the
instrumental, "thank the day you pulled away", the ceiling touch, the
coffee on the bench and the final stair. At 84 BPM a bar is 2.86 s.

**The plant challenge.** The pre-chorus is caption-ready. Post the vertical
windowsill time-lapse (shots 13–16 and 45) with *"I hated you in March, by
August I was up"* on screen and invite people to post their own "the plant I
bought the week it ended" then-and-now. The walk-out-into-sun cut (shots
17–24) is the shareable glow-up edit with *"you were only the ride"* as the
caption line.

## 6. Quality-control checklist

- Three looks in the right sections: camel coat and beanie only on the winter platform; grey sweatshirt only in the early apartment (shots 11–16, 25–28); linen shirt and rust trousers from shot 17 on and in every city shot
- The ex never has a visible face; the sister and the friend do
- The plant is bigger every time the windowsill appears, in order, and touches the ceiling by shot 59; it is never smaller than in the previous windowsill shot
- The crack in the wall is visible in shots 9–13 and painted over from shot 15 on
- No tears in any shot; the emotion is calm and warm throughout
- All screens and signage composited; no readable departure boards or street signs
- No distorted hands, especially the wrench, the watering can and the coffee cups
- The last shot is locked-off and holds until the audio fades
