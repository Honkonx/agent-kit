# Verificar con evidencia real antes de dar algo por resuelto

> Aplica a: todo proyecto. Reglas relacionadas: [[usuario-declara-listo]], [[no-asumir-separar-confirmado]], [[qa-independiente-y-oraculos]], [[documentar-fallas]].

"Compila", "el proceso arrancó" y "los tests pasan" no prueban que algo funcione: prueban que no falló de la forma más obvia. Antes de declarar un cambio listo, se ejecuta el camino real, se verifica la post-condición y se dice en qué peldaño de la escalera está.

## Por qué
Un arreglo "conocido" de internet no hacía nada en el entorno real; un instalador terminaba con exit 0 y el binario no corría; miles de pruebas en verde dejaron pasar un clic de usuario que fallaba; una tanda de ~20 arreglos nunca se volvió a mirar y el usuario terminó diciendo que "casi nada funciona". Nada de eso se vio leyendo código.

## Cómo se aplica
- **Ejecutar el camino real**, no el código que lo rodea: endpoint llamado de verdad contra datos temporales; pantalla cargada en un navegador real revisando consola y red; ejecutable o instalador corrido contra un directorio limpio; impresión o archivo generado abierto de verdad; migración aplicada sobre una copia de una base antigua.
- **Verificar la post-condición, no el código de salida.** ¿El registro quedó con los campos esperados? ¿El binario existe Y corre? ¿El puerto responde? Un `command -v` o un `{"ok": true}` no bastan.
- **No fiarse de una solución "documentada en otro lado"** (foro, README, experiencia previa) sin confirmarla en este entorno: probarla, o descartar alternativas una por una hasta la causa raíz confirmada.
- **Probar como lo vive una persona**, no solo con unidades que sustituyen todo. Todo flujo de usuario necesita al menos un recorrido de punta a punta: esquema construido con las migraciones reales, componentes reales, y solo lo externo simulado en el límite. Probar una matriz de estados (esquema al día/atrasado, con/sin permiso, datos vacíos, fuentes caídas, doble clic), priorizando por riesgo y diciendo qué quedó sin probar.
- **Entradas de persona, no de máquina**: formatos locales de miles y decimales, símbolos de moneda, espacios, letras, signo menos, pegar, apretar dos veces, cambiar de pantalla y volver. Lo que importa es **qué quedó guardado**, no si apareció un mensaje.
- **Contraprueba**: toda prueba que atrapa un defecto se comprueba reintroduciendo ese defecto; si al reintroducirlo la prueba no falla, no sirve. Todo hallazgo se queda como caso permanente.
- **Una tanda grande de arreglos simultáneos sobre el mismo subsistema necesita su propia pasada de verificación posterior**, con evidencia real, además de la verificación de cada arreglo.
- **No dar por causa raíz el primer hallazgo**: solo se confirma tras revisar el panorama y las alternativas.
- **Nota de verificación**: toda corrección dice contra qué se verificó y cuándo (`Verificado AAAA-MM-DD contra <comando/entorno>`).
- Si algo no se pudo verificar (no hay dispositivo, no hay entorno), se dice explícitamente; nunca se rellena con "debería funcionar".
- **Una función accesoria** (memoria, avisos, métricas) **no puede romper el flujo central**: se aísla (captura del error y reversión) y una prueba lo demuestra con su dependencia ausente.
- **Un nombre de paquete o dependencia que "suena correcto" se comprueba contra el repositorio real**; un fallback que lo oculta en silencio (por ejemplo `|| warn` en shell) no es verificación.
- **Subsistema de piezas acopladas**: tras tocar una, se verifica el subsistema completo, no solo el paso cambiado; un arreglo local puede romper la coordinación sin que ningún registro individual lo muestre.
- **Ante una falla reproducible**, capturarla con una prueba de regresión *antes* de corregir cuando sea práctico.
- **Al cerrar**: declarar el nivel de verificación alcanzado, el **riesgo residual concreto** y el siguiente chequeo necesario; informar por separado pruebas automáticas, integración y QA real. Un respaldo se prueba **restaurándolo** en un lugar aislado.
- Si el usuario pidió solo análisis, no se corren verificaciones que modifiquen el entorno.
- Las pruebas no dependen de la máquina (servicios locales, archivos de entorno, binarios): se aíslan para que den lo mismo en cualquier equipo.

## Escalera de "listo" (no saltar peldaños; decir en cuál se está)
1. compila y las pruebas automáticas pasan: "escrito"
2. arranca con datos limpios: "arranca"
3. QA de punta a punta en el entorno real: "funciona en QA"
4. uso real controlado: "funciona"
5. un tiempo de uso real sin incidentes: "está listo" (solo lo declara el usuario, ver [[usuario-declara-listo]])

## Checklist post-ronda (al cerrar una ronda que tocó código; no hace falta si fue solo documentación)
- Sintaxis/compilación de cada archivo tocado; formatos de datos (JSON, XML, YAML) parsean; sin IDs duplicados en catálogos.
- Copias sincronizadas entre carpetas espejo (comparar por hash, no por existencia).
- El estado del repositorio contiene solo lo del alcance pedido; ningún archivo suelto fuera de él.
- Ninguna ruta de usuario/máquina nueva hardcodeada; ningún secreto nuevo en logs, respuestas o commits (ver [[secretos]]).
- Un tamaño de archivo no prueba contenido: en artefactos empaquetados comparar el contenido real, no el peso en disco.
- Un punto en rojo se corrige antes de cerrar; un falso positivo conocido se dice, no se silencia.
- Este checklist es mecánico: confirma "no rompí lo obvio", no "la funcionalidad es correcta".

## Ejemplos
- No: "Arreglado, compila y los tests pasan."
- Sí: "Verificado 2026-xx-xx: llamé al endpoint con base temporal y el registro quedó con total X (esperado X). Sin probar: impresión real."
- No: "El script ya no da error, listo."
- Sí: "Leí el registro resultante y tiene los campos esperados; reintroduje el error y la prueba cae."

## Qué se ajusta por proyecto
- Qué significa "camino real" (entorno, datos temporales, navegador, dispositivo) y los comandos de prueba por plataforma.
- Los comandos del checklist post-ronda según el stack y las carpetas espejo que existan.
- La escalera concreta si el dominio añade peldaños (ej. modo de prueba antes de uso real).
