---
name: changelog-generator
description: Usar cuando se va a preparar un release, hay que actualizar el CHANGELOG, el usuario pregunta qué cambió desde la última versión, o se quiere validar que los mensajes de commit sigan Conventional Commits.
---

# Generador de changelog

Genera notas de versión verificables a partir del historial de git y sugiere el salto de versión. Documentar el cambio en la misma ronda forma parte de [[cierre-de-ronda]]. Los mensajes de commit y las etiquetas del repo público siguen `publicar-solo-con-orden`. El changelog es una foto fechada: se antepone una entrada nueva y no se reescriben las anteriores ([[docs-organizacion-y-fechada]]).

## Pasos
1. **Detectar la convención de versiones**, en este orden: la sección de versionado del archivo de instrucciones del proyecto; las etiquetas (`git tag --sort=-version:refname | head`); los encabezados del `CHANGELOG.md` existente; si no hay nada, preguntar una vez.

   | Patrón | Estilo | Salto |
   |---|---|---|
   | `v3.15.0`, `release-3.15.0` | SemVer (con o sin prefijo) | major.minor.patch |
   | `v2.1` | dos componentes | major.minor |
   | `2026.01`, `2026.01.1` | CalVer | año.mes[.patch] |
2. **Leer el changelog existente** y copiar su formato: nivel de encabezado, orden de secciones, estilo de enlaces. Si no existe, usar Keep a Changelog (`## [Unreleased]`, `## [1.2.0] - AAAA-MM-DD`).
3. **Fijar el rango**: `git describe --tags --abbrev=0` y `git log <tag>..HEAD --oneline --no-merges`. Si el rango no es válido, muestra el rango exacto en el error.
4. **Validar los commits** (opcional, pero recomendado): `python scripts/commit_linter.py --from-ref <tag> --to-ref HEAD --strict`.
5. **Generar la entrada**: `python scripts/generate_changelog.py --from-tag <tag> --to-tag HEAD --next-version <vX.Y.Z> --format markdown`. También acepta `--input archivo` o stdin, `--format json` y `--write CHANGELOG.md` para anteponer la entrada. Consulta `--help` de cada script.
6. **Revisar a mano** el texto: cada viñeta describe un cambio visible para quien usa el producto, no ruido de implementación; los cambios incompatibles llevan la acción de migración; las correcciones de seguridad van en una sección aparte; no quedan secciones vacías ni duplicados.
7. **Sugerir el salto de versión** según el estilo detectado. El usuario decide y etiqueta ([[usuario-declara-listo]]).

## Mapeo de Conventional Commits
Tipos: `feat`, `fix`, `perf`, `refactor`, `docs`, `test`, `build`, `ci`, `chore`, `security`, `deprecated`, `remove`. Cambio incompatible: `tipo(alcance)!: resumen`, o `BREAKING CHANGE:` en el cuerpo.

| Commit | Sección | Salto SemVer |
|---|---|---|
| `feat` | Added | minor |
| `fix` | Fixed | patch |
| `perf`, `refactor`, `build(deps)` | Changed (o Security si es una vulnerabilidad) | patch |
| `deprecated` / `remove` | Deprecated / Removed | patch (major si rompe) |
| `security` | Security | patch |
| incompatible | Changed, con nota en negrita y migración | major |

Orden por defecto (si el archivo no tiene uno): Security, Added, Changed, Deprecated, Removed, Fixed. Sin commits convencionales: listarlos en Changed con el mensaje original.

## Enlaces
Conviene usar enlaces de referencia (`[#123]: https://.../issues/123` al final) y un enlace de comparación por versión (`[1.2.0]: .../compare/v1.1.0...v1.2.0`, `[unreleased]: .../compare/v1.2.0...HEAD`). Se reutilizan los ya definidos y se actualiza el de `unreleased`.

## Gobernanza de release
Pasa el linter sobre el rango, genera un borrador, revisa la redacción, valida el salto de versión y etiqueta solo con el changelog aprobado. Escribir en el `CHANGELOG.md` de la rama principal requiere aprobación humana. Para CI, ver `references/ci-integration.md`. Para monorepos, `references/monorepo-strategy.md`. Para el formato, `references/changelog-formatting-guide.md`.

## Fallos
- Sin commits convencionales válidos: fallar pronto, sin emitir notas vacías que engañen.
- Archivo destino ausente: crear el encabezado base.
- No mezclar commits de merge con los del release, ni sobrescribir secciones históricas.
