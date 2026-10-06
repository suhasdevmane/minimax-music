# Wan 2.2 Shot List — "Hey Stranger"

Shot-by-shot prompts for a local Wan 2.2 music video. Modern romantic-drama
look. Every shot is anchored to the lyric it covers so cuts land on phrases;
get the timestamps from the rendered WAV, never from word counts.

## 1. Visual style

Cinematic realism: natural faces and skin, controlled camera, shallow depth of
field. The palette is the story — **cold fluorescent green-white** for the
supermarket present, **warm amber and sun flare** for the memories at
nineteen, **blue rain with one yellow raincoat** for the parking lot, **pale
clean morning** for the end. Mahima's yellow raincoat is the only warm colour
in every present-day frame until the final chorus.

| Time layer | Look |
|---|---|
| Supermarket present | Cold fluorescent, wet reflective floors, static or slow lateral camera |
| Memories at nineteen | Warm amber, handheld, sun flare, soft grain, windows down |
| Parking lot / rain | Deep blue, sodium-orange streetlights, slow dolly, the yellow coat |
| Final release | Pale morning, wide compositions, gentle forward camera |

## 2. Character bible — paste into every prompt

Wan 2.2 has no character memory; identity comes from repeating the exact same
description and reusing the same reference still. Copy verbatim.

**Mahima** (present day, 29)
> Same female protagonist Mahima, woman in her late twenties, expressive dark eyes, oval face, long dark wavy hair, small silver earrings, graceful natural features, emotionally restrained expression, wearing a mustard-yellow raincoat over a plain grey sweater, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (memory, 19)
> Same female protagonist Mahima at nineteen, expressive dark eyes, oval face, long dark wavy hair loose and windblown, small silver earrings, oversized denim jacket over a white tank top, open sunlit expression, realistic cinematic photography, consistent identity

**Eli** (present day, 30)
> Same male character Eli, man around thirty, sandy-brown short hair, grey eyes, light stubble, lean build, navy rain jacket over a flannel shirt, a worn leather cord bracelet on his right wrist, tired kind expression, realistic cinematic photography, consistent identity

**Eli** (memory, 19)
> Same male character Eli at nineteen, sandy-brown hair falling over his forehead, grey eyes, lean build, faded band t-shirt, the same worn leather cord bracelet on his right wrist, bright reckless grin, realistic cinematic photography, consistent identity

The **yellow raincoat** is Mahima's signature; the **leather cord bracelet** is
Eli's — he wore it at nineteen and still does, and one shot lands on it. The
**coffee cup with a number on it** is the object of the bridge.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.

1. **Lock the characters** — front, three-quarter, profile, full body, neutral
   and emotional, present outfit and memory outfit, for both. IP-Adapter or a
   character LoRA for Mahima; a second reference or LoRA for Eli.
2. **Keyframes first** — strongest realistic checkpoint; OpenPose for walking
   and the two-shots; Depth/SoftEdge for the aisle compositions. 16:9 first;
   separate 9:16 recomposition for Shorts.
3. **Animate conservatively** — slow push-in, hair and coat movement, rain,
   breathing, small hand movement. No choreography or long walks in one clip.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Keep most shots 4–8 s.

## 4. Shot-by-shot prompts

### Intro

**Shot 1 — Tuesday rain** · *"Tuesday rain, fluorescent light"*
> Exterior of a small-town supermarket at night in steady rain, cold fluorescent light spilling through the glass front onto a wet parking lot, Mahima crossing toward the doors in a mustard-yellow raincoat with her hood up, the only warm colour in the frame, slow push-in, realistic film photography, 35mm lens.

**Shot 2 — Aisle seven** · *"Aisle seven on an ordinary night"*
> Interior supermarket aisle under flat fluorescent light, Mahima in the yellow raincoat reaching for a shelf, a basket on her arm, shelves receding into shallow focus, mundane and quiet, slow lateral dolly, cinematic realism.

**Shot 3 — The voice** · *"Then a voice I'd know in any crowd or storm"*
> Close-up of Mahima's face as she hears something behind her, her hand stopping mid-reach on the shelf, eyes widening very slightly, breath held, fluorescent light reflected in her eyes, locked-off camera, realistic emotional micro-expression.

**Shot 4 — Ten years came undone** · *"Said my name, and ten years came undone"*
> Mahima turning slowly in the supermarket aisle to find Eli standing at the far end holding a shopping basket, both frozen, the aisle between them long and empty, rack focus from her to him, cold light, quiet cinematic tension.

### Verse 1 — Memory

**Shot 5 — Nineteen** · *"We were nineteen in a car that barely ran"*
> Warm summer memory, nineteen-year-old Mahima and Eli in a rusted old sedan on a country road, windows down, her bare feet on the dashboard, hair whipping in the wind, both laughing, handheld 35mm camera, golden sun flare, soft nostalgic grain.

**Shot 6 — Heartbeat in my hand** · *"Windows down, your heartbeat in my hand"*
> Close-up inside the moving car, young Mahima's hand pressed flat against young Eli's chest over his t-shirt, his leather cord bracelet visible on the wrist beside hers, sunlight strobing through trees, intimate and youthful, gentle handheld motion.

**Shot 7 — By the water** · *"You kissed me by the water, said, wait for me"*
> Young Mahima and Eli standing at the edge of a lake at sunset, his hands on her face, foreheads touching, he is speaking earnestly, the water glowing gold behind them, slow orbit, emotional cinematic realism.

**Shot 8 — The calls got shorter** · *"The calls got shorter, then the calls got rare"*
> Young Mahima sitting on the floor of a small bedroom at night with her back against the bed, holding an old phone to her ear, listening, her expression slowly emptying, a single warm lamp, static camera, realistic quiet drama.

**Shot 9 — Dial tone** · *"No goodbye, no reason, just a dial tone"*
> Extreme close-up of young Mahima lowering the phone from her ear, the screen showing a call ended, her thumb resting on it, then the phone slipping onto the blanket beside her, shallow focus, cold blue night light, almost no movement.

**Shot 10 — Sleep alone** · *"And a girl who learned to sleep alone"*
> Wide shot of young Mahima lying awake in bed at dawn, curled on one side facing an empty half of the mattress, pale light through thin curtains, slow push-in, quiet cinematic loneliness.

### Pre-chorus 1

**Shot 11 — Rehearsed** · *"I rehearsed this moment a thousand nights"*
> Present-day Mahima in the supermarket aisle, jaw set, lifting her chin into a composed cold expression, the practised armour going on, tight close-up, fluorescent light, slow push-in.

**Shot 12 — Every line didn't last** · *"And every line I practised didn't last"*
> Reverse angle: Eli walking slowly down the aisle toward her with a small uncertain smile, and Mahima's composed expression softening despite herself, her shoulders dropping, rack focus from him to her, realistic emotional shift.

### Chorus 1

**Shot 13 — Say my name the same** · *"Hey stranger, you still say my name the same"*
> Two-shot in the supermarket aisle, Eli speaking softly and Mahima listening, a shopping basket in each of their hands, an old couple passing behind them out of focus, warm smile fighting through her face, slow circular camera, bittersweet realism.

**Shot 14 — Only weather** · *"Like the years were only weather, like nothing changed"*
> Match cut: young Mahima and Eli laughing in the sunlit car dissolving into present-day Mahima and Eli standing in the cold fluorescent aisle in the same positions, warm memory fading into cool present, smooth cinematic dissolve.

**Shot 15 — Somewhere I should be** · *"Hey stranger, I've got somewhere I should be"*
> Mahima glancing down at her phone in her hand, a notification on the screen, then looking back up at Eli and not moving, torn between leaving and staying, medium close-up, fluorescent light, subtle handheld.

**Shot 16 — Standing in the rain** · *"But I'm standing in the rain like it's still you and me"*
> Exterior: Mahima and Eli standing under the supermarket's entrance canopy in the rain, bags at their feet, neither leaving, the yellow raincoat glowing against blue rain and sodium-orange streetlights, slow pull-back wide shot, cinematic melancholy.

**Shot 17 — Did you ever look back** · *"Hey stranger, tell me, did you ever look back"*
> Direct close-up of Mahima looking at Eli and asking the question with her eyes rather than her mouth, rain behind her, a tear she does not let fall, slow gentle push-in, realistic emotional performance.

**Shot 18 — Hasn't learned to let go** · *"And my heart still hasn't learned how to let go"*
> Extreme close-up of Mahima's hand at her side, fingers slowly closing into her palm and opening again, rain dripping from the yellow sleeve, shallow focus, slow motion, symbolic restraint.

### Post-chorus 1

**Shot 19 — Hey stranger chant**
> Rhythmic sequence of three quick close-ups on the beat: Eli's leather cord bracelet on his wrist, Mahima's yellow hood catching rain, the two of them side by side under the canopy not quite looking at each other, cinematic music-video pacing, blue and amber.

### Verse 2

**Shot 20 — Are you happy** · *"You asked if I was happy, and I said yes"*
> Mahima and Eli walking slowly side by side along the supermarket's outer wall under the canopy, she answers him with a small honest nod and a real smile, rain curtain beside them, steadicam tracking, warm-cool contrast.

**Shot 21 — The city swallowed you** · *"You said the city swallowed you, you lost your way"*
> Close-up of Eli speaking, looking down at his hands, ashamed and tired, the bracelet turning on his wrist, the fluorescent glow behind him, Mahima's out-of-focus shoulder in the foreground, static camera, realistic confession.

**Shot 22 — Hands still move the same** · *"Your hands still move the way they did at nineteen"*
> Split memory: extreme close-up of Eli's hands gesturing as he talks in the present, dissolving to the same hands at nineteen on the steering wheel of the old car, the bracelet identical in both, slow cinematic cross-dissolve.

**Shot 23 — The checkout line** · *"And I realised, standing in the checkout line"*
> Mahima standing in a supermarket checkout line, Eli two places behind her, she stares at the conveyor belt with a calm dawning expression, the beep of the scanner, fluorescent light, slow push-in, quiet cinematic realisation.

**Shot 24 — Not for you, for that time** · *"The ache is not for you, it's for that time"*
> Mahima's face in the checkout line softening into something like peace, a slow exhale, the faintest smile at no one, then a cut to a two-second flash of the sunset lake at nineteen, shallow focus, gentle handheld.

### Pre-chorus 2

**Shot 25 — No one to fight** · *"I rehearsed a war, but there's no one to fight"*
> Mahima looking back at Eli in the checkout line and seeing him fully: tired, older, harmless, her armour visibly gone, medium close-up, fluorescent light, subtle handheld.

**Shot 26 — Not waiting by the phone** · *"Who isn't waiting by the phone at all"*
> Match cut from young Mahima on the bedroom floor holding the dead phone, to present-day Mahima sliding her phone into her raincoat pocket without looking at it, warm past into cool present, smooth cinematic dissolve.

### Chorus 2

Reuse shots 13–18 with changed angle, lighting or expression. Chorus 1 shows
longing; chorus 2 shows the longing turning into calm.

### Instrumental

**Shot 27 — Memory montage**
> Dreamlike montage of Mahima and Eli at nineteen: the car on the country road, feet on the dashboard, jumping into the lake at sunset, sharing headphones on a pier, hands almost touching, warm golden colour, gentle motion blur, soft grain, lyrical music-video pacing.

**Shot 28 — The coffee counter**
> Present day, a small in-store coffee counter near the exit, Eli buying two coffees, Mahima waiting beside a rain-streaked window with her bags, distant fluorescent hum, slow dolly, quiet cinematic pause.

### Bridge

**Shot 29 — Number on a cup** · *"You wrote your number on a coffee cup"*
> Extreme close-up of Eli writing a phone number on the side of a paper coffee cup with a borrowed pen, the leather bracelet on his wrist, then sliding the cup across the counter toward Mahima's hands, warm counter light, slow motion.

**Shot 30 — I'm sorry** · *"Then you said, I'm sorry, I'm sorry I never called"*
> Intense close-up of Eli apologising, eyes wet, voice barely there, rain-streaked window glowing blue behind him, slow handheld push-in, realistic emotional performance.

**Shot 31 — Nineteen again** · *"And I held that cup like I was nineteen again"*
> Close-up of Mahima holding the coffee cup with both hands against her chest, eyes closed for one breath, a two-second flash of the sunset lake, then her eyes opening calm, shallow focus, warm and cool light mixing.

**Shot 32 — Set it down** · *"Then I set it down, and I let the moment end"*
> Mahima gently placing the coffee cup down on the counter, the number facing up, her hand resting on it for a moment and then lifting away, extreme close-up, slow motion, symbolic release.

**Shot 33 — Maybe I'll call** · *"Maybe I'll call you, maybe I won't"*
> Two-shot at the exit doors, Mahima giving Eli a small warm honest smile and a shrug, he nods, neither reaching for the other, the rain visible through the glass behind them, slow circular camera, tender restraint.

### Final chorus

**Shot 34 — Not the girl you left in the rain** · *"But I'm not the girl that you left in the rain"*
> Mahima pushing through the supermarket doors into the rain alone, hood down, letting the rain hit her face, the yellow raincoat bright against the blue night, camera moving backward in front of her, the parking lot lights beginning to feel warm.

**Shot 35 — Walking, setting me free** · *"And this time I'm walking, and it's setting me free"*
> Wide tracking shot of Mahima walking across the wet parking lot with her bags, steady and unhurried, her reflection in the puddles, Eli a small figure under the canopy behind her not following, sodium lights haloed by rain, cinematic freedom.

**Shot 36 — The life turned out nice** · *"Then I built a whole life, and the life turned out nice"*
> Mahima in the driver's seat of a modest modern car, rain on the windshield, she looks at herself in the rearview mirror and smiles, real and unguarded, dashboard light warm on her face, slow intimate close-up.

**Shot 37 — Finally learned to let you go** · *"And my heart finally learned how to let you go"*
> Through the rain-streaked windshield from outside: Mahima resting her forehead on the steering wheel for one breath, then lifting her head, wiping her eyes once, and starting the car, headlights coming on and flooding the frame, slow push-in.

### Post-chorus 2

**Shot 38 — Ten years and one goodbye**
> Rhythmic sequence on the beat: the coffee cup left on the counter with the number facing up, Eli's hand picking it up, Mahima's taillights pulling out of the lot in the rain, cinematic music-video pacing, blue and amber.

### Outro

**Shot 39 — Ordinary night** · *"Tuesday rain, fluorescent light"*
> Mirror of shot 1: exterior of the supermarket at night in rain, but now the camera is inside Mahima's car pulling away, the fluorescent glow shrinking in the rear window, the wipers moving, calm, slow dolly backward.

**Shot 40 — Didn't feel nineteen anymore** · *"And I didn't feel nineteen anymore"*
> Final wide shot: Mahima's car driving down a wet country road at dawn, the rain stopping, first pale light breaking over the fields, the yellow of her coat just visible through the window, the camera slowly rising and pulling away, hopeful cinematic ending, soft lens flare, no text.

## 5. Edit to the song

Import the WAV and add markers at: the first vocal entrance, each "Hey
stranger", the instrumental break, "I'm sorry I never called", "But I'm not the girl
that you left in the rain", and the final "anymore." Cut on those. At 96 BPM
a bar is 2.5 s — hold shots for whole bars.

## 6. Vertical teaser (15–20 s)

Built around *"Hey stranger, you still say my name the same / Like the years
were only weather, like nothing changed."*

1. Mahima frozen in aisle seven (shot 3)
2. Eli at the end of the aisle (shot 4)
3. Feet on the dashboard at nineteen (shot 5)
4. The coffee cup set down (shot 32)
5. Walking out into the rain, hood down (shot 34)

On-screen lyrics only during the hook, large and high-contrast. Understandable
within the first two seconds: a woman in a yellow raincoat sees someone.

## 7. Quality-control checklist

- Mahima's face recognisable in every shot; the yellow raincoat in every present-day shot
- Eli's leather bracelet visible in both timelines
- No duplicated shoppers or distorted hands
- The bride-free story: Eli is never villainous, just someone who got scared
- The turn from longing (chorus 1) to peace (final chorus) is visible without dialogue
- Cuts land on musical phrases
- Fluorescent, amber, and blue-rain grades stay consistent within their timelines
- On-screen lyrics contain no spelling errors
