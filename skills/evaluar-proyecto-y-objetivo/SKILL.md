---
name: evaluar-proyecto-y-objetivo
description: Usar cuando hay que evaluar el estado de un proyecto y si un objetivo concreto encaja con él antes de planear o lanzar un trabajo largo: leer la memoria, los planes abiertos y las mejoras pendientes, comprobar el estado real con las comprobaciones del proyecto y devolver un diagnóstico con riesgos y una recomendación de qué incluir, qué dejar fuera y en qué orden; también cuando el usuario pide evaluar un proyecto o ver qué mejoras le faltan.
---

# Evaluar el proyecto y su objetivo

Diagnóstico **de solo lectura** que va antes de planear. Responde dos preguntas: ¿cómo está el proyecto de verdad? y ¿este objetivo encaja con él? Apoyos: [[no-asumir-separar-confirmado]] (hechos frente a suposiciones), [[verificacion-empirica]], [[niveles-de-madurez]], [[archivos-protegidos]], [[memoria-del-proyecto]], [[subagentes-max-3-y-verificar]] y las skills `inicio-de-sesion`, `estado-del-proyecto` y `delegar-a-subagentes`. Se usa como primer paso de `preparar-goal`, pero sirve sola.

## 1. Fijar qué se evalúa
Ruta del proyecto y, si lo hay, el objetivo pedido (aunque sea una frase vaga: aclararlo es el paso siguiente, no este). Si el usuario solo pidió evaluar el proyecto, no hay objetivo y se omite la parte 4.

## 2. Reunir hechos
Reparte la lectura entre **hasta 3 ayudantes** (`analisis` o `auditoria`, con encargo específico y alcances que no se pisen) o hazla tú si es pequeña. Tres frentes:
- **Estado real:** `git status` y rama, la corrida de las comprobaciones que el proyecto ya define (`estado-del-proyecto`) y las fallas abiertas. Solo se ejecuta lo que el propio proyecto declara.
- **Pendientes y planes:** `.memory/` (estado, decisiones, lecciones), metas abiertas o parciales de `docs/planes/`, y cualquier archivo de pendientes o mejoras (busca nombres como pendientes, mejoras, backlog, TODO; si no hay ninguno, **pregunta** dónde los guarda el usuario).
- **Propósito y límites:** qué es el proyecto (README o instrucciones), su nivel de madurez declarado, los archivos protegidos y lo que exige autorización (producción, datos reales, dinero).

Lo que devuelva un ayudante es una afirmación: **repite tú** al menos las comprobaciones que sostienen cada riesgo o bloqueo que vayas a reportar.

## 3. Evaluar el proyecto
Escribe una tabla corta de lo encontrado: hecho comprobado (con la salida o `archivo:línea`), inferencia (rotulada) o sin evidencia. Marca lo que **bloquea** (pruebas rotas, plan abierto con el mismo alcance, deuda que cruza el objetivo) y lo que solo **acompaña**.

## 4. Evaluar el objetivo contra el proyecto
- ¿Encaja con el propósito del proyecto y con su nivel de madurez?
- ¿Tiene una salida verificable (algo que se pueda comprobar con un comando o una prueba)?
- ¿Es del tamaño adecuado o hay que partirlo?
- ¿Choca con mejoras pendientes o con un plan abierto?
- ¿Toca archivos protegidos, producción, datos reales o dinero?

## 5. Recomendar
Dilo con una de tres palabras y su motivo: **PROCEDER** (puede pasar a aclarar y planear), **ACOTAR** (hay que reducir o reordenar antes), o **NO USAR OBJETIVO PERSISTENTE** (sin salida verificable, o decide el usuario). Después, tres listas: **incluir** (mejoras pendientes que son prerrequisito del objetivo: van como primera fase del plan), **dejar fuera** (se anotan para después) y **orden sugerido**.

## 6. Entregar
Diagnóstico en pantalla con la plantilla `references/diagnostico.md`, de 25 líneas como máximo, terminando con **lo no verificado**. En `preparar-goal` ese texto pasa al plan (sección "Diagnóstico previo") y al apartado "Contexto" del prompt. No crees un archivo aparte salvo que el usuario lo pida.

## Cuándo NO usar
- Para auditar el código a fondo: eso es `auditoria-integral` o `revision-tecnica`.
- Para decidir cómo implementar algo: eso es `spec-driven-workflow`.
- Cuando el pedido es pequeño y claro: se hace directamente.
- Para modificar el proyecto o arreglar los pendientes: esta skill solo lee y recomienda.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Ya conozco el proyecto, no hace falta mirar" | La memoria envejece y el repo pudo avanzar desde otra máquina: se comprueba el estado real. |
| "El ayudante dijo que las pruebas pasan" | Es una afirmación: repites la comprobación antes de reportarla como hecho. |
| "El objetivo está claro, sigo" | Si hay pendientes que lo bloquean o no tiene salida verificable, la recomendación es ACOTAR o no usar un objetivo persistente. |
| "Arreglo de paso los pendientes que veo" | Esta skill no modifica nada: propone qué incluir y el usuario decide. |

## Errores comunes
- Mezclar hechos con suposiciones en el diagnóstico.
- Recomendar PROCEDER sin haber comprobado el estado real.
- Dar un diagnóstico enorme: más de 25 líneas no se lee.
- Dejar fuera un pendiente que bloquea el objetivo, o meter en el objetivo uno que no tiene relación.

## Verificación
- Cada hecho del diagnóstico cita una salida de comando de esta ronda o un `archivo:línea` que se puede abrir.
- Cada bloqueo reportado se comprobó por mi cuenta, no solo por el informe de un ayudante.
- La recomendación es una de las tres palabras, con su motivo y las tres listas.
- Termina con lo no verificado y no usa "listo" para el proyecto.
