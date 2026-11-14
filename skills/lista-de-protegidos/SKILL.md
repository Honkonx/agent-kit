---
name: lista-de-protegidos
description: Usar cuando hay que definir o actualizar la lista de archivos o módulos protegidos de un proyecto, antes de editar un archivo que podría estar en ella, al pedir permiso para tocar uno, o cuando se descubre que ya se modificó uno sin permiso.
---

# Lista de archivos protegidos: definirla, leerla y pedir permiso

La regla [[archivos-protegidos]] dice **qué** se cumple; esta skill dice **cómo** se mantiene la lista y se pide el permiso. Se apoya en [[no-asumir-separar-confirmado]], [[usuario-declara-listo]] y [[secretos]]. Los protegidos no se delegan a subagentes de edición ([[subagentes-max-3-y-verificar]]).

## 1. Crear la lista (una sola vez, en un único lugar)
1. Copiar `references/plantilla-protegidos.md` al sitio fijo que el proyecto elija (por ejemplo su archivo de reglas locales) y anotar esa ruta en las instrucciones del proyecto.
2. Proponer candidatos al usuario; la lista final la decide él. Qué suele entrar:
   - credenciales y manejo de secretos;
   - controles de riesgo, seguridad y autenticación;
   - dinero, facturación y cálculos críticos;
   - bases de datos de producción y migraciones aplicadas;
   - configuración de compilación y de despliegue;
   - módulos que el usuario declaró intocables.
3. Por cada entrada: ruta o patrón, **motivo**, **fecha** de alta y **quién autoriza** cambios.
4. Anotar también lo que es siempre libre: documentación y memoria.

## 2. Antes de editar cualquier archivo
1. **Leer la lista vigente** (no inferirla de memoria).
2. Comprobar si el archivo o su módulo está en ella, incluso si el cambio parece inocuo: se juzga por pertenencia, no por tamaño ni apariencia.
3. Si no está: seguir. Si está: **parar**, no aplicar el cambio y pasar al punto 3.

## 3. Pedir el permiso (explícito y fresco)
Un permiso vale solo si nombra **ese archivo y ese cambio** y se dio **en esta sesión**. No cuentan: un "sí" de otra sesión o de otro archivo, ni órdenes generales ("arregla todo", "audita X") que no lo nombran, ni un bug verificado.

Mensaje modelo (corto):
```
Hallazgo en el módulo protegido <ruta>, línea <N>: <síntoma y evidencia>.
No lo toqué. Cambio propuesto: <descripción o diff>.
¿Autorizas editarlo?
```
Mientras no haya respuesta, dejar el cambio propuesto sin aplicar y seguir con el resto del trabajo. Un permiso concedido vale para ese módulo y esa ronda; no se extiende.

## 4. Mantener la lista
- Cuando el usuario agrega o retira algo, actualizar la lista **en el momento** con fecha y motivo (no borrar la historia: marcar "retirado el AAAA-MM-DD, motivo").
- Revisarla al auditar la documentación ([[docs-organizacion-y-fechada]]) y al añadir un módulo nuevo sensible.
- Comprobar que la ruta de la lista aparece en las instrucciones del proyecto.

## 5. Si ya se tocó uno
1. Decirlo de inmediato, sin esperar al informe final.
2. Mostrar el cambio exacto (diff) y el motivo.
3. No revertir ni conservar por cuenta propia: el usuario decide.
4. Anotar el incidente con fecha (ver [[documentar-fallas]]) y revisar por qué no se leyó la lista.

## Cuándo NO usar
- Para decidir qué cambio hacer en un archivo que no está en la lista: se edita con las demás reglas.
- Para documentación y memoria: son libres por definición (se anota en la lista).
- Para dar un permiso por iniciativa propia: solo el usuario lo da, y vale para ese módulo y esa ronda.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Es un bug real, lo arreglo de paso" | Un bug real no es permiso: se reporta con evidencia y se pregunta. |
| "Es un comentario o formato, no cambia la lógica" | No hay excepción por tamaño o apariencia: manda la pertenencia a la lista. |
| "Dijo 'arregla todo', incluye este archivo" | Una orden general que no lo nombra no cuenta como permiso. |
| "Ya me autorizó ayer para este módulo" | El permiso es fresco: vale en esta sesión, para ese cambio. |
| "Sé qué archivos son protegidos, no releo la lista" | La lista se lee antes de editar; no se infiere de memoria. |

## Errores comunes
- "Lo arreglé de paso" porque el bug era real.
- Reutilizar un permiso viejo o de otro archivo.
- Inferir la lista de memoria en lugar de leerla.
- Editar comentarios o formato en un archivo protegido porque "no cambia la lógica".
- Dejar que un subagente edite un protegido.

## Verificación
- La lista tiene una sola ubicación, con ruta, motivo, fecha y quién autoriza por entrada, y esa ruta figura en las instrucciones del proyecto.
- Antes de cada edición sobre un área sensible se leyó la lista vigente en esta sesión.
- Cada permiso usado nombra el archivo y el cambio, y está citado (bitácora o decisión).
- Si se tocó un protegido por error, el cambio exacto se mostró al usuario y el incidente está anotado con fecha.
