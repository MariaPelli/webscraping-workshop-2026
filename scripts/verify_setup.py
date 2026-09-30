#!/usr/bin/env python3
"""Aufruf aus der Repo-Wurzel: python scripts/verify_setup.py."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from webscraping_workshop.checks import (  # noqa: E402
    format_result,
    run_setup_checks,
    summary_text,
    write_report,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüfe die technische Basis des Webscraping-Workshops.")
    parser.add_argument("--skip-browser", action="store_true", help="Nur Basistests; bestätigt keine funktionierende Browserumgebung.")
    parser.add_argument("--online", action="store_true", help="Zusätzliche getrennte Live-Prüfungen: ECB und Books to Scrape.")
    parser.add_argument("--report", type=Path, default=None, help="JSON-Reportpfad; Standard: data/output/setup_report.json im Repo.")
    args = parser.parse_args()
    print("Webscraping-Workshop: technische Einrichtung prüfen", flush=True)
    print("Die Browserprüfung wartet bei Bedarf bis zu 45 Sekunden auf Selenium.", flush=True)
    report = run_setup_checks(
        ROOT,
        include_browser=not args.skip_browser,
        online=args.online,
        on_result=lambda result: print(format_result(result), flush=True),
    )
    destination = args.report if args.report is not None else ROOT / "data/output/setup_report.json"
    try:
        write_report(report, destination)
    except OSError as exc:
        print(f"[FEHLER] JSON-Report konnte nicht gespeichert werden ({type(exc).__name__}).", flush=True)
        print("ABSCHLUSS FEHLGESCHLAGEN – wähle einen beschreibbaren Berichtspfad.", flush=True)
        return 1
    print("JSON-Report gespeichert." if args.report is not None else "JSON-Report: data/output/setup_report.json", flush=True)
    print(summary_text(report), flush=True)
    return 0 if report["overall_status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
