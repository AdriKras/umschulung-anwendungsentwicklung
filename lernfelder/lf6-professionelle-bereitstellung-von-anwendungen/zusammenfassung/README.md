# LF 6.1 - Gesamtzusammenfassung: Service Desk, Arbeitsplatz und Dokumentation

Diese Zusammenfassung bündelt die Kernkonzepte der Module 6.1.1, 6.1.2 und 6.1.3 für die schnelle Wiederholung und Vorbereitung auf die Abschlussprüfung Teil 1 (AP1).

---

## Modul 6.1.1: Anfrageeingang, Qualifizierung und Service Desk Management

### 1. ITIL-Kernbegriffe
* **Störung (Incident):** Ungeplante Unterbrechung oder Qualitätsminderung eines IT-Services. *Ziel:* Schnelle Wiederherstellung des Betriebs.
* **Serviceanfrage (Service Request):** Formeller Antrag auf Bereitstellung, Information oder Standardänderung (z. B. Passwort-Reset, Zugangsrechte).
* **Problem:** Die unbekannte, zugrundeliegende Ursache einer oder mehrerer Störungen. *Ziel:* Dauerhafte Ursachenbehebung.
* **Behelfslösung (Workaround):** Vorübergehende Maßnahme zur Betriebsaufrechterhaltung bis zur Behebung der Ursache.

### 2. Qualifizierung & Priorisierung
* **W-Fragen:** Wer meldet? Was ist das Problem (Logs/Fehlermeldungen)? Wo tritt es auf (Umgebung/System)? Wann tritt es auf (Reproduzierbarkeit)?
* **Priorisierung:** 
  $$\text{Priorität} = \text{Auswirkung (Impact)} \times \text{Dringlichkeit (Urgency)}$$
  * **Auswirkung (Impact):** Maß für den Schadensumfang (Betroffene Nutzer / Geschäftsprozesse).
  * **Dringlichkeit (Urgency):** Zeitkritikalität bis zur Behebung.

### 3. Service Level Agreements (SLA)
* **SLA:** Vertrag über Dienstleistungen zwischen IT-Dienstleister und externem Kunden.
* **OLA (Operational Level Agreement):** Interne Vereinbarung zwischen IT-Abteilungen.
* **UC (Underpinning Contract):** Vertrag mit externen Drittherstellern/Lieferanten.
* **Metriken:** Reaktionszeit (Time to Respond) vs. Lösungszeit (Time to Resolve).

---

## Modul 6.1.2: Arbeitsplatzaufbau, Ergonomie und elektrische Sicherheit

### 1. Elektrische Sicherheit (DGUV V3 / VDE 0701-0702)
* **VDE-Sichtprüfung vor Inbetriebnahme:** Prüfung auf Gehäuseschäden, Isolationsmängel, defekte Zugentlastungen, verbogene Kontaktstifte oder Schmorerspuren.
* **Verhalten bei Mängeln:** Das Gerät darf nicht in Betrieb genommen werden, muss sofort gesperrt/gekennzeichnet und durch eine Elektrofachkraft geprüft werden.

### 2. Ergonomie am Bildschirmarbeitsplatz (ArbStättV)
* **Sehabstand:** 50 cm bis 70 cm zum Monitor.
* **Monitorhöhe:** Oberkante des Bildschirms maximal auf Augenhöhe (leicht gesenkter Blickwinkel).
* **Lichteinfall:** Blickrichtung parallel zur Fensterfront ausrichten, um Blendungen und Reflexionen zu vermeiden.

### 3. Verkabelung & Sicherheit
* **Trennung:** Physikalische Trennung von stromführenden Leitungen (230V) und Datenleitungen (EMV - Elektromagnetische Verträglichkeit).
* **Stolperfallen vermeiden (DGUV-Regel 108-007):** Kabelkanäle, Klettbinder und Wannen nutzen. Kabelsalat führt zu Verletzungsgefahren und Gerätestürzen.

---

## Modul 6.1.3: Dokumentation, CMDB und Übergabe

### 1. Configuration Management Database (CMDB)
* **Configuration Item (CI):** Jede verwaltete Komponente (Hardware, Softwarelizenz, Server, Benutzer).
* **Beziehungsgeflecht:** Speichert nicht nur das Objekt, sondern dessen Verknüpfungen (Nutzer, Service, Rechte).
* **Vermeidung von "Geister-Arbeitsmitteln":** Jede Hardware-Änderung muss in der CMDB nachgehalten werden, um Inventur- und Lizenzkonflikte zu vermeiden.

### 2. Rechtssichere Übergabe
* **Übergabeprotokoll:** Nachweis über Erhalt, Seriennummern und Zustand der Hardware.
* **Beweislastumkehr & Haftung:** Ab der Unterschrift haftet der Anwender bei grober Fahrlässigkeit. Oft verknüpft mit der Bestätigung der IT-Sicherheitsunterweisung.

### 3. Ticketabschluss & Lösungstext
* **Qualifizierter Lösungstext:** Präzise Beschreibung der durchgeführten Maßnahmen (welches Gerät/Seriennummer getauscht, Tests, CMDB-Update).
* **Wissensdatenbank (Knowledge Base):** Dient Kollegen zur schnelleren Lösungsfindung bei wiederkehrenden Problemen.

---

## FIAE-Spezifische Kernerkenntnisse

1. **Bug-Tracking vs. Change Request:** Klare Trennung zwischen echten Softwarefehlern (Incidents) und neuen Anforderungen (Feature Requests).
2. **Reproduzierbarkeit:** Vollständige Qualifizierung (Logs, Schritte, OS-Version) spart Entwicklungszeit bei der Fehlersuche.
3. **Commit- & Dokumentationsdisziplin:** Qualifizierte Lösungstexte in Tickets entsprechen präzisen Commit-Messages und Pull-Request-Beschreibungen im Entwickler-Alltag.
