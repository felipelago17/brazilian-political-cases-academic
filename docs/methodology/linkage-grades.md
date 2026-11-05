# Linkage grades

Any connection between a **signal** (a bill, a CPI, an impeachment request, a public statement, a foreign sanction or tariff) and an **action** (a court decision, a TCU or CGU act, a delisting, a legislative vote) is recorded in `trackers/linkages.yaml` with one of three grades. Temporal proximity alone is never sufficient.

| Grade | Definition | Example |
|---|---|---|
| `statutory-mandate` | A statute or binding legal requirement explicitly directs or constrains the action. | Mandatory loss of office on final conviction (Constitution art. 55); ineligibility under the Ficha Limpa law. |
| `documented-request` | The acting institution, in its own document, cites the signal as a reason for or context of the action. | A judgment that records a defendant's efforts to obtain foreign sanctions (AP 2782); a TCU acórdão that cites a CPI report. |
| `proximity-only` | The signal and action are topically or temporally related, but no documentary evidence of linkage exists. **No inference of causation is drawn.** | A foreign designation shortly before or after a conviction; a bill filed near a ruling. |

## Rules

- Prefer the strongest grade that is fully supported by Tier 1 sources.
- Always include at least one primary-source URL or citation in `evidence`.
- If the grade is `proximity-only`, `notes` must state that no inference is drawn.
- Aggregation is by party, institution or branch. No per-person scorecards.
- The direction of a linkage is recorded as `signal → action`; the grade never asserts motive.
