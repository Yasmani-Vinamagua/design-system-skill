---
name: yas-core
description: Núcleo compartido de Yas Design: reglas comunes obligatorias, artefactos compartidos, especificación de tokens, criterios de calidad y referencias externas que usan /yas-design, /yas-audit y /yas-figma. No se invoca directamente; las otras skills lo leen.
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
| `references/referencias-externas.md` | Lista única de fuentes (IBM, Wolff Olins, Google, LEGO, Adobe, M3, HIG) y reglas de uso | Las tres |

Debe instalarse **junto** a las otras tres skills, en la misma carpeta de skills, porque ellas lo referencian con la ruta relativa `../yas-core/`.
