[Start](../README.md) · [Update](UPDATE_ETAPPE2.md) · [Testanleitung](TESTANLEITUNG_ETAPPE2.md)

# Prüfstatus – Etappe 2

Stand: **0.2.0-etappe2, 30.09.2026**. Die folgende Übersicht trennt ausgeführte Codeprüfungen, simulierte Zustände und noch offene Tests auf den Zielumgebungen.

## Technische Basis

Die Anwenderin hat `notebooks/00_setup_check.ipynb` lokal über JupyterLab und in GitHub Codespaces erfolgreich ausgeführt (`SETUP OK`). Das bestätigt die bereits ausgelieferte Umgebung. Die neuen Demos und Aufgaben waren dabei noch nicht enthalten.

`environment.yml`, `requirements.txt`, beide Compose-Dateien, `devcontainer.json`, `post-create.sh`, die Setup-Prüflogik und das Setup-Notebook sind gegenüber Etappe 1 unverändert. Dies wurde durch Vergleich der SHA-256-Prüfsummen kontrolliert. Die API-Beispiele verwenden bereits vorhandene Pakete; `.env.example` erhält lediglich optionale leere Schlüsselvariablen. Eine neue Installation oder ein Rebuild ist für Etappe 2 nicht erforderlich.

## Neue Materialien: ausgeführte Prüfungen

| Prüfung | Ergebnis und Aussagekraft |
|---|---|
| Demo 01: EZB-Sample | Alle Codezellen in einem frischen Python-Prozess ausgeführt; vier Kurse und 100 EUR → 96 CHF; Rohdaten, CSV und Metadaten geprüft |
| Demo 02: CoinGecko-/Flickr-Samples | Alle Codezellen in einem frischen Python-Prozess ausgeführt; vier Coin-Währungs-Zeilen und drei Fotometadatensätze; Exporte geprüft |
| Demo 03: HTML-Sample | Vollständiger Ablauf in einem frischen Python-Prozess mit echtem lokalem HTTP; zwei Seiten, sechs Beobachtungen und fünf Produkt-URLs; CSV zurückgelesen und verglichen |
| Task 01: Musterlösung | Vollständiger Ablauf in einem frischen Python-Prozess mit echtem lokalem HTTP; sechs Beobachtungen, fünf eindeutige Bücher und zwei ausgewählte Bücher; CSVs zurückgelesen |
| Task 01: Fehlerfälle | Fehlende Produktcontainer, Preis 0, unbekannte Ratingklasse und unbekannte Verfügbarkeit werden abgewiesen |
| Dynamische HTML-Datei | Eigenes JavaScript in einer jsdom-DOM-Simulation ausgeführt: 0 → 3 → 6 Zeilen, Button-Zustände, vier verfügbare und drei ausgewählte Produkte geprüft. **Kein echter Browserlauf.** |
| Demo 04 und Task 02: Auswertung | Parsing, Datenprüfung, Filter und CSV-Exporte mit dem durch die DOM-Simulation erzeugten HTML geprüft. Browsersteuerung und Screenshot dabei nicht erfolgreich ausgeführt; kein vollständiger Notebooknachweis |
| Gezielte automatisierte Tests | 23 erfolgreich: sieben bestehende Setup-Tests, elf API-/XML-Tests und fünf Datenqualitätsprüfungen der dynamischen Musterlösung |
| Notebooks | Schema, Python-Syntax, Kernel-Metadaten, relative Links und leere Ausgaben geprüft |
| Paket | Pflichtdateien, interne Links, Git-Ausschlüsse und unveränderte Umgebung geprüft; keine echten API-Schlüssel oder erzeugten Testausgaben enthalten |

Die Arbeitsnotebooks `task.ipynb` enthalten absichtlich offene Bearbeitungsstellen mit `NotImplementedError`. Ein unverändertes Arbeitsnotebook ist keine vollständige Lösung. Die voll ausgearbeiteten Lösungen liegen direkt im jeweiligen Task-Ordner und werden durch `.gitignore` von Git ausgeschlossen.

Die fünf Tests der dynamischen Musterlösung liegen ebenfalls im ausgeschlossenen Dozierendenbereich (`instructor/tests/`), da sie auf das Lösungsnotebook zugreifen. Die öffentlichen Tests unter `tests/` benötigen keine Lösungsdateien.

## Grenzen der Erstellungsumgebung

Ein echter Jupyter-Kernel konnte hier wegen eingeschränkter Socket-Berechtigungen (`Operation not permitted`) nicht starten. Die erfolgreichen Python-Prüfungen oben führen Codezellen in ihrer Reihenfolge in frischen gewöhnlichen Python-Prozessen aus. Das ist keine Bestätigung der Notebook-Oberfläche oder Kernel-Auswahl in JupyterLab/VS Code.

Für die neuen Browsermaterialien wurde ein separater Prüfbrowser ausserhalb des Workshop-Repos bereitgestellt. Der Remote-WebDriver-Dienst war erreichbar; der Browserstart scheiterte jedoch ebenfalls an einer Socket-Berechtigung der Erstellungsumgebung. Deshalb werden weder die neuen Selenium-Interaktionen noch ein Browser-Screenshot als erfolgreich getestet ausgewiesen. Die DOM-Simulation und die Parserprüfungen ersetzen diese Prüfung nicht. Am Workshop-Environment wurden dafür keine Pakete oder Einstellungen geändert.

## Externe Quellen

| Quelle | Status |
|---|---|
| EZB XML live | Ein begrenzter Python-Abruf versucht; kontrollierter Netzwerkfehler, kein erfolgreicher Live-Export |
| Books to Scrape live | Ein begrenzter Live-Lauf versucht; bereits die erste Anfrage scheiterte beim Verbindungs-/TLS-Aufbau mit Timeout. Keine Live-Seite erfolgreich geladen |
| CoinGecko live | Ohne eigenen Demo-Key nicht ausgeführt |
| Flickr live | Ohne eigenen API-Key nicht ausgeführt |
| Offizielle Dokumentation | Endpunkte und wesentliche Parameter im Browser-Recherchewerkzeug anhand offizieller Quellen geprüft; das ist kein erfolgreicher Python-Live-Abruf |

Live-Fehler führen nicht automatisch zu Beispieldaten. Die Standardmodi bleiben ausdrücklich synthetisch und benötigen keine API-Schlüssel. Erfolgreiche Sample-Tests belegen keinen funktionierenden persönlichen Anbieterzugang.

## Nächster Prüfpunkt

Führe die vier Demos lokal und danach in Codespaces mit einem frischen Notebook-Kernel aus. Prüfe besonders Demo 04 und die Musterlösung von Task 02 vollständig inklusive Browserinteraktion. Die [Testanleitung](TESTANLEITUNG_ETAPPE2.md) enthält erwartete Ergebnisse und ein kurzes Rückmeldeschema. Eine Wiederholung des bereits erfolgreichen Setup-Tests ist nur bei technischen Problemen nötig.

Ein separater lokaler VS-Code-Lauf und weitere Betriebssysteme sind weiterhin nicht bestätigt. Nutze für die fachliche Durchsicht zunächst die bereits bei Dir funktionierende JupyterLab-Umgebung.

[↑ Start](../README.md) · [Testanleitung](TESTANLEITUNG_ETAPPE2.md)
