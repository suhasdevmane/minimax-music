# Call Me After Midnight

**Status: written and verified, NOT rendered. Not yet in the queue.**

Song forty. Female lead **Mahima**, synth-R&B with eighties production —
analogue polysynths, gated reverb snare, chorused bass — flirty, low and
confident, US register. 96 BPM, C♯ minor, ballad/mid pacing. Same singer as
songs 1–8.

Source of record: [`source/original-submission.md`](source/original-submission.md) —
the song and its scene-by-scene direction exactly as submitted.

## Files

| File | Purpose |
|---|---|
| [`lyrics.txt`](lyrics.txt) | Render-ready lyrics — 640 sung words |
| [`caption.txt`](caption.txt) | Music description. `Vocal Details` and `Sonics` byte-identical to song 1 — the voice lock. 96 BPM, C♯ minor, the gated snare's first entry pinned to the end of pre-chorus one, the half-time electric-piano bridge and the dial-tone textures. |
| [`video/wan22-shot-list.md`](video/wan22-shot-list.md) | **One scene per lyric line** — 71 entries — with a two-look character bible, the never-show-the-man rule, the corded-landline motif, the day-versus-neon grade rule, workflow and QC checklist |
| `source/` | Original submission |
| `output/` · `logs/` | Render lands here |

## Render (when queued)

```powershell
.\.venv\Scripts\python.exe scripts\render_queue.py 40-call-me-after-midnight
```

or directly:

```powershell
.\.venv\Scripts\python.exe scripts\generate.py `
  --prompt-file songs\40-call-me-after-midnight\caption.txt `
  --lyrics-file songs\40-call-me-after-midnight\lyrics.txt `
  --duration 355 --seed 42 `
  --out songs\40-call-me-after-midnight\output\call_me_after_midnight.wav
```

Expected ~2 h.

## What changed from the submission

| Change | Why |
|---|---|
| Quotation marks and em-dashes removed throughout | Punctuation is not sung; the model reads the lyric body literally |
| Digits spelled as words (*twelve o'clock*, *nine to six*, *three time zones*, *half past two*, *six in the morning*) | The model sings digits unpredictably |
| Descriptive tag lines (`[intro – pad, dial tone, no drums]`, `[chorus – full eighties palette]`, `[bridge – half-time, one electric piano]`, `[verse 2]`) reduced to plain tags | Only the plain tag set exists; text on a tag line is dropped |
| Every repeated section written out in full — both pre-choruses, all three choruses | `(repeat)` would be sung as the word |
| Sixteen lines tightened by a word or two each | 663 words fell to 640, inside the 600–640 ballad band |

Kept exactly as written: every image, 96 BPM, C♯ minor, the instrumentation,
the mood arc, the stairwell turn, the bridge.

## The story and the hooks

Between nine and six she is a name on somebody's list, nodding in an
elevator with no signal, saying yes about a hundred times a day in a voice
that doesn't mean anything. Then the hall light goes off, her shoulders come
down and her voice drops. The rule is simple and she states it herself: don't
text, call — she wants the sound, not the typing. Verse two is where she
breaks her own rule, whispering into a stairwell at four in the afternoon
because his midnight landed sideways in her day, and getting caught doing the
day voice and dropping it half an octave to prove his point. The bridge says
why the hour matters: the woman at noon is a highlight reel and a good coat,
and the one at two in the morning will tell you the whole thing. At six she
is on the floor with the line still open and somebody breathing on the other
end of it.

**The hook:** *"Call me after midnight, that's when I'm all yours"* — first
and last line of every chorus.

**The line for captions:** *"Everybody gets the daylight. You get the rest."*

**The rule:** *"Don't text me, I don't want it typed / I want the low and
lazy sound of you alive."*

**The turn:** *"The girl at noon is a highlight reel and a good coat / She
says the right thing twice and never the rest."*

**Why it can travel:** it is a phone song with no scrolling in it. Everything
in this catalogue's phone imagery is a screen; this one is a voice, which
makes it the opposite record and the one that will land with anyone in a
different time zone from the person they want. The corded landline gives the
video a single unmistakable prop.

## Lyrics as they will be sung

```
[intro]
Twelve o'clock, and the city drops a gear,
Laptop shut, kettle cold, nobody here.
Everybody had a piece of me today,
Now the light goes low and I'm not giving it away.

[verse]
From nine to six I'm a name on somebody's list,
Nodding in an elevator where the signal won't stick.
Six voices in my ear and a badge on a string,
And a daytime voice that doesn't mean a thing.
By eleven I've said yes about a hundred times,
By half past I've run out of the good kind.
Then the hall light goes off and the day lets go,
And my shoulders come down and my voice goes low.

[pre-chorus]
Don't text me, I don't want it typed,
I want the low and lazy sound of you alive.
Let it ring twice, I'll get it on the third,
Nothing in the world I'd rather have than your word.

[chorus]
Call me after midnight, that's when I'm all yours,
When the office goes dark and they lock all the doors.
Nobody wants a thing from me at half past two,
Nothing left to give, and I'm giving it to you.
Call me after midnight, let the line run long,
Say it slow, say it wrong, keep the talking on.
Every hour before this one was the world's, not ours,
Call me after midnight, that's when I'm all yours.

[verse]
Tuesday you were three time zones out of line,
And your midnight came down sideways into mine.
So I broke my own rule in a stairwell at four,
Whispered like a thief with my back to the door.
You said, that's the day voice, and I said, it's not,
Then I dropped it half an octave and proved your point.
So the rule's got a hole in the shape of you,
And I'm in no hurry to make it new.

[pre-chorus]
Don't text me, I don't want it typed,
I want the low and lazy sound of you alive.
Let it ring once this time, I'm already awake,
Been holding my real voice back for your sake.

[chorus]
Call me after midnight, that's when I'm all yours,
When the office goes dark and they lock all the doors.
Nobody wants a thing from me at half past two,
Nothing left to give, and I'm giving it to you.
Call me after midnight, let the line run long,
Say it slow, say it wrong, keep the talking on.
Every hour before this one was the world's, not ours,
Call me after midnight, that's when I'm all yours.

[instrumental]

[bridge]
The girl at noon is a highlight reel and a good coat,
She says the right thing twice and never the rest.
The one at two in the morning has a rougher throat,
And she'll tell you the whole thing straight from her chest.
So if you want the real one, you know when to call,
And nobody in daylight ever gets her at all.

[chorus]
Call me after midnight, that's when I'm all yours,
When the office goes dark and they lock all the doors.
Nobody wants a thing from me at half past two,
Nothing left to give, and I'm giving it to you.
Call me after midnight, let the line run long,
We can fall asleep together with the phone on.
Every hour before this one was the world's, not ours,
Call me after midnight, that's when I'm all yours.

[post-chorus]
After midnight, after midnight, that's when I'm all yours,
Let it ring, let it ring, till the morning is ours.
After midnight, after midnight, that's when I'm all yours,
Call me, call me, the whole night is ours.

[outro]
Six in the morning and the line is still on,
You fell asleep first and I let it run long.
The city's coming up and I'm still on the floor,
Call me after midnight, and I'll answer once more.
```

## Budget (verified)

| Check | Result |
|---|---|
| Sung words | 640 → ~5.5 min at 116 wpm, 92% of frame cap |
| Caption + lyrics tokens | 2088 of 5000 |
| Section tags alone on their lines | yes |
| Stage directions in lyric body | none |
| Character name in lyrics | none |
| `Vocal Details` / `Sonics` vs song 1 | byte-identical |
