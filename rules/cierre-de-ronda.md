# Cada ronda con resultado real se cierra con docs, memoria, verificación e informe

> Aplica a: todo proyecto. Reglas relacionadas: [[usuario-declara-listo]], [[verificacion-empirica]], [[secretos]], [[documentar-en-vivo]], [[bitacora-humana]], [[publicar-solo-con-orden]], [[seguridad-despliegue-y-datos]], [[archivos-protegidos]].

Al terminar una tarea, tanda o sesión que produjo un resultado real, el cierre es una orden permanente: no hace falta que el usuario lo pida en cada mensaje. Orden fijo: verificar, documentar, guardar memoria, commit (y push solo si está autorizado) e informe en pantalla.

## Por qué
Sin cierre fijo, cada sesión nueva reconstruye el contexto leyendo código, y el usuario repite la misma orden en cada turno. Un cierre que solo dice "listo" oculta lo no verificado.

## Cómo se aplica
1. **Verificar el efecto, no la invocación**, con pruebas proporcionales al riesgo ([[verificacion-empirica]]). Un fallo impide hablar de cierre correcto, pero no obliga a esconder el avance ni a borrar cambios.
2. **Documentar** lo que el cambio toca: el documento vigente afectado, el changelog, los índices, los pendientes que se abren o cierran. Corregir el doc desfasado en la misma ronda, no "la próxima". **Bitácora al día** (si el proyecto lleva bitácora humana): comprobar que el mensaje del usuario de esta ronda está registrado con su interpretación completa ([[bitacora-humana]]); sin eso no hay cierre. Los **artefactos entregables** vigentes se reconstruyen; si uno no se pudo, se declara desactualizado y no se presenta como vigente, ni se publica una versión parcial como final.
3. **Memoria**: guardar solo lo durable (decisiones, hallazgos que otra sesión necesitaría, lecciones); nada que se deduzca del código ni secretos.
4. **Commit** solo de lo propio: revisar diff y alcance, escanear secretos de lo que entra ([[secretos]]), mensaje técnico y específico, sin enlaces ni correos ([[commits-tecnicos-sin-enlaces]]), `git add` por nombre. Nunca mezclar cambios ajenos. No se hace commit si las verificaciones relevantes fallan o si el usuario pidió solo análisis.
5. **Push solo si el proyecto o el usuario lo autoriza** para esa rama/remoto (ver [[publicar-solo-con-orden]]). Una autorización de push a una rama no se extiende a otra, a repos públicos, release ni despliegue. Si el push falla, informar el estado exacto; no decir que quedó publicado. Nunca `--no-verify` ni `--force`.
6. **Informe en pantalla** (no solo un archivo): lo hecho, lo verificado y lo no verificado por separado, pendientes, opinión honesta y siguiente plan con propuestas concretas. Nunca "listo": lo declara el usuario ([[usuario-declara-listo]]).
7. **No hay cierre** si la ronda fue una pregunta, opinión o auditoría solo lectura, o no produjo trabajo real: ni escrituras, ni commit, ni push.
8. El cierre **no amplía permisos**: despliegue, migraciones, operaciones con dinero, borrados destructivos y archivos protegidos conservan su propia autorización. Un commit solo de documentación no se despliega.

## Cuando se piden opinión, propuesta o plan (o el tema es grande y ambiguo)
- La respuesta **termina** con: (a) opinión completa y honesta; (b) plan por fases y puntos numerados (qué, quién lo ejecuta, esfuerzo, impacto y riesgo de cada propuesta, qué queda sin tocar); (c) decisiones que se necesitan del usuario; (d) esperar su luz verde.
- Plan y preguntas van **en el texto de la respuesta**, nunca solo en un archivo; el archivo con el detalle es complemento, con una línea final que indique dónde está.
- No ejecutar el plan ni piezas de él mientras se espera. Una luz verde parcial cubre solo esa parte.
- Hallazgos laterales: una línea al final; no reemplazan el plan.

## «Haz todo» significa todo
- «Haz todo», «sigue con todo», «lo que falta» = todo el backlog pendiente, no el trozo que el agente elija. No se cierra con "el siguiente paso sería…" ni se pide permiso para continuar.
- Las únicas paradas permitidas son los puntos de cierre (docs, memoria, commit, y push si está autorizado); tras cada uno se continúa de inmediato.
- Se termina cuando el backlog está hecho o cada ítem restante tiene un **bloqueo real y demostrado** (recurso externo, decisión que solo el usuario puede tomar, riesgo de dinero o credenciales), con evidencia.
- «Todo» no concede permisos nuevos ni salta archivos protegidos, secretos o verificación.

## Ejemplos
- No: terminar con "listo, todo subido" sin pruebas, o hacer push a un remoto no autorizado porque "el cierre lo incluye".
- No: entregar solo un enlace a un `.md` con el plan y las preguntas.
- Sí: "Hecho: X (probado con Y). No verificado: Z. Opinión: … Plan: 1) … 2) … Necesito que decidas: …".

## Qué se ajusta por proyecto
- Qué documentos, índices, changelog y ubicación de memoria se actualizan.
- Rama(s) y remoto(s) donde el commit y el push están autorizados (o que el push exige orden explícita).
- Verificaciones mínimas del cierre (pruebas, linters, build) y qué se despliega o no.
- Formato del mensaje de commit.
