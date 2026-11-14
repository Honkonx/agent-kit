# Un objetivo que la IA persigue sin supervisión lleva plan, fin medible, tope y verificación propia

> Aplica a: todo proyecto y toda herramienta con un objetivo persistente (por ejemplo `/goal` en Claude Code y en Codex) o con una tarea larga sin supervisión. Reglas relacionadas: [[pedidos-sin-ambiguedad]], [[planes-con-casillas]], [[usuario-declara-listo]], [[subagentes-max-3-y-verificar]], [[verificacion-empirica]], [[seguridad-despliegue-y-datos]], [[archivos-protegidos]], [[secretos]].

Un objetivo persistente se lanza solo después de tener el pedido aclarado, el plan escrito y el prompt preparado. Su condición de término es un **estado medible** cuya comprobación se **muestra en la conversación**, y lleva un **tope**. Que la condición se dé por cumplida no equivale a "listo".

## Por qué
Quien decide que un objetivo persistente terminó puede ser un modelo aparte que solo ve lo que se mostró en la conversación, o el propio agente que trabaja. Con una condición vaga ("que funcione") aprueba sin prueba o no termina nunca, y sin tope el gasto no tiene límite. La documentación de Claude Code dice que su evaluador no ejecuta comandos ni lee archivos, y no documenta un tope configurable de turnos ni de costo.

## Cómo se aplica
- **Antes de lanzar:** diagnóstico del proyecto y del objetivo (el objetivo debe encajar y no chocar con pendientes que lo bloquean), pedido aclarado ([[pedidos-sin-ambiguedad]]), plan con casillas ([[planes-con-casillas]]) y prompt guardado; las skills `evaluar-proyecto-y-objetivo`, `aclarar-pedido`, `plan-con-casillas`, `crear-prompt-para-ia` y `preparar-goal` son el cómo.
- **La condición de término** tiene: un estado final medible, la comprobación exacta (comando o prueba) con su salida visible en la conversación, restricciones que no deben cambiar, y una cláusula de **tope** (turnos, tiempo o tokens, según lo que admita la herramienta).
- **No se usa** cuando no hay salida verificable, cuando la decisión es del usuario, ni sobre producción, datos reales o dinero: esas acciones conservan su autorización específica ([[seguridad-despliegue-y-datos]]). Tampoco amplía permisos: sin supervisión se usa el modo de permisos más estricto que permita el trabajo, y los archivos protegidos y los secretos siguen siéndolo ([[archivos-protegidos]], [[secretos]]).
- **Mientras corre:** el plan se actualiza al cerrar cada meta; el orquestador reparte lo acotado entre ayudantes (máximo 3 vivos) y verifica lo que devuelven ([[subagentes-max-3-y-verificar]]).
- **Si se atasca** (varios turnos sin avance o el mismo error repetido), se detiene y reporta lo intentado en lugar de insistir.
- **Al terminar:** el hilo principal repite la comprobación con sus propios comandos y informa lo verificado y lo no verificado; el producto "listo" lo declara el usuario ([[usuario-declara-listo]]).
- **El gasto se revisa:** una herramienta sin tope duro obliga a la cláusula escrita y a mirar el consumo.

## Ejemplos
- No: `/goal terminar la migración` y dejarlo correr toda la noche.
- Sí: "Termina cuando `python -m pytest` salga con 0 y el resultado se vea aquí, sin tocar `docs/`; o tras 25 turnos".

## Qué se ajusta por proyecto
- La herramienta y su tope disponible (claves de configuración, variables o solo la cláusula escrita).
- Las comprobaciones concretas del proyecto (pruebas, linter, construcción) y el modo de permisos para trabajo desatendido.
- Qué acciones nunca se hacen en un objetivo persistente (despliegue, migraciones, publicación).
