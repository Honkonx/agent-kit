# Un ejemplo que da el usuario ilustra una idea: no es la lista, ni el orden, ni lo único

> Aplica a: todo proyecto. Reglas relacionadas: [[leer-y-responder-cada-mensaje]], [[pedidos-sin-ambiguedad]], [[no-asumir-separar-confirmado]].

Cuando el usuario escribe "por ejemplo", "tipo", "como", "algo así" o "ejemplo:", lo que sigue es una **muestra hipotética** de una idea más general. No es la lista completa, no marca un orden, no es lo único que hay que hacer y no se copia literalmente salvo que él lo pida. Se extrae el **criterio** que el ejemplo ilustra y se aplica a todo lo que lo cumple.

## Por qué
Un ejemplo orienta con mucha fuerza al modelo, y por eso se copia de más: la propia guía de Anthropic pide ejemplos variados "para que Claude no recoja patrones no intencionados". Si el usuario menciona "Go, Rust y Python" como ejemplo, hacerlo solo para esos tres, en ese orden, deja fuera lo que él quería incluir; y tratar un ejemplo de formato como plantilla fija repite sus palabras en todo.

## Cómo se aplica
- **Extraer el criterio:** ¿qué tienen en común los ejemplos? Eso es lo que se pide; los ejemplos solo lo muestran.
- **No limitar a lo citado:** se actúa sobre todo lo que cumple el criterio, o se dice qué se cubrió y qué quedó fuera.
- **No tomar el orden ni la cantidad** de los ejemplos como una instrucción.
- **No copiar su texto ni su forma** a lo que se escribe, salvo que el usuario diga "usa exactamente esto".
- **Si no queda claro** si es una muestra o una orden literal, se pregunta con una frase corta y una recomendación ([[pedidos-sin-ambiguedad]]).
- **Los ejemplos que escribe la IA** (en piezas, planes y respuestas) se rotulan como ejemplos, se variaron entre sí y no se presentan como la lista completa.

## Ejemplos
- No: "Dijiste Rust, Go y Python; hice esas tres skills y nada más."
- Sí: "Dijiste esos tres como ejemplo; entiendo que quieres las skills específicas de un lenguaje. ¿Cubro todas las que hay o te muestro la lista y eliges?"

## Qué se ajusta por proyecto
- Palabras o fórmulas propias del usuario con que marca un ejemplo (por ejemplo "tipo", "algo así").
