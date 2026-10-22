# Plantilla del manual de identidad

## Propósito y alcance

Esta plantilla define la estructura, el contenido mínimo y los criterios de presentación del manual de identidad de la marca. Debe completarse con las decisiones aprobadas en el brief, los specs del proyecto y los archivos finales de identidad.

El manual debe explicar qué regla se debe seguir, cómo aplicarla y por qué existe. No inventes decisiones, valores, justificaciones, archivos ni pruebas que no estén respaldados por el proyecto. Si un dato está pendiente, márcalo como *pendiente de definir* (no consta) o *no verificado* (consta pero no se comprobó), según el vocabulario de `SKILL.md`, y regístralo en la lista de pendientes.

El manual documenta el sistema de identidad aprobado; no debe introducir cambios conceptuales ni redefinir la marca por iniciativa propia.

## Criterios editoriales y visuales

- Mantén el nombre de la marca, su escritura, mayúsculas, acentos y tagline consistentes en todo el documento.
- Utiliza la paleta, tipografía, recursos gráficos y tono visual oficiales. El propio manual debe funcionar como una aplicación de la identidad.
- Para cada regla relevante, incluye una justificación basada en el brief, el concepto aprobado, una decisión documentada o una prueba realizada.
- Distingue los hechos verificados de las recomendaciones y los valores provisionales.
- Usa ejemplos visuales claros, con etiquetas y anotaciones legibles.
- Evita repetir información: si un dato aparece en varias secciones, mantenlo idéntico en todas.
- Usa rutas relativas que funcionen desde la ubicación del archivo final. Verifica que los recursos referenciados existan.
- Si una sección no aplica, indícalo brevemente y explica el motivo cuando sea necesario; no la rellenes con contenido genérico.

## Índice

1. Introducción
2. El logo
3. Construcción
4. Versiones
5. Área de respeto y tamaño mínimo
6. Usos incorrectos
7. Color
8. Tipografía
9. Aplicaciones
10. Estructura gráfica y recursos
11. Entregables y contacto

## 1. Introducción

Incluye:

- **Propósito del manual:** qué regula y a quién va dirigido.
- **Descripción de la marca:** qué es, qué hace y a quién sirve.
- **Valores y personalidad:** utiliza los atributos acordados en el brief.
- **Concepto del logo:** sintetiza la idea aprobada en una frase clara.
- **Nombre oficial:** registra la escritura exacta de la marca, incluyendo mayúsculas, acentos, signos y tagline cuando corresponda.

No inventes valores de marca, públicos ni atributos que no estén documentados.

## 2. El logo

Incluye:

- **Logo principal** en un tamaño destacado sobre un fondo que permita apreciarlo sin interferencias.
- **Anatomía:** identifica y nombra las partes reales del sistema, por ejemplo símbolo, nombre y tagline. No atribuyas componentes que el logo no tenga.
- **Concepto:** explica brevemente la idea de la que nace la propuesta y por qué se eligió frente a las alternativas registradas.
- **Decisiones formales:** explica qué comunican las formas, proporciones, contraformas y relaciones entre los elementos, sin atribuir significados que no estén justificados por el proceso.

Usa el concepto y las decisiones aprobadas; no reconstruyas una historia ficticia después de diseñar el logo.

## 3. Construcción

Documenta los criterios reales de construcción:

- Retícula y unidad base `u`, con sus medidas.
- Proporciones y relaciones entre los elementos.
- Radios, ángulos, grosores y alineaciones relevantes.
- Ajustes ópticos que se aparten de la retícula geométrica.
- Diagrama de construcción con líneas guía y anotaciones legibles.

La proporción áurea u otros sistemas geométricos solo deben mencionarse si su uso puede demostrarse con medidas en el arte final. No superpongas retículas decorativas para justificar una forma construida de otra manera.

## 4. Versiones

Muestra cada versión aprobada, su nombre de archivo y sus usos previstos.

| Versión | Archivo | Uso previsto |
|---|---|---|
| Positiva a color | `logo-color.svg` | Fondos claros y uso general, cuando el contraste sea suficiente. |
| Negativa a color | `logo-negativo.svg` (o `logo-negativo-<nombre-color>.svg`) | Fondos corporativos u oscuros aprobados. |
| Una tinta negra | `logo-1tinta-negro.svg` | Aplicaciones monocromáticas como sellos, impresión, troquelado, bordado o grabado, según las restricciones del proceso. |
| Una tinta blanca | `logo-1tinta-blanco.svg` | Fondos oscuros o fotografía con contraste suficiente. |
| Horizontal / vertical | `logo-horizontal.svg`, `logo-vertical.svg` | Según el espacio y el formato disponible. |
| Con y sin tagline | `logo-con-tagline.svg` y la versión base | Según el tamaño, el espacio y las variantes oficiales. |
| Icono / avatar | `icono.svg`, `icono-circulo.svg` | Redes sociales, favicon y aplicaciones que requieran el símbolo aislado. |
| Reducida | `logo-reducido.svg` | Solo cuando exista una variante simplificada aprobada para tamaños pequeños. |

Los nombres de archivo son los de la sección 4 de `construccion-logo.md` (fuente única); en el manual solo aparecen las variantes que existan y estén aprobadas.

- Incluye muestras visuales y etiquetas consistentes con los nombres reales de los archivos.
- Indica cuándo debe usarse cada versión y qué restricciones tiene.
- Documenta las versiones descartadas y el motivo, si esa información forma parte del proceso y es útil para prevenir usos futuros.
- No presentes una variante como oficial si no existe o no ha sido aprobada.

## 5. Área de respeto y tamaño mínimo

- Define el área de respeto con una unidad reproducible, como `u` o una dimensión del logo.
- Especifica el tamaño mínimo en milímetros para impresión y en píxeles para pantalla, por cada variante relevante.
- Basa los tamaños mínimos en pruebas visuales; no declares valores arbitrarios como si estuvieran validados.
- Muestra el área de respeto con un diagrama y explica cómo medirla.
- Indica cuándo debe utilizarse la versión reducida o el icono.
- Aclara si el margen está incluido en el archivo SVG o si se aplica como regla de composición externa.

## 6. Usos incorrectos

Incluye ejemplos visuales de los errores que deben evitarse, acompañados de una breve explicación. Como mínimo, considera:

- Deformar, estirar o alterar las proporciones.
- Cambiar los colores o introducir colores fuera de la paleta.
- Añadir sombras, efectos, contornos o adornos no aprobados.
- Girar o espejar el logo sin autorización.
- Sustituir la tipografía del nombre o alterar sus proporciones.
- Colocar el logo sobre fondos que comprometan la legibilidad.
- Recortar, separar o reorganizar sus partes fuera de las versiones oficiales.
- Aplicar el logo sobre imágenes sin suficiente contraste.

Utiliza ejemplos derivados del logo real. No crees versiones erróneas que puedan confundirse con variantes oficiales; identifícalas claramente como incorrectas.

## 7. Color

Documenta cada color oficial con una tabla completa y coherente:

| Campo | Valor |
|---|---|
| Nombre | *Pendiente de definir* si no está documentado. |
| Función | Principal, apoyo, neutro u otra función aprobada. |
| HEX | Valor verificado. |
| RGB | Valor verificado. |
| CMYK | Conversión de referencia; validar según el perfil y proceso de impresión. |
| Pantone aproximado | Solo si existe una equivalencia de referencia, siempre provisional; verificar con guía física y papel. Si no es fiable, *pendiente de definir*. |

Incluye también:

- **Justificación:** relación con el brief, la personalidad de marca o decisiones documentadas. Evita afirmaciones universales sobre psicología del color.
- **Proporciones de uso:** orientaciones para equilibrar los colores, si se han definido.
- **Combinaciones permitidas y no recomendadas:** especifica el contexto y los ratios de contraste cuando sean relevantes.
- **Degradados:** colores, posiciones, dirección y versión sólida alternativa, solo si forman parte del sistema aprobado.
- **Uso del logo:** combinaciones permitidas sobre fondos corporativos, neutros y fotografía.

No inventes equivalencias CMYK o Pantone ni presentes conversiones aproximadas como valores de impresión definitivos.

## 8. Tipografía

Documenta:

- Familias tipográficas oficiales, estilos y pesos autorizados.
- Licencia y fuente de procedencia, cuando se disponga de esa información.
- Muestras del alfabeto, números y signos necesarios para los idiomas de la marca; incluye tildes y ñ cuando corresponda.
- Jerarquía tipográfica: título, subtítulo, cuerpo de texto y etiqueta, con tamaños, pesos e interlineado.
- Justificación basada en coherencia con el símbolo, legibilidad y tono de marca.
- Alternativas web o de sistema para los contextos donde la fuente oficial no esté disponible.

No declares una licencia como verificada si no se ha comprobado. Distingue las fuentes usadas dentro del logo de las fuentes recomendadas para documentos y comunicaciones.

## 9. Aplicaciones

Incluye entre 6 y 10 aplicaciones pertinentes al sector y a los usos definidos en el brief. Selecciona solo las que ayuden a demostrar cómo funciona la identidad en contextos reales. Pueden incluir:

- Tarjeta y papelería.
- Firma de correo.
- Publicaciones y avatar para redes sociales.
- Presentación.
- Documento corporativo.
- Packaging.
- Uniforme.
- Señalética o rotulación.

Para cada aplicación:

- Explica brevemente por qué se resolvió de esa manera.
- Utiliza la paleta, tipografía y recursos oficiales.
- Mantén un estilo visual coherente entre las piezas.
- Incluye un detalle distintivo solo si pertenece al sistema de identidad y tiene una función clara.
- Comprueba que el logo conserva su legibilidad y no se deforma.

Si las aplicaciones son mockups conceptuales y no piezas finales de producción, identifícalos como tales.

## 10. Estructura gráfica y recursos

Documenta los recursos adicionales que formen parte del sistema aprobado:

- Patrones y formas de apoyo.
- Iconografía: estilo, cuadrícula, tamaños, color y set base, a partir de `iconografia/iconografia.md` (Fase 8b) con ejemplos reales de `iconografia/iconos/`.
- Estilo fotográfico.
- Tono de voz, si corresponde al alcance del manual.
- Colores y degradados permitidos para los recursos, siempre coherentes con la paleta.
- Plantillas para presentaciones y documentos, con rutas o enlaces funcionales.

No agregues recursos decorativos solo para completar esta sección. Si la marca no los necesita, indica que no se han definido recursos adicionales.

## 11. Entregables y contacto

Incluye:

- Lista de archivos entregados, formato, ubicación y uso recomendado.
- Fecha de emisión y versión del manual.
- Persona o canal de contacto, solo con información proporcionada o confirmada.
- Registro de cambios con versión, fecha y descripción de las modificaciones.

No inventes nombres, datos de contacto ni fechas de aprobación.

## Formato de salida

### Markdown — `manual-identidad.md`

- Mantén las secciones numeradas y el índice actualizado.
- Usa tablas para valores, versiones y entregables.
- Incluye imágenes con rutas relativas válidas, por ejemplo `![Logo](../logo/logo-color.svg)`.
- Verifica que los archivos referenciados existan desde la ubicación del Markdown.
- Si una imagen no está disponible, indícalo; no inventes rutas.

### HTML — `manual-identidad.html`

Cuando se solicite una versión HTML:

- Genera un archivo autocontenido en lo posible, con CSS en `<style>` y recursos SVG incrustados o referenciados mediante rutas relativas verificadas.
- Incluye navegación entre secciones, diseño responsive y modo claro, salvo que los requisitos del proyecto indiquen otra cosa.
- Utiliza la paleta y las tipografías reales de la marca.
- Presenta muestras de color con sus valores exactos.
- Muestra el logo a tamaño normal y reducido para ilustrar las pruebas de legibilidad.
- Usa fuentes desde Google Fonts solo cuando la licencia y la disponibilidad sean adecuadas; en otros casos, indica una alternativa autorizada.
- Incluye estilos de impresión con `@media print` y saltos de página razonables.
- Comprueba que las rutas, imágenes y estilos funcionen en el contexto de entrega. Si el HTML depende de recursos externos, decláralo.

No generes el HTML si solo se ha solicitado el Markdown.

## Lista de comprobación final

- [ ] El nombre, los acentos, el tagline y las mayúsculas son consistentes.
- [ ] Las decisiones descritas coinciden con el brief y los specs aprobados.
- [ ] Cada regla relevante incluye su justificación.
- [ ] Los valores de color coinciden en todas las secciones.
- [ ] Todas las variantes documentadas existen y corresponden a los archivos entregados.
- [ ] La versión a una tinta está incluida.
- [ ] El área de respeto y los tamaños mínimos están documentados y respaldados por pruebas.
- [ ] Los usos incorrectos están ilustrados y claramente identificados.
- [ ] Las licencias y alternativas tipográficas están documentadas sin afirmaciones no verificadas.
- [ ] Las aplicaciones utilizan los recursos oficiales y son pertinentes al sector.
- [ ] Las rutas de imágenes, enlaces y archivos se han comprobado.
- [ ] Los formatos entregados corresponden a lo solicitado.
- [ ] Las pruebas no realizadas están marcadas como pendientes o no verificadas.
- [ ] La fecha, la versión y el registro de cambios están completos cuando corresponde.

## Criterio de calidad

El manual debe permitir que otra persona aplique la identidad de forma consistente sin tener que adivinar medidas, colores, variantes ni restricciones. Debe explicar las decisiones documentadas con claridad, diferenciar los datos confirmados de los pendientes y representar fielmente la identidad aprobada.
