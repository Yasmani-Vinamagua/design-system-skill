# Módulos de la auditoría de marca

La auditoría no se limita a decir si un logo "se ve bien": detecta problemas, justifica cada hallazgo y propone mejoras priorizadas. Los controles se organizan en **siete módulos independientes** que se agrupan en **cinco categorías puntuadas** (cada una de 0 a 4, total sobre 20).

## De los módulos a las categorías

| Categoría puntuada | Módulos que la alimentan |
|---|---|
| 1. Estrategia y posicionamiento | Estrategia · Identidad verbal · Competencia |
| 2. Identidad visual | Identidad visual |
| 3. Consistencia de marca | Consistencia |
| 4. Experiencia digital | Presencia digital |
| 5. Evaluación técnica de los activos | Sistema de marca |

Un módulo se puede auditar por separado. Las categorías cuyos módulos no se auditaron aparecen como *no verificadas* (no se puntúan).

## Entrada y contexto

- **Si la marca salió de `/yas-design`:** `marca-spec.md`, la paleta, el manual y los SVG de `.yas/brand/` (o la ruta de `.yas/brand-source.json`). El brief y las decisiones aprobadas son el criterio de comparación.
- **Si la marca es ajena:** logo (imagen, PDF o SVG), manual si existe, URL de la web y de las redes, materiales visibles. Mira de verdad cada archivo; lo que no puedas ver es *no verificable*.
- **Contexto mínimo antes de puntuar,** en cuatro líneas: qué hace la marca y su sector, público, competencia directa (3-6 marcas; búscalas si el usuario no las da) y objetivo de la auditoría (lanzar, rediseñar, evaluar, comparar).
- **Percepción real.** Cómo ven la marca sus públicos solo se puede afirmar con datos aportados (encuestas, entrevistas, analítica, reseñas). Sin ellos, queda como hipótesis o *no verificado*; no se infiere de la apariencia.

## Módulos

### Estrategia
**Evalúa:** propósito, propuesta de valor, público y posicionamiento.
**Comprobar:** que la marca tiene una idea clara y un solo mensaje; que responde al brief y a los objetivos; que el público está definido y la identidad lo sirve; durabilidad (simple, atemporal, no dependiente de modas); en un rediseño, que se respeta la equidad de marca.

### Identidad verbal
**Evalúa:** nombre, tono de voz, mensajes, eslogan y claridad.
**Comprobar:** escritura exacta del nombre (mayúsculas, acentos, signos) y su coherencia en todo el material; facilidad de pronunciación y de recuerdo; tono de voz coherente con la personalidad aprobada; mensajes clave y eslogan claros y verificables; claridad de lo que la marca hace. La disponibilidad legal del nombre **no** se evalúa aquí (requiere una búsqueda de marcas registradas).

### Competencia
**Evalúa:** diferenciación, códigos visuales compartidos y posicionamiento relativo.
**Comprobar:** 3-6 competidores relevantes (o justificar una muestra menor), con enlaces y fecha de consulta; separar observaciones directas de interpretaciones; comparar logos, paletas por familias cromáticas, tipografías y tono; detectar patrones compartidos del sector y oportunidades de diferenciación. No forzar un "hueco de color" si la evidencia no lo respalda; cuando los ejes sean justificables, un mapa de posicionamiento de dos ejes.

### Identidad visual
**Evalúa:** logo, isotipo, color, tipografía, composición e imágenes.
**Comprobar:**
- **Logo:** concepto y relación con el brief; construcción (retícula, geometría, espacio negativo como huecos reales, trazados limpios, equilibrio, silueta); coherencia entre símbolo y nombre.
- **Color:** paleta funcional y diferenciadora; **contraste calculado** de las combinaciones declaradas; valores HEX y RGB coherentes; CMYK y Pantone presentados solo como referencia.
- **Tipografía:** carácter y coherencia con el símbolo; legibilidad pequeña; jerarquía; licencias registradas sin afirmar lo no verificado.
- **Composición e imágenes:** estilo fotográfico, iconografía, patrones y recursos de apoyo coherentes con el sistema.

### Consistencia
**Evalúa:** aplicación de la identidad en web, redes, documentos, publicidad y material físico.
**Comprobar:** en una muestra declarada de piezas (con enlace o archivo y fecha), si usan el mismo logo y versiones, la misma paleta, las mismas tipografías y el mismo tono; desviaciones entre canales; uso de versiones no oficiales; si el logo conserva su legibilidad y no se deforma. Solo se afirma consistencia de lo que se vio; lo demás es *no verificado*.

### Presencia digital
**Evalúa:** web, redes, legibilidad, accesibilidad y adaptación a dispositivos.
**Comprobar:** legibilidad y contraste efectivo del texto y de los componentes (calculado, con la combinación concreta); accesibilidad básica (etiquetas, estructura, foco, textos alternativos); adaptación a móvil y tablet; favicon, avatar y vista previa al compartir; rendimiento percibido. Umbrales y cálculo en `../../yas-core/references/criterios-calidad.md`.

**Herramientas complementarias**, si están disponibles en el entorno (no sustituyen la revisión ni determinan si la marca está bien posicionada):

| Herramienta | Para qué sirve | Enlace |
|---|---|---|
| WAVE | Problemas de accesibilidad web: contraste, etiquetas, estructura | https://wave.webaim.org/ |
| Lighthouse | Rendimiento, accesibilidad, buenas prácticas y SEO | https://developer.chrome.com/docs/lighthouse/overview?hl=es-419 |

Si no puedes ejecutarlas, o no hay acceso a la web, **no afirmes sus resultados**: marca esas comprobaciones como *no verificadas* e indica qué herramienta las confirmaría.

### Sistema de marca
**Evalúa:** variantes, activos disponibles, reglas de uso y documentación, y su calidad técnica.
**Comprobar:**
- **Variantes:** existen las necesarias con los nombres de la tabla de `yas-design/references/construccion-logo.md` sección 4 (una tinta negra y blanca, negativa, horizontal y vertical si hay texto, icono, reducida si hace falta); coherencia entre variantes.
- **Activos y organización:** los archivos están disponibles, ordenados y con nombres previsibles, como en un centro de recursos de marca.
- **Reglas de uso:** área de respeto y tamaño mínimo **basados en pruebas**, usos incorrectos ilustrados, combinaciones permitidas sobre fondos.
- **Documentación:** manual completo frente a `yas-design/references/manual-plantilla.md` (sus 11 secciones y su lista de comprobación); datos idénticos en todas las secciones; rutas y enlaces que funcionan; pendientes declarados; versión y registro de cambios.
- **Calidad técnica:** SVG válidos que se abren y no dependen de recursos externos; texto convertido a trazados o declarado como dependiente de fuente; pruebas de la sección 5 de `construccion-logo.md` que apliquen (negro al 100 %, negativa, tamaño reducido a 16 px y 2 cm, silueta, equilibrio, espacio negativo, contraste, producción física como revisión preliminar, integridad del archivo, consistencia, diferenciación).

## Anclajes de puntuación por categoría

| Categoría | 0 | 2 | 4 |
|---|---|---|---|
| 1. Estrategia y posicionamiento | Sin idea, público ni mensaje, o sin relación con el brief | Idea presente pero genérica, poco diferenciada o con mensajes poco claros | Estrategia clara, diferenciada, verbal y conceptualmente coherente |
| 2. Identidad visual | Construcción deficiente o paleta y tipografía sin criterio | Funciona con irregularidades, contraste sin verificar o inconsistencias | Sistema visual preciso, verificado y coherente |
| 3. Consistencia de marca | Cada pieza usa una marca distinta | Coherente en lo principal con desviaciones notables entre canales | Aplicación consistente en todos los canales vistos |
| 4. Experiencia digital | Ilegible, inaccesible o roto en móvil | Funciona con carencias de accesibilidad o adaptación | Legible, accesible y adaptada, comprobado |
| 5. Evaluación técnica de los activos | Sin versión a una tinta, ni reglas, ni manual; archivos inservibles | Variantes básicas con reglas sin probar o manual parcial | Conjunto completo, probado y documentado, utilizable por un tercero sin adivinar |

## Antipatrones a buscar y nombrar

- Logo que depende de degradados, sombras o efectos para sostenerse.
- Varios conceptos compitiendo en una sola marca.
- Cliché del sector sin giro propio, o símbolo que ilustra literalmente la actividad.
- Tipografía por defecto, mal espaciada o desconectada del símbolo.
- Color igual al de los líderes del sector.
- Detalle fino que desaparece al reducir.
- Falta de versión a una tinta o negativa.
- Formas blancas superpuestas en lugar de huecos.
- Estilo ligado a una moda del momento.
- Parecido accidental con otra marca (se señala como riesgo; no sustituye una búsqueda legal de marcas registradas).
- Texto como `<text>` descrito como convertido a trazados; proporción áurea afirmada sin medidas.
- Tono de voz o nombre escrito de forma distinta según el canal.

## Notas

- En un rediseño, valora la equidad de marca existente y no juzgues contra tu gusto.
- Si te piden comparar marcas, usa la misma tabla para cada una y añade una columna de conclusión.
- No rediseñes el logo: indica la dirección de la mejora.
