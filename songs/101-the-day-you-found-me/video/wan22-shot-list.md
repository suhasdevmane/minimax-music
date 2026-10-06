# Wan 2.2 Shot List — "The Day You Found Me"

**One shot per lyric line**, built from the scene-by-scene direction in
`source/original-submission.md`. There are 76 lyric lines in `lyrics.txt`, so
there are 76 numbered shots, in order, with the instrumental covered by five
unnumbered shots. Timestamps come from the rendered WAV; cut on the sung line.
At 72 BPM a bar is 3.33 s.

## 1. Visual style

A warm, quiet domestic world. The **present** is grey and early: the kitchen
before dawn, the window still dark blue-grey, the light coming up slowly. The
**turn** is the child, and every shot after the doorway carries more warmth,
gold morning light, and yellow from the crayon sun. Nothing is glossy; the
home is lived-in, a little worn, real. Camera work is patient: locked-off for
the kitchen, a gentle handheld for the hallway and the child's movement, a
slow dolly for the car park. No quick cuts, no drama in the frame.

| Section | Grade | Camera |
|---|---|---|
| Intro / kitchen before dawn | Cool grey, one warm pendant | Locked-off close-ups |
| Verse 1 (routine, hallway) | Cool grey, then warm as she appears | Still wide, then handheld on the child |
| Pre-chorus 1 | Cool at the sink, warm hall backlight | Medium, reverse to doorway |
| Chorus 1 (admission) | Morning grey turning gold | Static, slow dolly |
| Verse 2 (drawing, car park) | Soft morning, flat daylight | Macro on paper, then slow pan |
| Pre-chorus 2 (office) | Fluorescent cool, warm hand on the paper | Medium, reverse |
| Chorus 2 (car park) | Flat daylight, warm car interior | Static through windscreen, slow push |
| Instrumental (car, lot) | Grey afternoon, building lights | Static wide, slow dolly |
| Bridge (the future) | Dim hall, one strip of light, evening kerb | Static, one piano |
| Chorus 3 (final) | Warm late-afternoon gold | Wide, slow move in |
| Post-chorus (kettle again) | Grey dawn on the floor | Static, handheld |
| Outro (night, then morning) | Warm hall light, cold night, clean sun | Locked-off, then slow |

## 2. Character bible — paste into every prompt

**Kai** (the father, present day)
> Same male character Kai, man in his late thirties, short dark hair, warm tired face, faint stubble, plain cardigan over a grey t-shirt, sleepy eyes, gentle expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (final chorus and outro, rested)
> Same male character Kai, man in his late thirties, short dark hair neatly combed, warm tired face softening into a smile, plain cardigan worn open, sleeves pushed to the elbow, relaxed expression, realistic cinematic photography, consistent identity, natural skin texture

**Ellie** (the daughter, morning)
> Same young girl Ellie, girl about four years old, wavy dark hair loose and slightly messy, pyjamas with small stars, one sock up to the knee, bare feet, bright curious expression, realistic cinematic photography, consistent identity, natural skin texture

**Ellie** (daytime, drawing)
> Same young girl Ellie, girl about four years old, wavy dark hair in a loose ponytail, yellow t-shirt, crayon marks on her fingers, focused proud expression, realistic cinematic photography, consistent identity, natural skin texture

**The drawing** — a child's crayon drawing on plain paper: a house with seven windows and a door too small to use, a yellow sun above the roof, purple-edged clouds, a fence round the lawn, and a tall figure holding a small one by the hand. The crayon sun is always yellow. It is a prop, shot close and real.

Kai and Ellie are the only people on screen in the home. The office, car park
and street may have background people, kept small and blurred.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All text is composited in the edit.** There is no visible text in this video
beyond the crayon drawing, which is a real prop shot close and then animated
without any letters on it. The kettle, the car clock and the office sign are
not legible; generate them blurred or cropped.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Kai in both looks and Ellie in both looks with IP-Adapter or a character
LoRA, and check the child's identity across the hallway, kitchen and bedroom
shots, since she carries the whole song. Keyframes first; OpenPose for the
hallway walk and the climb onto the counter; Depth for the kitchen and bedroom
compositions. 16:9 throughout. Animate conservatively: a kettle steaming, a
thumb on the paper, breathing, a sock pulled up, the light moving across the
floor.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the kitchen before dawn

1. *"The kettle clicks at ten past six,"* — close, locked-off on a kettle on a gas ring as it clicks off, steam rising into the grey window light, no people in frame, cool and still.
2. *"The window's holding grey,"* — wide static of the kitchen window, the sky dark blue-grey, the table and an empty mug in the foreground, the first hint of dawn.
3. *"I'm counting up the things to fix"* — Kai (present look) at the table, hands wrapped round a cold mug, eyes down, a list visible in his head, medium close, one warm pendant overhead.
4. *"Before I drive away."* — Kai lifting his keys from the worktop, closing his hand round them, the car keys ring catching the pendant light, close-up on the hand.

### Verse 1 — the routine, then the doorway

5. *"I used to carry mornings like a crate I couldn't set down,"* — Kai in the hallway with a bag on one shoulder and his keys in the other hand, walking the length of the hall, handheld, cool grey light.
6. *"Keys in one hand, trouble in the other, both my shoulders down."* — close on his shoulders and hands as he shifts the bag, the weight visible in how he holds himself, static from the side.
7. *"I kept a running total of the ways I came up short,"* — Kai at the front door, one hand on the frame, looking at the floor, a slow push in, cool blue light.
8. *"And I called that being careful, and I called that being tough."* — Kai buttoning his cardigan in the dark hallway mirror, his face tired and set, medium, cool grey light.
9. *"Then a door came open slowly at the far end of the hall,"* — the far bedroom door opening, a warm strip of light across the hall floor, wide static, the first warm light in the frame.
10. *"And two bare feet went running on a floor that's always cold."* — Ellie (morning look) running barefoot down the hallway toward camera, the floor cold and grey, handheld, low angle, the feet in focus.
11. *"You had your hair gone sideways and one sock up to your knee,"* — Ellie stopping in the kitchen doorway, hair sideways, one sock up, pyjamas with small stars, medium, warm light.
12. *"And you asked me if the morning had a plan for you and me."* — Ellie looking up at Kai, asking, Kai crouched to her height at the kitchen table, over-the-shoulder with the child in profile.
13. *"You climbed up on the counter where you're never let to climb,"* — Ellie climbing onto the kitchen counter, Kai's hands steadying her by the waist, a slight rise in the frame, warm light.
14. *"And you told me it was going to be a good one, this time."* — Ellie on the counter beaming and pointing at the window, Kai laughing for the first time, both in warm light, wide and handheld.

### Pre-chorus 1 — the reasons

15. *"I had been hunting for my reasons"* — Kai at the sink in the grey light, both hands on the edge of the basin, head down, searching, medium, cool and still.
16. *"In the hardest hour of day,"* — Kai on the back step outside in the early dark, hands in cardigan pockets, looking at nothing, wide, cold blue.
17. *"Then a small voice in a doorway"* — reverse: the kitchen doorway, Ellie framed in it with the warm hall light behind her, calling out, shallow depth of field.
18. *"Took the heavy part away."* — Kai turning from the sink toward the doorway, his face opening, the first real lift in the picture, medium close, warm light flooding in.

### Chorus 1 — the admission

19. *"Everybody thinks I saved you,"* — Kai at the kitchen table, Ellie on the floor with a crayon box, facing the room, a slow dolly from the table toward the child, gentle warm light.
20. *"But I've got it upside down."* — Kai's hands flat on the table, looking at them, a small shake of the head, close and static.
21. *"I was the one who went missing,"* — Kai looking over at the window, the morning light coming up gold through the glass, static medium, face in profile.
22. *"Standing right here, not around."* — Kai standing up slowly from the chair, the child looking up from her drawing at him, medium-wide, warm.
23. *"I was tired and I was quiet"* — Kai's face close and still, his mouth closed, eyes tired, soft gold on his cheekbone, extreme close-up.
24. *"And I called it getting by,"* — Ellie tugging his cardigan sleeve, Kai looking down at her, a slight smile, medium, warm.
25. *"Till you found me in the hallway"* — the hallway behind them, the morning light a long strip along the floor, Ellie's bare feet visible in the corner, wide static.
26. *"At ten past six one day."* — Kai and Ellie on the kitchen floor sharing a crayon, the kettle clicking in the background, both warm, a locked-off wide.

### Verse 2 — the drawing and the car park

27. *"You drew a house with seven windows and a door too small to use,"* — macro on the crayon drawing on the table: a house with seven windows, the door small, Ellie's fingers holding a yellow crayon in the corner.
28. *"And a yellow sun above the roof the sky could never lose."* — macro on the yellow sun drawn over the roof, the crayon strokes visible, the paper grain catching morning light, slow pan.
29. *"You gave the clouds a purple edge, you put a fence around the lawn,"* — Ellie holding the drawing up to the camera with both hands, the purple cloud and the fence in focus, medium, warm.
30. *"And a man beside a little girl, and the man was holding on."* — the drawing close, the two figures in crayon, one tall and one small, held by hands; cut to Kai's hand resting on the table beside it.
31. *"You held it up and waited there and watched me while I read,"* — Kai at the table reading the drawing, Ellie watching him from across the table, both faces in warm light, medium.
32. *"And you said that I could keep it if I kept it by my bed."* — Ellie on her tiptoes handing him the drawing, Kai taking it with both hands, close, warm.
33. *"So I folded up your masterpiece and slid it in my coat,"* — Kai folding the paper carefully in half, then into quarters, sliding it into the inside pocket of his cardigan, close on the hands, morning light.
34. *"And it rode there through the whole long day, a small and folded note."* — Kai in a car park under flat daylight, walking to the office door, his hand resting on the pocket over the paper, wide, slow dolly.
35. *"Nobody in that building knew the reason I could stand,"* — Kai inside the office lobby among suited colleagues, unseen by them, standing straight, a small private steadiness, medium, flat daylight.
36. *"There was paper in my pocket with a sun you drew by hand."* — extreme close on the pocket, the corner of the folded drawing showing a yellow crayon edge, his hand pressing it flat, warm light.

### Pre-chorus 2 — the same lift, with the drawing

37. *"I had been hunting for my reasons"* — Kai at his office desk, the screen dim, his hand resting over the cardigan pocket, head bowed, medium, cool fluorescent light.
38. *"In the hardest hour of day,"* — Kai in the stairwell at his workplace, one hand on the rail, looking up at the window, wide, cool blue.
39. *"Then a small voice in a doorway"* — reverse: a corridor door, the light behind it, and for a moment a small figure framed in the glass, shallow depth of field, a faint warm glow.
40. *"Took the heavy part away."* — Kai putting his hand flat on the pocket with the drawing, his shoulders dropping, medium close, warm light spilling from the corridor.

### Chorus 2 — the wider chorus, the car park

41. *"Everybody thinks I saved you,"* — Kai sitting in his parked car in the car park, the drawing on the passenger seat, looking at it through the windscreen, static wide, flat daylight.
42. *"But I've got it upside down."* — the drawing on the passenger seat, close, the purple cloud and the fence, a slow push-in, the car interior warm from the sun through the glass.
43. *"I was the one who went missing,"* — Kai's face in the rear-view mirror, eyes tired, a slow push toward the mirror, wide shot, mirror glass reflecting the car park.
44. *"Standing right here, not around."* — Kai's hand on the passenger seat resting on the drawing, the car park out the window, medium, warm.
45. *"I was tired and I was quiet"* — Kai's face close through the windscreen, mouth closed, a slow breath, the sky grey-blue behind him.
46. *"And I called it getting by,"* — extreme close on Kai's eyes, one tear held back, static, warm car light across his face.
47. *"Till you found me in the hallway"* — a brief warm memory flash of the hallway and Ellie's feet on the cold floor, then back to the car park, cut in on the sung word.
48. *"At ten past six one day."* — Kai in the car, closing his eyes for one beat and opening them, a small nod, wide, flat daylight.

### Instrumental — sixteen bars, no lyrics

- Kai in the parked car, engine off, both hands on the wheel, a locked-off wide of the car in the car park, flat daylight dimming to grey.
- Slow dolly to the drawing on the passenger seat, a shallow focus on the yellow sun.
- Kai's hand reaching for the passenger seat and resting on the paper, close, warm.
- Kai getting out of the car, the drawing in his hand, walking toward the office building, handheld, the building lights coming on behind him.
- Kai stopping at the office door, looking back at the car park, then turning in, the door closing softly, static from the side.

### Bridge — the future, nearly spoken

49. *"One day this hall will be a city"* — the hallway at home, empty and dim, one strip of light across the floor from an open door, a long static frame, a slow exhale in the dark.
50. *"And the door you open, yours alone,"* — a bedroom door swinging open at the end of the hall, a grown silhouette of a young woman in the doorway, back to camera, warm light behind her.
51. *"And the feet that came out running to me"* — a close on bare feet on the cold floor, then the feet in trainers stepping over the threshold, the same floor, handheld low.
52. *"Will be running down a road of your own."* — a wide exterior of an evening street, the young woman walking away from camera down the pavement, small in the frame, golden light.
53. *"I'll be glad. I'll carry boxes."* — Kai in an open-back van at a kerb, lifting a cardboard box with a grin, medium, evening light, his face looking forward.
54. *"I'll stand waving at the kerb."* — Kai at the kerb raising one hand, small in the wide frame, the street empty, a slow push in.
55. *"And I'll keep a folded drawing"* — extreme close on Kai's hand touching the cardigan pocket, the folded drawing visible through the cloth, warm.
56. *"In my coat, the way I learned."* — Kai at the front door of an empty house, pressing the folded drawing into his inside pocket one more time, morning light, medium.
57. *"You won't know you ever did it,"* — Ellie (grown, seen only from behind) walking across a crowded platform, unaware of him, wide and still, soft focus.
58. *"You'll just think you grew up fine."* — back in the present: Kai in the hallway at home, one hand on the wall, eyes closed, a long breath, a warm light on his face, cut to the child's bedroom door.

### Chorus 3 — the final chorus, full arrangement

59. *"Everybody thinks I saved you,"* — the kitchen in late afternoon gold: Kai and Ellie at the table with her drawings spread out, a wide locked-off, light through the window across the room.
60. *"But I've got it upside down."* — Ellie holding up a new drawing, a house with seven windows again and a bigger yellow sun, Kai leaning in to look, medium, warm.
61. *"You're the one who came and got me,"* — Ellie climbing down from her chair and running round the table to Kai, arms open, a slow handheld follow.
62. *"You're the reason I'm around."* — Kai lifting her up onto his lap at the table, both laughing, the drawings sliding across the wood, medium-wide, gold light.
63. *"I was tired and I was quiet"* — Kai in profile looking out the window, a rested expression, sleeves pushed up, the late sun on his face, static.
64. *"And I called it getting by,"* — Kai laughing at something Ellie says, his head thrown slightly back, warm, medium close.
65. *"Then you found me in the hallway,"* — a quick cut to the hallway, the light falling in a long strip across the floor, the child's bare feet, warm, a slow dolly.
66. *"And you find me every day."* — the family wide shot: Kai and Ellie at the window of the kitchen, the sun going down, both in warm silhouette against the glass, wide and slow, the choir lifting.

### Post-chorus — the kettle and the hallway

67. *"Ten past six, the kettle clicking,"* — the kitchen the next morning, the kettle on the gas ring clicking, steam rising, the drums gone, a locked-off close on the kettle, grey light.
68. *"Grey light coming through the floor,"* — the grey dawn light falling in a long soft patch across the kitchen floor, the child's bare feet stepping into it, low static.
69. *"You found me in the hallway"* — Ellie walking down the hall toward the kitchen, her small figure in the doorway, Kai turning to look at her from the counter, handheld, warm.
70. *"And you don't even know."* — Kai at the counter, a slow smile as Ellie climbs onto the stool beside him, close on the two of them, the light building.

### Outro — the step

71. *"So sleep now, there's no hurry,"* — night: Ellie asleep in her bed under a blanket, the bedside lamp low, the door open a crack and the hall light on, locked-off close.
72. *"Let the morning do the rest."* — the hall light left on, a long static frame of the empty hallway with a warm strip across the floor, the sound of the house settling.
73. *"You found a man who'd gone missing"* — Kai at the front door in the dark, the drawing in his coat, looking back at the lit window of his daughter's room, medium, cool blue night.
74. *"And you walked him to the step."* — Ellie in her pyjamas on the front step beside him in the cold, her hand in his, the two of them looking at the stars, wide and still.
75. *"And he isn't going back there,"* — Kai closing the front door gently behind them, walking with Ellie to the car in the first grey light, handheld, slow.
76. *"Not while you still say his name."* — final shot: Ellie in the back seat of the car with the window down, the morning sun on her face, the drawing on her knee, Kai's hand on the wheel, locked-off through the windscreen, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the kettle click at the top of the song,
the bridge's first line ("One day this hall will be a city"), the final
chorus's first line ("Everybody thinks I saved you"), and the outro's last
line ("Not while you still say his name"). At 72 BPM a bar is 3.33 s. The
instrumental is sixteen bars, about 53 s; the five unnumbered instrumental
shots cover it in roughly 11 s each.

**The shareable cut.** The post-chorus kettle shot (shots 67–70) is the
calmest and most shareable frame: a kettle, grey dawn light, a child walking
into the kitchen. Post it vertical, with the line *"you don't even know"* on
screen, and invite parents to post their own kitchen-morning moment with a
drawing their kid made for them.

**The drawing challenge.** The drawing is the prop. Invite viewers to share a
drawing a child gave them, the moment it was handed over, tagged with the first
chorus. The caption to pin is *"everybody thinks I saved you, but I've got it
upside down."*

## 6. Quality-control checklist

- Kai reads as one man across every shot: late thirties, short dark hair, warm tired face, plain cardigan; in the final chorus and outro the cardigan is open and the sleeves are pushed up
- Ellie reads as one girl across every shot: about four, wavy dark hair, pyjamas with small stars in the morning and the yellow t-shirt in the daytime; the bedroom and outro shots keep the same hair and face
- The yellow sun on the drawing is the same in every close-up, and the drawing is never shown with any legible letters
- The grade moves from cool grey (intro, verse 1) to warm gold (chorus 1 onward) and stays warm through the outro; the bridge is the only dim section
- The bridge's grown-up figure is shot from behind or in soft focus, never a clear face
- No text, lettering or legible UI generated by the model; the kettle, car clock and office sign stay blurred or cropped
- No distorted hands, especially in the counter climb, the drawing close-ups and the folding shot
- The last shot is locked-off through the windscreen and holds until the audio fades
