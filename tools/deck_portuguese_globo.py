# -*- coding: utf-8 -*-
"""Portuguese (Brazil) deck — "01x02 O Globo da Morte".

A1 for a Spanish speaker. Second deck of the language: every term already carded
in loira-do-banheiro was removed (checked with tools/cobertura.py), so the weight
shifts away from vocabulary and towards structure — proclisis, the future
subjunctive, the nasal plural, obrigado/obrigada.

Sentences are taken from the YouTube video transcript (heavy ASR typos fixed;
unrecoverable stretches were not harvested).

Run:  python tools/deck_portuguese_globo.py   ->  portuguese/globo-da-morte.apkg
"""

import deck_builder

LANGUAGE = "portuguese"
SLUG = "globo-da-morte"
DECK_ID = 1987452331   # stable: re-import updates instead of duplicating
LEVEL = "a1"

SOURCE_URL = "https://www.youtube.com/watch?v=fU59SHYyB5E"
DESCRIPTION = (
    "Portuguese (Brazil) &middot; A1. Second deck of the language: no term repeats "
    "from <i>loira-do-banheiro</i>, so the load moves to structure &mdash; proclitic "
    "pronouns, the future subjunctive, the nasal plural, obrigado/obrigada. From "
    "<i>Historietas Assombradas 01x02 &mdash; O Globo da Morte</i>. English carries the gloss."
    + (f"<br>Source video: <a href='{SOURCE_URL}'>{SOURCE_URL}</a>" if SOURCE_URL else "")
)

CARDS = [
    # ============ EVERYDAY VOCABULARY ============
    dict(plane="vocab", term="joelho",
         text="Ai, meu {{c1::joelho}}!",
         meaning="knee",
         intention="Core body part — the one you scrape falling off a bike.",
         image="A grazed knee after a fall.",
         note="Same -lh- trap as espelho. Masculine: o joelho."),
    dict(plane="vocab", term="capacete",
         text="Você esqueceu o {{c1::capacete}}.",
         meaning="helmet",
         intention="Safety gear for bikes and motorbikes.",
         image="A helmet left hanging on the handlebars.",
         note="Nothing like Spanish 'casco'. Masculine: o capacete."),
    dict(plane="vocab", term="faca",
         text="Enguias elétricas, escorpiões, {{c1::faca}} pequena.",
         meaning="knife",
         intention="Core kitchen and table object.",
         image="A small knife on the table.",
         note="Nothing like Spanish 'cuchillo'. Feminine: a faca."),
    dict(plane="vocab", term="copo",
         text="Me passa o {{c1::copo}}, por favor.",
         meaning="glass / cup (for drinking)",
         intention="What you ask for at any table.",
         image="A glass of water being passed across.",
         note="FALSE FRIEND: not Spanish 'copo' (flake). Masculine: o copo. "
              "A wine glass is a taça."),
    dict(plane="vocab", term="malas",
         text="Hora de fazer as {{c1::malas}}, velhota.",
         meaning="suitcases / bags",
         intention="What you pack when you are leaving — or dying.",
         image="Two suitcases by the door.",
         note="FALSE FRIEND: not Spanish 'malas' (bad). Feminine: a mala."),
    dict(plane="vocab", term="velhota",
         text="Hora de fazer as malas, {{c1::velhota}}.",
         meaning="old lady (cheeky)",
         intention="Tease an older woman — rude from a stranger, affectionate from family.",
         image="Death calling the grandmother 'old girl'.",
         note="velho + -ota. Not neutral: say senhora if you want to be polite."),
    dict(plane="vocab", term="caixote",
         text="Além disso, o Pepe está no {{c1::caixote}}.",
         meaning="crate / big box",
         intention="A wooden box big enough to hide a person in.",
         image="A wooden crate with someone crouching inside.",
         note="caixa (box) + -ote (augmentative). Masculine: o caixote."),
    dict(plane="vocab", term="ninho",
         text="Atenção: a águia pousou no {{c1::ninho}}.",
         meaning="nest",
         intention="Bird's nest; also the punchline of every spy-code joke.",
         image="An eagle landing on a nest.",
         note="-nh- = the Spanish ñ sound. ninho = nido. Masculine: o ninho."),
    dict(plane="vocab", term="medo",
         text="Fizemos isso para você perder o {{c1::medo}}.",
         meaning="fear",
         intention="Core emotion word; goes with estar com and ter.",
         image="Hiding in a box because you are afraid.",
         note="Spanish 'miedo' loses its diphthong here: medo. Masculine: o medo."),
    dict(plane="vocab", term="irmã",
         text="Normal, ela é minha {{c1::irmã}} mais nova.",
         meaning="sister",
         intention="Core family word.",
         image="A younger sister bossing you around.",
         note="Nothing like Spanish 'hermana'. Masculine: irmão. "
              "The ã is nasal — the sound does not exist in Spanish."),
    dict(plane="vocab", term="mão",
         text="Olha, vó, eu tô pedalando! Sem uma {{c1::mão}}! Tem as duas!",
         meaning="hand",
         intention="Core body part.",
         image="Letting go of the handlebars with one hand.",
         note="Feminine despite the -ão ending: a mão. Plural: as mãos."),
    dict(plane="vocab", term="desenhar",
         text="Presta atenção, para de {{c1::desenhar}}.",
         meaning="to draw",
         intention="Core activity verb — drawing, sketching.",
         image="Doodling instead of listening.",
         note="Nothing like Spanish 'dibujar'. The noun is o desenho — "
              "and desenho animado is a cartoon."),
    dict(plane="vocab", term="pirralho",
         text="O {{c1::pirralho}} competirá no globo da morte de bicicleta.",
         meaning="brat / little kid",
         intention="Dismissive word for a child — insulting or joking.",
         image="An adult pointing at a small annoying kid.",
         note="Feminine: pirralha. Not neutral; criança is the polite word."),
    dict(plane="vocab", term="neném",
         text="Não esquece o capacete, é pra sua segurança, {{c1::neném}}.",
         meaning="baby",
         intention="A baby; also a condescending nickname, as here.",
         image="Calling a grown boy 'baby' to wind him up.",
         note="Also written nenê. bebê works too."),
    dict(plane="vocab", term="gente",
         text="{{c1::Gente}}, eu também!",
         meaning="guys / everyone (addressing people)",
         intention="Call out to a group of friends — the standard way to get attention.",
         image="Turning to your friends: 'guys!'",
         note="MINIMAL PAIR: plain 'gente' = you guys. 'A gente' = we "
              "(see deck loira-do-banheiro). One little word changes everything."),

    # ============ SPOKEN FORMULAS ============
    dict(plane="expression", term="jura?",
         text="Ai, você tá vivo? {{c1::Jura}}? Jura?",
         meaning="really?! / you're kidding!",
         intention="React to news you can hardly believe.",
         note="Literally 'do you swear?'. Stronger and more surprised than sério?"),
    dict(plane="expression", term="opa",
         text="{{c1::Opa}}, mais pesado do que parecia.",
         meaning="oops / whoa / hey",
         intention="Catch yourself in a small surprise — a stumble, a wrong step.",
         note="Also a casual greeting on its own: Opa! = hey!"),
    dict(plane="expression", term="nossa",
         text="{{c1::Nossa}}, você deixa ela falar assim com você?",
         meaning="wow! / oh my!",
         intention="The default Brazilian reaction to anything surprising.",
         note="Shortened from 'Nossa Senhora'. You cannot guess it from Spanish — "
              "and you will hear it every few minutes."),
    dict(plane="expression", term="pera aí",
         text="{{c1::Pera aí}}, não esquece o capacete.",
         meaning="hold on / wait a second",
         intention="Stop someone mid-action.",
         note="Squashed from 'espera aí'. Also 'peraí' written as one word."),
    dict(plane="expression", term="que isso",
         text="{{c1::Que isso}}, vó, você tá ótima.",
         meaning="come on! / no way! / don't be silly",
         intention="Brush off what someone just said — modesty, disbelief or protest.",
         note="From 'o que é isso'. Tone decides whether it is comforting or shocked."),
    dict(plane="expression", term="vai lá",
         text="{{c1::Vai lá}}, Pepe, você consegue.",
         meaning="go on / go for it",
         intention="Push someone to take the step they are scared of.",
         note="Literally 'go there'. Encouraging, not dismissive."),
    dict(plane="expression", term="é o seguinte",
         text="{{c1::É o seguinte}}, Pepe: quando a gente soltar o Ramirez, ele vai atacar.",
         meaning="here's the thing / here's the plan",
         intention="Announce that an explanation is coming. Buys you a second.",
         note="Extremely common opener in spoken Brazilian."),
    dict(plane="expression", term="como assim",
         text="Ele vai competir no meu lugar. — {{c1::Como assim}}?",
         meaning="what do you mean? / how so?",
         intention="Demand an explanation for something that made no sense.",
         note="Said alone, as a whole question."),
    dict(plane="expression", term="hora de",
         text="{{c1::Hora de}} fazer as malas, velhota.",
         meaning="time to...",
         intention="Announce that the moment for something has arrived.",
         pattern="hora de + infinitive (hora de ir, hora de acordar)"),
    dict(plane="expression", term="de última hora",
         text="Apoio moral {{c1::de última hora}}.",
         meaning="last-minute",
         intention="Describe something thrown together at the very end.",
         note="Note it is 'de última hora', not 'de último minuto'."),
    dict(plane="expression", term="carta na manga",
         text="Eu ainda tenho uma {{c1::manga na carta}}.",
         meaning="an ace up my sleeve",
         intention="Say you still have a hidden advantage left.",
         note="CAREFUL — this line is scrambled ON PURPOSE. The real idiom is "
              "'uma CARTA NA MANGA' (a card in the sleeve). Death is dyslexic and "
              "swaps words all episode ('minha alma será sua' for the opposite). "
              "Learn the correct order; recognise the joke."),
    dict(plane="expression", term="dar uma licencinha",
         text="Vocês podem me {{c1::dar uma licencinha}}?",
         meaning="excuse me / let me through",
         intention="Ask people to move aside, politely and lightly.",
         note="licença + -inha softens it. Plain 'com licença' is the standard form."),

    # ============ GRAMMAR ============
    dict(plane="grammar", term="se você tiver",
         text="Te espero hoje à noite, {{c1::se você tiver}} coragem.",
         meaning="if you have (at some future point)",
         intention="Talk about a future condition — 'if/when X happens'.",
         pattern="se / quando / enquanto + FUTURE SUBJUNCTIVE (se tiver, quando puder, se quiser)",
         note="THE big divergence from Spanish: Spanish lost this tense, Portuguese "
              "uses it daily. Spanish says 'si tienes'; Portuguese cannot use the "
              "present here. Above A1 on paper, but fossilises badly if learnt late."),
    dict(plane="grammar", term="Me passa",
         text="{{c1::Me passa}} o copo, por favor.",
         meaning="pass me",
         intention="The pronoun goes BEFORE the verb — including in commands.",
         pattern="me / te / se + VERB  (me passa, me responde, te achar, te dou)",
         note="STRUCTURAL TRAP: Spanish attaches it to the end ('pásame'). Brazilian "
              "Portuguese puts it in front. All over this episode: me responde, "
              "me buscar, te achar, me machucar, me encontrar."),
    dict(plane="grammar", term="mãos",
         text="Não, eu não vou voltar de {{c1::mãos}} abanando.",
         meaning="hands (plural)",
         intention="The nasal plural — the ending changes shape, not just adds -s.",
         pattern="-ão -> -ãos (mão/mãos) · -ões (coração/corações) · -ães (pão/pães)",
         note="Three different plurals for one ending; there is no rule, they are "
              "learnt word by word. -ões is the most common."),
    dict(plane="grammar", term="Presta atenção",
         text="{{c1::Presta atenção}}, para de desenhar.",
         meaning="pay attention",
         intention="Give an order the way Brazilians actually do.",
         pattern="use the HE/SHE form as the command (presta, para, olha, vai, come)",
         note="Textbook imperative would be 'preste', 'pare'. Spoken Brazilian uses "
              "the você form instead. Same with para de = stop it."),
    dict(plane="grammar", term="melhor que",
         text="Ainda não percebeu que eu sou {{c1::melhor que}} você?",
         meaning="better than",
         intention="Compare two things.",
         pattern="mais/menos ... (do) que · melhor (do) que · pior (do) que",
         note="The 'do' is optional: melhor que você = melhor do que você. Both are "
              "correct and both are said."),
    dict(plane="grammar", term="obrigado",
         text="Me passa o copo, por favor. {{c1::Obrigado}}, escrava.",
         meaning="thank you (said by a male speaker)",
         intention="Thank someone — and agree with YOURSELF while doing it.",
         pattern="man says obrigado · woman says obrigada",
         note="TRAP FOR SPANISH SPEAKERS: 'gracias' never changes, but obrigado "
              "agrees with the person SPEAKING, not the person thanked. Death "
              "(female) says 'muito obrigada' later in this same episode."),

    # ============ VERBS & CONSTRUCTIONS ============
    dict(plane="verb-construction", term="andar de",
         text="Eu não quero aprender a {{c1::andar de}} bicicleta.",
         meaning="to ride / to go by (a vehicle)",
         intention="Say how you travel: by bike, by car, by bus.",
         pattern="andar de + vehicle (de bicicleta, de carro, de ônibus, de avião)",
         note="No article: andar de bicicleta, never 'andar da bicicleta'. "
              "On foot breaks the pattern: a pé."),
    dict(plane="verb-construction", term="aprender a",
         text="Eu não quero {{c1::aprender a}} andar de bicicleta.",
         meaning="to learn to",
         intention="Say what skill you are acquiring.",
         pattern="aprender A + infinitive (aprender a ler, aprender a dirigir)",
         note="The preposition 'a' is obligatory."),
    dict(plane="verb-construction", term="é só",
         text="Valendo! {{c1::É só}} pedalar.",
         meaning="you just have to / all you need to do is",
         intention="Reassure someone that the task is simpler than they think.",
         pattern="é só + infinitive (é só pedalar, é só pedir, é só esperar)",
         note="Said three times in this episode. Very high frequency, very easy to reuse."),
    dict(plane="verb-construction", term="acha",
         text="Você {{c1::acha}} que o Pepe está morto?",
         meaning="do you think",
         intention="Ask someone's opinion — the everyday verb for it.",
         pattern="achar que + opinion · achar + object = to find something",
         synonyms="pensar, crer (both rarer in speech)",
         note="DOUBLE LIFE: achar = to think AND to find. Both appear here: "
              "'você acha que...' (think) and 'ninguém vai te achar' (find). "
              "Spanish 'hallar' is rare; in Portuguese this is a top-10 verb."),
    dict(plane="verb-construction", term="consegue",
         text="Vai lá, Pepe, você {{c1::consegue}}.",
         meaning="you can do it / you'll manage",
         intention="Say someone is capable of pulling something off.",
         pattern="conseguir + infinitive (consegui abrir, não consigo dormir)",
         note="Narrower than poder: conseguir is about MANAGING, not being allowed. "
              "'Eu tô conseguindo!' = I'm doing it!"),
    dict(plane="verb-construction", term="demorou",
         text="Uma vez eu me escondi aí e o Gaston {{c1::demorou}} seis horas para me encontrar.",
         meaning="took a long time / took (a period of time)",
         intention="Say how long something took, or complain that it dragged.",
         pattern="demorar + time + para + infinitive",
         note="Nothing like Spanish 'tardar', which is what you will reach for. "
              "'Demorou!' alone = finally!"),
    dict(plane="verb-construction", term="machucar",
         text="Qual é o problema? Eu sou o Ramires, ele não vai me {{c1::machucar}}.",
         meaning="to hurt / to injure",
         intention="Physical harm — to someone else or to yourself.",
         pattern="machucar (alguém) · machucar-se / se machucar = get hurt",
         synonyms="ferir (formal), doer (to ache)",
         note="Nothing like Spanish 'lastimar' or 'herir'."),
    dict(plane="verb-construction", term="perder o medo",
         text="Fizemos isso para você {{c1::perder o medo}}.",
         meaning="to get over your fear",
         intention="Talk about overcoming fear — of heights, of speaking, of anything.",
         pattern="perder o medo DE + noun/infinitive",
         note="perder also = to lose and to miss (perder o ônibus)."),
]

if __name__ == "__main__":
    deck_builder.build(LANGUAGE, SLUG, DECK_ID, CARDS, LEVEL, DESCRIPTION)
