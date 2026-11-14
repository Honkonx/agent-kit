---
name: debugging-sistematico
description: "Usar cuando haya un bug, un test que falla, un fallo de importación o sincronización o un comportamiento inesperado, antes de proponer un fix (no después del segundo intento fallido). Incluye investigación de causa raíz en 4 fases y rastreo hacia atrás."
---

# Depuración sistemática

> La regla `verificacion-empirica` dice qué verificar; esta skill es el método para llegar a la causa. Delegar investigación al agente `depuracion` y corrección al agente `correccion`. Documentar la falla con `documentar-fallas`.

## Ley de hierro
**Ningún fix sin investigación de causa raíz primero.** Bajo presión de tiempo, adivinar y probar es más lento que investigar. Un fix puesto donde aparece el síntoma suele ser solo un parche sobre él.

## Fase 1: causa raíz
1. **Definir el fallo**: comportamiento observado exacto, esperado, pasos, entradas, versión/plataforma y si los datos son sintéticos o reales.
2. **Leer el error completo**: stack trace entero, archivo y línea.
3. **Reproducir de forma consistente**, con un fixture pequeño y anonimizado; no experimentar destructivamente sobre datos reales o de producción. Si no es reproducible, reunir más evidencia antes de adivinar.
4. **Revisar cambios recientes**: `git log`/`git diff` del área, dependencias, configuración, variables de entorno.
5. **Sistemas de varios componentes** (backend, servicio externo, base de datos, frontend, API): agregar logging temporal en cada frontera ANTES de proponer un fix, correr una vez y ver en qué capa se rompe; no asumir de qué lado está el problema.
6. **Rastrear el flujo de datos** cuando el error aparece lejos del origen (técnica abajo).

## Rastreo hacia atrás
1. Observar el síntoma tal cual se manifiesta.
2. Encontrar la causa inmediata (qué línea produce ese valor).
3. Preguntar qué la llamó y con qué argumento; seguir subiendo hasta donde se originó el valor incorrecto.
4. Arreglar en el origen, no en cada punto intermedio.
5. Si el rastreo manual no alcanza, instrumentar con logging temporal antes de la operación problemática (valores de entrada, estado, marca de tiempo) y quitarlo al resolver, sobre todo si expone datos personales o financieros (`secretos`).

## Fase 2: análisis de patrón
- Buscar un caso similar que SÍ funcione y comparar línea por línea.
- Si se implementa un patrón ya usado en el proyecto, leer la implementación de referencia completa antes de adaptarla.
- Listar TODAS las diferencias, por pequeñas que parezcan.
- Distinguir defecto de código de datos obsoletos, configuración, desajuste de esquema/versión, comportamiento de plataforma o expectativa incorrecta.

## Fase 3: hipótesis y prueba
1. Formular UNA hipótesis por escrito: "X es la causa raíz porque Y". Una sospecha no es un bug confirmado hasta que la evidencia lo respalde (`no-asumir-separar-confirmado`).
2. Probar con el cambio más pequeño que la aísle, una variable a la vez, buscando evidencia que pueda refutarla.
3. Si falló: nueva hipótesis, sin apilar un segundo cambio sobre el primero.
4. Si no se entiende algo, decirlo en vez de simular certeza.

## Fase 4: implementación
1. Crear primero un caso de reproducción (test automatizado o script puntual), antes de arreglar.
2. Un solo fix dirigido a la causa raíz, el más acotado y autorizado; refactor y fix son cambios distintos.
3. Verificar la post-condición real, no el código de salida: el test nuevo pasa, la suite no rompió nada, el síntoma original desapareció comparando contra el resultado esperado.
4. Prevenir recurrencia: dejar la regresión; en fallos persistentes registrar pasos, entorno, esperado/obtenido y verificación en el artefacto autorizado.
5. **Contar los intentos**: con menos de 3 fixes fallidos, volver a la Fase 1 con la información nueva; con 3 o más sobre el mismo síntoma es un problema de arquitectura: parar y discutirla antes de seguir parchando.

## Señales de alarma: volver a la Fase 1
"Fix rápido ahora, investigo después"; "pruebo cambiar X a ver"; "es simple, no necesito el proceso"; "es una emergencia"; dos o más intentos fallidos y a punto de probar un tercero sin cambiar de enfoque.

## Verificación
- Hay un caso de reproducción que falló antes del arreglo y pasa después.
- El fix toca solo la causa raíz y la suite completa no empeoró.
- El síntoma original desapareció comparado con el resultado esperado, no solo con el código de salida.
