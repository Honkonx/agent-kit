# Cada proyecto lleva una memoria durable en `.memory/` que cualquier sesión lee primero

> Aplica a: todo proyecto que se trabaje en más de una sesión, máquina o herramienta. Reglas relacionadas: [[documentar-en-vivo]], [[bitacora-humana]], [[docs-organizacion-y-fechada]], [[continuidad-multi-maquina]], [[secretos]], [[no-asumir-separar-confirmado]].

El proyecto guarda su **memoria durable** en una carpeta **`.memory/` en la raíz**: lo asentado que una sesión nueva necesitaría redescubrir (estado, decisiones, lecciones, preferencias). Es un **índice de contexto**, no la fuente de verdad: enlaza a los documentos y al código, no los duplica.

## Por qué
Una sesión nueva (u otra herramienta o máquina) no recuerda nada: sin memoria en el repo, redescubre lo mismo, repite errores ya corregidos o contradice decisiones tomadas. La memoria propia de cada herramienta no se comparte: lo único común es lo que está en el repositorio.

## Cómo se aplica
- **Carpeta y archivos fijos:** `.memory/` con `README.md` (índice), `PROJECT_STATE.md` (estado vigente y un **único** bloque `Para retomar`), `decisiones.md`, `lecciones.md` y `preferencias.md`. La skill `memoria-del-proyecto` trae las plantillas.
- **Qué entra:** hechos o decisiones **asentadas** y útiles más allá de la tarea actual; correcciones del usuario que no deben repetirse; fallas recurrentes y su arreglo; cómo prefiere trabajar el usuario en este proyecto. Breve y buscable: tema, estado, enlace a la fuente.
- **Qué NO entra:** secretos, claves ni tokens ([[secretos]]); datos personales innecesarios; registros financieros reales; transcripciones (eso es la [[bitacora-humana]]); lo que se deduce del código o del historial de git; lo que solo importa a esta conversación.
- **Cuándo se escribe:** en el momento en que se confirma un hallazgo, se toma una decisión o el usuario corrige algo ([[documentar-en-vivo]]), no al final. No se actualiza "porque hubo trabajo": solo si hay algo durable. Una ronda de solo análisis no escribe nada sin autorización.
- **Cuándo se lee:** al **empezar** una sesión real (junto con la última bitácora, ver `inicio-de-sesion`) y al retomar. Si algo de la memoria se va a usar como hecho, se **verifica** contra el código o el sistema antes ([[no-asumir-separar-confirmado]]): la memoria envejece.
- **Fecha y estado dentro de cada entrada**, no en el nombre del archivo: `Fecha`, `Estado` (`vigente`, `provisional`, `superada por …`). Lo provisional se marca como tal.
- **No se reescribe el pasado:** si una decisión cambia, la entrada vieja se marca `superada por <ID>` y se añade la nueva; una memoria que resulta falsa se corrige con una nota fechada.
- **Tamaño acotado:** cada archivo corto; si crece, se resume y el detalle va a un documento de `docs/`. Una sola fuente: la memoria enlaza, no copia.
- **Única fuente compartida:** si una herramienta guarda además su propia memoria privada, lo importante se refleja aquí; lo que solo vive en la memoria de una herramienta no existe para las demás.

## Ejemplos
- No: "Recordé que usamos X" (sin comprobar), o guardar la clave de un servicio "para no perderla".
- Sí: en `decisiones.md`: `D4 · Fecha 2026-11-13 · Decisión: los docs llevan la fecha dentro, no en el nombre · Por qué: … · Estado: vigente · Fuente: docs/…`.
- No: pegar la conversación completa en `PROJECT_STATE.md`. Sí: un bloque `Para retomar` de 5 a 10 líneas y enlaces.

## Qué se ajusta por proyecto
- Qué otros archivos temáticos se añaden (p. ej. glosario, mapa de integraciones) y su tope de tamaño.
- Si el proyecto espeja la memoria para otras herramientas (y cómo se comprueba que no divergen).
- Qué se considera "durable" en ese dominio y qué datos personales o financieros nunca se guardan.
