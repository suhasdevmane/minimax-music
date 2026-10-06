# Wan 2.2 Shot List — "Polaroids in My Pocket"

Couple-led, memory-driven music video. Every shot is anchored to the lyric it
covers so cuts land on phrases; take timestamps from the rendered WAV.

## 1. Visual style and motifs

Warm indie-film realism: natural faces, cosy clothes, handheld intimacy,
soft grain. Two colour worlds — **present day** is warm lamplight and
neutral tones; **memories** are the slightly faded, cyan-shifted look of an
actual polaroid, with a white border when a photo is on screen.

Three motifs run the whole video:

1. **Polaroid → memory.** A polaroid enters frame, briefly glows at the edges,
   and the camera pushes *into* it to become the memory. Use it for every
   verse transition.
2. **Phone screens.** Old chats — "good morning", "are you okay?", a voice
   note waveform — shown close on a phone in someone's hand, never as a
   graphic overlay.
3. **Split screen, past vs present.** Same bench, same kitchen, same door,
   same sofa. Left: the polaroid version. Right: now.

| Time layer | Look |
|---|---|
| Present day (bedroom floor, kitchen, living room) | Warm tungsten lamps, neutral tones, slow handheld |
| Memory (café, train, rooftop) | Polaroid palette, slight cyan shift, soft grain, white border on entry |
| The fight (kitchen 3 a.m., bathroom, hallway) | Cold overhead kitchen light, hard shadows, static camera |
| Final chorus / outro | Golden late-afternoon window light, wider, gentle forward camera |

## 2. Character bible — paste into every prompt

Wan 2.2 has no character memory; identity comes from repeating the exact same
description and reusing the same reference still. Copy verbatim.

**Mahima** (present day)
> Same female protagonist Mahima, woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair loosely tied back, small silver earrings, natural no-makeup look, wearing an oversized cream knit sweater and grey joggers, warm open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (memory)
> Same female protagonist Mahima a few years younger, expressive dark eyes, oval face, long dark wavy hair loose, small silver earrings, wearing a faded denim jacket over a striped t-shirt, shy half-smile, realistic cinematic photography, consistent identity

**Noah** (present day)
> Same male character Noah, man in his mid-twenties, short dark-blond messy hair, hazel eyes, light stubble, warm easy smile, wearing a worn olive-green hoodie, realistic cinematic photography, consistent identity

**Noah** (memory)
> Same male character Noah a few years younger, short dark-blond messy hair, hazel eyes, clean-shaven, wearing an old grey hoodie and holding a paper coffee cup, nervous warm smile, realistic cinematic photography, consistent identity

The **old grey hoodie** is the first-photo object; Noah wears it in the memory
of the café and it reappears folded in the box in the outro. Mahima's
**cream sweater** is present-day only. The **shoebox of polaroids** and the
**handwritten list on the wall** are the story's two props.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.

1. **Lock the characters** — front, three-quarter, profile, full body,
   neutral and emotional, present outfit and memory outfit, for both.
   IP-Adapter or a character LoRA per person. Two-shots are most of this
   video, so also generate 3–4 approved *couple* reference stills (sofa,
   kitchen, bench) and reuse them.
2. **Keyframes first** — strongest realistic checkpoint; OpenPose for the
   hug, the dance and the floor-sitting shots; Depth for the split screens.
   16:9 first; 9:16 recomposition for Shorts and the duet challenge.
3. **Animate conservatively** — slow push-in, hair and fabric movement,
   breathing, small hand movement, polaroids being shuffled. Split the hug
   and the kitchen dance into 3–5 s pieces.
4. **Polaroid transitions** are done in the edit, not in Wan: generate the
   memory clip, then composite it inside a polaroid frame and push in.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Keep most shots 4–8 s.

## 4. Shot-by-shot prompts

### Intro — Mahima

**Shot 1 — The box** · *"I found a box beneath our bed"*
> Mahima kneeling on a bedroom floor in warm lamplight pulling a dusty shoebox from under the bed, cream sweater, hair loosely tied, curious gentle expression, slow push-in from behind her shoulder, intimate indie-film realism, soft grain.

**Shot 2 — Polaroids we never framed** · *"Full of polaroids we never framed"*
> Overhead close-up of Mahima's hands lifting the lid of the shoebox to reveal a loose pile of old polaroids, she spreads a few with her fingertips, warm lamplight, shallow depth of field, slow tilt.

**Shot 3 — Your handwriting** · *"Your handwriting on every back"*
> Extreme close-up of Mahima turning a polaroid over to show handwritten words and a date in blue ink on the white back, her thumb resting on the writing, soft warm light, static macro, realistic texture.

**Shot 4 — Silly names** · *"Little dates and silly names"*
> Mahima sitting cross-legged on the floor with polaroids fanned in her lap, laughing quietly at one of them, a hand over her mouth, Noah's blurred figure appearing in the doorway behind her, gentle handheld, warm domestic light.

### Verse 1 — Mahima's memory (the café)

**Shot 5 — First photo** · *"First photo, you in that old grey hoodie"*
> A polaroid held up in Mahima's hand fills the frame: young Noah in an old grey hoodie at a café table holding a paper coffee cup, the photo's edges glow softly and the camera pushes into it until it becomes the live scene, polaroid palette, slight cyan shift, soft grain.

**Shot 6 — Trying not to stare** · *"Coffee in your hand, trying not to stare"*
> Memory: young Noah at a café window table in the grey hoodie, coffee cup halfway to his mouth, glancing across the room and quickly looking down, shy and caught, rain on the window behind him, warm café light, slow push-in.

**Shot 7 — I noticed everything** · *"But I noticed everything about you there"*
> Memory, reverse angle: young Mahima at another table in a denim jacket pretending to read, her eyes lifting to him over the top of the page and staying there, a small private smile, rainy window light, shallow focus, gentle handheld.

**Shot 8 — Cheap earphones** · *"Rain on the window, cheap earphones sharing"*
> Memory: young Mahima and Noah now sitting side by side at the café window sharing a pair of white wired earphones, one bud each, rain streaking the glass, their shoulders just touching, slow lateral dolly, warm and cyan-shifted polaroid look.

**Shot 9 — How you laugh** · *"You said, this one feels like how you laugh"*
> Memory: extreme close-up of young Noah's face turned toward young Mahima, saying something and watching for her reaction, then her laugh breaking out beside him, the earphone cord between them, soft rainy light, slow motion.

### Verse 2 — Noah's memory (the night train)

**Shot 10 — Asleep on my shoulder** · *"Next one, you asleep on my shoulder"*
> A polaroid held in Noah's hand: young Mahima asleep with her head on his shoulder on a train seat, it glows and the camera pushes into it to become the live memory, polaroid palette.

**Shot 11 — Night train** · *"On that night train to nowhere special"*
> Memory: interior of a near-empty night train, young Mahima asleep against young Noah's shoulder, city lights sliding across the window behind them, he sits perfectly still so as not to wake her, wide static shot, dim blue-and-amber light.

**Shot 12 — Watched you breathe** · *"I didn't sleep, I just watched you breathe"*
> Memory: close-up of young Noah looking down at sleeping Mahima on his shoulder, a tender disbelieving expression, his hand hovering near hers on the seat and then gently resting beside it, not quite touching, slow push-in, soft grain.

### Pre-chorus — both

**Shot 13 — Building a forever** · *"We didn't know we were building a forever"*
> Montage of small present-day moments, three quick shots: Mahima and Noah cooking together in a small kitchen bumping hips, both asleep on a sofa under one blanket with a laptop still open, laughing on a rooftop at dusk with takeaway boxes, warm handheld, indie realism.

**Shot 14 — Good morning text** · *"But every little good morning text"*
> Extreme close-up of a phone screen in Noah's hand showing a chat thread of dozens of "good morning" messages scrolling upward, dates changing, his thumb scrolling, then the phone lowering to reveal Mahima asleep beside him, morning window light, soft focus.

### Chorus 1 — both

**Shot 15 — Still writing our story** · *"We're still writing our story"*
> Present day: Mahima and Noah on the bedroom floor with polaroids spread between them, both looking at one photo together, her head leaning on his shoulder in the same pose as the train polaroid, warm lamplight, slow orbit, tender realism.

**Shot 16 — Polaroids and phone screens** · *"In polaroids and phone screens"*
> Fast-cut montage on the beat: a polaroid of them on a beach, a phone screen with a voice note waveform, a polaroid at a birthday with cake on his nose, a phone screen with "are you okay?" and "I'm here", a polaroid of moving boxes, each held in a hand in warm light, rhythmic music-video pacing.

**Shot 17 — Are you okay** · *"In late-night talks and are you okay"*
> Present day, night: Mahima and Noah sitting up in bed in the dark talking, faces lit only by a bedside lamp, she is mid-sentence and he is listening with his full attention, intimate two-shot, static camera, realistic.

**Shot 18 — Every stay** · *"Every stay when we could've gone"*
> Split screen: left, a polaroid of young Mahima and Noah on a park bench; right, present-day Mahima and Noah on the same bench in the same pose, older, closer, her hand in his, the two halves matching exactly, slow simultaneous push-in.

**Shot 19 — The slow scene** · *"If love is a film, then we're the slow scene"*
> Present day: Mahima and Noah brushing their teeth side by side at a small bathroom mirror, she nudges him with her hip, he grins with the toothbrush in his mouth, ordinary and warm, static mirror shot, morning light.

### Verse 3 — the fight (Noah)

**Shot 20 — Kitchen at 3 a.m.** · *"Remember that kitchen at 3 a.m."*
> A blurry polaroid in Noah's hand of an empty kitchen at night, it glows and the camera pushes in: present-tense memory of a small kitchen under cold overhead light at three in the morning, Mahima and Noah standing on opposite sides of the counter, both in sleep clothes, tense silence, static wide, hard shadows.

**Shot 21 — Not enough** · *"You said, maybe we're just not enough"*
> Close-up of Mahima in the cold kitchen light saying something that costs her, eyes wet, arms crossed tight, then a cut to Noah not answering, looking at the floor, jaw tight, two static close-ups, hard overhead light.

**Shot 22 — I sat on the floor** · *"You cried in the bathroom, I sat on the floor"*
> Noah sitting on the hallway floor with his back against a closed bathroom door, holding a mug of tea he isn't drinking, a strip of light under the door, muffled crying implied by his expression, static wide, cold light, quiet drama.

### Verse 4 — the reconciliation (Mahima)

**Shot 23 — Eyes all red** · *"But then you came out with your eyes all red"*
> The bathroom door opening and Mahima stepping out with red swollen eyes, looking down at Noah on the floor, a long beat, then she slides down the wall to sit beside him, medium shot, cold light softening as a hallway lamp comes on, handheld.

**Shot 24 — I just want us** · *"Said, I don't wanna win, I just want us"*
> Close-up two-shot on the hallway floor, Mahima speaking softly with her forehead almost touching Noah's temple, his eyes closing as he hears it, the mug set down beside them, warm lamp light now, shallow focus, near-static.

**Shot 25 — Held you through the shaking** · *"And held you through the shaking and the dust"*
> Mahima and Noah holding each other on the hallway floor, his face in her shoulder, her hand on the back of his head, both shaking slightly, slow push-in, warm lamp against cold kitchen light in the background, realistic emotion.

**Shot 26 — Puffy-eyed** · *"Both of us laughing, puffy-eyed"*
> A blurry selfie polaroid held in Mahima's hand: the two of them the next morning with swollen eyes and messy hair, laughing, faces squashed together, the photo glows and cuts to the live version of the same moment, morning kitchen light, handheld.

**Shot 27 — We didn't die** · *"We almost broke. We didn't die"*
> Extreme close-up of the back of that polaroid, handwritten in blue ink: a short caption, Mahima's thumb brushing over the words, then the camera tilting up to her present-day face, calm and grateful, warm lamplight.

### Chorus 2 (short) — both

Reuse shots 15, 18 and 19 with softer light and slower movement. This chorus
is quieter than the first; it should feel like relief.

### Instrumental

**Shot 28 — Memory montage**
> Lyrical montage in the polaroid palette: Mahima and Noah carrying moving boxes up a stairwell, an airport goodbye at a departure gate with her holding his face, a video call on a laptop at night with her hand on the screen, a reunion hug in an arrivals hall with her feet off the ground, soft grain, gentle motion blur, warm and cyan-shifted.

**Shot 29 — Ambient room**
> Present day: a quiet living room in late afternoon light, dust in the sunbeam, a door closing softly off-screen, Mahima alone on the sofa looking at one polaroid she hasn't shown him, distant traffic through the window, static wide, calm.

### Bridge — Mahima, then Noah, then both

**Shot 30 — The one I haven't shown you** · *"There's one I haven't shown you yet"*
> Close-up of Mahima's hand holding a polaroid face-down against her knee, then slowly turning it over: a packed duffel bag on a bed, the photo glows and the camera pushes in to the memory, warm lamplight, slow motion.

**Shot 31 — Packed a bag, sat back down** · *"You packed a bag, then sat back down"*
> Memory: Noah sitting on the edge of a bed at night with a packed duffel bag beside him, jacket on, keys in his hand, staring at the door, then setting the keys down, static medium shot, single bedside lamp, quiet devastation.

**Shot 32 — Tired of the almosts** · *"I said, I love you, but I'm tired"*
> Memory: Noah on the bed speaking to Mahima who stands in the doorway, his voice breaking, his hands open in his lap, honest and exhausted, close-up, lamp light, near-static.

**Shot 33 — Stop being almost** · *"You said, then let's stop being almost"*
> Memory: Mahima crossing the room and kneeling in front of Noah, taking both his hands, speaking with fierce gentleness, his eyes lifting to hers, two-shot, slow push-in, lamp light.

**Shot 34 — The list on the wall** · *"So we wrote a list on the living room wall"*
> Memory: Mahima and Noah sitting on the living room floor at night writing on a large sheet of paper taped to the wall, a marker passing between them, both crying and both writing, the paper filling with handwriting, slow lateral dolly, warm lamp light.

**Shot 35 — Again and again** · *"And that choice, again and again"*
> Split screen building on the beat: left, the list on the wall at night; right, the same list in daylight now, older, corners curling, still taped up, a new line added at the bottom in fresh ink, both halves pushing in together.

### Final chorus — both

**Shot 36 — Still writing, brighter** · *"We're still writing our story"*
> Present day, golden late-afternoon light: Mahima and Noah dancing badly in the kitchen, socks on tile, her laughing with her head back, him spinning her under his arm, wide handheld, warm and joyful, indie-film realism.

**Shot 37 — I'm proud of you** · *"In I'm proud of you and I messed up"*
> Fast-cut phone screens on the beat, each in a hand: "I'm proud of you", "I messed up", "let's talk", "give me space please", "ok. I love you", warm light, rhythmic pacing.

**Shot 38 — Every us** · *"Every us when it could've been me"*
> Split screen: left, the first-photo café with young Noah in the grey hoodie; right, present-day Noah in the same café seat in the olive hoodie with Mahima now sitting beside him, both halves pushing in until the right side fills the frame, rain on the window in both.

**Shot 39 — The long cut** · *"If love is a film, then we're the long cut"*
> Mahima and Noah walking in light rain under one umbrella on an ordinary street, unhurried, her arm through his, passing the park bench from the polaroid, slow tracking from the side, soft golden overcast light.

### Post-chorus — both

**Shot 40 — Polaroids and phone screens chant**
> Rhythmic sequence on the beat: real couples of all kinds each holding up a single polaroid of themselves to the camera, smiling, different rooms and light, cut fast on the chant, warm and celebratory, music-video pacing. (UGC-style; can be replaced with more shots of Mahima and Noah if no extras are available.)

### Outro — Mahima, Noah, both

**Shot 41 — Back under the bed** · *"I put the box back under the bed"*
> Mahima sliding the shoebox back under the bed in evening lamplight, then pausing and pulling three polaroids back out, slipping them into the pocket of her sweater, gentle handheld, warm, quiet.

**Shot 42 — Just in case** · *"Just in case we forget who we are"*
> Noah in the bedroom doorway holding the folded old grey hoodie he just found in the box, looking at Mahima with a soft smile, she looks back, a whole history in the look, static two-shot, warm light.

**Shot 43 — We're still here** · *"We're still here"*
> Final shot: Mahima and Noah sitting together on the edge of the bed in fading golden light, shoulders touching, looking at one last polaroid together, both smiling quietly, the camera slowly pulling back through the doorway and leaving them there, soft lens flare, no text.

## 5. Edit to the song

Import the WAV and add markers at: the first vocal entrance, the first male
vocal, each chorus, the instrumental break, "We almost broke. We didn't die",
"let's stop being almost", and the final "We're still here." Cut on those.
At 92 BPM a bar is 2.6 s — hold shots for whole bars. Every polaroid
transition lands on a downbeat.

## 6. Vertical teaser and duet challenge

**Teaser (15–20 s)** around *"We're still writing our story / In polaroids
and phone screens."*

1. Mahima pulls the box from under the bed (shot 1)
2. First-photo push-in to the café (shot 5)
3. Split screen, bench then and now (shot 18)
4. The list on the wall (shot 34)
5. Kitchen dance (shot 36)

**Couple duet challenge.** Post the chorus as a two-part duet template — left
side Mahima's lines, right side Noah's, both on the hook — so couples can
sing one half each. Prompt three formats:

- Recreate one old photo in the same pose and place.
- A before/after polaroid transition on the chorus.
- Caption their own story under *"Every stay when we could've gone."*

## 7. Quality-control checklist

- Mahima's and Noah's faces recognisable in every shot, in both timelines
- The grey hoodie only in memory shots and the outro box; the cream sweater only in present day
- Polaroid palette only on memory shots; present day stays warm and neutral
- Split screens match pose and framing exactly
- No duplicated people or distorted hands, especially in the hug and dance
- The fight is cold-lit and static; the reconciliation warms as the lamp comes on
- Phone-screen text has no spelling errors
- Every polaroid transition lands on a downbeat
