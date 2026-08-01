# ETIQUETA REAL — estado del proyecto

> Canal de vídeos narrativos en español, formato "ranking de marcas de supermercado" con
> B-roll de stock (Freepik), sin personaje animado — edición tipo Ken Burns/CapCut sobre
> clips reales. Nombre interno del proyecto: **Etiqueta Real** (visto en comentarios de
> `build_beats.py`). Es un canal DISTINTO de Neurocents (el del `CLAUDE.md` raíz del repo,
> que usa personaje animado Alex/Brain Villain — no aplican sus reglas a este proyecto).
>
> Guardado aquí el 2026-08-01 a petición del creador ("guarda todo el proceso en la
> memoria"), tras no poder crear un repo de GitHub nuevo por falta de permisos de la
> integración (403 al llamar a `create_repository`). Se guarda dentro de este repo
> (`7zwx6zwvfq-a11y/claudeeee`), en la carpeta `etiqueta-real/`, separado del contenido
> de Neurocents, en la rama `claude/youtube-content-cloning-omoe78`.

## Formato validado (usado en V1 — Aceite de Oliva, y V2 — Atún)

1. **HOOK** — dato de contexto (precio, producción, consumo) + promesa: "hoy revisamos N
   marcas... por qué pagas más de lo que crees por menos de lo que piensas" + tease de
   alternativas buenas al final.
2. **Ranking de peor a mejor (7 marcas)** — cada una con: quién la fabrica de verdad / grupo
   propietario oculto, el truco de etiquetado o proceso concreto, la ley/norma exacta que lo
   permite, por qué el comprador no lo detecta.
3. **CTA sutil de suscripción** a ~35% del vídeo (justo después del emotional/informational
   high point de la primera mitad, antes de la segunda tanda de marcas).
4. **3 "mejores opciones"** — marcas pequeñas/familiares con trazabilidad real, sello oficial,
   por qué sí cumplen lo que prometen.
5. **CIERRE** — checklist práctico (4-5 reglas) para aplicar en el súper + CTA de compartir
   con quien compra esa marca sin pensarlo.

Referencia de tono usada para pulir V2: el canal "Consumer Exposed" (script real de bread
brands aportado por el creador) — frases cortas tipo veredicto, cifras concretas sueltas,
corte de mitad de vídeo tipo re-hook, guardar la revelación más fuerte para el puesto nº1,
cierre con regla práctica de una sola línea + CTA de compartir.

---

## V1 — ACEITE DE OLIVA ✅ TERMINADO (carpeta `aceite_oliva/`)

- Guion completo en `aceite_oliva/full_script.py`. ~444 beats, audio real 22:30.
- Ranking (peor→mejor): 7 Coosur · 6 La Española · 5 Borges · 4 Hacendado · 3 Ybarra ·
  2 Hojiblanca · 1 Carbonell. Mejores: 3 Melgarejo · 2 Castillo de Canena · 1 Núñez de Prado.
- Revelación central repetida: Coosur/La Española = mismo grupo (DCOOP); Hojiblanca/Carbonell
  = mismo grupo (Deoleo, ex-SOS Cuétara), que también controla Bertolli fuera de España.
- Truco de etiquetado explicado varias veces: "Aceite de oliva" (sin "virgen") = refinado
  (calor+disolventes) + un % de virgen añadido para dar color/aroma — mismo apellido/botella
  que la línea premium, distinto producto.
- Normativa citada: Reglamento UE 29/2012 (normas de comercialización aceite de oliva),
  Reglamento UE 1169/2011 (información alimentaria — permite "Unión Europea" como origen
  genérico en mezclas). Categorías IOC por acidez: virgen extra ≤0,8%, virgen ≤2%, lampante
  por encima. Oleocanal (Monell Chemical Senses Center / Nature 2005) como indicador de
  frescura real.
- Pipeline de archivos: `full_script.py` → `build_beats.py` → 4 CSV
  (`Aceite_Oliva_1_Beats.csv`, `_2_Shots_unicos.csv`, `_3_Clip_a_Beats.csv`,
  `_4_Pendiente_por_buscar.csv`) → PDFs vía `make_pdfs.py` → `Aceite_Oliva_PRODUCTION.xlsx`,
  `Aceite_Oliva_ELEVENLABS.pdf`, `Aceite_Oliva_Frase_a_Video.pdf`.
- Pool de B-roll: ~120 tags reutilizables mapeados a IDs de Freepik REALES y verificados
  (`order.txt`, `urls.json`, dict `SHOTS`/`DOWNLOAD_URLS` dentro de `build_beats.py`).
- Pendientes NO bloqueantes (`Aceite_Oliva_4_Pendiente_por_buscar.csv`): varios clips
  bloqueados por rate limit de Freepik (IDs 977016, 1348524, 5751633, 5752936, 8809408); un
  ID inválido (134130) que da 404; tags sobreusados (generic_shelf, shelf_oils, network_anim,
  magnifier_doc, yellow_cap, >15-25 usos); temas sin cobertura de stock (testimonio experto,
  comparativa botella oscura/clara, infografía IOC, fachada súper genérica, laboratorio de
  catadores, camión de reparto, fábrica cerrada para el tramo Deoleo/crisis financiera).

---

## V2 — ATÚN ✅ GUION Y PRODUCCIÓN LISTOS, PENDIENTE STOCK REAL (carpeta `atun/`)

- Guion completo en `atun/atun_full_script.py`. **4.513 palabras, ~25.9 min** a 174 ppm
  (objetivo pedido: 25-27 min — cumplido; V1 se quedó corto en 22:30, aviso explícito del
  creador de que este debía ser más largo).
- **CTA sutil de suscripción al 35,8%** del guion (tras cerrar el bloque de Isabel, antes de
  Carrefour) — pedido explícito del creador: "sutil", no plantilla agresiva tipo Neurocents.
- **Sin porcentajes en la narración** (pedido explícito) — todas las cifras de cuota/proporción
  se expresan como fracciones habladas: "uno de cada cinco", "siete de cada diez gramos",
  "una de cada seis latas", "la mitad de su tamaño anterior". Verificado con grep antes de
  cerrar el guion, cero coincidencias de "%" o "por ciento" en el texto narrado.
- **Marcas del ranking = reconocibles en LatAm Y España a la vez** (pedido explícito tras
  descartar una primera propuesta que mezclaba iconos solo-regionales tipo Dolores/Mar de
  Plata). Ranking final (peor→mejor):

  | # | Marca | Reveal central |
  |---|---|---|
  | 7 | **Hacendado** (Mercadona) | Fabricada por Conservas Escurís, del grupo **Jealsa** — verificado: lo publican Mercadona/Jealsa en sus propias memorias de sostenibilidad, nunca en la lata. |
  | 6 | **Robinson Crusoe** (ícono chileno, 1953) | Desde 2004 pertenece a **Jealsa** (mismo grupo que Hacendado) — en España la misma empresa vende como **Rianxeira**. |
  | 5 | **Isabel** (España + Ecuador/Perú/Colombia/México) | Conservas Garavilla, accionista de control **Bolton Group** (mismo grupo de Rio Mare Italia y Saupiquet Francia). |
  | — | *CTA sutil de suscripción aquí (~35%)* | |
  | 4 | **Carrefour** (marca blanca, España+Argentina) | Opacidad de fabricante + OCU 2024-25 (32 marcas testadas, peor valorada por sal; 13/32 con girasol en vez de oliva) + regla de peso escurrido (≥70% natural / ≥65% aceite-escabeche). |
  | 3 | **Conservas Ortiz** (histórica, 1891, premium) | Peor nota OCU 2025 (exceso de sal + errores de etiquetado) pese al precio y la historia. |
  | 2 | **Nostromo** | 100% Grupo Calvo desde 1993 — aquí se explica el concepto de "marca lucha"/flanker brand. |
  | 1 | **Calvo** (ancla, Galicia 1940) | Cierra el hilo: dueña de Nostromo + Gomes da Costa (Brasil, 2004) + 2ª marca de Centroamérica + participación de **Bolton Group** (mismo accionista que Isabel, puesto 5). |

  Mejores opciones (España, independientes, no verifiqué un pick 100% latinoamericano
  igualmente transparente — pendiente si se quiere sustituir): 3 Frinsa (Ribeira 1961,
  flota propia) · 2 Palacio de Oriente (Vigo 1873, la conservera activa más antigua de
  España) · 1 Consorcio (Santoña, procesado artesanal pieza a pieza).

- Normativa citada: Reglamento UE 1379/2013 (especie exacta, arte de pesca, zona FAO en
  etiqueta), Reglamento UE 1881/2006 (límite de mercurio: 0,5 mg/kg general, hasta 1 mg/kg
  en especies depredadoras grandes como rabil/patudo), Reglamento UE 1169/2011 (origen
  genérico permitido en marca blanca), regla de peso escurrido (natural ≥70%, aceite o
  escabeche ≥65%).
- Pipeline generado: `atun_full_script.py` → `build_beats_atun.py` (488 beats, target
  26:00) → `Atun_Beats.csv` → `make_atun_pdfs.py` → `Atun_SCRIPT.pdf` (con cabeceras, para
  revisión), `Atun_ELEVENLABS.pdf` (narración limpia, 176 líneas), `Atun_Beats.pdf` (tabla
  con timecodes y CapCut Motion).
- **⚠️ PENDIENTE — lo único que falta para producción real:** los 488 beats tienen una
  columna "sugerencia visual" que es un CONCEPTO descriptivo (ej. "Mapa animado con España,
  Ecuador, Perú..."), NO un clip de stock real con ID de Freepik verificado como en V1. No
  se ha hecho búsqueda de stock real esta sesión — haría falta repetir el proceso de V1
  (`SHOTS`/`DOWNLOAD_URLS` con IDs y enlaces reales) antes de poder montar en CapCut.
- Nota de confianza: la participación exacta de Bolton Group en Grupo Calvo se dejó sin
  cifra concreta en el guion porque las fuentes encontradas se contradicen (una dice 40%
  desde 2012, otra dice familia al 77,8%) — se optó por "una participación" sin porcentaje,
  lo cual además encaja con la petición de no usar porcentajes.

---

## Archivos en `etiqueta-real/` (este repo)

```
etiqueta-real/
  PROJECT_STATE.md          <- este archivo
  aceite_oliva/              <- V1 completo (script, beats, shots reales, PDFs, xlsx)
  atun/                      <- V2 completo (script, beats, PDFs) — falta stock real
```

No incluye `junko_furuta/` (true crime, proyecto/canal distinto, no forma parte de
Etiqueta Real) — se quedó solo en el scratchpad de la sesión original si hace falta luego.

## Próximos pasos posibles

1. Aprobar el guion de V2 (Atún) tal cual, o pedir ajustes.
2. Buscar y verificar clips de stock reales (Freepik) para los 488 beats de Atún, igual que
   se hizo para Aceite — es el único bloque pendiente antes de poder montar el vídeo.
3. Generar `Atun_Prepublish_Checklist` (título, descripción, tags, Reddit) cuando el guion
   esté aprobado — no se ha hecho todavía para este vídeo.
4. Decidir el V3 de este canal (siguiente categoría de producto a rankear).
