# Textos cortos: si necesita un párrafo para explicarse, se arregla el diseño

> Aplica a: todo proyecto (texto que lee el usuario: pantallas, mensajes, errores, bots). Reglas relacionadas: [[usuario-declara-listo]], [[leer-y-responder-cada-mensaje]].

Si una pantalla o mensaje necesita un párrafo para explicarse, está mal diseñado: se arregla el diseño, no se agrega el párrafo. Un texto de ayuda solo existe si dice algo que el control no puede decir solo.

## Por qué
Los párrafos explicativos no se leen y empujan hacia abajo lo importante. Un mensaje de error que repetía el mismo aviso decenas de veces llegó a miles de caracteres y superó la altura de la ventana: un mensaje que no se lee de un vistazo no avisa nada.

## Cómo se aplica
- Cada cosa va en su lugar, en este orden:
  - Para qué sirve un control: en su etiqueta.
  - Qué pasa al accionarlo: en el propio botón ("Imprimir las 14 etiquetas", no "Imprimir").
  - Por qué está deshabilitado: una frase corta (`title`, descripción accesible); deshabilitar con motivo, no esconder.
  - Un dato extra: debajo, en una sola línea.
  - El porqué de una decisión técnica: comentario en el código.
  - La explicación larga: en la documentación, donde alguien la buscará.
- **Tope: una línea de ayuda por control, y corta.** Si no entra, se cambia el control.
- Si el texto repite lo que ya se ve (un estado "Configurada" ya lo dice todo), se elimina.
- Mensajes de error y de bots: agrupar o limitar (p. ej. máximo 3 motivos, una línea de referencia, una de qué lo habilitaría); legibles de un vistazo.
- Descripciones en tarjetas y listas: una frase llana con un tope de caracteres definido; el detalle va en la ficha o pantalla de detalle, o tras un enlace "Más información".
- Títulos de pocas palabras; un solo mensaje por aviso o estado.
- Formatos de dato breves y uniformes (p. ej. versión como `v` + dígitos, sin rótulos ni hashes).
- No quiere decir escribir menos código: los comentarios que explican el *por qué* siguen siendo obligatorios.

## Ejemplos
- No: un párrafo bajo una sección de claves explicando para qué sirven y cómo se guardan.
- Sí: nada; la casilla dice "Configurada" o "Sin configurar".
- No: "Imprimir" con una nota de dos líneas debajo.
- Sí: botón "Imprimir las 14 etiquetas".

## Qué se ajusta por proyecto
- Tope de caracteres de descripciones y nombre de la carpeta de documentación larga.
- Formato de versión u otros datos cortos, y superficies concretas (web, móvil, bots) a las que aplica.
