---
name: patrones-de-orquestacion
description: Usar cuando se diseña una tarea nueva de un orquestador multi-agente, al escalar de una tarea secuencial a varias, o al decidir cómo debe fallar y reintentar un subagente.
---

# Patrones de orquestación multi-agente

> Complementa la skill de diseño de agentes, si el proyecto la tiene (Supervisor/Swarm/Hierarchical/Pipeline), y `agent-harness-evals`. Límites de delegación en la regla `subagentes-max-3-y-verificar`; independencia de la revisión en `qa-independiente-y-oraculos`.

Partir de lo que el orquestador hace realmente hoy (comprobarlo en el código): no asumir orquestación multi-tarea que no exista.

## Los 7 patrones
1. **Pipeline**: pasos secuenciales, cada uno depende del anterior (descarga, cálculo, puntuación, reporte). Riesgo: una etapa lenta bloquea todo; no usarlo para tareas independientes.
2. **Fan-out/Fan-in**: una tarea se reparte en N sub-tareas independientes en paralelo; los resultados se agrupan y un worker que falla se degrada (resultado neutro u omitido) sin abortar el resto. Útil para escalar de un elemento a N (símbolos, cuentas, archivos).
3. **Expert Pool**: expertos heterogéneos (otro rol u otro proveedor de IA) evalúan el mismo input en paralelo; un voto o selección elige o combina. No confundir con Fan-out: aquí los workers difieren por diseño.
4. **Producer-Reviewer**: un agente produce (código, análisis, propuesta de configuración) y otro, nunca el mismo en el mismo turno, lo revisa antes de aceptarlo. Variante: dos productores enfrentados y un revisor que resuelve.
5. **Supervisor**: un coordinador delega en especialistas y agrega resultados; cuello de botella intencional para mantener coherencia.
6. **Hierarchical**: varias capas de supervisores; solo si realmente hay un "supervisor de supervisores".
7. **Handoff**: un agente cede el control total, sin retorno, a otro más especializado cuando detecta que está fuera de su alcance.

## Cómo elegir
1. ¿Sub-tareas dependientes y en orden? Pipeline.
2. ¿Independientes y una puede fallar sin tumbar el resto? Fan-out/Fan-in.
3. ¿Heterogéneas, evaluando lo mismo desde ángulos distintos? Expert Pool.
4. ¿Uno propone y otro debe aprobar? Producer-Reviewer.
5. ¿Coordinador central que agrega especialistas? Supervisor (Hierarchical si hay más de un nivel).
6. ¿Cesión total sin retorno? Handoff.

Si una tarea combina patrones (p. ej. Fan-out seguido de Producer-Reviewer sobre el agregado), nombrarlo en el diseño y en el comentario donde se registra la tarea; no dejarlo implícito.

## Ejemplo de Fan-out/Fan-in (TypeScript)
`Promise.allSettled` da la semántica de "un fallo individual no aborta":
```typescript
async function fanOutFanIn<T>(
  tareas: Array<() => Promise<T>>,
  degradarA: (error: unknown) => T,
): Promise<T[]> {
  const resultados = await Promise.allSettled(tareas.map(t => t()));
  return resultados.map(r => r.status === "fulfilled" ? r.value : degradarA(r.reason));
}
```

## Protocolo de fallo de tolerancia cero
Máximo 2 reintentos automáticos por sub-tarea. Al tercer fallo pasa a estado `Blocked` y exige confirmación humana: nunca reintento indefinido ni degradación silenciosa a "ignorar y seguir". Al tercer error repetido el problema es sistémico: se aplica `documentar-fallas` (a la tercera se automatiza o se investiga la causa).
```typescript
const MAX_REINTENTOS = 2;

async function ejecutarConProtocolo(tarea: () => Promise<unknown>, nombre: string) {
  for (let intentos = 0; ; intentos++) {
    try {
      return await tarea();
    } catch (e) {
      if (intentos >= MAX_REINTENTOS) {
        // Registrar la tarea como Blocked y notificar; esperar confirmación humana.
        throw new TareaBloqueadaError(nombre, e);
      }
    }
  }
}
```
