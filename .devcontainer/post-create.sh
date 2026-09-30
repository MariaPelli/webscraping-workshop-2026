#!/usr/bin/env bash
set -euo pipefail

# Darf erneut ausgefuehrt werden; vorhandene .env und Daten bleiben erhalten.
workshop_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
workshop_venv="/home/vscode/.venvs/webscraping-workshop"
cd "$workshop_root"

if [[ ! -x "$workshop_venv/bin/python" ]]; then
    mkdir -p "$(dirname "$workshop_venv")"
    python3 -m venv "$workshop_venv"
fi

"$workshop_venv/bin/python" -c 'import sys; assert sys.version_info[:2] == (3, 12), "Die Umgebung benoetigt Python 3.12."'
"$workshop_venv/bin/python" -m pip install --disable-pip-version-check -r requirements.txt
"$workshop_venv/bin/python" -m pip check
"$workshop_venv/bin/python" -m ipykernel install --user \
    --name webscraping-workshop \
    --display-name "Python (webscraping-workshop)"

if [[ ! -f .env ]]; then
    cp .env.example .env
fi
mkdir -p data/output

printf '\nPython-Umgebung eingerichtet. Waehle den Kernel Python (webscraping-workshop).\n'
printf 'Naechster Schritt: python scripts/verify_setup.py\n'
