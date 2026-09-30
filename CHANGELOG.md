[Startseite](README.md) · [Testanleitung](docs/TESTANLEITUNG_ETAPPE1.md) · [Prüfstatus](docs/VALIDIERUNG_ETAPPE1.md)

# Änderungen

## 0.1.1-etappe1 — 30.09.2026

- VS Code als lokale Alternative zu JupyterLab ergänzt: nach `conda activate webscraping-workshop` wahlweise `jupyter lab` oder `code .` starten.
- Kernel-Auswahl, VS-Code-Erweiterungen und Hilfe bei fehlendem `code`-Befehl beschrieben.
- README, Umgebungsvergleich, Vorbereitung und Testanleitung abgeglichen.
- Erfolgreichen lokalen JupyterLab-Notebooklauf laut Rückmeldung von Maria festgehalten.

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
