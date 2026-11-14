---
name: auditoria-adversarial
description: Usar cuando se pida auditar un CLI o sistema completo, probar cada opción, permutación o variable, intentar romperlo o buscar qué falla, antes de declarar confiable un módulo o tras un cambio grande.
---

# Auditoría exhaustiva y adversarial

Objetivo: **no demostrar que funciona, sino bajo qué condiciones deja de funcionar, por qué y cómo evitarlo.** Nunca se declara que algo funciona porque la inspección estática no halló nada.
Antes, leer las reglas `qa-independiente-y-oraculos` y `verificacion-empirica` y, si hay terminal y el proyecto tiene una guía de QA de terminal, esa. Agentes disponibles: `qa-adversarial` (ejecuta), `auditoria` (revisa) y `qa-regresion`.

## 1. Cobertura (qué se examina)
Variables, parámetros, argumentos y configuración; combinaciones y permutaciones de orden; escenarios normales, extremos, hipotéticos e inesperados; casos límite y adversariales; estados y transiciones; interacciones entre módulos; dependencias externas (red, servicios, IA); concurrencia; errores y recuperación; invariantes de negocio (lo que nunca debe pasar, p. ej. "una sola salida de escrituras: intención, validación, ejecutor").

## 2. Herramientas (usar las que el proyecto ya tenga; crear las que falten)
| Necesidad | Herramienta típica |
|---|---|
| Entradas hostiles, valores límite, pares con semilla | generador propio (textos hostiles, límites, pairwise) |
| Fuzzing con propiedades del motor/núcleo | script con `--semilla` y `--n` |
| Fuzzing de la capa de terminal (parseo, ajuste de línea, legibilidad) | tests de propiedades del CLI |
| Permutaciones por pares en el terminal real | arnés de terminal real (ver la guía de QA de terminal del proyecto, si la tiene) |
| Cada comando/subcomando, chat largo, sesiones, teclado | suite de comandos |
| **Matriz de cobertura** (¿algún comando sin probar?) | test que compara el registro real de comandos con los casos + lista de exclusiones con motivo; un comando nuevo sin ninguno hace fallar la suite |
| Variantes sistemáticas por comando (sin args, hostil, unicode, ruta, args de más, mayúsculas, largo) | política por comando: los que cambian estado solo reciben variantes inocuas |

## 2b. Suite total de comandos
Cuando se pide "probar la terminal / cada comando / cada opción": se prueba **todo** el registro real (comandos, subcomandos, menús, opciones, combinaciones de argumentos, permutaciones y escenarios de punta a punta, con y sin color) y se verifica el **propósito** (que el comando haga aquello para lo que fue creado, contra una verdad de terreno independiente), no solo formato ni robustez. Un comando sin comprobación de propósito es una **brecha** declarada, nunca un "ok".
Orden: guardián de cobertura, propósito en entorno temporal, casos con oráculo, variantes, permutaciones, **caos**, matriz.
**Caos**: romper a propósito (motor roto, datos corruptos, dependencia caída, entrada hostil, conducta humana desordenada, concurrencia) y registrar qué se rompe, por qué, qué pasa y si se recupera.

## 3. Método (en este orden)
1. **Mapear**: componente, entradas, salidas, invariantes y dependencias. Leer el código, no solo la documentación.
2. **Particiones de equivalencia + valores límite**: justo fuera, borde, justo dentro.
3. **Pares** cuando el producto cartesiano es grande; declarar casos generados y ejecutados.
4. **Propiedades** (nunca lanza, esquema estable, determinista, idempotente, "solo lectura no cambia estado", "lo válido se conserva", "lo inválido da un error accionable"). **Una propiedad que no pueda fallar no cuenta**: probarla reintroduciendo el defecto (mutación) y restaurar comparando con `cmp`.
5. **Fuzzing con semilla registrada**: cada fallo se reproduce con la semilla.
6. **Ejecutar de verdad** el camino real; reproducir 3 veces antes de clasificar.
7. **Corregir solo lo confirmado**, con prueba de regresión y mutación; repetir la auditoría del área.

## 4. Informe (plantilla por hallazgo)
ID (`F-xx` fuzzing, `P-xx` permutaciones, `H-xx` humano) · componente · descripción · condiciones · pasos de reproducción (semilla) · esperado · obtenido · evidencia (archivo:línea, salida) · severidad · probabilidad · impacto · causa raíz (si se pudo) · solución recomendada · **estado de validación de la corrección** (qué prueba lo cubre y qué mutación lo detecta).
Distinguir siempre **defecto confirmado**, **riesgo potencial** y **sospecha**. Listar **lo no cubierto** y por qué.

## 5. Restricciones
No inventar errores. No declarar superada una prueba no ejecutada. No tocar datos de producción ni cuentas reales (solo entornos de prueba y solo lectura salvo autorización). Si eres QA, no edites el código fuente: reporta con repro. No imprimir secretos (`secretos`). No dar la auditoría por terminada mientras queden áreas críticas sin analizar: se declaran. El "listo" lo declara el usuario (`usuario-declara-listo`).

## Cuándo NO usar
- Un cambio puntual ya escrito o un solo camino feliz: basta la escalera de [[verificacion-empirica]]; esta skill exige mapear todo el componente (§3, paso 1).
- Solo revisar código o documentación sin ejecutarlo: se delega en el agente `auditoria`, porque esta skill exige ejecutar de verdad (paso 6).
- La parte visual o de teclas de una terminal real: va a la guía de QA de terminal del proyecto (si la tiene) y al agente `qa-explorador`; aquí solo se invoca para las permutaciones por pares (§2).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "No hace falta ejecutarlo: la inspección estática no encontró nada." | Nunca se declara que algo funciona porque la inspección estática no halló nada; hay que ejecutar el camino real (paso 6). |
| "Ese comando solo cambia estado, no le hago variantes hostiles." | Los que cambian estado reciben solo variantes inocuas (§2): se prueban, sin efectos destructivos. |
| "La propiedad pasa en todos los casos, así que está bien probada." | Una propiedad que no pueda fallar no cuenta: se reintroduce el defecto a propósito y la prueba debe caer (paso 4). |

## Errores comunes
- Declarar la auditoría terminada con áreas críticas sin analizar, en lugar de listarlas como tales (§5).
- Fuzzing sin semilla registrada: el fallo no se puede reproducir y no sirve como hallazgo (paso 5).
- Corregir un hallazgo antes de reproducirlo tres veces y clasificarlo (paso 6).
- Añadir un comando nuevo sin entrada en la matriz de cobertura: la suite debe fallar si falta (§2).

## Verificación
- La matriz de cobertura compara el registro real de comandos con los casos y las exclusiones con motivo (§2).
- Cada propiedad probada con mutación: el defecto reintroducido hace caer la prueba, y la restauración se confirma con `cmp` contra el original (paso 4).
- Cada hallazgo se reproduce 3 veces con `--semilla` y `--n` registrados, y el informe incluye el estado de validación de la corrección (paso 6 y §4).
