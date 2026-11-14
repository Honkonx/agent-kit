# Plan con fases, metas y casillas antes de actuar (trabajo mediano o grande)

> Aplica a: todo proyecto. Reglas relacionadas: [[usuario-declara-listo]], [[subagentes-max-3-y-verificar]], [[leer-y-responder-cada-mensaje]], [[cierre-de-ronda]], [[docs-organizacion-y-fechada]], [[documentar-en-vivo]].

El trabajo mediano o grande se hace con un plan escrito, dividido en **fases**; cada fase agrupa **metas** numeradas con casilla y criterio verificable. El plan se crea **antes de construir**, se trabaja una fase y una meta a la vez, y cada casilla se tacha al terminar. Las casillas las cierra **el asistente con evidencia**; que el **producto** (sistema, programa, función) esté bien y aceptado es otra cosa, y solo lo declara el usuario ([[usuario-declara-listo]]).

## Por qué
En rondas grandes se lanzó mucho trabajo sin una lista verificable y el usuario no pudo saber qué estaba terminado. Con un plan se responde "¿lo hiciste?" mirando una tabla y no la memoria, se trabaja en orden y se ve el avance por fases.

## Cómo se aplica
**Cuándo lleva plan**
- Lleva plan: cambios que abarcan varias metas (tres o más archivos o varias tandas, cambian comportamiento, requieren medición, se reparten en subagentes o exceden una sesión corta) y documentación grande. **El plan se crea antes de construir; no se empieza sin él.**
- No lleva: preguntas, informes sueltos, opiniones, análisis, investigaciones (se documentan en su archivo), cambios pequeños y tareas de una sola meta. Ante la duda, no se crea plan: se hace lo pedido. Excepción: si el usuario pide una "auditoría extensa", se abre plan con una meta por área.

**Estructura: plan → fases → metas**
- El plan se divide en **fases ordenadas** (`F1`, `F2`…). Cada fase agrupa metas numeradas (`F1.1`, `F1.2`…), cada una con **casilla**.
- Cada meta lleva: entregable concreto, **criterio de verificación medible** (comando, prueba o número), esfuerzo estimado y dependencias. Un identificador estable por meta, para poder decir "la F2.3".
- El plan también lleva: objetivo y por qué, alcance y **no alcance**, riesgos, decisiones pendientes del usuario y un **registro de avance con fecha**.
- Cada pedido del usuario se transcribe como meta, con su texto.

**Casillas**
- `[ ]` pendiente · `[x]` verificada · `[~]` parcial (con lo que falta) · `[-]` descartada (con motivo).
- Dos columnas, **las dos las llena el asistente**: **Hecho** (entregable existente y verificado, con evidencia citada: comando, `archivo:línea`, prueba, fecha) y **Listo** (la meta quedó **cerrada**: Hecho `[x]`, plan, documentos y memoria al día y ningún pendiente de esa meta). Cerrar una meta no significa que el usuario haya aceptado el resultado: eso se registra aparte (ver Cierre del plan).
- **Una fase se tacha (`[x]`) solo cuando todas sus metas están `[x]` o `[-]` con evidencia.** Con una meta `[~]`, la fase queda `[~]`. No se abre la fase siguiente sin dejar la anterior con su casilla al día, salvo piezas independientes declaradas en el plan.
- La casilla la pone el principal tras verificar, nunca un subagente por su informe.

**Cómo se trabaja**
- **Una cosa a la vez:** la meta en curso se deja `[x]` o `[~]` con motivo y el plan se actualiza **en ese momento**, antes de pasar a la siguiente ([[documentar-en-vivo]]). El paralelismo de subagentes se limita a piezas independientes ya listadas como metas.
- El plan se muestra primero y se espera luz verde si el alcance es ambiguo o grande; con "haz todo" se ejecuta en el orden del plan sin volver a preguntar.
- Metas nuevas a mitad de camino se añaden al plan antes de empezarlas. Si cambia el alcance o el orden, se anota con fecha: el plan no se reescribe en silencio.
- Que una lista esté creada no quiere decir que esté completa: lo está solo si se contrastó con su fuente; si no, queda `[~]` y dice qué no se contrastó.
- Toda respuesta de cierre cita el plan y su estado real: fases y metas hechas, parciales (con el hueco) y pendientes ([[cierre-de-ronda]]).

**Cierre del plan**
- Un plan se cierra cuando todas sus metas están `[x]` o `[-]` y con **Listo** `[x]` (lo cierra el asistente). Eso cierra el **plan**, no el producto: la aceptación del resultado la declara el usuario aparte, en una línea `Aceptación del usuario:` con su cita; no es requisito para cerrar ni archivar el plan, y mientras falte el informe dice "plan cerrado; pendiente de tu aceptación del producto".
- Al cerrarlo: dejar un resumen en el índice de mejoras o pendientes, mover el archivo a la carpeta de planes archivados (con `git mv` si hay repositorio; no borrar) y corregir las referencias en la misma ronda.
- Un plan archivado es una foto fechada: ya no se edita ([[docs-organizacion-y-fechada]]).

**Comprobación automática** (recomendada)
- Una prueba que exija: columnas Hecho y Listo en cada tabla; ningún Listo `[x]` con Hecho sin marcar; ningún `[x]` sin evidencia; ninguna fase `[x]` con metas abiertas.

## Esqueleto mínimo
```
# Plan: <nombre>        Fecha · Objetivo · Alcance / No alcance
## F1 — <fase>          [ ]
| Meta | Entregable | Criterio verificable | Esfuerzo | Hecho | Listo |
| F1.1 | ...        | comando / número     | S/M/L    | [ ]   |       |
## F2 — <fase>          [ ]
...
Riesgos · Decisiones pendientes del usuario · Registro de avance (fecha — qué cambió)
```

## Ejemplos
- No: lanzar seis tareas en paralelo y responder "ya está casi todo".
- Sí: plan con F1 y F2; F1.1 `[x]` con la salida de la prueba, F1.2 `[~]` con lo que falta, F2 sin abrir; plan aún abierto y aceptación del usuario pendiente.
- No: crear un plan para corregir una errata.
- No: tachar la fase F1 con una meta parcial.

## Qué se ajusta por proyecto
- Carpeta, plantilla y convención de nombres de los planes; prefijo de las metas.
- Escala de esfuerzo, y umbral exacto de "mediano o grande" si el proyecto quiere afinarlo.
- Carpeta de planes archivados, índice donde queda el resumen y la prueba automática del formato.
