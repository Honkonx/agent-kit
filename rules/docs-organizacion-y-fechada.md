# Docs: un lugar por tipo, lo vigente se corrige y lo fechado no se toca

> Aplica a: todo proyecto con carpeta de documentación. Reglas relacionadas: [[documentar-en-vivo]], [[bitacora-humana]], [[cierre-de-ronda]], [[no-asumir-separar-confirmado]].

Cada documento va en la carpeta de su tipo. Hay dos clases opuestas: el documento **vigente** describe el sistema de hoy y se corrige contra el código; la **foto fechada** describe un momento y no se reescribe.

## Por qué
Corregir una foto fechada falsifica la historia (una auditoría dice lo que se vio ese día). Y un doc vigente viejo que parece mantenido es peor que uno ausente. Sin criterio de carpetas, las carpetas planas se vuelven ingobernables.

## Cómo se aplica
- **Vigente** (arquitectura, módulos, contratos, guías operativas, requisitos, instrucciones del proyecto): si envejece es un defecto; se actualiza in situ contra el código, en la misma ronda del cambio. Nombre por tema, con `**Última actualización:**` dentro y sin "decía X, ahora Y": la historia va al changelog o a un doc fechado.
- **Foto fechada** (bitácora de sesiones, auditorías, informes de QA, investigaciones, evaluaciones, planes cerrados, changelog, cada decisión registrada, memoria): no se toca el contenido. Si algo cambió, va en un documento **nuevo** (o en el vigente) enlazado al anterior. Se nombra **por su tema** (`auditoria-referencias.md`, `humano3.md`) y la **fecha va dentro del archivo**: una línea `**Fecha:** AAAA-MM-DD` al inicio, junto a `**Tipo:** foto fechada`. El nombre no necesita fecha.
- **Excepciones permitidas en una foto**: reparar una ruta/enlace que se movió, quitar un secreto, o anteponer una nota fechada ante un dato descubierto falso (indicando contra qué se verificó y cuándo).
- **Decisiones con estado** (`vigente | propuesta | superada por …`): lo superado se marca, no se borra.
- **Nunca se borra documentación**: lo obsoleto se mueve (con `git mv` si hay git, o el equivalente) a una carpeta de archivo con "Superado por …" al inicio. Antes de archivar, comprobar con búsqueda que ningún documento vigente (plan, pendientes, reglas) lo cita como fuente activa; si lo cita, no se mueve.
- **Carpetas temáticas**: al nivel superior de `docs/`, mono-tema, creadas cuando exista contenido real (no "para llenar"); sin pedir permiso para el nombre. Cada carpeta tiene un README con qué hay, qué va, qué NO va y su tipo (vigente o foto).
- **Un doc fuente por decisión**; los demás lo enlazan, sin copias divergentes.
- **El estado para retomar es un único bloque**, reescrito cada sesión, en vez de varios "retomar" sueltos que envejecen.
- Una carpeta con más de ~5 documentos lleva índice; sin anidar más de 2 niveles. Los documentos de referencia generados del código se regeneran con su script y no se editan a mano.
- **Al mover o renombrar**, corregir todas las referencias cruzadas en la misma ronda y actualizar el índice general.
- **No escribir cifras a mano** (conteos de reglas, archivos, pruebas) en docs vigentes: sacarlas de un comando y fecharlas.
- **Cadencia de auditoría**: auditar la documentación **contra el código** (no contra otros docs) tras una tanda grande de cambios o, si no la hubo, cada 3 meses. El índice raíz lleva "Próxima auditoría: AAAA-MM-DD". Entre auditorías solo es obligatorio actualizar el doc que toca cada cambio.
- Idealmente una prueba automática revisa que los docs vigentes no citen archivos inexistentes; las fotos se excluyen por diseño.

## Ejemplos
- No: reescribir el informe de una auditoría antigua porque el hallazgo ya se arregló.
- No: crear `arquitectura_v2.md` paralelo en vez de editar el vigente.
- Sí: auditoría vieja intacta + doc nuevo "estado posterior" que la enlaza; o nota fechada arriba de una evaluación cuyo método resultó erróneo.

## Qué se ajusta por proyecto
- Las carpetas concretas y su criterio "qué va / qué NO va" (esto es plantilla; cada proyecto define su tabla).
- Cuáles carpetas son vigentes y cuáles son fotos fechadas.
- Nombre de la carpeta de archivo y del índice raíz, y la fecha de la próxima auditoría.
- Convención de nombres de bitácora y de fechados.
