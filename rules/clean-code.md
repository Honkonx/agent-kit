# Código limpio: simple, claro y sin duplicar conocimiento

> Aplica a: todo proyecto. Reglas relacionadas: [[verificacion-empirica]], [[documentar-fallas]].

Aplicar DRY, KISS y YAGNI (ver abajo) donde mejoren la claridad y la corrección. Preferir nombres que expresen propósito y funciones enfocadas; los comentarios explican el porqué.

## Por qué
La duplicación hace que una regla de negocio se corrija en un sitio y siga rota en otro; las abstracciones prematuras y el código muerto añaden complejidad sin dar valor.

## Cómo se aplica
- **DRY**: un conocimiento, una representación. Extraer lógica o reglas de negocio duplicadas (bloques copiados, ramas paralelas, validaciones repetidas) a funciones, clases o constantes.
- **KISS**: la solución más simple que funcione. Más corto no es más simple: legibilidad sobre brevedad.
- **YAGNI**: no añadir funcionalidad ni capas de abstracción hasta necesitarlas. Eliminar código muerto, código comentado e imports sin usar.
- **Nombres**: sustantivos para clases, verbos para funciones, prefijo `es/tiene/puede/debe` (o su equivalente en el idioma) para booleanos; sin abreviaturas.
- **Funciones**: pequeñas, una sola responsabilidad, 0-2 parámetros (con 3 o más, agruparlos en un objeto), sin parámetros de salida (el resultado se devuelve con `return`). Sin límite rígido de líneas: ~20 es orientación, no ley.
- **Excepción nombrada**: coordinación de I/O externo con reintentos, tiempos de espera y saltos de hilo puede ser más larga cuando dividirla dispersaría pasos secuenciales acoplados sin reutilización. Es una excepción documentada, no excusa general.
- **Archivos**: si supera ~400 líneas, considerar dividirlo; suele hacer más de una cosa.
- **Comentarios**: preferir código autoexplicativo; comentar el POR QUÉ, no el QUÉ, citando la evidencia real cuando exista (error, restricción del entorno, decisión previa). Borrar los TODO al terminar la tarea.
- **Importes y datos críticos**: claridad, trazabilidad y transacciones pesan más que la brevedad. Nunca usar tipos de coma flotante para dinero; usar el modelo monetario exacto del proyecto.

## Ejemplos
- No: tres validaciones casi iguales copiadas en tres métodos; `calc(c, d, t)`; `// suma 1 a i`.
- Sí: una función `validarCliente()` reutilizada; `calcularTotal(pedido)`; `// el proveedor devuelve 200 con errores dentro del cuerpo`.

## Qué se ajusta por proyecto
- Convenciones de nombres y formato del lenguaje (ver las convenciones del stack del proyecto).
- Excepciones reconocidas al tamaño de función/archivo.
- El modelo monetario o de datos críticos y dónde está definido.
