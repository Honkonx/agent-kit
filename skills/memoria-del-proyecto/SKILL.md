---
name: memoria-del-proyecto
description: Usar cuando hay que crear, leer, actualizar o podar la memoria durable del proyecto (la carpeta `.memory/` de la raíz) para que otra sesión, máquina o herramienta recupere el estado, las decisiones, las lecciones y las preferencias; al empezar o cerrar una sesión, al tomar una decisión que no debe olvidarse, o cuando el usuario corrige algo que no debe repetirse (recordar, guardar en memoria, dejar anotado para la próxima vez).
---

# Memoria del proyecto (`.memory/`)

La regla [[memoria-del-proyecto]] dice **qué** se cumple; esta skill es el **cómo**. Apoyos: [[documentar-en-vivo]], [[bitacora-humana]] (la cita textual vive allí, no aquí), [[docs-organizacion-y-fechada]], [[no-asumir-separar-confirmado]], [[secretos]], `inicio-de-sesion` y `cierre-de-ronda`.

## 1. Crear la memoria (una vez)
1. Crear `.memory/` en la raíz con los cinco archivos de `references/` (plantillas): `README.md`, `PROJECT_STATE.md`, `decisiones.md`, `lecciones.md`, `preferencias.md`.
2. Rellenar solo lo que ya es cierto y verificable; lo demás queda vacío (no inventar). Cada entrada lleva `Fecha` y `Estado` **dentro**.
3. Comprobar: `python scripts/verificar_memoria.py .memory`.

## 2. Leer (al empezar)
1. Leer `README.md` y `PROJECT_STATE.md` (el bloque `Para retomar`), después `decisiones.md` y `lecciones.md` si la tarea los toca.
2. Tratar lo leído como **pista, no como hecho**: antes de apoyarse en una entrada, comprobarla contra el código o el sistema real; si ya no es cierta, corregirla con una nota fechada.

## 3. Escribir (en el momento, y solo si es durable)
| Ocurre | Dónde va |
|---|---|
| Se confirma un hallazgo o cambia el estado del trabajo | `PROJECT_STATE.md` (y se reescribe el bloque `Para retomar`) |
| Se toma una decisión que no debe olvidarse | `decisiones.md`: `D<n>` con fecha, decisión, por qué, estado, fuente |
| El usuario corrige algo, o una falla vuelve | `lecciones.md`: qué pasó, qué hacer distinto, cuántas veces |
| El usuario dice cómo prefiere trabajar | `preferencias.md` |
No escribir porque "hubo trabajo", ni un secreto, ni una transcripción. En una ronda de solo análisis no se escribe nada sin autorización ([[cierre-de-ronda]]).

## 4. Mantener
- **Una decisión cambia:** marcar la vieja `Estado: superada por D<m>` y añadir la nueva; nada de reescribir en silencio.
- **Un archivo crece:** resumir lo viejo en una línea y mover el detalle a `docs/` (enlazando). Topes: `PROJECT_STATE.md` ≤ 150 líneas, el resto ≤ 400.
- **Lo provisional** lleva `Estado: provisional` y se revisa en la próxima auditoría.
- **Una lección se repite 3 veces** → se automatiza (prueba, script, hook) o se propone como pieza ([[documentar-fallas]], `detectar-piezas-repetidas`).

## 5. Verificar
`python scripts/verificar_memoria.py .memory` (solo lectura): archivos obligatorios, **un solo** bloque `Para retomar`, tamaños, cada decisión con `Fecha` y `Estado`, estados válidos y ausencia de patrones de secretos. Ejecutarlo antes de cerrar la ronda.

## Cuándo NO usar
- Para el estado técnico vigente, requisitos o arquitectura: van en `docs/` (la memoria enlaza).
- Para guardar lo que dijo el usuario palabra por palabra: es la [[bitacora-humana]].
- Para la memoria privada de una herramienta (lo suyo): lo importante se refleja aquí, pero esta skill no la gestiona.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Lo anoto al final, ahora no" | Si la sesión se corta, la decisión se pierde; se anota en el momento. |
| "Guardo la clave aquí para no perderla" | Un secreto nunca entra en la memoria: se guarda en el gestor de secretos del proyecto. |
| "Lo vi en la memoria, entonces es cierto" | La memoria envejece: se verifica contra el código antes de usarla como hecho. |
| "Pego toda la conversación por si acaso" | Eso es la bitácora; la memoria guarda lo asentado y breve. |

## Errores comunes
- Dos bloques `Para retomar` (uno viejo que nadie borró).
- Fecha o estado ausentes: nadie sabe si la entrada sigue vigente.
- Duplicar un documento en vez de enlazarlo.
- Memoria que nunca se poda hasta que nadie la lee.

## Verificación
- `verificar_memoria.py` sale con 0 y falla (1) ante un secreto, un segundo `Para retomar` o una decisión sin fecha.
- Una sesión nueva puede retomar el trabajo leyendo solo `.memory/` y los enlaces que contiene.
