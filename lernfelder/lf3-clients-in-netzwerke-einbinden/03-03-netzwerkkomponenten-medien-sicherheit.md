# 03-03: Netzwerkkomponenten, Medien & Sicherheitszonen

Dieses Modul behandelt aktive und passive Netzwerkkomponenten, Übertragungsmedien, Sicherheitszonen (DMZ) sowie die systematische Fehlersuche aus Sicht der Anwendungsentwicklung.

---

## 1. Active & Passive Netzwerkkomponenten

Netzwerkgeräte verbinden Systeme und leiten Datenverkehr zielgerichtet weiter:

| Komponente | Hauptaufgabe | Relevanz für Softwareentwickler |
| :--- | :--- | :--- |
| **Switch (Layer 2)** | Verbindet Geräte im LAN via MAC-Adresse. | Beeinflusst Latenzen im internen Netzwerk (Cluster-Performance). |
| **Router (Layer 3)** | Verbindet Netze via IP-Adresse (Default Gateway). | Leitet Anfragen an externe APIs oder Cloud-Dienste weiter. |
| **Firewall** | Filtert Datenverkehr nach Regelwerken & Ports. | Häufiger Grund für `Connection Timeout` bei DB-/API-Zugriffen. |
| **Access Point** | Wandelt kabelgebundenes LAN in WLAN um. | Testumgebung für mobile Apps unter schwankenden Signalstärken. |
| **Load Balancer** | Verteilt Anfragen auf mehrere Server-Instanzen. | Erfordert zustandslose (stateless) Anwendungskonzepte. |

---

## 2. Übertragungsmedien: Eigenschaften & Performance-Faktoren

* **Kupferkabel (Cat 6A / Cat 7):** Standard im Büro/LAN; Günstig, RJ45-Stecker, bis 100m Länge.
* **Glasfaser (LWL):** Höchste Bandbreiten, keine elektromagnetische Störanfälligkeit. Einsatz im Rechenzentrum.
* **WLAN (Wi-Fi 6 / 6E):** Drahtlos, flexibel, aber geteiltes Medium (Shared Medium) mit schwankender Latenz.

---

## 3. Netzbereiche & Sicherheitszonen (DMZ & Internes LAN)

Eine professionelle IT-Architektur trennt Netzbereiche nach Schutzbedarf:

* **DMZ (Demilitarized Zone):** Zwischennetz für öffentlich erreichbare Dienste (Webserver, API-Gateway). Bei Kompromittierung bleibt das interne Netz geschützt.
* **Servernetz / Internes LAN:** Geschützter Bereich für vertrauliche Datenbanken und interne Logik.
* **Cloud-Einbindung:** Hybride Architekturen binden Cloud-Ressourcen (AWS, Azure) über sichere VPN-Tunnel ein.

---

## 4. Typische Fehler & Systematic Troubleshooting für Entwickler

| Problem / Fehlerbild | Ursache im Netzwerksystem | Lösungsansatz für Entwickler |
| :--- | :--- | :--- |
| `Host not found` | DNS-Auflösung schlägt fehl | Hostname in `.env` prüfen; DNS-Server anpingen. |
| `Connection Refused` | Port geschlossen oder Dienst down | Prüfen, ob DB-Dienst lauscht (`netstat`/`ss`/`nc`). |
| `SSL Certificate Error` | Zertifikat abgelaufen/unbekannt | CA-Bündel in der Laufzeitumgebung hinterlegen. |
| Schlechte API-Latenz | WLAN-Störung oder Switch-Engpass | Traceroute zur Identifikation des Flaschenhalses nutzen. |

---

## FIAE-Zusammenfassung

Das Verständnis von Netzwerkinfrastrukturen, Sicherheitszonen (DMZ) und Komponenten ermöglicht es Entwicklern, Fehler bei API-Zugriffen und Datenbankverbindungen schnell zu isolieren und Anwendungen sicher zu platzieren.
