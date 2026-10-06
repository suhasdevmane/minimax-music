# Golden Hour on Your Skin

**Status: written and verified, NOT rendered. Not yet in the queue.**

Thirteenth song. Female lead **Mahima**, dreamy pop / sun-drenched bedroom
pop with shimmering synths, a soft 808 and harp flourishes, 96 BPM, E major.
Same singer as songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 618 sung words, ballad/mid class, no trimming needed |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 96 BPM, E major, no modulation, the harp-and-shimmer instrumentation and the camera-shutter ear candy per the submission. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 79 entries — built from the submission's scene direction, plus a three-look character bible, Kai as the male lead, the phone-she-never-uses motif, workflow, golden-hour challenge, QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 13-golden-hour-on-your-skin
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\13-golden-hour-on-your-skin\caption.txt `
  --lyrics-file songs\13-golden-hour-on-your-skin\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\13-golden-hour-on-your-skin\output\golden_hour_on_your_skin.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks around *"here, my queen"* removed; commas instead | Punctuation is not sung, and the model reads quotes unpredictably |
| *7:40* → *"Seven forty"*, *7:30* → *"half past seven"*, *4 p.m.* → *"grey at four"* | The model sings digits unpredictably |
| The descriptive tag lines (`[intro – soft, close…]`, `[final chorus – fullest…]`) reduced to plain tags; the final chorus is a plain `[chorus]` | Only the plain section tags exist |
| Repeated choruses written out in full | The model would sing "(repeat)" |
| **Craft pass:** verse 2's last line, *"The one I'd hang above the door if you could frame a day"* → *"...if a day could stay the same"* | Both verses run in rhyming couplets and verse 2's fourth couplet was the only one that didn't rhyme (*frame / day*). *Same* answers *frame* and keeps the wistful conditional intact |

Kept exactly as written: every other line, 96 BPM, E major, the
instrumentation, the mood arc. No trimming was needed — 619 words fits.

## The story and the hooks

Twenty minutes before sunset on a rooftop car park, he's leaning on the
bonnet with his eyes half closed and she can't stop looking. A can of
lemonade, a story he's told before, dust floating in the light, freckles.
She raises her phone and lowers it, because a camera never gets him right.
Then a field, a dandelion crown, a back road with the windows down, the car
pulled onto the shoulder just to catch the light. In the bridge she imagines
winter, the grey light at four, and realises it was never the sun. She
finally takes the photo in the post-chorus. The sun goes under, the
streetlights come on, and he's still glowing.

**The hook:** *"Golden hour on your skin, and I'm falling all over again"* —
visual, warm, caption-ready.

**The line for captions:** *"Golden hour's just the hour I remember to look
at you."*

**The turn:** *"Cause it was never really the sun, it was you."*

**The quote:** *"A camera never gets you the way I do."*

**Why it can travel:** golden-hour couple reels are already a format; this
gives them a hook at the tempo they cut at, a challenge (film them at the
same twenty minutes for a week), and a still frame at the end that people
will screenshot.

## Lyrics as they will be sung

```
[intro]
Twenty minutes till the sun goes down,
The whole sky turning honey brown.
You're leaning on the car with your eyes half closed,
And I swear the light knows something I don't know.

[verse]
Seven forty on a Thursday, rooftop, no plans,
Warm can of lemonade sweating in your hands.
You're telling me a story that you've told before,
But the way the sun hits your jaw, I want to hear it more.
Dust in the air like it's floating on purpose,
Every little freckle coming up to the surface.
I've got a hundred pictures that I never take,
Cause a camera never gets you the way I do, babe.

[pre-chorus]
And I know it only lasts a little while,
The light, the heat, the way you smile.
But if this is all I ever get to keep,
Then let me stand here till it sinks beneath the street.

[chorus]
Golden hour on your skin,
And I'm falling all over again.
Every day the sun comes down,
And every day you pull me in.
Golden hour on your skin,
Like the light was made to fit you in.
I've loved you in the dark, I've loved you in the noon,
But nothing hits like you at half past seven in June.
Golden hour on your skin,
And I'm falling all over again.

[verse]
Sunday in the field where the long grass leans,
You made a crown of dandelions, said, here, my queen.
We drove the back roads with the windows wide,
Pulled over on the shoulder just to catch the light.
You sat up on the bonnet with your shoes kicked off,
Talking about nothing till the nothing felt like love.
And I thought, this is it, this is the frame,
The one I'd hang above the door if a day could stay the same.

[pre-chorus]
And I know the sun's already on its way,
It's got a whole other side of the world to save.
But if it's leaving, let it leave me slow,
Let me memorise the colour of your skin before it goes.

[chorus]
Golden hour on your skin,
And I'm falling all over again.
Every day the sun comes down,
And every day you pull me in.
Golden hour on your skin,
Like the light was made to fit you in.
I've loved you in the dark, I've loved you in the noon,
But nothing hits like you at half past seven in June.
Golden hour on your skin,
And I'm falling all over again.

[instrumental]

[bridge]
And when the winter comes and the sky goes grey at four,
And the light's a cold thing coming through the door,
I'll close my eyes and it's July again,
Rooftop, back road, you and the honey light, and then
You'll look at me the way you're looking now,
And I'll fall, I don't know how, but I'll fall somehow.
Cause it was never really the sun, it was you,
Golden hour's just the hour I remember to look at you.

[chorus]
Golden hour on your skin,
And I'm falling all over again.
Every day the sun goes down,
And every day I let you in.
Golden hour on your skin,
Every line and every grin.
I've loved you in the dark, I've loved you in the noon,
But nothing hits like you at half past seven in June.
Golden hour on your skin,
And I'm falling all over again.

[post-chorus]
Falling, falling, all over again,
Falling, falling, all over again.
Turn your face into the light, don't move,
Let me keep this one of you.

[outro]
The sun's gone under, the sky's gone blue,
Streetlights blinking on, nothing left to do.
But you're still glowing like the sun forgot to leave,
Guess I carry golden hour with me.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 619 → ~5.3 min at 116 wpm, 89% of frame cap |
| Caption + lyrics tokens | 2122 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
