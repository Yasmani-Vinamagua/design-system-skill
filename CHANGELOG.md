# Registro de cambios

## Sin publicar

### Añadido
- `/yas-design` genera ahora una **vista de opciones** en HTML antes de pedir una decisión, para poder ver lo que se elige:
  - Fase 3: `concepto/opciones.html` (los tres conceptos con un esquema de cada uno).
  - Fase 4: `logo/exploracion/opciones.html` (los tres candidatos y los bocetos descartados, en grande y a tamaño reducido).
  - Fase 7: `tipografia/opciones.html` (las finalistas con el nombre y el logo de la marca, alfabeto, texto corrido y jerarquía).
- Las exploraciones de paleta de la Fase 6 se guardan en `paleta/exploracion/`.
- `/yas-design`: **Fase 8b — Iconografía**. Define estilo, cuadrícula, tamaños, color y nombres, y crea el set base en SVG con `iconografia/iconografia.md`, `iconografia/iconos/*.svg` y `iconografia/vista-previa.html`. El manual (sección 10) y `/yas-figma` (Icons e «Iconos derivados») la usan como fuente.
- `/yas-design`, `construccion-logo.md`: nuevas subsecciones de **geometría** (primitivas, ángulos enteros, retícula al final) y **correcciones ópticas** (sobrepaso, efecto hueso, igualar tamaño visual, horizontales y verticales, centro óptico, irradiación), además de convenciones de escritura del SVG (lienzo, trazados, espacio negativo, trazos, color y tipografía). Tres pruebas nuevas en la sección 5: correcciones ópticas, versión invertida y lecturas no intencionadas.
- `/yas-design`, `proceso.md`: criterios de carácter de la forma y revisión con ojos frescos en la Fase 4; en la Fase 0b, motivo del cambio, equidad de marca y fusiones; técnicas de refresco en la Fase 5 y lanzamiento (antes y después, coste, revisión posterior) en la Fase 10b.
- `/yas-audit`: primera impresión y correcciones ópticas en el módulo de identidad visual, ocho antipatrones nuevos y notas sobre defectos fatales, motivo del rediseño y hallazgos accionables.
- `/yas-figma`: sección «Presupuesto de lecturas» (comprobar y verificar dentro de `use_figma`) y opción de usar un archivo en Drafts ante el límite de páginas.

- **Material Design 2, sistema de color** como referencia externa y base de ampliaciones en `tokens-spec.md`: `surface.background`, `accent.*` (opcional, con alias al color principal si no hay apoyo), `control.{selected,track,progress}` y `chart.categorical.*` (opcional), con sus reglas de derivación y contraste.

- **Adobe Spectrum, design tokens** como referencia externa y base de ampliaciones en `tokens-spec.md`: nivel opcional de **tokens de componente** (`component.<nombre>.*`, solo en `full`), regla de **orden de segmentos** de general a específico, y espaciado semántico opcional (`space.inset.*`, `space.gap.*`) como alias de la escala.

- `/yas-figma` incorpora los tokens nuevos de `tokens-spec.md`: `surface.background`, `accent.*`, `control.*` y `chart.categorical.*` en `colors` y en las semánticas de color; `space.inset/gap` y `component.*` (solo `full`) en el alcance y las variables.

- **Figma, variables, colecciones y modos** como referencia externa: `tokens-spec.md` incorpora la sección «Tokens y variables de Figma» (tipo de variable por categoría, sombras y easing fuera de las variables, alias solo del mismo tipo, redondeo a dos decimales, estilos frente a variables y límite de modos por plan), y `/yas-figma` la aplica y comprueba el plan antes de crear un tercer modo.

- **Atomic Design (Brad Frost)** como referencia externa y base de varias mejoras:
  - `/yas-figma full`: nivel atómico de cada componente (sin cambiar las 28 páginas), ficha de documentación (compuesto por / usado en, contenido extremo, ciclo de vida) y sección de gobernanza y versionado.
  - `/yas-audit`, módulo Sistema de marca: inventario de patrones, gobernanza y tres antipatrones nuevos.
  - `/yas-design`: test de 20 segundos en la Fase 1 y style tile con collage de elementos en la Fase 9, ambos opcionales.

- ***Design Systems Handbook* (InVision, 2017)** como referencia externa y base de mejoras:
  - `tokens-spec.md`: reglas de escalas (base 16 px, escala modular, interlineado 1,5, espaciado en base 4, máximo dos familias).
  - `criterios-calidad.md`: lista de principios del sistema y accesibilidad por componente (teclado, lector de pantalla, etiquetas, alternativas, contraste).
  - `/yas-figma full`: modelo de equipo, versionado semántico y definición de cambio incompatible en la gobernanza; buscador y navegación plana en el HTML; accesibilidad y principios en la ficha de cada componente.
  - `/yas-audit`: inventario visual de atributos (Consistencia), principios del sistema y dos antipatrones nuevos (Sistema de marca).
  - `/yas-design`: inventario visual de atributos en la Fase 0b de rebranding.

- **Checklist de sistema de diseño** (aportado por el usuario) en `yas-core/references/checklist-sistema-diseno.md`:
  - Fundamentos, requisitos específicos de los componentes base (botón, campo, modal…) y componentes opcionales para `Components - App`.
  - `/yas-figma full`: la ficha de cada componente incluye sus requisitos del checklist; los iconos se nombran por función y hay iconos reservados (también en la Fase 8b de `/yas-design`).
  - `tokens-spec.md`: sección de elevación (un token de superficie por nivel de sombra, clave en modo oscuro), tipografía adaptable, legibilidad y fuentes de respaldo.
  - `/yas-audit`: control de cobertura del checklist en el módulo Sistema de marca.
  - Quedan fuera el lenguaje de diseño (visión, tono, terminología) y el mantenimiento.

### Cambiado
- `/yas-figma`, «Presupuesto de lecturas»: corregida la contradicción sobre `use_figma`. Cuenta cuota en cada llamada (lee y escribe); solo las herramientas que únicamente escriben quedan fuera. El ahorro pasa por agrupar más trabajo por llamada y no hacer llamadas solo de comprobación.
- Regla común nueva en `yas-core`: todo lo que el usuario deba ver se anuncia con su **ruta completa** en el resumen de cierre, y antes de pedir la decisión si depende de ello. Aplicado en `/yas-design` (Fases 3 a 10) y en el cierre de `/yas-figma push`.
- Los archivos generados se enlazan en cada resumen de cierre como **enlaces clicables con ruta absoluta** (`file:///...`), en todas las fases y en las tres skills; ya no se nombran solo por su nombre.
- Cuando se pide una decisión con la herramienta de preguntas, la ruta absoluta del archivo con las opciones va **dentro de la pregunta**, también en rebranding. Fase 5: `logo/comparacion.html` para decidir entre variantes (por ejemplo el lockup).
- La excepción a «las propuestas conceptuales no se convierten en código» incluye ahora estas vistas de opciones.
- README: nueva sección «Actualizar» (`npx skills update`).
- README (español e inglés): fases 4 y 5, rebranding y auditoría reflejan las técnicas visuales y de refresco.
- `/yas-figma`: el archivo destino sigue un orden de prioridad (URL del usuario, estado, Drafts) y ya no se crean archivos por cuenta propia; acepta cualquier prefijo del MCP; `whoami` se usa una vez y no se deduce el límite de páginas del plan; `push` ya no exige cuota; `documentation figma` extrae todo con una sola llamada de solo lectura a `use_figma`, con capturas y Code Connect opcionales; `colors` verifica con lo que devuelve `use_figma`.

## Primeras versiones
- Reorganización de `/yas-figma`, corrección de la instalación con `npx` y licencia MIT.
- Primera versión de Yas Design System.
