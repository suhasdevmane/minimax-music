# Wan 2.2 Shot List — "Villain in Your Story"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
98 BPM a bar is 2.45 s. Most shots run 3–5 s, except the rap verse, which
cuts on the sixteenths and runs 1–2 s a shot.

## 1. Visual style

One London townhouse gala, one night, one staircase. **Red is the story he
is telling and blue is the one she is living**: the party interior is red
uplight on marble with warm chandeliers above it, the street and the terrace
are cold blue, and the only shot with no red on her at all is the bridge.
Slow, composed camera everywhere — she never hurries, so the camera never
does either, until the rap verse, where everything cuts on the beat for
forty seconds and then stops. Flash punctuation, deep shadow, real practicals.

| Section | Grade | Camera |
|---|---|---|
| Intro | Deep blue street, warm interiors, one hard mirror practical | Slow drifts, static mirror |
| Verse 1 | Warm chandeliers with red creeping in | Steady tracking through the crowd |
| Flashback (verse 1) | Desaturated fluorescent grey | Static, flat, ugly |
| Pre-choruses | Chandelier from behind, red from below | Locked-off, one slow push |
| Choruses | Red uplight on marble, white flash punctuation | Slow descent tracking, low angles |
| Verse 2 (rap) | Hard flash over red, near-black shadow | Fast handheld, cut on sixteenths |
| Instrumental | Red through glass, cold blue outside | Balcony wide, then still |
| Bridge | Cold blue, one warm doorway spill, no red | The only handheld drift in the video |
| Final chorus | Red into blue, the hardest colour cut | Moving with her, then locked at the door |
| Post-chorus / outro | Sodium and blue, then first daylight | One-beat inserts, then slow and wide |

## 2. Character bible — paste into every prompt

**Mahima** (the gala — everything from the mirror to the front door)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair swept back off her face and falling behind one shoulder, sharp evening makeup with a matte deep red lip and a fine liner, gold drop earrings, wearing a long black backless satin gown, composed unimpressed expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the flashback in verse one — deliberately plain)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark hair tied back tightly, minimal makeup, wearing a plain charcoal blazer over a white shirt, level unreadable expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the outro — dawn, going home)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly undone, evening makeup worn down, wearing the same long black gown under a long dark overcoat, barefoot, calm private expression, realistic cinematic photography, consistent identity, natural skin texture

**The ex** — faceless throughout. He is the man in the corner telling the
story, cropped at the chin or shot from behind, always with people leaning
toward him.
> a man in his late twenties, cropped at the chin or shot from behind, black dinner jacket, hands gesturing while he talks to a small group

**The party** — thirty to forty guests in black tie, no individual featured
twice, no face held longer than a beat. They exist as a crowd that turns.

**The press line** — a row of photographers at the foot of the stairs, faces
hidden behind cameras and flash. Never a recognisable person.

Objects that must stay continuous: the **tall old mirror** at the half-landing,
the **black satin gown**, the **gold drop earrings**, the **single drink** she
carries and later sets down on the balustrade, the **marble staircase**, the
**heels** (worn all night, carried at dawn).

**The crown is never a prop.** At the half-landing the chandelier behind her
throws light through her hair that reads as a crown for two frames only, in
the mirror. It is a lighting effect and a two-frame edit, never an object,
never a graphic, never worn.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All signage, place cards, the document she signs and any press pass is
composited in the edit.** Generate papers as blank sheets and overlay in
post — the model cannot render legible text, and a gala full of nonsense
lettering will read as cheap immediately.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
ex's reference deliberately faceless and never let a generation resolve his
jaw. Depth is essential for the staircase and the crowded interiors, which
the model flattens badly under coloured light. OpenPose for the descent and
the walk through the room. 16:9 first; 9:16 for the descent, which is the
shareable cut.

Animate conservatively: a dress moving on stairs, a hand sliding on a rail, a
crowd turning, a flash firing, a smirk arriving. **Camera flashes are added
in the edit as one-frame white pops on a lit plate**, deliberately out of
rhythm with the music; do not ask the model to generate flash.

The rap verse (shots 26–35) is the exception to every pacing rule here: cut
it on the sixteenths, generate each shot short, and accept that half of them
are one second long.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

## 4. Scene per lyric line

### Intro — the reputation arrives first

1. *"There's a version of me round Mayfair tonight"* — a wet Mayfair street from inside a moving black cab, lit townhouse windows going past, slow drift, deep blue.
2. *"Doing terrible things in somebody's mouth"* — inside the party: a faceless man in a dinner jacket telling a story to three people, hands moving, cropped at the chin.
3. *"Apparently I'm ruthless, apparently I'm ice"* — the listeners' faces reacting, one raising eyebrows, warm chandelier light, medium.
4. *"Apparently I burned a perfectly good house"* — a wide of the room where the story has clearly already travelled, small clusters all talking, static.
5. *"Black dress zipped, called a cab off the Strand"* — a dressing mirror: a black satin gown being zipped from behind by her own hand, close-up, one hard practical.
6. *"Walked in on time with a drink in my hand"* — her stepping through the front doors of the townhouse, taking a drink off a tray without breaking stride, tracking.

### Verse 1 — the polite room

7. *"They're polite when they think you can't hear"* — a tray of champagne moving through the crowd, her following behind it, over-the-shoulder.
8. *"Same room, same champagne, same knives"* — two people mid-sentence going quiet as she passes and starting again after, medium, warm with red creeping in.
9. *"I was quiet for years, I made myself small"* — a wide of the room where every face is turned very slightly the same way, static.
10. *"Then I asked what I'm worth and I ruined our lives"* — flashback, desaturated fluorescent: her in a meeting room saying a number out loud, the room going still, flat and ugly.
11. *"That's the charge sheet, if you want it read"* — the flashback continues: her signature going onto a blank document (composited), close-up on the pen.
12. *"I stopped apologising for the room that I fill"* — flashback: her walking out of an office at night carrying a box, wide, grey.
13. *"I never took a thing that wasn't mine"* — hard cut back to the party: her taking a drink from the tray and not thanking anybody, close-up.
14. *"I just stopped giving mine away, and I never will"* — her turning toward the staircase, the red uplight hitting her face for the first time, medium.

### Pre-chorus 1 — the mirror on the landing

15. *"Put me in the black hat, put me in the wrong"* — her climbing to the half-landing, the party noise dropping behind her, tracking from behind.
16. *"Give the tragic bit to you, I'll take the song"* — she stops in front of the tall old mirror, wide, chandelier behind her.
17. *"There's a mirror on the landing, it doesn't say cruel"* — her reflection, held, static, no push yet.
18. *"It says girl who finally stopped losing to you"* — a slow push into the reflection; for two frames only the chandelier light through her hair reads as a crown. **The two-frame crown.**

### Chorus 1 — the descent

19. *"Tell it how you tell it, I'll allow it"* — she starts down the marble staircase in red light, one hand on the rail, slow tracking beside her.
20. *"Paint me in the red light, make it loud"* — her face lit red from below, chandelier gold on her hair, close-up, unhurried.
21. *"Every story needs a shadow at the party"* — her shadow thrown huge up the wall behind her, moving with her, wide.
22. *"And I wear it better than you wore the crown"* — the room below turning toward her in waves, low angle from the foot of the stairs.
23. *"I'll be the villain in your story, the hero in mine"* — the press line firing, one-frame white flash pops out of rhythm, her not blinking, medium. **The hook frame.**
24. *"Same girl, two books, and I'm fine with the line"* — her hand leaving the rail at the bottom step, macro, red on marble.
25. *"I'll be the villain in your story, the hero in mine"* — she steps off the stairs into the room and the crowd opens without anyone deciding to, wide, held.

### Verse 2 — the rap verse, cut on the sixteenths

26. *"Cameras on the staircase, I don't blink, don't dip"* — a flashbulb freezing her face, eyes open, one second, hard flash over red.
27. *"Red light on the marble, got a smirk on my lip"* — extreme close-up: a smirk arriving and held one beat too long, one second.
28. *"Briefing all week, got a script, got a spin"* — the faceless man gesturing at the staircase while three people watch, one second.
29. *"Mate in the corner doing PR for your sin"* — a second man leaning in to listen and nodding along, cropped at the chin, one second.
30. *"Call me calculating, that's a compliment, mate"* — her walking straight through the middle of the room, people moving out of the line, handheld, two seconds.
31. *"Did the maths on my worth and sent you the rate"* — her signature going onto a blank page in a side room (composited), the party visible through a doorway behind her.
32. *"You liked me when I whispered, loved me when I shrank"* — two-second flashback flash: the plain blazer look, quiet, in a corridor, then hard cut back.
33. *"Now the girl in the glass has a crown and a bank"* — the mirror at the half-landing seen from below through the crowd, empty, still lit, one second.
34. *"Spell it properly when you take my name in vain"* — a photographer's lens racking focus onto her face, one second, flash.
35. *"Villain's just a woman who declined the blame"* — her stopping dead in the middle of the room and looking straight down the lens, three seconds, everything else moving.

### Pre-chorus 2 — the mirror again

36. *"Put me in the black hat, keep me in the wrong"* — the same half-landing, the party louder behind her, wide, one stop brighter.
37. *"Give the tragic bit to you, I've got the song"* — her setting her drink on the mirror's shelf and leaving it there, close-up.
38. *"There's a mirror on the landing, it doesn't say cruel"* — the same reflection framing as shot 17, identical lens and height.
39. *"It says girl who finally stopped bleeding for you"* — she holds her own eye contact this time with no push-in and no crown, static, held.

### Chorus 2 — from below

40. *"Tell it how you tell it, I'll allow it"* — low angle from the foot of the stairs looking up as she starts down, more saturated red.
41. *"Paint me in the red light, make it loud"* — the press line from behind her, a wall of lenses and flash, over-the-shoulder.
42. *"Every story needs a shadow at the party"* — the crowd from her eye level, parting, nobody meeting her eye, tracking.
43. *"And I wear it better than you wore the crown"* — the faceless man in the corner seeing her arrive and stopping mid-sentence, medium.
44. *"I'll be the villain in your story, the hero in mine"* — reuse the flash framing of shot 23, tighter, her chin fractionally higher.
45. *"Same girl, two books, and I'm fine with the line"* — the empty staircase behind her, still lit red, nobody on it, wide.
46. *"I'll be the villain in your story, the hero in mine"* — her walking into the crowd until it closes behind her, wide, holding into the break.

### Instrumental — the terrace, no lyrics

47. The whole room from a balcony above, everyone moving, nobody looking up, wide, red.
48. Her stepping out onto a stone terrace, the door closing on the sound behind her, tracking, red to blue.
49. A single drink set down on a stone balustrade and left there, macro, cold light.
50. The London rooftops over the balustrade, the city dark and awake, slow drift.
51. One bar of complete silence: her face in profile, the party a warm rectangle behind glass over her shoulder, static — the cut into the bridge.

### Bridge — the terrace, no red

52. *"Every story's got a narrator and it's you"* — her leaning on the balustrade with her back to the party, close-up, no red on her at all, cold blue.
53. *"Course I come out badly when you hold the pen"* — the only handheld drift in the video: a slow unsteady frame of her breathing out, close.
54. *"Stayed small and grateful, I'd be lovely in your book"* — a two-second flash of the plain blazer look sitting silently in a meeting, then black.
55. *"And I'd be sat here with nothing all over again"* — back on the terrace, her hands on cold stone, macro.
56. *"Write it. Print it. Put my name in bold."* — her looking back through the glass at the man still telling the story, medium, warm spill on one cheek.
57. *"Read worse about myself and slept just fine"* — her expression as she watches him: something close to sympathy, close-up, held.
58. *"Some of us are villains for an hour in one telling"* — the party through the glass, silent, all red, seen from the cold side, wide.
59. *"And the lead in every other, all of the time"* — she straightens up and turns back toward the door — the cut into the final chorus.

### Final chorus — back in, and out

60. *"Tell it how you tell it, I'll allow it"* — the terrace door opening and the red and the noise hitting her again, from inside, wide.
61. *"Paint me in the red light, make it loud"* — her walking back through the party without stopping for anyone, tracking, full red.
62. *"Every story needs a shadow on the staircase"* — the staircase behind her, empty, still lit, her shadow no longer on it, wide.
63. *"And I wear it better than you wore the crown"* — she passes the faceless man without turning her head, medium, one beat.
64. *"I'll be the villain in your story, the hero in mine"* — her collecting a long dark overcoat at the door, close-up on the hands.
65. *"Call me cold, call me clever, call it what you like"* — the coat going on over the gown in one movement, medium.
66. *"I'll be the villain in your story, the hero in mine"* — the front door opening onto a blue London street, the noise cutting off, locked-off from inside.

### Post-chorus — the street, on the snaps

67. *"Villain, villain, say it like a curse"* — a heel on wet pavement, macro, sodium light, one beat.
68. *"Been called a lot of things and villain isn't worse"* — a cab's orange light coming on down the street, one beat.
69. *"Villain, villain, in your telling of the night"* — the overcoat pulled closed at the throat, close-up, one beat.
70. *"Hero in mine, and I'm sleeping alright"* — her reflection walking level with her in a dark shop window, tracking, two beats.

### Outro — dawn

71. *"Black cab down the Strand and the city looking new"* — the back seat of a black cab going down the Strand, the sky lightening, her looking out.
72. *"Heels in my hand and the sky going blue"* — her barefoot on a bridge over the river, heels hooked on two fingers, the coat over the gown, medium.
73. *"Somewhere in your version I'm still doing the crime"* — a wide of the empty bridge and the city behind it, first gold on the buildings.
74. *"And I'm the hero in mine"* — final shot: her walking away from camera over the bridge into early sun, nobody else in frame, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the dress zip, the first red light on her face, the two-frame
crown, each *"the hero in mine"*, the first sixteenth of the rap verse, the
stop-dead look to camera, the instrumental, the terrace door, and the
barefoot bridge. At 98 BPM a bar is 2.45 s; the choruses cut on the bar, the
rap verse cuts on the sixteenths, and the post-chorus cuts on the snaps.

**The staircase challenge.** Post the vertical cut of chorus one (shots
19–25) with *"the hero in mine"* on screen and invite people to film one
slow walk down any stairs in red light, captioned with the worst thing
they have been called. The stop-dead look to camera (shot 35) is the second
shareable frame and the natural end of a fifteen-second cut.

## 6. Quality-control checklist

- Three looks in the right sections: black gown from shot 5 to shot 66, the plain blazer only in shots 10–12, 32 and 54, the coat and bare feet only from shot 65 on
- The ex is faceless in every appearance; no generation is kept where his jaw resolves
- The crown appears for two frames only, in the mirror, as chandelier light — never a prop, never a graphic, never worn
- Red is on her in every party shot and on none of the terrace shots; the bridge has no red at all
- Camera flashes are one-frame white pops added in the edit, deliberately out of rhythm with the music
- The rap verse is the only section cutting faster than a bar, and it stops dead at shot 35
- All documents, signage and press passes composited; no model-generated text anywhere
- She never hurries: no shot shows her walking faster than the shot before, including the final chorus
- The last shot is locked-off and holds until the audio fades
