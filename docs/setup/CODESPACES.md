[Start](../../README.md) · [Vorbereitung](../TECHNISCHE_VORBEREITUNG.md) · [Lokal](LOKAL.md) · [Testanleitung](../TESTANLEITUNG_ETAPPE1.md) · [Hilfe](../TROUBLESHOOTING.md)

# In GitHub Codespaces arbeiten

Das Repo muss zuerst vollständig auf GitHub liegen, einschliesslich `.devcontainer/`. Ein hochgeladenes ZIP allein genügt nicht. Falls Du das Repo bereitstellst, beginne mit der [GitHub-Anleitung](../GITHUB_UPLOAD.md).

## 1. Codespace erstellen

1. Öffne das Repo auf GitHub und wähle den gewünschten Branch, normalerweise `main`.
2. Wähle **Code → Codespaces → Create codespace on main**. Falls der Branch anders heisst, steht sein Name auf der Schaltfläche.
3. Warte, bis der Container eingerichtet und das Einrichtungsskript abgeschlossen ist. Der Editor kann schon sichtbar sein, während im Hintergrund noch Pakete installiert werden.
4. Öffne über **Terminal → New Terminal** ein neues Terminal.

Die Konfiguration startet einen Python-Arbeitscontainer und einen Selenium-Nebendienst. Das Skript `.devcontainer/post-create.sh` erstellt die Python-Umgebung und registriert den Notebook-Kernel. Du führst in Codespaces keine Conda-Befehle und keine lokalen Docker-Startbefehle aus.

## 2. Einrichtung prüfen

Im Codespaces-Terminal:

```bash
cd /workspaces/webscraping-workshop-2026
source /home/vscode/.venvs/webscraping-workshop/bin/activate
python scripts/verify_setup.py
```

**Erwartetes Endergebnis: `SETUP OK`.** Der Bericht liegt unter `data/output/setup_report.json`, die CSV-Beispieldaten unter `data/output/setup_records.csv`.

Für diesen Test brauchst Du keine Portweiterleitung und keine öffentliche Portfreigabe. Der Python-Code erreicht den Browser-Dienst intern über **`http://selenium:4444`**. `localhost` im Codespace bezeichnet den Arbeitscontainer, nicht Deinen eigenen Rechner und nicht den separaten Selenium-Container. Die passende Adresse ist bereits über `SELENIUM_REMOTE_URL` gesetzt.

## 3. Notebook ausführen

1. Öffne im Datei-Explorer `notebooks/00_setup_check.ipynb`.
2. Wähle rechts oben **Select Kernel** und dann **Python (webscraping-workshop)**. Je nach Oberfläche findest Du ihn unter **Select Another Kernel → Jupyter Kernel**.
3. Falls nur Python-Umgebungen angezeigt werden, wähle den Interpreter `/home/vscode/.venvs/webscraping-workshop/bin/python`.
4. Starte den Kernel frisch und führe mit **Run All** alle Zellen aus.

Auch das Notebook muss **`SETUP OK`** melden. Es nutzt dieselbe Prüflogik wie der Terminaltest. Ein laufender Terminaltest allein bestätigt noch nicht, dass im Notebook der richtige Kernel ausgewählt ist.

## Falls die Pakete oder der Kernel fehlen

Lass zunächst eine noch laufende Erstinstallation fertig werden. Ist sie abgebrochen, kannst Du die Python-Einrichtung im bestehenden Codespace erneut ausführen:

```bash
cd /workspaces/webscraping-workshop-2026
bash .devcontainer/post-create.sh
source /home/vscode/.venvs/webscraping-workshop/bin/activate
python scripts/verify_setup.py
```

Wähle danach den Kernel erneut. Dafür ist normalerweise kein Neustart und kein Rebuild erforderlich. Das Skript repariert die Python-Umgebung; es startet einen ausgefallenen Selenium-Nebendienst nicht neu. Hinweise für diesen gesonderten Fall stehen in der [Fehlerhilfe](../TROUBLESHOOTING.md#selenium-in-codespaces-nicht-erreichbar).

## Codespace mit GitHub abgleichen

Wenn neue Dateien bereits auf GitHub liegen, übernimmst Du sie im **Terminal des bestehenden Codespaces**, im Repo-Hauptordner und auf Branch **`main`**. Speichere und schliesse vorher offene Notebooks. Wähle **eine** der beiden Optionen.

### Option A – eigene Änderungen behalten

```bash
git pull --ff-only --autostash
```

Git legt Änderungen an bereits versionierten Dateien vorübergehend ab, holt die neuen Dateien und wendet Deine Änderungen anschliessend wieder an. Selbst angelegte Dateien bleiben erhalten. Dafür brauchst Du keinen eigenen Commit.

Falls Git einen Konflikt oder einen Abbruch meldet, halte an und kläre die Meldung. Bei einem Konflikt beim Wiederanwenden bleiben die Änderungen im Git-Stash gesichert; die Zusammenführung ist dann noch nicht abgeschlossen.

### Option B – lokale Änderungen verwerfen und GitHub-Stand übernehmen

**Damit verwirfst Du lokale Änderungen und setzt den Projektordner auf `origin/main` zurück. Auch lokale Commits werden von diesem Branch entfernt. Selbst angelegte, nicht von Git ignorierte Dateien und Ordner werden gelöscht.**

Führe die drei Befehle nacheinander aus; bei einem Fehler stoppe:

```bash
git fetch origin
git reset --hard origin/main
git clean -fd
```

Von Git ignorierte Dateien wie Deine `.env` und Ausgaben unter `data/output/` bleiben erhalten. Die installierte Python-Umgebung und der Selenium-Dienst bleiben ebenfalls bestehen. Der Codespace wird dabei nicht neu erstellt.

Für die neuen Demos und Tasks ist kein Rebuild nötig. Öffne danach die aktualisierten Notebooks und starte ihren Kernel neu.

## Arbeit fortsetzen und beenden

Öffne später denselben Codespace über [github.com/codespaces](https://github.com/codespaces). Erstelle nicht für jede Arbeitssitzung einen neuen. Speichere Deine Dateien und stoppe den Codespace dort, wenn Du fertig bist. Ein geschlossenes Browser-Tab allein ist kein verlässlicher Hinweis, dass der Codespace bereits gestoppt ist.

## Offizielle Dokumentation

- [GitHub: Codespace aus einem Repository erstellen](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository)
- [GitHub: Einführung in Devcontainer](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers)

---

[Start](../../README.md) · [Vorbereitung](../TECHNISCHE_VORBEREITUNG.md) · [Testanleitung](../TESTANLEITUNG_ETAPPE1.md) · [Hilfe](../TROUBLESHOOTING.md)
