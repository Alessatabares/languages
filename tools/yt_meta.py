# -*- coding: utf-8 -*-
"""Metadatos de un video de YouTube, para verificar que el transcript coincide.

NO baja los subtítulos: YouTube bloquea el endpoint `timedtext` sin token de
sesión (devuelve 0 bytes). El transcript lo sigue aportando Alessa. Esto sirve
para comprobar ANTES de curar que el video es el que dice ser y que el
transcript está completo.

Uso:  python tools/yt_meta.py <url-o-id> [--palabras N]
      --palabras N  = cuántas palabras trae el transcript pegado.
      --hasta MM:SS = último timestamp del transcript. Mejor señal de
                      completitud que el conteo de palabras.
"""

import json
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120 Safari/537.36"}
WPM_MIN, WPM_MAX = 100, 170   # habla narrada normal


def video_id(s):
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", s)
    return m.group(1) if m else (s if re.fullmatch(r"[A-Za-z0-9_-]{11}", s) else None)


def first(html, pattern, default=None):
    m = re.search(pattern, html)
    return m.group(1) if m else default


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("uso: python tools/yt_meta.py <url-o-id> [--palabras N]")
    vid = video_id(args[0])
    if not vid:
        sys.exit(f"no pude sacar el ID del video de: {args[0]}")

    palabras = None
    if "--palabras" in sys.argv:
        palabras = int(sys.argv[sys.argv.index("--palabras") + 1])
    hasta = None
    if "--hasta" in sys.argv:
        mm, ss = sys.argv[sys.argv.index("--hasta") + 1].split(":")
        hasta = int(mm) * 60 + int(ss)

    url = f"https://www.youtube.com/watch?v={vid}"
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")

    title = first(html, r'"title":"((?:[^"\\]|\\.)*)"', "?")
    title = json.loads(f'"{title}"')
    canal = first(html, r'"ownerChannelName":"((?:[^"\\]|\\.)*)"', "?")
    canal = json.loads(f'"{canal}"')
    fecha = first(html, r'"uploadDate":"([^"]+)"', "?")[:10]
    segs = int(first(html, r'"lengthSeconds":"(\d+)"', "0"))

    print(f"Título   : {title}")
    print(f"Canal    : {canal}")
    print(f"Subido   : {fecha}")
    print(f"Duración : {segs // 60}:{segs % 60:02d}  ({segs}s)")

    m = re.search(r'"captionTracks":(\[.*?\])', html)
    if not m:
        print("Subtítulos: NINGUNO declarado "
              "(o video restringido) -> el transcript no se puede contrastar")
    else:
        for t in json.loads(m.group(1)):
            kind = "AUTOMÁTICO (ASR)" if t.get("kind") == "asr" else "MANUAL"
            print(f"Subtítulos: {t.get('languageCode')} · {kind}")
        if any(t.get("kind") == "asr" for t in json.loads(m.group(1))):
            print("  -> esperar typos de ASR: homófonos, nombres propios rotos, "
                  "puntuación inventada. Corregir al cosechar.")

    if hasta and segs:
        falta = segs - hasta
        print(f"\nTranscript llega a {hasta//60}:{hasta%60:02d} de {segs//60}:{segs%60:02d} "
              f"-> faltan {falta//60}:{abs(falta)%60:02d}")
        if falta > 90:
            print("  INCOMPLETO -> se cortó antes del final. Pide el resto.")
        elif falta < -5:
            print("  RARO -> el transcript pasa de la duración del video. "
                  "¿Es el video correcto?")
        else:
            print("  OK -> cubre el episodio entero.")

    if palabras and segs:
        esperado = (int(segs / 60 * WPM_MIN), int(segs / 60 * WPM_MAX))
        print(f"\nTranscript: {palabras} palabras. Esperado para {segs//60}:{segs%60:02d}: "
              f"{esperado[0]}–{esperado[1]}")
        if palabras < esperado[0] * 0.7:
            print("  INCOMPLETO -> falta buena parte del video. Pídelo completo "
                  "antes de curar.")
        elif palabras > esperado[1] * 1.4:
            print("  DE MÁS -> puede traer texto que no es del video (descripción, "
                  "comentarios). Revisa antes de cosechar frases.")
        else:
            print("  OK -> coincide con la duración.")


if __name__ == "__main__":
    main()
