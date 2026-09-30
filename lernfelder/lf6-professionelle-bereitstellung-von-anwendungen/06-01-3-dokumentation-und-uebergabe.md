# LF 6.1.3 - Dokumentation, CMDB und Übergabe

## 1. Übersicht und Einordnung

Der letzte Schritt in der Bereitstellung von Hard- und Software (sowie im Incident Management) ist die saubere Dokumentation und rechtswirksame Übergabe an den Nutzer. Für Fachinformatiker (FIAE/FISI) ist dieser Schritt essenziell, da er die Grundlage für IT-Sicherheit, Lizenzmanagement, Inventur und den Aufbau einer Wissensdatenbank (Knowledge Base) bildet. Fehlende Dokumentation führt unweigerlich zu Folgekosten und Sicherheitsrisiken.

---

## 2. Configuration Management Database (CMDB)

Die CMDB ist weit mehr als nur eine Inventarliste (Asset Management). Sie speichert Konfigurationseinheiten (Configuration Items - CIs) und deren logische Beziehungen zueinander.

* **Configuration Item (CI):** Jede Komponente, die verwaltet werden muss, um einen IT-Service bereitzustellen (z. B. ein PC, ein Server, eine Softwarelizenz oder ein Netzwerk-Switch).
* **Beziehungsgeflecht:** In der CMDB wird nicht nur dokumentiert, dass ein Notebook "existiert", sondern:
  * Welchem **Nutzer** ist es zugeordnet?
  * Welcher **Software-Service** läuft darauf?
  * Welcher **Lizenzschlüssel** ist hinterlegt?
* **Inventarsicherheit:** Ein Gerätetausch ohne Aktualisierung der CMDB führt zu sogenannten "Geister-Arbeitsmitteln". Bei der nächsten Inventur oder beim Offboarding des Mitarbeiters fehlt der Nachweis über den Verbleib der alten und neuen Hardware.

---

## 3. Rechtssichere Übergabe (Übergabeprotokoll)

Die physische oder digitale Übergabe von Arbeitsmitteln muss stets dokumentiert werden. Dies schützt sowohl das Unternehmen als auch den Mitarbeiter.

* **Inhalte eines Übergabeprotokolls:** 
  * Datum, Name des Mitarbeiters, genaue Bezeichnung der Hardware (inkl. Seriennummer).
  * Zustand der Hardware (z. B. Neuware, gebraucht, sichtbare Mängel).
  * Bestätigung des Empfangs und der Funktionstüchtigkeit.
* **Haftung und Beweislastumkehr:** Mit der Unterschrift bestätigt der Benutzer den Erhalt. Ab diesem Zeitpunkt haftet der Benutzer (je nach Unternehmensrichtlinie) für Schäden durch grobe Fahrlässigkeit oder Vorsatz.
* **Sicherheitsunterweisung:** Oft wird im Protokoll gleichzeitig bestätigt, dass der Nutzer über die IT-Sicherheitsrichtlinien (z. B. Umgang mit Passwörtern, Verbot privater Nutzung) aufgeklärt wurde.

---

## 4. Ticketabschluss und Lösungstext (ITSM)

Ein Ticket darf niemals kommentarlos (z. B. nur mit dem Wort "Erledigt") geschlossen werden. Der Lösungstext ist die wichtigste Quelle für die IT-Dokumentation.

* **Qualifizierter Lösungstext:** Er muss nachvollziehbar beschreiben, was genau gemacht wurde. 
  * *Negativ-Beispiel:* "Monitor getauscht. Erledigt."
  * *Positiv-Beispiel:* "Monitor getauscht. Altgerät (S/N 1234) wegen Defekt am HDMI-Port entnommen und an Schrott-Palette übergeben. Neugerät (S/N 5678) aufgebaut, CMDB aktualisiert, Funktionstest mit Nutzer erfolgreich durchgeführt."
* **Wissensdatenbank (Knowledge Base):** Präzise Lösungstexte helfen Kollegen im Service Desk, ähnliche Störungen in Zukunft schneller zu lösen (Reduzierung der Lösungszeit / Time-to-Resolve).
* **Statistik und Nachvollziehbarkeit:** Aussagekräftige Tickets sind notwendig für das IT-Controlling, das SLA-Reporting und nachträgliche Audits.

---

## 5. Bedeutung für die Anwendungsentwicklung (FIAE)

* **Lizenz- und Berechtigungsmanagement:** Auch Entwickler-Tools (z. B. IDE-Lizenzen, Cloud-Zugänge, Datenbank-Rechte) sind CIs in der CMDB. Eine saubere Dokumentation verhindert teure Überlizenzierungen oder unberechtigte Zugriffe (Compliance).
* **Bug-Tracking und Versionierung:** Das Prinzip des qualifizierten Lösungstextes gilt analog für Commit-Messages und Pull-Requests. Ein "Bug fixed" reicht nicht – es muss dokumentiert werden, *welcher* Bug *wie* und in *welcher Version* behoben wurde.
* **Sauberes On- und Offboarding:** Bei Entwicklerwechseln muss klar dokumentiert sein, wer Zugriff auf welche Produktivsysteme, Repositories und Hardware-Token hat, um diese rechtssicher entziehen zu können.

---

## 6. Quellenverzeichnis

* **S. Kersken:** *IT-Handbuch für Fachinformatiker*innen*, Rheinwerk Verlag.
* **Wikipedia:** *Configuration Management Database (CMDB)* - Konzept der Configuration Items (CIs).
* **Lendis GmbH:** *Muster-Übergabeprotokoll (Equipment Handover)* - Nachweise und Haftung.
* **eesel.ai:** *ITSM-Ticketing Best Practices* - Dokumentation und Ticketabschluss.
