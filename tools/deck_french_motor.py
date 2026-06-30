# -*- coding: utf-8 -*-
"""French deck — THE MOTOR (core engine of French).

NOT an immersion/reading deck (that's the sorcière tale). This is the FOUNDATION:
the structural skeleton + high-frequency motor that carries most of spoken/written
French — gender & articles, the pillar verbs and their conjugation, the everyday
tenses, two-part negation, pre-verbal object pronouns, questions, prepositions,
the impersonal frames (c'est / il y a / il faut) and basic connectors.

Deliberate exception to the repo's "never invent" rule: a foundation deck has no
source video, so the sentences are invented on purpose — short, funny and vivid
(vivid, absurd sentences are more memorable). Active recall via cloze; system
thinking via Intention (the job) + Pattern (the reusable frame) + note (the
contrast / the gender trap). English is the bridge language: each French item
carries an English gloss (meaning).

Study one plane at a time (tags), not the whole deck at once.

Run:  python tools/deck_french_motor.py   ->  french/motor/motor.apkg
"""

import deck_builder

LANGUAGE = "french"
SLUG = "motor"         # Anki deck name -> french::motor
DECK_ID = 1987452321   # stable: re-import updates instead of duplicating
LEVEL = "core"
SUBFOLDER = "motor"    # the .apkg lives in french/motor/

SOURCE_URL = ""  # curated foundation deck, no source video (legitimately empty)
DESCRIPTION = (
    "French · CORE MOTOR. The structural engine of French (A1 &rarr; B1 span): "
    "gender &amp; articles, the pillar verbs and conjugation, the everyday tenses "
    "(pass&eacute; compos&eacute;, imparfait, futur proche), two-part negation, "
    "pre-verbal object pronouns, questions, prepositions, the impersonal frames "
    "and basic connectors. Active recall (cloze) + system thinking (every back "
    "gives the job, the reusable pattern and the contrast). English is the bridge "
    "(each item has a gloss). Sentences invented on purpose — short and memorable. "
    "Study one plane (tag) at a time."
)

# Each card:
#   term      : the target item (also the cloze answer) — for readability only
#   text      : a short, funny sentence with {{c1::term}} clozed
#   meaning   : English gloss of the item (bridge language)
#   intention : the JOB the item does (system thinking)
#   image     : a vivid/absurd mental picture (concrete words) OR omit
#   pattern   : the reusable, generative frame OR omit
#   note      : the gender trap / the contrast with a neighbour OR omit
#   plane     : "grammar" | "verb-construction" | "connector" | "expression"

CARDS = [
    # ============ A. GENDER & ARTICLES (every noun is M or F) ============
    dict(plane="grammar", term="La",
         text="{{c1::La}} lune surveille tout le quartier.",
         meaning="the (feminine 'the')",
         intention="Every French noun has a gender; 'la' marks a feminine noun, 'le' a masculine one.",
         pattern="le + M noun · la + F noun · les + plural",
         note="Gender is rarely logical — always learn it WITH the noun."),
    dict(plane="grammar", term="une",
         text="J'ai adopté {{c1::une}} licorne au supermarché.",
         meaning="a / an (feminine)",
         intention="Indefinite article: one, new to the listener. un (M) / une (F).",
         pattern="un + M · une + F · des + plural"),
    dict(plane="grammar", term="des",
         text="Il y a {{c1::des}} pingouins dans l'ascenseur.",
         meaning="some / (plural of un/une)",
         intention="'des' = the plural indefinite — several, unspecified.",
         note="des = indefinite plural (some) · les = definite plural (the)."),
    dict(plane="grammar", term="du",
         text="Je veux {{c1::du}} pain, pas tout le pain du monde.",
         meaning="some (masculine partitive)",
         intention="Partitive: 'some / an amount of' an uncountable. French REQUIRES it where English drops 'some'.",
         pattern="du + M mass · de la + F mass · des + plural",
         note="'I want bread' -> 'je veux du pain' (never 'je veux pain')."),
    dict(plane="grammar", term="au",
         text="Je vais {{c1::au}} marché acheter du courage.",
         meaning="to the / at the (à + le)",
         intention="Mandatory contractions: à+le=au, à+les=aux, de+le=du, de+les=des.",
         pattern="à+le = au · de+le = du",
         note="Never write 'à le' or 'de le'."),

    # ============ B. SUBJECT PRONOUNS (incl. on, tu/vous) ============
    dict(plane="grammar", term="On",
         text="{{c1::On}} mange à huit heures, comme des gens civilisés.",
         meaning="we / people / one",
         intention="'on' = informal 'we' (also generic 'one'); it takes the il/elle verb form.",
         pattern="on + 3rd-person-singular verb (on mange, on va)",
         note="In speech 'on' replaces 'nous' almost always."),
    dict(plane="grammar", term="Vous",
         text="{{c1::Vous}} pouvez arrêter de juger mon café ?",
         meaning="you (formal, or plural)",
         intention="tu = informal singular; vous = formal OR plural. Picking wrong is a social mistake.",
         pattern="tu (close / one) · vous (polite, or many)"),
    dict(plane="grammar", term="Elle",
         text="Où est la clé ? {{c1::Elle}} est dans le frigo, évidemment.",
         meaning="it / she",
         intention="The pronoun agrees with the noun's GENDER — 'la clé' is feminine, so 'elle', even for an object.",
         note="Objects are he/she in French: la table -> elle, le livre -> il."),

    # ============ C. THE 4 PILLAR VERBS (être / avoir / aller / faire) ============
    dict(plane="verb-construction", term="suis",
         text="Je {{c1::suis}} fatiguée mais élégante.",
         meaning="I am (être)",
         intention="être = to be — the most used, most irregular verb.",
         pattern="je suis · tu es · il est · nous sommes · vous êtes · ils sont"),
    dict(plane="verb-construction", term="ai",
         text="J'{{c1::ai}} faim et zéro patience.",
         meaning="I have (avoir)",
         intention="avoir = to have. It also builds the past tense (passé composé).",
         pattern="j'ai · tu as · il a · nous avons · vous avez · ils ont",
         note="French uses avoir for age & hunger: j'ai faim, j'ai 20 ans."),
    dict(plane="verb-construction", term="vais",
         text="Je {{c1::vais}} regretter cette troisième crêpe.",
         meaning="I go / I'm going (aller)",
         intention="aller = to go. It also makes the near future (aller + infinitive).",
         pattern="je vais · tu vas · il va · nous allons · vous allez · ils vont"),
    dict(plane="verb-construction", term="fais",
         text="Qu'est-ce que tu {{c1::fais}} avec ce poulet ?",
         meaning="do / make (faire)",
         intention="faire = do/make — used for weather and dozens of idioms.",
         pattern="il fait froid · faire du sport · faire la cuisine",
         note="je fais · tu fais · il fait · nous faisons · vous faites · ils font"),

    # ============ D. PRESENT TENSE (the regular endings) ============
    dict(plane="grammar", term="parlons",
         text="Nous {{c1::parlons}} aux plantes, et elles répondent.",
         meaning="we speak (parler)",
         intention="Regular -ER verbs (the biggest group). Most endings SOUND the same; only the spelling changes.",
         pattern="je parle · tu parles · il parle · nous parlons · vous parlez · ils parlent"),
    dict(plane="grammar", term="finis",
         text="Je {{c1::finis}} toujours par manger le dernier biscuit.",
         meaning="I finish (finir)",
         intention="Regular -IR verbs: the -iss- block shows up in the plural.",
         pattern="je finis · il finit · nous finissons · ils finissent"),

    # ============ E. THE PAST (passé composé + être-verbs + imparfait) ============
    dict(plane="grammar", term="mangé",
         text="J'ai {{c1::mangé}} toute la tarte. Aucun regret.",
         meaning="ate / have eaten",
         intention="Passé composé = avoir/être (present) + past participle = the everyday past. -ER verbs -> -é.",
         pattern="avoir + participe passé (j'ai mangé, tu as fini)"),
    dict(plane="grammar", term="partie",
         text="Elle est {{c1::partie}} sans dire au revoir.",
         meaning="left / has left (feminine)",
         intention="A small set of motion/change verbs use ÊTRE, and the participle AGREES with the subject.",
         pattern="être + participe passé (s'accorde): il est parti / elle est partie / ils sont partis",
         note="The 'house of être' verbs (aller, venir, partir...) + all reflexives."),
    dict(plane="grammar", term="étais",
         text="Quand j'{{c1::étais}} petite, je parlais aux escargots.",
         meaning="I was / used to be (imparfait)",
         intention="Imparfait = the background, habit or description in the past ('was -ing', 'used to').",
         pattern="endings -ais/-ais/-ait/-ions/-iez/-aient",
         note="Contrast: imparfait = the scenery; passé composé = the event that happens."),

    # ============ F. FUTURE & CONDITIONAL ============
    dict(plane="grammar", term="vais commencer",
         text="Je {{c1::vais commencer}} demain. Probablement.",
         meaning="I'm going to start",
         intention="Near future = aller (present) + infinitive — the everyday future in speech.",
         pattern="aller + infinitive (je vais partir, on va voir)"),
    dict(plane="grammar", term="voudrais",
         text="Je {{c1::voudrais}} un café et une nouvelle personnalité.",
         meaning="I would like",
         intention="Conditional 'voudrais / aimerais' softens a request — far more polite than 'je veux'.",
         pattern="je voudrais + noun / + infinitive",
         note="'je veux' (I want) sounds blunt; 'je voudrais' is the polite default."),

    # ============ G. NEGATION (the two-part wrap) ============
    dict(plane="grammar", term="ne",
         text="Je {{c1::ne}} comprends pas, et bizarrement j'aime ça.",
         meaning="not (first half)",
         intention="French negation WRAPS the verb: ne + verb + pas. Two pieces, one on each side.",
         pattern="ne + verb + pas (je ne sais pas)",
         note="In speech the 'ne' is often dropped: 'je sais pas'."),
    dict(plane="grammar", term="jamais",
         text="Je ne mange {{c1::jamais}} de coriandre. C'est un principe.",
         meaning="never",
         intention="Swap 'pas' for jamais (never) / plus (no more) / rien (nothing) / personne (nobody).",
         pattern="ne + verb + jamais / plus / rien / personne"),

    # ============ H. OBJECT PRONOUNS + y / en (they go BEFORE the verb) ============
    dict(plane="grammar", term="la",
         text="Tu vois la lune ? Je {{c1::la}} vois aussi.",
         meaning="it / her (before the verb)",
         intention="Direct-object pronouns (le/la/les) go BEFORE the verb — opposite to English word order.",
         pattern="subject + [le/la/les] + verb (je la vois)",
         note="English: 'I see it' (after). French: 'je la vois' (before)."),
    dict(plane="grammar", term="y",
         text="Tu vas à Paris ? J'{{c1::y}} vais aussi !",
         meaning="there (replaces à + place)",
         intention="'y' replaces 'à + a place/thing'. Pre-verbal, tiny, everywhere.",
         pattern="y = à + lieu (j'y vais = I'm going there)"),
    dict(plane="grammar", term="en",
         text="Du gâteau ? Oui, j'{{c1::en}} veux trois parts.",
         meaning="some / of it (replaces de + thing)",
         intention="'en' replaces 'de + noun' (some of it, of them).",
         pattern="en = de + noun (j'en veux = I want some)"),

    # ============ I. QUESTIONS (est-ce que / inversion) ============
    dict(plane="grammar", term="Est-ce que",
         text="{{c1::Est-ce que}} tu as vraiment lu le contrat ?",
         meaning="(yes/no question marker)",
         intention="The easy universal question opener: put it in front of any statement — no inversion needed.",
         pattern="Est-ce que + statement ?",
         note="3 ways to ask: intonation (Tu viens?), est-ce que, inversion (Viens-tu?)."),
    dict(plane="grammar", term="Qu'est-ce que",
         text="{{c1::Qu'est-ce que}} tu fais ce week-end ?",
         meaning="what (do)...",
         intention="'qu'est-ce que' = what + (statement). The default spoken 'what'.",
         pattern="Qu'est-ce que + subject + verb ?"),
    dict(plane="grammar", term="Pourquoi",
         text="{{c1::Pourquoi}} le chat me regarde comme ça ?",
         meaning="why",
         intention="The info-question words: où (where), quand (when), pourquoi (why), comment (how), combien (how much), qui (who).",
         pattern="[question word] + est-ce que + statement ?"),

    # ============ J. PREPOSITIONS (à / de pillars + chez / en) ============
    dict(plane="grammar", term="à",
         text="On se voit {{c1::à}} la gare à midi ?",
         meaning="to / at / in (a point)",
         intention="'à' = to/at a point — place or time. Contracts: à+le=au, à+les=aux.",
         pattern="à + place / time (à Paris, à midi, à 8h)"),
    dict(plane="grammar", term="de",
         text="C'est le chien {{c1::de}} ma voisine bizarre.",
         meaning="of / from",
         intention="'de' = of/from — possession and origin. Contracts: de+le=du, de+les=des.",
         pattern="X de Y (le livre de Marie)",
         note="Possession = 'de' (no English 's: 'Marie's book' = le livre de Marie)."),
    dict(plane="grammar", term="chez",
         text="On va {{c1::chez}} moi ou chez le dragon ?",
         meaning="at / to someone's place",
         intention="'chez' = at/to a person's home or a business. No one-word English equivalent.",
         pattern="chez + person (chez moi, chez le médecin)"),
    dict(plane="grammar", term="en",
         text="Je voyage {{c1::en}} train, jamais en retard (mensonge).",
         meaning="by / in",
         intention="'en' = by (transport), in (months, feminine countries): en mai, en France, en bus.",
         pattern="en + month / feminine country / transport"),

    # ============ K. IMPERSONAL FRAMES (c'est / il y a / il faut) ============
    dict(plane="expression", term="C'est",
         text="{{c1::C'est}} compliqué, mais pas impossible.",
         meaning="it is / this is",
         intention="'c'est' = the all-purpose identifier: c'est + noun or adjective.",
         pattern="c'est + noun/adj · ce sont + plural",
         note="c'est (identify a thing) vs il est (he/it is + profession/adjective)."),
    dict(plane="expression", term="Il y a",
         text="{{c1::Il y a}} un problème avec ton plan génial.",
         meaning="there is / there are",
         intention="'il y a' = there is/are (existence) — invariable, singular OR plural.",
         pattern="il y a + singular OR plural (il y a un chat / des chats)",
         note="Also means 'ago': il y a deux ans = two years ago."),
    dict(plane="expression", term="Il faut",
         text="{{c1::Il faut}} dormir, pas acheter un kayak à 3h du matin.",
         meaning="one must / it's necessary to",
         intention="'il faut' + infinitive = must / need to (impersonal obligation).",
         pattern="il faut + infinitive (il faut partir)",
         note="il faut que + subjunctive comes later — start with the infinitive."),

    # ============ L. CONNECTORS ============
    dict(plane="connector", term="mais",
         text="Je suis venue pour le fromage, {{c1::mais}} je reste pour le vin.",
         meaning="but",
         intention="The basic glue: et (and), mais (but), ou (or).",
         pattern="X mais Y (contrast)"),
    dict(plane="connector", term="parce que",
         text="Je chuchote {{c1::parce que}} le bébé dort enfin.",
         meaning="because",
         intention="'parce que' = because (+ clause); answers 'pourquoi'.",
         pattern="Y parce que X",
         note="parce que (spoken, answers why) vs car (more formal/written)."),
    dict(plane="connector", term="donc",
         text="Le sol était mouillé, {{c1::donc}} j'ai dansé sans le vouloir.",
         meaning="so / therefore",
         intention="'donc' = so/therefore — the result of the previous clause.",
         pattern="X, donc Y (result)"),
    dict(plane="connector", term="Si",
         text="{{c1::Si}} tu nourris le chat, il habite ici maintenant.",
         meaning="if",
         intention="si = if (condition); quand = when (time). si + present, ... future.",
         pattern="Si + présent, ... futur (si tu viens, on mangera)"),

    # ============ M. ADJECTIVES (position + agreement) ============
    dict(plane="grammar", term="géniale",
         text="Une idée {{c1::géniale}} et complètement absurde.",
         meaning="brilliant (feminine)",
         intention="Most adjectives go AFTER the noun and AGREE: +e (feminine), +s (plural).",
         pattern="noun + adjective(+e/+s): une voiture rouge, des voitures rouges",
         note="Opposite of English: 'a red car' -> 'une voiture rouge'."),
    dict(plane="grammar", term="beau",
         text="Un {{c1::beau}} désastre, vraiment.",
         meaning="beautiful (before the noun)",
         intention="A few short common adjectives go BEFORE the noun (Beauty, Age, Goodness, Size).",
         pattern="[BAGS adj] + noun: un grand problème, une jeune femme, un bon café",
         note="beau, joli, jeune, vieux, bon, mauvais, grand, petit, nouveau."),

    # ============ N. REFLEXIVE VERBS (the action returns to you) ============
    dict(plane="verb-construction", term="me",
         text="Je {{c1::me}} réveille déjà fatiguée.",
         meaning="myself (reflexive pronoun)",
         intention="Reflexive verbs carry a pronoun: the action returns to the subject. Far more common than in English.",
         pattern="je me · tu te · il se · nous nous · vous vous · ils se + verb",
         note="se lever, se laver, s'appeler: 'je m'appelle' = I'm called."),
]

if __name__ == "__main__":
    import shutil

    path = deck_builder.build(LANGUAGE, SLUG, DECK_ID, CARDS, LEVEL, DESCRIPTION)
    # Relocate the .apkg into the french/motor/ subfolder.
    sub = path.parent / SUBFOLDER
    sub.mkdir(exist_ok=True)
    dest = sub / f"{SLUG}.apkg"
    shutil.move(str(path), str(dest))
    print(f"Moved -> {dest.relative_to(path.parent.parent)}")
