# Plantilla: lista de archivos protegidos

Ubicación fija en el proyecto: `<ruta de este archivo>` (anotarla en las instrucciones del proyecto). Se lee antes de editar; no se infiere de memoria.

```markdown
# Archivos protegidos de <proyecto>
Última actualización: AAAA-MM-DD

Regla: no se edita ninguna línea sin permiso explícito y fresco del usuario para ese cambio puntual
(ver regla `archivos-protegidos`). Un bug real no es permiso: se reporta y se pregunta.

## Protegidos
| Ruta o patrón | Motivo | Desde | Quién autoriza cambios | Estado |
|---|---|---|---|---|
| `<ruta/archivo.ext>` | <credenciales / controles de riesgo / producción / compilación / declarado intocable> | AAAA-MM-DD | <usuario / rol> | vigente |
| `<carpeta/**>` | <motivo> | AAAA-MM-DD | <quién> | vigente |
| `<ruta antigua>` | <motivo> | AAAA-MM-DD | <quién> | retirado el AAAA-MM-DD: <motivo> |

## Siempre libres (sin pedir permiso)
- Documentación y memoria.
- Código que no vive en un archivo protegido.
- Módulos que el usuario nombró como tocables: <lista, con fecha y alcance de la ronda>.

## Permisos concedidos (solo vigentes en la ronda indicada)
| Fecha | Archivo y cambio | Frase textual del usuario | Vigencia |
|---|---|---|---|
| AAAA-MM-DD | `<archivo>`: <cambio> | "<cita>" | solo esta ronda |

## Incidentes (se tocó uno sin permiso)
| Fecha | Archivo | Qué se cambió | Decisión del usuario (revertir / conservar) |
|---|---|---|---|
```

## Mensaje para pedir permiso
```
Hallazgo en el módulo protegido <ruta>, línea <N>: <síntoma y evidencia>.
No lo toqué. Cambio propuesto: <descripción o diff>.
¿Autorizas editarlo?
```
