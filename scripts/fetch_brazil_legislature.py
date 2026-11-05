#!/usr/bin/env python3
"""Scan the Câmara dos Deputados and Senado Federal open-data APIs for proposições
matching the keywords in trackers/legislative-signals.yaml. No API key required.

  Câmara: https://dadosabertos.camara.leg.br/api/v2/proposicoes?keywords=...
  Senado: https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?palavraChave=...

Candidate items are listed on docs/trackers/legislature.md and stored in
data/legislature.json. Rows in trackers/legislative-signals.yaml are added by pull
request after review; this script never writes to the tracker.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "trackers" / "legislative-signals.yaml"
DATA_OUT = ROOT / "data" / "legislature.json"
PAGE_OUT = ROOT / "docs" / "trackers" / "legislature.md"
TIMEOUT = 75
UA = {"User-Agent": "brazil-accountability-tracker/1.0", "Accept": "application/json"}
CAMARA = "https://dadosabertos.camara.leg.br/api/v2/proposicoes"
SENADO = "https://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista"
SCAN_DAYS = int(os.environ.get("SCAN_DAYS", "30"))


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 503) and attempt < 2:
                time.sleep(5 * (attempt + 1)); continue
            raise RuntimeError(f"HTTP {exc.code} {url}") from None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if attempt < 2:
                time.sleep(5); continue
            raise RuntimeError(f"{type(exc).__name__}: {exc}") from None
    return {}


def camara(keyword: str, since: str) -> list[dict]:
    q = urllib.parse.urlencode({"keywords": keyword, "dataApresentacaoInicio": since, "ordem": "DESC", "ordenarPor": "id", "itens": 100})
    data = _get(f"{CAMARA}?{q}")
    out = []
    for p in data.get("dados", []):
        out.append({
            "chamber": "Câmara", "id": p.get("id"), "number": f"{p.get('siglaTipo')} {p.get('numero')}/{p.get('ano')}",
            "ementa": p.get("ementa"), "keyword": keyword,
            "url": f"https://www.camara.leg.br/propostas-legislativas/{p.get('id')}",
        })
    return out


def senado(keyword: str) -> list[dict]:
    q = urllib.parse.urlencode({"palavraChave": keyword, "tramitando": "S"})
    data = _get(f"{SENADO}?{q}")
    out = []
    mats = (((data.get("PesquisaBasicaMateria") or {}).get("Materias") or {}).get("Materia")) or []
    if isinstance(mats, dict):
        mats = [mats]
    for m in mats:
        ident = m.get("IdentificacaoMateria") or m
        cod = ident.get("CodigoMateria") or m.get("CodigoMateria")
        out.append({
            "chamber": "Senado", "id": cod,
            "number": (f"{ident.get('SiglaSubtipoMateria', '')} {ident.get('NumeroMateria', '')}/{ident.get('AnoMateria', '')}".strip()
                       if ident.get('NumeroMateria') else (m.get('DescricaoIdentificacaoMateria') or "—")),
            "ementa": m.get("Ementa") or (m.get("DadosBasicosMateria") or {}).get("EmentaMateria"), "keyword": keyword,
            "url": f"https://www25.senado.leg.br/web/atividade/materias/-/materia/{cod}" if cod else "",
        })
    return out


def render(payload: dict) -> str:
    gen = payload["generated_at"][:16].replace("T", " ") + " UTC"
    out = ["# Legislative signals (Câmara / Senado open data)", "",
           f"*Auto-generated {gen} from the Câmara dos Deputados and Senado Federal open-data APIs. Candidate items only — curated rows live in `trackers/legislative-signals.yaml`. Not legal advice.*", "",
           f"Keywords: {', '.join('`' + k + '`' for k in payload['keywords'])} · Câmara window: proposições presented in the last {payload['scan_days']} days · Senado: matérias em tramitação", ""]
    if payload["items"]:
        out += ["| Chamber | Number | Ementa | Keyword | Link |", "|---|---|---|---|---|"]
        for r in payload["items"]:
            em = (r.get("ementa") or "").replace("|", "/")
            em = em[:220] + ("…" if len(em) > 220 else "")
            out.append(f"| {r['chamber']} | {r['number']} | {em} | {r['keyword']} | [link]({r['url']}) |")
    else:
        out.append("_No matches._")
    return "\n".join(out) + "\n"


def main() -> int:
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
    keywords = cfg.get("keywords", [])
    since = (datetime.now(timezone.utc) - timedelta(days=SCAN_DAYS)).strftime("%Y-%m-%d")
    items, seen = [], set()
    for kw in keywords:
        for name, fn in (("Câmara", lambda: camara(kw, since)), ("Senado", lambda: senado(kw))):
            try:
                for r in fn():
                    key = (r["chamber"], r["id"])
                    if key in seen:
                        continue
                    seen.add(key); items.append(r)
            except Exception as exc:  # noqa: BLE001
                print(f"  ⚠ {name} '{kw}': {exc}")
        time.sleep(0.5)
    print(f"  ✓ {len(items)} candidate items")
    payload = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "scan_days": SCAN_DAYS, "keywords": keywords, "items": items}
    DATA_OUT.parent.mkdir(parents=True, exist_ok=True)
    DATA_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PAGE_OUT.parent.mkdir(parents=True, exist_ok=True)
    PAGE_OUT.write_text(render(payload), encoding="utf-8")
    s = os.environ.get("GITHUB_STEP_SUMMARY")
    if s:
        open(s, "a", encoding="utf-8").write(f"### Legislature: {len(items)} candidate items\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
