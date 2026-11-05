# Brazil Accountability Tracker

*(repository: `brazilian-political-cases-academic` — rename to `brazil-accountability-tracker` pending)*

Academic, source-tiered record of **legal cases, institutional actions, legislative signals and foreign measures** involving Brazilian public figures and institutions — across parties and branches — with any connection between them recorded only as a graded linkage.

Site: https://felipelago17.github.io/brazilian-political-cases-academic/ (English · Português · Español)

**Not legal advice. Presumption of innocence applies to every entry.** Not affiliated with any party, candidate, government or court.

## Layout

```
trackers/            YAML — single source of truth (rows added by pull request, Tier 1 source required)
  cases.yaml                 legal cases (stage × outcome × mechanism)
  foreign-actions.yaml       OFAC, visas, tariffs, FCPA — foreign measures touching Brazil
  linkages.yaml              graded signal → action connections
  legislative-signals.yaml   curated bills/CPIs/impeachment requests + daily-scan keywords
  institutional-actions.yaml TCU / CGU / CADE / leniency (phase 3)
  presidential-documents.yaml, agency-releases.yaml   targets for the US-side scrapers
scripts/
  build_pages.py             YAML → docs/{,pt/,es/} tables
  fetch_brazil_legislature.py Câmara + Senado open-data keyword scan (no key)
  fetch_federal_register.py  US presidential documents, Brazil-filtered (no key)
  fetch_agency_releases.py   OFAC / DOJ / BIS releases, Brazil-filtered (no key)
docs/                MkDocs Material site; generated pages are overwritten by the scripts
data/                JSON outputs of the daily scans
tracker.py           Python loader over the YAML
REVIEW-2026-11.md    review and phased roadmap
```

## Method

- **Signals and actions, not "influence."** Connections appear only in `linkages.yaml` with a grade (`statutory-mandate` / `documented-request` / `proximity-only`); proximity alone is never sufficient.
- **Tiered sources.** Tier 1 official records (STF, STJ, TSE, TCU, CGU, DOU, Câmara/Senado, OFAC, Federal Register); Tier 2 official news agencies; Tier 3 press, labelled. Campaigning outlets excluded.
- **Controlled vocabulary** for case stage, outcome and mechanism.
- **Coverage follows the record**, whatever the party. Aggregation by party and institution only; no per-person scorecards.

## Automation

Four workflows run daily (08:00–08:20 UTC) and on relevant pushes: legislature scan, Federal Register, agency releases, and page regeneration; a fifth deploys the site. Each scraper has a `targets` list so a missing official link resolves itself on the next run.

## Contributing

Fork, edit `trackers/*.yaml` following the schema comments and the methodology pages, and open a pull request. See `REVIEW-2026-11.md` for the roadmap and open decisions.

## Licence

Documentation and original analysis: [CC BY 4.0](LICENSE).
