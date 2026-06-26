# languages

Anki decks for learning languages, built from YouTube videos. One folder per
language. Each deck targets the **B2/C1 → C2** jump: advanced lexis, dense
verb/grammar constructions, and connectors that elevate writing.

## Structure

```
languages/
├── english/        # decks built from English videos
│   └── nietzsche-truth-lies.{apkg,tsv,md}
├── french/         # (coming)
└── tools/
    └── build_deck.py   # generator: card list -> .apkg + .tsv + .md
```

## Each deck = 3 files

| File | Use |
|---|---|
| `.apkg` | **Download and double-click** → imports straight into Anki |
| `.tsv`  | Manual import (note type Cloze, separator Tab, Allow HTML) |
| `.md`   | Readable on GitHub, grouped by plane |

## Card design

Cloze note type. Front = a real sentence from the video with the term hidden.
Back (all in English, on purpose — monolingual = transfer):

- **Intention** — when you reach for the word / the job it does
- **Image** (lexis) or **Pattern** (verbs, grammar, connectors → a template you can reuse when *you* write)
- **Synonyms** — alternatives and register equivalents

## Workflow (per video)

1. Pick a YouTube video and grab its transcript.
2. Curate the C1→C2 items across three planes: advanced lexis · verbs &
   grammar · connectors. Skip what's already B2, plus proper nouns and Latin.
3. Add them to a `CARDS` list and run the generator.
4. Commit the three output files into the language folder.

```bash
pip install -r requirements.txt
python tools/build_deck.py
```
