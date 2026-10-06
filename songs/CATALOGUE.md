# Song catalogue — songs 09 to 100

The long todo. Ninety-two new songs, written to the same template as songs
01–08 (see [`docs/SONG_TEMPLATE.md`](../docs/SONG_TEMPLATE.md)). Every song
targets 5–6 minutes of audio, the same female lead voice as song 1, and a
modern, share-first style: love, romance, cheeky flirtation, fun, parties,
memories, moving on, confidence, travel.

Legend for the checklist at the bottom: `[ ]` not written · `[x]` written and
verified (`verify_lyrics.py` PASS) · `[!]` needs a fix.

## Rules that apply to every entry

- **Pacing class** decides the word budget. *Ballad/mid* (≤ 117 BPM): no
  `render.json`, 600–640 sung words (≈ 5.2–5.5 min at 116 wpm). *Uptempo*
  (≥ 118 BPM): `render.json` with `{"wpm": 140}`, 700–760 sung words
  (≈ 5.0–5.4 min at 140 wpm).
- **Voice**: Singer A is always the song-1 female lead. Duets add Singer B
  (male) exactly as songs 04 and 08 do.
- **Video**: the female lead on screen is Mahima. The romantic male lead,
  when he has a face, is Kai (song 08's character bible). Exes are faceless.
- **The name is never sung.** Lyrics, captions and hooks contain no
  character name.
- **No two songs share a hook, a title word-pattern, or a stanza.**

## Production standard (applies to every song)

These songs are written for high-end English-language production houses
(UK and US). Every one must read as a credible commercial release.

- **No novelty, comedy or gimmick songs.** Humour appears only as wit inside
  a real emotional song. Fun songs are party or summer records, not jokes.
- **Native idiom.** Write the way current English-language hits are written:
  contemporary spoken phrasing and slang used naturally and sparingly
  (*lowkey, ride or die, situationship, main character, no cap, it's giving,
  the ick, on read, ghosted, glow up, soft launch, ate, iconic, vibe,
  delulu*), never forced, never a punchline. The *Register* line below says
  whether a song sits in a US or UK voice; UK-register songs use UK
  spelling, UK slang (*mate, fit, peak, bare, innit, buzzin', proper, ends,
  bare jokes, mandem*) and London or Manchester street detail, US-register
  songs use US idiom and cities. Default register is US pop.
- **Rap and delivery variation.** Not every song is sung straight. The map
  below assigns rap-sung verses, male rap features, spoken bridges and
  chant hooks. Where the female lead raps, write real bars with internal
  rhyme and a clear cadence, not sing-song couplets. Male rap features are
  Singer B in the caption with a `Duet Structure` line. Rap verses are
  denser: an eight-to-twelve-line rap verse is normal.
- **Style breadth.** Across the catalogue: cinematic pop, dance-pop, house,
  UK garage, Afroswing, Afrobeats, Latin pop, reggaeton, drill-pop,
  trap-R&B, neo-soul, pop-punk, pop-rock, synthwave, country-pop,
  indie-folk, Bollywood fusion, jazz-pop, disco, funk. Each brief's *Sound*
  line is binding.

**Rap and delivery map**

| Song | Treatment |
|---|---|
| 11 Eyes on Me | her half-rapped second verse, US R&B cadence |
| 24 Yes to Everything | male rap feature (Singer B) as a third verse, US pop-rap |
| 29 Sugar on My Tongue | her rap-sung pre-choruses |
| 32 Read at Eleven Fifty-Nine | her melodic-rap second verse |
| 37 Mirror, Mirror | her rap verse two, fast and confident |
| 39 Your Place or Mine | male rap feature verse, UK register |
| 44 No Plans, No Problem | her Afroswing rap-sung verses, UK register |
| 52 After Hours | male MC feature verse, UK garage register |
| 54 Barefoot on the Boulevard | her spoken-then-rapped second verse |
| 55 Ride or Die | her rap verse two |
| 68 Unfollowed | her half-rapped bridge |
| 72 Wrong Number | her pop-rap verses, sung chorus |
| 73 I'm the Prize | her melodic-rap verses |
| 77 Glow Up Season | male rap feature on the bridge |
| 79 Villain in Your Story | her rap-sung second verse |
| 89 Soft Girl, Steel Spine | her melodic-rap second verse |
| 90 Pretty and Powerful | male rapper Singer B on both rap verses |
| 93 Diamond Season | her rap verse two |
| 94 High Heels on Concrete | her drill-cadence rap verses, UK register |
| 99 City Lights Don't Sleep | spoken-word bridge |
| 100 The Hundredth Song | male spoken-word section before the last chorus |

**Register map**

| Register | Songs |
|---|---|
| UK | 30, 39, 41, 44, 52, 54, 69, 72, 79, 92, 94, 99 |
| Australian | 42, 47 |
| Indian-English (neutral, no slang) | 21, 65, 96 |
| US (default) | every other song |

## The briefs

### 09 · Slow Dance in the Kitchen
- Slug `09-slow-dance-in-the-kitchen` · romance · **duet**
- Sound: acoustic pop ballad, 88 BPM, G major, brushed drums, upright piano, warm nylon guitar
- Pacing: ballad
- Concept: a couple with no money for a night out turns the kitchen into a ballroom; socks on tile, the oven timer as a metronome, burnt toast and a first "I love you"
- Hook: *"Turn the radio low, we don't need a floor / slow dance in the kitchen, that's what the kitchen's for"*
- Video: one small apartment kitchen, string lights, steam, socks, a single continuous-feeling evening

### 10 · Sunday Mornings
- Slug `10-sunday-mornings` · romance · solo
- Sound: indie-pop, 100 BPM, D major, jangly guitar, soft claps, mellotron
- Pacing: ballad/mid
- Concept: the whole relationship measured in Sunday mornings: first one awkward, the fiftieth one with pancakes and a cat, the day she realises she never wants a Monday without him
- Hook: *"Give me Sunday mornings, messy hair and coffee rings"*
- Video: sunlit bedroom and balcony, seasons changing outside the same window

### 11 · Eyes on Me
- Slug `11-eyes-on-me` · romance / flirt · solo
- Sound: pop-R&B, 94 BPM, B♭ minor, finger snaps, sub-bass, Rhodes
- Pacing: ballad/mid
- Concept: across a crowded party she catches him looking and decides she'll make him keep looking; confidence as courtship
- Hook: *"Keep your eyes on me, I know you already do"*
- Video: a house party in slow motion, one red dress, a staircase, a glance that lasts a whole chorus

### 12 · First Kiss at Last Call
- Slug `12-first-kiss-at-last-call` · romance · solo
- Sound: pop-rock, 120 BPM, A major, driving guitars, big snare, gang vocals
- Pacing: uptempo
- Concept: a whole night of almost, then the lights come up in the bar and they finally kiss in the ugly fluorescent light and it's perfect
- Hook: *"First kiss at last call, lights up and I don't care at all"*
- Video: a dive bar, a jukebox, closing time, a kiss under harsh light that reads as beautiful

### 13 · Golden Hour on Your Skin
- Slug `13-golden-hour-on-your-skin` · romance · solo
- Sound: dreamy pop, 96 BPM, E major, shimmering synths, soft 808, harp flourishes
- Pacing: ballad/mid
- Concept: the twenty minutes before sunset when everything about him looks like a photograph she wants to keep
- Hook: *"Golden hour on your skin, and I'm falling all over again"*
- Video: a rooftop, a field, a car bonnet, all at golden hour, lens flare, film grain

### 14 · Your Name in Cursive
- Slug `14-your-name-in-cursive` · romance · solo
- Sound: cinematic pop, 92 BPM, F minor lifting to A♭ major, piano, strings, trap hats
- Pacing: ballad
- Concept: she's been writing his name in the margins since the first week, notebooks and steamed mirrors and the sand at the beach; the song is her finally saying it out loud
- Hook: *"I wrote your name in cursive, now I'm saying it out loud"*
- Video: notebooks, mirrors, sand, a café receipt, the handwriting motif everywhere, never legible text

### 15 · Butterflies Don't Lie
- Slug `15-butterflies-dont-lie` · romance · solo
- Sound: bubbly synth-pop, 122 BPM, C major, plucky synths, four-on-the-floor
- Pacing: uptempo
- Concept: she keeps telling her friends she's not into him, and her stomach keeps disagreeing every time his name comes up
- Hook: *"My mouth says maybe, but butterflies don't lie"*
- Video: colourful, candy-bright, a girls' brunch, a phone that keeps lighting up, a smile she can't hide

### 16 · Airplane Mode
- Slug `16-airplane-mode` · romance · solo
- Sound: chill pop, 98 BPM, G minor, lo-fi drums, warm pads, guitar harmonics
- Pacing: ballad/mid
- Concept: a weekend where they both switch their phones off; the world can wait, she has never been this present
- Hook: *"Put the world on airplane mode, it's just you and me tonight"*
- Video: a cabin, a lake, two phones face-down on a table for the whole video, real light

### 17 · Corner Table
- Slug `17-corner-table` · romance · solo
- Sound: understated indie-pop, 110 BPM, C major, warm electric guitar, soft kick, upright piano, restrained strings in the last chorus
- Pacing: mid
- Concept: a whole love story told through one café's corner table across a year: the first time she pretended to read, the day he knew her order, the winter he didn't come, the spring he did
- Hook: *"Same corner table, different me, and you still sat down"*
- Video: a single café through four seasons, the same table, a barista as a silent witness, cinematic and quiet

### 18 · Forever Looks Like Tuesday
- Slug `18-forever-looks-like-tuesday` · romance · **duet**
- Sound: country-pop ballad, 84 BPM, D major, pedal-steel-style guitar, brushed snare
- Pacing: ballad
- Concept: forever isn't a wedding, it's the boring Tuesday when he fixes the tap and she does the taxes and neither would trade it
- Hook: *"Forever looks like Tuesday, and Tuesday looks like you"*
- Video: a house being lived in: groceries, a leaking tap, laundry, the small ordinary sacred

### 19 · Hold My Hand in Public
- Slug `19-hold-my-hand-in-public` · romance · solo
- Sound: pop, 104 BPM, E♭ major, piano stabs, snaps, big chorus
- Pacing: mid
- Concept: the moment a secret thing becomes a real thing: she wants to be held on the street, tagged in the photo, introduced by name
- Hook: *"Hold my hand in public, let the whole street know"*
- Video: a city crossing, a market, a family dinner door, the first time hands touch outside

### 20 · Pretty When You Laugh
- Slug `20-pretty-when-you-laugh` · romance · solo
- Sound: pop-soul, 90 BPM, A♭ major, horns, Rhodes, gospel-tinged backing vocals
- Pacing: ballad
- Concept: she fell for his laugh before his face; a song listing every time it happened
- Hook: *"You're pretty when you laugh, so I'll never stop trying"*
- Video: warm interiors, a comedy of small moments, a man laughing filmed like a love letter

### 21 · Under the Same Umbrella
- Slug `21-under-the-same-umbrella` · romance · **duet**
- Sound: Bollywood-pop fusion, 98 BPM, D minor, tabla, sitar-like plucks, cinematic strings, modern bass
- Pacing: ballad/mid
- Concept: a monsoon downpour, one umbrella, two strangers who share it for six blocks and never quite say goodbye
- Hook: *"Under the same umbrella, we're the only ones dry"*
- Video: a rain-soaked Indian city street, a chai stall, a bus stop, colour everywhere

### 22 · Stay Till the Credits
- Slug `22-stay-till-the-credits` · romance · solo
- Sound: cinematic ballad, 86 BPM, C minor, piano, cello, sub-bass
- Pacing: ballad
- Concept: he's the kind who stays till the credits end; she wants a love that stays through the boring part after the ending
- Hook: *"Stay till the credits, stay till the lights come on"*
- Video: an empty cinema, two people alone in the back row as the credits roll

### 23 · Made of Sunlight
- Slug `23-made-of-sunlight` · romance · **duet**
- Sound: Afrobeats-pop, 106 BPM, F major, log drums, bright guitar, shakers
- Pacing: mid
- Concept: a call-and-response love song, each singing what the other is made of
- Hook: *"You're made of sunlight, I'm made of you"*
- Video: a beach town, a street dance, orange and blue, joy as the whole grade

### 24 · Yes to Everything
- Slug `24-yes-to-everything` · romance / fun · solo
- Sound: dance-pop, 124 BPM, B major, sidechained synths, drop chorus
- Pacing: uptempo
- Concept: a first date where she says yes to every dumb suggestion: karaoke, the ferris wheel, the 3 a.m. pancakes, the second date
- Hook: *"Tonight I'm saying yes to everything"*
- Video: a fairground and a city at night, fast cuts, every yes a new location

### 25 · Falling Slowly, Landing Soft
- Slug `25-falling-slowly-landing-soft` · romance · solo
- Sound: piano ballad, 80 BPM, E♭ major, piano, strings, minimal drums
- Pacing: ballad
- Concept: after a hard love she's scared to fall again; he catches her so gently she doesn't notice she's already down
- Hook: *"I was falling slowly, you made me land soft"*
- Video: slow motion, feathers, a trust fall in a park, muted pastels

### 26 · Fireworks in February
- Slug `26-fireworks-in-february` · romance · solo
- Sound: pop, 112 BPM, G major, synth bells, punchy drums
- Pacing: mid
- Concept: no holiday, no reason, he set off fireworks in a frozen parking lot because she said she'd never seen them up close
- Hook: *"Fireworks in February, just because you could"*
- Video: a frozen parking lot, breath in the air, sparklers, a coat shared

### 27 · The Way You Say Good Morning
- Slug `27-the-way-you-say-good-morning` · romance · solo
- Sound: R&B, 92 BPM, D♭ major, silky synths, snaps, layered harmonies
- Pacing: ballad
- Concept: a slow, sensual ode to first-light intimacy: his voice before coffee, the sheets, the light through blinds
- Hook: *"The way you say good morning makes me wanna stay in bed"*
- Video: a bedroom in blinds-striped light, tasteful, close, slow

### 28 · We Look Good Together
- Slug `28-we-look-good-together` · romance / fun · **duet**
- Sound: funk-pop, 116 BPM, E minor, slap bass, brass, wah guitar
- Pacing: mid
- Concept: two people who know they're a power couple and enjoy it; matching outfits, mirror selfies, a walk-in like a runway
- Hook: *"Baby, we look good together, and we know it"*
- Video: a colour-blocked city, matching fits, mirrors and shop windows, a strut

### 29 · Sugar on My Tongue
- Slug `29-sugar-on-my-tongue` · flirty · solo
- Sound: bouncy dance-pop, 118 BPM, C minor lifting to E♭, kiss-sound percussion, bass drops
- Pacing: uptempo
- Concept: a cheeky, sweet-tooth flirt; she talks about him like dessert and dares him to earn it
- Hook: *"You're like sugar on my tongue, and I've got a sweet tooth tonight"*
- Video: a candy-coloured diner, a milkshake, red lips, playful never explicit

### 30 · Don't Tell the Neighbours
- Slug `30-dont-tell-the-neighbours` · flirty · solo
- Sound: reggaeton-pop, 100 BPM, A minor, dembow, plucked synths
- Pacing: ballad/mid
- Concept: a late-night dance party for two in a thin-walled apartment; giggling, shushing, curtains, the neighbour banging on the wall
- Hook: *"Turn it down, don't tell the neighbours what we do"*
- Video: one apartment at night, curtains, a lamp, a hallway, a nosy neighbour as comic relief

### 31 · Lipstick on Your Collar
- Slug `31-lipstick-on-your-collar` · flirty · solo
- Sound: retro doo-wop modernised, 108 BPM, F major, finger snaps, baritone sax, trap hats
- Pacing: mid
- Concept: she leaves a mark on purpose so the whole office knows he's taken; playful possessiveness
- Hook: *"Lipstick on your collar, so they know you're mine"*
- Video: 60s styling with a phone in hand, an elevator, an office, a wink

### 32 · Read at Eleven Fifty-Nine
- Slug `32-read-at-eleven-fifty-nine` · flirty · solo
- Sound: trap-R&B, 90 BPM, F♯ minor, 808 slides, vocal chops
- Pacing: ballad
- Concept: the texting game: the read receipt, the typing dots, the one-minute-to-midnight reply that changes everything
- Hook: *"You read it at eleven fifty-nine, and I know you're on your way"*
- Video: two apartments across a city, split screen, a phone glow, a taxi

### 33 · Bad Idea, Good Night
- Slug `33-bad-idea-good-night` · flirty / fun · solo
- Sound: pop-punk, 150 BPM, E major, power chords, fast drums, shouted backing
- Pacing: uptempo
- Concept: everyone says he's a bad idea; she agrees, then has the best night of her year
- Hook: *"You're a bad idea, but a good night"*
- Video: a skate park, a basement gig, a scooter ride, fast, chaotic, fun

### 34 · Trouble Looks Cute on You
- Slug `34-trouble-looks-cute-on-you` · flirty · solo
- Sound: Latin-pop, 105 BPM, G minor, nylon guitar, congas, brass
- Pacing: mid
- Concept: a slow-burn flirt on a dance floor with a man who's clearly trouble and wears it well
- Hook: *"Trouble looks cute on you, so I'll take my chances"*
- Video: a salsa bar, red light, sweat, a rooftop after

### 35 · Borrowed Shirt
- Slug `35-borrowed-shirt` · flirty / intimate · solo
- Sound: bedroom R&B, 84 BPM, B♭ major, soft keys, vinyl crackle, muted guitar
- Pacing: ballad
- Concept: the morning after, walking around in his shirt, the intimacy of ordinary things
- Hook: *"I'm wearing your shirt and nothing else is on my mind"*
- Video: a morning apartment, sunlight, coffee, the shirt as the whole costume, tasteful

### 36 · Dance Like Nobody's Sober
- Slug `36-dance-like-nobodys-sober` · fun / flirty · solo
- Sound: party pop, 126 BPM, D major, big synths, chant chorus
- Pacing: uptempo
- Concept: a wild wedding-reception-style night where nobody cares how they dance
- Hook: *"Dance like nobody's sober, sing like nobody's home"*
- Video: a wedding reception gone feral, aunties and cousins, confetti, a conga line

### 37 · Mirror, Mirror
- Slug `37-mirror-mirror` · flirty / confidence · solo
- Sound: hyperpop-leaning pop, 130 BPM, A minor, pitched vocal chops, distorted bass
- Pacing: uptempo
- Concept: getting ready for a night out as a ritual of power; the mirror agrees she's the one
- Hook: *"Mirror, mirror, tell me who's the baddie"*
- Video: a getting-ready sequence, mirrors, lipstick, a door opening onto a crowd

### 38 · Wine and Whispers
- Slug `38-wine-and-whispers` · flirty / intimate · solo
- Sound: jazz-pop lounge, 92 BPM, E♭ major, upright bass, brushed kit, muted trumpet
- Pacing: ballad
- Concept: a candle-lit night in, a bottle, whispered confessions, the slow dance that ends the song
- Hook: *"Wine and whispers, keep the lights down low"*
- Video: candlelight, a record player, a window, rain outside

### 39 · Your Place or Mine
- Slug `39-your-place-or-mine` · flirty · solo
- Sound: house-pop, 122 BPM, F minor, piano house chords, filtered vocal
- Pacing: uptempo
- Concept: the end of the night decision, played as a flirty negotiation where she's holding all the cards
- Hook: *"Your place or mine? Either way, you're mine tonight"*
- Video: a club exit, a taxi rank, two doors, a coin flip

### 40 · Call Me After Midnight
- Slug `40-call-me-after-midnight` · flirty · solo
- Sound: synth-R&B, 96 BPM, C♯ minor, 80s synths, gated snare
- Pacing: ballad/mid
- Concept: she's busy all day, but after midnight the phone is his; a late-night-voice song
- Hook: *"Call me after midnight, that's when I'm all yours"*
- Video: a neon bedroom, a landline phone as a prop, a city window

### 41 · Weekend Starts on Thursday
- Slug `41-weekend-starts-on-thursday` · fun · solo
- Sound: dance-pop, 124 BPM, G major, disco bass, claps
- Pacing: uptempo
- Concept: quitting the week early, friends, the first drink, a countdown chant
- Hook: *"Weekend starts on Thursday when I'm with you"*
- Video: an office at 5 p.m. becoming a party, a rooftop bar, a taxi full of friends

### 42 · Sunburn and Strawberries
- Slug `42-sunburn-and-strawberries` · fun / summer · solo
- Sound: summer pop, 118 BPM, A major, surf guitar, handclaps, whistle
- Pacing: uptempo
- Concept: a beach day that turns into the best day of the summer
- Hook: *"Sunburn and strawberries, that's my kind of summer"*
- Video: a beach, an ice-cream van, a pier, saturated film look

### 43 · Rooftop Radio
- Slug `43-rooftop-radio` · fun · solo
- Sound: disco-pop, 120 BPM, B♭ major, strings, four-on-the-floor, funk guitar
- Pacing: uptempo
- Concept: a rooftop party running off one old radio, a city skyline and no permit
- Hook: *"Rooftop radio, turn it up, let the whole block know"*
- Video: a summer rooftop at dusk, fairy lights, a skyline, dancing on a water tank

### 44 · No Plans, No Problem
- Slug `44-no-plans-no-problem` · fun · solo
- Sound: Afrobeats, 104 BPM, E major, log drums, warm bass, whistle synth
- Pacing: mid
- Concept: an unplanned day that beats every planned one; wandering, eating, dancing where they stand
- Hook: *"No plans, no problem, just vibes and my people"*
- Video: a city wander, a street food market, an impromptu dance in a square

### 45 · Windows Down
- Slug `45-windows-down` · fun / road trip · solo
- Sound: pop-rock road anthem, 128 BPM, E major, driving guitars, big toms
- Pacing: uptempo
- Concept: a road trip with the radio loud and nowhere to be
- Hook: *"Windows down, volume up, nowhere left to be"*
- Video: a convertible on a coast road, hair in the wind, petrol stations, a sunset

### 46 · Confetti in My Hair
- Slug `46-confetti-in-my-hair` · fun · solo
- Sound: party pop, 126 BPM, C major, brass stabs, big chorus
- Pacing: uptempo
- Concept: the morning after the best party: confetti in her hair, glitter on the floor, no regrets
- Hook: *"Woke up with confetti in my hair, and I don't even care"*
- Video: a trashed apartment in morning light, a flashback to the party, both joyful

### 47 · Beach Bonfire Hearts
- Slug `47-beach-bonfire-hearts` · fun / summer / romance · solo
- Sound: acoustic summer pop, 102 BPM, D major, campfire guitar, cajón, group harmonies
- Pacing: mid
- Concept: a beach bonfire, a borrowed guitar, and the friend who becomes something more
- Hook: *"Beach bonfire hearts, burning slow"*
- Video: a beach at night, a fire, sparks, a circle of friends, one look across the flames

### 48 · Cheap Champagne
- Slug `48-cheap-champagne` · fun / celebration · solo
- Sound: indie-dance pop, 114 BPM, F major, disco bass, bright guitar, claps, a big last chorus
- Pacing: mid
- Concept: celebrating the small wins with cheap champagne on a fire escape: the rent paid, the job, the friend who made it through; a toast to being young and broke and alive
- Hook: *"Cheap champagne on the fire escape, tonight we're rich"*
- Video: a fire escape at dusk, a corner-shop bottle, a rooftop, a city that feels owned for one night

### 49 · Deep End
- Slug `49-deep-end` · fun / summer / romance · solo
- Sound: house, 124 BPM, A minor, piano stabs, filtered vocal, big drop
- Pacing: uptempo
- Concept: a rooftop pool party where she meets someone and decides, for once, to dive in headfirst; love as the deep end
- Hook: *"Meet me at the deep end, I'm done with wading in"*
- Video: a rooftop pool at sunset into neon night, water and city lights, a dive in slow motion

### 50 · Late Checkout
- Slug `50-late-checkout` · fun / romance · solo
- Sound: chill tropical pop, 100 BPM, G major, steel-drum synths, soft kick
- Pacing: ballad/mid
- Concept: the last morning of a holiday, asking for a late checkout because neither wants it to end
- Hook: *"Give me a late checkout, one more hour of you"*
- Video: a hotel room with the sea outside, room service, a balcony, the sound of waves

### 51 · Dancing on the Table
- Slug `51-dancing-on-the-table` · fun · **duet**
- Sound: Latin pop, 128 BPM, D minor, brass, cowbell, gang vocals
- Pacing: uptempo
- Concept: two strangers at a family wedding afterparty who end up dancing on the long table together while the whole family claps them on
- Hook: *"We're dancing on the table, let the whole street hear"*
- Video: a backyard wedding afterparty, string lights, a long table, grandparents clapping

### 52 · After Hours
- Slug `52-after-hours` · fun / city nights · solo with male MC feature
- Sound: UK garage / two-step, 132 BPM, C minor, shuffled hats, sub-bass, chopped vocal, organ stabs
- Pacing: uptempo
- Concept: the after-party at four a.m. in a flat above a chicken shop; the night's best hour is the one after the club; UK register
- Hook: *"After hours, that's when the night gets honest"*
- Video: a London night bus, a stairwell, a flat with the lights low, dawn on a balcony

### 53 · Festival Season
- Slug `53-festival-season` · fun · solo
- Sound: EDM-pop, 128 BPM, F♯ minor, supersaws, drop, crowd chant
- Pacing: uptempo
- Concept: festival weekend: mud, glitter, a stranger's shoulders, a sunrise set
- Hook: *"It's festival season, and we're not going home"*
- Video: a festival field, flags, a crowd from above, a sunrise stage

### 54 · Barefoot on the Boulevard
- Slug `54-barefoot-on-the-boulevard` · fun · solo
- Sound: funk, 112 BPM, A minor, clavinet, slap bass, horns
- Pacing: mid
- Concept: heels off at 2 a.m., walking the boulevard barefoot, the city as a dance floor
- Hook: *"Barefoot on the boulevard, heels in my hand"*
- Video: a city boulevard after the clubs close, wet streets, streetlights, a strut

### 55 · Ride or Die
- Slug `55-ride-or-die` · friendship · solo
- Sound: pop with a rap verse, 120 BPM, E♭ major, punchy drums, brass, chant chorus
- Pacing: uptempo
- Concept: an anthem for the friends who show up: the three a.m. call, the airport pickup, the one who held her hair and her secrets; the group chat as a family
- Hook: *"You're my ride or die, and I'd ride for you"*
- Video: four friends, a car at night, an airport, a kitchen dance, years passing in one apartment

### 56 · Cassette Tape Heart
- Slug `56-cassette-tape-heart` · memories · solo
- Sound: synthwave, 100 BPM, A minor, analogue synths, gated drums
- Pacing: ballad/mid
- Concept: a first love told through a mixtape found in a drawer; rewinding, side B, the song that skips
- Hook: *"I've got a cassette tape heart, and you're on side A"*
- Video: a teenage bedroom in memory, a Walkman, a car at night, VHS grain

### 57 · Hometown Radio
- Slug `57-hometown-radio` · memories · solo
- Sound: country-pop, 96 BPM, G major, acoustic guitar, banjo-like plucks, harmonies
- Pacing: ballad/mid
- Concept: driving back into her hometown and the local station is playing the same songs; everything changed and nothing did
- Hook: *"Hometown radio still plays our song"*
- Video: a small town at dusk, a water tower, a diner, an old friend

### 58 · Kids on Bicycles
- Slug `58-kids-on-bicycles` · memories · solo
- Sound: indie-folk, 92 BPM, C major, fingerpicked guitar, glockenspiel, strings
- Pacing: ballad
- Concept: the summer they were nine and the street was the whole world
- Hook: *"We were kids on bicycles, racing the streetlights home"*
- Video: a suburban street, bicycles, a garden hose, a streetlight coming on

### 59 · Grandma's Kitchen
- Slug `59-grandmas-kitchen` · memories / family · solo
- Sound: soul ballad, 78 BPM, E♭ major, piano, organ, strings
- Pacing: ballad
- Concept: a grandmother's kitchen as the safest place on earth; spices, radio, the recipe nobody wrote down
- Hook: *"Everything I know about love, I learned in grandma's kitchen"*
- Video: an old kitchen, hands kneading dough, a radio, a photo on the fridge, warm and slow

### 60 · The Old Playlist
- Slug `60-the-old-playlist` · memories · solo
- Sound: lo-fi pop, 88 BPM, D major, dusty drums, Rhodes, vinyl noise
- Pacing: ballad
- Concept: shuffling a playlist from three years ago and living every song again for one night
- Hook: *"Hit shuffle on the old playlist, and I'm nineteen again"*
- Video: a night bus, headphones, a lit phone, memory inserts triggered by each song

### 61 · Class of Forever
- Slug `61-class-of-forever` · memories / friendship · solo
- Sound: pop-rock, 116 BPM, B♭ major, ringing guitars, big drums
- Pacing: mid
- Concept: a graduation-night anthem: last locker, last bell, a promise on the football field
- Hook: *"We're the class of forever, no goodbye's gonna stick"*
- Video: a school at dusk, a field, caps in the air, a car full of friends

### 62 · Fireflies and Porch Lights
- Slug `62-fireflies-and-porch-lights` · memories · solo
- Sound: folk-pop, 94 BPM, G major, acoustic guitar, mandolin-like plucks, soft strings
- Pacing: ballad
- Concept: summer nights at her parents' porch, the neighbour boy, the jar of fireflies she let go
- Hook: *"Fireflies and porch lights, you and me and July"*
- Video: a porch, a jar, a lawn at dusk, a screen door, fireflies

### 63 · Photo Booth Strip
- Slug `63-photo-booth-strip` · memories · solo
- Sound: indie pop, 108 BPM, E major, jangly guitar, tambourine
- Pacing: mid
- Concept: a four-frame photo booth strip: the smile, the kiss, the laugh, the blur; the whole relationship in four squares
- Hook: *"Four frames, one night, photo booth strip of my life"*
- Video: a photo booth in a mall, the strip itself, then the four moments in full

### 64 · Best Friend Blueprint
- Slug `64-best-friend-blueprint` · friendship · solo
- Sound: pop, 118 BPM, F major, bright synths, claps
- Pacing: uptempo
- Concept: a manifesto for her best friend: shows up with snacks, tells the truth, holds her hair, never lets her text him
- Hook: *"You're the blueprint, best friend, everyone else is a copy"*
- Video: two friends, a road trip, a bathroom floor, a dance in a kitchen, years passing

### 65 · Mango Season
- Slug `65-mango-season` · memories / childhood · solo
- Sound: Bollywood-folk pop, 104 BPM, D major, dholak, flute, acoustic guitar, modern kick
- Pacing: mid
- Concept: childhood summers at a grandparents' house, mango trees, cousins, a monsoon that arrives early
- Hook: *"Take me back to mango season"*
- Video: a village courtyard, a mango tree, cousins, a first rain, saffron and green

### 66 · Scrapbook of Us
- Slug `66-scrapbook-of-us` · memories / romance · solo
- Sound: piano pop, 86 BPM, A major, piano, soft drums, strings
- Pacing: ballad
- Concept: an anniversary made from a scrapbook: tickets, receipts, a dried flower, a napkin with a phone number
- Hook: *"Every page in the scrapbook of us, I'd live again"*
- Video: hands turning pages, each page becoming the live moment, a kitchen table

### 67 · That Summer Song
- Slug `67-that-summer-song` · memories · solo
- Sound: nostalgia pop, 110 BPM, C major, bright guitars, claps, synth pads
- Pacing: mid
- Concept: the song that was everywhere the summer they fell in love, and what happens when it plays years later in a supermarket
- Hook: *"They're playing that summer song, and I'm right back there"*
- Video: a supermarket aisle dissolving into a beach, then a car, then a kiss

### 68 · Unfollowed
- Slug `68-unfollowed` · moving on · solo
- Sound: pop, 100 BPM, A minor, piano, snaps, trap hats
- Pacing: ballad/mid
- Concept: the day she unfollows him and the sky doesn't fall
- Hook: *"Unfollowed, unbothered, un-yours"*
- Video: a phone, a park, a haircut, a new dress, a life with him cropped out

### 69 · Cry in the Uber
- Slug `69-cry-in-the-uber` · heartbreak · solo
- Sound: sad pop, 90 BPM, F minor, piano, sub-bass, rain
- Pacing: ballad
- Concept: the ride home after it ends: the driver's small kindness, the city through wet glass, the choice to be okay by morning
- Hook: *"Let me cry in the Uber, I'll be fine by my door"*
- Video: a taxi interior at night, a kind driver, city lights on wet windows, a front door

### 70 · Better Without the Ending
- Slug `70-better-without-the-ending` · moving on · solo
- Sound: pop, 102 BPM, E♭ major, guitar, claps, big chorus
- Pacing: mid
- Concept: the story was good; she just didn't like how it ended, so she's writing a new one
- Hook: *"The story was good, I'm just better without the ending"*
- Video: a typewriter, torn pages, a woman walking out of a frame into daylight

### 71 · Thank You for Leaving
- Slug `71-thank-you-for-leaving` · moving on · solo
- Sound: piano pop, 84 BPM, D♭ major, piano, strings, soft drums
- Pacing: ballad
- Concept: a genuine, unbitter thank you to the one who left, because the leaving built her
- Hook: *"Thank you for leaving, I finally arrived"*
- Video: a train platform, a new apartment, a plant that grows across the video

### 72 · Wrong Number
- Slug `72-wrong-number` · moving on / sassy · solo
- Sound: pop-rap, 120 BPM, G minor, brass, trap drums, chant chorus; UK register
- Pacing: uptempo
- Concept: he texts after six months and she answers like a stranger would; a new city, a new number, a new woman
- Hook: *"Sorry, wrong number, she doesn't live here anymore"*
- Video: a new flat, a phone shop, a girls' night, a message left on read, a city move

### 73 · I'm the Prize
- Slug `73-im-the-prize` · self-love · solo
- Sound: trap-pop, 96 BPM, B minor, 808s, sparse piano, hats
- Pacing: ballad/mid
- Concept: a slow, certain declaration that she's the prize, not the contestant
- Hook: *"I'm not the game, baby, I'm the prize"*
- Video: a trophy room, a runway of ordinary streets, gold light, a slow walk

### 74 · Blocked and Blooming
- Slug `74-blocked-and-blooming` · moving on · solo
- Sound: Afro-pop, 108 BPM, F major, log drums, bright guitar, shakers
- Pacing: mid
- Concept: she blocked him in winter and by spring she's a garden
- Hook: *"Blocked and blooming, look at me now"*
- Video: a flat filling up with plants, a balcony garden, a season change, bright colour

### 75 · Dating Myself
- Slug `75-dating-myself` · self-love · solo
- Sound: R&B, 94 BPM, C major, silky keys, snaps, layered harmonies
- Pacing: ballad/mid
- Concept: a solo date: dinner for one, flowers for herself, a movie alone, no apology
- Hook: *"I'm dating myself, and honestly it's going great"*
- Video: a restaurant table for one, a bouquet, a cinema seat, a bathtub, a smile

### 76 · Never Yours to Break
- Slug `76-never-yours-to-break` · heartbreak / strength · solo
- Sound: cinematic pop, 92 BPM, E minor lifting to G, piano, strings, 808
- Pacing: ballad
- Concept: he thought he broke her; she was never his to break
- Hook: *"My heart was never yours to break"*
- Video: a glass house that doesn't shatter, a storm outside, a woman standing still

### 77 · Glow Up Season
- Slug `77-glow-up-season` · self-love / fun · solo
- Sound: dance-pop, 122 BPM, A major, bright synths, claps, drop
- Pacing: uptempo
- Concept: the post-breakup glow up as a festival of self: gym, hair, laughing, a new dress, a new door
- Hook: *"It's glow up season, and I'm the sun"*
- Video: a montage of small wins, a salon, a run, a rooftop, a mirror

### 78 · Closure Isn't a Text
- Slug `78-closure-isnt-a-text` · moving on · solo
- Sound: bedroom pop, 88 BPM, G minor, guitar, soft drums, vocal layers
- Pacing: ballad
- Concept: she stops waiting for the message that would explain it, and writes her own closure
- Hook: *"Closure isn't a text, it's a door I close myself"*
- Video: a phone left on a table, a letter written and burned, a door closing softly

### 79 · Villain in Your Story
- Slug `79-villain-in-your-story` · sassy / dark pop · solo
- Sound: dark pop, 98 BPM, D minor, cinematic bass, snaps, choir hits
- Pacing: ballad/mid
- Concept: if she's the villain in his story, she'll wear the cape well
- Hook: *"I'll be the villain in your story, the hero in mine"*
- Video: a black dress, a gala staircase, red light, a smirk, a mirror that shows a crown

### 80 · Two Time Zones
- Slug `80-two-time-zones` · long distance · **duet**
- Sound: pop ballad, 90 BPM, C major, piano, soft synths, drums enter late
- Pacing: ballad
- Concept: her morning is his night; a duet across two clocks
- Hook: *"Two time zones, one heartbeat"*
- Video: split screen, sunrise and midnight, two windows, two phones, one call

### 81 · Ring on a Rainy Day
- Slug `81-ring-on-a-rainy-day` · wedding · **duet**
- Sound: wedding ballad, 82 BPM, E♭ major, piano, strings, acoustic guitar
- Pacing: ballad
- Concept: the proposal happened in the rain and the wedding does too, and that's the point
- Hook: *"You gave me a ring on a rainy day, so let it rain"*
- Video: a rainy proposal, a wedding under umbrellas, a first dance in a wet garden

### 82 · Landing Gear
- Slug `82-landing-gear` · long distance / reunion · solo
- Sound: pop, 108 BPM, D major, driving guitar, piano, big drums
- Pacing: mid
- Concept: the last hour before a reunion at arrivals; landing gear down, heart up
- Hook: *"Landing gear down, my heart's coming home"*
- Video: an airport arrivals hall, a plane window, a run, an embrace

### 83 · Video Call Slow Dance
- Slug `83-video-call-slow-dance` · long distance · **duet**
- Sound: R&B, 94 BPM, A♭ major, keys, snaps, harmonies
- Pacing: ballad/mid
- Concept: they slow dance on a video call, each holding a laptop, in two bedrooms
- Hook: *"Video call slow dance, hold your screen like it's me"*
- Video: two rooms, laptops, dancing alone together, split screen that merges at the end

### 84 · Grow Old Loud
- Slug `84-grow-old-loud` · commitment / fun · **duet**
- Sound: pop-rock, 118 BPM, E major, guitars, gang vocals, brass
- Pacing: uptempo
- Concept: a promise to grow old loudly: dance in the kitchen at eighty, still be embarrassing at weddings
- Hook: *"Let's grow old loud, baby, never grow old quiet"*
- Video: a couple aged through the video with makeup and costume, same kitchen, decades passing

### 85 · Vows I Didn't Rehearse
- Slug `85-vows-i-didnt-rehearse` · wedding · solo
- Sound: acoustic ballad, 84 BPM, G major, guitar, piano, strings
- Pacing: ballad
- Concept: she wrote her vows but at the altar says something else entirely
- Hook: *"These are the vows I didn't rehearse"*
- Video: a small wedding, a garden, a crumpled paper, a laugh through tears

### 86 · The Long Way to You
- Slug `86-the-long-way-to-you` · romance / journey · solo
- Sound: country-pop, 100 BPM, A major, acoustic guitar, steel-style guitar, drums
- Pacing: mid
- Concept: every wrong turn and wrong person was the long way to him
- Hook: *"I took the long way, but the long way led to you"*
- Video: a map, a road, wrong turns in montage, a porch at the end

### 87 · Keys to the Same Door
- Slug `87-keys-to-the-same-door` · commitment · **duet**
- Sound: pop, 104 BPM, C major, piano, claps, big chorus
- Pacing: mid
- Concept: moving in together: two keys cut, boxes, the first night, the argument about the couch
- Hook: *"Two keys to the same door, that's what I've been waiting for"*
- Video: a moving day, boxes, a keysmith, a first dinner on the floor

### 88 · Main Character
- Slug `88-main-character` · confidence · solo
- Sound: pop, 124 BPM, F major, bright synths, punchy drums
- Pacing: uptempo
- Concept: a Monday morning walk to work shot like the opening of a film she's the star of; the day she stops being a supporting role in her own life
- Hook: *"Main character, and the city's my set"*
- Video: a morning commute as a movie: slow-mo crossing, coffee, headphones, a wink at a camera

### 89 · Soft Girl, Steel Spine
- Slug `89-soft-girl-steel-spine` · confidence · solo
- Sound: trap-pop, 94 BPM, F♯ minor, 808s, piano, hats
- Pacing: ballad/mid
- Concept: soft doesn't mean weak; a song for the girls who cry and still win
- Hook: *"Soft girl, steel spine, don't confuse the two"*
- Video: pastel and concrete, a ballet studio and a boxing gym, a woman who is both

### 90 · Pretty and Powerful
- Slug `90-pretty-and-powerful` · confidence · **duet** (male rapper as Singer B)
- Sound: hip-hop pop, 100 BPM, G minor, 808s, brass, chant
- Pacing: uptempo class because of the rap verses (`render.json` wpm 140)
- Concept: she sings, he raps, both agree she's pretty and powerful and neither cancels the other
- Hook: *"Pretty and powerful, don't make me choose"*
- Video: a runway in a warehouse, a boardroom, a boxing ring, gold and black

### 91 · Unbothered
- Slug `91-unbothered` · confidence · solo
- Sound: Afrobeats, 108 BPM, E major, log drums, warm bass, guitar
- Pacing: mid
- Concept: the art of not caring, danced
- Hook: *"Unbothered, untouchable, in my lane"*
- Video: a sunny street, a rooftop, a market, a dance that says nothing can touch her

### 92 · Loud Lipstick
- Slug `92-loud-lipstick` · confidence / fun · solo
- Sound: pop-rock, 130 BPM, A major, big guitars, chant chorus
- Pacing: uptempo
- Concept: a red lipstick as armour, a night out as a victory lap
- Hook: *"Loud lipstick, louder me"*
- Video: a red lip in a mirror, a club, a stage, a crowd chanting

### 93 · Diamond Season
- Slug `93-diamond-season` · confidence · solo
- Sound: dance-pop, 126 BPM, B minor, glittering synths, drop
- Pacing: uptempo
- Concept: pressure made her a diamond; now it's diamond season
- Hook: *"Pressure made me, now it's diamond season"*
- Video: a jewellery-store fantasy, a coal mine to a gala, light refractions everywhere

### 94 · High Heels on Concrete
- Slug `94-high-heels-on-concrete` · confidence · solo
- Sound: drill-pop, 140 BPM, D minor, sliding 808s, hi-hat rolls, dark keys
- Pacing: uptempo
- Concept: the sound of her heels on the pavement as a drumline; the city hears her coming
- Hook: *"High heels on concrete, that's my drumbeat"*
- Video: a night city, low angles on heels, a tunnel, a bridge, a crowd parting

### 95 · Passport Stamps
- Slug `95-passport-stamps` · travel · solo
- Sound: global pop, 116 BPM, G major, world percussion, bright synths, guitar
- Pacing: mid
- Concept: a life measured in passport stamps and the people who came with each one
- Hook: *"Passport stamps and a heart full of places"*
- Video: airports, trains, markets, a beach, a mountain, a stamp sound on each cut

### 96 · Midnight in Mumbai
- Slug `96-midnight-in-mumbai` · travel / romance · solo
- Sound: Bollywood-fusion pop, 110 BPM, B minor, tabla, strings, modern bass, sitar plucks
- Pacing: mid
- Concept: one night in a city that never sleeps: sea breeze, a scooter, chai at 2 a.m., a stranger who feels like home
- Hook: *"Midnight in Mumbai, and the city's wide awake"*
- Video: a sea-facing promenade at night, a scooter ride, a chai stall, neon and monsoon air

### 97 · Vespa Through the Old Town
- Slug `97-vespa-through-the-old-town` · travel / romance · solo
- Sound: Italian-flavoured pop, 112 BPM, C major, mandolin-like plucks, accordion touch, claps
- Pacing: mid
- Concept: a summer holiday romance on a scooter through cobbled streets, gelato, a fountain, a promise to come back
- Hook: *"On a Vespa through the old town, holding on to you"*
- Video: a Mediterranean old town, a scooter, a fountain, a piazza at night

### 98 · Hostel Hearts
- Slug `98-hostel-hearts` · travel / friendship · solo
- Sound: indie pop, 106 BPM, D major, acoustic guitar, claps, harmonies
- Pacing: mid
- Concept: the strangers you meet in a hostel who become family for four days
- Hook: *"Hostel hearts, strangers for a night, family by the morning"*
- Video: a hostel common room, a rooftop, a night market, a goodbye at a bus station

### 99 · City Lights Don't Sleep
- Slug `99-city-lights-dont-sleep` · city nights · solo
- Sound: synthwave, 114 BPM, F minor, analogue synths, gated drums, bass arp
- Pacing: mid
- Concept: an insomniac love letter to the city that stays up with her
- Hook: *"City lights don't sleep, and neither do we"*
- Video: a night skyline, a taxi, a diner, a bridge, neon reflected on wet streets

### 100 · The Hundredth Song
- Slug `100-the-hundredth-song` · anthem / closer · **duet**
- Sound: anthemic cinematic pop, 98 BPM, F♯ minor lifting to A major, piano, strings, full band, choir
- Pacing: ballad/mid
- Concept: the catalogue's closer: a song about all the songs, every heartbreak and party and kitchen dance, and the one voice that carried them
- Hook: *"This is the hundredth song, and I'm still singing"*
- Video: a montage of every previous video world, ending on an empty stage with one microphone

## Checklist

Tick when the folder is complete and `verify_lyrics.py --voice-ref songs/01-fire-in-the-rain` passes.

- [x] 09 Slow Dance in the Kitchen
- [x] 10 Sunday Mornings
- [x] 11 Eyes on Me
- [x] 12 First Kiss at Last Call
- [x] 13 Golden Hour on Your Skin
- [x] 14 Your Name in Cursive
- [x] 15 Butterflies Don't Lie
- [x] 16 Airplane Mode
- [x] 17 Corner Table
- [x] 18 Forever Looks Like Tuesday
- [x] 19 Hold My Hand in Public
- [x] 20 Pretty When You Laugh
- [x] 21 Under the Same Umbrella
- [x] 22 Stay Till the Credits
- [x] 23 Made of Sunlight
- [x] 24 Yes to Everything
- [x] 25 Falling Slowly, Landing Soft
- [x] 26 Fireworks in February
- [x] 27 The Way You Say Good Morning
- [x] 28 We Look Good Together
- [x] 29 Sugar on My Tongue
- [x] 30 Don't Tell the Neighbours
- [x] 31 Lipstick on Your Collar
- [x] 32 Read at Eleven Fifty-Nine
- [x] 33 Bad Idea, Good Night
- [x] 34 Trouble Looks Cute on You
- [x] 35 Borrowed Shirt
- [x] 36 Dance Like Nobody's Sober
- [x] 37 Mirror, Mirror
- [x] 38 Wine and Whispers
- [x] 39 Your Place or Mine
- [x] 40 Call Me After Midnight
- [x] 41 Weekend Starts on Thursday
- [x] 42 Sunburn and Strawberries
- [x] 43 Rooftop Radio
- [x] 44 No Plans, No Problem
- [x] 45 Windows Down
- [x] 46 Confetti in My Hair
- [x] 47 Beach Bonfire Hearts
- [x] 48 Cheap Champagne
- [x] 49 Deep End
- [x] 50 Late Checkout
- [x] 51 Dancing on the Table
- [x] 52 After Hours
- [x] 53 Festival Season
- [x] 54 Barefoot on the Boulevard
- [x] 55 Ride or Die
- [x] 56 Cassette Tape Heart
- [x] 57 Hometown Radio
- [x] 58 Kids on Bicycles
- [x] 59 Grandma's Kitchen
- [x] 60 The Old Playlist
- [x] 61 Class of Forever
- [x] 62 Fireflies and Porch Lights
- [x] 63 Photo Booth Strip
- [x] 64 Best Friend Blueprint
- [x] 65 Mango Season
- [x] 66 Scrapbook of Us
- [x] 67 That Summer Song
- [x] 68 Unfollowed
- [x] 69 Cry in the Uber
- [x] 70 Better Without the Ending
- [x] 71 Thank You for Leaving
- [x] 72 Wrong Number
- [x] 73 I'm the Prize
- [x] 74 Blocked and Blooming
- [x] 75 Dating Myself
- [x] 76 Never Yours to Break
- [x] 77 Glow Up Season
- [x] 78 Closure Isn't a Text
- [x] 79 Villain in Your Story
- [x] 80 Two Time Zones
- [x] 81 Ring on a Rainy Day
- [x] 82 Landing Gear
- [x] 83 Video Call Slow Dance
- [x] 84 Grow Old Loud
- [x] 85 Vows I Didn't Rehearse
- [x] 86 The Long Way to You
- [x] 87 Keys to the Same Door
- [x] 88 Main Character
- [x] 89 Soft Girl, Steel Spine
- [x] 90 Pretty and Powerful
- [x] 91 Unbothered
- [x] 92 Loud Lipstick
- [x] 93 Diamond Season
- [x] 94 High Heels on Concrete
- [x] 95 Passport Stamps
- [x] 96 Midnight in Mumbai
- [x] 97 Vespa Through the Old Town
- [x] 98 Hostel Hearts
- [x] 99 City Lights Don't Sleep
- [x] 100 The Hundredth Song
