# Taxonomia de situação

Não se usam campos de situação em texto livre. Cada caso traz três campos controlados, para que as entradas possam ser filtradas, contadas e comparadas.

## Fase (`stage`)

| Valor | Significado |
|---|---|
| `inquérito` | Inquérito policial ou procedimento investigatório em curso; sem denúncia |
| `denúncia` | Denúncia oferecida pelo Ministério Público |
| `denúncia-recebida` | Denúncia recebida pelo tribunal; o acusado torna-se réu |
| `instrução` | Fase probatória |
| `sentença` | Sentença de primeira instância ou de instância única proferida |
| `recurso` | Em grau de recurso |
| `trânsito-em-julgado` | Decisão definitiva, sem recurso cabível |
| `encerrado` | Encerrado sem julgamento de mérito subsistente (ver resultado) |

## Resultado (`outcome`)

| Valor | Significado |
|---|---|
| `pendente` | Sem resultado ainda |
| `condenação` | Condenação |
| `absolvição` | Absolvição no mérito |
| `anulação` | Sentença ou processo anulado (fundamento processual) |
| `prescrição` | Prescrição |
| `arquivamento` | Arquivado (qualquer fundamento; especificar nos mecanismos) |
| `rejeição-da-denúncia` | Denúncia rejeitada |

## Mecanismos (`mechanisms`)

Lista aberta com este vocabulário: `incompetência`, `suspeição`, `nulidade-probatória` (prova declarada imprestável), `prescrição`, `revisão-criminal`, `anistia`, `delação-premiada`, `acordo-de-leniência`, `foro-privilegiado`, `habeas-corpus`, `embargos`.

A combinação é o que importa: `encerrado` + `arquivamento` + [`incompetência`, `prescrição`] diz exatamente o que "encerrado" antes escondia.

## Itens regulatórios e institucionais

Toda entrada regulatória ou institucional traz campos separados de `announced` / `published` / `in_force` (e, quando cabível, `lifted`). Um anúncio nunca é tratado como ato publicado.
