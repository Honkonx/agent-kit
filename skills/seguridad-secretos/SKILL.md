---
name: seguridad-secretos
description: Usar cuando se vaya a commitear, hacer push o compartir archivos, y haya que escanear en busca de claves, tokens, credenciales o datos sensibles filtrados; o al auditar un repositorio por secretos expuestos.
---

# seguridad-secretos

> Índice de roles de seguridad, si el proyecto lo tiene. Respuesta a incidente de secreto filtrado paso a paso: guía de incidentes del proyecto, si la tiene.

Escáner por reglas de secretos, credenciales, tokens y datos sensibles en archivos locales (código, logs, volcados). La regla `secretos` dice QUÉ se debe cumplir (nunca mostrar, nunca subir, rotar si se filtró); aquí está el CÓMO del escaneo. Para una auditoría más amplia usa el agente `seguridad` (o una skill de auditoría de seguridad del proyecto, si la tiene).

## Requisito: ripgrep

El script usa `ripgrep` (`rg`) en el `PATH`. Verifica con `rg --version`; si falta, instálalo (`winget install BurntSushi.ripgrep.MSVC`, `choco install ripgrep` o el binario oficial) o pasa `--rg <ruta>`. Solo usa la librería estándar de Python (PyYAML es opcional, para reglas `.yml`).

## Cuándo correrlo

- **Antes de cada commit o push** que toque configuración, scripts que llaman APIs externas o archivos `.env*` (complementa el escaneo de lo staged de la regla `secretos`).
- **Auditoría periódica** del código completo, filtrando por el grupo `Sensitive Information`.
- Antes de compartir archivos fuera del equipo (logs, volcados, capturas de configuración).
- Si el escaneo confirma una fuga real (secreto que llegó a un commit, remoto, artefacto compartido o log): es un incidente. Avisa, rota la credencial en el servicio que la emitió y solo después limpia el historial con confirmación del usuario (regla `secretos`). Borrar el archivo no basta.

## Cómo correrlo

El objetivo es obligatorio (nunca escanea el directorio actual por defecto). Llama al script con su ruta, desde la raíz del repo:

```bash
python <ruta-skill>/scripts/hae_scan.py <carpeta-o-archivo> [<otro> ...]
python <ruta-skill>/scripts/hae_scan.py <objetivo> --group "Sensitive Information" --group "Basic Information"
```

Escribe `.hae/hae-scan-<timestamp>.json` en el directorio actual (añade `.hae/` al `.gitignore`: el reporte puede contener los valores encontrados) y un resumen por regla. Lee el JSON con una consulta pequeña en vez de volcarlo:

```bash
python -c "
import json,sys
d=json.load(open(sys.argv[1]))
for f in d['findings']:
    if f['group'] in ('Sensitive Information','Basic Information','Maybe Vulnerability'):
        loc=f['locations'][0]
        print(f\"{f['group']}/{f['rule']}\t{loc['file']}:{loc['line']}:{loc['column']}\tx{f['count']}\")
" .hae/hae-scan-<timestamp>.json
```

(Esa consulta imprime solo regla y ubicación: nunca imprimas `f['match']` de un hallazgo sensible. Reporta archivo, línea aproximada y tipo, jamás el valor; regla `secretos`.)

## Verificar antes de reportar

Las reglas están orientadas a recall: detectan de más. Confirma cada hallazgo de valor leyendo la línea real. Tratar como ruido salvo prueba en contrario: valores de ejemplo (`example.com`, `xxx`), fixtures de pruebas, dependencias vendorizadas (`node_modules`, `venv`), código minificado de terceros. Un match en un archivo que sí llegó a un commit es secreto real hasta que se demuestre lo contrario. Un escáner sin hallazgos no sustituye revisar a mano `.env`, JSON de credenciales, bases, capturas y logs.

## Opciones principales

| Opción | Default | Propósito |
|---|---|---|
| `targets` | obligatorio | Archivos o directorios |
| `--rules RUTA` | `<skill>/rules/Rules.json` | Conjunto de reglas alternativo |
| `--group NOMBRE` / `--rule NOMBRE` | todos | Filtrar por grupo o regla (repetible) |
| `-o, --out RUTA` | `.hae/hae-scan-<ts>.json` | Salida; `-` imprime a stdout |
| `--context N` | 50 | Caracteres de contexto por match (0 lo desactiva; útil para no guardar de más) |
| `--max-locations N` / `--max-matches N` | 5 / 200 | Límites por valor y por regla (0 = sin límite) |
| `--ignore-ext EXT` | imágenes | Extensiones a omitir |
| `--rg RUTA` | `rg` del PATH | Binario de ripgrep |

## Grupos de reglas

| Grupo | Contenido | Señal |
|---|---|---|
| Sensitive Information | claves, tokens, campos de credenciales, AK/SK de nube, cabeceras de autorización | máxima prioridad |
| Basic Information | correo, teléfono, documento de identidad, IP, dominio | media: ¿dato real o fixture? |
| Maybe Vulnerability | deserialización, parámetros de debug, formularios de subida | media: confirmar a mano |
| Fingerprint | JWT, Swagger UI, modo dev, etc. | alta como inventario |
| Other | Linkfinder, All URL, Request URI, Source Map | baja y muy ruidosa: reporta conteos y ejemplos, no listados |

## Mantenimiento de reglas

`rules/Rules.json` es el set HaE reducido a `group`, `name`, `loaded`, `regex`, `sensitive`. Para añadir una regla, copia una de HaE, renombra `f_regex` a `regex` y quita los demás campos. Añade también los patrones propios del proyecto (prefijos de sus proveedores) y prueba la regla nueva contra un archivo con un valor falso evidente.

## Checklist

- [ ] ripgrep instalado; objetivo explícito; `.hae/` ignorado por git.
- [ ] Hallazgos de valor confirmados leyendo la línea; el informe no contiene valores.
- [ ] Nombres staged revisados a mano (`.env*`, `*.pem`, `*.key`, bases, respaldos).
- [ ] Fuga confirmada: credencial rotada antes de seguir (regla `secretos`).
