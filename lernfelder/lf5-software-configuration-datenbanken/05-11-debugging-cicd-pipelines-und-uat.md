# 05-11: LF 5.5 Debugging-Techniken, CI/CD-Pipelines & User Acceptance Test (UAT)

Dieses Modul behandelt professionelles Debugging (Breakpoints, Steuerung), den Aufbau von CI/CD-Pipelines (Linter, Pipeline-Vorteile) sowie die formale Abnahme im User Acceptance Test (UAT).

---

## 1. Debugging: Breakpoints vs. Print-Debugging

| Kriterium | Print-Statements (`print()`, `console.log`) | Professioneller Debugger (IDE) |
| :--- | :--- | :--- |
| **Ablauf** | Manuelles Einfügen und Löschen von Log-Ausgaben im Code. | Haltepunkte (**Breakpoints**) im laufenden Prozess setzen. |
| **Code-Sauberkeit** | Risiko: Vergesse Log-Meldungen im Produktivcode. | **Keine Code-Änderung erforderlich.** |
| **Zustandsanalyse** | Zeigt nur festgelegte Variablen zum Zeitpunkt der Ausgabe. | Inspect aller Variablen, Call-Stacks und Speicherstände in Echtzeit. |

### Grundbegriffe der Debugger-Steuerung
* **Breakpoint:** Hält die Programmausführung an einer bestimmten Zeile an.
* **Step Over (F8):** Führt die aktuelle Zeile aus und springt zur nächsten (überspringt das Innere von Funktionsaufrufen).
* **Step Into (F7):** Springt in die in der aktuellen Zeile aufgerufene Funktion hinein.
* **Step Out (Shift+F8):** Führt den Rest der aktuellen Funktion aus und springt zurück zum Aufrufer.

---

## 2. Continuous Integration (CI) & Continuous Delivery/Deployment (CD)

* **CI (Continuous Integration):** Entwickler mergen ihren Code regelmäßig. Jeder Push löst automatische Builds, Linter und Tests aus.
* **CD (Continuous Delivery):** Der geprüfte Code wird automatisch für das Deployment auf eine Staging-Umgebung vorbereitet.
* **CD (Continuous Deployment):** Jede erfolgreiche Änderung wird automatisch direkt in die Produktion eingespielt.

### Die Rolle von Lintern in der Pipeline
Ein **Linter** (z. B. `flake8` für Python, `ESLint` für JS) analysiert den Quellcode statisch auf Syntaxfehler, Code-Smells und Style-Verstöße (z. B. PEP 8), **ohne den Code auszuführen**.

```yaml
# Beispiel: GitHub Actions Pipeline (.github/workflows/ci.yml)
name: CI Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Linter ausfuehren
        run: flake8 .
      - name: Tests ausfuehren
        run: pytest
```

---

## 3. User Acceptance Test (UAT) & Abnahmeprotokoll

| Kriterium | System-Test | User Acceptance Test (UAT / Abnahmetest) |
| :--- | :--- | :--- |
| **Ziel** | Technische Korrektheit & Vollständigkeit prüfen. | Geschäftliche Validierung: "Erfüllt die Software den Geschäftszweck?" |
| **Tester** | QA-Team / Entwickler. | **Endanwender, Kunde oder Fachbereich.** |
| **Umgebung** | Test- / Staging-Umgebung. | Produktionsnahe UAT-Umgebung mit Realdaten-Szenarien. |

### Wichtigkeit des formalen Abnahmeprotokolls
Das **Abnahmeprotokoll** ist das juristisch und kaufmännisch entscheidende Dokument am Ende eines Projekts:
* **Gefahrenübergang:** Das Risiko geht vom Auftragnehmer auf den Auftraggeber über.
* **Zahlungsauslösung:** Mit der formalen Unterzeichnung wird die Schlussrechnung fällig.
* **Beweislastumkehr:** Ab der Unterzeichnung muss der Kunde Mängel beweisen (Zuvor musste der Auftragnehmer die Mängelfreiheit beweisen).

---

## FIAE-Zusammenfassung
Entwickler nutzen Breakpoints zur schnellen Fehlersuche, richten Linter und automatisierte Tests in CI-Pipelines ein und sichern den Projekterfolg durch Vorbereitung der UAT-Tests für das finale Abnahmeprotokoll.
