---
hide:
  - toc
---

# Brazil Accountability Tracker

**English** · [Português](pt/index.md) · [Español](es/index.md)
{ .lang-bar }

An academic, source-tiered record of **legal cases, institutional actions, legislative signals and foreign measures** involving Brazilian public figures and institutions — across parties and branches — with any connection between them recorded only as a graded linkage.
{ .lead }

!!! warning "Not legal advice"
    **Presumption of innocence applies to every entry.** This site is not affiliated with any party, candidate, government or court.

## What is tracked

<div class="grid cards" markdown>

-   :material-gavel: **[Cases](cases.md)**

    ---

    Criminal, civil and electoral cases against public figures. Live: 7 matters, migrating from the original list.

-   :material-earth: **[Foreign actions](foreign-actions.md)**

    ---

    US and other foreign measures: OFAC designations and delistings, visa actions, tariffs, FCPA resolutions. Live: the Magnitsky lifecycle and the 2025 tariff.

-   :material-link-variant: **[Linkages](linkages.md)**

    ---

    Graded signal → action connections. Live.

-   :material-bank: **[Legislative signals](trackers/legislature.md)**

    ---

    Bills, PECs, CPIs and impeachment requests from Câmara and Senado open data. Automated daily (candidates); curated rows by pull request.

-   :material-file-document-outline: **[US presidential documents](trackers/presidential-documents.md)**

    ---

    Executive orders, proclamations and memoranda from the Federal Register, Brazil-filtered. Automated daily.

-   :material-shield-search: **[US agency releases](trackers/agency-releases.md)**

    ---

    OFAC, DOJ and BIS releases, Brazil-filtered. Automated daily.

</div>

### Planned

<div class="grid cards" markdown>

-   **Institutional actions**

    ---

    TCU, CGU sanction lists, CADE, leniency agreements.

    Phase 3
    { .planned }

-   **Elections 2026**

    ---

    TSE rulings, ineligibilities, candidacies.

    Phase 4
    { .planned }

-   **Indicators**

    ---

    Open-data anomaly layers (Serenata, Querido Diário); reported separately, never as evidence.

    Phase 4
    { .planned }

</div>

## Method

- **Signals and actions, not "influence."** Connections appear only in a graded `linkage` field — see [Linkage grades](methodology/linkage-grades.md).
- **Tiered sources.** Official records first; press labelled as secondary; campaigning outlets excluded — see [Source hierarchy](methodology/source-hierarchy.md).
- **Controlled vocabulary.** Stage × outcome × mechanism instead of "closed" — see [Status taxonomy](methodology/status-taxonomy.md).
- **Coverage follows the record.** Whoever appears in a Tier 1 action is recorded, whatever their party. Aggregation by party and institution only.
- **Single source of truth.** `trackers/*.yaml`; the three language versions are generated.

## Contribute

Fork, add or correct a row in `trackers/*.yaml` with a Tier 1 source, and open a pull request. The [review and roadmap](https://github.com/felipelago17/brazilian-political-cases-academic/blob/main/REVIEW-2026-11.md) describes the phases.

## Licence

CC BY 4.0. Always verify against primary sources.
