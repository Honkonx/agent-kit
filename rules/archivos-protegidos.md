# Los archivos protegidos no se tocan sin permiso explícito y fresco

> Aplica a: todo proyecto (plantilla: cada proyecto define su lista). Reglas relacionadas: [[usuario-declara-listo]], [[no-asumir-separar-confirmado]], [[secretos]].

Un archivo o módulo de la lista de protegidos no se modifica sin permiso explícito del usuario para ese cambio puntual. Un bug real no es permiso: se reporta y se pregunta.

## Por qué
Se editó un archivo protegido "para arreglar un bug real" en una parte que parecía ajena a la lógica sensible, y el usuario lo corrigió: el criterio es si el archivo está en la lista, no si el cambio parece inocuo. Tocarlos mal puede ser caro o irreversible.

## Cómo se aplica
- **Antes de editar cualquier línea** de un archivo protegido: parar, no aplicar el cambio, reportar el hallazgo y pedir permiso.
- El permiso es **explícito y fresco**: nombra ese archivo/cambio, en esta sesión. Un "sí" de otra sesión o de otro archivo, o una orden general ("arregla todo", "audita X") que no lo nombra, no cuenta.
- No hay excepciones por tamaño o apariencia: comentarios, formato, fixes chicos, bloques que "nunca corren en el camino normal", ni cambios motivados por un bug verificado.
- Qué **sí** se puede hacer sin pedir permiso: documentación y memoria; código que no vive en el archivo protegido; módulos que el usuario nombró explícitamente como tocables o cuyo error pidió investigar (permiso válido solo para ese módulo y esa ronda).
- La lista vigente se escribe en un solo lugar y se **lee antes de editar**; no se infiere de memoria. Cuando el usuario retira o agrega algo, se actualiza con la fecha y el motivo.
- Si ya se tocó uno por error: decirlo, mostrar el cambio exacto y dejar que el usuario decida si se revierte o se conserva.
- Mientras no haya permiso, se deja el cambio propuesto (descripción o diff) sin aplicar y se continúa con lo demás.

## Ejemplos
- No: "Encontré un bug en el módulo protegido y lo corregí de paso."
- Sí: "Hallazgo en el módulo protegido X, línea N: [síntoma, evidencia]. No lo toqué. ¿Autorizas editarlo?"

## Qué se ajusta por proyecto
- La lista de archivos/módulos protegidos y el motivo de cada uno (credenciales, controles de riesgo, bases de producción, configuración de compilación, módulos que el usuario declaró intocables).
- El archivo donde vive la lista vigente y cómo se actualiza.
- Qué carpetas/archivos son siempre libres (docs, memoria).
