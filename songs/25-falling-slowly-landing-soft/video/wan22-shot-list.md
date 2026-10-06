# Wan 2.2 Shot List — "Falling Slowly, Landing Soft"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
80 BPM a bar is 3.0 s, so most shots run a full bar or two and the choruses
breathe rather than cut fast.

## 1. Visual style

A slow-motion, pastel romance. Two worlds: the **guarded present** at the
start is muted grey-blue with her coat on and doors in frame; the **caught
present** is blush, sage and cream with feathers drifting through it. The
**coat is a character** — buttoned in the intro, dropped in the first
chorus, hung on his hook in the post-chorus, gone from the outro. The
**feathers** appear only when she is caught. Camera moves are slow and
mostly locked-off; the slow motion does the work.

| Section | Grade | Camera |
|---|---|---|
| Intro / verse 1 present | Muted grey-blue, soft overcast | Static two-shots |
| Memory of the old fall | Desaturated, flat, cold | Static, faceless |
| Pre-choruses | Pastel morning warming | Slow tilts |
| Choruses (the catches) | Blush, sage, cream, feathers | Slow-motion, side-on and overhead |
| Verse 2 | Warm porch light, cream daylight | Locked-off, repeated framings |
| Instrumental | Near-white pastel | Macro, very slow |
| Bridge | One warm lamp, soft shadow | Static, slow push-in |
| Final chorus / post-chorus | Brightest pastel daylight, hallway warmth | Slow overhead pull-up, macro |
| Outro | Pale dawn | Overhead, static, hold |

## 2. Character bible — paste into every prompt

**Mahima** (guarded, intro through pre-chorus 1)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose over one shoulder, minimal natural makeup, wearing a long camel wool coat buttoned to the collar over a cream knit dress, guarded watchful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (caught, choruses and verse 2)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and windblown, light natural makeup, wearing a cream knit dress with no coat, open laughing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge / outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely, light natural makeup, wearing a soft sage-green cardigan over a white top, calm resolved expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a charcoal crew-neck jumper and dark jeans, patient warm expression, hands often open and relaxed, realistic cinematic photography, consistent identity

**The ex** — never shown clearly: a back walking away down a hallway, a hand leaving a door open. Desaturated. Never a face.
> a man's back walking away down a grey hallway, dark jacket, face never visible

Objects: the **camel coat**, the **mug of tea**, the **porch light**, the
**feathers** (white, drifting, only in catch shots), the **coat hook** by
his door.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, notifications, chats, search bars and story views are
composited in the edit.** Generate the phone as a lit blank screen in her
hand and overlay the UI in post — the model cannot render legible UI. The
coffee-cup scribble in verse 2 must be an illegible scrawl, never a word.

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

Most shots 3–5 s. For this song specifically: OpenPose on every trust fall
(the backwards fall, the catch, the forward fall in the bridge, the jump in
the final chorus) — two bodies in contact is where the model invents limbs.
Feathers are best added as a compositing layer over a clean plate rather
than prompted; if prompted, keep them few and large.

## 4. Scene per lyric line

### Intro — coat on, hand on the door

1. *"I kept my coat on for the first three dates"* — a pale pastel café at dusk, Mahima (guarded look) sitting opposite Kai with her camel coat buttoned to the collar, medium two-shot from the side, soft grey window light, static.
2. *"Hand on the door in case I had to leave"* — close-up of her hand resting on her bag strap, then drifting to the café door handle as they stand, muted grey-blue.
3. *"I said, I don't do the falling anymore"* — her face across the table, saying it without looking up, close-up, one eye flicking to the door.
4. *"You said, that's fine, I'll wait while you breathe"* — Kai's face, unhurried, a small nod, his hands staying flat on the table, close-up, warm against the grey.

### Verse 1 — the old fall, the flinch, the tea

5. *"The last one dropped me from a height I can't name"* — memory, desaturated: a man's back walking away down a grey hallway, a door left open behind him, static, cold and flat.
6. *"I hit so hard I learned to walk on glass"* — memory: Mahima alone on a hallway floor, coat on, knees up, face turned from camera, the open door beyond her, wide static.
7. *"When you reached for me, I flinched before you touched"* — present, a park path: Kai reaching to brush a leaf off her shoulder and her flinching, slow motion, extreme close-up on her shoulder and his hand stopping in the air.
8. *"You smiled and said, we've got time, there's no rush"* — Kai's face, no offence taken, a small smile, his hands going back into his pockets, close-up, overcast daylight.
9. *"You never asked why my back's against the wall"* — her flat at evening, Mahima sitting on the floor with her back pressed to the wall, coat still on, wide static, one warm lamp.
10. *"You brought me tea and sat a little further off"* — Kai setting a steaming mug beside her and sitting down a metre away, also on the floor, the gap between them in frame, same wide framing.
11. *"You learned the way I go quiet when I'm scared"* — close-up of her face in the lamp light, eyes down, silent, then a glance at him.
12. *"You got quiet too, till the quiet wasn't hard"* — the same wide framing dissolving across three evenings, different clothes, the gap between them shrinking each time, the tea always there.

### Pre-chorus 1 — the hundred exits, then looking down

13. *"I built a hundred exits, drew them in my head"* — her point of view scanning her flat: the front door, the window, the stairwell, each lingering a beat, slow pans.
14. *"Every door had a plan, every plan had a name"* — close-up on her eyes moving from exit to exit, jaw set, the coat collar up.
15. *"Then I looked down one morning, feet not touching ground"* — morning, the kitchen: a slow tilt down her body to her bare feet hanging a foot above the tiles, weightless, pastel light through thin curtains.
16. *"And I realised I'd been falling all along"* — her face, startled, the beginning of a laugh, close-up, the first warm light of the video.

### Chorus 1 — the catch

17. *"I was falling slowly, you made me land soft"* — the hero image: a park lawn under a soft grey sky, Mahima (caught look, coat still on for now) standing with her back to Kai, arms crossed over her chest, letting herself fall backwards in slow motion, side-on wide.
18. *"Feather on a pillow, coat I finally took off"* — Kai catching her, then an overhead of her lying in his arms on the grass as white feathers drift down and settle on her coat, slow motion.
19. *"Braced for the crash, braced for the drop"* — close-up of her arms still crossed tight over her chest in his arms, then loosening, feathers on her sleeve.
20. *"I was falling slowly, you made me land soft"* — her unbuttoning the camel coat and letting it slide off onto the grass, the cream dress underneath, medium, pastel daylight.
21. *"No sirens, no shatter, no sorry on the floor"* — the two of them lying back on the grass, nothing broken, her laughing up at the sky, overhead.
22. *"Just your hand in my hair, your voice saying, more"* — extreme close-up of his hand in her hair, her eyes closing, feathers drifting through the frame.
23. *"I was falling slowly, but I never felt the ground"* — a slow-motion replay of the backwards fall from a new angle, low on the grass, her hair fanning out.
24. *"You made me land soft, you caught me coming down"* — the coat lying on the grass with feathers settling on it, then her face over his shoulder, grinning, medium.

### Verse 2 — coffee, porch light, habits

25. *"You memorised my coffee, then you memorised my fears"* — a takeaway coffee set down in front of her with an illegible scribble on the cup, her small surprised smile, close-up, cream daylight.
26. *"Don't take it personal when I need a night alone"* — Mahima alone on her own sofa at night, phone lit with a short kind message (composited), a soft exhale, medium, warm lamp.
27. *"Porch light on like a question I can answer"* — Kai's porch light glowing against blue dusk, locked-off, then the same frame at midnight, the sky darker.
28. *"Any hour I decide to come home"* — the same porch frame at two in the morning, Mahima walking up the path, the light still on, the door opening for her, wide static.
29. *"I still check the exits, only out of habit"* — a bright room, her hand reaching out for a wall that isn't there, then laughing at herself, medium, full soft daylight.
30. *"Like reaching for a wall in a room full of light"* — Kai standing beside her doing nothing, just there, the space between them a hand's width, two-shot.
31. *"You don't try to fix me, you just stand closer"* — a tiny trust fall in the living room, a foot of drop, his hands ready, both of them grinning, slow motion, medium.
32. *"And the closer you stand, the further I can fall"* — the same living-room fall from further back, a bigger drop this time, his catch easy, wide.

### Pre-chorus 2 — one open sky

33. *"So I stopped counting doorways, stopped rehearsing goodbye"* — the same point-of-view scan of her flat as shot 13, but the camera never lingers on the doors, drifting past them.
34. *"Let the hundred exits blur into one open sky"* — a slow tilt up through the window to pale open sky, clouds moving, soft focus on the frame edges.
35. *"I looked down this morning, feet not touching ground"* — her bare feet hanging above the kitchen tiles again, the same tilt as shot 15, brighter light.
36. *"And I laughed, cause I'd been falling all along"* — her laughing out loud alone in the kitchen, head back, close-up, bright pastel morning.

### Chorus 2 — everywhere he catches her

37. *"I was falling slowly, you made me land soft"* — a beach at low tide, Mahima falling backwards into Kai's arms on wet sand, feathers drifting, slow motion, wide.
38. *"Feather on a pillow, coat I finally took off"* — reuse shot 18, tighter on her face in his arms.
39. *"Braced for the crash, braced for the drop"* — a rooftop at dusk, the backwards fall again, the sky blush and lavender behind them, side-on.
40. *"I was falling slowly, you made me land soft"* — the catch on the rooftop, feathers against the dusk sky, overhead.
41. *"No sirens, no shatter, no sorry on the floor"* — the camel coat left hanging on a park bench, forgotten, nobody near it, static.
42. *"Just your hand in my hair, your voice saying, more"* — reuse shot 22, on the beach, wind in her hair.
43. *"I was falling slowly, but I never felt the ground"* — a series of three catches cut on the beat: park, beach, rooftop, each from a new angle.
44. *"You made me land soft, you caught me coming down"* — the two of them walking away from the park bench and the coat, her arm through his, tracking from behind, pastel.

### Instrumental — feathers, no lyrics

45. A single white feather falling the whole length of a pale stairwell, macro, near-white light, very slow.
46. Mahima lying on the park grass looking up while feathers drift down onto her face, eyes open, overhead, slow motion.
47. Kai's hands, open, palms up, waiting, extreme close-up, soft daylight.
48. The porch light at dawn being switched off from inside because she's already there, the window warm behind it, locked-off.
49. A slow fade from near-white to a single warm lamp in a dark room, the cut into the bridge.

### Bridge — arms crossed, then arms open

50. *"I used to think love meant bracing for the fall"* — night, Kai's living room, one lamp: Mahima (bridge look) standing in the middle of the room with her arms crossed tight over her chest, eyes closed, wide static.
51. *"Arms crossed over my chest, waiting for the sound"* — slow push-in on her closed eyes and crossed arms, the old bracing pose, soft shadows.
52. *"You never let me hit, you never let me break"* — Kai behind her, arms wide open, waiting, not touching, medium from the side.
53. *"You kept your arms wide open till I came down"* — her arms slowly uncrossing, hands dropping to her sides, close-up.
54. *"Here's the thing I never said to anyone before"* — her turning to face him, eyes open now, close-up on her face as she speaks.
55. *"Not scared of the height, not scared of the drop"* — a wide two-shot, her stepping toward him, the lamp light warming as the strings enter.
56. *"If I'm falling for you, then I'm falling for good"* — she falls forward this time, not backward, eyes open, into his chest, slow motion, wide.
57. *"I know the way you catch, I'll land soft"* — both of them on the floor, laughing, the lamp on them, feathers appearing for the first time indoors, medium.

### Final chorus — the jump

58. *"I was falling slowly, you made me land soft"* — the park lawn in the brightest pastel daylight of the video, Mahima (caught look) running at Kai and jumping, slow motion, wide.
59. *"Feather on a pillow, coat I finally took off"* — he catches her and they both go down onto the grass in a small avalanche of feathers, slow motion, side-on.
60. *"No bracing for the crash, no bracing for the drop"* — close-up of her arms, not crossed, wrapped around his neck as they fall.
61. *"I was falling slowly, you made me land soft"* — the two of them landing on the grass, feathers everywhere, overhead.
62. *"No sirens, no shatter, no sorry on the floor"* — their faces close, both grinning, her hair across his arm, extreme close-up, soft haze.
63. *"Just your hand in my hair, your voice saying, more"* — his hand in her hair on the grass, her eyes closed, a feather landing on her cheek.
64. *"I was falling slowly, now I'm lying on the ground"* — a slow overhead pull-up of the two of them on the grass surrounded by feathers, not getting up.
65. *"You made me land soft, and I'm staying where I'm found"* — the overhead continuing to rise until the lawn fills the frame, the two small figures still, no coat anywhere.

### Post-chorus — coat on the hook

66. *"Land soft, land soft, you made me land soft"* — Kai's front hallway at evening, the camel coat being hung on the hook by the door, macro on the hook, warm lamp.
67. *"Coat off at the door, both hands off the lock"* — her hand resting on the door lock and then leaving it without turning it, extreme close-up.
68. *"Land soft, land soft, you made me land soft"* — a single white feather on the doormat, macro, then her feet stepping over it into the flat.
69. *"Never felt the ground, only felt you catch"* — her walking away from the door down the hallway without looking back at it, the coat on its hook in the foreground, static.

### Outro — dawn, the grass

70. *"If you see me falling, don't run, don't shout"* — pale dawn, the park empty, Mahima (bridge look) lying alone on the grass, eyes closed, calm, a single feather on her chest, overhead static.
71. *"Don't bring a net, don't brace, don't work it out"* — Kai's shadow entering the frame across the grass, unhurried, the overhead holding.
72. *"Just be exactly where you've been this whole time"* — Kai lying down next to her on the grass, both on their backs, side by side, overhead static.
73. *"Cause I was falling slowly, and I landed soft"* — final shot: her hand finding his on the grass between them, fingers closing, the overhead holding through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "land soft", the first backwards
fall (shot 17), the instrumental, "If I'm falling for you, then I'm falling
for good", the jump (shot 58), the coat on the hook, and the final "soft."
At 80 BPM a bar is 3.0 s; the choruses cut every bar or two, the verses hold
longer.

**Land-soft challenge.** Post the vertical cut of chorus 1 (shots 17–24) —
the slow-motion backwards fall, the catch, the feathers — with *"I was
falling slowly, you made me land soft"* on screen, and invite couples to
film their own trust fall and catch. The forward fall in the bridge (shot
56) is the second shareable frame; the hand on the grass (shot 73) is the
quote card.

## 6. Quality-control checklist

- Three looks in the right sections: camel coat buttoned from shot 1 until it comes off in shot 20; cream dress with no coat through the choruses and verse 2; sage cardigan for the bridge and outro
- The coat's journey is continuous: on her, on the grass (24), on the bench (41), on the hook (66), absent from the outro
- Feathers appear only in catch shots and the instrumental, never in the guarded intro or the memory
- The ex never has a visible face; the memory shots are the only desaturated frames
- OpenPose on every fall and catch; no fused limbs where two bodies meet
- Composited UI only (the phone in shot 26); the coffee-cup scribble is illegible
- Light warms steadily from grey-blue to pastel; no shot after the memory is colder than the one before it
- The last shot is a locked-off overhead and holds until the audio fades
