# La profundidad de la calidad depende del nivel de madurez que declara el proyecto

> Aplica a: todo proyecto. Reglas relacionadas: [[verificacion-empirica]], [[secretos]], [[qa-independiente-y-oraculos]], [[planes-con-casillas]], [[cierre-de-ronda]], [[usuario-declara-listo]], [[memoria-del-proyecto]].

Cada proyecto declara en qué nivel está (**prueba de concepto**, **producto mínimo** o **producción**). El nivel decide **cuánta profundidad** se exige en pruebas, errores, seguridad, documentación, rendimiento, revisión e infraestructura. No decide **qué fases se siguen**: plan, revisión, construcción y verificación se hacen siempre; en un nivel bajo los artefactos son más ligeros, no se omiten.

## Por qué
Sin un nivel declarado, o se exige a una prueba de concepto lo que solo corresponde a producción (y no avanza), o se trata producción con la laxitud de un prototipo (y se rompe con usuarios reales). Pedir la misma profundidad en todo desperdicia esfuerzo o esconde riesgo.

## Cómo se aplica
- **El nivel lo declara el usuario**, queda escrito en un solo lugar (instrucciones del proyecto) y en la memoria con fecha ([[memoria-del-proyecto]]). El asistente no sube ni baja el nivel por su cuenta; si el trabajo parece pedir otro, lo señala y pregunta.
- **Qué cambia con el nivel** (de menor a mayor exigencia; las cifras concretas las fija cada proyecto, no esta regla):

| Preocupación | Prueba de concepto | Producto mínimo | Producción |
|---|---|---|---|
| Pruebas | comprobaciones mínimas de que corre | camino feliz y bordes críticos | cobertura definida por el proyecto, regresión permanente |
| Errores | un mensaje legible | respuestas de error básicas | errores estructurados, monitoreo y alertas |
| Seguridad | datos ficticios | autenticación y validación de entradas | revisión de seguridad completa y dependencias vigiladas |
| Documentación | cómo arrancarlo | uso básico e interfaces | documentación completa, decisiones y guías operativas |
| Rendimiento | solo si falla | medir los cuellos obvios | metas medidas y pruebas de carga |
| Revisión | opcional | revisión ligera | revisión completa y compuerta de seguridad |
| Infraestructura | solo local | integración básica y un destino | entornos separados, despliegue controlado y reproducible |

- **Lo que no baja nunca, en ningún nivel:** los secretos no se muestran ni se suben ([[secretos]]), los archivos protegidos exigen permiso, nada remoto ni sobre datos reales sin autorización, y "listo" lo declara el usuario ([[usuario-declara-listo]]).
- Todo informe y todo plan dicen el nivel contra el que se verificó ("verificado para producto mínimo"), porque un OK no significa lo mismo en cada nivel ([[verificacion-empirica]]).
- Pasar de nivel es una decisión registrada y abre un plan con casillas con lo que falta para el nivel siguiente ([[planes-con-casillas]]).

## Ejemplos
- No: exigir revisión de seguridad completa a una prueba de concepto de una tarde, o dejar sin pruebas un servicio ya usado por clientes "porque empezó como prototipo".
- Sí: "El proyecto está declarado como producto mínimo (decisión del usuario, 2026-11-13). Verificado a ese nivel: camino feliz y dos bordes críticos. Para producción faltarían pruebas de regresión y alertas."

## Qué se ajusta por proyecto
- El nivel vigente, quién lo cambia y dónde queda escrito.
- Los umbrales concretos de cada preocupación en cada nivel (por ejemplo, el criterio de cobertura).
- Qué preocupaciones propias del dominio se añaden a la tabla (dinero, datos personales, hardware).
