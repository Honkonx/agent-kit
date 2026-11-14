---
name: cerrar
description: Usar cuando el usuario escribe /cerrar o pide cerrar la ronda de trabajo (verificar, documentar, guardar memoria, commit con push solo si está autorizado, e informe en pantalla).
disable-model-invocation: true
---

# /cerrar — cerrar la ronda

Sigue la regla [[cierre-de-ronda]] y la skill `cierre-de-ronda`, sin saltarte pasos. Si la ronda fue solo análisis, pregunta u opinión, **no hay cierre**: dilo y no escribas nada.

1. **Verificar el efecto, no la invocación** (regla [[verificacion-empirica]]): ejecuta las comprobaciones del proyecto (compilar, linter, pruebas, y la prueba de punta a punta si la ronda llegó a una pantalla). Si algo falla, muestra la salida real.
2. **Documentar:** el documento vigente que el cambio toca, el registro de cambios, los pendientes que se abren o cierran y las decisiones. Verifica que la **bitácora** (`docs/humano/`) tiene el mensaje de esta ronda con su interpretación ([[bitacora-humana]]).
3. **Memoria:** actualiza `.memory/` con la skill `memoria-del-proyecto`: reescribe el bloque `Para retomar`, añade decisiones y lecciones con fecha y estado, y corre `verificar_memoria.py`. Solo lo durable; nada que se deduzca del código ni secretos.
4. **Artefactos entregables:** si el proyecto los tiene, reconstrúyelos; los que no se pudieron reconstruir se declaran desactualizados.
5. **Secretos:** escanea lo que entra al commit ([[secretos]]).
6. **Commit** de lo propio, mensaje técnico y específico, `git add` por nombre. **Push solo si el proyecto o el usuario lo autorizó** para esa rama y remoto (`publicar-solo-con-orden`). Nunca `--force` ni `--no-verify`.
7. **Informe en pantalla:** lo hecho; lo verificado y lo **no verificado** por separado (compilación, pruebas automáticas y QA real); pendientes; tu opinión; y el siguiente plan por fases. **Nunca digas que el producto está "listo"**: lo declara el usuario (las metas y el plan sí los cierras tú, con evidencia).

Si un paso no aplica, dilo y explica por qué.

## Cuándo NO usar
- En una ronda de pregunta, opinión o auditoría solo de lectura: no hay cierre y no se escribe nada.
- Para desplegar o publicar: el cierre no amplía permisos ([[cierre-de-ronda]]).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Los tests pasaron, hago commit sin documentar" | Verificar, documentar, memoria y commit van en ese orden dentro de la misma ronda. |
| "El cierre incluye el push" | El push solo se hace si fue autorizado para esa rama y remoto. |

## Errores comunes
- Informe que dice "listo" en vez de separar lo verificado de lo no verificado.
- Commit que mezcla cambios ajenos.

## Verificación
- Las comprobaciones corrieron y se mostró su salida; la bitácora y la memoria tienen la ronda; el informe separa verificado y no verificado.
