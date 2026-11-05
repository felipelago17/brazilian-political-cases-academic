# Grados de vínculo

Toda conexión entre una **señal** (proyecto de ley, CPI, solicitud de impeachment, declaración pública, sanción o arancel extranjero) y una **acción** (decisión judicial, acto del TCU o la CGU, retiro de una lista, votación legislativa) se registra en `trackers/linkages.yaml` con uno de tres grados. La proximidad temporal por sí sola nunca basta.

| Grado | Definición | Ejemplo |
|---|---|---|
| `statutory-mandate` | Una ley o exigencia jurídica vinculante ordena o condiciona expresamente la acción. | Pérdida del mandato por condena firme (Constitución, art. 55); inelegibilidad bajo la Ley de Ficha Limpa. |
| `documented-request` | La institución que actúa cita, en su propio documento, la señal como razón o contexto de la acción. | Una sentencia que registra los esfuerzos de un acusado por obtener sanciones extranjeras (AP 2782); un acórdão del TCU que cita un informe de CPI. |
| `proximity-only` | Señal y acción guardan relación temática o temporal, pero no existe evidencia documental de vínculo. **No se infiere causalidad.** | Una designación extranjera poco antes o después de una condena; un proyecto presentado cerca de un fallo. |

## Reglas

- Prefiera el grado más fuerte plenamente sustentado por fuentes de nivel 1.
- Incluya siempre al menos una URL o cita de fuente primaria en `evidence`.
- Si el grado es `proximity-only`, `notes` debe declarar que no se hace inferencia alguna.
- La agregación es por partido, institución o poder. Sin "marcadores" individuales.
- La dirección del vínculo se registra como `señal → acción`; el grado nunca afirma motivación.
