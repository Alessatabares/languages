# -*- coding: utf-8 -*-
"""French deck — "L'histoire de Lustucru" (Contes de la rue Broca).

Targets the A2 band. This tale is NARRATED, not just spoken, so it carries what
the A1 decks cannot: the passe simple, the plus-que-parfait, the passive, and
cleft sentences. Fourth French deck - nothing repeats from gentil-petit-diable,
sorciere-rue-mouftard or motor (checked with tools/cobertura.py).

Sentences are taken from the YouTube video transcript (obvious ASR typos fixed;
proper nouns restored: Alesia, Vercingetorix, Jules Cesar).

Run:  python tools/deck_french_lustucru.py   ->  french/lustucru.apkg
"""

import deck_builder

LANGUAGE = "french"
SLUG = "lustucru"
DECK_ID = 1987452323   # stable: re-import updates instead of duplicating
LEVEL = "a2"

SOURCE_URL = "https://www.youtube.com/watch?v=AkZyxDAPdX0"
DESCRIPTION = (
    "French &middot; A2. A NARRATED tale, so it carries what the A1 decks cannot: "
    "the pass&eacute; simple, the plus-que-parfait, the passive and cleft sentences, "
    "plus the connectors of written storytelling. From <i>L'histoire de Lustucru</i> "
    "(Contes de la rue Broca). Nothing repeats from the other French decks."
    + (f"<br>Source video: <a href='{SOURCE_URL}'>{SOURCE_URL}</a>" if SOURCE_URL else "")
)

CARDS = [
    # ============ VOCABULARY ============
    dict(plane="vocab", term="roi",
         text="Il y a très longtemps, dans un pays lointain, vivait un {{c1::roi}} barbare et cruel.",
         meaning="king",
         intention="Core tale word; you will meet it in every story you read.",
         image="A barbarian king on a rough throne.",
         note="Masculine: le roi. Feminine: la reine (completely different word)."),
    dict(plane="vocab", term="avenir",
         text="Alors sorcière, quel {{c1::avenir}} prévois-tu pour mon fils?",
         meaning="future",
         intention="Talk about what lies ahead — for a person, a country, a plan.",
         image="A witch reading what is to come.",
         note="Masculine: l'avenir. Careful: 'le futur' exists but is mostly the "
              "grammatical tense; for life ahead, use l'avenir."),
    dict(plane="vocab", term="vieille",
         text="Eh bien parle, la {{c1::vieille}}!",
         meaning="old woman (blunt)",
         intention="Address or refer to an old woman — rude, as here.",
         image="The king shouting at the witch.",
         note="Feminine of 'vieux'. Note the irregular pair: vieux / vieille. "
              "Polite version: une vieille dame."),
    dict(plane="vocab", term="nom",
         text="Ton fils laissera son {{c1::nom}} dans l'histoire.",
         meaning="name",
         intention="The word the entire tale turns on.",
         image="A name carved into a monument — or rubbed out of one.",
         note="Masculine: le nom. 'Le prénom' = first name, 'le nom' = surname."),
    dict(plane="vocab", term="vainqueur",
         text="Voici notre nouvel empereur, le véritable {{c1::vainqueur}} des Gaulois.",
         meaning="winner / victor",
         intention="Who won — a battle, a race, a competition.",
         image="The general getting the credit for someone else's victory.",
         note="Masculine: le vainqueur. From vaincre (to defeat)."),
    dict(plane="vocab", term="chef",
         text="Les Romains obligèrent le {{c1::chef}} des Gaulois à venir déposer ses armes.",
         meaning="leader / chief; also a head chef",
         intention="Whoever is in charge — of a tribe, a team, a kitchen.",
         image="The Gaulish leader laying down his weapons.",
         note="Masculine: le chef. 'Le chef d'orchestre', 'le chef de service'."),
    dict(plane="vocab", term="récit",
         text="Le secrétaire avait truqué le {{c1::récit}}.",
         meaning="account / narrative / telling",
         intention="The written version of events — the story as reported.",
         image="A scroll where one name has been swapped for another.",
         note="Masculine: le récit. From raconter. More formal than 'histoire'."),
    dict(plane="vocab", term="exploits",
         text="Mais enfin, voici le livre où sont racontés mes {{c1::exploits}}!",
         meaning="feats / great deeds",
         intention="Remarkable achievements, usually heroic or sporting.",
         image="A book listing everything he supposedly did.",
         note="Masculine: un exploit. The -t is silent."),
    dict(plane="vocab", term="tentatives",
         text="Il fit encore bien d'autres {{c1::tentatives}} pour entrer dans l'histoire.",
         meaning="attempts",
         intention="Say someone tried repeatedly and failed.",
         image="Two thousand years of failed attempts.",
         note="Feminine: une tentative. From tenter (to attempt, to tempt)."),
    dict(plane="vocab", term="siècles",
         text="Et quelques {{c1::siècles}} plus tard, savez-vous qui a découvert l'Amérique?",
         meaning="centuries",
         intention="Situate a story in time — essential for any narrative.",
         image="Whole centuries skipping past in one sentence.",
         note="Masculine: un siècle. 'Le XXIe siècle' = the 21st century."),
    dict(plane="vocab", term="conseil",
         text="Tu veux un {{c1::conseil}} d'ami? Laisse tomber tout de suite.",
         meaning="a piece of advice",
         intention="Offer or ask for advice. Countable in French, unlike English.",
         image="The art teacher telling him to give up.",
         note="Masculine: un conseil. 'Donner un conseil', 'demander conseil'. "
              "Also means a council: le conseil municipal."),
    dict(plane="vocab", term="voisine",
         text="Bonjour, je suis votre {{c1::voisin}} d'en face.",
         meaning="neighbour",
         intention="Core social word; the second half of this tale is built on it.",
         image="The man from the flat opposite, holding flowers.",
         note="Masculine voisin / feminine voisine. 'D'en face' = across the way."),
    dict(plane="vocab", term="fleurs",
         text="Tenez, voici des {{c1::fleurs}} pour vous.",
         meaning="flowers",
         intention="Core everyday noun — and the standard way to court someone.",
         image="A bunch handed over at the door.",
         note="Feminine: une fleur."),
    dict(plane="vocab", term="minet",
         text="{{c1::Minet}}, minet, où es-tu mon petit minet?",
         meaning="kitty / puss (calling a cat)",
         intention="How French speakers actually call a cat — you will never guess it.",
         image="A woman leaning out of the window calling the cat.",
         note="Also minou. The ordinary word is 'le chat'; minet/minou are the "
              "pet names, like English 'kitty'."),
    dict(plane="vocab", term="église",
         text="Au moment où les nouveaux mariés sortaient de l'{{c1::église}}.",
         meaning="church",
         intention="Core place word; also where weddings happen in these tales.",
         image="A couple stepping out of the church door.",
         note="Feminine: une église. Note the accent: é-glise."),

    # ============ NARRATIVE AND SPOKEN CONNECTORS ============
    dict(plane="expression", term="tout de même",
         text="On est des barbares, mais pas des brutes {{c1::tout de même}}!",
         meaning="all the same / still / really",
         intention="Push back: 'come on, there are limits'.",
         note="Often shortened in speech to 'quand même'. Adds indignation."),
    dict(plane="expression", term="quand même",
         text="C'est pas Lustucru {{c1::quand même}}!",
         meaning="surely not! / anyway / still",
         intention="Express disbelief, or concede a point grudgingly.",
         note="One of the most-used phrases in spoken French, with several jobs. "
              "Here it is disbelief; elsewhere it means 'nevertheless'."),
    dict(plane="expression", term="au fait",
         text="Mais {{c1::au fait}}, comment t'appelles-tu, mon petit?",
         meaning="by the way",
         intention="Change the subject to something that just occurred to you.",
         note="Do NOT confuse with 'en fait' (= actually, in fact). "
              "au fait = by the way · en fait = actually."),
    dict(plane="expression", term="d'ailleurs",
         text="{{c1::D'ailleurs}}, voici notre nouvel empereur.",
         meaning="besides / moreover / incidentally",
         intention="Add a further point that strengthens what you just said.",
         note="Written and spoken alike. Literally 'from elsewhere'."),
    dict(plane="expression", term="laisse tomber",
         text="Tu veux un conseil d'ami? {{c1::Laisse tomber}} tout de suite.",
         meaning="forget it / drop it / give up",
         intention="Tell someone to abandon an idea.",
         note="Literally 'let it fall'. Very common; polite form: laissez tomber."),
    dict(plane="expression", term="à peine",
         text="Mais je vous connais {{c1::à peine}}!",
         meaning="barely / hardly",
         intention="Say something is only just true, or only just happened.",
         note="Also starts sentences: 'à peine arrivé, il repartit' = no sooner had "
              "he arrived than he left again."),
    dict(plane="expression", term="une fois de plus",
         text="Et c'est ainsi qu'{{c1::une fois de plus}} le nom de Lustucru fut rayé de l'histoire.",
         meaning="once again / yet again",
         intention="Mark a repetition, usually a weary one.",
         note="'C'est ainsi que' before it = 'and that is how'. Both are storytelling glue."),
    dict(plane="expression", term="promis juré",
         text="Si je vous épouse, vous me rendez mon chat? — {{c1::Promis juré}}, voisine.",
         meaning="cross my heart / I promise, I swear",
         intention="Give a solemn childish promise.",
         note="Two past participles stacked. Children say 'promis, juré, craché'."),
    dict(plane="expression", term="à la longue",
         text="On doit pouvoir s'y habituer {{c1::à la longue}}.",
         meaning="in the long run / eventually",
         intention="Say that time will make something bearable or apparent.",
         note="Fixed phrase; the noun is invisible. Compare 'à court terme'."),
    dict(plane="expression", term="minute",
         text="{{c1::Minute}}, voisine! Je vous ai dit qu'il était chez moi.",
         meaning="hold on! / just a second!",
         intention="Interrupt to stop someone assuming too fast.",
         note="Shortened from 'une minute!'. Also 'minute papillon!' for the same job."),
    dict(plane="expression", term="figurez-vous",
         text="Je suis une personne sérieuse, moi, {{c1::figurez-vous}}.",
         meaning="would you believe / let me tell you / just imagine",
         intention="Insist on something about yourself that the other person doubts.",
         note="From se figurer (to imagine). Informal 'tu': figure-toi."),

    # ============ GRAMMAR — the written narrative machinery ============
    dict(plane="grammar", term="il fit",
         text="Il voulait absolument laisser son nom dans l'histoire, {{c1::il fit}} d'autres tentatives.",
         meaning="he made / he did (passé simple)",
         intention="The tense of WRITTEN storytelling: tales, novels, history books.",
         pattern="il fit (faire) · il fut (être) · il eut (avoir) · il alla (aller) · ils firent",
         note="You need to RECOGNISE it, not produce it — nobody speaks this tense. "
              "In conversation the same events take the passé composé: 'il a fait'. "
              "This tale is full of them: s'installa, se replièrent, assiégèrent, fut rayé."),
    dict(plane="grammar", term="avait truqué",
         text="Mais le secrétaire {{c1::avait truqué}} le récit.",
         meaning="had faked (plus-que-parfait)",
         intention="Talk about what happened BEFORE the past moment you are describing.",
         pattern="avoir/être in the IMPERFECT + past participle (il avait fait, elle était partie)",
         note="Exactly like English 'had done'. The secretary faked the account "
              "BEFORE the emperor read it — two layers of past in one sentence."),
    dict(plane="grammar", term="aurait dû",
         text="Partout où il {{c1::aurait dû}} écrire Lustucru, il avait écrit Jules César.",
         meaning="should have / ought to have",
         intention="Say what should have happened but did not — regret or reproach.",
         pattern="aurais / aurait / auriez + DÛ / PU / VOULU + infinitive",
         note="The three most useful: aurait dû (should have), aurait pu (could have), "
              "aurait voulu (would have liked). The tale's other A1 deck uses "
              "'ce qu'auraient voulu leurs parents' the same way."),
    dict(plane="grammar", term="je viens de",
         text="On vous a raconté, {{c1::je viens de}} conquérir la Gaule!",
         meaning="I have just...",
         intention="Say something happened moments ago — the recent past.",
         pattern="venir de + INFINITIVE (je viens de manger, il vient d'arriver)",
         note="Present tense of venir, but it means the past. Mirror image: "
              "'aller + infinitive' = the near future. One verb each way."),
    dict(plane="grammar", term="à condition que",
         text="Il sera immortel, mais à une condition... {{c1::à condition que}} tu lui donnes le nom de Lustucru.",
         meaning="on condition that / provided that",
         intention="Attach a requirement to a promise.",
         pattern="à condition que + SUBJUNCTIVE  ·  à condition de + INFINITIVE",
         note="Same subjunctive trigger as 'pour que', 'avant que', 'bien que'. "
              "If both halves share a subject, use 'à condition de' + infinitive instead."),
    dict(plane="grammar", term="ce fut lui qui",
         text="{{c1::Ce fut lui qui}} en 778 sonna du cor à Roncevaux.",
         meaning="it was he who / he was the one who",
         intention="Spotlight one element of a sentence — French does this constantly.",
         pattern="c'est / ce fut + X + QUI (subject) or QUE (object)",
         note="French has no stress accent, so it rearranges the sentence instead of "
              "saying it louder. 'C'est moi qui l'ai fait' = I'M the one who did it."),
    dict(plane="grammar", term="a été découverte",
         text="De quoi aurions-nous l'air si on disait que l'Amérique {{c1::a été découverte}} par Lustucru?",
         meaning="was discovered (passive)",
         intention="Put the result first and the doer last — or hide the doer entirely.",
         pattern="être + PAST PARTICIPLE (+ par + doer). The participle agrees: découverte.",
         note="Agreement is the trap: l'Amérique is feminine, so découvertE. "
              "French often dodges the passive with 'on': 'on a découvert l'Amérique'."),

    # ============ VERBS & CONSTRUCTIONS ============
    dict(plane="verb-construction", term="s'appelait",
         text="À cette époque la France {{c1::s'appelait}} la Gaule.",
         meaning="was called / was named",
         intention="Give the name of a person, a place or a thing.",
         pattern="je m'appelle · tu t'appelles · il s'appelle · comment t'appelles-tu?",
         note="Reflexive: literally 'it calls itself'. The single most useful "
              "reflexive verb in the language."),
    dict(plane="verb-construction", term="manquaient de",
         text="Les Gaulois étaient très courageux mais {{c1::manquaient de}} discipline.",
         meaning="lacked / were short of",
         intention="Say something or someone is missing a quality or a resource.",
         pattern="manquer DE + noun (manquer de temps, manquer d'argent)",
         note="Careful, manquer has three lives: 'manquer de' = to lack; "
              "'manquer le train' = to miss it; 'tu me manques' = I miss YOU "
              "(the subject and object swap — a classic trap)."),
    dict(plane="verb-construction", term="obligèrent",
         text="Les Romains {{c1::obligèrent}} le chef des Gaulois à venir déposer ses armes.",
         meaning="forced / compelled",
         intention="Say someone was made to do something.",
         pattern="obliger quelqu'un À + infinitive  ·  être obligé DE + infinitive",
         note="The preposition flips between the active and the passive form: "
              "'il m'a obligé À partir' but 'je suis obligé DE partir'."),
    dict(plane="verb-construction", term="ça me sert",
         text="À quoi {{c1::ça me sert}} d'avoir un secrétaire particulier?",
         meaning="what's the use / what good does it do me",
         intention="Question whether something is worth anything at all.",
         pattern="servir À + purpose  ·  se servir DE = to use",
         note="'À quoi ça sert?' = what's it for? The other French deck uses the "
              "reflexive version: 'c'est le moment de t'en servir'."),
    dict(plane="verb-construction", term="j'ai envie de",
         text="Si tu n'es jamais là quand {{c1::j'ai envie de}} dicter mes mémoires!",
         meaning="I feel like / I want to",
         intention="Express a desire or an urge — softer and more natural than 'je veux'.",
         pattern="avoir envie DE + noun/infinitive",
         note="Another AVOIR expression, like avoir faim. 'Je n'ai pas envie' is the "
              "everyday way to refuse. The negative appears here: "
              "'je n'ai pas envie qu'on m'appelle madame Lustucru'."),
    dict(plane="verb-construction", term="demander en mariage",
         text="Je suis venu vous {{c1::demander en mariage}}, je vous aime.",
         meaning="to propose (marriage) to someone",
         intention="The fixed phrase for a proposal.",
         pattern="demander quelqu'un en mariage  ·  épouser quelqu'un = to marry them",
         note="Note: épouser takes NO preposition — 'je veux vous épouser'. "
              "'Se marier AVEC quelqu'un' does take one."),
    dict(plane="verb-construction", term="s'y habituer",
         text="Après tout, Lustucru ce n'est pas un vilain nom, on doit pouvoir {{c1::s'y habituer}} à la longue.",
         meaning="to get used to it",
         intention="Say you can adapt to something unpleasant over time.",
         pattern="s'habituer À quelque chose -> the À becomes Y: s'y habituer",
         note="This is why 'y' exists: it replaces any à + thing. "
              "'Je m'habitue au bruit' -> 'je m'y habitue'."),
    dict(plane="verb-construction", term="se mirent à",
         text="Les enfants du pays {{c1::se mirent à}} chanter une chanson.",
         meaning="began to / started",
         intention="Mark the moment an action starts, often suddenly.",
         pattern="se mettre À + infinitive (il se met à pleuvoir = it starts raining)",
         synonyms="commencer à",
         note="Here in the passé simple (se mirent). In speech: 'ils se sont mis à chanter'."),
]

if __name__ == "__main__":
    deck_builder.build(LANGUAGE, SLUG, DECK_ID, CARDS, LEVEL, DESCRIPTION)
