# Continuidad entre máquinas y herramientas: no arrancar a ciegas, no hardcodear rutas

> Aplica a: todo proyecto que se trabaje desde más de una máquina, entorno o herramienta de IA. Reglas relacionadas: [[no-asumir-separar-confirmado]], [[verificacion-empirica]], [[documentar-en-vivo]], [[bitacora-humana]], [[secretos]].

Antes de trabajar, comprobar el estado real del repo y del entorno; nunca asumirlo por memoria de una sesión previa. Ningún archivo del proyecto lleva rutas con usuario o máquina hardcodeados.

## Por qué
Otra máquina o herramienta puede haber avanzado el repo muchos commits sin que la sesión lo sepa; un fix aplicado al repo puede no estar en lo que corre en producción; y una ruta con el usuario de una PC antigua deja configuraciones rotas sin que nadie lo note.

## Cómo se aplica
**Al empezar una sesión de trabajo real** (no en preguntas puntuales):
1. `git status` y `git fetch`; comparar la rama con su remoto (adelante/atrás). Si el local está detrás, actualizar antes de confiar en el contenido.
2. Si el resultado es inesperado (diverge, adelante y atrás, no cuadra con lo que se creía): **parar** y entender con `git log`/`git merge-base --is-ancestor` antes de `pull`/`merge`/`reset`. Nunca `reset --hard` ni `checkout .` para "resolver" una sorpresa.
3. Leer el registro de sesiones más reciente (la bitácora, si existe) y el estado o la memoria compartida que viven **dentro del repo**.

**Qué no asumir sin verificar**:
- Que lo que corre en un entorno remoto (servidor, VPS, dispositivo) coincide con el repo: puede estar parcheado a mano. Ante "arreglé el bug pero sigue pasando", la primera pregunta es qué versión corre realmente.
- Que la memoria personal de una herramienta de IA está sincronizada con la de otra: la única fuente compartida es lo que está en el repo.
- Que un archivo "recordado" conserva su contenido: leerlo de nuevo antes de citarlo como vigente.
- Que algo que desaparece del repo o del disco sin explicación debe restaurarse: se pregunta antes, porque pudo ser una baja deliberada; una regla desactualizada que mencione una herramienta o espejo descontinuado no autoriza recrearlo.
- En qué rama se está, si hay duda: se comprueba (`git branch --show-current`) antes de commitear; una rama creada como excepción no se fusiona a la principal sin que el usuario lo pida.
- Que no hay trabajo sin subir en otra carpeta o máquina: no es detectable desde aquí; no afirmarlo.
- Que una limitación de una máquina (cuota de CI agotada, fallo de entorno local, herramienta que se cuelga) es un bug del proyecto: registrar la causa real y en qué máquina aplica, en la bitácora o memoria del proyecto.
- Que los espejos de memoria o reglas (si el proyecto mantiene copias) están iguales: si divergen, reconciliar antes de seguir.

**Portabilidad (sin rutas de usuario)**:
- Ni configuraciones, archivos de servidores de herramientas (p. ej. MCP), scripts ni reglas llevan rutas absolutas con nombre de usuario o de máquina. Usar variables de entorno (`%USERPROFILE%`, `$HOME`, una variable del proyecto con fallback) o rutas relativas al proyecto.
- Al migrar de máquina o usuario: buscar con grep patrones de rutas de usuario en configuración, docs y scripts; confirmar que las rutas existen en la máquina actual; si algo estaba roto, dejar nota fechada de qué se rompió y desde cuándo.

## Ejemplos
- No: continuar editando tras ver el repo "detrás" del remoto, o ejecutar `reset --hard` ante una divergencia.
- No: una config con `C:\Users\<nombre>\proyecto\...` literal.
- Sí: `git fetch`, comparar, leer la última bitácora, y rutas como `./mcp/...` o `%USERPROFILE%`.

## Qué se ajusta por proyecto
- Entornos y máquinas reales (producción, remotos) y cómo comprobar la versión que corre en cada uno.
- Dónde viven la bitácora y la memoria compartida en el repo.
- Rama de trabajo y política de ramas.
- Qué máquina puede compilar o probar qué (limitaciones de entorno), registrado en el proyecto.
- Variable de entorno raíz y patrón de grep para detectar rutas de usuario.
