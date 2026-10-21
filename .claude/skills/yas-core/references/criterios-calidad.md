# Criterios de calidad compartidos

Umbrales y reglas de comprobación que usan las tres skills: `/yas-design` los cumple al diseñar, `/yas-figma` los respeta al construir y `/yas-audit` los verifica. Se definen una vez aquí. Las pruebas del logo no se repiten: están en `yas-design/references/construccion-logo.md`, sección 5.

## Accesibilidad

| Criterio | Umbral |
|---|---|
| Contraste de texto normal | ≥ 4,5:1 (WCAG AA); 7:1 para AAA |
| Contraste de texto grande (≥ 24 px, o ≥ 18,66 px en negrita) | ≥ 3:1 (AA); 4,5:1 para AAA |
| Contraste de componentes de interfaz y gráficos | ≥ 3:1 |
| Foco | Visible en todo elemento interactivo, con contraste suficiente |
| Área táctil | 44 × 44 px como criterio del ecosistema (web y Apple); 48 × 48 dp en Android con Material. Por encima del mínimo AA de WCAG 2.2 (24 × 24 px) |
| Movimiento | Respetar `prefers-reduced-motion` con una alternativa que conserve el cambio de estado; sin destellos por encima del umbral |
| Color como único canal | Nunca: acompañar con texto, icono o forma |

## Cálculo de contraste (reproducible)

1. Convertir cada canal sRGB a 0–1 y linealizar: `c ≤ 0,03928 ? c / 12,92 : ((c + 0,055) / 1,055)^2,4`.
2. Luminancia: `L = 0,2126 R + 0,7152 G + 0,0722 B`.
3. Ratio: `(L_claro + 0,05) / (L_oscuro + 0,05)`.
4. Si el color de primer plano tiene transparencia, componerlo antes sobre el fondo real.

Registra siempre la **combinación concreta** (primer plano, fondo, modo claro u oscuro) y el ratio. No se afirma accesibilidad por el aspecto ni por el nombre del color.

## Tokens y theming

- Ningún componente ni pantalla usa colores, tamaños o espaciados fijos: consumen tokens semánticos (`tokens-spec.md`).
- Todo token semántico de color tiene valor en modo claro y oscuro, o declara que no aplica.
- Los alias se resuelven; no hay referencias circulares ni variables huérfanas o duplicadas.
- Los valores de los tokens coinciden con los de la paleta y el sistema tipográfico aprobados.

## Componentes

- Todo componente define: anatomía, variantes, tamaños y estados.
- Estados mínimos cuando apliquen: reposo, hover, foco, activo, deshabilitado y error.
- Se construye sobre tokens semánticos y no duplica otro componente con variaciones accidentales.
- Cita la guía consultada (M3 o HIG, según `referencias-externas.md`).

## Nomenclatura y estructura

- Nombres consistentes en tokens, variables de Figma, capas, variantes y archivos (convenciones de `tokens-spec.md` y de `construccion-logo.md`).
- Sin páginas vacías ni separadores simulados en Figma.

## Verificación

- Valida con lo disponible en el entorno: renderizar, validar XML y JSON, abrir los archivos, calcular contrastes, ejecutar lint o pruebas si existen, leer de vuelta lo creado en Figma.
- Marca cada comprobación con el estado que corresponda (vocabulario en `reglas-comunes.md`) y nunca declares validado lo que no ejecutaste ni afirmes validación visual sin haber inspeccionado el resultado renderizado.
