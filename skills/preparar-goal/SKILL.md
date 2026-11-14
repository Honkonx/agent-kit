---
name: preparar-goal
description: Usar cuando el usuario quiere que la IA trabaje sola hasta terminar una tarea (el comando /goal de Claude Code o de Codex, o un objetivo persistente equivalente) y hay que prepararlo antes: evaluar el proyecto y sus pendientes, aclarar el pedido, crear el plan, redactar el prompt, guardarlo en docs/goal y entregar el comando listo para pegar; prepara pero no ejecuta el objetivo.
---

# Preparar un objetivo persistente (`/goal`)

Orquesta cinco piezas que también sirven por separado: `evaluar-proyecto-y-objetivo`, `aclarar-pedido`, `plan-con-casillas`, `crear-prompt-para-ia` y, para el modo de trabajo, la regla [[subagentes-max-3-y-verificar]] (orquestador y ayudantes). La regla [[objetivos-persistentes-verificables]] dice **qué** se cumple; esto es el **cómo**. Apoyos: [[pedidos-sin-ambiguedad]], [[usuario-declara-listo]], [[planes-con-casillas]]. **No lanza el objetivo:** entrega el comando y el usuario lo pega.

## 1. Comprobar que aplica
Un objetivo persistente sirve para trabajo grande con **salida verificable** (pruebas que pasan, archivos que existen, una lista vacía). No sirve si no hay forma de comprobar el fin, si la decisión es del usuario, ni para producción, datos reales o dinero. Si no aplica, dilo y propón la alternativa (trabajar por metas con supervisión).

## 2. Evaluar el proyecto y el objetivo
Usa la skill `evaluar-proyecto-y-objetivo` (solo lectura): estado real del proyecto, mejoras pendientes y si el objetivo encaja con su propósito y madurez. Su recomendación manda: **PROCEDER** sigue adelante; **ACOTAR** vuelve al usuario con lo que hay que reducir o reordenar; **NO USAR OBJETIVO PERSISTENTE** detiene el flujo y propone la alternativa. Los pendientes que son prerrequisito pasan a la primera fase del plan.

## 3. Aclarar el pedido
Usa la skill `aclarar-pedido`: seis datos (objetivo, fin medible, comprobación, alcance, restricciones, qué decide el usuario). Sin los seis, no se sigue.

## 4. Crear el plan
Usa `plan-con-casillas` (en esta herramienta también el comando manual `/plan`): fases y metas con casilla y criterio medible, en `docs/planes/<tema>.md`. Si el alcance es grande, muestra el plan y espera el visto bueno antes de seguir. El diagnóstico previo va en una sección "Diagnóstico previo" del plan.

## 5. Redactar y guardar el prompt
Usa `crear-prompt-para-ia`: prompt largo en `docs/goal/<tema>.md` y versión corta, validados con `validar_prompt.py`. El apartado "Contexto" recoge el diagnóstico previo; el corto lleva el fin medible, la comprobación y el tope.

## 6. Armar el comando
Según la herramienta (`references/herramientas.md`): en Claude Code, `/goal <condición>` con la condición corta; en Codex, el objetivo con su tope de tokens en la configuración; en otra IA, el prompt corto como primer mensaje. La condición incluye siempre: fin medible, comprobación **visible en la conversación** y un tope.

## 7. Preguntar qué mostrar y entregar
Pregunta **una vez**: ¿el prompt **largo** en pantalla o solo el **corto** que dice "lee `docs/goal/<tema>.md` y haz esto primero"? (recomendado: el corto). Muestra siempre el comando listo para pegar y las rutas del plan y del prompt. Recuerda al usuario: cómo cancelarlo, que el gasto se revisa, y que "cumplida" no es "listo".

## 8. Dejar constancia
Anota en `.memory/` solo lo durable (que existe el objetivo y dónde está el plan); el detalle ya vive en el plan y el prompt ([[memoria-del-proyecto]]).

## Cuándo NO usar
- Tareas pequeñas o con supervisión continua: basta pedir y revisar por metas.
- Cuando solo hace falta un plan: `plan-con-casillas`. Cuando solo hace falta un prompt para otra sesión: `crear-prompt-para-ia`.
- Para ejecutar el objetivo: esta skill no lo hace; lo lanza el usuario.
- Para trabajo sobre producción, datos reales o dinero: cada acción exige su autorización ([[seguridad-despliegue-y-datos]]).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El usuario ya dijo qué quiere, voy directo al comando" | Sin los seis datos y el plan, la condición queda vaga y el evaluador aprueba sin prueba o no termina. |
| "El tope se lo pone la herramienta" | En Claude Code no hay un tope configurable de turnos ni de costo: va escrito en la condición. |
| "Que el evaluador compruebe el resultado" | No ejecuta comandos ni lee archivos: solo ve lo que se muestra en la conversación; la salida de la comprobación debe verse. |
| "El objetivo se cumplió, entonces está listo" | Cumplir la condición es un veredicto sobre la condición; lo verifica el hilo principal y el producto lo acepta el usuario. |

## Errores comunes
- Una condición de término que solo dice "funciona" o "termina".
- Prompt corto que apunta al archivo sin repetir el fin medible ni el tope.
- Saltarse el diagnóstico y lanzar un objetivo que choca con pendientes que lo bloquean.
- Lanzar el objetivo con permisos amplios sobre archivos protegidos o producción.
- Olvidar guardar el prompt en `docs/goal/` y quedarse solo con el chat.

## Verificación
- Hubo diagnóstico previo y su recomendación no fue "no usar objetivo persistente".
- Existen el plan (`docs/planes/<tema>.md`) y el prompt (`docs/goal/<tema>.md`), y `validar_prompt.py` sale con 0 sobre el archivo y el corto.
- El comando cabe en el límite de la herramienta (4000 caracteres en Claude Code) y lleva fin medible, comprobación visible y tope.
- El usuario eligió qué ver en pantalla y se mostró el comando.
- No se lanzó nada: el objetivo sigue sin ejecutarse.
