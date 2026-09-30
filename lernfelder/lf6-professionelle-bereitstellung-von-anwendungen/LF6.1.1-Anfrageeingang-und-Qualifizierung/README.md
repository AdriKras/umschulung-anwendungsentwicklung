# LF 6.1.1 – Anfrageeingang und Qualifizierung
*Quelle & Grundlagen: IT-Handbuch für Fachinformatiker*innen (Sascha Kersken, Rheinwerk Verlag)*


## Kernkonzepte (Kersken Basis)

### 1. Störung vs. Serviceanfrage (ITIL)
* **Störung (Incident):** Ungeplante Unterbrechung oder Qualitätsminderung eines IT-Services (*"Die App stürzt beim Klick auf Speichern ab"*). 
  * *Ziel:* Schnellstmögliche Wiederherstellung der Funktion.
* **Serviceanfrage (Service Request):** Antrag auf Bereitstellung, Information oder Standardänderung (*"Ich benötige API-Zugangsdaten für die Testumgebung"*).
  * *Ziel:* Standardisierte und effiziente Abwicklung.

### 2. Qualifizierung & W-Fragen
Damit ein Ticket bzw. Bug-Report verarbeitet werden kann, müssen beim Anfrageeingang wesentliche Informationen vorliegen:
* **Wer** meldet das Problem / wer ist betroffen?
* **Was** genau ist das Problem (Fehlermeldung, Log-Auszug)?
* **Wo** tritt es auf (Entwicklungsumgebung, Staging, Produktion, OS-Version)?
* **Wann** / unter welchen Bedingungen tritt der Fehler auf (Schritte zur Reproduktion)?

### 3. Klassifizierung & Priorisierung
* **Klassifizierung:** Einordnung in Kategorien (z. B. *Backend > Datenbank > Timeout*), zur Zuweisung an das richtige Entwickler-Team.
* **Priorisierung:** 
  $$\text{Priorität} = \text{Auswirkung (Impact)} \times \text{Dringlichkeit (Urgency)}$$
  * **Auswirkung (Impact):** Betrifft es das gesamte Abrechnungssystem oder nur eine seltene UI-Farbabweichung?
  * **Dringlichkeit (Urgency):** Steht der Release-Termin unmittelbar bevor?

### 4. Service Level Agreements (SLA)
* **Reaktionszeit:** Zeitspanne bis zur ersten Rückmeldung / ersten Diagnose.
* **Lösungszeit / Fix-Time:** Zeitspanne bis zum Einspielen eines Patches oder Hotfixes.

---

## Relevanz für die Anwendungsentwicklung (FIAE)

Warum ist Anfrageeingang und Qualifizierung für Softwareentwickler*innen wichtig?

1. **Bug-Reporting & Reproduzierbarkeit:**
   * Unvollständige Tickets (*"Das Programm geht nicht"*) kosten wertvolle Entwicklungszeit. Qualifizierte W-Fragen liefern **Logs, Screenshots, Schritte zur Reproduktion** und die exakte **Laufzeitumgebung**.

2. **Fehler-Klassifizierung vs. Feature-Request:**
   * Ein unerwartetes Verhalten kann ein **Bug (Störung)** sein oder eine **unvollständige Anforderung (Service Request / Feature Request)**. Entwickler müssen dies unterscheiden, um Aufwände und Sprints richtig zu planen.

3. **Einhaltung von Critical-Bug-SLAs (DevOps & Support):**
   * Produktionskritische Fehler (z. B. Absturz der Checkout-Seite eines Online-Shops) unterliegen strengen SLA-Lösungszeiten. Entwickler müssen die Priorisierung verstehen, um **Hotfixes direkt freizugeben**, während kleine Schönheitsfehler im normalen Backlog verbleiben.

4. **Feedback für die Software-Architektur:**
   * Häufen sich Incident-Tickets in einer bestimmten Kategorie (z. B. *Datenbank-Timeouts*), ist das für Entwickler das Signal für ein tieferliegendes Architektur-Problem (Refactoring-Bedarf).

---

## Typische Fallstricke in der Praxis

* **Versteckte Feature-Wünsche:** Nutzer melden fehlende Funktionen oft als *"Fehler/Störung"*, um eine schnellere Bearbeitung zu erzwingen.
* **Zuruf-Entwicklung vermeiden:** Code-Änderungen auf Zuruf im Flur am Ticket-System vorbei führen zu ungetesteten Versionen, fehlender Dokumentation und unklaren Code-Releases.
* **Prioritäten-Konflikt:** Die Bitte von Führungskräften um kleine Anpassungen darf nicht die Behebung kritischer Systemausfälle in der Produktion blockieren.
