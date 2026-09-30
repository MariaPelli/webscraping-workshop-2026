# Daten für den Einrichtungstest

[← Startseite](../README.md) · [Testanleitung](../docs/TESTANLEITUNG_ETAPPE1.md) · [Testnotebook](../notebooks/00_setup_check.ipynb)

Alle Daten in `fixtures/` sind synthetisch: drei frei erfundene Bücher mit IDs, Titeln und Preisen in CHF. Sie enthalten keine persönlichen Daten oder Zugangsdaten.

| Datei | Zweck |
|---|---|
| `fixtures/synthetic_records.json` | Drei strukturierte Datensätze als Vergleichsbasis. |
| `fixtures/static_catalog.html` | Dieselben Datensätze als HTML-Tabelle. |
| `fixtures/dynamic_catalog.html` | Dieselben Datensätze werden nach dem Laden durch JavaScript erzeugt. |

Der Einrichtungstest startet vorübergehend einen HTTP-Server auf einer freien lokalen Portnummer. `requests` ruft JSON und HTML über diesen Server ab. Der Server endet nach der Prüfung automatisch. Der Selenium-Browser erhält die dynamische Seite als `data:`-URL und benötigt deshalb keinen Zugriff auf den HTTP-Server Deines Rechners.

Nach erfolgreichem Basistest findest Du unter `output/` die Datei `setup_records.csv`. Das Skript und das Notebook speichern zudem `setup_report.json`; ein erneuter Lauf ersetzt diese Dateien. Sie sind in `.gitignore` ausgeschlossen. Der Report enthält Prüfstatus und Paketversionen, aber keine Umgebungsvariablen oder Selenium-Adresse.

Die Grundprüfung benötigt nach der Installation und dem Start des Selenium-Dienstes keine externe Website. Nur `--online` ruft zusätzlich öffentliche Beispielquellen ab. Diese Live-Daten werden nicht als Kursdatensatz gespeichert.

[↑ Startseite](../README.md)
