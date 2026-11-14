---
name: cierre-de-ronda
description: Usar cuando una tarea, tanda o sesión produjo un resultado real y toca cerrarla (verificar, documentar, guardar memoria, commit, push si está autorizado e informe en pantalla), o cuando el usuario pide opinión, propuesta o plan, o dice haz todo; o cuando se terminó el trabajo y toca dejar todo documentado y subir o guardar los cambios con un resumen final.
---

# Cierre de ronda

La regla [[cierre-de-ronda]] dice **qué** se cumple; esta skill es el checklist para ejecutarlo. Apoyos: [[usuario-declara-listo]], [[verificacion-empirica]], [[secretos]], `publicar-solo-con-orden`, [[archivos-protegidos]], [[seguridad-despliegue-y-datos]]. Enlaza con las skills `plan-con-casillas` y `bitacora-humana`.

## 0. ¿Hay cierre?
No hay cierre (ni escrituras, ni commit, ni push) si la ronda fue una pregunta, opinión o auditoría solo lectura. En ese caso solo el informe y, si procede, el plan del paso 7.

## 1. Verificar el efecto
1. Ejecuta pruebas, linters o build proporcionales al riesgo y mira el **efecto**, no que el comando se invocó.
2. Un fallo impide hablar de cierre correcto, pero no obliga a esconder el avance ni a borrar cambios. Anótalo.
3. Separa lo verificado de lo no verificado.

## 2. Documentar
1. Actualiza el documento vigente afectado, el changelog, los índices y los pendientes abiertos o cerrados; corrige lo desfasado en esta ronda.
2. Plan con casillas: fichas al día con evidencia; Hecho y Listo los marcas tú al cerrar cada meta (skill `plan-con-casillas`). Que el producto esté bien lo declara solo el usuario.
3. Bitácora al día: el mensaje de esta ronda registrado con cita e interpretación; ejecuta el verificador de la skill `bitacora-humana` (`verificar_bitacora.py`). Sin eso no hay cierre.
4. Artefactos entregables: reconstruye los vigentes; si uno no se pudo, decláralo desactualizado.

## 3. Memoria
Guarda solo lo durable: decisiones, hallazgos que otra sesión necesitaría, lecciones. Nada deducible del código ni secretos. Actualiza `.memory/` (skill `memoria-del-proyecto`): reescribe el bloque único `Para retomar`, añade las decisiones y lecciones nuevas con fecha y estado, y corre `verificar_memoria.py .memory`.

## 4. Commit (solo si hay trabajo real y verificaciones en verde)
1. Revisa `git status` y `git diff`; solo lo propio, nunca cambios ajenos.
2. Escanea secretos de lo que entra.
3. `git add` por nombre de archivo, mensaje técnico y específico.
4. No hagas commit si las verificaciones relevantes fallan o si se pidió solo análisis.

## 5. Push (solo si está autorizado)
Solo a la rama y remoto que el proyecto o el usuario autorizó; esa autorización no se extiende a otra rama, repos públicos, release ni despliegue. Nunca `--no-verify` ni `--force`. Si falla, informa el estado exacto, no digas que se publicó. Un commit solo de docs no se despliega.

## 6. Informe en pantalla
Usa `references/plantilla-informe-cierre.md`. Va **en el texto de la respuesta**, no solo en un archivo: hecho, verificado, no verificado, pendientes, opinión honesta y siguiente plan. Nunca digas "listo": lo declara el usuario.

## 7. Si piden opinión, propuesta o plan
Termina con: (a) opinión completa y honesta; (b) plan por fases y puntos numerados (qué, quién, esfuerzo, impacto, riesgo, qué queda sin tocar); (c) decisiones que necesitas; (d) espera la luz verde. No ejecutes nada del plan mientras esperas. Plan complejo: ver `plan-con-casillas` (el comando `/plan` y el agente `planificador` lo redactan). El comando `/cerrar` ejecuta esta skill.

## 8. "Haz todo"
Significa todo el backlog pendiente. Las únicas paradas son los puntos de cierre; tras cada uno sigues. Terminas cuando no queda nada o cada resto tiene un bloqueo real demostrado. No concede permisos nuevos.

## Cuándo NO usar
- Ronda de pregunta, opinión o auditoría solo lectura: no hay cierre, solo el informe (paso 0).
- Si el usuario pidió solo análisis, no se crean documentos ni se hace commit para "cerrar".
- Un cierre no concede permisos: despliegue, migraciones, dinero y archivos protegidos conservan su autorización propia.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Pasan las pruebas, ya está" | El cierre separa compilación, pruebas automáticas y QA real; y nunca dice "listo": lo declara el usuario. |
| "El push va incluido en el cierre" | Solo si el proyecto o el usuario lo autorizó para esa rama y remoto. |
| "Documento después, ahora subo" | Verificar, documentar, memoria y commit van en ese orden dentro de la misma ronda. |

## Errores comunes
- "Listo, todo subido" sin pruebas.
- Push a un remoto no autorizado porque "el cierre lo incluye".
- Informe solo como enlace a un `.md`.
- Mezclar lo verificado con lo supuesto.
- Pedir permiso para continuar tras "haz todo".
- Cerrar con la bitácora sin escribir.
