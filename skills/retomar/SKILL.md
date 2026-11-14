---
name: retomar
description: Usar cuando el usuario escribe /retomar o pide ponerse al día al empezar una sesión (dónde quedamos, qué cambió y qué está pendiente), sin cambiar nada hasta que lo diga.
disable-model-invocation: true
---

# /retomar — ponerse al día antes de empezar

Sigue la skill `inicio-de-sesion` y la regla [[continuidad-multi-maquina]]. No cambies nada hasta que el usuario lo diga. Resume en pocas líneas:

1. **Estado del repositorio:** `git status --short` y `git fetch`; compara la rama con su remoto (adelante o atrás). Si diverge o no cuadra con lo que se creía, **para y explica**; no hagas `pull`, `merge` ni `reset`.
2. **Dónde quedamos:** el bloque "Para retomar" de `.memory/PROJECT_STATE.md` (y `.memory/decisiones.md` si toca algo ya decidido), las últimas entradas del registro de cambios y la **bitácora abierta** más reciente (`docs/humano/humanoN.md` de mayor número).
3. **Pendientes:** lo que espera una decisión del usuario y lo bloqueado.
4. **Planes abiertos:** si hay planes con casillas, el estado de cada fase (hechas, parciales, pendientes), citando el archivo.

Termina con: **en qué quedamos**, **qué espera decisión del usuario** y **qué propones hacer hoy**. Separa lo confirmado (visto ahora) de lo que solo dice un documento.

## Cuándo NO usar
- Para trabajo concreto: este comando solo informa; el trabajo empieza cuando el usuario lo indica.
- En una pregunta puntual que no es una sesión de trabajo.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "La memoria dice que está al día, no hago `git fetch`" | La memoria envejece; el estado real del repo se comprueba. |
| "Hago `pull` ya que está detrás" | Si el resultado es inesperado se para y se entiende primero; nunca `reset --hard`. |

## Errores comunes
- Dar como hecho lo que solo dice un documento sin contrastarlo.
- Empezar a editar antes de que el usuario decida.

## Verificación
- El resumen separa lo visto ahora de lo que dice un documento y termina con las tres líneas pedidas.
