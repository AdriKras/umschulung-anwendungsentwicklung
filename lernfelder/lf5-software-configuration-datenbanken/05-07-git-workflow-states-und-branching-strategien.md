# 05-07: LF 5.3 Git-Dateizustände, Core-CLI & Branching-Strategien

Dieses Modul behandelt die 3 Dateizustände in Git, die Kernbefehle zur lokalen und entfernten Synchronisation sowie den Vergleich gängiger Branching-Modelle (Trunk-based vs. Feature-Branching).

---

## 1. Die 3 Dateizustände (States) in Git

```text
[ Working Directory ]  --- git add --->  [ Staging Area (Index) ]  --- git commit --->  [ Local Repository (.git) ]
    (Modified)                                (Staged)                                    (Committed)
```

* **Modified (Geändert):** Dateiveränderungen im Arbeitsverzeichnis, die noch nicht für den nächsten Commit vorgemerkt sind.
* **Staged (Vorgemerkt):** Änderungen wurden markiert (`git add`) und für den nächsten Schnappschuss (Commit) in den Index gelegt.
* **Committed (Gespeichert):** Die Daten sind sicher in der lokalen Git-Datenbank (`.git/`) protokolliert.

---

## 2. Git CLI Core-Befehle

```bash
# Repository initialisieren & Status prüfen
git init
git status

# Änderungen vormerken & committen
git add .                          # Alle Änderungen in Staging Area legen
git commit -m "Feat: Add API login" # Lokalen Snapshot mit Nachricht erstellen

# Remote-Synchronisation
git remote add origin <URL>        # Entferntes Repository verknüpfen
git push origin main               # Lokale Commits auf Server hochladen
git pull --rebase origin main      # Server-Stand holen und lokale Commits oben aufsetzen
```

---

## 3. Branching-Strategien & Team-Workflows

Ein **Branch (Zweig)** ist ein beweglicher Zeiger auf einen spezifischen Commit. Er erlaubt isoliertes Arbeiten ohne den Haupt-Codebase zu gefährden.

| Kriterium | Feature-Branching / Git Flow | Trunk-Based Development |
| :--- | :--- | :--- |
| **Funktionsweise** | Für jedes Feature wird ein langlebiger Branch erstellt (`feature/login`, `release/v1.0`). | Alle Entwickler committen mehrmals täglich direkt auf den Hauptzweig (`main`/`trunk`) oder sehr kurzlebige Branches. |
| **Code Reviews** | Erfolgen über **Pull Requests (PRs)** / Merge Requests vor dem Mergen in den `main` Branch. | Automatisierte Tests (CI/CD) sichern die Stabilität; Reviews erfolgen post-commit oder via Pair Programming. |
| **Merge-Konflikte** | Höheres Risiko für komplexe Merge-Konflikte durch langlebige Branches. | Sehr geringes Konfliktrisiko durch ständige kleine Integrationen. |
| **Teamgröße** | Ideal für große Teams, Open-Source-Projekte und geregelte Release-Zyklen. | Ideal für erfahrene, agile Teams mit hoher CI/CD-Automatisierung. |

### Rolle von Pull Requests (PRs)
Ein **Pull Request (PR)** fordert das Team auf, den Code eines Feature-Branches zu überprüfen (**Code Review**), bevor dieser automatisiert über CI-Pipelines getestet und in den `main`-Branch gemergt wird.

---

## FIAE-Zusammenfassung
Entwickler steuern Git versiert über das Terminal, nutzen Staging-Areas für atomare Commits und wählen passende Branching-Strategien (z. B. Feature-Branching mit Pull Requests), um die Code-Qualität im Team zu sichern.
