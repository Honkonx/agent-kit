# Plantilla: fallas recurrentes (tabla viva)

Única pieza de documentación de fallas que se edita después del hecho. Cada falla vive con su dato exacto en el registro de cambios o en el documento del área; aquí solo se anota que volvió.

```markdown
# Fallas recurrentes
Última actualización: AAAA-MM-DD

| Clase | Síntoma exacto (textual) | Cuándo | Dónde (entorno, archivo:línea) | Qué se hizo | Automatizada |
|---|---|---|---|---|---|
| <nombre corto de la clase> | `<mensaje de error exacto>` | AAAA-MM-DD | <entorno>, `<archivo:línea>` | <arreglo y contra qué se verificó> | no |
| <misma clase> | `<mensaje>` | AAAA-MM-DD | <entorno> | <arreglo> | no |
| <misma clase> | `<mensaje>` | AAAA-MM-DD | <entorno> | <arreglo> | sí: `<prueba o script>` |
```

## Entrada de falla individual
```markdown
### AAAA-MM-DD — <síntoma en pocas palabras>
- Síntoma: "<mensaje textual>" / `<valor visto>` cuando debía ser `<valor esperado>`
- Dónde: `<archivo:línea>`, entorno `<cuál>`
- Verificado contra: `<comando o entorno>` el AAAA-MM-DD
- Causa: <entendida | probable (sin verificar) | desconocida: queda abierta>
- Arreglo: <qué se cambió> (o "sin arreglo")
- ¿Vuelve? <primera vez | segunda: ver tabla | tercera: automatizar>
```

## Reglas rápidas
- Tercera fila de la misma clase: automatizar y rellenar la columna "Automatizada".
- Una nota que corrige otra nota: no escribir una tercera; buscar la causa o automatizar.
- Sin causa entendida: escribirlo así y dejarlo abierto.
- Anotar también las fallas propias (prueba que pasaba por casualidad, "OK" que no verificaba nada).
