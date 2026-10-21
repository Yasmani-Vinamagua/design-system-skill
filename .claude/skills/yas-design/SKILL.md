---
name: yas-design
description: Crea la identidad de un proyecto: estrategia de marca o rebranding, marca gráfica (logo) y manual de identidad, documentando cada decisión en archivos reales del proyecto. El manual de identidad que genera es la fuente de datos de /yas-figma. Úsala cuando el usuario pida crear o rehacer una marca o definir su identidad visual. Para evaluar algo ya hecho usa /yas-audit; para llevarlo a Figma, /yas-figma.
argument-hint: "[init | brief | brand | rebrand] [descripción, ruta o adjunto]"
---

# Yas Design

Responsabilidad: **analizar, decidir, ejecutar y documentar** la identidad de un proyecto. No audita (eso es `/yas-audit`) ni escribe en Figma (eso es `/yas-figma`).

Método: **Analizar → Decidir → Ejecutar → Documentar → Validar**. Cada subcomando deja archivos reales en `.yas/` y registra sus decisiones con su justificación.

## Reglas obligatorias

Antes de actuar, lee `../yas-core/references/reglas-comunes.md`: inspección inicial, contexto, ejecución, archivos, protección, calidad, documentación, transparencia y regla de alcance. Valen para todos los subcomandos y no se repiten aquí.

**Alcance de esta skill:** ejecuta el subcomando pedido, fase a fase y con aprobación. Las propuestas conceptuales (brief, concepto, bocetos, dirección visual, estructura de pantallas) no se convierten en código si no se pidió código. No audita, no exporta a Figma ni añade entregables que no se pidieron: los ofrece.

## Vocabulario y criterios de marca

Esta sección es la fuente única de estos términos y reglas para `SKILL.md` y para `references/` (`proceso.md`, `construccion-logo.md`, `manual-plantilla.md`). Si algún documento los contradice, vale lo que dice aquí.

**Términos**
- **Marca gráfica** o **logo**: la pieza visual completa de la marca, sea cual sea su tipo. "Logo" es la forma corta de "marca gráfica".
- **Tipos de marca gráfica:** *logotipo* (solo el nombre dibujado), *isotipo* (solo símbolo), *imagotipo* (símbolo y nombre separables) e *isologo* (símbolo y nombre fusionados). "Logotipo" se usa **solo** para el primer tipo, nunca como sinónimo de logo.
- **Símbolo** y **nombre**: las dos partes de una marca gráfica; el símbolo es la parte de isotipo y el nombre es la parte de logotipo.
- **Maestro**: `logo-master.svg`, del que se derivan todas las variantes.

**Estados** (un único vocabulario)
- Para **pruebas**: *verificada*, *fallida*, *no aplicable*, *no verificada*.
- Para **datos y valores**: *verificado* (consta y se comprobó), *no verificado* (consta pero no se comprobó) y *pendiente de definir* (no consta).
- Nunca presentes una prueba no ejecutada como superada ni un dato supuesto como confirmado.

**Valores de color:** HEX y RGB son los valores de pantalla. CMYK es siempre una conversión de referencia y el Pantone, siempre aproximado y provisional; ambos se validan con el proceso de impresión y una guía física vigente. Si no pueden determinarse con fiabilidad, se escriben como *pendiente de definir*; no se inventan.

**Nombres de archivo de las variantes:** la tabla de la sección 4 de `construccion-logo.md` es la fuente única. Ningún otro documento define nombres propios.

**Precedencia** (de mayor a menor), cuando dos instrucciones chocan:
1. Las decisiones aprobadas por el usuario, registradas en `marca-spec.md`.
2. El brief aprobado.
3. `construccion-logo.md` y `manual-plantilla.md`.
4. Las referencias externas.

Todo conflicto se registra en el Registro de decisiones del spec, con su motivo; no se resuelve en silencio.

## Inicio: marca nueva o rebranding

Al invocar `/yas-design` sin subcomando, o con `brand`, lo primero es preguntar con AskUserQuestion cuál es el punto de partida (si el usuario ya lo dijo o ya hay `.yas/brand/` con una elección registrada, úsalo sin volver a preguntar, indicándolo en una línea). `rebrand` entra directo por la opción 2 y `brand` por la 1 si el usuario ya está claro.

| Opción | Cuándo |
|---|---|
| **1. Nueva (new)** | No existe identidad: se crea desde cero. |
| **2. Rebranding** | Existe una marca que se evoluciona o rehace. |

### Si es nueva: tipo de marca

Pregunta primero **quién decide el tipo de marca**, y solo si el usuario quiere decidirlo, pregunta cuál. Son dos preguntas encadenadas, porque AskUserQuestion admite máximo 4 opciones:

1. **¿Defines tú el tipo de marca o lo decido yo según el brief?** (recomendado: que lo decida Yas Design, si el brief está claro).
2. Si lo define el usuario, elige entre estas cuatro:

| Tipo | Qué es | Suele encajar cuando |
|---|---|---|
| **Logotipo** | Solo tipografía: el nombre dibujado. | Nombre corto, distintivo y pronunciable; marcas de servicios o personales. |
| **Isotipo** | Solo símbolo, sin texto. | La marca ya es reconocida o el símbolo debe funcionar solo (app, icono, sello). |
| **Imagotipo** | Símbolo y texto **separables**, que pueden usarse juntos o por separado. | Se necesita flexibilidad entre versión completa y símbolo (el caso más versátil). |
| **Isologo** | Símbolo y texto **fusionados** en una sola pieza indivisible. | Se busca sello o emblema compacto; menos flexible al reducir. |

Si el usuario pide que lo decida Yas Design:
- Analiza el brief (nombre y su longitud, sector, público, medios donde vivirá la marca: app, impreso, señalética, redes, tamaño mínimo, competencia).
- **Propón un tipo con su justificación** en pocas líneas, indica la alternativa más cercana y por qué se descartó, y **pide aprobación antes de construir**. No lo des por hecho.
- Si falta información para decidir (por ejemplo, dónde se aplicará la marca), pregunta solo eso.

Registra la decisión, quién la tomó (usuario o Yas Design) y su justificación en el registro de decisiones de `marca-spec.md`. Cualquier tipo debe entregar además las **versiones necesarias** que no cubra el principal (por ejemplo, un símbolo para tamaños pequeños si se eligió imagotipo, o una versión compacta si se eligió logotipo).

### Si es rebranding

No se asume que todo deba cambiarse. Antes del brief hay una **evaluación inicial de la marca existente** (Fase 0b de `references/proceso.md`): inventariar logos, tipografías, colores, manuales y aplicaciones; identificar los activos reconocibles que convenga conservar; separar problemas de ejecución visual de problemas de posicionamiento; y **definir el alcance del cambio**. La marca existente puede aportarla el usuario como adjunto o URL; si no hay material, se pide.

Pregunta con AskUserQuestion el alcance (si la evaluación ya lo deja claro, propón uno con su razón y pide confirmación):

| Alcance | Qué es | Qué se conserva |
|---|---|---|
| **Ajuste** (ajuste puntual) | Corregir la ejecución visual sin cambiar la idea. | Casi todo: forma, color y concepto. |
| **Evolución** (evolucionar una marca existente) | Refinar y modernizar sin perder el reconocimiento. | La equidad de marca: el símbolo, el color o la silueta reconocibles. |
| **Rebranding integral** (estrategia y nueva identidad) | Replantear estrategia (posicionamiento, propósito, público, personalidad) y crear una identidad nueva, con la pregunta de tipo de marca de "nueva". | Solo lo que la evaluación justifique; la identidad anterior es referencia. |

Reglas:
- **El alcance se aprueba antes de reemplazar ningún activo existente.** Hasta entonces se trabaja sobre copias y no se modifican los originales.
- **La decisión de conservar, evolucionar o eliminar cada elemento queda justificada** en `marca-spec.md` (tabla de la sección 0b y registro de decisiones).
- Todos los alcances terminan con manual de identidad, registro de decisiones y plan de transición (Fase 10b).

## Proceso por fases con puertas de aprobación

`brand` y `rebrand` se ejecutan como un spec por fases. **Cada fase tiene: objetivo, qué hacer, qué preguntar, entregable y criterio de aprobación. Al terminar, resume y pide aprobación**, y no avanza sin ella. Léelo en `references/proceso.md` antes de empezar: allí están el detalle de cada fase, la plantilla de `marca-spec.md` (en `.yas/brand/` por defecto) y las diferencias entre marca nueva y rebranding.

| Fase | Contenido | Variante de rebranding |
|---|---|---|
| 0 | Preparación y alcance | Igual |
| 0b | — | Evaluación inicial de la marca existente y alcance del cambio |
| 1 | Brief y estrategia | Parte de la evaluación inicial |
| 2 | Investigación y documentación | Contrasta con la marca existente |
| 3 | Exploración conceptual | Líneas de evolución (ajuste, evolución) o estrategia y conceptos (integral) |
| 4 | Bocetos y selección | Con comparación antes y después |
| 5 | Construcción de la marca gráfica | Igual |
| 6 | Color | Respeta el color reconocible |
| 7 | Tipografía | Igual |
| 8 | Versiones y activos de marca | Igual |
| 9 | Aplicaciones de marca | Con antes y después |
| 10 | Manual de identidad | Igual |
| 10b | — | Plan de transición |
| 11 | Control final y entrega | Igual |

## Subcomandos

| Subcomando | Propósito |
|---|---|
| `init` | Solo la **Fase 0** del proceso: prepara `.yas/` y la carpeta de salida, inspecciona lo que ya existe y fija el alcance. |
| `brief` | Las **Fases 0 y 1**: fija el alcance y el brief (negocio, público, objetivos, restricciones) y se detiene tras su aprobación. |
| `brand` | Identidad desde cero: el proceso completo, de la Fase 0 a la 11, hasta el **manual de identidad**. |
| `rebrand` (alias `rebranding`) | Rebranding de una marca existente: el proceso completo con la Fase 0b (evaluación inicial y alcance) y el plan de transición. |

El manual de identidad se guarda en `.yas/brand/` (ruta que `/yas-figma` ya busca como fuente de datos).

## Recursos compartidos

Estos recursos viven en `../yas-core/references/` y se usan sin copiarlos:
- `artefactos.md`: qué archivos produce esta skill y cuáles consume de las demás (el manual y la paleta son la base de `/yas-figma` y `/yas-audit`). Antes de producir un artefacto, comprueba si ya existe y complétalo.
- `criterios-calidad.md`: umbrales de accesibilidad y reglas de calidad que el diseño debe cumplir.

## Referencias externas

La lista de fuentes y sus reglas de uso están en `../yas-core/references/referencias-externas.md`. En esta skill se usan así: IBM (documentación visual del manual), Wolff Olins (`brief`, `brand`, `rebrand`), Google Brand Resource Center (fase 8 y manual), caso de LEGO (`brand`), Adobe Illustrator (fase 5) y M3 o HIG, según la plataforma, como apoyo para aplicar la identidad en interfaces y componentes (fase 9).

## Principios

- **Las decisiones se justifican:** cada elección de marca o de diseño lleva su razón, ligada al brief.
- **No inventes datos:** lo que no conste (público, competencia, Pantone) se pregunta o se marca como *pendiente de definir*.
- **Entrega archivos, no solo texto:** SVG, Markdown y HTML reales en el proyecto, con la ruta al terminar.
- **El manual de identidad es la fuente de verdad** del resto del ecosistema (`/yas-figma` lo consume; `/yas-audit` lo usa para validar).
