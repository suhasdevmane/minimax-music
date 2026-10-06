# Lyric craft standard

Craft rules every song in this catalogue must meet. Distilled from the
`bitwize-music` plugin's `lyric-writer` skill
(`~/.claude/plugins/cache/bitwize-music/bitwize-music/0.101.0/skills/lyric-writer/`),
adapted to this project's engine.

Read this alongside [`SONG_TEMPLATE.md`](SONG_TEMPLATE.md). The template says
what files to produce and what the engine accepts. This file says what makes
the words good.

## What does NOT carry over from the skill

The skill targets Suno. Three of its rules are wrong for MiniMax Music 3 and
must be ignored:

| Skill says | Here instead |
|---|---|
| 220–400 words (non-hip-hop), 400–600 (hip-hop) | **600–640 ballad / 700–760 uptempo.** Suno paces differently. Our measured pacing is 116 wpm for ballads and ~140 for uptempo, against a 6.0-minute hard cap. The template's budget is the authority. |
| Phonetic respelling for tricky words, homograph tables | **Never.** MiniMax sings the lyric body literally. Respelled words would be sung wrong. Choose words that read unambiguously instead. |
| Suno tags: `[Instrumental Break]`, `[Synth Solo]`, `[Drop]` | **Only** `[intro]` `[verse]` `[pre-chorus]` `[chorus]` `[post-chorus]` `[instrumental]` `[bridge]` `[outro]`, alone on their line. Anything else is dropped or sung. |

Everything below does carry over.

## The rules

### Show, don't tell

Verses carry sensory detail; choruses carry the emotional statement.
Replace a named feeling with the action or object that proves it. "I was
waiting up" is weaker than the plate still set at the table. Engage more
than sight: sound, smell, touch, motion.

### Verse two must develop

V2 rephrasing V1 is the single most common failure. V2 must move the story
forward, deepen the feeling, or turn the perspective. New detail, new
moment, new information. If V2 could swap places with V1 and nothing would
change, rewrite it.

### No verse-chorus echo

Compare the last two lines of every verse against the first two lines of
the chorus that follows, for every verse and the bridge. Flag and fix:

- an exact phrase appearing in both
- the verse ending on the chorus's opening rhyme word
- the verse paraphrasing the hook before the hook lands
- the verse using the chorus's signature image

The verse sets up tension; the chorus resolves it. Complementary, never
redundant. A hook that has already been said in the verse lands flat.

### Rhyme

- Never rhyme a word with itself, and never rhyme the same pair twice in
  consecutive lines.
- Avoid near-identical repeats.
- No forced rhymes: never invert word order, bend grammar, invent a word,
  or pad with filler to reach a rhyme. Meaning outranks the rhyme every
  time; use a slant rhyme instead.
- Vary the type: perfect, slant, consonance, assonance, internal.
- Keep one scheme through a section; no switching mid-verse, no orphan
  lines that should rhyme and don't.
- Scheme by genre: pop leans conversational with near rhymes; country and
  folk use the ballad stanza where lines two and four rhyme; rap needs
  multisyllabic and internal rhyme carrying through the bar, not just at
  the end; rock and punk favour meaning and energy over technical rhyming.

### Prosody

Stressed syllables land on strong beats. Say every line out loud. If the
natural emphasis of a word fights the meter, rewrite the line. Keep
syllable counts consistent between corresponding lines of V1 and V2:
roughly 6–8 syllables for pop and folk, 8–10 for rock, 10–13 for rap.

### Hook and title

The title sits in the first or last line of the chorus, and appears near
the song's start and its end. Give it the rhythmic accent.

### Point of view and tense

Pick one and hold it. Don't drift between past and present inside a
section without a reason.

### Section shape

Reach length by adding sections, not by inflating them. A ten-line verse
or a rambling chorus makes the model rush. Guide limits: verse six to eight
lines, chorus four to eight, pre-chorus two to four, bridge four to six,
outro two to four. Our word budget is met through the full arc, which is
why the template's structure repeats the chorus and adds a pre-chorus and
post-chorus.

### Avoid

Dead phrases: cold as ice, broke my heart, by my side, set me free,
learning to fly, and "tonight" parked at the end of a line to buy a rhyme.
Predictable pairs like fire and desire. Filler that pads a line to set up a
quote. Abstractions with no image under them. Being so specific that the
listener is locked out.

## The check, before any song is called done

Run all of these on the finished lyrics:

1. Rhyme: no self-rhymes, no repeated end words, no lazy pairs.
2. Prosody: stresses on strong beats, read aloud.
3. Point of view and tense consistent.
4. Structure: tags correct and alone on their line, V2 develops.
5. Flow: consistent syllable counts, no filler, no forced rhymes.
6. Length: inside this project's word budget for the pacing class.
7. Section lengths inside the guide limits.
8. Rhyme scheme fits the genre, no orphan lines.
9. Verse-chorus echo checked at every transition, bridge included.
10. Pitfalls list above: clichés, twin verses, buried hook, telling not
    showing.
11. No character name anywhere in the lyrics.
12. Nothing in the body that would be sung wrong: no digits, no quotation
    marks, no em-dashes, no stage directions, no parentheses-only lines.

### Then one refinement pass

Go back through and tighten: cut filler, compress, replace a generic image
with a specific one, and read it aloud for singability at the song's tempo.
Refinement polishes what is there. It does not add new metaphors,
characters or story beats, and it must not break the word budget or any
rule above. Re-run the check after the pass. If the pass changes nothing,
the lyrics were already tight.

## Originality

Every song in this catalogue is original work. Never reproduce lyrics from
a real released song, and never write a light paraphrase of one. Reference
artists in a brief describe a sound and a register, never words to borrow.
No stanza, hook, title phrase or signature image may repeat between two
songs in `songs/`. `scripts/audit_catalogue.py` fails the build on any
lyric line of five or more words shared between two songs.
