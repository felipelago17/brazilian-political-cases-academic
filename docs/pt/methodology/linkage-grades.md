# Graus de vínculo

Qualquer conexão entre um **sinal** (projeto de lei, CPI, pedido de impeachment, declaração pública, sanção ou tarifa estrangeira) e uma **ação** (decisão judicial, ato do TCU ou da CGU, remoção de lista, votação legislativa) é registrada em `trackers/linkages.yaml` com um de três graus. Proximidade temporal, por si só, nunca basta.

| Grau | Definição | Exemplo |
|---|---|---|
| `statutory-mandate` | Lei ou exigência jurídica vinculante determina ou condiciona expressamente a ação. | Perda do mandato por condenação definitiva (Constituição, art. 55); inelegibilidade pela Lei da Ficha Limpa. |
| `documented-request` | A instituição que age cita, em documento próprio, o sinal como razão ou contexto da ação. | Julgamento que registra os esforços de um réu para obter sanções estrangeiras (AP 2782); acórdão do TCU que cita relatório de CPI. |
| `proximity-only` | Sinal e ação têm relação temática ou temporal, mas não há evidência documental de vínculo. **Nenhuma inferência de causalidade é feita.** | Designação estrangeira pouco antes ou depois de uma condenação; projeto apresentado perto de uma decisão. |

## Regras

- Prefira o grau mais forte integralmente sustentado por fontes de nível 1.
- Inclua sempre ao menos uma URL ou citação de fonte primária em `evidence`.
- Se o grau for `proximity-only`, `notes` deve declarar que nenhuma inferência é feita.
- A agregação é por partido, instituição ou poder. Sem "placares" individuais.
- A direção do vínculo é registrada como `sinal → ação`; o grau nunca afirma motivação.
