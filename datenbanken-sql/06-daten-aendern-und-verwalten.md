# 6. Daten ändern und verwalten

In diesem Kapitel geht es darum, wie Daten mit SQL eingefügt, geändert und gelöscht werden.

Datenbanken werden nicht nur gelesen. In der Praxis müssen Daten auch erstellt, aktualisiert oder entfernt werden. Dabei muss man vorsichtig arbeiten, weil falsche `UPDATE`- oder `DELETE`-Befehle viele Datensätze auf einmal verändern können.

Für Fachinformatiker für Systemintegration ist dieses Thema wichtig, weil man Daten in Testumgebungen pflegen, Beispielwerte einfügen, Datenbankprobleme nachvollziehen und einfache Korrekturen verstehen können sollte.

---

## Kurz erklärt

Die wichtigsten Befehle zum Ändern von Daten sind:

| Befehl   | Bedeutung                    |
| -------- | ---------------------------- |
| `INSERT` | neue Datensätze einfügen     |
| `UPDATE` | vorhandene Datensätze ändern |
| `DELETE` | Datensätze löschen           |

Diese Befehle gehören zu:

```text
DML = Data Manipulation Language
```

DML bedeutet:

```text
Daten innerhalb von Tabellen bearbeiten
```

Wichtiger Merksatz:

```text
Erst SELECT prüfen, dann UPDATE oder DELETE ausführen.
```

---

## INSERT

`INSERT` fügt neue Datensätze in eine Tabelle ein.

Beispiel:

```sql
INSERT INTO users (id, name, email)
VALUES (1, 'Max Müller', 'max@example.com');
```

Bedeutung:

| Teil                | Erklärung                         |
| ------------------- | --------------------------------- |
| `INSERT INTO users` | Daten in Tabelle `users` einfügen |
| `(id, name, email)` | diese Spalten werden befüllt      |
| `VALUES (...)`      | diese Werte werden eingefügt      |

Die Reihenfolge der Werte muss zur Reihenfolge der Spalten passen.

---

## INSERT mit mehreren Datensätzen

Man kann mehrere Datensätze gleichzeitig einfügen.

```sql
INSERT INTO users (id, name, email)
VALUES
  (1, 'Max Müller', 'max@example.com'),
  (2, 'Lisa Schmidt', 'lisa@example.com'),
  (3, 'Sara Klein', 'sara@example.com');
```

Das ist übersichtlicher als drei einzelne `INSERT`-Befehle.

Praktisch für:

- Testdaten
- Beispieldaten
- Seed-Daten
- kleine Lernprojekte

---

## INSERT ohne alle Spalten

Man muss nicht immer alle Spalten angeben.

Beispiel:

```sql
CREATE TABLE tickets (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  status TEXT DEFAULT 'open'
);
```

Einfügen:

```sql
INSERT INTO tickets (id, title)
VALUES (1, 'Drucker funktioniert nicht');
```

Da `status` einen Standardwert hat, wird automatisch gesetzt:

```text
open
```

Das funktioniert nur, wenn fehlende Spalten entweder `NULL` erlauben oder einen `DEFAULT`-Wert haben.

---

## INSERT und NOT NULL

Wenn eine Spalte `NOT NULL` hat, muss ein Wert angegeben werden.

Beispiel:

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT
);
```

Falsch:

```sql
INSERT INTO users (id, email)
VALUES (1, 'max@example.com');
```

Problem:

```text
name darf nicht fehlen.
```

Richtig:

```sql
INSERT INTO users (id, name, email)
VALUES (1, 'Max Müller', 'max@example.com');
```

---

## INSERT und UNIQUE

`UNIQUE` verhindert doppelte Werte.

Beispiel:

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email TEXT UNIQUE
);
```

Wenn diese E-Mail schon existiert:

```sql
INSERT INTO users (id, email)
VALUES (1, 'max@example.com');
```

Dann führt dieser zweite Insert zu einem Fehler:

```sql
INSERT INTO users (id, email)
VALUES (2, 'max@example.com');
```

Die Datenbank schützt dadurch die Datenqualität.

---

## INSERT und Fremdschlüssel

Ein Fremdschlüssel verweist auf eine andere Tabelle.

Beispiel:

```sql
CREATE TABLE members (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE loans (
  id INTEGER PRIMARY KEY,
  member_id INTEGER NOT NULL,
  loan_date DATE NOT NULL,
  FOREIGN KEY (member_id) REFERENCES members(id)
);
```

Zuerst muss das Mitglied existieren:

```sql
INSERT INTO members (id, name)
VALUES (1, 'Max');
```

Dann kann eine Ausleihe erstellt werden:

```sql
INSERT INTO loans (id, member_id, loan_date)
VALUES (1, 1, '2026-08-25');
```

Falsch wäre:

```sql
INSERT INTO loans (id, member_id, loan_date)
VALUES (2, 999, '2026-08-25');
```

Wenn es kein Mitglied mit `id = 999` gibt, verletzt das den Fremdschlüssel.

---

## UPDATE

`UPDATE` ändert vorhandene Datensätze.

Beispiel:

```sql
UPDATE users
SET email = 'max.neu@example.com'
WHERE id = 1;
```

Bedeutung:

| Teil              | Erklärung                     |
| ----------------- | ----------------------------- |
| `UPDATE users`    | Tabelle `users` ändern        |
| `SET email = ...` | neue E-Mail setzen            |
| `WHERE id = 1`    | nur Datensatz mit ID 1 ändern |

`WHERE` ist hier extrem wichtig.

---

## UPDATE ohne WHERE

Ein gefährlicher Fehler:

```sql
UPDATE users
SET email = 'test@example.com';
```

Das ändert alle Datensätze in der Tabelle.

Deshalb sollte man vor einem `UPDATE` zuerst prüfen:

```sql
SELECT *
FROM users
WHERE id = 1;
```

Dann erst:

```sql
UPDATE users
SET email = 'max.neu@example.com'
WHERE id = 1;
```

Gute Regel:

```text
Bei UPDATE fast immer WHERE nutzen.
```

---

## Mehrere Spalten ändern

Man kann mehrere Spalten gleichzeitig ändern.

```sql
UPDATE tickets
SET status = 'closed',
    updated_at = '2026-08-25'
WHERE id = 5;
```

Das ändert bei Ticket 5:

```text
status
updated_at
```

Mehrere Änderungen werden mit Komma getrennt.

---

## UPDATE mit Bedingungen

`UPDATE` kann mit normalen `WHERE`-Bedingungen genutzt werden.

Beispiel:

```sql
UPDATE tickets
SET status = 'closed'
WHERE status = 'open'
  AND created_at < '2026-08-01';
```

Das schließt offene Tickets, die vor dem 01.08.2026 erstellt wurden.

Vorher prüfen:

```sql
SELECT *
FROM tickets
WHERE status = 'open'
  AND created_at < '2026-08-01';
```

So sieht man, welche Datensätze betroffen wären.

---

## UPDATE mit NULL

Man kann Werte auf `NULL` setzen, wenn die Spalte `NULL` erlaubt.

Beispiel:

```sql
UPDATE users
SET phone = NULL
WHERE id = 1;
```

Das bedeutet:

```text
Keine Telefonnummer gespeichert.
```

Wichtig:

`NULL` ist nicht dasselbe wie leerer Text.

```text
NULL = kein Wert vorhanden
'' = leerer Text vorhanden
```

---

## DELETE

`DELETE` löscht Datensätze aus einer Tabelle.

Beispiel:

```sql
DELETE FROM users
WHERE id = 1;
```

Bedeutung:

| Teil                | Erklärung                      |
| ------------------- | ------------------------------ |
| `DELETE FROM users` | aus Tabelle `users` löschen    |
| `WHERE id = 1`      | nur Datensatz mit ID 1 löschen |

Auch hier ist `WHERE` sehr wichtig.

---

## DELETE ohne WHERE

Sehr gefährlich:

```sql
DELETE FROM users;
```

Das löscht alle Datensätze aus der Tabelle.

Die Tabelle selbst bleibt bestehen, aber sie ist danach leer.

Vor einem `DELETE` sollte man prüfen:

```sql
SELECT *
FROM users
WHERE id = 1;
```

Dann erst:

```sql
DELETE FROM users
WHERE id = 1;
```

Gute Regel:

```text
Erst SELECT, dann DELETE.
```

---

## DELETE und Fremdschlüssel

Fremdschlüssel können verhindern, dass Daten gelöscht werden.

Beispiel:

Ein Mitglied hat Ausleihen.

```text
members.id -> loans.member_id
```

Wenn man das Mitglied löschen möchte, kann die Datenbank das verhindern, weil noch Ausleihen darauf verweisen.

Beispiel:

```sql
DELETE FROM members
WHERE id = 1;
```

Möglicher Fehler:

```text
foreign key constraint violation
```

Das bedeutet:

```text
Ein anderer Datensatz verweist noch auf diesen Datensatz.
```

---

## ON DELETE

Bei Fremdschlüsseln kann man festlegen, was beim Löschen passiert.

Häufige Varianten:

| Regel      | Bedeutung                               |
| ---------- | --------------------------------------- |
| `RESTRICT` | Löschen wird verhindert                 |
| `CASCADE`  | abhängige Datensätze werden mitgelöscht |
| `SET NULL` | Fremdschlüssel wird auf NULL gesetzt    |

Beispiel:

```sql
FOREIGN KEY (member_id) REFERENCES members(id)
ON DELETE RESTRICT
```

Vorsicht bei:

```sql
ON DELETE CASCADE
```

Das kann viele abhängige Datensätze automatisch löschen.

---

## TRUNCATE kurz erklärt

`TRUNCATE` leert eine Tabelle sehr schnell.

Beispiel:

```sql
TRUNCATE TABLE users;
```

Unterschied zu `DELETE`:

| Befehl                  | Wirkung                              |
| ----------------------- | ------------------------------------ |
| `DELETE FROM users;`    | löscht alle Zeilen                   |
| `TRUNCATE TABLE users;` | leert Tabelle schneller und direkter |

`TRUNCATE` ist eher für Admin- oder Testumgebungen relevant.

In echten Systemen sehr vorsichtig nutzen.

---

## DROP TABLE

`DROP TABLE` löscht die ganze Tabelle.

Beispiel:

```sql
DROP TABLE users;
```

Das löscht:

```text
Tabellenstruktur
Daten
Constraints
```

Unterschied:

| Befehl       | Wirkung                       |
| ------------ | ----------------------------- |
| `DELETE`     | löscht Daten, Tabelle bleibt  |
| `TRUNCATE`   | leert Tabelle, Tabelle bleibt |
| `DROP TABLE` | löscht Tabelle komplett       |

Für Lernprojekte okay. In echten Systemen nur mit sehr viel Vorsicht.

---

## ALTER TABLE

`ALTER TABLE` ändert die Struktur einer Tabelle.

Beispiel Spalte hinzufügen:

```sql
ALTER TABLE users
ADD COLUMN phone TEXT;
```

Beispiel Spalte entfernen:

```sql
ALTER TABLE users
DROP COLUMN phone;
```

Beispiel Spalte umbenennen:

```sql
ALTER TABLE users
RENAME COLUMN phone TO phone_number;
```

Je nach Datenbanksystem unterscheiden sich manche Details.

---

## Constraints hinzufügen

Constraints sichern Regeln in Tabellen ab.

Beispiel:

```sql
ALTER TABLE users
ADD CONSTRAINT unique_email UNIQUE (email);
```

Fremdschlüssel hinzufügen:

```sql
ALTER TABLE loans
ADD CONSTRAINT fk_loans_member
FOREIGN KEY (member_id) REFERENCES members(id);
```

Constraints geben der Datenbank klare Regeln.

Dadurch werden ungültige Daten früher verhindert.

---

## Constraints entfernen

Manchmal muss ein Constraint entfernt werden.

Beispiel:

```sql
ALTER TABLE users
DROP CONSTRAINT unique_email;
```

Das sollte man nur bewusst tun, weil dadurch Schutzregeln wegfallen.

Wenn ein Constraint entfernt wird, kann die Datenbank bestimmte Fehler nicht mehr verhindern.

---

## DEFAULT-Werte

Ein `DEFAULT`-Wert wird genutzt, wenn beim `INSERT` kein Wert angegeben wird.

Beispiel:

```sql
CREATE TABLE tickets (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  status TEXT DEFAULT 'open'
);
```

Insert:

```sql
INSERT INTO tickets (id, title)
VALUES (1, 'Netzwerkproblem');
```

Status wird automatisch:

```text
open
```

Das ist praktisch für Startwerte.

---

## CHECK-Constraints

`CHECK` prüft eine Bedingung.

Beispiel:

```sql
CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price DECIMAL CHECK (price >= 0)
);
```

Falsch:

```sql
INSERT INTO products (id, name, price)
VALUES (1, 'Monitor', -50);
```

Die Datenbank verhindert den negativen Preis.

Weitere Beispiele:

```sql
CHECK (age >= 0)
CHECK (stock >= 0)
CHECK (status IN ('open', 'closed', 'pending'))
```

---

## Transaktionen

Eine Transaktion fasst mehrere SQL-Befehle zusammen.

Beispiel:

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 100
WHERE id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE id = 2;

COMMIT;
```

Wenn alles funktioniert, speichert `COMMIT` die Änderungen.

Wenn etwas schiefgeht:

```sql
ROLLBACK;
```

Dann werden die Änderungen zurückgenommen.

---

## Warum Transaktionen wichtig sind

Transaktionen verhindern halbe Änderungen.

Beispiel Überweisung:

```text
Konto A verliert 100 Euro.
Konto B bekommt 100 Euro.
```

Beide Schritte müssen zusammen passieren.

Wenn nur der erste Schritt funktioniert und der zweite nicht, wären Daten falsch.

Deshalb nutzt man Transaktionen.

---

## ACID kurz erklärt

Datenbanken nutzen bei Transaktionen oft das ACID-Prinzip.

| Buchstabe | Bedeutung   | Erklärung                           |
| --------- | ----------- | ----------------------------------- |
| A         | Atomicity   | alles oder nichts                   |
| C         | Consistency | Daten bleiben gültig                |
| I         | Isolation   | Transaktionen stören sich nicht     |
| D         | Durability  | gespeicherte Daten bleiben erhalten |

Für den Einstieg reicht:

```text
Eine Transaktion soll Daten zuverlässig und vollständig ändern.
```

---

## COMMIT

`COMMIT` speichert Änderungen dauerhaft.

Beispiel:

```sql
BEGIN;

UPDATE users
SET email = 'neu@example.com'
WHERE id = 1;

COMMIT;
```

Nach `COMMIT` sind die Änderungen gespeichert.

---

## ROLLBACK

`ROLLBACK` nimmt Änderungen zurück.

Beispiel:

```sql
BEGIN;

UPDATE users
SET email = 'falsch@example.com'
WHERE id = 1;

ROLLBACK;
```

Die Änderung wird nicht dauerhaft übernommen.

Das ist sehr nützlich beim Testen von Änderungen.

---

## Vorsicht mit Produktivdaten

In echten Systemen muss man mit Datenänderungen sehr vorsichtig sein.

Vor Änderungen prüfen:

```text
Welche Tabelle ist betroffen?
Welche Datensätze sind betroffen?
Gibt es ein Backup?
Gibt es Fremdschlüssel?
Gibt es abhängige Daten?
Ist die WHERE-Bedingung korrekt?
Ist es ein Testsystem oder Produktivsystem?
```

Bei Unsicherheit:

```text
nicht ausführen
erst nachfragen
Backup prüfen
Änderung dokumentieren
```

---

## Datenänderungen dokumentieren

Bei wichtigen Datenänderungen sollte dokumentiert werden:

- was geändert wurde
- warum es geändert wurde
- wann es geändert wurde
- welche Tabelle betroffen war
- welche WHERE-Bedingung genutzt wurde
- ob ein Backup vorhanden war
- wer die Änderung durchgeführt hat

Das ist besonders wichtig in produktionsnahen Systemen.

---

## SQL-Dateien für Änderungen

Änderungen können in SQL-Dateien dokumentiert werden.

Beispiele:

```text
schema.sql
sample_data.sql
update_test_data.sql
migration_001.sql
```

Typische Inhalte:

| Datei             | Inhalt                    |
| ----------------- | ------------------------- |
| `schema.sql`      | Tabellenstruktur          |
| `sample_data.sql` | Beispieldaten             |
| `migration.sql`   | Strukturänderungen        |
| `cleanup.sql`     | kontrollierte Bereinigung |
| `queries.sql`     | Beispielabfragen          |

In Git-Projekten ist das sehr praktisch, weil Änderungen nachvollziehbar bleiben.

---

## Migrationen kurz erklärt

Eine Migration beschreibt eine kontrollierte Änderung an einer Datenbankstruktur.

Beispiel:

```sql
ALTER TABLE users
ADD COLUMN created_at DATE;
```

Migrationen werden genutzt, damit Datenbankänderungen nachvollziehbar und wiederholbar bleiben.

In größeren Projekten nutzt man dafür oft spezielle Tools.

Für Lernprojekte reicht es oft, SQL-Dateien sauber zu benennen und zu dokumentieren.

---

## Testdaten

Testdaten helfen beim Lernen und Prüfen.

Beispiel:

```sql
INSERT INTO users (id, name, email)
VALUES
  (1, 'Max', 'max@example.com'),
  (2, 'Lisa', 'lisa@example.com'),
  (3, 'Sara', 'sara@example.com');
```

Gute Testdaten sollten:

- nicht echt oder privat sein
- verschiedene Fälle abdecken
- verständliche Namen haben
- auch Sonderfälle enthalten
- keine echten Zugangsdaten enthalten

Beispiele für Sonderfälle:

```text
Benutzer ohne Telefonnummer
Ticket mit Status open
Ticket mit Status closed
Produkt mit Preis 0
Buch ohne Rückgabedatum
```

---

## Daten prüfen nach Änderungen

Nach einem `INSERT`, `UPDATE` oder `DELETE` sollte man prüfen.

Nach `INSERT`:

```sql
SELECT *
FROM users
WHERE id = 1;
```

Nach `UPDATE`:

```sql
SELECT *
FROM users
WHERE id = 1;
```

Nach `DELETE`:

```sql
SELECT *
FROM users
WHERE id = 1;
```

So sieht man, ob die Änderung wie erwartet funktioniert hat.

---

## Praktische Beispiele

### Beispiel 1: Benutzer einfügen

```sql
INSERT INTO users (id, name, email)
VALUES (1, 'Max Müller', 'max@example.com');
```

Prüfen:

```sql
SELECT *
FROM users
WHERE id = 1;
```

### Beispiel 2: E-Mail ändern

```sql
UPDATE users
SET email = 'max.neu@example.com'
WHERE id = 1;
```

Prüfen:

```sql
SELECT id, name, email
FROM users
WHERE id = 1;
```

### Beispiel 3: Ticket schließen

```sql
UPDATE tickets
SET status = 'closed'
WHERE id = 5;
```

Prüfen:

```sql
SELECT id, title, status
FROM tickets
WHERE id = 5;
```

### Beispiel 4: Datensatz löschen

```sql
DELETE FROM users
WHERE id = 1;
```

Prüfen:

```sql
SELECT *
FROM users
WHERE id = 1;
```

---

## Typische Fehler

| Fehler                                | Problem                            |
| ------------------------------------- | ---------------------------------- |
| `UPDATE` ohne `WHERE`                 | alle Datensätze werden geändert    |
| `DELETE` ohne `WHERE`                 | alle Datensätze werden gelöscht    |
| falsche ID im `WHERE`                 | falscher Datensatz betroffen       |
| Fremdschlüssel ignoriert              | Löschen oder Einfügen schlägt fehl |
| `NULL` falsch verwendet               | Daten werden falsch interpretiert  |
| echte Daten als Testdaten genutzt     | Datenschutzproblem                 |
| keine Prüfung nach Änderung           | Fehler bleibt unbemerkt            |
| kein Backup bei wichtigen Daten       | Wiederherstellung schwierig        |
| `DROP TABLE` mit `DELETE` verwechselt | ganze Tabelle gelöscht             |
| `CASCADE` nicht beachtet              | abhängige Daten werden mitgelöscht |

---

## Gute Arbeitsweise

Eine sichere Arbeitsweise:

1. Tabelle verstehen
2. betroffene Datensätze mit `SELECT` prüfen
3. `WHERE`-Bedingung genau kontrollieren
4. Änderung ausführen
5. Ergebnis mit `SELECT` prüfen
6. bei wichtigen Daten Transaktion nutzen
7. bei echten Systemen Backup und Freigabe beachten
8. Änderung dokumentieren
9. keine echten Zugangsdaten oder Kundendaten in Beispiele schreiben
10. SQL-Dateien sinnvoll versionieren

Wichtiger Ablauf:

```sql
SELECT *
FROM users
WHERE id = 1;

UPDATE users
SET email = 'neu@example.com'
WHERE id = 1;

SELECT *
FROM users
WHERE id = 1;
```

---
FIAE-Bezug
    • REST-APIs: Zuordnung von INSERT (POST), UPDATE (PUT/PATCH) und DELETE (DELETE). 
    • Transaktionen: Nutzung von ORM-Transaktionen (z. B. @Transactional). 
    • Migrationen: Versionierung von Schema-Änderungen über Flyway oder Alembic. 

## Kurze Zusammenfassung
DML verarbeitet Inhalte, DDL steuert die Struktur. Transaktionen sichern zusammengehörende Änderungen nach den ACID-Kriterien ab.


In der Praxis hilft dieses Wissen bei:

- Testdaten einfügen
- Datenbankprojekte prüfen
- Adminer oder psql nutzen
- einfache Korrekturen nachvollziehen
- Datenbankfehler verstehen
- Fremdschlüsselprobleme erkennen
- Docker-Datenbankumgebungen betreuen
- SQL-Dateien in Git-Projekten lesen
- Datenbankänderungen dokumentieren
- vorsichtig mit produktionsnahen Daten arbeiten


---

hbar und sauber dokumentiert werden sollten.
