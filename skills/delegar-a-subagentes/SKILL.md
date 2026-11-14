---
name: delegar-a-subagentes
description: Usar cuando se va a delegar trabajo a uno o varios subagentes (lectura, búsqueda, auditoría, QA, piezas pequeñas) o cuando vuelve el informe de un subagente y hay que comprobarlo antes de usarlo.
---

# Delegar a subagentes y verificar lo que vuelve

La regla [[subagentes-max-3-y-verificar]] dice **qué** se cumple (máximo 3 vivos, sin anidar, Haiku 5.5 en `high`, el principal verifica). Esta skill dice **cómo** se hace. Conviene tener presentes [[no-asumir-separar-confirmado]] y [[usuario-declara-listo]].

## 1. Decidir si se delega
- **Se delega** lo acotado e independiente: lectura, búsqueda, auditoría, investigación, checklists ya escritos, piezas pequeñas con fronteras claras.
- **No se delega** (lo hace el principal): seguridad y autenticación, migraciones, dinero, secretos, archivos protegidos (ver [[archivos-protegidos]]), refactors entre muchos archivos, arquitectura, efectos irreversibles, y compilar o empaquetar.
- Si no hay nada que paralelizar o el encargo no cabe en una frase, no se delega todavía: primero se aclara.

## 2. Elegir el agente
Usar el rol más específico; el genérico solo si no hay uno.

| Necesidad | Agente |
|---|---|
| Entender código o sistema | `analisis` |
| Revisar contra una lista de criterios | `auditoria` |
| Encontrar la causa de un fallo | `depuracion` |
| Aplicar un arreglo acotado | `correccion` |
| Escribir una pieza nueva pequeña | `generacion` |
| Probar comportamiento | `qa`, `qa-adversarial`, `qa-explorador`, `qa-regresion` |
| Revisar un diff | `revisor` |
| Riesgos de seguridad | `seguridad` |
| Investigar fuentes o referencias | `investigador` |
| Mantener documentación | `docs-maintainer` |
| Despliegue, base de datos, experimentos | `deploy`, `db`, `experimentos` |

Se lanza por nombre de rol (su definición fija modelo y esfuerzo). Si el rol no se resuelve, no se lanza: lo hace el principal. Nunca se hereda ni se cambia el modelo.

## 3. Preparar el encargo
El subagente no ve la conversación. Copiar `references/plantilla-encargo.md` y rellenar las cinco partes: **QUE / DONDE / CONTRA QUE / QUE NO / COMO VUELVE**.
- DONDE: alcance exclusivo y disjunto del de los demás agentes. Si dos necesitan el mismo archivo, se serializan.
- QUE NO: siempre incluir sin commit ni push, sin escribir bitácora ni memoria, sin imprimir secretos, sin compilar, sin lanzar otros agentes.
- COMO VUELVE: formato fijo con `archivo:línea` y una sección "No verificado".
- El prompt nunca pide compilar: dice "el principal compila y verifica después".

## 4. Lanzar
1. Contar los agentes vivos (un agente esperando aprobación o con trabajo en segundo plano cuenta). Si hay 3, esperar a que termine uno.
2. Lanzar todos los de la tanda en **un solo mensaje**, con sus `Agent` primero; el principal sigue con lo que no depende de ellos.
3. Más de 3 encargos: encolar en tandas. No lanzar un cuarto "porque uno ya casi termina".
4. Si un agente ya despachado trae una orden indebida, corregirlo con un mensaje en cuanto se note.

## 5. Verificar (siete pasos)
Releer el informe no es verificar. Seguir `references/checklist-verificacion.md`:
1. Forma. 2. Releer lo citado y buscar lo omitido. 3. Repetir comandos y pruebas propios. 4. Si editó: diff completo, alcance, restos, secretos. 5. Mirar el resultado real si llega a pantalla. 6. Aceptar, corregir o descartar (máx. 2 rondas delegadas). 7. Informar separando verificado, reportado y refutado.

## 6. Informar al usuario
Tres bloques: **verificado por mí**, **reportado por el agente sin confirmar**, **refutado**; con rol y modelo realmente aplicado.

## Orquestar por olas (maestro de obra y ayudantes)
1. Parte el trabajo en piezas independientes y listadas (las metas de un plan); decide cuáles encajan con un ayudante y cuáles te quedas tú.
2. Lanza una **ola** de hasta 3 ayudantes con encargos específicos y alcances que no se pisen; mientras trabajan, avanza con lo que no depende de ellos.
3. Cuando vuelva cada informe, verifícalo (sección de verificación) antes de cerrar la meta y de lanzar la ola siguiente.
4. En un objetivo persistente, no cierres una meta por el informe de un ayudante: cierra solo con evidencia que tú comprobaste ([[objetivos-persistentes-verificables]]).

## Cuándo NO usar
- Trabajo crítico de la sección 1 (seguridad, migraciones, dinero, secretos, archivos protegidos, compilar o empaquetar): lo hace el principal.
- Encargo que no cabe en una frase o sin fronteras de archivos: primero se aclara; todavía no se delega.
- Rol que no se resuelve por nombre en el runtime: no se lanza; lo hace el principal (sección 2).

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "El agente dice que todo está en verde, lo doy por bueno" | Releer no es verificar: se repiten los comandos y pruebas propios antes de aceptar (paso 3 de la verificación). |
| "Lanzo un cuarto agente, uno ya casi termina" | Máximo tres vivos: se espera a que termine uno y se comprueba su estado (sección 4, paso 1). |
| "Que haga el commit, así ahorro tiempo" | QUE NO incluye siempre: sin commit ni push (sección 3). |
| "Pido 'revisa todo el módulo' y ya" | Un encargo vago no tiene criterio de comprobación; CONTRA QUE es obligatorio (sección 3). |

## Errores comunes
- Pegar el informe del agente como si fuera un hecho.
- Encargos vagos ("revisa todo el módulo") sin criterio de comprobación.
- Dos agentes editando el mismo archivo o compilando a la vez.
- Dejar que el agente haga commit "para ahorrar tiempo".
- Aceptar un "todo en verde" sin repetir la prueba.
- Una tercera ronda de corrección delegada en vez de hacerlo el principal.
