[Start](../README.md) · [Update](UPDATE_ETAPPE2.md) · [Demos](../demos/README.md) · [Tasks](../tasks/README.md) · [Prüfprotokoll](VALIDIERUNG_ETAPPE2.md)

# Etappe 2 testen

Prüfe zuerst die neuen Materialien lokal und danach im bestehenden Codespace. Die bereits geprüfte Umgebung bleibt unverändert. Die folgenden Erwartungen beziehen sich auf den **Sample-Modus**; alle Live-Schalter bleiben zunächst `False` und die API-Schlüssel dürfen leer sein.

## 1. Vorhandene Umgebung verwenden

Die technische Basis wurde bereits lokal und in Codespaces erfolgreich geprüft. **Eine erneute Setup-Prüfung gehört nicht zum Kontrolllauf für dieses Update.** Aktiviere die vorhandene Umgebung. Lokal muss Docker laufen; starte den vorhandenen Dienst bei Bedarf mit `docker compose up -d`. Im Codespace verwendet das Notebook den bereits konfigurierten Selenium-Nebendienst.

Starte einen frischen Notebook-Kernel und beginne mit den neuen Demos. Führe Browser-Notebooks nacheinander aus, da der Dienst eine Sitzung gleichzeitig vorsieht.

Nur falls ein technischer Fehler auftritt oder die Umgebung noch nicht geprüft wurde, kannst Du zur Diagnose optional im Repo-Hauptordner ausführen:

```bash
python scripts/verify_setup.py
```

In diesem optionalen Diagnoselauf wird **`SETUP OK`** inklusive Browser erwartet. `TEILTEST OK` bestätigt den Browser nicht. Weitere Hinweise stehen in der [Fehlerhilfe](TROUBLESHOOTING.md).

## 2. Vier Demos ausführen

Wähle in jedem Notebook **Python (webscraping-workshop)**, starte einen frischen Kernel und führe alle Zellen von oben nach unten aus.

| Notebook | Erwartung im Sample-Modus |
|---|---|
| `01_strukturierte_daten_ezb.ipynb` | Vier Währungen CHF, USD, GBP und JPY; Beispieldatum 01.09.2026; 100 EUR ergeben im synthetischen Beispiel 96 CHF. XML, Tabelle und Metadaten werden gespeichert. |
| `02_rest_apis_coingecko_flickr.ipynb` | CoinGecko: vier Zeilen für zwei Coin-IDs und zwei Währungen. Flickr: drei Fotometadatensätze. Keine API-Schlüssel nötig, keine Bilddownloads. |
| `03_html_beautifulsoup.ipynb` | Zwei synthetische Buchseiten werden gelesen; sechs Beobachtungen ergeben fünf eindeutige Bücher. HTML-Rohdaten, Tabelle und Metadaten werden gespeichert. |
| `04_dynamische_seiten_selenium.ipynb` | Ausgangs-HTML hat keine gerenderten Produktzeilen. Browser zeigt zunächst drei, nach Klick sechs Produkte. Tabelle, Browser-Screenshot und Herkunftsangaben werden gespeichert. |

Die genauen Ausgabeordner stehen in der [Datenbeschreibung](../data/README.md). Öffne mindestens eine CSV-Datei und eine Metadatendatei. Die Inhalte müssen zum Sample-Modus passen und als synthetisch erkennbar sein. Eine alte Ausgabedatei allein beweist keinen erfolgreichen neuen Lauf; beachte den aktuellen Notebooklauf und die gespeicherten Zeitangaben.

## 3. Aufgaben und Musterlösungen prüfen

Die `task.ipynb`-Dateien sind absichtlich unvollständige Arbeitsgerüste. Offene Arbeitsstellen und ein entsprechend erklärter `NotImplementedError` sind kein Einrichtungsfehler. Prüfe, ob Aufgabenstellung, Eingaben und erwartete Ergebnisse verständlich sind.

Wenn Dir das Dozierendenpaket vorliegt, führe die jeweiligen `task_sample_solution.ipynb` in den Task-Ordnern mit frischem Kernel aus. Im Studierenden-Repo werden diese Dateien nicht veröffentlicht.

| Lösung | Erwartung |
|---|---|
| Task 01, statischer Katalog | Zwei Seiten; sechs Beobachtungen; fünf eindeutige Bücher; zwei Bücher erfüllen den Filter „verfügbar, Bewertung mindestens 4, Preis höchstens 25 GBP“. |
| Task 02, dynamischer Katalog | Sechs eindeutige Produkte nach dem Nachladen; vier sind verfügbar, drei erfüllen zusätzlich den Preisfilter bis 30 CHF, zusammen 63.90 CHF. |

Prüfe in Task 02 ausdrücklich, dass die Browser-Schritte ausgeführt werden. Ein ausgelassener oder abgefangener Browserfehler ist kein erfolgreicher Test der Aufgabe.

## 4. Rückmeldung festhalten

```text
Version: 0.2.1-etappe2
Umgebung: lokal / Codespaces
Technische Basis: bereits geprüft / neuer technischer Fehler
Demo 01 ECB: OK / Fehler
Demo 02 APIs im Sample-Modus: OK / Fehler
Demo 03 HTML: OK / Fehler
Demo 04 Selenium: OK / Fehler
Task 01 Aufgabenstellung verständlich: ja / Anmerkung
Task 01 Musterlösung, falls vorhanden: OK / Fehler / nicht geprüft
Task 02 Aufgabenstellung verständlich: ja / Anmerkung
Task 02 Musterlösung, falls vorhanden: OK / Fehler / nicht geprüft
Erste fehlschlagende Zelle oder inhaltliche Rückmeldung:
```

Bei einem Fehler gib Notebookname, erste fehlgeschlagene Zelle und bereinigte Fehlermeldung an. Bei technischen Problemen ergänze lokal das Betriebssystem. Teile keine API-Schlüssel oder vollständigen Flickr-Request-URLs.

## Optional: einen Live-Zugang testen

Erst nach einem erfolgreichen Sample-Durchlauf aktivierst Du gezielt einen Live-Schalter. Die [API-Anleitung](API_ZUGANG.md) beschreibt die Einrichtung. Live-Antworten dürfen andere Werte und Zeilenzahlen enthalten; die Beispielerwartungen oben gelten dafür nicht. Ein absichtlich aktivierter Live-Modus mit fehlendem Schlüssel muss klar fehlschlagen und darf keine vermeintlichen Live-Daten aus dem Sample ausgeben.

Ein erfolgreicher Sample-Lauf bestätigt weder einen persönlichen API-Zugang noch die aktuelle Erreichbarkeit externer Quellen. Das [Prüfprotokoll](VALIDIERUNG_ETAPPE2.md) unterscheidet die tatsächlich ausgeführten Prüfungen.

---

[Start](../README.md) · [Update](UPDATE_ETAPPE2.md) · [Datenbasis](../data/README.md) · [Hilfe](TROUBLESHOOTING.md)
