# Plantilla y ejemplo de flujo

Copiar la plantilla a la carpeta de flujos guardados del proyecto. Un flujo guardado lleva nombre, fecha de última revisión y la tabla.

## Plantilla
```
## FLUJO: <nombre>
Última revisión: AAAA-MM-DD
TIEMPO TOTAL ESTIMADO: ~X

| # | Responsable | Acción | Tiempo | Salida |
|---|---|---|---|---|
| 1 | [Asistente] | | | |
| 2 | [Usuario] | | | |

Si falla el paso N: <recuperación>
Skills de dominio relacionadas: <nombres>
```

## Ejemplo neutro: publicar una nueva versión de una librería
## FLUJO: Publicar versión
TIEMPO TOTAL ESTIMADO: ~45 min

| # | Responsable | Acción | Tiempo | Salida |
|---|---|---|---|---|
| 1 | [Asistente] | Revisar cambios desde la última etiqueta y generar el borrador del changelog (skill `changelog-generator`) | ~5 min | borrador de changelog |
| 2 | [Usuario] | Revisar y aprobar el texto y el salto de versión | ~10 min | changelog aprobado |
| 3 | [Asistente] | Correr la suite completa y el build | ~10 min | salida de pruebas |
| 4 | [Usuario] | Autorizar la etiqueta y la publicación | ~2 min | autorización explícita |
| 5 | [Servicio] | Publicar el paquete en el registro | ~5 min | enlace a la versión publicada |
| 6 | [Asistente] | Comprobar que el paquete publicado se instala y arranca en un directorio limpio | ~10 min | evidencia de instalación |

Si falla el paso 3: no etiquetar; documentar el fallo con su mensaje exacto y corregir antes de seguir.
