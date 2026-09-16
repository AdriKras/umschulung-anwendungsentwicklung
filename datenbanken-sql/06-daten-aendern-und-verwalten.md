# 6. Daten ändern und verwalten

In diesem Kapitel geht es um die Manipulation und Verwaltung von Daten und Schemas in SQL aus Sicht der Anwendungsentwicklung.
In der Backend-Entwicklung reicht das reine Auslesen von Daten (DQL) nicht aus. Anwendungen verarbeiten Benutzereingaben, erstellen neue Ressourcen, aktualisieren Statuswerte und löschen veraltete Daten (DML). Darüber hinaus verändern sich Datenmodelle im Laufe des Anwendungs-Lebenszyklus ständig (DDL).
Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist das Beherrschen von INSERT, UPDATE, DELETE, Schema-Migrationen und Transaktionen essenziell, um die Datenintegrität der Anwendung zu garantieren und unbeabsichtigten Datenverlust zu verhindern.

---

## Kurz erklärt

Die Befehle zur Datenbearbeitung gehören zur DML (Data Manipulation Language):
* **INSERT:** Neue Datensätze anlegen (POST /api/users)
* **UPDATE:** Bestehende Datensätze ändern (PUT/PATCH /api/users/42)
* **DELETE:** Datensätze entfernen (DELETE /api/items/42)

**Entwickler-Grundregel:** Führe vor jedem UPDATE oder DELETE im Client immer zuerst das analoge SELECT mit derselben WHERE-Bedingung aus!

---

## 1. Daten einfügen (INSERT INTO)

```sql
INSERT INTO users (username, email, password_hash)
VALUES ('max_dev', 'max@example.com', 'hash123');
```

**Batch-Inserts:**
```sql
INSERT INTO categories (name, slug)
VALUES
  ('Software', 'software'),
  ('Hardware', 'hardware');
```

---

## 2. Daten aktualisieren (UPDATE)

```sql
UPDATE users
SET email = 'max.neu@example.com',
    updated_at = CURRENT_TIMESTAMP
WHERE id = 42;
```

---

## 3. Daten löschen (DELETE vs. Soft Delete)

**Hard Delete (Physikalisch):**
```sql
DELETE FROM sessions WHERE expires_at < NOW();
```

**Soft Delete (Best Practice im Backend):**
```sql
UPDATE users SET deleted_at = CURRENT_TIMESTAMP WHERE id = 42;
SELECT id, username FROM users WHERE deleted_at IS NULL;
```

---

## 4. Transaktionen & ACID

Eine Transaktion fasst mehrere Operationen atomar zusammen:

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

Tritt ein Fehler auf, schützt `ROLLBACK;` vor inkonsistenten Zuständen.

**ACID-Prinzip:**
* **Atomicity (Atomarität):** Ganz oder gar nicht.
* **Consistency (Konsistenz):** Regeln und Constraints bleiben gewahrt.
* **Isolation (Isolierung):** Parallele Transaktionen stören sich nicht.
* **Durability (Dauerhaftigkeit):** Speicherung ist nach COMMIT permanent.

---

## FIAE-Bezug

* **REST-APIs:** Zuordnung von INSERT (POST), UPDATE (PUT/PATCH) und DELETE (DELETE).
* **Transaktionen:** Nutzung von ORM-Transaktionen (z. B. `@Transactional`).
* **Migrationen:** Versionierung von Schema-Änderungen über Flyway oder Alembic.

---

## Kurze Zusammenfassung

DML verarbeitet Inhalte, DDL steuert die Struktur. Transaktionen sichern zusammengehörende Änderungen nach den ACID-Kriterien ab.
