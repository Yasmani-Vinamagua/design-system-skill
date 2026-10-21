# Especificación de tokens

Formato único de los tokens de diseño del ecosistema. Lo usa `/yas-figma` (`colors`, `push`, `document manual`). Aquí se define una vez; las skills lo referencian.

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
| Estado | `feedback.{success,warning,error,info}.{bg,fg,border}` |

- Los colores salen de la **paleta aprobada**. Una escala tonal (por ejemplo, 50 a 900) derivada de un color de marca es una **propuesta** y se marca como tal hasta que el usuario la apruebe.
- Los roles de estado que el manual no define (éxito, aviso, error, información) se proponen y se marcan como *propuesta*.
- Cada token de texto y de componente declara su **par de fondo** y se calcula el contraste en ambos modos (criterios en `criterios-calidad.md`). El resultado va en `.yas/tokens/contraste.md`.

## Cabecera de origen y registro

Cada generación de `tokens.json` añade en `$description` del grupo raíz o en `.yas/tokens/CHANGELOG.md`: fecha, skill y subcomando, fuente (por ejemplo, `paleta/paleta.md`) y qué datos son `extracted`, `inferred` (propuesta) o `missing` (pendiente de definir).

## Quién escribe qué

- `/yas-figma colors` genera y actualiza **solo `color.*`**; no toca el resto.
- `/yas-figma` (`push`, `document manual`) genera las demás categorías del alcance elegido a partir del manual.
- Si el archivo ya existe, la skill lo lee, **fusiona** lo que falta y no reescribe lo existente sin confirmación (regla de Protección). Si un valor existente contradice la paleta aprobada, lo señala y pregunta.
