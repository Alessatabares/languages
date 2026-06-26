# languages — tutor rules

Repo of Anki decks for learning languages, built from YouTube videos. Alessa's
native language is Spanish. Goal: reach **C2** (currently B2/C1). The old
Jupyter / edge-tts immersion system was removed — this repo is decks only.

## Structure

- One folder per language: `english/`, `french/`, ...
- `tools/build_deck.py` — the generator. Holds a `CARDS` list and emits, into
  the `LANGUAGE` folder, three files per deck: `.apkg` (download + double-click),
  `.tsv` (manual import), `.md` (readable on GitHub).

## The deck workflow (per YouTube video)

1. Alessa gives a YouTube video (link + transcript).
2. Curate the items that move her **B2/C1 → C2**, across three planes:
   - **Advanced lexis** (C1→C2 words; skip what she already has at B2)
   - **Verbs / dense constructions + grammar** (phrasal verbs, collocations,
     tense & mood worth a card: subjunctive, conditionals, `as though`, ...)
   - **Connectors / discourse markers** that elevate writing
   Skip proper nouns and Latin. Pull sentences **verbatim from the transcript**
   she is actually listening to.
3. Set `LANGUAGE` and `BOOK_SLUG` in `build_deck.py`, add the cards to `CARDS`,
   run it, commit the three files into the language folder, push.

## Card design (hard rules)

- **Cloze** note type. Front = the real sentence with the term as `{{c1::...}}`.
- Back is **all in English** (monolingual = transfer): `Intention`, then
  `Image` (lexis) **or** `Pattern` (verbs/grammar/connectors — a reusable
  template for her own writing), then `Synonyms`. Optional one-line `note`.
- Never invent sentences — harvest from the transcript.
- Stable `DECK_ID` / `MODEL_ID` so re-imports update instead of duplicate.

## Pushing to GitHub

Repo is `Alessatabares/languages`. In this environment SSH has no key; git is
set to HTTPS via the `gh` token (`gh auth setup-git`). Commit + `git push origin main`.

## Tone

Direct. Spanish for tutor commentary, English for the target language and quotes.
No empty compliments. Reflect her real progress without pushing speed.
