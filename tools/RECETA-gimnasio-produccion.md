# Receta — Gimnasio de producción (juegos de escribir desde cero)

Cómo construir un "gimnasio de producción" para cualquier deck. Es un sitio HTML
estático, self-contained, que lleva del **reconocer** (Anki) al **producir por
instinto**: sacar la palabra de una situación y escribir en un contexto nuevo.

Ya hechos:
- `english/practica-produccion/index.html` — 45 palabras Nietzsche, nivel **C2**.
- `french/practica-produccion/index.html` — 40 palabras sorcière, nivel **A2**.

## Idea pedagógica (no la pierdas)

1. **Reconocer ≠ producir.** Anki entrena reconocer; esto entrena producir.
2. **Escalera de 5 escalones**, de fácil a difícil, **la misma para cada palabra**.
3. **La escalera se adapta al NIVEL del deck** (ver abajo). No es negociable:
   pedir humor a un A2 lo hace fracasar.
4. **Domain-shift obligatorio:** la regla del ejercicio es NO usar el tema del
   libro. Meter la palabra en la vida real de ella. Eso es lo que despega la
   palabra de su origen y construye instinto.
5. **Corrección por loop, no en vivo.** Un sitio estático (GitHub Pages) no puede
   llamar a una IA. Por eso: ella escribe → botón **Exportar** copia todo con una
   cabecera "corrige mi X" → lo pega al chat del tutor → yo corrijo → ella pega la
   versión corregida en la caja y marca `corregida ✓`. El localStorage lo guarda.

## Las escaleras por nivel

- **C1–C2 (avanzado): escalera de humor.**
  1 Observación · 2 Exageración · 3 Ironía · 4 Metáfora · 5 Absurdo.
  Palabra neutra demo que sube los 5: `slow`.
- **A1–A2 (principiante): escalera de tipos de frase.**
  1 Frase simple y verdadera · 2 Una pregunta · 3 La negación (`ne…pas`) ·
  4 Pasado o futuro · 5 Mini-historia (2 frases).
  Palabra neutra demo: `le café`.
- **B1–B2 (futuro, aún no hecho):** escalera intermedia sugerida —
  1 Frase con opinión · 2 Hipótesis (condicional) · 3 Contraste (conector) ·
  4 Reformular ("es decir…") · 5 Párrafo corto con 2 conectores.

## Idioma de la interfaz

- Deck **avanzado en su lengua meta** (inglés C2) → UI en esa lengua (inmersión).
- Deck de **nivel bajo** (francés A2) → UI en **español** (regla del repo:
  comentario de tutor en español; no apilar inglés sobre francés de principiante).

## Pasos para un gimnasio nuevo

1. Elige el deck fuente: `tools/deck_<lang>_<slug>.py` → su lista `CARDS` es el dato.
2. **Copia** un `index.html` existente (mejor el del nivel más parecido). El motor
   es genérico; solo cambian los datos y los textos.
3. Reescribe el array **`DATA`** con las cards. Campos por palabra:
   `t` (término) · `pl` (plane) · `m` (gloss/significado — solo si el back NO es
   monolingüe, p.ej. francés) · `j` (intención = "para qué sirve") · `img`
   (imagen) **o** `pat` (patrón) · `syn` (sinónimos, opcional) · `note` (ojo:
   género, falso amigo, conjugación).
4. Ajusta **`RUNGS`** a la escalera del nivel (ver arriba), con la palabra-demo.
5. Cambia los textos de UI, y **`const KEY`** (localStorage) a algo único por
   gimnasio, p.ej. `prod-<slug>-v1` — si repites KEY, dos juegos se pisan los datos.
6. Cabecera de exportación y placeholder en el idioma de UI que toque.
7. **Valida** el JS antes de subir (evita romperlo con una coma):
   ```bash
   python3 -c "import re;h=open('index.html',encoding='utf-8').read();open('/tmp/x.js','w').write(re.search(r'<script>(.*)</script>',h,re.S).group(1))"
   node --check /tmp/x.js
   ```
8. Sube SOLO la carpeta nueva (no barrer cambios sueltos del working tree):
   ```bash
   git add <lang>/practica-produccion/
   git commit -m "Production gym (<lang>): <slug> ..."
   git push origin main
   ```

## Motor (qué ya trae el index.html, no lo reescribas)

- 1 palabra a la vez · panel de apoyo (significado/intención/imagen o patrón/nota)
  · banner de la regla · 5 escalones con def + ejemplo demo + textarea + `corregida ✓`.
- Navegación `prev / next / select`, barra de progreso ("palabras empezadas").
- Autosave a `localStorage` con clave `KEY`. Exportar 1 palabra / Exportar todo
  (copia al portapapeles con cabecera de corrección). Botón reiniciar.
