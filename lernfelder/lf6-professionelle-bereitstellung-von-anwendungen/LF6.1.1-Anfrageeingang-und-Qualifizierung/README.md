# LF 6.1.1 – Anfrageeingang und Qualifizierung

*Quelle & Grundlagen: IT-Handbuch für Fachinformatiker*innen (Sascha Kersken, Rheinwerk Verlag)*

---

## 🎯 Lernziele
* Unterscheidung zwischen **Störung (Incident)** und **Serviceanfrage (Service Request)**.
* Zielgerichtete **Qualifizierung** von Meldungen mittels W-Fragen.
* Korrekte **Priorisierung** anhand von Auswirkung (*Impact*) und Dringlichkeit (*Urgency*).

---

## 🧠 Kernkonzepte (Kersken Basis)

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

## 💻 Relevanz für die Anwendungsentwicklung (FIAE)

1. **Bug-Reporting & Reproduzierbarkeit:** Unvollständige Tickets kosten Zeit. Qualifizierte W-Fragen liefern Logs, Screenshots und Umgebungsinfos.
2. **Fehler vs. Feature-Request:** Entwickler müssen unterscheiden, ob es ein Bug (Störung) oder ein neues Feature ist.
3. **Einhaltung von Critical-Bug-SLAs:** Produktionskritische Fehler benötigen sofortige Hotfixes.
4. **Feedback für die Software-Architektur:** Häufige Incidents in einem Bereich zeigen Refactoring-Bedarf auf.

---

## ⚠️ Typische Fallstricke in der Praxis

* **Versteckte Feature-Wünsche:** Anfragen als Fehler tarnen, um Bearbeitung zu beschleunigen.
* **Zuruf-Entwicklung vermeiden:** Änderungen am Ticket-System vorbei führen zu ungetesteten Versionen.
* **Prioritäten-Konflikt:** Wünsche von Führungskräften dürfen kritische Ausfälle nicht blockieren.
