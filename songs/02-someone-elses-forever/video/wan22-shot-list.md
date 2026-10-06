# Wan 2.2 Shot List — "Someone Else's Forever"

Source: `../source/improved-version-perplexity.pdf`. The 35 shots, character
bible, workflow, teaser and QC checklist below are that document's, adapted
for local Wan 2.2 in ComfyUI. Shot prompts are kept verbatim; each is anchored
to the lyric it covers so cuts land on phrases, not timestamps.

Timestamps come from the rendered WAV. Mark it up in your editor first (see
§5) and slot shots to the markers — do not guess from word counts.

## 1. Visual style

Cinematic romantic-drama: realistic faces, natural skin texture, controlled
camera movement, soft rain, shallow depth of field, blue-and-gold palette.

| Time layer | Look |
|---|---|
| Past memories | Warm amber, sun flare, handheld camera, soft film grain |
| Wedding present | Cool blue shadows, elegant golden practical lights, composed camera |
| Rain confrontation | Deep blue, silver reflections, slow dolly shots, emotional close-ups |
| Final release | Pale sunrise, warm natural light, wider compositions, gentle forward camera |

Build the video from short shots, never one continuous generation. Generate a
clean reference image for each character first, then reuse it in every shot.

## 2. Character bible — paste into every prompt

Wan 2.2 has no character memory; identity consistency comes from repeating the
exact same description and reusing the same reference still. Copy verbatim.

**Mahima** (present day)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair, small silver earrings, graceful natural features, emotionally restrained expression, wearing a deep blue flowing dress, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (memory, seventeen)
> Same female protagonist Mahima at seventeen, expressive dark eyes, oval face, long dark wavy hair loosely tied, small silver earrings, casual summer clothes, youthful open expression, realistic cinematic photography, consistent identity

**Aarav** (present day)
> Same male protagonist Aarav, young man in his mid-twenties, dark wavy hair, warm brown eyes, lean build, charcoal suit, simple silver watch, small scar above the right eyebrow, realistic cinematic photography, consistent identity

**Aarav** (memory, seventeen)
> Same male protagonist Aarav at seventeen, dark wavy hair, warm brown eyes, lean build, plain white shirt with rolled sleeves, small scar above the right eyebrow, hopeful expression, realistic cinematic photography, consistent identity

**Bride**
> Same bride, young woman in her mid-twenties, kind expressive eyes, elegant ivory wedding gown with a delicate veil, understated jewellery, gentle smile, dignified and warm presence, realistic cinematic photography

Mahima's signature is the **deep blue dress** — the colour he once said was
hers. Keep hairstyle, face shape, earrings and the blue consistent. For Aarav,
keep the eyebrow scar, hairstyle, watch and suit consistent. The bride stays
kind and dignified, never villainous — the conflict is timing and sacrifice,
not betrayal.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

## 3. Wan 2.2 workflow

**Image-to-video, not text-to-video.** Generate one strong still per shot,
approve the face, hands, costume and composition, then animate that frame.

1. **Lock the characters.** Per character: front portrait, three-quarter,
   side profile, full body, neutral and emotional expression, wedding outfit
   and memory outfit. Use IP-Adapter or a character LoRA for Mahima, a second
   reference or LoRA for Aarav.
2. **Keyframes first.** Strongest realistic checkpoint; ControlNet OpenPose for
   walking, embracing and confrontation shots; Depth or SoftEdge ControlNet
   for stable compositions. 16:9 first for YouTube; separate 9:16 crop or
   recomposition for Shorts.
3. **Animate conservatively.** Slow push-in, hair/dress movement, rain, eye and
   breathing motion, gentle hand movement. No choreography, long walks,
   kissing, crowd interaction or fast hand gestures in one clip — split those
   into 3–6 s shots.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Keep most shots between 4 and 8 seconds.

## 4. Shot-by-shot prompts

### Intro

**Shot 1 — Wedding arrival** · *"I wore the colour you once said was mine"*
> Cinematic establishing shot of an elegant countryside wedding estate at blue hour, warm golden lights glowing through tall windows, light rain beginning, Mahima arriving alone in a deep blue flowing dress, holding a small black clutch, long dark wavy hair moving gently in the wind, slow camera push-in, romantic heartbreak atmosphere, realistic film photography, 35mm lens.

**Shot 2 — Third row** · *"Sat in the third row, three seats from the aisle"*
> Interior wedding ceremony, Mahima seated alone in the third row, three seats from the aisle, deep blue dress contrasting with ivory flowers and warm candlelight, guests softly blurred in foreground, she sits upright and composed while hiding sadness, slow lateral camera movement, cinematic shallow depth of field.

**Shot 3 — The familiar song** · *"The band played the song we used to hum"*
> Close-up of Mahima listening to a live wedding band, soft piano and guitar players blurred behind her, her eyes glistening but she does not cry, warm lights reflected in her eyes, subtle breathing, slow push-in, intimate cinematic close-up.

**Shot 4 — First eye contact** · *plays under "I smiled like a stranger, like we were never one"* (the intro's second stanza was cut to fit the 6-minute cap; the eye-contact beat stays)
> Over-the-shoulder shot from behind Mahima toward Aarav standing at the altar in a charcoal suit, his eyes suddenly meeting hers across the wedding guests, bride beside him softly out of focus, golden lights and cool shadows, restrained shock, slow rack focus from bride to Aarav.

### Verse 1 — Memory

**Shot 5 — Seventeen** · *"We were seventeen, with the whole sky to steal"*
> Warm summer memory, teenage Mahima and teenage Aarav running through a golden field beneath a huge sunset sky, laughing freely, youthful romantic energy, handheld 35mm camera, glowing sun flare, soft nostalgic film grain.

**Shot 6 — Bridge carving** · *"Carved our names where the old bridge met the field"*
> Close-up of young Mahima and Aarav carving their initials into the wooden railing of an old railway bridge, hands touching, golden grass moving in the wind, intimate youthful romance, slow handheld camera movement, warm amber colour grade.

**Shot 7 — The promise** · *"You said, one day, they'll understand us too"*
> Two young lovers sitting on an old railway bridge at sunset, Aarav speaking hopefully while Mahima looks at him with complete trust, distant railway line and glowing sky behind them, gentle breeze moving her hair, slow orbiting camera, emotional cinematic realism.

**Shot 8 — Illness and goodbye** · *"There was a house and a family waiting still"*
> Present-day memory inside a modest family home, Aarav sitting distressed near his ill father's bedroom door, Mahima standing beside him with quiet understanding, muted evening light, emotional but dignified, slow static camera, realistic drama film.

**Shot 9 — Letting him go** · *"I held your face and said, go, I'll be fine without you"*
> Emotional close-up of Mahima holding Aarav's face with both hands, tears held back, she forces a brave smile and gently tells him to go, he is devastated, soft window light, shallow depth of field, almost no camera movement, realistic facial emotion.

### Pre-chorus

**Shot 10 — Walking away** · *"Watching you leave with my heart in your hold"*
> Rear tracking shot of Aarav walking away down a quiet street while Mahima remains alone in the doorway, evening rain beginning, her hand slowly falling from the doorframe, long emotional silence, cinematic blue-and-amber lighting.

**Shot 11 — Candle metaphor** · *"Some love is a candle you carry at night"*
> Poetic close-up of Mahima walking alone through a dark hallway carrying a small candle protected by both hands, her face illuminated by warm flame, background fading into blue darkness, gentle camera movement, symbolic cinematic music-video imagery.

### Chorus

**Shot 12 — Wedding celebration** · *"So dance with your forever, I'll clap along"*
> Wedding guests dancing under warm string lights, Mahima clapping softly from the edge of the room while trying to smile, Aarav and the bride dancing in the background, slow circular camera movement, beautiful celebration with visible emotional distance.

**Shot 13 — The knife line** · *"I taught your hands how to hold her tight"*
> Extreme close-up of Aarav's hands gently holding the bride's hands during the wedding dance, Mahima visible as a soft reflection in a glass window behind them, emotional symbolism, slow motion, elegant warm lighting, cinematic realism.

**Shot 14 — Back of the room** · *"I'll be the girl who loved you in a song"*
> Wide shot from the back of a wedding hall, Mahima standing alone near the doorway while everyone else celebrates, warm lights forming a halo around the dancing couple, she remains in cool blue shadow, slow pull-back camera, bittersweet cinematic composition.

**Shot 15 — Viral hook close-up** · *"You're someone else's forever now"*
> Direct cinematic close-up of Mahima looking toward the altar, a single tear finally moving down her cheek, she gives a small accepting smile instead of breaking, wedding lights reflected in her eyes, slow gentle push-in, realistic emotional performance.

### Post-chorus

**Shot 16 — Repeating memory** · *"I loved you first, but I let you go"*
> Match-cut style sequence showing young Mahima releasing Aarav's hand in the sunset memory, transitioning to present-day Mahima releasing the edge of her chair at the wedding, warm memory transforming into cool present, smooth cinematic dissolve.

### Verse 2

**Shot 17 — His mother** · *"Your mother hugged me, said, you're still our girl"*
> Aarav's mother warmly hugging Mahima at the wedding reception, Mahima smiling politely while hiding overwhelming sadness, floral decorations and guests blurred behind them, slow close camera movement, natural emotional acting, elegant wedding realism.

**Shot 18 — The bride** · *"The bride looked kind beneath her veil of white"*
> Close-up of the kind bride smiling softly beneath a delicate ivory veil, no villainous expression, warm natural light, Mahima watching her from the background with conflicted compassion, shallow depth of field, slow rack focus between the two women.

**Shot 19 — Third-row pain** · *"Where I held my heart together underneath"*
> Medium close-up of Mahima seated in the third row, fingers tightly clasped in her lap, deep blue fabric trembling slightly, she silently controls her breathing while the wedding ceremony continues, gentle handheld camera, cool shadows and warm highlights.

**Shot 20 — His repeated glance** · *"You kept looking past her to the third-row seat"*
> Over-the-shoulder shot behind the bride as Aarav looks past her toward Mahima, his expression filled with regret and conflict, bride remains calm and unaware, wedding guests softly blurred, slow focus pull toward Mahima.

### Pre-chorus 2

**Shot 21 — Don't look at me** · *"Don't look at me, you'll give us away"*
> Close-up of Mahima lowering her eyes as Aarav looks toward her, she subtly shakes her head and silently mouths "don't", crowded wedding hall around them, tension hidden beneath ceremony, controlled camera push-in.

**Shot 22 — The wrong side** · *"I'm only the girl on the wrong side of the end"*
> Symbolic wide shot of Mahima standing on one side of a long wedding hallway while Aarav stands far away on the other side, guests pass between them like moving shadows, cool blue light around Mahima, golden light around Aarav, slow symmetrical camera movement.

### Chorus 2 + Post-chorus 2

Reuse shots 12–16 with changed angle, lighting or expression. The first
chorus shows pain; save the release for the final chorus.

### Instrumental

**Shot 23 — Memory montage**
> Dreamlike montage of Mahima and Aarav's memories: running across a field, laughing beneath the railway bridge, sharing headphones on a train platform, hands almost touching, warm golden colour, gentle motion blur, soft film grain, lyrical music-video pacing.

**Shot 24 — Present-day isolation**
> Mahima alone in a quiet side room at the wedding, looking at an old photograph of herself and Aarav, distant celebration lights flickering through glass doors, she slowly turns the photograph face down, restrained emotion, slow dolly backward.

### Bridge

**Shot 25 — Rain at the garden door** · *"You found me in the rain by the garden door"*
> Nighttime wedding estate garden in heavy rain, Mahima standing beneath a glass garden doorway in her deep blue dress, Aarav running toward her in a soaked charcoal suit, dramatic backlight from the reception hall, slow-motion rain, cinematic romantic drama.

**Shot 26 — Wait, don't go** · *"Said, wait, don't go, I can't do this anymore"*
> Intense close-up of Aarav standing in the rain, begging her to wait, desperate, wet hair, tears blending with rain, the wedding reception glowing behind him through the glass, slow handheld push-in, realistic emotional performance.

**Shot 27 — The impossible choice** · *"One word, and I'll leave tonight"*
> Two-shot of Mahima and Aarav facing each other under the garden doorway, both crying quietly, his hand reaching toward hers but stopping before touching, rain between them, deep blue lighting, slow circular camera movement, tragic romantic tension.

**Shot 28 — Her decision** · *"But I saw your mother smiling through her tears"*
> Close-up of Mahima looking through the glass door toward Aarav's mother smiling proudly inside the wedding hall, bride waiting near the altar, Mahima's expression changes from longing to heartbreaking clarity, slow rack focus, warm interior versus cool rain exterior.

**Shot 29 — Letting go twice** · *"It's a girl at your wedding letting you go twice"*
> Mahima gently places one hand against Aarav's chest, gives him a tearful but peaceful smile, then slowly steps backward into the rain while he remains frozen, she turns away without looking back, elegant slow dolly shot, powerful emotional release.

### Final chorus

**Shot 30 — Walking alone** · *"But I'm finally learning to breathe somehow"*
> Mahima walking alone through the rain outside the wedding estate, removing one hairpin and letting her long hair fall naturally, she takes a deep breath, camera moves backward in front of her, blue night slowly beginning to brighten.

**Shot 31 — Choosing herself** · *"Now I'm teaching my heart to survive the night"*
> Mahima sitting alone in the back seat of a vintage car, rain sliding across the window, she looks at her reflection and gently wipes away her tears, then smiles with quiet strength, soft dashboard light, slow intimate close-up.

**Shot 32 — Carrying her heart home** · *"I gave you my heart, then I gave you away"*
> Wide shot of Mahima leaving the wedding estate through an open gate, blue dress moving in the rain, distant wedding lights behind her, she walks toward the road and dawn beyond it, slow crane upward, cinematic sense of freedom.

**Shot 33 — Final hook** · *"You're someone else's forever now / But I'm finally mine now"*
> Sunrise on a quiet city street, Mahima walking toward golden morning light, rainwater shining on the pavement, she turns once toward the distant wedding estate, then faces forward with a peaceful confident smile, slow forward tracking shot, warm hopeful cinematic ending.

### Outro

**Shot 34 — Washing the colour** · *"I'll wash it clean in the morning light"*
> Morning interior, Mahima standing before a mirror in soft sunlight, removing the deep blue shawl from her shoulders and placing it beside a window, no sadness in her expression, only calm acceptance, gentle camera pan, natural light.

**Shot 35 — Final image** · *"And I'm finally mine now"*
> Final wide cinematic shot of Mahima walking alone beneath trees in warm sunrise light, wind moving her hair and dress, the camera slowly pulls away as she becomes smaller but more free, hopeful romantic-drama ending, soft golden lens flare, no text.

## 5. Edit to the song

Import the final WAV and add markers at: the first vocal entrance, each
chorus, the instrumental break, the line "wait, don't go", the line "You're
someone else's forever now", and the final "I'm finally mine now." Cut on
those, never on round timestamps. At 96 BPM a bar is 2.5 s — hold shots for
whole bars.

## 6. Vertical teaser (15–20 s)

Built around *"You're someone else's forever now / But I'm finally learning
to breathe somehow."*

1. Mahima seated at the wedding (shot 2)
2. Aarav looking toward her (shot 20)
3. Rain confrontation (shot 27)
4. Mahima walking away (shot 29)
5. Final close-up: "I'm finally mine now" (shot 35)

On-screen lyrics only during the hook, large and high-contrast. The teaser
must be understandable within the first two seconds.

## 7. Quality-control checklist

- Mahima's face recognisable in every shot
- Aarav's scar and watch consistent
- No duplicated guests or distorted hands
- No unexplained costume changes
- The bride remains sympathetic
- The emotional twist is clear without dialogue
- The final chorus visibly changes from grief to freedom
- Cuts land on musical phrases, not random timestamps
- Rain, lighting, grain and colour grading match across shots
- On-screen lyrics contain no spelling errors
