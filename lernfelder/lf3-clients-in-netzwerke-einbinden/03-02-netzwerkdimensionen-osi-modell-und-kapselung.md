code lernfelder/lf3-clients-in-netzwerke-einbinden/03-03-netzwerkprotokolle-transport-und-firewall.md
# 03-02: LF 3.2 Kommunikation begreifen – Dimensionen, OSI-Modell & Kapselung

Dieses Modul behandelt die Klassifizierung von Netzwerken nach ihrer Ausdehnung, die Bedeutung globaler Standardisierungsgremien, die Architektur des 7-Schichten-OSI-Modells inklusive Datenkapselung sowie den systematischen Bottom-Up-Troubleshooting-Ansatz.

---

## 1. Klassifizierung von Netzwerken nach physischer Ausdehnung (K2)

Netzwerke werden anhand ihrer räumlichen Abdeckung, Übertragungsmedien, Geschwindigkeiten und Betreibermodelle klassifiziert:

| Netzwerkart | Name | Ausdehnung | Übertragungsmedien | FIAE- & Praxis-Kontext |
| :--- | :--- | :--- | :--- | :--- |
| **PAN** | Personal Area Network | ~1–10 m | Bluetooth, NFC, USB | Anbindung mobiler Peripherie, Smartcards, Bluetooth-Beacons. |
| **LAN** | Local Area Network | Gebäude / Campus | Ethernet (Kupfer S/FTP), WLAN | Zugriff auf lokale Dev-Server, Datenbanken, Git-Repositories. |
| **MAN** | Metropolitan Area Network| Stadtgebiet (~10–100 km)| Glasfaser (City-Ringe), Dark Fiber | Anbindung von Firmenstandorten innerhalb einer Metropole. |
| **WAN** | Wide Area Network | Länder / Weltweit | DSL, Glasfaser, Satellit, MPLS | Cloud-Infrastrukturen (AWS, Azure), Internet-Anbindung. |
| **GAN** | Global Area Network | Weltumspannend | Satellitennetze, Seekabel | Globale Unternehmensnetze, hochgradig verteilte Systeme. |

---

## 2. Standardisierungsgremien & ihre Relevanz (K2)

Einheitliche Protokolle und Schnittstellen garantieren die Interoperabilität zwischen verschiedenen Herstellern, Betriebssystemen und Software-Runtimes.

### 1. ISO (International Organization for Standardization)
* **Hauptaufgabe:** Entwicklung internationaler Industrie- und Technologiestandards.
* **Relevanz:** Entwicklerin des **OSI-Referenzmodells** (ISO/IEC 7498-1) sowie von Sicherheitsstandards wie ISO/IEC 27001 (Informationssicherheit).

### 2. IETF (Internet Engineering Task Force)
* **Hauptaufgabe:** Technische Weiterentwicklung der Internet-Architektur.
* **Relevanz:** Dokumentiert Standards in **RFCs (Request for Comments)**.
* **Beispiele für Entwickler:**
  * **RFC 791:** Internet Protocol (IPv4)
  * **RFC 793:** Transmission Control Protocol (TCP)
  * **RFC 9110:** HTTP Semantics & Protocol
  * **RFC 7519:** JSON Web Token (JWT)

### 3. IEEE (Institute of Electrical and Electronics Engineers)
* **Hauptaufgabe:** Standardisierung von Hardware-, Übertragungs- und Netzwerkschichten (Layer 1 und Layer 2).
* **Relevanz:** 
  * **IEEE 802.3:** Ethernet-Standards (Kabelgebundene Netze).
  * **IEEE 802.11:** WLAN / Wi-Fi-Standards.
  * **IEEE 802.1Q:** VLAN-Tagging.

---

## 3. Das 7-Schichten-OSI-Modell (K2)

Das OSI-Modell (Open Systems Interconnection) gliedert die Netzwerkkommunikation in 7 abstrahierte Schichten. Jede Schicht erfüllt wohldefinierte Aufgaben und stellt der übergeordneten Schicht ihre Dienste bereit.

### Übersicht der 7 OSI-Schichten

| Schicht (Layer) | Name | Hauptaufgabe | Protocol Data Unit (PDU) | Protokolle & Komponenten |
| :---: | :--- | :--- | :--- | :--- |
| **7** | **Anwendung (Application)** | Schnittstelle zur Anwendungssoftware / User | Daten (Data) | HTTP, HTTPS, REST-API, SSH, DNS, SMTP |
| **6** | **Darstellung (Presentation)**| Formatierung, Encrypting/Decrypting, Komprimierung | Daten (Data) | TLS/SSL, JSON, XML, UTF-8, Base64, JPEG |
| **5** | **Sitzung (Session)** | Sitzungssteuerung, Dialogkontrolle, Checkpoints | Daten (Data) | WebSockets, RPC, Named Pipes, NetBIOS |
| **4** | **Transport (Transport)** | Ende-zu-Ende-Verbindung, Port-Adressierung | Segment (TCP) / Datagramm (UDP) | TCP, UDP |
| **3** | **Netzwerk (Network)** | Logische Adressierung (IP) & Paket-Routing | Paket (Packet) | IPv4, IPv6, ICMP, IPsec |
| **2** | **Sicherung (Data Link)** | Physikalische Adressierung (MAC) & Fehlererkennung | Frame (Datenframe) | Ethernet, ARP, Wi-Fi (802.11), Switch |
| **1** | **Bitübertragung (Physical)**| Physikalische Bitübertragung (Spannung, Licht)| Bits | Netzwerkkabel, RJ45, LWL, Hub, Repeater |

---

## 4. Datenkapselung & Dekapselung (K2)

Beim Versenden von Daten durchläuft eine Nachricht die Schichten von **Layer 7 nach Layer 1**. Jede Schicht fügt den empfangenen Daten eigene Steuerinformationen (**Header** und ggf. **Trailer**) hinzu (**Kapselung**).

```text
[Layer 7 - Application]    ->  { Nutzdaten / JSON Payload }
                                          |
[Layer 4 - Transport]      ->  [TCP Header] + { Nutzdaten }                        = TCP-Segment
                                          |
[Layer 3 - Network]        ->  [IP Header] + [TCP Header] + { Nutzdaten }           = IP-Paket
                                          |
[Layer 2 - Data Link]      ->  [MAC Header] + [IP Header] + [TCP Header] + { Payload } + [FCS Trailer] = Ethernet Frame
                                          |
[Layer 1 - Physical]       ->  01101001 01101110 01110100 01100101 ...             = Physikalische Bits

5. Systematisches Troubleshooting: Der Bottom-Up-Ansatz (K4)
Beim Bottom-Up-Troubleshooting wird die Fehlersuche strukturiert auf Layer 1 begonnen und schrittweise bis zu Layer 7 hochgearbeitet. Das verhindert vorschnelle Fehldiagnosen in der Softwareentwicklung.

Layer 7 (Application)  ---> Prüfen: Reagiert der Dienst/API? (curl, Postman, Browser)
  ^
Layer 4 (Transport)    ---> Prüfen: Ist der Port offen & lauscht der Dienst? (netstat, ss, nc)
  ^
Layer 3 (Network)      ---> Prüfen: Ist die Ziel-IP erreichbar? Routing OK? (ping, traceroute)
  ^
Layer 2 (Data Link)    ---> Prüfen: Ist eine IP/MAC zugewiesen? ARP korrekt? (ip a, arp -a)
  ^
Layer 1 (Physical)     ---> Prüfen: Kabel eingesteckt? Link-LEDs grün? WLAN verbunden?

Anwendungsbeispiel für Entwickler
Problem: Ein Node.js-Backend meldet Database Connection Timeout.

Layer 1 & 2: Netzwerkkarte aktiv, Link-LED grün, IP-Adresse vorhanden (ip a).

Layer 3: Datenbank-Server lässt sich anpingen (ping 192.168.1.50). -> Verbindung steht!

Layer 4: Test des Datenbank-Ports mit Netcat (nc -zv 192.168.1.50 5432). -> Ergebnis: Connection Refused!

Analyse: Der Fehler liegt auf Layer 4 (PostgreSQL-Dienst läuft nicht oder die Firewall blockiert Port 5432). Schichten 1–3 arbeiten fehlerfrei.

---

### Block 2: `03-03-netzwerkprotokolle-transport-und-firewall.md`

```markdown
# 03-03: LF 3.2 Kommunikation begreifen – Protokolle, Transport & Firewall

Dieses Modul vertieft die Zuordnung wesentlicher Netzwerkprotokolle zum OSI-Modell, analysiert den Ablauf eines Webseitenaufrufs, vergleicht TCP und UDP, behandelt Netzwerk-Ports sowie die Konfiguration lokaler Firewalls.

---

## 1. Protokolle & ihre OSI-Schichten-Zuordnung (K2)

Protokolle definieren die exakten Syntax- und Semantik-Regeln für die Kommunikation zwischen IT-Systemen.

| OSI-Schicht | Protokoll | Primäre Funktion / Aufgabe |
| :--- | :--- | :--- |
| **Layer 7 (Application)** | **HTTP / HTTPS** | Übertragung von Webseiten, REST-APIs und Web-Ressourcen. |
| | **DNS** | Übersetzt Hostnamen (`api.dev.local`) in IP-Adressen. |
| | **DHCP** | Automatische Vergabe von IP-Adressen und Netzwerkeinstellungen. |
| **Layer 4 (Transport)** | **TCP** | Verbindungsorientiert, garantiert fehlerfreie & vollständige Datenübertragung. |
| | **UDP** | Verbindungslos, schnelles Streaming/Echtzeit ohne Zustellgarantie. |
| **Layer 3 (Network)** | **IP (IPv4 / IPv6)**| Logische Adressierung und paketbasiertes Routing über Netze hinweg. |
| | **ICMP** | Fehler- und Diagnosemeldungen (Grundlage für `ping` und `traceroute`). |
| **Layer 2 (Data Link)** | **Ethernet** | Frames-Übertragung im lokalen Netz (LAN) via MAC-Adressen. |
| | **ARP** | Löste IPv4-Adressen in physikalische MAC-Adressen auf (**IP -> MAC**). |

---

## 2. Das Protokoll-Zusammenspiel beim Webseitenaufruf (K3)

Was passiert auf Protokollebene, wenn ein Entwickler `https://api.unternehmen.de` im Browser aufruft?

```text
1. DNS-Anfrage   ---> Browser löst "api.unternehmen.de" via DNS in IP-Adresse auf (z. B. 203.0.113.45).
2. ARP-Anfrage   ---> Client sucht die MAC-Adresse des Default Gateways via ARP-Broadcast.
3. TCP-Handshake ---> 3-Way-Handshake (SYN -> SYN-ACK -> ACK) stellt Verbindung zu Port 443 her.
4. TLS-Handshake ---> Zertifikatsprüfung & Aushandlung der Verschlüsselung.
5. HTTP-Request  ---> Client sendet "GET /data HTTP/1.1".
6. HTTP-Response ---> Server antwortet mit "200 OK" und liefert die JSON-Nutzlast.
3. Transportprotokolle im Vergleich: TCP vs. UDP (K2)Auf Schicht 4 (Transport Layer) wird festgelegt, wie Datenpakete transportiert werden:KriteriumTCP (Transmission Control Protocol)UDP (User Datagram Protocol)VerbindungsaufbauVerbindungsorientiert (Drei-Wege-Handschlag)Verbindungslos (Send & Forget)ZuverlässigkeitHoch (Verlorene Pakete werden erneut angefordert)Keine ÜbertragungsgarantieReihenfolgeGarantiert (Pakete werden sortiert)Keine SortierungFlusskontrolleJa (Sliding Window Mechanism)NeinOverheadHoch (Mindestens 20 Byte Header)Gering (8 Byte Header)EinsatzbereicheHTTP/HTTPS, Datenbanken, SSH, E-Mail, GitDNS-Abfragen, Video-Streaming, VoIP, Online-Games4. Netzwerk-Ports & Standard-Ports (K2)Ein Port ist eine 16-Bit-Zahl (0 bis 65535), die festlegt, an welche Anwendung auf einem Zielsystem Daten geliefert werden. Die Kombination aus IP-Adresse + Port nennt man Socket (z. B. 192.168.1.50:5432).Wichtige Standard-Ports für EntwicklerPortDienst / ProtokollBeschreibung / Nutzung21FTPDateiübertragung (unverschlüsselt)22SSH / SFTPSichere Konsole & Dateitransfer53DNSNamensauflösung (meist UDP)80HTTPUnverschlüsseltes Web443HTTPSVerschlüsseltes Web (TLS/SSL)3306MySQL / MariaDBStandard-Port für MySQL-Datenbanken5432PostgreSQLStandard-Port für PostgreSQL-Datenbanken6379RedisIn-Memory Key-Value Store8080HTTP-AlternateHäufig genutzt für lokale Dev-Server (Node, Spring, Tomcat)5. Konfiguration lokaler Firewalls (K3)Eine Firewall filtert den Datenverkehr anhand von IP-Adressen, Ports und Protokollen.Linux (Uncomplicated Firewall - ufw)Bash# Status der Firewall prüfen
sudo ufw status

# Port 22 (SSH) und Port 443 (HTTPS) freigeben
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp

# Zugriffe auf PostgreSQL (Port 5432) nur aus dem lokalen Entwicklernetz zulassen
sudo ufw allow from 192.168.1.0/24 to any port 5432 proto tcp

# Firewall aktivieren
sudo ufw enable
Windows Defender Firewall (PowerShell)PowerShell# Inbound-Regel für lokalen Node.js-Dev-Server (Port 8080) erstellen
New-NetFirewallRule -Name "Allow_Dev_8080" -DisplayName "NodeJS Dev Server" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8080