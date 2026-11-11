# 07-03: LF 7.3 IoT-Sicherheit, OTA-Updates, Sensoranbindung & AIDA

Dieses Modul behandelt sichere Kommunikationswege, den zuverlässigen Betrieb und die Erweiterung vernetzter Geräte. Ergänzend wird erläutert, wie sich der technische und wirtschaftliche Nutzen einer Lösung verständlich präsentieren lässt.

---

## 1. Schutzziele: Die CIA-Triade

| Schutzziel | Bedeutung | Maßnahmen im IoT |
| :--- | :--- | :--- |
| **Confidentiality – Vertraulichkeit** | Nur berechtigte Personen und Systeme dürfen Daten lesen. | Transportverschlüsselung und Zugriffsschutz |
| **Integrity – Integrität** | Unberechtigte Änderungen sollen verhindert oder erkannt werden. | Authentisierte Übertragung, Firmware-Signaturen |
| **Availability – Verfügbarkeit** | Benötigte Funktionen bleiben im vereinbarten Umfang nutzbar. | Überwachung, lokale Verarbeitung, Redundanz und Wiederherstellung |

Verfügbarkeit bedeutet nicht nur Schutz vor DDoS. Auch Stromausfälle, Softwarefehler oder eine unterbrochene Internetverbindung müssen berücksichtigt werden.

### Schwachstellen bewerten

Für jede Schwachstelle werden **Eintrittswahrscheinlichkeit und Auswirkung** betrachtet. Daraus ergibt sich die Priorität der Maßnahmen.

| Schwachstelle | Mögliches Risiko | Gegenmaßnahme |
| :--- | :--- | :--- |
| Unverschlüsselte Kommunikation | Messwerte oder Zugangsdaten werden auf dem Übertragungsweg mitgelesen. | TLS einsetzen |
| Gemeinsame Zugangsdaten aller Geräte | Ein kompromittiertes Gerät gefährdet weitere Geräte. | Individuelle Geräteidentitäten und widerrufbare Zugangsdaten |
| Zu weitreichende MQTT-Berechtigungen | Ein Sensor veröffentlicht unberechtigt Steuerbefehle. | Topic-Rechte nach dem Prinzip der geringsten Berechtigung |
| Fehlende Update-Prüfung | Manipulierte Firmware wird installiert. | Signaturen und vertrauenswürdige Updatequelle prüfen |

**FIAE-Bezug:** Entwickler berücksichtigen Sicherheitsanforderungen beim Entwurf von Schnittstellen, Berechtigungen und Fehlerbehandlung.

---

## 2. MQTT mit TLS absichern

Unverschlüsseltes MQTT wird häufig über **TCP-Port 1883**, MQTT über TLS häufig über **TCP-Port 8883** angeboten. Entscheidend ist die tatsächliche Konfiguration, nicht allein die Portnummer.

Bei unverschlüsselter Übertragung können Teilnehmer mit Zugriff auf den entsprechenden Datenverkehr Inhalte und Zugangsdaten mitlesen. Nicht jeder Teilnehmer eines geswitchten Netzes sieht automatisch alle Verbindungen.

**TLS – Transport Layer Security** schützt die Verbindung gegen Abhören und Manipulation. SSL ist der veraltete Vorgänger und sollte nicht verwendet werden.

### Zertifikate richtig prüfen

Ein Client prüft insbesondere:

* die Vertrauenskette zu einer akzeptierten Zertifizierungsstelle;
* die Übereinstimmung des Servernamens mit dem Zertifikat;
* den Gültigkeitszeitraum anhand einer geeigneten Zeitbasis.

Nur aktivierte und korrekt umgesetzte Prüfung schützt vor der Verbindung zu einem falschen Server. Bei **gegenseitigem TLS (mTLS)** weist sich auch der Client mit einem Zertifikat aus.

**Grenze:** TLS schützt die jeweilige Verbindung. Ein Broker, an dem TLS endet, kann die Nachrichten weiterhin verarbeiten. Verschlüsselung ersetzt keine Zugriffsrechte.

### Ressourcen kleiner Geräte

TLS benötigt RAM, Rechenzeit und Energie, besonders beim Verbindungsaufbau. Hardwareunterstützung und geeignete Bibliotheken helfen. Bei stark eingeschränkten Geräten muss die Architektur passende Sicherheitsverfahren vorsehen; Zertifikatsprüfungen abzuschalten ist keine Lösung.

**FIAE-Bezug:** Sichere Standardkonfigurationen, Zertifikatserneuerung, Geräteauthentisierung und gezielte Topic-Berechtigungen gehören zur Anwendungsarchitektur.

---

## 3. Watchdog und Ausfallkonzept

Ein **Watchdog-Timer (WDT)** überwacht, ob Software innerhalb festgelegter Zeitgrenzen Fortschritte macht. Bleibt das erforderliche Lebenszeichen aus, kann je nach Konfiguration zunächst eine Fehlerbehandlung und anschließend ein Neustart ausgelöst werden.

**Wichtig:** Den Watchdog nur dann bedienen, wenn die überwachten Aufgaben tatsächlich funktionieren. Ein unabhängiger Timer, der ihn trotz blockierter Anwendung ständig zurücksetzt, verdeckt Fehler.

Ein Neustart behebt außerdem nicht automatisch die Ursache. Wiederholte Abstürze müssen erkannt und protokolliert werden.

### Fallback-Verhalten festlegen

| Fehlerfall | Geplantes Verhalten |
| :--- | :--- |
| Internet oder Cloud ausgefallen | Lokale Regeln fortsetzen; Daten begrenzt puffern |
| Sensordaten fehlen oder sind veraltet | Werte als ungültig kennzeichnen; definierten Ersatzbetrieb aktivieren |
| Steuerungssoftware hängt | Watchdog reagiert; nach Neustart Zustand prüfen |
| Wiederholte Neustarts | Fehlerzustand melden und Wiederanlauf begrenzen |
| Versorgung oder Controller fällt aus | Auch das Verhalten der Aktoren ohne laufende Software berücksichtigen |

**Fail-Safe** bedeutet, bei einem Fehler einen für die konkrete Anwendung geeigneten sicheren Zustand anzunehmen. Eine pauschale Abschaltung ist nicht für jede Anlage sicher. Bei einer Heizungsanlage können beispielsweise Überhitzungsschutz und Frostschutz unterschiedliche Anforderungen stellen.

**FIAE-Bezug:** Entwickler definieren Zustände, Zeitlimits und Übergänge ausdrücklich und testen den Betrieb auch ohne Cloud, Sensor oder stabile Verbindung.

---

## 4. Sichere OTA-Updates mit A/B-Partitionen

**Over-the-Air (OTA)** ermöglicht Firmware-Updates über eine Netzwerkverbindung statt über ein lokal angeschlossenes USB-Kabel.

Beim **A/B-Prinzip** läuft zunächst Firmware A. Die neue Firmware wird in den inaktiven Bereich B geschrieben, geprüft und beim nächsten Neustart gestartet. Dafür sind ausreichend Flash-Speicher und ein passender Bootloader nötig.

### Geplanter Update-Ablauf

1. **Vorbereiten:** Kompatibilität, Speicher und Energieversorgung prüfen; Aktoren in einen geeigneten Zustand bringen.
2. **Übertragen:** Firmware über eine authentisierte, verschlüsselte Verbindung herunterladen.
3. **Prüfen:** Vollständigkeit und kryptografische Signatur kontrollieren. Eine einfache Prüfsumme allein beweist keine vertrauenswürdige Herkunft.
4. **Teststart:** Neue Firmware starten und zentrale Funktionen mit Zeitlimit prüfen.
5. **Bestätigen oder zurückrollen:** Funktionierende Version freigeben; bei Fehlern zur vorherigen gültigen Version zurückkehren.

**Rollback ist nicht allein durch zwei Partitionen garantiert.** Bootloader, Rollback-Konfiguration und die Bestätigung der neuen Firmware müssen zusammenpassen. Bei ESP-IDF muss die Anwendung den erfolgreichen Teststart entsprechend bestätigen.

Download und Installation lassen sich während des Betriebs vorbereiten; der Firmwarewechsel benötigt üblicherweise einen Neustart. Ein vollständiger unterbrechungsfreier Betrieb folgt daraus nicht.

**FIAE-Bezug:** Updatekonzepte umfassen auch Konfigurationskompatibilität, gestaffelte Verteilung, Überwachung und Zertifikatserneuerung.

---

## 5. Sensoren anschließen: GPIO und ADC

| Schnittstelle | Aufgabe | Zu beachten |
| :--- | :--- | :--- |
| **GPIO** | Digitale Pegel einlesen oder ausgeben | Zulässige Spannung, Stromgrenzen und Pin-Funktion prüfen |
| **ADC** | Analoge Spannung in einen digitalen Messwert umwandeln | Eingangsbereich, Auflösung, Kalibrierung und Störungen berücksichtigen |

**HIGH** und **LOW** sind logische Pegelbereiche. Bei einem 3,3-V-System liegt HIGH typischerweise nahe 3,3 V; die konkreten Grenzen stehen im Datenblatt.

Nicht jeder GPIO besitzt eine ADC-Funktion. Motoren oder Relais werden außerdem nicht direkt durch einen GPIO versorgt, sondern über geeignete Treiberstufen angesteuert.

**FIAE-Bezug:** Software muss Rohwerte skalieren, unplausible Messungen erkennen und die Hardwareeigenschaften bei der Pin-Konfiguration berücksichtigen.

---

## 6. I²C und SPI im Vergleich

Beide sind lokale serielle Schnittstellen, typischerweise für kurze Verbindungen zwischen Mikrocontroller und Peripherie.

| Kriterium | I²C | SPI |
| :--- | :--- | :--- |
| **Signalleitungen** | SDA: Daten; SCL: Takt | Üblicherweise MOSI, MISO, SCK und CS |
| **Mehrere Geräte** | Gemeinsame Leitungen; Auswahl über Adresse | Geteilte Daten-/Taktleitungen; normalerweise eigene CS-Leitung je Gerät |
| **Geschwindigkeit** | Häufig 100 oder 400 kbit/s; schnellere Modi existieren | Häufig höhere Taktraten; geräteabhängig |
| **Typische Geräte** | Temperatur-/Drucksensoren, kleine Displays | SD-Karten, schnelle Sensoren, Farbdisplays |
| **Planungsfragen** | Adresskonflikte, Pull-ups, Buskapazität | Freie CS-Pins, Takt, SPI-Modus und Signalqualität |

Zusätzlich zu den Signalen benötigen die Geräte **Stromversorgung und einen gemeinsamen Massebezug**.

### I²C: Adressen und Pull-ups

I²C-Adressen sind nicht immer unveränderlich. Je nach Gerät sind sie fest, über Pins wählbar oder programmierbar. Bei gleichen Adressen können ein weiterer Bus, ein Multiplexer oder anders adressierbare Geräte nötig sein.

SDA und SCL benötigen geeignete Pull-up-Widerstände. Die mögliche Gerätezahl hängt nicht nur vom Adressraum ab, sondern auch von elektrischer Belastung und Leitungslänge.

### SPI: Auswahl und Takt

Der Controller aktiviert das gewünschte Gerät über CS. Taktfrequenz sowie Taktpolarität und -phase müssen zum Gerät passen. Bei gemeinsamem MISO muss ein nicht ausgewähltes Gerät die Leitung freigeben.

### Erweiterung planen

1. Datenblatt prüfen: Versorgung, Pegel, Adresse bzw. SPI-Modus und Strombedarf.
2. Freie Pins und vorhandene Busbelegung ermitteln.
3. Verdrahtung, Pull-ups oder CS-Leitungen planen.
4. Treiber einbinden und Sensor zunächst einzeln testen.
5. Fehlerfälle wie abgezogene Sensoren und blockierte Kommunikation prüfen.
6. Neue Messwerte in Payload, Backend und Dokumentation ergänzen.

**FIAE-Bezug:** Eine Sensorerweiterung betrifft nicht nur Kabel und Treiber, sondern häufig auch Datenformate, Validierung, Datenbank und Benutzeroberfläche.

---

## 7. Gesamtlösung nach AIDA präsentieren

Ein **Elevator Pitch** erklärt den Nutzen einer Lösung kurz und passend zur Zielgruppe. **AIDA** strukturiert die Argumentation:

| Phase | Ziel | Beispiel für eine Raumklima-Lösung |
| :--- | :--- | :--- |
| **Attention** | Aufmerksamkeit gewinnen | „Wie behalten Sie das Raumklima im Blick, wenn die Internetverbindung ausfällt?“ |
| **Interest** | Funktionsweise verständlich machen | „Unsere Sensoren liefern Werte an ein lokales Gateway, das vor Ort reagiert.“ |
| **Desire** | Relevanten Nutzen verdeutlichen | „Schlafphasen und kompakte Nachrichten können Batteriewechsel und Datenverkehr reduzieren.“ |
| **Action** | Einen konkreten nächsten Schritt vorschlagen | „Lassen Sie uns die Lösung in einem Raum testen und Verbrauch sowie Reaktionszeiten messen.“ |

### Technischen Nutzen wirtschaftlich übersetzen

| Technische Eigenschaft | Möglicher wirtschaftlicher Nutzen |
| :--- | :--- |
| Lokale Verarbeitung | Weniger Cloud-Datenverkehr und geringere Abhängigkeit von der Internetverbindung |
| Deep Sleep und kompakte Payloads | Längere Batterielaufzeit und weniger Wartungsaufwand |
| Sichere Fernupdates | Weniger Vor-Ort-Einsätze für Softwareaktualisierungen |
| Geplante Sensoranbindung | Einfachere Erweiterung statt vollständigem Systemaustausch |

**Wichtig:** Einsparungen sind zunächst Erwartungen. Pilotmessungen und eine Kostenbetrachtung einschließlich Hardware, Entwicklung und Betrieb müssen sie belegen.

Für technische Ansprechpartner stehen Architektur und Schnittstellen im Vordergrund; für Entscheider Nutzen, Kosten und Betriebsrisiken.

---

## FIAE-Zusammenfassung

1. **Kommunikation schützen:** TLS, Identitätsprüfung und passende Berechtigungen kombinieren.
2. **Ausfälle beherrschen:** Watchdog, lokale Funktionen und geeignete Fehlerzustände einplanen.
3. **Updates absichern:** Herkunft prüfen, Teststart durchführen und Rollback vorsehen.
4. **Erweiterungen durchdenken:** Elektrische Anbindung, Treiber und Datenverarbeitung gemeinsam planen.
5. **Nutzen erklären:** Technische Eigenschaften in nachvollziehbare Vorteile übersetzen.

**Merksatz:** Eine gute IoT-Lösung ist sicher betreibbar, kontrolliert erweiterbar und für ihre Zielgruppe verständlich begründet.

