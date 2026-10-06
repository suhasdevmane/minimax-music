# Song folder template

The exact spec every song folder follows. This file covers **what files to
produce and what the engine accepts**; [`LYRIC_CRAFT.md`](LYRIC_CRAFT.md)
covers **what makes the words good** and is mandatory reading before writing
any lyrics. Songs 07 and 08 are the reference implementations — read both
completely before writing a new song:
[`songs/07-ghost-in-my-dms/`](../songs/07-ghost-in-my-dms/) (solo ballad)
and [`songs/08-power-back-on/`](../songs/08-power-back-on/) (uptempo duet
with `render.json`).

## Folder

```
songs/NN-song-slug/
├── README.md                    ← song sheet (see §3)
├── caption.txt                  ← music description fed to the model (see §1)
├── lyrics.txt                   ← render-ready lyrics (see §2)
├── render.json                  ← ONLY for uptempo songs: {"wpm": 140, "note": "..."}
├── source/original-submission.md← concept + lyrics + scene-by-scene direction (see §4)
├── video/wan22-shot-list.md     ← one shot per lyric line + bible + workflow + QC (see §5)
├── output/.gitkeep
└── logs/.gitkeep
```

Folder and file names use the song title, never a character name. The WAV
stem the queue expects is the folder name without its `NN-` prefix, hyphens
replaced by underscores (`09-slow-dance-in-the-kitchen` → `output/slow_dance_in_the_kitchen.wav`).

## 1. `caption.txt`

Four blocks, in this order, with these exact headings and field labels:

```
Global Metadata
Basic Attributes: bpm is <N>. key is <Key>, and scale is <major|minor>. <Genre sentence>.
Global Emotional Progression: <one long paragraph, section by section: intro → verse → pre-chorus → chorus → verse → ... → outro, describing dynamics, instruments entering/leaving, the emotional turn, and where the lift or modulation happens>
Application Scenarios & Imagery: <one sentence of concrete images and use cases: reels, edits, the video world>
Sonics & Production Profile: Wide, cinematic soundstage with deep stereo pads and a tightly centered vocal. Modern pop-R&B polish: controlled low end with weighty sub-bass and 808s, scooped low-mids for vocal clarity, crisp airy top end. Dynamics are contained in the verses and open dramatically in the choruses. Generous plate and hall reverb on atmospheric elements, with the lead vocal kept close and dry for intimacy.

Vocal Details
Vocal Gender & Timbre: Singer A (Female). A young-adult lead with a warm, slightly husky tone; intimate and breathy in the low register, gaining a raw, expressive rasp as she pushes into her upper chest voice.
Vocal Style: Confessional and conversational in the verses, sitting close to the microphone with audible breath and soft consonants. The pre-chorus builds urgency through rising phrasing and tighter rhythmic delivery. The chorus is belted, powerful and slightly raspy at the peaks, with emotional cracks left intact rather than smoothed over. The bridge returns to near-spoken fragility before the final build.
Harmony/Backing Vocals: Stacked female harmonies thicken the chorus. Layered male and female harmonies join on the final hook for maximum width and lift. Airy wordless vocal echoes drift through the outro.
Vocal FX: Close, dry lead with subtle plate reverb and a short slapback delay. Throw delays on chorus phrase endings. The outro vocals are treated with long, washed-out reverb tails and rhythmic echo.

Arrangement
Instrument Lifecycle Description (Primary/Secondary Layering):
Primary: <which instruments carry the song and when they enter/leave>
Secondary: <supporting layers and where they appear>
Groove & Foundation Progression: <the rhythm section section by section>
Embellishments, Textures & Spatial FX: <ear candy, risers, ambience, transitions, what the instrumental break contains>
```

**The voice lock.** The `Sonics & Production Profile` line and the four
`Vocal Details` lines (`Vocal Gender & Timbre`, `Vocal Style`,
`Harmony/Backing Vocals`, `Vocal FX`) must be **byte-identical** to
[`songs/01-fire-in-the-rain/caption.txt`](../songs/01-fire-in-the-rain/caption.txt).
Copy them from that file. Do not paraphrase, do not fix punctuation.
`verify_lyrics.py --voice-ref songs/01-fire-in-the-rain` fails otherwise.

**Duets** add two lines between `Vocal Gender & Timbre` and `Vocal Style`
(extra lines are allowed; the four reference lines stay verbatim):

```
Duet Partner: Singer B (Male). <timbre description>
Duet Structure: <which voice sings which section, in order; where they harmonise>
```

Everything else in the caption is free per song. Write it in the same prose
register as songs 01–08: long, specific, musical, no bullet points, no
markdown inside the caption. Stage directions (whispered, spoken, half-time)
live **here**, never in the lyrics. Never mention the character name.

## 2. `lyrics.txt`

- Section tags **alone on their line**, lowercase, from this set only:
  `[intro]`, `[verse]`, `[pre-chorus]`, `[chorus]`, `[post-chorus]`,
  `[instrumental]`, `[bridge]`, `[outro]`. No `[verse 1]`, no `[rap]`, no
  `[final chorus]`, no text on a tag line.
- **Every repeated section is written out in full.** Never `(repeat)` — the
  verify script flags any line that is only parentheses, and the model would
  sing it.
- No stage directions, no asterisks, no bracketed notes, no line that is only
  a parenthesis. Anything in the body gets sung.
- No quotation marks, no em-dashes. Use commas. Spell numbers as words
  (*two a.m.*, *eleven fifty-nine*); the model sings digits unpredictably.
- **The character name never appears.** Not "Mahima", not any name.
- One `[instrumental]` section per song, placed after the second chorus,
  before the bridge (the shot list needs a no-lyrics stretch there).
- Typical shape (vary it): intro · verse · pre-chorus · chorus · verse ·
  pre-chorus · chorus · instrumental · bridge · chorus (varied or lifted) ·
  post-chorus · outro. Final choruses may vary their lines; keep the hook.

**Word budget** (the script counts `len(lyrics.split()) - number of "["`):

| Pacing class | BPM | `render.json` | Sung words | Estimated audio |
|---|---|---|---|---|
| ballad / mid | ≤ 117 | none | **600–640** | 5.2–5.5 min at 116 wpm |
| uptempo | ≥ 118 | `{"wpm": 140}` | **700–760** | 5.0–5.4 min at 140 wpm |

The hard cap is 647 words (ballad) / 781 words (uptempo) — the verify script
fails above that. The target is 5–6 minutes; write near the top of the range.
Hook-heavy lyrics sing faster (song 3 paced 153 wpm), so favour full verses
over chant lines to protect the length.

`render.json` for uptempo songs:

```json
{
  "wpm": 140,
  "note": "Uptempo (<BPM> BPM). Ballads measured 116-153 wpm; this will pace faster. 140 is a conservative estimate used by verify_lyrics.py for the length guard. If the outro truncates on the first render, drop the second post-chorus and re-render."
}
```

## 3. `README.md` — the song sheet

Follow song 07's README section for section. Headings, in order:

1. `# <Title>` then a bold status line: `**Status: written and verified, NOT rendered. Not yet in the queue.**`
2. One paragraph: song number, "Female lead **Mahima**" (or "Female + male duet"), genre, BPM, key, "Same singer as songs 1–8."
3. `Source of record:` line pointing at `source/original-submission.md`.
4. `## Files` — the table (lyrics, caption, `render.json` if present, shot list with its entry count, `source/` · `output/` · `logs/`).
5. `## Render (when queued)` — the `render_queue.py <folder>` command and the direct `generate.py` command with the correct `--out` stem. `--duration 355 --seed 42`.
6. `## What changed from the submission` — a table; typically "quotation marks and em-dashes removed", "digits spelled out", "descriptive tag lines reduced to plain tags", "repeated sections written out". Uptempo songs add the pacing note from song 08.
7. `## The story and the hooks` — the story in one paragraph, then **The hook**, **The line for captions**, **The turn** (or knife line / chant / quote as fits), **Why it can travel**.
8. `## Lyrics as they will be sung` — a fenced block with the full lyrics, identical to `lyrics.txt`.
9. `## Budget (verified)` — the table: sung words with the estimated minutes and % of cap, caption + lyrics tokens (from the verify output), section tags, stage directions, character name, voice lock. Fill in the real numbers from the script.

## 4. `source/original-submission.md`

The concept document, as songs 07 and 08 have it:

```
# <Title> — original submission

The song, direction and scene-by-scene video notes as submitted, before
cleanup for the lyric body. Kept as source material.

**Theme:** ...
**Mood:** ...
**Message:** "..."
**Genre:** ... (with two or three reference-artist "x" comparisons)
**Tempo & Key:** BPM, 4/4, key, where it lifts
**Vocal setup:** lead + backing (+ Singer B for duets)
**Instrumentation:** a bulleted list
**Mood arc:** intro / verses / pre-chorus / chorus / bridge / final chorus / outro, one line each

## Lyrics + Video Direction (scene-by-scene)

### [intro – <feel>]
```<the stanza>```
- Scene: ...
- Shot: ...
- Cut to: ...
- Her reaction / Emotion: ...
- Lighting: ...

### [verse 1] ... (every stanza of every section, with its own scene block)
### [instrumental] — scene block only
### [outro] ... 

## Viral moments  (four to six bullets: the hook frame, the challenge, the caption line, the quote)
```

Lyrics here may keep quotation marks and digits — this is the pre-cleanup
source. They must still never contain the character name.

## 5. `video/wan22-shot-list.md`

Follow song 07 (solo) or 08 (two leads) exactly. Sections:

1. `# Wan 2.2 Shot List — "<Title>"` + the intro paragraph (one shot per
   lyric line, timestamps from the WAV, the bar length at this BPM).
2. `## 1. Visual style` (or `Visual world`) — a paragraph, then the
   section / grade / camera table.
3. `## 2. Character bible — paste into every prompt` — Mahima in one to
   three looks, each a blockquote starting `Same female protagonist Mahima,
   young woman in her early twenties, expressive dark eyes, oval face, long
   dark wavy hair ...` with the look's hair, makeup, wardrobe, expression,
   and ending `realistic cinematic photography, consistent identity, natural
   skin texture`. The romantic male lead with a face is **Kai** (`Same male
   character Kai, man in his late twenties, close-cropped dark hair, short
   beard, athletic build, ...`). Exes and rivals are faceless. Then the
   **Always append** line and the **Negative prompt** block, both copied
   verbatim from song 07. Then the note that all screens/UI/text are
   composited in the edit.
4. `## 3. Wan 2.2 workflow` — the paragraph (I2V not T2V, IP-Adapter or
   LoRA, which ControlNets, aspect ratios, what to animate) and the model
   table, verbatim from song 07/08.
5. `## 4. Scene per lyric line` — a `###` heading per section, then a
   numbered list: `N. *"<lyric line>"* — <the shot: subject, action, framing,
   light, camera move>.` One entry for **every** lyric line in `lyrics.txt`,
   in order, including repeated choruses (repeats may say `reuse shot N,
   tighter` for some lines but should add new material for at least half).
   The `[instrumental]` gets four to six unnumbered-lyric shots. Numbering is
   continuous through the whole song.
6. `## 5. Edit and the challenge` — edit markers, the bar length, the
   shareable cut and the challenge idea.
7. `## 6. Quality-control checklist` — six to eight bullets specific to this
   video (looks per section, motifs, faceless rule, composited UI, last shot).

Video prompts may use the name Mahima freely. Lyrics quoted in the shot list
are the cleaned lyrics from `lyrics.txt`, verbatim.

## 6. Verify

```powershell
.\.venv\Scripts\python.exe scripts\verify_lyrics.py songs\NN-song-slug --voice-ref songs\01-fire-in-the-rain
```

All six checks must say `OK` and the last line must be `PASS`. Put the token
count and word count it prints into the README's Budget table.

## 7. Originality and production standard

Every song has its own hook, its own images and its own stanzas. Do not
reuse a stanza, hook or title phrase from any other song in `songs/`. Do
not reuse the stock images of songs 01–08 (rain on the window, the train
station clock, the bathroom floor, the ghost in the DMs, the power station).

The catalogue is written for high-end English-language production houses.
No novelty or comedy songs; humour only as wit inside a real song. Write in
current native idiom with slang used naturally and sparingly, in the
register (US or UK) the catalogue assigns. Follow the catalogue's *Rap and
delivery map*: where a song has a rap verse, write real bars with internal
rhyme and a clear cadence; a male rap feature is Singer B with a `Duet
Structure` line in the caption. See the *Production standard* section of
[`songs/CATALOGUE.md`](../songs/CATALOGUE.md).
