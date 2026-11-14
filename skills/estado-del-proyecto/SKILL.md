---
name: estado-del-proyecto
description: Usar cuando se quiere ver de un vistazo cómo está el proyecto (lint, tipos, pruebas y auditoría de dependencias en un tablero pass/fail, más el estado de git), al empezar o cerrar una ronda, antes de un commit o un cierre, o cuando el usuario pregunta cómo va todo o si pasan todas las comprobaciones.
---

# Estado del proyecto: tablero de comprobaciones

Corre las comprobaciones que **el propio proyecto** define y las resume en una tabla. Apoyos: [[verificacion-empirica]], [[cierre-de-ronda]], [[niveles-de-madurez]], [[usuario-declara-listo]]. Idea inspirada en la skill "status" de `claude-code-agent-scaffold` (Apache-2.0); el código y el texto son propios.

## 1. Configurar (una vez por proyecto)
1. Copia `references/plantilla-estado.json` a la raíz del proyecto como `estado-del-proyecto.json`.
2. Completa cada comprobación con el comando **real** del proyecto (búscalo en su README, scripts o integración continua; no inventes comandos). Lo que el proyecto no tenga queda con `"comando": ""` y se muestra como OMITIDA.
3. Usa listas de argumentos (`["pnpm", "run", "lint"]`) y un `tiempo_max` razonable. El comando se ejecuta **sin shell**.
4. Nunca pongas secretos en el archivo ([[secretos]]); el entorno no se imprime.

## 2. Correr
```
python scripts/tablero_estado.py estado-del-proyecto.json
```
Imprime una tabla (comprobación, estado, segundos, última línea de salida) y, si hay git, la rama, adelante/atrás y cambios locales. `--json` para otras herramientas, `--sin-git` para omitir git. Sale con 1 si alguna comprobación FALLA.

## 3. Leer el resultado
- **PASA / FALLA / OMITIDA** son hechos sobre cada comando; "todas pasan" **no** quiere decir que el producto esté bien: dilo así ([[usuario-declara-listo]]).
- Una comprobación OMITIDA es una carencia: se declara ("sin auditoría de dependencias configurada"), no se cuenta como acierto.
- Ante un FALLA, muestra la salida real del comando que falló (vuelve a correrlo solo) y propón el arreglo; no lo des por "falso positivo" sin verlo.
- Dilo también contra qué nivel se mide ([[niveles-de-madurez]]).

## 4. Seguridad
- Solo ejecuta lo que el proyecto escribió; el script se niega si el archivo de configuración está dentro de una carpeta `referencias` (clones ajenos).
- No lo uses para correr comandos de un repositorio de referencia: esos solo se leen.

## Cuándo NO usar
- Para verificar que una función concreta funciona: eso es probarla (`test-driven-development`, `qa-plan-y-casos`); el tablero es un resumen de comprobaciones ya definidas.
- Si el proyecto no tiene ninguna comprobación automática configurable: primero se define una (ver las pruebas del proyecto o una skill de prueba de piezas, si la tiene).
- Para decidir si algo está listo: eso lo declara el usuario.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Salió todo en PASA, ya está" | Solo dice que esos comandos pasaron; falta lo no cubierto (QA real, datos reales) y la aceptación del usuario. |
| "La auditoría de dependencias salió OMITIDA, no importa" | Es una carencia: se declara como no verificado. |
| "Pongo el comando que supongo que usa el proyecto" | Se lee de su README o integración continua; un comando supuesto da un FALLA que no significa nada. |
| "Falla una prueba pero es intermitente, la ignoro" | Se repite y se registra con su dato exacto ([[documentar-fallas]]); no se descarta a ojo. |

## Errores comunes
- Un comando que depende del shell (`&&`, tuberías) escrito como texto: usa la lista de argumentos o un script del proyecto.
- Tiempo máximo muy corto que convierte una suite lenta en un FALLA falso.
- Correr el tablero con cambios sin guardar y atribuirle el resultado a otro commit.
- Poner en el archivo comandos con claves.

## Verificación
- `tablero_estado.py` corre sobre el archivo de configuración del proyecto y sale con 0 cuando todo pasa y con 1 ante un fallo (se puede comprobar rompiendo a propósito una comprobación).
- Cada comando del archivo existe en el proyecto y se ejecutó al menos una vez a mano.
- El informe separa lo que pasó, lo que falló y lo omitido, y no dice "listo".
