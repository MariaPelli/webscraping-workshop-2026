[Start](README.md) · [Vorbereitung](docs/TECHNISCHE_VORBEREITUNG.md) · [Lokal](docs/setup/LOKAL.md) · [Codespaces](docs/setup/CODESPACES.md) · [Testanleitung](docs/TESTANLEITUNG_ETAPPE1.md) · [Hilfe](docs/TROUBLESHOOTING.md)

# Webscraping – Data Engineering

**Etappe 1: technische Basis zum Testen.** Dieses Zwischenpaket richtet die Arbeitsumgebung ein und prüft sie mit einem ausführbaren Notebook. Die Kurs-Demos, Aufgaben und Musterlösungen folgen in Etappe 2. In den Ordnern `demos/` und `tasks/` findest Du deshalb vorerst nur die geplanten Inhalte.

Der spätere Themenblock behandelt strukturierte Datenabrufe, das Auslesen von HTML sowie dynamisch nachgeladene Inhalte. Die technische Basis verwendet Python 3.12, Jupyter, `requests`, BeautifulSoup, `lxml` und Selenium. Chromium läuft in einem eigenen Container. Du musst keinen Browser-Treiber herunterladen.

## Einstieg

1. Wähle in der folgenden Tabelle Deine Arbeitsumgebung.
2. Folge der zugehörigen Anleitung bis zum Einrichtungstest.
3. Öffne [`notebooks/00_setup_check.ipynb`](notebooks/00_setup_check.ipynb) mit dem Kernel **Python (webscraping-workshop)** und führe alle Zellen aus.
4. Prüfe das Ergebnis mit der [Testanleitung für Etappe 1](docs/TESTANLEITUNG_ETAPPE1.md).

## Umgebungsvergleich

| Merkmal | Lokal: Anaconda und Docker | GitHub Codespaces |
|---|---|---|
| Voraussetzung | Anaconda, laufendes Docker mit Compose; Repo als entpackter Ordner oder Git-Klon | GitHub-Konto mit verfügbarem Codespaces-Kontingent; Repo auf GitHub |
| Python-Umgebung | Conda-Umgebung `webscraping-workshop`, Python 3.12 | Automatisch angelegte Python-3.12-Umgebung unter `/home/vscode/.venvs/webscraping-workshop` |
| Python-Pakete | `environment.yml` verwendet die gemeinsame `requirements.txt` | Einrichtungsskript verwendet dieselbe `requirements.txt` |
| Arbeitsoberfläche | JupyterLab im eigenen Browser oder lokal installiertes VS Code | Notebook-Editor in VS Code im Browser |
| Notebook-Kernel | `Python (webscraping-workshop)` | `Python (webscraping-workshop)` |
| Selenium und Chromium | `docker compose up -d` im Repo startet den Browser-Container | Selenium startet als Nebendienst des Devcontainers |
| Adresse für Python | Standard: `http://127.0.0.1:4444`; lokaler Port über `.env` anpassbar | Intern: `http://selenium:4444`; bereits konfiguriert |
| Portfreigaben | Selenium ist nur an die lokale Loopback-Adresse gebunden | Für die Einrichtungstests sind keine weitergeleiteten oder öffentlichen Ports erforderlich |
| Internet | Für Einrichtung und optionale Live-Tests; Grundtest arbeitet mit mitgelieferten Daten | Für Codespaces selbst und Einrichtung; Grundtest ruft keine fremde Website ab |
| Anleitung | [Lokal einrichten](docs/setup/LOKAL.md) | [Codespaces starten](docs/setup/CODESPACES.md) |

**Anaconda führt den Python-Code aus; Docker stellt lokal den automatisierten Browser bereit.** Ein Fenster mit Chromium erscheint beim Test nicht. In Codespaces laufen sowohl Python als auch der Browser in der entfernten Umgebung.

## Lokal: JupyterLab oder VS Code starten

Nach der [einmaligen Einrichtung](docs/setup/LOKAL.md) im Repo-Hauptordner die Umgebung aktivieren und den Browser-Dienst starten:

```bash
conda activate webscraping-workshop
docker compose up -d
```

Danach wählst Du Deine Oberfläche:

| Oberfläche | Startbefehl |
|---|---|
| JupyterLab | `jupyter lab` |
| VS Code | `code .` |

Im Notebook den Kernel **Python (webscraping-workshop)** wählen. Die [lokale Anleitung](docs/setup/LOKAL.md) beschreibt beide Varianten einschliesslich der benötigten VS-Code-Erweiterungen.

## Was der Einrichtungstest prüft

- Python-Version und benötigte Pakete.
- Projektpfade und Abruf synthetischer HTML-/JSON-Daten über einen kurzzeitig gestarteten lokalen HTTP-Server.
- Auslesen von drei Datensätzen und Speichern/Zurücklesen einer CSV-Datei.
- Verbindung zu Selenium, Start einer echten Browser-Sitzung und Auslesen von drei durch JavaScript erzeugten Datensätzen.

Der Grundtest benötigt keine API-Schlüssel. Ein vollständiger Erfolg endet mit **`SETUP OK`**. `--skip-browser` prüft nur die Python-Basis und endet bei Erfolg mit **`TEILTEST OK`**; damit ist Selenium noch nicht geprüft. Der Bericht liegt standardmässig unter `data/output/setup_report.json`.

## Orientierung im Repo

| Pfad | Zweck in Etappe 1 |
|---|---|
| [`docs/`](docs/TECHNISCHE_VORBEREITUNG.md) | Vorbereitung, Startanleitungen, Fehlerhilfe und Testablauf |
| [`notebooks/00_setup_check.ipynb`](notebooks/00_setup_check.ipynb) | Ausführbarer Einrichtungstest |
| [`scripts/verify_setup.py`](scripts/verify_setup.py) | Derselbe Test im Terminal |
| [`src/webscraping_workshop/`](src/webscraping_workshop/) | Gemeinsame Prüflogik für Notebook und Terminal |
| [`data/`](data/) | Synthetische Beispieldaten und lokaler Ausgabeordner |
| [`demos/`](demos/README.md) | Vorschau auf die Demos der nächsten Etappe |
| [`tasks/`](tasks/README.md) | Vorschau auf die Aufgaben der nächsten Etappe |
| [`environment.yml`](environment.yml), [`requirements.txt`](requirements.txt) | Python-Umgebung und gemeinsame Abhängigkeiten |
| [`compose.yaml`](compose.yaml), [`.devcontainer/`](.devcontainer/) | Lokaler Browser-Dienst und Codespaces-Konfiguration |

## Für die Vorbereitung des Unterrichts

- [Prüfprotokoll und offene Prüfungen](docs/VALIDIERUNG_ETAPPE1.md): tatsächlich ausgeführte Tests und deren Grenzen.
- [Repo auf GitHub bereitstellen](docs/GITHUB_UPLOAD.md): auch `.devcontainer` und weitere Konfigurationsdateien übertragen.
- [Änderungen](CHANGELOG.md): Stand des Zwischenpakets.

Eigene Ausgaben unter `data/output/`, die lokale `.env` und spätere Musterlösungen werden durch `.gitignore` von neuen Git-Commits ausgeschlossen. Vor dem Teilen von Änderungen prüfst Du dennoch die vorgemerkten Dateien.

---

[Nach oben](#webscraping--data-engineering) · [Vorbereitung](docs/TECHNISCHE_VORBEREITUNG.md) · [Lokal](docs/setup/LOKAL.md) · [Codespaces](docs/setup/CODESPACES.md) · [Testanleitung](docs/TESTANLEITUNG_ETAPPE1.md) · [Hilfe](docs/TROUBLESHOOTING.md)
