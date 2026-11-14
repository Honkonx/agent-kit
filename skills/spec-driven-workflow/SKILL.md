---
name: spec-driven-workflow
description: Usar cuando se va a construir una función sustantiva y hay que escribir la especificación antes del código, definir criterios de aceptación, o convertir requisitos confirmados en un plan de implementación verificable.
---

# Especificación primero, proporcional a la función

La spec es un contrato: qué DEBE hacer el sistema, qué NO hará y cómo se acepta. Va antes del código. Lo ambiguo se pregunta ([[no-asumir-separar-confirmado]]); una spec en borrador no autoriza cambios de código, datos ni servicios externos.

## Cuándo
- Sí: funciones nuevas o cambios que afectan dominio crítico (dinero, datos persistentes, sincronización, importación/exportación, seguridad) o flujos principales de usuario.
- No: arreglo acotado o cambio de documentación pequeño; bastan sus criterios en la tarea y su prueba. Mantenerla proporcional: sin API, modelo de datos ni métricas si la función no los necesita (en una sección que no aplica, escribir "N/A - motivo").

## Contenido de la spec
1. Objetivo, usuario y flujo afectado; contexto con evidencia.
2. Requisitos confirmados (`FR-n`, atómicos y verificables; MUST/SHOULD/MAY de RFC 2119) y no funcionales con umbral medible (`NFR-n`).
3. **Criterios de aceptación** (`AC-n`) en Dado / Cuando / Entonces, con resultado observable; cada uno cita al menos un FR/NFR. Sin lenguaje subjetivo ("rápido", "amigable"): si no se puede escribir una prueba, se reescribe.
4. Casos límite y de fallo (`EC-n`): al menos un fallo por dependencia externa (red, base, archivo, entrada de usuario).
5. Contratos y datos (si corresponde): interfaces de entrada/salida con éxito y error; entidades con campo, tipo y restricciones.
6. Fuera de alcance, con motivo.
7. Preguntas abiertas, separadas de lo confirmado y de los supuestos.
8. Trazabilidad `AC -> prueba -> resultado`.

Plantilla completa y ejemplo resuelto: `references/spec_format_guide.md`. Biblioteca de criterios: `references/acceptance_criteria_patterns.md`.

## Antes de aceptar una función con riesgo
Responder los cuatro riesgos: valor (¿alguien la usará?), usabilidad (¿se entiende a la primera?), factibilidad (¿encaja en la arquitectura y el offline/sync?) y viabilidad (¿se puede mantener?). Decidir construir, pivotar o descartar.

## Flujo en fases
1. **Requisitos:** preguntar problema, usuarios, éxito y qué NO se construye; leer el código existente; listar incógnitas. Salida: se puede explicar en 2 minutos.
2. **Escribir la spec** (arriba). Salida: otra persona puede implementarla sin preguntar.
3. **Validar:** `python scripts/spec_validator.py --file spec.md --strict` (puntaje 0-100, objetivo 80+) y revisar a mano: cada FR tiene AC, cada AC es probable, los fallos externos están cubiertos, los NFR son medibles.
4. **Generar pruebas** desde los AC y EC: `python scripts/test_extractor.py --file spec.md --framework pytest --output tests/` (stubs que fallan al inicio; adaptar el framework al stack). Una plantilla de spec: `scripts/spec_generator.py`.
5. **Implementar** un AC a la vez: prueba roja, código mínimo, suite completa sin regresiones, siguiente. Nada fuera de la spec; si falta un requisito, parar y actualizar primero la spec.
6. **Autorrevisión:** cada AC y EC tiene prueba que pasa; sin scope creep ni cosas de "Fuera de alcance"; contratos y esquema coinciden con el código; NFR con evidencia medida ([[verificacion-empirica]]). Nunca "listo": lo declara el usuario ([[usuario-declara-listo]]).

## Plan de implementación
Cuando la spec es mediana o grande, el plan de implementación se escribe con la skill `plan-con-casillas` y la regla [[planes-con-casillas]]: una fase por bloque de AC, una meta por AC o grupo, con su criterio verificable (la prueba del AC) y casillas Hecho/Listo. Si cambia el alcance, se actualiza primero la spec y luego el plan, con fecha.

## Cuándo parar y preguntar
Parar si: aparece algo fuera de la spec; la ambigüedad supera ~30% de un requisito; hay cambio incompatible de contrato o esquema; toca autenticación, cifrado o datos personales; hay un NFR que no se puede medir; depende de otro equipo o servicio. Seguir sola cuando la spec es clara, el cambio no rompe contratos y es traducción directa de un AC. Escalar con: bloqueo (ID), pregunta concreta, opciones con pros y contras, recomendación e impacto de esperar. Matriz completa: `references/bounded_autonomy_rules.md`.

## Antipatrones
Codificar antes de aprobar; criterios vagos; solo camino feliz; spec escrita después del código (eso es documentación); gold-plating; AC sin FR; saltarse la validación.

## Cuándo NO usar
- Arreglo acotado o cambio de documentación pequeño: la sección Cuándo lo excluye; bastan los criterios de la tarea y su prueba.
- Ya existe una spec aprobada y el paso es traducir un AC a código: se sigue sin reescribir la spec (sección "Cuándo parar y preguntar", "traducción directa de un AC").
- Entender código heredado sin especificación: eso es `spec-miner` (ingeniería inversa); esta skill escribe la spec hacia adelante.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Ya sé lo que quiero, escribo la spec cuando termine el código" | Es el antipatrón "spec escrita después del código": eso es documentación. La spec va antes, y una en borrador no autoriza cambios. |
| "'Rápido' y 'amigable' bastan para empezar" | Sin lenguaje subjetivo: si no se puede escribir una prueba, el AC se reescribe (contenido, punto 3). |
| "Probé el camino feliz, los fallos los veo después" | Cada dependencia externa (red, base, archivo, entrada de usuario) lleva al menos un EC de fallo (contenido, punto 4). |
| "Como el requisito cambió poco, lo implemento y actualizo la spec luego" | Si falta un requisito se para y se actualiza primero la spec (flujo en fases, paso 5). |

## Verificación
- Ejecutar `python scripts/spec_validator.py --file spec.md --strict` y obtener 80 o más; después revisar a mano que cada FR tiene AC.
- Tras `python scripts/test_extractor.py --file spec.md --framework pytest --output tests/`, comprobar que los stubs fallan antes de implementar.
- Cada `AC-n` aparece en la trazabilidad `AC -> prueba -> resultado` con una prueba que pasa (contenido, punto 8).
- Cada `NFR-n` tiene una medición con número en la evidencia (autorrevisión, paso 6).
