# Resumen de piezas

> **Para una IA:** este resumen solo sirve para elegir. Antes de usar una pieza, **lee su archivo completo** (`SKILL.md` en cada carpeta de `skills/`, o el `.md` de la regla o el agente).

## 🧩 skills (49)

| Pieza | Para qué sirve |
|---|---|
| [`aclarar-pedido`](skills/aclarar-pedido/SKILL.md) | Usar cuando un pedido del usuario es grande, vago o ambiguo (palabras como "listo", "todo", "mejora", "arregla", "como antes") o se va a ejecutar sin supervisión, y hay que convertirlo en un pedido c… |
| [`agent-harness-evals`](skills/agent-harness-evals/SKILL.md) | Usar cuando se diseñen evals de un agente, orquestador o subagentes, o cuando haya que decidir qué cuenta como evidencia de que "funciona" (capas de verificación, datasets dorados, holdout, métricas… |
| [`agent-memory`](skills/agent-memory/SKILL.md) | Usar cuando haya que decidir qué contexto duradero del proyecto guardar en una carpeta de memoria (`.memory/` o similar), cómo recuperarlo o cómo mantenerlo correcto entre sesiones. |
| [`auditoria-adversarial`](skills/auditoria-adversarial/SKILL.md) | Usar cuando se pida auditar un CLI o sistema completo, probar cada opción, permutación o variable, intentar romperlo o buscar qué falla, antes de declarar confiable un módulo o tras un cambio grande. |
| [`auditoria-integral`](skills/auditoria-integral/SKILL.md) | Usar cuando se pida auditar un proyecto completo de punta a punta (backend, frontend, servicios de IA e infraestructura) y accionar los hallazgos en lugar de solo reportarlos |
| [`bitacora-humana`](skills/bitacora-humana/SKILL.md) | Usar cuando hay que crear, ampliar, cerrar o revisar la bitácora humana del proyecto (archivos numerados por lotes de 6 a 9 mensajes del usuario con cita textual y cómo se entendieron), o cuando un m… |
| [`cerrar`](skills/cerrar/SKILL.md) | Usar cuando el usuario escribe /cerrar o pide cerrar la ronda de trabajo (verificar, documentar, guardar memoria, commit con push solo si está autorizado, e informe en pantalla). |
| [`changelog-generator`](skills/changelog-generator/SKILL.md) | Usar cuando se va a preparar un release, hay que actualizar el CHANGELOG, el usuario pregunta qué cambió desde la última versión, o se quiere validar que los mensajes de commit sigan Conventional Com… |
| [`cierre-de-ronda`](skills/cierre-de-ronda/SKILL.md) | Usar cuando una tarea, tanda o sesión produjo un resultado real y toca cerrarla (verificar, documentar, guardar memoria, commit, push si está autorizado e informe en pantalla), o cuando el usuario pi… |
| [`crear-agente-universal`](skills/crear-agente-universal/SKILL.md) | Usar cuando hay que crear un agente universal nuevo para el kit con el frontmatter estándar (Haiku 5.5, esfuerzo high, sin lanzar subagentes), solo lectura por defecto y un entregable de formato fijo… |
| [`crear-pieza-del-proyecto`](skills/crear-pieza-del-proyecto/SKILL.md) | Usar cuando el usuario aprobó convertir algo que se repite en una skill, regla o agente propios del proyecto y hay que escribirla en la carpeta `.claude/` del proyecto con la plantilla, validarla, re… |
| [`crear-prompt-para-ia`](skills/crear-prompt-para-ia/SKILL.md) | Usar cuando hay que escribir un prompt o instrucciones para que otra IA, otra sesión o un subagente ejecute una tarea sin ver esta conversación: convertir un pedido aclarado y un plan en un texto lar… |
| [`crear-regla-universal`](skills/crear-regla-universal/SKILL.md) | Usar cuando hay que crear una regla universal nueva para el kit (o reescribir una existente) con la plantilla estándar, 25 a 70 líneas, enlaces solo a reglas que existen, validada y registrada en el… |
| [`debugging-sistematico`](skills/debugging-sistematico/SKILL.md) | Usar cuando haya un bug, un test que falla, un fallo de importación o sincronización o un comportamiento inesperado, antes de proponer un fix (no después del segundo intento fallido) |
| [`deep-research`](skills/deep-research/SKILL.md) | Usar cuando se pida investigar a fondo arquitectura, referencias o alternativas y entregar una recomendación con evidencia trazable. |
| [`delegar-a-subagentes`](skills/delegar-a-subagentes/SKILL.md) | Usar cuando se va a delegar trabajo a uno o varios subagentes (lectura, búsqueda, auditoría, QA, piezas pequeñas) o cuando vuelve el informe de un subagente y hay que comprobarlo antes de usarlo. |
| [`detectar-piezas-repetidas`](skills/detectar-piezas-repetidas/SKILL.md) | Usar cuando se cierra una ronda o se lee la memoria del proyecto y hay que descubrir qué procesos, fallas o instrucciones se repiten y merecen convertirse en una skill, regla o agente propios del pro… |
| [`diagrams`](skills/diagrams/SKILL.md) | Usar cuando se pide crear o actualizar un diagrama técnico como código (arquitectura, secuencia, flujo, estados, ER) con Mermaid, elegir el tipo de diagrama correcto o mantenerlo veraz cuando el sist… |
| [`documentation-templates`](skills/documentation-templates/SKILL.md) | Usar cuando se redacta o revisa documentación: README, referencia de API, comentarios de código, changelog, registros de decisiones de arquitectura (ADR) o documentación pensada para agentes de IA |
| [`escribir-mensaje-de-commit`](skills/escribir-mensaje-de-commit/SKILL.md) | Usar cuando se va a escribir el mensaje de un commit o la descripción de un pull request (por orden del usuario), para que sea técnico y directo sobre lo que cambió y no lleve enlaces, correos ni lín… |
| [`estado-del-proyecto`](skills/estado-del-proyecto/SKILL.md) | Usar cuando se quiere ver de un vistazo cómo está el proyecto (lint, tipos, pruebas y auditoría de dependencias en un tablero pass/fail, más el estado de git), al empezar o cerrar una ronda, antes de… |
| [`evaluar-proyecto-y-objetivo`](skills/evaluar-proyecto-y-objetivo/SKILL.md) | Usar cuando hay que evaluar el estado de un proyecto y si un objetivo concreto encaja con él antes de planear o lanzar un trabajo largo: leer la memoria, los planes abiertos y las mejoras pendientes,… |
| [`flujos-de-trabajo`](skills/flujos-de-trabajo/SKILL.md) | Usar cuando el usuario pide un flujo, un paso a paso completo o "de principio a fin", o cuando la tarea tiene 4 o más pasos que mezclan responsables (asistente, usuario, servicio externo) |
| [`inicio-de-sesion`](skills/inicio-de-sesion/SKILL.md) | Usar cuando se arranca una sesión de trabajo real en un proyecto (sobre todo si se trabaja desde más de una máquina o herramienta), al migrar de máquina o usuario, o cuando algo "no cuadra" con lo qu… |
| [`interpretar-ejemplos`](skills/interpretar-ejemplos/SKILL.md) | Usar cuando el usuario da ejemplos en su pedido ("por ejemplo", "tipo", "como", "algo así", "ejemplo:") y hay que decidir qué hacer con ellos: entender el criterio que ilustran en lugar de tomarlos c… |
| [`investigacion-web`](skills/investigacion-web/SKILL.md) | Usar cuando se investiga una librería, herramienta o API de terceros antes de integrarla, se comparan opciones, se verifica si un dato sigue vigente o cambió con la versión, o se hace un panorama de… |
| [`lista-de-protegidos`](skills/lista-de-protegidos/SKILL.md) | Usar cuando hay que definir o actualizar la lista de archivos o módulos protegidos de un proyecto, antes de editar un archivo que podría estar en ella, al pedir permiso para tocar uno, o cuando se de… |
| [`mapa-de-areas`](skills/mapa-de-areas/SKILL.md) | Usar cuando hay que crear, actualizar o validar el mapa área a skills, reglas y agentes de un proyecto, o configurar el aviso por hook que recuerda qué invocar al tocar cada área, o cuando se añade u… |
| [`memoria-del-proyecto`](skills/memoria-del-proyecto/SKILL.md) | Usar cuando hay que crear, leer, actualizar o podar la memoria durable del proyecto (la carpeta `.memory/` de la raíz) para que otra sesión, máquina o herramienta recupere el estado, las decisiones,… |
| [`metodologia-dev`](skills/metodologia-dev/SKILL.md) | Usar cuando se planifica una funcionalidad con especificación previa, se escriben specs, changelog o documentación, se diagnostica un bug difícil, se revisa un cambio ya implementado o se resuelven c… |
| [`organizar-docs`](skills/organizar-docs/SKILL.md) | Usar cuando hay que crear u ordenar la carpeta docs/ de un proyecto, decidir si un documento es vigente o foto fechada, archivar documentación obsoleta, montar el índice raíz con la próxima auditoría… |
| [`patrones-de-orquestacion`](skills/patrones-de-orquestacion/SKILL.md) | Usar cuando se diseña una tarea nueva de un orquestador multi-agente, al escalar de una tarea secuencial a varias, o al decidir cómo debe fallar y reintentar un subagente. |
| [`plan`](skills/plan/SKILL.md) | Usar cuando el usuario escribe /plan o pide explícitamente un plan con fases, metas y casillas antes de construir un trabajo mediano o grande (crear el plan y esperar la luz verde, sin ejecutar nada). |
| [`plan-con-casillas`](skills/plan-con-casillas/SKILL.md) | Usar cuando una tarea mediana o grande (tres o más archivos, varias metas, o más de una sesión) necesita un plan escrito con fases, metas y casillas antes de construir (partir un trabajo grande en tr… |
| [`preparar-goal`](skills/preparar-goal/SKILL.md) | Usar cuando el usuario quiere que la IA trabaje sola hasta terminar una tarea (el comando /goal de Claude Code o de Codex, o un objetivo persistente equivalente) y hay que prepararlo antes: evaluar e… |
| [`qa-bugs-y-triage`](skills/qa-bugs-y-triage/SKILL.md) | Usar cuando se encontró un fallo y hay que reportarlo bien, cuando una prueba falla a veces (inestable/flaky) o al cerrar un informe de QA |
| [`qa-exploratorio-y-simulador`](skills/qa-exploratorio-y-simulador/SKILL.md) | Usar cuando se quiere probar "como una persona", tras cambios grandes de UX o comandos, o para buscar bugs que un guion no encuentra |
| [`qa-plan-y-casos`](skills/qa-plan-y-casos/SKILL.md) | Usar cuando se agrega una función o requisito, al decidir qué probar o al armar el informe de una fase |
| [`regression-test-counterfactual`](skills/regression-test-counterfactual/SKILL.md) | Usar cuando se arregló un bug o un test se ve sospechosamente verde, para probar que el test de regresión realmente detecta el defecto - control known-bad mínimo, rojo por la razón correcta y vuelta… |
| [`retomar`](skills/retomar/SKILL.md) | Usar cuando el usuario escribe /retomar o pide ponerse al día al empezar una sesión (dónde quedamos, qué cambió y qué está pendiente), sin cambiar nada hasta que lo diga. |
| [`revision-tecnica`](skills/revision-tecnica/SKILL.md) | Usar cuando se pide auditar de punta a punta (no un diff) un módulo o área en seguridad, arquitectura o rendimiento, revisar un RFC/ADR/propuesta ya escrita, generar un diagrama ER, puntuar la prepar… |
| [`seguridad-secretos`](skills/seguridad-secretos/SKILL.md) | Usar cuando se vaya a commitear, hacer push o compartir archivos, y haya que escanear en busca de claves, tokens, credenciales o datos sensibles filtrados; o al auditar un repositorio por secretos ex… |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Usar cuando hay que crear una skill nueva del kit, mejorar o fusionar una existente, validarla o revisar su calidad, o cuando un flujo repetido merece convertirse en skill. |
| [`skill-review`](skills/skill-review/SKILL.md) | Usar cuando se audite, adapte, fusione o retire una skill de un proyecto, o se evalúe una colección externa de skills antes de adoptarla (activación, utilidad, solapamiento, dependencias, seguridad,… |
| [`spec-driven-workflow`](skills/spec-driven-workflow/SKILL.md) | Usar cuando se va a construir una función sustantiva y hay que escribir la especificación antes del código, definir criterios de aceptación, o convertir requisitos confirmados en un plan de implement… |
| [`spec-miner`](skills/spec-miner/SKILL.md) | Usar cuando hay que entender un sistema heredado o sin documentación, derivar requisitos desde el código existente, dar IDs de requisito a QA, documentar un módulo sin docs o contrastar un documento… |
| [`template-skill`](skills/template-skill/SKILL.md) | Usar cuando se va a crear una skill nueva del kit y se necesita la plantilla lista para copiar (frontmatter, cuerpo, carpetas) |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Usar cuando se implementa lógica nueva, se arregla un bug o se cambia el comportamiento de algo existente y hay que demostrar con pruebas que funciona (escribir primero la prueba que falla, reproduci… |
| [`testing-qa`](skills/testing-qa/SKILL.md) | Usar cuando se vaya a decidir si un cambio está listo para commit (ship / ship con mitigación / hold), se verifique un cambio de UI en el navegador, o se escriban pruebas pytest con fixtures, mocks,… |

## 📏 rules (30)

| Pieza | Para qué sirve |
|---|---|
| [`actitud-autonomia`](rules/actitud-autonomia.md) | Buscar la manera, no decir «no se puede»; autonomía dentro de lo concedido |
| [`archivos-protegidos`](rules/archivos-protegidos.md) | Los archivos protegidos no se tocan sin permiso explícito y fresco |
| [`bitacora-humana`](rules/bitacora-humana.md) | Bitácora humana: el mensaje textual del usuario y la interpretación, por lotes |
| [`cierre-de-ronda`](rules/cierre-de-ronda.md) | Cada ronda con resultado real se cierra con docs, memoria, verificación e informe |
| [`clean-code`](rules/clean-code.md) | Código limpio: simple, claro y sin duplicar conocimiento |
| [`commits-tecnicos-sin-enlaces`](rules/commits-tecnicos-sin-enlaces.md) | El mensaje de un commit es técnico y directo: sin enlaces, correos ni líneas de sesión |
| [`continuidad-multi-maquina`](rules/continuidad-multi-maquina.md) | Continuidad entre máquinas y herramientas: no arrancar a ciegas, no hardcodear rutas |
| [`docs-organizacion-y-fechada`](rules/docs-organizacion-y-fechada.md) | Docs: un lugar por tipo, lo vigente se corrige y lo fechado no se toca |
| [`documentar-en-vivo`](rules/documentar-en-vivo.md) | Se documenta en el momento, no al final de la tanda |
| [`documentar-fallas`](rules/documentar-fallas.md) | Toda falla se escribe con su dato exacto; la que vuelve se automatiza |
| [`ejemplos-son-ilustrativos`](rules/ejemplos-son-ilustrativos.md) | Un ejemplo que da el usuario ilustra una idea: no es la lista, ni el orden, ni lo único |
| [`investigacion-y-referencias`](rules/investigacion-y-referencias.md) | Investigar sobre el código real y documentarlo; las referencias son solo lectura y se aprovechan por fragmentos |
| [`invocar-skills-reglas-agentes`](rules/invocar-skills-reglas-agentes.md) | Skills, reglas y agentes se invocan por ÁREA, sin esperar a que "parezca necesario" |
| [`leer-y-responder-cada-mensaje`](rules/leer-y-responder-cada-mensaje.md) | Leer el mensaje entero, responder cada parte y no exceder el alcance |
| [`lo-repetido-se-vuelve-pieza`](rules/lo-repetido-se-vuelve-pieza.md) | Lo que se repite se propone como pieza propia del proyecto; se crea solo con aprobación |
| [`memoria-del-proyecto`](rules/memoria-del-proyecto.md) | Cada proyecto lleva una memoria durable en `.memory/` que cualquier sesión lee primero |
| [`niveles-de-madurez`](rules/niveles-de-madurez.md) | La profundidad de la calidad depende del nivel de madurez que declara el proyecto |
| [`no-asumir-separar-confirmado`](rules/no-asumir-separar-confirmado.md) | No asumir: separar lo confirmado de lo supuesto, y el código manda sobre la documentación |
| [`objetivos-persistentes-verificables`](rules/objetivos-persistentes-verificables.md) | Un objetivo que la IA persigue sin supervisión lleva plan, fin medible, tope y verificación propia |
| [`pedidos-sin-ambiguedad`](rules/pedidos-sin-ambiguedad.md) | Un pedido grande o vago se aclara antes de ejecutarlo: objetivo, fin medible y alcance |
| [`piezas-sin-metadatos`](rules/piezas-sin-metadatos.md) | Una pieza lleva solo lo que necesita para funcionar: sin autor, fecha, licencia ni origen |
| [`planes-con-casillas`](rules/planes-con-casillas.md) | Plan con fases, metas y casillas antes de actuar (trabajo mediano o grande) |
| [`publicar-solo-con-orden`](rules/publicar-solo-con-orden.md) | Crear el repositorio, hacer commit y hacer push solo cuando el usuario lo diga, cada vez |
| [`qa-independiente-y-oraculos`](rules/qa-independiente-y-oraculos.md) | QA independiente, con oráculo, contraprueba y cobertura honesta |
| [`respuestas-concisas`](rules/respuestas-concisas.md) | Textos cortos: si necesita un párrafo para explicarse, se arregla el diseño |
| [`secretos`](rules/secretos.md) | Los secretos no se muestran, no se suben y no se hornean |
| [`seguridad-despliegue-y-datos`](rules/seguridad-despliegue-y-datos.md) | Nada remoto ni sobre datos reales sin autorización explícita en el mensaje actual |
| [`subagentes-max-3-y-verificar`](rules/subagentes-max-3-y-verificar.md) | Subagentes: máximo 3, sin anidar, Haiku 5.5 high, y el principal verifica todo |
| [`usuario-declara-listo`](rules/usuario-declara-listo.md) | Solo el usuario declara listo el producto: se reportan hechos observables (las metas y planes los cierra el asistente con evidencia) |
| [`verificacion-empirica`](rules/verificacion-empirica.md) | Verificar con evidencia real antes de dar algo por resuelto |

## 🤖 agents (15)

| Pieza | Para qué sirve |
|---|---|
| [`analisis`](agents/analisis.md) | Análisis e investigación de solo lectura sobre el código propio y su documentación |
| [`auditoria`](agents/auditoria.md) | Auditoría de solo lectura. Verifica afirmaciones (de otros agentes, de documentación o de un informe) contra el código y el comportamiento real, y revisa riesgos de seguridad y de efectos irreversibl… |
| [`correccion`](agents/correccion.md) | Corrección acotada. Aplica un arreglo YA ESPECIFICADO por el hilo principal (archivo exacto, qué cambiar, patrón a seguir, test esperado) sobre código no crítico. No diseña ni decide arquitectura. Ús… |
| [`depuracion`](agents/depuracion.md) | Depuración de un bug puntual ya reportado |
| [`docs-maintainer`](agents/docs-maintainer.md) | Mantiene la documentación y la memoria del proyecto sin tocar código |
| [`experimentos`](agents/experimentos.md) | Experimentación aislada (R&D): probar integraciones, APIs externas, IA, scraping, herramientas MCP o ideas nuevas antes de que entren al sistema, todo dentro de una carpeta de laboratorio |
| [`generacion`](agents/generacion.md) | Generación de archivos NUEVOS a partir de una especificación del hilo principal (documentación, fichas, casos de prueba, fixtures ficticios, plantillas) sin modificar código existente |
| [`investigador`](agents/investigador.md) | Investiga con fuentes. Lee código de repos de referencia, documentación oficial o la web y devuelve un informe con citas (archivo:línea o URL con fecha). No edita el proyecto. Indica siempre lo que n… |
| [`planificador`](agents/planificador.md) | Convierte un pedido mediano o grande en un plan escrito con fases, metas y casillas (usando la skill plan-con-casillas), lo valida y lo devuelve para luz verde |
| [`qa`](agents/qa.md) | QA independiente con evidencia reproducible |
| [`qa-adversarial`](agents/qa-adversarial.md) | Intenta ROMPER el sistema a propósito con lo que nadie debería hacer y alguien hará: valores imposibles, texto hostil, impaciencia, estados ilegales, concurrencia |
| [`qa-explorador`](agents/qa-explorador.md) | Tester exploratorio que se comporta como una persona, con una misión (charter) y un tiempo acotado |
| [`qa-regresion`](agents/qa-regresion.md) | Guardián de regresión. Ejecuta una batería repetible de humo (smoke), regresión y valores esperados independientes, y confirma con evidencia que lo que ya funcionaba sigue funcionando. Detecta prueba… |
| [`revisor`](agents/revisor.md) | Revisor técnico (puerta de control) que frena antes de cerrar una tarea o desplegar |
| [`seguridad`](agents/seguridad.md) | Auditoría de seguridad de solo lectura. Busca lo que se filtra sin que nadie lo note: secretos en código, logs, comandos, healthchecks e historial de git; endpoints sin autenticación o sin límites; e… |
