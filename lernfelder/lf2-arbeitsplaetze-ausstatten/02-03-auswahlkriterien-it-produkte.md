# LF 2.3: Auswahlkriterien für IT-Produkte (FIAE-Fokus)

Bei der Auswahl von IT-Produkten (Hardware, Software-Lizenzen, Cloud-Services) im Entwicklungsumfeld reichen Kaufpreis und Markennamen nicht aus. Entwickler benötigen Systeme, die stabil unter hohen Lasten arbeiten, sich nahtlos in bestehende Toolchains integrieren und den gesetzlichen sowie wirtschaftlichen Rahmenbedingungen entsprechen.

---

## 1. Anforderungen als Grundlage (Requirements-Driven Selection)

Bevor Hardware oder Software beschafft wird, müssen die funktionalen und nicht-funktionalen Anforderungen (NFA) definiert werden.

| Anforderungs-Kategorie | Fragestellung aus FIAE-Sicht | Beispiel |
| :--- | :--- | :--- |
| **Einsatzzweck** | Welches Entwicklungs-Szenario soll abgedeckt werden? | Lokale Docker-Cluster, iOS-App-Development, Machine Learning. |
| **Infrastruktur & Schnittstellen** | Welche Schnittstellen und Altsysteme existieren? | Einbindung in vorhandenes Active Directory, LDAP, Git-Server, CI/CD-Runner. |
| **Sicherheit & Compliance** | Welche Datenschutz- und Sicherheitsstandards gelten? | DSGVO-Konformität bei Cloud-Diensten, TPM 2.0 für Festplattenverschlüsselung. |
| **Lebenszyklus & Support** | Wie lange muss der Tech-Stack / die Hardware unterstützt werden? | LTS-Versionen (Long Term Support) bei Frameworks, 3 Jahre Vor-Ort-Garantie bei Laptops. |

---

## 2. Technische & Qualitativ-Methodische Auswahlkriterien

### Technical Evaluation für Entwickler-Hardware
* **CPU & Multithreading:** Hohe Single-Core-Leistung für schnelles Kompilieren; viele Kerne für Paralleles Ausführen von Containern und VMs.
* **Arbeitsspeicher (RAM):** 32 GB bis 64 GB als Minimum für moderne IDEs, lokale Datenbanken und Virtualisierung.
* **I/O-Performance (SSD):** NVMe-SSDs mit hohen zufälligen Schreib-/Leseraten (IOPS) zur Vermeidung von Build-Flaschenhälsen.
* **Erweiterbarkeit & Peripherie:** Thunderbolt/USB4-Ports für Multi-Monitor-Betrieb und schnelle externe Test-Devices.

### Business vs. Consumer Hardware
Im Entwicklungs-Alltag bieten Business-Geräte entscheidende Vorteile:
* **Stabilität & Kühlung:** Höhere thermische Belastbarkeit bei Dauerlast (z. B. stundenlanges Rendern oder Kompilieren).
* **Treiber- & Image-Stabilität:** Gleiche Komponenten über Jahre hinweg vereinfachen das Erstellen von Standard-Entwickler-Images.
* **Zentrales Management:** Unterstützung für vPro/AMT zur Fernwartung durch die interne IT.

---

## 3. IT-Sicherheit & Datenschutz (Compliance)

Sicherheits- und Datenschutzanforderungen fließen direkt in die Auswahl von Hardware und Software-Diensten ein.

* **Sicherheitsfunktionen (Hardware):**
  * **TPM 2.0 (Trusted Platform Module):** Pflicht für BitLocker-Verschlüsselung sensiver Quellcodes auf mobilen Laptops.
  * **Secure Boot:** Verhindert das Laden von manipulierten Bootloadern beim Systemstart.
* **Datenschutz & Cloud-Tools (DSGVO):**
  * Bei der Auswahl von SaaS-Tools (z. B. GitHub, Jira, AWS) muss geprüft werden, ob Auftragsverarbeitungsverträge (AVV) vorliegen und Serverstandorte innerhalb der EU liegen.
  * **SaaS vs. Self-Hosted:** Sensible Quellcodes erfordern oft selbstgehostete Repositories (z. B. GitLab On-Premise) statt öffentlicher Cloud-Dienste.

---

## 4. Wirtschaftlichkeit & Total Cost of Ownership (TCO)

Die Bewertung von IT-Produkten erfolgt nach dem TCO-Ansatz (Gesamtkosten über die Nutzungsdauer).

### Die TCO-Formel im Software- & Hardware-Bereich
TCO = Anschaffung (CAPEX) + Lizenzen + Betriebskosten (OPEX) + Wartung/Support + Schulung - Restwert

### Kostenarten in Software-Projekten

| Kostenart | Beispiele im FIAE-Umfeld |
| :--- | :--- |
| **Anschaffungskosten** | Kaufpreis von Entwickler-Workstations, Erstkauf von Software-Lizenzen. |
| **Lizenz- & Abokosten** | Monatliche/jährliche Gebühren für IDEs (z. B. JetBrains All Products), Copilot-Lizenzen, Cloud-Credits. |
| **Betriebs- & Ausfallkosten** | Stromverbrauch von Build-Servern; Kosten durch Entwickler-Stillstand bei defekter Hardware. |
| **Schulungskosten** | Einarbeitungszeit in ein neues Framework oder eine neue Toolchain. |

---

## 5. Software-Auswahl: Open-Source vs. Proprietaer

Bei der Auswahl von Software-Produkten und Bibliotheken müssen Entwickler rechtliche und wirtschaftliche Kriterien abwägen:

* **Proprietaere Software:**
  * *Vorteile:* Garantierter Herstellersupport, SLAs, klare Haftung.
  * *Nachteile:* Hohe Lizenzkosten, Vendor Lock-in (Abhängigkeit vom Anbieter).
* **Open-Source-Software (OSS):**
  * *Vorteile:* Keine Lizenzgebühren, einsehbarer Quellcode, große Community.
  * *Nachteile:* Kein kommerzieller Support (sofern nicht zugekauft), Lizenzbedingungen müssen strikt beachtet werden (z. B. GPL vs. MIT).

---

## 6. Sustainability & Green IT

Nachhaltigkeit beeinflusst Beschaffungsentscheidungen zunehmend:
* **Energieeffizienz:** Auswahl von ARM-basierten Servern oder Netzteilen mit hoher 80-PLUS-Zertifizierung zur Reduzierung des CO2-Fußabdrucks.
* **Reparierbarkeit:** Bevorzugung von Laptops mit geschraubten Komponenten (RAM/SSD) gegenüber komplett verklebten Systemen.
* **Resource-Efficient Software Design:** Auswahl von schlanken Frameworks zur Reduzierung des Server-Energieverbrauchs unter Last.

---

## Zusammenfassung (FIAE-Perspektive)

Die Produktauswahl im Entwicklungsbereich ist eine Abwägung aus **technischer Anforderungsabdeckung**, **Rechtssicherheit (DSGVO/Lizenzen)** und **Wirtschaftlichkeit (TCO)**. Ein teures Entwickler-Notebook oder eine kostenpflichtige IDE-Lizenz ist oft die wirtschaftlichere Wahl, wenn dadurch Ausfallzeiten minimiert und die Entwicklungsgeschwindigkeit gesteigert werden.
