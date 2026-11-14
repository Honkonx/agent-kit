---
name: flujos-de-trabajo
description: Usar cuando el usuario pide un flujo, un paso a paso completo o "de principio a fin", o cuando la tarea tiene 4 o más pasos que mezclan responsables (asistente, usuario, servicio externo). Define, guarda y ejecuta un flujo paso a paso.
---

# Motor de flujos de trabajo

Un flujo dice **qué hacer, en qué orden y quién lo hace**; las skills de dominio dicen **cómo hacerlo bien**. Esta skill es el motor genérico: sirve para cualquier dominio. Si el flujo es un plan de trabajo con casillas que se tachan, usar `plan-con-casillas` ([[planes-con-casillas]]); un flujo es más bien una receta repetible.

## 1. Cuándo generar un flujo
| Situación | Acción |
|---|---|
| El usuario dice "flujo", "paso a paso completo" o "de principio a fin" | Generarlo directo |
| La tarea tiene 4 o más pasos y mezcla responsables, pero no se dijo "flujo" | Preguntar una vez: "Esto tiene X pasos entre lo que hago yo y lo que haces tú, ¿armo el flujo?" |
| Hay un flujo guardado que encaja | Usarlo como base y adaptarlo |
| Tarea de 1 a 3 pasos, de un solo responsable; pregunta teórica; el usuario ya sabe los pasos | No generar flujo: responder o dar instrucciones directas |

Si dice que no, ir directo a ejecutar los pasos del asistente.

## 2. Formato
```
FLUJO: <nombre descriptivo>
TIEMPO TOTAL ESTIMADO: ~X min/horas

| # | Responsable | Acción | Tiempo | Salida |
|---|---|---|---|---|
| 1 | [Asistente] | descripción | ~X min | entregable concreto |

Si falla el paso N: <cómo recuperarse>
```
Responsables: `[Asistente]` (genera el entregable), `[Usuario]` (acción manual), `[Servicio]` (API o herramienta externa), `[Automatización]` (flujo automático ya montado), `[Pendiente]` (paso aún no implementado).

Reglas de contenido:
- Cada paso tiene salida concreta (archivo, texto, enlace, comando) y tiempo estimado.
- Las herramientas van como ejemplo ("editar video con la herramienta que uses"), nunca como obligatorias.
- Recuperación ante fallos solo en pasos críticos (compilación, llamada externa, publicación), no en todos.
- Más de 8 pasos: dividir en fases (preparación, ejecución, entrega).
- Una acción que cuesta dinero, sale de la máquina o es irreversible se marca y espera confirmación ([[actitud-autonomia]], [[seguridad-despliegue-y-datos]]).

## 3. Ejecutar
1. Mostrar el flujo completo antes de empezar: el usuario ve toda la cadena.
2. Ejecutar directamente los pasos del asistente, salvo los que requieren una decisión del usuario ([[no-asumir-separar-confirmado]]).
3. Para los pasos del usuario, dar instrucciones precisas; no asumir que sabe cómo.
4. Si un paso falla, diagnosticar antes de avanzar; no saltar pasos rotos ([[verificacion-empirica]]).
5. Si un paso necesita conocimiento especializado, consultar la skill de dominio correspondiente sin que lo pida ([[invocar-skills-reglas-agentes]]).
6. Al terminar, informar qué se hizo, qué se verificó y qué queda pendiente; no declarar "listo" ([[usuario-declara-listo]]).

## 4. Guardar flujos
- Un flujo nuevo no se guarda solo: se guarda cuando el usuario dice "guárdalo".
- Se guarda en la carpeta de flujos del proyecto (un archivo propio del proyecto, por ejemplo `flujos-guardados.md`), uno por sección, con el formato de la sección 2 y una línea `Última revisión: AAAA-MM-DD`. Un flujo desactualizado se corrige cuando el usuario lo pida o al detectarlo al usarlo.
- Los flujos guardados son del proyecto, no del kit. No guardar en ellos cuentas, credenciales ni datos personales ([[secretos]]).
- Plantilla en `references/plantilla-flujo.md`.

## Cuándo NO usar
- Tarea de 1 a 3 pasos de un solo responsable, pregunta teórica o usuario que ya conoce los pasos: se responde o se dan instrucciones directas (sección 1).
- Plan de trabajo con casillas que se tachan: eso es `plan-con-casillas` ([[planes-con-casillas]]); un flujo es una receta repetible.
- Cómo hacer bien un dominio concreto: lo dice la skill de dominio; el flujo solo fija el orden y los responsables.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es obvio que quiere guardarlo, lo guardo directo" | Un flujo nuevo no se guarda solo: se guarda cuando el usuario dice "guárdalo" (sección 4). |
| "Ya sé los pasos, no hace falta mostrar el flujo entero" | Antes de empezar se muestra el flujo completo para que el usuario vea toda la cadena (sección 3, paso 1). |
| "Esa acción es rápida, la hago sin marcarla" | Si cuesta dinero, sale de la máquina o es irreversible, se marca y espera confirmación (sección 2). |
| "Si el paso falla, lo salto y sigo" | Se diagnostica antes de avanzar; no se saltan pasos rotos (sección 3, paso 4). |

## Errores comunes
- Más de 8 pasos en una sola tabla en vez de fases (preparación, ejecución, entrega) (sección 2).
- Recuperación ante fallos en todos los pasos; solo va en los críticos: compilación, llamada externa, publicación (sección 2).
- Una herramienta concreta puesta como obligatoria, cuando la skill dice que son ejemplos.
- Una fila sin salida concreta (archivo, texto, enlace o comando).

## Verificación
- La tabla tiene las columnas `# | Responsable | Acción | Tiempo | Salida` y cada fila tiene salida concreta y tiempo estimado.
- Cada paso `[Usuario]` trae instrucciones precisas, y cada `[Pendiente]` dice qué falta.
- Si se guardó, `flujos-guardados.md` tiene la línea `Última revisión: AAAA-MM-DD` del flujo y no contiene cuentas, credenciales ni datos personales.
