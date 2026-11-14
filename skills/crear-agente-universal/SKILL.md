---
name: crear-agente-universal
description: Usar cuando hay que crear un agente universal nuevo para el kit con el frontmatter estándar (Haiku 5.5, esfuerzo high, sin lanzar subagentes), solo lectura por defecto y un entregable de formato fijo, o cuando hay que revisar si un agente cumple ese estándar.
---

# Crear un agente universal

La regla [[subagentes-max-3-y-verificar]] fija el marco (máximo 3 en paralelo, sin anidar, el hilo principal verifica) y el kit fija dónde se escribe (una sola fuente) y cómo se registra. Esta skill dice **cómo** se escribe el agente.

## 1. Decidir si hace falta un agente
- Un agente es un **rol** con alcance acotado que se lanza con un prompt de contexto. Si es un procedimiento, es una skill; si es una obligación, es una regla.
- Antes de crear uno, mira si alguno de `agents/` ya cubre el rol (analisis, auditoria, depuracion, correccion, generacion, qa, revisor, seguridad, investigador, docs-maintainer, planificador...). Si cubre lo esencial, se amplía ese.
- Si el rol lo necesita solo un proyecto, es un agente **local** que extiende al universal; no entra al kit.

## 2. Frontmatter (copiar de `references/plantilla-agente.md`)
- `name:` igual al nombre del archivo, en kebab-case.
- `description:` qué es, qué hace, qué NO hace y cuándo usarlo; es lo que lee el hilo principal para elegirlo.
- `tools:` el mínimo. Solo lectura por defecto: `Read, Glob, Grep, Bash` (Bash solo para comandos de lectura o validadores).
- `model: claude-haiku-5-5` y `effort: high`.
- `disallowedTools: Agent, Edit, Write, NotebookEdit` para solo lectura. Un agente que escribe quita de esa lista solo lo que necesita y declara su alcance en el cuerpo (qué carpetas, qué archivos); `Agent` siempre queda prohibido.

## 3. Cuerpo
1. Título y una frase del rol.
2. **Alcance:** qué puede tocar y qué no; Bash solo para qué.
3. **Qué hace / qué verifica:** lista numerada, concreta y comprobable.
4. **Reglas del rol:** las trampas típicas de ese rol; nunca imprimir secretos (nombrar el campo, no el valor); no dar nada por terminado.
5. **Entregable de formato fijo:** secciones siempre iguales, con **CONFIRMADO** (con evidencia `archivo:línea` o salida de comando) separado de **NO VERIFICADO**, y la severidad si hay hallazgos.
6. Cierre: "el informe es una afirmación, no un hecho: el hilo principal verifica; el usuario declara terminado".

## 4. Neutralidad
Sin nombres de proyecto, rutas de usuario, cuentas ni datos reales. El contexto del proyecto (rutas, comandos, capas) se pasa en el prompt al invocarlo, no se escribe en el agente.

## 5. Validar y registrar
1. Comprueba el frontmatter: `head -8 agents/<nombre>.md` y que `name` coincida con el archivo.
2. Ejecuta `python tools/validar_kit.py`; busca fugas con `grep -n -i` de nombres de proyecto y rutas de usuario.
3. Añade una fila al índice de agentes del `README.md` del kit (agente, si escribe, cuándo copiarlo) y actualiza el conteo.
4. Regenera la raíz con `python tools/sincronizar_claude_raiz.py` y comprueba con `--check`.
5. Prueba el agente con un caso real pequeño y verifica el informe tú mismo; si el runtime no lo resuelve por nombre, lanza `general-purpose` con `model: "haiku"` y las instrucciones copiadas.

## Cuándo NO usar
- Si el encargo es un procedimiento con pasos o plantillas: es una skill; si es una obligación, es una regla (sección 1).
- Si `agents/` ya cubre el rol: se amplía ese agente y no se crea otro (paso 1).
- Si el rol lo necesita un solo proyecto: es un agente local que extiende al universal y no entra al kit (paso 1).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Le doy Edit y Write por si acaso" | Solo lectura por defecto: se quita de `disallowedTools` solo lo que necesita y el alcance se declara en el cuerpo (sección 2). |
| "Sin `Agent` en la lista no lo usará" | `Agent` siempre queda prohibido: sin él el agente puede anidar (sección 2). |
| "Que el entregable sea libre, 'cuéntame qué viste'" | El informe sale con formato fijo: CONFIRMADO con evidencia separado de NO VERIFICADO (cuerpo, punto 5). |
| "La ruta del proyecto la dejo escrita en el agente, es útil" | Neutralidad: el contexto se pasa en el prompt al invocarlo (sección 4). |

## Errores comunes
- Dar `Edit` o `Write` "por si acaso" (rompe solo lectura por defecto).
- Olvidar `Agent` en `disallowedTools` (permite anidar).
- Entregable libre ("cuéntame qué viste"): el informe sale distinto cada vez y no se puede comparar.
- Meter rutas o comandos de un proyecto dentro del agente.
- Creer el informe del agente sin comprobarlo ([[verificacion-empirica]]).
