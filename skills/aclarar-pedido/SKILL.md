---
name: aclarar-pedido
description: Usar cuando un pedido del usuario es grande, vago o ambiguo (palabras como "listo", "todo", "mejora", "arregla", "como antes") o se va a ejecutar sin supervisión, y hay que convertirlo en un pedido claro con objetivo, fin medible, alcance y restricciones haciendo pocas preguntas; también cuando el usuario dice que no sabe cómo explicarle algo a la IA o que la IA entendió otra cosa.
---

# Aclarar un pedido

La regla [[pedidos-sin-ambiguedad]] dice **qué** debe tener un pedido antes de ejecutarlo; esta skill es el **cómo**. Apoyos: [[no-asumir-separar-confirmado]], [[leer-y-responder-cada-mensaje]], [[respuestas-concisas]]. El resultado alimenta a `plan-con-casillas` y a `preparar-goal`, pero sirve solo, para cualquier pedido.

## 1. Entender antes de preguntar
1. Lee el pedido completo y lo que ya existe sobre el tema: código, documentos, plan abierto, `.memory/`.
2. Todo lo que se pueda averiguar leyendo se averigua; no se pregunta lo que ya está escrito.
3. Si el pedido ya es claro y pequeño, no uses esta skill: hazlo.

## 2. Rellenar el borrador de los seis datos
Copia `references/pedido-aclarado.md` y marca cada dato como **dicho** (lo dijo el usuario), **inferido** (lo deduces; debe confirmarse) o **falta**. Los seis: objetivo, estado final medible, cómo se comprueba, alcance y fuera de alcance, restricciones, y qué decide solo el usuario.

## 3. Traducir las palabras ambiguas
Si el pedido usa "listo", "todo", "mejora", "arregla", "rápido", "como antes" u otra del estilo, busca la palabra en `references/palabras-ambiguas.md` y úsala para hacer la pregunta que la vuelve medible. Si trae ejemplos ("por ejemplo", "tipo"), aplica la skill `interpretar-ejemplos`: son una muestra, no una lista.

## 4. Preguntar poco y bien
- Hasta 5 preguntas por ronda, la más decisiva primero; cada una con 2 a 4 opciones y **tu recomendación y por qué** (con la herramienta de preguntas si existe; si no, en el texto).
- Para cuando cada uno de los seis datos esté dicho o inferido y confirmado. No sigas preguntando por perfección.
- Si el usuario responde "lo que tú veas", registra la decisión como **suposición tuya** con su motivo, para que pueda corregirla.

## 5. Confirmar y entregar
1. Escribe en pantalla el pedido aclarado, en pocas líneas: "Entendí: …" con los seis datos, marcando suposiciones.
2. Si el trabajo es grande o irreversible, espera el visto bueno antes de seguir; si no, continúa y deja la suposición a la vista.
3. Entrégalo al paso siguiente: `plan-con-casillas` (plan) o `preparar-goal` (objetivo persistente). El pedido aclarado queda dentro de ese plan o prompt, no solo en el chat.

## Cuándo NO usar
- Pedidos pequeños y claros: se hacen directamente.
- Cuando lo que falta es una decisión técnica que se resuelve leyendo el código: se lee.
- Para redactar el prompt final para otra IA: eso es `crear-prompt-para-ia`; aquí solo se aclara qué se quiere.
- Para decidir entre opciones de diseño del propio proyecto sin ambigüedad del usuario: eso es `spec-driven-workflow`.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Se entiende solo, empiezo" | Si admite dos lecturas que cambian el resultado, se pregunta antes: construir la lectura equivocada cuesta más que la pregunta. |
| "Le pregunto todo lo que se me ocurra" | Hasta 5 por ronda y solo lo que cambia el resultado; lo demás se averigua leyendo o se supone a la vista. |
| "Doy por dicho lo que deduje" | Lo deducido se rotula "inferido" y se confirma; no se presenta con el mismo peso que lo dicho. |
| "Con 'listo' basta como criterio de término" | "Listo" no es medible: se traduce a una comprobación concreta (comando, prueba, número) antes de seguir. |

## Errores comunes
- Preguntar sin haber leído antes el código y los documentos.
- Hacer preguntas sin recomendación, que obligan al usuario a diseñar la respuesta.
- Dejar el pedido aclarado solo en el chat.
- Seguir preguntando cuando ya están los seis datos.

## Verificación
- Los seis datos figuran en el pedido aclarado, cada uno marcado como dicho, inferido o falta, sin "falta" restantes.
- Cada palabra ambigua del pedido original tiene su traducción medible.
- El usuario confirmó la frase "Entendí: …" (o la suposición quedó a la vista).
- El pedido aclarado está escrito en el plan o en el prompt, no solo en la conversación.
