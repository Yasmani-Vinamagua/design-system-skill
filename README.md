<div align="center">

# 🎨 Yas Design System

**Branding y sistema de diseño con Claude Code:**
de la idea a una marca documentada, auditada y lista para Figma.

![Claude Code](https://img.shields.io/badge/Claude_Code-Skills-D97757?style=for-the-badge)
![Idioma](https://img.shields.io/badge/idioma-espa%C3%B1ol-2563EB?style=for-the-badge)
![Estado](https://img.shields.io/badge/estado-beta-F59E0B?style=for-the-badge)
![Figma MCP](https://img.shields.io/badge/Figma_MCP-opcional-7C3AED?style=for-the-badge)

[Instalación](#-instalación) · [Inicio rápido](#-inicio-rápido) · [Las skills](#-las-skills) · [Qué genera](#-qué-archivos-genera) · [Estado](#-estado-y-hoja-de-ruta)

</div>

---

## ✨ ¿Qué es?

Yas Design **no es una colección de prompts**: es una **metodología de diseño** empaquetada como skills de [Claude Code](https://claude.com/claude-code). Cada skill analiza, decide, ejecuta, documenta y valida, y deja **archivos reales** en tu proyecto.

- 🧭 **Proceso con puertas de aprobación.** Cada fase tiene objetivo, qué hacer, qué preguntar, entregable y criterio de aprobación. Al terminar, resume y espera tu visto bueno antes de avanzar.
- 🔗 **Tres especialistas que comparten resultados.** Lo que crea una skill lo leen las otras; nada se rehace ni se copia.
- 🧪 **Honestidad verificable.** Distingue lo comprobado de las hipótesis y de lo que no pudo verificar, y nunca declara validado lo que no ejecutó.
- 🛟 **Funciona aunque Figma falle.** Sin el MCP de Figma, o sin cuota, genera el sistema en local con un HTML navegable listo para entregar.

```mermaid
flowchart LR
    A["🎨 /yas-design<br/>crea la identidad"] --> M[("📘 Manual de identidad<br/>.yas/brand/")]
    M --> B["🔗 /yas-figma<br/>tokens y Figma"]
    M --> C["🔍 /yas-audit<br/>diagnóstico sobre 20"]
    B --> T[("🧩 Tokens<br/>.yas/tokens/")]
    C -. recomienda acciones .-> A
    K["⚙️ yas-core<br/>reglas y criterios compartidos"] -.-> A
    K -.-> B
    K -.-> C
```

---

## 🧰 Las skills

| Skill | Responsabilidad | Comandos |
|---|---|---|
| 🎨 **`/yas-design`** | **Crear** la identidad: marca nueva o rebranding, hasta el manual de identidad | `init` · `brief` · `brand` · `rebrand` |
| 🔍 **`/yas-audit`** | **Auditar** la marca y puntuar sobre 20. Solo diagnostica, nunca corrige | `estrategia` · `identidad-verbal` · `competencia` · `identidad-visual` · `consistencia` · `digital` · `sistema` |
| 🔗 **`/yas-figma`** | **Llevar** el sistema a Figma, o documentarlo | `push` · `colors` · `library` · `document` |
| ⚙️ **`yas-core`** | Núcleo compartido (no se invoca): reglas, artefactos, tokens, calidad y referencias | — |

> **Regla de alcance:** cada skill hace el tipo de trabajo que pediste y no pasa al siguiente sin que forme parte de lo solicitado. Una auditoría no rediseña; una propuesta conceptual no se convierte en código; el siguiente paso útil se **ofrece**, no se ejecuta por su cuenta.

### 🎨 `/yas-design` — de la idea a la marca

Empieza preguntando el punto de partida:

| Punto de partida | Qué ocurre |
|---|---|
| **Marca nueva** | Eliges el tipo de marca gráfica (logotipo, isotipo, imagotipo o isologo) o dejas que Yas Design lo proponga según el brief, con justificación y tu aprobación |
| **Rebranding** | Evaluación inicial de la marca existente y alcance del cambio: **ajuste**, **evolución** o **rebranding integral**. No se asume que todo deba cambiar |

El proceso completo son **fases con puerta de aprobación**:

| Fase | Contenido |
|---|---|
| 0 · 0b | Preparación y alcance · *(rebranding)* evaluación inicial de la marca existente |
| 1 | Brief y estrategia |
| 2 | Investigación y documentación de la competencia |
| 3 | Exploración conceptual (diagramas radiales, tres conceptos) |
| 4 | Bocetos y selección |
| 5 | Construcción de la marca gráfica en SVG, primero a una tinta |
| 6 · 7 | Color · Tipografía |
| 8 | Versiones y activos de marca |
| 9 | Aplicaciones de marca |
| 10 · 10b | Manual de identidad (Markdown y HTML) · *(rebranding)* plan de transición |
| 11 | Control final y entrega |

### 🔍 `/yas-audit` — diagnóstico con puntuación sobre 20

No se limita a decir si un logo «se ve bien»: **detecta problemas, justifica cada hallazgo y propone mejoras priorizadas.** Siete módulos independientes alimentan cinco categorías, cada una de 0 a 4:

| Categoría puntuada | Módulos |
|---|---|
| 1 · Estrategia y posicionamiento | Estrategia · Identidad verbal · Competencia |
| 2 · Identidad visual | Identidad visual |
| 3 · Consistencia de marca | Consistencia |
| 4 · Experiencia digital | Presencia digital |
| 5 · Evaluación técnica de los activos | Sistema de marca |

**Bandas:** 18–20 Excelente · 14–17 Bueno · 10–13 Aceptable · 6–9 Pobre · 0–5 Crítico.

Cada hallazgo incluye **problema, evidencia, impacto, prioridad** (crítica, alta, media o baja, con criterios explícitos), **recomendación y validación**. Además, la skill separa lo **comprobado**, las **hipótesis** y lo **no verificado**: si no puede renderizar o abrir algo, no afirma haberlo validado visualmente. Las hipótesis no restan puntos.

### 🔗 `/yas-figma` — del manual a Figma

| Comando | Qué hace |
|---|---|
| `push [mini\|full]` | Crea o completa el design system en Figma (variables, estilos, componentes). Es **idempotente y reanudable**: si se corta por límite de uso, el siguiente `push` continúa donde se quedó |
| `colors` | Convierte la paleta de la marca en tokens de color y **variables semánticas** (claro y oscuro) |
| `document figma <URL>` | Lee un archivo de Figma (solo lectura) y genera un **entregable HTML** con sus datos reales |
| `document manual` | Genera el design system **en local** solo con el manual de identidad, sin tocar Figma |

**Dos alcances:**

| | **Mini** (9 páginas) | **Full** (28 páginas) |
|---|---|---|
| Contenido | Solo fundamentos: Cover, Icons, Brand assets, Colors, Type scale, Spacing and layout, Radios, Shadows, Grids | Fundamentos + 16 componentes base + componentes de la app, patrones y plantillas |
| Pensado para | MVP, prototipo o marca nueva | Producto existente o varios equipos |

> 💡 **Plan gratuito de Figma (3 páginas por archivo):** la skill lo detecta y te ofrece tres opciones: ampliar el plan, crear la estructura de páginas manualmente, o generar solo iconos, color y tipografía.

> 🛟 **Sin MCP, sin cuota o con errores persistentes:** `/yas-figma` avisa con el motivo concreto y genera el paquete local (`.yas/figma-local/`) con `design-system.html`, variables, estilos y una guía para implementarlo a mano. `document figma` es la excepción: si no puede leer Figma, anuncia el problema y termina.

---

## 📦 Instalación

Las skills son carpetas. Copia **las cuatro** (`yas-core`, `yas-design`, `yas-audit` y `yas-figma`) **juntas** en la misma carpeta de skills, porque se referencian entre sí con rutas relativas.

**Opción A · Para todos tus proyectos (global)**

```bash
git clone https://github.com/Yasmani-Vinamagua/yas-design-system.git
```

```bash
# macOS / Linux
mkdir -p ~/.claude/skills
cp -r yas-design-system/.claude/skills/yas-* ~/.claude/skills/
```

```powershell
# Windows (PowerShell)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse yas-design-system\.claude\skills\yas-* "$env:USERPROFILE\.claude\skills\"
```

**Opción B · Solo en un proyecto**

Copia las cuatro carpetas `yas-*` dentro de `<tu-proyecto>/.claude/skills/`.

**Verifica:** abre una sesión nueva de Claude Code y escribe `/yas-` . Deberían aparecer `/yas-design`, `/yas-audit` y `/yas-figma` (`yas-core` no aparece porque no se invoca directamente).

### Requisitos

| Requisito | ¿Obligatorio? |
|---|---|
| [Claude Code](https://claude.com/claude-code) | Sí |
| MCP de Figma | **Opcional.** Solo para crear o leer archivos de Figma. Sin él, `/yas-figma` trabaja en modo local |
| Navegador o herramientas de renderizado | Opcional. Mejoran la validación visual de `/yas-audit`; sin ellas, la skill lo declara como *no verificado* |

**Instalar el MCP de Figma** (según la [documentación oficial de Figma](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation)):

```bash
# Recomendado por Figma: el plugin oficial
claude plugin install figma@claude-plugins-official

# O el servidor MCP remoto (añade --scope user para usarlo en todos los proyectos)
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

Después, escribe `/mcp` en Claude Code para autenticarte.

---

## 🚀 Inicio rápido

**Crear una marca nueva**

```text
/yas-design brand
```
Responde a las preguntas de cada fase y aprueba el entregable de cada una. Al final tendrás el manual de identidad en `.yas/brand/manual/`.

**Rehacer una marca existente**

```text
/yas-design rebrand
```
Adjunta el logo, el manual o la URL. Primero se evalúa lo que hay y se acuerda el alcance del cambio.

**Auditar una marca**

```text
/yas-audit
```
Adjunta el material (logo, manual, URL, ruta del proyecto). Audita todos los módulos, o uno concreto: `/yas-audit digital`.

**Llevar el sistema a Figma**

```text
/yas-figma colors          # solo la paleta, como variables semánticas
/yas-figma push mini       # fundamentos completos
/yas-figma document manual # design system local en HTML, sin Figma
```

---

## 🧾 Qué archivos genera

Todo vive en `.yas/` dentro de tu proyecto, y las skills comparten estos archivos en lugar de copiarlos.

```text
.yas/
├── brand/                        ← /yas-design
│   ├── marca-spec.md             especificación y registro de decisiones
│   ├── investigacion/  concepto/
│   ├── logo/                     SVG: maestro y variantes
│   ├── paleta/paleta.md          tabla de colores (HEX, RGB, CMYK, Pantone de referencia)
│   ├── tipografia/  aplicaciones/
│   └── manual/manual-identidad.{md,html}
├── tokens/                       ← /yas-figma
│   ├── tokens.json               formato DTCG, primitivas y semánticas, claro y oscuro
│   ├── contraste.md              pares de color con su ratio WCAG calculado
│   └── CHANGELOG.md
├── figma-local/                  ← /yas-figma (modo local)
│   └── design-system.html        entregable navegable
├── deliverables/                 ← /yas-figma document
├── audits/AAAA-MM-DD-marca.md    ← /yas-audit
└── figma-state.json              progreso de Figma, para reanudar
```

---

## 🛡️ Reglas de calidad compartidas

Las tres skills cumplen las mismas ocho reglas (`yas-core`):

| Regla | Comportamiento |
|---|---|
| **Inspección inicial** | Revisa archivos, estructura y tecnologías existentes antes de actuar |
| **Contexto** | Identifica el proyecto y sus restricciones antes de intervenir |
| **Ejecución** | Resuelve lo pedido sin activar procesos innecesarios |
| **Archivos** | Crea o modifica archivos reales cuando la tarea lo requiere |
| **Protección** | No sobrescribe archivos existentes sin comprobar su función |
| **Calidad** | Valida los resultados con las herramientas disponibles |
| **Documentación** | Registra decisiones, instrucciones de uso y cambios relevantes |
| **Transparencia** | Informa qué generó, qué verificó y qué quedó pendiente |

---

## 🧭 Estado y hoja de ruta

El proyecto está en **beta**. Las skills están diseñadas y revisadas, pero todavía no tienen una batería de pruebas automatizadas, y la integración con Figma depende del comportamiento real del MCP. Si encuentras algo roto, abre un issue.

| Estado | Funcionalidad |
|---|---|
| ✅ Disponible | `/yas-design` (`init`, `brief`, `brand`, `rebrand`) · `/yas-audit` (siete módulos) · `/yas-figma` (`push`, `colors`, `library`, `document`) |
| 🚧 Sin implementar | `/yas-figma pull`, `sync`, `connect` (Code Connect) y `push screens`. La skill lo indica con claridad si se invocan |
| ⚠️ Limitaciones conocidas | Solo en español · la creación de variables, estilos y páginas en Figma depende de las herramientas del MCP y de tu plan · las auditorías de percepción real necesitan datos que tú aportes |

---

## 📁 Estructura del repositorio

```text
.claude/skills/
├── yas-core/        reglas comunes, artefactos, especificación de tokens, criterios de calidad, referencias
├── yas-design/      SKILL.md + proceso por fases, construcción del logo, plantilla del manual
├── yas-audit/       SKILL.md + módulos de auditoría
└── yas-figma/       SKILL.md
```

---

## 📚 Referencias e inspiración

Las skills consultan estas fuentes como **referencias de método y de organización, no como modelos a imitar**:

- **Documentación y marca:** [IBM Design Language](https://www.ibm.com/design/language/) · [Wolff Olins](https://www.wolffolins.com/work) · [Google Brand Resource Center](https://partnermarketinghub.withgoogle.com/brands/google/overview/) · [Logo Design Love](https://www.logodesignlove.com/lego-logo) · [Adobe Illustrator](https://www.adobe.com/es/learn/illustrator)
- **Componentes y plataformas:** [Material Design 3](https://m3.material.io/) · [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- **Auditoría de marca:** [AAMA](https://americanadvertisingandmarketingassociation.org/resources/creative-brand-resources/brand-audit-editable-brand-strategy-identity-audit-template-aama/) · [Smartsheet](https://www.smartsheet.com/content/brand-audit-templates) · [Beyond Basics](https://beyondbasics.studio/resources/brand-audit-guide/) · [Brandfolder](https://brandfolder.com/resources/brand-audit-templates/)
- **Herramientas complementarias:** [WAVE](https://wave.webaim.org/) · [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview?hl=es-419)

> Este proyecto es independiente y **no está afiliado** a Figma, Google, Apple, IBM, Adobe ni a ninguna de las organizaciones citadas. Los nombres pertenecen a sus propietarios.

---

## 🤝 Contribuir

Las contribuciones son bienvenidas: abre un *issue* con el problema o la propuesta, o un *pull request* pequeño y enfocado. Para mantener la coherencia del ecosistema:

- Cada tema se define **una sola vez** en `yas-core` y las skills lo referencian; no dupliques documentación.
- Respeta la **regla de alcance**: una skill no debe hacer más de lo que anuncia.
- Si añades una función, indica en qué estado está (disponible, parcial o sin implementar) y no declares como verificado lo que no has probado.

---

<div align="center">

Hecho para diseñar marcas con criterio, método y trazabilidad. 🎨

</div>
