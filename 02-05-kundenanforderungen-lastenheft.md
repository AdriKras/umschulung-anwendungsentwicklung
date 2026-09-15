Kundenanforderungen im Leistungsprozess berücksichtigen (FIAE-Fokus)

Das Requirements Engineering bildet das Fundament jedes erfolgreichen Softwareprojekts. Für Anwendungsentwickler geht es darum, diffuse Kundenwünsche in präzise, prüfbable Anforderungen zu übersetzen, Geschäftsprozesse zu verstehen und diese im gesamten Software-Development-Life-Cycle (SDLC) systematisch zu berücksichtigen.

---

## 1. Der Leistungsprozess in der Softwareentwicklung

Der Leistungsprozess beschreibt den Weg von der ersten Kundenanfrage bis zur betriebsbereiten Softwareanwendung.

| Phase | Aufgabe & Relevanz im FIAE-Umfeld |
| :--- | :--- |
| **Anfrage** | Kunde beschreibt ein fachliches Problem oder Digitalisierungsziel. |
| **Anforderungsaufnahme** | Erhebung von Business-Rules, User Stories und Systemgrenzen. |
| **Beratung & Architektur** | Evaluation passender Tech-Stacks (z. B. Cloud-Native vs. On-Premise, SQL vs. NoSQL). |
| **Angebot & Kalkulation** | Aufwandsschätzung (z. B. via Planning Poker, Story Points) und Stundensatzkalkulation. |
| **Auftrag & Spezifikation** | Vertragliche Fixierung von Lastenheft, Pflichtenheft oder Product Backlog. |
| **Umsetzung (Sprint)** | Agiles Coden, Einrichten der Toolchain, CI/CD-Pipelines und Unit-Testing. |
| **Test (QS)** | Durchführung von Integrationstests, Penetrationstests und User Acceptance Tests (UAT). |
| **Übergabe / Deployment** | Go-Live, Release-Management und Übergabe der API- und Code-Dokumentation. |
| **Support & Wartung** | Bugfixing, Performance-Monitoring und Bereitstellung von Software-Updates. |

---

## 2. Differenzierung der Stakeholder-Perspektiven

In Softwareprojekten müssen Entwickler zwischen unterschiedlichen Rollen auf Kundenseite unterscheiden:

* **Externer Kunde:** Drittunternehmen, das eine Individualsoftware oder ein Customizing beauftragt.
* **Interner Kunde / Fachabteilung:** Interne Abteilungen (z. B. Buchhaltung, Logistik), deren Geschäftsprozesse durch Software automatisiert werden sollen.
* **Endbenutzer (User):** Personen, die täglich mit dem Frontend/UI arbeiten (Fokus auf Ergonomie, Usability und Barrierefreiheit nach BITV/WCAG).
* **Entscheider (Product Owner / Management):** Personen, die das Budget freigeben (Fokus auf ROI, TCO und Einhaltung von Fristen).

---

## 3. Unterscheidung: Bedarf, Wunsch und Anforderung

Im Kundendialog müssen unpräzise Aussagen schrittweise konkretisiert werden.

| Begriff | Definition | Beispiel im Software-Kontext |
| :--- | :--- | :--- |
| **Bedarf** | Echter fachlicher oder technischer Notstand. | "Unsere Kunden springen ab, weil der Checkout-Prozess im Browser zu lange dauert." |
| **Wunsch** | Angenehme Zusatzfunktion ohne kritischen Mehrwert. | "Die Buttons in der App könnten beim Drücken leicht animiert werden." |
| **Anforderung** | Konkret beschriebene, prüfbare Bedingung. | "Der API-Endpunkt `/api/v1/checkout` muss Transaktionen unter Volllast in unter 150 ms verarbeiten." |

---

## 4. Kategorisierung von Kundenanforderungen

Software-Anforderungen werden strukturiert erfasst, um Vollständigkeit zu gewährleisten:

* **Funktionale Anforderungen:** Beschreiben, *was* die Software leisten muss (z. B. "Das System muss bei einer Bestellung automatisch eine PDF-Rechnung generieren und per SMTP versenden.").
* **Nicht-Funktionale Anforderungen (NFA):** Beschreiben die Qualitätskriterien (*wie* die Software arbeitet):
  * **Performance:** Antwortzeiten und Durchsatz.
  * **Sicherheit:** Verschlüsselung (TLS 1.3), Schutz vor OWASP Top 10 (SQL-Injection, XSS).
  * **Wartbarkeit:** Clean Code, hohe Testabdeckung (Unit-Test-Coverage > 80 %).
  * **Skalierbarkeit:** Horizontales Hochskalieren via Container-Orchestrierung.
* **Technisch-Organisatorische Anforderungen:** Festlegung von Programmiersprachen, Frameworks, CI/CD-Tools und Git-Branching-Strategien.
* **Rechtliche Anforderungen:** DSGVO-Konformität (Data Privacy by Design), Lizenzrecht (GPL, MIT, Apache 2.0).

---

## 5. Priorisierung & Change Management

### Priorisierung nach der MoSCoW-Methode
Da Zeit und Budget im Projekt begrenzt sind, werden Anforderungen klassifiziert:
* **Must have:** Absolut zwingend für den Go-Live (Abnahmekriterium).
* **Should have:** Wichtiges Feature, für das kurzfristig ein Workaround existiert.
* **Could have:** Zusatzfeature ("Nice-to-have"), sofern Sprint-Kapazitäten übrig sind.
* **Won't have (this time):** Bewusst ausgeschlossene Funktion für das aktuelle Release.

### Änderungsmanagement (Change Management)
Ändern sich Anforderungen während der Entwicklung (Scope Creep), erfolgt eine formelle Auswirkungsanalyse auf Budget, Zeitplan und Architektur. Änderungen werden schriftlich über Change Requests freigegeben.

---

## Zusammenfassung (FIAE-Perspektive)

Für Anwendungsentwickler bedeutet die Berücksichtigung von Kundenanforderungen, nicht isoliert Code zu schreiben, sondern die fachlichen Probleme des Anwenders zu lösen. Die strukturierte Aufnahme, Dokumentation und agile Priorisierung schützt das Softwareprojekt vor Fehlinvestitionen, Fehlfunktionen und unkontrollierten Ausfall- und Wartungskosten.
