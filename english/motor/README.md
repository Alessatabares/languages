# english · motor

The **structural engine** of English: the high-frequency, closed-class core that
carries 70%+ of everything spoken and written. This is the foundation deck — the
layer you want automatic before the advanced reading decks (e.g. Nietzsche C2).

- **File:** `motor.apkg` → imports as the Anki deck `english::motor`
- **Source script:** `../../tools/deck_english_motor.py`
- **Cards:** 51 · monolingual English · Cloze
- **Stable `DECK_ID`** → re-importing updates the cards, never duplicates.

## Card design — pattern-centric

The learning unit is the **pattern**, not the word:

```
FORK (the discriminator) → VARIATION (several examples) → COMPRESSION (the rule)
```

Two card shapes, same Cloze note:

1. **Contrast set** — a fork with a confusable neighbour (`who` vs `which`,
   `much` vs `many`, `will` vs `going to`). Front = a **title** naming the fork +
   4–6 varied example lines, each with its pivot in `{{c1::…}}`. Every blank is
   `c1`, so it's **one card** ("fill every blank"), and the answers differ line
   to line — you have to actually discriminate, not autopilot.
2. **Simple** — an item with no obvious neighbour (`of`, `used to`). Front = 1–2
   clozed lines.

Back, all in English:

- **Rule** — the discriminator headline (red, on top): the one line to compress.
- **Intention** — the job the pattern does.
- **Pattern** — the reusable, generative frame (one card → many sentences).
- **Image** / **note** — a concrete picture, or the trap with the neighbour.

Sentences are **invented on purpose** (a foundation deck has no source video):
this is the declared exception to the repo's "harvest from source" rule, which is
why `SOURCE_URL` is empty.

## What it covers — structural map

9 subsystems (grouped `A–I` in the script; tag = `plane`). Study one at a time.
Most rows are **contrast sets** — the fork is right there in the title.

| Tag (`plane`) | Subsystem | Forks & items |
|---|---|---|
| `grammar` | Pointing & reference | `who` vs `which`, `this/that/these/those`, dummy `it` vs `there`, singular `they` |
| `grammar` | Articles & quantity | `a` vs `the`, `some` vs `any`, `much` vs `many`, `every` vs `all` |
| `grammar` | Prepositions | `at/on/in`, `to` vs `from`, `of`, `with/for/by/about`, `between`, `through` |
| `grammar` | Tense / mood engine | do-support, `be+ing`, present perfect vs `have been +ing`, passive, `will` vs `going to`, `can` vs `could`, `must` (2 jobs), `should` vs `must`, `might`, `would` |
| `expression` | Generative frames | the three conditionals, `the more…the more`, `used to`, `'d rather` vs `'d better` |
| `connector` | Connectors | `and/but/or`, `because` vs `so`, `although` vs `while`, `when` vs `while`, reporting `that` |
| `verb-construction` | Light verbs | `make` vs `do`, `get/take/have/go/give/keep/let`, `want/need` + collocations |
| `grammar` | Negation, degree, timing | no double negatives, frequency-adverb position, `very/too/so`, `already/yet/still`, `just` |
| `grammar` | Wh- questions | `what/why/how/where/whose` + subject-aux inversion |

**Out of scope (by design):** topical vocabulary, C1→C2 lexis, high-register
discourse connectors, rhetorical moves — those belong to the elevation decks
built from real sources.

## Workflow

```
# 1. Build the deck (from repo root, venv active)
source .venv/bin/activate
python3 tools/deck_english_motor.py       # -> english/motor/motor.apkg

# 2. Import
#    double-click english/motor/motor.apkg  -> deck "english::motor" in Anki

# 3. Study one subsystem at a time, by tag, e.g.
#    tag:expression          (the generative frames)
#    tag:verb-construction   (the light verbs)

# 4. Sync (local + GitHub)
git add tools/deck_english_motor.py english/motor/
git commit -m "english/motor: <change>"
git push origin main
```

To edit cards: change `CARDS` in `tools/deck_english_motor.py`, re-run the build,
re-import. The stable `DECK_ID` makes Anki update the existing cards in place.

## Architecture

```
elevation decks  → essays + deep conversation (C2), harvested from real sources
─────────────────────────────────────────────────────────────────────────────
motor (this deck) → structural skeleton + light verbs + frames (automaticity)
```
