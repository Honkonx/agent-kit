---
name: crear-prompt-para-ia
description: Usar cuando hay que escribir un prompt o instrucciones para que otra IA, otra sesión o un subagente ejecute una tarea sin ver esta conversación: convertir un pedido aclarado y un plan en un texto largo guardado en un archivo y en una versión corta que apunta a ese archivo, con contexto, objetivo, condición de término, restricciones y formato de entrega.
---

# Crear un prompt para otra IA

Quien lo recibe **no ve esta conversación**: todo lo necesario va en el texto o en archivos que pueda leer. Apoyos: [[pedidos-sin-ambiguedad]] (el pedido debe estar aclarado antes), [[planes-con-casillas]], [[usuario-declara-listo]], [[secretos]], [[respuestas-concisas]]. Se usa dentro de `preparar-goal`, pero sirve para cualquier prompt (un subagente, otra herramienta, otra sesión).

## 1. Reunir las entradas
1. **Pedido aclarado** (skill `aclarar-pedido`): objetivo, fin medible, comprobación, alcance, restricciones. Si falta, aclararlo antes.
2. **Plan** (skill `plan-con-casillas`): ruta del archivo; el prompt lo cita en lugar de copiarlo.
3. Dónde vive lo que hay que leer: archivos clave, reglas del proyecto, comandos de prueba.

## 2. Escribir el prompt largo
Copia `references/plantilla-prompt-largo.md` a `docs/goal/<tema>.md` (nombre por tema; la fecha va dentro) y complétala. Secciones:
- **Contexto:** qué es el proyecto en 3 líneas y qué archivos leer primero.
- **Objetivo:** una frase.
- **Condición de término:** estado final medible, la comprobación (comando o prueba) cuya salida **se muestra en la conversación**, y un tope.
- **Restricciones y qué NO hacer:** archivos protegidos, secretos, permisos, producción, con el motivo de cada una.
- **Cómo trabajar:** leer el plan, orquestar y delegar, actualizar el plan al cerrar cada meta, verificar con comandos propios, parar y reportar si se atasca.
- **Entrega al terminar:** informe con lo hecho, lo verificado, lo no verificado y lo pendiente; no declarar "listo".

Reglas de redacción: instrucciones concretas y afirmativas, el motivo de cada restricción, rutas relativas al proyecto, nada que dependa de la conversación, sin secretos ni rutas de usuario, ejemplos solo donde el formato sea crítico. Corto: lo que no cambia el resultado sobra.

## 3. Escribir el prompt corto
Una a tres frases que **apuntan al archivo** y repiten lo mínimo para que quien juzga el término lo entienda sin abrirlo: "Lee `docs/goal/<tema>.md` y haz lo que dice, empezando por <primera meta>. Termina cuando <fin medible en una frase>; la comprobación es <comando> y su salida debe verse aquí. Tope: <turnos, tiempo o tokens>." El fin medible y el tope van **en el corto** también.

## 4. Validar y guardar
```
python scripts/validar_prompt.py docs/goal/<tema>.md --corto "<texto corto>"
```
Comprueba secciones, fin medible, comprobación y tope no vacíos, sin marcadores `<…>` sin reemplazar, sin secretos ni rutas de usuario, y que el corto nombre el archivo y un tope. Si el proyecto no tiene `docs/goal/README.md`, créalo con una tabla de los prompts guardados (qué hay, qué no va, tipo: foto fechada).

## 5. Preguntar qué mostrar
Pregunta **una vez** al usuario si quiere el prompt **largo** en pantalla o solo el **corto** que apunta al archivo (recomendado: el corto; el largo ya está guardado). Muestra siempre la ruta del archivo.

## Cuándo NO usar
- Para aclarar qué quiere el usuario: eso es `aclarar-pedido`.
- Para planificar fases y metas: eso es `plan-con-casillas`; el prompt lo cita.
- Para el encargo de un subagente en una tarea corriente: basta el formato de encargo de `delegar-a-subagentes`; esta skill es para tareas largas o sin supervisión.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El contexto ya lo sabe, está en el chat" | Quien recibe el prompt no ve el chat: lo que no esté en el texto o en un archivo legible no existe para él. |
| "Pego todo el plan dentro del prompt" | Se cita la ruta; copiarlo crea dos versiones que divergen. |
| "El corto solo apunta al archivo" | Quien juzga el término puede ver solo la conversación: el fin medible y el tope van también en el corto. |
| "Le pongo mis claves para que no se detenga" | Nunca: se pasan por variable de entorno o archivo ignorado ([[secretos]]). |

## Errores comunes
- Prompt con "haz que funcione" como condición de término.
- Dejar marcadores `<…>` sin reemplazar en el archivo guardado.
- Prompt larguísimo que entierra lo importante.
- Olvidar el tope: un objetivo persistente sin tope puede gastar sin límite.

## Verificación
- `validar_prompt.py` sale con 0 sobre el archivo y sobre el corto.
- El archivo está en `docs/goal/` con `**Fecha:**` y `**Tipo:** foto fechada`, y figura en su README.
- La comprobación del fin medible es un comando o prueba que existe y que se corrió una vez a mano.
- El usuario eligió qué ver en pantalla y se mostró.
