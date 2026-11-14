# Checklist: verificar tras cada delegación

Marcar cada punto antes de usar el informe. Releer el informe no cuenta.

- [ ] 1. **Forma**: trae el formato pedido, `archivo:línea` y la sección "No verificado". Si falta algo, rechazar y devolver.
- [ ] 2. **Releer lo citado**: abrir cada archivo y línea mencionados. Buscar lo que el informe **omite**: rutas inventadas, resultados "probables" sin evidencia. Medir con cifra propia lo que afirma.
- [ ] 3. **Repetir por cuenta propia** los comandos de solo lectura y las pruebas. Las cifras del agente no sustituyen a las propias.
- [ ] 4. **Si editó**: diff completo; nada fuera del alcance pedido; sin restos de depuración o mutación (`if False`, `or True`, validaciones comentadas); sin secretos; sin commit.
- [ ] 5. **Si llega a pantalla o ejecutable**: mirarlo de verdad.
- [ ] 6. **Decidir**: aceptar lo comprobado, corregir lo parcial, descartar lo refutado. Máximo 2 rondas de corrección delegada; después lo hace el principal.
- [ ] 7. **Informar** con tres bloques: verificado por mí / reportado por el agente sin confirmar / refutado. Indicar rol y modelo aplicado.

## Plantilla del informe al usuario
```
Verificado por mí: <hecho> (<archivo:línea o comando>)
Reportado por el agente, sin confirmar: <afirmación>
Refutado: <afirmación> -> <cifra o evidencia propia>
Agente: <rol>, <modelo y esfuerzo realmente aplicados>
```
