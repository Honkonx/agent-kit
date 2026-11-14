# Plantilla de encargo a un subagente

Copiar, rellenar los `<marcadores>` y pegar como prompt. El subagente no ve la conversación: todo lo necesario va aquí.

```
ROL          <agente universal elegido>
QUE          <la tarea en una frase>
DONDE        <archivos o rutas; alcance exclusivo, disjunto del de los demás agentes>
CONTRA QUE   <comando, prueba o medición con la que se comprueba; criterio de éxito>
QUE NO       - No hagas commit ni push.
             - No escribas bitácora, memoria ni documentación fuera de lo pedido.
             - No imprimas secretos ni valores de credenciales.
             - No compiles ni empaquetes: el principal compila y verifica después.
             - No lances otros agentes ni subagentes: trabaja tú directamente.
               Si te queda grande, dilo y devuélvela.
             - No toques: <archivos protegidos o fuera de alcance>
COMO VUELVE  1. Archivos leídos o cambiados, con archivo:línea.
             2. Cifras y comandos ejecutados, con su salida real.
             3. Hallazgos, uno por uno, con evidencia.
             4. Sección "No verificado": lo que no pudiste comprobar y por qué.
```

## Notas de uso
- Contexto mínimo útil: <dato del proyecto sin el cual la tarea se malinterpreta>.
- Si es una auditoría, pegar la lista de criterios completa; no remitir a "los de siempre".
- Si es una investigación de referencias, exigir revisar las categorías antes de recomendar (ver la skill de auditoría de referencias, si el proyecto la tiene).
- Pruebas que el agente puede correr: solo acotadas y con directorios temporales propios y nuevos.
