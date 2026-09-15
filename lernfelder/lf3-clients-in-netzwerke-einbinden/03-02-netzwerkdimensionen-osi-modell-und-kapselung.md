# 03-02: LF 3.2 Kommunikation begreifen – Netzwerkgrundlagen, OSI-Modell & Kommunikationsablauf

Dieses Modul bietet eine umfassende Analyse der Netzwerkarchitektur: Von der räumlichen Einteilung über Standardisierungsgremien und das 7-Schichten-OSI-Modell bis hin zum exakten Protokoll-Zusammenspiel bei Webanforderungen und dem systematischen Bottom-Up-Troubleshooting.

---

## 1. Netzwerkausdehnung & Reichweiten-Klassifikation

Netzwerke werden nach ihrer physischen Ausdehnung, den eingesetzten Übertragungsmedien, Geschwindigkeiten und Betreibermodellen unterteilt:

| Netzwerkart | Vollständiger Name | Räumliche Abdeckung | Typische Übertragungsmedien | FIAE- & Praxis-Kontext |
| :--- | :--- | :--- | :--- | :--- |
| **PAN** | Personal Area Network | ~1–10 Meter | Bluetooth, NFC, USB | Anbindung mobiler Peripheriegeräte, Smartcards, Bluetooth-Beacons. |
| **LAN** | Local Area Network | Gebäude / Campus | Ethernet (Kupfer S/FTP), WLAN | Zugriff auf lokale Dev-Server, Datenbanken, Git-Repositories, CI/CD-Node. |
| **MAN** | Metropolitan Area Network | Stadtgebiet (~10–100 km) | Glasfaser (City-Ringe), Dark Fiber | Anbindung verschiedener Unternehmensstandorte innerhalb einer Region. |
| **WAN** | Wide Area Network | Länder / Kontinente | Glasfaser, Satellit, MPLS-VPN | Anbindung von Cloud-Infrastrukturen (AWS, Azure), verteilte Rechenzentren. |
| **GAN** | Global Area Network | Weltumspannend | Seekabel, Satellitennetze | Transatlantische Netzverbindungen, globale Unternehmensnetze. |

---

## 2. Standardisierungsgremien & Internet-Standards

Einheitliche Standards garantieren, dass Hard- und Software unterschiedlicher Hersteller reibungslos miteinander kommunizieren können.

### 1. ISO (International Organization for Standardization)
* **Aufgabe:** Globale Entwicklung von Industrie- und Schnittstellenstandards.
* **Bedeutung:** Urheberin des **OSI-Referenzmodells** (ISO/IEC 7498-1) und relevanter IT-Sicherheitsnormen (z. B. ISO/IEC 27001).

### 2. IETF (Internet Engineering Task Force)
* **Aufgabe:** Technische Weiterentwicklung und Standardisierung der Internet-Architektur.
* **Bedeutung:** Veröffentlichung von **RFCs (Request for Comments)**, welche als offizielle Protokoll-Spezifikationen dienen.
* **Relevante RFC-Beispiele für Softwareentwickler:**
  * **RFC 791:** Internet Protocol (IPv4)
  * **RFC 793:** Transmission Control Protocol (TCP)
  * **RFC 9110:** HTTP Semantics (REST-APIs, Statuscodes, Header)
  * **RFC 7519:** JSON Web Token (JWT für Authentifizierung)

### 3. IEEE (Institute of Electrical and Electronics Engineers)
* **Aufgabe:** Standardisierung physikalischer Signale, Kabel und Übertragungstechniken auf den unteren Schichten (Layer 1 & 2).
* **Bedeutung:**
  * **IEEE 802.3:** Ethernet (kabelgebunden)
  * **IEEE 802.11:** WLAN / Wi-Fi-Standards (802.11ax/be)
  * **IEEE 802.1Q:** VLAN-Tagging

---

## 3. Das 7-Schichten-OSI-Modell im Detail

Das OSI-Modell (Open Systems Interconnection) strukturiert die Netzwerkkommunikation in 7 abstrahierte Ebenen. Jede Schicht nutzt die Dienste der darunterliegenden Schicht und stellt der darüberliegenden Schicht eigene Funktionen bereit.

```text
+-----------------------------------------------------------------+
| Layer 7: Anwendung (Application)     -> Interface zum Anwender  |
| Layer 6: Darstellung (Presentation)  -> Formatierung & TLS/SSL  |
| Layer 5: Sitzung (Session)           -> Verbindungssteuerung    |
+-----------------------------------------------------------------+  <- Anwendungsorientiert
| Layer 4: Transport (Transport)       -> End-to-End & Ports      |
| Layer 3: Netzwerk (Network)          -> Routing & IP-Adressen   |
| Layer 2: Sicherung (Data Link)       -> MAC-Adressen & Frames   |
| Layer 1: Bitübertragung (Physical)   -> Signale & Hardware      |
+-----------------------------------------------------------------+  <- Transportorientiert

3. Sockets & Netzwerk-PortsEin Port ist eine 16-Bit-Zahl (0 bis 65535), die Datenpakete auf einem Zielsystem der korrekten Anwendung zuordnet.Die eindeutige Verbindungsschnittstelle aus IP-Adresse + Port nennt man Socket (z. B. 192.168.1.100:5432).Port-Klassifizierung nach IANAWell-Known Ports (0 – 1023): Reserviert für standardisierte Systemdienste (z. B. HTTP, HTTPS, SSH).Registered Ports (1024 – 49151): Registriert für spezifische Datenbanken, Frameworks und Anwendungen.Dynamic / Private Ports (49152 – 65535): Temporäre Ports, die Betriebssysteme für ausgehende Client-Verbindungen vergeben.Entwickler-PortreferenzPortDienst / ProtokollStandard-Einsatz / Relevanz in der Softwareentwicklung21FTPUnverschlüsselter Dateitransfer22SSH / SFTPSichere Konsolenverbindung, Remote-Deployment & SFTP53DNSNamensauflösung (nutzt primär UDP, bei großen Zonen TCP)80HTTPUnverschlüsselte Webseiten & APIs443HTTPSVerschlüsselte Webseiten & REST-APIs (TLS/SSL)1433MS SQL ServerStandard-Port für Microsoft SQL Server3306MySQL / MariaDBStandard-Port für MySQL- & MariaDB-Datenbanken5432PostgreSQLStandard-Port für PostgreSQL-Datenbanken6379RedisIn-Memory Cache & Key-Value Store8080HTTP-AlternateHäufiger Port für lokale Entwicklungs-Server (Node, Spring, Vue)27017MongoDBStandard-Port für MongoDB NoSQL-Datenbanken4. Firewalls & NetzwerksicherheitEine Firewall überwacht und filtert den ein- und ausgehenden Datenverkehr anhand festgelegter Regelwerke.Firewall-ArtenPaketfilter (Stateless): Prüft Pakete isoliert nach Quell-/Ziel-IP, Port und Protokoll.Stateful Inspection: Verfolgt den Zustand von Verbindungen (z. B. ob ein eingehendes Paket die Antwort auf eine eigene Anfrage ist).Application Level Gateway (Next-Gen Firewall): Untersucht Nutzdaten auf Layer 7 (z. B. Erkennung von SQL-Injections oder Schadcode).5. Praxis: Firewall-Konfiguration für EntwicklerLinux (ufw - Uncomplicated Firewall)Bash# Status & aktive Regeln anzeigen
sudo ufw status verbose

# Standard: Eingehung blockieren, Ausgehend erlauben
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Ports 22 (SSH) und 443 (HTTPS) freigeben
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp

# Datenbank-Zugriff (Port 5432) nur für ein bestimmtes Entwickler-Subnetz erlauben
sudo ufw allow from 192.168.1.0/24 to any port 5432 proto tcp

# Firewall aktivieren
sudo ufw enable
