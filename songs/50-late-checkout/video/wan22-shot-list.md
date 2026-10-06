# Wan 2.2 Shot List — "Late Checkout"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
100 BPM a bar is 2.4 s, so most shots are 4–6 s and nothing in this video is
cut fast.

## 1. Visual style

One hotel room, one balcony, one morning, and **the light is the clock**. The
video opens with hard bars of shutter light lying across the floor at eleven,
and over its length that light climbs the wall until, in the last section, the
shutters close and the room is in shade for the only time. Nothing is graded
tropical-postcard: the sea is blown out and white, the shade is genuinely
dark, and the colour comes from wood, tile, salt and skin. The camera is slow.
There are no whip pans, no drone spins and no fast cuts anywhere in this
video. The only cold, flat, blue frames are the two inserts of the life
waiting at home.

| Section | Grade | Camera |
|---|---|---|
| Intro | High-contrast white sun, deep interior shade | Static, macro on light bars |
| Verse 1 | Warm interior, one hard stripe per object | Slow macro inserts, from directly below |
| Pre-chorus | Warm lamp side, cool window side | Close on hands, over-the-shoulder |
| Choruses | Blown-out sea, brightest the room gets | Slow lateral tracks, wide balcony two-shots |
| Post-chorus | Flat bright, no drama | Two lazy macro cuts |
| Verse 2 | Warm room, two cold grey inserts | Static two-shot on the bed |
| Instrumental | Light climbing the wall | Static objects, one wide |
| Bridge | Deep shade against a blown-out sea | Static, low, on the balcony floor |
| Final chorus | High hard midday sun, hot stone | Handheld running, macro feet |
| Outro | Clean natural, then shade | Macro, then locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the whole morning)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and sea-textured with a faint tan line at her shoulders, no makeup, wearing a white cotton slip dress over a swimsuit and a thin gold chain, unhurried contented expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (outro, travelling)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back, no makeup, wearing a plain linen shirt over the slip dress with a canvas bag on her shoulder, calm slightly wistful expression, realistic cinematic photography, consistent identity

**Kai** (the male lead)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, sun-darkened, wearing a loose open linen shirt over swim shorts, barefoot, easy relaxed expression, realistic cinematic photography, consistent identity

**The woman at the front desk** — heard on the phone, seen once at the very
end behind the reception counter.
> a woman in her fifties, hair pinned up, a hotel polo shirt, reading glasses on a chain, kind unhurried expression

Objects that must stay consistent: the **shell on the nightstand**, the
**shirt with a salt tidemark** over the chair, the **open suitcase** with
nothing folded in it, the **damp towel on the balcony rail**, the **old hotel
telephone**, the two **coffee cups** that go cold, the **key card**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, the laptop inbox, the room number, the key card and any hotel
signage are composited in the edit.** Generate the laptop as a lit blank
rectangle and the key card as a blank white card; the model cannot render
legible text and this video has three close-ups where text would be the
subject.

Keep this PG throughout: the two leads are affectionate and easy with each
other, but the video is about a room, a clock and a phone call. No bedroom
staging beyond two people sitting on the end of a made bed.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA. **The
shutter light is the continuity problem in this video**: build one lighting
setup for the room and generate every interior shot from stills that place the
light bars at the correct height for their section — floor, low wall, high
wall, gone. Do not let the model choose. Depth for the room and balcony
compositions so the sea sits correctly beyond the rail. OpenPose only for the
running-to-the-water shots. Animate very conservatively: a fan turning, a
towel moving in wind, a hand lifting off a counter, steam off a cup. 16:9
first; 9:16 recomposition for the phone call and the celebration on the bed,
which are the vertical clips.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 4–6 s; nothing under 2 s anywhere in this video.

## 4. Scene per lyric line

### Intro — eleven o'clock

1. *"Eleven in the morning and the light comes through the slats"* — hard bars of light through wooden shutter slats lying across a tiled floor, dust moving in them, static macro.
2. *"Falls across the floor and stops right where your bag is"* — the same bars reaching the edge of a packed holdall by the door and stopping there, slow push-in.
3. *"And the sea is doing what it always does"* — through the shutter gap: a blown-out white sea, moving, indifferent, static wide.

### Verse 1 — the room at the end of a week

4. *"The fan is still turning and the room is still warm"* — a ceiling fan turning slowly, shot from directly below, the blades cutting the shutter light.
5. *"There's a shell on the nightstand from the second day"* — a shell beside an old hotel telephone on the nightstand, macro, one hard stripe of light across it.
6. *"Your shirt is on the chair with the salt still in it"* — a linen shirt over the back of a chair with a white tidemark of salt on the collar, macro.
7. *"And my case has been open since we got here anyway"* — an open suitcase on a luggage rack with nothing folded in it, a week of clothes, static.
8. *"The towel on the rail has not dried out all week"* — a damp towel on a balcony rail moving slightly in the wind, the blown-out sea behind it out of focus.
9. *"And the sea keeps on saying the same thing to me"* — Mahima at the balcony door with a coffee, looking out, not going out, medium from behind.

### Pre-chorus 1 — the phone call

10. *"There's a number by the bed for the front desk"* — the hotel telephone on the nightstand with a small card propped beside it (blank; composited), her hand next to it and not on it.
11. *"And your hand on my back saying, go on, ask"* — Kai's hand flat on her back, one small push, seen from behind her, close.
12. *"It's a small thing to want and a small thing to say"* — her looking at the phone the way you look at a much larger problem, close-up, half a smile.
13. *"So I picked it up and asked her if we could stay"* — the handset lifted, her sitting down on the bed with it, the coiled cord straightening, wide.

### Chorus 1 — the room, alive

14. *"Give me a late checkout, one more hour of you"* — the shutters pushed fully open, the room flooding with white light and sea noise, wide, the brightest frame so far.
15. *"Sun on the sheets and the sea coming through"* — sun landing on a rumpled bed, the curtain moving, the sea audible, slow lateral track.
16. *"I will pay for the hour, I will pay for the day"* — her going through a purse on the desk, entirely unserious about it, medium.
17. *"Anything to keep the eleven o'clock away"* — a small travel clock turned face-down on the nightstand, macro.
18. *"Give me a late checkout, let the coffee go cold"* — two coffee cups on the balcony rail, untouched, steam long gone, macro.
19. *"Leave the shutters wide and the suitcase in the hall"* — the suitcase pushed out of the frame with a bare foot, still open, wide.
20. *"There's a plane with our names on it, I know, I know"* — a plane crossing very high above the balcony, both of them not looking at it, wide from below.
21. *"Give me a late checkout before we have to go"* — the two of them on the balcony talking, no urgency at all, wide two-shot with the sea behind.

### Post-chorus 1 — half spoken

22. *"One more hour, one more hour"* — a coffee cup with a full skin on it, macro, flat bright light.
23. *"Everything else can wait downstairs"* — the packed holdall by the door, untouched, and the room key on top of it, static.

### Verse 2 — the world outside the room

24. *"The woman at the desk said that she'd have to go and check"* — the two of them sat on the end of the bed, side by side, the phone between them on speaker, looking at the floor.
25. *"And we sat down on the end of the bed like it was a test"* — the same shot tighter, both of them absolutely still, the fan turning behind them.
26. *"I know there's an inbox with a hundred things unread"* — a cold grey insert, two seconds: a laptop inbox in an office (composited), rain on a window behind it.
27. *"And a coat in a closet in a city where it's wet"* — a cold grey insert: a heavy winter coat on the back of a door in a dim flat, static.
28. *"I know the girl who gets off that plane tomorrow morning"* — back to warm: her face while she waits, close-up, the sea the only sound.
29. *"Is careful and quiet and busy again by ten"* — her eyes moving, thinking about a Monday, the shutter light now higher up the wall behind her.
30. *"Then the phone clicked back on and she said we've got till two"* — both of them reacting at once, undignified, delighted, a small celebration on the end of a bed.
31. *"And I have never loved a stranger like I loved her then"* — her holding the handset with both hands and saying thank you to it, close-up, laughing.

### Pre-chorus 2 — the comic repeat

32. *"There's a number by the bed for the front desk"* — her hand going back to the telephone, macro, deliberate.
33. *"And your hand on my back saying, ask her again"* — Kai with a hand over his eyes, laughing, shaking his head, medium.
34. *"It's a small thing to want and a small thing to say"* — the two of them arguing happily about whether she can push it to three, no sound needed.
35. *"So I picked it up and asked her if we could stay"* — the handset lifted again, her sitting on the floor with her back to the bed this time, wide.

### Chorus 2 — the hour they bought

36. *"Give me a late checkout, one more hour of you"* — a slow lateral track along the balcony: two chairs, two cups, the sea, both of them, nothing happening.
37. *"Sun on the sheets and the sea coming through"* — the bed with the light bars now across the pillows instead of the floor, static.
38. *"I will pay for the hour, I will pay for the day"* — coins and a folded note left on the desk under the clock, macro.
39. *"Anything to keep the eleven o'clock away"* — the shadow of the balcony rail on the tiles, visibly shorter than it was, static.
40. *"Give me a late checkout, let the coffee go cold"* — a third coffee made and put down and forgotten in the same shot, macro.
41. *"Leave the shutters wide and the suitcase in the hall"* — the open suitcase in the doorway with a foot resting on it, wide.
42. *"There's a plane with our names on it, I know, I know"* — two boarding passes face-down on the desk (blank; composited), her turning them over and turning them back.
43. *"Give me a late checkout before we have to go"* — both of them lying across the bed sideways with their feet on the floor, looking at the ceiling fan, overhead.

### Instrumental — the room emptying

44. A shirt folded properly for the first time all week and laid into the case, macro, slow.
45. The shell picked up off the nightstand, considered, and put into a side pocket of the case.
46. The towel taken off the balcony rail, still damp, folded over an arm.
47. The ceiling fan slowing to a stop after the switch goes off, from directly below.
48. A wide of the room made neutral again, bed straightened, light bars now high on the wall.

### Bridge — the balcony floor

49. *"I'm not asking for forever, I'm just asking for an hour"* — the two of them sat on the balcony floor with their backs to the wall, shoulders touching, looking out through the railings.
50. *"But if the two of us out here on this balcony"* — her face in profile, deep shade, the blown-out sea beyond, saying it to the water rather than to him.
51. *"Can make it to the airport, we can make it through the rest"* — his hand finding hers on the tile between them, macro, no faces.
52. *"So give me sixty minutes and a door we haven't shut"* — the open room door behind them seen through the balcony doorway, the corridor beyond it, static.
53. *"And I'll go quietly, I promise, when it's up"* — both of them standing up, brushing off, the frame holding on the empty patch of tile where they were sitting.

### Final chorus — the last hour, used

54. *"Give me a late checkout, one more hour of you"* — the two of them going down the hotel steps toward the water in their clothes, running the last few, handheld.
55. *"Sun on the sheets and the sea coming through"* — the sea from the water's edge, hard midday light, both of them walking straight in up to their knees.
56. *"She gave us until two and she did not have to"* — wet feet on hot stone coming back up the steps, macro, prints drying behind them.
57. *"And I'm spending all of it right here with you"* — the two of them dripping in the corridor, laughing, trying to be quiet, wide.
58. *"Give me a late checkout, let the coffee go cold"* — the cold coffee cups collected and stacked by the door, macro.
59. *"Leave the shutters wide and the suitcase in the hall"* — the suitcase finally closed and set upright in the hall, static.
60. *"There's a plane with our names on it, I know, I know"* — her looking around the room one more time from the doorway, medium.
61. *"Give me a late checkout before we have to go"* — the shutters pulled closed, the light bars vanishing, the room in shade for the first time in the video.

### Post-chorus 2 — done

62. *"One more hour, one more hour"* — two cases by the closed door, the room dark and made, static.
63. *"Everything else can wait downstairs"* — the balcony seen from inside through closed shutter slats, thin lines of sea, static.

### Outro — leaving

64. *"Key card on the counter and the door clicks shut"* — a key card set down on a reception counter, a hand lifting away, the woman from the desk taking it, macro then medium.
65. *"The sea is still going and it doesn't know we left"* — the room door swinging shut on an empty made bed, from inside, the frame going dark.
66. *"Somewhere over water I'll be holding on to your hand"* — an aeroplane window with sea underneath it, her hand and his on the armrest between the seats, close.
67. *"Still asking anybody for a late checkout"* — final shot: the empty balcony from outside, the towel gone, the rail bare, the sea still going, locked-off and held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first shutter bar, the handset lifted, each *"give me a late
checkout"*, the two cold inserts, the answer at shot 30, the balcony floor,
the run to the water, the shutters closing, and the key card. At 100 BPM a bar
is 2.4 s; the choruses cut on the two-bar phrase and nothing in this video
cuts faster than the beat.

**The late-checkout challenge.** Shots 24–31 are the shareable unit: two
people on the end of a bed waiting on hold, then the reaction when the front
desk says yes. Everybody has made that call. Post it vertical with the hook on
screen. Second clip: shots 1–3, the shutter light and the bag, with the first
line — it is the whole feeling of the last day of a holiday in nine seconds.

**Caption:** *"I'm not asking for forever, I'm just asking for an hour."*

## 6. Quality-control checklist

- The shutter light climbs: on the floor for shots 1–13, across the bed for 36–43, high on the wall by 48, and gone from 61 onward. No shot puts it back where it was.
- Mahima is in the white slip dress for shots 4–63 and the linen shirt look only from 64; Kai is barefoot in every shot until the corridor.
- The shell, the salt-marked shirt, the open suitcase, the damp towel, the hotel telephone and the two coffee cups are identical wherever they recur, and each one is packed or removed exactly once.
- Only two frames in the video are cold and grey, shots 26 and 27, and they are the only rain in it.
- No readable text anywhere: the laptop, the boarding passes, the card by the phone and the key card are all composited.
- The pace never breaks: no shot is under two seconds and there are no whip pans or drone moves.
- The two leads stay affectionate and PG; the only bed staging is two people sitting on the end of one.
- The last shot is locked-off on the empty balcony and holds until the audio fades under the sea.
