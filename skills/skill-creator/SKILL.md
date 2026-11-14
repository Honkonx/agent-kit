---
name: skill-creator
description: Usar cuando hay que crear una skill nueva del kit, mejorar o fusionar una existente, validarla o revisar su calidad, o cuando un flujo repetido merece convertirse en skill.
---

# Crear, validar y mantener una skill

Una skill es un paquete que enseña un procedimiento que el modelo no trae de fábrica. **La regla dice el QUÉ; la skill dice el CÓMO**: si una skill solo repite lo que ya manda una regla de `rules/`, se reduce a un enlace a ella ([[invocar-skills-reglas-agentes]]). Punto de partida: la plantilla en la skill `template-skill`.

## 1. Decidir si hace falta
- ¿Existe ya una skill, regla o agente que lo cubre? Ampliar esa antes de crear otra; fusionar duplicados.
- ¿Es un procedimiento (pasos, comandos, checklist) y no solo una norma? Si es norma, va a una regla.
- Aclarar con 2-3 ejemplos concretos de uso: qué diría el usuario para dispararla y qué debería producir.
- **Preguntas guiadas** (si el usuario no las contestó, usar el valor por defecto y declararlo, no quedarse esperando):

| Pregunta | Valor por defecto |
|---|---|
| ¿Qué frases diría el usuario para dispararla? | pedir 3 ejemplos reales; sin ellos no se escribe la descripción |
| ¿Qué entrega (archivo, informe, decisión)? | un informe corto en pantalla |
| ¿Qué regla, skill o agente cubre ya una parte? | ampliar el existente en vez de crear otro |
| ¿Es de un stack concreto? | no: universal; si sí, línea `> Módulo: <stack>` |
| ¿Necesita un script? | no; solo si hace falta determinismo o se reescribe cada vez |
| ¿Cuándo NO debe usarse? | al menos 2 casos cercanos donde parece servir y no sirve |

## 2. Estructura
```
nombre-skill/
  SKILL.md        obligatorio: frontmatter + cuerpo operativo
  references/     detalle que se lee solo si hace falta (guías, tablas, catálogos)
  scripts/        código determinista y repetible, ejecutable sin leerlo
  assets/         archivos que se usan en la salida (plantillas, iconos)
```
Carga progresiva: la descripción siempre está en contexto; el cuerpo se carga al activarse (ideal menos de 250 líneas, tope 500); `references/` y `scripts/` solo cuando se necesitan. Si el cuerpo crece, mover el detalle a `references/` y dejar punteros claros de cuándo leer cada uno.

## 3. Frontmatter
```yaml
---
name: nombre-en-kebab-case      # igual que la carpeta; minúsculas, dígitos y guiones; máx. 64
description: Usar cuando <situación que la dispara>. <Qué entrega, en una frase>.   # máx. 1024
---
```
- La `description` es lo único que el modelo ve para decidir si la usa: dice **cuándo** activarla (situaciones y frases del usuario), no resume el contenido. Un poco insistente: los modelos tienden a no usar skills que sí ayudarían.
- Sin `<` ni `>` en la descripción. Nada de nombres de proyecto, rutas de usuario ni cuentas.
- Mal: "Ayuda con seguridad de APIs." Bien: "Usar cuando se diseñan endpoints nuevos, se implementa autenticación o se revisa código que toca datos sensibles."

## 4. Escribir el cuerpo
1. Primera línea: enlace a la regla que fija el QUÉ (si existe) y, en una skill de stack, `> Módulo: <stack>. Si el proyecto no usa este stack, no se copia.`
2. Pasos numerados, en imperativo, cada uno con su salida o criterio de paso. Explicar el porqué de lo no obvio en vez de imponer con MAYÚSCULAS.
3. Valores por defecto explícitos: la skill no debe quedarse esperando datos.
4. Formato de salida cuando importa (plantilla o ejemplo entrada/salida).
5. Casos de error y qué hacer si falta una herramienta ([[actitud-autonomia]]).
6. Generalizar: que sirva para muchos casos, no solo el que la motivó. Releer con ojos frescos y recortar.
7. Referenciar solo reglas y agentes universales del kit; lo propio de un proyecto va en una regla o skill local.
8. **Skills de proceso** (las que guían un procedimiento con juicio): añadir estas cuatro secciones, cortas:
   - **Cuándo NO usar**: casos cercanos donde no aplica (evita que la skill se active de más y la acota).
   - **Excusas → realidad**: tabla de las justificaciones típicas para saltarse un paso y por qué no valen (ejemplo: "ya lo probé en mi cabeza").
   - **Errores comunes** (o señales de alarma): lo que suele salir mal.
   - **Verificación**: cómo se comprueba que la skill se aplicó bien (qué debe verse, qué comando debe dar qué).

## 5. Recursos
- `scripts/`: cuando el mismo código se reescribe cada vez o hace falta determinismo. Con `--help`, sin dependencias exóticas, sin secretos.
- `references/`: documentos grandes; si pasan de ~300 líneas, índice al inicio. Nada de archivos mayores de 300 KB ni binarios pesados.
- **Una subcarpeta solo se justifica si el `SKILL.md` la cita por nombre y dice cuándo abrirla** (las guías de Anthropic y OpenAI describen `references/`, `scripts/` y `assets/` como carga bajo demanda; un archivo que nadie nombra no se abre). Los enlaces salen del `SKILL.md` y a un solo nivel: un archivo que remite a otro se lee a medias.
- Plantillas, tablas largas y catálogos van a `references/`; lo que se ejecuta igual cada vez, a `scripts/`; el cuerpo de decisión se queda en el `SKILL.md`. Nada de ejemplos decorativos (HTML, capturas) que no cambien lo que hace la IA.
- Una sola fuente por dato: o en `SKILL.md` o en `references/`, no en ambos. `python tools/validar_kit.py --todos` avisa de los archivos que ningún `.md` de la skill cita.

## 6. Validar
`python scripts/validar_skill.py <carpeta-skill>...` comprueba nombre = carpeta, descripción que empieza por "Usar cuando", longitudes, caracteres prohibidos, nombres de proyecto o rutas de usuario, tamaños, enlaces a `references/` y `scripts/` existentes y (aviso) scripts citados por nombre que no existen en la skill. Para una skill de proceso nueva, usar `--estricto` (exige las cuatro secciones del punto 4.8; `--secciones` solo avisa). Después medir si la descripción la dispara (con una medición de disparo, si el proyecto la tiene) y probarla de verdad con un caso real ([[verificacion-empirica]]) y comparar con el camino sin la skill. Rúbrica de calidad en `references/rubrica-calidad.md`.

## 7. Mantener
- Si resulta desactualizada al usarla, se corrige en el momento.
- Skills de terceros: leerlas enteras antes de adoptarlas, escanear scripts, verificar licencia y conservarlas en su idioma; no editar la fuente ajena ([[investigacion-y-referencias]]).
- No instalar ni copiar skills sin mostrar antes la lista y el motivo ([[leer-y-responder-cada-mensaje]]).
- Lo que nadie invoca se archiva (mover, no borrar) y toda skill nueva se añade al mapa de áreas del proyecto en la misma ronda.

## Cuándo NO usar
- Para una norma de conducta sin pasos: es una **regla** (`crear-regla-universal`).
- Para crear o cambiar un agente: `crear-agente-universal`.
- Para algo que solo sirve a un proyecto o negocio: pieza local de ese proyecto, no del kit.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es corta, no necesita validarse" | Las skills cortas también llevan enlaces rotos, nombres de proyecto o descripciones que no disparan: se valida siempre. |
| "Con una buena descripción se activará sola" | Se mide con frases reales y paráfrasis; sin casos así no se sabe. |
| "La copio de otro repo, ya funciona" | Se lee entera, se revisa la licencia, se neutraliza y se reescribe con criterio propio. |

## Errores comunes
- Descripción que resume el contenido en vez de decir cuándo usar la skill.
- Una skill que repite lo que ya dice una regla (debería enlazarla).
- Citar un script que no existe, o dejar un cuerpo de más de 250 líneas sin mover el detalle a `references/`.
