"""
Brazil Accountability Tracker — Python loader.

The source of truth is the YAML under trackers/. This module loads it for anyone who
wants the data in Python (the previous hard-coded dict has been migrated to trackers/cases.yaml).

    from tracker import load
    data = load()           # {'cases': [...], 'foreign_actions': [...], 'linkages': [...], ...}
"""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent / "trackers"
FILES = {
    "cases": "cases.yaml",
    "foreign_actions": "foreign-actions.yaml",
    "linkages": "linkages.yaml",
    "legislative_signals": "legislative-signals.yaml",
    "institutional_actions": "institutional-actions.yaml",
}


def load() -> dict:
    return {k: yaml.safe_load((ROOT / f).read_text(encoding="utf-8")) for k, f in FILES.items()}


if __name__ == "__main__":
    d = load()
    print({k: (len(v) if isinstance(v, list) else len(v.get("signals", v.get("actions", [])))) for k, v in d.items()})
