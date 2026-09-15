# 03-07: LF 3.5 Routing, WAN-Technologien & Dual-Stack / DS-Lite

Dieses Modul behandelt die Analyse von Routing-Tabellen (Linux/Windows), Paket-Tragewege (traceroute), WAN-Zugangstechnologien (DSL, Cable, Fiber/FTTx) sowie IPv4/IPv6-Transition-Mechanismen.

---

## 1. Routing-Tabellen & Routing-Entscheidung des Clients

Ein Host entscheidet anhand seiner Routing-Tabelle, ob ein Paket direkt im lokalen Subnetz zugestellt wird oder an das **Default Gateway** (Router) gesendet werden muss.

### CLI-Befehle zur Anzeige der Routing-Tabelle
```bash
# Linux
ip route show

# Windows
route print
```

### Logische Routing-Entscheidung
1. **Ziel-IP im selben Subnetz?** (Prüfung via Netzmaske/Prefix).
   * *Ja:* Direktzustellung via ARP / Layer 2 MAC-Adresse.
   * *Nein:* Paket wird an die MAC-Adresse des **Default Gateways** gesendet.
2. **Paketverfolgung:**
   * `traceroute <Ziel-IP>` (Linux) / `tracert <Ziel-IP>` (Windows) zeigt alle Zwischenstationen (Hops) und ICMP-Laufzeiten an.

---

## 2. WAN-Zugangstechnologien im Vergleich

| Technologie | Physikalische Basis | Typische Bandbreiten | Besonderheiten / Übertragung |
| :--- | :--- | :--- | :--- |
| **DSL / VDSL** | Kupfer-Doppelader (Telefonnetz) | bis 250 Mbit/s (Vectoring) | Signal wird über DSLAM moduliert; stärkere Dämpfung auf Strecke. |
| **DOCSIS (Kabel)** | Koaxialkabel (TV-Kabelnetz) | bis 1000 Mbit/s | *Shared Medium* (Bandbreite sinkt bei hoher Auslastung im Segment). |
| **Glasfaser (Fiber)** | Lichtwellenleiter (LWL) | Gigabit+ (symmetrisch) | Immun gegen Störungen, sehr geringe Latenz. |

### Glasfaser-Ausbaustufen (FTTx)
* **FTTC (Fiber to the Curb):** Glasfaser bis zum grauen Schaltkasten an der Straße. Reststrecke ins Haus via Kupfer (VDSL).
* **FTTB (Fiber to the Building):** Glasfaser bis in den Keller des Gebäudes. In-House-Verkabelung via Kupfer/G.fast.
* **FTTH (Fiber to the Home):** Durchgehende Glasfaserverbindung direkt bis in die Wohnung/das Büro.

---

## 3. Provider-Strategien: Dual-Stack vs. DS-Lite

| Modell | IPv4-Adresse | IPv6-Adresse | FIAE-Auswirkung / Problemstellen |
| :--- | :--- | :--- | :--- |
| **Dual-Stack** | Echte öffentliche IPv4 | Echte öffentliche IPv6 | **Ideal:** Uneingeschränkte Erreichbarkeit von außen via Port-Forwarding. |
| **DS-Lite (Dual-Stack Lite)** | Keine eigene IPv4 (CG-NAT / AFTR-Gateway) | Echte öffentliche IPv6 | **Problematisch:** Lokale Server/Dev-APIs sind **nicht direkt über IPv4 von außen erreichbar**! |

---

## FIAE-Zusammenfassung
Entwickler müssen DS-Lite (CG-NAT) kennen, da selbst erstelle Home-Office-Server oder Dev-APIs bei Kunden ohne öffentliche IPv4 nicht per IPv4-Port-Forwarding freigegeben werden können und IPv6/Tunneling genutzt werden muss.
