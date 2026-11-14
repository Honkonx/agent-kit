# Qué cambia por herramienta

Lo propio de cada herramienta vive solo aquí; el resto de las piezas del flujo es universal. **Verificado el 2026-11-13** en la documentación oficial (Claude Code: `code.claude.com/docs/en/goal.md`; Codex: referencia de configuración en `learn.chatgpt.com`). Revisa la versión instalada antes de depender de un dato.

| Aspecto | Claude Code | Codex | Otra IA |
|---|---|---|---|
| Comando | `/goal <condición>` (también `claude -p "/goal …"`) | `/goal <objetivo>` | no hay: se pega el prompt corto como primer mensaje |
| Quién juzga el término | un modelo pequeño aparte, tras cada turno; solo ve lo que se mostró en la conversación | según terceros, el propio agente (no verificado en la documentación oficial) | el propio agente |
| Longitud de la condición | hasta 4000 caracteres | no verificado | la del prompt |
| Tope de turnos | solo una cláusula escrita en la condición ("o parar tras 20 turnos") | no hallado | cláusula escrita |
| Tope de tokens o costo | no hay clave; el estado muestra el gasto | `goals.max_goal_token_budget` en `config.toml` | cláusula escrita |
| Activar o desactivar | queda no disponible si `disableAllHooks` es `true` o hay `allowManagedHooksOnly` | `features.goals` (activado por defecto) | no aplica |
| Ver o cancelar | `/goal` (estado) y `/goal clear` | `/goal` y subcomandos (pausa, reanudar, editar: no verificados en documentación oficial) | cerrar la sesión |
| Un error de autenticación, saldo agotado o modelo no disponible | borra el objetivo | no verificado | no aplica |

Notas:
- El comando se pega en una sesión de la herramienta; esta skill no puede lanzarlo.
- En modo manual la herramienta sigue pidiendo permisos; para trabajo desatendido hace falta un modo de permisos que lo permita, y eso conviene fijarlo con cuidado ([[archivos-protegidos]]).
- Un subagente o comando en segundo plano aún en marcha aplaza la evaluación de ese turno en Claude Code.
- Detalle y fuentes: `docs/investigaciones/comando-goal.md` (en el proyecto fábrica).
