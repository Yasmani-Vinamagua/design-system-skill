---
name: yas-audit
description: "Audita una marca (estrategia, identidad visual y verbal, consistencia, presencia digital y sistema de activos) y entrega un informe con puntuación sobre 20 (cinco categorías de 0 a 4), hallazgos priorizados con evidencia, impacto, recomendación y validación, y acciones recomendadas con los comandos de Yas Design. Solo diagnostica; no corrige ni rediseña. Úsala cuando el usuario pida auditar, revisar, evaluar o validar una marca, su identidad o su manual, comparar con la competencia o comprobar qué mejoró tras un cambio."
argument-hint: "[estrategia | identidad-verbal | competencia | identidad-visual | consistencia | digital | sistema] [ruta | URL | adjunto]"
---

# Yas Audit

Responsabilidad: **auditar la marca**. Detecta problemas, justifica cada hallazgo con evidencia, puntúa y propone mejoras priorizadas. **No corrige nada**: documenta los problemas para que los resuelva `/yas-design`.

No se limita a decir si un logo "se ve bien": evalúa la estrategia, la identidad visual y verbal, su consistencia en los canales, la presencia digital y la calidad técnica de los activos. Juzga contra el brief y el manual aprobados, no contra preferencias personales.

## Reglas obligatorias

Antes de actuar, lee `../yas-core/references/reglas-comunes.md`: inspección inicial, contexto, ejecución, archivos, protección, calidad, documentación, transparencia y regla de alcance. Valen para toda la skill y no se repiten aquí.

**Alcance de esta skill:** diagnostica, puntúa y recomienda. **No rediseña ni corrige**, ni siquiera arreglos pequeños; las correcciones se recomiendan como comandos de `/yas-design`. Si el usuario pide auditar y corregir, primero audita, presenta el resultado y pide aprobación antes de pasar a corregir. Lo único que escribe es el informe en `.yas/audits/`.

## Recursos compartidos

Se usan los mismos criterios y los mismos archivos que `/yas-design` y `/yas-figma`; no se redefinen aquí (viven en `../yas-core/references/`):
- `artefactos.md`: de dónde sale cada dato (manual, paleta, activos del logo) y contra qué se audita.
- `criterios-calidad.md`: umbrales de contraste y accesibilidad y el método de cálculo.
- `referencias-externas.md`: Google Brand Resource Center, las plantillas de auditoría y las herramientas complementarias, con sus reglas de uso.

## Módulos y categorías

Los controles se organizan en **siete módulos independientes** que alimentan **cinco categorías puntuadas** (el detalle de cada módulo, los anclajes de puntuación y los antipatrones están en `references/modulos.md`, que se lee **antes** de puntuar):

| Categoría puntuada | Módulos |
|---|---|
| 1. Estrategia y posicionamiento | Estrategia · Identidad verbal · Competencia |
| 2. Identidad visual | Identidad visual |
| 3. Consistencia de marca | Consistencia |
| 4. Experiencia digital | Presencia digital |
| 5. Evaluación técnica de los activos | Sistema de marca |

`/yas-audit` sin argumento audita todos los módulos. Con argumento (`estrategia`, `identidad-verbal`, `competencia`, `identidad-visual`, `consistencia`, `digital`, `sistema`) audita solo esos; las categorías sin auditar quedan *no verificadas*. Si el usuario no indica qué auditar y hay varios materiales, pregunta con AskUserQuestion.

## Proceso

1. **Entrada y contexto.** Identifica qué marca se audita y reúne el material: mira de verdad las imágenes y los archivos, abre las URL, lee el manual. Lee el brief, `marca-spec.md` y la paleta si existen, porque son el criterio de comparación. Si falta algo imprescindible, pregunta solo lo mínimo; si puedes inferirlo, infiérelo y declara la suposición.
2. **Escaneo por módulos.** Ejecuta los controles de cada módulo y recoge evidencia concreta (archivo, captura, enlace con fecha, valor medido).
3. **Puntuación.** Puntúa cada categoría de 0 a 4 con los anclajes de `references/modulos.md`.
4. **Informe.** Genera el informe con la estructura de abajo y guárdalo.

### Escala de puntuación

| Puntos | Significado |
|---|---|
| 0 | Falla grave o ausente |
| 1 | Lagunas mayores |
| 2 | Parcial: hay esfuerzo, con carencias significativas |
| 3 | Bueno: cumple en lo esencial, con fallos menores |
| 4 | Ejemplar: coherente e intencional |

### Bandas de valoración (sobre 20)

| Total | Banda | Qué significa |
|---|---|---|
| 18–20 | Excelente | Solo pulido menor |
| 14–17 | Bueno | Atender las categorías débiles |
| 10–13 | Aceptable | Hace falta trabajo significativo |
| 6–9 | Pobre | Revisión profunda |
| 0–5 | Crítico | Problemas de base |

### Evidencia y honestidad

**Todo hallazgo se clasifica en uno de tres estados:**

| Estado | Qué es | Cómo se trata |
|---|---|---|
| **Comprobado** | Se observó directamente y se verificó con un método declarado (lectura del archivo, cálculo de contraste, renderizado, captura, herramienta ejecutada). | Cuenta en la puntuación y se prioriza. |
| **Hipótesis** | Es plausible por indicios, pero no se pudo comprobar. Se formula como hipótesis, con qué haría falta para confirmarla. | **No resta puntos** ni se cuenta como problema confirmado. Va en su propia sección. |
| **No verificado** | No se pudo inspeccionar por una limitación del entorno o del material. Se indica el motivo. | No se puntúa a ciegas; se declara en las limitaciones. |

**Validación visual.** Si el entorno no permite inspeccionar lo renderizado (no hay navegador, no se puede abrir la URL o la imagen, no se puede renderizar el SVG), **no afirmes que validaste visualmente el resultado**. Di que la revisión fue de archivos o de código y marca como *no verificado* lo que solo se ve renderizado: contraste efectivo, aspecto real del logo, adaptación a móvil. Indica siempre qué produjo la evidencia: lectura de archivos, renderizado, captura, herramienta (WAVE, Lighthouse) ejecutada o no.

**Reglas generales**
- **Puntúa solo lo comprobado.** Si no puedes verificar una categoría, márcala *no verificada* y no inventes una nota. El total se expresa sobre el máximo de las categorías verificadas (por ejemplo, `13/16`, con una categoría no verificada) y la banda se calcula con el mismo porcentaje.
- **Pruebas:** se marcan *verificada*, *fallida*, *no aplicable* o *no verificada*. Nunca presentes como superada una prueba que no ejecutaste.
- **Cálculos reales:** los contrastes se calculan con la fórmula WCAG y se registra la combinación concreta y su ratio; no se afirma accesibilidad por el aspecto ni por el nombre del color.
- **Percepción real:** cómo perciben la marca sus públicos solo se afirma con datos aportados (encuestas, entrevistas, analítica); si no, es hipótesis o *no verificado*.
- **Separa lo medible del juicio visual** y nombra los falsos positivos que descartaste tras verificar en contexto.
- **No afirmes** significados culturales, datos de mercado o requisitos legales que no puedas respaldar. Una evaluación visual no sustituye una búsqueda legal de marcas registradas.

## Informe

Presenta el informe en pantalla y guárdalo en `.yas/audits/<AAAA-MM-DD>-marca.md`. Estructura:

### 1. Puntuación de salud

| # | Categoría | Puntos | Hallazgo clave |
|---|---|---|---|
| 1 | Estrategia y posicionamiento | ?/4 | Problema más crítico, o "—" |
| 2 | Identidad visual | ?/4 | |
| 3 | Consistencia de marca | ?/4 | |
| 4 | Experiencia digital | ?/4 | |
| 5 | Evaluación técnica de los activos | ?/4 | |
| **Total** | | **??/20** | **Banda** |

### 2. Veredicto de coherencia
**Empieza aquí.** Aprobado o no aprobado: ¿la marca expresa una identidad coherente y propia, y respeta lo aprobado en el brief y el manual? Cita evidencia verificada.

### 3. Resumen ejecutivo
- Puntuación: **??/20** (banda).
- Cantidad de problemas comprobados por prioridad (crítica P0, alta P1, media P2, baja P3), y cuántas hipótesis y aspectos no verificados quedan.
- Los 3-5 problemas más críticos.
- Siguientes pasos recomendados.

### 4. Cobertura, pruebas y comprobaciones
Qué módulos se auditaron y qué muestra de piezas, competidores y canales se revisó (con enlaces y fecha de consulta). Tabla con cada prueba ejecutada y su estado (verificada, fallida, no aplicable, no verificada), más las limitaciones: qué no se pudo comprobar y por qué.

### 5. Hallazgos

Cada hallazgo comprobado usa este formato, con **todos** los campos:

```markdown
**[P?] Título corto**
- Estado: comprobado
- Categoría y módulo: <una de las cinco categorías> · <módulo>
- Problema: qué está mal.
- Evidencia: dónde se observa (archivo, pieza, URL, pantalla) y cómo se verificó (lectura de archivo, cálculo de contraste con la combinación y su ratio, renderizado, captura, herramienta ejecutada).
- Impacto: por qué afecta a la marca, al usuario o al sistema.
- Prioridad: crítica | alta | media | baja — y el criterio de la tabla que se aplicó.
- Recomendación: qué debería cambiarse, de forma concreta.
- Validación: cómo comprobar que se resolvió (una comprobación repetible: por ejemplo, "contraste de #XXXXXX sobre #YYYYYY ≥ 4,5:1" o "el SVG negativo se abre y conserva los huecos"; y volver a ejecutar `/yas-audit`).
- Comando sugerido: <comando del ecosistema, o "sin comando propio">
```

**Criterios de prioridad** (se aplican de forma explícita y se cita cuál motivó la asignación):

| Prioridad | Equivalencia | Criterio |
|---|---|---|
| **Crítica** | P0 | Impide que la marca funcione (ilegible en su tamaño mínimo, sin versión a una tinta, nombre o marca confundible con otra del sector) o excluye a usuarios (incumple WCAG A). Corregir de inmediato. |
| **Alta** | P1 | Degrada claramente la identidad, incumple WCAG AA, o contradice el brief o el manual aprobados, y afecta a un canal principal o a muchas piezas. Corregir antes de publicar. |
| **Media** | P2 | Debilidad con alternativa razonable o que afecta a canales secundarios o a pocas piezas. Corregir en la siguiente pasada. |
| **Baja** | P3 | Pulido sin impacto real. Si hay tiempo. |

Las hipótesis y los aspectos no verificados **no llevan prioridad**: se listan aparte (sección 6).

### 6. Hipótesis y aspectos no verificados

Dos listas separadas de los hallazgos comprobados:

- **Hipótesis:** qué se sospecha, en qué indicios se basa, qué impacto tendría si fuera cierta y **qué haría falta para comprobarla** (una prueba concreta, acceso, datos de percepción, una herramienta). No se puntúan.
- **No verificado:** qué no se pudo inspeccionar y por qué (por ejemplo, "no se pudo abrir la web: contraste efectivo y adaptación a móvil quedan sin verificar").

### 7. Patrones y problemas sistémicos
Problemas recurrentes que indican una carencia de base y no un descuido puntual (por ejemplo, "el logo aparece con tres versiones distintas en seis canales: no hay reglas de uso"; "el color de marca no alcanza 4,5:1 sobre blanco en ninguna pieza de texto").

### 8. Hallazgos positivos
Qué funciona y conviene conservar y replicar. Es obligatorio: una auditoría sin aciertos no es fiable.

### 9. Acciones recomendadas
Lista priorizada (P0, P1, P2) de comandos **solo del ecosistema Yas**, con el contexto concreto del hallazgo:

| Tipo de hallazgo | Comando |
|---|---|
| Ejecución visual (construcción, versiones, legibilidad) | `/yas-design rebrand` con alcance *ajuste* |
| Estrategia, concepto, mensaje o diferenciación | `/yas-design rebrand` (evolución o integral) o `/yas-design brief` |
| Color, tipografía, versiones, reglas de uso o manual | `/yas-design brand` (fases 6, 7, 8 y 10) |
| Consistencia entre canales | `/yas-design rebrand` con alcance *ajuste*, y actualizar los activos según el plan de transición |
| Presencia digital (accesibilidad, adaptación, rendimiento) | Sin comando propio en el ecosistema: se describe la corrección concreta en la recomendación del hallazgo, sin nombrar un comando |

Termina con la nota: se puede pedir ejecutar las acciones una a una o en el orden que prefiera el usuario, y **volver a ejecutar `/yas-audit` tras los cambios** para ver mejorar la puntuación.

### Comparación con auditorías anteriores
Si ya existe un informe en `.yas/audits/`, añade una línea con la puntuación anterior, la actual y la diferencia por categoría. No compares auditorías con categorías no verificadas distintas sin decirlo.

## Principios

- **Diagnostica, no corrijas.** Ni siquiera arreglos pequeños: se documentan.
- **Sé exhaustivo pero útil.** Demasiados hallazgos de prioridad baja son ruido; centra el informe en lo que importa.
- **Cada hallazgo explica su impacto** y propone una acción específica; nada de recomendaciones genéricas.
- **Prioriza:** no todo puede ser crítico.
- **Verifica antes de reportar:** un falso positivo sin verificar resta credibilidad. Lo que no puedas comprobar es hipótesis o no verificado, nunca un hallazgo confirmado.
- **No afirmes validación visual** si no pudiste inspeccionar el resultado renderizado, ni resultados de herramientas que no ejecutaste.
- **Compara contra lo aprobado:** el brief, el manual y la paleta son el criterio; las guías oficiales de una marca (por ejemplo, las de Google) son estándares de comparación para esa marca, no reglas universales para todos los logos. Cita la fuente consultada; si no carga, marca el dato como *no verificado*.
