# Referencias externas

Fuentes que consultan las tres skills, con una sola lista y unas reglas de uso. Consúltalas con WebFetch en lugar de apoyarte solo en memoria.

## Diseño, marca y sistemas

| Fuente | Úsala para | Skills y subcomandos |
|---|---|---|
| IBM Design Language — https://www.ibm.com/design/language/ | **Documentación visual**: cómo estructurar, ilustrar y explicar fundamentos de marca y de sistema. | Manual de identidad de `/yas-design`; HTML de `/yas-figma` |
| Wolff Olins — https://www.wolffolins.com/work | **Estrategia y procesos de rebranding**: cómo se plantea una idea de marca, el diagnóstico y la transición. | `/yas-design` `brief`, `brand`, `rebrand` |
| Google Brand Resource Center — https://partnermarketinghub.withgoogle.com/brands/google/overview/ | **Organización de activos oficiales**: versiones del logo, descargas por formato y restricciones de uso de marca. Sus reglas son un estándar de comparación **para Google**, no una lista universal para todos los logos. | `/yas-design` fase 8 y manual; `/yas-figma` Brand assets; `/yas-audit` módulo Sistema de marca |
| Caso del logo de LEGO en Logo Design Love — https://www.logodesignlove.com/lego-logo | **De la idea a una marca visual coherente**. | `/yas-design` `brand` |
| Adobe Illustrator, aprendizaje — https://www.adobe.com/es/learn/illustrator | **Parte técnica del logo**: dibujo vectorial, construcción de formas, curvas Bézier, geometría, trazados y archivos escalables. | `/yas-design` fase 5 |
| Material Design 3 — https://m3.material.io/ | **Componentes y sistemas** para web, Android o multiplataforma: anatomía, variantes, estados, tokens (roles de color, tipografía, forma, elevación, movimiento). | `/yas-design` fase 9 (aplicaciones en interfaz); `/yas-figma` `mini`, `full`, `colors` |
| Apple Human Interface Guidelines — https://developer.apple.com/design/human-interface-guidelines/ | **UX/UI de plataformas Apple** (iOS, iPadOS, macOS, watchOS, tvOS, visionOS): navegación, tamaños de toque, tipografía del sistema, materiales y convenciones. | Las mismas que M3 cuando el destino es Apple |

## Auditoría de marca (`/yas-audit`)

| Fuente | Úsala para | Origen del enlace |
|---|---|---|
| AAMA, plantilla de auditoría de marca (estrategia e identidad) — https://americanadvertisingandmarketingassociation.org/resources/creative-brand-resources/brand-audit-editable-brand-strategy-identity-audit-template-aama/ | Estructura integral: estrategia, público, posicionamiento, mensajes, identidad visual, experiencia del cliente y gobernanza. | Aportado por el usuario |
| Smartsheet, plantillas de auditoría de marca — https://www.smartsheet.com/content/brand-audit-templates | Estructura del informe y listas de verificación: identidad central, identidad verbal, identidad visual y evaluación; informes que enlazan cada recomendación con el problema detectado. | Aportado por el usuario; localizado también en una búsqueda |
| Beyond Basics, guía de auditoría de marca — https://beyondbasics.studio/resources/brand-audit-guide/ | Distinción entre identidad visual, identidad verbal y percepción real. | Aportado por el usuario |
| Brandfolder, plantillas de auditoría de marca — https://brandfolder.com/resources/brand-audit-templates/ | Identidad central, comunicación, consistencia y experiencia de usuario. | Aportado por el usuario |

Estos enlaces son los que dio el usuario; no se ha leído su contenido desde esta skill, así que al usarlos hay que consultar la página concreta (regla de abajo) antes de apoyarse en ella.

**Herramientas complementarias de presencia digital** (no auditan la identidad de marca ni determinan su posicionamiento):

| Herramienta | Para qué sirve | Enlace |
|---|---|---|
| WAVE | Problemas de accesibilidad web: contraste, etiquetas, estructura | https://wave.webaim.org/ |
| Lighthouse | Rendimiento, accesibilidad, buenas prácticas y SEO | https://developer.chrome.com/docs/lighthouse/overview?hl=es-419 |

## Reglas de uso

- **Son referencias de método y de organización, no modelos a imitar.** Aprende cómo documentan, razonan o estructuran; no copies identidades, logos, textos, recursos ni composiciones, ni presentes el resultado como afín a esas marcas o como un sistema oficial de Google o Apple.
- **Consulta la página concreta** relevante (por ejemplo, la de botones o la de campos de texto) antes de decidir. Si no carga, dilo y marca el dato como *no verificado*, sin completarlo de memoria.
- **Elige M3 o HIG según la plataforma del proyecto:** HIG si el destino es Apple; M3 si es web o Android; en multiplataforma, M3 como base señalando dónde la HIG exige otra cosa (navegación o tamaños de toque en iOS). Si no está claro, pregunta.
- **Las guías oficiales de una marca** (por ejemplo, las de Google) sirven de estándar de comparación para esa marca, no como reglas para otras.
- **Las herramientas** solo cuentan como evidencia si se ejecutaron; sus resultados no se afirman si no pudieron ejecutarse.
- **Cita la fuente consultada** (enlace a la página) en el documento que la use: manual, `componentes.md`, HTML, notas de Figma o informe de auditoría.
- Las decisiones propias ya registradas en el proyecto prevalecen sobre cualquier referencia (precedencia en `yas-design/SKILL.md`, "Vocabulario y criterios de marca").
