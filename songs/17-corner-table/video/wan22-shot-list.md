# Wan 2.2 Shot List — "Corner Table"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
110 BPM a bar is 2.18 s, so most shots run 3–5 s and the choruses cut every
two bars.

## 1. Visual style

One café, one corner table, one window, four seasons. The **table never
moves and the camera keeps returning to the same three set-ups**: the
locked-off wide from the counter, the push-in through the window from the
street, and the close two-shot across the table. The seasons are told
entirely by the window and by wardrobe. Warm interior, weather outside. The
**barista is the silent witness**: she appears in every section, never
speaks, never gets a close-up on her face until the post-chorus. The
**paperback** is a prop that is open in autumn, closed in winter, and gone
by spring.

| Section | Grade | Camera |
|---|---|---|
| Intro / outro | Overcast soft daylight, warm lamps | Locked-off wide from the counter |
| Verse 1 (September) | Grey rain outside, warm inside | Over-the-shoulder, slow two-shot |
| Pre-choruses | Autumn gold, then flat winter grey | Locked-off wide, jump cuts on the beat |
| Choruses | The full year dissolving behind the glass | Slow push-in from the street |
| Verse 2 (Nov → Jan) | Cold blue outside, deep warm inside, then flat white | Handheld close-ups, then static |
| Instrumental | Cold window light, one warm counter lamp | Slow, quiet, macro |
| Bridge (March) | First low gold sun, motes in the air | Static, close, held |
| Final chorus / post-chorus | Spring sun, the warmest frames | Push-in, then close-ups |

## 2. Character bible — paste into every prompt

**Mahima** (autumn, September to November)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose over one shoulder, light natural makeup, wearing a rust-coloured knit cardigan over a white t-shirt and jeans, a paperback book in her hands, shy watchful expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (winter, December to the instrumental)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tucked under a cream wool beanie, light natural makeup, wearing a long camel coat over a dark jumper, hands around a paper cup, quiet patient expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (spring, bridge to outro)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and pushed back, light natural makeup, wearing a pale blue linen shirt with the sleeves rolled, no book, open easy expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the man two tables over)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a dark green waxed jacket with rain on the shoulders over a grey sweater, a laptop bag, warm unhurried expression, realistic cinematic photography, consistent identity

**The barista** — the silent witness. Seen from behind, from the side, or from the counter's point of view with her hands in frame; her face is soft-focus or cropped until shot 60.
> a woman in her thirties behind a café counter, dark apron, hair tied up, steady hands pouring milk into a cup, calm knowing expression

Objects: the **corner table** with the **wobbling chair**, the **paperback**
(cover always turned away, never legible), the **latte with a leaf in the
foam**, the **shop bell** above the door, the **sugar bowl**, the **paper
napkin**. The window is the calendar.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, book covers, the wall clock, the napkin and any signage are
composited in the edit.** Generate the book with a blank cover, the clock as
a blank face, the napkin as plain paper, and overlay in post — the model
cannot render legible text, and the ten o'clock clock is a storytelling
beat.

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

Most shots 3–5 s. For this song there is no dance and no running; the
OpenPose reference is only needed for Kai sitting down into the chair (a
motion the model likes to invent). Build one plate of the café in each of
the four seasons and reuse it: the geography must not drift.

## 4. Scene per lyric line

### Intro — the table, the chair, the witness

1. *"Same chair, same window, same wobble in the leg"* — locked-off wide from behind the counter: the corner table by the window empty in soft overcast light, then Mahima (autumn look) sitting down into frame; cut to a macro of the chair leg rocking on the tile.
2. *"Same latte going cold beside a book I never read"* — top-down close-up of a latte with a leaf in the foam set down beside a closed paperback with a blank cover, her hand resting on the book without opening it.
3. *"The girl behind the counter draws a leaf into the foam"* — the barista's hands pouring milk into a cup, the leaf forming, her face out of frame above, warm counter lamp.
4. *"She's watched this whole thing happen and she's never said a word"* — from behind the barista, her glance up toward the corner table and back down to the machine, Mahima small in the background, static.

### Verse 1 — September, the paperback

5. *"September, I was hiding in a paperback"* — over Mahima's shoulder onto the open book, her thumb on the page, rain streaking the window beside her, grey light.
6. *"Same page for an hour, eyes on the door instead"* — her eyes lifting from the page to the door as the bell rings, then dropping again, close-up, three times on the beat.
7. *"You came in shaking rain out of your jacket"* — the door opening, Kai stepping in and shaking rain from a green waxed jacket, the bell swinging above him, medium from inside.
8. *"Sat two tables over and I lost my place"* — Kai taking a table by the wall socket and opening a laptop; Mahima looking back at her book and blinking, a private smile, two-shot with the empty table between them.
9. *"I pretended I was reading, you pretended you were working"* — slow two-shot: she glances up as he looks down; he glances up as she looks back at the page, the timing just missing each time, static.
10. *"Both of us just stealing looks across the room"* — a close-up on Kai's eyes over the laptop screen, then a matched close-up on Mahima's eyes over the top of the book.
11. *"Then you asked me what the book was, and I couldn't tell you"* — Kai standing at her table with an empty cup on his way to the counter, saying something, Mahima looking up, then turning the book over to check the cover, medium.
12. *"Because I'd never made it past the first line"* — her laughing with her hand over her face, him grinning, over-the-shoulder from behind him; the barista visible in the far background, turning to the machine.

### Pre-chorus 1 — every week at ten

13. *"And every week I told myself, this isn't anything"* — the locked-off wide: Mahima sitting down in a different top, the wall clock (blank, composited to ten) above the door, jump cut, sitting down again in another top.
14. *"Just coffee and a window and a habit I can't kick"* — the same wide, the door opening on Kai; jump cut; the door opening on Kai in a different sweater; the light outside a little more gold each time.
15. *"But I kept coming back at ten, and you kept coming in at ten"* — four fast jump cuts on the beat: her sitting, him entering, her sitting, him entering, the clock every time.
16. *"And the girl behind the counter kept on smiling like she knew"* — the barista from the side at the counter, watching the door open, a small smile she hides by turning to the steamer, her face soft-focus.

### Chorus 1 — the year in a window

17. *"Same corner table, different me, and you still sat down"* — from the street: a slow push-in on the café window, Mahima at the corner table inside, rain running down the glass, the reflection of the street on it.
18. *"Watched a whole year through that window, and you're still around"* — the push-in continues and the rain dissolves to falling leaves blowing past the glass, then to string lights, Mahima's wardrobe changing with each dissolve.
19. *"I came in pretending, now I'm not pretending anymore"* — inside, from her point of view across the table: the chair opposite empty, then Kai pulling it out and sitting down, autumn light.
20. *"Same corner table, and I'm not who I was before"* — the same point-of-view shot, Kai sitting down in winter light in a coat, then in spring light in shirt sleeves, three dissolves.
21. *"Same corner table, different me, and you still sat down"* — the push-in from the street landing on the glass, the two of them at the table inside, the leaf-in-foam latte between them, hold.

### Verse 2 — November, December, January

22. *"November, you got to the counter before I did"* — Mahima coming through the door in the camel coat, the bell ringing, and Kai already at the counter with his back to her, ordering, medium.
23. *"Said, oat milk, extra hot, and turned around and grinned"* — Kai turning from the counter with two cups and a grin; the barista's hands sliding the second cup across with a leaf already in the foam, close-up.
24. *"I didn't know you'd been paying attention"* — Mahima stopped in the doorway with her scarf half off, the bell still swinging above her, close-up, cold blue behind her.
25. *"I'd been so careful to look like I wasn't"* — her taking the cup from him and trying to keep a straight face, failing, steam catching the window light, two-shot.
26. *"By the time the lights went up along the street outside"* — from the street at dusk: string lights being hoisted across the road by a figure on a ladder, the café window glowing gold behind them, wide.
27. *"We were sharing one table and pretending it was small"* — inside: two cups on the corner table, elbows almost touching, both laughing at something on the laptop, the coloured lights reflected in the window, close two-shot.
28. *"Then January, the door kept opening and it was never you"* — hard cut: snow on the window, the same table, one cup, Mahima (winter look) in the beanie looking to the door as the bell rings and a stranger comes in, then again, then again, static.
29. *"And she wiped your side of the table twice and didn't say a thing"* — the barista's hand with a cloth wiping the empty side of the table, a beat, wiping it again, then walking out of frame; Mahima's hands around the cup at the edge of the shot, top-down.

### Pre-chorus 2 — the door stays shut

30. *"And every week I told myself, it wasn't anything"* — the locked-off wide: Mahima in the winter look sitting down, the clock at ten, the door shut, jump cut, sitting down again, the door shut.
31. *"Just coffee and a window and a chair across from mine"* — the empty chair opposite her, the window white with snow behind it, static, held a beat too long.
32. *"But I kept coming back at ten, and the door stayed shut at ten"* — four jump cuts on the beat: her sitting, the shut door, her sitting, the shut door, the clock reading ten each time.
33. *"And the foam went flat, and I let it, and I stayed"* — macro of the latte, the leaf in the foam slowly dissolving into flat milk, time-lapse feel; then a slow pull back to Mahima still there with her coat on.

### Chorus 2 — the year stops at winter

34. *"Same corner table, different me, and you still sat down"* — the push-in from the street begins again, rain on the glass, Mahima inside in autumn.
35. *"Watched a whole year through that window, and you're still around"* — reuse shot 18, but the dissolve slows as it reaches the string lights.
36. *"I came in pretending, now I'm not pretending anymore"* — inside, her point of view across the table: Kai sitting down in autumn light, then in December light, then the chair stays empty in January light.
37. *"Same corner table, and I'm not who I was before"* — the push-in from the street holding on the winter window, snow, Mahima alone at the table, the reflection of the empty street on the glass.
38. *"Same corner table, different me, and you still sat down"* — inside: the empty chair opposite her, her hand resting on the table where his cup would be, close-up, flat winter light.

### Instrumental — winter in the café, no lyrics

39. The espresso machine steaming in slow motion, the counter lamp behind it, macro.
40. Mahima at the corner table actually reading now, turning a page of the paperback, snow light on her face, close-up.
41. The barista drawing a leaf in the foam of a cup for another customer, hands only, then setting it on the counter.
42. Snow falling past the window from inside, the string lights from December gone, the street empty, static.
43. The bell above the door, still, in close-up, then ringing once on the held chord as the door begins to open — the cut into the bridge.

### Bridge — March, the door

44. *"March, and the window's open, there's blossom on the street"* — the café window propped open, blossom blowing along the pavement outside, Mahima (spring look) at the corner table with a cup and nothing else, low gold sun, static.
45. *"I stopped bringing the book, I stopped saving you the seat"* — close-up of the table: one cup, no book, and her bag set on the chair opposite, sun across the wood.
46. *"Then the bell above the door, and the rain-shaken jacket"* — the bell ringing; she does not look up this time; a shadow crosses the table; Kai's green waxed jacket with rain on the shoulders entering the edge of the frame beside her chair.
47. *"And you say, it's a long story, is anybody sitting here"* — Kai standing at the chair with his hand on the back of it, tired, honest, a little wet, medium from her side of the table; her looking up slowly.
48. *"You say, my dad got sick, I went home, I didn't have your number"* — close-up on Kai as he explains, his eyes down then up, the sun on half his face.
49. *"And I laugh, because a year of ten o'clocks and I never gave it to you"* — Mahima's laugh breaking out, her hand over her mouth, her eyes wet, close-up, motes in the air.
50. *"I could say a hundred things about the winter"* — a beat of silence between them, a two-shot across the table, the bag still on the chair, held.
51. *"But I push the sugar over and I say, sit down"* — tilt down to her hand pushing the sugar bowl across the table and lifting the bag off the chair; in the background the barista stopped mid-motion at the counter with a cup halfway to a saucer.

### Final chorus — the strings, the napkin

52. *"Same corner table, different me, and you still sat down"* — Kai pulling the chair out and sitting down opposite her, from her point of view, spring sun on the glass behind him.
53. *"Watched a whole year through that window, and you're still around"* — the push-in from the street one last time, the dissolves running fast, rain, leaves, lights, snow, and settling on blossom and the two of them at the table.
54. *"I came in pretending, now I'm not pretending anymore"* — close two-shot across the table, both talking at once, both laughing, warm.
55. *"Here's my number on a napkin, should have done it long before"* — close-up of her writing on a paper napkin (blank, composited) and sliding it across; Kai pocketing it without looking, grinning.
56. *"Same corner table, different me, and you still sat down"* — the locked-off wide from the counter: two people at the corner table for the first time in this set-up, the door open, blossom drifting in.
57. *"Same corner table, different me, and you still sat down"* — the push-in from the street lands on the glass and holds on the two of them, the sun flaring on the window, the warmest frame in the video.

### Post-chorus — two leaves

58. *"The girl behind the counter draws two leaves into the foam"* — close-up of the barista's hands pouring two cups, a leaf in each, warm counter light.
59. *"Sets them down between us, doesn't say a word, and goes"* — the barista walking the two cups to the table, setting them down between them, and turning away, from behind her.
60. *"She's watched the whole thing happen from the first page to the last"* — the barista's face for the first and only time, in a close-up as she turns back toward the counter, a small knowing smile, soft light.
61. *"She never had to read it, she was always there"* — top-down: the two cups side by side with their leaves, steam rising, the paperback closed and pushed to the edge of the table.

### Outro — the first frame, with two people in it

62. *"Same chair, same window, same wobble in the leg"* — macro of the chair leg rocking on the tile, then Kai's foot coming down to steady it, warm spring light.
63. *"Two coffees going warm beside a book I'll never read"* — top-down on the two cups and the closed book, her hand and his hand on the table, not quite touching, then touching.
64. *"It was never the table, it was never this street"* — from the street through the open window, the two of them talking, blossom passing in the foreground, the street bright, medium.
65. *"It's who keeps showing up, it's who keeps showing up"* — final shot: the locked-off wide from the counter, identical framing to shot 1, two people at the corner table, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "you still sat down", the first
"ten" jump-cut run, the January hard cut (shot 28), the instrumental, the
bell (shot 43), "sit down" (shot 51), the napkin (shot 55), and the final
frame. At 110 BPM a bar is 2.18 s; the jump-cut runs in the pre-choruses
land one cut per bar, the choruses cut every two bars.

**Same-seat challenge.** The pre-chorus jump-cut run (shots 13–15) is the
template: a locked-off frame, the same seat, the same time, weeks apart.
Post the vertical cut with *"same corner table, different me"* on screen and
invite people to film their own ritual seat: a café, a library desk, a bus
stop, a gym bench. The second shareable frame is the year-in-a-window
push-in (shots 17–21), which works as a nine-second loop with no lyric on
screen at all.

## 6. Quality-control checklist

- Three looks in the right seasons: rust cardigan and the book until shot 21, camel coat and beanie from shot 22 to the instrumental, blue linen shirt and no book from shot 44 on
- The café geography never drifts: door with bell on the left, counter at the back, corner table by the window on the right, in every wide
- The barista never has a visible face before shot 60, and speaks in no shot
- Kai is only ever seen sitting down into the chair from Mahima's point of view or across the table; use the OpenPose reference for every sit-down
- All book covers, the clock face, the napkin and any signage are blank in generation and composited in the edit
- The window is the calendar: rain in September, leaves in October, string lights in December, snow in January, blossom in March, never mixed within one shot
- The paperback is open in autumn, closed in winter, absent in spring
- The last shot matches the first shot's framing exactly and holds until the audio fades
