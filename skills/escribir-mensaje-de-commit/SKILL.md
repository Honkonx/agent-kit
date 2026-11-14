---
name: escribir-mensaje-de-commit
description: Usar cuando se va a escribir el mensaje de un commit o la descripción de un pull request (por orden del usuario), para que sea técnico y directo sobre lo que cambió y no lleve enlaces, correos ni líneas de sesión; también al revisar mensajes ya escritos o al configurar la herramienta para que no los añada.
---

# Escribir el mensaje de un commit

La regla [[commits-tecnicos-sin-enlaces]] dice **qué** debe cumplir el mensaje; esta skill es el **cómo**. Solo se hace commit cuando el usuario lo ordena ([[publicar-solo-con-orden]]).

## 1. Mirar qué entra
`git status` y `git diff --staged`. El mensaje describe solo lo que está en el diff, no la conversación.

## 2. Escribir el mensaje
- **Asunto** (una línea, máx. 72 caracteres, sin punto final): verbo en imperativo + qué y dónde. Ejemplo: `Corrige el redondeo del subtotal en servicio_cobro`.
- **Cuerpo** (si hace falta, tras una línea en blanco): por qué cambió, qué comportamiento cambia, cómo se verificó (comando y resultado), límites conocidos. Datos exactos, no adjetivos.
- **Nada más.** Sin enlaces (ni de sesión, chat, PR o documentación), sin correos, sin "Generated with…", sin emojis, sin rutas de usuario ni secretos.
- Un commit, un propósito. Si el diff mezcla dos, se divide.

## 3. Comprobar antes de confirmar
Guardar el mensaje en un archivo y correr:
`python <ruta-de-la-skill>/scripts/validar_mensaje_commit.py mensaje.txt`
Con `--permitir-coautor` admite solo la línea `Co-Authored-By: <nombre> <noreply@anthropic.com>`, si el proyecto decidió conservarla. Si falla, se corrige y se repite. Sale con 0 solo si no hay problemas.

## 4. Que la herramienta no lo añada sola
Las instrucciones por texto no bastan: una herramienta puede añadir líneas por su cuenta. En Claude Code la configuración `attribution` (válida en cualquier archivo de ajustes) lo controla: `commit: ""` quita el trailer de co-autor, `pr: ""` quita la línea de las descripciones y `sessionUrl: false` quita el enlace `Claude-Session` de los commits hechos desde sesiones en la nube o remotas. Cambiar un archivo de ajustes lo decide el usuario; esta skill propone el cambio, no lo aplica.
Como red de seguridad en el repositorio, el mismo script sirve de hook `commit-msg` de git (`python <ruta>/validar_mensaje_commit.py "$1"`); instalarlo también es decisión del usuario.

## 5. Mensajes ya publicados con enlaces
`python <ruta>/validar_mensaje_commit.py --log 50` solo informa cuáles commits tienen problemas. Reescribir el historial (`rebase`, `filter-repo`) y el `push --force` son destructivos: exigen orden aparte del usuario y, si el commit ya está en un remoto público, el enlace ya pudo copiarse.

## Cuándo NO usar
- Cuando el usuario escribe el mensaje exacto que quiere: se usa tal cual (se le avisa si lleva un enlace o un correo).
- Para el changelog o las notas de versión: eso es `changelog-generator`.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El enlace de la sesión da contexto" | El historial es público y permanente; el contexto va en el cuerpo, con datos. |
| "Esa línea la añade la herramienta, no yo" | Aun así se comprueba y se quita, o se configura la herramienta para que no la ponga. |
| "Un asunto largo dice más" | Lo que no cabe en 72 caracteres va en el cuerpo. |

## Errores comunes
- Pegar el resumen de la conversación como mensaje.
- Dejar "Co-Authored-By" con un correo personal.
- Corregir un mensaje ya subido con `--force` sin orden.

## Verificación
- El validador sale con 0 sobre el mensaje final.
- El asunto cabe en 72 caracteres y describe un cambio presente en el diff.
