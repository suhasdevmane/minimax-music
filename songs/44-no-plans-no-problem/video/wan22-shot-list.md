# Wan 2.2 Shot List — "No Plans, No Problem"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
104 BPM a bar is 2.3 s, so most shots are 3–5 s and the rap-sung verses cut
on the half-bar where the internal rhymes land.

## 1. Visual style

One London Saturday, filmed like a documentary that got lucky. The camera
walks: nothing is on a dolly, nothing is stabilised to death, and the whole
video moves east through the city as the sun moves west across it. **The
light is the clock** — blown-out late morning, hard afternoon, smoke-gold at
the market, long low gold on the canal, blue at the very end, then a clean
ordinary morning for the outro. Colour is saturated and real: brick, sun,
food, water. No neon, no night, no club.

| Section | Grade | Camera |
|---|---|---|
| Intro | Dim room, one hard blade of sun | Static, macro |
| Verse 1 | Blown-out late morning, saturated | Handheld walking, bus front window |
| Pre-chorus | Street-level hard sun | Close on hands and pockets |
| Choruses | High summer sun, deep colour | Backwards-walking tracking, low feet shots |
| Post-chorus | Hard, bright, high contrast | Two fast wides |
| Verse 2 | Smoke-gold market, then late gold canal | Handheld inside the crowd |
| Instrumental | Deep gold turning blue at the edges | Bridge wide, drone lift |
| Bridge | Low orange on one side of her face | Static, held |
| Final chorus | Last direct sun, bouncing off water | Drone, then inside the group |
| Outro | Clean ordinary morning | Locked-off, matched to shot 1 |

## 2. Character bible — paste into every prompt

**Mahima** (the whole day)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair half-up in a claw clip with strands loose, minimal makeup and gold hoop earrings, wearing a cropped white vest, a light denim jacket tied at her waist and wide black trousers with white trainers, easy amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (outro, next morning)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and slept-in, no makeup, wearing an oversized grey t-shirt, calm rested expression, realistic cinematic photography, consistent identity, natural skin texture

There is **no romantic lead in this video** and no Kai. Nobody is a love
interest; this is a friendship and a city.

**The three friends** — consistent across the whole video, they are in almost
every wide: a tall young man in a football shirt and a bucket hat; a young
woman with long braids and a crossbody bag; a young man in a bright orange
vest with brand-new white trainers he keeps protecting.

**The market auntie** — the emotional beat of verse two.
> a woman in her sixties, headwrap, gold earrings, an apron over a bright print dress, standing behind a market food stall, warm direct expression

**The chain reaction** — a boy of about eight, his mother, a barber in a
black apron, a jogger. Ordinary bodies, ordinary clothes, real dancing.

Objects that must stay consistent: the **speaker bungee-corded to a bicycle
rack**, the **paper plate of food**, the **denim jacket** tied at her waist
from shot 7 onward, her **phone** which is only ever in a pocket after
shot 18.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, phone UI, shop signage, bus destination boards and price
tickets are composited in the edit.** Generate phones as lit blank
rectangles and market signage as blank card. The model cannot render legible
English signage and a wrong London sign kills the register instantly.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA, and lock the
three friends as a set — they recur in over twenty shots and drift is the
main risk here. Keyframes first; OpenPose is essential for every dance shot,
especially the chain reaction, where four different people must each move
differently and none of them are trained dancers. Depth for the market
interiors and the towpath so the canal sits correctly behind the crowd.
16:9 first; 9:16 recomposition for the walk-and-dance chorus and the chain
reaction, which are the vertical clips. Animate in short bursts: a curtain
pulled, a fork turning chicken, a note handed over, one dance move per clip.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–5 s; verse shots 2–3 s to match the rap-sung cadence.

## 4. Scene per lyric line

### Intro — the flat, no drums

1. *"No alarm, no reason, just a Saturday"* — a hard blade of sunlight lying across a bedroom wall and a bare shoulder, everything else in shadow, static macro.
2. *"Sunlight on the wall and the curtains still drawn"* — the closed curtain itself, glowing at the edges, dust moving in the light leak, static.
3. *"Somebody is typing in the group chat asking what we're doing"* — a phone face-up on a duvet, screen lit, three dots typing (UI composited), nobody reaching for it.
4. *"And the honest answer is, we haven't got a plan at all"* — Mahima's face on the pillow, eyes open, a slow grin starting, close-up.

### Verse 1 — out of the house, onto the bus

5. *"Half eleven, curtains drawn, no alarm, no shame"* — a clock face on a bedside shelf with no hands legible, then her feet swinging onto the floor, two quick cuts.
6. *"Group chat asking what's the plan, there ain't one, that's the game"* — her thumb replying with one word (composited), then the phone going face-down on the bed.
7. *"Meet me by the station, bring your appetite and time"* — curtains yanked open on the downbeat, the room blowing out white for a frame, then resolving.
8. *"We're not booking, we're not queueing, we're just letting the day decide"* — trainers going on at the door, keys off the hook, the denim jacket pulled off a chair, three fast cuts.
9. *"Missed the train on purpose so we took the bus instead"* — a train pulling out of an overground platform without her, shot from the stairs, unbothered.
10. *"Top deck, front seat, all of Kingsland Road ahead"* — the front window of a double-decker top deck, the road unspooling, shot from behind their heads.
11. *"Somebody's shoes are brand new, somebody's aunt is on the phone"* — brand-new white trainers lifted away from a scuffing foot; a friend loudly on the phone; the row laughing.
12. *"Somebody swears they know a spot, they don't, but we go on"* — the friend in the bucket hat pointing confidently out of the window at nothing, the others already standing up.

### Pre-chorus 1 — the phone gives up

13. *"No reservation, no itinerary, no rush"* — the bus bell being pressed by three hands at once, close-up.
14. *"Phone on ten percent and I am not topping up"* — her battery indicator low and red (composited), held two beats, then ignored.
15. *"Wherever we end up is exactly where we should be"* — the four of them stepping off the bus into a busy street, the doors hissing shut behind them, medium wide.
16. *"Turn it up a little bit and drop that beat on me"* — a hand turning up a small speaker clipped to a bag strap, macro, the street noise dropping under it.

### Chorus 1 — the pavement

17. *"No plans, no problem, just vibes and my people"* — the four of them walking straight at camera down a busy street, the camera walking backwards ahead of them, high sun.
18. *"Nowhere to be by nine and nothing to prove"* — her sliding the phone into a back pocket and not touching it again, close on the hand, then back to the walk.
19. *"No plans, no problem, no map and no timing"* — a folded paper map on a rack outside a shop, passed without a glance, quick insert.
20. *"Just a speaker, a pavement and a reason to move"* — feet in four different pairs of shoes doing four different steps, low and tight on the beat.
21. *"Feet doing something that could pass for a dance"* — a wider version of the same, waist-down, real pedestrians walking around them.
22. *"Best day of the summer and it came by chance"* — her face mid-laugh, hair moving, sun blowing out behind her head, close-up.
23. *"No plans, no problem, just vibes and my people"* — all four turning to walk the other way at once, mid-crossing, for no reason, wide.
24. *"Nothing in the diary, so tell me what we do"* — the group stopping dead at a junction and all looking in different directions, held one beat.

### Post-chorus 1 — chant

25. *"No plans, no problem, no plans, no problem"* — four hands going up together at a crossing, hard cut, bright.
26. *"Just vibes and my people and a whole day free"* — a wide of the four crossing against the traffic light with the whole junction behind them.

### Verse 2 — market, then canal

27. *"Two o'clock, we hit the market and the street is full of smoke"* — smoke rising off a grill into hard sun, the street beyond it soft in haze, wide.
28. *"Jerk chicken, roti, plantain and a mango for the road"* — a fork turning chicken; steam off a tray; a mango going into a jacket pocket, three macro cuts.
29. *"Auntie on the corner says she'll do it for a fiver"* — the market auntie behind her stall, hands working, talking straight to camera-left, medium close.
30. *"Takes the fiver, gives me change, and then she calls me daughter"* — a five-pound note handed across, change pressed back into her palm with an extra piece of fruit, macro, then both faces.
31. *"Down beside the water there's a speaker on a bike"* — a bicycle leaning on a bollard on the towpath, a battered speaker bungee-corded to the rack, low angle.
32. *"Playing something old enough that everybody likes"* — three faces along the towpath lifting at the same moment, recognising the song, a slow lateral track.
33. *"Kid starts moving, then his mum, then the barber from the shop"* — the chain reaction in one continuous handheld move: the boy, his mother, the barber in a black apron coming out of a doorway.
34. *"Now the towpath is a dance floor and there's nobody to stop us"* — a wide from the far bank: twenty people dancing along the water, a narrowboat passing behind them.

### Pre-chorus 2 — the heat

35. *"It's proper warm, the ice cream queue is halfway round the block"* — an ice cream van with a queue snaking round a corner, everybody squinting, one child already dripping.
36. *"Phone on four percent and I am not topping up"* — her phone at four percent (composited), then her switching it off entirely and pocketing it, macro.
37. *"Wherever we end up is exactly where we should be"* — her looking down the length of the canal, hand shading her eyes, medium.
38. *"Turn it up a little bit and drop that beat on me"* — the speaker's volume dial thumbed up on the bike, macro, the crowd noise swelling behind it.

### Chorus 2 — the towpath in full

39. *"No plans, no problem, just vibes and my people"* — a long lateral track along the water beside twenty people dancing in a loose line.
40. *"Nowhere to be by nine and nothing to prove"* — the barber dancing in his apron with his scissors still in the chest pocket, medium, delighted.
41. *"No plans, no problem, no map and no timing"* — a church clock or station clock in the background of a wide, deliberately out of focus.
42. *"Just a speaker, a pavement and a reason to move"* — the speaker on the bike, shot low with the whole crowd behind it, wide angle.
43. *"Feet doing something that could pass for a dance"* — feet on the towpath gravel, twenty pairs, dust coming up, low macro.
44. *"Best day of the summer and it came by chance"* — the four friends in a huddle, foreheads nearly touching, shouting the line at each other.
45. *"No plans, no problem, just vibes and my people"* — the boy from the chain reaction on his mother's shoulders, both moving, medium.
46. *"Nothing in the diary, so tell me what we do"* — a wide from a bridge above, the whole towpath moving, the water flat gold.

### Instrumental — percussion and guitar

47. A man on the towpath playing a talking drum he simply had with him, close, hands only, dead on the beat.
48. Hands passing a paper plate of food along a low wall, four pairs of hands, one shot.
49. A narrowboat going by with someone waving from the tiller, the dancing reflected in its windows.
50. Mahima sitting on the towpath edge with her feet over the water, laughing at something off frame, medium.
51. A wide from the bridge as the sun drops behind the buildings and the whole scene shifts from gold to blue in one shot.

### Bridge — the still moment

52. *"I had a whole year of calendars and colour-coded weeks"* — her alone on a bench, party out of focus behind her, catching her breath, static medium, low orange light.
53. *"Alarms to go to the gym and reminders to eat"* — two-second inserts of the life she is not living today: a laptop calendar grid of coloured blocks (composited), a gym bag by a door, an alarm ringing in an empty room.
54. *"But today was never written down and look at what it gave"* — back to her on the bench, looking out at the crowd, the light directly on one side of her face, close-up.
55. *"The best ones don't get booked, they only find you on the way"* — her standing up and walking back into the crowd, the camera staying on the empty bench for one beat before following.

### Final chorus — the fullest

56. *"No plans, no problem, just vibes and my people"* — a drone lift straight up off the towpath, revealing how far along the water the dancing goes.
57. *"Nowhere to be by nine and nothing to prove"* — the four friends in the middle of it, arms round shoulders, singing into each other's faces.
58. *"No plans, no problem, no map and no timing"* — the market auntie's stall being packed down in the background of a wide while the dancing continues in front of it.
59. *"Just a speaker, a pavement and a reason to move"* — the bicycle speaker at the centre of a ring of people, shot from directly above.
60. *"Half of the towpath in a kind of a dance"* — the longest lateral track of the video, thirty people, one continuous move along the water.
61. *"Best day of the summer and it came by chance"* — her face, last direct sun coming up off the water and under her chin, close-up.
62. *"No plans, no problem, just vibes and my people"* — all four jumping together on the beat, wide, the canal behind them.
63. *"Nothing in the diary, so tell me what we do"* — the group turning and walking away up the towpath into the blue end of the evening, from behind.

### Post-chorus 2 — street chant

64. *"No plans, no problem, no plans, no problem"* — a wide of twenty people with hands up on the beat, gold in the middle, blue at the edges.
65. *"Just vibes and my people and a whole day free"* — the same crowd jumping, held one beat longer, the speaker still on the bike in the foreground.

### Outro — the next morning

66. *"Half eleven tomorrow and the curtains will be drawn"* — the same wall and the same blade of sun as shot 1, one day later, matched exactly.
67. *"Group chat will be asking me the same"* — the phone lighting up on the duvet with the group chat again (composited), her hand reaching over.
68. *"And I'll tell them what I told them here today"* — her turning the phone face-down and lying back, smiling, close-up.
69. *"No plans, no problem, come and find me anyway"* — final shot: her pulling the curtain fully open onto a bright ordinary street, holding on the window, locked-off through the fade. No text.

## 5. Edit and the challenge

Markers at: the curtain pull, the bus front window, each *"no plans, no
problem"*, the fiver, the first move of the chain reaction, the drone lift,
*"they only find you on the way"*, and the matched morning frame. At 104 BPM
a bar is 2.3 s; the choruses cut on the bar and the rap-sung verses cut on
the half-bar where the internal rhymes land.

**The chain-reaction challenge.** Shots 31–34 are the shareable unit: one
person starts moving to a speaker, then a parent, then a shopkeeper, then a
stranger, cut one per beat. Film your own chain in your own ends and drop it
on the hook. Second clip: shots 17–24, the backwards-walking chorus, vertical,
four people and four different steps.

**Caption:** *"Nothing in the diary, so tell me what we do."*

## 6. Quality-control checklist

- The day only moves forward: late morning, hard afternoon, market gold, canal gold, blue. No shot returns to an earlier light except the deliberate matched frame in the outro.
- Mahima is in the vest-and-denim look for shots 5–65 and the grey t-shirt look only for 66–69.
- The three friends are the same three people in every wide; no substitutions, no duplicated faces in crowds.
- The phone is visible in shots 3, 6, 14, 18 and 36 only, and is off and pocketed from shot 36 to the end.
- No readable English text anywhere: bus boards, shop fascias, market price cards and phone UI all composited in the edit.
- The market auntie, the boy, his mother and the barber are the same people wherever they recur.
- Dancing is ordinary-body, ordinary-clothes, real; nobody is a trained dancer and nobody is filmed as a performer.
- The final frame is locked-off on the open window and holds through the fade.
