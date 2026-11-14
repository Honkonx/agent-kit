---
name: inicio-de-sesion
description: Usar cuando se arranca una sesión de trabajo real en un proyecto (sobre todo si se trabaja desde más de una máquina o herramienta), al migrar de máquina o usuario, o cuando algo "no cuadra" con lo que se creía del repo.
---

# Inicio de sesión: comprobar antes de confiar

La regla [[continuidad-multi-maquina]] dice **qué** se cumple; esta skill dice **cómo** arrancar. Se apoya en [[verificacion-empirica]], [[bitacora-humana]] y [[secretos]]. No aplica a preguntas puntuales.

## 1. Correr el chequeo mecánico
```
python scripts/chequeo_inicio.py <carpeta-del-proyecto>
```
Solo lee: ejecuta `git status --porcelain`, `git fetch --dry-run`, cuenta commits adelante/atrás y busca rutas absolutas con usuario en configs y docs. Si la carpeta no es un repo git, lo dice y sigue con la búsqueda de rutas. Salida 0 sin alertas, 1 con alertas.

## 2. Interpretar el estado del repo
1. **Limpio y al día**: seguir.
2. **Detrás del remoto**: actualizar (`git pull --ff-only`) antes de confiar en el contenido.
3. **Cambios locales sin commit**: leer qué son; no son tuyos hasta comprobarlo.
4. **Adelante y atrás (diverge) o resultado inesperado**: **parar**. Entender con `git log --oneline --graph` y `git merge-base --is-ancestor` antes de cualquier `pull`, `merge` o `reset`. Nunca `reset --hard` ni `checkout .` para "resolver" la sorpresa.
5. Confirmar la rama: `git branch --show-current`. Una rama de excepción no se fusiona a la principal sin que el usuario lo pida.

## 3. Leer el contexto que vive en el repo
- Última bitácora (el `humanoN.md` de mayor número en `docs/humano/`) y el bloque de estado para retomar.
- La memoria del proyecto: `.memory/` (`README.md`, `PROJECT_STATE.md` con el bloque `Para retomar`, `decisiones.md`, `lecciones.md`; ver la skill `memoria-del-proyecto`). Es pista, no hecho: se verifica contra el código antes de usarla. La memoria personal de una herramienta no está sincronizada con otra.
- Releer cualquier archivo que se vaya a citar como vigente: no confiar en lo recordado.

## 4. Qué no asumir
- Que el entorno remoto (servidor, dispositivo) corre lo mismo que el repo: preguntar qué versión corre realmente.
- Que no hay trabajo sin subir en otra máquina: no es detectable desde aquí; no afirmarlo.
- Que algo que desapareció debe restaurarse: preguntar, pudo ser una baja deliberada.
- Que una limitación de la máquina (cuota de CI, herramienta colgada) es un bug del proyecto: anotar la causa real y en qué máquina aplica.
- Que las copias espejo de reglas o memoria están iguales: si divergen, reconciliar antes de seguir.

## 5. Rutas de usuario hardcodeadas
Si el chequeo lista rutas con nombre de usuario o de máquina:
1. Sustituir por variable de entorno (`%USERPROFILE%`, `$HOME`, una variable del proyecto con valor por defecto) o ruta relativa al proyecto.
2. Comprobar que las rutas resultantes existen en la máquina actual.
3. Si algo estaba roto, dejar nota fechada: qué se rompió y desde cuándo.
Los falsos positivos (ejemplos en docs que explican el patrón) se ignoran, pero se miran uno a uno.

## 6. Cerrar el arranque
Decir en una línea: rama, adelante/atrás, cambios locales, última bitácora leída y alertas. Recién entonces empezar a trabajar.

## Cuándo NO usar
- En una pregunta puntual o una consulta sin trabajo sobre el repo: el chequeo es para sesiones de trabajo real.
- Para resolver una divergencia del repo: esta skill manda parar y entender; el arreglo es otra decisión.
- Dentro de un subagente: no ve el estado compartido; el arranque lo hace el hilo principal.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Acabo de trabajar aquí, el repo no cambió" | Otra máquina o herramienta pudo avanzar el repo; se comprueba con `git fetch`. |
| "Está detrás del remoto, hago `reset --hard` y listo" | Un resultado inesperado se entiende con `git log` antes de tocar nada; nunca `reset --hard` ni `checkout .`. |
| "El arreglo está en el repo, entonces corre en producción" | El entorno remoto puede estar parcheado a mano; se pregunta qué versión corre. |
| "La ruta con mi usuario funciona en esta máquina" | En otra máquina o usuario rompe sin avisar; se sustituye por variable o ruta relativa. |

## Errores comunes
- Editar con el repo detrás del remoto.
- Resolver una divergencia con `reset --hard`.
- Creer que el arreglo está en producción porque está en el repo.
- Ignorar una ruta con usuario porque "en esta máquina funciona".

## Verificación
- El resumen de arranque dice rama, adelante/atrás, cambios locales, última bitácora leída y alertas (sección 6).
- Se corrió `git fetch` y la rama coincide con la esperada (`git branch --show-current`).
- La bitácora leída es el `humanoN.md` de mayor número y la memoria se leyó de `.memory/` (y se verificó antes de usarla como hecho).
- Ninguna ruta con usuario o máquina quedó sin tratar, o está anotada como falso positivo.
