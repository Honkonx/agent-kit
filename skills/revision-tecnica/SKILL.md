---
name: revision-tecnica
description: Usar cuando se pide auditar de punta a punta (no un diff) un módulo o área en seguridad, arquitectura o rendimiento, revisar un RFC/ADR/propuesta ya escrita, generar un diagrama ER, puntuar la preparación para producción o diseñar reintentos, timeouts y circuit breakers para una integración externa.
---

# revision-tecnica

> Pasadas profundas y puntuales, con categorías fijas, severidad y confianza, e informe con formato. No sustituye el control rápido de cada tarea (una revisión de calidad de código), la guía para construir de forma segura (una skill de desarrollo seguro, si el proyecto la tiene) ni el Dockerfile y el CI (guía de despliegue del proyecto, si la tiene); tampoco la presión previa de un plan antes de que exista código (`metodologia-dev`). La revisión es **solo lectura**: reporta, no corrige. La corrección la hace el hilo principal o el agente `correccion` tras la luz verde ([[leer-y-responder-cada-mensaje]]). Se puede delegar en los agentes `seguridad`, `auditoria` y `revisor` (máximo 3; el principal verifica cada hallazgo: [[subagentes-max-3-y-verificar]]). Cada hallazgo cita un `archivo:línea` abierto en esta ronda y separa lo confirmado de lo inferido ([[no-asumir-separar-confirmado]]).

Cada hallazgo lleva: archivo, líneas, categoría, **severidad** y **confianza**. Un mismo patrón repetido en muchos sitios es **un** hallazgo sistémico con todas sus ubicaciones. Nunca se descarta un hallazgo solo por tener confianza baja: se anota qué lo volvería falso positivo. El informe termina con la sección de lo no verificado.

## 1. Seguridad estructurada
Recorrer las 10 categorías, marcando "no aplica" solo si es genuinamente cierto: inyección (SQL, NoSQL o de comandos), **control de acceso roto** (autenticar no es autorizar; que el código "parezca" protegido no basta), XSS, SSRF, deserialización insegura, mal uso de criptografía (hashes débiles para contraseñas, IV o sal fijos, `random` en vez de `secrets`), secretos en el código ([[secretos]]), path traversal (`../`, zip-slip al extraer), mass assignment (cuerpo ligado a un modelo sin lista de campos permitidos) y CSRF (solo con autenticación por cookie).
- Severidad: Critical = remoto, sin autenticación y de alto impacto; High = requiere alguna precondición; Medium = radio acotado; Low = defensa en profundidad.
- Confianza: High = se trazó el flujo completo; Medium = el patrón se ve mal pero no se confirmó; Low = por precaución.
- Fuera de alcance: CVEs de dependencias (usar el auditor del gestor de paquetes; no se deduce del código).

## 2. Revisión de RFC, ADR o propuesta
Sobre un documento ya escrito. Detectar si sigue una plantilla (RFC, ADR o PRFAQ) o es libre; no penalizar secciones de una plantilla que nunca dijo seguir. Evaluar por dimensión, saltando la que no aplique (con motivo): completitud, ambigüedad (juzgar cada frase vaga en su contexto), riesgo (seguridad, pérdida de datos, radio de impacto, migración), factibilidad, alcance (metas y no metas), costo frente a valor, impacto en los interesados y testeabilidad. Si hay un diagrama o imagen: "diagrama no analizado, verificar a mano".

Veredicto, uno de tres: **Not Ready** (hay Blocking) · **Ready with Revisions** (sin Blocking, hay Should-Fix) · **Ready to Approve** (solo Nice-to-Have o preguntas). Cada hallazgo indica qué está mal, por qué importa y una **propuesta concreta**.

## 3. Diagrama ER
Fuente por orden de preferencia (indicar cuál se usó): modelos del ORM (clases, relaciones, claves foráneas); migraciones si los modelos no reflejan la base real; introspección de una base **local** o temporal (`.schema`). Nunca conectar a una base de producción sin que el usuario dé la conexión y lo autorice ([[seguridad-despliegue-y-datos]]).

Salida: bloque ` ```mermaid ` con `erDiagram` (ver la skill `diagrams`). Los campos JSON o array van como un solo campo `json`, sin aplanarlos. Notación de pata de gallo: FK requerida `||--o{`, opcional `|o--o{`, muchos a muchos `}o--o{`. Con más de ~40 entidades, agrupar por dominio real y decir que el agrupamiento es heurístico.

## 4. Arquitectura
Sobre el código completo o un subárbol: (1) **dependencias circulares** (confianza siempre High); (2) **violaciones de capas**, solo si el proyecto declaró esa separación; (3) **acoplamiento y cohesión** (módulo con fan-in o fan-out inusual, un `utils` enorme del que depende todo); (4) **desviación de un patrón declarado**, solo si el proyecto lo declaró. Nunca juzgar contra un patrón que nadie pidió. Severidad según el impacto en la mantenibilidad: Critical = ya causó un bug real o obliga a rodeos; High = frenará los cambios cercanos; Medium = olor real, no urgente; Low = estilo.

## 5. Rendimiento (estático, no medido)
Se enmarca como "este patrón degrada a escala", nunca como "esto tarda 400 ms". Para medir, ver [[verificacion-empirica]] y la skill de optimización de rendimiento. Siete categorías: N+1; complejidad algorítmica (bucles anidados sin tope realista); paginación o límite faltante; I/O bloqueante en rutas asíncronas; trabajo redundante dentro de bucles; caché faltante; cliente o conexión creados por petición en vez de reutilizar uno con pool. Severidad según el impacto a escala realista de producción.

## 6. Checklist pre-producción
Se reporta **por categoría**, con hallazgos y severidad, sin un veredicto único. Aparte, una lista corta de quick-wins (menos de 5 minutos de arreglo y mayor impacto).
- **Seguridad**: toda ruta que modifica datos exige autenticación y autorización; límite de intentos en el login; clave de firma fuerte solo en el entorno; sin trazas en las respuestas de error; CORS limitado a orígenes conocidos; cabeceras de seguridad.
- **Errores**: sin `except: pass` en rutas críticas; toda llamada saliente con timeout explícito; degradación elegante en lo no crítico.
- **Observabilidad**: logging estructurado, ID de correlación en los errores, endpoint de salud sin autenticación.
- **Despliegue**: configuración sensible desde variables de entorno; sin `DEBUG` ni `localhost` fijos; migraciones nuevas revisadas por bloqueos en tablas grandes ([[seguridad-despliegue-y-datos]]).
- **Base de datos**: pool de conexiones; sin `SELECT *` en producción; índices en las FK consultadas; dinero en tipo exacto y nunca en coma flotante.

## 7. Taxonomía de errores y circuit breakers
Clasificar **cada** error antes de escribir su manejo:

| Categoría | Respuesta | ¿Reintentar? | Ejemplos |
|---|---|---|---|
| Transitorio | reintento con backoff | sí | timeout de red, 503, conexión reseteada, 429 |
| Permanente | falla inmediata | nunca | 400, 401, 404, validación |
| Parcial | degradar con gracia | opcional | caché caída, analítica, correo |
| Fatal | caída rápida | nunca | configuración faltante, estado corrupto, disco lleno |

- **Retry**: `delay = min(base * 2^intento + jitter, max_delay)`; nunca lineal (provoca una avalancha al recuperarse el servicio). No reintentar 4xx (salvo 429) ni peticiones no idempotentes sin clave de idempotencia (un cobro reintentado puede cobrar doble). Siempre `max_retries` (3-5), `max_delay` (30-60 s) y timeout en la llamada base.
- **Circuit breaker** por servicio externo: Closed (cuenta fallas) → Open tras `fail_max` (corta y usa el fallback) → Half-Open tras `recovery_timeout` (una sonda: si tiene éxito cierra; si falla, vuelve a abrir). Los errores Permanentes no cuentan como falla del servicio. Siempre con fallback (caché, cola o respuesta degradada).
- **Logging**: cada error indica qué, dónde, cuándo, quién y qué tan grave; `expected` = warning sin traza, `unexpected` = error con traza, `critical` = alerta. La traza va al log, **nunca** a la respuesta de la API.
- **Capturar en los bordes**: dejar propagar desde servicios y repositorios; capturar y transformar en el manejador de la capa exterior.

## Informe
Hallazgos ordenados por severidad, cada uno con evidencia y propuesta; lo no verificado; siguiente paso propuesto. Si se guarda, va fechado ([[docs-organizacion-y-fechada]]); sin declarar nada "listo" ([[usuario-declara-listo]]).

## Cuándo NO usar
- Un diff o una tarea normal: sirve el control rápido de calidad de código y la revisión del Dockerfile o CI (guía de despliegue del proyecto, si la tiene), no esta pasada profunda (ver encabezado).
- Una propuesta que aún no tiene código: eso es la presión de `metodologia-dev`, no una revisión de código (ver encabezado).
- Un CVE de dependencias: está fuera de alcance; se usa el auditor del gestor de paquetes (sección 1).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es un módulo pequeño, no hace falta recorrer las 10 categorías" | La sección 1 pide recorrerlas todas; "no aplica" solo si es genuinamente cierto. |
| "El código parece protegido, con la autenticación basta" | Autenticar no es autorizar: el control de acceso roto se revisa flujo por flujo (sección 1). |
| "Un patrón repetido en tres sitios son tres hallazgos" | Un patrón repetido en muchos sitios es un único hallazgo sistémico con todas las ubicaciones. |

## Errores comunes
- Confundir "no aplica" con "no revisado": cada categoría de seguridad lleva veredicto o motivo (sección 1).
- Juzgar la arquitectura contra un patrón que el proyecto nunca declaró; solo se reportan desviaciones de un patrón declarado (sección 4).
- Escribir "esto tarda 400 ms": el rendimiento es estático y se enmarca como "este patrón degrada a escala" (sección 5).
- Dar un veredicto único en el checklist pre-producción: se reporta por categoría, con los quick-wins aparte (sección 6).

## Verificación
- Cada hallazgo cita `archivo:línea` abierto en esta ronda y separa lo confirmado de lo inferido (encabezado).
- El diagrama ER indica la fuente usada (modelos, migraciones o `.schema` sobre una base local) y sale como bloque `erDiagram` (sección 3).
- Se recorren las 10 categorías de la sección 1 y las 7 de la sección 5; cada "no aplica" lleva su motivo.
