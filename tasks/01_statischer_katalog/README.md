# Task 1 · Einen statischen Katalog erschliessen

[← Alle Tasks](../README.md) · [Startseite](../../README.md) · [HTML-Demo](../../demos/03_html_beautifulsoup.ipynb)

## Auftrag

Du bereitest eine kleine Einkaufsliste aus einem mehrseitigen Bücherkatalog vor. Gesucht sind **verfügbare Bücher mit mindestens 4 Sternen und einem Preis von höchstens 25 GBP**. Erstelle dazu eine nachvollziehbare Ingestion mit Rohdaten, Qualitätsprüfungen und CSV-Ausgabe.

Beginne in [task.ipynb](task.ipynb). Das Notebook enthält vorbereitete Imports, Einstellungen und markierte Arbeitsstellen. Es ist absichtlich noch keine fertige Lösung: Ein unveränderter vollständiger Lauf stoppt an `NotImplementedError`.

## Datengrundlage und Umgebung

- Standard: `LIVE = False`, zwei mitgelieferte synthetische HTML-Seiten mit je drei Produktbeobachtungen. Titel, Preise und Bewertungen sind erfunden. Ein Buch erscheint auf beiden Seiten.
- Die Seiten werden über einen temporären lokalen HTTP-Server mit `requests` abgerufen. Du benötigst den Workshop-Kernel; Selenium/Docker wird für diesen Task nicht gebraucht.
- Die Produktlinks identifizieren Bücher. Im Sample liegen keine Detailseiten vor; rufe diese Links nicht ab.
- Optional: `LIVE = True` ruft höchstens zwei Seiten von [Books to Scrape](https://books.toscrape.com/) ab, mit einer Pause zwischen den Seiten. Das ergibt einen **Ausschnitt**, keinen vollständigen Live-Katalog. Die Seite ist für Scraping-Übungen vorgesehen; ihre Preise und Bewertungen haben keine reale Bedeutung.

## Arbeitsschritte

1. Prüfe am HTML, welche Selektoren Titel, Preis, Bewertung, Verfügbarkeit und nächste Seite erschliessen. Verwende das `title`-Attribut des Produktlinks für den vollständigen Buchtitel.
2. Rufe die erste und gegebenenfalls die zweite Seite mit Timeout und HTTP-Statusprüfung ab. Verwende `urljoin` für Produkt- und Folgeseitenlinks. Beende bei fehlendem Weiter-Link oder nach höchstens zwei Seiten; melde den Abbruchgrund.
3. Extrahiere pro Produkt `title`, `price_gbp`, `rating`, `in_stock`, `detail_url` und `source_page`. Die Bewertung steht in einer CSS-Klasse, nicht als sichtbare Zahl.
4. Prüfe nichtleere Titel/URLs, positive numerische Preise, Bewertungen von 1 bis 5 und bekannte Verfügbarkeitstexte. Fehlende Produktcontainer oder unbekannte Werte müssen auffallen. Ein leerer Parser-Erfolg ist hier kein gültiges Ergebnis.
5. Prüfe doppelte Detail-URLs. Entferne identische Wiederholungen nachvollziehbar. Bei widersprüchlichen Werten soll die Verarbeitung mit einer klaren Meldung stoppen.
6. Filtere nach dem Auftrag, sortiere aufsteigend nach Preis und exportiere alle eindeutigen Bücher sowie die Auswahl als CSV. Lies die Dateien zur Kontrolle wieder ein.
7. Speichere die abgerufenen HTML-Dateien und Metadaten mit Modus, Abrufzeitpunkt, Quellseiten, Seiten-/Datensatzanzahl, Duplikatanzahl und Abbruchgrund.

## Abgabe und Selbstkontrolle

Abgabe: Dein bearbeitetes Notebook, eine kurze Antwort auf die Reflexionsfragen und die erzeugten Dateien aus `data/output/task_static/sample/` bzw. `live/`. Wiederholte Läufe ersetzen die Dateien desselben Modus.

| Kriterium | Erwartung im synthetischen Modus |
|---|---|
| Abgerufene Seiten | 2 |
| Produktbeobachtungen vor Bereinigung | 6 |
| Eindeutige Bücher | 5 |
| Identische Wiederholungen | 1 |
| Bücher in der Auswahl | 2 |
| Filter | Preis ≤ 25 GBP, Bewertung ≥ 4, verfügbar |
| Abschluss | Keine weitere Seite im Sample; erfolgreiche Prüfung und CSV-Roundtrip |

Die genauen Titel der Auswahl leitest Du selbst her. Für Live-Daten gelten diese festen Anzahlen nicht. Auch ein erfolgreicher Abruf zweier Live-Seiten bestätigt keine Vollständigkeit des gesamten Katalogs.

## Reflexion

1. Warum genügen hier HTTP-Abruf und BeautifulSoup? Welche Beobachtung würde einen anderen Zugriffsweg rechtfertigen?
2. Wie unterscheidest Du „keine nächste Seite“ von „Selektor funktioniert nicht mehr“? Was würdest Du zusätzlich überwachen?
3. Warum ist `urljoin` robuster als das Zusammenkleben von Strings? Auf welche Basis-URL beziehst Du relative Links?
4. Warum verwendest Du die Detail-URL statt den Titel als Duplikatschlüssel? Welche Grenze hat auch dieser Schlüssel?
5. Was ist der Unterschied zwischen einem regulären Ende und Deinem Sicherheitslimit von zwei Seiten?
6. Würdest Du einen offiziell angebotenen CSV-Download oder eine API vorziehen? Begründe anhand Wartbarkeit, Inhalt und Nutzungsbedingungen.

[↑ Startseite](../../README.md)
