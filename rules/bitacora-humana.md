# Bitácora humana: el mensaje textual del usuario y la interpretación, por lotes

> Aplica a: todo proyecto con un dueño humano que da instrucciones. Relacionadas: [[documentar-en-vivo]], [[secretos]], [[leer-y-responder-cada-mensaje]], [[docs-organizacion-y-fechada]], [[cierre-de-ronda]].

El proyecto lleva una **bitácora humana** (archivos numerados) donde cada archivo guarda, para un lote de **6 a 9 mensajes** del usuario: su **cita textual** y la **interpretación** del asistente. Sirve para volver a leer *qué pidió* y *cómo se entendió*, y detectar si no coincidían.

## Por qué
Sin la cita, el archivo cuenta lo que se hizo pero no contra qué se mide. Sin registro en el momento, una sesión futura (u otra máquina) no encuentra decisiones, correcciones ni autorizaciones, y repite trabajo ya hecho. Los informes en "lenguaje llano" sin cita textual se fueron imponiendo por inercia y perdieron justo lo que el archivo debía conservar.

## Lo que lleva cada archivo
```markdown
# <Fecha> — tema, tema y tema          (rango de fechas y "mensajes N–M")

## 1. Título corto del tema
**Lo que pidió:** *"cita textual, tal cual la escribió, con sus erratas"*
**Cómo lo entendí:** la lectura que hice y qué decidí. Si había más de una lectura posible, cuál elegí y por qué.
Detalle: qué cambió, números medidos, cómo sé que está bien (no "porque el programa dijo listo"), límites y vínculos.

## 2. ...
```
Las cuatro cosas que no se negocian:
1. **La cita va textual**, con erratas y sin "arreglarla". Es lo que dijo, no lo que creo que quiso decir.
2. **"Cómo lo entendí" va aparte de la cita**, siempre. Es la parte que permite descubrir un malentendido.
3. **De 6 a 9 puntos por archivo**, numerados. Con menos de 6 el lote sigue **abierto** y se sigue ampliando el mismo archivo; con más de 9 se abre el siguiente número. Se cuentan mensajes del usuario, no turnos del asistente ni notificaciones automáticas.
4. **Un punto por tema.** Si el mensaje traía ocho cosas, son ocho puntos, no uno titulado "varios ajustes".

Además se conserva: lenguaje llano (sin jerga que el dueño no lee), números medidos en bloque, y **lo que quedó sin hacer** dicho con esas palabras.

## Cuándo y cómo se escribe
- **En el momento:** cada mensaje con una orden, decisión, corrección o autorización se anota en el lote abierto al procesarlo, no al cerrar la ronda. Un "sí, entendido" se consolida con el mensaje anterior o siguiente. Un arreglo de una línea no necesita archivo propio.
- **Carpeta y nombre:** el proyecto fija la carpeta (por ejemplo **`docs/humano/`**) y los lotes se llaman **`humano1.md`, `humano2.md`, `humano3.md`…** (número consecutivo, sin ceros y **sin tope**; cada archivo es un lote de 6 a 9 mensajes). Sin saltarse ninguno; nunca se sobrescribe un archivo existente. La **fecha va dentro** del archivo (línea `**Fecha:**` al inicio), no en el nombre.
- **Un `INDEX.md`** en la carpeta explica el propósito y lista los lotes.
- **Los hallazgos técnicos** confirmados se propagan además a la memoria persistente y a su documento técnico: la bitácora aporta contexto, **no reemplaza** requisitos, arquitectura ni evidencia de QA.

## Qué NO se hace
- **No se corrige un archivo viejo.** Es una foto con fecha: así se entendió ese día, incluso si se entendió mal. Lo que cambió va en el archivo nuevo, que enlaza al anterior. *(Un lote abierto sí se puede completar.)*
- **No se inventa una cita.** Si el pedido fue verbal o quedó implícito: *"no lo dijo con estas palabras; lo entendí de…"*.
- **Nunca se transcribe un secreto ni datos financieros reales**, ni citando al usuario. "Textual" no significa "con la clave en texto plano". Se reemplaza por `<REDACTADO-fecha — descripción>` y el resto queda tal cual. Es la **única** excepción a "no editar un archivo ya escrito": si se detecta un secreto en uno ya commiteado, se redacta apenas se encuentra y se avisa para rotarlo ([[secretos]]).
- **Un subagente no crea archivos de bitácora.** No ve la conversación real: su "mensaje del usuario" sería el prompt de delegación del hilo principal, atribuido mal. Lo decide y escribe el hilo que tiene la conversación. Si un agente lo hizo, se corrige la procedencia con una nota corta al inicio, sin reescribir el resto.

## Qué se ajusta por proyecto
- La carpeta (por ejemplo `docs/humano/`) y el nombre `humanoN.md` se fijan una vez por proyecto. Solo si dos sesiones escriben a la vez y chocan, una serie paralela en una subcarpeta (`docs/humano/<serie>/humano1.md`) con su propia numeración.
- Tamaño de lote si el dueño fijó otro distinto de 6 a 9.
- Si el proyecto lleva una bitácora por ronda en lugar de por lote de mensajes, el dueño lo declara en una regla local.
