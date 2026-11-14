---
name: plan-con-casillas
description: Usar cuando una tarea mediana o grande (tres o más archivos, varias metas, o más de una sesión) necesita un plan escrito con fases, metas y casillas antes de construir (partir un trabajo grande en tramos o etapas y llevar una lista de tareas para tachar lo terminado), o cuando hay que actualizar, fichar o cerrar un plan existente.
---

# Plan con fases, metas y casillas

La regla [[planes-con-casillas]] dice **qué** se debe cumplir; esta skill dice **cómo** se hace, paso a paso. Convive con [[usuario-declara-listo]] (las casillas las cierras tú con evidencia; que el **producto** esté bien lo declara solo el usuario) y [[documentar-en-vivo]] (se ficha al terminar cada meta, no al final).

## 1. Decidir si lleva plan
- **Sí:** cambios que abarcan varias metas, tres o más archivos, cambian comportamiento, necesitan medición, se reparten en subagentes o exceden una sesión corta; documentación grande; una "auditoría extensa" pedida por el usuario (una meta por área).
- **No:** preguntas, informes sueltos, opiniones, análisis, investigaciones (van en su propio documento), cambios pequeños, tareas de una sola meta.
- Ante la duda, **no se crea plan**: se hace lo pedido.

## 2. Crear el plan (antes de construir)
> Atajo: el comando `/plan` delega esta redacción en el agente `planificador` (Haiku 5.5, esfuerzo high), que escribe el plan y lo valida; tú verificas su resultado y lo muestras. Los pasos de abajo son lo que ese agente hace.

1. Copia `references/plantilla-plan.md` a la carpeta de planes del proyecto, con nombre por tema (`<tema>.md`); la fecha va dentro del archivo (línea `**Fecha:**`).
2. Escribe objetivo y por qué, alcance y **no alcance**.
3. Divide en **fases ordenadas** (`F1`, `F2`…): cada una es un tramo con sentido propio que se puede verificar y cerrar.
4. En cada fase, las **metas** (`F1.1`, `F1.2`…): entregable concreto, criterio de verificación **medible** (comando, prueba o número), esfuerzo (S/M/L) y dependencias. Cada pedido del usuario se transcribe como meta, con su texto.
5. Anota riesgos y decisiones pendientes del usuario.
6. **Muestra el plan en pantalla** y espera luz verde si el alcance es grande o ambiguo. Con "haz todo" se ejecuta en el orden del plan sin volver a preguntar.

## 3. Ejecutar: una meta a la vez
1. Trabaja la meta en curso hasta dejarla `[x]` o `[~]` con motivo.
2. **En ese momento** actualiza el plan: pon la casilla Hecho y escribe la línea `Evidencia F1.1:` con el comando y su resultado, el `archivo:línea` o la medición. Sin evidencia no hay `[x]`.
3. Solo entonces pasa a la siguiente. Subagentes: solo piezas independientes ya listadas como metas; la casilla la pone el hilo principal tras verificar, nunca el subagente por su informe.
4. Si aparece una meta nueva o cambia el alcance, **añádela al plan antes de empezarla** y anótalo en el registro de avance con fecha. El plan no se reescribe en silencio.

Estados de casilla: `[ ]` pendiente · `[x]` verificada · `[~]` parcial (con lo que falta) · `[-]` descartada (con motivo).

## 4. Cerrar una fase
- La fase pasa a `[x]` solo si **todas** sus metas están `[x]` o `[-]` con evidencia. Con una meta `[~]`, la fase queda `[~]`.
- No se abre la fase siguiente sin dejar la anterior fichada (salvo piezas independientes declaradas en el plan).

## 5. Cerrar el plan
1. Todas las metas `[x]` o `[-]`, y con **Listo** `[x]` (lo marcas tú cuando la meta tiene Hecho `[x]`, el plan, los documentos y la memoria están al día y no queda pendiente de esa meta). Eso cierra el **plan**; no significa que el usuario acepte el producto.
2. La aceptación del producto la declara el usuario aparte: si la da, anótala en `Aceptación del usuario:` con su cita; mientras falte, el informe dice "plan cerrado; pendiente de tu aceptación del producto". No bloquea archivar el plan.
3. Deja un resumen en el índice de mejoras o pendientes del proyecto.
4. Mueve el plan a la carpeta de planes archivados con `git mv` (no se borra) y corrige las referencias en la misma ronda.
5. Un plan archivado es una foto fechada: ya no se edita ([[docs-organizacion-y-fechada]]).

## 6. Validar (recomendado)
```
python scripts/validar_plan.py <plan.md>
```
Comprueba: columnas Hecho y Listo; ningún `[x]` sin línea `Evidencia`; ningún Listo `[x]` con Hecho sin marcar; ninguna fase `[x]` con metas abiertas. Úsalo antes de decir "plan al día" y como prueba automática del proyecto.

## 7. En cada respuesta de cierre
Cita el plan y su estado real: fases y metas cerradas, parciales (con el hueco) y pendientes ([[cierre-de-ronda]]). Puedes decir "plan cerrado"; nunca digas que el **producto** está "listo": eso lo declara el usuario.

## Cuándo NO usar
- Preguntas, informes sueltos, opiniones, análisis o investigaciones (van en su propio documento).
- Cambios pequeños o tareas de una sola meta: se hace lo pedido, sin plan.
- Cuando el usuario ya dio un plan escrito: se ejecuta ese, no se crea otro.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es rápido, lo tacho al final" | Se ficha al terminar cada meta; al final se olvida qué evidencia había. |
| "La fase está casi lista, la tacho" | Una fase con una meta parcial queda `[~]`, nunca `[x]`. |
| "El validador da OK, entonces el producto está listo" | El validador comprueba el formato y la evidencia, no que el producto esté bien: cierras la **meta** y el **plan**; que el **producto** esté aceptado lo declara el usuario. |
| "Dejo Listo vacío hasta que el usuario lo apruebe" | Listo es el cierre de la meta y lo marcas tú con evidencia; la aceptación del producto es otra línea, del usuario. |

## Errores comunes
- Tachar una fase con una meta parcial.
- Fichar al final de la tanda en vez de al terminar cada meta.
- Crear plan para una errata o una pregunta.
- Meta sin criterio medible ("mejorar el rendimiento"): reescríbela con un número o una prueba.
- Una barra vertical `|` dentro de una celda (por ejemplo un comando con tubería) rompe la tabla y `validar_plan.py` la rechaza: describe la comprobación sin ella ("`ls salida` muestra 12 archivos") o escríbela como `\|`.
