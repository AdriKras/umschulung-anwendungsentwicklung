# 05-08: LF 5.4 Programmierparadigmen, Bash-Automatisierung & Python-Syntax

Dieses Modul behandelt die Einordnung moderner Programmiersprachen und -paradigmen (prozedural, OOP, funktional), das Schreiben von Bash-Automatisierungsskripten sowie die Syntax-Grundlagen von Python (Einrückung, Kontrollstrukturen).

---

## 1. Top-Programmiersprachen & Paradigmen im Vergleich

| Paradigma | Kernkonzept / Philosophie | Typische Sprachen | FIAE-Einsatzbereich |
| :--- | :--- | :--- | :--- |
| **Prozedural / Imperativ** | Schritt-für-Schritt-Anweisungen, Prozeduren/Funktionen verändern Zustand. | C, Bash, Go | Systemnahe Programmierung, CLI-Tools, Automatisierungs-Skripte. |
| **Objektorientiert (OOP)** | Kapselung von Daten (Attribute) und Verhalten (Methoden) in Objekten. | Java, C#, C++, Python | Enterprise-Backends, große Softwaresysteme, GUI-Anwendungen. |
| **Funktional** | Immutabilität (Unveränderlichkeit), keine Seiteneffekte, Functions als First-Class-Citizens. | Haskell, Elixir, Scala, JS/TS (multi) | Datenverarbeitung, Concurrent Programming, Reaktive UIs (React). |

---

## 2. Bash-Automatisierungsskripte unter Linux

### Der Shebang (`#!`)
Die erste Zeile eines Skripts (`#!/bin/bash` oder `#!/usr/bin/usr/env bash`) gibt dem Betriebssystem an, welcher Interpreter zur Ausführung der Datei genutzt werden muss.

### Beispiel: Automatisches Setup-Skript
```bash
#!/bin/bash
# Setup-Skript fuer Entwicklungs-Umgebung
PROJECT_NAME="my_app"

echo "Starte Setup fuer $PROJECT_NAME..."
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME" || exit

python3 -m venv venv
echo "Virtuelle Umgebung erstellt."
```

### Ausführrechte vergeben (Linux CLI)
```bash
chmod +x setup.sh   # Vergibt Ausfuehrrechte (Execution Bits)
./setup.sh          # Skript manuell ausfuehren
```

---

## 3. Python-Syntax: Einrückung & Kontrollstrukturen

Im Gegensatz zu C-basierten Sprachen (Java, C++, JS), die geschweifte Klammern (`{}`) nutzen, verwendet Python **strikte Einrückungen (Indentation, standardmäßig 4 Leerzeichen)** zur Definition von Code-Blöcken.

```python
# Kontrollstrukturen und Schleifen
user_role = "admin"
active_users = ["Alice", "Bob", "Charlie"]

if user_role == "admin":
    print("Zugriff gewaehrt: Admin-Bereich")
    for user in active_users:
        print(f"Pruefe Status fuer: {user}")
else:
    print("Zugriff verweigert")
```

---

## FIAE-Zusammenfassung
Entwickler wählen das passende Paradigma für ihr System (z. B. OOP für Business-Logik, Prozedural für Bash-Automatisierung) und achten in Python strikt auf PEP-8-Einrückungskonventionen.
