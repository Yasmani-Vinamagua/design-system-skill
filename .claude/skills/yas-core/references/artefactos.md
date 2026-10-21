# Artefactos compartidos

Las tres skills trabajan sobre **los mismos archivos**, no sobre copias. Este documento fija qué archivo existe, dónde vive, quién lo produce y quién lo consume. Una skill **lee** lo que otra produjo en lugar de volver a pedirlo o regenerarlo, y **enlaza** a la fuente en lugar de repetir su contenido.

## Flujo de ejemplo

1. `/yas-design rebrand` (también `rebranding`) crea la nueva identidad y fija la paleta en `.yas/brand/paleta/paleta.md` y en el manual.
2. `/yas-figma colors` lee esa paleta y la transforma en tokens y variables semánticas: escribe los tokens de color en `.yas/tokens/tokens.json` (según `tokens-spec.md`) y crea las variables en Figma, o el paquete local si no hay MCP.
3. `/yas-audit` comprueba, en el módulo de consistencia, que la identidad aplicada usa esa paleta de forma coherente en los activos y canales, tomando como criterio el manual y la propia paleta.

Cada skill conserva su especialidad: diseña, traduce o verifica. Ninguna rehace el trabajo de otra.

## Mapa de artefactos

Rutas relativas a la raíz del proyecto. `.yas/brand/` es la carpeta de salida por defecto del manual; si el usuario eligió otra, su ruta está en `.yas/brand-source.json` (`manualPath`) y todas las skills la usan.

| Artefacto | Ruta | Lo produce | Lo consumen |
|---|---|---|---|
| Especificación y registro de decisiones | `.yas/brand/marca-spec.md` | `/yas-design` | `/yas-audit` (criterio), `/yas-figma` |
| Paleta de marca | `.yas/brand/paleta/paleta.md` | `/yas-design` (fase 6) | `/yas-figma colors`, `/yas-audit` |
| Sistema tipográfico | `.yas/brand/tipografia/sistema-tipografico.md` | `/yas-design` (fase 7) | `/yas-figma`, `/yas-audit` |
| Logo y variantes | `.yas/brand/logo/*.svg` | `/yas-design` (fases 5 y 8) | `/yas-figma` (Brand assets), `/yas-audit` |
| Manual de identidad | `.yas/brand/manual/manual-identidad.{md,html}` | `/yas-design` (fase 10) | `/yas-figma` (fuente de datos), `/yas-audit` |
| Origen de datos de marca | `.yas/brand-source.json` | `/yas-figma` | `/yas-design`, `/yas-audit` |
| **Tokens de diseño** | `.yas/tokens/tokens.json` (formato DTCG) | `/yas-figma` (`colors`, `push`, `document manual`) | `/yas-figma` |
| Informe de contraste | `.yas/tokens/contraste.md` | Quien genere los tokens semánticos | `/yas-audit` |
| Registro de cambios de tokens | `.yas/tokens/CHANGELOG.md` | Quien modifique los tokens | Las tres |
| Estado de Figma | `.yas/figma-state.json` | `/yas-figma` | `/yas-figma` |
| Lectura de Figma | `.yas/figma-snapshot.json` | `/yas-figma document` | `/yas-figma` |
| Paquete local de Figma y HTML | `.yas/figma-local/` | `/yas-figma` | `/yas-figma` |
| Informes de auditoría | `.yas/audits/AAAA-MM-DD-marca.md` | `/yas-audit` | `/yas-design` (para corregir) |

## Reglas de compartición

- **Una fuente de verdad por dato.** El color vive en la paleta y en los tokens; la tipografía, en su sistema y en los tokens; los nombres de archivo del logo, en `yas-design/references/construccion-logo.md`. Los demás archivos enlazan, no copian.
- **Leer antes de producir.** Antes de crear un artefacto, comprueba si ya existe. Si existe, léelo y complétalo; no lo regeneres de cero ni lo sobrescribas (regla de Protección de `reglas-comunes.md`).
- **Producir cuando falta.** Si una skill necesita un artefacto que otra produciría y no existe (por ejemplo, tokens de color antes de que se ejecute `/yas-figma push`), puede crearlo siguiendo la especificación común, y lo registra en el `CHANGELOG.md` del artefacto. Después, la otra skill lo completa sin reescribirlo.
- **Cabecera de origen.** Todo artefacto generado lleva fecha, skill y subcomando que lo produjo, y de qué fuente salió (por ejemplo, "desde `paleta/paleta.md`").
- **Cambios con registro.** Cualquier cambio en `tokens.json` se anota en `.yas/tokens/CHANGELOG.md` con fecha, qué cambió y por qué.
- **Divergencias.** Si dos artefactos se contradicen (la paleta dice un HEX y los tokens otro), no se resuelve en silencio: se señala, prevalece lo aprobado en `marca-spec.md` y se registra el conflicto.
- **Lo generado se regenera.** Los archivos derivados (paquete local, HTML) se vuelven a generar desde su fuente; no se editan a mano.

## Contrato de la paleta (lectura por máquina)

Para que `/yas-figma colors` pueda leer la paleta sin interpretar prosa, `paleta/paleta.md` incluye siempre una tabla con estas columnas, en este orden:

| Nombre | Rol | HEX | RGB | CMYK (referencia) | Pantone (aproximado) |
|---|---|---|---|---|---|

- **Rol:** `principal`, `apoyo`, `neutro` u otro aprobado.
- Los valores que no consten van como *pendiente de definir*, no se inventan (ver las reglas de valores de color de `yas-design/SKILL.md`).
- Si la paleta llega solo en un manual PDF o imagen, `/yas-figma` extrae los valores y los registra en `.yas/brand-source.json` como `extracted`, `inferred` o `missing`.
