# Wan 2.2 Shot List — "Soft Girl, Steel Spine"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
94 BPM a bar is 2.55 s; the choruses cut every bar and the rap verse cuts
every half-bar where the macro inserts land.

## 1. Visual world

**Pastel and concrete, and the video's entire grammar is the cut between
them.** Two rooms: a ballet studio at dawn — wooden floor, pastel light, a
barre, a window — and a boxing gym — concrete walls, cold overheads, a heavy
bag on a chain. They are cut against each other from the first chorus,
matched on shape rather than on subject: the line of an extended leg against
the line of an extended arm. From the second chorus the grades begin to
**contaminate each other** (gold in the gym, cold blue at the studio
window), and by the final chorus the two rooms have merged into a single
space with a barre on one wall and the bag on the other, crossed in one
continuous camera move with no cut.

There is one pastel object in every corporate frame and one hard object in
every soft frame. Nothing in this video is ironic; the ballet is real
ballet and the boxing is real boxing.

| Section | Grade | Camera |
|---|---|---|
| Intro | Blue pre-dawn, one warm bulb, pastel against dark | Macro, static |
| Verse 1 | Cool office daylight through glass; warm flashbacks | Slow pans, tracking |
| Pre-chorus | Cold room, warm hallway behind her | Static, one push |
| Chorus 1 | Studio pastel-gold vs gym concrete-blue, hard cuts | Match cuts on shape |
| Verse 2 (rap) | Locker strip light; bathroom green-white; boardroom warm | Macro inserts, half-bar cuts |
| Chorus 2 | The two grades bleeding into each other | Wider, looser |
| Instrumental | Slow motion, then one light | Slow, then locked |
| Bridge | Stairwell green-grey, warm doorway beyond | Static, then climbing |
| Final chorus | One merged room, fullest warm light | One continuous move |
| Post-chorus | Alternating pastel and concrete, half a second each | Ultra-fast |
| Outro | Blue pre-dawn turning to full morning | Slow, locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (corporate)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in a low sleek bun, soft natural makeup with long lashes and a pale pink lip, wearing a pastel-pink single-breasted blazer over a white silk shell and wide grey trousers, small pearl studs, pale pink manicure, calm unreadable expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (studio)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair in a tight low ballet bun, minimal makeup, wearing a pale blush leotard with a soft wrap skirt and pink pointe shoes with satin ribbons, pale pink manicure, focused serene expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (gym)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair pulled into a high tight ponytail, no makeup, wearing a black cropped training top and black leggings with hot-pink hand wraps around both hands, pale pink manicure visible past the wraps, set determined expression, realistic cinematic photography, consistent identity, natural skin texture

The **pale pink manicure is in every look and every shot it can be in** — it
is the thread that stitches the three worlds together, so keep hands in
frame wherever possible.

Objects: the **black coffee mug** on a concrete worktop, the **hot-pink hand
wraps**, the **pink pointe shoes and their ribbons**, the **glittered
mouthguard**, the **lavender candle** on a concrete ledge beside the heavy
bag, the **one duffel bag** that holds both lives, the **contract and pen**.

**Colleagues and the other party** are faceless: the back of a head through
glass, a shoulder at a table, a hand offered for a shake, a jaw cropped out
of frame. Nobody in the office is ever a character.

**The stairwell women** (bridge only) are four different young women, each
seen once, each real and specific — a lanyard, a courier bag, a chef's
jacket, a hospital badge. They are not extras; give each of them a face and
one clear beat.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All screens, phone faces, the contract's text, badges, lanyards and any
signage are composited in the edit.** Generate documents as blank paper and
overlay in post — and note that the contract is never legible even in the
composite. It is a shape, not a plot point.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock all three looks with IP-Adapter or a character LoRA (front,
three-quarter, profile, at the barre, at the bag, seated at a table).
**OpenPose is essential for every ballet and boxing shot** — a développé, a
pointe rise, a guard position and a straight right all need a pose reference
or the model invents joints. Depth for the studio and the gym so the two
rooms stay dimensionally consistent, since the final chorus asks you to
combine them into one plate. 16:9 first; 9:16 recomposition for the barre-
to-bag match cut, which is the vertical hero.

Animate in short bursts: one movement per clip. A punch is 2 s, a
développé is 3 s. The barre-to-bag continuous move in the final chorus is a
single generated camera move across a merged set, so build that plate first
and light it before generating anything else in that section.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–4 s; the rap-verse macros 1.5–2 s.

## 4. Scene per lyric line

### Intro — six a.m.

1. *"Pink nails, black coffee, six a.m."* — macro: a pale pink manicure wrapped around a matte black mug on a concrete worktop, blue pre-dawn from one window, static.
2. *"Wrapped my hands before I said amen"* — hot-pink hand wraps pulled tight around a wrist one loop at a time, in near darkness, extreme close-up, the only sound-motivated movement in frame.
3. *"Cried in the car, fixed my face in the glass"* — inside a parked car: her reflection in the rear-view mirror, eyes wet, a knuckle under the lower lash line, one warm streetlight, static.
4. *"Then I walked in like the whole room asked"* — a glass office door from inside, her silhouette pushing through it, the warm hallway light behind her, medium wide.

### Verse 1 — everything they misread

5. *"They see the lashes and the pastel set"* — macro on lashes and a pastel-pink blazer sleeve, shallow focus, cool daylight.
6. *"Think I'm a pushover, easy bet"* — her walking past a glass meeting room; two faceless colleagues glance at her and go back to talking, tracking alongside.
7. *"Called me sensitive like it's a flaw"* — a soft pink manicure resting on a hard steel handrail, macro, the whole contrast of the video in one frame.
8. *"Baby, sensitive is how I saw it all"* — her face in the corridor, not reacting, still walking, close-up, cool light.
9. *"I feel everything, that's the gift"* — a meeting in progress; slow pan across the table on her eyeline: a jaw tightening, a pen stopping, someone leaning back.
10. *"I know the room before the mood shifts"* — her eyes moving from one person to the next, ahead of the room, extreme close-up.
11. *"I'll hold your hand and I'll hold my ground"* — under the table: her hand taking a colleague's hand for exactly one second, then letting go, low static.
12. *"Softest voice in here, but I don't back down"* — the same hand flat on the table as she starts to speak, the room turning toward her, medium.
13. *"Mom said, keep your heart wide open"* — flashback, warm and grainy: a kitchen table, an older woman's hands folded over hers, handheld.
14. *"Coach said, keep your guard up, so I did both of them"* — flashback, gym: a coach's hands lifting her elbows into a guard position, cut hard against shot 13 on the beat.
15. *"Lavender candle next to a heavy bag"* — a wide of her home gym: a lavender candle burning on a concrete ledge, the heavy bag hanging two feet away, static, held long enough to stop being strange.
16. *"Both of them mine and neither one's an act"* — her in frame between them, one hand near the candle, the other on the bag, medium wide, candle and one cold overhead.

### Pre-chorus 1 — the door

17. *"So go ahead, underestimate"* — a boardroom door from the outside, her hand on the handle, held for a beat, close-up.
18. *"Watch me smile while I take the plate"* — the push; the room turning to look; a small polite smile, from behind her shoulder.
19. *"Yeah, I cry, and then I win"* — her setting a folder down on the table without hurrying, macro on the hands.
20. *"Silk on the outside, steel within"* — her taking the chair at the head, cold room, warm hallway light still on her back, medium wide.

### Chorus 1 — the two worlds

21. *"Soft girl, steel spine, don't confuse the two"* — ballet studio at dawn: her at the barre, pastel light on a wooden floor, a slow rise to pointe, wide.
22. *"I can break down, then break through"* — hard cut: the gym, concrete, her straight right into the heavy bag, the chain jumping, low angle.
23. *"Petal on the outside, iron in the root"* — macro pair cut together: a satin ribbon being tied at an ankle, then a hand wrap being cinched at a wrist.
24. *"Kindness ain't a weakness, kindness is the proof"* — a slow développé in the studio, the leg line extending across the frame, tracking.
25. *"Soft girl, steel spine, say it with me now"* — the match cut: the extended leg becomes an extended arm mid-punch, same line, same frame position, same speed.
26. *"I bend, I bloom, I never bow"* — a deep cambré back at the barre, then her rolling under an imagined hook at the bag, cut on the movement.
27. *"You thought the tears meant I was through"* — her face at the bag, breathing hard, absolutely composed, extreme close-up, cold light.
28. *"Soft girl, steel spine, don't confuse the two"* — her face at the barre, breathing, absolutely composed, identical framing, pastel light. Cut the pair together.

### Verse 2 — the rap: two disciplines, one bag

29. *"Studio at six, bag by the door, gloves in the pocket"* — one duffel bag unpacked on a locker-room bench under a strip light, macro pan along it.
30. *"Ballet for the posture, boxing for the way I drop it"* — her at the barre; hard cut to her at the bag; same posture, same spine, matched framing.
31. *"Pointe shoes pink, hand wraps pink, that was not an accident"* — the two objects side by side on the bench, pink on pink, macro, static.
32. *"Soft is the uniform, the discipline's the evidence"* — the pastel blazer folded on top of them in the same bag, close-up, the third piece of the same uniform.
33. *"Glitter on the mouthguard, gloss on the grin I bring"* — extreme close-up of a glittered mouthguard being pushed in, then a grin around it.
34. *"They saw the sparkle, slept on it, then felt the swing"* — a left hook landing on the bag, glitter still catching the overhead, low angle, one second.
35. *"Cried in the third stall, eleven minutes, no sound at all"* — a pair of pastel heels under a bathroom stall door, completely still; a phone face-down on the cistern, harsh green-white light, static, held.
36. *"Blotted, buttoned, walked back in and I ran the whole call"* — hands at a sink blotting under the eyes with a folded tissue; a blazer button done up; then a hard cut to her at the head of a table, entirely composed, running the room.
37. *"Mascara did the running, honey, I did the math"* — her at a whiteboard mid-sentence, the faceless room watching, warm boardroom light, medium.
38. *"Shook through the signature and still signed it fast"* — macro: a hand holding a pen visibly shaking above a blank contract, then the signature going down in one clean movement. Leave the shake in.
39. *"They asked me for quiet, so I handed them polite"* — a handshake; her face pleasant and unreadable; the faceless other party's shoulders dropping, close-up.
40. *"Politeness is a razor if you angle it right"* — her turning away first, the smile going as she turns, late-afternoon window light, medium.

### Pre-chorus 2 — walking out

41. *"So go ahead, read me wrong"* — tracking from behind, the glass meeting rooms sliding past, the faceless colleagues now watching her go.
42. *"I've been writing the end of this song"* — her reflection in a lift door as it closes on her, static.
43. *"Yeah, I cry, and then I win"* — the corridor lights coming on behind her one by one as she passes, wide from the far end.
44. *"Silk on the outside, steel within"* — reuse the framing of shot 20 in reverse: her standing up from the chair, the room still seated.

### Chorus 2 — the two rooms start to bleed

45. *"Soft girl, steel spine, don't confuse the two"* — her at the barre wearing hot-pink hand wraps, pastel light, wide.
46. *"I can break down, then break through"* — her at the heavy bag in the leotard and wrap skirt, cold light, wide.
47. *"Petal on the outside, iron in the root"* — pastel light spilling across the concrete gym floor for the first time, the bag swinging through it, low angle.
48. *"Kindness ain't a weakness, kindness is the proof"* — cold blue at the studio window behind her as she rises to pointe, the first cold frame in that room.
49. *"Soft girl, steel spine, say it with me now"* — a wider match cut than shot 25, more floor, more air, both rooms in the same rhythm.
50. *"I bend, I bloom, I never bow"* — a slow fouetté turn that cuts mid-rotation into a pivot at the bag, one continuous spin across two rooms.
51. *"You thought the tears meant I was through"* — chalk dust off a hand in the studio; resin dust off a wrap in the gym; macro pair.
52. *"Soft girl, steel spine, don't confuse the two"* — the widest two-room cut of the section, held on the last beat.

### Instrumental — half-time, then one light

53. Slow motion: chalk dust leaving a hand, backlit, pastel.
54. Slow motion: the heavy bag swinging back toward camera and filling the frame.
55. Her sitting on the studio floor unlacing a pointe shoe, a bruised foot, no drama, static close-up.
56. Her sitting on a gym bench unwrapping her hands, the hot-pink wrap pooling on concrete, matched framing to 55.
57. A bare frame, one light: the lavender candle blown out on the single piano note, extreme close-up, then black.

### Bridge — the stairwell

58. *"To every girl who cried in the stairwell"* — a concrete stairwell, green-grey: a young woman with a lanyard sitting on a landing, head down, phone in hand, static wide.
59. *"Then walked in the room and nailed it"* — a different woman straightening her collar in the reflection of a stairwell window, then pushing through a fire door into bright office light.
60. *"Who felt every word and still stayed kind"* — a third, in a chef's jacket, sitting on the stairs, wiping her face with the back of her wrist, then getting up.
61. *"Who got called weak for a heart that size"* — a fourth, a hospital badge on her hip, standing very still on a landing with her eyes closed for one breath.
62. *"Let them call it soft, let them call it sweet"* — Mahima on the same landing, sitting down next to the first woman without saying anything, static.
63. *"Soft is the part they can't defeat"* — both of them standing up, the kit returning under the shot, medium.
64. *"Cry it out, then stand up straight"* — the four women and Mahima climbing the stairs together, not in slow motion, just walking, tracking from below.
65. *"Steel don't bend from a little weight"* — the stairwell lights warming through as they climb, wide from the top of the flight.
66. *"You can be the softest thing in the building"* — a low wide from the ground floor of an atrium, looking straight up through the floors to the ceiling, the women small at the top.
67. *"And still be the one holding up the ceiling"* — her face, close, lit warm, looking up. The brightest frame of the video so far.

### Final chorus — one room

68. *"Soft girl, steel spine, don't confuse the two"* — the merged space for the first time: wooden floor, concrete wall, a barre on one side and the heavy bag on the other, her in the middle, wide.
69. *"I can break down, then break through"* — one continuous camera move from the barre to the bag with no cut, her moving with it.
70. *"Velvet on the glove, but the punch is true"* — a pointe shoe and a boxing glove side by side on the floor, macro, both lit by the same light.
71. *"Kindness ain't a weakness, kindness is the proof"* — a rise to pointe that carries straight into a guard position, one take, medium.
72. *"Soft girl, steel spine, say it louder now"* — her to camera for the first and only time, no smile, no aggression, close-up.
73. *"I bend, I bloom, I never bow"* — the cambré and the roll again, but now inside one frame with both rooms visible behind her.
74. *"You thought the tears meant I was through"* — pastel light and cold light falling on the same face from opposite sides, extreme close-up.
75. *"Soft girl, steel spine, don't confuse the two"* — the widest shot of the video: the whole merged room, her at the centre, fullest warm light.

### Post-chorus — the chant

76. *"Soft, soft, steel, steel"* — pink nails, half a second, macro.
77. *"Cry, then close the deal"* — a fist in a hot-pink wrap, half a second, macro.
78. *"Soft, soft, steel, steel"* — mascara under an eye, half a second, macro.
79. *"Pink on the wrap, but the hook is real"* — a left hook connecting with the bag, half a second, low angle. Alternate pastel and concrete grades one per cut.

### Outro — the same six a.m.

80. *"Pink nails, black coffee, six a.m."* — the opening kitchen the next morning, the same macro of pink nails around the black mug, blue pre-dawn.
81. *"Wrap my hands and go again"* — the same wraps pulled tight, same framing as shot 2, but the light is a shade warmer.
82. *"Cried in the car and still won the day"* — the car mirror again, no tears this time, just a look and a small nod, close-up.
83. *"Both of those are me, they're not going away"* — the duffel bag zipped shut on the passenger seat with the pointe shoes and the gloves both inside, macro.
84. *"Don't confuse the two, don't confuse the two"* — her hand on the front door, the bag on her shoulder, morning light coming under the door, medium.
85. *"Soft girl, steel spine, I'm both, it's true"* — final shot: her walking out of frame into full morning, the door left open behind her, locked-off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the hand wraps in shot 2, each *"don't confuse the two"*, the
barre-to-bag match cut (shot 25), the bathroom stall (shot 35), the
signature (shot 38), the instrumental, *"holding up the ceiling"* (shot 67),
the merged room (shot 68), and the open door. At 94 BPM a bar is 2.55 s;
choruses cut every bar, the rap verse cuts every half-bar on the macro
inserts, the bridge holds two bars a shot.

**The two-worlds transition.** Cut the vertical hero from shots 24–25 — the
développé becoming the straight right — with *"soft girl, steel spine, don't
confuse the two"* on screen, and invite people to post their own: one
outfit, one spin, and you land in the other life. The second shareable frame
is shot 38, the shaking hand signing anyway; the third is shot 66, the
atrium looking up.

## 6. Quality-control checklist

- The pale pink manicure appears in every look and in as many frames as a hand can be got into
- Three looks in the right sections: corporate in verse 1, pre-choruses and the rap verse; studio and gym in the choruses; both crossed from shot 45 on
- The pastel/concrete cut is always matched on **shape**, never on subject — check every chorus pair before locking
- The grades stay separate through chorus 1 and only begin to contaminate at shot 47
- Every ballet and boxing movement is anatomically real (OpenPose on all rises, développés, cambrés, guards and punches); no invented joints, no floating pointe
- Colleagues and the other party never have a visible face; the four stairwell women all do
- The shake in shot 38 stays in the cut — it is the cost, not a weakness
- All documents, screens, badges and signage composited; the contract is never legible
- The last shot is locked-off, the door stays open, and it holds until the audio fades
