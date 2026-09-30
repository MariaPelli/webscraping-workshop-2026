[Start](README.md) · [Vorbereitung](docs/TECHNISCHE_VORBEREITUNG.md) · [Lokal](docs/setup/LOKAL.md) · [Codespaces](docs/setup/CODESPACES.md) · [Demos](demos/README.md) · [Tasks](tasks/README.md) · [Hilfe](docs/TROUBLESHOOTING.md)

# Webscraping – Data Engineering

**Etappe 2: vier Demos und zwei Aufgaben auf der geprüften technischen Basis.** Du lernst, strukturierte Daten abzurufen, HTML auszulesen und dynamisch erzeugte Inhalte im Browser zu erfassen. Dabei prüfst Du die Ergebnisse und speicherst sie mit nachvollziehbarer Herkunft.

Alle Demos und Aufgaben starten mit **mitgelieferten synthetischen Daten**. Diese Daten sind für die Lehre erstellt und keine historischen Downloads von ECB, CoinGecko, Flickr oder Books to Scrape. Live-Abrufe sind bewusst wählbare Ergänzungen; für den Kurskern brauchst Du keine API-Schlüssel. Für die dynamischen Beispiele muss der Selenium-Dienst laufen.

Die technische Basis verwendet weiterhin Python 3.12, Jupyter, `requests`, BeautifulSoup, `lxml` und Selenium. Chromium läuft in einem eigenen Container. Du musst keinen Browser-Treiber herunterladen. Die in Etappe 1 getesteten Abhängigkeiten und Container-Konfigurationen bleiben unverändert.

## Einstieg

1. **Schon eingerichtet?** Übernimm die neuen Dateien gemäss [Update auf Etappe 2](docs/UPDATE_ETAPPE2.md). Eine Neuinstallation oder ein Container-Rebuild ist für dieses Update nicht erforderlich.
2. **Neu dabei?** Wähle unten eine Arbeitsumgebung und folge der [technischen Vorbereitung](docs/TECHNISCHE_VORBEREITUNG.md).
3. **Bei der ersten Einrichtung:** Öffne [`notebooks/00_setup_check.ipynb`](notebooks/00_setup_check.ipynb) mit dem Kernel **Python (webscraping-workshop)** und führe alle Zellen aus. Der vollständige Test muss `SETUP OK` melden.
4. Beginne mit den [Demos](demos/README.md) und bearbeite danach die [Tasks](tasks/README.md). Die [Testanleitung für Etappe 2](docs/TESTANLEITUNG_ETAPPE2.md) hilft beim ersten Kontrolllauf.

## Lernweg

| Schritt | Material | Leitfrage |
|---|---|---|
| 1 | [Strukturierte Daten: ECB](demos/01_strukturierte_daten_ezb.ipynb) | Wie werden XML-Daten zu einer prüfbaren Tabelle? |
| 2 | [REST-APIs: CoinGecko und Flickr](demos/02_rest_apis_coingecko_flickr.ipynb) | Wie unterscheiden sich Datenformat, Endpunkt, Parameter und Zugang? |
| 3 | [HTML mit BeautifulSoup](demos/03_html_beautifulsoup.ipynb) | Wie finde ich wiederkehrende Elemente und weitere Seiten? |
| 4 | [Task 1: statischer Katalog](tasks/01_statischer_katalog/README.md) | Wie erfasse und prüfe ich selbstständig einen mehrseitigen Datenbestand? |
| 5 | [Dynamische Seiten mit Selenium](demos/04_dynamische_seiten_selenium.ipynb) | Wie unterscheiden sich Ausgangs-HTML und der durch JavaScript veränderte DOM? |
| 6 | [Task 2: dynamischer Katalog](tasks/02_dynamischer_katalog/README.md) | Wie warte ich auf Inhalte, lade weitere Einträge und prüfe Vollständigkeit? |

**BeautifulSoup führt kein JavaScript aus.** Selenium steuert einen Browser, der JavaScript ausführen und den DOM verändern kann. BeautifulSoup kann anschliessend auch dieses gerenderte HTML auswerten. Welche Methode Du brauchst, hängt davon ab, wo die Daten tatsächlich vorliegen. Ein leerer Selektor allein beweist nicht, dass eine Website Browserautomatisierung benötigt. Mehr dazu im [didaktischen Überblick](docs/DIDAKTIK.md).

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
| Portfreigaben | Selenium ist nur an die lokale Loopback-Adresse gebunden | Für Einrichtungstests und mitgelieferte Kursbeispiele sind keine weitergeleiteten oder öffentlichen Ports erforderlich |
| Internet | Für Einrichtung und optionale Live-Abrufe; Kurskern arbeitet mit mitgelieferten Daten | Für Codespaces selbst und Einrichtung; Kurskern ruft keine fremde Website ab |
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

| Pfad | Zweck |
|---|---|
| [`docs/`](docs/TECHNISCHE_VORBEREITUNG.md) | Vorbereitung, Startanleitungen, Fehlerhilfe und Testablauf |
| [`notebooks/00_setup_check.ipynb`](notebooks/00_setup_check.ipynb) | Ausführbarer Einrichtungstest |
| [`scripts/verify_setup.py`](scripts/verify_setup.py) | Derselbe Test im Terminal |
| [`src/webscraping_workshop/`](src/webscraping_workshop/) | Gemeinsame Prüflogik und Verbindung zum Browser-Dienst |
| [`data/`](data/README.md) | Synthetische Beispieldaten, Herkunftshinweise und lokaler Ausgabeordner |
| [`demos/`](demos/README.md) | Vier geführte Beispiele |
| [`tasks/`](tasks/README.md) | Zwei Aufgaben für die selbstständige Bearbeitung |
| [`environment.yml`](environment.yml), [`requirements.txt`](requirements.txt) | Python-Umgebung und gemeinsame Abhängigkeiten |
| [`compose.yaml`](compose.yaml), [`.devcontainer/`](.devcontainer/) | Lokaler Browser-Dienst und Codespaces-Konfiguration |

## Für die Vorbereitung des Unterrichts

- [Didaktischer Überblick](docs/DIDAKTIK.md): Lernziele, methodische Unterschiede und Bezug zu den Vorjahresmaterialien.
- [API-Zugang](docs/API_ZUGANG.md): eigene Schlüssel und bewusst aktivierte Live-Abrufe; für den Kurskern nicht erforderlich.
- [Update-Anleitung](docs/UPDATE_ETAPPE2.md) und [Testanleitung](docs/TESTANLEITUNG_ETAPPE2.md): neue Dateien übernehmen und Ergebnisse prüfen.
- [Prüfprotokoll Etappe 2](docs/VALIDIERUNG_ETAPPE2.md): tatsächlich ausgeführte Tests der neuen Materialien und offene Prüfungen.
- [Prüfprotokoll Etappe 1](docs/VALIDIERUNG_ETAPPE1.md): technische Basis.
- [Repo auf GitHub bereitstellen](docs/GITHUB_UPLOAD.md): auch `.devcontainer` und weitere Konfigurationsdateien übertragen.
- [Änderungen](CHANGELOG.md): Stand des Zwischenpakets.

Eigene Ausgaben unter `data/output/`, die lokale `.env` sowie die Dozierendenmaterialien und Musterlösungen werden durch `.gitignore` von neuen Git-Commits ausgeschlossen. `.gitignore` entfernt keine bereits versionierten Dateien. Prüfe vor dem Teilen von Änderungen die vorgemerkten Dateien. Das Repo verändert keine GitHub-Kostenlimits und keine Idle-Timeout-Einstellungen Deines Kontos.

---

[Nach oben](#webscraping--data-engineering) · [Vorbereitung](docs/TECHNISCHE_VORBEREITUNG.md) · [Lokal](docs/setup/LOKAL.md) · [Codespaces](docs/setup/CODESPACES.md) · [Demos](demos/README.md) · [Tasks](tasks/README.md) · [Testanleitung](docs/TESTANLEITUNG_ETAPPE2.md) · [Hilfe](docs/TROUBLESHOOTING.md)
