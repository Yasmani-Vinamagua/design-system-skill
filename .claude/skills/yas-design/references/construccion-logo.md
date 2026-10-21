# Construcción del logo en SVG y exportación de versiones

## Propósito

Establecer los criterios técnicos para construir, validar y exportar la marca gráfica en formato vectorial. Esta especificación se aplica durante la fase de construcción y debe respetar el brief, las decisiones aprobadas y los specs del proyecto.

No redefine el proceso general de diseño ni sustituye las decisiones conceptuales ya aprobadas. Si una instrucción de este documento entra en conflicto con el brief o con un spec de mayor prioridad, registra el conflicto y aplica la precedencia definida en "Vocabulario y criterios de marca" de `SKILL.md`.

## 1. Principios de construcción

- **Construir primero a una tinta.** Desarrolla y revisa el logo en negro sobre blanco antes de aplicar color, degradados o efectos. La forma debe funcionar por sí sola.
- **Usar espacio negativo real.** Los huecos deben ser transparentes, no formas blancas superpuestas. En SVG, utiliza subtrazados con `fill-rule="evenodd"` o una máscara cuando sea necesario.
- **Priorizar geometría limpia.** Evita nodos innecesarios, curvas irregulares y detalles que no contribuyan a la identidad o legibilidad.
- **Definir una retícula.** Establece una unidad base `u` para organizar proporciones, espacios, radios y grosores. Documenta las medidas relevantes. Permite ajustes ópticos cuando mejoren el resultado visual.
- **Mantener coherencia formal.** Unifica el criterio de terminales, esquinas, radios, curvas y grosores. Las excepciones deben ser intencionales.
- **Preparar trazados de producción.** Cuando el diseño esté aprobado, convierte los trazos a formas rellenas si el flujo de trabajo y las herramientas disponibles lo permiten. Si el archivo conserva `stroke`, documenta su grosor, terminales y uniones; no lo presentes como contorno expandido.
- **Resolver la tipografía.** Para el arte final, convierte el nombre y el tagline a trazados cuando sea posible. Si no puedes hacerlo, conserva una versión con `<text>` e indica la familia tipográfica necesaria. No afirmes que el texto está convertido si aún depende de una fuente.
- **Mantener una fuente maestra.** Todas las variantes deben derivarse de un mismo diseño de referencia para evitar diferencias accidentales de proporción, geometría o espaciado.
- **Respetar las decisiones aprobadas.** No cambies el concepto, la tipografía, la paleta ni los elementos establecidos en el brief sin documentar la necesidad y el impacto.

## 2. Estructura y requisitos del SVG

Usa SVG válido, escalable y organizado con grupos identificables. La siguiente estructura es una referencia; adapta los grupos a los elementos reales del logo:

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 W H"
     role="img"
     aria-labelledby="logo-title">
  <title id="logo-title">Nombre de marca</title>

  <g id="simbolo" fill="#000">
    <path d="..." fill-rule="evenodd"/>
  </g>

  <g id="nombre" fill="#000">
    <path d="..."/>
  </g>
</svg>
```

Criterios técnicos:

- Sustituye `W`, `H` y los trazados de ejemplo por valores y geometría reales.
- Usa un `viewBox` que abarque correctamente el arte. Evita dimensiones fijas en el maestro salvo que el destino de exportación las requiera.
- Organiza los elementos con identificadores descriptivos, por ejemplo `simbolo`, `nombre` y `tagline`.
- Mantén los huecos como transparencias reales; no los simules con formas blancas.
- Evita filtros, metadatos, grupos o definiciones que no se utilicen.
- No uses imágenes rasterizadas incrustadas como sustituto de los trazados vectoriales.
- Comprueba la validez del XML y que no existan referencias rotas.
- Si se necesitan dimensiones explícitas para una plataforma o aplicación, defínelas en el archivo exportado correspondiente sin alterar innecesariamente el maestro.
- Mantén el código razonablemente legible para facilitar revisiones y futuras modificaciones.

## 3. Retícula, proporciones y espacio de protección

- Define una unidad base `u` y úsala para documentar las proporciones, separaciones, radios y grosores relevantes.
- Registra los ajustes ópticos que se aparten de la retícula geométrica.
- Define el área de respeto con una medida reproducible, por ejemplo `u`, la altura de una letra o una dimensión del símbolo.
- Decide si el margen de protección forma parte del lienzo SVG o si se documenta por separado. Aplica el mismo criterio a las variantes equivalentes.
- No agregues contornos, círculos, anillos ni fondos decorativos para compensar problemas de equilibrio.
- No impongas simetría matemática si el concepto requiere una composición asimétrica.

## 4. Versiones y exportaciones

Esta tabla es la **fuente única de nombres de archivo** de las variantes; el resto de documentos la referencian. Parte del maestro aprobado. Cada variante debe conservar la identidad, las proporciones y la geometría base, salvo los ajustes específicos necesarios para su uso.

| Variante | Criterio |
|---|---|
| `logo-master.svg` | Fuente maestra de referencia, organizada y editable. |
| `logo-1tinta-negro.svg` | Logo negro sobre fondo transparente. |
| `logo-1tinta-blanco.svg` | Logo blanco para fondos oscuros; verificar contraste sobre los fondos previstos. |
| `logo-color.svg` | Versión con la paleta de marca aprobada. |
| `logo-negativo.svg` | Versión invertida para un fondo corporativo o de color especificado. Si hay varios fondos, `logo-negativo-<nombre-color>.svg`. |
| `logo-horizontal.svg` | Símbolo y nombre en disposición horizontal, con separación consistente. |
| `logo-vertical.svg` | Símbolo y nombre en disposición vertical, con jerarquía consistente. |
| `icono.svg` | Solo el símbolo, encuadrado para el uso previsto. Base del favicon, que se exporta solo si se solicita. |
| `icono-circulo.svg` | Avatar. Crear únicamente si el sistema de identidad lo contempla o el usuario lo solicita. |
| `logo-con-tagline.svg` | Solo si existe tagline y es legible; sin tagline se usa la versión base. |
| `logo-reducido.svg` | Variante simplificada si las pruebas demuestran que el logo principal pierde legibilidad a tamaño pequeño. |

No generes automáticamente todas las variantes si el encargo no las necesita. Prioriza los entregables solicitados y añade solo los que sean útiles para los usos definidos.

### Color y degradados

- Construye y valida primero la versión a una tinta.
- Utiliza los colores aprobados en el brief o en el spec de identidad.
- Documenta los valores exactos de la paleta, preferentemente HEX/RGB para medios digitales.
- Si se utiliza un degradado, especifica los colores, las posiciones, la dirección y los contextos de uso.
- Entrega también una versión de color sólido cuando el logo use degradados.
- No inventes equivalencias CMYK o Pantone. Si no pueden determinarse con fiabilidad, indica que requieren validación con el flujo de impresión.
- Comprueba el contraste sobre los fondos relevantes. No asumas que una versión funciona sobre cualquier fondo.

### Tamaños reducidos

- Comprueba el logo en los tamaños reales o previstos para su uso.
- Como referencia, revisa 16 px para iconografía digital y 2 cm para impresión cuando esas dimensiones sean pertinentes para el encargo.
- Observa si los huecos se cierran, los elementos se fusionan o desaparecen detalles esenciales.
- Si el diseño pierde legibilidad, crea una variante simplificada con detalles reducidos o grosores ajustados y documenta el umbral de uso basado en las pruebas.
- No declares un tamaño mínimo sin haberlo evaluado.

## 5. Pruebas y validación

Utiliza las herramientas disponibles en el entorno para renderizar y revisar el resultado. No presupongas que un renderizador específico está instalado.

Cuando sea posible:

1. Renderiza el SVG a una imagen para inspeccionar su apariencia.
2. Inspecciona visualmente el resultado renderizado; no te bases únicamente en el código.
3. Comprueba la validez del XML y las referencias internas.
4. Revisa las variantes exportadas, no solo el maestro.
5. Corrige los problemas detectados y vuelve a renderizar antes de entregar.

Registra los resultados en el spec o informe de la fase:

| Prueba | Qué comprobar |
|---|---|
| Negro al 100 % | Formas limpias y legibles sobre blanco, sin depender del color. |
| Versión negativa | Legibilidad del logo blanco sobre negro y sobre los fondos corporativos previstos. |
| Tamaño reducido | Persistencia de los huecos, separación de formas y reconocimiento de los detalles esenciales. |
| Silueta | Reconocimiento del símbolo sin depender del color ni del nombre. |
| Equilibrio visual | Balance de masas, centrado óptico y proporciones. El giro o espejo puede usarse como diagnóstico, no como requisito de uso. |
| Espacio negativo | Los huecos son transparentes reales y se conservan en el renderizado. |
| Tipografía | Espaciado y kerning consistentes; confirmar si el texto está convertido a trazados. |
| Contraste | Legibilidad sobre los fondos definidos para la marca. |
| Producción física | Viabilidad para bordado, grabado, corte o troquelado cuando esos procesos formen parte del encargo. |
| Integridad del archivo | SVG válido, sin referencias rotas ni recursos externos inesperados. |
| Consistencia | Las variantes mantienen la geometría, proporciones y espaciados aprobados. |
| Diferenciación | La marca no se confunde con las referencias competitivas estudiadas en la investigación. Una evaluación visual no sustituye una búsqueda legal de marcas registradas. |

Marca cada prueba como **verificada**, **fallida**, **no aplicable** o **no verificada**. Si no puedes renderizar el archivo o comprobar un criterio, indica la limitación; nunca presentes una prueba no ejecutada como superada.

La viabilidad para bordado, grabado, corte o troquelado depende del proceso y de sus tolerancias. Si no se dispone de esos parámetros, registra la revisión como preliminar y no como certificación de producción.

## 6. Organización de archivos

- Respeta las convenciones del proyecto si ya existen.
- No sobrescribas ni elimines archivos existentes sin autorización.
- Usa nombres descriptivos y consistentes.
- Mantén separados el maestro, las exportaciones y las vistas previas.
- Exporta PNG con transparencia cuando sea necesario o solicitado.
- Exporta PDF vectorial si el entorno lo permite y el entregable lo requiere.
- No entregues únicamente PNG cuando se solicita un logo vectorial.
- No afirmes que un archivo se exportó correctamente sin comprobar que existe y puede abrirse.

## 7. Errores que deben evitarse

- Simular espacios negativos con formas blancas superpuestas.
- Cambiar geometría, tipografía o espaciados de manera inconsistente entre versiones.
- Introducir colores que no pertenezcan a la paleta aprobada.
- Añadir aros, contornos, círculos o fondos que no estén justificados por el sistema de identidad.
- Dejar texto como `<text>` y describirlo como texto convertido a trazados.
- Usar degradados o efectos para disimular una silueta débil.
- Mantener detalles que desaparecen en tamaños pequeños sin evaluar una variante reducida.
- Entregar solo un archivo rasterizado cuando se requiere un vector.
- Afirmar que el logo es apto para producción física sin evaluar los requisitos del proceso.
- Declarar verificaciones que no se han ejecutado.
- Modificar decisiones aprobadas del brief sin registrar el conflicto.

## 8. Registro de entrega

Al terminar la construcción, registra en el spec o informe de la fase:

- Archivos generados y sus ubicaciones.
- Variantes incluidas y variantes omitidas, con su motivo cuando sea relevante.
- Unidad base y criterios de retícula utilizados.
- Área de respeto definida y dónde se aplica.
- Paleta y tipografía utilizadas, incluyendo si el texto está convertido a trazados.
- Pruebas realizadas y su estado.
- Limitaciones, conflictos con el brief o specs y pruebas pendientes.
- Formatos que no pudieron generarse y la razón.

No repitas en este documento decisiones de estrategia, investigación o concepto que ya estén registradas en el proceso principal; referencia el spec correspondiente cuando sea necesario.

## Criterio de aceptación técnica

La construcción puede considerarse técnicamente comprobada cuando:

1. El SVG maestro es válido y se renderiza correctamente en las herramientas disponibles.
2. La versión a una tinta conserva la legibilidad y la intención del diseño aprobado.
3. Los huecos y las formas vectoriales se comportan correctamente.
4. Las variantes solicitadas mantienen la consistencia del sistema.
5. Los archivos de entrega existen y se han revisado.
6. Los resultados de las pruebas y las limitaciones están documentados con precisión.

Este criterio valida la construcción técnica; no sustituye la aprobación conceptual o de marca definida por el proceso principal.
