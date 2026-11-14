# Lo que se repite se propone como pieza propia del proyecto; se crea solo con aprobación

> Aplica a: todo proyecto (cada proyecto decide qué piezas propias necesita). Reglas relacionadas: [[documentar-fallas]], [[memoria-del-proyecto]], [[invocar-skills-reglas-agentes]], [[leer-y-responder-cada-mensaje]], [[secretos]].

Cuando un proceso se repite, una falla vuelve o una instrucción se da más de una vez, el agente lo detecta y **propone** convertirlo en una skill, regla o agente propios del proyecto. Crea la pieza solo después de que el usuario apruebe esa propuesta.

## Por qué
Lo repetido que solo vive en la cabeza del usuario o en el chat se reexplica en cada sesión y se hace distinto cada vez. Pero crear piezas por iniciativa propia llenó proyectos de material que nadie pidió y que nadie invoca. El equilibrio es detectar y proponer, no construir en silencio.

## Cómo se aplica
- **Qué cuenta como señal**: el mismo proceso hecho a mano tres veces; una falla que vuelve por tercera vez ([[documentar-fallas]]); una corrección o instrucción del usuario repetida; un paso a paso largo que se reescribe en cada tarea; un documento plantilla que se copia siempre.
- **Qué pieza elegir** (la regla dice el QUÉ; la skill dice el CÓMO):
  - algo que **siempre** debe cumplirse → regla;
  - un procedimiento con pasos, plantillas o scripts → skill;
  - un rol de solo lectura con entregable fijo → agente.
  Si lo que se repite ya lo cubre una pieza del kit o del proyecto, se usa o se mejora esa; no se crea otra.
- **Detectar** al cerrar una ronda y al leer la memoria: buscar señales en `.memory/lecciones.md`, la bitácora y el historial reciente. Registrar la candidata en la memoria con `Estado: provisional`.
- **Proponer** en el texto de la respuesta, nunca solo en un archivo: qué se repite, cuántas veces y dónde (evidencia), qué pieza se crearía, nombre, a qué área pertenece y cuánto cuesta. Una propuesta por pieza; el usuario aprueba una a una.
- **Crear** solo lo aprobado, con la skill `crear-pieza-del-proyecto`: pieza **local** en el `.claude/` del proyecto, con descripción "Usar cuando…", sin secretos ni rutas de usuario, validada y registrada en el mapa de áreas ([[invocar-skills-reglas-agentes]]).
- **Lo local no sube solo**: si una pieza propia resulta servir a más proyectos, se propone al kit universal y se publica por el flujo del kit de piezas; no se copia a ojo.
- **Sin sorpresas**: una idea "a futuro" o una opinión no es aprobación. Rechazada una propuesta, se anota como `descartada` con el motivo para no volver a proponerla.
- **Cada pieza propia se mide**: si pasado un tiempo nadie la invoca, se archiva (mover, no borrar).

## Ejemplos
- No: ver el mismo despliegue a mano por cuarta vez y crear una skill de despliegue sin avisar.
- Sí: "El despliegue se hizo a mano 4 veces (bitácora 3, 5, 7 y 9) con los mismos 6 pasos. Propongo la skill `desplegar-<proyecto>` (área: infraestructura). ¿La creo?".
- No: una regla nueva por cada preferencia dicha una sola vez.

## Qué se ajusta por proyecto
- Umbral de repetición (por defecto tres veces) y dónde se buscan las señales.
- Carpeta de piezas locales y archivo donde se registran (mapa de áreas).
- Quién aprueba (el dueño del proyecto) y cómo queda registrada la aprobación.
