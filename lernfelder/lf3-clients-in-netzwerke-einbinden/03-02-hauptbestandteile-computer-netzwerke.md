# 03-02: Hauptbestandteile von Computernetzen (AE-Fokus)

Ein Computernetzwerk besteht aus weit mehr als nur Kabeln und Computern. Es bildet das Gesamtsystem aus Endgeräten, Servern, Netzwerkkomponenten, Übertragungsmedien, Netzwerkkonfigurationen, Sicherheitsbereichen und Cloud-Infrastrukturen. Für Anwendungsentwickler (FIAE) ist dieses Verständnis essenziell, um verteilte Anwendungen, API-Endpunkte, Datenbankanbindungen und Microservices stabil in Unternehmensnetzen zu betreiben.

---

## 1. Das Netzwerk als Gesamtsystem der Software-Kommunikation

Damit eine moderne Anwendung (Web-App, Mobile-App, Desktop-Software) Daten austauschen kann, müssen alle Ebenen der Netzwerk-Infrastruktur nahtlos zusammenarbeiten:

| Bereich | Bedeutung im Software-Lebenszyklus |
| :--- | :--- |
| **Geräte & Hosts** | Entwickler-PCs, Test-Clients, Datenbank-Server, API-Gateways |
| **Verbindung & Medien** | Gigabit-Ethernet, Glasfaser (Rechenzentrum), Wi-Fi, VPN-Tunnel |
| **Adressierung** | Eindeutige Zuweisung von MAC-Adressen, IP-Adressen und Hostnamen |
| **Protokolle & Dienste**| HTTP/HTTPS, TCP/UDP, DNS, DHCP, REST/GraphQL, WebSockets |
| **Sicherheitszonen** | Firewalls, DMZ, CORS-Policies, Subnetz-Segmentierung |
| **Verwaltung & Doku** | Network-Diagramme, Environment-Configs (`.env`), CI/CD-Pipelines |

---

## 2. Endgeräte & Client-Klassifizierung aus Entwicklersicht

Anwendungen laufen auf unterschiedlichsten Endgeräten (Hosts). Je nach Client-Architektur ändern sich die Anforderungen an Rechenleistung, Speicher und Netzwerkstabilität:

| Client-Art | Erklärung & Funktionsweise | AE- / Entwickler-Perspektive |
| :--- | :--- | :--- |
| **Fat Client** | Eigenständige Rechenleistung & lokaler Speicher. Anwendung läuft direkt auf dem Gerät (z. B. Desktop-App). | Hohe Anforderungen an lokale Ressourcen; Benötigt lokale DB-Treiber oder Direct-APIs. |
| **Thin Client** | Minimalistische Hardware. Berechnung und Anwendungslogik laufen auf zentralen Servern (VDI/RDP). | Webbasierte UIs oder Terminal-Server-Anwendungen; Minimale lokale Datenhaltung. |
| **Web Client** | Ausführung im Webbrowser (Single Page Applications in React, Angular, Vue). | Rendering im Browser; Datenaustausch strictly via REST/GraphQL und JSON. |
| **Mobile Client** | Smartphones/Tablets (iOS, Android). Nutzen oft wechselnde Netzwerke (WLAN/Cellular). | Robustes Handling von Verbindungsabbrüchen (Offline-First-Strategien, Caching). |
| **Remote Client** | Zugriff aus dem Homeoffice über verschlüsselte VPN-Tunnel. | Zugriff auf geschützte interne Staging-Datenbanken und Git-Repositories. |

---

## 3. Servertypen & Rollen in der Software-Architektur

Ein Server stellt Dienste bereit. In modernen Anwendungsarchitekturen arbeiten spezialisierte Serverrollen zusammen:

* **Applikationsserver (Application Server):** Führt die Geschäftslogik aus (z. B. Node.js, Spring Boot, .NET Core, Django).
* **Datenbankserver:** Speichert und verwaltet strukturierte Daten (z. B. PostgreSQL, MySQL, MongoDB).
* **Webserver / Reverse Proxy:** Nginx, Apache oder Traefik zur Verteilung von HTTP-Anfragen, SSL/TLS-Offloading und Caching.
* **DNS- & DHCP-Server:** Zentrale Netzwerkinfrastruktur zur automatischen Adressvergabe und Namensauflösung (`db.internal`).
* **Authentifizierungsserver:** OAuth2/OpenID-Connect-Server (z. B. Keycloak, Auth0) zur Verifizierung von Logins und JWT-Tokens.
* **Physisch vs. Virtuell vs. Container:** Moderne Server laufen selten auf "nackter Hardware" (Bare Metal), sondern als Virtuelle Maschinen (VMs) oder Docker-Container.

---

## 4. Active & Passive Netzwerkkomponenten

Netzwerkgeräte verbinden Systeme und leiten den Datenverkehr zielgerichtet weiter:

| Komponente | Hauptaufgabe | Relevanz für Softwareentwickler |
| :--- | :--- | :--- |
| **Switch (Layer 2)** | Verbindet Geräte im LAN via MAC-Adresse. | Beeinflusst Latenzen im internen Netzwerk (Cluster-Performance). |
| **Router (Layer 3)** | Verbindet Netze via IP-Adresse (Default Gateway). | Leitet Anfragen an externe APIs oder Cloud-Dienste weiter. |
| **Firewall** | Filtert Datenverkehr nach Regelwerken & Ports. | Häufiger Grund für `Connection Timeout` bei DB-/API-Zugriffen. |
| **Access Point** | Wandelt kabelgebundenes LAN in WLAN um. | Testumgebung für mobile Apps unter schwankenden Signalstärken. |
| **Load Balancer** | Verteilt Anfragen auf mehrere App-Instanzen. | Erfordert zustandslose (stateless) Anwendungskonzepte. |
| **Patchpanel / Racks**| Physische Rangierverteilung im Serverraum. | Ordnung und Struktur der physikalischen Infrastruktur. |

---

## 5. Übertragungsmedien: Eigenschaften & Performance-Faktoren

Die Wahl des Mediums bestimmt Bandbreite, Latenz und Störanfälligkeit:

* **Kupferkabel (Twisted Pair / Cat 6A / Cat 7):** Standard im Büro/LAN; Günstig, RJ45-Stecker, bis zu 100m Segmentlänge.
* **Glasfaser (LWL - Lichtwellenleiter):** Extrem hohe Bandbreiten, keine elektromagnetische Störanfälligkeit. Einsatz im Rechenzentrum und zwischen Gebäuden.
* **WLAN (Wi-Fi 6 / 6E):** Drahtlos, flexibel, aber geteiltes Medium (Shared Medium) – anfällig für Dämpfung, Störungen und schwankende Latenzen.

---

## 6. Netzbereiche & Sicherheitszonen (LAN, DMZ, Cloud)

Eine professionelle IT-Architektur trennt Netzbereiche nach Schutzbedarf:

```text
[ INTERNET / UNINORM ]
         |
    [ FIREWALL ]
         |
  +------+------+
  |             |
[ DMZ ]      [ INTERNES LAN ]
  |             |
 (Webserver/   (Entwickler-PCs, Interner DB-Server,
  Reverse      Applikationsserver, Git-Server)
  Proxy)

DMZ (Demilitarized Zone): Zwischennetz für öffentlich erreichbare Dienste (Webserver, API-Gateway). Bei Kompromittierung bleibt das interne Netz geschützt.Servernetz / Internes LAN: Geschützter Bereich für vertrauliche Datenbanken und interne Logik.Cloud-Einbindung: Hybride Architekturen binden Cloud-Ressourcen (AWS, Azure) über sichere VPN-Tunnel (IPsec) direkt in das Unternehmensnetz ein.7. Typische Fehler & Systematic Troubleshooting für EntwicklerProblem / FehlerbildUrsache im NetzwerksystemLösungsansatz für EntwicklerHost not foundDNS-Auflösung schlägt fehlHostname in .env prüfen; DNS-Server anpingen.Connection RefusedPort geschlossen oder Dienst downPrüfen, ob DB-Dienst lauscht (netstat/ss/nc).SSL Certificate ErrorZertifikat abgelaufen/unbekanntCA-Bündel in der Laufzeitumgebung (Node/Java) hinterlegen.Schlechte API-LatenzWLAN-Störung oder Switch-EngpassTraceroute zur Identifikation des Flaschenhalses nutzen.FIAE-ZusammenfassungAls Anwendungsentwickler ist die Netzwerk-Infrastruktur das Fundament für jede verteilte Software. Das Verständnis von Fat vs. Thin Clients, Serverrollen, Firewalls, DMZ-Strukturen und Netzwerkmedien ermöglicht es, Anwendungen performant zu gestalten, Sicherheitszonen einzuhalten und Fehler in der Kommunikation zwischen Frontend, Backend und DDMZ (Demilitarized Zone): Zwischennetz für öffentlich erreichbare Dienste (Webserver, API-Gateway). Bei Kompromittierung bleibt das interne Netz geschützt.Servernetz / Internes LAN: Geschützter Bereich für vertrauliche Datenbanken und interne Logik.Cloud-Einbindung: Hybride Architekturen binden Cloud-Ressourcen (AWS, Azure) über sichere VPN-Tunnel (IPsec) direkt in das Unternehmensnetz ein.7. Typische Fehler & Systematic Troubleshooting für EntwicklerProblem / FehlerbildUrsache im NetzwerksystemLösungsansatz für EntwicklerHost not foundDNS-Auflösung schlägt fehlHostname in .env prüfen; DNS-Server anpingen.Connection RefusedPort geschlossen oder Dienst downPrüfen, ob DB-Dienst lauscht (netstat/ss/nc).SSL Certificate ErrorZertifikat abgelaufen/unbekanntCA-Bündel in der Laufzeitumgebung (Node/Java) hinterlegen.Schlechte API-LatenzWLAN-Störung oder Switch-EngpassTraceroute zur Identifikation des Flaschenhalses nutzen.FIAE-ZusammenfassungAls Anwendungsentwickler ist die Netzwerk-Infrastruktur das Fundament für jede verteilte Software. Das Verständnis von Fat vs. Thin Clients, Serverrollen, Firewalls, DMZ-Strukturen und Netzwerkmedien ermöglicht es, Anwendungen performant zu gestalten, Sicherheitszonen einzuhalten und Fehler in der Kommunikation zwischen Frontend, Backend und Datenbank schnell zu lokalisieren.DMZ (Demilitarized Zone): Zwischennetz für öffentlich erreichbare Dienste (Webserver, API-Gateway). Bei Kompromittierung bleibt das interne Netz geschützt.Servernetz / Internes LAN: Geschützter Bereich für vertrauliche Datenbanken und interne Logik.Cloud-Einbindung: Hybride Architekturen binden Cloud-Ressourcen (AWS, Azure) über sichere VPN-Tunnel (IPsec) direkt in das Unternehmensnetz ein.7. Typische Fehler & Systematic Troubleshooting für EntwicklerProblem / FehlerbildUrsache im NetzwerksystemLösungsansatz für EntwicklerHost not foundDNS-Auflösung schlägt fehlHostname in .env prüfen; DNS-Server anpingen.Connection RefusedPort geschlossen oder Dienst downPrüfen, ob DB-Dienst lauscht (netstat/ss/nc).SSL Certificate ErrorZertifikat abgelaufen/unbekanntCA-Bündel in der Laufzeitumgebung (Node/Java) hinterlegen.Schlechte API-LatenzWLAN-Störung oder Switch-EngpassTraceroute zur Identifikation des Flaschenhalses nutzen.FIAE-ZusammenfassungAls Anwendungsentwickler ist die Netzwerk-Infrastruktur das Fundament für jede verteilte Software. Das Verständnis von Fat vs. Thin Clients, Serverrollen, Firewalls, DMZ-Strukturen und Netzwerkmedien ermöglicht es, Anwendungen performant zu gestalten, Sicherheitszonen einzuhalten und Fehler in der Kommunikation zwischen Frontend, Backend und Datenbank schnell zu lokalisieren.DMZ (Demilitarized Zone): Zwischennetz für öffentlich erreichbare Dienste (Webserver, API-Gateway). Bei Kompromittierung bleibt das interne Netz geschützt.Servernetz / Internes LAN: Geschützter Bereich für vertrauliche Datenbanken und interne Logik.Cloud-Einbindung: Hybride Architekturen binden Cloud-Ressourcen (AWS, Azure) über sichere VPN-Tunnel (IPsec) direkt in das Unternehmensnetz ein.7. Typische Fehler & Systematic Troubleshooting für EntwicklerProblem / FehlerbildUrsache im NetzwerksystemLösungsansatz für EntwicklerHost not foundDNS-Auflösung schlägt fehlHostname in .env prüfen; DNS-Server anpingen.Connection RefusedPort geschlossen oder Dienst downPrüfen, ob DB-Dienst lauscht (netstat/ss/nc).SSL Certificate ErrorZertifikat abgelaufen/unbekanntCA-Bündel in der Laufzeitumgebung (Node/Java) hinterlegen.Schlechte API-LatenzWLAN-Störung oder Switch-EngpassTraceroute zur Identifikation des Flaschenhalses nutzen.FIAE-ZusammenfassungAls Anwendungsentwickler ist die Netzwerk-Infrastruktur das Fundament für jede verteilte Software. Das Verständnis von Fat vs. Thin Clients, Serverrollen, Firewalls, DMZ-Strukturen und Netzwerkmedien ermöglicht es, Anwendungen performant zu gestalten, Sicherheitszonen einzuhalten und Fehler in der Kommunikation zwischen Frontend, Backend und Datenbank schnell zu lokalisieren.DMZ (Demilitarized Zone): Zwischennetz für öffentlich erreichbare Dienste (Webserver, API-Gateway). Bei Kompromittierung bleibt das interne Netz geschützt.Servernetz / Internes LAN: Geschützter Bereich für vertrauliche Datenbanken und interne Logik.Cloud-Einbindung: Hybride Architekturen binden Cloud-Ressourcen (AWS, Azure) über sichere VPN-Tunnel (IPsec) direkt in das Unternehmensnetz ein.7. Typische Fehler & Systematic Troubleshooting für EntwicklerProblem / FehlerbildUrsache im NetzwerksystemLösungsansatz für EntwicklerHost not foundDNS-Auflösung schlägt fehlHostname in .env prüfen; DNS-Server anpingen.Connection RefusedPort geschlossen oder Dienst downPrüfen, ob DB-Dienst lauscht (netstat/ss/nc).SSL Certificate ErrorZertifikat abgelaufen/unbekanntCA-Bündel in der Laufzeitumgebung (Node/Java) hin
