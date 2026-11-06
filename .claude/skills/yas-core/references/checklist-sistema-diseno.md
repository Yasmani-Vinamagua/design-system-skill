# Checklist de sistema de diseño

Lista de verificación destilada de un checklist para planificar y construir sistemas de diseño (documento aportado por el usuario; sin fuente pública conocida). La usan `/yas-figma full` para saber qué debe cubrir cada pieza y `/yas-audit` (módulo Sistema de marca) para medir la cobertura de un sistema existente. Es una referencia de método: no se copia su texto, y las decisiones registradas del proyecto prevalecen (ver `referencias-externas.md`).

**Fuera de alcance de este archivo:** el lenguaje de diseño (visión, principios, tono de voz, terminología, pautas de redacción, microcopia) y el bloque de mantenimiento (decisiones, hoja de ruta, soporte, contribución). No se exigen en el sistema ni se puntúan en la auditoría; la gobernanza que sí se entrega está en `yas-figma/SKILL.md`.

**Cómo se usa**
- **Construir (`/yas-figma full`):** cada componente y cada fundamento cubre los puntos de su sección o declara `no aplica` con el motivo. Lo que no se define queda *pendiente de definir*, no se inventa.
- **Auditar (`/yas-audit`):** cada punto se marca *cubierto*, *parcial*, *no cubierto* o *no verificado*, con la evidencia (archivo, token, componente). La cobertura se informa como «n de N verificados»; no es una puntuación nueva ni sustituye a las cinco categorías.

## 1. Fundamentos

| Área | Puntos a cubrir | Dónde se define en Yas |
|---|---|---|
| Color | Pares de color con contraste AA calculado; colores semánticos (deshabilitado, fondo, acción, texto de alto contraste); modo oscuro; pauta de uso (cuándo, cuidados, cuándo no) | `tokens-spec.md`, `criterios-calidad.md`; la pauta va en el manual |
| Disposición | Unidades con incrementos constantes; cuadrícula por móvil, tableta y escritorio (columnas, márgenes, gutters); breakpoints; espaciado horizontal y vertical independiente de la cuadrícula | `tokens-spec.md` (reglas de escalas, `breakpoint.*`), páginas Layout and spacing y Grids |
| Tipografía | Escala adaptable al viewport; tamaño e interlineado alineados con la cuadrícula; legibilidad (interletraje, interlineado, longitud de línea); rendimiento de las fuentes (alternativas y carga rápida); pauta de uso | `tokens-spec.md` (reglas de escalas) |
| Elevación | 3 o 4 niveles de sombra; **un color de fondo asociado a cada nivel** (en claro, cerca del blanco junto a la sombra; en oscuro, el fondo sustituye a la sombra para indicar la distancia); sistema de `z-index` | `tokens-spec.md` (elevación), `shadow.*`, `z.*` |
| Movimiento | Funciones de suavizado estándar (estándar, aceleración, deceleración); varias duraciones; respeto de `prefers-reduced-motion` | `tokens-spec.md` (`motion.*`), `criterios-calidad.md` |
| Iconografía | Nombre accesible para los que tienen significado y ninguno para los decorativos; estilo único (contorno o relleno); **nombres por función, no por forma** («reproducir», no «triángulo»); recuadro alineado con la cuadrícula; palabras clave de búsqueda; **iconos reservados** para acciones comunes (navegación, añadir, eliminar); pauta de uso | Fase 8b de `/yas-design`, «Iconos derivados» de `/yas-figma` |

## 2. Componentes base

Requisitos por componente. Los estados mínimos (reposo, hover, foco, activo, deshabilitado, error) y los umbrales de contraste, teclado y lector de pantalla están en `criterios-calidad.md`; aquí solo lo específico de cada uno. Los nombres son los de las páginas de `/yas-figma full`.

| Componente (página) | Puntos específicos |
|---|---|
| **Buttons** | Función por color (principal, secundaria, destructiva) con contraste AA; variantes primaria y secundaria; tamaños; icono con etiqueta, y etiqueta accesible si va solo el icono; hover, activo y deshabilitado; **estado de carga que no cambia el ancho ni el alto**; rol anunciado correctamente (botón o enlace); indicador de foco visible |
| **Badge** | Color por función con contraste AA; variantes (por ejemplo, fondo suave); tamaños; icono legible en tamaño pequeño; acción para descartar si muestra valores seleccionados; versión sin texto; posicionamiento como indicador de estado sobre otro elemento |
| **Check** (Checkbox, Radio y sus grupos) | Etiqueta asociada (clicable, y anunciada aunque no se vea); marcado, indeterminado, deshabilitado y error (texto de error además del color); grupo; Radio siempre en grupo; operable con teclado |
| **Toggle** | Etiqueta asociada; estado activado; deshabilitado; teclado; etiqueta accesible si no hay texto visible |
| **Inputs** | Etiqueta asociada que mueve el foco; error (texto + color), deshabilitado; marcador de posición que **no sustituye** a la etiqueta; texto de ayuda; icono inicial; prefijo y sufijo; tamaños; etiqueta accesible si no hay etiqueta visible |
| **Text area** | Etiqueta, error, deshabilitado, marcador de posición (nunca en lugar de la etiqueta), texto de ayuda, tamaños, etiqueta accesible |
| **Progress bar** | Etiqueta visible opcional; tamaños; duración determinada o indeterminada; etiqueta accesible si no hay etiqueta visible |
| **Tooltip** | Reposicionamiento dinámico si no cabe; pequeño retardo antes de abrir; accesible también al enfocar con el teclado |
| **Accordion** | Dos estados con indicador distinto; contenido flexible (admite otros componentes); transición sutil; el contenido enfocado con tecnología de asistencia conserva el contexto de su activador |
| **Banner** (alerta) | Apariencia distinta por función con contraste AA; título opcional; icono (pista extra para daltonismo); acciones relacionadas con el mensaje; adaptable (ancho completo en móvil); rol de accesibilidad correcto |
| **Avatar** | Imagen enmascarada a su forma con cualquier tamaño de origen; respaldo (imagen, icono o iniciales) si falla; 2 o 3 tamaños, al menos uno pequeño; color de fondo con contraste AA cuando no hay imagen; formas (cuadrada o circular); grupos apilados; etiqueta accesible si no hay texto |
| **Card** | Contenido flexible; zona multimedia (ancho completo o lateral); acciones complementarias (o tarjeta interactiva entera); adaptable (ancho completo en móvil); grupos de tarjetas |

Las páginas `Help text` (su idea aparece como "texto de ayuda" dentro de Inputs), `Segmented controls`, `Search bar` y `Tag` no tienen sección equivalente en el checklist: cubren los estados mínimos de `criterios-calidad.md`.

## 3. Componentes opcionales (`Components - App`)

Si el proyecto los necesita, se añaden como secciones de `Components - App`, no como páginas nuevas. Con sus requisitos clave:

| Componente | Puntos clave |
|---|---|
| Modal | **Atrapa el foco** al abrir y lo devuelve al cerrar; se cierra con Esc; botón de cierre o acción de cierre; título y subtítulo etiquetados con el rol correcto; tamaños; posición central o lateral |
| Tabs | Siempre una pestaña seleccionada; flechas, Inicio y Fin para moverse; variantes; icono; ancho igual |
| Dropdown / Select | Posicionamiento dinámico; trampa de foco; teclado y cierre con Tab; marcador de posición; error con icono |
| Toast | Cierre por tiempo suficiente o con botón; apilado; acción contextual (por ejemplo, deshacer); el tiempo se detiene mientras el foco está dentro; movimiento reducido |
| Breadcrumb | Elementos desactivables; estado contraído; separador configurable |
| Pagination | Página seleccionada no interactiva; rango alrededor de la actual; número de elementos por página; total desconocido; etiquetas claras para tecnologías de asistencia |
| Calendar | Fecha única y rango; cambio de mes; nombres de días; formatos y primer día de la semana por región; teclado con flechas; anuncio de la fecha elegida |
| Carousel | Controles para ratón; parte del siguiente elemento visible; navegación táctil y por teclado sin clic |
| Skeleton | Mismo tamaño y forma que el componente real para evitar saltos; movimiento reducido |
| Loading indicator | Función de color; tamaños; indeterminado o con tiempo restante; movimiento reducido; etiqueta accesible |
| Link, List, Divider, Image, Icon | Enlace: heredar tipografía y color, multilínea, nunca solo icono. Lista: orden y rol. Divider: dirección y rol si no es decorativo. Imagen: relación de aspecto, respaldo, texto alternativo. Icono: tamaños y color por tokens, interactivo solo dentro de un botón o enlace |

## 4. Cobertura en la auditoría

Para `/yas-audit`: cuenta los puntos de las secciones 1 y 2 (y los de la 3 solo si el sistema tiene esos componentes) que el sistema auditado cubre, con evidencia. Un punto sin material que lo muestre es *no verificado*, no *no cubierto*. La cobertura orienta la recomendación (qué completar con `/yas-figma full`); no resta puntos por sí misma.
