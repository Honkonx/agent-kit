---
name: qa-bugs-y-triage
description: Usar cuando se encontró un fallo y hay que reportarlo bien, cuando una prueba falla a veces (inestable/flaky) o al cerrar un informe de QA. Plantilla de bug, severidad vs prioridad, triage y repetición N veces.
---

# Bugs, triage e inestabilidad

El QUÉ (independencia, repetir antes de clasificar, "no verificable" explícito) está en la regla [[qa-independiente-y-oraculos]]. Esta skill cubre el CÓMO. La usan los agentes `qa`, `qa-adversarial`, `qa-explorador` y `qa-regresion`.

## Plantilla de bug
```
ID: BUG-AAAAMMDD-n     Título: <síntoma en una línea, sin suponer causa>
Severidad: S1 dinero/seguridad/datos | S2 función central rota | S3 secundaria | S4 cosmético
Prioridad: P1 ya | P2 esta fase | P3 luego     Estado: nuevo
Entorno: commit (git rev-parse --short HEAD), SO, versión de runtime, datos temporales/ficticios
Pasos (exactos, numerados; incluir semilla si vino de un simulador): 1. ...
Esperado: ...     Obtenido: ... (salida literal)
Evidencia: captura o log en la carpeta de informes, comando de repro de una línea
Frecuencia: N de M repeticiones     Notas: lo descartado (no es entorno ni transitorio)
```
Un bug sin repro determinista se reporta como "intermitente" con su tasa; no se descarta. Un hallazgo sin pasos ni medición no es accionable.

## Severidad vs prioridad
La severidad mide el daño si ocurre y la fija QA. La prioridad mide cuándo se arregla y la fija el dueño o el usuario. Pueden diferir: un S4 en la portada puede ser P1.

## Triage (en orden)
1. ¿Se reproduce 3 veces?
2. ¿Es del producto, del entorno (otra sesión recompilando, base sucia, servicio caído) o de la propia prueba?
3. ¿Es duplicado?
4. Asignar severidad y responsable. QA no arregla código de producto: reporta ([[subagentes-max-3-y-verificar]]).

## Inestabilidad (flaky)
Repetir el mismo caso N=5 (10 si es P1).
- 5/5 falla: determinista. 0/5: no reproducido; anótalo.
- Mixto: flaky. Reporta la tasa y sospecha de esperas fijas, procesos en segundo plano, datos que cambian, orden de ejecución y estado compartido.
- Arregla el test con esperas por condición, no con sleeps más largos. Un test flaky no se ignora: se pone en cuarentena con motivo y fecha.

## Cierre de informe
Resumen (N casos, M pasan), fallos con repro, bugs nuevos, lo **no verificable** (hardware, dispositivo táctil, servicios externos reales) y el peldaño de la escalera de [[verificacion-empirica]]. Nunca "listo": lo declara el usuario ([[usuario-declara-listo]]). Las fallas con causa raíz se registran con [[documentar-fallas]].

## Cuándo NO usar
- Un fallo ya diagnosticado, con causa raíz y arreglo: se registra con [[documentar-fallas]] (cierre de informe), no con esta plantilla.
- Un defecto de código de producto que QA quiere arreglar: QA no lo arregla; reporta con repro y lo decide el hilo principal (triage, paso 4).
- Decidir qué casos probar o qué oráculo usar: eso es el QUÉ de [[qa-independiente-y-oraculos]]; esta skill es el CÓMO del reporte y de la inestabilidad.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Solo falló una vez, no vale la pena reportarlo." | Un bug sin repro determinista se reporta como intermitente con su tasa; no se descarta (plantilla de bug). |
| "Subo el sleep y listo, el test ya pasa." | Las esperas van por condición, no con sleeps mayores; un test flaky se pone en cuarentena con motivo y fecha, no se ignora (inestabilidad). |
| "Se rompe al guardar, con eso basta." | Un hallazgo sin pasos ni medición no es accionable: hacen falta pasos exactos y la salida literal (plantilla de bug). |

## Errores comunes
- Título que supone la causa ("el caché rompe el guardado") en vez del síntoma (la plantilla pide no suponer causa).
- Escribir solo una severidad sin separar la prioridad, o al revés (severidad vs prioridad).
- Clasificar tras una sola reproducción en lugar de las 3 del paso 1 del triage.
- Anotar "Obtenido: falla" sin la salida literal del comando o del log.
- Descartar un fallo sin anotarlo en Notas (plantilla de bug).

## Verificación
- Repetir el caso N=5 (10 si es P1) y anotar si el resultado es 5/5, 0/5 o mixto (inestabilidad).
- Cada bug lleva Entorno con `git rev-parse --short HEAD` y Frecuencia como N de M (plantilla de bug).
- Antes de clasificar como defecto del producto, descartar entorno o sesión: otra sesión recompilando, base sucia o servicio caído (triage, paso 2).
- El cierre del informe da N casos, M pasan, la lista de no verificable y el peldaño de [[verificacion-empirica]] (cierre de informe).
