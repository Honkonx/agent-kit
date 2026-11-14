# Toda falla se escribe con su dato exacto; la que vuelve se automatiza

> Aplica a: todo proyecto. Reglas relacionadas: [[verificacion-empirica]], [[documentar-en-vivo]], [[docs-organizacion-y-fechada]].

Toda falla se documenta, por pequeña que sea, con el número y el mensaje exactos, no con un adjetivo. Si la misma clase de falla vuelve, se anota que volvió y a la tercera vez se automatiza.

## Por qué
La falla chica de hoy es el diagnóstico de mañana: un error que parecía culpa de un tercero lo causaba un reinicio propio, y costó horas porque nadie anotó la hora. Sin registro, la misma falla se "arregla con más cuidado" una y otra vez.

## Cómo se aplica
- **Concreta**: mensaje de error textual (entre comillas o bloque de código), dónde (archivo:línea), cuándo y contra qué se verificó. Un error parafraseado no se puede buscar después.
- **El síntoma es lo que se buscará en seis meses**, no el arreglo: no basta "se corrigió un bug", ni dejarlo solo en el mensaje de commit si es de las que vuelven.
- **Entorno**: si la falla solo aparece en uno (otra base de datos, navegador, versión, plan de un servicio, contenedor vs. local), el entorno es parte del hallazgo. Si las pruebas pasan y el entorno real falla, el defecto está en el entorno.
- **Recurrente**: se documenta que volvió, en una tabla `cuándo | dónde | qué`. **A la tercera vez se automatiza** (prueba, script, comprobación de build o hook), no se repite el arreglo manual.
- **Señal de alarma**: una nota que corrige otra nota. No se escribe una tercera; se busca la causa o se automatiza.
- **Cierre honesto**: un arreglo sin causa entendida se escribe así y queda abierto; "causa probable" sin verificar se dice como tal. Se anotan también las fallas propias: una prueba que pasaba por casualidad, un "OK" que no verificaba nada.
- **Dónde va**: el arreglo en el registro de cambios; lo pendiente en la lista de pendientes; el documento del área si existe; la tabla de recurrentes. Los informes fechados no se corrigen después, salvo la tabla viva (ver [[docs-organizacion-y-fechada]]).

## Ejemplos
- No: "el subtotal estaba mal" / "se corrigió un bug en el cobro".
- Sí: "`SUBTOTAL $3.271` cuando debía ser $2.749 (`servicio.py:88`, verificado contra base temporal)."
- No: tercer arreglo manual del mismo olvido.
- Sí: tabla con las tres fechas y una prueba nueva que lo detecta.

## Qué se ajusta por proyecto
- Ruta del registro de cambios, lista de pendientes y tabla de fallas recurrentes.
- Entornos que el proyecto distingue y dónde se prueba cada uno.
- Qué mecanismo automatiza una recurrencia (suite, prueba de navegador, hook).
