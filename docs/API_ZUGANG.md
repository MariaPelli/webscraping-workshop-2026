[Start](../README.md) · [API-Demo](../demos/02_rest_apis_coingecko_flickr.ipynb) · [Datenbasis](../data/README.md) · [Update](UPDATE_ETAPPE2.md)

# API-Zugänge und optionale Live-Abrufe

**Für den Standarddurchlauf brauchst Du keine Schlüssel.** Die Notebooks verwenden deutlich gekennzeichnete synthetische Daten. Pro Anbieter gibt es einen eigenen Live-Schalter, der standardmässig auf `False` steht. Aktiviere nur den gewünschten Anbieter. Ein Live-Fehler wird nicht automatisch durch Sample-Daten ersetzt.

| Quelle | Standard | Für den optionalen Live-Modus |
|---|---|---|
| ECB | Synthetische XML-Datei | Kein API-Schlüssel |
| CoinGecko | Synthetische JSON-Datei | Eigener CoinGecko-Demo-API-Key |
| Flickr | Synthetische JSON-Datei mit Fotometadaten | Eigener Flickr-API-Key |
| Books to Scrape | Synthetische HTML-Seiten | Kein API-Schlüssel; begrenzter Abruf von höchstens zwei Seiten |
| Dynamischer Produktkatalog | Mitgelieferte synthetische HTML-Datei | Kein externer Live-Modus und kein Schlüssel |

Die Schalter heissen `EZB_LIVE`, `COINGECKO_LIVE` und `FLICKR_LIVE` in den jeweiligen Notebooks. In der HTML-Demo sowie Task 01 heisst der optionale Schalter `LIVE`. Jeder dieser Werte bleibt beim ersten Test auf `False`.

## Schlüssel in der bestehenden .env ergänzen

Behalte Deine bisherige `.env` inklusive `SELENIUM_PORT`. Ergänze diese Zeilen einmalig, falls sie noch fehlen:

```dotenv
COINGECKO_DEMO_API_KEY=
FLICKR_API_KEY=
```

Trage Deinen jeweiligen Schlüssel rechts vom Gleichheitszeichen ein. Leere Werte sind im Sample-Modus korrekt. Die Vorlage `.env.example` bleibt ohne echte Schlüssel.

Die Notebooks laden `.env` mit `override=False`: Eine bereits gesetzte Umgebungsvariable hat Vorrang. Falls ein geänderter Schlüssel noch nicht verwendet wird, starte den Notebook-Kernel neu und kontrolliere mögliche übergeordnete Umgebungsvariablen, ohne deren Werte auszugeben. Verwende keine Zelle, die die gesamte `.env`, einen Schlüssel oder ein vollständiges Request-Objekt anzeigt.

In Codespaces kannst Du die lokale, nicht versionierte `.env` im Repo bearbeiten. Sie wird nicht durch `git push` von Deinem Rechner übertragen. Schlüssel sind nur für Deinen Codespace bzw. Deine lokale Umgebung erforderlich, in der Du den jeweiligen Live-Abruf tatsächlich ausführen möchtest.

## CoinGecko Demo API

1. Öffne die [offizielle Anleitung zur Demo-Authentifizierung](https://docs.coingecko.com/demo/reference/authentication).
2. Melde Dich bei CoinGecko an und erstelle bzw. kopiere im Developer Dashboard einen **Demo-API-Key**.
3. Hinterlege ihn unter `COINGECKO_DEMO_API_KEY` in Deiner `.env`.
4. Aktiviere im API-Notebook nur den CoinGecko-Live-Schalter und führe die betreffenden Zellen erneut aus.

Das Beispiel verwendet den Demo-Endpunkt unter `https://api.coingecko.com/api/v3/` und übergibt den Schlüssel im Header `x-cg-demo-api-key`. Ein Pro-Key gehört zu einem anderen Zugang und ist kein austauschbarer Demo-Key. Verwende eindeutige Coin-IDs statt mehrdeutiger Kürzel.

Kontingente und Rate-Limits richten sich nach dem gewählten Zugang. Prüfe sie im Anbieter-Dashboard; die Unterlagen versprechen keine bestimmte Anzahl kostenloser Abrufe und richten kein kostenpflichtiges Angebot ein.

## Flickr

1. Öffne [Flickr: API Keys](https://www.flickr.com/services/api/misc.api_keys.html) und folge dem dortigen Antrag für einen eigenen Anwendungsschlüssel.
2. Beschreibe Deinen tatsächlichen Verwendungszweck. Die passende Zugangskategorie richtet sich nach den Anbieterbedingungen.
3. Hinterlege den API-Key unter `FLICKR_API_KEY` in Deiner `.env`.
4. Aktiviere im API-Notebook nur den Flickr-Live-Schalter.

Die Demo verwendet [`flickr.photos.search`](https://www.flickr.com/services/api/flickr.photos.search.html) für öffentliche Fotos. Dafür ist ein Anwendungsschlüssel nötig, jedoch keine Anmeldung für private Fotos und kein Flickr-Secret. Es wird höchstens eine Seite mit fünf Metadatensätzen angefordert. Standardmässig werden **keine Bilddateien heruntergeladen**.

Öffentliche Sichtbarkeit bedeutet nicht automatisch, dass ein Bild frei weiterverwendet werden darf. Prüfe vor einer tatsächlichen Bildnutzung die konkrete Lizenz und deren Bedingungen.

## Bei Fehlern

| Beobachtung | Prüfung |
|---|---|
| Fehlender Schlüssel | `.env`-Eintrag und richtigen Live-Schalter prüfen; alternativ bewusst zum Sample-Modus zurückkehren. |
| Abgelehnter API-Zugang | Schlüsseltyp, Anbieter-Dashboard und erlaubten Endpunkt prüfen. |
| Rate-Limit erreicht | Weitere Abrufe stoppen und die Vorgaben des Anbieters beachten. |
| HTTP-Erfolg, aber API-Fehlermeldung | API-Status im Antwortkörper auswerten; besonders Flickr kann eine Fehlermeldung als JSON zurückgeben. |
| Leere oder unerwartete Antwort | Parameter und erwartete Felder prüfen; keine leere Tabelle als Erfolg behandeln. |

Die Notebooks verwenden HTTP-Timeouts und geben bei Schlüsselzugängen keine vollständigen Request-URLs oder Header aus. Teile bei Rückfragen nur bereinigte Fehlertexte. Insbesondere bei Flickr kann eine vollständige URL den Schlüssel enthalten.

Live-Abrufe speichern Daten und Herkunftsangaben in eigenen `live`-Ausgabeordnern. API-Schlüssel werden nicht als Herkunftsmetadaten gespeichert. Auch synthetische Ausgaben bleiben ausdrücklich als `sample` gekennzeichnet.

## Offizielle Quellen

Geprüfter Dokumentationsstand: **30.09.2026**. Die Einrichtung eines eigenen Kontos und erfolgreiche Live-Abrufe mit Deinem Schlüssel sind damit nicht bestätigt.

- [CoinGecko: Demo-Authentifizierung](https://docs.coingecko.com/demo/reference/authentication)
- [Flickr: API Keys](https://www.flickr.com/services/api/misc.api_keys.html)
- [Flickr: öffentliche Fotosuche](https://www.flickr.com/services/api/flickr.photos.search.html)
- [ECB: Euro-Referenzkurse und Datenzugänge](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)

---

[Start](../README.md) · [Demos](../demos/README.md) · [Testanleitung](TESTANLEITUNG_ETAPPE2.md)
