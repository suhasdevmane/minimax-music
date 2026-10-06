# Wan 2.2 Shot List — "Ghost in My DMs"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line.

## 1. Visual style

Late-night bedroom pop. Two worlds: the **present** is cool phone-glow blue
in dark rooms, desaturated daylight when she's out; the **memories** are warm,
soft, slightly overexposed. The **phone is a character** — most present-day
shots have it in frame, and the ending is the first frame where it isn't in
her hand. Handheld, intimate, close.

| Section | Grade | Camera |
|---|---|---|
| Intro / present nights | Cool blue phone glow, deep shadow | Static close-ups |
| Memories | Warm, soft, slightly overexposed | Handheld, dreamy |
| Daytime with friends | Natural but desaturated | Handheld |
| Choruses (city) | Evening, streetlights, neon, moody | Tracking |
| Instrumental | Cool blue + one warm lamp | Raw, close |
| Bridge | Single lamp, hard shadows; bathroom flash cold | Static |
| Final chorus / post-chorus | Warmer, brighter, natural | Moving, wider |
| Outro | Clean warm morning | Slow, calm |

## 2. Character bible — paste into every prompt

**Mahima** (present day)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly messy, no makeup, wearing an oversized black hoodie two sizes too big, tired expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (memories)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, light natural makeup, wearing a cropped white t-shirt and high-waisted jeans, open happy expression, realistic cinematic photography, consistent identity

**Mahima** (final chorus / outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied in a loose bun, light natural makeup, wearing a sage-green oversized shirt and jeans, calm rested expression, realistic cinematic photography, consistent identity

**The ex** — never shown clearly: a hand, a shoulder, the back of a head, a figure in a phone-story frame. In memory shots keep him out of focus or cropped at the jaw.
> a young man in his early twenties, back to camera or face out of frame, dark hair, grey hoodie

**The new girl** — only ever on a phone screen, never in the real world.
> a young woman on a phone screen, long hair, similar style to Mahima, posed selfie, slightly over-filtered

**Friends** — two young women, casual, warm, seen on a laptop video call and at a café.

The **black hoodie** is his; she wears it in the present until the final
chorus and never after. The **phone** is in every present-day frame until
shot 61.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, notifications, chats, search bars and story views are
composited in the edit.** Generate the phone as a lit blank screen in her
hand and overlay the UI in post — the model cannot render legible UI, and
the UI is where half this video's storytelling lives.

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

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — dark bedroom, phone glow

1. *"Two a.m., phone glow on my face"* — Mahima (present look) lying on her side in a dark bedroom, face lit only by a phone screen, eyes tired, thumb scrolling slowly, extreme close-up, cool blue, static.
2. *"Your story popped up, same old place"* — the phone screen fills the frame: a lit blank story frame (UI composited: him at a party, laughing, a girl half in frame), her thumb frozen on it.
3. *"You're laughing with them like nothing changed"* — her face, a small flinch, eyes moving across the screen, jaw tightening, close-up, blue glow.
4. *"While I'm here stuck, feeling deranged"* — her locking the phone, the glow dying, her face falling into shadow, a long exhale in the dark, static.

### Verse 1 — memory, then the hoodie

5. *"We said we'd be different, not like the rest"* — memory, warm: Mahima (memory look) and the ex on a couch under one blanket laughing at a movie, his face cropped out of frame at the jaw, handheld, soft overexposed light.
6. *"No games, no lies, just put us to the test"* — memory: a messy kitchen, the ex's hands flipping pancakes, Mahima leaning on the counter laughing, warm morning light, handheld.
7. *"You called me babe, said I was your safe place"* — memory: a night bus, Mahima asleep on his shoulder, only his shoulder and hand in frame, passing lights on the window, warm and dreamy.
8. *"Now I'm just a name you erase from your trace"* — present: Mahima on the bed looking at an old photo on the phone, then swiping it away, the screen going to a blank grid, cool light, close-up.
9. *"I still got your hoodie, smells like your smoke"* — her opening a drawer and pulling out a black hoodie, holding it to her face for one breath, warm lamp, close-up.
10. *"I wear it when I'm sad, like a joke"* — her pulling the hoodie on over her head, swallowing hard, the sleeves past her hands, medium shot, lamp light.
11. *"My girls say, burn it, he's toxic, babe"* — a laptop on the bed with two friends on a video call, animated and mock-stern (UI composited), Mahima half-smiling and shaking her head, over-the-shoulder.
12. *"But it's the closest I get to the way you stayed"* — her curled up on the bed in the hoodie hugging a pillow, the laptop closed, one warm lamp, the rest dark, wide static.

### Pre-chorus 1 — daytime, friends, the buzz

13. *"I swear I'm doing better, most of the time"* — daylight café, Mahima (memory look, no hoodie) laughing with two friends, phone face-up on the table, natural desaturated light, handheld.
14. *"Then your name lights up and I lose my mind"* — the phone on the table buzzing and lighting (notification composited), her smile dropping mid-laugh, close-up on the phone then her.
15. *"I tell myself, don't look, don't care"* — her looking at her friend, nodding, but her eyes drifting back to the phone twice, medium close-up.
16. *"But I'm already stalking your air"* — under the table: her thumb scrolling a profile on the phone in her lap while she pretends to listen, low angle, her face slightly shadowed.

### Chorus 1 — he's everywhere (city montage)

17. *"You're a ghost in my DMs, haunting my nights"* — Mahima walking a city street at evening, phone in hand, streetlights and neon, tracking from the front, desaturated moody.
18. *"Every like, every view, feels like a fight"* — extreme close-up of the phone: a like on an old photo, a view on her story (composited), her thumb hovering.
19. *"I try to move on, but you're everywhere"* — her passing a café window and seeing a couple inside in their old seats who look like them, she slows, then keeps walking.
20. *"In my playlist, my streets, in the clothes that I wear"* — three quick cuts on the beat: a playlist on her phone (his song, composited), the street corner, her catching her reflection in a shop window in an outfit and looking away.
21. *"You're the what if I can't let go"* — her stopped on the pavement, people flowing past, headphones in, eyes closed for one beat, slow push-in.
22. *"The high I miss, even though it broke me slow"* — a two-second warm flash of the couch memory, then back to her face in the cold street light.
23. *"I know I should block, delete, set me free"* — her thumb on the phone over a block button (composited), not pressing it, extreme close-up.
24. *"But you're a ghost in my DMs, and you're still haunting me"* — her walking on with the phone lowered, her reflection ghosting in a dark shop window beside her, tracking from the side.

### Verse 2 — the roof, the new girl

25. *"Remember that night on the roof, just us two"* — memory, warm: a rooftop at night, city lights behind, Mahima and the ex sitting close sharing headphones, his face turned away, handheld.
26. *"Said you'd never leave, said I was your truth"* — memory: Mahima's head on his shoulder, his hand on her hair, the city glow, her eyes closed and smiling, close-up.
27. *"Now you're out there living your best life"* — present: Mahima on her bed in the hoodie, laptop open, blue screen light, staring, static.
28. *"While I'm here Googling how to cut ties"* — extreme close-up of the laptop screen search bar (composited: "how to stop missing someone"), her fingers on the keys.
29. *"I see your new fit, she's got my vibe"* — the phone screen: a selfie of the new girl in a similar style (composited), Mahima's face reflected faintly in the glass.
30. *"Same pose, same smile, same late-night drive"* — split screen: the new girl's photo on the left; an old photo of Mahima in the same pose on the right, the match obvious.
31. *"I hate that I care, but I zoom right in"* — her fingers pinching to zoom on the screen, jaw tight, extreme close-up on the phone and her eyes.
32. *"Then close the app, pretend I didn't"* — her closing the app fast, throwing the phone onto the bed, and covering her face with both hands, medium shot, phone glow gone.

### Pre-chorus 2 — his mum saw my story

33. *"I swear I'm doing better, most of the time"* — daylight: Mahima posting a story, a coffee and a window, a small genuine smile, warm natural light.
34. *"Then your mum likes my post and I lose my mind"* — the story-views list on the phone (composited: a name that is his mum), her small laugh that turns into a wince, close-up.
35. *"Even your family won't let me go"* — memory, warm: a family dinner table, Mahima laughing with an older couple and the ex half in frame, holidays, everyone happy, handheld.
36. *"Like they're keeping tabs on the girl you chose to know"* — present: her looking at the phone a long time, then setting it down gently, bittersweet, medium close-up, cool light.

### Chorus 2 — more haunted

37. *"You're a ghost in my DMs, haunting my nights"* — Mahima walking down a street at night and stopping at a specific spot under a streetlight, looking at it, the first-kiss corner, static wide.
38. *"Every like, every view, feels like a fight"* — reuse shot 18, tighter.
39. *"I try to move on, but you're everywhere"* — inside a shop, a song starting on the speakers, her freezing mid-aisle, then walking straight out, tracking.
40. *"In my playlist, my streets, in the clothes that I wear"* — a fitting room mirror, her catching herself in a top he liked, pulling it off fast and reaching for another, over-the-shoulder into the mirror.
41. *"You're the what if I can't let go"* — reuse shot 21, neon behind her more saturated.
42. *"The high I miss, even though it broke me slow"* — a two-second warm flash of the rooftop, then the cold street.
43. *"I know I should block, delete, set me free"* — reuse shot 23, her thumb closer to the button.
44. *"But you're a ghost in my DMs, and you're still haunting me"* — her sitting on a night bus alone in the hoodie, forehead on the window, the city sliding past, close-up.

### Instrumental — no lyrics, raw

45. Mahima in the shower, water running over her face, crying, close-up, cool blue.
46. Her sitting on the bedroom floor against the bed, phone in hand, typing, deleting, one warm lamp.
47. Her running at night on an empty street, hoodie up, headphones in, breath visible, tracking from the side.
48. Her lying in bed staring at the ceiling, the phone face-down beside her, overhead shot, dark.
49. Brief drop: black frame, then her face in the dark, breathing — the cut into the bridge.

### Bridge — almost, then the promise

50. *"There were nights I almost texted I miss you"* — Mahima in her room at night, phone in hand, single lamp, hard shadows, static.
51. *"Almost drove to your street, almost broke through"* — extreme close-up of her thumb hovering over his name in messages (composited), then her grabbing her keys off the desk.
52. *"Almost let your story rewrite what I knew"* — her at the apartment door with the keys, hand on the handle, stopping, the phone in her other hand still lit with an open story frame, leaning her forehead against the door, medium shot.
53. *"Almost lost the girl I built without you"* — her sliding down the door to sit on the floor, keys loose in her hand, lamp light across her face, static.
54. *"But then I thought of her on the bathroom tiles"* — cold flash: Mahima on a bathroom floor on cold tiles, sobbing, the phone beside her lit with a last message, harsh overhead light, two seconds.
55. *"Phone face down, counting breaths through the tears"* — the bathroom flash continues, her hand turning the phone face down on the tiles, then pressed to her chest, then a hard cut back to the present hallway floor.
56. *"And I swore to her I would not go back there"* — present: her standing up, walking to the bathroom mirror, looking at herself, eyes tired but set, over-the-shoulder into the mirror.
57. *"I swore that this time I choose me"* — extreme close-up of her mouth whispering to the reflection, then her eyes, softer warmer light than the flash.

### Final chorus — taking control

58. *"You're a ghost in my DMs, haunting my nights"* — daylight, warmer: Mahima (final look, bun, sage shirt) at a table with the phone, deleting a contact (composited), a deep breath.
59. *"Every like, every view, feels like a fight"* — the phone: block, unfollow, archive, three taps on the beat (composited), her thumb steady.
60. *"I try to move on, but you're everywhere"* — her unfollowing the new girl too, then putting the phone face-down on the table and pushing it away, close-up.
61. *"In my playlist, my streets, in the clothes that I wear"* — her out with the two friends in daylight, laughing for real, the phone nowhere in frame for the first time, handheld, warm.
62. *"You're the what if I can't let go"* — her dancing alone in her room with the curtains open and daylight in, no hoodie, arms up, wide handheld.
63. *"The high I miss, even though it broke me slow"* — the black hoodie folded and dropped into a donation bag by the door, close-up, warm light.
64. *"I know I should block, delete, set me free"* — her at the window with the afternoon sun on her face, eyes closed, breathing, medium close-up.
65. *"But you're a ghost in my DMs, and you're still haunting me"* — her looking at the phone on the table across the room and not going to it, a small shrug, then turning back to the window.

### Post-chorus — do not disturb

66. *"But tonight I'm turning off the screen"* — night, her bedroom, soft lamp: her thumb switching the phone to do not disturb (composited), extreme close-up.
67. *"Putting my phone on do not disturb, letting me be me"* — her placing the phone face-down on the nightstand and turning off the lamp, the frame going near-black.
68. *"You can haunt my past, but not my future"* — her lying in bed in the dark, no scrolling, just breathing, a little window light on her face, overhead.
69. *"I'm blocking the ghost, I'm closing the door for sure"* — her eyes closing, calm, the smallest real smile, extreme close-up, then darkness.

### Outro — morning

70. *"One day I'll wake and you won't be the first thought"* — morning sunlight through curtains, Mahima waking and stretching, no phone in hand, warm and clean, wide.
71. *"One day your name won't make my chest lock"* — her making coffee at the counter, humming, looking out the window, medium shot, morning light.
72. *"Till then I'll keep choosing me over the pain"* — her slipping the phone into her bag without looking at it, close-up on the hands, warm.
73. *"Even if you're a ghost, I won't let you stay"* — final shot: her walking out the front door into morning light, bag on her shoulder, phone not in her hand, the door closing behind her, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "ghost in my DMs", the
instrumental, "I swore that this time I choose me", "do not disturb", and the
final "stay." At 92 BPM a bar is 2.6 s.

**Phone-POV challenge.** The hook is caption-ready. Post the vertical
phone-POV cut of chorus 1 (shots 17–24) with *"you're a ghost in my DMs"* on
screen and invite people to post their own late-night-scroll, "he viewed my
story", do-not-disturb moments. The do-not-disturb toggle (shot 66) is the
second shareable frame.

## 6. Quality-control checklist

- Three looks in the right sections: black hoodie present-day until the final chorus, never after; sage shirt and bun from shot 58 on
- The ex never has a visible face; the new girl exists only on a screen
- The phone is in every present-day frame until shot 61, and not in her hand from shot 70 on
- All UI composited; no model-generated text
- Memory shots warm and soft; present cold; the bathroom flash is the coldest frame in the video
- No distorted hands, especially the phone close-ups
- The last shot is locked-off and holds until the audio fades
