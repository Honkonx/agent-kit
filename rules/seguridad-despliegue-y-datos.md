# Nada remoto ni sobre datos reales sin autorización explícita en el mensaje actual

> Aplica a: todo proyecto con despliegue, migraciones o bases de datos. Reglas relacionadas: [[secretos]], [[archivos-protegidos]], [[verificacion-empirica]], [[no-asumir-separar-confirmado]], [[usuario-declara-listo]], [[cierre-de-ronda]].

Desplegar, migrar, respaldar, purgar o ejecutar cualquier script contra un servidor o contra datos reales exige autorización explícita del usuario en el mensaje actual. Lo que se verifica va contra el mismo motor y el mismo camino que producción.

## Por qué
En un servidor real no hay ensayo: los datos son los que se usan para vender y declarar. Scripts no idempotentes ejecutados "para verificar" duplicaron datos; una suite en verde sobre un motor distinto ocultó cientos de errores y un bug que perdía avisos en silencio; una copia de producción restaurada en local conservaba los tokens reales y podía invalidar la conexión del servidor al renovarlos.

## Cómo se aplica
**Autorización**
- La autorización es **por acción y por turno**: un "sí" a un script no cubre el siguiente ni repetir el mismo después. Sin excepción por ser "solo lectura de escritura", pequeño o "ya probado en local".
- Se pide diciendo **qué** se ejecuta, **qué hará**, **sobre qué datos** y **cómo se revierte**. Si escribe datos, primero en seco, se muestra el resultado y luego se pide aplicar.
- Cuenta como "correr un script en el servidor" todo lo que se ejecuta de su lado: scripts por contenedor o SSH, `.sh` del repo, SQL que modifica (`UPDATE`, `INSERT`, `DELETE`, `ALTER`), tareas programadas nuevas o cambiadas.
- No pide permiso cada vez: **mirar** (logs, estado, `SELECT` de diagnóstico, petición a un endpoint público) y el script de despliegue ya autorizado, que trae sus verificaciones. Mirar no pide permiso; ejecutar algo propio, sí.
- Migrar o sincronizar datos o esquema entre entornos (producción a local o al revés): permiso explícito para esa sincronización puntual, aunque la tarea general la sugiera.
- **Respaldos**: solo con autorización cada vez; una señal de "cuándo tendría sentido" (cambio grande, algo riesgoso) no es autorización.
- Ventana de despliegue: los días y horas en que se puede interrumpir el servicio son parámetro del proyecto; fuera de ella, no se despliega sin autorización expresa.
- Los scripts que borran o modifican en masa llevan en el código: guarda de entorno, bandera explícita para lo irreversible, y en la ayuda cuántas filas afecta y si es idempotente.

**Despliegue**
- Flujo manual y explícito: repositorio remoto, luego el paso humano, luego el servidor. Nunca copiar código directo al servidor real ni CI con disparador automático hacia producción.
- Con un túnel o recurso compartido entre entornos, nunca levantar "todo" el conjunto de servicios (p. ej. el orquestador de contenedores): se nombran los servicios. Dos conectores del mismo túnel enrutan tráfico real a un entorno de prueba sin error visible.
- Un health check en 200 no prueba que el código nuevo corre: confirmar un endpoint o campo que solo existe en la versión nueva. Si hay caché del lado cliente (Service Worker), la navegación va red primero; caché primero (*cache-first*) solo para recursos con huella en el nombre (un hash en el nombre del archivo), y el archivo del Service Worker se sirve **sin caché**, o un CDN lo deja pegado a una versión vieja.
- La suite limpia contra el motor real es condición para desplegar; si no, un fallo en el servidor no distingue cambio nuevo de defecto previo.

**Migraciones**
- Crear la migración no termina la tarea: se **aplica** en el entorno real de trabajo y se prueba la pantalla o endpoint que usa lo nuevo. Los tests suelen armar el esquema desde los modelos, no desde las migraciones, y pueden quedar en verde con la base real rota.
- Verificar también la vuelta atrás (`downgrade`) cuando el motor de pruebas lo limita.
- Escrituras concurrentes sobre un mismo registro: bloqueo a nivel fila en la transacción, no confiar en que "no ocurre".

**Bases bajadas de producción**
- Una copia trae datos **y** la conexión con lo real (tokens de integraciones, ambiente de facturación o pago, sincronizaciones). Justo después de restaurarla y **antes de arrancar nada**, se desconecta de todo servicio externo (script idempotente que no toca datos de negocio, solo corre contra una base local).
- Si aparece otra integración con credenciales en la base, se añade al script con su prueba.
- Segunda defensa en el código: el programa se niega a arrancar con credenciales reales fuera del entorno de producción.
- Bajar la copia sigue pidiendo autorización; restaurarla pisa la base local, así que antes se guarda la local.

**Purga antes de producción**
- Los datos de prueba en la base real son ruido que miente (informes, cierres, totales). Se purgan solo cuando el usuario lo ordena explícitamente. Lo externo (numeración y documentos oficiales emitidos) es otro sistema y se atiende aparte, sin frenar la purga.
- Orden: respaldo verificable (con autorización) → purgar lo generado probando → conservar configuración real → reiniciar correlativos → dejar constancia de qué y cuándo.

**Suite contra el mismo motor**
- Todo cierre que toque backend, modelos, migraciones o consultas corre la suite contra el **motor de producción** antes del commit. Un motor más permisivo (bloqueos que no aplica, claves foráneas desactivadas, `ALTER` limitado) esconde defectos y hace pasar pruebas "por casualidad".
- La sesión de pruebas se configura como la de producción (por ejemplo, sin vaciado automático antes de consultar); lo que crea y luego busca filas se vacía explícitamente.
- Una prueba que solo es válida en el motor real se **salta con el motivo escrito**, no se relaja.
- No hace falta para cambios solo de documentación o solo de interfaz (ahí basta compilar y probar en navegador). Un arreglo de una línea corre su archivo de pruebas contra el motor real y la suite completa al cerrar la tanda.

## Ejemplos
- No: "Corrí el script en el servidor para comprobar; como lo autorizaste ayer..."
- Sí: "`<script>` sumaría X unidades a N códigos; se revierte restando los movimientos que deja. Probé en seco. ¿Lo aplico?"
- No: restaurar la copia de producción y arrancar el backend.
- Sí: restaurar, desconectar integraciones con el script, verificar que no quedan tokens, y recién arrancar.
- No: "Migración creada y tests en verde."
- Sí: "Migración aplicada en la base de trabajo y probado el endpoint nuevo; suite pasada contra el motor de producción."

## Qué se ajusta por proyecto
- Servidores y entornos, y cómo se accede; la ventana de despliegue (días y horas).
- Comando del script de despliegue y de la desconexión de la base bajada, y qué integraciones cubre.
- Motor de producción, comando de la suite contra él y su duración esperada.
- Qué cuenta como dato de prueba a purgar y qué como configuración real; dónde queda la constancia.
