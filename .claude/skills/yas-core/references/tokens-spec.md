# Especificación de tokens

Formato único de los tokens de diseño del ecosistema. Lo usa `/yas-figma` (`colors`, `mini`, `full`, `documentation manual`). Aquí se define una vez; las skills lo referencian.

**Archivo:** `.yas/tokens/tokens.json`, en formato DTCG (Design Tokens Community Group): cada token tiene `$value` y `$type`, y los grupos pueden fijar un `$type` heredado.

## Dos niveles

| Nivel | Qué es | Ejemplo |
|---|---|---|
| **Primitivas** | Valores crudos de la marca, sin significado de uso. | `color.primitive.brand.500` = `#1A5FB4` |
| **Semánticas** | Roles de uso que **alias** a primitivas; son lo que usan los componentes. | `color.semantic.action.primary.bg` = `{color.primitive.brand.500}` |

Los componentes y las pantallas **solo** consumen tokens semánticos. Un valor fijo en un componente es un hallazgo de auditoría.

## Nomenclatura

- Ruta con puntos, en minúsculas y con guion para palabras compuestas: `color.semantic.text.primary`.
- Convención para variables CSS, cuando un entregable o el proyecto las use: la ruta con guiones y prefijo `--` (`--color-semantic-text-primary`). No hay un archivo CSS de tokens generado por el ecosistema; el HTML de `/yas-figma` las declara en su propio `<style>`.
- Variable de Figma: la ruta con barras (`color/semantic/text/primary`), en la colección correspondiente.
- Alias entre llaves: `{color.primitive.brand.500}`. Sin referencias circulares ni sin resolver.

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
| Espaciado | `space.*` | Escala con unidad base (4 u 8 px) |
| Radios | `radius.*` | |
| Sombras | `shadow.*` | Composite o cadena CSS, por niveles de elevación |
| Bordes | `border.width.*` | Solo en full |
| Movimiento | `motion.duration.*`, `motion.easing.*` | Solo en full |
| Breakpoints | `breakpoint.*` | |
| Capas | `z.*` | Solo en full |

El alcance mini incluye color, tipografía, espaciado, radios y las sombras y cuadrículas; el full añade el resto (ver `/yas-figma`).

## Roles semánticos de color

Mínimo que debe cubrir la paleta semántica, derivado de los roles de la paleta (`principal`, `apoyo`, `neutro`) y de los roles de estado:

| Grupo | Tokens |
|---|---|
| Superficie | `surface.default`, `surface.subtle`, `surface.inverse`, `surface.overlay` |
| Texto | `text.primary`, `text.secondary`, `text.disabled`, `text.inverse`, `text.link` |
| Borde | `border.default`, `border.strong`, `border.focus` |
| Acción | `action.primary.{bg,fg,hover,pressed,disabled}`, `action.secondary.*` |
| Icono | `icon.{default,strong,subtle,disabled,inverse,brand}` |
| Estado | `feedback.{success,warning,error,info}.{bg,fg,border}` |

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
