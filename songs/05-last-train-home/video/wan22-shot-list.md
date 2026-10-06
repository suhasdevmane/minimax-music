# Wan 2.2 Shot List — "Last Train Home"

Nocturnal, cinematic, mostly one location: a late-night metro train and its
platform. Every shot is anchored to the lyric it covers so cuts land on
phrases; take timestamps from the rendered WAV.

## 1. Visual style

Night city realism: neon, empty platforms, reflective glass, rain on windows.
Cool blues and deep greens outside, warm amber interior train light. Handheld
but smooth; intimate close-ups. The whole song lives at **2:13 a.m.** until
the bridge breaks the pattern with **7 p.m. daylight**, so the palette shift
is the story's turn.

| Time layer | Look |
|---|---|
| The last train (nights) | Warm amber interior light, black windows with reflections, cool neon outside, slow lateral camera |
| The platform (nights) | Empty, teal-green fluorescent, light rain, wide static shots |
| Absence (bridge, first half) | Same train, colder grade, emptier seats, slower camera |
| 7 p.m. platform (bridge turn) | Golden evening daylight, crowds, movement, handheld |
| Outro | Station exit at dusk, warm city lights, no train in frame |

## 2. Character bible — paste into every prompt

Wan 2.2 has no character memory; identity comes from repeating the exact same
description and reusing the same reference still. Copy verbatim.

**Mahima**
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair under a soft grey beanie, small silver earrings, wearing a dark olive jacket over a cream sweater with a chunky knit scarf, thoughtful quiet expression, realistic cinematic photography, consistent identity, natural skin texture

**Theo** (the stranger)
> Same male character Theo, young man in his mid-twenties, dark curly hair, deep-set brown eyes, pale tired face, wearing a black hoodie with the hood down and over-ear headphones around his neck, quiet reserved presence, realistic cinematic photography, consistent identity

Mahima's signature is the **grey beanie and chunky scarf**; Theo's is the
**black hoodie and headphones**. The recurring objects are the **folded note
in the seat pocket**, the **receipts with song titles**, the **second door**,
and the **station clock reading 2:13**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

Note on the clock and the notes: Wan renders legible text unreliably. Shoot
the clock face and the handwritten notes as separate close-up stills (or real
props photographed) and composite them in the edit.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.

1. **Lock the characters** — front, three-quarter, profile, full body,
   neutral and emotional, for both. IP-Adapter or a character LoRA each.
   Because most of the video is the same train interior, also generate 3–4
   approved *set* stills (Mahima's seat, the second door, the platform) and
   reuse them as backgrounds.
2. **Keyframes first** — strongest realistic checkpoint; OpenPose for the
   platform walk and the final approach; Depth for the train interiors.
   16:9 first; 9:16 recomposition for Shorts.
3. **Animate conservatively** — train sway, passing lights on the window,
   breathing, small hand movements, a note being folded. Split the final
   approach through the crowd into 3–5 s pieces.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Keep most shots 4–8 s.

## 4. Shot-by-shot prompts

### Intro

**Shot 1 — Platform three** · *"Two-thirteen a.m., platform three"*
> Wide static shot of an empty underground metro platform at night, teal fluorescent light, light drizzle blowing in from the stairwell, a station clock on the wall, Mahima in a grey beanie and chunky scarf standing alone near the platform edge, a train's headlights appearing in the tunnel, cinematic realism, 35mm.

**Shot 2 — Same seat** · *"Same train, same seat, same view"*
> Interior of a near-empty late-night train carriage, warm amber light, Mahima sitting down in a window seat with the practised ease of habit, setting her bag beside her, black window reflecting her face, slow push-in, quiet nocturnal mood.

**Shot 3 — The second door** · *"You always stand by the second door"*
> From Mahima's seat: Theo standing by the second door of the carriage in a black hoodie with headphones on, holding the rail, looking down at the floor, the door glass reflecting the passing tunnel lights, shallow focus, static.

**Shot 4 — Eyes meet through the glass** · *"But sometimes our eyes meet through the glass"*
> Close-up of Mahima looking at Theo's reflection in the dark train window rather than at him directly, and in the reflection his eyes lifting to meet hers, both holding it for one beat, then both looking away, warm interior light, slow motion.

**Shot 5 — Only us** · *"Like it's only us, and everyone else is past"*
> Wide shot of the carriage with Mahima in her seat and Theo at the door, the two of them the only sharp figures while the few other passengers blur and the passing lights streak, dreamlike, slow lateral dolly, warm amber.

### Verse 1

**Shot 5a — First week** · *"First week, you wore that black hoodie, scrolling through songs I couldn't hear"*
> Close-up of Theo by the second door in the black hoodie, thumb scrolling slowly on his phone, headphones on, his face unreadable and tired, the reflection of Mahima watching him faint in the window glass beside him, warm interior light, static, shallow focus.

**Shot 6 — The dropped pen** · *"Second week, you dropped a pen"*
> Close-up of a pen slipping from Theo's hoodie pocket and rolling across the train floor toward Mahima's boots as the carriage sways, warm light, macro, slow motion.

**Shot 7 — Thanks so low** · *"I picked it up, you said thanks so low"*
> Mahima holding the pen out to Theo, he takes it and says one word without quite meeting her eyes, a small nod, both awkward, medium two-shot by the door, the train rocking gently, handheld.

**Shot 8 — Watched you go** · *"And I pretended I didn't watch you go"*
> Over Mahima's shoulder as Theo steps off at his stop onto a neon-lit platform, the doors closing between them, she looks down at her phone too late to be caught watching, then looks up again as the platform slides away, slow push-in.

**Shot 9 — The note** · *"Third week, you left a note in the pocket of the seat in front"*
> Extreme close-up of Mahima's hand finding a small folded piece of paper tucked into the mesh pocket on the back of the seat in front of her, pulling it out slowly, warm light, macro. (Composite the handwriting in post.)

**Shot 10 — Are you** · *"I'm still here. Are you?"*
> Close-up of Mahima reading the unfolded note in her lap, her expression changing from curiosity to something softer, a breath, the train lights passing across her face, static, shallow focus.

**Shot 11 — Still here, still tired, still trying** · *"Still here. Still tired. Still trying."*
> Mahima writing a reply under the note with a pencil balanced on her knee, tongue between her teeth in concentration, then folding it small, very small, warm light, macro on the hands, slow motion. (Composite the words in post.)

**Shot 12 — Train lights died** · *"Heart beating loud as the train lights died"*
> Mahima tucking the folded note back into the seat pocket just as the carriage lights flicker and go dark in a tunnel, her face lit for a second by the window, then black, then the lights returning and her sitting back with her hand on her chest, static.

### Pre-chorus

**Shot 13 — Same sky** · *"Just two strangers sharing the same sky"*
> Exterior: the train crossing an elevated bridge over a night city, its lit windows the only warm thing against a blue skyline, wide drone-style slow tracking, rain in the air.

**Shot 14 — Living for that seat** · *"I started living for that seat"*
> Quick sequence of Mahima arriving at platform three on different nights: different scarves, same beanie, the clock always the same time, each arrival cut on the beat, teal platform light, rhythmic pacing.

### Chorus 1

**Shot 15 — A world no one knows** · *"We built a world no one knows"*
> Wide two-shot of the carriage at night with Mahima in her seat and Theo by the door, both pretending to look elsewhere, both smiling very slightly, the world outside a blur of neon, slow orbit, warm and intimate.

**Shot 16 — Between stations** · *"In the space between stations"*
> Extreme close-up of the black train window with the tunnel wall rushing past, Mahima's and Theo's reflections faintly visible in the glass at opposite edges of the frame, slow push-in, abstract and cinematic.

**Shot 17 — Everything without words** · *"We said everything without words"*
> Montage of small exchanges over several nights, three quick shots: a folded note passed into the seat pocket, Theo holding up a receipt with something written on it before tucking it away, Mahima biting back a smile with her scarf pulled up over her mouth, warm light, on the beat.

**Shot 18 — Not okay alone** · *"I almost told you I'm not okay alone"*
> Direct close-up of Mahima looking toward the door, lips parting as if to speak, then closing, her hand tightening on her bag strap, the train slowing, slow push-in, realistic restraint.

**Shot 19 — The doors opened** · *"But the doors opened, you stepped out"*
> The train doors sliding open on a neon platform, Theo stepping out without looking back, the doors closing again, Mahima's reflection alone in the glass, static, slow motion.

### Verse 2

**Shot 20 — Song titles on receipts** · *"Little scribbles on old receipts"*
> Extreme close-up of Mahima's hands unfolding a crumpled paper receipt with a handwritten line on the back, then another, then another, laid out on her knee, warm train light, macro. (Composite the handwriting in post.)

**Shot 21 — When the city sleeps** · *"Play this when the city sleeps"*
> Mahima in her seat at night with her own earphones in, eyes closed, the receipt in her hand, the city lights sliding across her face through the window, small private smile, slow push-in.

**Shot 22 — The question** · *"What if we got off at the same stop someday"*
> Close-up of Mahima reading a longer note, her eyes moving across the lines, then stopping, then reading it again, her breath catching, the carriage sway, static, shallow focus.

**Shot 23 — Because we chose to stay** · *"But because we chose to stay"*
> Mahima looking up from the note toward the second door where Theo stands with his hood up, and for the first time he is already looking at her, not at the floor, both holding the look through a whole passing station, wide two-shot, slow motion.

**Shot 23a — Didn't sleep at all** · *"That night I didn't sleep at all, just rehearsing what I'd say if you asked"*
> Mahima lying awake in bed in a small dark apartment, the note held above her face against the ceiling light, her lips moving silently as she rehearses, city neon through the blinds striping the wall, static overhead shot, quiet.

### Pre-chorus 2

**Shot 24 — Two ghosts** · *"Two ghosts on the last train home"*
> Wide shot of the carriage with Mahima and Theo in their usual places, the image slightly doubled like a long-exposure ghost, the reflections in the window more solid than the people, blue-tinted, slow dolly, haunting.

**Shot 25 — Afraid to melt** · *"Afraid to be real, afraid to melt"*
> Split screen: left, Mahima's hand on her knee holding the note; right, Theo's hand on the door rail, the leather of his headphone cord wrapped around his fingers, both hands still, neither moving toward the other, static, warm light.

### Chorus 2

Reuse shots 15–19 with the grade slightly warmer and the two of them slightly
closer in frame each time. The second chorus should feel like it is about to
break, and doesn't.

### Instrumental

**Shot 26 — Night ride**
> Long unbroken shot from the front of the train looking down the tunnel as it curves, lights rushing past, then the train bursting out onto the elevated section over the city, rain on the windshield, cinematic, slow and hypnotic.

**Shot 27 — The announcement**
> Close-up of a speaker grille in the carriage ceiling, then a slow tilt down to Mahima sitting alone at night with the receipts in her lap, her eyes on the door, calm, waiting, warm light, static.

### Bridge — absence

**Shot 28 — You weren't there** · *"Then one night you weren't there"*
> Wide static shot of the carriage at 2:13, Mahima in her seat, and the second door empty, nobody there, the space where Theo stands lit and vacant, colder grade, the train pulling out.

**Shot 29 — Just late, not gone** · *"You were just late, not gone for good"*
> Close-up of Mahima trying to keep her face neutral, her eyes going to the door at every stop, the doors opening on empty platforms, closing again, her jaw tightening, handheld, cold light.

**Shot 30 — Every face through the glass** · *"Watching every face through the glass"*
> Mahima standing now, by the second door herself, scanning the faces on each passing platform through the glass, strangers in hoods and headphones who are never him, slow push-in, blue and green light, aching.

**Shot 31 — The film forgot to cast** · *"That the film forgot to cast"*
> Mahima riding the whole line to the end and back, the carriage completely empty, her alone in the middle of it under the amber light, the receipts and notes held in both hands, wide, slow pull-back, the loneliest frame in the video.

**Shot 31a — Weeks passed** · *"Weeks passed. I kept the notes, kept riding, kept checking the door"*
> Time-lapse-style sequence on the beat: Mahima in her seat on night after night, the notes and receipts in her lap growing into a small stack held with a hair tie, the second door empty in every frame, her scarf changing, the clock never changing, colder grade each cut, rhythmic pacing.

### Bridge — the turn

**Shot 32 — Seven p.m.** · *"Then last Tuesday, seven p.m."*
> Hard cut to daylight: the same platform three at seven in the evening, golden light slanting down the stairwell, crowded with commuters, Mahima in her beanie and scarf moving through them, the station clock reading a different time, handheld, warm, alive.

**Shot 33 — Same hoodie, different eyes** · *"Same hoodie, but different eyes"*
> Through the crowd on the daylight platform: Theo standing still in his black hoodie with his headphones around his neck instead of on, hood down, looking not at the floor but at the stairwell, waiting for someone, medium shot, rack focus onto him.

**Shot 34 — I stopped taking the last train** · *"Said, I stopped taking the last train"*
> Close-up of Theo seeing Mahima, his whole face changing, a real smile, and him speaking to her, the first words we ever see him say to her, golden evening light, slow push-in, realistic emotional performance.

**Shot 35 — A start, not an in-between** · *"Wanted a start, not an in-between"*
> Close-up of Mahima hearing it, her hand going to her mouth under the scarf, eyes bright, commuters flowing past on both sides of her like water around a stone, slow motion, golden light.

### Final chorus

**Shot 36 — Stepped off** · *"So I stepped off the last train home"*
> Mahima walking toward Theo through the moving crowd on the platform, steady and certain, people parting around her, camera tracking backward in front of her, golden light, the guitar-line energy.

**Shot 37 — Your name, finally loud** · *"Just your name, finally loud"*
> Two-shot as Mahima reaches Theo and says his name, both of them laughing at the strangeness of it, his hand coming up to her scarf, her hand on his sleeve, the crowd blurred, slow motion, warm.

**Shot 38 — Walk out that door** · *"And I said, yes. Let's walk out that door"*
> Mahima and Theo turning together toward the station exit stairs, the last train arriving behind them on the platform and neither of them looking at it, hand in hand, wide tracking from behind, golden light flooding down the stairs.

### Outro

**Shot 39 — Two-thirteen, different** · *"Now when I think of two-thirteen"*
> A last look at the station clock, then a slow dissolve to Mahima's and Theo's clasped hands walking up the station stairs into the evening, no train in frame, warm dusk city light, intimate handheld.

**Shot 40 — A first step** · *"A first step, not a last one"*
> Final wide shot: Mahima and Theo walking out of the station entrance onto a rain-washed city street at dusk, neon reflecting in puddles, their backs to camera, her beanie and his black hood side by side, getting smaller, the camera slowly rising, hopeful, soft lens flare, no text.

## 5. Edit to the song

Import the WAV and add markers at: the first vocal entrance, "Still here.
Still tired. Still trying.", each chorus, the instrumental break, "Then one
night you weren't there", "seven p.m.", "I stopped taking the last train", and the final
"a last one." Cut on those. At 98 BPM a bar is 2.45 s — hold shots for whole
bars. The hard cut to daylight in shot 32 must land exactly on "seven p.m."

## 6. Vertical teaser and UGC hook

**Teaser (15–20 s)** around *"On the last train home / We built a world no one
knows."*

1. Platform three, 2:13 (shot 1)
2. Eyes meet in the window reflection (shot 4)
3. The note in the seat pocket (shot 9)
4. The empty second door (shot 28)
5. He speaks to her in daylight (shot 34)

**The note as the hook.** A clean close-up still of the handwritten note —
*"Still here. Still tired. Still trying."* — is the shareable image. Post it
on its own and invite people to write the note they'd leave on a train.

## 7. Quality-control checklist

- Mahima's beanie and scarf, Theo's black hoodie and headphones, in every shot
- The second door is the same door in every train shot
- The clock reads 2:13 in every night shot and a different time only from shot 32 on
- Handwritten notes and receipts composited, never left to the model
- No duplicated passengers or distorted hands
- The absence section is visibly colder and emptier than the nights before it
- The daylight turn is a hard cut on the lyric, not a dissolve
- Cuts land on musical phrases
- No text on screen except the note in the teaser
