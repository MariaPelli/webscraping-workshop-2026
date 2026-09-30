[Start](../README.md) · [Vorbereitung](../docs/TECHNISCHE_VORBEREITUNG.md) · [Demos](../demos/README.md) · [Datenbasis](../data/README.md)

# Aufgaben

Die zwei Aufgaben verwenden mitgelieferte **synthetische Katalogdaten** und benötigen keine API-Schlüssel. Öffne jeweils zuerst das README und danach `task.ipynb` mit dem Kernel **Python (webscraping-workshop)**.

| Aufgabe | Voraussetzung | Ergebnis |
|---|---|---|
| [01 – Statischer Katalog](01_statischer_katalog/README.md) | HTML-Demo; Python-Umgebung | Felder extrahieren, mehrere Seiten erfassen, Datenqualität und Vollständigkeit prüfen sowie Ergebnisse exportieren |
| [02 – Dynamischer Katalog](02_dynamischer_katalog/README.md) | Selenium-Demo; laufender Browser-Dienst | Ausgangs-HTML mit DOM vergleichen, auf Inhalte warten, alle sechs Produkte laden und die Methodenwahl begründen |

Die Demos zeigen die Werkzeuge. In den Aufgaben entscheidest Du selbst über passende Selektoren, Prüfkriterien und den Ablauf. Halte auch Deine Antworten auf die Reflexions- und Transferfragen im Notebook fest.

Beginne mit einem frischen Kernel. Führe die Vorbereitungszellen aus und ergänze die markierten Arbeitsstellen. Das Aufgaben-Notebook ist ein Gerüst: Ohne Deine Bearbeitung soll es noch keine vollständige Lösung erzeugen. Prüfe nach der Bearbeitung durch einen vollständigen Neustart und erneutes Ausführen, ob Deine Lösung ohne versteckten Zustand funktioniert.

Für Task 02 reicht ein erfolgreicher Python-Teiltest nicht. Der vollständige [Einrichtungstest](../notebooks/00_setup_check.ipynb) muss inklusive Browser `SETUP OK` ergeben. Die Aufgaben laufen nacheinander; der Selenium-Dienst ist für eine gleichzeitige Browser-Sitzung eingerichtet.

---

[Start](../README.md) · [Demos](../demos/README.md) · [Testanleitung](../docs/TESTANLEITUNG_ETAPPE2.md) · [Datenbasis](../data/README.md)
