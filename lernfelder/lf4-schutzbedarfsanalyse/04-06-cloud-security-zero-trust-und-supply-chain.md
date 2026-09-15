# 04-06: LF 4.3 Cloud Security, Zero Trust Architecture & Supply-Chain-Abwehr

Dieses Modul behandelt das Shared-Responsibility-Modell in der Cloud, den Paradigmenwechsel zu Zero Trust sowie Schutzstrategien gegen Angriffe auf die Software-Lieferkette via Software Bill of Materials (SBOM).

---

## 1. Cloud Security & Shared-Responsibility-Modell

In Cloud-Umgebungen teilen sich Cloud-Anbieter (AWS, Azure, GCP) und Kunden die Sicherheitsverantwortung.

| Deployment-Modell | Verantwortung des Cloud-Providers | Verantwortung des Kunden / Entwicklers |
| :--- | :--- | :--- |
| **IaaS (z. B. EC2, Compute Engine)** | Physikalische Hardware, Rechenzentrum, Hypervisor, Basis-Netzwerk. | Betriebssystem-Patches, Laufzeitumgebung, Firewall-Regeln, Anwendung, Daten, IAM. |
| **PaaS (z. B. Beanstalk, App Service)** | Physikalische Hardware, OS, Laufzeitumgebung (Node.js, Java), Auto-Scaling. | Anwendungscode, API-Konfiguration, Daten, Access-Management (IAM). |
| **SaaS (z. B. M365, GitHub)** | Gesamtes System, Infrastruktur, Anwendung, Security-Updates. | Daten-Klassifizierung, Nutzer-Zugriffsrechte, Passwort-Policies. |

### Typische Cloud-Sicherheitsrisiken
* **Fehlkonfigurationen (Misconfigurations):** Öffentlich zugängliche S3-Buckets oder offene Datenbank-Ports.
* **Identity & Access Management (IAM) Lücken:** Zu weit gefasste Berechtigungen (Überprivilegierte Service-Accounts).
* **Unverschlüsselte Datenübertragung:** Fehlen von TLS zwischen Cloud-Komponenten.

### IAM & Security Groups
* **IAM (Identity & Access Management):** Zentrale Steuerung, *wer* (Identität) *was* (Ressource) *womit* (Rolle/Recht) tun darf.
* **Security Groups:** Virtuelle Firewalls auf Instanz-Ebene, die den ein- und ausgehenden Traffic über Port-Regeln filtern.

---

## 2. Castle-and-Moat vs. Zero Trust Architecture (ZTA)

| Kriterium | Trad. Castle-and-Moat (Perimeter) | Zero Trust Architecture (ZTA) |
| :--- | :--- | :--- |
| **Grundannahme** | Alles innerhalb des Firmennetzes (VPN) ist vertrauenswürdig. | Niemandem wird vertraut (*Assume Breach*).
| **Sicherheits-Perimeter** | Physische Netzwerkgrenze / Router-Firewall. | **Identität & Gerät** sind der neue Perimeter.
| **Zugriffssteuerung** | Einmalige Authentifizierung beim Netz-Beitritt. | Kontinuierliche Re-Authentifizierung & Re-Autorisierung. |

### Die 3 Kernprinzipien von Zero Trust
1. **Verify Explicitly:** Immer explizit authentifizieren und autorisieren (Identität, Gerät, Kontext, Standort).
2. **Use Least Privilege Access:** Strenge Beschränkung von Zugriffsrechten (Just-In-Time / Just-Enough-Access).
3. **Assume Breach:** Ausgehen von ständiger Kompromittierung; Nutzung von Mikrosegmentierung und E2E-Verschlüsselung.

---

## 3. Supply-Chain-Angriffe & SBOM (Software Bill of Materials)

### Definition & Abgrenzung
* **Supply-Chain-Angriff (Software):** Gezielte Kompromittierung von Drittanbieter-Bibliotheken oder Build-Pipelines (z. B. bösartige `npm`-, `PyPI`-Packages oder manipulierter Quellcode in Open-Source-Projekten).
* **Abgrenzung zu Dienstleister-Angriffen:** Dienstleister-Angriffe zielen auf die Infrastruktur/Zugänge externer Partner ab; Software-Supply-Chain-Angriffe injizieren Schadcode direkt in das Endprodukt.

### Software Bill of Materials (SBOM)
Eine **SBOM** ist eine strukturierte Inventarliste aller in einer Software verwendeten Open-Source-Bibliotheken, Frameworks und deren Abhängigkeiten (z. B. im SPDX- oder CycloneDX-Format).

* **Zweck:** Ermöglicht das blitzschnelle Scannen der eigenen Software auf neu entdeckte Sicherheitslücken (CVEs) in Dritthersteller-Code.
* **FIAE-Praxis:** Automatische Generierung der SBOM in der CI/CD-Pipeline (z. B. via `trivy` oder `syft`).

---

## FIAE-Zusammenfassung
Entwickler müssen IAM-Rollen nach dem Least-Privilege-Prinzip vergeben, Zero-Trust-Konzepte (mTLS zwischen Services) umsetzen und SBOMs in CI/CD-Pipelines integrieren, um Abhängigkeiten abzusichern.
