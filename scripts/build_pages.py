#!/usr/bin/env python3
"""Generate the English, Portuguese and Spanish tracker pages from trackers/*.yaml.

Free text is authored in English; labels, headings and fixed vocabularies are translated
here. Run after any tracker change (the build-pages workflow does this on push).

Outputs: docs/cases.md, docs/foreign-actions.md, docs/linkages.md and the same under docs/pt/ and docs/es/.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TR = ROOT / "trackers"
DOCS = ROOT / "docs"

L = {
    "en": {
        "cases_title": "Cases", "fa_title": "Foreign actions", "lk_title": "Linkages",
        "status": "Status as of", "presumption": "**Presumption of innocence.** Allegations and investigations are not findings of guilt. Not legal advice.",
        "matter": "Matter", "persons": "Persons", "affiliation": "Affiliation", "origin": "Origin", "forum": "Forum",
        "allegation": "Allegation", "stage": "Stage", "outcome": "Outcome", "mechanisms": "Mechanisms", "sources": "Sources",
        "timeline": "Timeline", "official": "Official record", "how": "How to retrieve", "reference": "Reference", "notes": "Notes",
        "date": "Date", "actor": "Actor", "instrument": "Instrument", "target": "Target", "summary": "Summary", "in_force": "In force",
        "signal": "Signal", "action": "Action", "grade": "Grade", "evidence": "Evidence",
        "cases_intro": "Legal cases involving Brazilian public figures and institutions, across parties and branches. Source of truth: `trackers/cases.yaml`. Stages and outcomes use the fixed vocabulary in [Status taxonomy](methodology/status-taxonomy.md).",
        "fa_intro": "Actions by foreign governments (chiefly the United States) touching Brazilian public figures, institutions or trade. These are actions; any connection to a Brazilian decision is graded in [Linkages](linkages.md).",
        "lk_intro": "Graded connections between a signal and an action. `proximity-only` entries draw no inference. See [Linkage grades](methodology/linkage-grades.md).",
        "yes": "yes", "no": "no", "lifted": "lifted", "tier": "T",
        "stage_v": {"inquérito": "inquiry", "denúncia": "charged", "denúncia-recebida": "charges accepted", "instrução": "trial phase", "sentença": "judgment", "recurso": "appeal", "trânsito-em-julgado": "final", "encerrado": "closed"},
        "outcome_v": {"pendente": "pending", "condenação": "conviction", "absolvição": "acquittal", "anulação": "annulment", "prescrição": "time-barred", "arquivamento": "archived", "rejeição-da-denúncia": "charges rejected"},
    },
    "pt": {
        "cases_title": "Casos", "fa_title": "Ações estrangeiras", "lk_title": "Vínculos",
        "status": "Situação em", "presumption": "**Presunção de inocência.** Acusações e investigações não são condenações. Não constitui aconselhamento jurídico.",
        "matter": "Caso", "persons": "Pessoas", "affiliation": "Filiação", "origin": "Origem", "forum": "Foro",
        "allegation": "Acusação", "stage": "Fase", "outcome": "Resultado", "mechanisms": "Mecanismos", "sources": "Fontes",
        "timeline": "Cronologia", "official": "Registro oficial", "how": "Como obter", "reference": "Referência", "notes": "Notas",
        "date": "Data", "actor": "Autor", "instrument": "Instrumento", "target": "Alvo", "summary": "Resumo", "in_force": "Em vigor",
        "signal": "Sinal", "action": "Ação", "grade": "Grau", "evidence": "Evidência",
        "cases_intro": "Casos judiciais envolvendo figuras públicas e instituições brasileiras, de todos os partidos e poderes. Fonte: `trackers/cases.yaml`. Fases e resultados seguem o vocabulário fixo da [taxonomia de situação](../methodology/status-taxonomy.md). Texto livre em inglês.",
        "fa_intro": "Ações de governos estrangeiros (sobretudo dos EUA) que afetam figuras públicas, instituições ou o comércio do Brasil. São ações; qualquer conexão com decisão brasileira é graduada em [Vínculos](linkages.md).",
        "lk_intro": "Conexões graduadas entre um sinal e uma ação. Entradas `proximity-only` não implicam inferência. Ver [graus de vínculo](../methodology/linkage-grades.md).",
        "yes": "sim", "no": "não", "lifted": "revogada", "tier": "N",
        "stage_v": {}, "outcome_v": {},
    },
    "es": {
        "cases_title": "Casos", "fa_title": "Acciones extranjeras", "lk_title": "Vínculos",
        "status": "Situación al", "presumption": "**Presunción de inocencia.** Las acusaciones e investigaciones no son condenas. No constituye asesoramiento jurídico.",
        "matter": "Caso", "persons": "Personas", "affiliation": "Afiliación", "origin": "Origen", "forum": "Foro",
        "allegation": "Acusación", "stage": "Etapa", "outcome": "Resultado", "mechanisms": "Mecanismos", "sources": "Fuentes",
        "timeline": "Cronología", "official": "Registro oficial", "how": "Cómo obtenerlo", "reference": "Referencia", "notes": "Notas",
        "date": "Fecha", "actor": "Autor", "instrument": "Instrumento", "target": "Objetivo", "summary": "Resumen", "in_force": "Vigente",
        "signal": "Señal", "action": "Acción", "grade": "Grado", "evidence": "Evidencia",
        "cases_intro": "Casos judiciales que involucran a figuras públicas e instituciones brasileñas, de todos los partidos y poderes. Fuente: `trackers/cases.yaml`. Etapas y resultados siguen el vocabulario fijo de la [taxonomía de situación](../methodology/status-taxonomy.md). Texto libre en inglés.",
        "fa_intro": "Acciones de gobiernos extranjeros (principalmente EE. UU.) que afectan a figuras públicas, instituciones o el comercio de Brasil. Son acciones; cualquier conexión con una decisión brasileña se gradúa en [Vínculos](linkages.md).",
        "lk_intro": "Conexiones graduadas entre una señal y una acción. Las entradas `proximity-only` no implican inferencia. Ver [grados de vínculo](../methodology/linkage-grades.md).",
        "yes": "sí", "no": "no", "lifted": "levantada", "tier": "N",
        "stage_v": {"inquérito": "investigación", "denúncia": "acusación", "denúncia-recebida": "acusación admitida", "instrução": "instrucción", "sentença": "sentencia", "recurso": "recurso", "trânsito-em-julgado": "firme", "encerrado": "cerrado"},
        "outcome_v": {"pendente": "pendiente", "condenação": "condena", "absolvição": "absolución", "anulação": "anulación", "prescrição": "prescrito", "arquivamento": "archivado", "rejeição-da-denúncia": "acusación rechazada"},
    },
}


def _load(name: str):
    return yaml.safe_load((TR / name).read_text(encoding="utf-8"))


def _src(sources: list[dict], t: dict) -> str:
    return "<br>".join(f"[{s.get('outlet','source')}]({s['url']}) ({t['tier']}{s.get('tier','?')})" for s in sources or [])


def _v(t: dict, key: str, val: str) -> str:
    return t.get(key, {}).get(val, val) or ""


def cases_page(lang: str, t: dict, today: str) -> str:
    cases = _load("cases.yaml")
    out = [f"# {t['cases_title']}", "", f"**{t['status']} {today}**", "", t["presumption"], "", t["cases_intro"], "",
           f"| {t['matter']} | {t['persons']} | {t['affiliation']} | {t['origin']} | {t['forum']} | {t['stage']} | {t['outcome']} | {t['mechanisms']} | {t['sources']} |",
           "|---|---|---|---|---|---|---|---|---|"]
    for c in cases:
        out.append(f"| [{c['matter']}](#{c['id']}) | {', '.join(c.get('persons', []))} | {c.get('affiliation','')} | {c.get('origin','')} | {c.get('forum','')} | "
                   f"{_v(t,'stage_v',c.get('stage',''))} | {_v(t,'outcome_v',c.get('outcome',''))} | {', '.join(c.get('mechanisms', []))} | {_src(c.get('sources'), t)} |")
    out.append("")
    for c in cases:
        out += [f"## {c['matter']} {{#{c['id']}}}", "", f"**{t['allegation']}.** {c.get('allegation','')}", ""]
        if c.get("timeline"):
            out += [f"**{t['timeline']}.**", ""] + [f"- {x.get('date','')} — {x.get('event','')}" for x in c["timeline"]] + [""]
        o = c.get("official") or {}
        link = f"[{o['reference']}]({o['link']})" if o.get("link") else f"{o.get('reference','')} — [portal]({o.get('portal','')})"
        out += [f"**{t['official']}.** {link}. {t['how']}: {o.get('how_to_retrieve','')}", ""]
        if c.get("notes"):
            out += [f"**{t['notes']}.** {c['notes']}", ""]
    return "\n".join(out)


def foreign_page(lang: str, t: dict, today: str) -> str:
    rows = _load("foreign-actions.yaml")
    out = [f"# {t['fa_title']}", "", f"**{t['status']} {today}**", "", t["fa_intro"], "",
           f"| {t['date']} | {t['actor']} | {t['instrument']} | {t['target']} | {t['in_force']} | {t['summary']} | {t['sources']} |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        st = r.get("status") or {}
        inf = t["lifted"] + f" {st.get('lifted')}" if st.get("lifted") else (t["yes"] if st.get("in_force") is True else t["no"] if st.get("in_force") is False else str(st.get("in_force", "")))
        out.append(f"| {r.get('date','')} | {r.get('actor','')} | {r.get('instrument','')} | {r.get('target','')} | {inf} | {r.get('summary','')} | {_src(r.get('sources'), t)} |")
    return "\n".join(out) + "\n"


def linkages_page(lang: str, t: dict, today: str) -> str:
    rows = _load("linkages.yaml")
    out = [f"# {t['lk_title']}", "", f"**{t['status']} {today}**", "", t["lk_intro"], "",
           f"| {t['signal']} | {t['action']} | {t['grade']} | {t['evidence']} | {t['notes']} |", "|---|---|---|---|---|"]
    for r in rows:
        ev = "<br>".join(r.get("evidence") or []) or "—"
        out.append(f"| `{r.get('signal')}` | `{r.get('action') or '—'}` | `{r.get('grade')}` | {ev} | {r.get('notes','')} |")
    return "\n".join(out) + "\n"


def main() -> int:
    today = date.today().strftime("%-d %B %Y")
    for lang, t in L.items():
        base = DOCS if lang == "en" else DOCS / lang
        base.mkdir(parents=True, exist_ok=True)
        (base / "cases.md").write_text(cases_page(lang, t, today), encoding="utf-8")
        (base / "foreign-actions.md").write_text(foreign_page(lang, t, today), encoding="utf-8")
        (base / "linkages.md").write_text(linkages_page(lang, t, today), encoding="utf-8")
        print(f"  ✓ {lang}: cases, foreign-actions, linkages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
