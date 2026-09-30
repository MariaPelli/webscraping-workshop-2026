[Start](../README.md) · [Vorbereitung](../docs/TECHNISCHE_VORBEREITUNG.md) · [Aufgaben](../tasks/README.md) · [API-Zugang](../docs/API_ZUGANG.md)

# Demos

Öffne die Notebooks mit **Python (webscraping-workshop)**. Jedes Notebook ist eigenständig ausführbar und beginnt im **Sample-Modus mit synthetischen Daten**. Du brauchst keine Ergebnisse eines vorherigen Notebooks und keine API-Schlüssel für diesen Modus.

| Notebook | Was Du nachvollziehst | Optionaler Live-Zugang |
|---|---|---|
| [01 – Strukturierte Daten: ECB](01_strukturierte_daten_ezb.ipynb) | XML laden, Währungskurse auslesen und mit Herkunftsangaben speichern | Öffentlicher ECB-XML-Abruf ohne API-Schlüssel |
| [02 – REST-APIs: CoinGecko und Flickr](02_rest_apis_coingecko_flickr.ipynb) | JSON-Strukturen, Endpunkte, Parameter, Fehlerfälle und getrennte Exportdaten | Eigener CoinGecko-Demo-Key bzw. Flickr-API-Key |
| [03 – HTML mit BeautifulSoup](03_html_beautifulsoup.ipynb) | Elemente selektieren, Werte bereinigen und Pagination berücksichtigen | Begrenzter Abruf von Books to Scrape |
| [04 – Dynamische Seiten mit Selenium](04_dynamische_seiten_selenium.ipynb) | Dasselbe HTML mit `requests` und im Browser vergleichen, auf Daten warten und weitere Einträge laden | Kein Live-Abruf; laufender Selenium-Dienst erforderlich |

Wenn Deine Umgebung aus Etappe 1 bereits vollständig geprüft ist, kannst Du direkt beginnen. Bei einer neuen oder ungeprüften Umgebung führst Du zuerst den [Einrichtungstest](../notebooks/00_setup_check.ipynb) aus. Für Demo 04 muss auch die Browserprüfung erfolgreich sein; `TEILTEST OK` reicht nicht.

## Worauf Du beim Vergleich achtest

- `requests` liefert die HTTP-Antwort. BeautifulSoup analysiert das übergebene HTML und führt dessen JavaScript nicht aus.
- In Demo 04 enthält das Ausgangs-HTML noch keine gerenderten Produktzeilen. Der Browser erzeugt zunächst drei und nach einem Klick insgesamt sechs Zeilen.
- Beide Methoden erhalten in diesem Vergleich **den gleichen HTML-Inhalt**. Der Browser bekommt ihn als `data:`-URL, damit der Selenium-Container weder lokal noch in Codespaces auf den temporären Python-HTTP-Server zugreifen muss.
- Nach dem Rendern kann BeautifulSoup auch `browser.page_source` auswerten. Browserautomatisierung und HTML-Parsing können sich ergänzen.

Eine andere Website kann Daten bereits im gelieferten HTML enthalten oder über einen geeigneten JSON-Endpunkt bereitstellen. Prüfe ausserdem HTTP-Status, Selektor und Antwortinhalt, bevor Du aus einem leeren Ergebnis auf JavaScript schliesst.

## Live-Modus bewusst einschalten

Lass die Live-Schalter für den ersten Durchlauf ausgeschaltet. Aktiviere später nur den Anbieter, den Du testen möchtest. Die [API-Anleitung](../docs/API_ZUGANG.md) beschreibt die nötigen Schlüssel. Ein fehlgeschlagener Live-Aufruf stoppt mit einer Erklärung; Du entscheidest selbst, ob Du den Fehler behebst oder den Sample-Modus erneut wählst.

Ausgaben liegen unter `data/output/` mit getrennten Sample-/Live-Pfaden. Die [Datenbeschreibung](../data/README.md) erläutert Herkunft und Ablage.

---

[Start](../README.md) · [Aufgaben](../tasks/README.md) · [Testanleitung](../docs/TESTANLEITUNG_ETAPPE2.md) · [Datenbasis](../data/README.md)
