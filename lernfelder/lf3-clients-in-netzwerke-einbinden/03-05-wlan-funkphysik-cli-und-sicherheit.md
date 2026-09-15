# 03-05: LF 3.4 WLAN – Funkphysik, CLI-Steuerung & Sicherheit

Dieses Modul behandelt die physikalischen Grundlagen von WLAN (Dämpfung, CSMA/CA, EU-Vorgaben), die Steuerung unter Linux/Windows sowie Sicherheitsstandards und Gastnetz-Konzepte.

---

## 1. Funkphysik, Frequenzbänder & EU-Vorgaben

| Parameter | 2,4 GHz Band | 5 GHz Band | 6 GHz Band (Wi-Fi 6E/7) |
| :--- | :--- | :--- | :--- |
| **Reichweite / Dämpfung** | Hohe Reichweite, gute Wanddurchdringung. | Geringere Reichweite, höhere Dämpfung durch Wände. | Sehr geringe Reichweite, hohe Dämpfung. |
| **Kanalbreiten** | 20 MHz (max. 40 MHz) | 20 / 40 / 80 / 160 MHz | bis zu 320 MHz |
| **Kollisionsgefahr** | Hoch (nur 3 überschneidungsfreie Kanäle: 1, 6, 11). | Gering (viele überschneidungsfreie Kanäle). | Extrem gering. |

### EU-Vorgaben & Regulatorien
* **EIRP (Equivalent Isotropically Radiated Power):** Gesetzliche maximale Sendeleistung inkl. Antennengewinn.
  * **2,4 GHz:** max. **100 mW** (20 dBm).
  * **5 GHz (Kanal 36–64):** max. **200 mW** (23 dBm, nur Indoor).
  * **5 GHz (Kanal 100–140):** max. **1000 mW** (30 dBm, Outdoor gestattet).
* **DFS (Dynamic Frequency Selection) & TPC:** Pflicht im 5-GHz-Bereich (ab Kanal 52). Der AP muss das Band scannen und bei Erkennung von Primärnutzern (Wetterradar) automatisch den Kanal wechseln.

### Medienzugriff: CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
Da WLAN ein geteiltes Medium (*Shared Medium*) ist und Kollisionen in der Luft nicht direkt wie im Kabel erkannt werden können, nutzt es **CSMA/CA**:
1. **Listen Before Talk:** Client hört das Frequenzband ab.
2. **IFS (Interframe Space):** Wartet eine definierte Zeitspanne ab.
3. **Random Backoff:** Bei belegtem Kanal wartet der Client eine zufällige Zeitabfolge.
4. **RTS/CTS (Optional):** Request to Send / Clear to Send vermeidet das *Hidden-Node-Problem*.

---

## 2. WLAN-Steuerung & Troubleshooting unter Linux

Linux nutzt im Hintergrund den `wpa_supplicant` Daemon für WPA-Handshakes.

### Wichtige CLI-Befehle
```bash
# Verfügbare WLAN-Netze scannen
nmcli device wifi list

# Mit einem WLAN-Netzwerk verbinden
nmcli device wifi connect "SSID_Name" password "WLAN_Passwort"

# Status der WLAN-Schnittstelle prüfen
iwconfig wlan0
```

### Diagnose bei Verbindungsabbrüchen
```bash
# Kernel-Logs nach WLAN- und Treiber-Events filtern
dmesg | grep -i wlan

# Logs des NetworkManagers und wpa_supplicant in Echtzeit verfolgen
journalctl -u NetworkManager -u wpa_supplicant -f
```

> **VM-Hinweis (Hardware-Passthrough):** USB-WLAN-Sticks müssen in Hypervisoren (VirtualBox/VMware) direkt per USB-Passthrough an die VM durchgereicht werden, da reine NAT/Bridged-Netzwerkkarten die PCI/USB-Funkhardware verbergen.

---

## 3. WLAN-Standards & Sicherheitsarchitektur

| Standard | Wi-Fi Name | Max. Datenrate | Schlüsseltechnologien |
| :--- | :--- | :--- | :--- |
| **IEEE 802.11ac** | Wi-Fi 5 | bis 3,5 Gbit/s | 5 GHz, Beamforming, MU-MIMO (Downlink) |
| **IEEE 802.11ax** | Wi-Fi 6 / 6E | bis 9,6 Gbit/s | 2,4 / 5 / 6 GHz, OFDMA, MU-MIMO (Up/Down) |

### WPA3-Personal vs. WPA3-Enterprise
* **WPA3-Personal (SAE):** Nutzt *Simultaneous Authentication of Equals* (Diffie-Hellman). Schützt gegen Offline-Wörterbuchangriffe, selbst bei schwachen Passwörtern.
* **WPA3-Enterprise (802.1X):** Nutzen von Zertifikaten & zentralem RADIUS-Server. Jeder Mitarbeiter nutzt eigene Anmeldedaten.

### Sichere Gastnetze
* **Client Isolation:** Unterbindet die direkte Kommunikation zwischen WLAN-Clients untereinander.
* **Captive Portal:** Umleitung unauthentifizierter Nutzer auf eine Anmeldeseite.

---

## FIAE-Zusammenfassung
Entwickler müssen WPA3-Enterprise (802.1X/RADIUS) verstehen, um mobile Apps oder IoT-Geräte sicher im Firmennetzwerk zu authentifizieren und API-Endpoints vor unberechtigten Zugriffen aus Gastnetzen zu schützen.
