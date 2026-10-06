# Wan 2.2 Shot List — "The Hundredth Song"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
98 BPM a bar is 2.45 s, so most shots run 3–5 s; the choruses cut every bar
and the spoken-word section holds far longer than anything else in the
catalogue.

## 1. Visual world

Three worlds and one circle. The **rehearsal room** is where the video
starts and ends: bare, cold, one work light, an upright piano, a mic stand,
a cable loose on the floor and a door that will not close. The **stage**
grows across the video from a club riser to an arena, and it is the only
warm, gold, hazy world. Between them sit the **catalogue rooms** — two-second
visits to the worlds of the ninety-nine songs before this one, each kept in
its own grade so they read as other films cut into this one. The video's
shape is a closing circle: the cable in shot 1 and the cable in shot 68 are
the same cable in different rooms, and the last frame has nobody in it.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cold overhead work light, unstaged, slight green in the shadows | Static macro and close-ups |
| Verse 1 | Cold blue corridor, each doorway warm and saturated | Slow tracking behind her |
| Pre-chorus 1 | First warm light creeping in from behind | Slow rise, backlit |
| Chorus 1 | Gold and deep amber, hard backlight, haze in the beams | Wide, craning, one held close-up |
| Verse 2 | Grey afternoon daylight, dust, no colour | Static, seated, unhurried |
| Pre-chorus 2 | Near black, one white spot, crowd in silhouette | Slow push |
| Chorus 2 | The stage gold intercut with the catalogue rooms, each in its own grade | Hard cuts, one per line |
| Instrumental | Single-source hard light, then flat house light, then one lamp | Locked-off, then handheld, then still |
| Bridge | One buzzing strip light, hard shadows, concrete | Static, close |
| Spoken word | Half house light, low front wash, tape-hiss texture | One long push-in, one-beat cutaways |
| Final chorus | A full stop brighter, warm white and gold, confetti in the beams | Craning, wide, moving |
| Post-chorus | Warm, cooling a step per line | Alternating close-ups |
| Outro | Back to the cold work light of shot 1 | Locked-off, long holds |

## 2. Character bible — paste into every prompt

**Mahima** (rehearsal room — intro, verse 1, bridge, outro)

> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slightly messy, no makeup, wearing an oversized cream knit cardigan over a black vest and dark jeans, thick socks and no shoes, tired focused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the stage — every chorus, both pre-choruses, the final chorus)

> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a deep wave, defined stage makeup with a matte dark lip, wearing a black silk shirt untucked over black tailored trousers and boots, open exhilarated expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the nine-person back room, verse 2 flashback)

> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back in a low knot, no makeup, wearing a plain white t-shirt and a denim jacket, absolutely committed expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the male lead, one look for the whole video)

> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a faded black work shirt with the sleeves rolled and dark jeans, a coil of cable over one shoulder in the daytime shots, steady unhurried expression, realistic cinematic photography, consistent identity

**The woman in the hallway** (bridge) — never shown clearly: filmed from
behind, a coat and a shoulder, her face out of frame the entire time.

> a woman in her fifties seen only from behind, dark wool coat, grey hair pinned up, no face visible

Objects: the **loose XLR cable** on the floor, the **borrowed microphone**
and its clip, the **door wedged half open**, the **single folding chair**
placed at the front, the **wall of set lists** backstage, the **road case**
Kai sits on, the **nine empty chairs** in the back room, the **one working
light** on the empty stage.

Everyone else — band, crew, choir, audience — is background. No other named
character appears, and nobody in the crowd is ever held long enough to
become a character.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All set lists, tour posters, departure boards, phone screens and the wall
of paper backstage are composited in the edit.** Generate them as blank
paper, blank boards and lit blank screens; the model cannot render legible
print, and none of it needs to be readable — the set-list wall only has to
read as a hundred sheets of paper.

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

For this song specifically: the crowd is the hard problem. Never generate a
full arena as one plate — build the crowd as a dark silhouette foreground
layer plus a mid-ground of ten to fifteen people and let the haze and the
backlight do the rest, or the model will produce fused faces by the hundred.
Depth on every stage wide. The catalogue-room cutaways in chorus 2 and the
spoken word are two-second single-move clips and should be generated at the
shortest frame count; they are quotations, not scenes. The modulation hit at
shot 57 is a light change on a locked-off camera, so generate it as one
still lit two ways and cross-dissolve in the edit rather than asking the
model to animate a rig. The 9:16 recomposition is for the final chorus and
the spoken-word section.

## 4. Scene per lyric line

### Intro — the rehearsal room

1. *"It started in a room with a borrowed microphone,"* — extreme close-up, macro: a hand pushing an XLR plug into the base of a microphone until it clicks, cold overhead work light, static.
2. *"A cable on the floor and a door that wouldn't close."* — the cable running loose across bare floorboards to a door wedged half open on a dark corridor, low angle along the floor, static.
3. *"I had no plan, I had a hundred things to say,"* — Mahima (rehearsal look) sitting on a folding chair with the mic stand at her knee, looking at it and not singing yet, wide, unstaged.
4. *"And I've said ninety-nine of them, so here goes."* — her leaning in until her mouth is almost on the microphone and breathing in, extreme close-up, the room tone audible, static.

### Verse 1 — the corridor of doorways

5. *"There's a girl in the first one learning how to leave,"* — a long backstage corridor, cold blue, Mahima walking away from camera; the first doorway she passes is a rain-lit window at night, warm and saturated for two seconds, tracking behind her.
6. *"And a girl in the fortieth still learning how to stay."* — the next doorway: a small kitchen with a string of fairy lights and two people barely moving in socks, held two seconds, then gone as she walks past.
7. *"There were kitchens and taxis and a bus at six,"* — three doorways in quick succession on the beat: a taxi back seat with the window down, a night bus with a forehead against the glass, a bus stop in early light.
8. *"And every one of them was somebody's whole day."* — her hand trailing along the corridor wall and touching each door frame as she passes, close-up on the hand, the warm light from each room crossing her fingers.
9. *"I sang about a summer like it was a person,"* — a two-second flash of a festival field at dusk, then a hard cut back to her face in the cold corridor, still walking.
10. *"I sang about a doorway I was frightened to walk out."* — she stops at one dark doorway that has no world in it, only black, and looks into it, medium, static.
11. *"I gave away my worst night so yours would feel smaller,"* — back in the rehearsal room, her at the microphone, eyes closed, the work light hard across one cheek, extreme close-up.
12. *"And that's how you put a heavy thing down."* — her shoulders dropping on the line, a real exhale, the mic stand tilting a fraction under her hand, close-up, static.

### Pre-chorus 1 — the room fills

13. *"The last note of a song isn't an ending,"* — the rehearsal room in wide: a cellist walking in and sitting down behind her without a word, static.
14. *"It's the room going quiet enough to hear."* — the wedged door and the dark corridor beyond it, absolutely still, the room tone dropping out, held.
15. *"If you came in late, if you only know the one,"* — a single folding chair being carried into the front row of a dark hall and set down, tracking with the chair, the first warm light in the video.
16. *"Pull a chair to the front, we're nearly there."* — behind her: a rack of stage lights coming up one at a time in a slow rise, her still unlit, silhouette against them.

### Chorus 1 — the stage

17. *"This is the hundredth song, and I'm still singing,"* — hard cut to a full stage mid-show, Mahima (stage look) at the front with her arms open, gold backlight and haze, crane pulling back.
18. *"Same two hands, same crack in the same high note."* — her two hands on the microphone in exactly the grip of shot 1, extreme close-up, the same hands in a different life.
19. *"Ninety-nine goodbyes, a hundred ways to begin,"* — her face held straight through the crack in the high note, no cutaway, no flattering angle, close-up.
20. *"And a voice you carried further than I could alone."* — a wide from the back of the hall over a dark sea of raised arms, her small and lit at the end of it, static.
21. *"Sing the part you know, I'll hold the rest,"* — she pulls the microphone off her own mouth and points it out at the room, and the room sings, medium, the vocal audibly thinner.
22. *"This is the hundredth song, and I'm still singing."* — Kai at the side of the stage under the hook, singing beneath her rather than beside her, half in shadow, medium.

### Verse 2 — Kai, afternoon, before doors

23. *"I came in on a verse, I was only meant to stay,"* — the same stage in grey afternoon daylight, empty, Kai sitting on a road case with a bass across his knee, coiling cable with one hand, wide, static.
24. *"Then a hundred rooms went by and I never left the floor."* — his boots on the stage floor, gaffer tape marks layered a hundred deep in a hundred colours, macro, slow tilt up.
25. *"I've watched a stadium learn a private thing by heart"* — his POV from the wing: her small in the middle of a huge lit room, the crowd's mouths moving in time, long lens.
26. *"And hand it back to her a little louder than before."* — reverse: her face on stage hearing it come back, her mouth stopping, close-up, gold.
27. *"Some nights the sound was awful and the crowd was nine,"* — a tiny back room above a pub, nine chairs, four of them empty, a beer sign on the wall, wide, ugly practical light.
28. *"And she sang it like the room was gold, and made it true."* — Mahima (back-room look) singing at total commitment to nine people, sweat at her hairline, the lamp making the room amber, medium close-up.
29. *"That's the whole trick, if anybody asks,"* — back to Kai on the road case in the grey afternoon, talking flat to camera, no music in his face, static.
30. *"You sing the small ones like they matter, and they do."* — the back room again: one man at the back who has stopped drinking to listen, filmed over his shoulder toward her, close-up.

### Pre-chorus 2 — both, the held silence

31. *"The last note of a song isn't an ending,"* — the two of them side by side at one microphone in a near-dark arena, one white spot, medium two-shot.
32. *"It's the sound of a room breathing in the dark."* — the crowd in total silhouette, no light on any face, absolutely still, wide, held longer than any chorus shot.
33. *"If you came in late, if you only know the one,"* — the single folding chair from shot 15, now in the front row of the full arena, someone finally sitting in it, low angle.
34. *"That's enough, that was always enough to start."* — a slow inhale of noise from the crowd, the silhouette beginning to move, the spot widening, slow push.

### Chorus 2 — the song leaves her hands

35. *"This is the hundredth song, and I'm still singing,"* — reuse shot 17's angle, wider, the choir now visible walking on behind the band.
36. *"Same two hands, same crack in the same high note."* — a kitchen with string lights, two people slow-dancing in socks, singing the hook at each other, warm, handheld, two seconds.
37. *"Ninety-nine goodbyes, a hundred ways to begin,"* — a festival field at dusk from a drone, a hundred thousand arms up on the beat, saturated, wide.
38. *"And a voice you carried further than I could alone."* — a taxi at night with the window down and the driver singing it badly, phone in the cradle with a lit blank screen, close-up.
39. *"Sing the part you know, I'll hold the rest,"* — a night bus, one pair of headphones, a forehead against the glass and lips moving, passing lights, close-up.
40. *"This is the hundredth song, and I'm still singing."* — an airport gate at four in the morning, a row of empty seats, one person asleep across three of them with an earbud in, cold fluorescent, static.

### Instrumental — the years, in objects and rooms

41. The cellist alone in a single hard pool of light on the otherwise black stage, bow moving, the rest of the band gone, locked-off, long.
42. A backstage wall covered in a hundred taped-up set lists, blank paper (composited), a slow drift along it, some sheets curled, some new.
43. Time-lapse handheld: a crew striking a stage and building the same stage again, the truss going down and up, night into day into night.
44. Mahima from behind, walking out into the middle of an empty stage in flat daylight with nobody in the room, house lights up and unglamorous, wide, static.
45. The timpani hit and the suspended cymbal, then everything falling away: one held string note over one held frame of the mic stand alone, the light dropping to a single lamp — the cut into the bridge.

### Bridge — the woman in the hallway

46. *"I used to think the point of this was being heard,"* — a concrete corridor outside a dressing room, one buzzing strip light, Mahima (rehearsal look) with a coat over her stage clothes, static, hard shadows.
47. *"Then a woman in a hallway said, that one got me through."* — the woman filmed entirely from behind, a dark wool coat, saying something short; the audio drops to nothing but room tone, over-the-shoulder.
48. *"I've never written anything as useful as that sentence,"* — Mahima's face receiving it, no performance in it at all, extreme close-up, the strip light buzzing.
49. *"So I keep the microphone and I keep making room."* — the woman gone down the corridor and out of frame, Mahima still standing in the same spot after, wide, held.

### Spoken word — Kai, half house light, the room silent

50. *"Ninety-nine of these. Think about that."* — Kai alone at centre stage, house lights half up so the whole room is visible and unglamorous, a very slow push-in from the back of the hall, no cuts.
51. *"Ninety-nine nights somebody played one on the wrong side of a hard week."* — a bedroom ceiling at three in the morning, a phone face-down beside a hand, one lamp on, static, held.
52. *"Ninety-nine kitchens, airports, back seats, bus stops."* — four cutaways, one beat each, hard cut: a kitchen tap running, a departure board (composited blank), a back seat with a seatbelt across a chest, a bus stop in rain.
53. *"She didn't write a hundred songs. She wrote one song a hundred times,"* — the push-in on Kai continuing, now at medium, the crowd's faces in the spill behind him not moving at all.
54. *"And everyone who heard it was certain it was theirs."* — a slow lateral track along the front row: five faces, each lit only by stage spill, each one completely still, each one clearly somewhere else.
55. *"That is not a career. That is a promise kept."* — Kai in close-up, unraised, one hand not on the mic, the tape-hiss grade at its heaviest, static.
56. *"So here it is, the last one, which is a funny way of saying the next one."* — he steps back off the mic and looks stage left toward the wings, where a strip of white light is showing under a door, medium, held into the modulation.

### Final chorus — the key change

57. *"This is the hundredth song, and I'm still singing,"* — the modulation: every light in the rig hitting at once on the downbeat, locked-off wide of the whole stage, the grade a full stop brighter than anything before it.
58. *"Same two hands, same crack in the same high note."* — the two of them shoulder to shoulder at the front of the stage singing in octaves, confetti crossing the beams, crane in.
59. *"A hundred ways of leaving, a hundred coming home,"* — the choir behind the band at full voice, twenty faces, warm white, slow lateral track.
60. *"And a voice that was never only mine to hold."* — she stops singing entirely and lets the room carry the line, her hands off the microphone, close-up on her face listening.
61. *"Take the part you love, leave the rest behind,"* — the crowd from the stage, front to back, arms and streamers and haze, the widest frame in the catalogue.
62. *"This is the hundredth song, and I'm still singing."* — reuse shot 18's framing on her two hands on the microphone, now gold and confetti-lit, the same grip a third time.

### Post-chorus — trading, half-time

63. *"Still singing, still here, still yours,"* — her line: close-up on Mahima, half-time, the rig cooling a step, warm.
64. *"Still finding new ways to say the same true thing."* — his line: close-up on Kai, cut on the trade, matched framing.
65. *"Still singing, still here, still ours,"* — her line again, but pulled back to a two-shot with him in it now, both mouths moving.
66. *"A hundred is a doorway, not a wall."* — a slow push toward the wings: an actual doorway at the side of the stage with white light coming through it, nobody in it yet, the rig dimming behind.

### Outro — the empty stage

67. *"An empty stage, one light, a microphone still warm,"* — the hall after: house lights off, crew gone, seats empty, one working light on a stand at centre stage, wide, cold, locked-off.
68. *"And a cable on the floor where all of it began."* — the same loose XLR cable as shot 2 running across the stage floor, a different room and the same cable, low angle, macro at the plug.
69. *"Whoever picks it up next, I hope the room is loud,"* — a hand laying the microphone back into its clip on the stand and letting go, extreme close-up, then the hand leaving frame.
70. *"This is the hundredth song, and I'm still singing."* — final shot: the empty stage, one working light, one microphone in its clip, the cable on the floor, nobody in frame, locked-off, hold through the fade and two seconds past it. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, each "this is the hundredth song", the
first stage cut at shot 17, the crowd taking the line at shot 21, the drop
into the near-dark at shot 32, the top and the collapse of the instrumental,
the woman's line at shot 47, the first word of the spoken section, the
modulation downbeat at shot 57, the doorway at shot 66, and the last "still
singing." At 98 BPM a bar is 2.45 s; choruses cut every bar, verse 2 and the
bridge hold three to four bars, and the spoken-word section is edited to the
sentence rather than the bar.

**The hundred challenge.** The spoken-word section is the shareable cut. Post
shots 50–56 vertical, with *"she wrote one song a hundred times"* on screen,
and invite people to post the one song of the hundred that got them through,
cutting on the count of ninety-nine. The modulation at shot 57 is the second
shareable frame — one second, the whole rig hitting — and the empty stage at
shot 70 is the end-card for the whole campaign, posted silent with no text.

## 6. Quality-control checklist

- Three Mahima looks in the right sections: rehearsal room for the intro, verse 1, the bridge and the outro; stage look for every chorus and pre-chorus; back-room look only in shots 28 and 30
- Kai has one look throughout; the coil of cable is on his shoulder only in the daytime shots 23 and 29
- The woman in the hallway never shows her face, and no crowd face is held long enough to become a character
- All set lists, boards and screens are composited; no model-generated print
- The catalogue-room cutaways (shots 5–9, 36–40, 52) are each in their own grade and never longer than two seconds, so they read as quotations from other videos and not as this one
- The circle closes: the cable in shot 2 matches the cable in shot 68, the hand grip in shot 18 matches shot 1 and shot 62, and the cold work light of the intro is the light of the outro
- The crack in the high note (shot 19) is not cut away from and not prettified
- The modulation at shot 57 is a light change on a locked-off frame, cross-dissolved, not an animated rig
- The last shot has no people in it, is locked-off, and holds two seconds past the audio fade
