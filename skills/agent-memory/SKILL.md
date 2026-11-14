---
name: agent-memory
description: Usar cuando haya que decidir qué contexto duradero del proyecto guardar en una carpeta de memoria (`.memory/` o similar), cómo recuperarlo o cómo mantenerlo correcto entre sesiones.
---

# Memoria auxiliar del agente

> Guía auxiliar. El proceso completo (archivos fijos, plantillas y verificador) está en la skill `memoria-del-proyecto` y en la regla del mismo nombre. Complementa las reglas `documentar-en-vivo`, `docs-organizacion-y-fechada` y `continuidad-multi-maquina`: la memoria es un índice de contexto, no la fuente de verdad.

## Qué retener
- Solo hechos o decisiones asentadas que una sesión futura tendría que redescubrir y que sigan siendo útiles más allá de la tarea actual.
- Entradas breves y buscables: tema, fecha, estado (vigente/reemplazada), enlaces a los archivos fuente y límites de verificación.
- Enlazar la fuente autoritativa (requisito, decisión o implementación) en lugar de duplicarla.
- Separar los hechos confirmados de las hipótesis (`no-asumir-separar-confirmado`) y marcar lo que cambia con el tiempo para volver a verificarlo.

## Qué no guardar
Secretos o tokens (regla `secretos`), registros financieros reales, datos personales innecesarios ni transcripciones completas.

## Cuándo escribir
- No crear ni actualizar memoria solo porque hubo trabajo: mandan las instrucciones explícitas del usuario y las reglas del repositorio. Una auditoría pedida «en pantalla» se queda en pantalla, salvo que una regla vigente exija un artefacto durable.
- Cuando una decisión cambia, marcar la nota vieja como reemplazada y apuntar a la nueva; no reescribir en silencio el contexto histórico.

## Cuándo NO usar
- Para decidir dónde va un documento vigente o fechado: eso es la regla `docs-organizacion-y-fechada`; la memoria solo indexa.
- Para crear la estructura o las plantillas de la memoria: usar la skill `memoria-del-proyecto`, que trae los archivos fijos.
- Para lo que solo importa a la conversación actual, o una auditoría pedida «en pantalla»: se queda en pantalla.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Hubo trabajo hoy, lo anoto en la memoria por si acaso" | No se escribe porque hubo trabajo: solo si hay algo asentado y útil más allá de la tarea. |
| "Pongo la decisión aquí y no en el documento, es más rápido" | La memoria enlaza a la fuente autoritativa y no la duplica. |
| "La memoria dice X, así que X es cierto" | La memoria envejece: se verifica contra el código o el sistema antes de usarla como hecho. |
| "Cambio la nota vieja para que quede al día" | La decisión cambiada marca la nota vieja como reemplazada y apunta a la nueva; el contexto histórico no se reescribe. |

## Errores comunes
- Guardar una transcripción o un resumen largo de la sesión en lugar de un hecho asentado.
- Copiar una decisión que ya vive en `docs/` y dejar dos versiones que divergen.
- Guardar como durable un dato provisional sin marcarlo para volver a verificarlo.
- Anotar un token, una contraseña o un registro financiero real "para no perderlo" (ver la regla `secretos`).

## Verificación
- Cada entrada tiene tema, fecha, estado (vigente o reemplazada) y enlace a su fuente; se comprueba releyendo la entrada y buscando la ruta citada en el proyecto.
- Ningún secreto ni dato personal en la carpeta de memoria: buscar los patrones de la regla `secretos` (`ghp_`, `sk-`, `-----BEGIN`) antes de confirmar.
- El `SKILL.md` pasa `validar_skill.py --estricto` de la skill `skill-creator` sobre la carpeta de esta skill.
