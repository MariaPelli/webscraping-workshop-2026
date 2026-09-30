[Start](../../README.md) · [Vorbereitung](../TECHNISCHE_VORBEREITUNG.md) · [Codespaces](CODESPACES.md) · [Testanleitung](../TESTANLEITUNG_ETAPPE1.md) · [Hilfe](../TROUBLESHOOTING.md)

# Lokal arbeiten: Anaconda und Docker

Alle Befehle führst Du im **Repo-Hauptordner** aus. Dort liegen `environment.yml`, `requirements.txt` und `compose.yaml`. Öffne und bearbeite Dateien nicht direkt im ZIP-Archiv.

## 1. Ordner und Werkzeuge prüfen

Entpacke das ZIP vollständig, beispielsweise nach `C:\Workshops\webscraping-workshop-2026`. Wenn beim Entpacken ein zusätzlicher äusserer Ordner entsteht, wechsle in den inneren Ordner mit der `README.md` und `environment.yml`.

**Windows – Anaconda Prompt** (Beispielpfad anpassen):

```bat
cd /d "C:\Workshops\webscraping-workshop-2026"
conda --version
docker compose version
docker info
```

**macOS/Linux – Terminal** (Beispielpfad anpassen):

```bash
cd "$HOME/Workshops/webscraping-workshop-2026"
conda --version
docker compose version
docker info
```

Starte Docker Desktop vor `docker info`. Unter Linux muss der Docker-Dienst laufen und Dein Konto darauf zugreifen dürfen. Eine Versionsnummer bei `docker compose version` allein bestätigt noch nicht, dass der Docker-Dienst läuft.

## 2. Konfiguration vorbereiten

Erzeuge die lokale Konfiguration **einmalig** aus der Vorlage. Eine bereits angepasste `.env` nicht überschreiben.

**Windows – Anaconda Prompt:**

```bat
copy .env.example .env
```

**macOS/Linux – Terminal:**

```bash
cp .env.example .env
```

Die Voreinstellung `SELENIUM_PORT=4444` reicht normalerweise aus. Für den Einrichtungstest und die synthetischen Kursbeispiele sind keine API-Schlüssel erforderlich. Optionale API-Live-Zugänge erklärt [API-Zugang](../API_ZUGANG.md). Die Datei `.env` bleibt lokal und ist in `.gitignore` eingetragen.

## 3. Python-Umgebung erstellen

Diese Befehle sind für alle drei Betriebssysteme gleich:

```bash
conda env create -f environment.yml
conda activate webscraping-workshop
python -m ipykernel install --user --name webscraping-workshop --display-name "Python (webscraping-workshop)"
```

Warte, bis die Installation abgeschlossen ist. Die Umgebung installiert die gemeinsamen Python-Pakete aus `requirements.txt`; eine zusätzliche Installation in der Anaconda-Basisumgebung ist nicht nötig.

Falls die Umgebung aus einem früheren Zwischenpaket bereits existiert, aktualisiere sie, statt sie erneut anzulegen:

```bash
conda env update -n webscraping-workshop -f environment.yml
conda activate webscraping-workshop
python -m ipykernel install --user --name webscraping-workshop --display-name "Python (webscraping-workshop)"
```

## 4. Browser-Dienst starten und prüfen

```bash
docker compose up -d
python scripts/verify_setup.py
```

Beim ersten Start lädt Docker das Chromium-/Selenium-Image. Der Einrichtungstest wartet begrenzt auf die Bereitschaft des Dienstes und öffnet anschliessend eine echte Browser-Sitzung. Der Browser läuft ohne sichtbares Fenster im Container.

**Erwartetes Endergebnis: `SETUP OK`.** Der Bericht wird unter `data/output/setup_report.json` gespeichert; die gespeicherten Beispieldaten liegen unter `data/output/setup_records.csv`.

Der Browser-Dienst ist standardmässig für Python unter `http://127.0.0.1:4444` erreichbar. Du musst diese Adresse nicht im eigenen Browser öffnen. Falls der Test fehlschlägt, folge der [Fehlerhilfe](../TROUBLESHOOTING.md), bevor Du die Umgebung neu erstellst.

## 5. Arbeitsoberfläche wählen und Notebook öffnen

Nach der Aktivierung der Conda-Umgebung kannst Du im Repo-Hauptordner entweder JupyterLab oder VS Code starten. Beide verwenden dieselbe Umgebung und denselben bereits gestarteten Selenium-Dienst.

### Variante A – JupyterLab

```bash
conda activate webscraping-workshop
jupyter lab
```

Öffne `notebooks/00_setup_check.ipynb`. Wähle über **Kernel → Change Kernel** den Kernel **Python (webscraping-workshop)**. Führe das Notebook mit **Kernel → Restart Kernel and Run All Cells** vollständig aus. Der genaue Menütext kann je nach Sprache der Oberfläche leicht abweichen.

### Variante B – VS Code

VS Code muss lokal installiert sein. Für Python-Notebooks benötigst Du darin die Microsoft-Erweiterungen **Python** und **Jupyter**.

Im selben Anaconda Prompt bzw. Terminal, im Repo-Hauptordner:

```bash
conda activate webscraping-workshop
code .
```

Der Punkt öffnet den aktuellen Repo-Ordner in VS Code. Ein zusätzlicher Start von JupyterLab ist für diese Variante nicht nötig.

1. Öffne `notebooks/00_setup_check.ipynb` im Datei-Explorer.
2. Wähle oben rechts im Notebook den Kernel **Python (webscraping-workshop)** bzw. die Python-Umgebung **webscraping-workshop**.
3. Falls nötig, wähle zusätzlich über **Python: Select Interpreter** in der Befehlspalette diese Umgebung für Python-Dateien und das Terminal. Die Interpreter-Auswahl ersetzt die Kernel-Auswahl im Notebook nicht.
4. Starte den Notebook-Kernel frisch und führe mit **Run All / Alle ausführen** alle Zellen aus.

Prüfe den Notebook-Kernel auch beim Start aus einer aktivierten Conda-Umgebung, besonders wenn VS Code bereits geöffnet war. Der Startbefehl allein legt einen zuvor ausgewählten Notebook-Kernel nicht zwingend neu fest.

Falls `code` nicht erkannt wird: Öffne VS Code zunächst direkt und wähle **Datei → Ordner öffnen**. Unter macOS kannst Du über die Befehlspalette **Shell Command: Install 'code' command in PATH** einrichten; unter Windows/Linux muss der VS-Code-Befehlsordner im `PATH` liegen. Öffne danach ein neues Terminal bzw. Anaconda Prompt.

Bei beiden Varianten muss der Test **`SETUP OK`** ergeben. Der Bericht unter `data/output/setup_report.json` wird bei einem neuen Testlauf überschrieben. Die [Testanleitung](../TESTANLEITUNG_ETAPPE1.md) beschreibt das Festhalten der Ergebnisse.

## Beim nächsten Arbeiten

Wechsle wieder in den Repo-Hauptordner und starte Docker. Danach genügen:

```bash
conda activate webscraping-workshop
docker compose up -d
```

Starte danach die gewünschte Oberfläche:

| Oberfläche | Startbefehl |
|---|---|
| JupyterLab | `jupyter lab` |
| VS Code | `code .` |

Die Conda-Umgebung muss nicht neu erstellt werden. Zum Beenden: In JupyterLab den Server im Terminal mit `Strg+C` stoppen und bestätigen; in VS Code das Notebook speichern und den Kernel beenden. Danach bei Bedarf `docker compose stop` ausführen. Das stoppt nur die Dienste dieser lokalen Compose-Konfiguration.

## Offizielle Dokumentation

- [Conda: Umgebungen verwalten](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Selenium: offizielle Docker-Images](https://github.com/SeleniumHQ/docker-selenium)
- [VS Code aus der Kommandozeile starten](https://code.visualstudio.com/docs/configure/command-line)
- [Jupyter-Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

---

[Start](../../README.md) · [Vorbereitung](../TECHNISCHE_VORBEREITUNG.md) · [Testanleitung](../TESTANLEITUNG_ETAPPE1.md) · [Hilfe](../TROUBLESHOOTING.md)
