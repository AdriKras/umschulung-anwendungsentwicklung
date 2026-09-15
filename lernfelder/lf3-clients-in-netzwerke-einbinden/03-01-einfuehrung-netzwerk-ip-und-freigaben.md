# 03-01: LF3.1 Der erste Kontakt (Einführung in Netzwerke, IP & Freigaben)

Ein Rechnernetz verbindet IT-Systeme (Clients, Server, Komponenten) zum Austausch von Daten und Diensten. Für Anwendungsentwickler (FIAE) ist Netzwerkwissen essenziell: Jede moderne Anwendung kommuniziert über Netzwerke – sei es via REST-API, Datenbank-Verbindungsstring, WebSockets oder Microservices.

---

## 1. Netzwerke im Unternehmen & Die 5 Ebenen

Typische Aufgaben im Unternehmen sind zentraler Dateizugriff, Internetanbindung, E-Mail, Cloud-Dienste, zentrales Rechtemanagement und Backup-Prozesse.

### Die 5 Ebenen eines funktionierenden Netzwerks

| Ebene | Bedeutung | FIAE- / Relevanz |
| :--- | :--- | :--- |
| **Physische Ebene** | Kabel (Kupfer S/FTP, LWL), WLAN, Switches, NICs | Physikalische Signalübertragung |
| **Logische Ebene** | IP-Adressen, Subnetze, Routing, DNS | Network Addressing & Sockets (`IP:Port`) |
| **Dienste-Ebene** | DHCP, DNS, SMB, HTTP/HTTPS, DB-Server | API-Endpunkte, Datenbank-Connectors |
| **Sicherheits-Ebene** | Firewalls, TLS-Verschlüsselung, JWT, Rechte | Auth, CORS-Header, HTTPS-Zertifikate |
| **Organisatorische Ebene**| Dokumentation, Prozesse, Zuständigkeiten | API-Dokumentation, SLA-Vorgaben |

---

## 2. Kommunikationsparadigmen: Client-Server vs. Peer-to-Peer

### Client-Server-Prinzip
Der Client fordert Ressourcen/Dienste an; der Server verarbeitet und antwortet.
* **Vorteile:** Zentrale Datenhaltung, einfacheres Rechte- & Backup-Management, bessere Kontrolle.
* **Nachteile:** Single Point of Failure (Serverausfall betrifft alle), Hohe Anforderungen an Server-Verfügbarkeit.
* **FIAE-Perspektive:** Standard für Web-Apps, Mobile Apps und Cloud-Backend (z. B. React Client fragt Node.js/Spring Boot API an).

### Peer-to-Peer-Prinzip (P2P)
Geräte kommunizieren direkt als gleichberechtigte Partner ohne zentralen Server.
* **Nachteile im Unternehmen:** Schwer administrative Kontrolle durchzusetzen, dezentrale Rechtevergabe, Sicherheitsrisiken.

---

## 3. Netzwerkarten & Reichweiten

| Typ | Bezeichnung | Reichweite / Merkmale |
| :--- | :--- | :--- |
| **PAN** | Personal Area Network | Bluetooth, NFC (~10m) |
| **LAN** | Local Area Network | Lokales Gebäude-Netzwerk, hohe Datenraten, Ethernet/Kupfer |
| **WLAN** | Wireless LAN | Drahtloses LAN (IEEE 802.11), flexibel, störungsanfälliger als Kabel |
| **MAN / WAN**| Wide Area Network | Standortübergreifend, Glasfaser, Provider-Anbindung |
| **VPN** | Virtual Private Network | Verschlüsselter Tunnel über öffentliche Netze (Homeoffice/Standorte) |

---

## 4. Netzwerkkomponenten & Identifikatoren im Überblick

### Hardware- & Logik-Komponenten
* **Switch (Layer 2):** Verbindet Geräte im LAN gezielt via **MAC-Adressen**.
* **Router (Layer 3):** Verbindet unterschiedliche Subnetze/WANs via **IP-Adressen** (Gateway).
* **Firewall:** Filtert Datenverkehr anhand von IP-, Port- und Protokoll-Regeln.
* **Access Point:** Stellt die Brücke von WLAN-Clients in das kabelgebundene LAN her.

### Die 3 Ebenen der Gerät-Identifikation
1. **MAC-Adresse (Layer 2):** Physikalische Hardware-Adresse der Netzwerkkarte (`AA:BB:CC:...`).
2. **IP-Adresse (Layer 3):** Logische Standort-Adresse im Netz (z. B. `192.168.1.50`).
3. **Hostname / DNS-Name (Layer 7):** Menschenlesbarer Name (z. B. `api.unternehmen.de`).

---

## 5. Adressierung, Subnetting & Netzdienste (IPv4/IPv6, DHCP, DNS)

### Private vs. Öffentliche IPv4-Adressen (RFC 1918)
Private IP-Bereiche sind im Internet nicht routbar:
* `10.0.0.0/8`
* `172.16.0.0/12`
* `192.168.0.0/16`

### Subnetting (CIDR-Notation)
Die Subnetzmaske (z. B. `/24` = `255.255.255.0`) trennt den **Netz-Teil** vom **Host-Teil**.
* **Beispiel `192.168.1.0/24`:** Netz-ID: `192.168.1.0`, Broadcast: `192.168.1.255`, Nutzbare IPs: `192.168.1.1` bis `192.168.1.254` ($2^8 - 2 = 254$).

### IPv6 & Autokonfiguration
* **Struktur:** 128 Bit Hexadezimal (`2001:db8::1`), aufgeteilt in Präfix (64 Bit) und Interface-ID (64 Bit).
* **SLAAC:** Client baut sich seine IP-Adresse ohne DHCP-Server selbst zusammen.

### Netzdienste: DHCP & DNS
* **DHCP (DORA-Prinzip):** **D**iscover (Client fragt) -> **O**ffer (Server bietet) -> **R**equest (Client wählt) -> **A**cknowledge (Server bestätigt IP, Gateway, DNS).
* **DNS (Domain Name System):** Name-Resolution.
  * **A-Record:** Hostname -> IPv4
  * **AAAA-Record:** Hostname -> IPv6
  * **PTR-Record:** IP -> Hostname (Reverse DNS)

---

## 6. Plattformübergreifende Dateifreigaben (SMB), Rechte & DSGVO

### SMB & Linux-Dateirechte
* **SMB (Server Message Block):** Protokoll für Netzlaufwerke zwischen Windows und Linux (Samba).
* **POSIX-Rechte (`chmod`/`chown`):** `r=4`, `w=2`, `x=1` für User/Group/Others.
  * *Beispiel `chmod 750`:* Owner=Vollzugriff (7), Group=Lesen/Ausführen (5), Others=Kein Zugriff (0).

### Datenschutz & Recht (DSGVO)
Unsichere SMB-Freigaben oder fehlende Rechteverwaltung verstoßen gegen Art. 32 DSGVO (Schutz personenbezogener Daten) und ermöglichen Datenlecks sowie Ransomware-Schäden.

---

## 7. Systematisches Troubleshooting & Netzwerkdokumentation

### Reihenfolge bei Netzwerkproblemen
1. **Link-Status prüfen:** Kabel eingesteckt? Link-LED grün? WLAN verbunden?
2. **IP-Konfiguration:** Hat der Client eine gültige IP (keine `169.254.x.x` APIPA-Adresse)?
3. **Local Gateway Test:** Ist der lokale Router erreichbar (`ping 192.168.1.1`)?
4. **DNS-Auflösung:** Funktioniert Namensauflösung (`nslookup api.local` / `dig`)?
5. **Dienst & Firewall:** Blockiert die lokale Firewall den Port (z. B. Port 80/443/5432)?

### Wichtige Elemente der Dokumentation
Netzpläne, IP-Adresskonzepte, VLAN-Zuordnungen, Server-Dienste, Firewallebenen und Notfall-Kontaktdaten.

---

## 8. FIAE-Perspektive: Warum Netzwerke für Entwickler entscheidend sind

Als Anwendungsentwickler schreibt man selten Netzwerk-Treiber, baut aber dauerhaft auf funktionierenden Netzen auf:

* **Connection Strings & Timeouts:** Wenn eine App keine Datenbank erreicht, liegt es oft an DNS-Fehlern, falschen Subnetzen oder geschlossenen Ports (Firewall).
* **Rest-APIs & HTTP-Statuscode:** Verstehen von L7-Payloads auf Basis von L3/L4-Routings.
* **CORS & Zertifikate (HTTPS/TLS):** Netzwerksicherheit erfordert richtige Zertifikate und Freigaben im Frontend/Backend.
* **Service Discovery:** In Microservice- und Docker-Umgebungen ersetzen interne DNS-Server statische IP-Adressen.
