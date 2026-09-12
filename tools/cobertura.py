# -*- coding: utf-8 -*-
"""Qué términos ya están cubiertos en los decks de un idioma.

La fuente de verdad son los propios `tools/deck_<lang>_*.py`, así que esto nunca
se desincroniza. Sirve para que un deck nuevo del mismo idioma NO repita lo que
otro deck ya practica.

Uso:
  python tools/cobertura.py portuguese
  python tools/cobertura.py portuguese --candidatos "brincar, chata, tô, gostar de"
"""

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def norm(s):
    """minúsculas sin acentos, para que 'tá' y 'ta' choquen igual."""
    s = unicodedata.normalize("NFD", s.strip().lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def decks(lang):
    return sorted(p for p in ROOT.glob(f"deck_{lang}_*.py"))


def terms_of(path):
    """Decks de contenido usan term="..."; los decks motor usan rule="..." .
    Los dos cuentan como cobertura."""
    src = path.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'dict\(plane="([^"]+)",\s*term="([^"]+)"', src):
        out.append((m.group(2), m.group(1)))
    for m in re.finditer(r'dict\(plane="([^"]+)",\s*\n?\s*rule="([^"]+)"', src):
        out.append((m.group(2), m.group(1)))
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python tools/cobertura.py <idioma> [--candidatos "a, b, c"]')
    lang = sys.argv[1]
    files = decks(lang)
    if not files:
        print(f"No hay ningún deck de '{lang}' todavía. Todo término es nuevo.")
        if "--candidatos" not in sys.argv:
            return

    cubierto = {}   # norm -> (término original, deck, plano)
    for f in files:
        slug = f.stem.replace(f"deck_{lang}_", "")
        ts = terms_of(f)
        print(f"\n{slug}  ({len(ts)} términos)")
        by_plane = {}
        for t, pl in ts:
            by_plane.setdefault(pl, []).append(t)
            cubierto.setdefault(norm(t), (t, slug, pl))
        for pl in sorted(by_plane):
            print(f"  {pl:19} {' · '.join(by_plane[pl])}")

    if files:
        print(f"\nTOTAL en {lang}: {len(cubierto)} términos únicos, {len(files)} decks.")

    if "--candidatos" in sys.argv:
        raw = sys.argv[sys.argv.index("--candidatos") + 1]
        cands = [c.strip() for c in raw.split(",") if c.strip()]
        def choque(c):
            n = norm(c)
            if n in cubierto:
                return cubierto[n]
            # los decks motor guardan reglas largas ("je voudrais -> polite...");
            # buscar la subcadena atrapa el término dentro de la regla.
            for k, v in cubierto.items():
                if len(n) >= 3 and n in k:
                    return v
            return None

        choques = [(c, h) for c in cands if (h := choque(c))]
        nuevos = [c for c in cands if not choque(c)]
        print(f"\n--- {len(cands)} candidatos ---")
        if choques:
            print(f"YA CUBIERTOS ({len(choques)}) — sácalos, o justifica el sentido nuevo:")
            for c, (orig, slug, pl) in choques:
                print(f"  {c:22} -> ya está en {slug} como '{orig}' ({pl})")
        print(f"NUEVOS ({len(nuevos)}): {' · '.join(nuevos) if nuevos else '(ninguno)'}")
        if len(nuevos) < 25:
            print("\n  OJO: menos de 25 términos nuevos. Este transcript ya no da "
                  "para un deck propio a este nivel. Dile en vez de rellenar.")


if __name__ == "__main__":
    main()
