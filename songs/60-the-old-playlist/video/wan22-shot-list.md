# Wan 2.2 Shot List — "The Old Playlist"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-one entries. Timestamps come from the rendered WAV; cut
on the sung line. At 88 BPM a bar is 2.73 s, so most shots run 3–5 s and the
choruses cut every bar and a half.

## 1. Visual style

One night bus, one journey, no cheating. The **present** is the upper deck of
a night bus in cold green-blue strip light with sodium orange rushing past the
glass. The **memories** are warm, grainy, slightly overexposed, shot as if on
8mm and cropped a touch tighter. The recurring device is the **aisle of
rooms**: in the choruses, each pair of bus seats becomes a different lit
memory, warm practicals inside a cold vehicle, so the bus itself never leaves
the frame. The only two shots with warm light on her present-day face are the
bridge and the final chorus. Handheld everywhere except the aisle tracking
shots, which are on a slider.

| Section | Grade | Camera |
|---|---|---|
| Intro | Cold green-blue interior, orange streaks | Wide, static, then phone macro |
| Verses (memory) | Warm, overexposed, 8mm grain | Handheld, loose |
| Verses (present) | Cold, flat, one overhead light | Static close-ups |
| Pre-choruses | Cold with the light dipping in the underpass | Slow push-in |
| Choruses | Aisle cold, seat-rooms warm and saturated | Slider tracking down the aisle |
| Instrumental | The coldest passage in the video, rain on glass | Slow, observational |
| Bridge | One warm practical over two seats, rest black | Locked-off two-shot |
| Final chorus | Interior finally reads gold, not green | Slider, wider, moving with her |
| Post-chorus | Phone glow dying to window light only | Macro, then close |
| Outro | Warm shop light on wet pavement | Steady, then a held wide |

## 2. Character bible — paste into every prompt

**Mahima** (present day, on the bus)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly flattened from a hood, no makeup, wearing a charcoal wool coat over a plain white tee, tired open expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (nineteen, in the memories and the bridge)
> Same female protagonist Mahima, young woman in her late teens, expressive dark eyes, oval face, long dark wavy hair with a blunt fringe she cut herself, smudged eyeliner, wearing an oversized borrowed indigo denim jacket over a band tee, bright unguarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (working the doubles)
> Same female protagonist Mahima, young woman in her late teens, expressive dark eyes, oval face, dark wavy hair pulled back under a plain work cap, no makeup, wearing a shapeless maroon fast-food polo with a grease stripe up the forearm, exhausted end-of-shift expression, realistic cinematic photography, consistent identity

**The boy who left** — faceless throughout: hands on a mug, a shoulder in a doorway, a rucksack strap. Never a clean face, never in the aisle-of-rooms shots.
> a young man in his late teens, face out of frame or cropped at the jaw, dark hair, olive canvas jacket

**The friends** — three young people in the car and on the stairwell, seen mid-laugh, faces allowed, never named, never repeated in the present.

Objects that recur: the **white wired earbuds**, the **cracked phone** with the
low-battery ring, the **borrowed indigo denim jacket**, the **paper world map**
on the bedroom ceiling, and the **stop-request button** she never presses.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, playlist names, track lists, waveforms, battery
percentages and bus signage are composited in the edit.** Generate the phone
as a lit blank rectangle in her hand and overlay the UI in post — the model
cannot render legible interfaces, and this video's whole ticking clock is a
battery number.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA; keep the
boy's reference deliberately faceless. Keyframes first; OpenPose for the
aisle walks and the bridge two-shot where both versions of her share a frame
(shoot the plate twice, lock the camera, composite); Depth for the bus
interiors, which are long and narrow and confuse the model without it. 16:9
first; 9:16 for the aisle-of-rooms cut and the reflection swap, which are
natural vertical content. Animate conservatively: a thumb on a screen, fog
spreading on glass, streetlights crossing a face, a jacket settling on a
shoulder.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s.

## 4. Scene per lyric line

### Intro — the last bus

1. *"Last bus out and the windows are sweating"* — wide from the back of an almost empty upper deck, Mahima alone six rows down, fogged windows, streetlights strobing across the ceiling, static, cold green-blue.
2. *"Twelve percent of battery to spare"* — macro on the cracked phone in her lap, a low-battery ring (composited), her thumb wiping the screen with her sleeve.
3. *"I push the old white earbuds in and settle"* — close-up of her pressing a white wired earbud in with one finger, shoulders dropping, head going back against the seat.
4. *"And a name I stopped saying is there"* — over-the-shoulder on the phone, the scroll slowing and stopping on one old playlist (composited), her face going still.

### Verse 1 — three tracks, three rooms

5. *"Track one is a summer of working the doubles"* — memory: a fast-food back kitchen at closing, Mahima in the work look wiping down a steel counter, fryer baskets up, warm sodium and grain, handheld.
6. *"Grease on my sleeve and the walk home at three"* — memory: her walking an empty road at night under sodium lights, the same white earbuds in, breath visible, tracking from the side.
7. *"Track two is a back seat with somebody's cousin"* — memory: interior of a car at night, three friends crammed in the back, one arm out the window, dashboard glow, handheld and loose.
8. *"All of us shouting the part we can't reach"* — memory: all four of them shouting one line at the roof of the car, badly and joyfully, faces open, hard cut on the beat.
9. *"Skip, and it lands on a blue kitchen table"* — memory, cooler: a blue formica kitchen table at night, two mugs, a boy's hands only, a rucksack already by the door, static.
10. *"A boy who was leaving before the leaves turned"* — present: extreme close-up of her thumb moving toward the skip arrow, hovering, not pressing, cold light.
11. *"I made this in a bedroom with a map on the ceiling"* — memory: her teenage bedroom from a low angle looking up, a paper world map taped across the ceiling, a laptop glow on her face, warm.
12. *"And a whole lot of nerve I hadn't earned"* — memory: nineteen-year-old Mahima lying on the duvet typing the playlist, mouthing along, one bare foot against the wall, handheld.

### Pre-chorus 1 — caught out

13. *"I only meant to check the time and get home"* — present: the lock screen and the time (composited), her eyes flicking to the window and back.
14. *"I did not mean to open up a door"* — her sitting up straighter, pressing the earbud in harder, a slow push-in on her face.
15. *"But the first four seconds hit me like a hallway"* — a one-second flash of an empty school corridor with the lights on and nobody in it, then hard cut back to the bus.
16. *"I have not walked down in three years or more"* — her fingertip drawing on the fogged glass and stopping halfway, the bus entering an underpass, the light dying and blooming back.

### Chorus 1 — the aisle of rooms

17. *"Hit shuffle on the old playlist and I'm nineteen again"* — the window reflection: present-day her in the glass, then a slow pan back to her seat and the reflection is nineteen, no cut, the hero shot of the video.
18. *"Cheap perfume, borrowed denim, the whole night to spend"* — match cut: the borrowed indigo denim jacket settling onto her shoulders over the wool coat, close-up on the collar.
19. *"Every song is a door I never got around to closing"* — slider tracking down the aisle: the first three pairs of seats are lit rooms, a bedroom, a stairwell, a kitchen, warm inside the cold bus.
20. *"Every chorus is a room with all the lights still glowing"* — she stands and walks the aisle, fingertips brushing the seat backs, the rooms holding steady as she passes, tracking ahead of her.
21. *"Nothing bad has happened yet inside a three-minute track"* — inside one seat-room: the four friends in the car, frozen mid-shout, her standing in the aisle watching them from outside the frame line.
22. *"I know how it ends, and I still want it back"* — her face in profile in the aisle, lit warm from one side by a room and cold from the other by the bus, slow push-in.
23. *"So let the window fog, let the long way be the plan"* — the stop-request button in the foreground, unpressed; behind it, the aisle of rooms still burning.
24. *"Hit shuffle on the old playlist and I'm nineteen again"* — she sits back down and the rooms snap off in sequence behind her, back to front, leaving cold blue, static wide.

### Verse 2 — the skipped track, the voice memo

25. *"Track eleven is the one I always used to skip"* — extreme close-up of her thumb resting beside the skip arrow, the nail tapping once, not pressing.
26. *"He was the only reason it was ever on the list"* — a two-second cold flash: the boy's hand lifting a mug off the blue table, no face, then black.
27. *"Tonight I let it play the whole way to the ending"* — the progress bar crossing the middle of the screen (composited), her face in the reflection above it, one overhead light, everything else dark.
28. *"And it's only a good song. That's the whole of what I missed"* — her eyebrow going up very slightly, a small exhale that is almost a laugh, close-up, held one beat too long.
29. *"There's a voice memo buried near the bottom of the album"* — the screen: a waveform among the track artwork (composited), her thumb hovering over it.
30. *"Somebody laughing, half a sentence, then it's gone"* — memory: three friends on a concrete stairwell under flat fluorescent, one starting a sentence, everyone laughing over the end of it, handheld, deliberately unglamorous.
31. *"I can't tell you what was funny anymore"* — present: her holding her breath through the silence at the end of the clip, the bus noise flooding back, static.
32. *"But I can tell you who I was when I put it on"* — the memory bedroom again, nineteen-year-old her recording the memo by accident, the phone face-up on the duvet, warm.

### Pre-chorus 2 — she misses her stop

33. *"I only meant to ride until my stop"* — the stop-request button, her hand rising toward it, close-up.
34. *"I did not mean to fall through thirty tracks"* — her actual stop sliding past the window behind her head, the shelter empty, she does not turn.
35. *"But a bassline from a song I half remember"* — her foot tapping the bassline against the metal seat frame, low angle, the vibration visible in the pole.
36. *"Hands me that whole summer, all of it, right back"* — streetlight rhythm speeding up across her face, the fog on the glass beginning to bloom orange.

### Chorus 2 — the rooms spill out

37. *"Hit shuffle on the old playlist and I'm nineteen again"* — reuse the reflection swap from shot 17, tighter, and this time she looks straight at the reflection.
38. *"Cheap perfume, borrowed denim, the whole night to spend"* — the denim jacket now fully on her, sleeves pushed up, present-day coat gone, close-up on her forearms.
39. *"Every song is a door I never got around to closing"* — the seat-rooms overflow into the aisle: a beach towel, a birthday cake with the candles lit, a wet festival field, a bedroom floor covered in clothes.
40. *"Every chorus is a room with all the lights still glowing"* — she walks faster now, the slider moving with her, objects brushing her legs, the light changing colour temperature every two steps.
41. *"Nothing bad has happened yet inside a three-minute track"* — one room that stops her: a hospital waiting-room chair with a coat over it, cold white, empty, the only cold room on the bus.
42. *"I know how it ends, and I still want it back"* — reuse shot 22 composition, the warm side of her face now much brighter than the cold side.
43. *"So let the window fog, let the long way be the plan"* — a wide from the front of the deck: the aisle lit all the way down, her small at the far end of it.
44. *"Hit shuffle on the old playlist and I'm nineteen again"* — every room goes out at once, hard, and she is back in her own seat mid-breath, static, cold.

### Instrumental — the bus, and only the bus

45. The driver's mirror: his eyes, the empty deck behind him, the bus rocking, static.
46. Rain starting on the glass, the reflected phone screen dimming behind the drops, macro rack focus.
47. A sleeping passenger on the lower deck, head against the window, bag clutched to his chest, wide.
48. Her own reflection in the black glass, present day, no costume change, no nineteen-year-old, held long.
49. Her hand wiping a clear circle in the fog and the city sliding through it, then the circle fogging over again.

### Bridge — two of her, one seat apart

50. *"I wouldn't go back, and I want that on the record"* — locked-off two-shot of her row, the seat beside her empty, one warm practical overhead, everything else black.
51. *"I like my life, I like my quiet, I like my bed"* — same frame, hard cut, and the nineteen-year-old is in the seat, headphones on, looking forward, not at her.
52. *"I only want five minutes on this bus beside her"* — present-day Mahima talking to the window rather than to the girl, her breath fogging the glass, profile.
53. *"Just enough to tell her what's ahead"* — the girl's hands in her lap, chewed nails, a friendship bracelet, macro, no face.
54. *"That it's going to cost her more than she has planned"* — the two of them in the same wide, both looking forward, neither speaking, held four seconds.
55. *"And she still gets there. Tired, but she lands"* — the girl turns her head for the first time. Cut before eye contact lands. Do not resolve it.

### Final chorus — gold, not green

56. *"Hit shuffle on the old playlist and I'm nineteen again"* — the interior now graded warm gold, Mahima standing in the aisle facing front, the rooms lighting up behind her, wide.
57. *"Cheap perfume, borrowed denim, the whole night to spend"* — she takes the denim jacket off and folds it over the seat back, unhurried, close-up.
58. *"Every song is a door I never got around to closing"* — the rooms slide past her now like stations rather than doors she has to enter, slider moving with her.
59. *"Every chorus is a room with all the lights still glowing"* — she looks into one room, the stairwell, smiles at it, and keeps walking, over-the-shoulder.
60. *"Nothing bad has happened yet inside a three-minute track"* — the hospital chair room from shot 41, now with the coat gone and the light warm, passing in one second.
61. *"I know how it ends, and I don't need it back"* — her face at the front window, gold light, eyes open, the road coming at her, slow push-in.
62. *"So let the window fog, let the driver make the bend"* — both versions of her at the front window watching the road, shoulder to shoulder, from behind.
63. *"Hit shuffle on the old playlist and I get to be her friend"* — same frame, same lens, one of them is gone and the frame is not empty, held.

### Post-chorus — one percent

64. *"Nineteen again, nineteen again"* — macro: the battery indicator dropping (composited), her cupping the phone with both hands as if that helps.
65. *"Two stops out and the battery's at one"* — her face lit only by the dying screen, eyes wide with a very small comic panic.
66. *"Nineteen again, nineteen again"* — the screen goes black mid-track, the earbuds go dead, ambient bus sound floods the mix, close-up.
67. *"Let it play, let it play till it's done"* — she leaves the dead earbuds in anyway, looking out at the street, lit only by the window, static.

### Outro — her stop, three late

68. *"Doors hiss open and the cold comes in"* — the doors folding open at the front, cold air visible against the warm interior, low wide from her seat.
69. *"Earbuds out, I put the old thing away"* — her winding the white cable around two fingers and dropping it in a coat pocket, close-up on the hands.
70. *"But I added one more song before I stood up"* — last screen shot: the old playlist with one new track added at the bottom (composited), then the phone goes into the pocket too.
71. *"Something from tonight, for whoever's listening one day"* — final shot: her stepping down onto a wet pavement under warm shop light and walking out of frame, the bus pulling away behind her and taking its light with it, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first vocal entrance, the reflection swap in shot 17, each
"nineteen again", the entry to the aisle of rooms, the instrumental, the
bridge cut where the second Mahima appears, "I don't need it back", the
battery dying, and the doors. At 88 BPM a bar is 2.73 s; the choruses cut on
every bar and a half, the verses on the line.

**The shareable cut** is shots 17–24, vertical: the reflection swap into the
aisle of rooms, with *"every chorus is a room with all the lights still
glowing"* on screen.

**The challenge — post the old playlist.** Screen-record your own oldest
playlist, scroll it slowly to the chorus, and cut on the hook. The prompt is
one line: which track do you always skip, and did you let it play tonight.
The battery-dying frame (shot 65) is the second shareable moment.

## 6. Quality-control checklist

- Three looks in the right sections: wool coat in the present, the work polo only in shots 5 and 6, the borrowed denim from shot 18 until she folds it away in shot 57
- The boy who left never has a visible face and never appears inside an aisle room
- Memory footage is warm, grainy and slightly overexposed; present footage is cold and clean, with the instrumental the coldest stretch in the video
- Every seat-room is a warm practical inside a cold vehicle, never a full-frame flashback — the bus must stay visible in the shot
- All screens, playlist names, waveforms and battery numbers composited; no model-generated text anywhere
- The two-Mahima frames in the bridge and shot 62 are locked-off composites of two plates, not a single generation
- The bridge does not resolve into eye contact; cut before it lands
- The last shot is locked-off, holds through the fade, and the bus light leaves before she does
