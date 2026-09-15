# 05-03: LF 5.2 ER-Modellierung & Logischer Datenbankentwurf

Dieses Modul behandelt die Grundlagen des Entity-Relationship-Modells (ERM), die Identifikation von Entitäten, Attributen und Primärschlüsseln sowie die Modellierung von Kardinalitäten im Entwurfsprozess.

---

## 1. Zweck des ER-Modells in der Softwareentwicklung

Das **Entity-Relationship-Modell (ERM)** dient in der Entwurfsphase der konzeptionellen Datenmodellierung. Es abstrahiert die realen Geschäftsobjekte und deren Beziehungen unabhängig von der späteren konkreten Datenbanktechnologie (z. B. PostgreSQL, MySQL, NoSQL).

---

## 2. Grundbausteine eines ERM

| Baustein | Beschreibung | Beispiel im FIAE-Kontext | Notation (Chen / IE / Chen-Krähenfuß) |
| :--- | :--- | :--- | :--- |
| **Entität (Entity)** | Ein eindeutig identifizierbares Objekt der Realwelt. | `Kunde`, `Bestellung`, `Produkt` | Rechteck |
| **Attribut** | Eine Eigenschaft, die eine Entität näher beschreibt. | `Kunden_ID`, `E_Mail`, `Erstellungsdatum` | Oval / Liste im Rechteck |
| **Primärschlüssel (Primary Key)** | Attribut(e), die jede Entitätsinstanz eindeutig identifizieren. | `kunden_id` (PK) | Unterstrichenes Attribut |
| **Beziehung (Relationship)** | Logische Verknüpfung zwischen zwei oder mehr Entitäten. | "Kunde *platziert* Bestellung" | Raute / Verbindungslinie |

---

## 3. Kardinalitäten (Beziehungstypen)

Kardinalitäten legen fest, wie viele Instanzen einer Entität mit wie vielen Instanzen einer anderen Entität in Beziehung stehen können.

| Kardinalität | Beschreibung | Beispiel | Auflösung in relationalen Datenmodellen |
| :---: | :--- | :--- | :--- |
| **1 : 1** | Jedes Element A gehört zu genau einem Element B und umgekehrt. | `Benutzer` $\leftrightarrow$ `Benutzerprofil` | Fremdschlüssel in einer der beiden Tabellen (mit `UNIQUE`-Constraint). |
| **1 : n** | Ein Element A kann mit mehreren Elementen B verknüpft sein; B gehört zu genau einem A. | `Kunde` $\leftrightarrow$ `Bestellung` | Fremdschlüssel (FK) auf der **n-Seite** (`Bestellung` erhält `kunden_id`). |
| **m : n** | Mehrere Elemente A stehen mit mehreren Elementen B in Beziehung. | `Bestellung` $\leftrightarrow$ `Produkt` | **Zwischentabelle (Junction Table)** notwendig (z. B. `Bestellposition` mit zusammengesetztem PK). |

---

## FIAE-Zusammenfassung
Entwickler nutzen das ERM zur Vorbereitung der DDL-Skripte (`CREATE TABLE`), wandeln m:n-Beziehungen durch Zwischentabellen um und stellen über Primär- und Fremdschlüssel die referenzielle Integrität im Datenmodell sicher.
