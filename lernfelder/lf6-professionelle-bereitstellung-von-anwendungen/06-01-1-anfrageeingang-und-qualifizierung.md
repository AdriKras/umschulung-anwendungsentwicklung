# LF 6.1.1 - Anfrageeingang, Qualifizierung und Service Desk Management

## 1. Übersicht und Einordnung

Im Rahmen des IT-Service-Managements (nach ITIL) ist der Service Desk die zentrale Schnittstelle (Single Point of Contact - SPOC) zwischen Anwendern, Kunden und der IT-Abteilung. Für die Softwareentwicklung (FIAE) ist eine präzise Qualifizierung von Anfragen essenziell, um Fehlerberichte (Bug-Reports) von neuen Anforderungen (Feature Requests) zu trennen und Entwicklungsressourcen effizient zu steuern.

---

## 2. ITIL-Kernbegriffe (AP1-relevantes Basiswissen)

### Störung (Incident)
* **Definition:** Eine ungeplante Unterbrechung oder Qualitätsminderung eines IT-Services.
* **Beispiel:** Die Datenbankverbindung der Anwendung bricht bei der Verarbeitung von Zahlungen ab.
* **Primärziel:** Schnellstmögliche Wiederherstellung des normalen Servicebetriebs (ggf. auch über vorübergehende Behelfslösungen).

### Serviceanfrage (Service Request)
* **Definition:** Eine formelle Anfrage eines Anwenders nach der Bereitstellung von Informationen, Beratung oder Zugängen im Rahmen vorgegebener Standardabläufe.
* **Beispiel:** Anforderung von API-Zugangsdaten für die Testumgebung oder Einrichtung eines neuen Entwickler-Accounts.

### Problem
* **Definition:** Die unbekannte, zugrundeliegende Ursache einer oder mehrerer Störungen.
* **Beispiel:** Wiederholte Anwendungsabstürze aufgrund eines unbekannten Speicherlecks (Memory Leak).
* **Ziel:** Identifikation und Behebung der Ursache (Problem Management).

### Behelfslösung (Workaround)
* **Definition:** Eine temporäre Maßnahme zur Wiederherstellung des Servicebetriebs, solange die eigentliche Ursache (Problem) noch nicht behoben ist.

---

## 3. Qualifizierung und Ticket-Bearbeitung

### Qualifizierung über W-Fragen
Beim Eingang einer Meldung müssen folgende Informationen vollständig erfasst werden:
* **Wer:** Identifikation des Melders und der betroffenen Benutzergruppe.
* **Was:** Exakte Beschreibung des Verhaltens inklusive Fehlermeldungen, System-Logs und Screenshots.
* **Wo:** Identifikation der betroffenen Umgebung (Lokale Entwicklung, Testserver, Staging, Produktion).
* **Wann:** Zeitpunkt des ersten Auftretens sowie Schritte zur exakten Reproduktion des Fehlers.

### Klassifizierung und Priorisierung
Die Klassifizierung dient der Zuweisung des Tickets an das zuständige Entwicklungsteam (z. B. Backend, Frontend, Datenbank). Die Priorität bestimmt die Reihenfolge der Bearbeitung und berechnet sich wie folgt:

$$\text{Priorität} = \text{Auswirkung (Impact)} \times \text{Dringlichkeit (Urgency)}$$

* **Auswirkung (Impact):** Maß für den finanziellen, betrieblichen oder personellen Schaden (z. B. Ausfall des gesamten Online-Shops vs. Darstellungsfehler auf einem Einzelarbeitsplatz).
* **Dringlichkeit (Urgency):** Maß dafür, wie schnell eine Lösung zur Vermeidung weiterer Schäden vorliegen muss (z. B. bevorstehender Monatsabschluss).

---

## 4. Service Level Agreements (SLA)

### Vertragsarten im Service Management
* **SLA (Service Level Agreement):** Vereinbarung über IT-Dienstleistungen zwischen IT-Service-Erbringer und externem Kunden.
* **OLA (Operational Level Agreement):** Interne Vereinbarung zwischen verschiedenen IT-Teams desselben Unternehmens (z. B. zwischen Support und Anwendungsentwicklung).
* **UC (Underpinning Contract):** Vertrag mit externen Drittherstellern oder Lieferanten (z. B. Cloud-Anbieter, Datenbank-Lizenzgeber).

### Relevante Kennzahlen
* **Reaktionszeit (Time to Respond):** Zeitspanne von der Ticketerstellung bis zur ersten qualifizierten Bearbeitung.
* **Lösungszeit (Time to Resolve):** Zeitspanne von der Ticketerstellung bis zur vollständigen Behebung oder Bereitstellung eines Workarounds.

---

## 5. Bedeutung für die Anwendungsentwicklung (FIAE)

* **Effizientes Bug-Tracking:** Vollständige Qualifizierungsdaten reduzieren Rückfragen und ermöglichen eine unmittelbare Fehleranalyse im Code.
* **Unterscheidung von Bug und Change Request:** Verhindert, dass neue Funktionswünsche fälschlicherweise als kostenfreie Fehlerbehebung deklariert werden.
* **SLA-Einhaltung bei Hotfixes:** Kritische Fehler in der Produktion erfordern die sofortige Bereitstellung von Patches im Rahmen vertraglicher Lösungszeiten.
* **Identifikation von Code-Schulden (Technical Debt):** Häufig auftretende Incidents in einem Modul signalisieren die Notwendigkeit von Refactoring.

## 💻 Relevanz für die Anwendungsentwicklung (FIAE)

1. **Bug-Reporting & Reproduzierbarkeit:** Unvollständige Tickets kosten Zeit. Qualifizierte W-Fragen liefern Logs, Screenshots und Umgebungsinfos.
2. **Fehler vs. Feature-Request:** Entwickler müssen unterscheiden, ob es ein Bug (Störung) oder ein neues Feature ist.
3. **Einhaltung von Critical-Bug-SLAs:** Produktionskritische Fehler benötigen sofortige Hotfixes.
4. **Feedback für die Software-Architektur:** Häufige Incidents in einem Bereich zeigen Refactoring-Bedarf auf.

