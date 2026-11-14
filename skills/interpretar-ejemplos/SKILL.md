---
name: interpretar-ejemplos
description: Usar cuando el usuario da ejemplos en su pedido ("por ejemplo", "tipo", "como", "algo así", "ejemplo:") y hay que decidir qué hacer con ellos: entender el criterio que ilustran en lugar de tomarlos como lista cerrada, orden o texto a copiar; también al escribir ejemplos propios en una pieza, un plan o una respuesta.
---

# Interpretar los ejemplos del usuario

La regla [[ejemplos-son-ilustrativos]] dice **qué** se cumple; esta skill es el **cómo**. Apoyos: [[pedidos-sin-ambiguedad]], [[leer-y-responder-cada-mensaje]]. Se usa dentro de `aclarar-pedido` y sirve sola.

## 1. Reconocer el ejemplo
Marcas típicas: "por ejemplo", "tipo", "como", "algo así", "ejemplo:", "digamos", una lista corta tras "cosas como". Si el usuario dice "exactamente", "solo", "literal" o "usa esto", **no es un ejemplo**: es una orden.

## 2. Sacar el criterio
1. Lista los ejemplos y busca lo que tienen en común: ¿qué los hace candidatos?
2. Escribe el criterio en una frase ("skills de un tema que no se puede universalizar") y compruébalo contra cada ejemplo.
3. Si los ejemplos parecen de dos criterios distintos, es ambiguo: pregunta.

## 3. Aplicar a todo lo que cumple
- Busca **todo** lo que cumple el criterio, no solo lo citado.
- Si es demasiado para hacerlo de una vez, muestra la lista completa o el alcance y deja que el usuario elija; no recortes en silencio a lo citado.
- Ignora el orden y la cantidad de los ejemplos; no copies su texto ni su formato salvo orden expresa.

## 4. Decir lo entendido
Una frase: "Tomé X, Y y Z como ejemplos del criterio C; apliqué C a N casos". Así el usuario ve si la lectura fue la suya. Si no estás seguro, pregunta con una recomendación antes de actuar.

## 5. Cuando los ejemplos los escribes tú
Marca que son ejemplos, usa varios y distintos entre sí (para que no se tomen como plantilla) y no los presentes como la lista completa.

## Cuándo NO usar
- Cuando el usuario fijó algo literal ("exactamente así", "solo estos"): se hace tal cual.
- Cuando la lista es una enumeración completa dicha como tal ("estas tres, nada más").
- Para aclarar un pedido vago en general: eso es `aclarar-pedido`.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Lo dijo así, lo hago así" | Un ejemplo ilustra; copiarlo literal deja fuera lo que quería incluir. |
| "Hago los tres que dijo y listo" | Si eran ejemplos de un criterio, faltan los demás que lo cumplen. |
| "Si pregunto, molesto" | Una pregunta corta con recomendación cuesta menos que rehacer el trabajo. |
| "Su ejemplo de formato sirve de plantilla" | Solo si lo pidió; si no, se repite su texto en todo. |

## Errores comunes
- Convertir una lista de ejemplos en la lista completa.
- Seguir el orden de los ejemplos como si fuera prioridad.
- Copiar las palabras del ejemplo en el resultado.
- No decir qué criterio se entendió.

## Verificación
- El criterio está escrito en una frase y encaja con cada ejemplo citado.
- Se cubrió todo lo que cumple el criterio, o se mostró el alcance para que el usuario elija.
- Lo entendido se dijo en una frase y no hay texto copiado de los ejemplos.
