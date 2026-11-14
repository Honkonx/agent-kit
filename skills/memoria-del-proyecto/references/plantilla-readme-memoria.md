# Memoria del proyecto

Contexto **durable** del proyecto para cualquier sesión, máquina o herramienta. Es un índice de contexto: enlaza a la fuente (documento o código) y no la duplica. Lo leído aquí se verifica antes de usarlo como hecho.

| Archivo | Qué contiene | Cuándo leerlo |
|---|---|---|
| `PROJECT_STATE.md` | Estado vigente y el bloque único `Para retomar` | siempre, al empezar |
| `decisiones.md` | Decisiones con fecha, motivo y estado | al tocar algo ya decidido |
| `lecciones.md` | Correcciones y fallas recurrentes | antes de repetir un tipo de tarea |
| `preferencias.md` | Cómo prefiere trabajar el usuario aquí | al empezar |

**Reglas:** nada de secretos ni datos personales innecesarios; la fecha y el estado van dentro de cada entrada; no se reescribe el pasado (se marca `superada por`); tamaño acotado (el detalle va a `docs/`).
Verificación: `python <skill memoria-del-proyecto>/scripts/verificar_memoria.py .memory`.
