# 03-02: Netzwerkeinführung – Protokolle & Webseitenaufruf 

Dieses Modul behandelt die Zuordnung der wichtigsten Netzwerkprotokolle zum OSI-Modell sowie den schrittweisen Ablauf einer Netzwerkanforderung (Webseitenaufruf) aus Sicht der Anwendungsentwicklung.

---

## 1. Protokolle & ihre OSI-Schichten-Zuordnung

Protokolle definieren die exakten Syntax- und Semantik-Regeln für die Kommunikation zwischen IT-Systemen.

| OSI-Schicht | Protokoll | Primäre Funktion / Aufgabe |
| :--- | :--- | :--- |
| **Layer 7 (Application)** | **HTTP / HTTPS** | Übertragung von Webseiten, REST-APIs und Web-Ressourcen. |
| | **DNS** | Übersetzt Hostnamen (`api.dev.local`) in IP-Adressen. |
| | **DHCP** | Automatische Vergabe von IP-Adressen und Netzwerkeinstellungen. |
| **Layer 4 (Transport)** | **TCP** | Verbindungsorientiert, garantiert fehlerfreie Übertragung. |
| | **UDP** | Verbindungslos, schnelles Streaming/Echtzeit ohne Zustellgarantie. |
| **Layer 3 (Network)** | **IP (IPv4 / IPv6)**| Logische Adressierung und paketbasiertes Routing. |
| | **ICMP** | Diagnosemeldungen (Grundlage für `ping` und `traceroute`). |
| **Layer 2 (Data Link)** | **Ethernet** | Frames-Übertragung im lokalen Netz (LAN) via MAC-Adressen. |
| | **ARP** | Löst IPv4-Adressen in physikalische MAC-Adressen auf (IP -> MAC). |

---

## 2. Das Protokoll-Zusammenspiel beim Webseitenaufruf

Was passiert auf Protokollebene, wenn ein Entwickler `https://api.unternehmen.de` im Browser aufruft?

1. **DNS-Anfrage:** Browser löst `api.unternehmen.de` via DNS in eine IP-Adresse auf (z. B. `203.0.113.45`).
2. **ARP-Anfrage:** Client sucht die MAC-Adresse des Default Gateways via ARP-Broadcast.
3. **TCP-Handshake:** 3-Way-Handshake (`SYN` -> `SYN-ACK` -> `ACK`) stellt eine Verbindung zu Port 443 her.
4. **TLS-Handshake:** Zertifikatsprüfung & Aushandlung der Verschlüsselung.
5. **HTTP-Request:** Client sendet `GET /data HTTP/1.1`.
6. **HTTP-Response:** Server antwortet mit `200 OK` und liefert die JSON-Nutzlast.

---

## FIAE-Zusammenfassung

Das Verständnis des Zusammenspiels von DNS, ARP, TCP und HTTP ermöglicht es Entwicklern, Netzwerk-Latenzen bei API-Anfragen zu verstehen und Verbindungsfehler im Frontend/Backend präzise zu lokalisieren.

