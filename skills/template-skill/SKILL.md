---
name: template-skill
description: Usar cuando se va a crear una skill nueva del kit y se necesita la plantilla lista para copiar (frontmatter, cuerpo, carpetas). Para el proceso completo de crear, validar y mantener, ver la skill `skill-creator`.
---

# Plantilla de skill

Proceso y criterios: skill `skill-creator`. Recordatorio central: **la regla dice el QUÉ y la skill el CÓMO**; si ya hay una regla, la skill la enlaza en vez de repetirla.

## Cómo usarla
1. Crear la carpeta `.claude/skills/<nombre-en-kebab-case>/` (el nombre es idéntico al de `name:`).
2. Copiar el bloque de abajo a `SKILL.md` y rellenarlo; borrar lo que no aplique.
3. Añadir `references/` (detalle que se lee solo si hace falta), `scripts/` (código repetible) o `assets/` (archivos de salida) únicamente si hacen falta.
4. Validar: `python validar_skill.py .claude/skills/<nombre>` (script de la skill `skill-creator`).
5. Añadir la skill al mapa de áreas del proyecto en la misma ronda ([[invocar-skills-reglas-agentes]]).

## Plantilla

````markdown
---
name: nombre-de-la-skill
description: Usar cuando <situación o frase del usuario que la dispara>. <Qué entrega, en una frase>.
---

# Título

La regla [[nombre-de-regla]] dice el QUÉ; aquí el CÓMO.
> Módulo: <stack>. Si el proyecto no usa este stack, no se copia.   (solo en skills de un stack)

## Pasos
1. <Verbo en imperativo + objeto>. Salida o criterio de paso: <...>.
2. ...

## Valores por defecto
| Parámetro | Valor por defecto |
|---|---|

## Formato de salida
<plantilla o ejemplo entrada/salida>

## Si falla o falta algo
<qué hacer: alternativa, qué preguntar una sola vez>

## Cuándo NO usar
- <caso cercano donde parece servir y no sirve>

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "<justificación típica para saltarse un paso>" | <por qué no vale> |

## Errores comunes
- <lo que suele salir mal>

## Verificación
<cómo se comprueba que se aplicó bien: qué debe verse o qué comando debe dar qué>

## Referencias
- `references/<tema>.md` - cuándo leerlo
- `scripts/<script>.py` - qué hace y cómo se llama
````

## Lista de comprobación
- [ ] `name` igual a la carpeta; descripción empieza por "Usar cuando" y no resume el contenido.
- [ ] Cuerpo corto (menos de 250 líneas); detalle en `references/`.
- [ ] Pasos con salida verificable; valores por defecto explícitos.
- [ ] Skill de proceso: tiene "Cuándo NO usar", "Excusas → realidad", "Errores comunes" y "Verificación" (`validar_skill.py --estricto`).
- [ ] Medida con una prueba de disparo (si el proyecto la tiene): casos positivos (con paráfrasis) y negativos pasan.
- [ ] Enlaza reglas y agentes universales; sin nombres de proyecto, rutas de usuario ni cuentas.
- [ ] Sin archivos mayores de 300 KB ni binarios pesados.
