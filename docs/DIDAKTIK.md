[Start](../README.md) · [Demos](../demos/README.md) · [Tasks](../tasks/README.md) · [Datenbasis](../data/README.md)

# Lernziele und Aufbau

Webscraping ist in diesem Themenblock Teil der Datenaufnahme im Data-Engineering-Lifecycle. Entscheidend ist, einen geeigneten Zugriffsweg auszuwählen und einen nachvollziehbaren, prüfbaren Datenbestand zu erzeugen.

Nach dem Themenblock kannst Du:

- strukturierte Downloads, REST-APIs und HTML als unterschiedliche Zugriffswege unterscheiden;
- HTTP-Antworten und deren Inhalte prüfen, bevor Du Daten extrahierst;
- HTML-Selektoren, relative Links und Pagination für einen kleinen Katalog einsetzen;
- geliefertes HTML und einen durch JavaScript veränderten DOM unterscheiden;
- auf Browserzustände warten und dynamisch hinzugefügte Einträge erfassen;
- Ergebnisse auf eindeutige IDs, Pflichtfelder und Vollständigkeit prüfen;
- Rohdaten, Tabellen und Herkunftsangaben nachvollziehbar ablegen;
- den gewählten Abrufweg sowie dessen Grenzen begründen.

## Von der Datenquelle zum Export

| Baustein | Methodischer Schwerpunkt | Anwendung |
|---|---|---|
| ECB | XML als strukturierter Download; Datenformat und Referenzdatum | Werte aus einer definierten Struktur in eine Tabelle überführen |
| CoinGecko und Flickr | API-Endpunkte, Parameter, JSON und Zugangsbedingungen | Anbieterabhängige Antwortstrukturen und Fehler behandeln |
| BeautifulSoup | Wiederkehrende HTML-Strukturen und Seitenverknüpfungen | Task 1: vollständigen statischen Katalog erfassen |
| Selenium | Browserzustand, JavaScript und explizites Warten | Task 2: dynamisch erscheinende Produkte und weiteren Ladezustand erfassen |

Die Beispiele beginnen reproduzierbar mit synthetischen Daten. Erst danach können Live-Abrufe zeigen, welche zusätzlichen Unsicherheiten in der Praxis entstehen: geänderte Strukturen, Abrufgrenzen, Antwortfehler oder nicht verfügbare Quellen. Beispieldaten und Live-Daten bleiben in Ablage und Metadaten unterscheidbar.

## BeautifulSoup und Selenium richtig vergleichen

BeautifulSoup ist ein Parser: Es wertet das HTML aus, das Du ihm übergibst. Es lädt keine Seite wie ein Browser und führt kein JavaScript aus. Selenium steuert einen Browser. Dieser kann JavaScript ausführen, auf Interaktionen reagieren und den DOM verändern. Du kannst die Daten danach mit Selenium abfragen oder den aktuellen HTML-Zustand erneut mit BeautifulSoup analysieren.

Für den Vergleich verwenden Demo 04 und Task 02 dieselbe synthetische Datei `data/teaching/dynamic_products.html`:

1. `requests` ruft die Datei über einen temporären lokalen HTTP-Server ab.
2. BeautifulSoup untersucht die Produktzeilen im gelieferten HTML. Die Tabellenzeilen werden erst später durch JavaScript erzeugt; die Produktwerte können dennoch bereits im Skript der Quelldatei stehen.
3. Selenium öffnet **denselben HTML-Inhalt** als `data:`-URL. Nach dem Ausführen des JavaScripts erscheinen zunächst drei Produkte.
4. Ein Klick auf „Weitere Produkte laden“ ergänzt drei weitere Produkte. Das Ziel sind sechs eindeutige Produkte.
5. Explizites Warten prüft die erwartete Änderung. Die anschliessende Auswertung kontrolliert Inhalte und Vollständigkeit.

Die `data:`-URL ist eine technische Vereinfachung für die gemeinsame lokale/Codespaces-Umgebung. Sie verhindert, dass der separate Browser-Container den HTTP-Server im Python-Prozess erreichen muss. Das Beispiel lädt keine Produkte von einem echten entfernten Dienst nach; es modelliert die Änderung des DOM nach JavaScript-Ausführung und Interaktion.

## Wann brauchst Du einen Browser?

| Beobachtung | Was Du zuerst prüfst |
|---|---|
| Die Daten stehen bereits im Antwort-HTML | `requests` und BeautifulSoup können genügen. |
| Ein dokumentierter Download oder geeigneter API-Endpunkt liefert die Daten | Strukturierter Abruf kann direkter und stabiler sein. |
| Der Selektor liefert keine Elemente | HTTP-Status, tatsächlichen Antwortinhalt und Selektor prüfen. |
| Eine Website liefert eine Fehler-, Login- oder Blockseite | Ursache und erlaubten Zugriffsweg klären; Browserautomatisierung ist kein allgemeiner Ausweg. |
| Inhalte entstehen erst nach JavaScript oder Interaktion | Prüfen, ob eine passende API verfügbar ist; andernfalls Browserautomatisierung erwägen. |
| Die erste Ansicht zeigt nur einen Teil | Pagination, „Mehr laden“, Scrollen und Vollständigkeitskriterium untersuchen. |

Die Methodenwahl folgt aus der beobachteten Datenquelle. Die pauschale Aussage „kein Treffer mit BeautifulSoup, also braucht es Selenium“ ist nicht ausreichend.

## Herkunft, Zugriff und Wiederholbarkeit

Halte Quelle, Abrufzeitpunkt, Modus (`sample` oder `live`) und wichtige Abrufparameter fest. API-Schlüssel gehören weder in Ausgaben noch in Metadaten. Bewahre Rohdaten zusammen mit der daraus erzeugten Tabelle auf, soweit die Bedingungen der Quelle dies erlauben.

Vor echten Abrufen prüfst Du den erlaubten Verwendungszweck, Nutzungsbedingungen und bei Bildern die konkrete Lizenz. [`robots.txt`](https://www.rfc-editor.org/rfc/rfc9309.html) gibt Crawler-Regeln an; sie ersetzt keine Erlaubnis zur Nutzung. Begrenze Abrufe, respektiere Rate-Limits und überwinde keine Zugangsschranken. Die Flickr-Demo verarbeitet zunächst Metadaten und lädt keine Bilddateien herunter.

## Bezug zu den Vorjahresmaterialien

| Vorjahresbeispiel | Umsetzung in diesem Paket |
|---|---|
| ECB | Eigene Demo für den strukturierten XML-Download mit synthetischem Standarddatensatz und optionalem Live-Abruf |
| CoinGecko | In der API-Demo, mit eindeutigen Coin-IDs und eigenem optionalen Demo-Key |
| Flickr | In der API-Demo als öffentliche Metadatensuche; eigener optionaler API-Key, kein Download von Bildern |
| Books to Scrape | HTML-Demo mit synthetischer Nachbildung und begrenztem optionalem Live-Abruf |
| Yahoo Finance: HTML/JavaScript-Vergleich | Durch den kontrollierten Vergleich am identischen synthetischen HTML ersetzt; daraus wird keine Aussage über den aktuellen Aufbau von Yahoo Finance abgeleitet |
| IKEA/Browser-Erweiterung und E-Mail-Extraktion | Nicht Bestandteil des vereinbarten Kurskerns |

Die neuen Aufgaben verwenden eigene kleine Katalogfälle und übertragen die gezeigten Verfahren auf selbstständig zu bearbeitende Schritte.

---

[Start](../README.md) · [Demos](../demos/README.md) · [Tasks](../tasks/README.md) · [Datenbasis](../data/README.md)
