---
name: investigacion-web
description: "Usar cuando se investiga una librería, herramienta o API de terceros antes de integrarla, se comparan opciones, se verifica si un dato sigue vigente o cambió con la versión, o se hace un panorama de un área. Investiga desde varios ángulos en paralelo y basa cada hallazgo en fuentes citadas, con URL y fecha."
---

# investigacion-web

Investigación web en paralelo desde varios ángulos, con hallazgos respaldados por fuentes.

---

## Cuándo usar
- Investigar cómo funciona una API externa antes de integrarla (ej. cómo se hace con la REST API de una tienda en línea, OAuth2 de un marketplace, los folios/CAF del SII, Webpay Plus).
- Comparar librerías o enfoques (ej. "qué opciones hay para generar PDF de boletas en Python").
- Verificar si algo sigue vigente o cambió (ej. "¿el timbre impreso sigue siendo obligatorio para el SII?").
- Hacer un panorama de un área (ej. "qué proveedores de envío tienen API en Chile aparte de Blue Express").

**No usar para**: preguntas sobre el código del propio repositorio (leer los archivos directamente), ni para automatizar un navegador en vivo (usar una herramienta de prueba de interfaz web).

## Modos de profundidad

Si el pedido no lo indica, deducir el modo del texto:

| Modo | Cuándo | Salida |
|------|--------|--------|
| **scan** | Pregunta rápida, "¿esto existe?" | Top 3 hallazgos + URLs |
| **brief** | Pregunta de investigación estándar | Resumen sintetizado con recomendación |
| **breadth** | Mapear un espacio, "qué opciones hay" | Mapa de categorías, actores clave, huecos |
| **deep** | Crítico para una decisión, necesita verificación | Reporte completo con nivel de confianza y fuentes verificadas |

Reglas para deducir el modo: "rápido"/"¿existe?" → scan · "investiga"/"cómo se hace" → brief · "compara"/"qué opciones" → breadth · "necesito decidir"/"a fondo" → deep.

## Pipeline

1. **Revisar lo que ya se sabe** (salvo en scan): buscar en `docs/`, en el código existente y en la memoria del proyecto antes de salir a la web, para no reinvestigar lo ya documentado (si `docs/` ya tiene notas sobre una integración, se reutilizan).
2. **Planificar**: definir 1 dimensión de búsqueda (scan), 2-3 (brief), 5-8 (breadth) o 3-5 priorizadas (deep), todas distintas entre sí. Mostrar el plan antes de lanzar las búsquedas.
3. **Buscar en paralelo**: si el entorno lo permite, repartir cada dimensión entre subagentes que trabajen a la vez con búsqueda y lectura web. Cada uno debe traer extractos textuales con su URL fuente, no solo un resumen. Una dimensión siempre busca evidencia en contra (ej. "problemas conocidos de la API de X" además de "cómo usarla").
4. **Contrastar entre sí** (solo deep): cada agente revisa los hallazgos de los demás y completa los huecos.
5. **Sintetizar**: fusionar los hallazgos citando sus URLs y contrastarlos con el contexto del proyecto (ej. "esto aplica a Chile" o "esto exige HTTPS, que el proyecto ya cumple"). Scan omite este paso: se entregan los resultados de búsqueda tal cual.
6. **Verificar** (solo deep): revisar que las URLs no den 404 y que los números de versión sigan vigentes.

## Manejo de fallos

| Situación | Acción |
|-----------|--------|
| Una búsqueda no devuelve nada | Reformular y reintentar una vez; si sigue vacía, reportar el hueco |
| Un agente de búsqueda falla | Seguir con los demás y anotar la dimensión fallida |
| Todos fallan | Reportar el fallo con las consultas intentadas y sugerir alternativas |
| Una URL da 404 al verificar | Marcarla y quitarla de la recomendación si era la única fuente |

## Selección de modelo y esfuerzo
- Planificador y agentes de búsqueda: un modelo ligero con esfuerzo medio; no necesitan el más potente, pero sí buena extracción.
- Síntesis final: usar el modelo de la sesión actual; no forzar uno distinto.

## Guardar los hallazgos
Al investigar una API de terceros, guardar el hallazgo en `docs/` (nunca solo en la respuesta del chat) y también en la memoria del proyecto, siguiendo el flujo de trabajo que el proyecto tenga definido.
