# Wan 2.2 Shot List — "Butterflies Don't Lie"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
122 BPM a bar is 1.97 s, so most shots are 2–4 s and the choruses cut on the
bar.

## 1. Visual style

Candy-bright and deliberately over-saturated, shot in real daylight rather
than graded into a fantasy. Yellows, pinks, a hard blue sky, one sunflower
that carries the whole color scheme. **The rule of the video is that her
face and body are always telling the truth while her mouth is not** — every
denial line is paired with a shot of her hands, ears, knee or heart rate. One
sequence, and only one, is cool and blue: the bedroom and the corner in the
cold. Everything else is warm. Handheld, close, alive; the only unreal beat
in the film is the sunflower turning.

| Section | Grade | Camera |
|---|---|---|
| Intro | Hard clean daylight, candy color | Overhead, then slow motion |
| Verse 1 | Warm daylight, color-popped | Handheld, fast cuts on the beat |
| Pre-choruses | Daylight narrowing to one warm shaft | Static, macro inserts |
| Choruses | Peak saturation, yellows and pinks | Moving, wide, choreographed |
| Post-choruses | Hard bright, high contrast | Half-second impact cuts |
| Verse 2 | Cool blue bedroom, then cold street with warm windows | Still, then handheld |
| Instrumental | Saturated, then one flat white frame | Loose handheld, then locked |
| Bridge | Warm, soft, background gone quiet | One long unbroken take |
| Final chorus | Brightest in the video | Wide, crane-style, moving |
| Outro | Intro daylight, one stop warmer | Matched overhead, then close |

## 2. Character bible — paste into every prompt

**Mahima** (café and street, the main look)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair loose with a claw clip half in it, fresh glowy makeup with a warm pink lip, wearing a butter-yellow cropped cardigan over a white top and wide-leg jeans, bright animated expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the bedroom and the cold corner, the one cool sequence)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair down and slightly flat, no makeup, wearing a grey ribbed long-sleeve top and pyjama shorts, then the same top under a big navy coat outdoors, uncertain private expression, realistic cinematic photography, consistent identity

**Kai** (the male lead, seen properly only from verse two on)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a rust-orange overshirt over a plain tee and dark jeans, holding two takeout coffee cups, warm slightly awkward expression, realistic cinematic photography, consistent identity

**The three friends** — young women in their early twenties, distinct from
each other and from Mahima: one with a short blunt bob and gold hoops, one
with box braids and round glasses, one with a shaved-side crop. They have
faces, they have opinions, and they are in almost every café frame.

**The waiter** — a man in his fifties with a jug of water, sincerely
concerned, in exactly two shots.

Objects: the **sunflower in a jam jar**, the **three iced coffees and one
untouched shared plate**, the **smartwatch**, the **shredded paper napkin**,
the **two takeout cups**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All phone screens, the group chat, the typed and deleted message, the
smartwatch face and any café signage are composited in the edit.** Generate
the phone and the watch as lit blank screens and overlay the UI in post — the
model cannot render legible interfaces, and the watch's heart-rate reading is
one of this video's best frames.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in both looks and Kai with IP-Adapter or a character LoRA, and
lock the three friends too — they recur more than Kai does and drifting faces
would be obvious. Keyframes first; OpenPose for the booth dancing, the spin
out of the doorway and the street choreography; Depth for the café interior
so the window light stays behind the table. 16:9 first; 9:16 for the chorus
and post-chorus cuts. Animate in short bursts: a napkin being shredded, a
knee bouncing, ice cracking, one turn of a flower. The sunflower rotation is
a single slow 2 s clip and should be the most carefully rendered shot in the
video.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–4 s; the post-chorus impact shots 0.5 s.

## 4. Scene per lyric line

### Intro — the table

1. *"Table for four on a Saturday, sun through the glass"* — overhead of a café window table: three tall iced coffees, one untouched shared plate, a sunflower in a jam jar, four pairs of hands, hard clean daylight.
2. *"I said his name like it was nothing and the whole table laughed"* — Mahima mid-sentence, deliberately casual, then three heads turning toward her at once in slow motion, wide.
3. *"Three iced coffees and a plate we're all pretending to share"* — macro travelling across the table: condensation on a glass, a fork nobody is using, the plate, the flower.
4. *"And I'm suddenly the only one who's going pink in here"* — close-up on her face and the tips of her ears, the color arriving, her trying to drink through it.

### Verse 1 — the defence and the evidence

5. *"I said it's nothing, honestly, we're only talking a bit"* — Mahima making a very reasonable point with a fork in one hand, handheld, fast.
6. *"He texted twice this morning and I haven't answered it"* — her phone face-down beside the plate, lit with two waiting messages (UI composited), her hand covering it without looking.
7. *"Then somebody says his name a second time out loud"* — the friend with the bob leaning in and saying it again, deadpan, close-up.
8. *"And the sunflower on the table turns around to look at me"* — the sunflower in the jar rotating a few degrees toward her, slow, the only unreal beat in the video, macro.
9. *"My watch buzzes, tells me that my heart rate's high for sitting"* — extreme close-up of the smartwatch on her wrist flashing a high reading (UI composited), her other hand covering it a beat too late.
10. *"The waiter asks if I'm alright and I say I'm doing fine"* — the waiter paused with a water jug, genuinely concerned; her giving a very bright thumbs up, medium two-shot.
11. *"The group chat has the receipts and the receipts run long"* — a phone held up across the table, a chat scrolling far too fast to read (UI composited), three friends leaning in.
12. *"Somebody kept a screenshot of the things I said in June"* — a screenshot held at arm's length toward camera (composited), her reaching for it and missing.
13. *"And they read the whole thing back to me in my own voice"* — one continuous take on her face going through four emotions while a friend reads aloud off-screen, close-up.

### Pre-chorus 1 — the last stand

14. *"I can talk my way around it, I can argue it to death"* — Mahima building an argument with both hands, the café defocusing behind her, static medium.
15. *"I had fourteen good excuses and I'm somewhere down to nine"* — the three friends in a row, unimpressed, one blinking slowly, wide.
16. *"But my hands are on the table doing something on their own"* — macro on her fingers shredding the corner of a paper napkin into a small pile without her noticing.
17. *"And nobody has to ask me, they can watch me lose the line"* — the light narrowing to one warm shaft across the table, her smile breaking through mid-sentence, slow push-in.

### Chorus 1 — the drop

18. *"My mouth says maybe"* — all four of them coming up out of the booth on the beat, color at maximum, wide handheld.
19. *"But butterflies don't lie"* — Mahima spinning out from the table into a sunlit doorway, arms out, tracking.
20. *"I can hold it together in a room full of people"* — the four of them dancing in a line in the café aisle, other customers unbothered, wide.
21. *"I just can't hold it together on the inside"* — macro: goosebumps rising along her forearm in real time.
22. *"Ask the goosebumps, ask the shaking in my knee"* — under the table: her knee bouncing at double speed, low angle.
23. *"Ask whoever's running things down there instead of me"* — her hand flat on her own stomach, close-up, everything else moving around her.
24. *"I get one vote in this body and I lose it every time"* — a wide of the four of them crossing the street in a line, perfectly on the beat, hard sun.
25. *"My mouth says maybe"* — Mahima to camera, mouthing it, one shoulder shrugging, close-up.
26. *"But butterflies don't lie"* — the sunflower in the jar, back-lit and blazing yellow, macro.

### Post-chorus 1 — chant

27. *"Don't lie, don't lie, they never learned how"* — half-second: a hand slapping the table, the glasses jumping.
28. *"Don't lie, don't lie, and they're telling on me now"* — half-second: three friends pointing at her at once.
29. *"Don't lie, don't lie, they never learned how"* — half-second: her grin caught mid-denial.
30. *"My mouth says maybe but the butterflies are loud"* — half-second: the sunflower, hard flash of yellow.

### Verse 2 — the bedroom and the corner

31. *"Tuesday, he asks if I'm free and I typed out a no"* — cool blue: Mahima (second look) lying across a bed holding the phone above her face, evening light, overhead.
32. *"Sat and read it for a minute and I let it go"* — extreme close-up of a thumb hovering over a send button (UI composited), not pressing.
33. *"Deleted every letter, wrote a yes with a little too much"* — the message typed, deleted and typed again (composited), her face lit blue from below.
34. *"Took the mark off, put it back, then took it off again"* — macro on the thumb making one tiny edit, twice, then a third time.
35. *"Forty minutes on a message that was two letters long"* — a wall clock in three cuts moving forty minutes while nothing else in the room changes.
36. *"Thursday he was early, on the corner in the cold"* — Kai on a street corner with two takeout cups, breath visible, checking the time, wide, cold blue with warm store windows behind.
37. *"Two coffees and my order right and I had never told him"* — close-up of one cup held out, then her face registering that it is exactly her order.
38. *"I had a whole speech ready about keeping this thing light"* — Mahima rounding the corner and stopping dead for one beat, medium, her mouth already open.
39. *"Then my body walked me over there before I said a word"* — low angle on her feet starting to move before anything else does, then the two of them meeting, no speech happening.

### Pre-chorus 2 — back at the table

40. *"I could talk my way around it, I could argue it all week"* — warm daylight returns: Mahima mid-argument with a coffee cup for emphasis, same table, different day.
41. *"I had fourteen good excuses and I'm down to about two"* — the friend with the braids holding up two fingers without looking up from her phone.
42. *"But my face went and answered while my mouth was still deciding"* — slow push-in on her face as the smile arrives without permission, close-up.
43. *"And the girls don't say a word, they let me dig myself through"* — the three of them in a row saying absolutely nothing, wide, holding two beats longer than comfortable.

### Chorus 2 — outdoors

44. *"My mouth says maybe"* — the four of them coming out of the café door onto the sidewalk on the beat, wide.
45. *"But butterflies don't lie"* — Mahima spinning past a fruit stall, color everywhere, tracking.
46. *"I can hold it together in a room full of people"* — the four moving through a market in a line, stall-holders unbothered, handheld.
47. *"I just can't hold it together on the inside"* — reuse shot 21, tighter, the goosebumps in harder sunlight.
48. *"Ask the goosebumps, ask the shaking in my knee"* — her foot tapping on a bus stop curb at double speed, low angle.
49. *"Ask whoever's running things down there instead of me"* — her hand on her stomach again, this time laughing, close-up.
50. *"I get one vote in this body and I lose it every time"* — a crane-style pull back over a pedestrian crossing, the four of them small and dancing in the middle of it.
51. *"My mouth says maybe"* — reuse shot 25, wider, the market behind her.
52. *"But butterflies don't lie"* — a whole bucket of sunflowers at a flower stall, one being lifted out, macro.

### Instrumental — the room dancing

53. The four friends dancing badly and joyfully in the café doorway, one long loose handheld take.
54. The waiter joining in for exactly one beat and then going back to work, medium.
55. Macro: ice cracking and shifting in a glass, the sound cue for the chopped vocal.
56. Mahima alone and completely still in the middle of the moving crowd, one hand on her stomach, slow push-in.
57. Hard cut to a single flat white frame for the half-bar of silence — the cut into the bridge.

### Bridge — she says it

58. *"Fine. Fine. You want it slow and out loud"* — one unbroken medium close-up begins: Mahima across the table, no cuts, warm soft light, the café gone quiet behind her.
59. *"I like him. I like him. I have liked him since the fourth of March"* — the same unbroken take continues, her hands finally still on the table.
60. *"I like the way he listens with his whole entire face"* — two-second insert: Kai listening to someone off-camera with his entire face, unposed.
61. *"I like that he remembered something I said and didn't mean"* — two-second insert: Kai holding a small object out toward camera, whatever it is deliberately unclear.
62. *"I like that he is not smooth about it, not at all"* — two-second insert: Kai dropping a coffee cup lid and laughing at himself, unflattering and warm.
63. *"So take the plate away, I'm not eating anything"* — back on her; a friend's hand slides the untouched shared plate out of frame without a word.
64. *"I have got a stomach full of something with a mind of its own"* — the unbroken take ends on her exhaling, relieved, still, close-up.

### Final chorus — the biggest version

65. *"My mouth says maybe"* — the four of them dancing on the sidewalk with strangers clapping along, widest shot in the video.
66. *"But butterflies don't lie"* — Mahima spinning down the middle of the street, arms out, tracking backwards.
67. *"I said it out loud in a room full of people"* — the café through the window from outside, everyone inside on their feet, static wide.
68. *"And the ceiling didn't fall out of the sky"* — low angle straight up at a clean blue sky and a completely intact awning, held two beats.
69. *"Ask the goosebumps, ask the shaking in my knee"* — reuse the goosebumps macro, in full sun, the brightest version.
70. *"Ask whoever's running things down there instead of me"* — her hand on her stomach, then opening out toward the corner where Kai is waiting, close-up.
71. *"I got one vote in this body and I finally let it go"* — her walking toward the corner, still dancing, the friends falling back behind her, tracking.
72. *"My mouth said maybe"* — Mahima and Kai in the same frame in full daylight for the first time, both slightly embarrassed, medium two-shot.
73. *"But the butterflies were right"* — the two of them, and behind them the three friends visibly celebrating, wide, sun flare.

### Post-chorus 2 — chant on the street

74. *"Don't lie, don't lie, they never learned how"* — half-second: clapping hands in a row.
75. *"Don't lie, don't lie, and they're telling on me now"* — half-second: her shoes on the sidewalk, mid-step.
76. *"Don't lie, don't lie, they never learned how"* — half-second: the sunflower being carried out of the café.
77. *"My mouth said maybe but the butterflies were loud"* — half-second: two takeout cups touching.

### Outro — the bookend

78. *"Table for four on a Saturday, sun through the glass"* — the identical overhead from shot 1, matched exactly, one week later, one stop warmer.
79. *"I said his name like it was something and the whole table clapped"* — the same three friends applauding around the same table, the sunflower still there, wide.
80. *"Same iced coffee, same plate that we never share"* — the overhead again: four cups now instead of three, the plate still untouched, macro pull.
81. *"And I'm the only one still smiling like an idiot in here"* — final shot: her face, smiling, not hiding it, phone face-up beside her, locked off, hold through the fade. No text.

## 5. Edit and the challenge

Markers at: the first overhead, the sunflower turn, the watch buzz, each
*"butterflies don't lie"*, the cold-corner cut, the instrumental, the white
frame, the start of the unbroken bridge take, and the matched overhead in the
outro. At 122 BPM a bar is 1.97 s; the choruses cut on the bar and the
post-chorus chants cut on the half-bar.

**The heart-rate challenge.** The shareable cut is the vertical chorus, shots
18–26, opening on the smartwatch reading. Invite people to post their own
high-heart-rate screenshot with the name blurred, cut on the drop. The second
shareable frame is the sunflower turn (shot 8), which loops perfectly on
its own.

## 6. Quality-control checklist

- Two Mahima looks in the right sections: butter-yellow cardigan everywhere except shots 31–39, which are the only cool-graded shots in the film
- The three friends are distinct from each other and identical to themselves in every café frame; Kai does not appear in a clear shot before shot 36
- Every denial line is cut against a body-truth insert — hands, ears, knee, stomach, goosebumps, watch — with no exceptions
- The sunflower turn is the only unreal beat; nothing else in the video breaks physics
- All phone screens, the group chat, the typed message and the watch face composited in the edit; no model-generated text
- The bridge is one unbroken take on her face apart from the three inserts, and the inserts never cut back to her mid-sentence
- No distorted hands in the napkin, thumb, cup and stomach close-ups
- Shots 1 and 78 are the same framing, lens and height so the bookend cut reads as intentional; the last shot is locked off and holds through the fade
