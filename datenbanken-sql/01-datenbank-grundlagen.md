# 1. Datenbank-Grundlagen

In diesem Kapitel geht es um die Grundlagen von Datenbanken aus Sicht der Softwareentwicklung.

Datenbanken werden genutzt, um Anwendungsdaten strukturiert, dauerhaft, performant und gezielt abrufbar zu speichern. Nahezu jede Anwendung – egal ob Web-App, Mobile App, REST-API oder Enterprise-Software – arbeitet im Hintergrund mit einer Datenbank.

Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist es essenziell zu verstehen, wie Datenbanken aufgebaut sind, wie Datenmodelle strukturiert werden und wie Anwendungen mit relationalen Datenbanken interagieren.

---

## Kurz erklärt

Eine Datenbank ist eine strukturierte Sammlung von Daten, die von einem Datenbankmanagementsystem (DBMS) verwaltet wird.

**Beispiele für Datenobjekte (Entitäten) in der Softwareentwicklung:**
* User / Accounts
* Produkte / Kataloge
* Bestellungen / Transaktionen
* Support-Tickets
* Authentifizierungs-Tokens
* Anwendungs-Logs

Eine Datenbank sorgt dafür, dass diese Daten nicht ungeordnet abgelegt werden, sondern nach definierten Regeln verarbeitet werden.

**Grundfunktionen:**
* Speichern
* Suchen & Filtern
* Sortieren
* Aktualisieren
* Löschen
* Verknüpfen (Beziehungen)
* Auswerten

---

## Warum Datenbanken in der Entwicklung gebraucht werden

Ohne Datenbank müssten Anwendungen Daten in einfachen Textdateien (z. B. JSON, CSV, TXT) auf der Festplatte verwalten.

**Probleme einfacher Dateispeicher in Anwendungen:**
* **Redundanz:** Daten kommen leicht mehrfach vor.
* **Performance:** Suche in großen Dateien ist extrem langsam.
* **Nebenläufigkeit (Concurrency):** Parallele Lese- und Schreibzugriffe von mehreren Usern führen zu Konflikten oder Datenverlust.
* **Datenintegrität:** Keine automatische Prüfung von Datentypen und Abhängigkeiten.
* **Sicherheit:** Granulare Rechtekonzepte auf Spalten- oder Datensatz-Ebene sind kaum umsetzbar.

Eine Datenbank löst diese Probleme und sichert durch Prinzipien wie **ACID** (Atomizität, Konsistenz, Isolation, Dauerhaftigkeit) die Verlässlichkeit der Anwendungsdaten.

---

## Beispiele aus der Praxis

* **Onlineshop-App:** Kunden, Produkte, Warenkörbe, Bestellpositionen
* **Bibliothekssystem:** Bücher, Autoren, Mitglieder, Ausleihen
* **SaaS-Ticketsystem:** Benutzer, Rollen, Tickets, Status, Kommentare
* **Schulverwaltungs-Software:** Schüler, Kurse, Noten, Anwesenheiten
* **Social-Media-API:** User, Posts, Likes, Kommentare, Follower

---

## Datei vs. Datenbank

* **Struktur:** Dateien sind oft unstrukturiert – Datenbanken erzwingen ein klares Schema.
* **Suche:** Dateien erfordern manuelles Durchsuchen – Datenbanken nutzen Indizes und SQL-Queries.
* **Beziehungen:** In Dateien schwer abbildbar – in relationalen DBs über Primär- und Fremdschlüssel gelöst.
* **Multi-User:** Für Dateien problematisch – für DBs der Standardfall.
* **Konsistenz:** In Dateien schwer zu sichern – in DBs über Constraints abgesichert.

---

## Relationale Datenbanken

In der Softwareentwicklung unterscheidet man verschiedene Datenbank-Paradigmen. Der Industriestandard für strukturierte Daten sind **relationale Datenbanken (RDBMS)**.

**Bekannte RDBMS-Systeme:**
* PostgreSQL (Sehr beliebt im Backend-Umfeld)
* MariaDB / MySQL
* SQLite (Ideal für Mobile Apps, Desktop-Apps und lokale Tests)
* Microsoft SQL Server
* Oracle Database

Der Begriff „relational“ bedeutet, dass Daten in zweidimensionalen Tabellen organisiert werden und diese Tabellen logisch miteinander in Beziehung stehen.

---

## Tabellen

Eine Tabelle vertritt in der Regel ein Konzept oder eine Klasse aus dem Anwendungscode (z. B. Klasse `User` $\rightarrow$ Tabelle `users`).

Eine Tabelle besteht aus:
* **Spalten (Attributen):** Definieren die Merkmale der Klasse.
* **Zeilen (Datensätzen/Tupeln):** Stellen die konkreten Objekte / Instanzen dar.
* **Werten:** Die konkrete Eigenschaft in einer Zelle.

---

## Spalten & Datentypen

Jede Spalte hat einen fest definierten Datentyp. Die Wahl des richtigen Datentyps schützt vor ungültigen Daten und optimiert die Performance.

**Häufige SQL-Datentypen in der Entwicklung:**
* `INTEGER` / `BIGINT`: Ganze Zahlen (z. B. IDs, Zähler)
* `VARCHAR(n)` / `TEXT`: Zeichenketten mit/ohne Längenbegrenzung
* `BOOLEAN`: Wahrheitswerte (`true` / `false`)
* `DATE` / `TIMESTAMP`: Datum und Uhrzeit (Wichtig für Audit-Logs wie `created_at`)
* `DECIMAL` / `NUMERIC`: Exakte Kommazahlen (Unerlässlich für Geldbeträge!)

---

## Beispiel einer Tabelle in SQL

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE
);
```

---

## Grundlegende Data-Operations

**Daten einfügen (`INSERT`):**
```sql
INSERT INTO users (id, name, email)
VALUES (1, 'Max Müller', 'max@example.com');
```

**Daten abfragen (`SELECT`):**
```sql
SELECT name, email FROM users WHERE id = 1;
```

**Daten aktualisieren (`UPDATE`):**
```sql
UPDATE users SET email = 'max.neu@example.com' WHERE id = 1;
```

**Daten löschen (`DELETE`):**
```sql
DELETE FROM users WHERE id = 1;
```

---

## Primärschlüssel & Fremdschlüssel

* **Primärschlüssel (Primary Key):** Identifiziert jeden Datensatz in einer Tabelle eindeutig (z. B. `id`). Vermeidet Verwechslungen bei Namensgleichheit.
* **Fremdschlüssel (Foreign Key):** Eine Spalte, die auf den Primärschlüssel einer anderen Tabelle verweist. Stellt die Beziehung zwischen Objekten her (z. B. `user_id` in der Tabelle `orders`).

---

## Beziehungen zwischen Entitäten (Beziehungstypen)

* **1:1 (One-to-One):** Ein Datensatz A gehört zu genau einem Datensatz B (z. B. `User` $\leftrightarrow$ `UserProfile`).
* **1:n (One-to-Many):** Ein Datensatz A kann mehreren Datensätzen B zugeordnet sein (z. B. `Kunde` $\rightarrow$ `Bestellungen`). Der häufigste Beziehungsfall!
* **n:m (Many-to-Many):** Viele Datensätze A stehen mit vielen Datensätzen B in Verbindung (z. B. `Bücher` $\leftrightarrow$ `Autoren`). Wird relational über eine **Zwischentabelle** gelöst.

---

## Constraints (Datenintegrität)

Constraints sind Regeln, die die Datenbank automatisch auf Datenebene erzwingt, damit fehlerhafte Daten aus dem Anwendungscode abgeblockt werden:

* `PRIMARY KEY`: Eindeutig und nicht `NULL`
* `FOREIGN KEY`: Garantiert, dass der verwiesene Datensatz existiert (referenzielle Integrität)
* `NOT NULL`: Wert darf beim Erstellen nicht leer gelassen werden
* `UNIQUE`: Wert darf in dieser Spalte nur einmal in der gesamten Tabelle vorkommen
* `CHECK`: Prüft mathematische/logische Bedingungen (z. B. `CHECK (price > 0)`)

---

## Das Konzept `NULL`

`NULL` bedeutet in der Datenbankwelt: **Wert ist unbekannt oder nicht vorhanden**.

Wichtig für Anwendungsentwickler: `NULL` ist **nicht** gleich `0`, `false` oder ein leerer String `""`. Das unbedachte Verarbeiten von `NULL`-Werten im Backend führt häufig zu `NullPointerExceptions` oder Abstürzen.

---

## DB-Systeme & Architektur

* **DBMS:** Das Gesamtsystem zur Verwaltung der Daten.
* **Client-Server-Prinzip:** Der Anwendungscode (z. B. Python Backend) fungiert als **Client** und sendet über einen Datenbanktreiber SQL-Queries an den **Database Server**.
* **CRUD:** Ein fundamentales Akronym in der Softwareentwicklung:
  * **C**reate = `INSERT`
  * **R**ead = `SELECT`
  * **U**pdate = `UPDATE`
  * **D**elete = `DELETE`

---

## Datenbankentwurf & Normalisierung

Bevor Code geschrieben wird, wird das **Datenmodell** entworfen (z. B. als ER-Diagramm).

Ziel der **Normalisierung** ist es, Daten frei von Redundanzen (doppelten Inhalten) zu speichern. Ändert sich z. B. die E-Mail eines Kunden, muss sie bei sauberer Normalisierung nur an **einer** Stelle in der Datenbank angepasst werden.

---

## Typische Fehler in der Softwareentwicklung

* **`UPDATE` / `DELETE` ohne `WHERE`:** Überschreibt oder löscht ungewollt die gesamte Tabelle.
* **SQL-Injection:** Dynamische String-Konkatenation von User-Eingaben in SQL-Statements anstelle von Prepared Statements.
* **Fehlende Constraints:** Überlassen der Datenvalidierung rein dem Anwendungscode (Datenbank wird dadurch anfällig für inkonsistente Zustände).
* **Falsche Datentypen:** Verwendung von Strings für Datumsangaben oder Gleitkommazahlen (`FLOAT`) für Geldbeträge.

---

## FIAE-Bezug

Für Anwendungsentwickler sind Datenbankgrundlagen essenziell:
* **Software-Architektur:** Entwerfen von Datenmodellen, die sauber mit OOP-Klassen harmonieren.
* **Backend-Entwicklung:** Anbindung von Datenbanken über SQL-Treiber oder ORMs.
* **Sicherheit:** Schutz vor SQL-Injections und Garantieren der Konsistenz.
* **DevOps & Testing:** Aufsetzen von isolierten Test-Datenbanken via Docker.

---

## Kurze Zusammenfassung

Datenbanken verwalten Anwendungsdaten strukturiert, sicher und dauerhaft. Relationale Datenbanken organisieren Entitäten in Tabellen und verbinden diese über Primär- und Fremdschlüssel. Die grundlegenden Operationen einer Anwendung entsprechen den CRUD-Befehlen in SQL.
