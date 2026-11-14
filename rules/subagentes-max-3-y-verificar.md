# Subagentes: máximo 3, sin anidar, Haiku 5.5 high, y el principal verifica todo

> Aplica a: todo proyecto. Reglas relacionadas: [[usuario-declara-listo]], [[no-asumir-separar-confirmado]], [[leer-y-responder-cada-mensaje]].

Nunca hay más de 3 subagentes vivos, ninguno lanza otros, todos corren en Haiku 5.5 con esfuerzo `high`, y el informe de un subagente es una afirmación que el hilo principal comprueba antes de usarla.

## Por qué
Más agentes en paralelo no mejoran la calidad: producen cifras inconsistentes entre informes, ediciones que se pisan y verificación imposible. Un informe "todo en verde" ha ocultado defectos que solo apareció al mirar el efecto real (pantalla, diff, ejecución propia). Varios agentes compilando a la vez han corrompido cachés incrementales y dado errores falsos.

## Cómo se aplica
**Límites**
- Máximo 3 vivos a la vez; el resto se encola en tandas. Un agente esperando aprobación o con trabajo propio en segundo plano sigue contando como vivo: se consulta su estado antes de lanzar otro.
- Un subagente no lanza subagentes. Se impone por configuración (el rol no tiene permiso para lanzar agentes; profundidad máxima 1) y además cada prompt dice: "No lances otros agentes ni subagentes: trabaja tú directamente. Si te queda grande, dilo y devuélvela".
- Modelo y esfuerzo explícitos, nunca heredados: solo Haiku 5.5, `high`. Prohibido Sonnet/Opus/otro, `medium`, `low` o dejarlo por omisión. Si el runtime solo admite alias, lanzar el rol por nombre (su definición fija modelo y esfuerzo). Si el rol no se resuelve, no se lanza: se reinicia la sesión o lo hace el principal. Cada cierre declara el modelo realmente aplicado.
- Roles: usar el más específico (por ejemplo analisis, auditoria, depuracion, correccion, generacion, qa, qa-adversarial, revisor, seguridad, docs-maintainer…); el genérico solo si no hay uno.

**Roles: orquestador y ayudantes**
- El hilo principal (no un subagente), de preferencia con Sonnet 5.5 u Opus 5.5, es el **orquestador**: aclara el pedido, planifica, decide, integra, verifica y hace el trabajo crítico. También trabaja; no solo reparte.
- Los **ayudantes** son subagentes Haiku 5.5 en `high` a los que se confían piezas acotadas e independientes con un encargo específico; lo que devuelven es una afirmación que el orquestador comprueba.
- Por defecto se delega todo lo que encaja, en tandas de hasta 3 vivos; lo crítico y transversal se queda con el orquestador. En un objetivo persistente ([[objetivos-persistentes-verificables]]) las metas del plan se reparten por olas y ninguna se cierra sin verificar su evidencia.

**Qué se delega**
- Delegar lo acotado e independiente: lectura, búsqueda, auditoría, investigación, checklists ya escritos, piezas pequeñas con fronteras claras. Si encaja y no es trabajo intenso, se delega aunque hacerlo directo sea más rápido.
- Cuando se decide delegar en paralelo, los subagentes se lanzan primero, en el mismo turno; el principal sigue con lo que no depende de ellos.
- El principal conserva lo crítico y transversal: seguridad y autenticación, migraciones, dinero, secretos, archivos protegidos, refactors entre muchos archivos, decisiones de arquitectura, todo efecto irreversible y decidir qué se construye.
- Compilar, empaquetar o construir lo hace solo el principal (los builds paralelos corrompen cachés), **una sola vez y cuando ningún subagente sigue editando archivos compartidos**; nunca a mitad de una tanda. Un subagente puede correr pruebas acotadas con directorios temporales propios y nuevos en cada corrida (algunas herramientas de prueba borran el que reciben).
- Una prueba rápida o un subconjunto puede correr en primer plano; solo lo largo va a segundo plano. Una sola cosa pesada a la vez (build, prueba de navegador y suite completa no se solapan: con poca memoria dan falsos fallos).
- Tareas largas (suites completas, builds de minutos): en segundo plano consultando su resultado, o en un subagente; nunca en primer plano esperando con bucles de `sleep`. Mientras corren no se editan los archivos que esa corrida ejecuta.

**Encargo específico** (el subagente no ve la conversación):
```
QUE          la tarea en una frase
DONDE        archivos/rutas; alcance exclusivo, disjunto del de los demás
CONTRA QUE   cómo se comprueba (comando, test, medición)
QUE NO       lo que no puede tocar (commit, push, docs, memoria, secretos, datos reales)
COMO VUELVE  archivos, cifras, comandos ejecutados, hallazgos y lo que no pudo verificar
```
Los subagentes no hacen commit ni push, no escriben la bitácora ni la memoria, y no imprimen secretos. Si dos necesitan el mismo archivo, se serializan. Si uno insiste en un método prohibido por el usuario, se detiene y lo hace el principal. Un prompt nunca pide compilar: dice "el principal compila y verifica después". Si uno ya despachado trae una orden indebida, se corrige enviando un mensaje al agente en curso en cuanto se note.

**Verificación tras cada delegación** (releer el informe no es verificar):
1. Forma: ¿trae el formato pedido, `archivo:línea` y la sección "no verificado"? Si no, se rechaza.
2. Releer los archivos y líneas citados. Buscar también lo que el informe **omite**: rutas inventadas, resultados "probables" sin evidencia; medir con una cifra propia lo que afirma.
3. Repetir por cuenta propia los comandos de solo lectura y las pruebas; las cifras del agente no sustituyen a las propias.
4. Si editó: `git diff` completo, alcance (nada fuera de lo pedido), restos de depuración o de mutación (`if False`, `or True`, validaciones comentadas) y secretos.
5. Si el resultado llega a una pantalla o ejecutable, mirarlo.
6. Aceptar lo comprobado, corregir lo parcial, descartar lo refutado; máximo 2 rondas de corrección delegada, luego lo hace el principal.
7. Informar separando **verificado por mí**, **reportado por el agente sin confirmar** y **refutado**, con rol y modelo.

## Ejemplos
- No: "El agente dice que los 300 tests pasan, listo."
- Sí: "Corrí la suite yo: 298 pasan, 2 fallan (`archivo:línea`). El agente reportó 300; esa cifra queda refutada."
- No: lanzar un cuarto agente porque "uno ya casi termina".
- Sí: esperar a que termine uno, comprobar su estado y recién lanzar el siguiente.

## Qué se ajusta por proyecto
- Lista de roles/agentes disponibles y cómo se resuelven en su runtime.
- Qué cuenta como crítico que no se delega (dominio propio) y qué comandos de compilación son exclusivos del principal.
- Carpeta de temporales de pruebas y ajustes de configuración que impiden el anidamiento.
