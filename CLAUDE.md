# NEUROCENTS — CLAUDE SESSION CONTEXT
> Este archivo se carga automáticamente en cada sesión. Contiene todo el contexto del canal,
> personaje, videos, workflow y estrategia. Actualizar aquí cuando cambien métricas o estado de videos.

---

## CANAL

- **Nombre:** Neurocents (archivos anteriores dicen "Crayon Capital" — mismo canal)
- **Handle YouTube:** [RELLENAR — @handle]
- **Nicho:** Behavioral finance / psicología del dinero
- **Formato:** Faceless, 2D animated, inglés
- **Cadencia:** 2 videos/semana
- **Horario publicación:** 20:00–22:00 hora Bali = 12:00–14:00 EST
- **Localización creador:** Bali

---

## PERSONAJE — ALEX

Descripción exacta para Google Flow / prompts de imagen:

> Large beige oval head with a transparent glass upper skull revealing a pink cartoon brain
> villain inside. Small black dot eyes, thin neutral mouth, black spiky hair, **blue t-shirt**,
> gray pants. The brain is an expressive villain character with heavy-lidded eyes, slight smirk,
> small teeth. 2D flat cartoon illustration, thick solid black outlines, clean solid color fills,
> no gradients. Palette: beige skin (#F5E6C8), black hair, muted blue shirt, gray pants, pink
> brain (#E8A598).

**Regla de Google Flow para mantener personaje:**
- Poner imágenes del personaje PRIMERO (posiciones 1, 2, 3 mínimo)
- NO subir imágenes de otros canales como referencia de formato — el modelo mezcla personajes
- Describir el estilo Andy/MoneyTom en texto, no con imágenes de referencia
- Usar thumbnails ya correctos del propio canal como referencia de personaje

**Expresiones (variar — no siempre sudando/preocupado):**
- Sorpresa / ojos abiertos
- Confianza / brazos cruzados
- Señalando algo fuera de frame
- Confundido / cabeza ladeada
- Satisfecho / sonrisa discreta

---

## ESTILO THUMBNAIL (nuevo — desde sesión actual)

**Referencia:** Andy Explains Money + MoneyTom
- Fondo blanco (no saturado como antes)
- Texto bold Impact, izquierda o centro
- Personaje en pose expresiva — variedad de layouts
- NO siempre "texto izquierda, personaje derecha" — rotar composición
- Max 5 palabras en thumbnail
- Texto crea pregunta, nunca responde

**Layouts a rotar (nunca dos iguales seguidos):**
1. Texto izquierda grande — personaje derecha
2. Personaje izquierda señalando derecha — texto derecha
3. Texto arriba — personaje abajo centrado
4. Split panel (izquierda vs derecha)
5. Personaje centro — texto encima y debajo
6. Grid / infographic con personaje lateral

---

## VIDEOS — PIPELINE COMPLETO

### PUBLICADOS (6 videos)

| # | Título original | Título nuevo (Andy/MoneyTom style) | Bias |
|---|---|---|---|
| V1 | YOUR BRAIN IS KEEPING YOU POOR / Three Brain Glitches | **Your Brain Is Keeping You Broke** | Múltiples sesgos — hecho antes de nuestra relación |
| V2 | The Dopamine Trap | **Why Buying Feels Better Than Having** | Dopamine / nucleus accumbens |
| V3 | Why Poor People Make Bad Decisions | **Why Being Poor Makes You Dumber** | Bandwidth Tax — Mullainathan & Shafir |
| V4 | Iowa Gambling Task / Damasio | **Your Brain Decided. You Just Signed the Receipt.** | Somatic markers — Elliot/Damasio |
| V5 | Mental Accounting — Why Free Money Is Most Expensive | **Why Losing Money Makes You Want to Lose More** | Mental Accounting — Thaler |
| V6 | Status Quo Bias / bank defaults | **The Billion-Dollar Bet Your Bank Wins Every Day** | Status Quo Bias |
| V7 | Someone Needs You to Buy at the Top. Here's Who. | **Someone Needs You to Buy at the Top** | Peak-End Rule / exit liquidity |

> **V7 URGENTE:** CTR 2% — necesita nuevo thumbnail ya. Causa: thumbnail frío + audiencia fría.
> Estrategia: Reddit posts en r/investing + r/CryptoCurrency el día de nuevo thumbnail.

### EN PRODUCCIÓN (no publicados)

| # | Título | Bias | Estado |
|---|---|---|---|
| V8 | Getting Rich Is Making You Poorer | Hedonic Treadmill + Diderot Effect | Script completo ✅ |
| V9 | The First Number They Show You in a Job Interview Is Not an Offer | Anchoring Bias | Script completo ✅ |
| V10 | Your Brain Won't Let You Quit — And It's Costing You Everything | Sunk Cost Fallacy — Concorde | Script completo ✅ |
| V11 | 3 Traps That Rewire Your Brain to Stay Broke | Reward Trap + Mental Accounting + Present Bias | Script + producción + beats completo ✅ |
| V12 | The One Decision That Defeats All Three Brain Traps | Sistema automático de ahorro | Script + producción completo ✅ |

**Cola de publicación (después de V7):** V8 → V3 → V5 → V4 (según last session)

---

## MÉTRICAS DE VIDEOS PUBLICADOS

> ⚠️ RELLENAR con capturas de YouTube Studio. Columnas: Views · CTR · Retención media · Subs ganados · Fecha publicación

| Video | Views | CTR | Retención | Subs | Fecha pub |
|---|---|---|---|---|---|
| V1 — Three Brain Glitches | — | — | — | — | — |
| V2 — Dopamine Trap | — | — | — | — | — |
| V3 — Poor Decisions | — | — | — | — | — |
| V4 — Iowa / Damasio | — | — | — | — | — |
| V5 — Mental Accounting | — | — | — | — | — |
| V6 — Status Quo Bias | — | — | — | — | — |
| V7 — Buy at the Top | — | **2%** | — | — | — |

---

## ARCHIVOS EN EL REPO

Cada video tiene su set completo de archivos Python + PDF/DOCX generados:

```
build_[video]_script.py        → guión narración (ElevenLabs)
build_[video]_doc.py           → documento de producción (beats)
build_[video]_elevenlabs_pdf.py → PDF para ElevenLabs
build_[video]_pdf.py           → PDF producción
```

**PDFs especiales:**
- `V10_Image_Prompts.txt` — 73 beats de imagen listos para copiar
- `V11_beats_prompts.pdf` — 145 beats (Camera/Lighting/Mood/Character/Motion) listos para copiar
- `One_Decision_IMAGE_PROMPTS.pdf` — beats V12
- `Mental_Traps_IMAGE_PROMPTS.pdf` — imagen prompts V11
- `Neurocents_Content_Framework.txt` — framework completo de contenido
- `Neurocents_Keywords.pdf` — keywords para YouTube Studio

**Checklists pre-publicación generados:**
- V4, V5, V6, V7, V9 — `[N4/N5/V6/V7/V9]_Prepublish_Checklist.docx`

---

## WORKFLOW DE PRODUCCIÓN (cómo trabajamos)

Cada video pasa por estos estados:

1. **Script narración** → `build_[x]_script.py` → genera SCRIPT.docx + SCRIPT.pdf
2. **ElevenLabs VO** → `build_[x]_elevenlabs_pdf.py` → genera PDF con formato especial para TTS
3. **Documento de producción** → `build_[x]_doc.py` → genera Production.docx/pdf con beats completos
   - Columnas: # · NARRACIÓN · IMAGE PROMPT · CAMERA · LIGHTING · MOOD · CHARACTER ACTION · VIDEO MOTION
4. **Image prompts** → extraídos del production doc, listos para copiar a Google Flow / Imagen 4
5. **Video beats** → formato `BEAT N | Camera: | Lighting: | Mood: | Character Action: | Video Motion:`
6. **Checklist pre-publish** → `build_[x]_publish_doc.py`

**Formato beats para copiar (lo que usa el animador):**
```
BEAT N | Camera: [valor] | Lighting: [valor] | Mood: [valor] | Character Action: [valor] | Video Motion: [valor]
```

**Google Flow — thumbnails:**
- Subir 3–4 imágenes del personaje como referencia primero
- Describir estilo Andy/MoneyTom en texto
- Nunca subir thumbnails de otros canales como referencia

---

## ESTRATEGIA DE DISTRIBUCIÓN

### Reddit
- **V3 (Bandwidth Tax):** r/personalfinance · r/sociology · r/psychology · r/science
- **V7 (Buy at the Top):** r/investing · r/CryptoCurrency
- **V10 (Sunk Cost):** r/personalfinance
- **V11 (3 Traps):** r/cogsci ← post ya escrito en sesión anterior

**Formato Reddit:**
- Post corto (150–200 palabras), sin spam, aporta valor
- Menciona el video de forma natural al final, no como promoción principal
- Postear el día de publicación del video

### LinkedIn
- V9 (Anchoring / Job Interview) — audiencia profesional

---

## OBJETIVOS CANAL

- **Septiembre 2026:** primer "signal month" (spike visible en métricas)
- **Condición:** V3 con buena ejecución en Reddit + V7 con thumbnail nuevo
- **Breakout potential ranking (de mayor a menor):**
  1. V3 — Why Poor People Make Bad Decisions (stat de 13 IQ points, controversial, multi-subreddit)
  2. V7 — Someone Needs You to Buy at the Top (crypto/inversión = alta distribución)
  3. V10 — Sunk Cost (r/personalfinance siempre activo)
  4. V9 — Anchoring / Job Interview (LinkedIn + profesionales)
  5. V11 — 3 Traps (behavioral, amplio)
  6. V12 — One Decision (solución práctica)

---

## NOTAS IMPORTANTES

- El canal se llamó "Crayon Capital" en sesión anterior → ahora es **Neurocents**. Los archivos más antiguos dicen CRAYON CAPITAL en los subtítulos.
- V11 en los archivos dice NEUROCENTS · VIDEO 11 (primer video con branding nuevo)
- V12 dice CRAYON CAPITAL — puede necesitar actualización de branding
- La tabla de métricas de arriba hay que rellenarla — mandar captura de YouTube Studio
