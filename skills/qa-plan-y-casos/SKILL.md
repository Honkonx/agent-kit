---
name: qa-plan-y-casos
description: Usar cuando se agrega una función o requisito, al decidir qué probar o al armar el informe de una fase. Plan de pruebas, diseño de casos (equivalencia, límites, tablas de decisión, transiciones, negativos) y matriz requisito-caso-resultado.
---

# Plan de pruebas y diseño de casos

El QUÉ (casos con ID y trazabilidad, oráculo independiente, criterios por fase, cobertura honesta) está en [[qa-independiente-y-oraculos]]. Esta skill cubre el CÓMO. La usan los agentes `qa` y `qa-adversarial`. Los fallos se reportan con `qa-bugs-y-triage`.

## 1. Plan (una página por fase)
Alcance (qué sí y qué no), riesgos ordenados (dinero > seguridad > datos > usabilidad), tipos de prueba (smoke, regresión, exploratoria, adversarial, oráculos), entorno (datos ficticios, base temporal, anchos de pantalla o TTY), criterios de entrada y de salida, y qué queda fuera y por qué. Un plan que no dice lo que NO cubre miente por omisión.

## 2. Caso: campos obligatorios
`ID` (TC-nnn), `requisito` (R-xxx), `título` (verbo + condición), `precondición`, `pasos`, `esperado` (observable y medible), `severidad` S1 a S4, `prioridad` P1-P3, `tipo` (smoke | regresión | negativo). Al menos un chequeo que pueda fallar.

## 3. Diseñar casos (no solo el camino feliz)
- **Clases de equivalencia:** un representante por clase. Ej.: en un descuento, válido, 0, negativo, mayor que el total, no numérico.
- **Valores límite:** justo antes, en y justo después (stock 0/1, longitud 0/1/5000, vuelto exacto, cambio de día).
- **Tabla de decisión:** combinaciones de condiciones, con el resultado explícito en cada fila.
- **Transiciones de estado:** abierto → cerrado → inmutable; libre → ocupado → cobrado. Prueba también las transiciones ilegales.
- **Negativos:** entradas hostiles (unicode, comillas, fórmulas `=` en CSV/XLSX, escapes ANSI). Esperan un rechazo claro, no un fallo ni un silencio.
- **Oráculo independiente:** el esperado sale de otra vía (aritmética exacta aparte, referencia lenta y obvia, lectura directa de la fuente), nunca de la función probada.

## 4. Trazabilidad
Tabla requisito → casos → resultado, generada por script o a partir de los casos, no editada a mano. Requisito sin caso = hueco; caso sin requisito = ruido; requisito con casos fallando = riesgo abierto.

## 5. Cobertura honesta
Reporta "N casos, M requisitos cubiertos, K sin cubrir, y no verificable: X". Nunca "cobertura completa".

## Cuándo NO usar
- Una exploración libre con charter y notas: eso es `qa-exploratorio-y-simulador`; aquí se diseñan casos con ID, no se explora.
- Reportar un fallo ya reproducido: va a `qa-bugs-y-triage`; esta skill decide qué probar y registra el resultado en la matriz.
- Un cambio sin requisito asociado: no hay caso que trazar; se comprueba directamente y se dice que no tiene trazabilidad.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El camino feliz ya lo cubre" | El paso 3 pide clases de equivalencia, límites, tablas de decisión, transiciones y negativos; el camino feliz es una sola clase. |
| "Saco el esperado de la misma función, es más rápido" | El oráculo sale de otra vía (aritmética exacta, referencia lenta, lectura de la fuente); `f(x) == f(x)` no prueba nada ([[qa-independiente-y-oraculos]]). |
| "Con todos los casos en verde ya hay cobertura completa" | La sección 5 pide "N casos, M requisitos cubiertos, K sin cubrir, y no verificable: X"; nunca se escribe "cobertura completa". |

## Errores comunes
- Casos sin los campos obligatorios: ID TC-nnn, requisito R-xxx, severidad S1 a S4, prioridad P1 a P3 y tipo.
- Un plan que no dice lo que no cubre: miente por omisión.
- Matriz de trazabilidad editada a mano en lugar de generada desde los casos; se desfasa.
- Esperados como "funciona bien" en vez de un valor observable y medible.

## Verificación
- Cada requisito de la matriz tiene al menos un caso; los huecos (requisito sin caso) salen listados en el informe, según la sección 4.
- Cada caso trae todos sus campos obligatorios: se comprueba con una búsqueda de texto sobre la tabla de casos.
- Contraprueba: reintroducir el error en el código bajo prueba y confirmar que el caso que lo cubre cae.
- El informe trae la frase de la sección 5 con sus cifras, no solo un porcentaje.
