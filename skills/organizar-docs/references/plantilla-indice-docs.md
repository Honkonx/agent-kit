# Plantilla: índice raíz de docs (`docs/README.md`)

```markdown
# Documentación de <proyecto>

Próxima auditoría: AAAA-MM-DD   (contra el código; última: AAAA-MM-DD)

## Estado para retomar
<Un único bloque, reescrito cada sesión: qué se hizo, qué sigue, qué está bloqueado, fecha.>

## Carpetas
| Carpeta | Tipo | Qué va | Qué NO va |
|---|---|---|---|
| `<arquitectura>/` | vigente | <diseño actual, módulos, contratos> | <decisiones históricas, auditorías> |
| `<guias>/` | vigente | <guías operativas, instrucciones> | <informes puntuales> |
| `<auditorias>/` | foto fechada | <informes por tema, con la fecha dentro> | <estado actual del sistema> |
| `<investigaciones>/` | foto fechada | <investigaciones con evidencia> | <decisiones sin fuente> |
| `<decisiones>/` | foto fechada con estado | <una decisión por archivo: vigente / propuesta / superada por …> | <guías operativas> |
| `<planes>/` | foto fechada al cerrar | <planes abiertos; los cerrados van a archivo> | <análisis sueltos> |
| `<bitacora>/` | foto fechada | <lotes numerados `NNNN-tema`> | <contenido técnico de referencia> |
| `<archivo>/` | foto fechada | <lo superado, con "Superado por …" al inicio> | <nada vigente> |

## Reglas de esta carpeta
- Vigente: se corrige in situ contra el código, en la misma ronda. Sin fecha en el nombre.
- Foto fechada: no se reescribe; lo nuevo va en un documento nuevo que enlaza al anterior.
- Nunca se borra: se mueve con `git mv` a `<archivo>/`.
- Cada carpeta tiene su `README.md`; con más de ~5 documentos lleva índice; máximo 2 niveles.
- Al mover o renombrar: corregir referencias cruzadas y este índice en la misma ronda.
- Cifras: de un comando, con fecha. Nunca a mano.

## Fallas recurrentes
Ver `<ruta>/fallas-recurrentes.md`.
```

## README de cada carpeta
```markdown
# <Carpeta>
Tipo: <vigente | foto fechada>
Qué hay: <una línea>
Qué va: <criterio>
Qué NO va: <criterio>
Índice: <lista, si hay más de ~5 documentos>
```
