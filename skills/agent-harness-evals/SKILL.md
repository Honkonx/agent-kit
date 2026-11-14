---
name: agent-harness-evals
description: Usar cuando se diseñen evals de un agente, orquestador o subagentes, o cuando haya que decidir qué cuenta como evidencia de que "funciona" (capas de verificación, datasets dorados, holdout, métricas de trayectoria).
---

# Evals de agentes y harness: evidencia, no impresión

> Complementa `patrones-de-orquestacion` y las reglas `qa-independiente-y-oraculos.md` y `verificacion-empirica.md`.

## 1. Cadena de capas ("gauntlet"), cada una puede fallar
Pruebas, tipos, lint, cobertura de **líneas cambiadas** con un umbral que haga fallar (sin umbral solo imprime un número y sale con 0), mutación (los mutantes sobrevivientes delatan pruebas débiles) y propiedades. Antes de añadir otras herramientas, usar las que ya tenga el stack; cada dependencia nueva lleva una línea que la justifique.

## 2. El autor no se verifica a sí mismo
Quien escribió el cambio hereda su punto ciego. La verificación corre en otro agente o contexto (no en una bifurcación del mismo), con el spec y los criterios fijados **antes** y los tests congelados durante la comparación. El verificador puede terminar en estados explícitos (aprobado, rechazado, no concluyente, bloqueado), no solo en "pasó / no pasó".

## 3. Runner honesto
Un runner casero de mutación o de evals debe **demostrar que ejecutó** cada caso. Por ejemplo, dos mutantes que comparten caché de bytecode pueden contar como muertos mutantes que nunca se ejecutaron: ese defecto solo infla el puntaje, así que nunca se ve como rojo. Marcar o hashear cada variante, y fallar si la ejecución no se puede probar. Preferir la herramienta estándar.

## 4. Capacidades nuevas = revisión obligatoria
Diff de capacidades: ¿el cambio empezó a usar red, subprocess, filesystem o variables de entorno que antes no usaba? Toda capacidad nueva de **escritura sobre un sistema externo** (broker, base de datos, API de pago) pasa por un gate explícito de aprobación.

## 5. Dataset dorado, holdout y métricas
- Casos con entrada, salida o trayectoria esperada y un oráculo independiente; se separa un **holdout** que no sirve para ajustar prompts ni reglas.
- Métricas en agentes con herramientas: fundamentación (¿citó datos reales?), rechazo correcto, alucinación, trayectoria (¿herramientas correctas en un orden razonable?), costo y latencia con un límite duro fuera del agente.
- Regresión: comparar contra la corrida anterior, no solo contra un umbral fijo.
- Repetir N veces si hay azar del modelo; reportar dispersión, no una sola corrida.

## 6. Salud de la suite
Orden aleatorio por corrida, repetir los sospechosos de ser inestables (flaky), matriz de versiones si se declara soporte múltiple, y verificar que un fallo silencioso en producción deje log o métrica.

## 7. Contratos y memoria
Cada subagente declara entradas, salidas y qué puede hacer sin confirmación humana. Memoria: probar deduplicación, decaimiento y recuperación con casos dorados, no solo "guarda y lee".

## Reporte
Qué capas se corrieron, cuáles no existen todavía (decirlo), N y semilla, qué mutación o contrafactual se probó, y el peldaño de `verificacion-empirica.md`.

## Cuándo NO usar
- Código sin agentes, orquestador ni subagentes (una función o un módulo): basta el oráculo y los casos de `qa-independiente-y-oraculos.md`.
- Diseñar el agente o elegir la orquestación: eso es la skill de diseño de agentes del proyecto (si la tiene) y `patrones-de-orquestacion`; esta skill solo evalúa lo ya diseñado.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Los tests pasan y la cobertura ya es alta, no hace falta mutación" | La sección 1 pide cobertura de líneas cambiadas con umbral que haga fallar, y mutación: los sobrevivientes son tests débiles. Verde no prueba que los tests detecten fallos. |
| "Quien escribió el cambio lo verifica más rápido" | La sección 2: el autor hereda su punto ciego. La verificación corre en otro contexto, con criterios fijados antes y los tests congelados. |
| "El runner casero dio 100% de muertes, está bien" | La sección 3 exige probar que se ejecutó cada caso. Dos mutantes que comparten caché de bytecode inflan el puntaje y deben fallar, no verse en verde. |
| "Una corrida basta, el modelo es estable" | La sección 5: si hay azar del modelo, repetir N veces y reportar dispersión, no una sola cifra. |

## Errores comunes
- Umbral de cobertura que solo imprime un número y sale con 0 (sección 1).
- Ajustar prompts o reglas mirando el holdout, que debía quedar sin usar (sección 5).
- Comparar solo contra un umbral fijo y no contra la corrida anterior, así una regresión pasa sin verse (sección 5).
- Editar los tests mientras se hace la comparación, en vez de congelarlos (sección 2).

## Verificación
- Introducir a propósito un mutante o un caso que debe fallar y comprobar que el runner sale con código distinto de cero (secciones 1 y 3).
- Comprobar que el verificador corrió en otro contexto y que los criterios son anteriores a la ejecución (sección 2).
- Repetir la corrida N veces con semilla registrada y confirmar que el informe muestra dispersión (sección 5).
- Comparar las llamadas a red, subprocess, filesystem y variables de entorno contra la versión anterior del código (sección 4).
