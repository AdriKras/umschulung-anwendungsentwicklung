# Datenbanken & SQL

In diesem Bereich geht es um relationale Datenbanken und SQL aus Sicht der Softwareentwicklung.
Datenbanken sind ein zentraler Baustein jeder Anwendung, weil Software Daten dauerhaft, strukturiert und performant speichern, verwalten und auswerten muss. SQL (Structured Query Language) wird genutzt, um Datenstrukturen zu definieren, Daten einzufügen, abzufragen, zu aktualisieren und zu löschen.
Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist SQL essenziell, weil nahezu jedes Softwareprojekt (von der REST-API bis zur Enterprise-App) mit einer Datenbank interagiert – sei es direkt über SQL oder über Object-Relational Mapper (ORMs).

## Kurz erklärt

Eine relationale Datenbank speichert Daten in strukturierten Tabellen.
SQL bedeutet: **Structured Query Language**

SQL ist die Standardsprache zur Kommunikation mit relationalen Datenbankmanagementsystemen (RDBMS).

**Typische Aufgaben in der Softwareentwicklung:**
* Datenmodelle und Entitäten-Beziehungen entwerfen
* Tabellenstrukturen (Schemas) definieren
* Test- und Anwendungsdaten einfügen (`INSERT`)
* Komplexe Datenabfragen schreiben (`SELECT`)
* Anwendungsdaten sicher aktualisieren (`UPDATE`)
* Nicht mehr benötigte Datensätze löschen (`DELETE`)
* Tabellen über Relationen effizient miteinander verknüpfen (`JOIN`)
* Constraints zur Sicherstellung der Datenintegrität einsetzen
* Datenbankabfragen auf Performance optimieren

---

## Kapitelübersicht

* **1. Datenbank-Grundlagen:** Grundbegriffe, Tabellen, Datensätze und relationale Datenbanken
* **2. Tabellen, Schlüssel und Beziehungen:** Primärschlüssel, Fremdschlüssel, Normalisierung und Datenmodellierung
* **3. SQL-Grundlagen:** Grundstruktur von SQL-Befehlen und wichtige SQL-Kategorien
* **4. SELECT, Filter und Sortierung:** Daten zielgerichtet abfragen, filtern, sortieren und begrenzen
* **5. Joins und Beziehungen:** Tabellen verbinden und relationale Datenmodelle auswerten
* **6. Daten ändern und verwalten:** INSERT, UPDATE, DELETE, Transaktionen und Konsistenz

---

## Warum Datenbanken in der Softwareentwicklung wichtig sind

Fast jede professionelle Softwareanwendung arbeitet mit persistenten Daten.

**Beispiele:**
* **Onlineshop:** Kunden, Produkte, Bestellungen, Zahlungsarten
* **Bibliothekssystem:** Bücher, Mitglieder, Ausleihen, Vormerkungen
* **Ticketsystem:** Benutzer, Tickets, Status, Kommentare
* **Schulverwaltung:** Schüler, Kurse, Noten, Zuordnungen
* **Web-API / Mobile App:** User-Profile, Tokens, Anwendungsdaten

Ohne Datenbanken müssten Daten flüchtig im Hauptspeicher oder unstrukturiert in Textdateien gehalten werden. Das wäre langsam, schwer zu durchsuchen und anfällig für Datenverlust. Eine relationale Datenbank sorgt für Konsistenz, Performance und strukturierte Zugriffe.

---

## Wichtige Grundbegriffe

* **Datenbank:** Sammlung strukturierter Daten unter Verwaltung eines RDBMS
* **Tabelle:** Geordnete Struktur aus Zeilen (Datensätzen) und Spalten (Attributen)
* **Spalte:** Ein bestimmtes Attribut einer Entität (z. B. `email`, `created_at`)
* **Zeile / Datensatz:** Eine konkrete Instanz / Entität in einer Tabelle
* **Primärschlüssel (Primary Key):** Eindeutige Identifikation eines Datensatzes
* **Fremdschlüssel (Foreign Key):** Verweis auf einen Primärschlüssel einer anderen Tabelle zur Abbildung von Beziehungen
* **Constraint:** Regel zur Sicherstellung der Datenqualität (z. B. `NOT NULL`, `UNIQUE`)
* **Query:** Eine an die Datenbank gerichtete SQL-Abfrage
* **Relation:** Logische Beziehung zwischen Tabellen

---

## SQL-Befehlskategorien

* **DDL (Data Definition Language):** Struktur definieren (`CREATE`, `ALTER`, `DROP`)
* **DML (Data Manipulation Language):** Daten bearbeiten (`INSERT`, `UPDATE`, `DELETE`)
* **DQL (Data Query Language):** Daten abfragen (`SELECT`)
* **DCL (Data Control Language):** Rechte steuern (`GRANT`, `REVOKE`)
* **TCL (Transaction Control Language):** Transaktionen verwalten (`COMMIT`, `ROLLBACK`)

Für den Anwendungsentwickler sind **DQL**, **DML** und **DDL** das tägliche Werkzeug.

---

## Typischer SQL-Ablauf im Code

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE
);

INSERT INTO users (id, name, email)
VALUES (1, 'Max', 'max@example.com');

SELECT * FROM users;

UPDATE users
SET email = 'max.neu@example.com'
WHERE id = 1;

DELETE FROM users
WHERE id = 1;
```

---

## Relationale Datenmodellierung

Relationale Datenbanken vermeiden Redundanzen, indem Daten auf mehrere spezialisierte Tabellen verteilt werden (Normalisierung).

**Beispiel Bibliothek:**
* `books` (Buchdetails)
* `authors` (Autorendaten)
* `members` (Nutzerkonten)
* `loans` (Ausleihvorgänge)

Über Primär- und Fremdschlüssel verknüpft das RDBMS diese Tabellen logisch miteinander. Dadurch bleibt das Datenmodell sauber, flexibel und erweiterbar.

---

## SQL in der FIAE-Praxis

Für Anwendungsentwickler ist SQL ein Kernbaustein:
* **Datenbankdesign:** Entwerfen robuster ER-Diagramme und Datenmodelle für neue Features
* **Backend-Entwicklung:** Anbindung von Datenbanken an APIs (z. B. in Python, Node.js, C# oder Java)
* **ORM-Verständnis:** Verstehen, welchen SQL-Code ORMs (wie SQLAlchemy, Entity Framework, Prisma) im Hintergrund generieren
* **Performance-Optimierung:** Schreiben effizienter Queries mit passender Indizierung
* **Datenintegrität:** Absichern von Geschäftslogik durch Transaktionen und Constraints

---

## Verbindung zu Docker

In der Entwicklung werden Datenbanken selten lokal fest installiert. Stattdessen nutzt man Docker-Container für eine saubere Trennung:

```yaml
services:
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: appdb
    volumes:
      - db_data:/var/lib/postgresql/data

  adminer:
    image: adminer
    ports:
      - "8080:8080"

volumes:
  db_data:
```

---

## Typische Entwickler-Fehler

* **`SELECT *` im Produktionscode:** Überträgt unnötige Daten und verschlechtert die Performance
* **Fehlende `WHERE`-Klausel bei `UPDATE` / `DELETE`:** Überschreibt oder löscht ungewollt die gesamte Tabelle
* **Fehlende Indizierung:** Abfragen auf großen Tabellen werden ohne Indizes extrem langsam
* **N+1 Query-Problem:** Exzessive Datenbankabfragen innerhalb von Schleifen im Anwendungscode
* **Fehlende SQL-Injection-Absicherung:** Dynamisches Zusammenbauen von SQL-Strings statt Prepared Statements
* **Vergessene Transaktionen:** Teilschritte schlagen fehl und hinterlassen inkonsistente Zustände

---

## Gute Entwickler-Praxis

* **Prepared Statements nutzen:** Absicherung gegen SQL-Injections
* **Erst selektieren, dann ändern:** Vor `UPDATE` oder `DELETE` die `WHERE`-Bedingung mit `SELECT` prüfen
* **Explizite Spalten abfragen:** Statt `SELECT *` nur die tatsächlich benötigten Spalten anfordern
* **Transaktionen verwenden:** Zusammengehörende Schreiboperationen atomar verarbeiten
* **Code & Schema versionieren:** Datenbank-Migrationen im Git-Repository verwalten

---

## Praktische Lernziele

Nach diesem Bereich solltest du in der Lage sein:
* Relationale Datenmodelle sauber zu entwerfen
* Komplexe SQL-Abfragen mit `JOIN`, `WHERE`, `GROUP BY` und `ORDER BY` zu schreiben
* Datenmanipulationen (`INSERT`, `UPDATE`, `DELETE`) sicher auszuführen
* Datenbank-Container via Docker Compose in Anwendungs-Setups zu integrieren
* SQL-Injections im Anwendungscode zu verhindern

---

## Kurze Zusammenfassung

Datenbanken sichern Anwendungsdaten dauerhaft und strukturiert. SQL ist die universelle Schnittstelle zur Datenverarbeitung. Für Anwendungsentwickler ist die Beherrschung von SQL Voraussetzung für das Schreiben performanter, sicherer und skalierbarer Backends.
