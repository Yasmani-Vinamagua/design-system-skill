# Registro de cambios

## Sin publicar

### Añadido
- `/yas-design` genera ahora una **vista de opciones** en HTML antes de pedir una decisión, para poder ver lo que se elige:
  - Fase 3: `concepto/opciones.html` (los tres conceptos con un esquema de cada uno).
  - Fase 4: `logo/exploracion/opciones.html` (los tres candidatos y los bocetos descartados, en grande y a tamaño reducido).
  - Fase 7: `tipografia/opciones.html` (las finalistas con el nombre y el logo de la marca, alfabeto, texto corrido y jerarquía).
- Las exploraciones de paleta de la Fase 6 se guardan en `paleta/exploracion/`.

### Cambiado
- Regla común nueva en `yas-core`: todo lo que el usuario deba ver se anuncia con su **ruta completa** en el resumen de cierre, y antes de pedir la decisión si depende de ello. Aplicado en `/yas-design` (Fases 3 a 10) y en el cierre de `/yas-figma push`.
- Los archivos generados se enlazan en cada resumen de cierre como **enlaces clicables con ruta absoluta** (`file:///...`), en todas las fases y en las tres skills; ya no se nombran solo por su nombre.
- Cuando se pide una decisión con la herramienta de preguntas, la ruta absoluta del archivo con las opciones va **dentro de la pregunta**, también en rebranding. Fase 5: `logo/comparacion.html` para decidir entre variantes (por ejemplo el lockup).
- La excepción a «las propuestas conceptuales no se convierten en código» incluye ahora estas vistas de opciones.
- README: nueva sección «Actualizar» (`npx skills update`).

## Primeras versiones
- Reorganización de `/yas-figma`, corrección de la instalación con `npx` y licencia MIT.
- Primera versión de Yas Design System.
