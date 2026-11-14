---
name: organizar-docs
description: Usar cuando hay que crear u ordenar la carpeta docs/ de un proyecto, decidir si un documento es vigente o foto fechada, archivar documentación obsoleta, montar el índice raíz con la próxima auditoría, o registrar una falla y llevar la tabla de fallas recurrentes.
---

# Organizar la documentación y registrar fallas

Las reglas [[docs-organizacion-y-fechada]] y [[documentar-fallas]] dicen **qué** se cumple; esta skill dice **cómo**. Convive con [[documentar-en-vivo]], [[bitacora-humana]] y [[cierre-de-ronda]]. Para delegar la auditoría de docs, usar el agente `docs-maintainer`.

## 1. Clasificar cada documento
| Clase | Qué es | Qué se hace con el contenido | Nombre |
|---|---|---|---|
| **Vigente** | Describe el sistema de hoy (arquitectura, contratos, guías, requisitos) | Se corrige in situ contra el código, en la misma ronda | Sin fecha |
| **Foto fechada** | Describe un momento (bitácora, auditoría, QA, investigación, plan cerrado, changelog, decisión) | No se toca; lo nuevo va en otro documento que lo enlaza | nombre por tema; **fecha dentro** (`**Fecha:**`) |

Excepciones en una foto: reparar un enlace movido, quitar un secreto, o anteponer una nota fechada indicando contra qué se verificó el dato falso.

## 2. Crear la estructura
1. Copiar `references/plantilla-indice-docs.md` como `docs/README.md` (índice raíz).
2. Crear carpetas temáticas **solo cuando exista contenido real**, mono-tema, al nivel superior de `docs/` (máximo 2 niveles).
3. Cada carpeta lleva su `README.md` con: qué hay, qué va, qué **no** va y su tipo (vigente o foto).
4. Rellenar la **tabla de carpetas** del índice raíz (carpeta, tipo, qué va, qué no va).
5. Poner "Próxima auditoría: AAAA-MM-DD" (hoy + 3 meses, o antes si hubo una tanda grande de cambios). Las cifras que se escriban salen de un comando y llevan fecha.
6. Un único bloque de "estado para retomar", reescrito cada sesión.
7. Carpeta con más de ~5 documentos: lleva índice.

## 3. Mover, renombrar y archivar
1. Antes de archivar, buscar si algún documento vigente (plan, pendientes, reglas) lo cita como fuente activa. Si lo cita, no se mueve.
2. `git mv docs/<carpeta>/<doc>.md docs/archivo/<doc>.md`. Nunca borrar.
3. Añadir al inicio: `> Superado por: <enlace>` y la fecha.
4. En la misma ronda: corregir todas las referencias cruzadas y el índice.
5. Decisiones con estado: `vigente | propuesta | superada por …`; lo superado se marca, no se borra.

## 4. Verificar mecánicamente
```
python scripts/verificar_docs.py <carpeta-docs> [--raiz <carpeta-proyecto>]
```
Solo lee. Detecta: documentos vigentes que citan archivos inexistentes, enlaces markdown rotos y carpetas con más de 5 documentos sin índice. Trata como foto fechada lo que está en una carpeta de fotos (`planes`, `decisiones`, `investigaciones`, `auditorias`, `qa`, `humano`, `informes`, `archivo`…) o lleva la línea `**Tipo:** foto fechada` al inicio (y, por compatibilidad, un nombre que empieza por una fecha); el resto es vigente. Salida 0 sin problemas, 1 con problemas. Las fotos se excluyen por diseño.

## 5. Auditar contra el código
Tras una tanda grande de cambios o cada 3 meses: auditar los docs vigentes **contra el código**, no contra otros docs. Delegar la lectura a `docs-maintainer` o `auditoria` con el encargo de [[subagentes-max-3-y-verificar]]; el principal verifica. Actualizar "Próxima auditoría" al terminar.

## 6. Registrar una falla
1. Escribir el síntoma exacto: mensaje textual entre comillas o bloque de código, `archivo:línea`, cuándo, entorno y contra qué se verificó. Nunca "se corrigió un bug".
2. Poner el arreglo en el registro de cambios y lo pendiente en la lista de pendientes.
3. Si es de una clase que ya ocurrió: añadir una fila en la tabla de recurrentes (`references/plantilla-fallas-recurrentes.md`): cuándo | dónde | qué.
4. **A la tercera fila** de una misma clase: automatizar (prueba, script, comprobación de build o hook) y anotar cuál. No repetir el arreglo manual.
5. Alarma: una nota que corrige otra nota. No se escribe una tercera; se busca la causa o se automatiza.
6. Cierre honesto: sin causa entendida se escribe "abierto"; "causa probable" se dice como tal.
La tabla de recurrentes es la única pieza viva; los informes fechados no se corrigen después.

## Cuándo NO usar
- Para escribir el contenido técnico de un documento: esta skill decide dónde va y de qué clase es.
- Para la bitácora de mensajes del usuario (`docs/humano/`): se lleva con la skill `bitacora-humana`.
- Para corregir una foto fechada porque el hallazgo ya se arregló: se escribe un documento nuevo que la enlace.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "La auditoría vieja dice algo que ya cambió, la reescribo" | Una foto fechada dice lo que se vio ese día; lo nuevo va en otro documento que la enlaza. |
| "Creo `arquitectura_v2.md` para no tocar el original" | El vigente se edita en su sitio; un paralelo genera copias divergentes. |
| "Este documento ya no sirve, lo borro" | Nunca se borra: `git mv` a la carpeta de archivo con "Superado por …". |
| "Anoto la cifra a mano, es rápida" | Las cifras a mano envejecen; se sacan de un comando y se fechan. |
| "Cuadra con los otros docs, está auditado" | Se audita contra el código, no contra otros documentos. |

## Errores comunes
- Reescribir una auditoría vieja porque el hallazgo ya se arregló.
- Crear `arquitectura_v2.md` en vez de editar el vigente.
- Borrar un doc en vez de `git mv` al archivo.
- Cifras escritas a mano en docs vigentes.
- Carpetas "para llenar" sin contenido real.
- Auditar los docs contra otros docs en vez de contra el código.

## Verificación
- `verificar_docs.py <carpeta-docs> --raiz <proyecto>` sale con 0: sin citas a archivos inexistentes, sin enlaces rotos y sin carpetas de más de 5 documentos sin índice.
- Cada documento está en la carpeta de su tipo y tiene su fecha dentro del archivo (fotos) o `Última actualización` (vigentes).
- Tras mover o renombrar, las referencias cruzadas y el índice raíz están corregidos en la misma ronda.
- El índice raíz lleva "Próxima auditoría: AAAA-MM-DD".
