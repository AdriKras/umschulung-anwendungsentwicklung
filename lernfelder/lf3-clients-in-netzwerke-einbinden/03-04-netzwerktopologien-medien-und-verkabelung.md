# 03-04: LF 3.3 Netzwerktopologien, Medien & Verkabelung

Dieses Modul behandelt die physischen und logischen Netzwerktopologien, Übertragungsmedien (Kupfer vs. Glasfaser), die 3-stufige strukturierte Verkabelung sowie aktive/passive Netzwerkkomponenten.

---

## 1. Netzwerktopologien im Vergleich

| Topologie | Funktionsweise | Vorteile | Nachteile | Praxis-Relevanz |
| :--- | :--- | :--- | :--- | :--- |
| **Stern (Star)** | Alle Knoten sind an einen zentralen Switch angeschlossen. | Ausfall eines Kabels betrifft nur ein Gerät; leicht erweiterbar. | Central Point of Failure (Switch fällt aus = Netz tot). | **Standard in modernen LANs.** |
| **Bus** | Alle Geräte hängen an einer gemeinsamen Hauptleitung. | Geringer Kabelaufwand. | Kollisionen; Kabelbruch legt gesamtes Netz lahm. | Veraltet (Koaxialzeiten). |
| **Ring** | Jedes Gerät ist mit zwei Nachbarn verbunden. | Kein Kollisionsrisiko (Token-Passing). | Ein Knotenausfall unterbricht den gesamten Ring. | Kaum noch genutzt. |
| **Vermascht (Mesh)**| Mehrfache direkte Verbindungen zwischen den Knoten. | Extrem ausfallsicher durch redundante Wege. | Sehr hoher Verkabelungs- und Konfigurationsaufwand. | Backbone, WAN, WLAN-Mesh. |

---

## 2. Übertragungsmedien: Kupfer vs. Lichtwellenleiter (LWL)

| Kriterium | Kupfer (Twisted Pair / S/FTP) | Glasfaser / LWL (Single- / Multi-Mode) |
| :--- | :--- | :--- |
| **Übertragungsart** | Elektrische Signale | Lichtimpulse |
| **Störanfälligkeit** | Empfindlich gegen elektromagnetische Felder | Völlig immun gegen EM-Störungen |
| **Reichweite** | **Max. 100 Meter** (90 m Verlegekabel + 10 m Patchkabel) | Mehrere Kilometer (Single-Mode) |
| **Kosten & Montage** | Günstig, einfach zu crimpen/aufzulegen | Teurer, erfordert Spleißgerät |
| **Einsatzbereich** | Tertiärbereich (Etagenverteiler -> PC) | Primär- & Sekundärbereich (Building/Campus) |

---

## 3. Strukturierte Gebäudeverkabelung (EN 50173)

Die strukturierte Verkabelung garantiert eine herstellerunabhängige und zukunftssichere Netzwerkinfrastruktur.

```text
[ Primärbereich / Campus-Backbone ]   ---> Gebäude A <---> Gebäude B (Glasfaser)
               |
[ Sekundärbereich / Steigbereich ]   ---> Gebäudeverteiler <---> Etagenverteiler (Glasfaser)
               |
[ Tertiärbereich / Etagenbereich ]   ---> Etagenverteiler <---> Patchpanel <---> Dose (Kupfer, max. 100m)
```

---

## 4. Aktive vs. Passive Komponenten & Switch-Features

* **Passive Komponenten:** Patchpanel, Netzwerkdosen (RJ45), Verlegekabel, Patchkabel (übertragen nur Signale, benötigen keinen Strom).
* **Aktive Komponenten:** Switches, Router, Access Points (verarbeiten Pakete, benötigen Strom).

### Switch-Features für Entwickler
* **Power over Ethernet (PoE):** Stromversorgung von Access Points/IP-Kameras direkt über das Netzwerkkabel.
* **Managed Switches:** Erlauben VLAN-Konfiguration (VLAN-Tagging nach IEEE 802.1Q), Port-Security (MAC-Filter) und Port-Spiegelung (*Port Mirroring* für Wireshark-Analysen).

---

## FIAE-Zusammenfassung
Entwickler müssen Leitungslängen (100m-Kupfer-Limit bei Vor-Ort-Installationen) berücksichtigen und Managed Switches verstehen, um z. B. bei Wireshark-Analysen via Port-Spiegelung Netzwerktraffic abzugreifen.
