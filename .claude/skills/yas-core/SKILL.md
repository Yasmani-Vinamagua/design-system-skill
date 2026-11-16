---
name: yas-core
description: "Núcleo compartido de Yas Design: reglas comunes obligatorias, artefactos compartidos, especificación de tokens, criterios de calidad y referencias externas que usan /yas-design, /yas-audit y /yas-figma. No se invoca directamente; las otras skills lo leen."
user-invocable: false
---

# Yas Core

Núcleo compartido del ecosistema Yas Design. No tiene comandos propios. Cada tema se define **una sola vez** aquí y las tres skills lo referencian, de modo que trabajan sobre los mismos resultados con los mismos criterios sin repetir documentación.

| Documento | Qué fija | Lo usan |
|---|---|---|
| `references/reglas-comunes.md` | Reglas obligatorias (inspección inicial, contexto, ejecución, archivos, protección, calidad, documentación, transparencia) y regla de alcance | Las tres, siempre, antes de actuar |
| `references/artefactos.md` | Qué archivos de `.yas/` existen, quién los produce y quién los consume; reglas de compartición; contrato de la paleta | Las tres |
| `references/tokens-spec.md` | Formato de los tokens (DTCG), niveles primitivo y semántico, nomenclatura, modos claro y oscuro, roles semánticos | `/yas-figma` |
| `references/criterios-calidad.md` | Umbrales de accesibilidad, cálculo de contraste, criterios de tokens, componentes y nomenclatura | Las tres |
| `scripts/` | Herramientas de Python sin dependencias (ver más abajo) | `/yas-design` |
| `references/referencias-externas.md` | Lista única de fuentes (IBM, Wolff Olins, Google, LEGO, Adobe, M3, HIG) y reglas de uso | Las tres |

Debe instalarse **junto** a las otras tres skills, en la misma carpeta de skills, porque ellas lo referencian con la ruta relativa `../yas-core/`.

## Scripts (`scripts/`)

Python 3.8+ sin dependencias. Renderizan con el primer motor disponible (cairosvg, rsvg-convert, Inkscape o Chromium/Chrome/Edge); si no hay ninguno, lo dicen y no dan la prueba por superada. Ejecútalos con `python -I`.

| Script | Uso | Qué hace |
|---|---|---|
| `svg_audit.py` | `svg_audit.py logo-master.svg [--json]` | Valida XML, viewBox, referencias, filtros/imágenes/`<text>`, colores, trazos, anclas, ángulos casi enteros, microdetalles y precisión. Solo diagnostica: mide construcción, no calidad de diseño. |
| `test_sheet.py` | `test_sheet.py logo.svg -o carpeta` | Genera `hoja-pruebas.html/.png`: tamaños 16–128 px, una tinta, blanco sobre negro, fondos de contraste, giros, espejo, desenfoque y silueta. |
| `concept_sheet.py` | `concept_sheet.py conceptos.json -o concepto` | Genera `opciones.html/.png` con una tarjeta por concepto (A, B, C), esquema SVG y recomendado. |
| `export_variants.py` | `export_variants.py logo-master.svg -o logo/ --png --ico` | Deriva `logo-1tinta-negro.svg`, `logo-1tinta-blanco.svg`, PNG por tamaño y `favicon.ico`. No sobrescribe sin `--force`. No genera color, negativo, lockups ni reducido (son decisiones de diseño). |
| `_render.py` | `_render.py` | Módulo común; ejecutado solo, lista los renderizadores disponibles. |
