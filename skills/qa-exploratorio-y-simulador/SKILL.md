---
name: qa-exploratorio-y-simulador
description: Usar cuando se quiere probar "como una persona", tras cambios grandes de UX o comandos, o para buscar bugs que un guion no encuentra. Sesiones exploratorias con charter, simulador con semilla reproducible y heurísticas de usabilidad.
---

# Exploratorio y uso "como persona"

El QUÉ (QA aparte, semilla siempre registrada, lo no explorado se declara) está en [[qa-independiente-y-oraculos]]. Para terminal, ver también la guía de QA de terminal del proyecto, si la tiene. Esta skill cubre el CÓMO. La usa el agente `qa-explorador`. Los hallazgos se reportan con `qa-bugs-y-triage`.

## Charter
Plantilla: **Explorar** `<área>` **con** `<recursos/datos/estado>` **para descubrir** `<riesgo>`.
Ejemplo: "Explorar el carrito con 12 ítems, descuento y propina para descubrir totales que no cierran".
Sesión de 30-45 min con notas: qué se hizo, qué se vio, hallazgos, preguntas y qué se dejó sin explorar.

## Guiones tipo
Elige un flujo real del usuario: jornada completa de uso, cambio de turno o de sesión, corte a mitad de una operación (reabrir y verificar qué quedó guardado), carga masiva de datos, reposición tras un error.

## Simulador de usuario (si el proyecto lo tiene o se escribe uno)
- Cada sesión sale de `(semilla, índice)`; una opción de reproducción repite la sesión idéntica. Imprime siempre la semilla.
- Escenarios mínimos: lenguaje coloquial, erratas, MAYÚSCULAS, pegado multilínea, Enter repetido, línea larguísima, unicode/RTL/cero-ancho/ANSI, comandos inexistentes, entrada mixta, EOF a mitad de línea, Ctrl+C.
- Invariantes: no se cuelga; toda entrada no vacía recibe respuesta; sin trazas ni rutas internas; sin secretos; termina limpio tras el cierre.
- Autoprueba: inyecta a propósito una versión defectuosa y exige que los invariantes salten. El probador debe poder fallar.
- Guarda la transcripción de cada corrida en la carpeta de informes.
- Trampa: si el programa reimprime el prompt antes de contestar, mide la "respuesta" esperando contenido distinto del prompt, no silencio.

## Heurísticas de usabilidad
1. Todo error dice qué pasó y qué hacer.
2. Nunca silencio: cada acción muestra un resultado o un estado.
3. Formatos consistentes (moneda, fechas, atajos, marcadores).
4. Estado visible: modo, sesión o cola de sincronización siempre a la vista.
5. Prevención de daño: las acciones destructivas o de dinero piden confirmación; el modo por defecto es el seguro.
6. Ayuda descubrible y coherente con lo que el sistema hace.
7. Objetivos táctiles de al menos 44 px; sin desborde horizontal en pantalla angosta (390 px).
8. Salida legible: sin `undefined`/`NaN`/`[object Object]`, sin rutas internas.
9. Cierre limpio y predecible (EOF, Ctrl+C); idioma y tono uniformes.

## Reglas
Datos ficticios y base temporal. Un fallo durante una recompilación o con otra sesión usando el entorno no es un bug: reproduce 3 veces antes de reportar.

## Cuándo NO usar
- Verificar un requisito con resultado esperado fijo: eso es un caso de `qa-plan-y-casos` (oráculo independiente y trazabilidad), no una sesión exploratoria.
- Probar una terminal con teclas, menús y capturas: va a la guía de QA de terminal del proyecto (si la tiene), que define el arnés PTY y lo que no se prueba.
- Reportar un fallo ya reproducido: su informe va con `qa-bugs-y-triage`, no dentro de la sesión.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "La suite está en verde, explorar sobra" | Una suite solo busca lo que alguien escribió; la sesión existe para lo que un guion no encuentra, con charter y objetivo escrito. |
| "Ese fallo no sale otra vez, no vale la pena" | Se reproduce 3 veces antes de reportar; solo se descarta si pasó durante una recompilación o con otra sesión usando el entorno. |
| "El simulador funciona, no hace falta probarlo" | Sin autoprueba no sabemos si puede fallar: hay que inyectar una versión defectuosa y comprobar que los invariantes saltan. |

## Errores comunes
- Empezar sin charter ni lista de lo no explorado; la skill exige qué se hizo, qué se vio, hallazgos, preguntas y lo dejado sin explorar.
- Lanzar el simulador sin imprimir la semilla: la corrida no se puede repetir y el hallazgo no es reproducible.
- Medir la "respuesta" de un programa que reimprime el prompt: hay que esperar contenido distinto del prompt, no silencio.
- Usar datos reales o una base que no es temporal, en vez de datos ficticios.

## Verificación
- Relanzar la semilla impresa con la opción de reproducción y comparar con la transcripción guardada en la carpeta de informes: deben coincidir.
- Autoprueba: con una versión defectuosa inyectada, al menos un invariante debe fallar; si todo pasa, el probador no sirve.
- Buscar en la transcripción `undefined`, `NaN` y `[object Object]` con una búsqueda de texto; cada coincidencia es un hallazgo de salida.
- Cada hallazgo tiene sus tres repeticiones anotadas antes de pasarlo a `qa-bugs-y-triage`.
