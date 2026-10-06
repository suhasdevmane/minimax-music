# Wan 2.2 Shot List — "Sunday Mornings"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
100 BPM a bar is 2.4 s; most shots run 3–5 s and the choruses cut on the bar.

## 1. Visual style

One sunlit bedroom and its balcony, filmed across a year. **The window is
the clock**: every time the camera returns to it the season outside has
moved on, bare branches to full green to frost to summer and back to buds.
The room itself barely changes; the objects accumulate (a second mug, a
plant, a cat, coffee rings on the nightstand). Warm, soft, slightly
overexposed, film-grain, handheld and close. The weekday inserts are the only
cool frames in the video. Kai has a face here; he is in half the shots.

| Section | Grade | Camera |
|---|---|---|
| Intro / Sunday one | Pale spring light, soft, a little cool | Static close-ups, one slow tilt |
| Verse 1 | Curtain-striped warm light, then full spring sun | Handheld, intimate |
| Pre-choruses (weekday inserts) | Cool, flat, desaturated | Fast static cuts |
| Pre-choruses (balcony) | Gold | Slow push-in |
| Choruses | Warmest light, window flare, film grain | Handheld montage, overhead |
| Verse 2 | Winter white, then lamp warmth, then summer gold | Handheld |
| Instrumental | Full gold into dappled green | One continuous push-in |
| Bridge | Dappled leaf light moving on the sheets | Static, close |
| Final chorus / post-chorus | Widest, brightest | Moving, wider |
| Outro | Pale spring again, a degree warmer than the intro | Locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (Sunday one, intro and verse 1)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and sleep-tangled on the pillow, no makeup, wearing an oversized men's blue flannel shirt to her knees, shy careful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the Sundays after, verse 2 through final chorus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in a loose messy bun with strands falling, no makeup, wearing a white cotton camisole and soft grey shorts, relaxed happy expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge and outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose over one shoulder, no makeup, wearing the same oversized blue flannel shirt, calm wondering expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the boyfriend)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded grey t-shirt and navy sleep shorts, sleepy warm expression, realistic cinematic photography, consistent identity

Objects that carry the year: the **blue flannel shirt** (hers now), the
**two mugs** (a white one and a chipped green one), the **coffee rings** on
the wooden nightstand (one in verse 1, several by the second chorus), the
**pothos on the windowsill** (from verse 2), the **grey cat** (from Sunday
fifty), the **balcony rail** (bare, then frosted, then with the cat on it).

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, alarms, inboxes and forms in the weekday inserts are
composited in the edit.** Generate the phone and laptop as lit blank
screens and overlay the UI in post — the model cannot render legible UI.
The newspaper in verse 2 is generated as blurred grey columns, never
readable print.

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

Most shots 3–5 s. For this song there is no ex; Kai is locked with his own
LoRA. The one OpenPose shot is the kitchen dance in the instrumental. The
season-change push-in (shot 44) is four plates of the same window
cross-dissolved in the edit, not one generation.

## 4. Scene per lyric line

### Intro — Sunday one, not moving

1. *"The first one, I woke up before you and I didn't move"* — Mahima (Sunday-one look) lying on her side on a white pillow, eyes open, absolutely still, Kai asleep behind her with his arm heavy across her waist, pale spring light, extreme close-up, static.
2. *"Counting the cracks in a ceiling that wasn't mine"* — her POV: a white ceiling with a hairline crack, then a second one, the camera drifting very slowly, soft light.
3. *"You mumbled something about coffee in your sleep"* — Kai's face half in the pillow, mouth moving, eyes shut, close-up, then her eyes in the foreground flicking toward him.
4. *"And I thought, okay, I could get used to this in time"* — her trying and failing to hide a smile, the camera tilting from her face up to the window, bare early-spring branches outside, slow tilt.

### Verse 1 — Sundays one and six

5. *"Sunday number one, we were shy about the light"* — Kai reaching over to pull the curtain across the bright window, sheepish, medium shot, the light narrowing to a stripe.
6. *"You kept the curtains closed like the morning might stare"* — the curtain-striped light on the sheets, Mahima pulling the duvet up to her nose, only her eyes showing, close-up.
7. *"I wore your flannel to my knees and I burned the eggs"* — Mahima in the small kitchen in the oversized blue flannel shirt, smoke rising from a pan, waving a tea towel at it, wide handheld.
8. *"You ate them anyway and swore you didn't care"* — Kai at the counter eating black-edged eggs with a straight face, then cracking up, Mahima's hand covering her face, medium.
9. *"Sunday number six, you already knew my order"* — the window: full green leaves now. Over Kai's shoulder at the counter: two mugs, a white one and a chipped green one, close-up.
10. *"Two sugars and a splash, and you never asked me twice"* — his hands dropping two sugars into the green mug and adding a splash of milk without looking, macro, morning sun.
11. *"I stood in the doorway while you poured out two"* — Mahima leaning on the doorframe in the flannel, arms folded, watching him, backlit by the bedroom window, medium.
12. *"Thinking, I could stand here all my life"* — close-up of her face in the doorway, the smile she is not hiding this time, slow push-in.

### Pre-chorus 1 — the week versus Sunday

13. *"Monday's got alarms, and Tuesday's got the train"* — two fast cool inserts: a hand slapping an alarm clock on the nightstand; a commuter train window with grey buildings sliding past.
14. *"Wednesday wants an answer, Thursday wants my name"* — two more: a laptop inbox glowing (UI composited) in a flat office; a pen hovering over a signature line on a form (composited, illegible).
15. *"But Sunday doesn't ask me to be anyone"* — hard cut to warmth: Mahima's bare feet stepping onto a sunlit balcony floor, low angle, gold.
16. *"Just barefoot on your balcony, that's all"* — her leaning on the balcony rail in the flannel, green mug in both hands, eyes closed, the city soft behind, slow push-in.

### Chorus 1 — small things

17. *"Give me Sunday mornings, messy hair and coffee rings"* — overhead: Mahima's dark hair spread messy across the white pillow, laughing up at the camera, a coffee ring on the nightstand at the edge of frame, warm and overexposed.
18. *"Your voice before you're really awake, a window open, small things"* — Kai's face half in the pillow saying something, eyes still shut; cut to the window being pushed open, leaves and light.
19. *"Give me Sunday mornings, no alarm, no place to be"* — the alarm clock on the nightstand face-down, then a stripe of sun crawling across the sheets, macro.
20. *"Sun across the pillow and your arm across me"* — Kai's arm across her waist, her hand resting on it, the sun stripe over both, close-up, still.
21. *"Give me every Sunday, and the Sundays after that"* — the two of them under the duvet laughing at something, the camera handheld above them, lens flare from the window.
22. *"Give me Sunday mornings, I don't need more than that"* — wide of the whole room in full sun: bed, window, two mugs, one coffee ring, the flannel over a chair, locked-off.

### Verse 2 — Sundays twenty, thirty, fifty

23. *"Sunday number twenty, there was frost along the rail"* — the balcony rail rimed with frost, macro, breath fogging past the lens, winter-white light.
24. *"Two mugs, one blanket, and the paper split in two"* — Mahima and Kai on two balcony chairs under one blanket, each holding half a newspaper (blurred columns, never readable), the two mugs steaming on the ledge, medium wide.
25. *"Sunday number thirty, you were sick, I made the soup"* — Mahima (second look) carrying a bowl of soup into the bedroom, Kai pale under the duvet with a tissue box, lamp light, handheld.
26. *"You said it tasted like a home, and I said, that's you"* — Kai tasting the soup and saying something, Mahima on the edge of the bed laughing and pushing his shoulder, close-up two-shot, warm lamp.
27. *"Sunday number fifty, there's a cat we didn't plan"* — the window: full summer again. A grey cat walking across the duvet and sitting squarely on Kai's chest, his hands up in surrender, medium.
28. *"Pancakes in the shape of nothing we have seen before"* — a pan of misshapen pancakes, the two of them squinting at one on a spatula and arguing, kitchen, morning sun, handheld.
29. *"There's a plant on the sill that we've kept alive two years"* — a pothos on the windowsill with the summer leaves behind it, Mahima's hand turning it toward the light, macro.
30. *"And the ceiling that I counted, I don't count it anymore"* — Mahima lying back on the pillow looking up at the ceiling crack, eyes soft, not counting, extreme close-up, still.

### Pre-chorus 2 — the week again, faster

31. *"Monday's got alarms, and Tuesday's got the train"* — reuse shot 13, cut tighter, half a beat each.
32. *"Wednesday wants an answer, Thursday wants my name"* — reuse shot 14, cut tighter.
33. *"But Sunday doesn't ask me to be anyone"* — hard cut to warmth: her bare feet on the summer balcony, the grey cat winding around her ankles, low angle.
34. *"Just barefoot on your balcony, that's all"* — Mahima at the rail in the camisole, Kai stepping out behind her with the two mugs, her leaning back into him, medium, gold.

### Chorus 2 — a year of Sundays

35. *"Give me Sunday mornings, messy hair and coffee rings"* — the nightstand: now four or five overlapping coffee rings on the wood, the green mug being set down on a new one, macro.
36. *"Your voice before you're really awake, a window open, small things"* — reuse shot 18, tighter on Kai's mouth in the pillow.
37. *"Give me Sunday mornings, no alarm, no place to be"* — the window in one push-in, spring leaves cross-dissolving to frost to summer, the room unchanged around it.
38. *"Sun across the pillow and your arm across me"* — the cat asleep in the gap between them, Kai's arm across both Mahima and the cat, overhead, warm.
39. *"Give me every Sunday, and the Sundays after that"* — Mahima sitting cross-legged on the bed brushing her hair while Kai reads, the sun stripe across both, wide.
40. *"Give me Sunday mornings, I don't need more than that"* — reuse shot 22's wide of the room, now with the plant, the cat and the extra mug in it, locked-off.

### Instrumental — a silent Sunday

41. Mahima dancing in socks in the kitchen with a spatula as a microphone, Kai watching from the doorway with his arms folded and grinning, wide handheld, gold (OpenPose).
42. The two of them on the balcony with their feet up on the rail, the cat on the ledge, the city soft, static wide.
43. The cat chasing a sunbeam across the bedroom floor, low angle, slow motion.
44. A slow continuous push-in on the window as the leaves outside change colour, green to gold to bare to green, the room still, the shareable shot.
45. Drop: Mahima alone on the bed in dappled leaf light, propped on one elbow, Kai asleep beside her — the cut into the bridge.

### Bridge — the math

46. *"Then one Sunday you were sleeping, and the light came through the leaves"* — dappled leaf-light moving on Kai's sleeping face, Mahima (bridge look) watching him, close-up, static.
47. *"And I did the math on all the Mondays I would ever have to leave"* — her eyes moving from him to the door to her keys on the nightstand, three slow looks, extreme close-up.
48. *"And I don't want a single one without you in it"* — her hand resting flat on his chest, the light moving over both, macro.
49. *"Not a Tuesday, not a Thursday, not a minute"* — her face, the enormity of it arriving quietly, a breath, close-up.
50. *"I used to think that Sunday was the day I got to rest"* — her looking at the window, the leaves moving, the light steadying, medium.
51. *"Turns out Sunday's just the day I get to see you best"* — back to him asleep, her thumb touching his beard, close-up.
52. *"So I woke you up to tell you, and you said, go back to sleep"* — her shaking his shoulder, Kai not opening his eyes, mumbling, waving a hand, close two-shot.
53. *"Then you pulled me in and said, I know, I've known for weeks"* — his arm pulling her in against his chest, his eyes opening just enough to smile, the light going full sun as the band returns, close-up, hold.

### Final chorus — every morning

54. *"Give me Sunday mornings, messy hair and coffee rings"* — reuse shot 17, the overhead of her hair on the pillow, now Kai's head in frame too, both laughing.
55. *"Give me Monday mornings too, the alarms and everything"* — a Monday: the alarm going off and both of them groaning and laughing under the duvet instead of getting up, a shirt and tie hanging on the door, handheld.
56. *"Give me Sunday mornings, and the Wednesdays in between"* — a Wednesday: the two of them on the balcony in work clothes with coffee, five stolen minutes, morning, medium.
57. *"Sun across the pillow and your arm across me"* — his arm across her on a weekday, her half in a blouse, the sun stripe, close-up.
58. *"Give me every Sunday, and the Sundays after that"* — the window through all four seasons again in a faster push-in, then the room.
59. *"Give me all the mornings, I don't need more than that"* — wide of the room at full brightness, the two of them sitting up in bed with mugs, the cat, the plant, the coffee rings, everything in frame, locked-off.

### Post-chorus — the inventory

60. *"Messy hair, coffee rings"* — two quick macros on the beat: her hair on the pillow; a coffee ring.
61. *"Cat on the bed, the window open, small things"* — three quick cuts: the cat; the window pushed open; Kai's sleepy face.
62. *"Messy hair, coffee rings"* — the same two macros, tighter.
63. *"Fifty Sundays down, and I'm not counting anything"* — Mahima's face on the pillow looking straight up, eyes soft, the smallest shake of her head, extreme close-up.

### Outro — Sunday one, reversed

64. *"Sunday number one, I didn't move, I didn't dare"* — a flash of shot 1, Mahima awake and still, pale spring light, one second.
65. *"Sunday number fifty, I'm the one still sleeping there"* — the mirror of shot 1: Kai awake on the pillow, very still, watching Mahima asleep with her hair across her face, his arm across her, extreme close-up.
66. *"So if you wake before me, don't move, there's nowhere to be"* — Kai not moving, a small smile, the alarm clock face-down behind him, static.
67. *"It's Sunday, it's Sunday, and you get to look at me"* — final shot: the ceiling crack, then the camera tilting to the window, bare branches with the first buds, birdsong, hold through the held chord and the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "give me Sunday mornings", the
first balcony cut, the instrumental, the window push-in, "I've known for
weeks", "give me Monday mornings too", and the final tilt to the window. At
100 BPM a bar is 2.4 s.

**The Sunday-count challenge.** Post the vertical cut of chorus 1 (shots
17–22) with *"messy hair and coffee rings"* on screen, and invite couples to
post their own "Sunday number ___" with one small thing in frame: the mug,
the cat, the plant, the flannel. The season-change window (shot 44) is the
second shareable frame, and *"I know, I've known for weeks"* (shot 53) is
the quote cut.

## 6. Quality-control checklist

- Three looks in the right sections: flannel and loose hair for Sundays one and six, camisole and bun from verse 2 to the final chorus, flannel again for the bridge and outro
- The window season is correct in every shot it appears in: buds, green, frost, summer, buds
- Objects accumulate and never disappear: one coffee ring in verse 1, several by chorus 2; the plant from shot 29 on; the cat from shot 27 on
- Kai is recognisable in every shot: cropped hair, short beard, grey t-shirt
- The weekday inserts are the only cool-graded frames; all UI composited, the newspaper unreadable
- No distorted hands on the mug close-ups and the pancake shot
- The last shot is locked-off, the tilt ends on the window, and it holds until the audio fades
