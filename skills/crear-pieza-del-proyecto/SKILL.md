---
name: crear-pieza-del-proyecto
description: Usar cuando el usuario aprobó convertir algo que se repite en una skill, regla o agente propios del proyecto y hay que escribirla en la carpeta `.claude/` del proyecto con la plantilla, validarla, registrarla en el mapa de áreas y comprobar que se activa (crear una skill del proyecto, hacer una regla local, dejar esto como pieza propia).
---

# Crear una pieza propia del proyecto

La regla [[lo-repetido-se-vuelve-pieza]] manda detectar, proponer y crear **solo con aprobación**; esta skill es el **cómo** de crear lo aprobado. Antes: `detectar-piezas-repetidas`. Apoyos: [[invocar-skills-reglas-agentes]], [[secretos]], [[memoria-del-proyecto]], `mapa-de-areas`.

Esta skill es para piezas **locales** del proyecto (carpeta `.claude/` del proyecto). Las piezas del kit universal se hacen con `skill-creator`, `crear-regla-universal` y `crear-agente-universal`.

## 1. Comprobar la aprobación
Debe existir una aprobación del usuario **para esta pieza concreta** (cita en la bitácora o decisión en `.memory/decisiones.md`). Sin ella, no se crea: se vuelve a proponer.

## 2. Elegir y copiar la plantilla
| Pieza | Plantilla | Destino |
|---|---|---|
| Skill | `references/plantilla-skill-local.md` | `.claude/skills/<nombre>/SKILL.md` |
| Regla | `references/plantilla-regla-local.md` | `.claude/rules/<nombre>.md` |
| Agente | `references/plantilla-agente-local.md` | `.claude/agents/<nombre>.md` |

Nombre en minúsculas con guiones, igual que la carpeta (skills). Sin nombres de personas o clientes ni rutas de usuario.

## 3. Escribir con el contenido real del proceso
1. Skill: descripción que empieza por "Usar cuando…" con las frases con que el usuario lo pediría; pasos tomados de **cómo se hizo de verdad** las veces anteriores (la evidencia de la propuesta), no inventados.
2. Incluir las secciones de proceso: cuándo NO usar, excusas → realidad, errores comunes y verificación.
3. Si hay un paso mecánico que se repite, pasarlo a `scripts/` y probarlo.
4. Nada de secretos ni datos reales; lo variable por entorno se lee de configuración.

## 4. Validar
```
python scripts/validar_piezas.py <carpeta-.claude-del-proyecto> [--mapa <archivo-mapa>]
```
Comprueba nombre = carpeta, descripción "Usar cuando" y ≤ 1024, cabeceras mínimas de reglas y agentes, patrones de secretos y rutas de usuario, y (con `--mapa`) que cada pieza figure en el mapa de áreas.

## 5. Registrar y comprobar que se activa
1. Añadir la pieza al mapa de áreas del proyecto (skill `mapa-de-areas`).
2. Comprobar que la descripción queda entre las candidatas para 3 frases reales del usuario y no compite con otra (con una medición de disparo, si el proyecto la tiene).
3. Anotar en `.memory/decisiones.md`: pieza creada, fecha, aprobación, evidencia de la repetición.

## Cuándo NO usar
- Sin aprobación del usuario para esa pieza.
- Para piezas del kit universal (otras skills) o para cambiar una pieza existente (ver una skill de mejora de piezas, si el proyecto la tiene).
- Cuando lo repetido ya lo cubre una pieza existente.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es chica, la creo y aviso después" | Sin aprobación no se crea; así se llenó un proyecto de piezas que nadie pidió. |
| "La descripción la afino luego" | Una pieza que no se activa no existe; se comprueba ahora con frases reales del usuario (paso 2 de la sección 5). |
| "No hace falta registrarla en el mapa" | Lo que no está en el mapa nadie lo invoca por área. |
| "Copio los pasos de otra skill" | Los pasos salen de cómo se hizo de verdad en este proyecto. |

## Errores comunes
- Describir lo que hace la pieza en vez de **cuándo** usarla.
- Dejar texto de plantilla ("Describe…", `<…>`) sin reemplazar.
- Ruta de una máquina o un nombre real dentro de la pieza.
- Crear una regla para algo que es un procedimiento (eso es una skill).

## Verificación
- `validar_piezas.py` sale con 0.
- La pieza figura en el mapa de áreas y la descripción se comprueba con frases reales del usuario.
- La aprobación del usuario está citada y la creación anotada en la memoria.
