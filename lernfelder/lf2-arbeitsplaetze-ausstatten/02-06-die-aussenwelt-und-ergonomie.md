Dieses Modul behandelt die physikalischen und logischen Schnittstellen zur Außenwelt, Display- und Audiotechnologien, drahtlose Kommunikation sowie Ergonomie- und Inklusionsnormen (ArbStättV, ISO 9241, BITV). Für Anwendungsentwickler ist dieses Wissen essenziell, um leistungsfähige Multi-Monitor-Workstations zu konzipieren und Software-GUIs barrierefrei (Zwei-Sinne-Prinzip) zu gestalten.

---

## 1. Schnittstellen, Bus-Systeme & Standardisierungsgremien

Es gilt die fundamentale Unterscheidung:
* **Physikalische Schnittstelle:** Der mechanische Stecker, Kabelformfaktor oder Port (z. B. USB-C-Stecker, RJ45).
* **Übertragungsprotokoll:** Die logische Regelung der Datenübertragung und Befehlssätze (z. B. PCIe, DisplayPort-Tunneling, USB Power Delivery).

### Evolution von USB und Thunderbolt (K2)

| Schnittstelle / Standard | Max. Bandbreite | Übertragungsprotokoll / Besonderheiten | Physischer Stecker |
| :--- | :--- | :--- | :--- |
| **USB 1.1** | 12 Mbps | USB 1.1 (Half-Duplex) | USB-A, USB-B |
| **USB 2.0** | 480 Mbps | USB 2.0 (Half-Duplex) | USB-A, USB-B, Micro-USB |
| **USB 3.2 Gen 1** | 5 Gbps | SuperSpeed USB (Full-Duplex) | USB-A, USB-B, USB-C |
| **USB 3.2 Gen 2** | 10 Gbps | SuperSpeed+ USB | USB-A, USB-C |
| **USB 3.2 Gen 2x2** | 20 Gbps | SuperSpeed+ Dual-Lane | USB-C exklusiv |
| **USB4 1.0 / 2.0** | 40 / 80 Gbps | Basiert auf Thunderbolt 3 (PCIe/DP Tunneling) | USB-C exklusiv |
| **Thunderbolt 3 / 4 / 5** | 40 bis 120 Gbps | PCIe, DisplayPort, USB & Power Delivery (bis 240W) | USB-C exklusiv |

### Standardisierungsgremien (K1)
* **USB-IF (USB Implementers Forum):** Pflege, Spezifikation und Zertifizierung von USB-Standards und Power Delivery (PD).
* **VESA (Video Electronics Standards Association):** Standardisierung von DisplayPort-Spezifikationen, Adaptive-Sync und VESA-Monitorhalterungen.
* **IEEE (Institute of Electrical and Electronics Engineers):** Weltweite Normung von Netzwerk- (IEEE 802.3 Ethernet) und WLAN-Protokollen (IEEE 802.11).

---

## 2. Display- & Video-Technologie

### Evolution der Video-Standards ab 2010 (K2)
* **HDMI (HDMI 2.0/2.1):** Proprietärer Standard. HDMI 2.1 unterstützt bis zu 8K@60Hz / 4K@120Hz, Dynamic HDR und VRR (Variable Refresh Rate).
* **DisplayPort (DP 1.4/2.1):** Offener VESA-Standard. Unterstützt Multi-Stream Transport (MST) zum Durchschleifen mehrerer Monitore an einem einzigen Kabel (Daisy-Chaining).
* **USB-C Alt-Mode:** Ermöglicht das direkte Tunneln nativer DisplayPort-Videosignale über USB-C-Kabel.

### Panel-Technologien im Vergleich (K2)

| Panel-Typ | Funktionsweise | Vorteile | Nachteile | FIAE-Einsatzbereich |
| :--- | :--- | :--- | :--- | :--- |
| **TN (Twisted Nematic)** | Flüssigkristalle drehen sich | Schnellste Schaltzeiten | Blickwinkelinstabil, schwache Farben | Simple Terminals |
| **IPS (In-Plane Switching)** | Flüssigkristalle parallel | Hohe Farbtreue, breiter Blickwinkel | Kontrast schwächer als OLED | **Standard IDEs & UI-Design** |
| **VA (Vertical Alignment)** | Flüssigkristalle vertikal | Hoher Kontrast, tiefes Schwarz | Langsamere Schaltzeiten | Allround-Arbeitsplätze |
| **OLED (W/P/MLA)** | Selbstleuchtende Pixel | Perfektes Schwarz, kein Bleeding | Einbrennrisiko bei statischen IDEs | UX/Grafik-Testing |

### Farbtiefe, Frequenzen & Umgebungslicht (K2)
* **Farbtiefe (Bit):** 8-Bit (16,7 Mio. Farben) vs. 10-Bit (1,07 Mrd. Farben). Entscheidend im UI/UX-Design für stufenlose Farbverläufe ohne Color Banding.
* **Bildwiederholfrequenz (Hz):** 60 Hz Standard; 120 Hz+ schont die Augen bei stundenlangem Scrolling im Quellcode.
* **Licht & Reflexion:** Entspiegelte Displays (Matted) verhindern Blendungen nach ArbStättV.

---

## 3. Audio-Technik & Codecs

### Signalkette (ADC / DAC) (K2)
Analoger Schall (Mikrofon) -> ADC -> Digitale Verarbeitung (DSP) -> DAC -> Analoge Ausgabe (Kopfhörer)

* **ADC (Analog-to-Digital Converter):** Wandelt kontinuierliche analoge Schallwellen durch Abtastung (Sampling Rate in kHz) und Quantisierung (Bit-Tiefe) in digitale Bitstreams um.
* **DAC (Digital-to-Analog Converter):** Rekonstruiert aus digitalen Bits wieder ein genaues analoges Spannungssignal für Lautsprecher/Kopfhörer.

### Formate & Bluetooth-Codecs (K2)
* **Lossy (Verlustbehaftet):** MP3, AAC, SBC. Psychoakustische Entfernung für das menschliche Ohr kaum wahrnehmbarer Frequenzen.
* **Lossless (Verlustfrei):** FLAC, ALAC. Komprimierung ohne mathematischen Informationsverlust.
* **Bluetooth-Codecs:** SBC (Standard), aptX / aptX HD (Low Latency), LDAC (High Bitrate), LC3 (Bluetooth LE Audio).

---

## 4. Eingabegeräte, Druck- & Scanner-Technologien

### Tastatur-Techniken & Ergonomie (K2)
* **Membran / Rubberdome:** Günstig, leise, aber schwammiger Druckpunkt und kürzere Lebensdauer.
* **Mechanisch (Switches):** Präziser Druckpunkt, haptisches Feedback, sehr hohe Langlebigkeit.
* **Ergonomische Alternativen:** Geteilte Tastaturfelder (Split Keyboards) und vertikale Mäuse zur Vorbeugung von RSI (Repetitive Strain Injury / "Mausarm").

### Druck- & Scanner-Technologien (K2)
* **Laserdrucker:** Erhitzen von Toner via Fixiereinheit. Schnell, dokumentenecht, geringe Seitenpreise.
* **Tintenstrahldrucker:** Tröpfchenauswurf (Piezo/Thermatisch). Hohe Auflösung für Fotodruck, aber Gefahr verstopfter Düsen.
* **Nadeldrucker:** Mechanischer Durchschlag via Farbband. Unverzichtbar für Durchschreibesätze und Formulare.
* **Scanner (CCD vs. CIS):** CCD nutzt Linsensystem mit hoher Schärfentiefe (für gewölbte Buchseiten); CIS nutzt LED-Zeilen, ist kompakt und extrem energiesparend.

---

## 5. Drahtlose Technologien (Wireless) (K2, K4)

### WLAN-Frequenzen & Physikalische Eigenschaften (K2)

| Frequenzband | Reichweite | Wanddurchdringung | Max. Bandbreite | Störungsanfälligkeit |
| :--- | :--- | :--- | :--- | :--- |
| **2,4 GHz** | Hoch (~50m) | Sehr gut | Niedrig | Hoch (Bluetooth, Mikrowellen) |
| **5 GHz** | Mittel (~15m) | Mittel | Hoch | Gering (DFS-Kanalwahl) |
| **6 GHz (Wi-Fi 6E/7)** | Kurz (~10m) | Schwach | Extrem hoch | Minimal (Keine Überlappung) |

### Funkstrategien: MIMO & Beamforming (K2, K4)
* **MIMO (Multiple-Input Multiple-Output):** Parallele Nutzung mehrerer Sende- und Empfangsantennen zur Vervielfachung der Datenrate.
* **Beamforming:** Gezielte Signalformung in Richtung der Empfangsgeräte statt ungerichteter kreisförmiger Abstrahlung.
* **Störungsfreie Strategie (K4):** Ausleuchtungsmessung (Site Survey), Trennung von 2,4-GHz-Legacy-Geräten und 5/6-GHz-Dev-Workstations, Nutzung überschneidungsfreier Kanäle (1, 6, 11 bei 2,4 GHz).

### Bluetooth-Historie & Funktionsweise (K2)
* **FHSS (Frequency-Hopping Spread Spectrum):** Wechselt 1.600-mal pro Sekunde die Frequenz im 2,4-GHz-Band zur Störungsvermeidung.
* **Profile:** HID (Human Interface Device für Tastatur/Maus), A2DP (Audio-Streaming), HFP (Freisprechen).

---

## 6. Arbeitsplatzkonzeption, Ergonomie & Verkabelung (K5)

### Arbeitsstättenverordnung (ArbStättV) & Konzeption
* **Bildschirm:** Reflexions- und blendfrei, leicht neigbar und höhenverstellbar.
* **Tastatur & Maus:** Getrennt vom Bildschirm, reflexionsarm, ergonomisch geformt.
* **Beleuchtung:** Blendfreie Ausrichtung parallel zum Fenster zur Vermeidung von Schattenwurf.

### Technisches Verkabelungskonzept
* **Stolperfreie Verlegung:** Führung in Kabelkanälen, Wannen oder Schläuchen.
* **Biegeradien & Zugentlastung:** Verhindert Kabelschäden (Glasfaser/Kupfer) und versehentliches Trennen von Verbindungen.

---

## 7. Inklusion, Barrierefreiheit & Normen (K1, K3, K5, K6)

### Das Zwei-Sinne-Prinzip (K3, K5)
Informationen müssen für Anwender über mindestens zwei der drei Sinne (Sehen, Hören, Tasten) wahrgenommen werden können:
* **Sehen + Hören:** Visuelle Systemwarnungen in der GUI müssen gleichzeitig mit akustischen Signaltönen hinterlegt sein.
* **Sehen + Tasten:** Software-Bedienelemente müssen vollständig per Tastatur/Braille-Zeile bedienbar sein.
* **Hören + Sehen:** Audioinhalte benötigen Untertitel.

### Barrierefreie MFPs & Software (K1, K5)
* **MFP-Kriterien:** Höhenverstellbares Touchscreen-Bedienfeld, kontrastreiche Tasten, Sprachführung.
* **Software-Inklusion (BITV / WCAG):** ARIA-Attribute im HTML-Frontend, Screenreader-Kompatibilität, High-Contrast-Modi.

### Umwelt- & Qualitätsnormen (K1, K6)
* **Blauer Engel:** Deutsches Umweltzeichen für geringen Energieverbrauch, Feinstaub-Armut (Drucker) und Recyclingfähigkeit.
* **TCO Certified:** Internationales Prüfsiegel für Ökologie, Ergonomie und Schadstoffarmut bei Monitoren und IT-Geräten.
* **GS-Zeichen & ISO 9241-400:** Gesetzlicher Nachweis für geprüfte Sicherheit und Ergonomie von Mensch-System-Eingabegeräten.

---

## Zusammenfassung (FIAE-Perspektive)

Das Wissen über Schnittstellen, Displays und Funknetze sichert die Konzeption hochleistungsfähiger Entwickler-Arbeitsplätze. Gleichzeitig bilden Gesetze (ArbStättV), Umweltnormen (Blauer Engel, TCO) und das Zwei-Sinne-Prinzip (BITV) das notwendige Fundament für die Prüfungsanforderungen der AP 1 sowie das Design barrierefreier Software.
