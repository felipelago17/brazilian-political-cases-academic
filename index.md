---
layout: default
title: Home
---
[Home](./) · [English](cases.html) · [Português](cases_pt.html) · [Español](cases_es.html) · [Fork](https://github.com/felipelago17/brazilian-political-cases-academic/fork)

# Brazilian Political Cases – Academic Tracker

**English** · [Português](index_pt.html) · [Español](index_es.html)

Academic compilation of publicly reported legal cases involving major Brazilian political figures and institutions.

**Status as of 31 October 2026**

## Purpose

This repository documents publicly reported cases for research and academic reference. It is not affiliated with any political party, candidate, government, or judicial authority.

Every entry includes:
- At least one independent public source link
- Notes on the availability of the official court or prosecutor decision (and how to obtain it)

## Contents

- [`tracker.py`](tracker.py) – Structured data of the cases (single source of truth)
- [Cases – English](cases.html) – Readable tables
- [Casos – Português](cases_pt.html)
- [Casos – Español](cases_es.html)

## Methodology

Sources are limited to mainstream press, legal outlets, Agência Brasil, official court/government/legislative sites, and US DOJ/Treasury. Partisan and openly campaigning outlets are excluded.

**Presumption of innocence:** Allegations and investigations are not findings of guilt. This is not legal advice.

## Related open-data projects

This tracker records **cases** (allegations, investigations, convictions). Complementary Brazilian civic-tech projects measure **indicators** from open government data and are useful as a quantitative layer alongside the case timelines:

- [Operação Serenata de Amor](https://github.com/okfn-brasil/serenata-de-amor) (Open Knowledge Brasil, 2016–; MIT) — *Rosie*, a classifier that assigns a suspicion score to each congressional expense-quota (CEAP) reimbursement, and *Jarbas*, the API/dashboard that publishes flagged items for citizen validation. The project is largely dormant, but the method — unsupervised anomaly scoring over official reimbursement data, published with the underlying receipt — is the reference design for any "measurable irregularity" indicator here. Companion package: [serenata-toolbox](https://github.com/okfn-brasil/serenata-toolbox).
- [Querido Diário](https://github.com/okfn-brasil/querido-diario) (Open Knowledge Brasil; active) — scrapes and searches municipal official gazettes; the live source for procurement and appointment notices.
- [FiscalizaJá — Dados Abertos](https://github.com/FiscalizaJa/dadosabertos) (2023–) — normalises Chamber and Senate quota data into a single schema in English.

Indicators from these sources would be reported separately from case entries and never read as evidence of guilt.

## Open source collaboration

This repository is open for contributions. Fork it, make your changes, and open a pull request.

[Fork the repository](https://github.com/felipelago17/brazilian-political-cases-academic/fork)

## Disclaimer

This repository is for educational and informational purposes only. Always verify against primary sources. License: [CC BY 4.0](LICENSE).
