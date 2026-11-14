---
name: spec-miner
description: Usar cuando hay que entender un sistema heredado o sin documentación, derivar requisitos desde el código existente, dar IDs de requisito a QA, documentar un módulo sin docs o contrastar un documento contra el código real.
---

# Spec Miner: especificación por ingeniería inversa

Deriva requisitos observados a partir del código. Se mira desde dos ángulos: **arquitectura** (módulos, flujos de datos, dependencias) y **QA** (comportamiento observable, casos límite, errores).

## Reglas
1. **El código manda; la documentación se contrasta al final** ([[no-asumir-separar-confirmado]]). Cada requisito cita `archivo:línea` y lleva `Verificado AAAA-MM-DD`.
2. **Solo lectura** (leer archivos, buscar por nombre y buscar por texto): no se ejecuta código, ni tests, ni instalaciones, y no se escriben archivos salvo pedido explícito ([[leer-y-responder-cada-mensaje]]).
3. **Referencias y clones se leen, no se ejecutan.** Si el escaneo halla patrones de riesgo (`postinstall`, `eval(`/`atob(`, `EncodedCommand`, `base64 -d`, hooks de compilación), se reporta y se deja de leer ese clon ([[investigacion-y-referencias]]).
4. **Nunca se leen secretos:** no se abre ni se cita el contenido de `.env` ni de archivos de credenciales; si aparece uno, solo se anotan ruta y tipo ([[secretos]]).
5. **Archivos protegidos:** se pueden leer si hace falta, pero no se propone modificarlos sin permiso fresco; un bug real se reporta, no se corrige de paso ([[archivos-protegidos]]).
6. Si documento y código divergen, se señala; no se elige una versión en silencio.

## Flujo
1. **Alcance:** un módulo o el sistema completo; anota qué queda fuera.
2. **Explorar:** puntos de entrada, rutas y comandos, modelos, configuración, tests y manejo de errores (patrones y fases en `references/analysis-process.md` y `references/analysis-checklist.md`). *Checkpoint:* si quedan sin leer puntos de entrada, configuración o módulos núcleo, sigue explorando antes de documentar.
3. **Trazar** el flujo de punta a punta (entrada → lógica → efecto).
4. **Documentar** en formato EARS (`references/ears-format.md`), cada requisito con su ID y su cita.
5. **Marcar** incertidumbres y divergencias en una sección propia.

## Observado vs inferido
- **Observado:** el código lo hace literalmente; se cita.
- **Inferido:** se deduce de nombres, comentarios o patrones; se marca `[INFERIDO]` con su razón y no se presenta como requisito firme.
- **No verificado:** no se pudo leer ni contrastar; va a incertidumbres.

```
REQ-<AREA>-001 [OBSERVADO] When <disparador>, the system shall <acción>.
  Verificado AAAA-MM-DD contra <archivo:línea>
```

## Seguridad y errores (siempre)
Revisa la autenticación y la validación de firmas en endpoints, CORS, la validación de entrada, el manejo de errores (fallo abierto frente a cerrado) y cualquier ruta que llegue a un efecto irreversible (dinero, borrado, envío). Un fallo abierto en una ruta de efecto es una incertidumbre de prioridad alta.

## Salida
La respuesta es el lugar principal. Solo se escribe un archivo (por ejemplo, un documento del módulo en la carpeta de docs, añadido a su índice) si se pide ([[docs-organizacion-y-fechada]]). La plantilla está en `references/specification-template.md`. Sus secciones son, en orden: 1. stack y arquitectura; 2. estructura de módulos; 3. requisitos EARS con ID, cita y fecha; 4. observaciones no funcionales; 5. criterios de aceptación inferidos (`[INFERIDO]`); 6. incertidumbres y preguntas; 7. divergencias doc-código; 8. recomendaciones.

Los IDs de requisito alimentan los casos de prueba ([[qa-independiente-y-oraculos]], skill `qa-plan-y-casos`) y las especificaciones nuevas (skill `spec-driven-workflow`).

## Cierre
- [ ] Puntos de entrada y superficie (HTTP/CLI) leídos
- [ ] Modelos, base de datos y configuración leídos, sin secretos
- [ ] Manejo de errores y fallo abierto/cerrado revisados
- [ ] Rutas con efectos trazadas
- [ ] Cada requisito con cita y fecha
- [ ] Incertidumbres listadas

## Cuándo NO usar
- Para escribir una especificación nueva antes de construir: eso es `spec-driven-workflow`; aquí se extrae lo que ya existe.
- Para probar el comportamiento o ejecutar el código: la regla 2 lo prohíbe; para casos de prueba a partir de los IDs, `qa-plan-y-casos`.
- Para un clon de referencia con patrones de riesgo (`postinstall`, `eval(`, `base64 -d`): la regla 3 manda dejar de leer ese clon y reportarlo.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es solo lectura, ejecuto el módulo y veo qué sale" | Regla 2: no se ejecuta código, tests ni instalaciones. El comportamiento se deduce del código citado y las dudas van a incertidumbres. |
| "El README dice lo mismo, lo pongo como requisito" | Regla 1 y "Observado vs inferido": el código manda. El README se contrasta al final y la divergencia se señala. |
| "Ese .env me da contexto, lo leo rápido" | Regla 4: no se abre ni se cita el contenido de `.env` ni de credenciales; solo se anotan ruta y tipo. |
| "Ese fallo abierto no es prioritario" | En "Seguridad y errores (siempre)": un fallo abierto en una ruta de efecto es una incertidumbre de prioridad alta. |

## Errores comunes
- Requisito sin `archivo:línea` ni fecha `Verificado AAAA-MM-DD`.
- Un hallazgo inferido presentado como observado, sin la marca `[INFERIDO]` y su razón.
- Documentar un módulo sin leer sus puntos de entrada, su configuración o sus módulos núcleo (checkpoint de Explorar).
- Elegir en silencio una versión cuando documento y código divergen.

## Verificación
- Releer las líneas citadas de tres requisitos al azar y confirmar que dicen lo que el requisito afirma.
- Comprobar que `references/specification-template.md` tiene sus ocho secciones y que las divergencias doc-código están en la séptima.
- Marcar las casillas del Cierre solo si el paso se hizo en esta ronda.
