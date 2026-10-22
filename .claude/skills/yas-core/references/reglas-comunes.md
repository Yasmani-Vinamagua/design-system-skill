# Reglas comunes obligatorias

Se aplican a **todas** las skills de Yas Design (`/yas-design`, `/yas-audit`, `/yas-figma`) y a todos sus subcomandos. Cada `SKILL.md` remite a este documento y solo añade su regla de alcance concreta; esta es la fuente única, así que no se repiten ni se reescriben en otro sitio.

## Reglas

| Regla | Comportamiento esperado |
|---|---|
| **Inspección inicial** | Revisar archivos, estructura y tecnologías existentes antes de actuar. |
| **Contexto** | Identificar el proyecto y sus restricciones antes de intervenir. |
| **Ejecución** | Resolver la tarea solicitada sin activar procesos innecesarios. |
| **Archivos** | Crear o modificar archivos reales cuando la tarea lo requiera. |
| **Protección** | No sobrescribir archivos existentes sin comprobar su función. |
| **Calidad** | Validar los resultados con las herramientas disponibles. |
| **Documentación** | Registrar decisiones, instrucciones de uso y cambios relevantes. |
| **Transparencia** | Informar qué se generó, qué se verificó y qué quedó pendiente. |

## Qué significa cada regla en Yas Design

### Inspección inicial
- Antes de proponer o escribir nada, mira lo que hay: carpeta del proyecto, `.yas/` (brief, `marca-spec.md`, manual, tokens, informes), código, framework y forma de estilar (CSS, Tailwind, componentes), archivos adjuntos y enlaces.
- Usa las herramientas de lectura y búsqueda (Glob, Grep, Read); no supongas lo que puedes comprobar. Mira de verdad las imágenes, los PDF y los SVG.

### Contexto
- Identifica qué proyecto es, su plataforma (web, Android, Apple, multiplataforma), su público y sus restricciones: licencias, plazos, plan y límites de Figma, disponibilidad del MCP, convenciones del repositorio.
- Si falta algo imprescindible, pregunta solo lo mínimo y **agrupa las preguntas en una sola interacción**. Si puedes inferirlo, infiérelo y declara la suposición.

### Ejecución
- Haz lo que se pidió, y nada más: sin lanzar procesos, subagentes, auditorías, generación de variantes o exportaciones que la tarea no necesita.
- El siguiente paso útil se **ofrece**, no se ejecuta por iniciativa propia (por ejemplo, ofrecer `/yas-audit` tras un diseño, o `/yas-figma push` tras generar el design system).

### Archivos
- Cuando la tarea produce algo, entrega archivos reales en el proyecto (Markdown, SVG, HTML, JSON de tokens), no solo texto en pantalla. Por defecto van en `.yas/` salvo que el usuario indique otra carpeta.
- Usa nombres descriptivos y rutas previsibles, respeta las convenciones que el proyecto ya tenga e indica la ruta de cada archivo al terminar.
- **Todo lo que el usuario deba ver** (vistas de opciones, bocetos, vistas previas, mockups, HTML de entrega, manual) se anuncia con su **ruta completa** en el resumen de cierre del paso que lo genera, y **antes de pedir una decisión** si de él depende. No basta con describirlo en el chat: si hay un archivo para mirar, di dónde está y cómo abrirlo (doble clic en el navegador para HTML; abrir con el navegador o un editor de imágenes para SVG).
- **Formato de la ruta: enlace clicable con la ruta absoluta.** Nunca nombres un archivo solo por su nombre («opciones.html y paleta.md»). Escríbelo como enlace Markdown cuyo destino es la ruta absoluta del archivo con esquema `file:///`, barras `/` y los espacios como `%20`, y cuyo texto es la ruta relativa al proyecto: `[.yas/brand/paleta/paleta.md](file:///C:/Users/ana/proyecto/.yas/brand/paleta/paleta.md)`. En macOS o Linux: `file:///home/ana/proyecto/...`. Obtén la ruta absoluta del directorio de trabajo real; no la inventes ni la dejes relativa. Si el entorno no hace clicable el enlace, el texto con la ruta relativa sigue permitiendo encontrar el archivo. Para una carpeta, enlaza la carpeta.
- Esto vale para **todas las fases y todos los subcomandos** de las tres skills, también para los resúmenes cortos de una línea: si el resumen menciona un archivo que el usuario puede abrir, lo enlaza así.

### Protección
- **Antes de modificar o reemplazar un archivo existente, léelo y comprueba qué función cumple.** Un archivo que no sabes qué hace no se sobrescribe.
- No elimines nada sin autorización. Si hay riesgo de pisar contenido, trabaja sobre una copia o pide confirmación y di qué se perdería.
- Distingue los archivos generados (por ejemplo, el HTML y el paquete local de `/yas-figma`) de los editados a mano: los primeros se regeneran desde su fuente; los segundos no se pisan.
- En un rebranding o una importación a Figma, no reemplaces activos existentes hasta que el alcance esté aprobado.

### Calidad
- Valida el resultado con lo que haya disponible en el entorno: renderizar el SVG o el HTML, comprobar que el XML y el JSON son válidos, abrir los archivos generados, calcular contrastes con la fórmula WCAG, ejecutar el lint, la compilación o las pruebas si existen, leer de vuelta lo creado en Figma.
- **No declares validado lo que no ejecutaste.** Si el entorno no permite una comprobación (por ejemplo, no se puede renderizar la interfaz), dilo y no afirmes validación visual.

### Documentación
- Registra las decisiones con su motivo y quién las aprobó (en el registro de decisiones de `marca-spec.md` o el equivalente del proyecto), las instrucciones de uso de lo entregado y los cambios relevantes (registro de cambios con versión y fecha cuando corresponda).
- Documenta lo que otra persona necesitaría para continuar sin tener que adivinar.

### Transparencia
- Al terminar, informa en pocas líneas de tres cosas: **qué se generó** (cada archivo como enlace clicable con su ruta, según el formato de «Archivos»), **qué se verificó** (y cómo) y **qué quedó pendiente** (incluidas limitaciones y aprobaciones sin resolver).
- Usa el vocabulario de estados de cada skill: pruebas *verificada*, *fallida*, *no aplicable*, *no verificada*; datos *verificado*, *no verificado*, *pendiente de definir*; hallazgos de auditoría *comprobado*, *hipótesis*, *no verificado*.
- No declares terminado un trabajo con aprobaciones o validaciones importantes sin resolver.

## Regla de alcance

**Haz el tipo de trabajo que se pidió y no pases al siguiente sin que forme parte de lo solicitado.** Un diagnóstico no se convierte en rediseño, y una propuesta no se convierte en implementación.

| Si el usuario pide… | Debe hacer | No debe hacer |
|---|---|---|
| **Una auditoría** (`/yas-audit`) | Diagnosticar, puntuar y recomendar | Rediseñar ni corregir; las correcciones se recomiendan como comandos |
| **Una propuesta conceptual** (marca, concepto, UX, estructura de pantallas, dirección visual) | Proponer, justificar y presentar para aprobación | Implementar código sin que forme parte de lo solicitado |
| **Diseñar o construir** (`/yas-design`) | Ejecutar el subcomando pedido, fase a fase y con aprobación | Auditar, exportar a Figma o añadir entregables que no pidió, salvo ofrecerlos |
| **Llevar el sistema a Figma o documentarlo** (`/yas-figma`) | Mover lo existente entre el proyecto y Figma, o documentarlo | Decidir diseño de marca nuevo ni criticarlo; `documentation figma` es de solo lectura |

Reglas de aplicación:
- Si la petición es ambigua entre analizar y ejecutar (por ejemplo, "revisa y mejora la interfaz"), **pregunta** cuál de las dos quiere antes de empezar. Si pide ambas cosas explícitamente ("audita y corrige"), haz primero la auditoría, presenta el resultado y pide aprobación antes de pasar a corregir.
- Una instrucción explícita del usuario sobre el alcance prevalece sobre esta tabla.
- Los subcomandos que por naturaleza producen archivos (por ejemplo, `/yas-figma colors`, que genera los tokens de color y sus variables) no se consideran "implementar código no solicitado": generar esos archivos **es** lo solicitado.
