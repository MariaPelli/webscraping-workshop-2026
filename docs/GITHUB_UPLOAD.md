[Start](../README.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md)

# Das Repo auf GitHub bereitstellen

Die lokale Einrichtung funktioniert bereits mit dem entpackten ZIP. Ein GitHub-Repo brauchst Du erst für Codespaces und zum Teilen bzw. gemeinsamen Versionieren.

**Lade nicht einfach das ZIP als einzelne Datei auf GitHub hoch.** GitHub entpackt es dabei nicht; Codespaces benötigt die Dateien direkt im Repo. Git bzw. GitHub Desktop übertragen auch die benötigten Konfigurationsdateien und den Ordner `.devcontainer/`.

## Variante A – mit Git

Die folgenden Schritte gelten für den frisch entpackten Ordner **ohne bestehende Git-Historie** und ein **neues, leeres GitHub-Repo**. Git muss lokal installiert sein. Wenn Du stattdessen ein bestehendes Repo weiterbearbeitest, behalte dessen Historie und Remote-Konfiguration bei.

1. Erstelle auf [github.com/new](https://github.com/new) ein Repository, beispielsweise `webscraping-workshop-2026`. Wähle die gewünschte Sichtbarkeit. **Lass die Optionen für README, `.gitignore` und Lizenz leer**, denn dieses Paket enthält bereits Projektdateien.
2. Öffne ein Terminal im entpackten Repo-Hauptordner. Unter Windows kann das Anaconda Prompt mit installiertem Git sein.
3. Prüfe vor dem ersten Commit die zu übertragenden Dateien:

```bash
git init -b main
git add .
git status
```

Bei `git status` müssen unter anderem `.devcontainer/devcontainer.json`, `.devcontainer/compose.yaml`, `.devcontainer/post-create.sh`, `.env.example` und `.gitignore` erscheinen. Deine lokale `.env` und Dateien aus `data/output/` sollen nicht vorgemerkt sein; `.gitkeep` ist dort absichtlich erlaubt.

4. Erstelle den ersten Commit und verbinde das leere GitHub-Repo:

```bash
git commit -m "Add webscraping workshop technical setup"
git remote add origin https://github.com/YOUR_ACCOUNT/webscraping-workshop-2026.git
git push -u origin main
```

Ersetze **`YOUR_ACCOUNT`** und gegebenenfalls den Repo-Namen durch die Werte Deines neuen Repos. Die Beispieladresse ist ein Platzhalter, kein bereits bereitgestelltes Repository. Folge beim Push der Anmeldung von Git/GitHub; trage keine Zugangsdaten in Projektdateien ein.

Wenn Git vor dem Commit einen Namen und eine E-Mail-Adresse verlangt, hinterlege Deine gewünschten Angaben in der Git-Konfiguration. Falls `origin already exists` erscheint, prüfe zuerst `git remote -v`, statt einen bestehenden Remote ungeprüft zu ersetzen. Wenn das Zielrepo bereits Dateien enthält, passt dieser Ablauf für ein leeres Repo nicht; verwende dann dessen bestehende Git-Historie.

## Variante B – mit GitHub Desktop

1. Entpacke das Paket lokal und öffne GitHub Desktop.
2. Wähle **File → Add local repository** und den Ordner mit der `README.md`. Wenn GitHub Desktop meldet, dass dieser Ordner noch kein Git-Repository ist, nutze die angebotene Funktion zum Erstellen eines Repositories **an diesem Ort**. Achte darauf, keinen zusätzlichen verschachtelten Projektordner anzulegen.
3. Prüfe in **Changes**, dass `.devcontainer/`, `.env.example` und `.gitignore` enthalten sind und Deine `.env` ausgeschlossen ist.
4. Erstelle den ersten Commit und wähle **Publish repository**. Lege Name und Sichtbarkeit fest.

## Auf GitHub kontrollieren

- Die `README.md` erscheint auf der Startseite des Repos.
- `environment.yml`, `requirements.txt`, `compose.yaml` und der Ordner `.devcontainer/` liegen auf derselben obersten Ebene wie im lokalen Paket.
- Im Ordner `notebooks/` ist `00_setup_check.ipynb` vorhanden.
- Der Branch enthält einen Commit; ein leerer Branch kann keinen Codespace bereitstellen.

Folge danach der [Codespaces-Anleitung](setup/CODESPACES.md). Dafür musst Du die lokale Conda-Umgebung nicht ändern.

## Weitere Zwischenpakete übernehmen

Behalte Dein vorhandenes Git-Repo und dessen `.git`-Ordner bei. Übernimm die geänderten Projektdateien aus dem neuen Paket in denselben Repo-Hauptordner; überschreibe Deine lokale `.env` nicht. Prüfe mit `git status` bzw. in GitHub Desktop die Änderungen vor dem Commit. Wenn später Dateien entfernt oder umbenannt werden, beachte dazu die Hinweise im jeweiligen [Changelog](../CHANGELOG.md), damit keine alten Dateien zurückbleiben.

## Offizielle Dokumentation

- [GitHub: lokalen Code zu GitHub hinzufügen](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [GitHub Desktop: ein lokales Repository hinzufügen](https://docs.github.com/en/desktop/adding-and-cloning-repositories/adding-a-repository-from-your-local-computer-to-github-desktop)

---

[Start](../README.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md)
