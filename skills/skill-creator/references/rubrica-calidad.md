# Rúbrica de calidad de una skill

Puntuar cada dimensión de 1 a 10. 70 o más en total = utilizable; 80 o más = buena.

| # | Dimensión | Qué mirar |
|---|---|---|
| 1 | Activación | La descripción dice cuándo usarla, con situaciones y frases reales del usuario; no es un resumen del contenido |
| 2 | Cómo, no qué | Da pasos y comandos; lo normativo está enlazado a su regla, no copiado |
| 3 | Estructura de pasos | Pasos numerados, cada uno con salida o criterio de paso |
| 4 | Valores por defecto | Cada parámetro tiene un valor por defecto; no se detiene a esperar datos |
| 5 | Carga progresiva | Cuerpo corto (idealmente menos de 250 líneas); detalle en `references/`, código en `scripts/` |
| 6 | Salida | Formato de salida o ejemplo entrada/salida cuando importa |
| 7 | Errores y huecos | Qué hacer si falta una herramienta, un dato o un permiso; nada de "debería funcionar" |
| 8 | Código y comandos | Ejecutables tal cual, con sus importaciones; probados |
| 9 | Neutralidad | Sin nombres de proyecto, rutas de usuario, cuentas ni cifras de negocio |
| 10 | Exactitud | El contenido es correcto y está verificado; las afirmaciones no verificadas se rotulan |

## Interpretación
- Por debajo de 60: borrador, rehacer la estructura.
- 60-69: usable pero frustrante; arreglar primero activación y pasos.
- 70-79: bien, 2 o 3 mejoras puntuales.
- 80 o más: lista para el kit.

## Mejorar una skill existente
1. Leerla entera con sus `references/` y `scripts/`.
2. Puntuarla y mostrar la tabla con el problema de cada dimensión.
3. Proponer cambios ordenados por impacto (normalmente: descripción, defaults, salida).
4. Aplicarlos tras aprobación y volver a puntuar.
