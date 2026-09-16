# 3. SQL-Grundlagen

In diesem Kapitel geht es um die Grundlagen von SQL (Structured Query Language) aus Sicht der Softwareentwicklung.

SQL ist die universelle Schnittstelle zwischen Anwendungscode und relationalen Datenbanken. Egal ob in Python, JavaScript, Java oder C# – im Hintergrund kommuniziert das Backend über SQL-Statements mit dem Datenbankserver, um Daten abzufragen, zu manipulieren oder Schemas zu verwalten.

Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist das sichere Beherrschen von SQL essenziell, um performante Queries zu verfassen, Geschäftslogik auf Datenbankebene abzusichern und Sicherheitslücken wie SQL-Injections zu verhindern.

---

## Kurz erklärt

SQL bedeutet: **Structured Query Language**

SQL ist eine **deklarative** Programmiersprache. Das bedeutet: Im Anwendungscode beschreibst du, *welche* Daten du haben oder ändern möchtest, nicht *wie* die Datenbank diese intern suchen oder verarbeiten muss.

**Kernfunktionen von SQL:**
* Datenmodelle & Tabellen definieren (`DDL`)
* Anwendungsdaten einfügen, ändern und löschen (`DML`)
* Gezielte Abfragen und Auswertungen erstellen (`DQL`)
* Zugriffsrechte verwalten (`DCL`)
* Transaktionen und Datenkonsistenz steuern (`TCL`)

Die wichtigsten Befehle im Entwickler-Alltag:
```text
SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, WHERE, ORDER BY, LIMIT, JOIN, COMMIT, ROLLBACK
```

---

## Imperativ vs. Deklarativ

Im Gegensatz zur objektorientierten oder funktionalen Programmierung (wie Python oder Java) denkst du in SQL nicht in Schleifen (`for`/`while`) oder Bedingungen (`if`/`else`).

**Beispiel:**
```sql
SELECT name, email
FROM users
WHERE is_active = true;
```
Du weist die Datenbank an: *"Gib mir Name und E-Mail aller aktiven User."* Der Abfrage-Optimizer des RDBMS entscheidet selbstständig, welche Indizes genutzt werden, um das Ergebnis am schnellsten zu liefern.

---

## Syntax-Regeln & Konventionen im Code

* **Schlüsselwörter GROSS:** SQL-Befehle werden nach Industriestandard in GROSSBUCHSTABEN geschrieben (`SELECT`, `FROM`, `WHERE`).
* **Identifikatoren klein:** Tabellen- und Spaltennamen werden klein in `snake_case` geschrieben (`user_profiles`, `created_at`).
* **Semikolon am Befehlsende:** Beendet ein SQL-Statement (besonders wichtig bei Datenbank-Skripten).
* **Kommentare:**
  * Einzeilig: `-- Einzeiliger Kommentar`
  * Mehrzeilig: `/* Mehrzeiliger Kommentar */`

```sql
-- Abfrage aktiver Premium-Kunden für das Dashboard
SELECT id, username, email
FROM users
WHERE status = 'premium'
ORDER BY created_at DESC;
```

---

## Die 5 SQL-Kategorien im Überblick

### 1. DDL (Data Definition Language) – Schema-Design
Definiert und verändert die Struktur der Datenbank.
* `CREATE TABLE`: Erstellt neue Tabellen
* `ALTER TABLE`: Erweitert/verändert bestehende Tabellen
* `DROP TABLE`: Löscht eine Tabelle samt Inhalt

### 2. DML (Data Manipulation Language) – Daten verarbeiten
Bearbeitet die Inhalte innerhalb der Tabellen.
* `INSERT INTO`: Fügt neue Datensätze ein
* `UPDATE`: Aktualisiert bestehende Daten
* `DELETE FROM`: Entfernt Datensätze

### 3. DQL (Data Query Language) – Daten abfragen
Die mit Abstand am häufigsten genutzte Kategorie in Backends.
* `SELECT`: Liest Daten aus einer oder mehreren Tabellen

### 4. TCL (Transaction Control Language) – Transaktionssicherheit
Sichert atomare Operationen ab (z. B. Geldüberweisungen).
* `BEGIN` / `START TRANSACTION`: Startet einen Block
* `COMMIT`: Speichert alle Änderungen unumkehrbar ab
* `ROLLBACK`: Macht alle Änderungen des Blocks bei einem Fehler rückgängig

### 5. DCL (Data Control Language) – Rechteverwaltung
* `GRANT` / `REVOKE`: Vergibt oder entzieht Datenbank-Berechtigungen (z. B. Lese-Rechte für Analytics-User).

---

## DQL-Grundaufbau: Das `SELECT`-Statement

Ein `SELECT`-Befehl wird logisch in folgender Reihenfolge aufgebaut:

```sql
SELECT id, username, email    -- 1. Spaltenauswahl
FROM users                    -- 2. Quell-Tabelle
WHERE is_active = true        -- 3. Zeilen-Filterung
ORDER BY created_at DESC       -- 4. Sortierung
LIMIT 10;                     -- 5. Mengenbegrenzung
```

### Warum `SELECT *` im Produktionscode vermieden werden muss
In der Entwicklung oder im SQL-Client nutzt man gerne `SELECT * FROM table;` zum Testen. In Produktiv-Code (z. B. REST-APIs) gilt `SELECT *` jedoch als **Anti-Pattern**:
* **Performance:** Lädt unnötig Spalten über das Netzwerk, die gar nicht gebraucht werden.
* **Sicherheit:** Kann ungewollt sensible Daten (z. B. `password_hash`) ans Frontend übertragen.
* **Bruch bei Schema-Änderungen:** Neue Spalten verändern unerwartet das Datenformat im Backend.

---

## Filterung mit `WHERE` & Operatoren

Die `WHERE`-Klausel beschränkt die Abfrage auf relevante Datensätze.

**Vergleichsoperatoren:**
`=`, `!=` (oder `<>`), `>`, `<`, `>=`, `<=`

**Logische Verknüpfungen:**
* `AND`: Beide Bedingungen müssen zutreffen.
* `OR`: Mindestens eine Bedingung muss zutreffen.
* `NOT`: Invertiert die Bedingung.

**Spezielle Operatoren für Entwickler:**
* **`IN (...)`**: Prüft gegen eine Liste von Werten (`WHERE status IN ('open', 'pending')`).
* **`BETWEEN a AND b`**: Bereichsabfrage (z. B. für Datumsspannen oder Preise).
* **`LIKE '%muster%'`**: Mustervergleich für Strings (`%` als Platzhalter für beliebige Zeichen).
* **`IS NULL` / `IS NOT NULL`**: Prüft explizit auf das Fehlen von Werten.

---

## Datenmanipulation mit `INSERT`, `UPDATE` & `DELETE`

### `INSERT` (Neuen Datensatz anlegen)
```sql
INSERT INTO users (username, email, password_hash)
VALUES ('max_dev', 'max@example.com', '$2b$12$eImi...');
```

### `UPDATE` (Daten anpassen)
```sql
UPDATE users
SET email = 'max.neu@example.com', updated_at = NOW()
WHERE id = 42;  -- WICHTIG: Immer gezielt per Primary Key filtern!
```

### `DELETE` (Daten entfernen)
```sql
DELETE FROM users
WHERE id = 42;  -- WICHTIG: Ohne WHERE wird die GESAMTE Tabelle geleert!
```

**Entwickler-Goldene-Regel:** Führe vor einem `UPDATE` oder `DELETE` immer zuerst ein `SELECT` mit exakt derselben `WHERE`-Bedingung aus, um zu prüfen, welche Datensätze betroffen sein werden!

---

## Sicherheits-Risiko: SQL-Injection & Prepared Statements

Eine der gefährlichsten Sicherheitslücken in der Softwareentwicklung ist die **SQL-Injection**. Sie entsteht, wenn Usereingaben ungeprüft über String-Konkatenation in ein SQL-Statement eingebunden werden.

**Gefährlicher Code (String Concatenation):**
```python
# FALSCH: Anfällig für SQL-Injection!
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
```
Gibt ein Angreifer als `user_input` den String `' OR '1'='1` ein, lautet die Query:
`SELECT * FROM users WHERE username = '' OR '1'='1';` $ightarrow$ Der Angreifer umgeht das Login und erhält Zugriff auf alle Konten!

**Sicherer Code (Prepared Statements / Parameterized Queries):**
```python
# RICHTIG: Parameterbindung schützt vor Injection
cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
```
Hier trennt die Datenbank-Engine SQL-Code strikt von den Benutzereingaben.

---

## DDL & Schema-Migrationen

Im Entwicklungsverlauf ändert sich das Datenmodell ständig. Diese Änderungen werden in **Migrations-Skripten** (z. B. `V1__init_schema.sql`, `V2__add_phone_to_users.sql`) festgehalten und versioniert.

```sql
-- Erstellen der Tabelle
CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(200) NOT NULL,
  price DECIMAL(10, 2) CHECK (price >= 0),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Nachträgliche Erweiterung
ALTER TABLE products ADD COLUMN stock_quantity INTEGER DEFAULT 0;
```

---

## Typische Fehler bei Entwicklern

* **Fehlendes `WHERE` bei `UPDATE`/`DELETE`:** Führt zu ungewolltem Datenverlust in der gesamten Tabelle.
* **`SELECT *` in der Produktion:** Verschwendet Bandbreite und erhöht Latenzen.
* **Falsche `NULL`-Vergleiche:** Nutzung von `= NULL` statt `IS NULL` (liefert immer ein leeres Ergebnis).
* **Dynamic SQL / SQL-Injection:** Zusammenbauen von Queries per Plus-Zeichen statt Parameter-Binding.
* **Nicht-transaktionale Mehrfach-Updates:** Wenn ein Teilschritt abbricht, bleibt die Datenbank in einem inkonsistenten Zustand.

---

## FIAE-Bezug

Für Anwendungsentwickler bildet SQL das Fundament der Datenverarbeitung:
* **Backend-Entwicklung:** Anbindung von relationalen Datenbanken über Treiber oder ORMs.
* **Datensicherheit:** Konsequenter Einsatz von Prepared Statements gegen Injection-Angriffe.
* **Transaktionsmanagement:** Absichern kritischer Geschäftslogiken (z. B. Payment oder Checkouts).

---

## Kurze Zusammenfassung

SQL ist die deklarative Abfragesprache für relationale Datenbanken. **DQL** (`SELECT`) liest Daten, **DML** (`INSERT`, `UPDATE`, `DELETE`) verarbeitet sie und **DDL** (`CREATE`, `ALTER`) verwaltet das Schema. Entwickler müssen `UPDATE`/`DELETE` immer mit `WHERE` absichern und stets Prepared Statements gegen SQL-Injections einsetzen.
