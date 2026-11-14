---
name: testing-qa
description: Usar cuando se vaya a decidir si un cambio está listo para commit (ship / ship con mitigación / hold), se verifique un cambio de UI en el navegador, o se escriban pruebas pytest con fixtures, mocks, fechas congeladas, pruebas adversariales de seguridad o suite contra el motor real de base de datos.
---

# testing-qa

Describe el PROCESO para decidir y reportar pruebas, con patrones pytest reutilizables.

La regla `qa-independiente-y-oraculos` fija QUÉ debe cumplir el QA (agente aparte, oráculo, contraprueba, cobertura honesta). Esta skill cubre el CÓMO del día a día. Para QA independiente, delega en los agentes `qa`, `qa-adversarial`, `qa-explorador` y `qa-regresion`; esta skill no los reemplaza. Un "listo" lo declara el usuario (regla `usuario-declara-listo`); aquí se decide ship o hold sobre evidencia.

Para planificar la cobertura en una pasada grande (no en cada cambio), ver [references/coverage-strategy.md](references/coverage-strategy.md).

## 1. Decisión al terminar una tarea
Antes de cerrar con un vago "corrí los tests y quedó bien", elige una de estas tres y escríbela:
- **Ship**: probado a fondo y sin riesgo conocido.
- **Ship con mitigación**: funciona, pero hay un riesgo residual conocido; **nómbralo** ("no se probó con dos sucursales simultáneas; el diseño lo soporta").
- **Hold**: falta verificar algo concreto antes de hacer commit; di qué.

Añade el peldaño alcanzado (regla `verificacion-empirica`) y lo que NO se probó.

## 2. Verificación en navegador (acotada)
Evita las verificaciones lentas: si basta con DOM/JS o con una prueba quirúrgica, usa eso; abre el navegador completo solo para ver el render.
1. Abre la consola y la red antes de interactuar (errores, peticiones fallidas).
2. Primero el camino feliz; después 1-2 casos límite (vacío, error, otro rol).
3. Si falla, reporta con formato fijo: **pasos, esperado, real**; no "no funciona".
4. Cierra con ship / ship con mitigación / hold.

Error frecuente: comprobar solo que "no lanza error" sin contrastar el resultado esperado. Un cambio puede no fallar y mostrar la cifra equivocada: compara las cifras contra la fuente de verdad.

## 3. Fixtures y mocks pytest
- **Fixture de fábrica**: crea N instancias y las limpia al final.
  ```python
  @pytest.fixture
  def item_factory(db_session):
      creados = []
      def _make(codigo="T-001", **kw):
          o = Item(codigo=codigo, **kw)
          db_session.add(o); db_session.commit(); creados.append(o)
          return o
      yield _make
      for o in creados:
          db_session.delete(o)
      db_session.commit()
  ```
- **autouse** para reiniciar el estado global (limitador, caché) entre pruebas: `yield` y limpieza.
- **`monkeypatch`** para variables de entorno y atributos (`monkeypatch.setenv("API_KEY", "clave-falsa")`); se revierte solo.
- **`mocker`/`unittest.mock.patch`** para servicios externos: parchea en el módulo donde se USA la función, no donde se define.
- **`tmp_path`** para pruebas que escriben archivos.
- **`parametrize`** para varios casos sin duplicar: `@pytest.mark.parametrize("stock,cant,ok", [(10,5,True),(3,5,False),(0,1,False)])`.
- Datos ficticios siempre; las claves de prueba, evidentemente falsas (regla `secretos`).

## 4. Fechas con `freezegun`
Para código que usa `datetime.now()` (expiraciones, ventanas de tiempo, cierres), añade `freezegun` como dependencia de pruebas.
```python
from freezegun import freeze_time

@freeze_time("2026-01-05 10:00:00")
def test_token_expira_en_una_hora():
    assert crear_token(3600).expira_en == datetime(2026, 1, 5, 11, 0, 0)

def test_ventana():
    with freeze_time("2026-01-05 15:00:00") as t:
        job = crear_job(inicio="2026-01-05 13:00:00")
        assert not job.en_ventana()
        t.move_to("2026-01-05 16:30:00")
        assert job.en_ventana()
```
Limítalo a las pruebas ligadas al tiempo, no a toda la suite. Prueba los bordes exactos de cada ventana.

## 5. Pruebas adversariales de seguridad (sobre tu propio sistema)
Pruebas reales que ejercen las protecciones, no solo una lectura del código. Estructura sugerida (`tests/test_security_adversarial.py`):
- Inyección SQL en búsquedas y filtros (`' OR '1'='1`, `DROP TABLE`).
- XSS almacenado: guarda `<script>` tal cual y comprueba que la salida HTML lo escapa.
- JWT: `alg: none`, firma inválida, token expirado.
- IDOR horizontal (leer o modificar recursos de otro usuario o sucursal) y escalada vertical (rol bajo en endpoints de admin).
- CSRF en mutaciones con cookie de sesión; payloads enormes; path traversal (zip-slip, `..`).
- Rate limiting real: si las pruebas lo desactivan globalmente, actívalo de forma puntual y verifica el 429.
- Un script de humo de caja negra contra un servidor en marcha: **solo contra localhost o desarrollo**; nunca contra pruebas compartidas o producción sin autorización en el mensaje actual (regla `seguridad-despliegue-y-datos`).
- Una prueba dejada fallando a propósito documenta un hallazgo abierto; al corregirlo, anótalo como foto fechada, no como pendiente (regla `documentar-fallas`).

Para una auditoría de seguridad completa usa el agente `seguridad` (o una skill de auditoría de seguridad del proyecto, si la tiene).

## 6. Suite contra el motor real de base de datos
Una suite sobre SQLite en memoria es rápida, pero no detecta diferencias de dialecto (`with_for_update()`, tipos numéricos exactos, restricciones que otro motor sí valida). Conviene una pasada extra antes de un despliegue grande o al tocar escrituras concurrentes; no sustituye a la corrida rápida. La política detallada está en la regla `seguridad-despliegue-y-datos`.
```bash
docker compose -f docker/docker-compose.test.yml up -d     # motor descartable, puerto de pruebas, sin volumen
TEST_DATABASE_URL="postgresql://test:test@localhost:5433/test_db" python -m pytest tests/ -q
docker compose -f docker/docker-compose.test.yml down      # apagar al terminar
```
- El motor de pruebas nunca comparte puerto ni datos con el real.
- Las bases secundarias que también son SQLite en producción quedan fuera de esta pasada.
- Si el motor real exige una URL válida al importar, pásala aunque la fixture la reemplace.

## Cuándo NO usar
- Para escribir el QA independiente de un cambio grande (casos con ID, oráculo, informe): eso lo hacen los agentes `qa` y `qa-adversarial` con la regla `qa-independiente-y-oraculos`; esta skill es el cierre diario.
- Para planificar la cobertura de todo el sistema: `references/coverage-strategy.md` y `qa-plan-y-casos`.
- Para una auditoría de seguridad completa: el agente `seguridad` (o una skill de auditoría de seguridad del proyecto, si la tiene); la sección 5 cubre solo pruebas adversariales acotadas sobre tu propio sistema.
- Para cambios de solo documentación: no hay decisión de commit que tomar.

## Excusas → realidad
| Excusa | Realidad |
|---|---|
| "Corrí los tests y quedó bien" | La sección 1 pide escribir ship, ship con mitigación o hold, con el riesgo residual nombrado y lo no probado. |
| "Las pruebas pasan, no hace falta contraprueba" | El checklist pide romper el código a propósito y confirmar que las pruebas nuevas caen. |
| "La suite pasa en SQLite en memoria, basta" | La sección 6: SQLite no detecta diferencias de dialecto (`with_for_update()`, tipos numéricos, restricciones); antes de un despliegue grande se corre contra el motor real de pruebas. |
| "Abro el navegador completo por si acaso" | La sección 2: si basta DOM/JS o una prueba quirúrgica, se usa eso; el navegador completo solo cuando hay que ver el render. |
| "Dejo la prueba fallando y lo anoto como pendiente" | La sección 5: una prueba que falla a propósito documenta un hallazgo abierto; al corregirlo se anota como foto fechada. |

## Errores comunes
- Cerrar con un "quedó bien" sin decisión ship / mitigación / hold ni peldaño alcanzado.
- Comparar solo contra "no dio error" y no contra el resultado esperado real.
- Mockear en el módulo que define la función y no en el módulo de uso, o usar datos y claves reales en las pruebas.
- Pruebas de tiempo sin fecha congelada ni bordes.
- Compartir puerto o datos entre el motor de pruebas y el real.

## Checklist

- [ ] Decisión ship / ship con mitigación / hold escrita, con riesgo residual y lo no probado.
- [ ] Resultado comparado contra el esperado real, no solo ausencia de error.
- [ ] Pruebas nuevas verificadas con contraprueba (rompe el código y confirma que caen).
- [ ] Mocks en el módulo de uso; datos y claves ficticios.
- [ ] Pruebas de tiempo con fecha congelada y bordes.
- [ ] Cambios de seguridad o de escritura concurrente: adversarial y motor real corridos.
