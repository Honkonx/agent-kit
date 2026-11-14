# Estrategia de cobertura y pirámide de pruebas (referencia)

Esta referencia sirve para una pasada de planificación mayor: tras una funcionalidad grande, antes de una versión, o al detectar un módulo con poca cobertura. El `SKILL.md` cubre la decisión ship/hold del día a día. No la uses en cada cambio pequeño.

## Objetivos de cobertura (orientativos; ajustar al riesgo)

| Categoría | Objetivo |
|---|---|
| Lógica de negocio crítica (dinero, stock, permisos) | > 80 % |
| Rutas críticas de punta a punta | > 90 % |
| Total del backend | > 60 % |

Reporte: `pytest tests/ -v --cov=<paquete> --cov-report=html` (solo cuando se necesite el número, no en cada corrida).

## Mapear rutas críticas antes de escribir pruebas

No persigas el número global a ciegas. Lista qué caminos de usuario no pueden fallar:

```
Ruta crítica        Archivos involucrados        Prioridad
Cobro / venta       router, servicio de stock    P0
Autenticación       servicio auth, seguridad     P0
Sync con externo    servicio de integración      P1
```
Un cambio en un archivo P0 sin prueba nueva es señal de **hold**.

## Pirámide orientativa

```
Unitarias (70 %)     lógica pura, validaciones, utilidades
Integración (20 %)   endpoints con cliente de prueba + BD de prueba
E2E (10 %)           flujo completo en navegador
```
Si un módulo tiene 0 pruebas de integración y 20 unitarias sobre helpers sueltos, la pirámide está invertida: primero se cierra el hueco de integración.

## Casos límite por función nueva (dinero, stock, permisos)

- [ ] Camino feliz
- [ ] Entrada `None` o vacía
- [ ] Límite inferior y superior (cantidad 0, negativa, precio 0)
- [ ] Tipo inválido (si el esquema no lo bloquea antes)
- [ ] Concurrencia si toca un recurso compartido (dos peticiones simultáneas; bloqueo de fila)

No apliques la lista completa a un helper trivial de formato.

## Priorización

| Prioridad | Criterio |
|---|---|
| P0 | Ruta crítica sin ninguna prueba |
| P1 | Ruta crítica con cobertura baja |
| P2 | Riesgo medio (validación de datos, cálculos no financieros) |
| P3 | Bajo riesgo (formato, utilidades) |

No gastes horas subiendo un módulo P3 mientras un P0 sigue en 0 %: el número global sube sin que baje el riesgo.
