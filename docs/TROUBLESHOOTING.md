[Start](../README.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md)

# Fehler finden und beheben

Führe Befehle im Repo-Hauptordner aus. Beginne bei der ersten fehlgeschlagenen Prüfung im Terminal bzw. Notebook. Der Bericht `data/output/setup_report.json` enthält zusätzliche Angaben.

## Schnellübersicht

| Meldung oder Beobachtung | Nächster Schritt |
|---|---|
| Neue Demos oder Tasks fehlen im Codespace; `git pull` meldet lokale Änderungen | [Codespace abgleichen: Option A behält Änderungen, Option B verwirft sie](setup/CODESPACES.md#codespace-mit-github-abgleichen). |
| `conda` nicht gefunden | Unter Windows Anaconda Prompt verwenden; unter macOS/Linux ein Terminal mit initialisiertem Conda öffnen. Codespaces verwendet kein Conda. |
| `environment.yml` oder `scripts/verify_setup.py` nicht gefunden | In den inneren Repo-Ordner wechseln, nicht im ZIP oder dessen äusserem Entpackordner arbeiten. |
| `ModuleNotFoundError` | Richtige Umgebung aktivieren bzw. richtigen Notebook-Kernel auswählen. Siehe unten. |
| Docker meldet `npipe`, fehlende Verbindung oder „daemon not running“ | Docker Desktop starten, dessen Bereitschaft abwarten und `docker info` prüfen. Unter Windows Linux-Container verwenden. |
| Port 4444 bereits belegt | Nur lokal den Port in `.env` ändern und den Selenium-Container neu erstellen; genaue Schritte unten. |
| Browser-Sitzung kann nicht erstellt werden | Bereitschaft des Dienstes prüfen; Terminal- und Notebooktest nacheinander ausführen. Es ist eine gleichzeitige Browser-Sitzung vorgesehen. |
| Keine sichtbare Chromium-Oberfläche | Erwartetes Verhalten: Der automatisierte Browser läuft im Container. Entscheidend ist das Prüfergebnis. |
| `TEILTEST OK` statt `SETUP OK` | Der Browser wurde ausgelassen. Vollständigen Test ohne `--skip-browser` ausführen. |
| Nur `--online` meldet Fehler | Externe Erreichbarkeit gesondert prüfen. Der Grundtest kann trotzdem funktionieren. |

## Falsche Python-Umgebung oder fehlende Pakete

**Lokal** im Repo-Hauptordner:

```bash
conda activate webscraping-workshop
python -c "import sys; print(sys.executable)"
python -m pip check
```

Der ausgegebene Python-Pfad muss zur Umgebung `webscraping-workshop` gehören. Bei unvollständiger Installation:

```bash
conda env update -n webscraping-workshop -f environment.yml
python -m ipykernel install --user --name webscraping-workshop --display-name "Python (webscraping-workshop)"
```

**Codespaces:**

```bash
bash .devcontainer/post-create.sh
source /home/vscode/.venvs/webscraping-workshop/bin/activate
python -c "import sys; print(sys.executable)"
```

Hier wird `/home/vscode/.venvs/webscraping-workshop/bin/python` erwartet. Wähle im Notebook anschliessend **Python (webscraping-workshop)** und starte den Kernel neu. Nutze keine pauschalen Installationsbefehle in der ersten Notebook-Zelle: Sie können eine andere Umgebung verändern als diejenige, die Du gerade verwenden möchtest.

## Selenium lokal nicht erreichbar

```bash
docker info
docker compose ps
docker compose logs --tail 80 selenium
```

Der Dienst `selenium` sollte laufen und nach dem Start `healthy` anzeigen. Starte ihn nötigenfalls mit `docker compose up -d`. Der Einrichtungstest wartet bis zu 45 Sekunden auf die Bereitschaft.

Bleibt der Dienst fehlerhaft, prüfe die Logausgabe. Wenn keine andere Ursache erkennbar ist, starte nur den Browser-Dienst neu:

```bash
docker compose restart selenium
python scripts/verify_setup.py
```

Das erfordert weder eine Neuerstellung der Conda-Umgebung noch einen Neustart Deines Rechners. Falls mehrere Tests gleichzeitig laufen, beende sie und starte genau einen erneut.

## Lokaler Port 4444 ist belegt

Ändere in `.env` die Zeile auf beispielsweise:

```dotenv
SELENIUM_PORT=4445
```

Erstelle danach den lokalen Dienst neu, damit Docker die geänderte Portzuordnung übernimmt:

```bash
docker compose up -d --force-recreate selenium
python scripts/verify_setup.py
```

Ein blosses `docker compose restart` übernimmt keine geänderte Portzuordnung. Starte für das Notebook auch den Kernel neu, damit es die aktuelle Konfiguration liest. Der neue lokale Endpunkt lautet `http://127.0.0.1:4445`.

Falls Du selbst die Umgebungsvariable `SELENIUM_REMOTE_URL` gesetzt hast, hat sie Vorrang vor dem lokalen Port. Entferne eine veraltete Überschreibung oder passe sie an. Die voreingestellte `.env.example` setzt diese Variable nicht.

## Selenium in Codespaces nicht erreichbar

In Codespaces gilt der interne Dienstname `selenium`. Prüfe zuerst die konfigurierte Adresse und den Status:

```bash
source /home/vscode/.venvs/webscraping-workshop/bin/activate
python -c "import os; print(os.getenv('SELENIUM_REMOTE_URL'))"
python -c "import requests; r = requests.get('http://selenium:4444/status', timeout=10); print(r.status_code); print(r.text)"
```

Erwartet werden `http://selenium:4444`, HTTP-Status `200` und im JSON `"ready": true`. Wenn das funktioniert, führe den vollständigen Einrichtungstest nochmals aus. Prüfe bei einem Notebookfehler zusätzlich den ausgewählten Kernel.

Wenn der Dienstname nicht aufgelöst wird oder keine Verbindung möglich ist:

1. Prüfe, ob der Codespace mit der mitgelieferten `.devcontainer/devcontainer.json` angelegt wurde und die Erstinstallation abgeschlossen ist.
2. Öffne über die Befehlspalette **Codespaces: View Creation Log** bzw. die angebotenen Erstellungs-/Containerlogs. Suche nach Fehlern beim Start des Dienstes `selenium` oder beim Laden seines Images.
3. Falls Du nur Python-Pakete reparieren musst, genügt `bash .devcontainer/post-create.sh`. Dieses Skript repariert keinen ausgefallenen Nebendienst.
4. Wenn die Container-Erstellung fehlgeschlagen ist oder eine korrigierte Devcontainer-Konfiguration übernommen werden muss, speichere Deine Dateien und verwende ausnahmsweise **Codespaces: Rebuild Container** in der Befehlspalette. Dadurch werden die Dienste anhand der Repo-Konfiguration neu aufgebaut. Prüfe danach erneut.

Der Arbeitscontainer enthält keine Docker-CLI zur Verwaltung des Nebendienstes. Die lokale `compose.yaml` dort zu starten, einen lokalen Port zu ändern oder Port 4444 öffentlich freizugeben behebt diesen Fehler daher nicht. Bei weiterhin fehlerhaftem Dienst sende die relevante Logausgabe mit; ein neuer Codespace ist kein erster Reparaturschritt.

## Download oder Installation schlägt fehl

Prüfe zuerst die konkrete Fehlermeldung: fehlender Internetzugang, Proxy, Zertifikatsprüfung, fehlender Speicher oder nicht erreichbare Paketquelle erfordern unterschiedliche Lösungen. Wiederhole die Einrichtung nach Behebung der Ursache mit den oben beschriebenen Aktualisierungsbefehlen. Schalte die TLS-/Zertifikatsprüfung nicht pauschal aus.

## Was Du bei einer Fehlermeldung weitergeben solltest

- Weg: lokal oder Codespaces; lokal zusätzlich Betriebssystem und Prozessorarchitektur.
- Den ausgeführten Befehl bzw. die erste fehlschlagende Notebook-Zelle.
- Die vollständige zugehörige Fehlermeldung und `data/output/setup_report.json`, falls erstellt.
- Bei einem Docker-/Dienstfehler die passende Logausgabe.

Ein Screenshot kann helfen; kopierbarer Fehlertext erleichtert die Diagnose. Teile keine Anmeldetokens oder sonstigen privaten Konfigurationen.

## Offizielle Dokumentation

- [GitHub: Codespaces-Protokolle öffnen](https://docs.github.com/en/codespaces/troubleshooting/github-codespaces-logs)
- [GitHub: Container neu aufbauen](https://docs.github.com/en/codespaces/developing-in-a-codespace/rebuilding-the-container-in-a-codespace)

---

[Start](../README.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md)
