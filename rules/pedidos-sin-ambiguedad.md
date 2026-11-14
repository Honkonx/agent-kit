# Un pedido grande o vago se aclara antes de ejecutarlo: objetivo, fin medible y alcance

> Aplica a: todo proyecto. Reglas relacionadas: [[leer-y-responder-cada-mensaje]], [[no-asumir-separar-confirmado]], [[planes-con-casillas]], [[usuario-declara-listo]], [[objetivos-persistentes-verificables]].

Antes de ejecutar un pedido grande, vago o que se va a ejecutar sin supervisión, se convierte en un pedido claro con seis datos: **objetivo, estado final medible, cómo se comprueba, alcance y fuera de alcance, restricciones y qué decide solo el usuario**. Lo que falta se pregunta (poco, y con una recomendación); no se supone.

## Por qué
La misma frase ("arregla esto", "déjalo listo", "como antes") significa cosas distintas para una persona y para una IA, y en un trabajo largo o desatendido un malentendido se ejecuta durante horas. En este proyecto ya ocurrió dos veces: se crearon carpetas por tipo que el usuario solo había nombrado como idea futura, y se entendió que unas categorías iban dentro de una carpeta de configuración cuando iban fuera. En ambos casos la lectura elegida no se confirmó.

## Cómo se aplica
- **Cuándo:** el pedido abarca varias metas, se va a delegar o ejecutar sin supervisión (un objetivo persistente), o admite más de una lectura que cambia el resultado. Un pedido ya claro y pequeño no se interroga.
- **Los seis datos** deben estar dichos por el usuario o confirmados por él. Lo que la IA infiere se rotula "inferido", nunca como dicho.
- **Palabras que obligan a traducir** a algo medible: "listo", "todo", "mejora", "arregla", "rápido", "simple", "bien", "como antes". La skill `aclarar-pedido` trae la pregunta que aclara cada una.
- **Antes de preguntar**, se verifica lo que se pueda averiguar en el código, los documentos o la memoria ([[no-asumir-separar-confirmado]]).
- **Preguntas:** pocas por ronda (hasta 5), la más decisiva primero, cada una con opciones y la recomendada. Si el usuario responde "lo que tú veas", la decisión se registra como suposición propia y con su motivo.
- **Confirmar antes de actuar:** una frase "Entendí: …" con los seis datos, y esperar el visto bueno cuando el trabajo es grande o irreversible.
- **Dejarlo por escrito:** el pedido aclarado queda en el plan o en el prompt que se prepare, no solo en el chat ([[planes-con-casillas]]).
- La skill `aclarar-pedido` es el cómo; el pedido aclarado alimenta a `plan-con-casillas` y a `preparar-goal`.

## Ejemplos
- No: "Mejora el rendimiento" y empezar a optimizar lo primero que salte a la vista.
- Sí: "¿Mejorar qué página, medido cómo y hasta qué número? Recomiendo la de inicio, tiempo de carga con la prueba que ya existe, meta 2 s." y, con la respuesta, escribir el fin medible.
- No: preguntar diez cosas seguidas que el código ya responde.

## Qué se ajusta por proyecto
- Las palabras ambiguas propias del dominio (términos de negocio que la gente usa con otro sentido).
- Cuántas preguntas por ronda se admiten y qué herramienta se usa para hacerlas.
- Dónde queda guardado el pedido aclarado (plan, archivo de prompt, memoria).
