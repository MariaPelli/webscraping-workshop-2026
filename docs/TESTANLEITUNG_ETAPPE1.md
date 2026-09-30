[Start](../README.md) · [Vorbereitung](TECHNISCHE_VORBEREITUNG.md) · [Lokal](setup/LOKAL.md) · [Codespaces](setup/CODESPACES.md) · [Hilfe](TROUBLESHOOTING.md)

# Etappe 1 prüfen

Diese Anleitung dient zur Rückmeldung zum ersten Zwischenpaket. Prüfe zuerst Deinen lokalen Arbeitsweg. Wenn das Repo auf GitHub bereitsteht, prüfe zusätzlich einen Codespace. Was bei der Erstellung bereits geprüft wurde, steht im [Prüfprotokoll](VALIDIERUNG_ETAPPE1.md).

## 1. Einrichtung abschliessen

Folge der Anleitung [lokal](setup/LOKAL.md) oder [Codespaces](setup/CODESPACES.md). Öffne ein Terminal im Repo-Hauptordner und aktiviere die passende Python-Umgebung.

## 2. Vollständigen Terminaltest ausführen

```bash
python scripts/verify_setup.py
```

| Prüfung | Erwartetes Ergebnis |
|---|---|
| Python und Pakete | Python 3.12 und alle benötigten Imports erfolgreich |
| Projektpfade | Repo und synthetische Beispieldaten werden gefunden |
| HTTP und Parsing | JSON und HTML liefern jeweils die drei vorbereiteten Datensätze |
| CSV | Drei Datensätze werden gespeichert und wieder eingelesen |
| Browser | Echte Remote-Sitzung startet; drei mit JavaScript erzeugte Datensätze werden erkannt; Sitzung wird geschlossen |
| Gesamtresultat | **`SETUP OK`**, Prozess-Exitcode 0 |

Es entstehen `data/output/setup_report.json` und `data/output/setup_records.csv`. Die CSV enthält drei synthetische Bücher mit den IDs 1–3. Die Daten sind ausschliesslich für den Einrichtungstest erstellt; sie stammen von keiner externen Website.

Zum Aufbewahren getrennter Terminalberichte kannst Du den Berichtspfad selbst wählen:

```bash
python scripts/verify_setup.py --report data/output/setup_report_local.json
```

Im Codespace verwendest Du beispielsweise `--report data/output/setup_report_codespaces.json`. Bestehende Berichte am gewählten Pfad werden überschrieben.

## 3. Notebook unabhängig prüfen

Öffne `notebooks/00_setup_check.ipynb` in JupyterLab oder VS Code, wähle **Python (webscraping-workshop)**, starte den Kernel frisch und führe alle Zellen der Reihe nach aus. Der Terminaltest muss vorher beendet sein, da der Browser-Dienst eine Sitzung gleichzeitig vorsieht.

**Erwartet: alle Zellen laufen ohne Fehler durch und das Ergebnis lautet `SETUP OK`.** Das Notebook verwendet dieselbe Prüflogik wie das Terminal. Sein Standardbericht überschreibt `data/output/setup_report.json`.

## 4. Ergebnisse zurückmelden

Für die Vorbereitung genügt diese kurze Rückmeldung:

```text
Paket: Etappe1_v1, Dokumentationsstand 0.1.1-etappe1
Lokal: [Windows / macOS / Linux; Prozessorarchitektur]
Terminal: [SETUP OK / Fehler]
Lokale Oberfläche: [JupyterLab / VS Code]
Notebook mit Kernel Python (webscraping-workshop): [SETUP OK / Fehler]
Codespaces-Terminal: [SETUP OK / Fehler / noch nicht geprüft]
Codespaces-Notebook: [SETUP OK / Fehler / noch nicht geprüft]
Anmerkung oder erste Fehlermeldung:
```

Bei einem Fehler sende den Testbericht und die erste relevante Fehlermeldung mit. Fehlt der Bericht wegen eines frühen Startfehlers, genügt zunächst die Terminalausgabe. Nach erfolgreicher Prüfung kann die Ausarbeitung der Kursmaterialien auf dieser Basis beginnen.

## Optionale Zusatzprüfungen

### Python-Basis ohne Browser eingrenzen

```bash
python scripts/verify_setup.py --skip-browser
```

Bei Erfolg lautet das Ergebnis **`TEILTEST OK`**. Ein erfolgreicher Exitcode 0 bedeutet in diesem Modus nur, dass die ausgelassenen Browserprüfungen nicht bewertet wurden. Er bestätigt **keine funktionsfähige Selenium-Umgebung**. Zur Abnahme immer den vollständigen Test ohne diese Option durchführen.

### Live-Erreichbarkeit prüfen

```bash
python scripts/verify_setup.py --online
```

Diese Option ergänzt den Grundtest um externe Abrufe bei ECB und Books to Scrape. Der Test kann an einer Netzwerksperre oder einer vorübergehend nicht erreichbaren Website scheitern, auch wenn die technische Basis funktioniert. Die Ausgabe bewertet die Live-Prüfungen gesondert. Dieser Schritt ist für den isolierten Grundtest nicht erforderlich und noch kein vollständiger Test der späteren Kursaufgaben.

---

[Start](../README.md) · [Prüfprotokoll](VALIDIERUNG_ETAPPE1.md) · [Hilfe](TROUBLESHOOTING.md)
