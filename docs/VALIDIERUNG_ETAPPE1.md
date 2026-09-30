[Start](../README.md) · [Testanleitung](TESTANLEITUNG_ETAPPE1.md) · [Hilfe](TROUBLESHOOTING.md)

# Prüfstatus – Etappe 1

Paketstand: **0.1.1-etappe1**, 30.09.2026.

Dieses Protokoll unterscheidet die hier ausgeführten Prüfungen von den noch auf den Zielumgebungen auszuführenden Tests. Eine gültige Konfigurationsdatei allein belegt keinen erfolgreichen Containerstart.

## Bei der Erstellung geprüft

| Prüfung | Ergebnis |
|---|---|
| Installation aller direkten Abhängigkeiten aus `requirements.txt` in einer frischen Python-3.12-Umgebung unter Linux | Erfolgreich |
| Paketverträglichkeit mit `python -m pip check` | `No broken requirements found.` |
| Registrierung des Notebook-Kernels | Erfolgreich in der isolierten Prüfumgebung |
| JSON-/YAML-Dateien und Bash-Syntax | Erfolgreich geprüft |
| Terminaltest mit `--skip-browser` | `TEILTEST OK`; echter Loopback-HTTP-Abruf, HTML-/JSON-Vergleich und CSV-Roundtrip bestanden |
| Vollständiger Terminaltest ohne vorhandenen Selenium-Dienst | Erwarteter Fehler nach Bereitschaftsfrist; Exitcode 1; kein falsches `SETUP OK` |
| Sieben gezielte Regressionstests | Bestanden; prüfen Kernablauf, Pfade, Konfiguration und die Unterscheidung von Fehlern/Teiltests |
| Notebook-Dateiformat und Python-Syntax | Gültiges Notebook ohne vorausgefüllte Ausgaben |
| Notebook-Codezellen der Reihe nach, Browserprüfung ausdrücklich ausgelassen | Erfolgreich in einem frischen Python-Prozess ausgeführt; kein Jupyter-Kerneltest |
| Lokale Dokumentationslinks | Alle Ziele vorhanden |
| Git-Ausschlüsse | `.env`, Ausgaben und spätere Lösungen ausgeschlossen; erforderliche Konfigurationsdateien eingeschlossen |

Die installierten direkten Abhängigkeiten sind exakt festgelegt. Transitive Abhängigkeiten löst pip auf; `requirements.txt` ist kein vollständiger plattformübergreifender Lockfile.

## Rückmeldung aus den Zielumgebungen

Die Anwenderin meldete am 30.09.2026 erfolgreiche Läufe von `notebooks/00_setup_check.ipynb` lokal über JupyterLab sowie in GitHub Codespaces (`SETUP OK`). Diese Statusangaben beruhen auf ihrer Rückmeldung. Ein separater lokaler VS-Code-Lauf wurde nicht gemeldet.

Die Ergänzung in Version 0.1.1 betrifft ausschliesslich die Dokumentation und den Versionsstand. Python-Code, Notebook, Paketversionen sowie Docker-/Devcontainer-Konfiguration bleiben gegenüber dem getesteten Erstpaket unverändert.

## Weitere Prüfungen auf den Zielumgebungen

| Prüfung | Status |
|---|---|
| Neueinrichtung auf weiteren lokalen Rechnern/Betriebssystemen | Offen |
| Lokaler Notebooklauf über JupyterLab | Erfolgreich laut Rückmeldung der Anwenderin; oben dokumentiert |
| Separater lokaler Terminaltest | Noch nicht gesondert rückgemeldet |
| Lokaler Notebooklauf über VS Code | Offen |
| Erster Start des Repos in einem echten GitHub Codespace | Erfolgreich laut Rückmeldung der Anwenderin vom 30.09.2026 |
| Vollständiger Test in Codespaces inklusive Selenium | Erfolgreich laut Rückmeldung der Anwenderin vom 30.09.2026 |
| Notebooklauf in Codespaces mit tatsächlichem Jupyter-Kernel | Erfolgreich laut Rückmeldung der Anwenderin vom 30.09.2026 |
| Native Ausführung unter macOS, einschliesslich Apple Silicon | Offen |

In der Erstellungsumgebung stehen kein ausführbarer Docker-Dienst, keine Conda-Installation und kein Browser zur Verfügung. Deshalb wird hier kein vollständiger `SETUP OK`-Nachweis für Docker, Windows, macOS oder Codespaces behauptet. Der Browser-Test im Paket erzeugt eine echte Selenium-Sitzung und prüft drei von JavaScript erstellte Tabellenzeilen; er überspringt einen fehlenden Browser nicht stillschweigend.

Der zusätzlich versuchte Start eines echten Jupyter-Kernels scheiterte in der Erstellungsumgebung an eingeschränkten Socket-Berechtigungen (`Operation not permitted`). Als getrennte Prüfung wurden deshalb die Notebook-Codezellen ohne Kernel in ihrer Reihenfolge ausgeführt. Das ersetzt die Kernel-Auswahl und den vollständigen Notebooklauf auf Deinem Rechner bzw. in Codespaces nicht. Das ausgelieferte Notebook verlangt standardmässig den vollständigen Test inklusive Browser.

Live-Abfragen bei ECB und Books to Scrape wurden in dieser Etappe nicht als erfolgreich getestet ausgewiesen. Sie sind als gesonderte Option verfügbar; die Kerntests verwenden ausschliesslich mitgelieferte Daten. Die Regressionstests simulieren einzelne Fehlerfälle zur Prüfung der Statuslogik und weisen diese nicht als echte Browser-/Live-Läufe aus.

Das Selenium-Image ist auf `selenium/standalone-chromium:4.48.0-20260905` festgelegt. Die Wahl des Tags und der Konfiguration orientiert sich an der [offiziellen Selenium-Dokumentation](https://github.com/SeleniumHQ/docker-selenium); der Start lokal und in Codespaces wurde durch die Anwenderin bestätigt. Weitere Zielrechner sind nicht separat geprüft.

## Rückmeldung

Verwende die [Testanleitung](TESTANLEITUNG_ETAPPE1.md). Entscheidend sind die Schlussmeldung im Terminal und im Notebook sowie der erzeugte Bericht `data/output/setup_report.json`. Sichere Berichte getrennt nach lokalem Lauf und Codespaces-Lauf, weil der Standardbericht beim nächsten Test überschrieben wird.

[Zurück zur Startseite](../README.md)
