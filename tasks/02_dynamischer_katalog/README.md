[Start](../../README.md) · [Aufgaben](../README.md) · [Demo 4](../../demos/04_dynamische_seiten_selenium.ipynb)

# Task 2 – Dynamischer Produktkatalog

Eine Beschaffungsstelle benötigt eine vollständige Liste verfügbarer Produkte bis einschliesslich **30 CHF**. Der Katalog zeigt zuerst nur einen Teil der Produkte. Weitere Einträge erscheinen nach einem Klick. Die sechs mitgelieferten Produkte sind synthetisch.

## Dein Auftrag

1. Öffne [task.ipynb](task.ipynb) mit **Python (webscraping-workshop)**. Lokal muss der Selenium-Container laufen; in Codespaces startet der vorhandene Nebendienst automatisch.
2. Untersuche die HTTP-Antwort: Welche Inhalte stehen schon im HTML, welche entstehen erst im DOM?
3. Ergänze die Extraktion von ID, Name, Kategorie, Preis und Verfügbarkeit. Prüfe fehlende Felder, Datentypen und eindeutige IDs.
4. Steuere den Browser mit expliziten Wartebedingungen. Lade den gesamten Katalog nach und berücksichtige ein Klicklimit.
5. Filtere verfügbare Produkte bis einschliesslich 30 CHF. Sortiere nach Preis und ID. Ermittle Anzahl und Preissumme je Kategorie.
6. Speichere den vollständigen Katalog, die Auswahl und Herkunftsmetadaten. Lies die CSVs zurück und vergleiche sie mit Deinen Ergebnissen.
7. Beantworte die Transferfragen zur Methodenwahl und Fehlerdiagnose.

## Erwartetes Ergebnis mit den Lehrdaten

| Prüfung | Erwartung |
|---|---|
| Tabellenzeilen im Ausgangs-HTML | 0 |
| Nach dem ersten Rendern | 3 |
| Vollständiger Katalog | 6 eindeutige Produkte |
| Verfügbare Produkte | 4 |
| Verfügbar und höchstens 30 CHF | 3; IDs P101, P103 und P105 |
| Preissumme der Auswahl | 63.90 CHF |

Deine Ausgaben liegen unter `data/output/task02_dynamic_sample/`: `all_products.csv`, `available_products.csv` und `provenance.json`. Die Metadaten enthalten Quelle, synthetischen Modus, UTC-Abrufzeit, Währung, Zeilenzahlen, Klickanzahl und Filter.

**Bearbeitungshinweis:** Vier TODO-Stellen enthalten absichtlich `NotImplementedError`. Ein unverändertes Ausführen aller Zellen ist noch keine fertige Lösung. Der Browserlauf darf bei fehlender Verbindung nicht als erfolgreich übersprungen werden.

## Qualitätskriterien

Das Ergebnis ist erst vollständig, wenn die gesamte angekündigte Produktzahl erfasst wurde. Verwende einen booleschen Verfügbarkeitswert (`"false"` ist kein boolesches `False`), beende jede Browser-Sitzung und begründe Deine Methodenwahl. Ein Screenshot allein ersetzt diese Prüfungen nicht.

[↑ Aufgaben](../README.md) · [Demos](../../demos/README.md)
