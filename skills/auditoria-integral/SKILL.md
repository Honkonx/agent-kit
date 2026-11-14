---
name: auditoria-integral
description: Usar cuando se pida auditar un proyecto completo de punta a punta (backend, frontend, servicios de IA e infraestructura) y accionar los hallazgos en lugar de solo reportarlos. No sirve para un módulo puntual: para eso basta una revisión de calidad de código sobre ese archivo.
---

# Auditoría integral de un proyecto

Procedimiento para auditar el sistema completo y **accionar** los hallazgos, no solo reportarlos. Apoyos: [[subagentes-max-3-y-verificar]], [[verificacion-empirica]], [[no-asumir-separar-confirmado]], [[documentar-en-vivo]], [[memoria-del-proyecto]] y la skill `delegar-a-subagentes`.

## Por qué existe
Una auditoría general, si se improvisa, sale distinta cada vez. Fijar el procedimiento evita repetir el mismo arreglo manual y recoge una lección: **un agente puede devolver un resultado inventado o vacío** (un «en progreso», un hallazgo sin evidencia). Por eso todo resultado delegado se contrasta antes de usarse.

## Procedimiento
1. **Acotar con el usuario** si queda poco tiempo: mejor menos áreas bien hechas («hoy backend e IA, el frontend la próxima») que cuatro revisiones superficiales.
2. **Dividir por área** (backend, frontend, IA y servicios, infraestructura o despliegue si aplica) y delegar la lectura en los agentes `auditoria` o `analisis`, con un encargo específico y máximo 3 vivos. La infraestructura (tamaño de disco, procesos, configuración de despliegue) se revisa mejor con llamadas directas del hilo principal que delegada.
3. **Desconfiar de resultados sospechosos:** si un agente devuelve algo genérico, un marcador («esperando…») o algo sin evidencia concreta (línea de archivo, nombre de función, salida de un comando real), se descarta y se repite el análisis con lectura directa; no se reintenta el mismo agente esperando otro resultado.
4. **Priorizar hallazgos reales sobre preferencias de estilo:** errores de seguridad, datos que se pierden, endpoints sin autenticación, consultas N+1 reales y código muerto que confunde pesan más que nombres o formato.
5. **Separar lo que se arregla ahora** (bajo riesgo, alcance conocido) **de lo que exige decisión del usuario** (cuesta dinero, cambia comportamiento visible o es un refactor grande en el módulo más complejo). Lo segundo se propone, no se hace de paso.
6. **Verificar cada arreglo** con las comprobaciones del proyecto (linter, pruebas del área tocada, compilación); que «se ve bien» no prueba nada.
7. **Registrar el hallazgo y la acción** en la lista de pendientes del proyecto y en `.memory/` (lo durable); un hallazgo que solo queda en el chat se pierde en la siguiente sesión.
8. **Anotar lo que salió mal en el propio proceso** (por ejemplo, un agente que alucinó), no solo los hallazgos del código.

## Cuándo NO usar
- Auditar un solo módulo o archivo: basta una revisión de calidad de código sobre ese archivo.
- Una revisión de seguridad a fondo: agente `seguridad` (o una skill de auditoría de seguridad del proyecto, si la tiene).
- Cuando el usuario pidió solo un informe: se reporta y no se arregla nada ([[leer-y-responder-cada-mensaje]]).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El agente dijo que no hay problemas" | Una ausencia de hallazgos sin evidencia no es un resultado; se verifica con lectura directa. |
| "Arreglo todo de una vez" | Lo que cambia comportamiento o cuesta se separa y se pregunta. |
| "Lo dejo en el informe del chat" | Sin registro en pendientes y memoria se pierde en la siguiente sesión. |
| "Lanzo cuatro agentes a la vez" | Máximo 3 vivos; el resto en tandas. |

## Errores comunes
- Mezclar "documentar el hallazgo" con "arreglarlo ya" cuando el arreglo tiene costo real.
- Dar por bueno un resultado delegado sin repetir la comprobación.
- Reintentar el mismo agente esperando que esta vez funcione.
- Revisar infraestructura delegando a un agente sin acceso a herramientas reales.

## Verificación
- Cada hallazgo cita `archivo:línea` o la salida de un comando de esta ronda.
- Cada arreglo pasó las comprobaciones del proyecto, con la salida mostrada.
- Hallazgos y acciones quedaron en la lista de pendientes y en `.memory/`.
- El informe separa lo arreglado, lo propuesto al usuario y lo no verificado.
