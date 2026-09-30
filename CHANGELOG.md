[Startseite](README.md) · [Testanleitung](docs/TESTANLEITUNG_ETAPPE2.md) · [Prüfstatus](docs/VALIDIERUNG_ETAPPE2.md)

# Änderungen

## 0.2.0-etappe2 – 30.09.2026

- Vier ausgearbeitete Demos: EZB-XML, CoinGecko/Flickr REST APIs, BeautifulSoup und Selenium.
- Zwei Aufgaben mit Arbeitsnotebooks, Musterlösungen und Walkthroughs direkt in den Task-Ordnern.
- Reproduzierbare synthetische Daten als Standard; externe Live-Abrufe ausdrücklich zuschaltbar.
- Vergleich derselben HTML-Quelle vor und nach JavaScript sowie nach einer Browserinteraktion.
- Datenprüfung, begrenzte Pagination, Rohdaten/CSV-Export und Herkunftsmetadaten.
- Optionale, leere API-Key-Einträge in `.env.example`; bestehende `.env` beim Update behalten.
- Unterrichts-, API-, Update- und Testanleitungen sowie Dozierendenleitfaden ergänzt.
- Bestehende Python-Abhängigkeiten, Container-Konfiguration, Setup-Prüflogik und Setup-Notebook unverändert. Keine Neuinstallation und kein Codespaces-Rebuild erforderlich.
- Lokales JupyterLab-Setup und Codespaces-Setup durch Rückmeldung der Anwenderin bestätigt. Die neuen Browsernotebooks sind separat zu testen; siehe [Prüfprotokoll](docs/VALIDIERUNG_ETAPPE2.md).
- Keine Dateien entfernt oder umbenannt, die in Etappe 1 ausgeliefert wurden. Keine Zugangsdaten aus den Vorjahresunterlagen übernommen.


## 0.1.1-etappe1 — 30.09.2026

- VS Code als lokale Alternative zu JupyterLab ergänzt: nach `conda activate webscraping-workshop` wahlweise `jupyter lab` oder `code .` starten.
- Kernel-Auswahl, VS-Code-Erweiterungen und Hilfe bei fehlendem `code`-Befehl beschrieben.
- README, Umgebungsvergleich, Vorbereitung und Testanleitung abgeglichen.
- Erfolgreichen lokalen JupyterLab-Notebooklauf laut Rückmeldung der Anwenderin festgehalten.

Nur Dokumentation und Versionsstand geändert. Die bestehende Conda-Umgebung kann weiterverwendet werden; eine Neuinstallation oder ein erneuter lokaler Volltest ist für diese Ergänzung nicht erforderlich. Nächster Prüfschritt ist Codespaces.

## 0.1.0-etappe1 — 30.09.2026

Erstes Testpaket für den Themenblock Webscraping im Modul Data Engineering.

- Gemeinsame Python-Abhängigkeiten für Anaconda und GitHub Codespaces.
- Selenium mit Chromium als Docker-Dienst; kein manueller Treiberdownload.
- Einrichtungstest für Python, HTTP, HTML-/JSON-Verarbeitung, CSV-Export und JavaScript im Browser.
- Mitgelieferte synthetische Testdaten für einen Grundtest ohne externe Datenquellen.
- Startanleitungen, Umgebungsvergleich, Fehlersuche und Rückmeldeschema.

Dieses Paket dient der technischen Erprobung. Demos, Tasks und Musterlösungen werden nach der Rückmeldung zur Einrichtung in Etappe 2 ergänzt.

[Zurück zur Startseite](README.md)
