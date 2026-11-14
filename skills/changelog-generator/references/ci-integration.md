# CI Integration Examples

> Úsalo solo si el proyecto tiene CI. Si no lo usa, el linter se corre en local y no se crea CI sin una orden nueva.
> `<ruta-de-la-skill>` es la carpeta donde está instalada esta skill en el proyecto (no se fija aquí).

## GitHub Actions

```yaml
name: Changelog Check
on: [pull_request]

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 <ruta-de-la-skill>/scripts/commit_linter.py \
          --from-ref origin/main --to-ref HEAD --strict
```

## GitLab CI

```yaml
changelog_lint:
  image: python:3.12
  stage: test
  script:
    - python3 <ruta-de-la-skill>/scripts/commit_linter.py --to-ref HEAD --strict
```
