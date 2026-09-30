# LF 6: Serviceanfragen und IT-Service-Management (ITSM)

---

## Epic User Story
Als IT-Service-Team
möchten wir eine Hardware-Serviceanfrage von der ersten Meldung über die physische Bereitstellung bis zum formalen Abschluss bearbeiten,
damit der Prozess transparent, sicher (nach VDE/DGUV V3) und standardisiert abläuft.

---

## Kernkompetenzen (Celebration Criteria)
* Ticket-Lebenszyklus: Beherrschung der Phasen Annahme, Qualifizierung, Bearbeitung und Abschluss.
* Klassifizierung & Priorisierung: Sicheres Unterscheiden zwischen Serviceanfragen (Service Requests) und Störungen (Incidents) sowie Priorisierung nach SLA-Vorgaben.
* Ergonomie & Arbeitsschutz: Ergonomischer Aufbau von Arbeitsplätzen (gemäß BildscharbV / Arbeitsstättenverordnung) und Durchführung von Sicherheitsprüfungen (VDE 0701-0702 / DGUV Vorschrift 3).
* Revisionssichere Dokumentation: Pflege der Bestandsdatenbank (CMDB) und rechtssichere Übergabe mittels Abnahmeprotokoll.

---

## Die 5 Schlüsselrollen im Prozess ("Der Anfrage-Marathon")

[1. Koordinator (Service Desk)] --> [2. Hardware-Techniker] --> [3. Bestandsverwalter]
                                                                        |
[5. Vor-Ort-Techniker (Abnahme)] <-- [4. Dokumentationsverantwortlicher] <--'

1. Koordinator (Service Desk):
   * First-Level-Support: Entgegennahme des Erstkontakts (Telefon/Portal).
   * Erstellung und Erstqualifizierung des Tickets.
   * Prüfung von Service Level Agreements (SLAs) und Zuweisung an die zuständige Fachgruppe (Second-Level).
2. Hardware-Techniker:
   * Durchführung der VDE-Sichtprüfung (Kabel, Stecker, Gehäuse auf Beschädigungen).
   * Physischer und ergonomischer Aufbau des Arbeitsplatzes (Blickrichtung, Monitorabstand, Kabelmanagement).
3. Bestandsverwalter (Asset / Configuration Management):
   * Inventarisierung und Kennzeichnung von Hardware (z. B. via Barcode/Asset-Tag).
   * Erfassung und Aktualisierung der Configuration Items (CIs) in der CMDB / Bestandsdatenbank.
4. Dokumentationsverantwortlicher:
   * Erstellung des rechtssicheren Übergabeprotokolls.
   * Sicherstellung der Ticket-Qualität (nachvollziehbarer Lösungstext für die Knowledge Base).
5. Vor-Ort-Techniker (Übergabe & Abnahme):
   * Einweisung der Endanwenderin bzw. des Endanwenders vor Ort.
   * Einholen der formalen Abnahme (Unterschrift/Protokoll) und finale Schließung des Tickets.

---

## Fachliche Grundlagen (aus dem IT-Handbuch von Sascha Kersken)

### 1. Unterschied: Incident vs. Service Request (ITIL)
* Incident (Störung): Ungeplante Unterbrechung oder Qualitätsminderung eines IT-Services (z. B. "Bildschirm bleibt schwarz" oder "Datenbank offline"). Ziel: Schnellstmögliche Wiederherstellung des Normalbetriebs.
* Service Request (Serviceanfrage): Formelle Anfrage eines Benutzers nach etwas, das bereitgestellt werden soll (z. B. "Einrichtung eines neuen Arbeitsplatzes", "Passwort-Reset" oder "Software-Installation").

### 2. SLA, OLA und UC
* SLA (Service Level Agreement): Vereinbarung über die Dienstgüte (Reaktions- und Lösungszeiten) zwischen IT-Dienstleister und Kunde.
* OLA (Operational Level Agreement): Interne Vereinbarung zwischen IT-Abteilungen zur Einhaltung des SLAs.
* UC (Underpinning Contract): Vertrag mit externen Zulieferern/Dienstleistern.

### 3. Vorschriften beim Arbeitsplatzaufbau
* Ergonomie (Arbeitsstättenverordnung / BildscharbV):
  * Blickrichtung parallel zum Fenster (Vermeidung von Blendungen/Reflexionen).
  * Sehabstand zum Monitor: ca. 50-80 cm (je nach Displaygröße).
  * Tastatur und Maus auf einer Ebene; Beine im 90-Grad-Winkel.
* Elektrische Sicherheit (VDE 0701-0702 / DGUV V3):
  * Wiederkehrende Prüfung elektrischer Betriebsmittel (Sichtprüfung, Schutzleiterwiderstand, Isolationswiderstand).

---

## Relevanz für Anwendungsentwickler (FIAE)

Auch wenn die physische Bereitstellung von Hardware oft vom Systemintegrationsteam durchgeführt wird, ist dieser Prozess für Anwendungsentwickler aus folgenden Gründen essenziell:

1. Entwicklung von ITSM- und Ticket-Systemen / Schnittstellen:
   * Anwendungsentwickler schreiben, erweitern oder integrieren Workflows in Systemen wie Jira, ServiceNow oder OTRS. Das Verständnis für Ticket-Lebenszyklen, SLAs und CMDBs ist Voraussetzung für die korrekte Datenmodellierung.
2. DevOps und Software-Deployment:
   * Die Bereitstellung von Entwicklungs-Umgebungen (Dev, Staging, Prod) folgt oft standardisierten Service-Requests. Entwickler müssen verstehen, welche Abhängigkeiten zu Assets und CIs (Configuration Items) bestehen.
3. Schnittstelle zum IT-Betrieb (Operations):
   * Bei Fehlern im Anwendungscode (Bugs) gelangen Tickets über den Service Desk an die Entwicklungsabteilung (Third-Level-Support). Ein sauberes Verständnis von Störungs- und Anfrageprozessen sichert eine reibungslose Zusammenarbeit zwischen Dev und Ops.
4. Compliance & Revisionssicherheit:
   * Entwickelte Software muss den Anforderungen der Nachvollziehbarkeit genügen. Das Wissen um Übergabeprotokolle und geordnete Abnahmeprozesse schützt vor Haftungs- und Sicherheitsrisiken im Software-Lebenszyklus.
