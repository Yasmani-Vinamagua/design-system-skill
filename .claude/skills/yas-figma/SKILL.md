---
name: yas-figma
description: "Genera el design system de una marca a partir de su manual de identidad y lo lleva a Figma. Comandos mini (solo fundamentos) y full (sistema completo) crean el sistema en Figma, o en local con un HTML entregable si no hay MCP de Figma o cuota; push carga a Figma un sistema ya generado; documentation genera el HTML del design system a partir de un archivo de Figma o de un manual de identidad; colors convierte la paleta en variables semánticas. Úsala cuando el usuario pida crear el design system o sus variables en Figma, cargarlo a Figma o documentarlo como entregable."
argument-hint: "[mini | full | push | documentation | colors] [figma | manual] [URL de Figma | ruta]"
---

# Yas Figma

Responsabilidad: **generar el design system a partir del manual de identidad y moverlo entre el proyecto y Figma**. No decide el diseño de la marca (eso es `/yas-design`) ni audita la marca (eso es `/yas-audit`).

## Reglas obligatorias

Antes de actuar, lee `../yas-core/references/reglas-comunes.md`: inspección inicial, contexto, ejecución, archivos, protección, calidad, documentación, transparencia y regla de alcance. Valen para todos los comandos y no se repiten aquí.

**Alcance de esta skill:** convierte en design system lo que el manual ya define, y lo mueve o documenta. No decide diseño de marca nuevo ni audita la marca (eso es de `/yas-design` y `/yas-audit`), y `documentation figma` es de solo lectura. Las reglas de protección aplican a Figma: no se sobrescribe ni se elimina contenido existente del archivo sin comprobar su función y pedir confirmación.

## Comandos

| Comando | Qué hace | Necesita MCP de Figma |
|---|---|---|
| `/yas-figma mini` | Genera el **Mini Design System** (solo fundamentos, 9 páginas) | Opcional: sin MCP lo genera en local |
| `/yas-figma full` | Genera el **Full Design System** (fundamentos, componentes, patrones y plantillas, 28 páginas) | Opcional: sin MCP lo genera en local |
| `/yas-figma push` | **Carga a Figma un design system ya generado** anteriormente (por `mini` o `full`) | Sí |
| `/yas-figma documentation` | Genera el **HTML del design system** a partir de un archivo de Figma (`figma`) o de un manual de identidad (`manual`) | `figma`: sí (solo lectura). `manual`: no |
| `/yas-figma colors` | Convierte la paleta de la marca en tokens de color y variables semánticas (claro y oscuro) | Opcional: sin MCP genera los tokens y los archivos para crearlas a mano |

`document` se acepta como sinónimo de `documentation`.

Sin argumento, pregunta con AskUserQuestion qué se quiere hacer: `mini` o `full` si no hay sistema generado todavía (recomendando mini para un MVP, prototipo o marca nueva sin código, y full si ya hay producto o varios equipos), `push` si ya hay uno generado, o `documentation`.

Si el usuario pide otra cosa (importar de Figma al código, sincronizar Figma con el código, Code Connect, llevar pantallas del código a Figma), dile con claridad que **no está implementado** y ofrece lo disponible. No improvises su comportamiento.

## Fuente de datos: el manual de identidad

Los valores de `Colors`, `Typography`, `Brand assets`, `Icons`, etc. **no se inventan ni se eligen aquí**: salen del manual de identidad de la marca. Localízalo en este orden y usa el primero que exista:

1. **Material que adjunta el usuario** (PDF, HTML, Markdown, imágenes, SVG, enlace). Tiene prioridad sobre lo generado, porque es la intención explícita más reciente.
2. **Manual generado por `/yas-design`** y su salida en `.yas/` (incluidos `.yas/tokens/` si ya existen). Busca el manual de identidad y los assets en esa carpeta antes de decir que no hay nada.
3. **Ninguno de los dos:** detente y pide al usuario que adjunte el manual o ejecute antes `/yas-design`. No generes un sistema con colores o fuentes de relleno.

Extracción:
- Lee el material de verdad (Read para PDF e imágenes, WebFetch para URL) y extrae: paleta con nombres, valores (HEX, y RGB/CMYK/Pantone si constan) y roles; familias tipográficas, pesos y escala; logotipo y versiones; estilo de iconos e imágenes; reglas de espaciado, forma o movimiento si existen.
- Registra el origen en `.yas/brand-source.json`: archivo o URL usados y, por cada dato, `extracted` (consta en el manual), `inferred` (deducido, con la razón) o `missing` (no consta).
- **Antes de marcar algo como `missing`, intenta derivarlo** de lo que el manual sí define (paleta, logotipo, formas, tipografía). Lo derivable es `inferred` y se **propone con valor**, no se deja "pendiente": estados de acción (`hover`, `pressed`, `disabled`, `action.secondary`), roles de iconos (`icon.*`), `feedback.*` (éxito, aviso, error, info), enlace y foco (reglas en `tokens-spec.md`), y la especificación del set de iconos (ver "Iconos derivados").
- Lo `inferred` se muestra al usuario para confirmar antes de construir. Solo es `missing` lo que no se puede derivar de nada del manual (por ejemplo, el nombre de un archivo de iconos o un Pantone); aparece como "pendiente" en Figma y en el HTML, nunca con un valor inventado. Ejemplo: si el manual no define escala de espaciado, se propone una (base 4 u 8) y se marca como propuesta.
- Si el adjunto y lo generado por `/yas-design` se contradicen, usa el adjunto, indica las diferencias y pregunta antes de sobrescribir `.yas/tokens/`.
- Si una fuente tipográfica del manual no está disponible en Figma, avísalo y propón la alternativa más cercana sin sustituirla en silencio.

Los archivos que esta skill lee y escribe, y quién es dueño de cada uno, están en `../yas-core/references/artefactos.md`; los tokens siguen `../yas-core/references/tokens-spec.md`; los umbrales de calidad, `../yas-core/references/criterios-calidad.md`. Se leen, no se copian.

## Tokens (los comparten `mini`, `full` y `documentation manual`)

Comprueba qué hay en `.yas/tokens/tokens.json`:
- **Existe y cubre el alcance:** úsalo tal cual.
- **No existe o está incompleto:** derívalo del manual (según "Fuente de datos") con las categorías del alcance (mini: color, tipografía, espaciado, radios, sombras y cuadrículas; full: además bordes, movimiento, breakpoints y capas), siguiendo `../yas-core/references/tokens-spec.md`. Para `color.*` aplica el mismo procedimiento que `colors` (incluidos el informe de contraste y el registro de cambios); si `colors` ya se ejecutó, reutiliza lo que generó.
- **Propuestas:** las escalas derivadas y los valores que el manual no define (por ejemplo, la escala de espaciado, los estados de acción como `action.primary.hover` o los iconos, que se derivan de la paleta según `tokens-spec.md`) se marcan como *propuesta* y se **muestran al usuario para aprobar antes de crearlos en Figma**.
- **Fusión:** si el archivo ya existe, fusiona lo que falta sin reescribir lo existente ni contradecir la paleta aprobada (regla de Protección), y anota el cambio en `.yas/tokens/CHANGELOG.md`.

## Iconos derivados

Si existe `iconografia/iconografia.md` (Fase 8b de `/yas-design`), es la fuente: se usa tal cual, con sus iconos SVG. Si el manual no define un set de iconos, no se deja la sección vacía: se propone la **especificación** a partir del manual, marcada *propuesta*:
- **Tamaños:** 16, 20 y 24 px (cuadrícula base de 24 con margen de 2 px).
- **Trazo:** grosor tomado del trazo o del peso del logotipo si lo hay; si no, 1.5 px a 24 px, escalado proporcional.
- **Esquinas y terminales:** redondeadas o rectas según el radio y la forma del logotipo y de `radius.*`.
- **Color:** tokens `icon.*` de `tokens-spec.md`.
- **Nombres:** `icon/<categoría>/<nombre>` en minúsculas con guion.
Los iconos concretos (dibujos) solo se crean si el proyecto los usa o los pide; la especificación sí se entrega siempre.

## Qué genera cada alcance

| | **Mini** | **Full** |
|---|---|---|
| Objetivo | Base mínima y coherente para empezar a diseñar ya | Sistema completo, escalable y documentado |
| Contenido | **Solo fundamentos**, en 9 páginas (ver abajo). Sin componentes | Fundamentos, componentes, patrones y plantillas, en 28 páginas (ver abajo) |
| Variables | Color (primitivas + semánticas claro/oscuro), tipografía, espaciado y layout, radios | Todo lo de mini + bordes, opacidad, z-index, movimiento (duración y easing), breakpoints, densidad |
| Estilos | Escala de texto, estilos de efecto (sombras) y estilos de cuadrícula | Escala completa, efectos, cuadrículas y estilos de capa |
| Componentes | No incluidos | Los 16 componentes base, los componentes de la app, patrones y plantillas |
| Variantes y estados | No aplica | Matriz completa de variantes, tamaños y estados, con propiedades de componente y *slots* |
| Marca | Páginas de brand assets (logos, versiones, símbolos) e iconos | Brand assets + librería de iconos ampliada, con guías de uso |
| Documentación en Figma | Portada y una página por fundamento | Portada, principios, fundamentos, guías de uso por componente, changelog |
| Accesibilidad | Contraste AA verificado en los pares de color | AA verificado + guías de foco, teclado y anotaciones |
| Esfuerzo (MCP) | Bajo; cabe en pocas llamadas | Alto; se construye por fases y con estado reanudable |

### Estructura de páginas del Mini Design System

El mini genera exactamente estas páginas en Figma, en este orden. No se crean páginas vacías ni separadores: todas las páginas llevan contenido.

```
Cover
Icons
Brand assets
Colors
Type scale
Spacing and layout
Radios
Shadows
Grids
```

| Página | Contenido |
|---|---|
| Cover | Nombre del sistema, versión, fecha, descripción breve y estado. |
| Icons | Set de iconos del proyecto con convención de nombres, cuadrícula base y tamaños (por ejemplo 16, 20, 24), como componentes o vectores nombrados. Solo los iconos que el proyecto use o defina. Si el manual no define set, se muestra la **especificación derivada** (ver "Iconos derivados") como *propuesta*, no un marcador vacío. |
| Brand assets | Logotipo y sus versiones (principal, secundaria, símbolo, una tinta, negativa), zona de seguridad y tamaño mínimo. Solo con assets que existan en el proyecto; si faltan, marcador "pendiente". |
| Colors | Primitivas y semánticas (claro/oscuro) como muestras enlazadas a variables, con ratio de contraste de los pares de texto/fondo. |
| Type scale | Escala tipográfica con fuente, tamaño, peso e interlineado, como estilos de texto. |
| Spacing and layout | Escala de espaciado, márgenes y principios de layout, enlazados a variables. |
| Radios | Escala de radios de esquina enlazada a variables. |
| Shadows | Niveles de elevación como estilos de efecto. |
| Grids | Cuadrículas por breakpoint (columnas, gutter, margen) como estilos de cuadrícula. |

### Estructura de páginas del Full Design System

El full genera estas 28 páginas en Figma, en este orden. Las líneas separadoras y los títulos `Foundations` y `Components` de la especificación original son **solo indicadores de sección**: no se crean como páginas, ni vacías ni con guiones.

```
Cover

Brand
Color
Iconography
Images
Layout and spacing
Shadows and effects
Typography
Motion

Buttons
Badge
Check
Help text
Inputs
Segmented controls
Search bar
Progress bar
Tag
Text area
Toggle
Tooltip
Accordion
Avatar
Banner
Card

Components - App

Patterns

Templates and applications
```

Cada línea del bloque es una página; las líneas en blanco solo agrupan visualmente Foundations, Components, App, Patterns y Templates.

Las páginas con subsecciones las llevan **dentro de la página**, como marcos o secciones de Figma con estos nombres, no como páginas aparte:

| Página | Secciones internas |
|---|---|
| Color | Documentation, Variables, Semantic variables |
| Iconography | Documentation, Iconography |
| Layout and spacing | Documentation, Layout, Spacing |
| Shadows and effects | Documentation, Shadows and effects |
| Typography | Documentation, Typography scale |
| Accordion | Documentation, Accordion items, Accordion bases |

La página `Check` agrupa toda la familia de selección, cada una como sección con sus variantes y estados: **Checkbox** (sin marcar, marcado, indeterminado), **Check list** (lista de checkboxes con etiqueta y texto de apoyo), **Radio** y **Radio group**. El `Toggle` queda en su propia página. Si el proyecto necesita otra variante de selección (por ejemplo, tarjetas seleccionables), se añade como sección de esta página.

Las demás páginas de componentes siguen la misma lógica: una sección `Documentation` (uso, anatomía, cuándo sí y cuándo no, fuente M3/HIG) y la sección con los componentes y sus variantes. Corrige el error de escritura de la especificación: la página es `Inputs`, no `imputs`.

Cada página de contenido de Foundations enlaza sus valores a variables; `Components - App` reúne los componentes específicos de la aplicación (compuestos a partir de los base), `Patterns` las composiciones recurrentes (formularios, listas, navegación, estados vacíos y de error) y `Templates and applications` las pantallas completas.

### Reglas entre alcances

- El alcance se guarda en `.yas/figma-state.json` (`"scope": "mini" | "full"`) y el HTML entregable lo declara en la portada.
- **Mini es un subconjunto de full** y se puede **ampliar de mini a full** sin rehacer contenido: `/yas-figma full` completa lo que falta y respeta lo existente. Como los nombres de página difieren, al ampliar renombra las páginas del mini (con confirmación previa) y reubica su contenido: `Icons` → `Iconography`, `Brand assets` → `Brand`, `Colors` → `Color`, `Type scale` → `Typography`, `Spacing and layout` → `Layout and spacing`, `Shadows` → `Shadows and effects`. `Radios` y `Grids` no tienen página en full: pasan como secciones a `Layout and spacing`.
- Pasar de full a mini no borra nada: avisa y pide confirmación antes de eliminar.
- El alcance también define el paquete local y el HTML: en mini solo aparecen las secciones y componentes del alcance; el resto se marca como "fuera de alcance (full)".

## Paquete local y HTML entregable

El **paquete local** vive en `.yas/figma-local/` y lo producen `mini` y `full`. Es el "design system ya generado" que luego carga `push`:

| Archivo | Contenido |
|---|---|
| `design-system.html` | **Entregable visual**: el sistema de diseño navegable como documento de entrega (ver abajo). |
| `LEEME.md` | Orden de implementación paso a paso en Figma, con checklist. |
| `variables.md` | Colecciones y modos (Primitivas, Semánticas, Claro/Oscuro) con nombre, tipo y valor, listos para crear en el panel de Variables. |
| `variables.json` | Mismo contenido en JSON, importable con plugins de tokens (formato DTCG). |
| `estilos.md` | Estilos de texto, efectos y cuadrículas. |
| `componentes.md` | **Solo en alcance full** (el mini no tiene componentes y no lo genera). Por componente: anatomía, variantes, propiedades, estados, auto layout, variables enlazadas. |
| `nomenclatura.md` | Convención de nombres de capas, páginas y variantes. |

### Especificación del HTML del design system

Un solo archivo autocontenido (CSS y JS inline, sin dependencias externas salvo fuentes del proyecto), que se abre con doble clic y se puede enviar a un cliente o equipo. Debe leerse como un entregable profesional, no como un volcado de datos. Lo usan `design-system.html` (paquete local) y el HTML de `documentation manual`:

- **Portada:** nombre del sistema, versión, fecha, alcance y origen de los datos.
- **Navegación lateral** fija con las secciones del alcance elegido. **Mini:** Color, Tipografía, Espaciado y layout, Radios, Sombras, Cuadrículas, Iconos y Brand assets. **Full:** además Principios, Imágenes, Movimiento, Componentes, Patrones, Plantillas, Accesibilidad y Changelog. Lo que queda fuera del alcance se marca como «fuera de alcance (full)», no se muestra vacío.
- **Color:** muestras con nombre del token, valor, y ratio de contraste WCAG de los pares de texto/fondo; primitivas y semánticas separadas.
- **Tipografía:** escala real renderizada con la fuente, tamaño, peso e interlineado.
- **Componentes (solo full):** cada uno renderizado vivo con todas sus variantes y estados (reposo, hover, foco, activo, deshabilitado, error), con anatomía y reglas de uso (cuándo sí, cuándo no).
- **Modo claro/oscuro** conmutable si el sistema define ambos.
- **Tokens como fuente:** el HTML declara en su propio `<style>` las variables CSS derivadas de `.yas/tokens/` (convención de `tokens-spec.md`; no hay un archivo CSS aparte), de modo que el entregable usa el sistema que documenta.
- **Responsive**, imprimible (CSS `@media print`) y con foco visible y contraste AA en el propio documento.
- **Pie de implementación:** cada valor indica cómo recrearlo en Figma (colección, modo, nombre de variable).

No inventes componentes ni tokens que no existan en el sistema; si falta algo que no se pueda derivar del manual, márcalo como "pendiente de definir". Lo derivable se propone con valor (ver "Tokens" e "Iconos derivados").

## Conexión con Figma (MCP)

Los comandos que usan Figma verifican primero si las herramientas del MCP de Figma están disponibles (`whoami`, `use_figma`, `create_session`…), con cualquier prefijo según cómo esté instalado (por ejemplo `mcp__plugin_figma_figma__*`, `mcp__figma__*` o `mcp__Figma__*`). Si aparecen como herramientas diferidas, cárgalas con ToolSearch; si no existen con ningún prefijo, el MCP no está instalado.

### Si el MCP no está instalado

Avisa al usuario **antes de hacer nada más**, con este mensaje (adáptalo, no lo omitas):

> **Falta el MCP de Figma.** Para trabajar directamente en Figma necesito el MCP oficial de Figma.
> Instálalo con una de estas vías y reinicia Claude Code:
> - Plugin oficial (recomendado por Figma): `claude plugin install figma@claude-plugins-official`, o desde `/plugin`.
> - MCP remoto: `claude mcp add --transport http figma https://mcp.figma.com/mcp` y luego `/mcp` para autenticarte (añade `--scope user` para usarlo en todos los proyectos).
> - Documentación oficial: https://developers.figma.com/docs/figma-mcp-server/remote-server-installation

Después, según el comando:
- `mini` y `full`: continúan en **modo local** y generan el sistema en `.yas/figma-local/` con todo lo necesario para implementarlo manualmente en Figma después (y para cargarlo con `push` una vez instalado el MCP).
- `colors`: sigue en modo local (genera los tokens y los archivos de variables).
- `push` y `documentation figma`: **terminan** con el aviso. No generes nada alternativo.

No intentes simular llamadas al MCP ni inventes URLs de Figma.

### Si el MCP está instalado

Confirma la sesión con `whoami` **una sola vez por ejecución**; si falla la autenticación, indica al usuario que ejecute `/mcp` y se autentique. No uses el plan que devuelva `whoami` para suponer límites: se detectan solo cuando Figma devuelve el error. Luego trabaja en **modo MCP**:
- **Archivo destino**, en este orden de prioridad:
  1. La URL de Figma que pase el usuario en este comando (`figma.com/design/:fileKey/...`): usa su `fileKey` y guárdalo en `.yas/figma-state.json`. Si el estado tenía otro `fileKey`, avisa del cambio y pregunta si es un archivo nuevo (empezar de cero) o el mismo sistema movido (conservar el progreso).
  2. Si no hay URL, el `fileKey` de `.yas/figma-state.json`, confirmando con el usuario el nombre del archivo antes de escribir.
  3. Si no hay ninguno, pide al usuario que cree un archivo en sus Drafts de Figma y pase el link. **No crees archivos nuevos por tu cuenta**: un archivo creado desde el MCP puede quedar dentro de un equipo con plan Starter y heredar sus límites.
- Llama a `create_session` con el `fileKey` y una descripción breve antes de cualquier otra herramienta de archivo.
- Comprueba el nombre del archivo dentro del primer script de `use_figma` (`figma.root.name`) y muéstralo al usuario; no gastes una herramienta de lectura en ello.
- Carga `figma:figma-use` antes de `use_figma`, `figma:figma-generate-library` para construir librerías y `figma:figma-design-to-code` antes de `get_design_context`. Esas guías las aporta el plugin oficial de Figma; si no está instalado, el propio servidor MCP las sirve como recursos (por ejemplo, `skill://figma/figma-use/SKILL.md`). Si no puedes cargar ninguna, dilo y no uses la herramienta correspondiente a ciegas.
- Para reutilizar lo existente y no duplicar, consulta `.yas/figma-state.json` y comprueba lo que ya hay dentro del propio script de `use_figma` (ver "Presupuesto de lecturas").

### Presupuesto de lecturas

Figma limita las herramientas de lectura del MCP según el plan y el asiento (el límite exacto no está verificado; se detecta cuando Figma devuelve el error). Cuenta como lectura toda llamada que lee, aunque también escriba: `use_figma` descuenta cuota en cada llamada (verificado en la práctica). Solo las herramientas que únicamente escriben, como `upload_assets`, quedan fuera. Cada llamada puede contar, así que:
- **No llames a `search_design_system` antes de cada creación.** Usa `.yas/figma-state.json` como registro de lo creado.
- **Comprueba y verifica dentro de `use_figma`:** el mismo script que crea variables, estilos, páginas o componentes lee con la Plugin API lo que ya existe (por nombre) antes de crear, y devuelve en su resultado los nombres e ids de lo creado. Eso sirve de verificación; no hace falta leer de vuelta con otra herramienta.
- **Agrupa:** crea varios elementos por llamada a `use_figma` cuando sea razonable, actualizando el estado con lo que devuelva cada llamada.
- **Herramientas de lectura** (`search_design_system`, `get_metadata`, `get_variable_defs`, `get_screenshot`, `get_libraries`, `get_design_context`, `get_code_connect_map`…): úsalas solo cuando no haya alternativa. Antes, di cuántas vas a usar y para qué, y pide confirmación si son más de una.
- Cada llamada a `use_figma` cuenta, también las que solo leen. Comprobar y verificar dentro del script evita llamadas adicionales, pero no la cuota de esa llamada: agrupa más trabajo en cada una y no hagas llamadas solo para comprobar.

### Si el MCP falla a mitad de trabajo

Si el MCP está instalado pero **no permite seguir editando** (cuota o límite de uso agotado, rate limit, plan sin permisos de edición, errores repetidos de la herramienta), no reintentes en bucle:
1. Detente tras el primer error claro y dile al usuario qué ocurrió, con el texto del error.
2. Indica qué quedó creado en Figma y qué falta (lista concreta de variables, estilos y componentes).
3. Pasa a **modo local** para lo pendiente: el paquete local y el HTML con el sistema **completo** quedan generados, y `push` retoma lo pendiente cuando se restablezca el límite.

## Creación en Figma (la comparten `mini`, `full` y `push`)

1. **Archivo y sesión:** determina el archivo destino según la prioridad de "Si el MCP está instalado" y abre la sesión.
2. **Plan:** lee los tokens, el paquete `.yas/figma-local/` y `.yas/figma-state.json`. Construye la lista de trabajo en este orden: páginas → colecciones y modos de variables → variables → estilos de texto, efectos y cuadrículas → componentes (uno a uno, solo en full) → contenido de las páginas de documentación.
3. **Páginas:** créalas con `use_figma` en el archivo destino. Si Figma devuelve el error de límite de páginas, aplica "Límite de páginas en equipos Starter".
4. **Estado:** `.yas/figma-state.json` guarda `fileKey`, URL del archivo, `scope` y, por elemento, `pending | done | error` con el id del nodo creado en Figma. Se actualiza **tras cada llamada a `use_figma`** con lo que devuelva, no al final, para no perder avance si el límite vuelve a cortar.
5. **Reanudación:** si el estado existe, no recrees lo `done`. En el primer script de `use_figma` comprueba por id o nombre que lo `done` sigue en el archivo (sin herramientas de lectura) y continúa con lo `pending` o `error`. Nunca dupliques variables o componentes.
6. **Cortes:** ante un límite de uso o error persistente aplica "Si el MCP falla a mitad de trabajo" y deja el estado consistente para que el siguiente `/yas-figma push` continúe donde se quedó.
7. **Cierre:** informa lo creado, lo pendiente y la URL del archivo de Figma. Actualiza `design-system.html` para reflejar el estado real (qué ya existe en Figma y qué no) e indica su ruta completa para abrirlo en el navegador.

### Límite de páginas en equipos Starter

En el plan Starter de Figma, los archivos dentro de un equipo admiten como máximo **3 páginas**; los archivos en Drafts (borradores) no tienen ese límite (según el blog oficial del plan Starter). El mini necesita 9 páginas y el full 28.

No supongas el límite por el plan que devuelva `whoami`: intenta crear las páginas en el archivo destino y aplica esta sección solo si Figma devuelve el error de límite. No reintentes en bucle ni recortes el sistema por tu cuenta. Explica que el archivo está en un equipo Starter y **presenta estas opciones** con AskUserQuestion:

| Opción | Qué ocurre |
|---|---|
| **1. Usar un archivo en Drafts (recomendada)** | Pide al usuario que mueva el archivo a sus Drafts o cree uno nuevo allí y pase el link. Actualiza el `fileKey` en el estado (conservando el progreso si es el mismo archivo movido) y continúa desde el estado guardado. |
| **2. Ampliar el plan de Figma** | Explica que se necesita un plan de pago para ese equipo. Pausa; cuando el usuario confirme, `/yas-figma push` retoma desde el estado guardado. |
| **3. Crear las páginas a mano** | Entrega la lista exacta de nombres del alcance elegido, en orden y lista para copiar (mini: `Cover`, `Icons`, `Brand assets`, `Colors`, `Type scale`, `Spacing and layout`, `Radios`, `Shadows`, `Grids`; full: las 28 páginas de su estructura), sin separadores. Solo sirve si el archivo admite tantas páginas (por ejemplo, en Drafts). Espera confirmación y verifica en el siguiente script de `use_figma` que existen con esos nombres exactos antes de continuar. |
| **4. Generar solo iconos, color y tipografía** | Construye en Figma únicamente 3 páginas (que caben en el límite): en mini `Icons`, `Colors` y `Type scale`; en full `Iconography`, `Color` y `Typography`. El resto se entrega en el paquete local y en el HTML. |

En cualquier opción, rellena solo páginas que ya existan, sin intentar crear más de las permitidas, y registra en `.yas/figma-state.json` la opción elegida (`"pageLimit": "drafts" | "upgrade" | "manual" | "reduced"`) y qué páginas están `done` o `pending`. Si el estado ya tiene la opción elegida y el archivo destino no ha cambiado, aplícala sin volver a preguntar.

## Procedimiento de cada comando

### `mini` y `full`: generar el design system

1. **Alcance:** el del comando. Si el estado ya tiene otro, aplica las "Reglas entre alcances" (ampliar de mini a full, o confirmar antes de pasar de full a mini).
2. **Conexión:** comprueba el MCP (ver "Conexión con Figma"). Si no está instalado, muestra el aviso y continúa en modo local.
3. **Fuente de datos:** localiza el manual. Sin manual, detente y pídelo.
4. **Tokens:** aplica la sección "Tokens", incluida la aprobación de las propuestas.
5. **Paquete local:** genera `.yas/figma-local/` y su `design-system.html` según el alcance. Se genera **siempre**, con o sin MCP: es el design system "ya generado" que cargará `push`.
6. **Figma (solo con MCP):** ejecuta la "Creación en Figma". Si falla a mitad de trabajo, aplica "Si el MCP falla a mitad de trabajo".
7. **Cierre:** ruta del paquete y del HTML, qué se creó en Figma (con la URL) o que quedó solo en local, lo que se marcó como propuesta o pendiente, y que `/yas-figma push` lo cargará a Figma cuando haya MCP y cuota.

### `push`: cargar a Figma un design system ya generado

`push` no genera ni deriva nada del manual: toma el sistema que `mini` o `full` ya dejó en el proyecto y lo carga a Figma. Es **idempotente y reanudable**, así que también sirve para continuar tras un límite de uso.

1. **Conexión:** requiere el MCP instalado y autenticado. Si no está instalado, muestra el aviso de instalación y termina; si falla la autenticación o la cuota, di el motivo y termina.
2. **Comprobación previa:** verifica que existen `.yas/figma-local/` y `.yas/tokens/tokens.json`. Si no hay un design system generado, dilo y sugiere ejecutar antes `/yas-figma mini` o `/yas-figma full`; no lo generes por tu cuenta.
3. **Archivo destino:** si el usuario pasa una URL de Figma, esa manda sobre la del estado (ver la prioridad en "Si el MCP está instalado").
4. **Alcance:** léelo de `.yas/figma-state.json` o de la portada del paquete; no lo preguntes.
5. **Creación en Figma** (ver la sección).

### `documentation`: entregable HTML del design system

`/yas-figma documentation` tiene **dos orígenes**. Elígelo por argumento (`documentation figma <URL>`, `documentation manual`) o, si no se indicó, pregúntalo con AskUserQuestion; si el usuario pasó una URL de Figma, entiende `figma`.

| Origen | Fuente de los datos | ¿Necesita MCP? |
|---|---|---|
| `figma` | Un archivo de Figma existente: se documenta lo que realmente hay en él | Sí |
| `manual` | **Solo el manual de identidad** (adjunto del usuario o generado por `/yas-design`, según "Fuente de datos") | No |

#### Origen `manual`: HTML del design system a partir del manual

No usa el MCP ni lee o escribe en Figma. Flujo:

1. **Fuente de datos:** localiza el manual. Sin manual, detente y pídelo.
2. **Alcance:** mini o full. Se indica como argumento (`documentation manual full`) o, si no, pregúntalo.
3. **Tokens:** aplica la sección "Tokens"; si no existen, se derivan del manual y se escriben en `.yas/tokens/`.
4. **Generación:** escribe `.yas/deliverables/<marca>-design-system.html` con la "Especificación del HTML del design system". La portada declara que el sistema **se generó solo desde el manual, sin verificación contra Figma**, y qué datos fueron `extracted`, `inferred` o `missing`.
5. **Cierre:** ruta del HTML y lo que quedó como propuesta o pendiente. Para construir el sistema en Figma o en local, `/yas-figma mini` o `/yas-figma full`.

#### Origen `figma`: HTML a partir de un proyecto de Figma

`/yas-figma documentation figma [URL de Figma]` documenta un archivo de Figma existente (creado con `mini`, `full` o `push`, o ajeno a este sistema) como un HTML de entrega. A diferencia del origen `manual`, **la fuente aquí es Figma**: lo que se documenta es lo que realmente hay en el archivo.

No pregunta el alcance: documenta lo que existe, sin construir nada. Es de solo lectura; nunca modifica el archivo.

1. **Conexión:** si no hay conexión con el MCP o no se puede leer el archivo (sin MCP, sin autenticación, sin cuota, sin acceso al archivo, error de lectura), **anuncia el problema con el motivo concreto y finaliza**. No generes HTML alternativo, ni paquete local, ni ofrezcas otras salidas.
2. **Archivo objetivo:** toma el `fileKey` de la URL; si no hay, usa el de `.yas/figma-state.json`; si tampoco, pídelo. Llama a `create_session` (tarea de solo lectura).
3. **Snapshot previo:** si existe `.yas/figma-snapshot.json` para ese `fileKey`, pregunta si se reutiliza en lugar de volver a leer Figma.
4. **Extracción en una sola llamada a `use_figma`**, con un script que **solo lea** (sin crear, mover ni modificar nada) y devuelva: páginas y marcos principales, colecciones de variables con modos, nombres y valores, estilos de texto, efectos y cuadrículas, y componentes con sus variantes, propiedades y descripciones. Guarda el resultado en `.yas/figma-snapshot.json`. Si el resultado es demasiado grande para una llamada, divídelo en el menor número de llamadas posible y guarda tras cada una.
   - **Capturas (`get_screenshot`):** opcionales. Solo de los marcos o componentes que el usuario elija, informando de cuántas lecturas consumirán y con confirmación previa.
   - **Code Connect (`get_code_connect_map`):** solo si el usuario lo pide; omítelo por defecto.
   - No uses `get_metadata`, `get_variable_defs`, `search_design_system` ni `get_libraries` si el script de `use_figma` ya obtuvo esos datos.
5. **Generación:** escribe `.yas/deliverables/<nombre-archivo>.html`, autocontenido, con las mismas cualidades que la "Especificación del HTML del design system" (navegación lateral, claro/oscuro si hay modos, responsive, imprimible, contraste AA). Secciones: Portada (nombre, fileKey, enlace, fecha de extracción, última modificación si se conoce), Resumen (cifras reales: variables, estilos, componentes, páginas), Color, Tipografía, Espaciado y demás variables por colección y modo, Componentes (captura real si se tomó; si no, la especificación leída), Pantallas, Mapeo a código (si se leyó) y Hallazgos.
6. **Imágenes:** incrústalas como `data:` URI si pesan poco; si el HTML superara ~10 MB, guárdalas en `.yas/deliverables/assets/` y avisa de que el HTML debe moverse junto a esa carpeta.
7. **Hallazgos honestos:** señala inconsistencias detectadas al leer (valores fijos sin variable, estilos duplicados, componentes sin descripción, nombres fuera de convención, contraste insuficiente). Es un resumen de la lectura, no una auditoría.
8. **Cierre:** indica ruta del HTML, qué se extrajo, cuántas llamadas de lectura se usaron y qué **no se pudo leer** (con el motivo). No rellenes con datos inventados: lo ausente aparece como "no disponible".

### `colors`: de la paleta de marca a tokens y variables

`/yas-figma colors` convierte la paleta aprobada en tokens de color y en variables semánticas de Figma. Trabaja **solo con color**: no toca el resto de los tokens. No requiere elegir alcance, porque las variables de color existen en mini y en full y no requieren páginas nuevas.

1. **Conexión:** comprueba el MCP. Sin MCP, o si el límite de uso corta el trabajo, avisa y sigue en modo local (los tokens se generan igualmente; solo se omite Figma).
2. **Fuente:** lee la paleta de los artefactos compartidos (`paleta/paleta.md` con su tabla de contrato, y el manual) según "Fuente de datos". Sin paleta, se detiene y la pide.
3. **Tokens:** crea o actualiza `color.*` en `.yas/tokens/tokens.json` según `tokens-spec.md`: primitivas de la paleta, semánticas (superficie, texto, borde, acción y estado) con modos claro y oscuro, y el informe `.yas/tokens/contraste.md` con los pares calculados según `criterios-calidad.md`. Los roles que el manual no define (estados de acción como `hover` o `pressed`, iconos, enlace, foco, estados de feedback) **se derivan de los colores del manual** con las reglas de "Derivación de los roles que el manual no define" de `tokens-spec.md`, sin añadir matices ajenos a la paleta. Esos roles y las escalas tonales derivadas se marcan como *propuesta* y se **muestran al usuario para aprobar antes de crearlos en Figma**. Si `tokens.json` ya existe, fusiona sin reescribir lo existente y anota el cambio en `.yas/tokens/CHANGELOG.md`.
4. **Figma (con MCP):** determina el archivo destino según la prioridad de "Si el MCP está instalado". Con `use_figma`, en el mismo script: comprueba qué colecciones y variables ya existen (para no duplicar), crea la colección de primitivas (sin modos) y la de semánticas (modos Light y Dark) con sus alias, y devuelve nombres, ids y valores de lo creado como verificación. No uses herramientas de lectura para verificar. Actualiza `.yas/figma-state.json` tras cada llamada para poder retomar.
5. **Modo local:** escribe `variables.md` y `variables.json` con las colecciones y los modos de color, listos para crear a mano en Figma.
6. **Cierre:** informa qué se generó, qué se verificó (contrastes calculados, variables devueltas por `use_figma`) y qué queda pendiente.

## Referencias externas

La lista y sus reglas de uso están en `../yas-core/references/referencias-externas.md`. Al definir o construir componentes y fundamentos (`mini`, `full`, `colors`) se consultan M3 o HIG según la plataforma del proyecto, citando la página consultada en `componentes.md`, en el HTML y en las notas de Figma.

## Principios

- **El manual de identidad aprobado es la fuente de datos; `.yas/tokens/` es su traducción y el código consume esos tokens.** Figma refleja el sistema, no lo contradice. Si hay conflicto entre manual, tokens, código y Figma, señálalo y pregunta; prevalece lo aprobado en el manual.
- **Tokens antes que componentes, componentes antes que pantallas.**
- **Nada con valores fijos:** en Figma todo se enlaza a variables.
- **El archivo que indica el usuario manda:** nunca escribas en otro archivo ni crees uno nuevo sin que el usuario lo pida.
- **La cuota de lectura es escasa:** el estado local y los scripts de `use_figma` sustituyen a las herramientas de lectura siempre que sea posible.
- **Declara siempre el modo** (MCP o local) al empezar y al entregar, y qué quedó pendiente.
- **No inventes:** si no puedes verificar algo en Figma, dilo.
