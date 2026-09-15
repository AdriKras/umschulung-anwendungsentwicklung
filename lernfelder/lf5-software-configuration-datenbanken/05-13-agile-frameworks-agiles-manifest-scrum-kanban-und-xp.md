# 05-13: LF 5.6 Agile Frameworks (Agiles Manifest, Scrum, Kanban & XP)

Dieses Modul behandelt die Kernwerte des Agilen Manifests, das Scrum-Framework (Rollen, Artefakte, Events), Kanban (WIP-Limits, Continuous Flow) sowie eXtreme Programming (XP, TDD, Pair Programming).

---

## 1. Das Agile Manifest (4 Core Values)

1. **Individuen und Interaktionen** stehen über Prozessen und Werkzeugen.
2. **Funktionierende Software** steht über umfassender Dokumentation.
3. **Zusammenarbeit mit dem Kunden** steht über Vertragsverhandlungen.
4. **Reagieren auf Veränderung** steht über dem Befolgen eines Plans.

---

## 2. Das Scrum-Framework

Scrum basiert auf Empirie (Transparenz, Überprüfung, Anpassung) und nutzt feste Zeitfenster (**Timeboxes**).

### Die 3 Rollen
* **Product Owner (PO):** Maximiert den Wert des Produkts, verwaltet und priorisiert das Product Backlog.
* **Scrum Master:** Servants Leader; stellt die Einhaltung des Scrum-Prozesses sicher und beseitigt Hindernisse (*Impediments*).
* **Developers (Entwicklerteam):** Schätzt, plant und setzt die Inkremente eigenverantwortlich und interdisziplinär um.

### Die 3 Artefakte
* **Product Backlog:** Geordnete Liste aller bekannten Anforderungen an das Produkt.
* **Sprint Backlog:** Auswahl von Product-Backlog-Einträgen für den aktuellen Sprint inklusive Umsetzungsplan.
* **Increment:** Das funktionsfähige, potenziell auslieferbare Produktteilstück am Ende eines Sprints (*Definition of Done* erfüllt).

### Die 5 Events (Ablauf eines Sprints)
```text
[ Sprint Planning ] ---> [ Daily Scrum (tägl. 15m) ] ---> [ Sprint Review ] ---> [ Sprint Retrospective ]
                                                                ^
                                                 (Der Sprint selbst ist das Event-Gefäß)
```

---

## 3. Kanban: Continuous Flow & WIP-Limits

Im Gegensatz zu den zeitboxorientierten Sprints von Scrum basiert Kanban auf einem **kontinuierlichen Fluss (Continuous Flow)** von Aufgaben.

* **WIP-Limit (Work In Progress Limit):** Maximale Anzahl von Aufgaben, die sich gleichzeitig in einer Spalte/Statusphase befinden dürfen.
* **Zweck von WIP-Limits:** Verhindert Überlastung, deckt Engpässe (*Bottlenecks*) im Arbeitsprozess sofort auf und fördert das Fertigstellen von Aufgaben vor dem Start neuer (*"Stop Starting, Start Finishing"*).

---

## 4. eXtreme Programming (XP) Engineering Practices

* **Pair Programming:** Zwei Entwickler arbeiten gemeinsam an einem Arbeitsplatz (Driver schreibt Code, Navigator prüft und denkt strategisch).
* **Test-Driven Development (TDD):** Entwurfsschleife *Red-Green-Refactor* (Erst fehlschlagenden Test schreiben $\rightarrow$ minimalen Code schreiben bis Test grün $\rightarrow$ Code refactorn).
* **Continuous Integration (CI):** Mehrmals tägliches Integrieren und automatisiertes Testen des Quellcodes.
* **Refactoring:** Kontinuierliches Verbessern der internen Code-Struktur ohne das externe Verhalten zu verändern.

---

## FIAE-Zusammenfassung
Entwickler wenden agile Praktiken wie TDD und Pair Programming (XP) an, steuern ihre Tasks via WIP-Limits auf Kanban-Boards und arbeiten im Scrum-Framework eigenverantwortlich an wertvollem Software-Inkrementen.
