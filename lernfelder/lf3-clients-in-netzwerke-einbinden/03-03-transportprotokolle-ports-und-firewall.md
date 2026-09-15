# 03-03: Transportprotokolle, Ports & Firewall (LF 3.2)

Dieses Modul behandelt die Unterschiede zwischen TCP und UDP, die Bedeutung von Netzwerk-Ports und Sockets sowie die Konfiguration lokaler Firewalls (Windows & Linux).

---

## 1. Transportprotokolle im Vergleich: TCP vs. UDP

Auf Schicht 4 (Transport Layer) wird festgelegt, wie Datenpakete transportiert werden:

| Kriterium | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
| :--- | :--- | :--- |
| **Verbindungsaufbau** | **Verbindungsorientiert** (Drei-Wege-Handschlag) | **Verbindungslos** (Send & Forget) |
| **Zuverlässigkeit** | Hoch (Verlorene Pakete werden erneut angefordert) | Keine Übertragungsgarantie |
| **Reihenfolge** | Garantiert (Pakete werden sortiert) | Keine Sortierung |
| **Flusskontrolle** | Ja (Sliding Window Mechanism) | Nein |
| **Overhead** | Hoch (Mindestens 20 Byte Header) | Gering (8 Byte Header) |
| **Einsatzbereiche** | HTTP/HTTPS, Datenbanken, SSH, E-Mail, Git | DNS, Video-Streaming, VoIP, Online-Games |

---

## 2. Netzwerk-Ports & Standard-Ports

Ein **Port** ist eine 16-Bit-Zahl (`0` bis `65535`), die festlegt, an welche Anwendung auf einem Zielsystem Daten geliefert werden. Die Kombination aus **IP-Adresse + Port** nennt man **Socket** (z. B. `192.168.1.50:5432`).

### Wichtige Standard-Ports für Entwickler

| Port | Dienst / Protokoll | Beschreibung / Nutzung |
| :---: | :--- | :--- |
| **21** | FTP | Dateiübertragung (unverschlüsselt) |
| **22** | SSH / SFTP | Sichere Konsole & Dateitransfer |
| **53** | DNS | Namensauflösung (meist UDP) |
| **80** | HTTP | Unverschlüsseltes Web |
| **443** | HTTPS | Verschlüsseltes Web (TLS/SSL) |
| **3306** | MySQL / MariaDB | Standard-Port für MySQL-Datenbanken |
| **5432** | PostgreSQL | Standard-Port für PostgreSQL-Datenbanken |
| **6379** | Redis | In-Memory Key-Value Store |
| **8080** | HTTP-Alternate | Häufig genutzt für lokale Dev-Server (Node, Spring) |

---

## 3. Konfiguration lokaler Firewalls

Eine Firewall filtert den Datenverkehr anhand von IP-Adressen, Ports und Protokollen.

### Linux (Uncomplicated Firewall - `ufw`)
```bash
# Status der Firewall prüfen
sudo ufw status

# Port 22 (SSH) und Port 443 (HTTPS) freigeben
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp

# Zugriffe auf PostgreSQL (Port 5432) nur aus dem lokalen Entwicklernetz zulassen
sudo ufw allow from 192.168.1.0/24 to any port 5432 proto tcp

# Firewall aktivieren
sudo ufw enable

Windows Defender Firewall (PowerShell)

# Inbound-Regel für lokalen Node.js-Dev-Server (Port 8080) erstellen
New-NetFirewallRule -Name "Allow_Dev_8080" -DisplayName "NodeJS Dev Server" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8080