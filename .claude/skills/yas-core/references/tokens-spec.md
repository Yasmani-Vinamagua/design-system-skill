# Especificación de tokens

Formato único de los tokens de diseño del ecosistema. Lo usa `/yas-figma` (`colors`, `mini`, `full`, `documentation manual`). Aquí se define una vez; las skills lo referencian.

**Archivo:** `.yas/tokens/tokens.json`, en formato DTCG (Design Tokens Community Group): cada token tiene `$value` y `$type`, y los grupos pueden fijar un `$type` heredado.

## Dos niveles

| Nivel | Qué es | Ejemplo |
|---|---|---|
| **Primitivas** | Valores crudos de la marca, sin significado de uso. | `color.primitive.brand.500` = `#1A5FB4` |
| **Semánticas** | Roles de uso que **alias** a primitivas; son lo que usan los componentes. | `color.semantic.action.primary.bg` = `{color.primitive.brand.500}` |

Los componentes y las pantallas **solo** consumen tokens semánticos y, en `full`, los tokens de su propio componente (ver abajo). Un valor fijo en un componente es un hallazgo de auditoría. Las primitivas se usan directamente solo cuando no existe un token semántico adecuado (fuente: Adobe Spectrum, design tokens).

### Tokens de componente (opcional, solo en `full`)

Tercer nivel para las medidas o decisiones que pertenecen a **un solo componente** y no tienen sentido como rol general (ancho máximo de un tooltip, altura de un campo).

- Ruta: `component.<nombre>.<propiedad>` (por ejemplo `component.tooltip.max-width`).
- Siempre son **alias** de un token semántico o primitivo (o, para una medida sin equivalente, de un valor de la escala `space.*`); un valor suelto solo se admite justificado.
- Deben ser **minoritarios** frente a los semánticos. Si un mismo valor se repite en dos o más componentes, se sube a un token semántico.
- Los consume únicamente su componente. Un componente no usa los tokens de otro.

## Nomenclatura

- Ruta con puntos, en minúsculas y con guion para palabras compuestas: `color.semantic.text.primary`.
- **Orden de los segmentos: de lo general a lo específico.** Categoría → nivel → qué se comunica (rol) → qué afecta → estado o variante. Ejemplo: `color.semantic.action.primary.hover` (color → semántica → acción → principal → hover). Dos tokens del mismo rol comparten prefijo, para que se agrupen y se lean de izquierda a derecha (fuente: Adobe Spectrum, nomenclatura).
- Convención para variables CSS, cuando un entregable o el proyecto las use: la ruta con guiones y prefijo `--` (`--color-semantic-text-primary`). No hay un archivo CSS de tokens generado por el ecosistema; el HTML de `/yas-figma` las declara en su propio `<style>`.
- Variable de Figma: la ruta con barras (`color/semantic/text/primary`), en la colección correspondiente.
- Alias entre llaves: `{color.primitive.brand.500}`. Sin referencias circulares ni sin resolver, y **solo entre tokens del mismo tipo** (ver «Tokens y variables de Figma»).

## Modos claro y oscuro

Un token semántico define su valor claro en `$value` y el oscuro en `$extensions.yas.dark`:

```json
"text": {
  "primary": {
    "$type": "color",
    "$value": "{color.primitive.neutral.900}",
    "$extensions": { "yas": { "dark": "{color.primitive.neutral.50}" } }
  }
}
```

En Figma, las semánticas viven en una colección con los modos **Light** y **Dark**; las primitivas, en una colección sin modos.

## Categorías

| Categoría | Ruta base | Notas |
|---|---|---|
| Color | `color.primitive.*`, `color.semantic.*` | Ver roles abajo |
| Tipografía | `font.family.*`, `font.size.*`, `font.weight.*`, `font.line-height.*` | La familia sale del sistema tipográfico del manual |
| Espaciado | `space.*` | Escala con unidad base (4 u 8 px). Opcional: `space.inset.*` (relleno interior) y `space.gap.*` (separación entre elementos), como **alias** de la escala, por ejemplo `space.inset.md` = `{space.16}` |
| Componente | `component.<nombre>.*` | Solo en full; ver «Tokens de componente» |
| Radios | `radius.*` | |
| Sombras | `shadow.*` | Composite o cadena CSS, por niveles de elevación |
| Bordes | `border.width.*` | Solo en full |
| Movimiento | `motion.duration.*`, `motion.easing.*` | Solo en full |
| Breakpoints | `breakpoint.*` | |
| Capas | `z.*` | Solo en full |

El alcance mini incluye color, tipografía, espaciado, radios y las sombras y cuadrículas; el full añade el resto (ver `/yas-figma`).

## Tokens y variables de Figma

Figma tiene cuatro tipos de variable: color, número, cadena y booleana. Un token se crea como variable según esta tabla (fuente: ayuda de Figma, «variables, colecciones y modos»):

| Token | Variable de Figma |
|---|---|
| `color.*` | Color |
| `font.family.*` | Cadena |
| `font.size.*`, `font.weight.*`, `font.line-height.*` | Número |
| `space.*`, `radius.*`, `border.width.*`, `breakpoint.*`, `z.*`, `motion.duration.*` | Número |
| `component.*` | El tipo del token al que apuntan |
| `shadow.*` | **No es variable**: va como estilo de efecto. Los colores que usa sí pueden ser variables de color |
| `motion.easing.*` | **No es variable**: no hay tipo equivalente. Se documenta (valores y uso) y, si hace falta, se guarda como cadena de referencia |

- **Alias solo entre el mismo tipo.** Un alias de número a cadena, o de color a número, no es válido en Figma; un token no puede apuntar a otro de distinto tipo.
- **Dos decimales como máximo.** Las variables de número admiten hasta dos decimales: una razón de 1,333 o un interlineado de 1,125 se redondea (1,33 y 1,13). En `tokens.json` se guarda ya el valor redondeado y se anota en la cabecera de origen que se redondeó.
- **Estilos frente a variables.** Los estilos (texto, efecto, cuadrícula) agrupan valores fijos y **no pueden referenciarse desde variables**. Se usan donde Figma no admite variable (sombras, escala de texto); el resto va como variable para poder tener alias y modos.
- **Modos por colección.** El número de modos depende del plan de Figma. El mínimo de yas son 2 (Light y Dark en las semánticas de color). Un tercer modo (por ejemplo, densidad) solo se crea tras comprobar que el plan lo permite; si no, se propone otra vía (una colección aparte sin modos, o documentar la variante).
- **Grupos.** La ruta con barras crea los grupos dentro de la colección (`color/semantic/text/primary`). Una colección admite hasta 5000 variables, límite que un sistema de yas no se acerca a tocar.

## Reglas de escalas (tipografía y espaciado)

Valores por defecto cuando el manual no define la escala; lo que el manual defina prevalece. Todo lo que se derive aquí se marca `inferred` / *propuesta* y se aprueba antes de crearlo (fuente: *Design Systems Handbook*, cap. 2, ver `referencias-externas.md`).

| Aspecto | Regla |
|---|---|
| Tamaño base | 16 px (`1rem` en sistemas con CSS). Los demás tamaños se expresan en relación con él |
| Escala de títulos | Escala modular: un número base y una razón que se aplica una y otra vez. Declara la razón elegida en `font.size.*` |
| Interlineado | Texto de párrafo ≈ 1,5 (valor que recomienda la WAI). Títulos más ajustados: 1,25 o 1,125. Se guarda sin unidad en `font.line-height.*` |
| Familias | Máximo dos: una para títulos y texto y, si hace falta, una monoespaciada para código. Una tercera solo con justificación (por ejemplo, un sistema multimarca) |
| Pesos finos | Solo en tamaños grandes; en texto pequeño comprometen la legibilidad |
| Espaciado | Escala con múltiplos de 4 (base 4); 8 para el horizontal es habitual. Un valor fuera de la escala (por ejemplo, compensar un borde de 1 px) es la excepción y se justifica caso a caso |
| Tamaños de elementos | Evita fijar anchos y alturas salvo necesidad: deja que el contenido fluya |
| Iconos | Tamaños de la misma escala (16, 24, 32) |
| Tipografía adaptable | Tamaños de títulos que crecen en pantallas grandes y se contienen en móvil (por breakpoint o con unidades de viewport). Tamaño e interlineado múltiplos de la unidad de espaciado para alinear con la cuadrícula |
| Legibilidad | Declara interletraje, interlineado y longitud de línea cómoda para el texto de párrafo; no se fijan sin criterio |
| Fuentes de respaldo | Cada familia declara una alternativa de sistema para mientras carga o si falla; una fuente personalizada pesa en la carga |

## Elevación

- 3 o 4 niveles bastan en la mayoría de productos: `shadow.1` a `shadow.4`.
- **Cada nivel de sombra tiene un token de superficie asociado** (por ejemplo `surface.elevation.1`). En modo claro, la superficie se acerca al blanco y la sombra comunica la altura. En modo oscuro la sombra apenas se ve: la altura se comunica con un fondo más claro a mayor elevación, por eso el token existe en ambos modos.
- Los niveles de `z.*` (solo full) definen qué se pinta por encima: contenido, desplegables, modales, avisos. Un valor de z fijo en un componente es un hallazgo.
- Fuente: `checklist-sistema-diseno.md`, sección 1.

## Roles semánticos de color

Mínimo que debe cubrir la paleta semántica, derivado de los roles de la paleta (`principal`, `apoyo`, `neutro`) y de los roles de estado:

| Grupo | Tokens |
|---|---|
| Superficie | `surface.background`, `surface.default`, `surface.subtle`, `surface.inverse`, `surface.overlay` |
| Texto | `text.primary`, `text.secondary`, `text.disabled`, `text.inverse`, `text.link` |
| Borde | `border.default`, `border.strong`, `border.focus` |
| Acción | `action.primary.{bg,fg,hover,pressed,disabled}`, `action.secondary.*` |
| Acento | `accent.{bg,fg,subtle}` (opcional; ver «Acento y controles») |
| Controles | `control.{selected,track,progress}` (ver «Acento y controles») |
| Icono | `icon.{default,strong,subtle,disabled,inverse,brand}` |
| Estado | `feedback.{success,warning,error,info}.{bg,fg,border}` |
| Datos | `chart.categorical.{1..n}` (opcional; ver «Colores de visualización de datos») |

`surface.background` es el lienzo detrás del contenido con scroll; `surface.default` es la superficie de componentes (cards, hojas, menús). Pueden tener el mismo valor, pero son tokens distintos para poder separarlos sin tocar los componentes (fuente: Material Design 2, sistema de color).

### Acento y controles

- `accent.*` es el color de `apoyo` de la paleta usado **con moderación** como acento: elementos destacados puntuales, selección de texto, enlaces o titulares si el manual lo indica. Es **opcional**: si la paleta no tiene color de apoyo, no se crea y el color principal hace de acento (`accent.bg` = `action.primary.bg` por alias, no un token vacío).
- `action.secondary.*` es un **estilo de botón** (borde y texto en el color principal) y no sustituye a `accent.*`: son conceptos distintos.
- `control.selected` (interruptores, casillas, radios, sliders activos), `control.progress` (barras de progreso) y `control.track` (el carril sin rellenar) salen por **alias** de `accent.bg` si existe, o de `action.primary.bg` si no. `control.track` = `border.default`, o un neutro de la paleta que cumpla ≥3:1 sobre la superficie.
- Fuente: Material Design 2, sistema de color (usos del color secundario).

### Colores de visualización de datos

- Opcional, solo si el producto tiene gráficos. `chart.categorical.1` a `chart.categorical.n` (de 5 a 8 suelen bastar) para distinguir categorías fuera del tema principal.
- Parten de la paleta; los matices adicionales se **proponen** (`inferred`) y se confirman, igual que `feedback.*`. Deben distinguirse entre sí y cumplir ≥3:1 sobre `surface.default` en ambos modos.
- No se usa solo el color para distinguir categorías: se acompaña de etiqueta, forma o patrón.

### Derivación de los roles que el manual no define

El manual suele dar solo la paleta (principal, apoyo, neutros) y no los estados de interacción ni los iconos. Esos tokens **se derivan siempre** de los colores del manual; no se dejan vacíos ni se inventan tonos nuevos. Regla general: no se introduce ningún matiz (hue) que no esté en la paleta; solo se varía la luminosidad dentro de la escala tonal de cada color, y todo token derivado se marca `inferred` / *propuesta*.

| Token | Derivación (modo claro; en oscuro se invierte el sentido del paso) |
|---|---|
| `action.primary.bg` | El color principal del manual (`extracted`) |
| `action.primary.fg` | Blanco o el neutro más oscuro, el que cumpla contraste AA (4.5:1) sobre `bg` |
| `action.primary.hover` | `bg` un paso más oscuro de su escala (en oscuro, un paso más claro) |
| `action.primary.pressed` | `bg` dos pasos más oscuros (en oscuro, dos más claros) |
| `action.primary.disabled` | Neutro claro de la paleta (por ejemplo `neutral.200`) con texto `text.disabled` |
| `action.secondary.*` | `bg` transparente o `surface.default`, `fg` y borde con el color principal; `hover` con el paso más claro de la escala principal (50 o 100) |
| `text.link` | El color principal; si no llega a 4.5:1 sobre `surface.default`, el paso más oscuro que cumpla |
| `border.focus` | El color principal o de apoyo, el que contraste ≥3:1 con la superficie |
| `surface.background` | = `surface.default` salvo que el manual distinga lienzo y superficie |
| `accent.bg` | El color de apoyo del manual; si no hay, = `action.primary.bg` (alias) |
| `accent.fg` | Blanco o el neutro más oscuro, el que cumpla AA (4.5:1) sobre `accent.bg` |
| `accent.subtle` | Paso muy claro de la escala del acento (50 o 100); en oscuro, muy oscuro |
| `control.selected` / `control.progress` | = `accent.bg` (alias) |
| `control.track` | = `border.default`, o neutro de la paleta ≥3:1 sobre la superficie |
| `icon.default` | = `text.secondary` |
| `icon.strong` | = `text.primary` |
| `icon.subtle` | Neutro medio de la paleta, ≥3:1 sobre la superficie |
| `icon.disabled` | = `text.disabled` |
| `icon.inverse` | = `text.inverse` |
| `icon.brand` | = `action.primary.bg` |
| `feedback.success` / `warning` / `error` / `info` | Convención universal de matiz (verde, ámbar, rojo, azul) ajustada a la saturación y luminosidad de la paleta; `fg` y `border` por pasos de su escala. Es la única excepción a "ningún matiz ajeno": se propone y se confirma con el usuario |

- Los tokens de icono salen por **alias** de tokens de texto y de acción, para que cambien con ellos en ambos modos. El estilo de los iconos (trazo, tamaño, esquinas) lo fija el manual; si no consta, queda `missing`.
- Si el paso derivado no cumple contraste, se ajusta al siguiente paso de la escala; si ninguno cumple, se señala en `contraste.md` y se pregunta.

- Los colores salen de la **paleta aprobada**. Una escala tonal (por ejemplo, 50 a 900) derivada de un color de marca es una **propuesta** y se marca como tal hasta que el usuario la apruebe.
- Los roles de estado que el manual no define (éxito, aviso, error, información) se proponen y se marcan como *propuesta*.
- Cada token de texto y de componente declara su **par de fondo** y se calcula el contraste en ambos modos (criterios en `criterios-calidad.md`). El resultado va en `.yas/tokens/contraste.md`.

## Cabecera de origen y registro

Cada generación de `tokens.json` añade en `$description` del grupo raíz o en `.yas/tokens/CHANGELOG.md`: fecha, skill y subcomando, fuente (por ejemplo, `paleta/paleta.md`) y qué datos son `extracted`, `inferred` (propuesta) o `missing` (pendiente de definir).

## Quién escribe qué

- `/yas-figma colors` genera y actualiza **solo `color.*`**; no toca el resto.
- `/yas-figma` (`mini`, `full`, `documentation manual`) genera las demás categorías del alcance elegido a partir del manual.
- Si el archivo ya existe, la skill lo lee, **fusiona** lo que falta y no reescribe lo existente sin confirmación (regla de Protección). Si un valor existente contradice la paleta aprobada, lo señala y pregunta.
