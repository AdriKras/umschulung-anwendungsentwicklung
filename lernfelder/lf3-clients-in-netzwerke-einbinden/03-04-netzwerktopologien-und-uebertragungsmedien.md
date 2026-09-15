# 03-04: LF3.3 Netzwerktopologien & Übertragungsmedien (AE-Fokus)

Dieses Modul behandelt die physikalische und logische Anordnung von Netzwerken (Topologien), die Eigenschaften von Übertragungsmedien (Kupfer, Glasfaser, Koax) sowie physikalische Störfaktoren der Datenübertragung.

---

## 1. Klassische Netzwerktopologien im Vergleich

Die Topologie beschreibt die Struktur der Verbindungen zwischen Geräten im Netzwerk.

| Topologie | Ausfallsicherheit | Erweiterbarkeit | Kosten | Haupt-Einsatzbereich |
| :--- | :--- | :--- | :--- | :--- |
| **Bus** | Sehr gering (Kabelbruch legt alles lahm) | Einfach (T-Stücke) | Sehr gering | Veraltet (Historische Koax-Netze) |
| **Ring** | Gering (Unterbrechung stoppt Token) | Aufwendig | Gering | Veraltet (Token Ring) |
| **Stern** | Hoch (Ausfall eines Endgeräts egal) | Sehr einfach | Mittel (Switch nötig) | **Standard in modernen Unternehmensnetzen** |
| **Baum** | Mittel (Ausfall eines Verteilers betrifft AST) | Gut (Hierarchisch) | Mittel bis Hoch | Gebäude-Verkabelung (Strukturierte Netze) |
| **Mesh (Voll)**| Extrem hoch (Redundanz pur) | Sehr aufwendig | Sehr hoch | WAN-Backbones, Rechenzentren, Mesh-WLAN |

### Standard für Unternehmen: Der erweiterte Stern (Hierarchisch/Baum)
In modernen Unternehmensnetzen ist die **Sterntopologie** (mit redundanten Switches als Baumstruktur) zwingend erforderlich:
* **Vorteil:** Ein defektes Kabel betrifft nur ein einziges Endgerät.
* **AE-Bezug:** Hohe Ausfallsicherheit stellt sicher, dass Microservices, Datenbanken und CI/CD-Pipelines nicht durch einzelne Kabelbrüche blockiert werden.

---

## 2. Übertragungsmedien (Kupfer, Glasfaser, Koaxial)

| Kriterium | Twisted-Pair (Kupfer) | Glasfaser (LWL) | Koaxialkabel |
| :--- | :--- | :--- | :--- |
| **Signalform** | Elektrische Impulse | Lichtimpulse (Laser/LED) | Elektrische Impulse |
| **Max. Distanz** | 100 Meter (per Segment) | Mehrere Kilometer (Single-Mode) | ~500 Meter |
| **Störanfälligkeit**| Anfällig für EMV (Elektromagnetismus) | **Immun gegen EMV** (Keine Galvanische Kopplung) | Mäßig anfällig |
| **Einsatzbereich**| Tertiärbereich (Arbeitsplatz) | Primär- & Sekundärbereich (Backbone, Server) | Kabelfernsehen / DOCSIS-Internet |
| **Abschirmung** | S/FTP, U/FTP, STP | Nicht nötig | Geflecht & Folie |

---

## 3. Elektrische Störfaktoren & Signalübertragung

* **Dämpfung (Attenuation):** Abschwächung des Signals über lange Strecken. *Gegenmaßnahme:* Einhaltung der max. Kabellängen (100 m bei Kupfer) oder Einsatz von Repeaters/Switches.
* **Übersprechen (Crosstalk / NEXT):** Signalüberkopplung zwischen benachbarten Adernpaaren. *Gegenmaßnahme:* Paarweise Verdrillung und Shielding (S/FTP).
* **Interferenz (EMV):** Störung durch Stromkabel, Motoren oder Leuchtstoffröhren. *Gegenmaßnahme:* Räumliche Trennung von Strom- und Datenkabeln.

### Half-Duplex vs. Full-Duplex
* **Half-Duplex (Halbduplex):** Daten können wechselseitig, aber **nicht gleichzeitig** gesendet und empfangen werden (z. B. WLAN, alte Hubs).
* **Full-Duplex (Vollduplex):** Gleichzeitiges Senden und Empfangen auf getrennten Kanälen/Adern (z. B. Switched Ethernet).
* **AE-Bezug:** Full-Duplex ist essenziell für datenbankintensive Anwendungen (zeitgleiches Streaming von Abfrage-Ergebnissen und Senden neuer Anfragen).
