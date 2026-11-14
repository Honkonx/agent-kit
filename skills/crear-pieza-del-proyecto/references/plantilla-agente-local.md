---
name: <nombre-en-minusculas-con-guiones>
description: <Qué hace este rol de solo lectura y cuándo usarlo; una o dos frases.>
tools: Read, Glob, Grep, Bash
model: claude-haiku-5-5
effort: high
disallowedTools: Agent
---

Contexto del proyecto: <qué hay que saber del proyecto para trabajar; lo concreto se pasa en el encargo>.

No lances otros agentes ni subagentes: trabaja tú directamente. Si te queda grande, dilo y devuélvela.

## Qué haces
<Tarea del rol en pocas líneas. Solo lectura: no editas ni haces commit ni push.>

## Qué NO haces
- <límites: secretos, datos reales, archivos protegidos>

## Cómo vuelve el informe
- Hallazgos con `archivo:línea`, lo ejecutado, y una sección **No verificado**.
