---
name: plan
description: Usar cuando el usuario escribe /plan o pide explícitamente un plan con fases, metas y casillas antes de construir un trabajo mediano o grande (crear el plan y esperar la luz verde, sin ejecutar nada).
disable-model-invocation: true
---

# /plan — crear un plan antes de construir

Sigue la skill `plan-con-casillas` y la regla [[planes-con-casillas]]. Este comando solo se invoca a mano: `/plan <pedido>`.

1. **Decide si lleva plan.** Una pregunta, un cambio pequeño o una tarea de una sola meta no lleva: dilo y hazlo directamente.
2. Si lleva plan, delega la redacción en el agente `planificador` (Haiku 5.5, esfuerzo high) con un encargo específico: el texto textual del pedido, la carpeta de planes y el nombre del archivo (por tema; la fecha va dentro).
3. **Verifica lo que devuelva:** que `validar_plan.py` dé OK, que cada pedido del usuario sea una meta, que cada meta tenga un criterio medible y que ninguna casilla venga fichada ni la columna Listo llena.
4. **Muestra el plan en pantalla** (fases, metas, riesgos y decisiones que necesitas) y **espera la luz verde** antes de construir.

No ejecutes ninguna meta mientras esperas.

## Cuándo NO usar
- Para preguntas, opiniones, análisis o cambios de una sola meta: se responde o se hace directamente.
- Para ejecutar un plan ya aprobado: eso es trabajo de las metas, no de `/plan`.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Empiezo con la primera meta mientras decide" | Mientras se espera la luz verde no se ejecuta nada. |
| "El agente dice que el plan es válido" | Lo compruebo yo con `validar_plan.py`; el informe del agente es una afirmación. |

## Errores comunes
- Plan sin criterio medible por meta.
- Casillas ya tachadas o columna Listo llena por quien redactó.

## Verificación
- El validador `validar_plan.py` de la skill `plan-con-casillas` da OK sobre el plan y el plan se mostró en pantalla.
