# Wan 2.2 Shot List — "High Heels on Concrete"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
140 BPM a bar is 1.71 s, so most shots run 2–4 s and the choruses cut on
every bar. The verses are rapped, so cut on the internal rhymes as well as
the line ends.

## 1. Visual style

A London high road between half past midnight and half past three. Wet
tarmac, shutters down, sodium above and cold shop-sign blue at ground level,
so she strobes warm–cold lamp by lamp as she walks. **The heel is the
camera's obsession**: at least one six-inch-off-the-ground heel-strike shot
in every section, always cut exactly on the beat. Nothing is shot from above
her eyeline until the final crane. No smiling to camera, ever — the
confidence is in the walk, not the face.

| Section | Grade | Camera |
|---|---|---|
| Intro | Sodium orange, cold blue fill, everything wet | Six-inch low angle, static |
| Verse 1 (rap) | Station strip light into street sodium | Tracking behind, hard beat cuts |
| Pre-chorus | Cold blue creeping over sodium | Push-in on shoulders |
| Choruses | Alternating warm/cold lamp strobe, saturated | Crane, tracking, reflections |
| Post-chorus | Hard single-source, near-black surround | Locked-off heel-level impacts |
| Verse 2 (rap) | Tunnel: one caged bulb every ten metres; then neon off water | Handheld, flashing in and out |
| Instrumental | Darkest frames in the film | Locked-off, slow motion |
| Bridge | Flashback colder, greener, noisier; present warm and steady | Static, one match cut |
| Final chorus | Fullest, warmest, most saturated | Wide crane rising out |
| Outro | Sodium cooling, sky lifting at frame top | Slow, static, held |

## 2. Character bible — paste into every prompt

**Mahima** (the walk — the whole song)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose and pushed back off her face, sharp minimal makeup with a dark matte lip, wearing a long black wool overcoat over a black slip dress, black stiletto heels, coat collar turned up, composed unsmiling expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (bridge flashback, one year earlier)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back, no makeup, wearing a grey puffer jacket zipped to the chin and flat black boots, shoulders raised, tense watchful expression, realistic cinematic photography, consistent identity, natural skin texture

There is no male lead in this video. **The doubter on the corner is
faceless** — cropped at the jaw, hood up, never in focus.
> a young man on a street corner, hood up, face out of frame or cropped at the jaw, dark clothing, looking down at a phone

**The night crowd** (final chorus): night-bus queue, two chefs on a break in
whites, a courier, a cleaner with a trolley, a group leaving a bar. Ordinary
London night people, mixed ages, all walking the same direction. Never fans,
never a crowd looking at her.

Objects: her **single door key**, the **black cab** (driver's hand only), the
**caged tunnel bulbs**, the **neon puddle**, the **iron railings**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All shopfront signage, station boards, phone screens, cab roof signs and
route numbers are composited in the edit.** Generate the plates clean and
blank; the model cannot render legible English signage and a wrong word on a
London high road destroys the location instantly.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks with IP-Adapter or a character LoRA; keep the
doubter's reference deliberately faceless. **OpenPose is essential for every
full-body walking shot** — a stiletto stride is the exact thing the model
invents anatomy for. Depth for the tunnel and the stairwell. 16:9 first;
9:16 recomposition for the heel-level cuts, which are natural vertical
content. Animate conservatively and in single beats: one heel-strike per
clip, one puddle break per clip, one railing drag per clip. Water splash and
reflection reassembly are far more reliable in slow motion than at speed.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 2–4 s. Post-chorus impacts 0.5 s.

## 4. Scene per lyric line

### Intro — the count-in

1. *"Half past midnight and the high road's humming"* — wide of an empty London high road, shutters down, wet tarmac holding sodium, one bus disappearing at the far end, static.
2. *"You can hear me on the pavement before you see me coming"* — six inches off the ground: an empty stretch of wet concrete, then a single black stiletto entering frame and striking it, low angle, hard shadow.
3. *"Steel on wet stone, that's the only sound"* — macro on the heel tip lifting, a bead of water breaking off it, extreme slow motion.
4. *"London, hold your breath, I am coming round"* — her silhouette from behind, coat collar up, turning a corner into the light, tracking.

### Verse 1 — the years of keeping quiet

5. *"Off the last Overground with my collar to my chin"* — the last train pulling out of an overground platform, Mahima the only figure left on it, wide, strip light.
6. *"Two years keeping quiet was a habit that I binned"* — her coming down the station steps in one continuous tracking move, collar up, barrier beeping behind her.
7. *"They said stay small, keep the volume low"* — close on her face in the stairwell light, no expression, eyes forward.
8. *"Now the whole road turns when I take it slow"* — her stepping out of the station into sodium, deliberately slowing her walk, medium wide.
9. *"Kick, snare, kick, that's the pavement talking"* — three hard cuts on the beat: heel on a drain cover, heel on a painted road marking, heel on a wet kerbstone.
10. *"Every crack in the concrete keeping time while I am walking"* — top-down macro of cracked pavement sliding past under her stride, tracking.
11. *"No entourage, no ring light, no crew"* — a lit shop window with a small group filming with a ring light, Mahima passing behind them in the dark half of frame, rack focus off them onto her.
12. *"Just a coat, a key and a couple of things to prove"* — extreme close-up of her hand in her coat pocket closing around one door key.
13. *"I was bare polite the whole time they took the mick"* — a flash insert, ungraded and handheld: her a year ago nodding politely in a bright office corridor, faces cropped out, one second.
14. *"Learned to keep receipts and let the silence stick"* — back to the street, her jaw set, walking, no reaction, close-up profile.
15. *"Now the same lot slide in, saying hope you're doing well"* — an escalator, her face lit by a phone she barely looks at (message composited), medium close-up.
16. *"I read it on the escalator, kept the story to myself"* — her pocketing the phone without replying and stepping off the escalator, the light changing on her face.

### Pre-chorus 1 — the gear change

17. *"Feel that in the tarmac, that's a shoulder squaring up"* — behind her on a long straight road, the lamps receding to a point, camera pushing in as her shoulders square.
18. *"Hear that in the doorway, that's a woman had enough"* — her reflection passing across a dark shuttered doorway, one frame of her whole body in the glass.
19. *"Give me one dark mile with a bassline underneath"* — her stride lengthening, low three-quarter tracking, coat moving with the pace.
20. *"And I'll turn two leather soles into a full percussion piece"* — macro on the heel landing, water jumping off the pavement, extreme slow motion, then snapping to speed.

### Chorus 1 — the drumline

21. *"High heels on concrete, that's my drumbeat"* — a crane rising behind her as she walks the centre line of the empty road, wide, the lamps in a row.
22. *"Every step a snare going down an empty street"* — heel-level again, dead centre of the white line, each strike on the beat.
23. *"Lamp light, long shadow, nothing in my lane"* — her shadow stretching thirty feet ahead under a lamp, then shortening as she passes it, static wide.
24. *"The city hears me coming and it learns to say my name"* — a shop window reflecting her whole body in one clean tracking pass, the street doubled in the glass.
25. *"Click, clack, hear it ricochet and rise"* — four street objects hit on the beat: a bollard, a railing, a drain grate, a bin lid, each ringing as her heel lands.
26. *"No apology, no permission, no disguise"* — her face in profile at close range, lit warm then cold as she passes between two lamps, tracking.
27. *"High heels on concrete, that's my drumbeat"* — low angle from directly in front, her walking straight at camera, the lens pulling back at her exact pace.
28. *"And the whole of London moves in time with my feet"* — very wide: the road, the terraces, the skyline behind, one small figure dead centre in motion.

### Post-chorus 1 — the chant

29. *"Listen to the concrete, listen how it rings"* — half-second impact: heel on a metal drain cover, hard single-source light, near-black surround.
30. *"Leather, steel and pavement, that's the only drum I bring"* — half-second impact: heel on a painted white line.
31. *"Listen to the concrete, hear it under me"* — half-second impact: heel on a wet cobble, water ringing out.
32. *"I don't need a stage tonight, I've got a whole street"* — half-second impact: heel on a metal utility plate, which rings audibly, then a two-second hold on the empty plate.

### Verse 2 — the tunnel, the cab, the doubter

33. *"Tunnel under the arches and the echo does the mixing"* — her entering a brick railway tunnel, the space visibly opening around her, wide, caged bulbs receding.
34. *"Bassline off the brickwork and the ceiling does the lifting"* — a train passing overhead, dust falling through the beams of the caged bulbs, low angle up.
35. *"Black cab slows beside me, says, love, where you going"* — a black cab rolling alongside at walking pace, window down, only the driver's hand visible, tracking from her side.
36. *"Nah mate, I'm still working, and the working's in the walking"* — her waving it on without breaking stride, the cab pulling away and leaving frame, medium.
37. *"There's a lad on the corner who once told me I was dreaming"* — a faceless young man on the corner, hood up, cropped at the jaw, glancing up as she approaches.
38. *"Head down now, phone out, pretending he's not seeing"* — his head dropping to his phone, her walking past out of focus behind him, shallow depth.
39. *"I don't want the last word, I would rather have the sound"* — her out of the tunnel, not looking back, the reverb space closing behind her, tracking from behind.
40. *"Every door I got shut out of, I just laid it in the ground"* — heel-level on the river walk, the boards and the water beyond, each strike on the beat.
41. *"Puddle catching neon and it doubles up the light"* — a puddle holding a full neon reflection, undisturbed, slow push-in, macro.
42. *"Two of me now walking and the both of us alright"* — her walking beside her own reflection in a wall of dark glass, two of her in step, long lateral tracking.
43. *"Nobody left a lane for me, so I poured one out of nothing"* — her heel breaking the neon puddle, the image shattering and reassembling behind her, slow motion.
44. *"Took the long way past the river just to hear the bridges drumming"* — very wide from across the water: one small lit figure crossing a bridge, the whole city behind her.

### Pre-chorus 2 — railings and stairwell

45. *"Feel that in the railings, that's the iron keeping score"* — her hand dragging along iron railings as she walks, each bar ringing on the beat, macro tracking.
46. *"Hear that in the stairwell, that's a nobody no more"* — a concrete stairwell, green strip light, her taking it two steps at a time, low angle up the well.
47. *"Give me one wet mile with a chorus in my chest"* — her chest and shoulders at close range, one deep breath, the strings entering, static.
48. *"And I'll turn a bad address into a name you won't forget"* — her arriving at the top of the stairwell and stepping out into open sodium, the city opening in front of her, wide.

### Chorus 2 — the street is no longer empty

49. *"High heels on concrete, that's my drumbeat"* — a wider, deeper crane than shot 21, traffic moving, the road alive, her still centre.
50. *"Every step a snare going down an empty street"* — heel-level again but now other feet cross frame around hers, none in time yet.
51. *"Lamp light, long shadow, nothing in my lane"* — her shadow crossed by other shadows for the first time, static wide.
52. *"The city hears me coming and it learns to say my name"* — a night-bus queue turning to watch her pass, held one beat too long, tracking.
53. *"Click, clack, hear it ricochet and rise"* — two chefs on a break in whites stopping mid-conversation, a courier looking up, fast cuts.
54. *"No apology, no permission, no disguise"* — reuse shot 26 framing, more saturated, the lamps brighter behind her.
55. *"High heels on concrete, that's my drumbeat"* — her walking straight at camera again as in shot 27, but now people flow past her on both sides.
56. *"And the whole of London moves in time with my feet"* — a rooftop-height wide of the whole junction with her crossing it, traffic, buses, light.

### Instrumental — the city on its own

57. Locked-off low angle on the empty tunnel: the heel sound arrives before she does, ten seconds of nothing, then her silhouette entering the far end.
58. Slow-motion overhead of the neon puddle, perfectly still, the reflection intact.
59. Her stopping dead on the bridge for the beat drop, the whole skyline behind her, static wide.
60. The drop: everything but the skyline goes black for two seconds, only rim light on her shoulders.
61. The low end slams back — her starting to walk again, straight at camera, hard cut to speed.

### Bridge — half-time, the truth

62. *"There was a year I walked this fast because I was frightened"* — flashback, ungraded and handheld: Mahima in the grey puffer a year earlier, walking fast on the same street, checking behind her.
63. *"Keys between my fingers and my shoulders always tightened"* — extreme close-up of the flashback hand, keys laced between the fingers, knuckles white.
64. *"Same street, same shoes, same length of stride"* — a split-second match cut: flashback stride and present stride in the same frame position, same lamp, same pavement.
65. *"I just stopped asking the dark for a place to hide"* — present: her hand opening, the keys going loose, then back into the coat pocket, macro.
66. *"So if you hear me late and you wonder what it is"* — her shoulders dropping, one long breath, static medium, warm steady light.
67. *"That's not running, that's a rhythm, that's a business"* — she takes a single deliberate step into frame centre and stops, chin level, the strings sustaining.

### Final chorus — the crowd falls in

68. *"High heels on concrete, that's my drumbeat"* — a busy night street, the crowd opening ahead of her without anybody being asked, wide tracking.
69. *"Every step a snare and now there's hundreds on the street"* — twenty pairs of feet joining the rhythm, all different shoes, heel-level, fast cuts.
70. *"Lamp light, long shadow, and they're falling into line"* — the crowd's shadows aligning with hers on the tarmac, high angle.
71. *"The city hears me coming and the city knows it's mine"* — a cleaner with a trolley, a group leaving a bar, all falling into the same direction of travel, tracking.
72. *"Click, clack, hear it ricochet and rise"* — the four street objects again, now struck by four different people's steps.
73. *"No apology, no permission, no disguise"* — Mahima close-up mid-walk, the fullest warmest light of the film on her face.
74. *"High heels on concrete, that's my drumbeat"* — the whole moving crowd from the front, her at its head, wide, lens pulling back.
75. *"And the whole of London moves in time with my feet"* — a crane pulling straight up until she is one lit point in a whole moving city, the widest frame in the video.

### Post-chorus 2 — the chant, shared

76. *"Listen to the concrete, listen how it rings"* — half-second impact: her heel on the drain cover, warmer light.
77. *"Leather, steel and pavement, that's the only drum I bring"* — half-second impact: a trainer on the white line.
78. *"Listen to the concrete, hear it under me"* — half-second impact: a work boot on the cobble.
79. *"I don't need a stage tonight, I've got a whole street"* — half-second impact: her heel again on the ringing utility plate, then a hold.

### Outro — half three

80. *"Half past three and the high road's gone quiet"* — the opening high road, empty again, wet, lit, static wide, nobody in frame.
81. *"Nothing left but me and the noise I made of it"* — her walking into frame from the near side, alone, medium.
82. *"High heels on concrete, that's my drumbeat"* — one last six-inch heel-strike, macro, the water lifting and falling back.
83. *"Let it ring out down the middle of the street"* — final shot: her walking away down the centre line, small, the frame held after she has left it, the sky lifting at the very top, no cut until the reverb tail dies. No text.

## 5. Edit and the challenge

Markers at: the first heel-strike, the drop into sodium after the station,
each *"High heels on concrete"*, both post-chorus chants, the tunnel
entrance, the beat drop in the instrumental, the bridge match cut, and the
final strike. At 140 BPM a bar is 1.71 s — choruses cut every bar, post-chorus
impacts every half-bar, and the rapped verses cut on internal rhymes as well
as line ends.

**The walk-out challenge.** Post the vertical heel-level cut of chorus 1
(shots 21–28) with *"that's my drumbeat"* on screen and invite people to film
their own walk on their own street cut to the post-chorus chant — any shoes,
which is both the joke and the point. The tunnel (shots 33–34) is the second
shareable frame: the reverb change is audible on a phone speaker.
**Caption:** *"No apology, no permission, no disguise."*

## 6. Quality-control checklist

- One heel-strike shot minimum in every section, always cut exactly on the beat
- Two looks only: black overcoat and stilettos throughout; grey puffer and flat boots in the bridge flashback only, never anywhere else
- The doubter on the corner has no visible face in either shot; no other man is featured
- The crowd in the final chorus are night workers and night people going the same way, never fans, never watching her
- No readable signage, route number, station board or phone content generated by the model — all composited
- The camera never rises above her eyeline until shot 75
- She never smiles at camera; the bridge is the only vulnerable passage and it is exactly six shots long
- Stiletto stride and ankle geometry checked on every full-body walking shot (OpenPose); no bent heels, no floating feet
- The last frame is locked off and holds until the reverb tail dies, with no text
