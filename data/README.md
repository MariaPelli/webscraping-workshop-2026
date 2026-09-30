[Start](../README.md) · [Demos](../demos/README.md) · [Tasks](../tasks/README.md) · [Testanleitung](../docs/TESTANLEITUNG_ETAPPE2.md)

# Datenbasis und Ausgaben

**Alle mitgelieferten Datensätze sind synthetisch.** Sie wurden für diese Übungen erstellt. Die Beispielkurse, Coin-Werte, Fotometadaten, Bücher und Produkte sind keine historischen oder aktuellen Anbieterabzüge.

## Daten für den Einrichtungstest

Der Ordner `fixtures/` bleibt unverändert aus Etappe 1:

| Datei | Inhalt |
|---|---|
| `fixtures/synthetic_records.json` | Drei erfundene Bücher mit IDs, Titeln und CHF-Preisen |
| `fixtures/static_catalog.html` | Dieselben drei Datensätze als HTML-Tabelle |
| `fixtures/dynamic_catalog.html` | Dieselben drei Datensätze, durch JavaScript erzeugt |

Der Einrichtungstest schreibt `output/setup_records.csv` und `output/setup_report.json`. Dieser dreiteilige Testdatensatz ist von den grösseren Kursbeispielen unten zu unterscheiden.

## Daten für die Kursmaterialien

| Datei | Inhalt und Verwendung |
|---|---|
| `samples/ezb_sample.xml` | XML nach dem Muster der ECB-Referenzkurse; vier erfundene Werte für CHF, USD, GBP und JPY mit Beispieldatum 01.09.2026 |
| `samples/coingecko_sample.json` | Synthetische Werte für Bitcoin und Ethereum in EUR und CHF; Hülle mit Kennzeichnung und `payload` |
| `samples/flickr_sample.json` | Drei erfundene Fotometadatensätze; Hülle mit Kennzeichnung und `payload`, keine Bilddateien |
| `teaching/books/page-1.html` und `page-2.html` | Zwei HTML-Seiten mit je drei Buchbeobachtungen; ein Buch erscheint auf beiden Seiten, sodass fünf eindeutige Bücher vorliegen |
| `teaching/dynamic_products.html` | Sechs Produkte; JavaScript zeigt zuerst drei, nach „Weitere Produkte laden“ alle sechs an |

Die Buchseiten orientieren sich für die Übung an wiederkehrenden Strukturen von Books to Scrape. Der dynamische Katalog vergleicht denselben HTML-Inhalt vor und nach der JavaScript-Ausführung. Er simuliert eine Interaktion im DOM, keinen echten API-Nachladevorgang.

## HTTP und Browser im Sample-Modus

Ein temporärer HTTP-Server liefert die statischen Dateien für `requests` auf einer freien lokalen Portnummer aus. Der Server wird nach der Verwendung geschlossen. Der Selenium-Browser erhält den dynamischen HTML-Inhalt als `data:`-URL. Dadurch braucht der Browser-Container keinen Zugriff auf den HTTP-Server des Python-Prozesses; lokal und in Codespaces bleiben die vorhandenen Portkonfigurationen ausreichend.

## Ausgabeordner

Die folgenden Pfade gelten relativ zu `data/output/`:

| Beispiel | Ausgabe |
|---|---|
| Demo 01 ECB | `demo01_ezb/sample/` oder `demo01_ezb/live/`: `raw.xml`, `rates.csv`, `metadata.json` |
| Demo 02 CoinGecko/Flickr | `demo02_apis/coingecko/sample/` bzw. `demo02_apis/flickr/sample/`: `raw.json`, `records.csv`, `metadata.json`; Live-Abrufe verwenden jeweils `live/` |
| Demo 03 HTML | `static_demo/sample/` oder `static_demo/live/`: `catalogue.csv`, `metadata.json` und die abgerufenen HTML-Seiten unter `raw/` |
| Demo 04 Selenium | `demo04_selenium_sample/`: `products.csv`, `browser.png`, `provenance.json` |
| Task 01 | `task_static/sample/` oder bei bewusst gewähltem Live-Modus `task_static/live/`: `observations.csv`, `all_books.csv`, `selected_books.csv`, `metadata.json` und HTML-Seiten unter `raw/` |
| Task 02 | `task02_dynamic_sample/`: `all_products.csv`, `available_products.csv`, `provenance.json` |

Ein neuer Lauf im gleichen Modus überschreibt gleichnamige Ausgaben. Die Metadaten dokumentieren Herkunft und Verarbeitung; API-Schlüssel werden nicht gespeichert. Die Ablage trennt Sample- und Live-Ergebnisse sichtbar. Ergebnisse aus Live-Abrufen können sich zwischen Ausführungen ändern.

Der Ausgabeordner ist bis auf `.gitkeep` in `.gitignore` ausgeschlossen. Das gilt auch für die lokale `.env`. Prüfe vor einer Veröffentlichung dennoch, dass keine früher bereits versionierten Ausgaben oder Schlüssel im Commit verbleiben.

---

[Start](../README.md) · [API-Zugang](../docs/API_ZUGANG.md) · [Testanleitung](../docs/TESTANLEITUNG_ETAPPE2.md)
