# 5. Joins und Beziehungen

In diesem Kapitel geht es um die Verknüpfung von Daten aus mehreren Tabellen mittels **Joins** aus Sicht der Softwareentwicklung.

In der Anwendungsentwicklung werden Datenmodelle bewusst in mehrere normalisierte Tabellen aufgeteilt (Separation of Concerns). Um im Backend zusammengesetzte Objekte (z. B. eine Bestellung inklusive Kundendaten und Bestellpositionen) für das Frontend aufzubereiten, müssen diese Daten über SQL-Joins performant zusammengeführt werden.

Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist das Verständnis von Joins essenziell, um komplexe Data Transfer Objects (DTOs) zu befüllen, ORM-Abfragen (wie SQLAlchemy oder Entity Framework) zu durchschauen und Performanz-Probleme wie das berichtigte **N+1 Query-Problem** zu vermeiden.

---

## Kurz erklärt

Ein Join kombiniert Daten aus zwei oder mehreren Tabellen basierend auf einer logischen Beziehung (meist **Primary Key <-> Foreign Key**).

**Beispiel aus dem Backend:**
Ein `Order`-Objekt im Anwendungscode benötigt den Kundennamen aus `users` und die Lieferadresse aus `addresses`.

```sql
SELECT orders.id, users.username, addresses.street
FROM orders
INNER JOIN users ON orders.user_id = users.id
INNER JOIN addresses ON orders.address_id = addresses.id;
```

---

## Die 4 wichtigsten Join-Typen im Überblick

| Join-Typ | Verhalten | Typischer Anwendungsfall im Backend |
| :--- | :--- | :--- |
| **`INNER JOIN`** | Gibt nur Datensätze zurück, die in **beiden** Tabellen einen Treffer haben. | Standard-Fetch: Nur Bestellungen anzeigen, die einem gültigen User zugeordnet sind. |
| **`LEFT JOIN`** | Gibt **alle** Datensätze der linken Tabelle zurück, auch wenn in der rechten kein Treffer existiert (`NULL`). | User-Listen inklusive optionaler Daten (z. B. User anzeigen, auch wenn sie noch kein Profil erstellt haben). |
| **`RIGHT JOIN`** | Gibt **alle** Datensätze der rechten Tabelle zurück (selten genutzt, da durch `LEFT JOIN` ersetzbar). | Wird in der Praxis meist vermieden und durch Umstellen der Tabellenreihenfolge als `LEFT JOIN` geschrieben. |
| **`FULL OUTER JOIN`** | Gibt alle Datensätze beider Tabellen zurück; nicht passende Seiten werden mit `NULL` aufgefüllt. | Daten-Audits und Abgleich zweier Datensätze auf Vollständigkeit. |

---

## 1. INNER JOIN (Der Standard-Join)

Ein `INNER JOIN` filtert alle Datensätze heraus, die keine Entsprechung in der verknüpften Tabelle besitzen.

```sql
SELECT u.username, p.title
FROM users AS u
INNER JOIN posts AS p ON u.id = p.author_id;
```
*Ergebnis:* Es werden nur User angezeigt, die bereits mindestens einen Post verfasst haben. User ohne Posts werden komplett ignoriert.

---

## 2. LEFT JOIN (Left Outer Join)

Ein `LEFT JOIN` sorgt dafür, dass die "Haupt-Entität" (links vom Join) **immer** im Ergebnis enthalten bleibt. Fehlen verknüpfte Daten auf der rechten Seite, werden die Spalten mit `NULL` aufgefüllt.

```sql
SELECT u.username, p.title
FROM users AS u
LEFT JOIN posts AS p ON u.id = p.author_id;
```
*Ergebnis:* Alle User werden aufgelistet. Hat ein User keine Posts geschrieben, erscheint sein `username`, während bei `title` der Wert `NULL` steht.

### Nicht-verknüpfte Daten finden
Ein mächtiges Muster in der Softwareentwicklung, um inaktive Objekte oder verwaiste Daten zu ermitteln:

```sql
-- Erleichtert das Finden von Usern, die noch NIE eine Bestellung getätigt haben
SELECT u.id, u.email
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
WHERE o.id IS NULL;
```

---

## 3. Joins bei n:m-Beziehungen (Zwischentabellen)

Da n:m-Beziehungen (z. B. `Studenten` <-> `Kurse`) über eine Zwischentabelle gelöst werden, sind mindestens **zwei Joins** nötig, um die Echtdaten miteinander zu verbinden:

```sql
SELECT s.first_name, c.title
FROM students AS s
INNER JOIN student_courses AS sc ON s.id = sc.student_id
INNER JOIN courses AS c ON sc.course_id = c.id
WHERE c.is_active = true;
```

---

## 4. Self Join (Tabellen mit sich selbst verbinden)

Ein Self Join wird verwendet, wenn eine Entität eine Hierarchie innerhalb derselben Tabelle abbildet (z. B. Mitarbeiter & Vorgesetzte).

```sql
SELECT 
  e.name AS employee_name, 
  m.name AS manager_name
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.id;
```

---


Das **N+1 Query-Problem** ist einer der häufigsten Performance-Killer in Backend-Anwendungen, die Object-Relational Mapper (ORMs) nutzen.

### Wie das Problem entsteht (Pseudocode):
```python
# 1 Query holt 100 Bestellungen
orders = db.query("SELECT * FROM orders LIMIT 100")

for order in orders:
    user = db.query("SELECT * FROM users WHERE id = %s", order.user_id)
```
*Folge:* Es werden 1 + 100 = 101 Datenbank-Queries ausgeführt! Das bringt die Datenbank unter Last zum Absturz.

### Die Lösung: Ein einziger sauberer SQL-Join
```sql
SELECT o.id, o.amount, u.username, u.email
FROM orders AS o
INNER JOIN users AS u ON o.user_id = u.id
LIMIT 100;
```
*Folge:* **1 einzige Abfrage** holt alle benötigten Daten auf einmal!

---

## Performance-Optimierung bei Joins

* **Indizes auf Fremdschlüsseln:** Jede Spalte in einer `ON`-Bedingung **muss** in der Datenbank indiziert sein (`INDEX`).
* **Selektive Spaltenwahl:** Nutze niemals `SELECT *` bei Joins!
* **Typengleichheit:** Die Datentypen der verknüpften Spalten müssen exakt übereinstimmen.

---

## Typische Fehler bei Entwicklern

* **Fehlende `ON`-Bedingung (CROSS JOIN):** Erzeugt ungewollte kartesische Produkte.
* **Unklare Aliase:** Verwende kurze, verständliche Kürzel (`usr`, `ord`, `itm`).
* **`LEFT JOIN` durch `WHERE` zerstört:** Ungewollte Umwandlung in einen `INNER JOIN`.

---

## FIAE-Bezug

Für Anwendungsentwickler sind Joins das tägliche Brot:
* **API-Entwicklung:** Effizientes Zusammenbauen von JSON-Payloads.
* **ORM-Verständnis:** Eager Loading (Joins) statt Lazy Loading einsetzen.
* **Backend-Performance:** Vermeiden von unnötigen Datenbank-Roundtrips.

---

## Kurze Zusammenfassung

SQL-Joins führen Daten aus verschiedenen Tabellen zusammen. **`INNER JOIN`** filtert auf exakte Treffer, **`LEFT JOIN`** behält alle Datensätze der Haupt-Tabelle bei. Entwickler nutzen Joins gezielt, um das N+1 Query-Problem zu verhindern.
