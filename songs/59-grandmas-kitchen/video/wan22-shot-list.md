# Wan 2.2 Shot List — "Grandma's Kitchen"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission, plus five shots for the instrumental. Timestamps come from the
rendered WAV; cut on the sung line. At 78 BPM a bar is 3.08 s, so most shots
run a full bar or two and the whole video breathes slowly.

## 1. Visual style

Two kitchens and one recipe. The **memory kitchen** is an old family kitchen
at golden hour: spice jars, tile, a wooden counter worn pale in the middle,
flour dust hanging in a shaft of sun, slightly overexposed at the window.
The **present kitchen** is a small city apartment, clean and a little too
tidy, natural afternoon light that is cooler and flatter. The two are shot
with **matched framings** on purpose — the counter, the hands, the plate,
the chair — so that by the final chorus the eye cannot tell which kitchen it
is in. Nothing is stylised. No slow-motion, no lens flare, no drone. Fixed
lenses, gentle push-ins, the camera at the height of a person standing at a
counter.

| Section | Grade | Camera |
|---|---|---|
| Intro | Warm amber, dusty, hot window | Slow push down the hall |
| Verse 1 (memory) | Golden, soft, kitchen-window gold | Static close-ups of hands |
| Pre-chorus 1 | Memory warm, present a touch cooler | Locked off, then a hesitating push-in |
| Chorus 1 | The widest, most golden the film gets so far | Wide, generous, slow drift |
| Verse 2 (present) | Natural afternoon, cooler, warm only at the window | Handheld, close |
| Pre-chorus 2 | Lamp light warming through the section | Matched frames to verse 1 |
| Chorus 2 | Both worlds warm, cut against each other | Matched pairs, hard cuts |
| Instrumental | Golden and dusty; the empty old kitchen desaturated | Slow, still, one long drift |
| Bridge | Evening lamp over the stove, the rest dark | Static, then the warmest frame in the film |
| Final chorus | Golden, brightest and widest of all | Wide, moving with people |
| Outro | Hallway dark, warm light under a door | Slow, then a locked-off hold |

## 2. Character bible — paste into every prompt

**Mahima** (present day, the granddaughter)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned up loosely with strands falling, no makeup, wearing a soft grey long-sleeved top with the sleeves pushed to the elbow and a faded floral apron over it, calm attentive expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (final chorus and outro, the room full)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pinned up loosely, no makeup, wearing the faded floral apron over a warm rust-coloured shirt, flour on her forearms, open laughing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima at eight** — the child in the memories. Cast one child and keep her
in every memory shot; same dark wavy hair, same eyes, cotton dress, bare
feet.
> a young girl of about eight, dark wavy hair, expressive dark eyes, a simple cotton dress, bare feet, realistic cinematic photography, consistent identity

**The grandmother** — never a hard close-up of her face. She is her hands,
her shoulder, the back of her head against the window light, a floral apron,
a soft three-quarter from behind. The one time her face is fully seen is in
the photograph on the fridge, and that is a real still, not a generated
performance.
> an older woman in her seventies, silver hair pinned back, a faded floral apron, seen from behind or in soft three-quarter, hands wrinkled and strong, warm kitchen light

**The best friend** — a young woman the same age as Mahima, mascara run,
coat still on when she arrives. Warm, ordinary, no styling.

**The mother** — voice only, on a speakerphone. Never on screen.

Objects that carry the story: the **small radio** (windowsill in the memory
kitchen, shelf in the apartment — the same object, the bridge between the
two rooms), the **floral apron** on its hook, the **wooden spoon** and the
grip on it, the **kitchen chair** pulled across the floor to the stove, the
**photograph** held to the fridge with a magnet, the **light in the window**
seen from the street.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, labels, handwriting and any signage are composited in the
edit.** The radio dial markings, the report card, the photograph on the
fridge and the speakerphone display are overlays. The model cannot render
legible text and this film has a recipe nobody wrote down at the centre of
it — nothing readable should ever appear.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and the child in her one look with IP-Adapter or a
character LoRA each; keep the grandmother's reference deliberately
face-light, three-quarter from behind, so the model never tries to build her
face. Depth for the two kitchen interiors so the matched framings hold across
memory and present. OpenPose for the kneading, the chair pull and the apron
tie — hands doing real work are where this model fails first. 16:9 first;
9:16 recomposition for the hands-and-dough hook cut.

Animate conservatively and in single gestures: one knead, one pinch of salt,
one dial turn, one chair pull, steam rising, a kettle beginning to sing. Do
not ask for a sequence of actions in one clip. The two-kitchen match cuts are
made in the edit from two separately generated plates with identical camera
metadata, not in one generation.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s at this tempo.

## 4. Scene per lyric line

### Intro — the hall, the doorway

1. *"Cardamom and cinnamon still hanging in the hall,"* — slow push down a narrow hallway toward a kitchen doorway, the light growing warmer as the camera moves, dust in the air, spice jars just visible on a shelf beyond the frame edge.
2. *"The radio was always on and never turned up at all."* — the small radio on the kitchen windowsill, morning sun behind it, the dial glowing faintly, macro, the room quiet around it.
3. *"Flour on the counter, morning sun across the floor,"* — a wide of the empty old kitchen, flour dust hanging in a shaft of sun, a bar of light lying across the tile, nothing moving.
4. *"I could walk that kitchen blindfolded, a thousand times before."* — present day: Mahima standing in the doorway with a set of keys in her hand, eyes closed, breathing in, a small smile, medium, static.

### Verse 1 — her hands, the chair by the stove

5. *"She never used a measuring cup, she measured with her hands,"* — memory, warm: the grandmother's hands working dough on the wooden counter, only hands and forearms in frame, close-up, golden window light.
6. *"A pinch of this, a little more, she said the dough understands."* — her fingers taking a pinch of salt from an open dish and scattering it, macro, the grains catching the light.
7. *"She'd hum along to something old while the kettle took the high part,"* — the grandmother's shoulder and the back of her head against the window, humming, the sun behind her; cut on the line's end to the kettle beginning to sing, steam lifting.
8. *"Pull a chair up by the stove and say, sit, baby, tell me your heart."* — a wooden kitchen chair being dragged across tile toward the stove, then the child sitting on it, feet not reaching the floor, low angle from the child's height. **The signature frame — reused exactly in shot 45.**
9. *"I brought her every broken thing, a scraped knee, a bad grade,"* — three quick memories in the same framing every time, the counter and the hands: a plaster smoothed onto a scraped knee; a report card pressed flat and a plate slid over it (composited); a teenage girl crying at the table.
10. *"She fixed them all with the same two hands and the same thing she made."* — a plate of something warm arriving on the table without a word, the girl's hands coming into frame to take it, close-up, the same lamp overhead as in every previous shot.

### Pre-chorus 1 — the rules

11. *"She'd say, you don't rush the rising, honey, and you don't skip the salt,"* — dough under a cloth on the windowsill, rising, a slow push-in over a long hold, warm.
12. *"And when somebody leaves the table, that's not always your fault."* — a full table seen past one chair pushed back and left empty, the grandmother's hand landing on the child's shoulder in the foreground, medium wide.
13. *"She said, you learn it by the feel, girl, you learn it by the smell,"* — the child watching her grandmother's face for how it is done, the grandmother in soft three-quarter, the child's eyes tracking her hands, over-the-shoulder.
14. *"And I'm still learning, standing here, trying to do it half as well."* — present day: Mahima's hands hovering over a bowl in the apartment, hesitating, not touching it, the light cooler, close-up.

### Chorus 1 — the kitchen at its fullest

15. *"Everything I know about love, I learned in grandma's kitchen,"* — wide of the memory kitchen full of people and steam, the grandmother at the centre seen softly from behind, everyone talking at once, generous and golden.
16. *"Where the door was never locked and nobody went missing."* — the back door swinging open on its own weight and a neighbour walking in without knocking, arms full, nobody looking up, medium.
17. *"How to feed a crowd, how to hold a hand, how to let the bread rise slow,"* — three cuts on the phrase: a pot too big for its burner; two hands meeting across the table; a covered bowl on the sill with the light moving on it.
18. *"How to leave a light on so the lost ones find their way home."* — the kitchen window seen from the street at night, one warm light on, the rest of the house dark, static wide, the widest exterior in the film.
19. *"She never wrote the recipe, she just lived it every day,"* — an open kitchen drawer full of everything except a recipe book, her hand pushing it shut, close-up.
20. *"Everything I know about love, she taught me anyway."* — bread coming out of the oven, the grandmother's hands and forearms, steam, the room in golden focus behind, close-up. **The hook frame.**

### Verse 2 — her own kitchen now

21. *"Now it's my apartment, my counter, and the sun still hits the floor,"* — the apartment kitchen in afternoon light, clean and a little too tidy, the same bar of light lying across the floor as shot 3, matched framing, static wide.
22. *"But I burn the onions every time, and there's no one to ask anymore."* — onions smoking hard in a pan, her pulling it off the heat fast, waving the smoke, swearing silently, handheld close.
23. *"A photo on the fridge, her in that apron, laughing at the lens,"* — the photograph under a magnet on the fridge door (composited still): the grandmother in the floral apron, laughing, the only time her face is fully seen, macro.
24. *"I talk to her while the water boils like the conversation never ends."* — Mahima at the counter talking toward the fridge while a pot comes to the boil behind her, half smiling and half not, no answer coming, medium.
25. *"Her radio sits on my shelf, still tuned to her old station,"* — the same small radio from shot 2, now on an apartment shelf between spice jars, matched framing, close-up.
26. *"It plays the songs she hummed to teach a hurried girl some patience."* — her fingers turning the dial, something faint and old coming through, and her stopping what she is doing to listen, the dial glow the only warm light, close-up.

### Pre-chorus 2 — the same hands

27. *"She'd say, you don't rush the rising, honey, and you don't skip the salt,"* — her scraping the burnt pan into the bin and setting it back on the heat clean, starting again, handheld.
28. *"When the whole thing falls apart, you start again, it's not your fault."* — a fresh onion going under the knife, steady this time, the cuts even, close-up on the board.
29. *"My mother says I've got her hands, the way I hold the spoon,"* — her phone face-up on the counter on speakerphone (UI composited), her mother's laugh audible; then close-up of her hand on the wooden spoon, the exact grip from shot 5, matched frame.
30. *"And I've got her stubborn heart, and I know just what to do."* — her looking down at her own hand on the spoon, recognising it, then getting on with it, the lamp light warmer than the start of the section, medium close.

### Chorus 2 — the two kitchens become one

31. *"Everything I know about love, I learned in grandma's kitchen,"* — hard cut pair: the old kitchen full of people, then Mahima's kitchen empty, same framing, same lens.
32. *"Where the door was never locked and nobody went missing."* — the old back door swinging open; cut to her apartment door with the chain hanging unhooked, matched, close-up.
33. *"How to feed a crowd, how to hold a hand, how to let the bread rise slow,"* — the grandmother's hands on the dough; cut to Mahima's hands on the dough, same angle, same counter height, the two shots edited to land on the same beat.
34. *"How to leave a light on so the lost ones find their way home."* — reuse shot 18's exterior, then its match: her apartment window from the street below, one warm light on among many dark ones.
35. *"She never wrote the recipe, she just lived it every day,"* — her opening her own drawer and finding no recipe book either, then almost laughing, close-up.
36. *"Everything I know about love, she taught me anyway."* — the old table and her small table cut back to back, both being laid, the two rooms now the same colour, medium wide.

### Instrumental — the bread, the empty kitchen

37. Mahima kneading dough on her own counter, flour to the elbows, working it properly for the first time, slow and unhurried, close on the hands and forearms, warm lamp.
38. The loaf going into the oven and the door closing, the oven light coming on inside, the glow across her face, medium.
39. Her sitting on the kitchen floor with her back against the oven door, knees up, waiting, the radio playing faint and old, wide, one lamp.
40. A long slow drift across the old kitchen, empty and clean, the sun moving over the tile, the counter bare, slightly desaturated, nobody in frame.
41. The floral apron hanging on its hook by the old door, still, and a slow fade to the same hook in the apartment with the same apron on it — the cut into the bridge.

### Bridge — the apron, the chair, the voice

42. *"So I put on her apron and I set the table for two,"* — close-up on the apron strings being tied at the small of her back, her fingers working the knot, evening lamp.
43. *"Even though it's only me tonight, that's what she would do."* — a second plate going down on a table set for one, her hand lingering on it, close-up, the rest of the apartment dark.
44. *"When my best friend called me crying, I said, come over, don't explain,"* — the phone lighting on the counter, her picking up, listening for two seconds and saying nothing back; cut to the friend at the door, coat on, mascara run.
45. *"I pulled a chair up by the stove and said, sit, baby, tell me your pain."* — **matched frame with shot 8**: a wooden chair dragged across the floor to the stove, the friend sitting on it, the same low angle, the same lamp position. A plate arrives.
46. *"And I heard her voice come out of me, the same words, the same key,"* — extreme close-up on Mahima's face as she stops with the spoon in her hand, hearing herself, a slow half-laugh she does not expect.
47. *"Turns out she wrote it down after all, she wrote it into me."* — her hands on the spoon and the pan, the grandmother's grip exactly, then her eyes lifting; the warmest and softest frame in the film, close-up. **The quote frame.**

### Final chorus — she is the kitchen now

48. *"Everything I know about love, I learned in grandma's kitchen,"* — the apartment filling up: the friend, two more friends, a neighbour, somebody's kid on a chair too tall for them, wide and generous, matched to shot 15.
49. *"Where the door was never locked and nobody went missing."* — the apartment door standing open onto the hallway, someone letting themselves in with their hands full, nobody getting up, medium.
50. *"How to feed a crowd, how to hold a hand, how to let the bread rise slow,"* — three cuts on the phrase, matched to shot 17: a pot too big for the burner; two hands meeting across her small table; the risen loaf turned out onto the board.
51. *"How to leave a light on so the lost ones find their way home."* — her apartment window from the street, warm and full of moving shapes, the brightest exterior in the film, static wide.
52. *"She never wrote the recipe, she just lived it every day,"* — Mahima at the centre of the room, seen the way the grandmother was seen in chorus one, soft three-quarter, steam and laughter around her.
53. *"And everything I know about love, I'm giving it away."* — her passing a plate into somebody else's hands, the camera staying on the plate as it goes, then lifting to her face, close-up, golden.

### Outro — the door left unlocked

54. *"Cardamom and cinnamon still hanging in the hall,"* — late. Everyone gone. The apartment hallway with coats off the hooks and one glass left on a shelf, slow drift, matched to shot 1.
55. *"The radio is always on, I never turn it up at all."* — her hand turning the radio down but not off, the dial glow lowering, macro, the room going quiet around it.
56. *"Everything I know about love, I learned it in her kitchen,"* — her straightening the photograph on the fridge with one finger, holding there a second, close-up.
57. *"And I'll leave the door unlocked in case you need it."* — final shot: her apartment door seen from the dark hallway outside, a strip of warm kitchen light under it, the lock not turned. Locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the chair pull in shot 8, each
*"everything I know about love"*, the burnt-onion cut, the matched spoon grip
in shot 29, the instrumental, the second chair pull in shot 45, *"she wrote
it into me"*, the final *"giving it away"*, and the last frame under the
door. At 78 BPM a bar is 3.08 s; the chorus cuts land two bars apart, the
verses four.

**The tribute template.** The shareable cut is shots 5–8 and 20 — the hands,
the salt, the kettle, the chair, the bread out of the oven — vertical, with
*"Everything I know about love, I learned in grandma's kitchen"* on screen.
Invite people to post their own grandmother's kitchen: her hands, her radio,
her apron, the recipe she never wrote down. The second shareable frame is
the matched chair pull, shots 8 and 45 cut straight against each other, with
*"Turns out she wrote it down after all, she wrote it into me."*

## 6. Quality-control checklist

- Two looks and one child: the apron is on from shot 42 onward and never before it; the child appears only in memory shots
- The grandmother's face is never generated — hands, shoulder, back of the head, soft three-quarter only; the photograph on the fridge is a real composited still
- The matched pairs land: shot 3 with 21, shot 5 with 33, shot 8 with 45, shot 18 with 34 and 51, shot 2 with 25, shot 15 with 48, shot 17 with 50
- The radio is the same physical object in both kitchens, and the dial markings are composited
- Memory kitchen golden and dusty, present kitchen cooler until the bridge, both warm from chorus two on; the empty old kitchen in shot 40 is the only desaturated frame
- No readable text anywhere — no recipe book, no report card, no phone screen, no radio dial numbers
- Hands are the subject of eighteen shots; every kneading, pinching and gripping clip gets a pose reference and a hand check before it is approved
- The last shot is locked-off on the closed door with the light beneath it and holds until the audio fades
