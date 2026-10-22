# Registro de cambios

## Sin publicar

### Añadido
- `/yas-design` genera ahora una **vista de opciones** en HTML antes de pedir una decisión, para poder ver lo que se elige:
  - Fase 3: `concepto/opciones.html` (los tres conceptos con un esquema de cada uno).
  - Fase 4: `logo/exploracion/opciones.html` (los tres candidatos y los bocetos descartados, en grande y a tamaño reducido).
  - Fase 7: `tipografia/opciones.html` (las finalistas con el nombre y el logo de la marca, alfabeto, texto corrido y jerarquía).
- Las exploraciones de paleta de la Fase 6 se guardan en `paleta/exploracion/`.
- `/yas-design`: **Fase 8b — Iconografía**. Define estilo, cuadrícula, tamaños, color y nombres, y crea el set base en SVG con `iconografia/iconografia.md`, `iconografia/iconos/*.svg` y `iconografia/vista-previa.html`. El manual (sección 10) y `/yas-figma` (Icons e «Iconos derivados») la usan como fuente.
- `/yas-figma`: sección «Presupuesto de lecturas» (comprobar y verificar dentro de `use_figma`) y opción de usar un archivo en Drafts ante el límite de páginas.

### Cambiado
- `/yas-figma`, «Presupuesto de lecturas»: corregida la contradicción sobre `use_figma`. Cuenta cuota en cada llamada (lee y escribe); solo las herramientas que únicamente escriben quedan fuera. El ahorro pasa por agrupar más trabajo por llamada y no hacer llamadas solo de comprobación.
- Regla común nueva en `yas-core`: todo lo que el usuario deba ver se anuncia con su **ruta completa** en el resumen de cierre, y antes de pedir la decisión si depende de ello. Aplicado en `/yas-design` (Fases 3 a 10) y en el cierre de `/yas-figma push`.
- Los archivos generados se enlazan en cada resumen de cierre como **enlaces clicables con ruta absoluta** (`file:///...`), en todas las fases y en las tres skills; ya no se nombran solo por su nombre.
- Cuando se pide una decisión con la herramienta de preguntas, la ruta absoluta del archivo con las opciones va **dentro de la pregunta**, también en rebranding. Fase 5: `logo/comparacion.html` para decidir entre variantes (por ejemplo el lockup).
- La excepción a «las propuestas conceptuales no se convierten en código» incluye ahora estas vistas de opciones.
- README: nueva sección «Actualizar» (`npx skills update`).
- `/yas-figma`: el archivo destino sigue un orden de prioridad (URL del usuario, estado, Drafts) y ya no se crean archivos por cuenta propia; acepta cualquier prefijo del MCP; `whoami` se usa una vez y no se deduce el límite de páginas del plan; `push` ya no exige cuota; `documentation figma` extrae todo con una sola llamada de solo lectura a `use_figma`, con capturas y Code Connect opcionales; `colors` verifica con lo que devuelve `use_figma`.

## Primeras versiones
- Reorganización de `/yas-figma`, corrección de la instalación con `npx` y licencia MIT.
- Primera versión de Yas Design System.
