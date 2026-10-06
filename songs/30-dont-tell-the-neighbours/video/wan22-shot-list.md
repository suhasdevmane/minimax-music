# Wan 2.2 Shot List — "Don't Tell the Neighbours"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
100 BPM a bar is 2.4 s, so most shots run 2–5 s and the choruses cut on the
half-bar where the dembow lands.

## 1. Visual style

One flat in a low-rise south London block, filmed across two nights and one
grey morning. **Everything is under-exposed on purpose**: a single warm lamp,
the blue of a muted television as a second source from the first chorus, and
sodium orange through a curtain from outside. The camera is inside the dance
rather than watching it — handheld, close, often too close, part of the joke.
The two exterior shots of the lit window are the only wide frames in the film
until the last chorus opens the curtains.

The bridge breaks the grade: cold, flat, public light, and it is the only
section shot outside this flat at night.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium orange outside, one warm lamp inside | Static wide, then close inserts |
| Verse 1 | Warm lamp, hard shadows, under-exposed | Handheld, close, low |
| Pre-choruses | Lamp only, ceiling in shadow | Tight, small movements |
| Chorus 1 | Lamp plus muted-television blue | Handheld inside the dance |
| Verse 2 | Night lamp and blue, then flat grey stairwell | Static, straight faces |
| Chorus 2 | Warm inside, sodium behind the curtain | One long unbroken handheld take |
| Instrumental | Lamp and blue, one exterior match cut | Locked-off wide, macro percussion |
| Bridge | Cold, flat, public — bus, table, corridor | Static, wide, unflattering |
| Final chorus | Warm light escaping the flat, exterior lifted a stop | Curtains opening, exterior wide |
| Post-chorus | Lamp only, faces lit, background black | Three angles on one gesture |
| Outro | Warm lamp against first cold blue of morning | Static, held |

## 2. Character bible — paste into every prompt

**Mahima** (both nights)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and moving, smudged eyeliner and no other makeup, wearing an oversized black band t-shirt over bike shorts and thick white socks with no shoes, delighted conspiratorial expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the bridge flashbacks, being small)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tucked inside a coat collar, no makeup, wearing a buttoned-up dark coat and a rucksack held on her lap, closed careful expression, realistic cinematic photography, consistent identity

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a plain white vest and grey joggers, barefoot, easy grinning expression, realistic cinematic photography, consistent identity

**Number Twenty-Four** — a man in his seventies, flat cap, cardigan, carrying a bin bag. Face allowed and warm. He is never angry on camera, only inconvenienced, and by the final chorus he is on the audience's side.
> a man in his seventies, flat cap, grey cardigan, kind lined face, carrying a black bin bag

There are no exes and no rivals. The people at the table in the bridge
flashback are faceless — cropped at the shoulder or out of focus — because the
point is that she cannot be seen in that frame.

Objects: the **door chain**, the **one warm lamp**, the **curtains**, the
**sofa that keeps moving**, the **glass on the shelf**, the **note under the
door**, the **flat cap and bin bag**, the **kettle**, the **two glasses in the
sink**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**The handwritten note, the phone screen, the flat numbers on the doors and
the lift panel are all composited in the edit.** The note is the single most
important text in the video and must be real handwriting shot separately, not
generated.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks, Kai in his one look and Number Twenty-Four with a
consistent reference. **OpenPose is essential for every dance shot** — the
whole video is two people moving in a space about two metres square, and
without pose references the model will float limbs through furniture. Depth
for the flat interiors so the sofa, the shelf and the doorway keep their
positions across the whole film, since the sofa's slow migration across the
room is a running gag.

Low light is the main technical risk. Build every interior still at the target
exposure rather than brightening in post, and keep the lamp inside frame in
most shots as a visible motivation. Animate small: a hand on a mouth, socks
on floorboards, a curtain moving, a light fitting swinging half a centimetre.

16:9 first; 9:16 recomposition for the "shh" post-chorus, which is the main
vertical deliverable.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; the chorus-two long take is assembled from four 5 s pieces.

## 4. Scene per lyric line

### Intro — half eleven

1. *"Half eleven and the block has gone quiet"* — static wide of a low-rise block from the walkway opposite, every window dark except one on the second floor, sodium orange.
2. *"One lamp on and the curtains pulled tight."* — inside: a hand pulling curtains across, the sodium going out, one warm lamp becoming the only light.
3. *"Nothing that happens in this flat leaves this flat"* — the lamp itself, close, the shade warm, the rest of the room black behind it.
4. *"So put your phone face down and come here for that."* — a phone turned face down on a table, the screen light dying under it, macro.

### Verse 1 — the chain and the sofa

5. *"Chain across the door and my shoes in the hall"* — a door chain sliding across, extreme close-up, then two pairs of shoes kicked off in a narrow hall.
6. *"Curtains doing shapes on the back of the wall."* — curtain shapes moving on a wall in lamp light, no people, held.
7. *"You pushed the sofa with your foot and you said, right"* — Kai's bare foot shoving a sofa back, the rug rucking up under it, low angle.
8. *"And the floorboards in this flat haven't settled since eight."* — floorboards in close-up with two pairs of feet crossing them, dust lifting.
9. *"Up on my toes trying to keep the noise low"* — Mahima up on her toes in thick white socks, exaggeratedly careful, full body, handheld.
10. *"And you're doing that thing with your shoulders, and I go."* — Kai doing one small shoulder move; hard cut to her face abandoning all restraint, close.

### Pre-chorus 1 — under the beat

11. *"Keep it low, keep it slow, keep it under the beat"* — both dancing in a space about two metres square, deliberately tiny movements, wide-ish.
12. *"Whisper it, don't shout it, put your hand on the heat."* — her mouth at his ear, both still moving, close, lamp only.
13. *"If the ceiling starts shaking then we've gone too far"* — a ceiling light fitting swinging half a centimetre, unlit, in shadow, static.
14. *"And I don't want to stop, and you know what you are."* — a glass on a shelf ticking against the wall, macro; then her face, decided.

### Chorus 1 — the hook and the wall

15. *"Turn it down, don't tell the neighbours what we do"* — handheld inside the dance, the camera part of it, both faces close and laughing silently.
16. *"Thin walls, low lamp, half eleven, me and you."* — a two-shot with the lamp between them in frame, the whole room dark behind.
17. *"One more song and I promise we're through"* — her holding up one finger, mock-solemn, close-up.
18. *"Turn it down, don't tell the neighbours what we do."* — both of them still dancing, the muted television now throwing blue across half the frame.
19. *"Palm across my mouth and my back against the door"* — his palm across her mouth, both silent-laughing, shot from her side, extreme close-up.
20. *"Bass through the boards and I'm not stopping anymore."* — her back flat against the front door, sliding half a step down it, still moving.
21. *"Number Twenty-Four is banging on the wall again"* — a fist hitting the party wall from the other side, seen only as the wall and a picture frame jumping.
22. *"Turn it down, don't tell the neighbours where we've been."* — both frozen mid-move, straight-faced, two seconds, then moving again on the last beat.

### Verse 2 — three knocks and the stairs

23. *"Half twelve, three knocks, and the wall goes bang bang bang"* — three hard knocks on the party wall, the whole frame flinching with each one, static.
24. *"And we froze like two kids caught halfway through a plan."* — both stopped mid-step with completely straight faces, wide, held a beat too long.
25. *"A note under the door in proper joined-up pen"* — a folded note pushed under the door and stopping on the hallway floor, low angle.
26. *"Saying, some of us have work, and we laughed and did it again."* — the note in her hand, old-fashioned handwriting on it (composited), then the two of them dancing again in the background out of focus.
27. *"Saw him on the stairs this morning with his bin bag and cap"* — morning, a concrete stairwell, Number Twenty-Four coming down with a bin bag and a flat cap, flat grey daylight and a strip light still on.
28. *"Said, sorry about the noise, mate, and I did not mean that."* — Mahima on the stairs, apologising with a face that is not apologising at all, medium.
29. *"He said, no bother, love, and he pressed the lift call"* — his finger on a lift call button (panel composited), the doors, the flat grey light.
30. *"Then he smiled at the floor like he remembered it all."* — his face looking down, a small private smile, close-up, held to the section end.

### Pre-chorus 2 — less careful

31. *"Keep it low, keep it slow, keep it under the beat"* — reuse shot 11's exact framing, the movements twice the size.
32. *"Whisper it, don't shout it, put your hand on the heat."* — her hand flat on his chest, both laughing, close.
33. *"If the ceiling starts shaking then we've gone too far"* — the same ceiling fitting swinging noticeably more, same framing as shot 13.
34. *"And I don't want to stop, and you know what you are."* — the same glass, now moved to the middle of the shelf, macro; then his face, daring her.

### Chorus 2 — every room in the flat

35. *"Turn it down, don't tell the neighbours what we do"* — the start of a long handheld take: the hall, both of them dancing backwards down it.
36. *"Thin walls, low lamp, half eleven, me and you."* — the take continuing into the living room, the sofa now further from the wall than it was.
37. *"One more song and I promise we're through"* — the take reaching the kitchen doorway, fridge light on one side of both faces.
38. *"Turn it down, don't tell the neighbours what we do."* — the take turning and coming back through the living room, television blue washing across.
39. *"Palm across my mouth and my back against the door"* — end of the take: her back against the door again, his palm across her mouth again, both breathless.
40. *"Bass through the boards and I'm not stopping anymore."* — hard cut outside: two silhouettes moving behind a closed curtain, the only lit window on the block.
41. *"Number Twenty-Four is banging on the wall again"* — the party wall from inside with a picture frame visibly out of true now, static.
42. *"Turn it down, don't tell the neighbours where we've been."* — both of them collapsed onto the sofa laughing with no sound, wide, lamp and blue.

### Instrumental — the dance at full size, half volume

43. Locked-off wide of the living room over the plucked-synth solo, both dancing badly and brilliantly, the whole take unbroken.
44. Knuckles knocking on the party wall in tempo, extreme close-up, the knocks becoming the percussion.
45. The sofa sliding another few inches across the floorboards, ground level, nobody visible.
46. Feet in thick white socks on floorboards, two pairs, close, quick.
47. The lit window from the walkway outside, held, one curtain twitching. Match cut back inside on the last beat.

### Bridge — a lifetime of being quiet

48. *"I've spent my whole life keeping the volume down"* — cold flash: Mahima (bridge look) on a night bus taking up as little room as possible, flat public light, static.
49. *"Small in the corridor and small in a crowd."* — cold flash: her flattened against a corridor wall to let people past, wide, unflattering overhead light.
50. *"Made myself easy so nobody complained"* — cold flash: her at a table of loud faceless people, saying nothing, cropped shoulders all around her.
51. *"Kept half of my laugh in the back of my throat and stayed."* — her laughing and immediately covering her mouth, cold light, close, the saddest frame in the film.
52. *"Then you came round on a Tuesday with a bag and a plan"* — warm again: the front door opening on Kai holding a carrier bag, hall light, static.
53. *"And I haven't been quiet since, and I don't think I can."* — both of them sitting on the floor with their backs against the sofa, out of breath, saying nothing, wide, warm.

### Final chorus — turn it up

54. *"Turn it down, don't tell the neighbours what we do"* — her hand arriving on a speaker dial, close, held on the last word before she moves it.
55. *"Thin walls, low lamp, half eleven, me and you."* — the dial turning the other way, macro, the room getting louder without the frame changing.
56. *"One more song, and I'm not promising we're through"* — her pulling the curtains fully open instead of closed, warm light spilling out onto the walkway.
57. *"Turn it up, let the neighbours hear it too."* — exterior wide of the block with the window now open and lit, light on the walkway, the grade a stop brighter.
58. *"Palm across my mouth and my back against the door"* — inside again, his palm across her mouth and her pulling it away this time, close.
59. *"Bass through the boards and I'm not stopping anymore."* — both dancing full size with the window open behind them, nothing small about it, wide handheld.
60. *"Number Twenty-Four can put the kettle on again"* — the other side of the party wall: Number Twenty-Four putting a kettle on, entirely calm, not banging on anything, static, two seconds.
61. *"Turn it up, let the neighbours know where we've been."* — the block from outside with two more windows now lit, nobody complaining, wide.

### Post-chorus — the whispered chant

62. *"Shh, shh, don't tell the neighbours"* — a finger to lips in close-up, angle one, lamp on the face, black behind.
63. *"Shh, shh, thin walls, low lamp."* — the same gesture, angle two, tighter.
64. *"Shh, shh, don't tell the neighbours"* — the same gesture, angle three, both of them doing it at once.
65. *"One more song and then we'll stop, I promise."* — locked-off wide of the living room, both doing the same two-count step exactly in time, the whole move learnable from this one frame.

### Outro — four in the morning

66. *"Four in the morning and the buzzer's gone still"* — an intercom buzzer panel by the door, dark and silent, macro.
67. *"Two glasses in the sink and the lamp on the sill."* — two glasses in a kitchen sink; the lamp moved onto the window sill, grey light starting behind the open curtain.
68. *"Somebody's alarm going off through the wall"* — the party wall, static, faint alarm audible, nothing moving in frame.
69. *"And we're still up, and I'm not sorry at all."* — final shot: both on the floor with their backs to the sofa, her looking at the wall and shrugging, warm lamp against the first cold blue of morning. Locked off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the curtain pull in shot 2, each *"don't tell the neighbours"*, the
three knocks at shot 23, the note landing, the first cold bridge flash, the
dial turning at shot 55, the kettle, and the shrug. At 100 BPM a bar is 2.4 s;
the choruses cut on the half-bar and the three knocks in shot 23 land exactly
on beats one, two and three of a bar.

**The "shh" challenge.** The post-chorus (shots 62–65) is the deliverable: a
finger to lips, three angles, then one locked-off wide with a two-count step
anybody can copy from a single clip. Post it vertically captioned *"nothing
that happens in this flat leaves this flat."* The second shareable frame is
shot 19 — a palm across a mouth, both silent-laughing — which is the hook
image of the whole record.

## 6. Quality-control checklist

- The whole film is under-exposed on purpose and the lamp is visible in most interior frames as the motivation; nothing is brightened in post
- The sofa moves further from the wall in every successive interior wide — check the running gag holds in shots 7, 36, 45 and 53
- The glass on the shelf moves between shots 14 and 34; the picture frame goes out of true between shots 21 and 41
- Number Twenty-Four is never angry on camera and is on the audience's side by shot 60
- The bridge flashbacks are the only cold, flat, public frames in the film, and the people around her in shot 50 are faceless
- OpenPose on every dance shot; nothing floats through the furniture in a two-metre space
- The handwritten note is real handwriting shot separately and composited; no model-generated text anywhere
- Light only escapes the flat from shot 56 onward, and the last shot holds on warm lamp against cold morning
