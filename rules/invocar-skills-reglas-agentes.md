# Skills, reglas y agentes se invocan por ÁREA, sin esperar a que "parezca necesario"

> Aplica a: todo proyecto (el mapa área→skill/regla/agente es plantilla: lo define cada proyecto). Reglas relacionadas: [[subagentes-max-3-y-verificar]], [[leer-y-responder-cada-mensaje]], [[cierre-de-ronda]], [[no-asumir-separar-confirmado]].

Antes de tocar código o documentación de un área que tiene skill, regla o agente dedicado, se invoca la skill, se aplica la regla y, si se delega, se usa el agente de esa área. Invocar de más cuesta poco; no invocar cuando aportaba cuesta el resultado. Ante la duda, se invoca.

## Por qué
Se midió: de decenas de skills instaladas casi ninguna se invocó nunca, y cientos de delegaciones fueron al agente genérico y cero a los especializados (sus definiciones ni siquiera eran descubribles). Una skill, regla o agente que existe pero no se usa da falsa confianza ("ya está cubierto"). Un aviso que llega cuando ya se decidió hacer el trabajo uno mismo, o que se repite hasta volverse ruido, tampoco cambia la conducta.

## Cómo se aplica
- **Al empezar** una tarea real (no una pregunta puntual), identificar el área tocada (capa, lenguaje, plataforma) y consultar el mapa del proyecto: skill principal **antes** de escribir código, no tras el primer error.
- **Skill**: invocarla de verdad y leer su archivo de instrucciones (`SKILL.md` u homólogo) completo, aplicando sus compuertas; citarla no cuenta. Si la herramienta no la expone, leer el archivo directamente y decir que fue consulta manual.
- **Regla**: el trabajo debe ser coherente con ella y se comprueba al cerrar. Leerla sin cumplirla no cuenta; una regla aplicable no seguida es un fallo de proceso, no un detalle.
- **Agente**: si hay uno dedicado al tipo de tarea, se delega en él y no en un prompt genérico que reinvente su checklist peor. Un archivo de agente no prueba que la herramienta lo haya descubierto: comprobarlo. Respeta [[subagentes-max-3-y-verificar]]. Cada agente se usa dentro de su alcance y de sus herramientas declaradas: uno de solo lectura o de QA no edita código.
- **Dominio primero**: entre las skills del área, las del dominio del proyecto van antes; las técnicas genéricas se suman después (en una medición, casi todas las que nadie invocaba eran técnicas genéricas).
- **Capacidad inexistente o no disponible**: declarar el hueco, trabajar con el mejor método verificable y nunca decir que se invocó lo que no se invocó. Los huecos del mapa se anotan como tales, no se inventa cobertura.
- **El aviso llega en el momento útil**: al leer el mensaje y al delegar (no solo al editar). Si hay hooks, informan una vez por área y sesión y no bloquean. Un hook de aviso entrega su texto como **contexto adicional** para el modelo, sin emitir decisión de permiso: el motivo de una decisión de permiso no lo lee el modelo, y aprobar una edición (con "allow" o su equivalente) autoriza solo esa edición.
- **Cada cosa en su área**: no cargar ni aplicar material ajeno a la tarea (el contexto es limitado y una guía fuera de lugar produce errores). Si una tarea cruza dos áreas, usar ambas y decirlo; si se usa algo fuera de su área por necesidad, declararlo.
- **Una skill no reemplaza las reglas**: las reglas mandan. Si una skill resulta desactualizada al usarla, se corrige en el momento.
- **Piezas nuevas nacen con su área**: toda skill, regla o agente nuevo se añade al mapa en la misma ronda, con una descripción que empiece por "Usar cuando… en <área>"; las reglas de área declaran qué archivos las activan (si la herramienta lo permite, p. ej. `paths:` en Claude Code), para cargarse solo al tocar esos archivos (las de conducta y seguridad no); lo que nadie invoca se archiva (mover, no borrar). Idealmente una prueba automática exige que todo lo existente figure en el mapa y que todo lo referenciado exista.
- **No instalar, copiar ni adaptar** skills, reglas o agentes adicionales sin autorización: se muestra la lista propuesta y el motivo ([[leer-y-responder-cada-mensaje]]).
- **Al cerrar una ronda grande**, confirmar que las skills, reglas y agentes del área se usaron; si no, es un hallazgo a corregir. Medir periódicamente (invocaciones por skill, delegaciones por tipo de agente) para detectar el patrón "todo al genérico, nada a lo especializado".

## Ejemplos
- No: editar el módulo de pagos sin abrir su skill porque "ya sé cómo va"; delegar una prueba de pantalla a un agente genérico existiendo `qa`.
- Sí: "Área: base de datos. Invoco `<skill de datos>`, aplico `<regla de datos>` y delego la revisión al agente `db`."
- No: "La skill X cubre esto" sin haberla leído.

## Qué se ajusta por proyecto
- El **mapa área → skills / reglas / agentes** (ruta o patrón, y qué se invoca), con su archivo y quién lo mantiene. Este archivo no contiene ninguno.
- Mecanismo de aviso (hook al leer el mensaje, al editar, al delegar) y la prueba que valida el mapa.
- Qué skills están archivadas y cómo se reactivan; criterio y cadencia para archivar las que no se usan.
- Qué se considera hueco conocido (áreas sin skill dedicada).
