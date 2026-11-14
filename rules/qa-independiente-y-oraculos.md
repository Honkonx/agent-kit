# QA independiente, con oráculo, contraprueba y cobertura honesta

> Aplica a: todo proyecto. Reglas relacionadas: [[verificacion-empirica]], [[subagentes-max-3-y-verificar]], [[documentar-fallas]], [[usuario-declara-listo]], [[secretos]]. Agentes de QA, si el proyecto los define: `qa`, `qa-adversarial`, `qa-explorador`, `qa-regresion`.

Quien escribe el código no es quien lo juzga: el QA corre como agente aparte, contra lo real, con pruebas que pueden fallar, casos trazables y un informe que dice qué **no** se probó.

## Por qué
Una suite con miles de pruebas en verde dejó pasar visores que no abrían y textos que decían algo distinto de lo que el sistema hacía; varios "OK" falsos seguidos (código 200 sin efecto, error silenciado, base que nunca se creó) salieron de chequeos que no podían fallar. Un QA hecho por el mismo hilo hereda su punto ciego. Un fuzzer pasó con el defecto presente porque no verificaba que lo válido se conservara.

## Cómo se aplica
**1. Independencia**
- El QA es un **agente aparte** (nunca un subagente que herede el contexto de quien implementó, porque hereda su sesgo), sobre el código ya quieto (sin cambios en curso), caja negra, contra lo real compilado y corriendo, con datos ficticios y base temporal. Quien implementa en paralelo no intenta el recorrido: declara que queda pendiente.
- No arregla código de producto: reporta con repro; decide el hilo principal o el usuario. Solo edita sus propias pruebas.
- Si el principal añadió pantallas, endpoints o comandos desde la última pasada, el QA añade casos antes de reportar: una función nueva sin caso no está cubierta.
- Al cerrar un cambio que llega a una pantalla, se adjunta el informe del QA; sin informe, no está terminado. Dos capas, ninguna reemplaza a la otra: un robot automatizado en cada cierre (consola, errores de red, desbordes, anchos de pantalla) y recorridos de persona en tandas grandes o periódicos (¿el texto y el número dicen lo que el sistema hace?).

**2. Oráculo independiente**
- El esperado se calcula por una vía distinta de la función probada (aritmética exacta, implementación lenta y obvia de referencia, o literal calculado a mano con su derivación). Nunca `f(x) == f(x)`.
- Entradas hostiles además de ejemplos: extremos, vacíos, nulos, unicode, comillas e inyección, textos enormes, basura binaria; y propiedades/invariantes (idempotencia, "cerrar(abrir(x)) deja balance 0", "lo válido se conserva").
- **Semilla siempre registrada**: todo test aleatorio o simulador imprime su semilla y permite reproducir (`semilla:índice`). Un hallazgo sin semilla no es reproducible y no cuenta.
- **Procedencia, no solo resultado**: toda operación relevante deja una traza (id, origen, causa con cada regla evaluada y su veredicto, marca de tiempo, secuencia, padre). El test verifica que está completa, ordenada y encadenada, y que reconstruir el estado solo desde la traza da el estado real. Los casos negativos nombran la regla culpable y no generan eventos posteriores.
- Dinero siempre con tipos exactos, nunca coma flotante, también en el oráculo.

**3. Contraprueba: el chequeo debe poder fallar**
- Todo test nuevo se prueba a sí mismo una vez: romper el código a propósito (invertir una condición, quitar una regla) o alterar la traza, confirmar que cae y restaurar comparando con el original. Reportar qué mutación se usó. Cada defecto confirmado termina con una regresión permanente.
- Prohibido silenciar el error del paso central (en PowerShell `SilentlyContinue`; en shell `2>/dev/null`); el mensaje de éxito va **dentro** del bloque que verificó el efecto; se verifica el efecto (la fila existe, la base contesta), no la invocación.
- Comprobar por lo que la persona ve (texto visible), no por estructura interna frágil (clases, detalles internos del DOM como `offsetParent`, portales de componentes). Si una sonda contradice lo esperado dos veces, tomar captura.
- Un ajuste que se guarda se **recarga y se vuelve a mirar**: un aviso de éxito es la invocación, no la verificación.
- Montos, sumas, códigos, cantidades y números de comprobante se comparan **número a número** contra la fuente de verdad; ver una etiqueta o un nombre no es verificar. Tamaños y posiciones se **miden**, no se estiman.
- Probar con **todos los roles** (lo que uno ve y puede hacer, lo que no puede aparece deshabilitado con motivo) y que lo que la pantalla ofrece lo acepta el backend. Campos: limpiar antes de escribir y verificar el largo. No disparar diálogos nativos del sistema o del navegador que bloquean la sesión sin avisar.

**4. Casos con ID y trazabilidad**
- Cada caso lleva ID, requisito, severidad, prioridad, pasos, esperado y prohibido; al menos un chequeo que pueda fallar (un "no crashea" genérico solo vale para eso).
- Los guiones o recorridos de QA reutilizables **no se marcan** como hechos: un tilde sin fecha no dice cuándo fue cierto. El resultado vive en el informe fechado. Un hallazgo sin pasos ni medición no es accionable: es una opinión.
- Todo requisito tiene caso; todo comando, pantalla o endpoint nuevo llega con el suyo. La matriz requisito→caso se **genera**, no se edita a mano; un requisito sin caso se declara hueco.
- Un fallo se repite varias veces antes de clasificarlo (determinista o intermitente) y se descarta interferencia de otra sesión.

**5. Criterios de entrada y salida por fase** (plantilla)

| Fase | Entrada | Salida |
|---|---|---|
| Smoke | compila y arranca | 100% de casos smoke pasan; si no, se corta y se reporta |
| Regresión | smoke verde | 0 fallos graves abiertos; los menores listados con repro |
| Exploratorio | objetivo escrito y semilla registrada | notas y hallazgos con plantilla; lo no explorado, listado |
| Oráculos | oráculos importables | todos pasan y la autoprueba de mutación falla como debe |
| Fase completa | las anteriores | informe con "no verificable" explícito |

Cumplir una salida significa "sin fallos observados en lo probado", no "listo" ([[usuario-declara-listo]]).

**6. Cobertura honesta**
- Una cobertura alta no es garantía. Todo informe tiene la sección **LO QUE NO PUDE PROBAR** con su motivo (hardware, sesión, cuota, entorno real, lo que depende de la vista); nunca "probablemente funciona".
- Declarar cuántos casos posibles hay (todas las combinaciones), cuántos se generaron y cuántos se ejecutaron; pares y límites antes que fuerza bruta.
- Distinguir defecto confirmado, riesgo potencial y sospecha; no inventar vulnerabilidades ni dar por superada una prueba no ejecutada.
- Solo entorno de demostración y solo lectura salvo autorización; nunca datos de producción ni secretos reales (claves falsas evidentes).

## Ejemplos
- No: "300 tests pasan y el botón responde, QA hecho."
- Sí: "QA aparte, 42 casos (C-001…C-042), 41 pasan, 1 falla con repro y semilla 7731. Mutación probada: invertí `<=` en el límite y el caso C-017 cayó. No pude probar: impresión física, dispositivo táctil."
- No: `assert total(x) == total(x)`.
- Sí: esperado con aritmética exacta, derivado en un comentario y fijado como literal.

## Qué se ajusta por proyecto
- Carpeta, formato e identificadores de casos, matriz y informes; herramienta de simulación/fuzzing y cómo se pasa la semilla.
- Comando para el robot de cierre y para la fase de oráculos; anchos de pantalla y roles a probar.
- Tabla concreta de fases con sus comandos y umbrales de severidad.
- Qué es "entorno de demostración", qué queda siempre sin verificar (hardware, dispositivos) y qué módulos exigen verificación numérica.
