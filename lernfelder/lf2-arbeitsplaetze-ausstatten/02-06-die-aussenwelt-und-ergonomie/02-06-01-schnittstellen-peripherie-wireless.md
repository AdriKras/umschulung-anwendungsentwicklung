# 02-06-01: Schnittstellen, Video-, Audio- & Drahtlostechnologien

## 1. Schnittstellen & Bus-Systeme

* **Physische Schnittstelle vs. Übertragungsprotokoll:**
  * **Physisch:** Der mechanische Stecker/Kabel-Typ (z. B. USB-C Stecker, RJ45).
  * **Protokoll:** Die logische Regelung der Datenübertragung (z. B. PCIe-, DisplayPort-Tunneling, USB Power Delivery).

### Evolution von USB und Thunderbolt

| Schnittstelle / Standard | Max. Bandbreite | Übertragungsprotokoll / Besonderheiten | Physischer Stecker |
| :--- | :--- | :--- | :--- |
| **USB 1.1** | 12 Mbps | USB 1.1 (Half-Duplex) | USB-A, USB-B |
| **USB 2.0** | 480 Mbps | USB 2.0 (Half-Duplex) | USB-A, USB-B, Micro-USB |
| **USB 3.2 Gen 1** | 5 Gbps | SuperSpeed USB (Full-Duplex) | USB-A, USB-B, USB-C |
| **USB 3.2 Gen 2** | 10 Gbps | SuperSpeed+ USB | USB-A, USB-C |
| **USB 3.2 Gen 2x2** | 20 Gbps | SuperSpeed+ Dual-Lane | USB-C exklusiv |
| **USB4 1.0 / 2.0** | 40 / 80 Gbps | Basiert auf Thunderbolt 3 (PCIe/DP Tunneling) | USB-C exklusiv |
| **Thunderbolt 3 / 4 / 5** | 40 bis 120 Gbps | PCIe, DisplayPort, USB & Power Delivery (bis 240W) | USB-C exklusiv |

### Standardisierungsgremien
* **USB-IF (USB Implementers Forum):** Zertifiziert USB-Hardware und Spezifikationen.
* **VESA (Video Electronics Standards Association):** Standardisiert DisplayPort und Monitorhalterungen.
* **IEEE (Institute of Electrical and Electronics Engineers):** Definiert Netzwerknormen (IEEE 802.3 Ethernet, IEEE 802.11 WLAN).

---

## 2. Video- & Display-Technologien

### Evolution der Video-Standards ab 2010
* **HDMI (HDMI 2.0/2.1):** Proprietärer Standard. Ab 2.0/2.1 Unterstützung von 4K/8K, HDR und Variable Refresh Rate (VRR).
* **DisplayPort (DP 1.4/2.1):** Offener VESA-Standard. Unterstützt *Multi-Stream Transport (MST)* für Daisy-Chaining (Durchschleifen mehrerer Monitore).
* **USB-C Alt-Mode:** Überträgt native DisplayPort-Signale direkt über USB-C.

### Panel-Technologien im Vergleich

| Panel-Typ | Funktionsweise | Vorteile | Nachteile | Einsatzbereich |
| :--- | :--- | :--- | :--- | :--- |
| **TN (Twisted Nematic)** | Flüssigkristalle drehen sich | Schnellste Schaltzeiten | Blickwinkelinstabil, schwache Farben | Simple Terminals |
| **IPS (In-Plane Switching)** | Flüssigkristalle parallel | Hohe Farbtreue, breiter Blickwinkel | Kontrast schwächer als OLED | **Standard IDEs/UI-Design** |
| **VA (Vertical Alignment)** | Flüssigkristalle vertikal | Hoher Kontrast, tiefes Schwarz | Langsamere Schaltzeiten | Allround-Arbeitsplätze |
| **OLED (W/P/MLA)** | Selbstleuchtende Pixel | Perfektes Schwarz, kein Bleeding | Einbrennrisiko bei statischen IDEs | UX/Grafik-Testing |

### Farbtiefe, Frequenz & Umgebungslicht
* **Farbtiefe:** 8-Bit (16,7 Mio. Farben) vs. 10-Bit (1,07 Mrd. Farben). Wichtig bei UI-Design für stufenlose Farbverläufe.
* **Bildwiederholfrequenz (Hz):** 60 Hz Mindeststandard; 120 Hz+ reduziert Augenmüdigkeit beim schnellen Quellcode-Scrolling.
* **Umgebungslicht:** Entspiegelte Displays (Matted) verhindern Reflexionen nach ArbStättV.

---

## 3. Audio-Technik & Codecs

### Signalkette (Analog zu Digital und zurück)
1. **Analoger Schall** (Sprache/Mikrofon)
2. **ADC (Analog-to-Digital Converter):** Abtastung (Sampling Rate) und Quantisierung (Bit-Tiefe).
3. **DSP (Digital Signal Processor):** Rauschunterdrückung.
4. **DAC (Digital-to-Analog Converter):** Rekonstruktion in analoge Spannung.
5. **Analoge Ausgabe** (Kopfhörer/Lautsprecher).

### Audioformate & Bluetooth-Codecs
* **Lossy (Verlustbehaftet):** MP3, AAC, SBC (Abtrennung psychoakustisch nicht wahrnehmbarer Frequenzen).
* **Lossless (Verlustfrei):** FLAC, ALAC (Komprimierung ohne Informationsverlust).
* **Bluetooth-Codecs:** SBC (Standard), aptX/aptX HD (Low Latency), LDAC (High Bitrate), LC3 (Bluetooth LE Audio).

---

## 4. Drahtlose Technologien (Wireless)

### WLAN-Frequenzen & Physikalische Eigenschaften

| Frequenzband | Reichweite | Wanddurchdringung | Max. Bandbreite | Störungsanfälligkeit |
| :--- | :--- | :--- | :--- | :--- |
| **2,4 GHz** | Hoch (~50m) | Sehr gut | Niedrig | Hoch (Bluetooth, Mikrowellen) |
| **5 GHz** | Mittel (~15m) | Mittel | Hoch | Gering (DFS-Kanalwahl) |
| **6 GHz (Wi-Fi 6E/7)** | Kurz (~10m) | Schwach | Extrem hoch | Minimal (Keine Überlappung) |

### Drahtlose Technologien: MIMO & Beamforming
* **MIMO (Multiple-Input Multiple-Output):** Nutzen mehrerer Sende- und Empfangsantennen zur Datenratenerhöhung.
* **Beamforming:** Gezielte Ausrichtung von Funksignalen auf das Empfangsgerät statt ungerichteter Abstrahlung.

### Bluetooth & Profil-Architektur
* **FHSS (Frequency-Hopping Spread Spectrum):** Wechselt 1.600-mal pro Sekunde die Frequenz im 2,4-GHz-Band zur Vermeidung von Interferenzen.
* **Profile:** HID (Human Interface Device für Tastatur/Maus), A2DP (Audio-Streaming), HFP (Freisprechen).
