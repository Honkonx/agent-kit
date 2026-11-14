# 🧰 agent-kit

Mi kit de **skills, reglas y agentes** para asistentes de programación con IA. Lo uso en la mayoría de mis proyectos.

> 💡 Es **mi estilo de trabajo**: puede que a ti no te encaje tal cual. Úsalo como punto de partida y adapta lo que haga falta.

## 📦 Qué hay

| | Carpeta | Qué es |
|---|---|---|
| 🧩 | [`skills/`](skills/) | Procedimientos paso a paso que la IA aplica cuando la tarea lo pide |
| 📏 | [`rules/`](rules/) | Lo que siempre debe cumplirse en un proyecto |
| 🤖 | [`agents/`](agents/) | Ayudantes con un rol fijo y un entregable definido |
| ⚙️ | [`settings/`](settings/settings.json) | Ajustes recomendados de Claude Code (modelo de los subagentes, permisos y atribución de commits) |

📚 El índice con enlaces a cada pieza está en [`RESUMEN.md`](RESUMEN.md).

## 🚀 Cómo usarlo

1. Clona el repositorio.
2. Abre [`RESUMEN.md`](RESUMEN.md) y elige solo lo que tu proyecto necesite (o pídele a tu IA que lo lea y te proponga qué copiar).
3. Copia esas piezas a la carpeta de tu herramienta (por ejemplo `.claude/skills/`, `.claude/rules/` y `.claude/agents/`) y **lee cada pieza antes de usarla**.

## ⚠️ Conviene saber

- 🇪🇸 Están escritas en español.
- 🧠 Los agentes siguen el formato de Claude Code (campos `model`, `effort`, `tools`); en otra herramienta habrá que adaptarlos.
- ✏️ Son texto: léelas, recórtalas y ajústalas a tu forma de trabajar.

## 📄 Licencia

[MIT](LICENSE)
