# Crear el repositorio, hacer commit y hacer push solo cuando el usuario lo diga, cada vez

> Aplica a: todo proyecto con repositorio. Reglas relacionadas: [[secretos]], [[commits-tecnicos-sin-enlaces]], [[cierre-de-ronda]], [[usuario-declara-listo]], [[leer-y-responder-cada-mensaje]], [[seguridad-despliegue-y-datos]].

Crear un repositorio remoto, hacer `commit`, hacer `push`, etiquetar o cambiar su visibilidad son acciones que **solo se hacen cuando el usuario lo ordena en ese momento**, una por una. Un repositorio nuevo nace **privado**, con el nombre que el usuario diga; sin nombre, no se crea.

## Por qué
Subir algo a un remoto es una publicación: queda copiado aunque se borre, y un repositorio público indexa lo que contenga. Una autorización dada una vez se tomó como patrón recurrente y el cierre de ronda se interpretó como permiso para subir.

## Cómo se aplica
- **Una orden por acción y por turno:** "crea el repo" no autoriza el primer commit; "haz commit" no autoriza el push; "push" a una rama no vale para otra. Ni el cierre de ronda ni un plan aprobado lo incluyen.
- **Repositorio nuevo:** nombre, cuenta o titular y visibilidad los dice el usuario; por defecto **privado**; pasarlo a público exige otra orden explícita aparte, después de revisar su contenido.
- **Antes de pedir la orden**, se deja preparado: lista de archivos que entrarían, escaneo de secretos, rutas de usuario y datos personales, y el mensaje de commit propuesto ([[secretos]]). La lista se muestra; no se sube.
- **Sin orden, se puede** preparar carpetas, correr el escaneo en modo informe y probar en una copia temporal fuera del repositorio.
- **Nunca** `--force`, `--no-verify` ni reescribir historial sin orden aparte.
- Si el push o la creación fallan, se informa el estado exacto; no se dice que quedó publicado.

## Ejemplos
- No: "Dejé el repositorio creado y subido para ahorrarte tiempo."
- Sí: "Está todo preparado en `publico/` y el escaneo no halló nada. Cuando quieras, dime el nombre y lo creo privado; el commit y el push los hago cuando me lo ordenes."

## Qué se ajusta por proyecto
- Cuenta o titular, nombre y visibilidad inicial del repositorio.
- Formato del mensaje de commit y qué escaneo se corre antes.
- Si el proyecto tiene una regla propia más estricta (por ejemplo, un repositorio público con lista blanca).
