# Taxonomía de situación

No se usan campos de situación en texto libre. Cada caso lleva tres campos controlados para que las entradas puedan filtrarse, contarse y compararse.

## Etapa (`stage`)

| Valor | Significado |
|---|---|
| `inquérito` | Investigación policial o fiscal abierta; sin acusación |
| `denúncia` | Acusación presentada por la fiscalía |
| `denúncia-recebida` | El tribunal admite la acusación; el imputado pasa a ser acusado |
| `instrução` | Fase probatoria |
| `sentença` | Sentencia de primera o única instancia dictada |
| `recurso` | En apelación |
| `trânsito-em-julgado` | Firme e inapelable |
| `encerrado` | Cerrado sin sentencia de fondo subsistente (ver resultado) |

## Resultado (`outcome`)

| Valor | Significado |
|---|---|
| `pendente` | Sin resultado aún |
| `condenação` | Condena |
| `absolvição` | Absolución en cuanto al fondo |
| `anulação` | Sentencia o proceso anulado (motivo procesal) |
| `prescrição` | Prescrito |
| `arquivamento` | Archivado (cualquier motivo; especificar en mecanismos) |
| `rejeição-da-denúncia` | Acusación rechazada |

## Mecanismos (`mechanisms`)

Lista abierta a partir de este vocabulario (en portugués, como en las fuentes): `incompetência` (falta de competencia), `suspeição` (parcialidad judicial), `nulidade-probatória` (prueba declarada inutilizable), `prescrição`, `revisão-criminal`, `anistia`, `delação-premiada` (colaboración eficaz), `acordo-de-leniência`, `foro-privilegiado`, `habeas-corpus`, `embargos`.

La combinación es lo que importa: `encerrado` + `arquivamento` + [`incompetência`, `prescrição`] dice con precisión lo que "cerrado" solía ocultar.

## Ítems regulatorios e institucionales

Toda entrada regulatoria o institucional lleva campos separados `announced` / `published` / `in_force` (y, cuando corresponda, `lifted`). Un anuncio nunca se trata como acto publicado.
