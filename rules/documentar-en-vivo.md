# Se documenta en el momento, no al final de la tanda

> Aplica a: todo proyecto. Relacionadas: [[bitacora-humana]], [[cierre-de-ronda]], [[continuidad-multi-maquina]], [[verificacion-empirica]].

Cada hallazgo, decisión o resultado se escribe **cuando aparece**, y en listas largas el archivo de progreso se actualiza **después de cada ítem**, antes de pasar al siguiente.

## Por qué
Una sesión larga que documenta al final pierde justo lo que más valía: el número exacto, el mensaje de error textual, la hipótesis descartada. Si la sesión se corta o el contexto se compacta, no queda forma de saber qué se probó y qué no. Un archivo de progreso creado al inicio y no actualizado **miente**: es peor que no tenerlo.

## Cómo se aplica
- **Qué se escribe en el momento:**
  - un bug: qué se esperaba, qué pasó, con el número o texto exacto (`"SUBTOTAL $3.271"`, no "el subtotal estaba mal");
  - una decisión del usuario: su frase textual, la fecha y qué se decidió;
  - una anomalía de un sistema externo: se avisa al usuario en el momento, no en el resumen final;
  - una verificación: contra qué se verificó, con `archivo:línea` o comando.
- **Listas largas** (módulos, bugs, plataformas, documentos): antes de pasar al ítem N+1, el ítem N ya está registrado con su estado real.
- **Estados permitidos:** `pendiente`, `en curso`, `bloqueado`, `verificado`, `descartado`. "Hecho" no significa "archivo creado" ni "documentación leída": solo `verificado` con evidencia.
- **Checkpoint mínimo por ítem:** alcance, estado, evidencia, fecha y siguiente acción. Si cambia el alcance, anotar la razón y revisar los ítems afectados.
- **Hallazgo técnico confirmado → también a la memoria persistente del proyecto** (si la tiene), en el momento, no solo a un documento temático. Memoria y bitácora son lo que una sesión nueva busca primero.
- **Estado provisional:** si se guarda algo no confirmado, se marca `provisional`; nunca como verdad duradera.
- **Agentes en paralelo:** cada uno edita **solo su fila o sección**, o devuelve un parche para que el hilo principal lo fusione y verifique. Nadie reescribe el archivo completo (pisaría lo de otro).
- **Commits:** pueden agruparse por lotes razonables. Lo que no se agrupa es el archivo de progreso: refleja el estado real en todo momento.
- **Ronda de solo lectura:** no autoriza escribir para cumplir esta regla. El progreso va en el informe de la ronda y se propone persistirlo cuando haya luz verde.
- **Chequeo antes de cerrar una respuesta con una prueba, un hallazgo o una decisión:** ¿ya quedó escrito? ¿está en memoria o solo en un documento técnico? Si falta algo, no se cierra.

## Al cerrar
El cierre ([[cierre-de-ronda]]) **recoge y ordena** lo ya escrito. Si al cerrar hay que reconstruir de memoria lo que pasó hace dos horas, la regla no se cumplió.

## Qué no exige
No pide un archivo completo por cada intercambio trivial ("sí, entendido"). El umbral es: *¿hay algo aquí que una sesión futura necesitaría poder encontrar?*

## Qué se ajusta por proyecto
- Dónde viven el archivo de progreso, la memoria persistente y su réplica por herramienta.
- Qué nombre llevan los estados si el proyecto usa otros equivalentes.
