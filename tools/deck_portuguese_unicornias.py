# -*- coding: utf-8 -*-
"""Portuguese (Brazil) deck — "01x03 Unicórnias Princesas".

A1 for a Spanish speaker. Third deck of the language: nothing repeats from
loira-do-banheiro or globo-da-morte (checked with tools/cobertura.py). Deliberate
pairing across sibling decks — the diminutive lives in deck 1 and the augmentative
here; proclisis in deck 2 and enclisis here; the future subjunctive in deck 2 and
the imperfect subjunctive here.

Sentences are taken from the YouTube video transcript (heavy ASR typos fixed;
unrecoverable stretches were not harvested).

Run:  python tools/deck_portuguese_unicornias.py -> portuguese/unicornias-princesas.apkg
"""

import deck_builder

LANGUAGE = "portuguese"
SLUG = "unicornias-princesas"
DECK_ID = 1987452332   # stable: re-import updates instead of duplicating
LEVEL = "a1"

SOURCE_URL = "https://www.youtube.com/watch?v=xn23PZC3K9E"
DESCRIPTION = (
    "Portuguese (Brazil) &middot; A1. Third deck of the language, curated against the "
    "other two so no term repeats. Carries the counterparts of their grammar: the "
    "augmentative (-&atilde;o/-ona), enclisis, and the imperfect subjunctive. From "
    "<i>Historietas Assombradas 01x03 &mdash; Unic&oacute;rnias Princesas</i>. "
    "English carries the gloss."
    + (f"<br>Source video: <a href='{SOURCE_URL}'>{SOURCE_URL}</a>" if SOURCE_URL else "")
)

CARDS = [
    # ============ EVERYDAY VOCABULARY ============
    dict(plane="vocab", term="brincamos",
         text="Nós usamos rosa e {{c1::brincamos}} de casinha porque nós somos meninas.",
         meaning="we play",
         intention="Children playing — games, pretend, toys.",
         image="Two kids playing house on the floor.",
         note="THE most expensive false friend in Portuguese for a Spanish speaker: "
              "'brincar' is NOT to jump (saltar/pular) — it is to PLAY. "
              "brincar de casinha = to play house. Also brincadeira = a joke."),
    dict(plane="vocab", term="chata",
         text="É aquela menina {{c1::chata}}.",
         meaning="annoying / boring / a pain",
         intention="Describe a person or a situation that wears you down.",
         image="The classmate who will not stop talking.",
         note="FALSE FRIEND: not Spanish 'chata' (flat-nosed). Masculine: chato. "
              "One of the ten words you will hear most in Brazil. "
              "'Que chato!' = what a drag!"),
    dict(plane="vocab", term="corrida",
         text="É uma {{c1::corrida}} de formigas contra o arroz.",
         meaning="a race",
         intention="Any race; also a taxi or Uber ride.",
         image="Ants racing across a table.",
         note="FALSE FRIEND: Spanish 'corrida' is a bullfight. From correr (to run)."),
    dict(plane="vocab", term="formigas",
         text="É uma corrida de {{c1::formigas}} contra o arroz.",
         meaning="ants",
         intention="Core small-creature word.",
         image="A line of ants crossing the floor.",
         note="KEY PATTERN: Spanish h- is often Portuguese f-. formiga/hormiga, "
              "fazer/hacer, falar/hablar, filho/hijo, ferro/hierro, fome/hambre. "
              "One card, fifty words unlocked."),
    dict(plane="vocab", term="lixo",
         text="Nunca vi nada tão doce e adorável. Que {{c1::lixo}}!",
         meaning="rubbish / trash / garbage",
         intention="Literal rubbish, and the insult thrown at anything worthless.",
         image="A bin bag. Or a show you hate.",
         note="Nothing like Spanish 'basura'. Masculine: o lixo."),
    dict(plane="vocab", term="porcaria",
         text="Como alguém gosta dessa {{c1::porcaria}}?",
         meaning="rubbish / junk / crap",
         intention="Dismiss something as worthless — softer and funnier than lixo.",
         image="Pointing at the TV in disgust.",
         note="From porco (pig). Also means junk food: comer porcaria."),
    dict(plane="vocab", term="vizinha",
         text="Olá, marujos. Meu nome é Pepita, eu sou a nova {{c1::vizinha}}.",
         meaning="neighbour (female)",
         intention="Core social word — who lives next door.",
         image="Someone new knocking at the door.",
         note="Masculine: vizinho. The z is a real z sound, unlike Spanish 'vecina'."),
    dict(plane="vocab", term="mocinha",
         text="E você, {{c1::mocinha}}, vai para o poço da vergonha.",
         meaning="young lady",
         intention="Address a girl — affectionate, or stern the way a parent does.",
         image="A grandmother wagging a finger: 'young lady...'",
         note="moça (young woman) + -inha. moço/moça is also how you call a waiter."),
    dict(plane="vocab", term="peruca",
         text="Essa {{c1::peruca}} é do mal!",
         meaning="wig",
         intention="Hair that is not yours — costume, disguise, theatre.",
         image="A wig yanked off mid-fight.",
         note="Careful with Spanish 'peluca': the r and the l swap. Feminine: a peruca."),
    dict(plane="vocab", term="bilhete",
         text="O {{c1::bilhete}} sorteado é o número 42.",
         meaning="ticket / short note",
         intention="A raffle ticket, a bus ticket, or a scribbled note.",
         image="A numbered raffle stub.",
         note="Narrower than Spanish 'billete' — money is dinheiro, a banknote is "
              "a nota. Masculine: o bilhete."),
    dict(plane="vocab", term="olhos",
         text="Você pode fechar os {{c1::olhos}} rapidinho?",
         meaning="eyes",
         intention="Core body part.",
         image="Closing your eyes for a surprise.",
         note="Third -lh- word after espelho and joelho — the pattern is worth "
              "noticing: Spanish -j- often becomes Portuguese -lh-. olho = ojo."),
    dict(plane="vocab", term="fã",
         text="Todo mundo vai saber que você é a nossa {{c1::fã}} número um.",
         meaning="fan (of something)",
         intention="Say you follow a show, a band, a team.",
         image="A number-one fan kit being delivered to your door.",
         note="Tiny word, nasal vowel: the ã does not exist in Spanish. "
              "Same for men and women; plural fãs."),
    dict(plane="vocab", term="machões",
         text="Cai fora, Marilu. Menina não entra no clube dos {{c1::machões}}.",
         meaning="tough guys / macho men",
         intention="The self-appointed manly ones — said mockingly here.",
         image="A treehouse sign: no girls allowed.",
         note="macho + -ão, plural -ões. Female version: machona (a tomboy). "
              "The ASR transcript mangles this as 'maçons' (freemasons) — it is machões."),

    # ============ SPOKEN FORMULAS ============
    dict(plane="expression", term="cai fora",
         text="{{c1::Cai fora}}, Marilu.",
         meaning="get out / beat it",
         intention="Tell someone to leave — rude, between kids or in a fight.",
         note="From cair (to fall) + fora (outside). Also 'vaza!' in newer slang."),
    dict(plane="expression", term="imagina",
         text="Você tava vendo o programa dos unicórnios? — Unicórnios? Eu? {{c1::Imagina}}.",
         meaning="no way / of course not / don't be silly",
         intention="Deny something while pretending it is absurd. Also waves away a thank-you.",
         note="Two opposite jobs: here it is denial; after 'obrigado' it means "
              "'don't mention it'."),
    dict(plane="expression", term="que horror",
         text="Eu gosto muito de unicórnias princesas. — {{c1::Que horror}}!",
         meaning="how awful! / that's terrible!",
         intention="React with disgust or dismay.",
         note="Pattern: que + noun = what a...! (que pena, que legal, que chato)."),
    dict(plane="expression", term="massa",
         text="É muito {{c1::massa}}!",
         meaning="awesome / cool",
         intention="Praise something you think is great. Casual, among friends.",
         note="Literally 'dough/mass'. Slang — fine with friends, not in writing. "
              "Synonyms: legal, maneiro, daora."),
    dict(plane="expression", term="pronto",
         text="{{c1::Pronto}}, pode abrir.",
         meaning="there / done / ready",
         intention="Announce that something is finished and the other person can go ahead.",
         note="FALSE FRIEND: Spanish 'pronto' means soon. Portuguese 'pronto' = ready, "
              "done. For 'soon' say logo or em breve."),
    dict(plane="expression", term="sabe como é",
         text="{{c1::Sabe como é}}, nós usamos rosa e brincamos de casinha.",
         meaning="you know how it is",
         intention="Appeal to shared understanding instead of explaining.",
         note="Softens whatever you are about to say."),
    dict(plane="expression", term="quer dizer",
         text="Te amo, quer ser minha amiga? {{c1::Quer dizer}}, desculpa, completa desconhecida.",
         meaning="I mean / that is to say",
         intention="Correct yourself mid-sentence — the everyday repair tool.",
         note="Literally 'it wants to say'. Also asks for meaning: "
              "'o que quer dizer isso?'"),
    dict(plane="expression", term="de verdade",
         text="Uma fã {{c1::de verdade}} não faz maldade.",
         meaning="real / genuine / for real",
         intention="Mark something as the authentic version, not the fake one.",
         pattern="noun + de verdade (um amigo de verdade, comida de verdade)"),
    dict(plane="expression", term="te amo",
         text="{{c1::Te amo}}! Quer ser minha amiga?",
         meaning="I love you",
         intention="Strong affection — family, partners, and in Brazil also close friends.",
         note="Note the proclitic te, as in deck globo-da-morte. Lighter version: "
              "'te adoro'. 'Eu te amo' is the fuller form."),
    dict(plane="expression", term="acabou",
         text="{{c1::Acabou}}! Mudaram de ideia.",
         meaning="it's over / it's finished",
         intention="Announce the end of something, often abruptly.",
         note="From acabar. 'Acabou de chegar' means something different: "
              "acabar de + infinitive = to have just done something."),
    dict(plane="expression", term="é isso aí",
         text="{{c1::É isso aí}}, amiguinhos.",
         meaning="that's it / that's right / there you go",
         intention="Wrap something up, or agree enthusiastically.",
         note="The standard sign-off of any Brazilian kids' show."),

    # ============ GRAMMAR ============
    dict(plane="grammar", term="se eu fosse",
         text="{{c1::Se eu fosse}} uma menina, ninguém ia ligar de ser fã das unicórnias.",
         meaning="if I were",
         intention="Imagine something contrary to fact — the hypothetical.",
         pattern="se + IMPERFECT SUBJUNCTIVE, ... + IA/-ria  (se eu fosse, eu ia / eu iria)",
         note="The partner of 'se você tiver' in deck globo-da-morte. Future "
              "subjunctive = a real future condition; imperfect subjunctive = an "
              "impossible one. In speech the 'ia' form beats the -ria form."),
    dict(plane="grammar", term="machona",
         text="Você não é {{c1::machona}}, Marilu.",
         meaning="tomboy / butch (from macho + -ona)",
         intention="The augmentative: makes things big, and adds an opinion.",
         pattern="noun/adj + -ão (M) / -ona (F)   (machão, machona, coisão, portão)",
         note="The counterpart of the diminutive -inho/-inha in deck loira-do-banheiro. "
              "Same engine, opposite direction — and rarely neutral: it usually "
              "carries mockery or exaggeration."),
    dict(plane="grammar", term="nós somos",
         text="Nós usamos rosa e brincamos de casinha porque {{c1::nós somos}} meninas.",
         meaning="we are",
         intention="The formal/emphatic 'we', with its own verb ending.",
         pattern="nós + -mos  (nós somos, nós usamos, nós aprendemos, nós gostamos)",
         note="Contrast with 'a gente' in deck loira-do-banheiro: same meaning, "
              "different grammar. 'nós somos' is emphatic or written; 'a gente é' "
              "is what people say. This episode uses nós for the moral of the story."),
    dict(plane="grammar", term="Todo mundo",
         text="{{c1::Todo mundo}} vai rir de mim.",
         meaning="everybody",
         intention="Say 'everyone' — the normal way, far more common than 'todos'.",
         pattern="todo mundo + SINGULAR verb (todo mundo sabe, todo mundo foi)",
         note="No article, unlike Spanish 'todo el mundo'. And the verb stays "
              "singular even though the meaning is plural."),
    dict(plane="grammar", term="prepare-se",
         text="É o seu fim. {{c1::Prepare-se}} para sentir a minha fúria!",
         meaning="get ready / brace yourself",
         intention="Pronoun AFTER the verb, joined by a hyphen — the formal pattern.",
         pattern="VERB-se / VERB-me / VERB-te  (prepare-se, chama-se, sente-se)",
         note="The mirror image of proclisis in deck globo-da-morte. Enclisis is the "
              "written and formal norm (and the everyday norm in Portugal); spoken "
              "Brazil puts the pronoun first instead. Here it is villain-speak."),

    # ============ VERBS & CONSTRUCTIONS ============
    dict(plane="verb-construction", term="gosto de",
         text="Eu {{c1::gosto de}} unicórnias princesas.",
         meaning="I like",
         intention="Say what you like — the single most useful verb at A1.",
         pattern="SUBJECT + gostar DE + thing  (eu gosto de, você gosta de, nós gostamos de)",
         note="THE structural trap for a Spanish speaker. Spanish inverts the sentence "
              "('me gusta el chocolate' — the chocolate is the subject). Portuguese "
              "does not: YOU are the subject, and the DE is obligatory. "
              "Never 'eu gosto chocolate'."),
    dict(plane="verb-construction", term="foi embora",
         text="Você não {{c1::foi embora}}?",
         meaning="left / went away",
         intention="Say that someone left — the normal way to express it.",
         pattern="ir embora (vou embora, foi embora, vai embora)",
         note="No Spanish equivalent — 'irse' is the closest. 'Embora' alone is a "
              "formal 'although', but ir + embora = to leave."),
    dict(plane="verb-construction", term="deixar",
         text="Mas antes vocês têm que me {{c1::deixar}} entrar no clube dos machões.",
         meaning="to let / to allow",
         intention="Ask or give permission.",
         pattern="deixar + person + infinitive = let someone do something",
         note="THREE lives in this one episode: 'me deixa gordo' (makes me look), "
              "'você me deixou presa' (left me), 'me deixar entrar' (let me). "
              "Context decides."),
    dict(plane="verb-construction", term="assistindo",
         text="{{c1::Assistindo}} unicórnias princesas para sempre!",
         meaning="watching",
         intention="Watch TV, a film, a match — the everyday verb.",
         pattern="assistir A algo (formal) · assistir algo (spoken)",
         note="FALSE FRIEND: Spanish 'asistir' means to attend. In Portuguese it is "
              "to WATCH. Very high frequency: assistir TV, assistir um filme."),
    dict(plane="verb-construction", term="ter vergonha de",
         text="Hoje nós aprendemos que não devemos {{c1::ter vergonha de}} quem somos.",
         meaning="to be ashamed of",
         intention="Talk about shame or embarrassment — the moral of this episode.",
         pattern="ter vergonha DE + noun/infinitive · estar com vergonha = feel it right now",
         note="Pairs with 'estar com fome' in deck loira-do-banheiro: Portuguese uses "
              "TER and ESTAR COM where Spanish uses tener."),
    dict(plane="verb-construction", term="estragou",
         text="Eu tava disfarçado, mas você {{c1::estragou}} tudo!",
         meaning="ruined / spoiled",
         intention="Say something was wrecked — a plan, a surprise, food going off.",
         pattern="estragar (estraguei, estragou, estragamos)",
         synonyms="arruinar, acabar com",
         note="Nothing like Spanish 'estropear' or 'arruinar' in shape. "
              "Food that has gone bad: está estragado."),
    dict(plane="verb-construction", term="fazer parte do",
         text="Agora posso {{c1::fazer parte do}} clube dos machões?",
         meaning="to be part of / to join",
         intention="Say you belong to a group, a team, a club.",
         pattern="fazer parte DE + group (faço parte da equipe)"),
    dict(plane="verb-construction", term="rir de",
         text="Todo mundo vai {{c1::rir de}} mim.",
         meaning="to laugh at",
         intention="The fear that drives this whole episode.",
         pattern="rir DE alguém = laugh AT · rir COM alguém = laugh WITH",
         note="The preposition changes everything, exactly as in English. "
              "rir is irregular: rio, ri, rimos."),
]

if __name__ == "__main__":
    deck_builder.build(LANGUAGE, SLUG, DECK_ID, CARDS, LEVEL, DESCRIPTION)
