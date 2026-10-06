# Wan 2.2 Shot List — "Cassette Tape Heart"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
100 BPM a bar is 2.4 s, so most shots are 3–5 s and the choruses cut on the
gated snare.

## 1. Visual style

Three worlds that gradually stop being separate. The **present** is a real
flat, one warm lamp, cold window light, handheld and close. The **memory**
is a teenage bedroom and a winter car, shot with heavy VHS grain, a magenta
cast and slightly wrong tracking. The **synthwave world** is what the
choruses do to both: magenta key, cyan rim, atmospheric haze, one practical
lamp always left in frame so it stays a room rather than a poster. The
bridge removes every gel in the video and shoots her under one overhead bulb
— that ugliness is the point. The final chorus brings colour back as amber
instead of magenta.

| Section | Grade | Camera |
|---|---|---|
| Intro | One warm lamp, deep shadow, cool window | Macro, static, close |
| Verse 1 | VHS grain, magenta cast, wrong tracking | Handheld, memory feel |
| Pre-choruses | Lamp only, face half-lit | Extreme close-ups, mechanical |
| Choruses | Magenta key, cyan rim, haze, one practical | Slow tracking, to lens |
| Verse 2 | Dashboard green, headlights, black water | Static in-car, macro |
| Instrumental | Most stylised, then a hard drop to black | Tape-stop, reverse, corridor |
| Bridge | One overhead bulb, no gels at all | Static, one slow push |
| Final chorus | Warm amber key, cyan reduced to a rim | Wide, moving, released |
| Post-chorus | Warm and level | Macro, mechanical |
| Outro | Lamp, then window blue, then dark | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (present day)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair loose and unstyled, no makeup, wearing a soft oversized grey knit and pyjama shorts, bare feet, quiet absorbed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (memory, nineteen)
> Same female protagonist Mahima, young woman of nineteen, expressive dark eyes, oval face, long dark wavy hair with a blunt fringe, eyeliner and clear lip gloss, wearing a striped long-sleeve top and a corduroy skirt over tights, large over-ear headphones around her neck, open hopeful expression, realistic cinematic photography, consistent identity

**Mahima** (bridge only)
> Same female protagonist Mahima, young woman in her mid-twenties, expressive dark eyes, oval face, long dark wavy hair pushed behind one ear, no makeup, wearing the same grey knit, sitting on a bare floor under a single overhead bulb, unguarded exhausted expression, realistic cinematic photography, consistent identity

**The boy** — never shown. He exists as hands only: a finger over a record
button, a hand on a heater dial, a sleeve clearing frost. No face, no
shoulder, no back of a head. He is a handwriting sample and a pair of hands.
> a young man's hands only, no face in frame, plain long-sleeved top

Objects, and they carry this video: the **cassette** and its **white card**
with sloping handwriting, the **personal stereo** and its lid, the **two
batteries** out of a **wall clock**, the **brown ribbon**, the **pencil**
used to wind a spool, the **dashboard tape deck**, the **drawer**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All handwriting, cassette labels, tape counters, radio displays and phone
screens are composited in the edit.** Generate the card as blank white and
the counter as a blank window; the model cannot render legible text, and the
handwriting must stay unreadable anyway — the audience should recognise the
gesture, not read the words. The VHS grain, tracking errors and the tape-stop
are all post effects, not prompts.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; the
nineteen-year-old look needs its own reference set with the fringe, not just
a wardrobe change. Depth for the shots where the teenage bedroom is visible
through a present-day doorway — the model will otherwise merge the two rooms
into one incoherent space, and the whole chorus idea depends on them being
two. OpenPose for the dancing in the final chorus. 16:9 first; 9:16 for the
macro mechanism shots, which are the shareable cuts. Macro work is the bulk
of this video: generate the cassette, spools, ribbon and drawer as their own
stills with a hand in frame for scale. Animate only one mechanical action per
clip — a lid closing, spools turning, a drawer sliding — and let the edit
carry the rest.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the drawer

1. *"Found it in a drawer with the batteries dead"* — macro into an open drawer: a cassette lying among tangled chargers and old cables, a hand entering frame, one lamp, static.
2. *"Your handwriting sloping across the white card"* — the white card in the case, handwriting sloping downhill and deliberately out of focus at the top, macro, composited.
3. *"A breath of static before anything starts"* — the battery hatch of a personal stereo opening onto corrosion, extreme close-up, silence in the frame.
4. *"And a girl I used to be sits down in the dark"* — Mahima sitting down on the floor with her back against the bed, tape in hand, wide, one lamp, held.

### Verse 1 — how it was made

5. *"You made it in a bedroom with the radio on"* — memory, VHS grain: a teenage bedroom, a stereo with a lit display, tapes stacked on the carpet, static wide, magenta cast.
6. *"One finger on the button, waiting hours for a song"* — a young man's finger hovering over a record button, only the hand, extreme close-up, held far too long.
7. *"You caught the deejay talking at the top of track four"* — the finger coming down late, a radio dial and lit display (composited), the small disaster of it, macro.
8. *"You swore, and you kept it, and I loved you all the more"* — the hand pulling back from the stereo and just leaving it, then the tape ejecting, medium macro.
9. *"I played it till the ribbon wore as thin as a thread"* — present day: brown ribbon pulled out an inch and held up to a lamp, thin and translucent, macro.
10. *"And the fourth song always skipped and I loved it instead"* — nineteen-year-old Mahima on a bedroom carpet with headphones on, laughing at a skip nobody else can hear, VHS grain, medium.

### Pre-chorus 1 — new batteries

11. *"New batteries out of the back of the clock"* — a wall clock lifted down and its battery hatch opened, the second hand stopping, macro, funny and a bit ruthless.
12. *"The lid clicks down and the motor kicks up"* — two batteries in, the lid clicking down, extreme close-up on the plastic catch, the spools starting.
13. *"Four beats of a drum that I'd know anywhere"* — her eyes closing on the fourth beat, close-up, lamp on one side of her face only.
14. *"And I'm nineteen again and you're still standing there"* — a slow push past her toward an open doorway where the teenage bedroom is visible in magenta, depth-mapped, the video's first world-merge.

### Chorus 1 — the synthwave world

15. *"I've got a cassette tape heart, and you're on side A"* — Mahima walking through her own flat as the corridor turns magenta and cyan around her, haze, slow tracking, one practical lamp still in frame.
16. *"Wound tight in a drawer where I left you that day"* — macro of the spools turning, a whole window and city reflected in the plastic window of the cassette.
17. *"Everyone after you got put down on side B"* — a wall of tapes, all unlabelled, filling the frame, slow pan.
18. *"Recorded over you, and you still bleed through the seams"* — the same wall, with one tape in the middle glowing faintly through the others, slow push, the single most composited shot in the video.
19. *"Press rewind, press rewind, let the spools start to turn"* — a thumb on a rewind button held down, spools blurring, extreme close-up, cyan rim.
20. *"There's a hiss in the silence I could never unlearn"* — her singing straight down the lens for the first time, magenta key, haze behind her, medium close-up.
21. *"I know how it ends and I press play anyway"* — the play button going down under a thumb, macro, the mechanism visibly engaging.
22. *"I've got a cassette tape heart, and you're on side A"* — a wide of her standing in the middle of the lit flat with the teenage bedroom glowing through the doorway behind her.

### Verse 2 — the car

23. *"A car with a tape deck and a heater that lied"* — memory: a car interior at night in winter, dashboard green, breath visible, static from the back seat.
24. *"Frost on the inside of the glass and your hand on the dial"* — a sleeve clearing frost from the inside of a windscreen, then a hand only on a heater dial, two macro cuts.
25. *"We drove past the water till the second side ran out"* — headlights on a wet road beside black water, seen through the windscreen, static, long.
26. *"And the click at the end of it was the loudest sound"* — the dashboard deck clicking and stopping, macro, and the cabin visibly going silent around it.
27. *"I never taped over side A and I don't know why"* — present day: the tape held between two fingers, turned over once and turned back, close-up.
28. *"I just wound it to the front and I put it back inside"* — a pencil inserted into a spool and wound back to the front, macro, the most tactile shot in the video.

### Pre-chorus 2 — the second play

29. *"Thumb on the button, and I know I should stop"* — a thumb on rewind held far too long, the counter numbers spinning (composited), extreme close-up.
30. *"The lid clicks down and the motor kicks up"* — reuse shot 12, tighter and slower, the catch closing.
31. *"Four beats of a drum that I'd know anywhere"* — her sitting on the floor with her back to the bed, phone face-down and glowing beside her, static.
32. *"And I'm nineteen again and you're still standing there"* — the teenage bedroom furniture now standing in her present-day flat, both rooms in one frame, wide.

### Chorus 2 — fully merged

33. *"I've got a cassette tape heart, and you're on side A"* — the two versions of her passing each other in the merged room without looking, deeper magenta, more haze, tracking.
34. *"Wound tight in a drawer where I left you that day"* — reuse shot 16, tighter, the reflection now showing the teenage bedroom instead of the city.
35. *"Everyone after you got put down on side B"* — a hand pushing a tape into a stack and it not fitting, macro.
36. *"Recorded over you, and you still bleed through the seams"* — magenta light leaking out of the seam of a closed drawer, macro, held.
37. *"Press rewind, press rewind, let the spools start to turn"* — the spools at full speed, the frame vibrating slightly with them.
38. *"There's a hiss in the silence I could never unlearn"* — her to lens again, closer, the haze now between camera and face.
39. *"I know how it ends and I press play anyway"* — nineteen-year-old Mahima pressing play in the memory and present-day Mahima pressing play in the flat, split on the same beat.
40. *"I've got a cassette tape heart, and you're on side A"* — the widest merged frame: two rooms, two eras, one lamp, magenta and cyan.

### Instrumental — tape-stop and rewind

41. The tape-stop rendered literally: everything in the room slowing, dropping in pitch, the light sagging, her movement slumping to a halt over two full seconds.
42. A full rewind sequence played backwards at speed: the car reversing along the water, the frost re-forming on the glass, the pencil unwinding, the drawer re-opening.
43. One bar of pure hiss: the frame goes to black except for a single ticking point of light, the arpeggio alone.
44. The lead synth solo shot as Mahima walking a corridor of vertical light bars toward camera, slow motion, magenta into white.
45. A hard cut to nothing: black frame, two seconds, the sound of a lid opening.

### Bridge — no gels

46. *"I don't want you back, I want the girl that I was"* — Mahima on the bare floor of a plain badly lit room under one overhead bulb, tape in hand, static, no colour gel anywhere.
47. *"The one who thought a tape was a promise you could hold"* — the tape held flat in both palms, macro, ordinary light, no glow.
48. *"I want the bedroom carpet and the waiting and the hiss"* — a single flashback frame: nineteen-year-old Mahima alone on a bedroom carpet with headphones on, entirely happy, no boy anywhere in the frame.
49. *"I want an afternoon spent making one thing good"* — the same memory continuing: her writing on a card with a ballpoint, the pen and the hand, never the words.
50. *"You were never the point, though I let you be for years"* — back to the bulb: a slow push to her face, the ugliest and most honest light in the video.
51. *"You're just the sound of the last time that I was new"* — she looks up and off camera, decides something, and the bulb flickers once, static, held.

### Final chorus — amber

52. *"I've got a cassette tape heart, and you're on side A"* — she stands up and the room comes back in warm amber instead of magenta, wide, released.
53. *"Wound tight in a drawer, and that's exactly where you stay"* — the flat's windows going gold, cyan reduced to a rim on her shoulders, medium.
54. *"Everyone after you got put down on side B"* — the wall of tapes again, warm now, and she walks past it without stopping.
55. *"And the bleed is getting quieter, and that is alright with me"* — the glow in the middle of the tape wall fading down to nothing over the length of the line, slow push.
56. *"Press rewind, press rewind, let the spools start to turn"* — the spools once more in macro, warm light on the plastic.
57. *"There's a hiss in the silence I could never unlearn"* — her dancing alone with the over-ear headphones on, properly and happily, not sadly, medium handheld.
58. *"I know how it ends and I press play anyway"* — the widest frame of the video: the whole flat in amber, her small and moving in the middle of it.
59. *"I've got a cassette tape heart, and you're on side A"* — her to lens one last time, warm key, no haze, a real smile.

### Post-chorus — the side runs out

60. *"Side A, side B, and the click at the end"* — the spools with one side nearly empty, macro, slowing.
61. *"Side A, side B, and I wind it again"* — the counter slowing to a stop (composited), macro.
62. *"All that hiss, all that hope, that afternoon"* — the mechanism clicking and stopping on its own, extreme close-up.
63. *"Side A, side B, and I let it run through"* — her not reaching for it, sitting still with the player in her lap, static, held.

### Outro — the drawer closes

64. *"Batteries out and the drawer slides away"* — two batteries taken out and stood upright on a desk, macro, deliberate.
65. *"Card in the case with the crease and the fray"* — the white card slid back into the case along its worn crease, the crease itself in macro.
66. *"I won't wind you back for a long time, but stay"* — the cassette placed in the drawer lying flat on top, not buried under the cables, close-up.
67. *"I've got a cassette tape heart, and you're on side A"* — final shot: the drawer sliding shut in macro, then a wide of the room as the lamp switches off, leaving only window blue. Hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the lid clicking down (shot 12), each "cassette tape heart", the
click at the end of the car side (shot 26), the pencil winding (shot 28),
the tape-stop, the bar of pure hiss (shot 43), the bulb (shot 46), the amber
turn (shot 52) and the drawer closing. At 100 BPM a bar is 2.4 s; the
choruses cut on the gated snare, and the post-chorus cuts on the mechanism
rather than the beat.

**The drawer challenge.** Shots 1–4 and 11–15 recut vertically are the
shareable fifteen seconds: the drawer, the card, the wall clock robbed for
batteries, the lid, the spools, the first chorus hit. Invite people to post
the object they have never been able to throw away. The pencil-winding shot
(28) is the second shareable frame and will travel on its own.

**Caption cut:** shots 46–48 with *"I don't want you back, I want the girl
that I was."*

## 6. Quality-control checklist

- Three looks: present-day grey knit, the nineteen-year-old with the fringe in every memory, and the bridge look which is the present-day one under a bare bulb
- The boy is hands only, in every single frame he appears; no face, no shoulder, no back of a head at any point
- The handwriting on the card is never legible in any frame, at any zoom
- The magenta and cyan world never appears in a verse and never appears in the bridge; the bridge has no colour gel of any kind
- The final chorus is amber, not magenta, and the change happens exactly on shot 52
- All labels, counters, radio displays and screens composited; the VHS grain, tracking errors and tape-stop are post effects
- Every macro of the cassette, spools, ribbon and drawer generated with a hand in frame for scale, and hand-checked before use
- The last shot is the drawer closing and the lamp going out, locked-off, held until the audio fades
