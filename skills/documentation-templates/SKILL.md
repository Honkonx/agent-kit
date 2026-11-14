---
name: documentation-templates
description: "Usar cuando se redacta o revisa documentación: README, referencia de API, comentarios de código, changelog, registros de decisiones de arquitectura (ADR) o documentación pensada para agentes de IA. Ofrece plantillas y pautas de estructura para cada tipo de documento."
---

# Documentation Templates

> Templates and structure rules for the most common document types.

---

## 1. README Structure

### Essential Sections (in priority order)

| Section | Purpose |
|---------|---------|
| **Title + One-liner** | What is this? |
| **Quick Start** | Running in under 5 min |
| **Features** | What can I do? |
| **Configuration** | How to customize |
| **API Reference** | Link to the detailed docs |
| **Contributing** | How to help |
| **License** | Legal |

### README Template

```markdown
# Project Name

Brief one-line description.

## Quick Start

[Minimum steps to run]

## Features

- Feature 1
- Feature 2

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |

## Documentation

- API Reference
- Architecture

## License

MIT
```

---

## 2. API Documentation Structure

### Per-Endpoint Template

```markdown
## GET /users/:id

Get a user by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

**Response:**
- 200: User object
- 404: User not found

**Example:**
[Request and response example]
```

---

## 3. Code Comment Guidelines

### JSDoc/TSDoc Template

```typescript
/**
 * Brief description of what the function does.
 *
 * @param paramName - Description of parameter
 * @returns Description of return value
 * @throws ErrorType - When this error occurs
 *
 * @example
 * const result = functionName(input);
 */
```

### When to Comment

| ✅ Comment | ❌ Don't Comment |
|-----------|-----------------|
| Why (business rules) | What (obvious) |
| Complex algorithms | Every line |
| Non-obvious behavior | Self-explanatory code |
| API contracts | Implementation details |

---

## 4. Changelog Template (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]
### Added
- New feature

## [1.0.0] - 2025-01-01
### Added
- Initial release
### Changed
- Updated dependency
### Fixed
- Bug fix
```

---

## 5. Architecture Decision Record (ADR)

```markdown
# ADR-001: [Title]

## Status
Accepted / Deprecated / Superseded

## Context
Why are we making this decision?

## Decision
What did we decide?

## Consequences
What are the trade-offs?
```

---

## 6. AI-Friendly Documentation (2025)

### llms.txt Template

For AI crawlers and agents:

```markdown
# Project Name
> One-line objective.

## Core Files
- [src/index.ts]: Main entry
- [src/api/]: API routes
- [docs/]: Documentation

## Key Concepts
- Concept 1: Brief explanation
- Concept 2: Brief explanation
```

### MCP-Ready Documentation

For RAG indexing:
- Clear H1-H3 hierarchy
- JSON/YAML examples for data structures
- Mermaid diagrams for flows
- Self-contained sections

---

## 7. Structure Principles

| Principle | Why |
|-----------|-----|
| **Scannable** | Headers, lists, tables |
| **Examples first** | Show, don't just tell |
| **Progressive detail** | Simple → Complex |
| **Up to date** | Outdated = misleading |

---

> **Note:** Templates are starting points. Adapt them to the needs of each project.

## When to Use
This skill applies when the task is to carry out the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly fits the scope described above.
- Do not treat the output as a replacement for validation in the real environment, testing, or expert review.
- Stop and ask for clarification when required inputs, permissions, safety boundaries or success criteria are missing.

---

## 8. Plantillas de documentos del proyecto (ejemplos a adaptar)

Complementan las genéricas de arriba; sin datos financieros reales ni secretos.

**Entrada de `docs/DECISIONES.md`:** `## AAAA-MM-DD - Título` · **Contexto** · **Decisión** (lista numerada) · **Consecuencias** (riesgos y qué queda sin verificar). Una sola fuente por decisión; marcar las propuestas como propuestas.

**Bitácora humana `docs/humano/humanoN.md`:** un archivo por cada 6–9 mensajes del usuario (`bitacora-humana.md`): encabezado con fechas y «mensajes N–M» · mensajes **literales** · interpretación · qué se hizo · límites · relacionados.

**Informe QA `docs/qa/<tema>.md`:** entorno y versión · **Build** · **Pruebas automáticas** · **QA real** (por separado) · casos y resultados · **Lo que no se pudo probar** · riesgos residuales.

**Auditoría `docs/auditorias/<tema>.md`:** pregunta y alcance · método y nivel de verificación · hallazgos con `archivo:línea` · veredictos · pendiente y no verificado.

**Investigación `docs/investigacion/<tema>.md`:** pregunta · fuentes con fecha de consulta · hechos observados frente a afirmaciones de fuentes frente a inferencias · alternativas y consecuencias para cada plataforma o componente afectado · recomendación (propuesta hasta que el usuario decida).

**Entrada de `CHANGELOG.md`:** `## Unreleased - AAAA-MM-DD (tema)` con viñetas de cambios del producto; build, pruebas y QA real se informan aparte.
