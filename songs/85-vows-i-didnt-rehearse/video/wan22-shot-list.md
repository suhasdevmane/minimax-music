# Wan 2.2 Shot List — "Vows I Didn't Rehearse"

**One shot per lyric line**, built from the scene-by-scene direction in the
submission. Timestamps come from the rendered WAV; cut on the sung line. At
84 BPM a bar is 2.86 s, so most shots run one to two bars and nothing in this
video cuts faster than the music.

## 1. Visual style

One back garden, one afternoon, shot on long lenses from where a guest would
actually be sitting. The whole film runs on a single light curve: the sun
drops visibly from late afternoon through the golden fifteen minutes into
blue hour, and it never goes back up. Everything else — the four months of
drafts, the kitchen sink, the road, the hospital corridor — is a flashback,
and every flashback is cooler and flatter than the garden it interrupts.

Two rules. The **paper** is the brightest object in any frame it appears in,
until it is in the grass, and then it is the dullest. And the camera never
moves toward anything sad — the hospital shot is at floor level and leaves
before anything happens.

| Section | Grade | Camera |
|---|---|---|
| Intro (the drafts) | Spring window light, bedside lamp, morning white | Static tabletop, mirror two-shot |
| Verse 1 | Late-afternoon garden, low and long | Macro on the paper, then wide |
| Pre-choruses | Same warm garden, crowd in slight shade | Static, patient, long lens |
| Choruses | Golden, flaring at frame edges | Slow arc, open hands |
| Verse 2 (flashbacks) | Flat road daylight, cold fluorescent, warm windscreen | Locked-off, low, respectful |
| Instrumental | Sun visibly dropping across four shots | Locked-off details, one wide |
| Bridge | Even and cold for the false version, one-sided gold for the real one | Static, unblinking |
| Final chorus | Last gold going blue, house practicals coming on | Wide, everyone moving |
| Post-chorus | Blue hour, one string of bulbs | Handheld, easy |
| Outro | One house window at night, then a warm later kitchen | Macro, then locked-off |

## 2. Character bible — paste into every prompt

**Mahima** (the drafts, four months before)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair tied back loosely, no makeup, wearing a grey sweatshirt and pyjama shorts, concentrating slightly frustrated expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the ceremony)
> Same female protagonist Mahima, young woman in her early twenties, expressive dark eyes, oval face, long dark wavy hair half-pinned with loose strands at the temples, soft natural makeup, wearing a simple ivory cotton wedding dress with short sleeves and no train, bare arms, open frightened then steady expression, realistic cinematic photography, consistent identity, natural skin texture

**Mahima** (the outro, years later)
> Same female protagonist Mahima, woman in her late twenties, expressive dark eyes, oval face, long dark wavy hair loose, no makeup, wearing a plain green t-shirt, calm unhurried expression, realistic cinematic photography, consistent identity, natural skin texture

**Kai** (the groom)
> Same male character Kai, man in his late twenties, close-cropped dark hair, short beard, athletic build, wearing a slightly ill-fitting rented navy suit with the sleeve label still faintly visible at the cuff, no tie, laughing openly with his whole face, realistic cinematic photography, consistent identity

The rest of the garden is thirty guests and stays that way: **the officiant**
(an ordinary friend in a jacket holding a printed script), **his mother**
(front row, a folded tissue in both hands), **the crying plus-one at the
back**, **a small dog trailing a lead**. Keep them at long-lens distance or in
profile; none needs a locked identity. There are no exes in this video and no
one from her past appears at all.

Objects that repeat: the **sheet of paper** — drafted, folded in fours, slid
into a sleeve, softened in a fist, dropped in the grass, trodden on, picked up
at the gate, filed in a drawer — the **jar of wildflowers**, the **white
folding chair** that blows over and is never righted, the **porch light**, the
**rented-suit cuff**.

**Always append:**
> no text, no subtitles, no watermark, no extra fingers, no duplicate people, stable facial identity

**Negative prompt (every generation):**
> bright colors, overexposed, static, blurry details, subtitles, style, artwork, painting, picture, still, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards, text, watermark, logo

**All handwriting, the index cards, the officiant's script and the drafts on
the page are composited in the edit.** Generate the paper as a blank sheet
with real creases and grass stains and lay the handwriting in afterwards — the
model cannot render legible script, and the crossed-out line in shot 67 is the
last beat of the story.

## 3. Wan 2.2 workflow

Image-to-video, not text-to-video. One approved still per shot, then animate.
Lock Mahima in all three looks and Kai in his one look with IP-Adapter or a
character LoRA each. This video's difficulty is not motion, it is **hands and
paper**: a sheet being folded in fours, a corner worried until the fibres go
furry, a fist closing on softened paper. Generate every paper close-up at
macro scale with a pose reference for the hands, and expect to discard more
takes here than anywhere else in the batch.

Keyframes first; Depth for the seated crowd on grass, which the model will
otherwise duplicate into rows of clones — generate the crowd as a plate and
composite her in for the wide shots. OpenPose only for the standing ceremony
two-shots and the final chorus crowd rise. 16:9 throughout; 9:16
recomposition for the paper macros and the officiant lowering the script,
which are the two vertical cuts.

Animate small: a page corner curling, a dog crossing frame, a chair going over
in wind, a tissue being finally used, a porch light coming on. Nothing in this
film needs a big move.

| Model | Resolution | Frames | FPS | Steps | CFG |
|---|---|---|---|---|---|
| Wan2.2 I2V-A14B | 1280×720 | 81 | 16 | 30–40 | 4–5 |
| Wan2.2 TI2V-5B | 1280×704 | 121 | 24 | 30–40 | 4–5 |

Most shots 3–6 s.

## 4. Scene per lyric line

### Intro — four months of drafts

1. *"I wrote it out in April, I rewrote it in June,"* — a kitchen table strewn with index cards and a pen, spring window light, static tabletop, a hand adding one more card.
2. *"Read it to the mirror till the mirror got bored."* — Mahima (drafts look) at a bedroom mirror mouthing words with no sound, then stopping mid-sentence and looking at herself, warm bedside lamp.
3. *"Folded it in fours and I slid it in my sleeve,"* — macro: a single sheet folded in half, in half again, and pushed inside a sleeve, morning white light.
4. *"And I never looked at it again."* — the same table, now almost bare, one sheet gone from it, locked-off, held.

### Verse 1 — the paper fails

5. *"Here's what the paper said, it said that you are kind,"* — the ceremony, standing: the folded sheet coming out of her sleeve, macro, late-afternoon garden light.
6. *"Which is true and useless, everyone's kind on paper."* — macro of her own handwriting on the opened page (composited), slightly out of focus at the edges.
7. *"It said something about oceans, it said something about time,"* — her eyes tracking down the page, then flicking up and back down, extreme close-up.
8. *"It was good, it was fine, it would have made them cry."* — a wide of thirty people on white folding chairs on grass, waiting, long lens, nobody moving.
9. *"But my hands went stupid and the paper went soft,"* — her thumb working a corner until the fibres go furry, then the whole sheet creasing in her fist, macro.
10. *"And I looked up and the whole speech left the yard."* — her eyes coming up off the page for the first time, the paper dropping out of focus at the bottom of frame, close-up.

### Pre-chorus 1 — the garden refuses to be solemn

11. *"So the wind took a folding chair, the dog got loose,"* — a white folding chair going over in the wind at the back of the rows, nobody getting up to fix it, static wide.
12. *"And your mother has a tissue she has not used yet."* — an older woman in the front row holding a folded tissue in both hands, not using it, close-up.
13. *"Everybody's waiting on the girl with the paper,"* — a small dog trailing a lead, walking unhurriedly across the grass between the chairs, long lens.
14. *"And the girl with the paper's got nothing left."* — the whole seated crowd from her eyeline, silent and patient, and every face turned to camera.

### Chorus 1 — the vows, with evidence

15. *"These are the vows I didn't rehearse,"* — Mahima in the garden, hands empty at her sides, not reading, medium, golden light.
16. *"The ones that came sideways, the ones that came first."* — her hands opening as she talks, palms up, close-up, the paper no longer in them.
17. *"You do the dishes when I'm three days low,"* — flashback: a kitchen sink at night, his hands in it, her sitting on the counter behind him not talking, one warm overhead in a dark room.
18. *"You say my name like it's somewhere to go."* — flashback: a hallway, his voice from another room, her head lifting from a book, close-up.
19. *"I don't have a metaphor, I don't have a line,"* — back to the garden, a slow push toward her face, everything else falling away.
20. *"I've got a man in a rented suit and the rest of my life."* — a close-up of the rented-suit cuff with the sleeve label still faintly visible, then a tilt up to Kai's face.
21. *"Every word I wrote down was somebody else's first,"* — the dropped paper lying in the grass beside her shoe, insert, dull against the gold.
22. *"So these are the vows I didn't rehearse."* — a two-shot of both of them, her talking, him listening, long lens, warm.

### Verse 2 — what she actually says

23. *"So I told them about the Tuesday the car gave up,"* — flashback: a car on a shoulder with the hood up, flat road daylight, locked-off wide.
24. *"How you walked two miles back with a coffee going cold."* — a small figure walking a long straight road toward camera carrying two cups, long lens, heat shimmer.
25. *"I told them what you said in the hospital hallway,"* — a hospital corridor at floor level: two pairs of shoes side by side on plastic chairs, nothing else, cold fluorescent, no faces.
26. *"Which I'm not repeating, that one's ours to keep."* — hold the same floor-level frame, then cut away before anything happens, back to the garden.
27. *"I told them that you sing badly and you sing anyway,"* — flashback: a car interior at a red light, Kai singing badly and confidently, warm windscreen sun, close-up.
28. *"I said I've watched you choose me on days I was hard to choose,"* — the garden: the crowd's faces changing as she goes, a slow pan across the front row.
29. *"And that's the only promise I know how to make."* — Mahima, close-up, steady for the first time in the film, no shake in her at all.

### Pre-chorus 2 — the room stops moving

30. *"The man with the script has let it fall to his side,"* — the officiant, an ordinary friend in a jacket, letting a printed script drop to his side and simply listening, medium.
31. *"And the folding chairs have stopped their little noise."* — thirty people completely still on chairs that were creaking a minute ago, wide, long lens, the golden light at its lowest.
32. *"Somebody's crying in the back who isn't even family,"* — a plus-one at the back crying openly and slightly embarrassed about it, close-up.
33. *"And you're laughing at me with your whole face."* — Kai laughing with his whole face and not wiping his eyes, close-up, the warmest frame in the video.

### Chorus 2 — the whole garden inside it

34. *"These are the vows I didn't rehearse,"* — a slow arc beginning around the two of them, the seated crowd wheeling past behind, flaring at the frame edge.
35. *"The ones that came sideways, the ones that came first."* — the arc continuing, her hands moving while she talks, medium.
36. *"You do the dishes when I'm three days low,"* — reuse the kitchen sink from shot 17, wider, both of them in frame this time.
37. *"You say my name like it's somewhere to go."* — reuse the hallway from shot 18, tighter, her already halfway out of the chair.
38. *"I don't have a metaphor, I don't have a line,"* — the arc completing behind her, the whole garden and fence line passing through frame.
39. *"I've got a man in a rented suit and the rest of my life."* — their hands finding each other, close-up, both sets shaking slightly.
40. *"Every word I wrote down was somebody else's first,"* — the paper in the grass again, an ant walking across it, macro.
41. *"So these are the vows I didn't rehearse."* — the two of them from the back of the garden, small in a wide frame, the crowd between camera and them.

### Instrumental — the garden, existing

42. The jar of wildflowers on a card table, macro, the light noticeably lower than it was.
43. The loose dog lying down at the end of a row of chairs, static.
44. The blown-over folding chair, still on its side, nobody having fixed it, locked-off.
45. The tissue, finally used, close-up on the older woman's hands.
46. A wide from the back fence: the whole garden, thirty chairs, two small figures at the front, the sun visibly on the horizon.

### Bridge — the version that would have been a lie

47. *"There's a version of today with the paper read out perfect,"* — a two-second insert shot like a commercial: the same wedding, posed, the paper read smoothly, colour cooler and light too even.
48. *"Clean and quotable, a good line for a frame."* — the false version continuing: a perfect symmetrical wide, everyone placed, nobody sweating.
49. *"And it would have been beautiful and it would have been a lie,"* — hard cut back to the real one, warmer, messier, half her face in shadow.
50. *"Because nothing about us has ever come out clean."* — her mid-sentence, genuinely losing her thread, stopping, close-up, no music underneath.
51. *"So take the mess, take the sentence that fell over,"* — her starting again badly and carrying on anyway, the same unbroken close-up.
52. *"Take the girl who lost her place and found it out loud."* — hold the same frame all the way to the end of the line, then a string swell lifts it.

### Final chorus — the lift

53. *"These are the vows I didn't rehearse,"* — the two of them holding both hands, wide, last gold going blue at the edges.
54. *"The ones that came sideways, the ones that came first."* — the crowd standing, chairs scraping back on grass, everyone moving at once.
55. *"I will not be easy and I will not be far,"* — the dog running through the middle of the standing crowd, low angle, delighted chaos.
56. *"I'll be the light left on when you pull in the yard."* — a porch light on at dusk seen from a car pulling in, headlights swinging across it, locked-off.
57. *"I don't have a metaphor, I don't have a line,"* — back to the garden, first practicals coming on in the house behind the crowd.
58. *"I've got a man in a rented suit and the rest of my life."* — Kai's face, close-up, entirely undone.
59. *"For better, for worse, for the paper in the dirt,"* — the paper still in the grass with feet stepping around it, insert.
60. *"These are the vows I didn't rehearse."* — a full wide of the garden with everyone standing and the sky going blue, held.

### Post-chorus — the reception starts itself

61. *"Not a word of it written, not a word of it wrong,"* — folding chairs being pushed back into a rough circle on the grass, handheld, blue hour.
62. *"I found it in my chest where it had been all along."* — a hand pressing a palm flat against a sternum, held, close-up.
63. *"Not a word of it written, not a word of it wrong,"* — a string of bulbs coming on over a table, and the guests singing along badly, medium.
64. *"And the paper's in the grass and I'm still going on."* — the paper being trodden into the grass by somebody dancing, unnoticed, low insert.

### Outro — the drawer

65. *"They found it in the grass by the gate,"* — a hand picking a damp grass-stained sheet up by the gate at night, lit by one house window, macro.
66. *"Three drafts and an arrow and a line crossed out twice."* — the page held flat and open: drafts, an arrow, a line crossed out twice (all composited), macro.
67. *"It lives in a drawer and I've never read it since,"* — years later: a kitchen drawer opening, the same page flat under other papers, and closing again, close-up, warm ordinary light.
68. *"I already said the true one out loud."* — final shot: Mahima (outro look) at the sink in that later kitchen, not looking at the drawer, a porch light on through the window behind her, locked-off, held through the fade. No text.

## 5. Edit and the challenge

Markers at: the first guitar note, the paper coming out of the sleeve (shot
5), the fist closing on it (shot 9), each *"vows I didn't rehearse"*, the
officiant lowering the script (shot 30), the instrumental, the false-version
cut (shots 47–49), the modulation into shot 53, the paper being trodden in
(shot 64), and the last frame. At 84 BPM a bar is 2.86 s; nothing cuts faster
than one shot per bar anywhere in this film, and the bridge holds a single
frame for four bars.

**The unread-vows challenge.** Post the vertical cut of shots 5–10 — the
paper coming out, going soft, being abandoned — under *"these are the vows I
didn't rehearse"* and invite people to post the moment their own speech went
off-script: wedding footage, best-man speeches, toasts, eulogies. The
officiant lowering the script (shot 30) is the still image that carries the
caption, and the paper in the grass with the ant (shot 40) is the loop.

## 6. Quality-control checklist

- Three Mahima looks in the right sections: sweatshirt only in shots 1–4, the ivory dress from shot 5 to shot 64, the green t-shirt only in shots 67–68
- The paper is the brightest object in every frame until shot 21, and the dullest in every frame after it
- The sun drops monotonically across the film and never comes back up; the false-version insert in shots 47–48 is the only cool-graded garden footage
- The hospital shot stays at floor level, shows no faces, and cuts away before anything happens
- All handwriting, index cards and the officiant's script are composited; no model-generated lettering anywhere
- Crowd wides are generated as plates with Mahima composited in — check for duplicated guests in every row
- The blown-over chair is never righted; the dog appears in shots 11, 13, 43 and 55 and nowhere else
- Hands on all paper macros checked frame by frame; no fused or extra fingers on the fist close-up
- The last shot is locked-off, the drawer is not reopened, and it holds until the audio fades
