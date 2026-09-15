# LF3: Clients in Netzwerke einbinden

Am Ende dieses Lernfelds haben die Auszubildenden weitreichende Fähigkeiten erworben, die über reines Auswendiglernen hinausgehen. Im Fokus stehen die hohen kognitiven Level der Bloomschen Taxonomie:

- **Analysieren (K4):** Die Lernenden können komplexe Netzwerkfehler systematisch anhand des 7-Schichten-OSI-Modells eingrenzen (Bottom-Up-Troubleshooting mittels Ping, Traceroute, Netstat und System-Logs).
- **Beurteilen (K5):** Die Lernenden können Übertragungsmedien, Netzwerktopologien und WAN-Zugangstechnologien bewerten und für spezifische Unternehmensszenarien (Störquellen, Bandbreitenbedarf, Ausfallsicherheit) die technisch und wirtschaftlich beste Wahl treffen.
- **Entwerfen (K5):** Die Lernenden können logische Netzwerkstrukturen (IPv4/IPv6-Subnetze, VLAN-Trennung) sowie ganzheitliche Sicherheitskonzepte (Dateifreigabe-Berechtigungen, Zonen-Firewalls, WLAN-Standards) für ein KMU konzipieren.
- **Entwickeln (K6):** Die Lernenden können ein funktionierendes, plattformübergreifendes Client-Setup (Linux/Windows) inklusive dynamischer Adressvergabe (DHCP), Namensauflösung (DNS) und sicherer WLAN-Anbindung konstruieren und in Live-Demos verteidigen.

## Lern-Reise (Überblick Lern-Epics)

Die Struktur des Lernfelds folgt dem Weg der Daten – vom lokalen PC bis hinaus in das weltweite Internet. Das Wissen wird in agilen Sprints erarbeitet und in Sprint Reviews anhand von "Ganzheitlichen Aufgaben" (GA) praktisch demonstriert.

- **Epic 1: Das Fundament (Mini-Netzwerk)**
  - _Inhalte:_ Physische Verbindung, IPv4/IPv6 Adressierung & Subnetting, Dual-Stack, Automatisierung durch DHCP & DNS, plattformübergreifende Dateifreigaben (SMB) inkl. DSGVO-Sensibilisierung.
  - _Meilenstein:_ Ein funktionierendes, per Ping und Dateiaustausch überprüfbares LAN zwischen Windows- und Linux-Systemen.
- **Epic 2: Die Anatomie der Daten (Das OSI-Modell)**
  - _Inhalte:_ Das 7-Schichten-Modell, Kapselung, LAN/WAN-Dimensionen, Transportprotokolle (TCP/UDP), Ports, lokale Firewalls und Dienste.
  - _Meilenstein:_ Ein interaktives Fehlerbehebungs-Flowchart und das erfolgreiche Live-Troubleshooting eines vom Dozenten sabotierten Netzwerks.
- **Epic 3: Vom Keller bis zum Schreibtisch (Infrastruktur)**
  - _Inhalte:_ Netzwerktopologien (Stern, Mesh), Übertragungsmedien (Kupfer S/FTP, Glasfaser), Strukturierte Verkabelung (Primär/Sekundär/Tertiär), Stecker und aktive/passive Komponenten.
  - _Meilenstein:_ Ein gezeichneter, physischer Gebäude-Netzplan inkl. Hardware-Stückliste für das Szenario-Unternehmen.
- **Epic 4: Der Client im Fokus (WLAN & VLAN)**
  - _Inhalte:_ WLAN-Diagnose auf dem Client (`nmcli`, `wpa_supplicant`), Access Point Emulatoren, Funkphysik (DFS, EIRP), Standards (Wi-Fi 6, WPA3), Captive Portals sowie die logische Segmentierung mittels VLANs (Tagged/Untagged).
  - _Meilenstein:_ Live-WLAN-Analyse und ein Pitch zur AP- und Switch-Konfiguration im Enterprise-Emulator.
- **Epic 5: Der Gateway zur Welt (WAN & Routing)**
  - _Inhalte:_ Client-Routing (Default Gateway), WAN-Zugänge (FTTx, DOCSIS, DS-Lite), NAT (Masquerading) & Zonen-Firewalls im OpenWrt-Emulator, moderne Standortvernetzung (SD-WAN, VPN) und Cloud-Modelle.
 

  - _Meilenstein:_ Die Live-Demo der Firewall-Sandbox und ein Architektur-Konzept zur sicheren Anbindung einer neuen Filiale.
