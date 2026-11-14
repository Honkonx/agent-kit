# El mensaje de un commit es técnico y directo: sin enlaces, correos ni líneas de sesión

> Aplica a: todo proyecto con repositorio. Reglas relacionadas: [[publicar-solo-con-orden]], [[secretos]], [[cierre-de-ronda]], [[usuario-declara-listo]].

El nombre y la descripción de un commit (y la descripción de un pull request) dicen **qué cambió y por qué**, con datos, y nada más. No llevan enlaces, correos, líneas de sesión ni texto de publicidad de la herramienta.

## Por qué
El historial de git es permanente y, en un repositorio público, lo lee cualquiera. Una herramienta de IA puede añadir por su cuenta un enlace a la sesión (`Claude-Session: https://…`) o una línea "Generated with…"; en dos repositorios públicos del usuario llegaron así enlaces a sesiones privadas. Reescribir el historial después es destructivo y no borra lo que ya se copió.

## Cómo se aplica
- **Asunto:** una línea, imperativo, qué y dónde, máx. 72 caracteres, sin punto. **Cuerpo:** por qué, qué comportamiento cambia y cómo se verificó (comando y resultado).
- **Prohibido:** URLs de cualquier tipo (sesión, chat, PR, documentación), correos, líneas `Claude-Session:` o equivalentes, "Generated with…", emojis, rutas con nombre de usuario y secretos ([[secretos]]).
- **Co-autor:** una línea `Co-Authored-By: <modelo> <noreply@anthropic.com>` es aceptable si el proyecto decide conservarla; es el único correo admitido y nunca se pone uno personal.
- **Comprobar antes de confirmar** con la skill `escribir-mensaje-de-commit` (su script falla si hay enlaces o correos). Las instrucciones por texto no bastan: se configura también la herramienta para que no los añada.
- **Ya publicado:** se informa cuáles commits tienen el problema; corregirlo reescribe el historial y exige orden aparte ([[publicar-solo-con-orden]]).
- El commit solo se hace cuando el usuario lo ordena.

## Ejemplos
- No: `Update stuff 🤖` + `Claude-Session: https://claude.ai/code/session_…`.
- Sí: `Corrige el redondeo del subtotal` + cuerpo "El subtotal daba 3271 en lugar de 2749 con descuento; se redondea al final. Verificado con la prueba de cobro: 14 pasan."

## Qué se ajusta por proyecto
- Si se conserva o no la línea de co-autor, y el formato del asunto (por ejemplo Conventional Commits).
- Cómo se configura la herramienta para no añadir atribuciones (archivo de ajustes o hook `commit-msg`).
