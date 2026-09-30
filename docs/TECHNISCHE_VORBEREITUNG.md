[Start](../README.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md) · [Hilfe](TROUBLESHOOTING.md)

# Technische Vorbereitung

Wähle **einen** der beiden unterstützten Wege. Du musst nicht beide Umgebungen einrichten.

## Weg A – lokal mit Anaconda und Docker

Du benötigst:

- Anaconda mit `conda` und Python-Umgebungen.
- Docker Desktop unter Windows/macOS oder Docker Engine mit Compose-Plug-in unter Linux; der Dienst muss laufen.
- Den vollständig entpackten Repo-Ordner. Git ist nur für das Klonen oder Veröffentlichen erforderlich.
- Internetzugang für Pakete und Container-Image während der Einrichtung.
- Als Oberfläche wahlweise JupyterLab (wird mitinstalliert) oder lokal installiertes VS Code mit den Microsoft-Erweiterungen Python und Jupyter.

Unter Windows verwendest Du **Anaconda Prompt** für die angegebenen Befehle und Docker im Modus für Linux-Container. Unter macOS/Linux verwendest Du ein Terminal, in dem `conda` verfügbar ist.

Nach `conda activate webscraping-workshop` startest Du im Repo-Hauptordner wahlweise `jupyter lab` oder `code .`. Die einmalige Einrichtung und den Start des Browser-Dienstes erklärt die folgende Anleitung.

**Weiter: [Lokale Einrichtung](setup/LOKAL.md).**

## Weg B – GitHub Codespaces

Du benötigst:

- Ein GitHub-Konto mit Zugriff auf das Repo und verfügbarem Codespaces-Kontingent.
- Einen Webbrowser und eine Internetverbindung.
- Das Repo inklusive `.devcontainer/` auf GitHub. Für die erstmalige Bereitstellung hilft die [Upload-Anleitung](GITHUB_UPLOAD.md).

Anaconda und Docker auf Deinem eigenen Rechner werden für diesen Weg nicht verwendet. Python-Umgebung und Selenium-Dienst werden im Codespace eingerichtet.

**Weiter: [Codespaces starten](setup/CODESPACES.md).**

## Einheitliche Namen

| Bestandteil | Name |
|---|---|
| Lokale Conda-Umgebung | `webscraping-workshop` |
| Notebook-Kernel | `Python (webscraping-workshop)` |
| Kernel-ID | `webscraping-workshop` |
| Erstes Notebook | `notebooks/00_setup_check.ipynb` |
| Test im Terminal | `python scripts/verify_setup.py` |
| Standardbericht | `data/output/setup_report.json` |

Das Testnotebook verwendet ausschliesslich synthetische Daten. Es prüft HTML, JSON, CSV und JavaScript-Inhalte ohne Zugriff auf eine fremde Website. Optional prüft `--online` zusätzlich die Erreichbarkeit ausgewählter späterer Datenquellen. Ein erfolgreicher Grundtest bestätigt diese Live-Erreichbarkeit noch nicht.

## Wann bist Du bereit?

Die Einrichtung ist vollständig geprüft, wenn sowohl der vollständige Terminaltest als auch das Testnotebook mit dem richtigen Kernel **`SETUP OK`** melden. Ein erfolgreicher `--skip-browser`-Lauf reicht dafür nicht aus.

Die einzelnen Prüfungen und die Angaben für eine Rückmeldung stehen in der [Testanleitung](TESTANLEITUNG_ETAPPE1.md). Welche Tests bei der Erstellung dieses Pakets bereits möglich waren, dokumentiert das [Prüfprotokoll](VALIDIERUNG_ETAPPE1.md).

---

[Start](../README.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md)
