# Una pieza lleva solo lo que necesita para funcionar: sin autor, fecha, licencia ni origen

> Aplica a: toda skill, regla o agente que se escriba o adapte. Reglas relacionadas: [[respuestas-concisas]], [[leer-y-responder-cada-mensaje]].

Las skills, reglas y agentes son texto que cualquiera puede escribir: dos personas llegan a las mismas instrucciones por caminos distintos. Por eso la pieza no lleva al principio nada que no cambie cómo se usa: ni "creado por", ni fecha, ni licencia, ni origen, ni versión. Cada línea de más es ruido que ocupa contexto.

## Por qué
Esos datos no ayudan a quien la usa ni al modelo, se desfasan y empujan a escribir de más. La historia de una pieza vive en los documentos del proyecto (bitácora, decisiones), no en la pieza.

## Cómo se aplica
- **Lo esencial y nada más:** cada línea de una pieza debe cambiar cómo se usa; si añade contexto sin beneficio, se quita. Lo mínimo: nombre y descripción ("Usar cuando…" en las skills y los agentes), más lo que la herramienta exija (por ejemplo `model` en un agente). Las reglas, su enunciado y "Aplica a".
- **Fuera de la pieza:** campos que ninguna herramienta lee (`license`, `compatibility`, `metadata`), autor, fecha de creación, licencia, procedencia, historial de cambios y avisos. Si hay que guardarlos, van en un documento aparte del proyecto, no al inicio de la pieza.
- **Una pieza de terceros** se adapta lo bastante para que sea propia: se reescribe con palabras propias, se recorta y se ajusta a nuestras reglas, de modo que parezca inspirada en la original y no una copia. Si no se logra, no se usa.
- **Piezas de un tema muy específico que no se puede hacer universal** (prácticas de un lenguaje, de una herramienta, de un dominio): antes de incorporarlas se pregunta al usuario; el foco son las piezas universales o que puedan serlo (la documentación, por ejemplo, suele poder serlo).
- **Subcarpetas de una skill** (`references/`, `scripts/`, `assets/`): solo las que el `SKILL.md` cita y explica cuándo abrir, a un solo nivel; un archivo que nadie nombra se quita.
- Esta regla no prohíbe un contexto corto que mejore la invocación (cuándo usarla y qué no cubre), solo lo que no cambia su uso.

## Ejemplos
- No: una skill que empieza con autor, fecha, versión y licencia antes de decir cuándo usarla.
- Sí: nombre, "Usar cuando…", y el contenido.

## Qué se ajusta por proyecto
- Qué campos exige su herramienta además del nombre y la descripción.
- Dónde guarda el proyecto la historia de sus piezas (bitácora, decisiones).
