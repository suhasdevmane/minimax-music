# Wan 2.2 Shot List — "Cheap Champagne"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
114 BPM a bar is 2.1 s, so most shots are 3–5 s and the choruses cut on the
bar.

## 1. Visual style

One fire escape, one evening, one bottle. The video runs from blue hour to
very late and never leaves a three-floor stretch of a single building except
for four flashback inserts and one two-second flash forward. **The lighting
is entirely practical**: street lamps from below, one warm window behind
them, and by the last chorus the whole building face lit window by window.
Handheld and close on the steps; wide and locked-off from across the street.
The **same framing of the fire escape recurs five times** — one year ago,
winter, spring, summer, tonight — and that repeated frame is the spine of the
video.

| Section | Grade | Camera |
|---|---|---|
| Intro | Store fluorescents, then blue hour | Macro, then a window climb |
| Verse 1 | Cool blue present, warm flashback inserts | Handheld on the steps, two-second cutaways |
| Pre-chorus | Blue hour, warm window behind | Close on hands, one held beat |
| Choruses | Street lamp gold against deep blue | Handheld close, wide from across the street |
| Post-chorus | Hard, close, warm | Two fast macro cuts |
| Verse 2 | Grey-blue and flatter for the past | The repeated fire-escape framing, four-shot dissolve |
| Instrumental | Deep blue and window gold | Lateral drift, overhead, a rising crane |
| Bridge | Cold and even for the flash forward | Static, then hard back to warm |
| Final chorus | Brightest of the video, all windows | Wide building face, low angle |
| Outro | Street lamps and one window | Slow pull back, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the whole video)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose over one shoulder, minimal makeup, wearing a thin white t-shirt under an open oversized denim shirt and jeans, bare feet on metal grating, warm easy expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge flash forward, seen from behind and in profile only)
> Same female protagonist Mahima, young woman in her late twenties, hair pinned up, wearing a well-cut camel coat, holding a matching wine glass, seen from behind or in profile, expression not clearly visible, realistic cinematic photography, consistent identity

There is **no romantic male lead in this video** and no Kai. This is three
friends and a building.

**The friend with the job** — the one who reads the email out.
> a young man in his early twenties, tall and thin, round glasses, close-cropped hair, wearing a faded work polo and shorts, delighted disbelieving expression

**The friend who made it through** — the emotional centre of verse one.
> a young woman in her early twenties, short bleached hair growing out dark at the roots, a small tattoo on her forearm, wearing an oversized cardigan over a t-shirt, tired and genuinely smiling

**The neighbour** — appears only in the final chorus, two floors up, raising a
mug back. Face visible, no dialogue.

Objects that must stay consistent: the **bottle with the gold foil cap**, the
three **chipped enamel mugs**, the **glass jar with masking tape** on the
kitchen shelf, the **rusted fire escape rail**, the **sash window** with a
warm lamp behind it.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the banking app, the email, the masking-tape label on the jar,
the envelopes and any store signage are composited in the edit.** Generate the
jar with a blank strip of tape and the phone as a lit blank rectangle. The
label on that jar is a plot point, so it has to be legible, which means it has
to be added in post.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock all three friends with IP-Adapter or a character LoRA each; they are on
screen together for most of the video and drift between them is the main
risk. Build the fire-escape plate once and reuse it for all five seasonal
versions of the repeated framing — same lens, same height, same distance —
then change the grade, the props and the number of people. OpenPose for the
window climb, the dancing on the steps and the overhead lying-back shot;
Depth for the wides from across the street. 16:9 first; 9:16 recomposition for
the mug-clink toast and the cork, which are the vertical clips. Animate in
short bursts: foam over a hand, a mug raised, a bottle rolling an inch.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; toast shots 1–2 s.

## 4. Scene per lyric line

### Intro — the bottle and the window

1. *"Seven dollars at the corner store for something with a foil top"* — a hand taking a bottle with a gold foil cap off a shelf near a store door, fluorescent light, macro.
2. *"You went out the window first and held the bottle while I climbed"* — a sash window pushed up from inside, the friend in glasses climbing out backwards onto the fire escape and reaching back in for the bottle.
3. *"And the whole city just sat there like it was waiting for us"* — the reverse: from the fire escape looking out, the city at blue hour, the last orange on the buildings opposite, wide and still.

### Verse 1 — three small wins

4. *"Rent went through on Thursday with two days left to spare"* — a two-second flashback insert: a banking screen going from red to black (composited), a hand over a mouth in a kitchen, warm light.
5. *"First time in a year that the number didn't scare"* — back to the present: Mahima settling onto a step with her back against the rail, exhaling, close-up.
6. *"You got the email that you'd given up on getting"* — flashback: the friend in glasses standing up in a café reading a phone out loud to nobody, other customers looking over.
7. *"Read it out to us twice, then you read it out again"* — present: him reading it off his phone again on the fire escape, the other two shouting him down and making him do it anyway.
8. *"And the third of us walked in tonight looking like herself"* — a door opening into the apartment, the third friend in the doorway smiling properly, the other two going quiet for half a second before they move.
9. *"Which is a sentence I could not have said in March"* — her face on the fire escape now, lit from the window, tired and here, close-up, held longer than the others.
10. *"So I took the twenty from the jar that says emergencies"* — a glass jar on a kitchen shelf with a masking-tape label (composited), a hand pulling a note out of it, macro.
11. *"And I have decided this is one"* — Mahima at the window with the empty jar in one hand and the note in the other, shrugging at someone off frame, medium.

### Pre-chorus 1 — the count

12. *"Out through the window, over the sill"* — bare feet swinging over a windowsill onto metal grating, low angle.
13. *"Two cups, no glasses, hold still"* — two chipped enamel mugs handed out through the window one at a time, close on the hands.
14. *"The bottle's warm, the night is not"* — a thumb working the foil cap off, the wire cage twisting, extreme close-up.
15. *"Count to three and let it pop"* — all three faces waiting, held for one silent beat, then the flinch, wide on the steps.

### Chorus 1 — the toast

16. *"Cheap champagne on the fire escape, tonight we're rich"* — the cork going, foam over a hand and down the rail, all three laughing, handheld close.
17. *"Seven dollars at the corner store and not one thing to fix"* — pouring into the two mugs, badly, most of it foam, macro.
18. *"Three flights over a city that we're never gonna own"* — a wide from across the street: three small figures on one lit fire escape against a whole dark building.
19. *"But you can see the whole of it from here, so it's on loan"* — her point of view along the street: the whole avenue in one frame, lights all the way down.
20. *"Cheap champagne on the fire escape, tonight we're rich"* — back close on the steps, all three toasting, arms crossing over each other.
21. *"To the rent, to the job, to the one who made it through"* — three quick cuts, one per clause: the banking screen, the phone, and the third friend's face.
22. *"Warm and flat and perfect and I wouldn't switch"* — all three drinking at once and pulling the same face at the taste, then laughing at each other.
23. *"Cheap champagne on the fire escape, tonight we're rich"* — a low angle from the step below, the three of them against the sky, mugs up.

### Post-chorus 1 — the small ones

24. *"To the small ones, to the small ones"* — three enamel mugs knocked together, macro, the dull sound of enamel rather than glass.
25. *"Here's to every small one that we won"* — a wide of the three of them on the steps, arms up, the warm window behind them.

### Verse 2 — a year ago on the same steps

26. *"This time last September we were out here with nothing"* — the identical fire-escape framing, graded grey-blue: two people instead of three, no warm window, a plastic bottle between them.
27. *"Passing round the cheapest thing and calling it a night"* — the plastic bottle passing from one hand to another, macro, flat light.
28. *"You were pulling doubles and I had a stack of letters"* — a name badge and a work polo over the back of a chair; a stack of unopened envelopes on a kitchen table with dust on the top one.
29. *"That I hadn't opened since the middle of July"* — a hand moving the envelopes to one side rather than opening them, macro, held.
30. *"Nobody announced it, nothing turned around at once"* — the repeated framing in winter: snow on the rail, the window shut, nobody out there.
31. *"It just got a little lighter every couple of months"* — the repeated framing dissolving through spring and summer: the window opening, a fan appearing in it, a plant on the sill.
32. *"Same three people on the same three metal steps"* — the repeated framing, tonight, with all three on it, the warmest version of the shot.
33. *"Same warm bottle and it tastes like something else"* — Mahima looking into her mug, then up, close-up, present tense again.

### Pre-chorus 2 — the second bottle

34. *"Out through the window, over the sill"* — a second bottle produced from inside a coat, held up, the other two reacting.
35. *"Two cups, then a third, hold still"* — a third mug appearing through the window, all three lined up on a step.
36. *"The bottle's warm, the night is not"* — the second foil cap coming off, faster and more confident than the first, macro.
37. *"Count to three and let it pop"* — three sets of fingers counting down together, then the cork, wide.

### Chorus 2 — dancing on metal

38. *"Cheap champagne on the fire escape, tonight we're rich"* — three people dancing in a space far too small for it, holding the rail, handheld and chaotic.
39. *"Seven dollars at the corner store and not one thing to fix"* — feet on metal grating shot from directly below, the street three floors down through the mesh.
40. *"Three flights over a city that we're never gonna own"* — the wide from across the street again, now with all three moving.
41. *"But you can see the whole of it from here, so it's on loan"* — a slow lateral drift across the lit windows of the building opposite, other lives visible.
42. *"Cheap champagne on the fire escape, tonight we're rich"* — the three of them leaning on the rail shoulder to shoulder, shouting the line at the street.
43. *"To the rent, to the job, to the one who made it through"* — the third friend laughing so hard she has to sit down on a step, the other two above her.
44. *"Warm and flat and perfect and I wouldn't switch"* — a mug refilled and overflowing over a hand, macro, nobody caring.
45. *"Cheap champagne on the fire escape, tonight we're rich"* — the whole fire escape from below with all three on it, warm window above, street lamp flare.

### Instrumental — the city at their level

46. A pigeon landing on the rail, unbothered, and staying, close-up.
47. The empty first bottle standing upright on a step, the city out of focus behind it.
48. The three of them lying back on the steps looking straight up, shot from directly above, arms and legs at angles.
49. A slow lateral drift across the building faces opposite, window after lit window.
50. A rising crane move up the front of the building through the build, ending on the sky above the roofline.

### Bridge — the flash forward

51. *"One day one of us will have the kind of job"* — two seconds of a bright expensive room: matching glasses on a tray, someone pouring, cold even light.
52. *"Where the glasses match and somebody else pours"* — a woman in a good coat holding one of the matched glasses, seen from behind, not looking at the room.
53. *"I'll be standing in a room that cost a fortune"* — the same room, wide, beautiful and completely quiet, nobody talking to her.
54. *"Thinking of a metal step and a seven dollar cork"* — hard cut back to the fire escape: her looking into the chipped mug in her hand, close-up, warm and uneven light.
55. *"You don't get this twice, so raise it while it's cheap"* — her lifting the mug slightly without a word, just to herself, medium.
56. *"Drink it while it still means everything to me"* — the other two noticing and lifting theirs back, three-shot, no dialogue.

### Final chorus — the building answers

57. *"Cheap champagne on the fire escape, tonight we're rich"* — a wide of the whole building face with windows lighting up one by one.
58. *"Every window in the building lit and not one thing to fix"* — a neighbour two floors up leaning out and raising a mug back at them without saying anything.
59. *"Three flights over a city that we're never gonna own"* — the widest frame of the video: the lit building, the street, the sky above it.
60. *"But you can see the whole of it from here, so it's on loan"* — the three of them at the rail looking out, from behind, the city in front of them.
61. *"Cheap champagne on the fire escape, tonight we're rich"* — close, handheld, all three singing at each other rather than at the camera.
62. *"To the year, to the three of us, to the ones who made it through"* — three faces in a row on the steps, one shot, each one lit slightly differently.
63. *"Warm and flat and perfect and I wouldn't switch"* — mugs knocked together one more time, macro, foam on the rail.
64. *"Cheap champagne on the fire escape, tonight we're rich"* — from below: three silhouettes against a lit window, mugs raised, held.

### Post-chorus 2 — shouted

65. *"To the small ones, to the small ones"* — mugs up, shouted at the street, from directly below, backlit.
66. *"Here's to every small one that we won"* — a wide of the lit building with three small figures on it and one neighbour still at a window.

### Outro — very late

67. *"Bottle's empty, city's loud, and nobody wants to go in"* — the empty bottle on its side on a step, rolling an inch and stopping, macro.
68. *"When they ask me for the best night I have ever had"* — the three of them sat in a row, shoulders touching, saying nothing, from the side.
69. *"I'll say a metal step, three cups, and cheap champagne"* — final shot: a slow pull back from across the street until the fire escape is one small lit detail on a huge dark building, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the cork, each *"tonight we're rich"*, the two toasts, the first
grey-blue frame of the past, the four-shot seasonal dissolve, the flash
forward, the first window lighting up in the final chorus, and the bottle
rolling. At 114 BPM a bar is 2.1 s; the choruses cut on the bar and the
toasts on the half-bar.

**The toast challenge.** Shots 24–25 are the shareable unit: name the small
win nobody threw you a party for, raise whatever you happen to be drinking
out of, cut on *"to the small ones."* Second clip: the four-shot seasonal
dissolve, shots 26 and 30–32, empty fire escape to full — it tells the whole
song in six seconds. Third: shot 16, the cork and the foam, vertical.

**Caption:** *"You don't get this twice, so raise it while it's cheap."*

## 6. Quality-control checklist

- The repeated fire-escape framing is identical in all five versions: same lens, same height, same distance from the building. Only the grade, the props and the number of people change.
- The evening only moves forward: blue hour, dark with street lamps, full window-lit, very late. The past-tense frames are the only grey ones and they are clearly colder.
- All three friends are recognisably the same people in every shot; the bleached-hair friend must read the same in the cold past frames as in the warm present ones.
- The bottle with the gold foil cap, the three chipped enamel mugs, the taped jar and the rusted rail are identical wherever they recur.
- The flash forward never shows her face clearly and is the only cold, even, expensive light in the video.
- No readable text anywhere: the banking screen, the email, the jar label and the envelopes are all composited.
- Nobody is ever in danger on the fire escape; the dancing is comic and hemmed in by the rail, never reckless at the edge.
- No distorted hands in the macro shots, especially the cork, the pour and the mug clinks.
- The last shot is locked-off from across the street and holds until the audio fades.
