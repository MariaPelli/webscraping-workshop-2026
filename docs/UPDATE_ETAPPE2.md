[Start](../README.md) · [Änderungen](../CHANGELOG.md) · [Testanleitung](TESTANLEITUNG_ETAPPE2.md) · [API-Zugang](API_ZUGANG.md)

# Von Etappe 1 auf Etappe 2 aktualisieren

Die technische Basis aus Etappe 1 wurde lokal in JupyterLab und in GitHub Codespaces erfolgreich mit `SETUP OK` geprüft (Rückmeldung zur Einrichtung). Das bestätigt die Umgebung; die neuen Demos und Aufgaben werden separat geprüft. Eine erneute Einrichtungskontrolle ist für dieses Update nicht erforderlich.

**Für dieses Update bleiben Python-Pakete, `environment.yml`, `requirements.txt`, `compose.yaml` und `.devcontainer/` unverändert.** Du brauchst weder eine neue Conda-Umgebung noch einen Codespaces-Rebuild. Die Idle-Timeout-Einstellungen werden nicht verändert. Ein persönliches Kostenlimit wird durch das Repo weder eingerichtet noch verifiziert.

## 1. Neue Dateien lokal übernehmen

1. Speichere offene Notebooks. Bewahre eigene Änderungen auf, bevor Du Dateien ersetzt; bei Git kannst Du sie separat committen. Sichere andere eigene Dateien bei Bedarf ausserhalb des Repo-Ordners.
2. Entpacke das neue ZIP in einen vorübergehenden Ordner.
3. Kopiere den Inhalt des darin enthaltenen Repo-Hauptordners in Deinen **bestehenden** Repo-Hauptordner. Achte darauf, keinen zusätzlichen verschachtelten Ordner anzulegen.
4. Ersetze die aktualisierten Projektdateien. Behalte Deinen vorhandenen `.git`-Ordner und Deine lokale `.env`. Lösche Deinen bisherigen Repo-Ordner nicht.
5. Prüfe `VERSION` und das [Changelog](../CHANGELOG.md). Etappe 2 trägt die Version `0.2.0-etappe2`.

Ein Dozierendenpaket kann zusätzlich `instructor/` und die Lösungsdateien in den Task-Ordnern enthalten. Die `.gitignore` schliesst diese aus; sie sollen nicht versehentlich im Studierenden-Repo veröffentlicht werden.

## 2. Bestehende .env behalten

Die Kernbeispiele funktionieren auch ohne neue Schlüssel. Wenn Du optionale API-Live-Abrufe nutzen möchtest, ergänze in Deiner bestehenden `.env` nur die noch fehlenden Einträge:

```dotenv
COINGECKO_DEMO_API_KEY=
FLICKR_API_KEY=
```

Lass die Werte zunächst leer oder ergänze später Deine eigenen Schlüssel nach der [API-Anleitung](API_ZUGANG.md). Behalte insbesondere Deinen eventuell angepassten `SELENIUM_PORT`. Kopiere die neue `.env.example` nicht über Deine vorhandene `.env`.

## 3. Lokal starten

Im Anaconda Prompt bzw. Terminal, im Repo-Hauptordner:

```bash
conda activate webscraping-workshop
docker compose up -d
```

Starte anschliessend `jupyter lab` oder `code .`. Wähle weiterhin **Python (webscraping-workshop)**. Starte den Notebook-Kernel frisch, damit aktualisierte Python-Module und neue Konfiguration eingelesen werden. Die [Testanleitung für Etappe 2](TESTANLEITUNG_ETAPPE2.md) beschreibt den Kontrolllauf.

Nur bei einem neuen technischen Fehler oder einer noch ungeprüften Umgebung hilft optional `python scripts/verify_setup.py` bei der Diagnose. Für die bereits erfolgreich geprüfte Umgebung kannst Du direkt mit den neuen Demos beginnen.

## 4. Git-Änderungen vor dem Push prüfen

Diese Schritte gelten, wenn Dein bestehender Repo-Ordner bereits mit GitHub verbunden ist:

```bash
git status
git diff --stat
git diff --name-only
```

`git diff` zeigt Änderungen bereits versionierter Dateien; neue Dateien erkennst Du zusätzlich an `git status`. Vergleiche bei Bedarf einzelne Dokumente mit `git diff -- README.md`. Prüfe dabei insbesondere, dass Deine eigenen Änderungen erhalten bleiben.

Prüfe die Ausschlüsse des Dozierendenpakets:

```bash
git check-ignore instructor/LEITFADEN.md tasks/01_statischer_katalog/task_sample_solution.ipynb tasks/01_statischer_katalog/WALKTHROUGH.md tasks/02_dynamischer_katalog/task_sample_solution.ipynb tasks/02_dynamischer_katalog/WALKTHROUGH.md
```

Bei korrekt greifenden Regeln gibt Git die ausgeschlossenen Pfade aus. **Bereits versionierte Dateien werden durch `.gitignore` nicht nachträglich entfernt.** Falls Lösungen oder `.env` zuvor schon versioniert waren, bereinige das gezielt vor dem Push; `git add -f` ist dafür kein geeigneter Schritt.

Wenn die Änderungen stimmen:

```bash
git add .
git diff --cached --stat
git diff --cached --name-only
```

Kontrolliere die vorgemerkte Liste: keine `.env`, keine erzeugten Ausgaben, kein `instructor/`, keine `task_sample_solution.ipynb` und keine `WALKTHROUGH.md`. Danach:

```bash
git commit -m "Add webscraping demos and tasks"
git push
```

Falls noch kein GitHub-Repo besteht, nutze stattdessen die [Anleitung zur erstmaligen Bereitstellung](GITHUB_UPLOAD.md).

## 5. Bestehenden Codespace aktualisieren

Speichere Deine Arbeiten im Codespace und prüfe zuerst dessen Arbeitsverzeichnis:

```bash
cd /workspaces/webscraping-workshop-2026
git status
```

Wenn dort eigene Änderungen liegen, sichere bzw. committe sie bewusst, bevor Du den Stand von GitHub übernimmst. Überschreibe sie nicht mit einem harten Reset. Bei einem sauberen Arbeitsverzeichnis:

```bash
git pull --ff-only
source /home/vscode/.venvs/webscraping-workshop/bin/activate
```

Falls Git unterschiedliche lokale und entfernte Änderungen meldet, halte an und kläre diese Unterschiede. Ersetze `--ff-only` nicht unbesehen durch erzwungene Befehle.

Starte anschliessend die Notebook-Kernel frisch und führe die neuen Demos nacheinander aus. Der Selenium-Nebendienst und die interne Adresse bleiben bestehen; es werden keine zusätzlichen Ports freigegeben. Eine lokal ergänzte `.env` wird nicht mitgepusht: Für optionale Live-Abrufe im Codespace trägst Du eigene Schlüssel dort separat ein.

Auch im bereits geprüften Codespace ist keine erneute Setup-Prüfung nötig. Verwende `python scripts/verify_setup.py` nur bei technischen Problemen oder wenn der Zustand der Umgebung unklar ist.

---

[Start](../README.md) · [Testanleitung](TESTANLEITUNG_ETAPPE2.md) · [Hilfe](TROUBLESHOOTING.md)
