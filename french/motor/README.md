# french · motor

The **structural engine** of French: the high-frequency core that carries most of
everyday French. This is the foundation deck — the layer to make automatic before
the reading decks (e.g. the sorcière tale).

- **File:** `motor.apkg` → imports as the Anki deck `french::motor`
- **Source script:** `../../tools/deck_french_motor.py`
- **Cards:** 41 · French target, English gloss (bridge language) · Cloze
- **Stable `DECK_ID`** → re-importing updates the cards, never duplicates.

## Card design

Cloze note. Front = a short, vivid sentence with the key French piece hidden in
`{{c1::…}}` (active recall). Back, in English (the bridge):

- **Meaning** — the English gloss of the French item.
- **Intention** — the job the item does.
- **Pattern** — the reusable, generative frame (one card → many sentences).
- **Image** — a concrete mental picture (concrete words only).
- **note** — the gender trap or the contrast with a confusable neighbour.

Sentences are **invented on purpose** (a foundation deck has no source video):
the declared exception to the repo's "harvest from source" rule, which is why
`SOURCE_URL` is empty.

## What it covers — structural map (and how it differs from English)

French has load-bearing structures English lacks; the motor is built around them.

| Tag (`plane`) | Subsystem | Covers |
|---|---|---|
| `grammar` | Gender & articles | `le/la/les`, `un/une/des`, partitive `du/de la`, contractions `au/du` — every noun is M/F |
| `grammar` | Subject pronouns | `on` (= informal we), `tu/vous`, gendered `il/elle` for objects |
| `verb-construction` | Pillar verbs | `être / avoir / aller / faire` conjugated |
| `grammar` | Present tense | regular `-er` / `-ir` endings |
| `grammar` | Past | passé composé, the `être`-verbs + agreement, imparfait |
| `grammar` | Future & conditional | futur proche (`aller` + inf), polite `voudrais` |
| `grammar` | Negation | two-part `ne … pas / jamais / rien` |
| `grammar` | Object pronouns | pre-verbal `le/la/les`, `y`, `en` |
| `grammar` | Questions | `est-ce que`, `qu'est-ce que`, question words |
| `grammar` | Prepositions | `à` / `de` pillars + contractions, `chez`, `en` |
| `expression` | Impersonal frames | `c'est`, `il y a`, `il faut` |
| `connector` | Connectors | `et/mais/ou`, `parce que`, `donc`, `si/quand` |
| `grammar` | Adjectives | position (mostly after) + gender/number agreement, BAGS exceptions |
| `verb-construction` | Reflexive verbs | `je me lève`, `je m'appelle` |

**Out of scope (by design):** topical vocabulary, advanced lexis, the subjunctive,
literary tenses — those belong to the reading/elevation decks.

## Workflow

```
# 1. Build the deck (from repo root, venv active)
source .venv/bin/activate
python tools/deck_french_motor.py         # -> french/motor/motor.apkg

# 2. Import
#    double-click french/motor/motor.apkg  -> deck "french::motor" in Anki

# 3. Study one subsystem at a time, by tag, e.g.
#    tag:verb-construction   (the pillar verbs + reflexives)
#    tag:expression          (c'est / il y a / il faut)

# 4. Sync (local + GitHub)
git add tools/deck_french_motor.py french/motor/
git commit -m "french/motor: <change>"
git push origin main
```

To edit cards: change `CARDS` in `tools/deck_french_motor.py`, re-run the build,
re-import. The stable `DECK_ID` makes Anki update the existing cards in place.

## Architecture

```
elevation decks  → real French sources (tales, talks), harvested verbatim
─────────────────────────────────────────────────────────────────────────
motor (this deck) → gender, articles, conjugation, frames (automaticity)
```
