# Proceso por fases (spec con puertas de aprobación)

Cada fase tiene: **objetivo**, **qué hacer**, **qué preguntar**, **entregable** y **criterio de aprobación**. Al terminar, resume y pide aprobación.

Reglas de las puertas:
- **No avances de fase sin aprobación explícita.** Resume lo hecho en pocas líneas, muestra el entregable (o su ruta) y pregunta con AskUserQuestion: aprobar, pedir cambios o volver a una fase anterior.
- Cada decisión y aprobación se anota en el **Registro de decisiones** del spec (fecha, fase, decisión, motivo, estado y quién la aprobó).
- Si una fase falla su criterio, vuelve a la fase indicada; no maquilles el resultado.
- Distingue siempre lo **verificado** de lo **supuesto**; lo que no conste se pregunta o queda como *pendiente de definir* o *no verificado* (estados y precedencia en "Vocabulario y criterios de marca" de `SKILL.md`).
- Las referencias externas (ver `SKILL.md`) se consultan en la fase que las necesita y se citan en el spec.
- Agrupa las preguntas en una sola interacción cuando sea práctico y no exijas respuestas que no sean necesarias para avanzar.

**Carpeta de salida:** por defecto `.yas/brand/` (es donde `/yas-figma` busca el manual). Si el usuario elige otra, créala ahí y anota la ruta en `.yas/brand-source.json` (`manualPath`) para que el resto del ecosistema la encuentre. El spec se llama `marca-spec.md` y vive en la raíz de esa carpeta; los entregables van en `investigacion/`, `concepto/`, `logo/`, `paleta/`, `tipografia/`, `aplicaciones/` y `manual/`.

**Documentos de apoyo** (incluidos en `references/` de esta skill): `construccion-logo.md` (fase 5) y `manual-plantilla.md` (fase 10). Compruébalos en la fase 0; si falta alguno, dilo, regístralo como dependencia faltante y pide al usuario cómo proceder. No los reconstruyas de memoria.

---

## Plantilla de `marca-spec.md`

Es el documento vivo del proyecto: se crea en la fase 0 y se completa fase a fase. Las secciones marcadas *(solo rebranding)* y la línea `Alcance del cambio` son adiciones de Yas Design a la plantilla base.

```markdown
# Especificación de marca: <nombre>

- Estado general: en curso / pausada / completada
- Fase actual:
- Última actualización:
- Responsable:
- Tipo de encargo: identidad nueva / rebranding / ajuste puntual
- Alcance del cambio (solo rebranding): ajuste / evolución / rebranding integral
- Carpeta de salida:

## 0b. Evaluación inicial de la marca existente (solo rebranding)
- Inventario (logos, tipografías, colores, manuales, aplicaciones) y qué no se pudo verificar:
- Activos reconocibles a conservar:
- Problemas de ejecución visual:
- Problemas de posicionamiento:
- Alcance del cambio y justificación:
- Decisión por elemento:
  | Elemento | Decisión (conservar / evolucionar / eliminar) | Justificación |
  |---|---|---|
- Aprobación del alcance (fecha y quién):

## 1. Brief
- Descripción del negocio:
- Público:
- Necesidad u oportunidad:
- Meta principal:
- Objetivos verificables:
- Propuesta de valor y diferenciadores:
- Valores y personalidad:
- Atributos deseados:
- Atributos que se deben evitar:
- Elementos de marca que deben conservarse:
- Aplicaciones previstas:
- Restricciones:
- Plazos y presupuesto, si aplica:

## 2. Investigación
- Alcance y fecha de investigación:
- Competidores y fuentes:
- Hallazgos:
- Patrones visuales del sector:
- Oportunidades de diferenciación:
- Dirección visual propuesta:
- Limitaciones de la investigación:

## 3. Concepto
- Universos conceptuales:
- Diagramas radiales:
- Conceptos candidatos:
- Concepto seleccionado:
- Justificación:
- Riesgos y aspectos por validar:
- Estrategia (solo "estrategia y nueva identidad"): posicionamiento, propósito, público, personalidad:
- Línea de evolución (solo "evolución"): grado de cambio por elemento:

## 4. Exploración y bocetos
- Candidatos:
- Criterios de evaluación:
- Candidato elegido:
- Motivo de selección:

## 5. Construcción de la marca gráfica
- Tipo de marca gráfica: (logotipo / isotipo / imagotipo / isologo; decidido por usuario o Yas Design, y por qué)
- Retícula y proporciones:
- Geometría y trazados:
- Relaciones entre símbolo y nombre:
- Pruebas realizadas:
- Limitaciones conocidas:

## 6. Color
- Colores y valores:
- Función de cada color:
- Combinaciones aprobadas:
- Combinaciones no recomendadas:
- Contraste y reproducción:

## 7. Tipografía
- Tipografía principal:
- Tipografía secundaria:
- Licencias y fuentes:
- Escala y jerarquía:
- Usos recomendados:

## 8. Versiones y activos
- Versiones creadas:
- Tamaños mínimos:
- Área de respeto:
- Variantes reducidas:
- Formatos y rutas:
- Versiones descartadas y motivos:

## 9. Aplicaciones
- Aplicaciones seleccionadas:
- Archivos creados:
- Reglas de aplicación:
- Aspectos pendientes de validación:

## 10. Manual
- Archivos generados:
- Lista de comprobación:
- Validaciones ejecutadas:
- Pendientes:

## 10b. Plan de transición (solo rebranding)
- Orden de actualización:
- Coexistencia de versiones antiguas y nuevas:
- Materiales a retirar o agotar:
- Comunicación del cambio:
- Activos a reemplazar y riesgos:

## Registro de decisiones
| Fecha | Fase | Decisión | Motivo | Estado | Aprobada por |
|---|---|---|---|---|---|
```

Notas de uso:
- `Estado general` y `Fase actual` se actualizan al cerrar cada fase; `Última actualización` lleva la fecha real.
- **Ajuste puntual** equivale al alcance "ajuste" de la Fase 0b: solo se recorren las fases que el ajuste toca, indicando cuáles se omiten y por qué.

---

## Fase 0 — Preparación y alcance
**Objetivo:** establecer el encargo, los archivos disponibles y las condiciones de trabajo.

**Qué hacer**
1. Inspeccionar los archivos adjuntos y la carpeta de proyecto indicada.
2. Confirmar si se trata de una marca nueva, un rebranding o un ajuste puntual (y, si es nueva, aplicar la pregunta de tipo de marca de "Inicio" en `SKILL.md`).
3. Crear la carpeta de salida y `marca-spec.md`.
4. Registrar los documentos de referencia disponibles y las dependencias que faltan (incluidas `construccion-logo.md` y `manual-plantilla.md`).
5. Determinar los formatos de entrega y las aplicaciones prioritarias.

**Qué preguntar**
- ¿Cómo se llama la marca y qué hace?
- ¿Para quién existe?
- ¿Es una marca nueva o un rediseño?
- ¿Qué elementos deben conservarse?
- ¿Dónde se utilizará principalmente?
- ¿Qué carpeta debe recibir los entregables?
- ¿Hay restricciones de tiempo, presupuesto, licencias o producción?

**Entregable:** carpeta inicial y secciones conocidas de `marca-spec.md`.
**Criterio de aprobación:** el usuario confirma el alcance y el nombre de marca.

## Fase 0b — Evaluación inicial de la marca existente (solo rebranding)
**Objetivo:** entender qué hay, qué vale la pena conservar y cuánto debe cambiar antes de definir el brief. No se asume que todo deba cambiarse.

**Qué hacer**
1. **Inventariar** logos, tipografías, colores, manuales y aplicaciones existentes (adjuntos, carpetas, URL, redes, aplicaciones visibles). Mirar el material de verdad; marcar como no verificable lo que no se pueda ver.
2. **Identificar los activos reconocibles** que convenga conservar (símbolo, color, silueta, tipografía, nombre, tono).
3. **Separar los problemas de ejecución visual** (construcción, legibilidad pequeña, versiones, kerning, inconsistencia) **de los problemas de posicionamiento** (público, diferenciación, mensaje, propósito). Un problema de ejecución no justifica cambiar la estrategia, ni al revés.
4. **Definir el alcance del cambio**, que condiciona todo el resto del proceso:

| Alcance | Qué implica |
|---|---|
| **Ajuste** | Corregir ejecución sin cambiar la idea: limpiar trazados, normalizar versiones, afinar color y tipografía. Es el "ajuste puntual". |
| **Evolución** | Refinar y modernizar manteniendo el reconocimiento ("evolucionar una marca existente"): cambios por elemento con la equidad de marca intacta. |
| **Rebranding integral** | Replantear estrategia e identidad ("estrategia y nueva identidad"): la marca anterior es referencia, no punto de partida. |

5. **Registrar por elemento** si se conserva, se evoluciona o se elimina, con su justificación, en la sección 0b de `marca-spec.md`.
6. **Obtener la aprobación del alcance antes de reemplazar cualquier activo existente.** Hasta entonces, trabaja sobre copias en la carpeta de salida y no modifiques ni sobrescribas los archivos originales de la marca.

**Qué preguntar**
- ¿Por qué se plantea el cambio ahora? ¿Qué cambió en el negocio, el público o el mercado?
- ¿Qué querría conservar el cliente y qué le molesta?
- ¿Qué activos están muy extendidos o registrados y no pueden cambiar?
- ¿Qué materiales seguirán circulando durante la transición?
- ¿Existe un manual o archivos originales (vectores, fuentes)?

Para una evaluación profunda de la marca actual, sugiere `/yas-audit`; no afirmes que se hizo hasta ejecutarlo.
**Entregable:** sección 0b de `marca-spec.md` con inventario, problemas separados, alcance y tabla de decisión por elemento.
**Criterio de aprobación:** el usuario aprueba el alcance y la decisión de conservar, evolucionar o eliminar cada elemento.

## Fase 1 — Brief y estrategia
**Objetivo:** convertir la idea en una dirección de marca concreta y evaluable.

**Qué hacer**
1. Redactar una frase que defina la meta principal.
2. Formular entre 3 y 5 objetivos observables o verificables.
3. Describir el público, sus necesidades y el contexto de uso.
4. Identificar propuesta de valor, diferenciadores, valores y personalidad.
5. Registrar atributos deseados y atributos que deben evitarse.
6. Definir restricciones de larga duración: legibilidad, simplicidad, reproducción, escalabilidad y vigencia.
7. Para un rebranding, partir de la evaluación inicial (Fase 0b): qué funciona, qué no funciona y qué debe conservarse, y alinear el brief con el alcance aprobado.

**Qué preguntar**
- ¿Qué tres adjetivos describen la marca y cuáles no deberían describirla?
- ¿Qué referentes gustan y cuáles no? ¿Por qué?
- ¿Qué colores o recursos se deben mantener o evitar?
- ¿Qué hace diferente a la marca?
- ¿En qué soportes debe funcionar: pantalla, impresión, bordado, grabado, señalética u otros?

No convertir preferencias aisladas en decisiones definitivas sin relacionarlas con el brief.
**Referencia:** Wolff Olins (cómo se plantea la idea y el propósito de una marca).
**Entregable:** sección Brief de `marca-spec.md`.
**Criterio de aprobación:** meta, objetivos, público y dirección estratégica confirmados.

## Fase 2 — Investigación y documentación
**Objetivo:** comprender el contexto competitivo y encontrar oportunidades de diferenciación.

**Qué hacer**
1. Identificar entre 4 y 6 competidores relevantes cuando existan suficientes fuentes fiables. Si no los hay, justificar el tamaño de la muestra.
2. Utilizar competidores aportados por el usuario y, si se autoriza o resulta necesario, buscar fuentes públicas.
3. Analizar identidad gráfica, color, tipografía, tono, aplicaciones y posicionamiento observable.
4. Registrar enlaces y fecha de consulta. Separar observaciones directas de interpretaciones.
5. Comparar las paletas por familias cromáticas y detectar saturaciones, patrones y posibles oportunidades. No forzar un "hueco de color" si la evidencia no lo respalda.
6. Considerar un mapa de posicionamiento de dos ejes cuando los ejes puedan justificarse.
7. Describir el moodboard en palabras: referencias, texturas, imágenes, composición y atmósfera; no copiar activos de terceros.

**Entregable:** `investigacion/competidores.md` y sección Investigación de `marca-spec.md`, con tabla comparativa, fuentes y oportunidades.
**Criterio de aprobación:** el usuario confirma los hallazgos relevantes y la dirección visual propuesta.

**Rebranding:** el diagnóstico de la marca actual ya se hizo en la Fase 0b; aquí solo se añade la investigación competitiva y se contrasta con la marca existente.

## Fase 3 — Exploración conceptual
**Objetivo:** generar conceptos relevantes, distintos y no limitados a las primeras asociaciones obvias.

**Qué hacer**
1. Definir entre 2 y 3 universos conceptuales derivados del brief.
2. Desarrollar diagramas radiales de tres niveles: idea central, asociaciones primarias y asociaciones secundarias.
3. Explorar el nombre, sus letras, sonidos, significado, historia y atributos como fuentes de ideas.
4. Cruzar ideas de universos distintos y redactar una frase que explique cada cruce útil.
5. Seleccionar tres conceptos realmente diferentes, no meras variaciones de color o composición.
6. Para cada concepto, documentar idea central, relevancia, traducción visual, fortalezas y riesgos.
7. Recomendar uno con criterios explícitos, sin ocultar las ventajas de las alternativas.
8. Si el tipo de marca gráfica quedó en "lo decide Yas Design", proponerlo aquí con su justificación y la alternativa más cercana (ver "Inicio" en `SKILL.md`), para que los bocetos partan de él.

**Presentación:** diagramas como listas anidadas; tabla de tres conceptos candidatos; recomendación razonada.
**Referencia:** el caso de LEGO en Logo Design Love (de la idea a un sistema visual coherente).
**Entregable:** `concepto/diagramas-radiales.md`, `concepto/conceptos.md` y actualización del spec.
**Criterio de aprobación:** el usuario selecciona un concepto, solicita una combinación concreta o autoriza una nueva exploración.

**Rebranding:** según el alcance aprobado en la Fase 0b. En **ajuste** y **evolución**, sustituye los conceptos por 2-3 **líneas de evolución** (grado de cambio por elemento; qué conserva cada una, qué cambia y el riesgo de perder reconocimiento) y recomienda una, respetando la decisión por elemento de la sección 0b. En **rebranding integral**, antes de los conceptos redacta el nuevo posicionamiento, propósito, público y personalidad, que el concepto debe expresar.

## Fase 4 — Bocetos y selección
**Objetivo:** comprobar el potencial de las ideas antes de invertir esfuerzo en el arte final.

**Qué hacer**
1. Describir entre 6 y 12 bocetos y producir exploraciones vectoriales muy simples en `logo/exploracion/`.
2. Priorizar el mensaje, la silueta y la idea. No usar color ni tipografía final para compensar una idea débil.
3. Evaluar los bocetos por relevancia, simplicidad, distinción, legibilidad a tamaño pequeño y potencial de aplicación.
4. Seleccionar tres candidatos y explicar diferencias reales entre ellos.
5. Si se generan SVG exploratorios, identificarlos claramente como bocetos no finales.

**Entregable:** bocetos y matriz de evaluación.
**Criterio de aprobación:** el usuario selecciona un candidato —o dos para una comparación controlada— antes de construir el arte final.

**Rebranding:** parte de la marca actual y muestra la comparación antes y después; no reemplaza ningún activo existente sin el alcance aprobado.

## Fase 5 — Construcción de la marca gráfica
**Objetivo:** construir una propuesta vectorial consistente y técnicamente comprobable, inicialmente a una tinta.

**Dependencia obligatoria:** leer `references/construccion-logo.md` (incluida en esta skill) antes de ejecutar esta fase. Aplicar sus instrucciones compatibles con el brief y registrar cualquier conflicto o limitación. Si no se encuentra, aplicar la regla de dependencias faltantes.
**Referencia:** Adobe Illustrator (dibujo vectorial, geometría, trazados y archivos escalables).

**Qué hacer**
1. Confirmar si el encargo requiere logotipo, isotipo, imagotipo o isologo; explicar la elección (si ya se decidió en la fase 0 o 3, registrarla aquí).
2. Definir retícula, proporciones, relaciones geométricas, grosores, radios y ángulos que tengan una función demostrable.
3. Construir el símbolo y el nombre en SVG cuando sea posible.
4. Usar trazados y huecos reales cuando la geometría lo requiera; evitar depender de formas blancas superpuestas que fallen sobre fondos de color.
5. Mantener la construcción editable y organizada. Evitar complejidad innecesaria y puntos de ancla superfluos.
6. Documentar las medidas relevantes. No afirmar que se usa proporción áurea salvo que exista una construcción verificable y justificada.
7. Generar una vista previa para facilitar la revisión.

**Pruebas:** ejecutar las de la sección 5 de `construccion-logo.md` (negro al 100 %, negativa, tamaño reducido, silueta, equilibrio, espacio negativo, tipografía, contraste, producción física, integridad del archivo, consistencia y diferenciación frente a la competencia estudiada) y marcar cada una con el estado definido allí. Una evaluación visual no sustituye una búsqueda legal de marcas registradas.

**Entregable:** `logo/logo-master.svg` (fuente maestra), `logo/logo-1tinta-negro.svg`, vistas previas y documentación de construcción, con las pruebas marcadas como verificada, fallida, no aplicable o no verificada y el registro de entrega de la sección 8 de `construccion-logo.md`.
**Criterio de aprobación:** el usuario aprueba el diseño a una tinta. Si no funciona, volver a la Fase 4.

## Fase 6 — Color
**Objetivo:** definir una paleta funcional, diferenciadora y reproducible.

**Qué hacer**
1. Proponer un color principal, entre uno y dos colores de apoyo y los neutros necesarios, de acuerdo con la estrategia y la investigación (en evolución, respetando el color reconocible).
2. Documentar nombre, función y valores HEX y RGB.
3. Añadir valores CMYK solo como conversiones de referencia, indicando que pueden variar según perfil ICC, proceso y soporte de impresión.
4. Si se propone un Pantone aproximado, identificarlo como referencia provisional y recomendar verificarlo con una guía física vigente, especificando coated o uncoated según el soporte. Si no puede determinarse con fiabilidad, escribir *pendiente de definir* (regla de valores de color en `SKILL.md`).
5. Definir proporciones orientativas de uso, combinaciones aprobadas y combinaciones que deben evitarse.
6. Comprobar contraste para texto e interfaz cuando corresponda, e identificar los fondos en los que el logo pierde legibilidad.
7. Si hay degradados, documentar colores, posiciones y dirección, además de una alternativa sólida.
8. Producir exploraciones vectoriales muy simples con cada paleta propuesta para que el usuario tenga una noción del resultado.
9. Anticipar los roles semánticos (acción, éxito, aviso, error, información) que necesitará el sistema de diseño.

No afirmar que un color es accesible solo por su nombre o apariencia: registrar la combinación concreta y el resultado del cálculo de contraste cuando sea aplicable.

**Entregable:** `paleta/paleta.md` y actualización del spec. `paleta.md` incluye siempre la tabla de colores del contrato de `../../yas-core/references/artefactos.md` (Nombre, Rol, HEX, RGB, CMYK de referencia, Pantone aproximado), que es la que lee `/yas-figma colors`.
**Criterio de aprobación:** el usuario aprueba la paleta, sus funciones y las combinaciones principales.

## Fase 7 — Tipografía
**Objetivo:** elegir un sistema tipográfico coherente con la personalidad, el logo y los usos de la marca.

**Qué hacer**
1. Preseleccionar cinco tipografías adecuadas, priorizando licencias compatibles con el uso previsto.
2. Registrar nombre, proveedor, licencia y disponibilidad de los archivos necesarios (incluida su disponibilidad para web y para Figma).
3. Comparar formas, terminales, proporciones, ritmo, pesos y legibilidad. Utilizar muestras de caracteres representativas; no limitar la evaluación a tres letras.
4. Seleccionar tres finalistas y recomendar un sistema final.
5. Definir tipografía de títulos, texto y, solo si es necesario, una tipografía auxiliar.
6. Especificar pesos, jerarquía, tamaños, interlineado y usos.
7. Comprobar la compatibilidad visual con el símbolo y la legibilidad en tamaños pequeños.

**Entregable:** `tipografia/sistema-tipografico.md` y actualización del spec.
**Criterio de aprobación:** el usuario aprueba las familias, sus usos y la jerarquía tipográfica.

## Fase 8 — Versiones y activos de marca
**Objetivo:** preparar las variantes realmente necesarias y documentar sus límites de uso.
**Referencia:** Google Brand Resource Center (organización de activos, versiones y restricciones de uso).

**Qué hacer**
1. Crear las versiones que funcionen, derivadas del maestro `logo-master.svg`, con los nombres y criterios de la tabla de la sección 4 de `construccion-logo.md` (fuente única de nombres de archivo). No generar todas si el encargo no las necesita: solo las útiles para los usos definidos, documentando las omitidas y por qué.
2. Mantener separados el maestro, las exportaciones y las vistas previas, con rutas previsibles.
3. Definir área de respeto y tamaños mínimos a partir de pruebas reales; evitar cifras arbitrarias.
4. Crear una versión reducida simplificada solo si el diseño principal no funciona a tamaños pequeños.
5. Descartar las variantes que fallen y documentar la razón.
6. Verificar que los archivos SVG se abran y que no dependan de recursos externos inesperados.

**Entregable:** SVG finales organizados en `logo/` y registro de variantes en el spec.
**Criterio de aprobación:** el usuario aprueba el conjunto de versiones y sus reglas de uso.

## Fase 9 — Aplicaciones de marca
**Objetivo:** demostrar que la identidad funciona en contextos representativos y consistentes.

**Qué hacer**
1. Seleccionar entre 6 y 10 aplicaciones adecuadas al negocio, los usuarios y los canales prioritarios.
2. Priorizar las aplicaciones de mayor valor; no producir mockups irrelevantes solo para completar una cantidad.
3. Crear composiciones en SVG, HTML u otros formatos compatibles con las herramientas disponibles.
4. Mantener consistencia en logo, paleta, tipografía y recursos gráficos, evitando repetir una misma composición sin adaptación.
5. Incluir al menos un documento de uso real con la identidad aplicada, por ejemplo una carta, propuesta, ficha o documento comercial, si es pertinente.
6. Diferenciar claramente los mockups ilustrativos de los archivos listos para producción.
7. Indicar las especificaciones que necesitan revisión física o técnica.

**Entregable:** archivos en `aplicaciones/` y registro de las aplicaciones aprobadas.
**Criterio de aprobación:** el usuario aprueba la selección y las aplicaciones representativas.

**Rebranding:** mostrar también antes y después de las aplicaciones clave.

## Fase 10 — Manual de identidad
**Objetivo:** consolidar decisiones y reglas en un documento claro que pueda utilizar otra persona, y que sea la fuente de datos de `/yas-figma`.
**Referencia:** IBM Design Language (documentación visual).

**Dependencia obligatoria:** leer `references/manual-plantilla.md` (incluida en esta skill) antes de redactar el manual. Conservar su estructura requerida y proponer modificaciones solo si se detectan omisiones o contradicciones. Si no se encuentra, aplicar la regla de dependencias faltantes.

**Qué hacer**
1. Generar `manual/manual-identidad.md` a partir de las decisiones aprobadas en el spec.
2. Generar `manual/manual-identidad.html` autocontenido, con estilos y recursos incrustados o rutas relativas válidas (salvo que el usuario haya pedido solo Markdown; `/yas-figma` puede leer ambos formatos).
3. Incluir ejemplos visuales reales del proyecto, no marcadores genéricos presentados como resultado final.
4. Verificar coherencia entre nombre, versiones, códigos de color, tipografías, tamaños y aplicaciones.
5. Incluir, cuando aplique:
   - Versiones aprobadas.
   - Área de respeto y tamaños mínimos.
   - Paleta con HEX, RGB, CMYK de referencia y Pantone aproximado, si se ha definido.
   - Sistema tipográfico y licencias.
   - Usos incorrectos.
   - Aplicaciones y ejemplos.
   - Reglas de reproducción y limitaciones conocidas.
6. Comprobar enlaces, imágenes y rutas locales del HTML.
7. Registrar las pruebas realizadas y los puntos que requieren validación humana o física.

**Entregable:** `manual/manual-identidad.md`, `manual/manual-identidad.html` y lista de comprobación final.
**Criterio de aprobación:** el usuario aprueba el manual y recibe un resumen de los archivos entregados y pendientes.

## Fase 10b — Plan de transición (solo rebranding)
**Objetivo:** que el cambio se implante sin romper el reconocimiento.
**Qué hacer:** definir el orden de actualización, la coexistencia de versiones antiguas y nuevas, qué materiales se retiran y cuáles se agotan, cómo se comunica el cambio, y listar activos a reemplazar y riesgos.
**Qué preguntar:** fechas clave, canales y materiales en circulación, quién debe aprobar el cambio.
**Entregable:** sección 10b del spec y `manual/transicion.md`.
**Criterio de aprobación:** plan y calendario confirmados.

## Fase 11 — Control final y entrega
**Objetivo:** asegurar que los archivos estén completos, organizados y sean utilizables.

**Lista de comprobación**
- [ ] El nombre y la estrategia corresponden al brief aprobado.
- [ ] El concepto y el logo cuentan con aprobación.
- [ ] Existe una versión monocromática funcional.
- [ ] Se incluyen las versiones horizontal, vertical o reducida que realmente funcionan.
- [ ] Los archivos vectoriales se abren correctamente.
- [ ] La paleta incluye valores y reglas de uso documentadas.
- [ ] Las tipografías y licencias están registradas.
- [ ] Los tamaños mínimos y el área de respeto se basan en pruebas.
- [ ] Se documentan usos incorrectos.
- [ ] Las aplicaciones utilizan los activos oficiales aprobados.
- [ ] El manual Markdown y el HTML son coherentes.
- [ ] Las rutas y recursos del manual HTML funcionan.
- [ ] Se registran las validaciones no realizadas y las limitaciones.
- [ ] Se entrega un índice de archivos y su finalidad.
- [ ] (Rebranding) El alcance y la decisión por elemento están aprobados y justificados en `marca-spec.md`.
- [ ] (Rebranding) El plan de transición está aprobado.

**Siguientes pasos que se ofrecen** (solo ofrecerlos si la skill correspondiente está disponible; nunca afirmar que se hicieron hasta haberlos ejecutado):
- **Auditoría:** `/yas-audit` sobre el resultado.
- **Design system en Figma:** `/yas-figma mini` o `/yas-figma full` lo generan a partir del manual y lo crean en Figma si el MCP está instalado; si no, lo dejan en local. `/yas-figma push` carga a Figma uno ya generado.
- **HTML del design system** solo a partir del manual: `/yas-figma documentation manual`.

**Entrega final:** resumir los archivos creados, las decisiones aprobadas, las pruebas ejecutadas y los pendientes. No declarar el proyecto completamente terminado si existen aprobaciones o validaciones importantes sin resolver.
