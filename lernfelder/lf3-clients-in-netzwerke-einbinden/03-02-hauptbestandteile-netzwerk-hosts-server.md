# 03-02: Hauptbestandteile von Computernetzen (Hosts & Server)

Ein Computernetzwerk bildet das Gesamtsystem aus Endgeräten, Servern und Anwendungs-Infrastrukturen. Für Anwendungsentwickler (FIAE) ist dieses Verständnis essenziell, um verteilte Anwendungen, API-Endpunkte und Datenbankverbindungen stabil zu betreiben.

---

## 1. Das Netzwerk als Gesamtsystem der Software-Kommunikation

Damit eine moderne Anwendung Daten austauschen kann, müssen alle Ebenen der Netzwerk-Infrastruktur nahtlos zusammenarbeiten:

| Bereich | Bedeutung im Software-Lebenszyklus |
| :--- | :--- |
| **Geräte & Hosts** | Entwickler-PCs, Test-Clients, Datenbank-Server, API-Gateways |
| **Verbindung & Medien** | Gigabit-Ethernet, Glasfaser (Rechenzentrum), Wi-Fi, VPN-Tunnel |
| **Adressierung** | Eindeutige Zuweisung von MAC-Adressen, IP-Adressen und Hostnamen |
| **Protokolle & Dienste**| HTTP/HTTPS, TCP/UDP, DNS, DHCP, REST/GraphQL, WebSockets |
| **Sicherheitszonen** | Firewalls, DMZ, CORS-Policies, Subnetz-Segmentierung |

---

## 2. Endgeräte & Client-Klassifizierung aus Entwicklersicht

Anwendungen laufen auf unterschiedlichsten Endgeräten (Hosts). Je nach Client-Architektur ändern sich die Anforderungen an Rechenleistung, Speicher und Netzwerkstabilität:

| Client-Art | Erklärung & Funktionsweise | AE- / Entwickler-Perspektive |
| :--- | :--- | :--- |
| **Fat Client** | Eigenständige Rechenleistung & lokaler Speicher. Anwendung läuft direkt auf dem Gerät. | Hohe Anforderungen an lokale Ressourcen; Benötigt lokale DB-Treiber. |
| **Thin Client** | Minimalistische Hardware. Berechnung und Logik laufen zentral auf Servern. | Webbasierte UIs; Minimale lokale Datenhaltung. |
| **Web Client** | Ausführung im Webbrowser (Single Page Applications in React, Angular, Vue). | Rendering im Browser; Datenaustausch via REST/GraphQL und JSON. |
| **Mobile Client** | Smartphones/Tablets (iOS, Android) in wechselnden Netzen. | Robustes Handling von Verbindungsabbrüchen (Offline-First-Strategien). |
| **Remote Client** | Zugriff aus dem Homeoffice über verschlüsselte VPN-Tunnel. | Zugriff auf geschützte interne Staging-Datenbanken und Git-Repositories. |

---

## 3. Servertypen & Rollen in der Software-Architektur

In modernen Anwendungsarchitekturen arbeiten spezialisierte Serverrollen zusammen:

* **Applikationsserver:** Führt die Geschäftslogik aus (z. B. Node.js, Spring Boot, .NET Core, Django).
* **Datenbankserver:** Speichert und verwaltet strukturierte Daten (z. B. PostgreSQL, MySQL, MongoDB).
* **Webserver / Reverse Proxy:** Nginx, Apache oder Traefik zur Verteilung von HTTP-Anfragen und SSL-Offloading.
* **DNS- & DHCP-Server:** Zentrale Infrastruktur zur Adressvergabe und Namensauflösung (`db.internal`).
* **Authentifizierungsserver:** Keycloak/Auth0 zur Verifizierung von Logins und JWT-Tokens.
