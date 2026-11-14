---
name: bitacora-humana
description: Usar cuando hay que crear, ampliar, cerrar o revisar la bitácora humana del proyecto (archivos numerados por lotes de 6 a 9 mensajes del usuario con cita textual y cómo se entendieron), o cuando un mensaje con orden, decisión, corrección o autorización debe quedar registrado en el momento (dejar por escrito, palabra por palabra, lo que dijo el usuario para recordarlo en otra sesión).
---

# Bitácora humana por lotes

Las reglas [[bitacora-humana]] y [[documentar-en-vivo]] dicen **qué** se cumple; esta skill dice **cómo** se lleva. Apoyos: [[secretos]], [[leer-y-responder-cada-mensaje]], [[docs-organizacion-y-fechada]], [[cierre-de-ronda]].

## 1. Preparar la carpeta (una vez)
1. Crea la carpeta **`docs/humano/`** con un `INDEX.md` (propósito y lista de lotes).
2. Nombre de archivo: **`humano1.md`, `humano2.md`, `humano3.md`…** (consecutivo, sin ceros, sin tope). La **fecha va dentro** del archivo (`**Fecha:**` al inicio), no en el nombre. Solo si dos sesiones chocan: una subcarpeta como serie paralela con su propia numeración.

## 2. Registrar en el momento
1. Al procesar un mensaje del usuario con orden, decisión, corrección o autorización, anótalo **ya** en el lote abierto; no al cerrar la ronda.
2. Un "sí, entendido" se consolida con el mensaje anterior o el siguiente. Un arreglo de una línea no pide archivo propio.
3. Un punto por tema: si el mensaje traía ocho cosas, son ocho puntos.
4. Solo el hilo que ve la conversación escribe la bitácora. Un subagente no la crea ([[bitacora-humana]]).

## 3. Escribir cada punto
Usa `references/plantilla-lote.md`. Cada punto lleva:
- **Lo que pidió:** cita textual, con sus erratas. Si fue implícito: "no lo dijo con estas palabras; lo entendí de…".
- **Cómo lo entendí:** mi lectura, qué decidí y, si había varias, por qué elegí una.
- Detalle: qué cambió, números medidos, cómo se verificó, lo que **quedó sin hacer** dicho claro.

## 4. Redactar secretos
Antes de pegar la cita, busca claves, tokens, contraseñas y datos financieros reales. Reemplaza solo ese fragmento por `<REDACTADO-AAAA-MM-DD — descripción>` y deja el resto tal cual. Si detectas un secreto ya escrito: redáctalo de inmediato y avisa para rotarlo ([[secretos]]). Es la única edición permitida de un archivo viejo.

## 5. Abrir y cerrar lotes
- Menos de 6 puntos: lote **abierto**, se sigue ampliando el mismo archivo.
- De 6 a 9: se puede cerrar. Más de 9: abre el siguiente (`humano<N+1>.md`).
- Se cuentan mensajes del usuario, no turnos del asistente ni notificaciones automáticas.
- Un archivo cerrado no se corrige: lo nuevo va en el siguiente, que lo enlaza.
- Al cerrar un lote, añádelo al `INDEX.md`.

## 6. Verificar
```
python scripts/verificar_bitacora.py docs/humano
```
Comprueba `humanoN.md` con numeración sin saltos desde 1, la fecha dentro del archivo, 6 a 9 puntos por archivo cerrado (el último puede estar abierto con menos de 6), "Lo que pidió" y "Cómo lo entendí" en cada punto, y ausencia de patrones de secretos (`ghp_`, `sk-`, `-----BEGIN`). Ejecútalo antes de cerrar la ronda ([[cierre-de-ronda]]).

## 7. Propagar
Los hallazgos técnicos confirmados van también a la memoria persistente y a su documento técnico; la bitácora no reemplaza requisitos, arquitectura ni evidencia de QA.

## Cuándo NO usar
- Para el estado técnico vigente (requisitos, arquitectura, pruebas): eso va en sus documentos; la bitácora aporta contexto y no los reemplaza.
- Para un "sí, entendido" suelto o un arreglo de una línea: se consolidan con el mensaje anterior o siguiente, sin archivo propio.
- Dentro de un subagente: no ve la conversación real del usuario; lo escribe el hilo principal.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Lo registro al cerrar la ronda" | Si la sesión se corta, se pierde justo la cita textual; se registra en el momento. |
| "Resumo lo que pidió, es más claro" | La cita va **textual y con sus erratas**: el archivo sirve para ver si se entendió bien lo que se dijo. |
| "Pego el mensaje completo, incluida la clave" | Un secreto nunca va textual: se redacta (`<REDACTADO-fecha>`). |

## Errores comunes
- Parafrasear o "arreglar" la cita.
- Fundir cita e interpretación en un solo párrafo.
- Un punto "varios ajustes".
- Escribir la bitácora al final de la tanda.
- Reescribir un archivo viejo porque se entendió mal: eso va en el nuevo.
- Transcribir una clave "porque es textual".
