---
name: detectar-piezas-repetidas
description: Usar cuando se cierra una ronda o se lee la memoria del proyecto y hay que descubrir qué procesos, fallas o instrucciones se repiten y merecen convertirse en una skill, regla o agente propios del proyecto, o cuando el usuario pregunta qué conviene automatizar o convertir en pieza (algo que hago siempre igual, otra vez lo mismo, ya es la tercera vez).
---

# Detectar piezas repetidas

La regla [[lo-repetido-se-vuelve-pieza]] dice **qué** se cumple (detectar y proponer; crear solo con aprobación); esta skill es el **cómo** de detectar. Apoyos: [[memoria-del-proyecto]], [[documentar-fallas]], [[bitacora-humana]], [[invocar-skills-reglas-agentes]].

## 1. Reunir señales
1. Correr `python scripts/buscar_repetidos.py <carpeta-.memory> [<carpeta-docs-humano>]`. Lista las lecciones con 3 o más repeticiones sin automatizar y las frases de la bitácora que se repiten.
2. Revisar a mano el historial reciente: pasos hechos a mano más de dos veces, instrucciones que el usuario dio más de una vez, plantillas que se copian siempre.
3. Descartar lo que ya cubre una pieza existente (kit o proyecto): leer su `SKILL.md`; en ese caso la acción es **mejorar** esa pieza, no crear otra.

## 2. Clasificar cada candidata
| Señal | Pieza |
|---|---|
| Algo que siempre debe cumplirse, sin pasos | regla |
| Procedimiento con pasos, plantillas o scripts | skill |
| Rol de solo lectura con entregable fijo | agente |
| Una sola vez o con solo una opinión | nada: se anota y se espera |

## 3. Registrar y proponer
1. Anotar la candidata en `.memory/` con `Estado: provisional` (qué, cuántas veces, evidencia con enlaces).
2. Proponer **en el texto de la respuesta**: qué se repite, evidencia, pieza propuesta, nombre, área, esfuerzo. Una por pieza.
3. Esperar la aprobación. No crear nada antes. Si la rechaza, anotar `descartada` con el motivo.
4. Aprobada: pasar a la skill `crear-pieza-del-proyecto`.

## Cuándo NO usar
- Para crear la pieza: eso es `crear-pieza-del-proyecto`.
- Para una falla que ocurre una vez: se documenta ([[documentar-fallas]]); la candidata nace a la tercera.
- Para piezas del kit universal: se hacen con `skill-creator`, `crear-regla-universal` o `crear-agente-universal`.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Ya es obvio, la creo directamente" | Crear sin aprobación llena el proyecto de piezas que nadie pidió; se propone primero. |
| "Lo hice dos veces, ya es patrón" | El umbral es tres; con dos se anota y se vigila. |
| "Haré una skill nueva" (cuando ya hay una parecida) | Se mejora la existente; dos piezas casi iguales divergen. |
| "Lo dijo una vez, es regla" | Una instrucción dicha una vez va a preferencias de la memoria, no a una regla. |

## Errores comunes
- Proponer sin evidencia (sin decir dónde y cuántas veces se repitió).
- Mezclar propuestas: el usuario debe poder aprobar una y rechazar otra.
- Olvidar registrar lo descartado y volver a proponerlo.

## Verificación
- Cada candidata tiene evidencia con enlace y número de repeticiones.
- `buscar_repetidos.py` corre sin error sobre `.memory/`.
- Ninguna pieza se creó sin una aprobación del usuario citable (bitácora o decisión).
