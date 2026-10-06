# Wan 2.2 Shot List — "Better Without the Ending"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Sixty-six lyric shots plus five for the instrumental, numbered
continuously. Timestamps come from the rendered WAV; cut on the sung line. At
102 BPM a bar is 2.35 s, so most shots run 3–5 s and the choruses cut on the
bar.

## 1. Visual style

Light is the plot. The video begins in a dim flat lit by one desk lamp and
ends outdoors at midday, and the brightness only ever increases — the single
biggest jump happens on the downbeat of the first chorus, when she pushes the
desk to the window and opens the curtains. The memories are shot with exactly
the same honesty as the present: warm daylight, no dreamy overexposure, no
soft filter. This is deliberate. The song refuses to make the past a fantasy
or the man a villain, and the grade has to refuse it too.

| Section | Grade | Camera |
|---|---|---|
| Intro | One desk lamp, everything else black | Static macro |
| Verse 1 / the good years | Warm honest daylight, no gauze | Handheld, close |
| Pre-choruses | Lamp plus first window light | Macro, overhead desk |
| Choruses | Full daylight, curtains open | Wide, tracking, exits of frame |
| Verse 2 | Bright, plain, flowers loudest in frame | Handheld, loose |
| Instrumental | A whole day crossing the floor | Locked-off, time-passing |
| Bridge | Low warm, one shaft of late sun | Static, to camera |
| Final chorus | Brightest of the video, exterior | Tracking, wide, push |
| Post-chorus | Midday, hard rhythmic cuts | Static, on the beat |
| Outro | Even, calm, full of light | Slow, held |

## 2. Character bible — paste into every prompt

**Mahima** (the flat, the whole first half)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair twisted up and held with a pencil, no makeup, wearing a soft oatmeal jumper with the sleeves pushed up and dark jeans, focused unhurried expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the memories)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, light natural makeup, wearing a striped linen shirt and blue jeans, easy laughing expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (final chorus and outro, out in the world)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and loose, warm natural makeup, wearing a cream trench coat over the oatmeal jumper, open confident expression, realistic cinematic photography, consistent identity

**The ex** — faceless in every frame, and never shot unkindly. He appears
only in the memory sequences as hands over a market stall, a forearm reaching
for a coffee pot, a shoulder at a family table.
> a young man in his mid twenties, face out of frame or cropped at the jaw, dark curly hair, olive shirt

Objects that repeat: the **typewriter**, the **red pen**, the **stack of
pages** and the **twelve torn ones**, the **desk lamp**, the **second chair**,
the **plant**, the **loud yellow flowers**, the **drawer**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every page, every line of handwriting, the note on the door and the phone
message are composited in the edit.** Generate blank paper and a blank lit
phone screen; the model cannot render legible writing, and the single red
line through one paragraph in shot 17 has to read exactly.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless and warm. Keyframes first; OpenPose for
the desk push, the walk out of frame and the street walk in the final chorus;
Depth for the flat interiors, which are shot from consistent angles so the
light change reads. Shoot the curtain-opening as a brightness ramp over a
lit-plate still rather than asking the model to animate a lighting change.
16:9 first; 9:16 for the desk macros and the curtain reveal, which are the
vertical hero cuts. Animate conservatively: a pen dying on paper, a page
being fed into a carriage, a curtain lifting, flowers moving in a doorway.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the dead pen

1. *"Three whole years and a bad last page,"* — a desk in a dim flat, one lamp, a typewriter, a tall stack of pages, wide static, everything beyond the lamp black.
2. *"A pen that ran out in the middle of a line."* — macro: a pen dying mid-word, ink going grey and then nothing, the nib pressing into paper.
3. *"I'm not tearing up the whole thing,"* — her hand flat on the whole stack, protecting it, not gripping it, close-up.
4. *"I'm just taking back an end that isn't mine."* — she lifts the top page off, deliberately, and sets it face-down beside her. Nothing violent.

### Verse 1 — the good years, told honestly

5. *"It was good, I won't pretend it wasn't good,"* — memory: a Sunday market in real daylight, both of them among stalls, his face out of frame, handheld.
6. *"Sunday markets, your handwriting on my door."* — memory: a paper bag splitting and fruit going everywhere, both of them laughing at it, then a note in handwriting stuck to a front door (composited).
7. *"You learned how I take my coffee, I learned your dad's jokes,"* — memory: a kitchen, his forearm pouring a coffee and setting it down correctly without asking, her not even looking up.
8. *"We were a decent book, and I'd read it once more."* — memory: a family table mid-laugh, her among them, him cropped at the shoulder, warm and ordinary.
9. *"Then somewhere in the middle you got tired of the plot,"* — memory, cooler: the same kitchen with two people in it not talking, a phone face-up between them.
10. *"Started skipping to the back to see how it would end."* — memory: a hand at the market moving past her without waiting, the crowd closing between them, handheld.
11. *"And a story knows the minute a reader stops believing,"* — present: her at the desk, still, listening to nothing, static.
12. *"It goes quiet, and it doesn't pretend."* — present: a wide of the dim flat with the second chair empty at the table, held two beats too long.

### Pre-chorus 1 — the red pen

13. *"So I sat down with a red pen and two years,"* — overhead of the desk: her hands, the stack, a red pen uncapped, the lamp and the first daylight from the window behind her.
14. *"And I crossed out the part where I got small."* — macro: one red line drawn through exactly one paragraph on a full page. The rest of the page is untouched.
15. *"Kept the markets, kept the jokes, kept the good bits,"* — pages being sorted into two piles: a large one and a very small one, overhead.
16. *"Kept the story, let go of the fall."* — her hand resting on the large pile, then pushing the small one to the far edge of the desk.

### Chorus 1 — the curtains

17. *"The story was good, I'm just better without the ending,"* — she stands, takes the desk by its edge and pushes it across the floor toward the window, tracking with the desk.
18. *"Better without those last twelve pages of pretending."* — she pulls the curtains back and daylight floods a room that has been dim for the entire video. The biggest lighting change in the piece, on the downbeat.
19. *"Keep the summer, keep the songs, keep how it began,"* — the pages on the desk lifting slightly in the air from the opened window, macro, sun across them.
20. *"I'm taking back the pen and writing where I stand."* — her picking up a new pen from a jar, uncapping it, standing at the desk rather than sitting, low angle.
21. *"It didn't need a villain, it didn't need a war,"* — a wide of the room, calm, no mess, no broken anything, sunlight across the floorboards.
22. *"It just needed to be over, and it's over, I'm sure."* — her at the window with the light on her face, breathing out, medium.
23. *"The story was good, I'm just better without the ending."* — she walks clean out of the edge of frame, leaving the empty bright room and the open window in shot, held.

### Verse 2 — the ordinary week

24. *"I moved the desk to the window on a Thursday,"* — the desk in its new place, seen from the doorway, the whole room reorganised around it, static.
25. *"Put a plant where the second chair had sat."* — a plant carried in and set down in the exact spot; then the second chair out on a landing with a note taped to it (composited).
26. *"You texted, could we talk about it properly,"* — a phone lighting on the desk beside the flowers (message composited), her looking at it without picking it up immediately.
27. *"And I sent a kind no, and I left it at that."* — her typing a short reply and sending it in one movement, then turning the phone face-down and going back to work.
28. *"I went back to the market on my own on Sunday,"* — the same market as shot 5, in the same light, with only her in it, handheld.
29. *"Bought the loud yellow flowers you always said were wrong."* — enormous yellow flowers being handed over and carried away, the loudest colour in the video so far.
30. *"Nobody died. I came home. I made dinner."* — three flat static shots on the line: a front door opening, a pan on a hob, a plate being set down.
31. *"And I ate the whole thing with the radio on."* — her eating alone at the table with a radio on the counter, entirely comfortable, wide, held.

### Pre-chorus 2 — the second edit

32. *"So I sat down with a red pen and a good lamp,"* — the desk at the window, lamp on anyway, late afternoon, overhead.
33. *"And I cut every line where I asked to be allowed."* — macro: a run of lines struck through, all of them beginning the same way (composited), the pen not hesitating.
34. *"Kept the market, kept the music, kept the mornings,"* — three pages held up to the window light one after another, kept.
35. *"And I let the ending go, and I said it out loud."* — the twelve torn pages going into a bin, unceremoniously, and her saying one sentence to the empty room.

### Chorus 2 — a place someone writes in

36. *"The story was good, I'm just better without the ending,"* — pages pinned in order along a whole wall, her stepping back to look at them, wide.
37. *"Better without those last twelve pages of pretending."* — a new stack starting beside the typewriter, growing, macro.
38. *"Keep the summer, keep the songs, keep how it began,"* — her feet up on the desk, pen in her mouth, thinking, medium.
39. *"I'm taking back the pen and writing where I stand."* — hands feeding a fresh page into the typewriter carriage, macro, on the beat.
40. *"It didn't need a villain, it didn't need a war,"* — the flat in full daylight with no lamp on for the first time, wide.
41. *"It just needed to be over, and it's over, I'm sure."* — her pulling her coat on in the hall, unhurried.
42. *"The story was good, I'm just better without the ending."* — filmed from inside the dark hallway, she opens the front door and exits into blinding daylight, held on the empty bright doorway.

### Instrumental — a day of writing

43. The typewriter carriage returning hard on the guitar phrase, macro, three times in a row.
44. A bin filling with crumpled starts, shot at intervals so it fills across the sequence.
45. Her on the floor with pages spread around her in a rough circle, rearranging them, overhead.
46. The window open and the curtain lifting, sunlight moving across the floorboards, locked-off, a whole afternoon compressed.
47. A hard drop to one bar of paper and typewriter noise: macro of a single blank page and a poised hand. The cut into the bridge.

### Bridge — the argument, plainly

48. *"For a while I let the last page grade the whole thing,"* — her sitting on the floor against the desk holding the last page, reading it, not reacting, static.
49. *"Like a bad review could reach back through the book."* — the whole pinned wall of pages behind her, in focus, her out of focus in front of it.
50. *"It can't. The summer happened. The kitchen happened."* — two two-second warm flashes: the market, then the kitchen coffee, both exactly as they were shot before.
51. *"The way you said my name still happened, and it was good."* — a third flash: a doorway, her turning because someone off-camera has said something, and smiling. No face on him.
52. *"An ending is a door, it is not a verdict,"* — her looking straight down the lens for the first time in the video, low warm light, static.
53. *"A place a story stops, not a place it failed."* — a real door in the flat standing open onto a lit hallway, nobody in frame, held.
54. *"So I keep the honest chapters and the mornings,"* — the kept stack going into a drawer, her hand resting on it before she closes it.
55. *"And I take back the pen the last one held."* — a shaft of late sun reaching the desk as she picks the pen up, strings arriving, low angle.

### Final chorus — out in the world

56. *"The story was good, I'm just better without the ending,"* — her walking a bright street in the trench coat with pages under one arm, tracking from the front, people around her.
57. *"Better without those last twelve pages of pretending."* — wide of the street, ordinary city life, nothing symbolic in frame at all.
58. *"Keep the summer, keep the songs, keep how it began,"* — her crossing a park with the yellow flowers, sun through the trees, tracking from the side.
59. *"I've taken back the pen and I'm writing where I stand."* — her stopping at a bench, writing standing up with the pages against her thigh, close-up.
60. *"It didn't need a villain, it didn't need a war,"* — a wide of the park, families, dogs, nothing dramatic anywhere in the frame.
61. *"It just needed to be over, and it's over, I'm sure."* — her face in full daylight, no shadow, medium close-up.
62. *"The story was good, I'm just better without the ending,"* — a push through an open doorway into a room full of light, her walking ahead of camera into it.
63. *"And I love the way this one begins."* — she turns in the light and looks back at the lens, the widest smile of the video, held.

### Post-chorus — claps and stomps

64. *"New page, new pen, new light on the table,"* — a fresh page going into the typewriter on a hard rhythmic cut, macro, midday.
65. *"No epilogue, no note on the door,"* — an empty door frame with no note on it, then the bin, full, going out.
66. *"The story was good, I'm just better without the ending,"* — the desk lamp switched off because the daylight has it covered, macro, on the beat.
67. *"And I'm not reading that last part anymore."* — a wide of the room from the doorway, bright, lived in, nobody in it.

### Outro — the answer

68. *"Somebody will ask me how it ended,"* — her at a café table with a friend off-camera, being asked something, medium.
69. *"And I'll say the good parts never did."* — her saying one short sentence and shrugging, warm and completely unbothered, close-up.
70. *"I keep the markets and the mornings in a drawer,"* — a drawer opening on a small ordered stack of kept pages, and closing again gently, macro.
71. *"And I left the last twelve pages where they lived."* — final shot: the desk at the window, a fresh page half-written in the typewriter, the room empty and full of light, held until the last chord stops ringing. No text.

## 5. Edit and the challenge

Markers at: the pen dying in shot 2, the single red line at 14, the curtains
at 18, her exit from frame at 23, the flowers at 29, the flat trio at 30, the
silent paper bar at 47, the look to camera at 52, the doorway at 62, and the
last chord. At 102 BPM a bar is 2.35 s; the choruses cut on the bar and the
post-chorus cuts on the clap.

**The red-pen challenge.** Post the vertical cut of shots 13–18 with *"an
ending is a door, it is not a verdict"* on screen, and invite people to post
one page of their own story with exactly one paragraph crossed out and
everything else left alone. The curtain-opening on the downbeat is the
shareable frame; *"Nobody died. I came home. I made dinner."* is the line the
comments will run on.

## 6. Quality-control checklist

- Brightness only ever increases across the video; no shot is darker than the one before it except the two-second memory flashes in the bridge
- Memories are graded exactly like the present — no soft filter, no dreamy overexposure, no fantasy
- The ex is faceless in every frame and is never shot unkindly; there is no villain image anywhere in this video
- Three looks in the right sections: oatmeal jumper in the flat, striped linen only in memories, trench coat only from shot 56
- All pages, handwriting, notes and phone screens composited; the single red line in shot 14 must strike exactly one paragraph
- The second chair leaves the flat at shot 25 and never reappears
- The curtain-opening is a brightness ramp over a lit plate, not a model-animated lighting change
- The last shot is locked-off and holds until the acoustic chord stops ringing
