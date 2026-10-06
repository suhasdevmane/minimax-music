# Wan 2.2 Shot List — "Hold My Hand in Public"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
104 BPM a bar is 2.31 s, so most shots are 3–5 s and the choruses cut on the
bar.

## 1. Visual world

Two visual registers, and the joke of the film is which one is real. The
**hidden life** is cold and architectural: stairwells, corners, corridors,
curbs, always with a gap of exactly one person between them. The **imagined
choruses** are golden, wide and slightly slowed, and they are shot like a
perfume commercial on purpose — because they are a fantasy, and the audience
should feel slightly embarrassed by how pretty they are. The final chorus,
when it actually happens, is deliberately **less** beautiful than the
fantasies: real Thursday light, real strangers, no grade. That reversal is
the whole film.

| Section | Grade | Camera |
|---|---|---|
| Intro | Gray-green stairwell, no warmth | Static, waiting |
| Verse 1 | Warm party light, she is always least lit | Handheld, split action |
| Pre-choruses | Flat afternoon daylight | Long observational holds |
| Choruses 1 and 2 | Golden, wide, slightly slowed — fantasy | Sweeping, moving |
| Verse 2 | Warm room, cold hallway, sodium in the car | Handheld, then static |
| Instrumental | Cool dawn into flat noon | Timelapse and long lenses |
| Bridge | Daylight from one side, half her face dark | Locked off, one subject |
| Final chorus | Real light, no grade, deliberately plainer | Handheld, at crowd level |
| Post-chorus / outro | Late gold, then warm kitchen | Following, then static |

## 2. Character bible — paste into every prompt

**Mahima** (the hidden months)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and tucked behind one ear, minimal makeup, wearing a slate-gray coat over a black top and dark jeans with white sneakers, composed guarded expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the birthday party, the worst night)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and styled, evening makeup with a dark lip, wearing a deep burgundy midi dress, polite fixed smile that does not reach her eyes, realistic cinematic photography, consistent identity

**Mahima** (the Thursday, the final chorus onward)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose, minimal makeup, wearing a cream sweater and light blue jeans with no coat, open easy expression, realistic cinematic photography, consistent identity

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a navy overcoat over a gray crew neck and dark trousers in the hidden scenes and just the gray crew neck on the Thursday, watchful expression that softens in the last act, realistic cinematic photography, consistent identity

**His mother** — a woman in her fifties, warm, opens a front door in the last
act. Filmed from the shoulder in the birthday handshake and given a full
clear face only when she opens the door.

**Party guests, market traders, the crossing crowd** — out of focus, cropped
or backs to camera. Nobody but Mahima, Kai and his mother gets a lit
close-up.

Objects: the **door keypad**, the **phone with the wrong contact name**, the
**group photograph**, the **coat over her arm**, the **crossing signal**, the
**front door**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every phone screen, the wrong contact name, the typed and deleted message,
the door keypad and the crossing signal are composited in the edit.**
Generate them as lit blank slabs and blank signal housings, then add the
interface in post — the model cannot render legible text, and the contact
name is the video's sharpest single frame.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai in his two with IP-Adapter or a
character LoRA; his mother needs a reference too, since she carries the
final beat. Keyframes first; Depth on the stairwell and corridor shots so
the architecture stays consistent across the film; OpenPose only for the
crossing sequence, where two people join hands inside a moving crowd and the
model will otherwise invent a third arm. 16:9 first; 9:16 for the crossing
and the two bookend photographs. Animate conservatively: a code being typed,
a phone lighting, a coat shifting on an arm, a crossing signal counting, a
door opening. The joined hands in shot 53 should be generated as a single
locked close-up rather than as part of a wider moving plate.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; the fantasy chorus shots run slightly long and slightly slow.

## 4. Scene per lyric line

### Intro — the mechanics of hiding

1. *"Six months of back stairs and the side of the building"* — Mahima (hidden look) on a concrete stairwell half-landing, back against the wall, phone in hand, not moving, one wired-glass window, static.
2. *"Six months of your car parked around the block"* — a navy car parked round a corner from a building entrance, seen from a first-floor window down a long lens, nobody in it yet.
3. *"I know the code to your door and the names of your sisters"* — macro on her fingers entering a code on a door keypad from memory, no hesitation (keypad composited).
4. *"And nobody knows mine"* — Mahima standing inside his hallway with the door closed behind her, alone in frame, cold light, held.

### Verse 1 — the logistics

5. *"You take the elevator, I take the stairs and count to twenty"* — split action: an elevator door closing on Kai, hard cut to Mahima going up a stairwell two steps at a time, counting under her breath.
6. *"We arrive at the same party like a coincidence"* — the same kitchen doorway twice, ninety seconds apart, the two of them greeting each other like acquaintances, matched framing.
7. *"There's a photograph of everybody in that kitchen"* — a group photo being taken on a phone, everyone leaning in, warm and loud, wide.
8. *"And I am the elbow at the edge of it"* — the resulting frame: Mahima cropped to a shoulder and an elbow at the very edge, freeze on it for a full beat.
9. *"I'm saved in your phone as somebody from work"* — extreme close-up of his phone face-up on a table, her name showing as something generic (composited), the video's sharpest frame.
10. *"Which is funny, because you don't work"* — Mahima seeing it from across the table and laughing genuinely, close-up, warm.
11. *"And I laughed the first time, honestly I did"* — the same phone in the same position three more times in fast cuts, same wrong name, the light cooling with each one.
12. *"But the joke has got a little older every month"* — her face in the last of those cuts, not laughing, the smile arriving a beat late, close-up.

### Pre-chorus 1 — the size of the ask

13. *"I don't need a ring, I don't need a speech"* — a couple holding hands at a bus stop doing nothing at all, shot plainly, given real time, wide.
14. *"Don't need your whole life rearranged"* — a second couple arguing cheerfully about a menu outside a restaurant, unremarkable, medium.
15. *"I just want to walk two blocks and be a person that you know"* — Mahima and Kai walking the same street with a gap of exactly one person between them, tracking from the side.
16. *"In the daylight, in front of people, with a name"* — the same walk from behind, the gap unchanged for the whole shot, held.

### Chorus 1 — the fantasy

17. *"Hold my hand in public"* — golden and slightly slowed: a pedestrian crossing full of people with two hands joined in the middle of it, wide, sweeping.
18. *"Let the whole street know"* — a market street, the two of them moving through it side by side, everything warm and blurred at the edges.
19. *"Not a message, not a maybe, not a coat on the back of a chair"* — a coat hung properly on a hook beside another coat, not over an arm, macro, golden.
20. *"Just your hand and my hand and the ordinary air"* — the joined hands at hip height moving through a crowd, close-up, slowed.
21. *"I don't want a secret, I want a front door"* — a front door opening from inside, light spilling out onto a step, wide.
22. *"I want to be the one you're walking in with, not the one before"* — a room turning to look as two people come in together, slowed, warm.
23. *"Hold my hand in public"* — a wide golden two-shot on a sunlit street, both laughing at nothing, over-pretty on purpose.
24. *"Let the whole street know"* — hard cut to reality: Mahima alone on the same street in flat grey afternoon light, no golden anything, static.

### Verse 2 — the birthday

25. *"Friday at your birthday you said, this is my friend"* — Mahima (party look) in a living room full of people, Kai's mouth forming an introduction, her face receiving the word and continuing to smile, close two-shot.
26. *"And I said it back and shook your mother's hand"* — a handshake with an older woman filmed from the woman's shoulder, warm on her side, medium.
27. *"I stood out in the hallway with a coat over my arm"* — Mahima in a hallway from behind, coat over her arm, the party audible through a doorway of warm light she is not in, static.
28. *"And I heard my own voice being polite from far away"* — her face in the hallway mirror, still smiling, the sound of the party dropping away in the mix, close-up.
29. *"Then I walked to the corner and I called myself a car"* — her walking to a street corner alone in a coat at night, a car pulling up, wide, sodium orange.
30. *"And you messaged me at midnight, are you mad"* — a phone lighting on her knee in a back seat (message composited), street light sliding across her face.
31. *"And I typed out a paragraph and sent a single word"* — extreme close-up: a long paragraph typed, then deleted down to one word, then sent (composited).
32. *"And I never felt so small in a room I helped set up"* — flashback, warm and bright: the same living room hours earlier, empty, Mahima on a chair hanging decorations alone. A written silent beat holds on this shot.

### Pre-chorus 2 — clarity

33. *"I don't need the whole world, I don't need a post"* — Mahima sitting on the edge of her bed in the coat she has not taken off, one lamp, static.
34. *"Don't need your friends to love me by the spring"* — the bus-stop couple again, briefly, now shot from much further away down a long lens.
35. *"I just want to stand beside you in a room with the lights on"* — her switching on the overhead light in her own flat and standing under it, wide.
36. *"And be a person, not a rumor, not a thing"* — her reflection in a dark window with the lamp behind her, close-up, half in shadow.

### Chorus 2 — the fantasy, colder

37. *"Hold my hand in public"* — the crossing shot again, now desaturated and slower, the golden gone out of it.
38. *"Let the whole street know"* — the market shot again, emptier, fewer people, same framing.
39. *"Not a message, not a maybe, not a coat on the back of a chair"* — the coat on the hook again, this time the second hook beside it is empty.
40. *"Just your hand and my hand and the ordinary air"* — the joined hands, but the shot is cropped tighter so neither face is in it.
41. *"I don't want a secret, I want a front door"* — the front door again, closed this time, nobody opening it.
42. *"I want to be the one you're walking in with, not the one before"* — the room turning to look, but the doorway is empty.
43. *"Hold my hand in public"* — the golden two-shot again, drained almost to grey.
44. *"Let the whole street know"* — hard cut back to her apartment, alone on the bed with the coat still on, static, the fantasy over earlier than last time.

### Instrumental — the city, indifferent

45. A pedestrian crossing filling and emptying with strangers, timelapse, cool dawn.
46. A market being set up in the dark, crates coming off a van, long lens.
47. The concrete stairwell with nobody in it, locked off, held six seconds.
48. Mahima walking one long block alone in flat noon daylight, tracking from the front, unbroken.
49. The navy car parked round the corner again with nobody in it — the cut into the bridge.

### Bridge — the doorway

50. *"It isn't about the street, it isn't about the photograph"* — Mahima standing in a doorway in her own flat, filmed straight on, not moving, daylight from one side, half her face dark.
51. *"It's that I have started making myself smaller in the door"* — the same shot continues; she does not move at all for the whole line.
52. *"I check the window before I laugh, I check the room before I lean"* — two two-second inserts: her glancing at a window before letting herself laugh; her checking a room before leaning toward him.
53. *"And a girl who used to take up space is holding still"* — a third insert: her physically stepping back from him half a pace, then hard cut back to the doorway.
54. *"So if you can't, then say you can't, and I will understand"* — the doorway shot, unchanged, her looking directly into the lens for the only time in the film.
55. *"But I am not shrinking anymore to fit inside a hand"* — the same frame, held through a written silent beat after the last word, no music, no movement.

### Final chorus — it happens

56. *"Hold my hand in public"* — a real pedestrian crossing, real strangers, real Thursday light, Mahima (Thursday look) and Kai waiting at the curb among a crowd, handheld at crowd level.
57. *"Let the whole street know"* — the crossing signal counting down (composited), then the crowd starting to move.
58. *"And you did, on a Thursday, on a crossing full of strangers"* — a locked close-up: his hand finding hers without ceremony, neither of them looking down at it.
59. *"With the light about to change and your fingers finding mine"* — her face as it registers, no big reaction, just a breath out, close-up.
60. *"I don't want a secret, I want a front door"* — a suburban front door, his knuckles knocking on it, macro.
61. *"And you knocked on your mother's and you said my name out loud"* — the door opening on his mother, his mouth saying a name, her face lighting up, medium three-shot.
62. *"Hold my hand in public"* — the two of them going in through the door, seen from the street behind them, wide.
63. *"Let the whole street know"* — the street outside the open door, an ordinary Thursday, nobody watching, static, held.

### Post-chorus — the long way home

64. *"Let the whole street know, let the whole street know"* — their hands still joined at hip height, walking, close-up.
65. *"Take the long way home and take it slow"* — a store window with both of them reflected in it, side by side, tracking.
66. *"Let the whole street know, let the whole street know"* — a street they have obviously never walked together, both looking around, wide.
67. *"It was never about the street, but let them know"* — the corner where his car used to hide, now empty, held.

### Outro — the bookend

68. *"Six months of back stairs, and then a Thursday in the sun"* — the concrete stairwell from shot 1, empty, unused, sunlight now reaching the half-landing.
69. *"Your car out at the front and both the windows down"* — the navy car parked directly in front of the building entrance with the windows down, matched to shot 2.
70. *"There's a photograph of everybody in that kitchen"* — another kitchen, another party, another group photo being taken, warm and loud, wide.
71. *"And I'm the one in the middle, and I've got a name"* — the resulting frame: Mahima in the middle of it, the flash going, then the room afterwards still full and moving, locked off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the keypad, the cropped group photo, the contact name, each
*"hold my hand in public"*, the word *friend*, the silent beat after the
decorations, the instrumental, the silent beat at the end of the bridge, the
hands joining, and the second group photo. At 104 BPM a bar is 2.31 s;
choruses cut on the bar, the fantasy shots run slightly long, and the two
written silences are held with no cut at all.

**The crossing challenge.** The shareable cut is shots 56–59, vertical, with
the signal counting down and *"hold my hand in public"* on screen. Invite
people to post the moment their hands join on a crossing. The second
shareable cut is shots 8 and 71 back to back: cropped out of the photograph,
then in the middle of it.

## 6. Quality-control checklist

- Three Mahima looks in the right sections: slate coat for the hidden months, burgundy dress only for shots 25–32, cream sweater and no coat from shot 56 onward and never before
- The fantasy choruses are visibly prettier than the real one — if the final chorus looks more cinematic than shots 17–23, the grade is wrong and the film does not work
- The one-person gap between them is exactly consistent in shots 15 and 16 and closes only at shot 58
- His mother's face is withheld in shot 26 and given fully in shot 61; no other party guest gets a lit close-up
- All phone screens, the contact name, the message, the keypad and the crossing signal composited in the edit; no model-generated text
- The two written silent beats (shots 32 and 55) hold with no cut and no camera movement
- No distorted hands in the keypad, phone, knuckles and joined-hands close-ups — shot 58 is the most important pair of hands in the video
- Shots 1 and 68, 2 and 69, 7/8 and 70/71 are framing matches; the last shot is locked off and holds through the fade
