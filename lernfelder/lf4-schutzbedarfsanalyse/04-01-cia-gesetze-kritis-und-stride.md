# 04-01: LF 4.1 CIA-Triade, Rechtliche Grundlagen & STRIDE-Threat-Modeling

Dieses Modul behandelt die Kern-Schutzziele der IT-Sicherheit, den rechtlichen Rahmen (DSGVO, BSIG, KRITIS) sowie die systematische Bedrohungsklassifikation nach dem STRIDE-Modell.

---

## 1. Die CIA-Triade (Schutzziele der Informationssicherheit)

| Schutzziel | Definition | FIAE-Praxisbeispiel 1 | FIAE-Praxisbeispiel 2 |
| :--- | :--- | :--- | :--- |
| **Vertraulichkeit (Confidentiality)** | Daten dürfen nur von autorisierten Personen gelesen werden. | Verschlüsselung sensibler DB-Felder (Bcrypt/AES). | Rollenbasierte Zugriffskontrolle (RBAC / JWT). |
| **Integrität (Integrity)** | Daten dürfen nicht unbemerkt verändert oder manipuliert werden. | Validierung von Formular-Inputs & SQL-Escaping. | Digitale Signierung von API-Requests (HMAC). |
| **Verfügbarkeit (Availability)** | Systeme und Daten müssen bei Bedarf zeitnah nutzbar sein. | Einsatz von Rate Limiting gegen DoS/Brute-Force. | Datenbank-Replikation & Failover-Mechanismen. |

### Verkettung von Schutzziel-Verletzungen
* **Beispiel:** Ein Angreifer hebelt durch eine SQL-Injection die **Vertraulichkeit** aus und entwendet Admin-Zugangsdaten. Mit diesen Rechten löscht er die Datenbank (**Verletzung der Integrität**), was schlussendlich zum vollständigen Systemausfall führt (**Verletzung der Verfügbarkeit**).

---

## 2. Rechtlicher Rahmen: Gesetze vs. Normen & KRITIS

* **Gesetze (Muss-Vorgaben):** Rechtlich bindend (z. B. DSGVO, BSIG). Zuwiderhandlung führt zu Strafen oder Bußgeldern.
* **Normen/Standards (Soll-Vorgaben):** Freiwillige Best Practices & Zertifizierungen (z. B. ISO/IEC 27001, BSI IT-Grundschutz).

### Relevante Gesetze
* **DSGVO:** Schutz personenbezogener Daten. Verlangt *Privacy by Design* & *Privacy by Default* im Quellcode.
* **BSIG (inkl. IT-Sicherheitsgesetz 2.0):** Regelung der Befugnisse des BSI, Ausweitung der Pflichten für Betreiber Kritischer Infrastrukturen (KRITIS) und Meldepflichten von Sicherheitslücken.

### KRITIS (Kritische Infrastrukturen)
Infrastrukturen von hoher Bedeutung für das Gemeinwesen, deren Ausfall dramatische Versorgungsengpässe verursachen würde.
* **Sektoren:** Energie, Informationstechnik/Telekommunikation, Transport/Verkehr, Gesundheit, Wasser, Ernährung, Finanz- & Versicherungswesen, Staat/Verwaltung.

---

## 3. Risikodefinition & STRIDE-Bedrohung Modellierung

### Die Risikogleichung
$$\text{Risiko} = \text{Gefährdung (Bedrohung)} \times \text{Schwachstelle} \times \text{Schadensausmaß}$$

* **Gefährdung:** Potenzielles Ereignis, das Schaden verursachen kann (z. B. Hackerangriff, Stromausfall).
* **Schwachstelle:** Sicherheitslücke im System oder Code (z. B. ungepatchtes Framework, fehlende Input-Sanitierung).
* **Risiko:** Die Wahrscheinlichkeit, dass eine Gefährdung eine Schwachstelle ausnutzt, multipliziert mit den Konsequenzen.

### STRIDE-Klassifikation (Bedrohungsanalyse für Softwareentwickler)

| Kategorie | Bedrohung (Threat) | Verletztes Schutzziel | Entwickler-Gegenmaßnahme |
| :---: | :--- | :--- | :--- |
| **S** | **Spoofing** (Identitätsanmaßung) | Authentizität | Strong Authentication (MFA, OAuth2, TLS-Zertifikate) |
| **T** | **Tampering** (Datenmanipulation) | Integrität | Input-Validierung, Hash-Prüfsummen, Parameterized Queries |
| **R** | **Repudiation** (Abstreitbarkeit) | Nicht-Abstreitbarkeit | Revisionssichere Audit-Logs (Logging von Write-Operationen) |
| **I** | **Information Disclosure** (Datenleck) | Vertraulichkeit | Verschlüsselung (At Rest & In Transit), Secrets-Management |
| **D** | **Denial of Service** (Dienstblockade) | Verfügbarkeit | Rate Limiting, Request Buffering, Autoscaling |
| **E** | **Elevation of Privilege** (Rechteausweitung) | Autorisierung | Principle of Least Privilege, Strikte Rechteprüfung in APIs |

---

## FIAE-Zusammenfassung
Entwickler nutzen STRIDE beim Softwaredesign (Threat Modeling), um Sicherheitslücken in APIs und Datenstrukturen frühzeitig vor der Codierung zu identifizieren und zu beheben.
