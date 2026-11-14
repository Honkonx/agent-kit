---
name: deep-research
description: Usar cuando se pida investigar a fondo arquitectura, referencias o alternativas y entregar una recomendación con evidencia trazable.
---

# Investigación profunda

> Norma completa en la regla `investigacion-y-referencias`; para delegar, el agente `investigador`.

1. Definir pregunta, alcance, restricciones y criterio de éxito.
2. Priorizar la documentación oficial y las fuentes primarias, y verificar contra el código o el comando real de esta ronda.
3. Separar hechos observados, afirmaciones de fuentes, inferencias y decisiones (`no-asumir-separar-confirmado`).
4. Comparar ventajas, desventajas, complejidad, costo y riesgos de cada alternativa.
5. No copiar arquitecturas completas de referencias: extraer contratos, patrones y pruebas (las referencias son solo lectura).
6. Cerrar con recomendación, alternativas, incertidumbres y plan verificable, con URL y fecha de consulta por afirmación.

## Cuándo NO usar
- Una pregunta de hecho que se responde leyendo un archivo o ejecutando un comando: se contesta directamente, sin informe comparativo.
- Copiar o portar la arquitectura entera de una referencia (paso 5): aquí se extraen contratos, patrones y pruebas.
- Cómo comunicarse con una app externa ya instalada: la norma es portar el mecanismo al proyecto; si hay duda, se pregunta antes de investigar (regla `investigacion-y-referencias`).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "La documentación oficial lo dice, no hace falta abrir el código." | Paso 2: la documentación indica dónde mirar; se verifica contra el código o el comando de esta ronda antes de escribir "verificado". |
| "Esto ya está claro, lo pongo como hecho." | Paso 3: hechos observados, afirmaciones de fuentes, inferencias y decisiones van separados. |
| "Con una alternativa basta, no hace falta comparar." | Paso 4: cada alternativa se compara en ventajas, desventajas, complejidad, costo y riesgos. |
| "Copio la arquitectura del repo y ya está." | Paso 5: no se copian arquitecturas completas de referencias; se extraen contratos, patrones y pruebas. |

## Errores comunes
- Escribir "verificado" sobre algo que solo se leyó en un README o en un documento antiguo.
- Mezclar en un mismo párrafo hechos, afirmaciones de fuentes e inferencias.
- Entregar una recomendación sin alternativas ni incertidumbres declaradas.

## Verificación
- Cada afirmación externa tiene URL oficial, fecha de consulta y versión; si falta algo, se marca como no verificada.
- Cada "verificado" cita `archivo:línea` o la salida del comando de esta ronda.
- La recomendación lista las alternativas comparadas y un plan con criterio verificable.
