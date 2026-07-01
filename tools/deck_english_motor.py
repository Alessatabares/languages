"""English deck — THE MOTOR (core engine of the language).

NOT an immersion/reading deck (that's the Nietzsche one, for when you already
have the level). This is the FOUNDATION: the structural skeleton + the
high-frequency motor that covers 70%+ of everything spoken and written —
function words, auxiliaries/modals, the basic connectors, the light verbs and
the generative sentence frames.

Deliberate exception to the repo's "never invent" rule: a foundation deck has no
source video, so the sentences are invented on purpose — short, funny and vivid
(vivid, absurd sentences are more memorable). Active recall via cloze; system
thinking via Intention (the job) + Pattern (the reusable frame) + note (the
contrast). All monolingual English.

Study one plane at a time (tags), not the whole deck at once.

Run:  python tools/deck_english_motor.py   ->  english/motor/motor.apkg
"""

import deck_builder

LANGUAGE = "english"
BOOK_SLUG = "motor"    # Anki deck name -> english::motor
DECK_ID = 1987452312   # stable: re-import updates instead of duplicating
LEVEL = "core"
SUBFOLDER = "motor"    # the .apkg lives in english/motor/

SOURCE_URL = ""  # curated foundation deck, no source video (legitimately empty)
DESCRIPTION = (
    "English · CORE MOTOR. The structural engine that covers 70%+ of the "
    "language: function words, the tense/modal engine, basic connectors, light "
    "verbs and generative sentence frames. Active recall (cloze) + system "
    "thinking (every back states the job, the reusable pattern and the contrast "
    "with its neighbour). Sentences are invented on purpose — short, funny, "
    "memorable. Study one plane (tag) at a time. Monolingual English = transfer."
)

# PATTERN-CENTRIC design (hybrid). The learning unit is the PATTERN, not the word:
#   FORK (the discriminator) -> VARIATION (several examples) -> COMPRESSION (the rule).
#
# Two card shapes, same note type:
#   1) CONTRAST SET — a fork with a confusable neighbour (who vs which, much vs
#      many). Front = a <div class='title'> naming the fork + 4-6 varied example
#      lines, EACH with its pivot in {{c1::...}}. All blanks are c1 -> ONE card
#      ("fill every blank"), and the answers differ across lines so you must
#      actually discriminate, not autopilot.
#   2) SIMPLE — an item with no obvious neighbour (of, used to). Front = 1-2
#      example lines clozed; no title needed.
#
# Fields:
#   plane     : "grammar" | "verb-construction" | "connector" | "expression"
#   rule      : the discriminator headline, shown big/red first on the back
#   text      : title (optional <div class='title'>) + example line(s), "\n"-joined,
#               pivots in {{c1::...}}  (invented on purpose — vivid & funny = memorable)
#   intention : the JOB the pattern does (system thinking)
#   image / pattern / synonyms / note : optional, as before

CARDS = [
    # ============ A. POINTING & REFERENCE (point / refer) ============
    dict(plane="grammar",
         rule="who → a PERSON · which → a THING · that → either (informal)",
         text=("<div class='title'>who vs which</div>"
               "① The neighbour {{c1::who}} narrates his own life is back.\n"
               "② He bought a horn {{c1::which}} only plays one sad note.\n"
               "③ The barista {{c1::who}} remembers my order is a wizard.\n"
               "④ A law {{c1::which}} nobody enforces is just a suggestion.\n"
               "⑤ People {{c1::who}} clap when the plane lands worry me."),
         intention="Relative pronouns glue extra info onto a noun; the blank forces the person/thing choice.",
         pattern="the PERSON who + verb · the THING which/that + verb",
         note="Trap: 'that' works for both informally, but never use 'which' for a person."),
    dict(plane="grammar",
         rule="this/these → near me · that/those → far from me",
         text=("<div class='title'>this / that / these / those</div>"
               "① Take {{c1::this}} pen here, not that one across the room.\n"
               "② {{c1::That}} noise upstairs has opinions.\n"
               "③ {{c1::These}} socks (on my feet) don't match.\n"
               "④ Who left {{c1::those}} shoes by the far door?"),
         intention="Demonstratives point by distance in space, time and conversation.",
         image="Jabbing your own shoe ('this') vs pointing at the moon ('that').",
         note="this/that = singular; these/those = plural."),
    dict(plane="grammar",
         rule="dummy IT → weather/time/distance · dummy THERE → something EXISTS",
         text=("<div class='title'>dummy it vs there</div>"
               "① {{c1::It}}'s raining frogs again, and nobody is surprised.\n"
               "② {{c1::There}}'s a raccoon in the lobby acting like a guest.\n"
               "③ {{c1::It}}'s already Monday? Rude.\n"
               "④ {{c1::There}} are three unread alarms judging me."),
         intention="English refuses a subjectless sentence: 'it' fills the seat; 'there' announces existence.",
         pattern="It is + weather/time · There is/are + something new",
         note="Neither is a real thing — both just hold the subject slot."),
    dict(plane="grammar",
         rule="singular they → one unknown/unspecified person, no he/she",
         text="Somebody left a sandwich in the printer; {{c1::they}} know what they did.",
         intention="Refer to one unknown (or nonbinary) person without picking he or she.",
         pattern="someone / a person ... they",
         note="Fully standard for an unknown referent."),

    # ============ B. ARTICLES & QUANTITY (new vs known, count vs mass) ============
    dict(plane="grammar",
         rule="a → new to the listener (1st mention) · the → we both know which one",
         text=("<div class='title'>a vs the</div>"
               "① I adopted {{c1::a}} goose today.\n"
               "② Then {{c1::the}} goose adopted the sofa.\n"
               "③ She wrote {{c1::a}} book about silence.\n"
               "④ {{c1::The}} book (that one) is now a doorstop."),
         intention="Switch a → the the moment the thing has been introduced or is unique.",
         pattern="a (new) → the (now known)",
         note="'a' before a consonant sound, 'an' before a vowel sound."),
    dict(plane="grammar",
         rule="some → positive & offers · any → questions & negatives",
         text=("<div class='title'>some vs any</div>"
               "① Is there {{c1::any}} dignity left after karaoke?\n"
               "② There's {{c1::some}} soup, if you're brave.\n"
               "③ I didn't bring {{c1::any}} regrets.\n"
               "④ Want {{c1::some}} tea? (offer)"),
         intention="Grade unknown quantity by sentence type.",
         pattern="some (positive) ↔ any (question / negative)",
         note="Offer exception: 'Want some tea?' uses some, not any."),
    dict(plane="grammar",
         rule="many + countable (plural) · much + uncountable (mass)",
         text=("<div class='title'>much vs many</div>"
               "① Too {{c1::many}} opinions, not enough evidence.\n"
               "② There isn't {{c1::much}} evidence, sadly.\n"
               "③ How {{c1::many}} tabs are open right now?\n"
               "④ I don't have {{c1::much}} patience left."),
         intention="Split quantity by whether the noun counts as separate items or one mass.",
         image="A crowd of waving hands ('many') vs one grey puddle ('much').",
         note="many + plural noun | much + mass noun."),
    dict(plane="grammar",
         rule="every → all, but one-by-one (singular verb) · all → the whole group",
         text=("<div class='title'>every vs all</div>"
               "① {{c1::Every}} plant in this house is plotting.\n"
               "② {{c1::All}} the plants are plotting together.\n"
               "③ {{c1::Every}} email deserves a nap first.\n"
               "④ {{c1::All}} my socks vanished at once."),
         intention="Same set, two camera angles: individual view vs the group as a whole.",
         pattern="every + singular noun + singular verb · all + plural noun + plural verb"),

    # ============ C. PREPOSITIONS (place things in space / time / logic) ============
    dict(plane="grammar",
         rule="at → a point · on → a surface/day · in → inside/month (zoom out)",
         text=("<div class='title'>at / on / in (place & time)</div>"
               "① Meet me {{c1::at}} the vending machine at noon.\n"
               "② The cat is asleep {{c1::on}} the keyboard on Monday.\n"
               "③ My motivation is hiding {{c1::in}} a drawer, in May.\n"
               "④ See you {{c1::at}} 8pm, {{c1::on}} Friday, {{c1::in}} 2026."),
         intention="One scale for space AND time: precise point → surface/day → enclosed/month.",
         image="A funnel zooming out: at (dot) → on (day) → in (month).",
         note="Same order works for place and for time."),
    dict(plane="grammar",
         rule="to → toward a destination · from → the origin/source",
         text=("<div class='title'>to vs from</div>"
               "① I'm walking {{c1::to}} the fridge with tremendous purpose.\n"
               "② This smell is coming {{c1::from}} the gym bag of doom.\n"
               "③ She drove {{c1::from}} chaos {{c1::to}} slightly-less-chaos."),
         intention="Direction as an arrow: from = tail (start), to = head (goal/receiver).",
         pattern="go / walk / give ... from + origin ... to + destination"),
    dict(plane="grammar",
         rule="of → part / possession / 'made of' (the invisible glue)",
         text="The leg {{c1::of}} the table has given up on life.",
         intention="Near-invisible relationship glue — belonging, a part, or material.",
         pattern="the X of Y (part / possession)",
         note="Glue, not 'about'. Hugely frequent."),
    dict(plane="grammar",
         rule="with → using a tool, or alongside a person",
         text="I fixed it {{c1::with}} tape and false confidence.",
         intention="Instrument or company.",
         pattern="do X with + tool / person"),
    dict(plane="grammar",
         rule="for → purpose, reason, or who benefits",
         text="This trophy is {{c1::for}} 'Most Naps Taken'.",
         intention="Points at the goal or beneficiary.",
         pattern="for + purpose / for + person"),
    dict(plane="grammar",
         rule="by → the doer in a passive · also 'by means of'",
         text="The cake was eaten {{c1::by}} 'nobody' (by hand, apparently).",
         intention="The passive's secret author; also transport/method.",
         pattern="X was done by + agent | by + transport (by bus)"),
    dict(plane="grammar",
         rule="about → concerning / on the topic of",
         text="We need to talk {{c1::about}} your relationship with the snooze button.",
         intention="Marks the topic.",
         pattern="talk / think / worry about + topic"),
    dict(plane="grammar",
         rule="between → in the gap separating two named things",
         text="The truth sits {{c1::between}} the menu photo and reality.",
         intention="Locates something in the space (or difference) dividing A and B.",
         image="A sad burger squeezed between two glossy photos.",
         pattern="between A and B"),
    dict(plane="grammar",
         rule="through → in one side and out the other (space/time/process)",
         text="I got {{c1::through}} Monday on snacks alone.",
         intention="Passage all the way across.",
         pattern="through + a tunnel / the week / a process"),

    # ============ D. THE TENSE / MOOD ENGINE (auxiliaries & modals) ============
    dict(plane="grammar",
         rule="do/does/did → build questions & negatives in simple present/past",
         text=("<div class='title'>do — questions & negatives</div>"
               "① {{c1::Do}} you actually like jazz, or just the idea of it?\n"
               "② I {{c1::don't}} trust stairs; they're up to something.\n"
               "③ {{c1::Does}} she know the plant is fake?\n"
               "④ We {{c1::didn't}} plan this, it just happened."),
         intention="The simple tenses have no other helper, so 'do' carries the question/negative.",
         pattern="Do/Does/Did + subject + base verb? · subject + don't/doesn't/didn't + base verb",
         note="No 'do' → no simple-tense question or negative."),
    dict(plane="grammar",
         rule="be + V-ing → happening now / temporary",
         text="Why {{c1::are}} you whispering to the broccoli?",
         intention="Present continuous: action around now, not permanent.",
         pattern="am/is/are + V-ing (now / around now)"),
    dict(plane="grammar",
         rule="have + V3 → past action, present relevance (no exact time)",
         text=("<div class='title'>present perfect vs its -ing form</div>"
               "① I {{c1::have}} never met a dog I didn't trust.\n"
               "② I've {{c1::been}} 'about to start' for three hours.\n"
               "③ She {{c1::has}} finished (result: it's done now).\n"
               "④ We've {{c1::been}} waiting since the ice age."),
         intention="have + V3 = result/experience now; have been + -ing = started earlier and still going.",
         pattern="have/has + V3 (result now) · have/has been + V-ing (up to now)",
         note="Links past to now; no exact time stated."),
    dict(plane="grammar",
         rule="be (was/were) + V3 → passive: the receiver becomes the subject",
         text="The window {{c1::was}} broken by 'the wind' (it was me).",
         intention="Move the doer off-stage; spotlight the thing acted on.",
         pattern="X was/were + V3 (by agent)"),
    dict(plane="grammar",
         rule="will → decided NOW / promise · going to → already-decided plan",
         text=("<div class='title'>will vs going to</div>"
               "① Fine — I {{c1::will}} water your cactus, calm down.\n"
               "② I'm {{c1::going to}} regret this third coffee.\n"
               "③ That glass {{c1::will}} fall — wait, it fell.\n"
               "④ We're {{c1::going to}} paint the room on Sunday (planned)."),
         intention="Both are future; the split is spontaneous decision vs pre-made plan/evidence.",
         pattern="will + base verb (decision/promise) · be going to + base verb (plan/prediction)"),
    dict(plane="grammar",
         rule="can → ability / informal permission · could → polite / past ability / soft maybe",
         text=("<div class='title'>can vs could</div>"
               "① I {{c1::can}} touch my elbow with my tongue. (I cannot.)\n"
               "② {{c1::Could}} you pass the chaos, please?\n"
               "③ She {{c1::can}} smell a lie from space.\n"
               "④ We {{c1::could}} leave now, or we could suffer."),
         intention="Same family; could is softer/more distant (politeness, past, tentative possibility).",
         pattern="can + base verb (able/allowed) · could + base verb (polite/maybe/used to be able)"),
    dict(plane="grammar",
         rule="must → strong obligation OR confident deduction ('surely true')",
         text=("<div class='title'>must — two jobs</div>"
               "① You {{c1::must}} wear shoes; it's the law of the café.\n"
               "② You've read it five times — you {{c1::must}} love it.\n"
               "③ I {{c1::must}} sleep. (obligation)\n"
               "④ The lights are off; they {{c1::must}} be asleep. (deduction)"),
         intention="Same word, two jobs: what's required, and what's almost certainly the case.",
         pattern="must + base verb (have to / surely)",
         note="The deduction sense runs half of real conversation."),
    dict(plane="grammar",
         rule="should → advice/expectation · must → obligation (stronger)",
         text=("<div class='title'>should vs must</div>"
               "① You {{c1::should}} sleep instead of buying a kayak online.\n"
               "② Passengers {{c1::must}} fasten their seatbelts.\n"
               "③ You {{c1::should}} call her (good idea).\n"
               "④ You {{c1::must}} not touch that wire (no choice)."),
         intention="Grade of pressure: should = recommended; must = required.",
         pattern="should + base verb (advice) · must + base verb (obligation)"),
    dict(plane="grammar",
         rule="might / may → uncertain, ~50/50 possibility",
         text="I {{c1::might}} go, or I might become one with the couch.",
         intention="Flag genuine uncertainty.",
         pattern="might / may + base verb (maybe)"),
    dict(plane="grammar",
         rule="would → result of an unreal/imagined situation · also politeness",
         text="A normal person {{c1::would}} stop here. I am not that person.",
         intention="The 'then' half of an imagined world; also softens requests.",
         pattern="would + base verb (if... / polite)",
         note="It's the 'd in I'd, he'd, we'd."),

    # ============ E. GENERATIVE FRAMES (one card → infinite sentences) ============
    dict(plane="expression",
         rule="1st → real future · 2nd → unreal now · 3rd → impossible past (regret)",
         text=("<div class='title'>the three conditionals</div>"
               "① {{c1::If}} you feed it once, it lives here now. (real)\n"
               "② If I {{c1::were}} a cloud, I'd rain on loud chewers. (unreal now)\n"
               "③ If I {{c1::had}} known, I would have stayed in bed. (past)"),
         intention="One ladder of distance from reality: real → imagined present → unchangeable past.",
         pattern="If + present, will... · If + past, would... · If + had V3, would have V3",
         note="Use 'were' for every subject in the 2nd: if I were, if he were."),
    dict(plane="expression",
         rule="The more X, the more Y → two things rise together",
         text="{{c1::The more}} I tidy, the more the cat un-tidies.",
         intention="Link two rising quantities elegantly and endlessly.",
         image="A seesaw where, impossibly, both sides go up.",
         pattern="The + comparative X, the + comparative Y"),
    dict(plane="expression",
         rule="used to → past habit/state that is no longer true",
         text="I {{c1::used to}} have hobbies; now I have browser tabs.",
         intention="Mark a discontinued past routine.",
         pattern="used to + base verb (past habit, now stopped)"),
    dict(plane="expression",
         rule="'d rather → prefer · 'd better → strong warning (or else)",
         text=("<div class='title'>would rather vs had better</div>"
               "① I'd {{c1::rather}} fight a goose than reply to that email.\n"
               "② You'd {{c1::better}} hide the snacks before he arrives.\n"
               "③ I'd {{c1::rather}} stay in.\n"
               "④ We'd {{c1::better}} leave now, or we'll miss it."),
         intention="Both are 'd + word, but one states a preference, the other a threat-tinged urgency.",
         pattern="'d rather + base verb (than...) · 'd better + base verb (or trouble)"),

    # ============ F. CONNECTORS (join ideas so they flow) ============
    dict(plane="connector",
         rule="and → add · but → contrast · or → alternative",
         text=("<div class='title'>and / but / or</div>"
               "① I came for closure {{c1::and}} stayed for the snacks.\n"
               "② The plan was perfect, {{c1::but}} reality showed up.\n"
               "③ Choose: your dignity {{c1::or}} the last slice."),
         intention="The three basic joins: pile on, turn against, offer a fork.",
         pattern="X and Y · X but Y · X or Y"),
    dict(plane="connector",
         rule="because → the cause · so → the result (mirror images)",
         text=("<div class='title'>because vs so</div>"
               "① I'm whispering {{c1::because}} the toddler finally slept.\n"
               "② The floor was wet, {{c1::so}} I did an unplanned dance.\n"
               "③ We left early {{c1::because}} the band was loud.\n"
               "④ The band was loud, {{c1::so}} we left early."),
         intention="Same causal link, opposite order: effect ← because ← cause · cause → so → effect.",
         pattern="Y because X (cause after) · X, so Y (result after)",
         note="because + clause; because OF + noun."),
    dict(plane="connector",
         rule="although → concede a fact · while → during / whereas",
         text=("<div class='title'>although vs while</div>"
               "① {{c1::Although}} the cake collapsed, morale did not.\n"
               "② I meditate {{c1::while}} the smoke alarm sings backup.\n"
               "③ {{c1::Although}} it's cheap, it works.\n"
               "④ She cooked {{c1::while}} he 'supervised'."),
         intention="although = surprise/concession; while = same-time (or soft contrast).",
         pattern="Although + clause, main · while + clause (during / whereas)",
         synonyms="although → even though, though"),
    dict(plane="connector",
         rule="when → at the time that (a point) · while → during (a stretch)",
         text=("<div class='title'>when vs while</div>"
               "① {{c1::When}} the music stops, everyone pretends to work.\n"
               "② {{c1::While}} the music played, chaos reigned.\n"
               "③ Call me {{c1::when}} you land. (moment)\n"
               "④ Don't text {{c1::while}} you drive. (during)"),
         intention="when points at a moment/trigger; while stretches over a duration.",
         pattern="When X happens, Y · while + ongoing action"),
    dict(plane="connector",
         rule="that → links a reported thought/fact to know/think/say",
         text="I knew {{c1::that}} the silence was suspicious.",
         intention="Introduces the content of a thought or report.",
         pattern="think / know / say (that) + clause",
         note="Often droppable: 'I knew the silence was...'."),

    # ============ G. LIGHT VERBS (the few verbs that do most of the work) ============
    dict(plane="verb-construction",
         rule="make → produce / cause · do → perform a task",
         text=("<div class='title'>make vs do</div>"
               "① Please {{c1::make}} it make sense.\n"
               "② I'll {{c1::do}} the dishes right after doing nothing.\n"
               "③ Don't {{c1::make}} me a promise you'll break.\n"
               "④ Could you {{c1::do}} me a favour?"),
         intention="make builds/causes something; do carries out an activity.",
         pattern="make + a decision/sense · make someone + adj/verb · do + the dishes/homework/a favour"),
    dict(plane="verb-construction",
         rule="get → obtain / become / arrive / cause-to-be (Swiss-army verb)",
         text="Let's {{c1::get}} this over with before I overthink it.",
         intention="If you can't find the verb, it's probably 'get'.",
         pattern="get + thing / adjective / place (get coffee / get tired / get home)"),
    dict(plane="verb-construction",
         rule="take → require time/effort, or grab/perform set actions",
         text="This will {{c1::take}} forever and at least two snacks.",
         intention="Duration or a fixed action-chunk.",
         pattern="take + time / a look / care / a break"),
    dict(plane="verb-construction",
         rule="have → possess, or 'experience/do' inside set chunks",
         text="Let's {{c1::have a look}} before we panic.",
         intention="Beyond possession: have packages many small experiences.",
         pattern="have + a look / a rest / a shower / breakfast"),
    dict(plane="verb-construction",
         rule="go → move away from here, or 'become' (go bad, go viral)",
         text="This conversation is {{c1::going}} nowhere, beautifully.",
         intention="Motion, or a change of state (usually for the worse).",
         pattern="go + place · go + adjective (go cold / go quiet)"),
    dict(plane="verb-construction",
         rule="give → transfer to someone (spawns give up, give a hand)",
         text="{{c1::Give}} me one good reason and the cookie is yours.",
         intention="Hand something over; a phrasal-verb factory.",
         pattern="give + someone + something"),
    dict(plane="verb-construction",
         rule="keep + V-ing → continue / don't stop",
         text="{{c1::Keep}} pretending you didn't see the mess.",
         intention="Maintain an ongoing action.",
         pattern="keep + V-ing (continue)"),
    dict(plane="verb-construction",
         rule="let + someone + base verb → allow / permit",
         text="{{c1::Let}} it go before it lives in your head rent-free.",
         intention="Grant permission or release.",
         pattern="let + someone + base verb"),
    dict(plane="verb-construction",
         rule="want / need + to + base verb → desire vs requirement",
         text="I {{c1::want}} the outcome but I don't need the process.",
         intention="want = desire; need = require. Both take to + verb.",
         pattern="want / need + to + base verb"),

    # ============ H. NEGATION, DEGREE & TIMING (invert / grade) ============
    dict(plane="grammar",
         rule="one negative per clause — nothing/never/nobody are ALREADY negative",
         text=("<div class='title'>negation — no double negatives</div>"
               "① I'm {{c1::not}} arguing; I'm just loudly correct.\n"
               "② I have {{c1::nothing}} to declare but glitter and regret.\n"
               "③ I {{c1::never}} cry at movies. (I always do.)\n"
               "④ {{c1::Nobody}} touched the last slice. (not: didn't touch nobody)"),
         intention="'not' rides the auxiliary; the -thing/-body/never words carry their own negative.",
         pattern="aux + not + verb · nothing/nobody/never (built-in negative)",
         note="Trap: 'I don't have nothing' is wrong — pick one negative."),
    dict(plane="grammar",
         rule="frequency (always>usually>often>sometimes>never): before main verb, after 'be'",
         text=("<div class='title'>frequency adverb placement</div>"
               "① I {{c1::always}} say I'll start on Monday.\n"
               "② She is {{c1::never}} late, somehow.\n"
               "③ We {{c1::usually}} forget the umbrella.\n"
               "④ He is {{c1::often}} right, annoyingly."),
         intention="Position is the rule: squeeze before the main verb, but sit after 'be'.",
         pattern="subject + [freq] + main verb · be + [freq]"),
    dict(plane="grammar",
         rule="very → neutral 'a lot' · too → a problem · so → intense, with feeling",
         text=("<div class='title'>very / too / so</div>"
               "① It's {{c1::too}} hot to function, so I won't.\n"
               "② The soup is {{c1::very}} good, thanks.\n"
               "③ I'm {{c1::so}} tired that I dreamt standing up.\n"
               "④ This box is {{c1::too}} heavy to lift."),
         intention="Grade an adjective by attitude: neutral, problem, or emotional intensity.",
         pattern="too + adj (to...) · very + adj (neutral) · so + adj (that...)"),
    dict(plane="grammar",
         rule="already → sooner than expected(+) · yet → so far(?/–) · still → continuing",
         text=("<div class='title'>already / yet / still</div>"
               "① You've {{c1::already}} eaten? It's 9am.\n"
               "② Are we there {{c1::yet}}? We haven't left.\n"
               "③ I {{c1::still}} haven't started, classic.\n"
               "④ Has it finished {{c1::yet}}?"),
         intention="Three timing lenses on an expected event.",
         pattern="already (+) · yet (? / –) · still (ongoing)"),
    dict(plane="grammar",
         rule="just → a moment ago (have just V3), or 'only / simply'",
         text="I {{c1::just}} finished — like, ten seconds ago.",
         intention="Tiny word, big nuance: recency or minimisation.",
         pattern="have just + V3 (recent) · just = only"),

    # ============ I. WH- QUESTIONS (open the missing information) ============
    dict(plane="grammar",
         rule="what → thing · why → reason · how → manner · where → place · whose → owner",
         text=("<div class='title'>wh- questions</div>"
               "① {{c1::What}} is that noise, and why is it friendly?\n"
               "② {{c1::Why}} is the printer always hungry on deadlines?\n"
               "③ {{c1::How}} did the goat get on the roof?\n"
               "④ {{c1::Where}} did my twenties go?\n"
               "⑤ {{c1::Whose}} idea was the indoor slip-n-slide?"),
         intention="Each wh- word opens a specific information gap; the frame after it stays the same.",
         pattern="Wh- + (aux) + subject + verb?  ·  Whose/Which + noun ...?",
         note="how also pairs with adjectives: how far / long / old."),
]

if __name__ == "__main__":
    import shutil

    path = deck_builder.build(LANGUAGE, BOOK_SLUG, DECK_ID, CARDS, LEVEL, DESCRIPTION)
    # Relocate the .apkg into the english/motor/ subfolder.
    sub = path.parent / SUBFOLDER
    sub.mkdir(exist_ok=True)
    dest = sub / f"{BOOK_SLUG}.apkg"
    shutil.move(str(path), str(dest))
    print(f"Moved -> {dest.relative_to(path.parent.parent)}")
