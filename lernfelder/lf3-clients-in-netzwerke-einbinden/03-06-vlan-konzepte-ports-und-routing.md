# 03-06: LF 3.4 VLAN-Konzepte, Tagging & Port-Zuweisungen

Dieses Modul behandelt die Trennung logischer Netzwerke über Virtual Local Area Networks (VLANs), den Unterschied zwischen Access- und Trunk-Ports (IEEE 802.1Q) sowie die Reduzierung von Broadcast-Domänen.

---

## 1. Grundprinzip von VLANs

Ein **VLAN (Virtual Local Area Network)** unterteilt einen physischen Switch in mehrere voneinander isolierte logische Netzwerke.

* **Ziel:** Reduzierung von Broadcast-Domänen, Erhöhung der Sicherheit und logische Trennung von Abteilungen (z. B. Dev, Produktion, Gastnetz).
* **Vorteil:** Keine zusätzliche Hardware nötig; Abteilungswechsel erfolgt rein softwareseitig über Switch-Ports.

```text
[ Switch (Managed) ]
  ├── Port 1 (VLAN 10 - Dev)  ---------> PC Entwickler
  ├── Port 2 (VLAN 10 - Dev)  ---------> Dev-Server
  └── Port 3 (VLAN 20 - Gast) ---------> Gast-Laptop (Kein Zugriff auf VLAN 10!)
```

---

## 2. Access-Ports vs. Trunk-Ports (IEEE 802.1Q)

| Port-Typ | Bezifferung | Datenstrom | Typischer Einsatzzweck |
| :--- | :--- | :--- | :--- |
| **Access-Port** | **Untagged (U)** | Pakete haben **keinen** VLAN-Tag. Switch ordnet den Port fest einem VLAN zu. | Verbindung zu Endgeräten (PC, Drucker, Server). |
| **Trunk-Port** | **Tagged (T)** | Pakete erhalten einen **802.1Q-Header** mit der VLAN-ID (1–4094). | Verbindung zwischen Switches oder Switch <-> Router. |

### Der IEEE 802.1Q Frame Tag
Beim Transport über einen Trunk-Port fügt der Switch einen **4-Byte-Header** in den Ethernet-Frame ein:
* **TPID (0x8100):** Identifiziert das Paket als 802.1Q-Frame.
* **VLAN-ID (VID):** 12-Bit-Zahl (ermöglicht 4094 VLANs).

---

## 3. Einbindung eines Clients in ein VLAN

1. **Am Managed Switch:** Port-Konfiguration vornehmen (z. B. Port 5 -> Access-Port für VLAN 10).
2. **Am Client (Betriebssystem):**
   * Normalerweise bemerkt der Client das VLAN nicht (Switch entfernt das Tag beim Verlassen des Access-Ports).
   * **VLAN-Tagging am Client (optional):** Falls der Client direkt an einem Trunk hängt, kann unter Linux ein VLAN-Interface angelegt werden:
```bash
# Erstellt ein VLAN 10 Interface auf der Schnittstelle eth0
sudo ip link add link eth0 name eth0.10 type vlan id 10
sudo ip link set dev eth0.10 up
sudo dhclient eth0.10
```

---

## 4. Routing zwischen VLANs (Inter-VLAN Routing)

VLANs isolieren den Datenverkehr auf **Layer 2**. Wenn Geräte aus VLAN 10 mit Geräten aus VLAN 20 kommunizieren müssen, wird ein **Layer-3-Gerät** benötigt:
* **Router-on-a-Stick:** Router ist über einen Trunk-Port an den Switch angebunden und nutzt Sub-Interfaces (z. B. `eth0.10`, `eth0.20`).
* **Layer-3-Switch (Multilayer Switch):** Führ das Routing intern über *Switched Virtual Interfaces (SVIs)* mit hoher Bandbreite aus.

---

## FIAE-Zusammenfassung
Entwickler müssen VLAN-Strukturen verstehen, um Docker-Container oder Test-Server in den richtigen Netzwerk-Subnetzen anzusprechen und Firewall-Freischaltungen zwischen Entwicklungs- und Produktiv-VLANs korrekt zu beantragen.
