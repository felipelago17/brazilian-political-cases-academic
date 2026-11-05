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
        "yes": "yes", "no": "no", "lifted": "lifted", "unknown": "unknown", "tier": "T",
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
        "cases_intro": "Casos judiciais envolvendo figuras públicas e instituições brasileiras, de todos os partidos e poderes. Fonte: `trackers/cases.yaml`. Fases e resultados seguem o vocabulário fixo da [taxonomia de situação](methodology/status-taxonomy.md). ",
        "fa_intro": "Ações de governos estrangeiros (sobretudo dos EUA) que afetam figuras públicas, instituições ou o comércio do Brasil. São ações; qualquer conexão com decisão brasileira é graduada em [Vínculos](linkages.md).",
        "lk_intro": "Conexões graduadas entre um sinal e uma ação. Entradas `proximity-only` não implicam inferência. Ver [graus de vínculo](methodology/linkage-grades.md).",
        "yes": "sim", "no": "não", "lifted": "revogada em", "unknown": "não confirmado", "tier": "N",
        "stage_v": {"inquérito": "inquérito", "denúncia": "denúncia oferecida", "denúncia-recebida": "denúncia recebida", "instrução": "instrução", "sentença": "sentença", "recurso": "recurso", "trânsito-em-julgado": "trânsito em julgado", "encerrado": "encerrado"},
        "outcome_v": {"pendente": "pendente", "condenação": "condenação", "absolvição": "absolvição", "anulação": "anulação", "prescrição": "prescrição", "arquivamento": "arquivamento", "rejeição-da-denúncia": "denúncia rejeitada"},
    },
    "es": {
        "cases_title": "Casos", "fa_title": "Acciones extranjeras", "lk_title": "Vínculos",
        "status": "Situación al", "presumption": "**Presunción de inocencia.** Las acusaciones e investigaciones no son condenas. No constituye asesoramiento jurídico.",
        "matter": "Caso", "persons": "Personas", "affiliation": "Afiliación", "origin": "Origen", "forum": "Foro",
        "allegation": "Acusación", "stage": "Etapa", "outcome": "Resultado", "mechanisms": "Mecanismos", "sources": "Fuentes",
        "timeline": "Cronología", "official": "Registro oficial", "how": "Cómo obtenerlo", "reference": "Referencia", "notes": "Notas",
        "date": "Fecha", "actor": "Autor", "instrument": "Instrumento", "target": "Objetivo", "summary": "Resumen", "in_force": "Vigente",
        "signal": "Señal", "action": "Acción", "grade": "Grado", "evidence": "Evidencia",
        "cases_intro": "Casos judiciales que involucran a figuras públicas e instituciones brasileñas, de todos los partidos y poderes. Fuente: `trackers/cases.yaml`. Etapas y resultados siguen el vocabulario fijo de la [taxonomía de situación](methodology/status-taxonomy.md). ",
        "fa_intro": "Acciones de gobiernos extranjeros (principalmente EE. UU.) que afectan a figuras públicas, instituciones o el comercio de Brasil. Son acciones; cualquier conexión con una decisión brasileña se gradúa en [Vínculos](linkages.md).",
        "lk_intro": "Conexiones graduadas entre una señal y una acción. Las entradas `proximity-only` no implican inferencia. Ver [grados de vínculo](methodology/linkage-grades.md).",
        "yes": "sí", "no": "no", "lifted": "levantada el", "unknown": "no confirmado", "tier": "N",
        "stage_v": {"inquérito": "investigación", "denúncia": "acusación", "denúncia-recebida": "acusación admitida", "instrução": "instrucción", "sentença": "sentencia", "recurso": "recurso", "trânsito-em-julgado": "firme", "encerrado": "cerrado"},
        "outcome_v": {"pendente": "pendiente", "condenação": "condena", "absolvição": "absolución", "anulação": "anulación", "prescrição": "prescrito", "arquivamento": "archivado", "rejeição-da-denúncia": "acusación rechazada"},
    },
}


def _load(name: str):
    return yaml.safe_load((TR / name).read_text(encoding="utf-8"))


def _tr(lang: str) -> dict:
    """Translation overlay for free text (trackers/translations/<lang>.yaml); English has none."""
    f = TR / "translations" / f"{lang}.yaml"
    return yaml.safe_load(f.read_text(encoding="utf-8")) if f.exists() else {}


def _overlay(item: dict, tr: dict | None) -> dict:
    """Return a copy of item with translated free-text fields where the overlay provides them."""
    if not tr:
        return item
    out = dict(item)
    for k in ("matter", "origin", "forum", "allegation", "notes", "actor", "instrument", "target", "summary"):
        if tr.get(k):
            out[k] = tr[k]
    if tr.get("timeline") and item.get("timeline"):
        tl = []
        for i, x in enumerate(item["timeline"]):
            ev = tr["timeline"][i] if i < len(tr["timeline"]) else x.get("event", "")
            tl.append({**x, "event": ev})
        out["timeline"] = tl
    if tr.get("how_to_retrieve") and item.get("official"):
        out["official"] = {**item["official"], "how_to_retrieve": tr["how_to_retrieve"]}
    return out


def _src(sources: list[dict], t: dict) -> str:
    return "<br>".join(f"[{s.get('outlet','source')}]({s['url']}) ({t['tier']}{s.get('tier','?')})" for s in sources or [])


def _v(t: dict, key: str, val: str) -> str:
    return t.get(key, {}).get(val, val) or ""


def cases_page(lang: str, t: dict, today: str) -> str:
    trs = (_tr(lang).get("cases") or {})
    cases = [_overlay(c, trs.get(c["id"])) for c in _load("cases.yaml")]
    out = [f"# {t['cases_title']}", "", f"**{t['status']} {today}**", "", t["presumption"], "", t["cases_intro"], "",
           f"| {t['matter']} | {t['persons']} | {t['affiliation']} | {t['stage']} | {t['outcome']} |",
           "|---|---|---|---|---|"]
    for c in cases:
        out.append(f"| [{c['matter']}](#{c['id']}) | {', '.join(c.get('persons', []))} | {c.get('affiliation','')} | "
                   f"{_v(t,'stage_v',c.get('stage',''))} | {_v(t,'outcome_v',c.get('outcome',''))} |")
    out.append("")
    for c in cases:
        out += [f"## {c['matter']} {{#{c['id']}}}", "",
                f"**{t['persons']}:** {', '.join(c.get('persons', []))} ({c.get('affiliation','')}) · **{t['origin']}:** {c.get('origin','')} · **{t['forum']}:** {c.get('forum','')}", "",
                f"**{t['stage']} / {t['outcome']}:** {_v(t,'stage_v',c.get('stage',''))} / {_v(t,'outcome_v',c.get('outcome',''))}"
                + (f" · **{t['mechanisms']}:** {', '.join(c.get('mechanisms', []))}" if c.get('mechanisms') else ""), "",
                f"**{t['allegation']}.** {c.get('allegation','')}", ""]
        if c.get("timeline"):
            out += [f"**{t['timeline']}.**", ""] + [f"- {x.get('date','')} — {x.get('event','')}" for x in c["timeline"]] + [""]
        o = c.get("official") or {}
        link = f"[{o['reference']}]({o['link']})" if o.get("link") else f"{o.get('reference','')} — [portal]({o.get('portal','')})"
        out += [f"**{t['official']}.** {link}. {t['how']}: {o.get('how_to_retrieve','')}", ""]
        if c.get("notes"):
            out += [f"**{t['notes']}.** {c['notes']}", ""]
        out += [f"**{t['sources']}.** " + " · ".join(f"[{x.get('outlet','source')}]({x['url']}) ({t['tier']}{x.get('tier','?')})" for x in c.get('sources') or []), ""]
    return "\n".join(out)


def foreign_page(lang: str, t: dict, today: str) -> str:
    trs = (_tr(lang).get("foreign_actions") or {})
    rows = [_overlay(r, trs.get(r["id"])) for r in _load("foreign-actions.yaml")]
    out = [f"# {t['fa_title']}", "", f"**{t['status']} {today}**", "", t["fa_intro"], "",
           f"| {t['date']} | {t['actor']} | {t['target']} | {t['in_force']} |", "|---|---|---|---|"]
    def _inf(r):
        st = r.get("status") or {}
        return t["lifted"] + f" {st.get('lifted')}" if st.get("lifted") else (t["yes"] if st.get("in_force") is True else t["no"] if st.get("in_force") is False else t["unknown"])
    for r in rows:
        out.append(f"| {r.get('date','')} | [{r.get('actor','')}](#{r['id']}) | {r.get('target','')} | {_inf(r)} |")
    out.append("")
    for r in rows:
        out += [f"## {r.get('date','')} — {r.get('actor','')} {{#{r['id']}}}", "",
                f"**{t['instrument']}:** {r.get('instrument','')}", "", f"**{t['target']}:** {r.get('target','')} · **{t['in_force']}:** {_inf(r)}", "",
                f"{r.get('summary','')}", "",
                f"**{t['sources']}.** " + " · ".join(f"[{x.get('outlet','source')}]({x['url']}) ({t['tier']}{x.get('tier','?')})" for x in r.get('sources') or []), ""]
    return "\n".join(out)


def linkages_page(lang: str, t: dict, today: str) -> str:
    rows = _load("linkages.yaml")
    notes_tr = _tr(lang).get("linkages") or []
    rows = [{**r, "notes": (notes_tr[i] if i < len(notes_tr) else r.get("notes", ""))} for i, r in enumerate(rows)]
    out = [f"# {t['lk_title']}", "", f"**{t['status']} {today}**", "", t["lk_intro"], "",
           f"| {t['signal']} | {t['action']} | {t['grade']} | {t['evidence']} | {t['notes']} |", "|---|---|---|---|---|"]
    for r in rows:
        ev = "<br>".join(r.get("evidence") or []) or "—"
        out.append(f"| `{r.get('signal')}` | `{r.get('action') or '—'}` | `{r.get('grade')}` | {ev} | {r.get('notes','')} |")
    return "\n".join(out) + "\n"


MONTHS = {
    "pt": ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"],
    "es": ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"],
}


def _today(lang: str) -> str:
    d = date.today()
    if lang in MONTHS:
        return f"{d.day} de {MONTHS[lang][d.month-1]} de {d.year}"
    return d.strftime("%-d %B %Y")


def main() -> int:
    for lang, t in L.items():
        today = _today(lang)
        base = DOCS if lang == "en" else DOCS / lang
        base.mkdir(parents=True, exist_ok=True)
        (base / "cases.md").write_text(cases_page(lang, t, today), encoding="utf-8")
        (base / "foreign-actions.md").write_text(foreign_page(lang, t, today), encoding="utf-8")
        (base / "linkages.md").write_text(linkages_page(lang, t, today), encoding="utf-8")
        print(f"  ✓ {lang}: cases, foreign-actions, linkages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
