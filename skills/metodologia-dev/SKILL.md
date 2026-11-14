---
name: metodologia-dev
description: "Usar cuando se planifica una funcionalidad con especificación previa, se escriben specs, changelog o documentación, se diagnostica un bug difícil, se revisa un cambio ya implementado o se resuelven conflictos de merge. Aporta la metodología de desarrollo: spec primero, convenciones de commits, ADR y protocolo de depuración."
---

# metodologia-dev

Metodología de desarrollo: flujo con spec primero, changelog, plantillas de documentación y convenciones de git.
Usar cuando se planifican funcionalidades, se escriben especificaciones, se generan changelogs o se crea documentación.

---

## Flujo spec primero
### Ley de hierro
**NINGÚN CÓDIGO SIN UNA SPEC APROBADA.** Escribir la especificación antes de implementar.

### Flujo en 6 fases
1. Reunir requisitos → entender las necesidades y restricciones del usuario
2. Escribir la spec → formato de 9 secciones (título, contexto, requisitos funcionales, no funcionales, criterios de aceptación, casos límite, contratos de API, modelos de datos, fuera de alcance)
3. Validar la spec → revisarla con criterios de aceptación Given/When/Then (Dado/Cuando/Entonces)
4. Generar pruebas → escribirlas a partir de la spec antes de programar
5. Implementar → programar hasta que pasen las pruebas, con autonomía acotada
6. Autorrevisión → contrastar con la spec, ejecutar las pruebas y revisar los casos límite

### Formato de la spec
- **Contexto**: ¿por qué se construye esto? ¿qué problema resuelve?
- **Funcional**: historias de usuario con las palabras clave RFC 2119 (MUST, SHOULD, MAY)
- **Aceptación**: formato Given/When/Then
- **Casos límite**: estados vacíos, errores, límites, acceso concurrente
- **Contratos de API**: endpoints, esquemas de petición y de respuesta
- **Modelos de datos**: tablas, columnas y relaciones nuevas o modificadas

## Convenciones de commits
- Formato: `tipo(ámbito): descripción` (Conventional Commits)
- Tipos: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `style`, `perf`
- `feat:` → changelog, sección "Añadido"
- `fix:` → changelog, sección "Corregido"
- `refactor:` → changelog, sección "Cambiado"
- Idioma: commits y documentos en **español**; código en **inglés**

## Changelog
- Actualizar `CHANGELOG.md` al terminar cada tarea
- Formato: Keep a Changelog, con encabezados de versión
- Generarlo a partir de los commits convencionales cuando sea posible
- Secciones: Añadido, Corregido, Mejorado, Técnico

## Plantillas de documentación
- **README**: secciones prioritarias — descripción, instalación, uso, API
- **Documentación de API**: plantilla por endpoint con método, ruta, autenticación, petición y respuesta
- **ADR** (registros de decisiones de arquitectura): contexto, decisión, consecuencias
- **Orientada a IA**: llms.txt, documentación lista para MCP, metadatos estructurados
- Documentos del proyecto en español; comentarios de código en inglés, lo mínimo necesario

## Protocolo para bugs (diagnóstico riguroso, no solo "encontrar y parchar")
1. **Construir un ciclo de retroalimentación corto ANTES de teorizar** — si reproducir o verificar tarda minutos por vuelta, invertir primero en acortar ese ciclo (un script mínimo, un log con etiqueta única, una prueba aislada) en vez de iterar teorías sobre un ciclo lento.
2. **Generar 3-5 hipótesis ordenadas por prioridad y refutables**, no una sola — cada hipótesis debe tener una forma concreta de confirmarla o descartarla, no ser solo una corazonada.
3. **Reproducir primero** — no corregir sin confirmar el bug de verdad (leer el código, no suponer por el síntoma reportado).
4. **Encontrar la causa raíz**, no el síntoma — si el arreglo es "agregar un `if` especial", probablemente no es la causa raíz.
5. **Etiquetar los logs de depuración temporales** con un marcador único (p. ej. `[DEBUG-pagos-0728]`) para poder limpiarlos después sin tener que adivinar cuáles borrar.
6. **Si no existe un punto de inserción correcto para la prueba de regresión, esa ausencia ES el hallazgo** — a veces el bug revela que el código no tiene un punto testeable; documentar esa brecha arquitectónica en vez de solo parchar alrededor.
7. **Documentar el "antes" si el cambio es grande** (ver la plantilla de snapshot pre-cambio más abajo).
8. Escribir la prueba que **habría atrapado el bug**, no una genérica — si el bug fue un nombre de prueba duplicado, la prueba de regresión debe verificar que ambas pruebas corren, no solo que el código "funciona".

## Evidencia graduada al investigar bugs difíciles
Complementa el protocolo anterior (paso 2, hipótesis ordenadas): además de ordenarlas, graduar cada hallazgo según qué tan sólido es, en vez de tratar todo como hecho confirmado:
- **Confirmed** — observado directamente (cita `archivo:línea`, log o commit concreto).
- **Deduced** — se sigue lógicamente de evidencia Confirmed (mostrar la cadena de razonamiento).
- **Hypothesized** — plausible pero sin confirmar (decir qué evidencia la confirmaría o refutaría).
- **Ancla primero**: partir de UN hallazgo Confirmed y expandir desde ahí — nunca partir de una teoría para buscar solo la evidencia que la sostiene. Preferir la explicación más simple y menos exótica.
- **Refutación activa antes de confirmar**: antes de pasar una hipótesis a Confirmed, buscar primero evidencia que la refute, no solo la que la sostiene.
- Una hipótesis descartada no se borra: se marca como refutada, con la razón. El camino equivocado también es información útil para la próxima sesión.

## Revisión adversarial en 3 capas
Para revisar un cambio de código ya implementado (complementa, no reemplaza, el punto 8 del protocolo sobre la prueba de regresión). Lanzar 3 revisores en paralelo (ver "Auditoría multi-agente en paralelo" más abajo), cada uno con un rol distinto y deliberadamente ciego a lo que ven los demás:
- **Blind Hunter** — recibe SOLO el diff, sin contexto del proyecto ni de la spec. Busca bugs a ciegas, sin dejarse influir por la intención declarada del cambio.
- **Edge Case Hunter** — recibe el diff y acceso de lectura al proyecto. Recorre cada rama y condición límite del código tocado (nulos, vacíos, concurrencia, límites) buscando casos no manejados.
- **Acceptance Auditor** — recibe el diff y la spec o criterio de aceptación original (si existe). Verifica que el código cumpla lo que pedía la spec, no solo que "funcione".

Al final, triage de los tres resultados juntos: deduplicar los hallazgos repetidos entre revisores y clasificar cada uno como **patch** (corrección sin ambigüedad), **decision_needed** (requiere una decisión humana, no se puede parchar solo), **defer** (real pero preexistente, no es de este cambio) o **dismiss** (ruido o falso positivo, se descarta).

## Glosario vivo de dominio y decisiones descartadas
Un dominio con términos ambiguos genera confusiones que se repiten de sesión en sesión (por ejemplo, dos nombres para la misma entidad, o si un módulo debe eliminarse) hasta que alguien las resuelve. Dos hábitos que lo evitan:
- **Cuestionar un término ambiguo en el momento en que aparece**, no dejarlo pasar — si dos personas (o dos sesiones) podrían entender "Variante" de forma distinta, es señal de definirlo ya, no después.
- **Registrar por qué se descartó una opción**, no solo qué se decidió — cuando una propuesta se rechaza (p. ej. "no generalizar Vehicle como módulo pluggable todavía"), dejar la razón en el documento de arquitectura correspondiente para no volver a proponerla sin saber por qué no se hizo.

## Vocabulario de diseño de módulos
Para decisiones de arquitectura o de servicios (no solo nombrar archivos, sino cómo repartir responsabilidades):
- **Módulo profundo vs superficial**: un módulo "profundo" tiene una interfaz simple que oculta bastante complejidad interna (p. ej. un servicio de inventario con una sola función `reponer()` que resuelve la concurrencia por dentro); uno "superficial" expone casi toda su complejidad en la interfaz. Preferir profundizar antes que fragmentar en funciones pequeñas que no reducen la complejidad real.
- **Seam** (costura): el punto donde el código puede interceptarse, probarse o reemplazarse sin tocar el resto (p. ej. un proveedor de pagos intercambiable detrás de una interfaz es una costura bien puesta).
- **Escaneo proactivo de oportunidades de profundizar**: de vez en cuando, y no solo cuando ya duele, revisar si algún módulo se volvió superficial con el tiempo. Candidatos naturales: archivos que superan unas ~400 líneas (límite de la regla de archivos grandes, si el proyecto la declara).

## Grilling — interrogatorio socrático para decisiones grandes
Cuando una sola persona decide, nadie hace de abogado del diablo antes de comprometerse con un plan grande. Antes de aprobar una migración de arquitectura o una propuesta grande (ver también el Pre-Mortem más abajo), hacer una ronda de preguntas de una en una, cada una atacando un punto débil concreto del plan ("¿qué pasa si X ya tiene datos reales cuando corra esto?", "¿por qué esta opción y no la más simple?"). No son preguntas genéricas: son específicas del plan que está sobre la mesa. Complementa al Pre-Mortem: este imagina el fracaso ya ocurrido; el Grilling presiona el plan ANTES de que exista una versión final.

## Handoff — traspaso de contexto entre sesiones
Cuando una tarea en curso va a seguir en otra sesión o con otro agente (no solo un hallazgo puntual para la memoria), compactar el estado en un documento de traspaso: qué se pidió, qué se decidió, qué falta y cualquier información que se perdería si solo se leyera el código. Complementa la memoria del proyecto y no la reemplaza: el traspaso sirve para una tarea completa en curso; la memoria, para observaciones puntuales ya cerradas.

## Snapshot pre-cambio (plantilla)
Antes de un cambio de arquitectura grande, congelar el estado exacto previo en `docs/referencia/{area}-snapshot-v{version}-{fecha}.md`. Este archivo no se actualiza después: es una foto fija; el estado actual vive en `docs/arquitectura/`. Secciones obligatorias:
- **Por qué se cambió** — el problema concreto que el estado anterior no resolvía
- **Modelo de datos antes** — tablas, columnas y relaciones tal como estaban
- **Puntos de llamada** — qué código leía y escribía ese modelo
- **Brecha que exponía** — qué fallaba o era frágil, con precisión

## Convención de IDs y ciclo de vida de hallazgos de auditoría
Cada ronda de auditoría genera hallazgos con un prefijo (`B`/`F`/`G`/`S` del catálogo original; `SEC-XX`/`NEW-XX` para hallazgos posteriores a la auditoría). Viven en tres documentos con roles distintos:
- `docs/operaciones/audit-status.md` — histórico, instantánea de una ronda concreta con el % de resolución por área
- `MEJORAS_PENDIENTES.md` — activo, lo que sigue pendiente hoy
- `CHANGELOG.md` — lo que ya se resolvió, con su versión

Al cerrar un hallazgo, marcarlo en los tres lugares (no solo tacharlo en `MEJORAS_PENDIENTES.md`) para que el histórico no quede desincronizado con el estado real.

## Expand-contract para refactors mecánicos de gran alcance
Para cambios que tocan muchos puntos de llamada (renombrar un campo compartido, o cambiar el tipo de un símbolo usado en decenas de lugares, como renombrar un identificador en un modelo central), dividir en tres pasos verticales en vez de un solo commit gigante:
1. **Expand**: agregar el campo o columna nuevo sin tocar el viejo; doble escritura temporal si hace falta.
2. **Migrar lectura y escritura** punto por punto, con pruebas de regresión en cada paso.
3. **Contract**: eliminar el campo viejo solo cuando el paso 2 esté completo y estable.

Cada paso es pequeño y reversible; no hace falta llegar al paso 3 de inmediato si el costo no lo justifica todavía.

## Exploración del repositorio (antes de tocar código desconocido)
- `git log --oneline -20` y `git blame` sobre el archivo antes de suponer por qué está escrito así.
- Buscar convenciones ya establecidas (`grep` de patrones parecidos) antes de inventar una nueva.
- Revisar `docs/screens/*.md` y `docs/arquitectura/*.md`: puede que ya exista documentación del área que se va a tocar.

## Pre-Mortem para decisiones grandes
Antes de una migración de arquitectura grande (p. ej. un cambio de modelo de datos): preguntar "si esto sale mal dentro de tres meses, ¿por qué habrá sido?". Sirve para encontrar el riesgo que no se está viendo, antes de comprometerse. Es coherente con la regla de no iniciar migraciones arquitectónicas grandes sin consultar antes.

## Auditoría multi-agente en paralelo
Para revisiones grandes (auditoría de seguridad, análisis de una colección grande de archivos o skills), lanzar varios agentes en paralelo, cada uno con un lote acotado y el mismo criterio de clasificación, y sintetizar sus resultados en un solo informe. Es preferible a un solo agente que lee todo en secuencia cuando el volumen es grande y los lotes son independientes entre sí.

## Resolución de conflictos de merge
Resolver siempre por la intención original de cada cambio en conflicto: leer qué problema resolvía cada lado, sin quedarse con "el más reciente" ni con "el más largo". Nunca usar `git merge --abort` para evitar decidir: si el conflicto es confuso, hay que pausar y entender ambos cambios, no descartar uno a ciegas. Tras resolverlo, correr la suite de pruebas completa; que ya no queden marcadores de conflicto no significa que el código esté bien.
