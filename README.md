# Umschulung zum Fachinformatiker für Anwendungsentwicklung – Lernprojekte und Dokumentation

In diesem Repository dokumentiere ich meine Lernfortschritte während meiner Umschulung zum Fachinformatiker für Anwendungsentwicklung, die ich im Dezember 2025 begonnen habe. Der Schwerpunkt liegt auf Python, relationalen Datenbanken, Linux und praktischen Grundlagen moderner Softwareentwicklung. Neben strukturierten Lernunterlagen enthält das Repository eigene Programmierübungen und kleine Projekte.

## Navigation

| Bereich | Inhalte |
| --- | --- |
| [Python](./python/) | Programmiergrundlagen, Aufgaben zum Würfelspiel und mehrere Entwicklungsstände eigener Python-Spiele |
| [Datenbanken und SQL](./datenbanken-sql/) | Relationale Datenbanken, Schlüssel und Beziehungen, SQL-Abfragen, JOINs und Datenänderungen |
| [Docker](./docker/) | Grundlagen, Images und Container, Volumes und Netzwerke, Docker Compose sowie Fehlerbehebung |
| [Lernfelder](./lernfelder/) | IT-Systeme, Netzwerke, IT-Sicherheit, Softwareentwicklung und Bereitstellung von Anwendungen |
| [Git-CheatSheet](./Git_CheatSheet.md) | Git-Befehle für Commits, Branches, Zusammenführen von Änderungen und die Arbeit mit Remote-Repositories |

## Praktische Programmierarbeiten

### Würfelspiel mit Python

Das [Würfelspiel](./python/wuerfelspiel/) zeigt, wie ich grundlegende Programmierkonzepte an einer konkreten Aufgabe anwende und schrittweise erweitere.

| Datei | Einblick in den Quellcode |
| --- | --- |
| [wuerfelspiel.py](./python/wuerfelspiel/wuerfelspiel.py) | Einfacher Einstieg mit Benutzereingabe, Schleifen, Zufallszahlen von 1 bis 6 und Speicherung der Würfe in einer Liste |
| [neu_wuerfelspiel.py](./python/wuerfelspiel/neu_wuerfelspiel.py) | Erweiterter Lernstand mit mehreren Spielern, Prüfung von Eingaben, Punkteverwaltung, Rundenschleife, Rangliste mit Bubble Sort sowie Code zum Laden und Speichern von Punkteständen als JSON oder XML |

Die [Python-Bereichs-README](./python/README.md) enthält ergänzende Aufgaben und Akzeptanzkriterien, unter anderem zu Würfelergebnissen, Wurfstatistiken und dem Zurücksetzen einer Spielrunde. Diese beschreiben die Lernanforderungen; die einzelnen Skripte zeigen unterschiedliche Bearbeitungsstände.

Dabei übe ich insbesondere Kontrollstrukturen, Listen und Dictionaries, Ausnahmebehandlung und den Umgang mit Dateien.

### Objektorientierter Rollenspiel-Prototyp

Im Ordner [spaßprogrammieren](./python/spa%C3%9Fprogrammieren/) liegen weitere Python-Spielentwürfe. Einen umfangreicheren Einblick bietet [python_spiel4.py](./python/spa%C3%9Fprogrammieren/python_spiel4.py).

Der Quellcode enthält:

- Klassen für Held, Monster, Gegenstände, Quests und Kämpfe;
- Vererbung für unterschiedliche Monstertypen;
- rundenbasierte Kämpfe mit zufälligen Schadenswerten;
- Erfahrungspunkte, Levelaufstiege und eine Skalierung der Monsterwerte;
- Questfortschritt, Belohnungen und Gegenstandsdrops.

Der Prototyp dient dazu, objektorientierte Programmierung und das Zusammenspiel mehrerer Spielsysteme praktisch zu erproben.

## Fachliche Dokumentation

### Datenbanken und SQL

Die Unterlagen verbinden Datenbankgrundlagen mit SQL-Beispielen. Direkte Einstiegspunkte sind:

- [Tabellen, Schlüssel und Beziehungen](./datenbanken-sql/02-tabellen-schluessel-und-beziehungen.md)
- [SELECT, Filter und Sortierung](./datenbanken-sql/04-select-filter-und-sortierung.md)
- [JOINs und Beziehungen](./datenbanken-sql/05-joins-und-beziehungen.md)
- [Daten ändern und verwalten](./datenbanken-sql/06-daten-aendern-und-verwalten.md)

### Docker

Die [Docker-Unterlagen](./docker/) behandeln Containergrundlagen und typische Aufgaben in Entwicklungsumgebungen. Dazu gehören [Images und Container](./docker/02-images-und-container.md), [Volumes und Netzwerke](./docker/03-volumes-und-netzwerke.md), [Docker Compose](./docker/04-docker-compose.md) sowie [Logs, exec und Troubleshooting](./docker/05-logs-exec-und-troubleshooting.md). Befehle und Konfigurationsbeispiele sind in den Markdown-Dokumenten enthalten.

### Lernfelder

Die [Lernfeld-Unterlagen](./lernfelder/) ergänzen die Programmierarbeiten um Themen aus der Umschulung. Dazu zählen Arbeitsplatzsysteme, Netzwerkgrundlagen, Schutzbedarfsanalyse, Anforderungserhebung, Datenmodellierung, UML, Git, Testverfahren und agile Vorgehensweisen. Die Materialien zur Anwendungsbereitstellung behandeln außerdem Service Desk, Inbetriebnahme, Dokumentation und Übergabe.

## Stand des Repositories

Dieses Repository wächst mit meiner Umschulung. Die Programmierarbeiten sind Lernprojekte mit unterschiedlichen Entwicklungsständen und werden schrittweise überarbeitet. Die Dokumentation dient der Vertiefung und Wiederholung der Ausbildungsinhalte.

Weitere Informationen zu mir, meinen technischen Schwerpunkten und Zertifikaten stehen auf meinem [GitHub-Profil](https://github.com/AdriKras).
