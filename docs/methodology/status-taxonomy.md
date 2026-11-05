# Status taxonomy

Free-text status fields are not used. Every case carries three controlled fields so that entries can be filtered, counted and compared.

## Stage (`stage`)

| Value | Meaning |
|---|---|
| `inquérito` | Police or prosecutorial inquiry open; no charges |
| `denúncia` | Charges filed by the prosecution |
| `denúncia-recebida` | Court has accepted the charges; defendant becomes réu |
| `instrução` | Evidence phase |
| `sentença` | First-instance or single-instance judgment delivered |
| `recurso` | Under appeal |
| `trânsito-em-julgado` | Final and unappealable |
| `encerrado` | Closed without a surviving merits judgment (see outcome) |

## Outcome (`outcome`)

| Value | Meaning |
|---|---|
| `pendente` | No outcome yet |
| `condenação` | Conviction |
| `absolvição` | Acquittal on the merits |
| `anulação` | Judgment or proceedings annulled (procedural ground) |
| `prescrição` | Time-barred |
| `arquivamento` | Archived (any ground; specify in mechanisms) |
| `rejeição-da-denúncia` | Charges rejected |

## Mechanisms (`mechanisms`)

Open list drawn from this vocabulary: `incompetência` (lack of jurisdiction), `suspeição` (judicial bias), `nulidade-probatória` (evidence declared unusable), `prescrição`, `revisão-criminal`, `anistia`, `delação-premiada` (cooperation agreement), `acordo-de-leniência`, `foro-privilegiado`, `habeas-corpus`, `embargos`.

The combination matters: `encerrado` + `arquivamento` + [`incompetência`, `prescrição`] says precisely what "closed" used to hide.

## Regulatory and institutional items

Every regulatory or institutional entry carries separate `announced` / `published` / `in_force` (and, where relevant, `lifted`) fields. An announcement is never treated as a published act.
