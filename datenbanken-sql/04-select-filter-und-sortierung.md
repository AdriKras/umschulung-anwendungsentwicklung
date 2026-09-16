# 4. SELECT, Filter und Sortierung

In diesem Kapitel geht es um den zentralen Befehl zur Datenabfrage in SQL: `SELECT`, kombiniert mit Filter- und Sortiermethoden aus Sicht der Softwareentwicklung.

`SELECT` ist das Herzstück der Data Query Language (DQL). In der Backend-Entwicklung verbringen Entwickler die meiste Zeit damit, gezielte Abfragen zu schreiben, um exakt die benötigten Daten für das Frontend oder die Geschäftslogik aus der Datenbank zu laden.

Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist das Beherrschen von `SELECT`, Filtern, Pagination und Aggregationen essenziell, um performanten Code zu schreiben, Netzwerk-Overhead zu minimieren und Datenbank-Ressourcen zu schonen.

---

## Kurz erklärt

Mit `SELECT` fragt man Daten aus einer oder mehreren Tabellen ab.

**Einfaches Beispiel:**

```sql
SELECT *
FROM users;
```

Im Produktionscode wird `SELECT *` jedoch vermieden. Stattdessen werden Spalten explizit selektiert.

**Bausteine einer DQL-Abfrage:**

* `FROM`: Gibt die Quell-Tabelle an.
* `WHERE`: Filtert Zeilen nach logischen Bedingungen.
* `ORDER BY`: Sortiert das Ergebnis auf- oder absteigend.
* `LIMIT` / `OFFSET`: Begrenzt die Trefferanzahl (Pagination / Seitenanzeige).
* `DISTINCT`: Entfernt Duplikate aus der Ergebnismenge.
* `LIKE` / `ILIKE`: Sucht nach Textmustern (Wildcards).
* `IN`: Prüft gegen eine Werteliste.
* `BETWEEN`: Filtert nach Wertebereichen.
* `IS NULL`: Filtert nach fehlenden Werten.

---

## Grundaufbau von SELECT im Backend-Code

Ein typisches SQL-Query für ein API-Endpunkt-Backend sieht so aus:

```sql
SELECT id, username, email, created_at
FROM users
WHERE is_active = true AND role = 'customer'
ORDER BY created_at DESC
LIMIT 20 OFFSET 0;
```

---

## Das SELECT * Anti-Pattern in der Softwareentwicklung

In SQL-Clients (z. B. DBeaver, Adminer) ist `SELECT *` für einen schnellen Überblick nützlich. In Produktiv-Apps bringt es gravierende Nachteile:

* **Performance & Speicher:** Unnötige Spalten werden über das Netzwerk übertragen.
* **Datenschutz:** Sensible Felder wie Passwort-Hashes könnten versehentlich an das Frontend durchgereicht werden.
* **Breaking Changes:** Verändert sich das Schema, bricht eventuell das Mapping im ORM.

---

## Pagination: LIMIT & OFFSET

In modernen Webanwendungen werden Ergebnisse in Seiten unterteilt (*Pagination*).

```sql
-- Seite 1 (Einträge 1 bis 10)
SELECT id, title FROM articles ORDER BY id ASC LIMIT 10 OFFSET 0;

-- Seite 2 (Einträge 11 bis 20)
SELECT id, title FROM articles ORDER BY id ASC LIMIT 10 OFFSET 10;
```

---

## FIAE-Bezug

* **Backend-Performance:** Minimieren der Datenlast zwischen DB-Server und Backend.
* **REST-API Pagination:** Implementierung von sortierten und paginierten Listen-Endpunkten.
* **Business-Logic & Reporting:** Erstellen korrekter Auswertungen mit `GROUP BY` und Aggregaten.

---

## Kurze Zusammenfassung

`SELECT` fragt Spalten ab, `WHERE` filtert Zeilen, `ORDER BY` sortiert und `LIMIT`/`OFFSET` steuern die Paginierung.
