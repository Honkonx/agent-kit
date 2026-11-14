# Los secretos no se muestran, no se suben y no se hornean

> Aplica a: todo proyecto. Reglas relacionadas: [[verificacion-empirica]], [[archivos-protegidos]], [[publicar-solo-con-orden]], [[seguridad-despliegue-y-datos]].

Ninguna credencial se imprime, se pega, se repite ni se sube a un repositorio; antes de cada push se escanea lo que se va a subir. Si un secreto ya se filtró, se rota: borrarlo no lo invalida.

## Por qué
Un token real quedó escrito en un script desde el primer commit y no causó daño solo porque el repositorio aún no tenía remoto. Otras veces varias claves llegaron a un commit. Un `.gitignore` no protege lo que ya está en el historial.

## Cómo se aplica
**Nunca revelar**
- No mostrar en pantalla, chat, commit, log ni documento: contraseñas, tokens, claves API, claves privadas, certificados, contenido de un `.env`, bases reales ni respaldos. Aunque el usuario lo haya escrito antes y aunque el fin sea "solo verificar".
- Se verifica **presencia, no valor**: "la variable está definida", longitud, prefijo o fecha. Ni siquiera parcialmente si el valor es reconstruible.
- Un secreto guardado solo se **usa, reemplaza o borra**: ninguna UI, endpoint ni log lo devuelve; el campo de reemplazo empieza vacío. Los endpoints exponen indicadores ("tiene_certificado"), no el secreto.
- Permisos restrictivos al guardarlo en disco. Un secreto de servidor nunca va a código que corre en el navegador. Los tokens se guardan en el almacenamiento seguro de la plataforma, no en archivos de configuración versionados.
- El `.gitignore` cubre archivos de entorno, credenciales, bases de datos y carpetas de memoria; se comprueba, no se supone. Un remoto de git no lleva credenciales en la URL (se ve con `git remote -v`): se autentica con la sesión de la herramienta.
- El asistente no teclea contraseñas en navegadores ni las pasa por línea de comandos.
- **Ningún secreto dentro de una cadena de comando** (`echo "clave"`, `printf '%s' 'clave'`, argumentos de un script): queda en el historial, en los listados de procesos y en los registros. Se pasa por variable de entorno inyectada al proceso o por un archivo con permisos restrictivos que no se versiona.
- **Ni en el entorno donde corre código generado por el modelo** (sandboxes, intérpretes, scripts que el asistente acaba de escribir): ese código puede leer el entorno y mostrarlo. Se entrega al proceso solo lo imprescindible, con vida corta y alcance mínimo, y se asume que el código generado podría leerlo.
- Datos de prueba, capturas, fixtures y reportes usan datos ficticios o anonimizados; los datos financieros o personales reales no salen del entorno.

**Antes de cada push** (no solo el primero)
- Buscar en lo que está **staged** (no en todo el repo) patrones de credenciales: `ghp_`, `gho_`, `github_pat_`, `glpat-`, `sk-`, `AIzaSy`, `xox[baprs]-`, `-----BEGIN`, cabeceras de autorización con valor literal, además de los patrones propios del proyecto, y valores de alta entropía.
- Revisar también los **nombres** staged: `.env*`, `*.pem`, `*.key`, bases de datos, respaldos, exportaciones reales, capturas y logs.
- En el primer push de un historial preexistente, revisar el historial completo, no solo lo staged.
- Un match es secreto real salvo prueba en contrario; "es un script viejo" no es prueba. Reportar solo archivo, línea aproximada y tipo; nunca el valor ni el diff entero.
- Un escáner sin hallazgos no sustituye la revisión de `.env`, JSON de credenciales, bases, capturas y logs.

**Si un secreto ya se filtró** (commit, log, mensaje, remoto)
1. Avisar de inmediato y considerarlo comprometido.
2. Si llegó a cualquier remoto (aunque sea privado) o a un chat/log compartido: **rotarlo o revocarlo** en el servicio que lo emitió. Reescribir historial no basta.
3. Si nunca salió del equipo, limpiar el historial (herramienta de reescritura con reemplazo del valor exacto) tras un respaldo del repo y con confirmación del usuario, porque es destructivo.
4. Solo después de rotar se sigue trabajando.

**Desarrollo vs. producción**
- En desarrollo: credenciales en un archivo local ignorado por git, rellenado por el usuario.
- En empaquetados, instaladores o scripts distribuidos: ninguna credencial horneada, ni de una cuenta de prueba; se lee de configuración que cada usuario llena en su equipo. Cada persona usa las suyas, nunca las del desarrollador.
- No reutilizar credenciales entre cuentas ni entornos.
- Una herramienta de IA o un servidor auxiliar puede no leer el archivo de entorno: si necesita una variable, va en una variable real del sistema o en la configuración local ignorada por git, no solo en el archivo de referencia.

## Ejemplos
- No: "El token es `ghp_ab12...`, ya lo puse en el script."
- Sí: "`GITHUB_TOKEN` está definida (40 caracteres, prefijo `ghp_`); el script la lee del entorno."
- No: "Borré el archivo del commit, listo."
- Sí: "Ese token llegó al remoto: hay que revocarlo y emitir uno nuevo; luego limpio el historial."

## Qué se ajusta por proyecto
- Lista de qué cuenta como secreto (proveedores, certificados, claves de terceros) y dónde viven.
- Patrones extra a escanear y el comando/hook que ejecuta el escaneo.
- Cuál es el archivo local ignorado y la configuración de la herramienta que lee variables.
