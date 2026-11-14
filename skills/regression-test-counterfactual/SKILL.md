---
name: regression-test-counterfactual
description: Usar cuando se arregló un bug o un test se ve sospechosamente verde, para probar que el test de regresión realmente detecta el defecto - control known-bad mínimo, rojo por la razón correcta y vuelta a verde.
---

# Test de regresión con contrafactual

El QUÉ ("el chequeo debe poder fallar", cada defecto confirmado deja una regresión permanente) está en [[qa-independiente-y-oraculos]] y [[verificacion-empirica]]. Esta skill cubre el CÓMO. La usa el agente `qa-regresion`.

Un verde contra el fix es evidencia débil. **El mismo test debe ponerse rojo con el defecto presente, por la razón correcta, y volver a verde con el fix.**

## Pasos
1. **Afirmación** (escríbela antes de tocar nada): disparador (entrada, estado o secuencia), comportamiento malo observable, esperado, autoridad que fija lo esperado (un requisito o un incidente, independiente del test), punto de decisión y testigo (la aserción que distingue). Si lo esperado todavía es una decisión de producto, para y pregunta ([[no-asumir-separar-confirmado]]).
2. **Frontera segura:** confirma que el comando no toca bases reales, servicios externos de producción ni `.env` ([[secretos]], [[seguridad-despliegue-y-datos]]). Registra `git status` y el hash del archivo de producción y del test.
3. **Línea base:** corre el test más estrecho (filtro por nombre, sin caché) y confirma que se descubrió, se ejecutó y no se saltó ni se reintentó. Anota el comando, el estado de salida y la salida decisiva.
4. **Control known-bad:** restaura el defecto con el cambio reversible más pequeño (idealmente la decisión previa al fix, tal como fue). Valídalo **sin** el test y observa la salida mala; si solo el test lo "confirma", es circular. Congela el test durante la comparación. No pises cambios ajenos ni hagas commit del estado malo: si hay solapamiento, usa una copia o un worktree (un worktree no trae cambios sin commitear; trasládalos y verifica los hashes).
5. **Rojo correcto:** falla en el testigo, no en la compilación, la colecta o el fixture, ni en una excepción ajena; un caso vecino sin defecto sigue verde; y el fallo es estable al repetir (más veces si hay azar, concurrencia, caché o reintentos).
6. **Restaurar** el fix, volver a correr y obtener verde; confirma que no queda rastro del control.

## Si sigue verde o rojo por otra causa
Es un test roto, no un fix probado: no llega a la decisión, asevera algo cercano o tolera todo (`err == nil` ignorado, `except Exception`, `assert x is not None`), o el control no reproduce el bug. Arregla el test y repite; no declares la regresión cubierta.

## Reporte
Comando exacto, control aplicado, rojo observado y por qué es el correcto, verde restaurado y qué NO se probó. Nunca "cubierto": di en qué peldaño está.

## Cuándo NO usar
- Si el defecto no está reproducido o lo esperado todavía es una decisión de producto: no hay defecto que restaurar como control. Para y pregunta ([[no-asumir-separar-confirmado]]) (paso 1).
- Si el comando tocaría una base real, un servicio de producción o un `.env`: no se ejecuta el control; antes se busca una frontera segura ([[secretos]], [[seguridad-despliegue-y-datos]]) (paso 2).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El test ya está en verde con el fix, con eso basta" | Un verde contra el fix es evidencia débil: el mismo test debe ponerse rojo con el defecto presente (pasos 4 y 5). |
| "Es obvio que falla sin el fix, no hace falta restaurarlo" | Sin ver la salida mala del control no hay prueba; si solo el test lo confirma, es circular (paso 4). |
| "Falla, así que el test ya sirve" | Debe fallar en el testigo; un fallo por compilación, colecta o excepción ajena no prueba la regresión (paso 5). |

## Errores comunes
- Escribir la afirmación después de ver el resultado: disparador, testigo y autoridad se escriben antes de tocar nada (paso 1).
- Aplicar el control sobre un árbol con cambios ajenos o hacer commit del estado malo: usa una copia o un worktree y verifica los hashes (paso 4).
- No restaurar el control al terminar: el verde posterior no demuestra nada si el defecto sigue presente (paso 6).
- Testigo que tolera todo (`err == nil` ignorado, `except Exception`, `assert x is not None`): es un test roto, no un fix probado (sección "Si sigue verde o rojo por otra causa").

## Verificación
- Antes del control, `git status` y el hash del archivo de producción y del test quedan anotados; al final deben coincidir, salvo el cambio reversible del defecto (paso 2).
- Línea base: el test más estrecho, filtrado por nombre y sin caché, se descubre, se ejecuta y no se salta ni se reintenta; comando y estado de salida anotados (paso 3).
- Con el defecto presente, la salida muestra el fallo en la aserción del testigo y no en la colecta, el fixture ni una excepción ajena (paso 5).
- Tras restaurar el fix, el mismo comando da verde y `git status` no muestra rastro del control (paso 6).
