# 03-08: LF 3.5 NAT, Firewall-Zonen, VPN / SD-WAN & Cloud-Modelle

Dieses Modul behandelt Network Address Translation (NAT), Firewall-Zonenkonzepte, Standortvernetzung via VPN und SD-WAN sowie Cloud-Deployment-Modelle.

---

## 1. NAT (Network Address Translation) & Masquerading

NAT übersetzt private IPv4-Adressen (z. B. `192.168.x.x`) beim Verlassen des Routers in eine einzige öffentliche IP-Adresse.

* **SNAT / Masquerading (Source NAT):** Mehrere Clients im LAN teilen sich eine öffentliche IP für ausgehenden Web-Traffic.
* **DNAT / Port-Forwarding (Destination NAT):** Eingehende Anfragen auf einem bestimmten Port der öffentlichen IP werden an ein internes Gerät (z. B. Webserver `192.168.1.50:80`) weitergeleitet.

---

## 2. Firewall-Zonenkonzept & Inter-VLAN-Filtering

Netzwerke werden in Zonen mit unterschiedlichen Sicherheitsstufen unterteilt (z. B. in OpenWrt / Enterprise-Firewalls):

```text
[ WAN / Internet ] (Unsanitisiert / Unsicher)
        |
   [ FIREWALL ]
     ├── [ LAN Zone ] -------> Internes Firmennetz (Voller Zugriff nach außen)
     ├── [ DMZ Zone ] -------> Demilitarisierte Zone (Öffentlich erreichbare Webserver)
     └── [ GUEST Zone ] -----> Gastnetzwerk (Nur Internet, kein LAN-Zugriff)
```

---

## 3. Standortvernetzung: VPN vs. Leased Line vs. SD-WAN

| Technologie | Funktionsweise | Vorteile | Nachteile |
| :--- | :--- | :--- | :--- |
| **Site-to-Site VPN** | Verschlüsselter Tunnel (IPsec/WireGuard) über das öffentliche Internet. | Günstig, flexibel über bestehende Internetanschlüsse. | Abhängig von Internet-Qualität (Latenz/Jitter). |
| **Client-to-Site VPN**| Einzelner Remote-Client (Home Office) verbindet sich per VPN-Software zum Firmennetz. | Sicheres Arbeiten von überall. | Verschlüsselungs-Overhead auf Client. |
| **Klassische Standleitung** | Exklusive, physikalisch gemietete Direktverbindung (Leased Line / MPLS). | Höchste Performance, garantierte Bandbreite & SLA. | Sehr teuer, unflexibel bei Änderungen. |
| **SD-WAN** | Software-definierte Steuerung über mehrere Verbindungen (DSL + Fiber + 5G). | Automatische Pfadauswahl nach Latenz/Kosten, hohe Ausfallsicherheit. | Höhere initiale Software-Komplexität. |

---

## 4. Cloud-Bereitstellungsmodelle

| Modell | Beschreibung | Beispiel | Verantwortung des Entwicklers |
| :--- | :--- | :--- | :--- |
| **On-Premises** | Eigene Hardware im eigenen Rechenzentrum. | Lokaler Serverraum | Alles (Hardware, OS, App, Daten) |
| **IaaS (Infrastructure as a Service)** | Bereitstellung virtueller Server, Speicher und Netze. | AWS EC2, Azure VMs | Betriebssystem, Runtime, App, Daten |
| **PaaS (Platform as a Service)** | Bereitstellung der Laufzeitumgebung für Entwickler. | Heroku, AWS Elastic Beanstalk | Nur Anwendungscode & Daten |
| **SaaS (Software as a Service)** | Fertige Anwendung über das Web nutzbar. | Microsoft 365, GitHub | Nur Konfiguration & eigene Daten |

---

## FIAE-Zusammenfassung
Entwickler müssen den Unterschied zwischen IaaS, PaaS und SaaS sowie VPN/NAT-Konzepte verstehen, um Cloud-Architekturen (z. B. Deployment auf AWS PaaS vs. eigenen IaaS-VMs) richtig zu planen und APIs sicher bereitzustellen.
