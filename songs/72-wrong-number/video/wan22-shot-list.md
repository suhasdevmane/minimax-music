# Wan 2.2 Shot List — "Wrong Number"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Seventy-five lyric shots plus five for the instrumental, numbered
continuously. Timestamps come from the rendered WAV. This is an uptempo
record: at 120 BPM a bar is 2 s, so the rap verses cut on the half-bar and
the post-chorus chant cuts on every line.

## 1. Visual world

A northern English city at night, shot warm rather than grim: tram lines,
station sodium, a chippy on a corner, a new flat with the good light already
found, a bar, a night bus. Two textures run against each other — the
**cold** of the phone (tram interior white-green, screen glow from below,
tunnel dark) and the **warm** of everything she has built instead (gold flat,
fluorescent chippy, red bar light, kitchen overheads). The cold shrinks
across the video until, by the outro, there is none of it left except a dark
phone screen nobody is looking at.

| Section | Grade | Camera |
|---|---|---|
| Intro | Tram white-green, black windows | Static, screen-lit from below |
| Verse 1 | Station sodium, neon, chippy fluorescent | Straight to camera, hard cuts on brass |
| Pre-choruses | Tunnel dark, then city all at once | Macro, then wide |
| Choruses | Gold flat, saturated bar light | Backwards tracking, wide |
| Post-choruses | Kitchen overheads, propped ring light | Handheld, too close, on the beat |
| Verse 2 | Sunday daylight, phone-shop retail white | Static, deadpan |
| Instrumental | Bar heat, cold street, empty platform | Handheld dance, then locked-off |
| Bridge | Tram reflections, then hard clean light | Static, to camera |
| Final chorus | Neon and streetlight, most colour in the piece | Widest of the video |
| Outro | Hall light, dark screen | Slow, held |

## 2. Character bible — paste into every prompt

**Mahima** (the tram and the verses)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly wind-blown, small gold ring in one nostril, minimal makeup, wearing an oversized camel wool coat over a black roll-neck, dry amused expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the new flat, daytime)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied up in a claw clip, small gold ring in one nostril, no makeup, wearing a grey sweatshirt and jogging bottoms with dust on them, delighted unguarded expression, realistic cinematic photography, consistent identity

**Mahima** (the night out — the loud red dress)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair blow-dried and full, small gold ring in one nostril, bold red lip and gold hoops, wearing a bright red slip dress, wide open laughing expression, realistic cinematic photography, consistent identity

**The ex** — faceless in every frame. He exists only as a name on a lit
screen, a set of three dots, and one two-second memory of a forearm in a
kitchen doorway. Never generate his face.
> a young man in his late twenties, face out of frame or cropped at the jaw, dark jacket

**The three friends** — one tall woman with braids, one with a short bleached
crop, one in glasses; consistent across the kitchen, the bar and the street.
They are a real group, not styled extras, and they are the emotional anchor
of the video.

**The chippy man** — an older man behind a fluorescent counter who knows her
order. One shot, warm, no dialogue readable.

Objects that repeat: the **phone** (buzzing, face-down, finally dark), the
**tram**, the **new key and fob**, the **receipt with the new number on it**,
the **red dress**, the **hall light**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**Every screen, message, three-dots bubble, buzzer panel, tenancy agreement,
shop ticket and receipt is composited in the edit.** Generate phones as lit
blank rectangles and paper as blank paper. The model cannot render legible
text, and the joke of this video lives entirely in text that appears for
under a second and is cut away from before it can be read.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks with IP-Adapter or a character LoRA, and lock
each of the three friends with her — group identity drift is the biggest risk
in this video because they appear in three separate environments. Keep the
ex's reference deliberately faceless. Keyframes first; **OpenPose is
essential** for the kitchen chant, the dance sequence and the four-abreast
street walk. Depth for the tram interiors and the bar. Shoot the
straight-to-camera rap bars as separate locked-off plates so they can be cut
hard on the brass without motion mismatch. 16:9 first; 9:16 for the kitchen
chant and the rap bars, which are the vertical hero cuts. Animate in short
bursts: one bar per clip on the verses.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s; rap bars 2 s.

## 4. Scene per lyric line

### Intro — the text arrives

1. *"Six months of nothing, then your name on my screen at ten to one,"* — an almost-empty late tram going through a dark cutting, her the only person awake, wide static.
2. *"Same three dots you always did when you were working out a lie."* — a phone face-up on her knee, three dots appearing and disappearing (composited), the screen lighting her chin from below.
3. *"I let it sit a minute while the tram went through the dark,"* — her face doing almost nothing for the whole line, black window behind her, static close-up.
4. *"Then I typed three small words and put the whole thing by."* — her thumb typing, then the phone going into her coat pocket in one movement, macro.

### Verse 1 — the reply, straight to camera

5. *"You said long time, hope you're keeping well,"* — the beat drops: her in the tram seat delivering straight down the lens, locked-off, hard cut on the brass.
6. *"Like half a year of silence was a holiday you spent."* — same delivery, different seat, the tram now lit and full, one bar.
7. *"I read it on the tram, coming into Piccadilly,"* — the tram sliding into a lit station, filmed from the platform as it passes, her visible in one window.
8. *"With my own bags in my hands and my own name on the rent."* — her stepping off with shopping bags; hard cut to her own name on a tenancy agreement (composited), macro.
9. *"You got the number off a mate who got it off a mate,"* — her on a station escalator delivering the bar, people going the other way, tracking.
10. *"And you opened with a compliment, which is peak, and it's late."* — the station concourse, big and empty, her small in it and delivering to camera, wide.
11. *"I've moved, I've changed the locks, I've changed the postcode too,"* — three hard cuts: a new key, a new lock, a new buzzer panel (composited), all macro, all on the beat.
12. *"There's a chippy on my corner and it knows my name, not you."* — the chippy under fluorescent light, the man behind the counter greeting her, handing over a wrapped parcel, warm.
13. *"You want the girl who sat up waiting on a maybe and a might,"* — her walking home eating chips, unbothered, tracking from the front.
14. *"She got made redundant, mate, they shut it down one night."* — she stops, delivers the punchline to camera, and carries on walking. One take, no coverage.

### Pre-chorus 1 — send and forget

15. *"So I typed it out slow with a smile on my face,"* — macro of a thumb typing on a lit blank screen, her mouth in the top of frame, half a smile.
16. *"Read it twice, sent it, put the phone away."* — the message going up the screen and gone before it can be read (composited), then the phone into a bag.
17. *"The tram went under the bridge and the signal cut,"* — the tram entering a tunnel, the carriage going dark, signal bars dropping to nothing (composited).
18. *"And I never checked it once for the rest of the day."* — the bag on her lap with the phone in it, closed, held for the whole line.

### Chorus 1 — the new flat

19. *"Sorry, wrong number, she doesn't live here anymore,"* — she walks backwards through the new flat ahead of the camera, arms out, boxes half unpacked, late gold light.
20. *"New city, new keys, new name on the door."* — a new key on a new fob spinning on her finger, macro, then a name going onto a buzzer panel (composited).
21. *"The girl you're texting, mate, moved out in the spring,"* — a window with a northern skyline in it, her stepping into frame to look out, wide.
22. *"She left no forwarding address for anything."* — an empty hallway with no post on the mat at all, static, held.
23. *"Sorry, wrong number, this is not who you think,"* — her in the claw clip and the dusty sweatshirt, singing straight to camera on a stepladder, low angle.
24. *"She doesn't wait up and she doesn't lose a wink."* — her asleep, properly asleep, in a bed with no phone anywhere near it, overhead.
25. *"Sorry, wrong number, she doesn't live here anymore,"* — the widest shot of the flat, sun across the floor, her in the middle of it turning slowly.
26. *"Try somebody else, like you did before."* — a door closing on the camera from inside the flat, warm, unhurried, hard cut to black.

### Post-chorus 1 — the kitchen chant

27. *"Wrong number, wrong number, wrong girl, wrong year,"* — four women in a kitchen mid-getting-ready, shouting the chant into a mirror, handheld and too close.
28. *"Wrong number, wrong number, she isn't here."* — one of them with a hairbrush as a microphone, the other three behind her, cut on the beat.
29. *"Wrong number, wrong number, wrong girl, wrong year,"* — hard rhythmic cuts of hands, hoops going in, a lipstick, a bottle opening.
30. *"Sorry, wrong number, she isn't here."* — a single wide of the four of them lined up against the kitchen units, still, staring down the lens.

### Verse 2 — the escalation, and the phone shop

31. *"Three dots, then a laugh, then a who's this, are you serious,"* — the phone on a kitchen table between two coffees, buzzing, screen lighting repeatedly (composited).
32. *"Then a paragraph at two in the morning, and it's furious."* — a long message filling a screen at speed, cut away from before a word can be read, macro.
33. *"I read it with my coffee and my flatmate on the Sunday,"* — two women at a table on a bright Sunday, both talking, the phone buzzing between them and neither reacting.
34. *"And we laughed like it was telly and I binned it before Monday."* — both of them genuinely laughing, then her deleting with one thumb without looking, static.
35. *"Went down to the phone shop on a Saturday in spring,"* — a phone shop exterior on a busy Saturday street, retail white light spilling out, wide.
36. *"Got a number on a receipt and it felt like a new thing."* — a ticket number, a plastic chair, a new SIM in a tray, a receipt held up like a certificate (composited).
37. *"Same face, same laugh, same ring in the same nose,"* — her reflection in the shop's glass, close, the gold nose ring catching the light.
38. *"Same girl, brand new terms, and the first term is, no."* — straight to camera in the shop doorway, delivering the bar, people passing behind her.
39. *"I'm not angry and I'm not owed and I'm not keeping score,"* — her walking a Saturday high street with the new phone box under her arm, tracking.
40. *"I just don't answer numbers that I deleted before."* — the old phone going into a drawer at home, the drawer closing, macro.

### Pre-chorus 2 — the night starts

41. *"Typed it out again with the very same grin,"* — the same thumb, the same three words, the same absence of drama, macro, in a bathroom mirror's light.
42. *"Three small words, and I let them do the rest."* — the message sending; her turning away from the phone to finish an earring.
43. *"The tram came over the bridge with the whole town lit,"* — the tram crossing a bridge above a lit city, filmed from outside at blue hour, wide.
44. *"And I went to meet the girls in the loud red dress."* — the tram doors opening and her stepping out in the red dress, doors closing behind her, tracking.

### Chorus 2 — out

45. *"Sorry, wrong number, she doesn't live here anymore,"* — tracking through a busy bar behind her, people greeting her the whole way, red and amber light.
46. *"New city, new keys, new name on the door."* — the four of them squeezing into a booth, drinks landing on the table, handheld.
47. *"The girl you're texting, mate, moved out in the spring,"* — the phone face-down on a sticky table, buzzing, nobody looking at it.
48. *"She left no forwarding address for anything."* — her singing the line to her friends rather than the camera, all four laughing, close.
49. *"Sorry, wrong number, this is not who you think,"* — the bar's mirror, four reflections, hoops and red lipstick, medium.
50. *"She doesn't wait up and she doesn't lose a wink."* — a shot of the dance floor filling, from above, movement everywhere.
51. *"Sorry, wrong number, she doesn't live here anymore,"* — her arms up in the middle of the floor, the widest bar shot, saturated.
52. *"Try somebody else, like you did before."* — the bar door swinging, the music cutting in and out with it, hard cut.

### Instrumental — the night, and one held breath

53. A brass-led dance sequence: the four of them, no choreography, real movement, cut on the horn phrases, handheld.
54. Close cuts on the beat: feet, a spilled drink, a hand on a shoulder, someone shouting a lyric with no sound.
55. Her outside in the cold with a coat over her shoulders, laughing at something off-camera, breath visible.
56. The bar door swinging open and shut behind her, cutting the room's noise into slices, static.
57. The hard beat switch: one half-time bar of tram hum on a locked-off shot of an empty night platform. The cut into the bridge.

### Bridge — the one soft second

58. *"For a second I remembered the good version of you,"* — her alone on the last tram, red dress under the camel coat, window reflections across her face, static.
59. *"The one that made me laugh in a kitchen in the rain."* — a two-second warm flash: a kitchen doorway, rain on a window, a forearm, her laughing. His face never in frame.
60. *"Then I put my coat on and I got the tram again."* — hard cut back: her pulling the coat closed, face level again, the tram moving.
61. *"It isn't that I hate you, it's that I'm not free labour,"* — straight to camera under a hard clean light, brass returning, locked-off.
62. *"I did the whole rebuild and you want the finished flat."* — cut to the flat mid-renovation earlier in the year: her painting a wall alone at night, dust, one work lamp.
63. *"The girl who lived here loved you and she paid for it in years,"* — the same wall, finished, in daylight, with a picture hung on it.
64. *"And she's happy, and she's gone, and you cannot have her back."* — back to camera on the tram, the last line delivered flat and final, full brass, hold.

### Final chorus — all of it at once

65. *"Sorry, wrong number, she doesn't live here anymore,"* — the four of them walking a street abreast, neon behind, the widest shot of the video, tracking backwards.
66. *"New city, new keys, new name on the door."* — reuse the key and buzzer macros, now cut twice as fast and lit warmer.
67. *"The girl you're texting, mate, moved out in the spring,"* — a night bus going past behind the four of them, the whole frame moving.
68. *"She left no forwarding address for anything."* — her turning to walk backwards ahead of her friends, arms wide, laughing.
69. *"Sorry, wrong number, this is not who you think,"* — the chippy again, late, all four of them in it now, fluorescent and warm.
70. *"She's out with her girls and she's on her second drink."* — a booth, four glasses, a toast that gets shouted, handheld.
71. *"Sorry, wrong number, she doesn't live here anymore,"* — the street corner, all four, brass hitting, saturated neon.
72. *"And I'm not sorry, and I'm not sorry, and I'm sure."* — she stops and delivers the last line to camera while the others carry on walking out of frame ahead of her.

### Post-chorus 2 — shouted outside

73. *"Wrong number, wrong number, wrong girl, wrong year,"* — the four of them shouting it on the corner, a night bus passing behind, handheld.
74. *"Wrong number, wrong number, she isn't here."* — hard cuts: feet, a chip carton, a taxi door, hands in the air.
75. *"Wrong number, wrong number, wrong girl, wrong year,"* — a taxi window going down and the chant coming out of it, from the pavement.
76. *"Sorry, wrong number, she isn't here."* — the taxi pulling away, the corner empty, one wide, held.

### Outro — home

77. *"New flat, new key, new light in the hall,"* — her letting herself in, shoes off in the hall, hall light on, handheld and quiet.
78. *"New number nobody's got but the people that I call."* — the phone going face-up on the kitchen counter, screen dark, macro.
79. *"If it rings after midnight it's my sister or my mate,"* — her filling a glass of water, entirely calm, the phone in the background not doing anything.
80. *"And whoever you're texting, she left. It's too late."* — final shot: the flat window with the northern skyline in it, the phone locking with a small sound, held through the fade. No text.

## 5. Edit and the cuts

Markers at: the three dots in shot 2, the beat drop on shot 5, the chippy
punchline at 14, each *"sorry, wrong number"*, both kitchen and street
chants, the beat switch at 57, the memory flash at 59, the four-abreast walk
at 65, and the phone lock at the end. At 120 BPM a bar is 2 s; rap verses cut
on the half-bar, the post-chorus cuts on every line, and the chorus holds two
bars per shot.

**Four shareable cuts.** The **kitchen chant** — shots 27–30, vertical, the
one the video is sold on. The **rap clip** — shots 11–14, ending on the
redundancy punchline. The **wrong-number challenge** — post the three words
on a blank screen over the chant and nothing else. The **caption** —
*"The girl you're texting, mate, moved out in the spring."*

## 6. Quality-control checklist

- Three looks in the right sections: camel coat on the tram and the verses, claw clip and dusty sweatshirt only in the flat, red dress only from shot 44 on
- The three friends are identity-locked across kitchen, bar and street; group drift is the biggest risk here
- The ex has no face in any frame, including the bridge flash — a forearm and a doorway only
- Cold phone light shrinks across the video and is gone by the outro except one dark screen
- All screens, messages, agreements, tickets and receipts composited, and every one of them is cut away from before it can be read
- Rap bars are locked-off plates cut hard on the brass, never handheld
- OpenPose on the kitchen chant, the dance sequence and the four-abreast walk
- The last shot is locked-off and holds until the phone lock sound
