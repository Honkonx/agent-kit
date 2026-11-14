---
name: mapa-de-areas
description: Usar cuando hay que crear, actualizar o validar el mapa área a skills, reglas y agentes de un proyecto, o configurar el aviso por hook que recuerda qué invocar al tocar cada área, o cuando se añade una skill, regla o agente nuevo.
---

# Mapa de áreas y aviso por hook

Las reglas [[invocar-skills-reglas-agentes]] y [[archivos-protegidos]] dicen **qué** se cumple; esta skill dice **cómo** se construye y mantiene el mapa que las hace operativas. Apoyos: [[subagentes-max-3-y-verificar]], [[leer-y-responder-cada-mensaje]], [[cierre-de-ronda]].

## 1. Construir el mapa
1. Copia `references/plantilla-mapa-areas.json` a la ubicación que use el proyecto (un solo archivo, con dueño).
2. Lista las **áreas** reales: capa, lenguaje, plataforma, base de datos, documentación, pruebas, despliegue. Una por línea de trabajo distinta.
3. Por área rellena:
   - `patrones`: rutas o globs que la identifican.
   - `skills`: las del **dominio del proyecto primero**, luego las técnicas genéricas.
   - `reglas`: las que aplican al tocarla.
   - `agentes`: el agente dedicado (`db`, `qa`, `seguridad`, `docs-maintainer`, etc.), que debe existir en `agents/`.
   - `protegida`: `true` si toca archivos de la lista protegida (ver paso 3).
4. Un hueco (área sin skill dedicada) se anota en `huecos`, no se inventa cobertura.
5. Usa descripciones de skill que empiecen por "Usar cuando… en <área>" para que sean descubribles.

## 2. Aviso por hook
El aviso debe llegar en el momento útil: al leer el mensaje, al delegar y al editar.
1. El hook identifica el área por el patrón del archivo o el texto del mensaje.
2. Entrega el texto como **contexto adicional** para el modelo (skill, reglas y agente del área). No emite decisión de permiso: el motivo de un permiso no lo lee el modelo, y "allow" autoriza solo cada edición.
3. **Una vez por área y sesión**: guarda las áreas ya avisadas en un archivo temporal de la sesión. Repetirlo lo convierte en ruido.
4. **Nunca bloquea** (salida 0). Un fallo del hook no debe impedir trabajar.
5. Solo avisa del área tocada: no cargues material ajeno.

## 3. Archivos protegidos
1. Define la lista de protegidos en un solo lugar, con motivo y fecha ([[archivos-protegidos]]).
2. En el mapa marca las áreas que los contienen; el aviso añade "área protegida: pedir permiso explícito y fresco antes de editar".
3. El aviso informa; el permiso lo da solo el usuario.

## 4. Validar
```
python scripts/verificar_mapa.py <mapa.json> <carpeta-skills> <carpeta-reglas> <carpeta-agentes>
```
Comprueba que todo lo referenciado existe y que toda skill, regla y agente presente figura en el mapa (o en `archivadas`). Sale 1 si algo falla. Úsalo como prueba automática del proyecto.

## 5. Mantener
- Toda pieza nueva se añade al mapa **en la misma ronda** que nace.
- Lo que nadie invoca se mueve a `archivadas` (se mueve, no se borra).
- Medir de vez en cuando invocaciones por skill y delegaciones por agente; si casi todo va al genérico, revisar el mapa.
- No instales ni copies piezas nuevas sin autorización: muestra lista y motivo.

## Cuándo NO usar
- Para decidir cómo hacer el trabajo de un área: eso lo dice la skill del área; esta solo construye y valida el mapa.
- Para definir la lista de archivos protegidos: es `lista-de-protegidos`; el mapa solo marca qué áreas los contienen.
- Para piezas del kit universal: el kit tiene sus inventarios (`_INVENTARIO.md`, `_INVENTARIO_SKILLS.md`).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "La skill es obvia, no la añado al mapa" | Lo que no está en el mapa no se invoca por área; se añade en la misma ronda que nace. |
| "El aviso lo pongo en cada edición para que no se olvide" | Repetido se vuelve ruido y se ignora: una vez por área y sesión. |
| "Que el hook bloquee si falta la skill" | Un hook que bloquea impide trabajar ante cualquier fallo; el aviso informa y sale con 0. |
| "Hay un hueco, cito una skill parecida" | Un hueco se anota como hueco; inventar cobertura da falsa confianza. |

## Errores comunes
- Mapa que cita skills inexistentes o que dejó fuera las nuevas.
- Hook que se repite en cada edición o que bloquea.
- Aviso como decisión de permiso en lugar de contexto adicional.
- Delegar al agente genérico habiendo uno dedicado.
- Inventar cobertura para un hueco.

## Verificación
- `verificar_mapa.py` sale con 0: todo lo referenciado existe y toda skill, regla y agente figura en el mapa o en `archivadas`.
- El hook, probado con un archivo de cada área, entrega contexto adicional una sola vez por área y sesión y termina con salida 0.
- Las áreas con protegidos llevan el aviso de "pedir permiso explícito y fresco".
