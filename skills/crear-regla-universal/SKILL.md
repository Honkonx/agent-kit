---
name: crear-regla-universal
description: Usar cuando hay que crear una regla universal nueva para el kit (o reescribir una existente) con la plantilla estándar, 25 a 70 líneas, enlaces solo a reglas que existen, validada y registrada en el inventario de reglas.
---

# Crear una regla universal

El kit exige que toda pieza nueva se escribe en la fuente, es neutra y se registra; esta skill dice **cómo** se escribe una regla. Una regla dice **qué** se cumple; el **cómo** paso a paso es una skill que la enlaza (ver `skill-creator`).

## 1. Decidir si es regla y si es universal
- Es regla si es una obligación o prohibición que debe cumplirse siempre en una situación reconocible. Si es un procedimiento, es una skill; si es un rol de trabajo, es un agente.
- Es universal si sirve en cualquier proyecto sin editarla. Si solo vale para un stack, es un **módulo** (`stack-<x>`). Si depende de un dominio o cliente, es **local**: no entra al kit.
- Comprueba que no exista ya: busca el tema en `rules/` y en `rules/_INVENTARIO.md`. Si existe, se amplía esa regla, no se crea otra.

## 2. Escribirla con la plantilla
1. Copia `references/plantilla-regla.md` a `rules/<nombre-en-kebab-case>.md`.
2. Título: la obligación en una frase. Línea `Aplica a:` con las reglas relacionadas como `[[nombre]]`.
3. Párrafo inicial: qué se cumple, en dos o tres frases.
4. `Por qué`: el daño real que evita (un hecho, no una opinión).
5. `Cómo se aplica`: viñetas verificables, en imperativo; agrupa con negritas si son más de seis.
6. `Ejemplos`: pares No / Sí con casos concretos y neutros.
7. `Qué se ajusta por proyecto`: lo que cada proyecto debe rellenar (rutas, comandos, listas, límites).

## 3. Qué va y qué NO va
- **Va:** la obligación, su motivo, pasos comprobables, ejemplos neutros, el punto de ajuste por proyecto.
- **No va:** nombres de proyectos, clientes o personas; rutas de usuario; cuentas, claves o datos reales; comandos específicos de un solo proyecto; la historia de cómo se descubrió (se resume en `Por qué` sin nombres); el procedimiento largo (va en una skill).

## 4. Medidas y enlaces
- Entre **25 y 70 líneas**. Si pasa de 70, divide: lo esencial en la regla, el procedimiento en una skill.
- Enlaces `[[x]]` solo a reglas que existen en `rules/` (compruébalo con `ls rules/`). Una regla universal no enlaza reglas locales.

## 5. Validar y registrar
1. Cuenta líneas: `wc -l rules/<nombre>.md` (25 a 70).
2. Ejecuta `python tools/validar_kit.py` y corrige lo que marque (enlaces rotos, secciones, fugas de nombres).
3. Busca fugas a mano: `grep -n -i "<nombre de proyecto>" rules/<nombre>.md` y rutas de usuario.
4. Añade UNA fila a la tabla "Grupos" de `rules/_INVENTARIO.md` (ID siguiente, regla, qué cubre, acción, tipo `core` o `modulo: x`, estado) y, si es core, a la lista del `README.md` del kit.
5. Si la regla pide una skill de procedimiento, regístrala en `skills/_INVENTARIO_SKILLS.md` y en `rules/_CRUCE_SKILLS_REGLAS.md`.
6. Regenera la raíz con `python tools/sincronizar_claude_raiz.py` y comprueba con `--check`.

## Cuándo NO usar
- Si es un procedimiento con pasos, scripts o plantillas: es una skill, y la regla solo la enlaza (secciones 1 y 4).
- Si solo vale para un stack: es un módulo con prefijo `stack-`, no una regla universal (sección 1).
- Si el tema ya existe en `rules/` o en `_INVENTARIO.md`: se amplía esa regla y no se crea otra (paso 1).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Meto el procedimiento entero en la regla, así queda todo junto" | Si pasa de 70 líneas se divide: lo esencial queda en la regla y el procedimiento va a una skill (sección 4). |
| "Enlazo mi regla local, así queda completa" | Una regla universal no enlaza reglas locales; los enlaces solo van a reglas que existen en `rules/` (sección 4). |
| "Con el validador en verde, la regla está terminada" | El validador revisa enlaces y fugas; la entrega la declara el usuario ([[usuario-declara-listo]]). |
| "No pongo 'Qué se ajusta por proyecto', la regla es obvia" | Sin esa sección la regla no es copiable entre proyectos (sección 2, paso 7). |

## Errores comunes
- Meter el procedimiento entero en la regla (se pasa de 70 líneas).
- Enlazar a una regla que solo existe en un proyecto.
- Ejemplos con datos reales o nombres propios.
- Olvidar `Qué se ajusta por proyecto`: sin él la regla no es copiable.
- Registrar en el README pero no en el inventario (o al revés).
- Dar la regla por entregada porque el validador pasa: lo declara el usuario ([[usuario-declara-listo]]).
