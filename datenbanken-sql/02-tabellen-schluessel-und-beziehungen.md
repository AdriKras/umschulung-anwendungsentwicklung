# 2. Tabellen, Schlüssel und Beziehungen

In diesem Kapitel geht es um die Grundpfeiler des relationalen Datenbankdesigns: Tabellen, Schlüssel und Beziehungen.

Relationale Datenbanken bestehen nicht aus isolierten Datensammlungen, sondern aus logisch verknüpften Tabellen. Ein sauberes Datenbankdesign verhindert Datenredundanzen, sichert die referenzielle Integrität und bildet das Fundament für objektorientierte Datenmodelle im Anwendungscode.

Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist dieses Thema entscheidend, um funktionierende Entity-Relationship-Modelle (ERM) zu entwerfen, korrekte ORM-Mappings (z. B. in SQLAlchemy, Entity Framework oder Hibernate) umzusetzen und performante Datenstrukturen zu schaffen.

---

## Kurz erklärt

Eine Tabelle vertritt ein Konzept oder eine Klasse aus der Anwendungsdomäne (Entität).

**Typische Entitäten in Softwareprojekten:**
* `users` / `accounts`
* `orders` / `order_positions`
* `products` / `categories`
* `courses` / `students`

Schlüssel garantieren die eindeutige Identifizierbarkeit und stellen logische Verknüpfungen her.

**Die wichtigsten Schlüsseltypen:**
* **Primärschlüssel (Primary Key):** Eindeutiger Identifikator einer Zeile
* **Fremdschlüssel (Foreign Key):** Verweis auf den Primärschlüssel einer anderen Tabelle
* **Zusammengesetzter Schlüssel (Composite Key):** Primärschlüssel aus mehreren Spalten (häufig bei Zwischentabellen)

**Die wichtigsten Beziehungstypen (Kardinalitäten):**
* `1:1` (One-to-One)
* `1:n` (One-to-Many)
* `n:m` (Many-to-Many)

---

## Das Single-Responsibility-Prinzip für Tabellen

Analoge Regel zum Clean Code in der Anwendungsentwicklung: **Eine Tabelle sollte genau eine Aufgabe haben**.

**Schlechtes Tabellendesign (Monolith-Tabelle):**
```text
Table: order_data
Columns: customer_name, customer_email, product_title, product_price, order_date
```
*Nachteil:* Ändert der Kunde seine E-Mail, muss sie in **jeder** seiner bisherigen Bestellzeilen geändert werden. Wenn kein Produkt gekauft wird, existieren keine Kundendaten.

**Gutes Tabellendesign (Separation of Concerns):**
* `customers` (Stammdaten des Kunden)
* `products` (Produktkatalog)
* `orders` (Bestellkopf)
* `order_items` (Bestellpositionen)

---

## Spalten-Design & Datenatomarität

Spalten beschreiben die Eigenschaften einer Entität (Attribute).

**Regeln für saubere Spalten im Anwendungsdesign:**
* **Atomarität:** Eine Spalte enthält nur genau *einen* unteilbaren Wert.
  * *Schlecht:* `address = "Musterstraße 5, 20095 Hamburg"`
  * *Gut:* `street`, `house_number`, `postal_code`, `city`
* **Eindeutige Benennung:** Verwende lesbare, einheitliche Namen (z. B. `snake_case` in SQL).
* **Keine redundanten Werte:** Berechenbare Daten (z. B. `alter` aus `geburtsdatum`) werden nicht in der DB gespeichert, sondern im Anwendungscode berechnet.

---

## Primärschlüssel (Primary Key - PK)

Der Primärschlüssel macht jeden Datensatz in einer Tabelle unverwechselbar.

```sql
CREATE TABLE members (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email VARCHAR(255) NOT NULL
);
```

**Kriterien für gute Primärschlüssel:**
* **Unveränderlichkeit:** Ein Primärschlüssel darf sich nach dem Erstellen **niemals** ändern.
* **Eindeutigkeit & Non-Null:** Darf niemals doppelt vorkommen und nicht `NULL` sein.
* **Surrogatschlüssel (Künstliche Schlüssel):** In der Praxis werden meist fortlaufende Integers (`id`) oder weltweit eindeutige UUIDs (`uuid`) verwendet. Natürliche Schlüssel (wie Namen oder E-Mail-Adressen) sind ungeeignet, da sie sich im Laufe der Zeit ändern können.

---

## Fremdschlüssel (Foreign Key - FK) & Referenzielle Integrität

Ein Fremdschlüssel baut die Brücke zwischen zwei Tabellen. Er verweist auf den Primärschlüssel einer Eltern-Tabelle.

```sql
CREATE TABLE loans (
  id INTEGER PRIMARY KEY,
  member_id INTEGER NOT NULL,
  loan_date DATE NOT NULL,
  FOREIGN KEY (member_id) REFERENCES members(id)
);
```

**Was leistet referenzielle Integrität?**
Das RDBMS lehnt jeden Versuch ab, in `loans` eine `member_id` einzutragen, die es in `members` gar nicht gibt. Die Datenbank garantiert so auf unterster Ebene die Datenkonsistenz – unabhängig von Bugs im Backend-Code.

---

## Löschweitergabe: `ON DELETE` Regelsätze

Beim Löschen eines Eltern-Datensatzes (z. B. ein User brennt sein Konto nieder) muss definiert werden, was mit den verknüpften Kind-Datensätzen passiert:

* **`ON DELETE RESTRICT` (Standard):** Das Löschen des Users wird blockiert, solange noch abhängige Bestellungen existieren.
* **`ON DELETE CASCADE`:** Löscht der User sein Konto, werden automatisch alle zugehörigen Daten (Profile, Einstellungen) mitgelöscht.
* **`ON DELETE SET NULL`:** Der Fremdschlüssel in der Kind-Tabelle wird auf `NULL` gesetzt (z. B. wenn der Ersteller eines Forenposts gelöscht wird, der Post aber als "Anonym" bestehen bleibt).

---

## Die drei Beziehungstypen in der Softwareentwicklung

### 1. `1:1`-Beziehung (One-to-One)
Ein Datensatz aus A gehört zu genau einem Datensatz aus B.
* **Beispiel:** `User` $\leftrightarrow$ `UserProfile` (Auslagerung von selten genutzten oder sensiblen Zusatzdaten).
* **Umsetzung:** Der Fremdschlüssel erhält zusätzlich einen `UNIQUE`-Constraint.

### 2. `1:n`-Beziehung (One-to-Many)
Ein Datensatz aus A kann mit vielen Datensätzen aus B verknüpft sein. Ein Datensatz aus B verweist aber auf genau einen Datensatz aus A.
* **Beispiel:** `Kunde` (1) $\rightarrow$ `Bestellungen` (n).
* **Umsetzung:** Der Fremdschlüssel liegt **immer auf der n-Seite** (in der Kind-Tabelle).

### 3. `n:m`-Beziehung (Many-to-Many)
Viele Datensätze aus A stehen mit vielen Datensätzen aus B in Beziehung.
* **Beispiel:** `Bücher` $\leftrightarrow$ `Autoren` (Ein Buch hat mehrere Autoren; ein Autor schreibt mehrere Bücher).
* **Umsetzung:** Relationale Datenbanken können `n:m` **nicht direkt** in zwei Tabellen abbilden. Es wird zwingend eine **Zwischentabelle (Join Table)** benötigt!

---

## Die Zwischentabelle (Junction Table / Join Table)

Die Zwischentabelle bricht eine `n:m`-Beziehung in zwei `1:n`-Beziehungen auf.

```sql
CREATE TABLE book_authors (
  book_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  PRIMARY KEY (book_id, author_id),
  FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);
```

**Eigenschaften einer echten Zwischentabelle:**
* Sie besitzt einen **zusammengesetzten Primärschlüssel** aus `(book_id, author_id)`. Das verhindert doppelte Verknüpfungen.
* Sie kann zusätzliche Attribute enthalten (z. B. `role` oder `created_at`).

---

## Constraints zur Datenvalidierung

Constraints entlasten den Anwendungscode von grundlegender Validierungslogik:

* **`NOT NULL`:** Verhindert fehlende Pflichtfelder (z. B. Passwort-Hash).
* **`UNIQUE`:** Erzwingt Eindeutigkeit (z. B. E-Mail-Adresse, Username).
* **`CHECK`:** Validiert Wertebereiche (z. B. `CHECK (age >= 18)` oder `CHECK (price > 0)`).
* **`DEFAULT`:** Injektiert Standardwerte (z. B. `status DEFAULT 'active'`).

---

## Entity-Relationship-Modellierung (ERM)

In der Anwendungsentwicklung wird die Datenbankstruktur vor dem Schreiben von Code in einem ER-Diagramm entworfen.

**Bausteine im ERM:**
* **Entität (Entity):** Rechteck $\rightarrow$ Bildet die spätere Tabelle
* **Attribut:** Ellipse / Liste $\rightarrow$ Bildet die Spalten
* **Beziehung (Relationship):** Rauten / Verbindungslinien $\rightarrow$ Bildet Schlüsselbeziehungen
* **Kardinalität:** Angaben wie `1:1`, `1:n`, `n:m` (oder Chen-/Krähenfuß-Notation)

---

## Typische Fehler beim Datenbankdesign

* **Kein Primärschlüssel:** Datensätze können nicht eindeutig identifiziert oder per ORM gemappt werden.
* **Vergessene Zwischentabelle bei `n:m`:** Der Versuch, Komma-separierte Listen (z. B. `"1,4,7"`) in einer Tabellenspalte zu speichern (Verletzung der 1. Normalform!).
* **Namen als Primärschlüssel:** Führt zu Chaos bei Namensänderungen oder Duplikaten.
* **Blinde `CASCADE`-Löschungen:** Ein Löschbefehl am User tilgt unbemerkt die halbe Datenbank.

---

## FIAE-Bezug

Für Anwendungsentwickler ist saubere Datenmodellierung das A und O:
* **ORM-Mapping:** ORMs (z. B. SQLAlchemy in Python, Entity Framework in C#) spiegeln `1:n`- und `n:m`-Beziehungen direkt als Objekt-Listen im Code wider.
* **Clean Architecture:** Eine durchdachte Tabellenstruktur vereinfacht das Schreiben von Backend-Code drastisch.
* **Performance:** Richtige Fremdschlüsselindizes verhindern schlechte Query-Laufzeiten.

---

## Kurze Zusammenfassung

Tabellen strukturieren Entitäten. **Primärschlüssel** identifizieren Datensätze eindeutig, **Fremdschlüssel** verbinden Tabellen und erzwingen die referenzielle Integrität. **`1:n`** ist der häufigste Beziehungsfall; **`n:m`** wird über eine Zwischentabelle gelöst.
