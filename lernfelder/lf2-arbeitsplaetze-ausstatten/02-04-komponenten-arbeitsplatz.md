LF 2.4: Komponenten eines Arbeitsplatzcomputers (FIAE-Fokus)

Ein Entwickler-Arbeitsplatz ist ein komplexes Gesamtsystem aus aufeinander abgestimmten Hardware- und Peripherie-Komponenten. Für Anwendungsentwickler ist das detaillierte Verständnis der Hardware-Komponenten entscheidend, um Build- und Laufzeit-Engpässe zu vermeiden, Multi-Container-Umgebungen effizient zu betreiben und barrierefreie Benutzeroberflächen (Accessibility/BITV) zu gestalten.

---

## 1. Systemarchitektur & Hauptplatine (Mainboard)

Das Mainboard (Motherboard) ist die zentrale Kommunikationszentrale. Für Entwickler-Workstations sind Schnittstellen-Vielfalt und Bandbreiten-Abdeckung entscheidend.

### Mainboard-Formfaktoren
* **ATX / Micro-ATX (mATX):** Standard-Formfaktoren für Entwickler-Workstations. Bieten mehrere PCIe-Slots (z. B. für dedizierte GPUs, NVMe-RAID-Controller, 10GbE-Karten).
* **Mini-ITX:** Kompaktformfaktor für Edge-Entwicklung, Test-Kits oder minimale Office-Desktops.

### Wichtige Mainboard-Bestandteile & Schnittstellen
* **CPU-Sockel & Chipsatz:** Steuern die Anzahl der PCIe-Lanes und die Kompatibilität zu Prozessor-Generationen.
* **PCIe-Slots (Lanes):** Punkt-zu-Punkt-Verbindungen. Wichtig: Ein physischer x16-Slot kann elektrisch nur mit x4 angebunden sein (Bandbreiten-Limitierung beachten!).
* **Storage-Schnittstellen:** M.2 (NVMe via PCIe) und SATA III (max. 600 MB/s).
* **UEFI / BIOS:** Firmware-Ebene zum Starten des Systems. Aus Dev-Sicht essenziell:
  * **Virtualization Technology (Intel VT-x / AMD-V):** Pflichtaktivierung im UEFI für Docker, WSL2 (Windows Subsystem for Linux) und VirtualBox/KVM.
  * **TPM 2.0 & Secure Boot:** Voraussetzung für Festplattenverschlüsselung (BitLocker/LUKS) bei mobilen Dev-Geräten.

---

## 2. Recheneinheiten: CPU & RAM im Entwicklungsalltag

### Prozessor (CPU): Multithreading & Caching
Die CPU bestimmt die Geschwindigkeit beim Kompilieren, Verlinken und Ausführen von Quellcode.

* **Kerne vs. Threads:** Parallele Build-Tools (z. B. make -j, Gradle, cargo) skalieren linear mit der Anzahl logischer CPU-Threads.
* **Cache-Hierarchie (L1, L2, L3):** Entwickler optimieren datenintensive Algorithmen auf Cache-Locality (Array-Iteration statt verketteter Listen), um teure Zugriffe auf den Hauptspeicher zu minimieren.

### Arbeitsspeicher (RAM): Der Auslagerungs-Flaschenhals
Zu wenig RAM zwingt das Betriebssystem zum Paging/Swappen auf den Massenspeicher, was Entwicklungs-Workflows massiv einbricht.

| Anwendungsbereich | RAM-Empfehlung | Begründung / Toolchain |
| :--- | :--- | :--- |
| **Standard-Office** | 8 – 16 GB | Browser, E-Mail, Office-Anwendungen. |
| **Fullstack-Entwicklung** | 32 GB | IDE (IntelliJ/VS Code), Docker Desktop (DB, Redis, Backend), Browser mit DevTools. |
| **Microservices & Cloud-Dev** | 32 – 64 GB | Mehrere parallele Container-Cluster, lokale Kubernetes-Nodes (minikube/k3s), VMs. |
| **ECC-RAM Requirement** | Server / Build-Runner | Error-Correcting Code schützt Build-Server und In-Memory-Datenbanken vor Bit-Flips. |

---

## 3. Massenspeicher: Performance, Haltbarkeit & Schnittstellen

### SSDs (NVMe vs. SATA) & Flash-Technologien
Für Entwickler sind zufällige Lese- und Schreibzugriffe (IOPS) beim Laden tausender kleiner Quellcodedateien (node_modules, Build-Caches) ausschlaggebend.

* **SATA-SSD:** Max. 550 MB/s (Limitiert durch AHCI-Protokoll, 1 Queue).
* **NVMe-SSD:** Bis zu 7.000+ MB/s (PCIe 4.0/5.0, 64.000 Queues).

#### Flash-Zelltypen & Haltbarkeit (TBW)
* **SLC / MLC:** Höchste Schreibhaltbarkeit, im Enterprise-Bereich eingesetzt.
* **TLC (Triple-Level Cell):** Der Standard für Entwickler-Workstations (gutes Verhältnis aus Performance und TBW).
* **QLC (Quad-Level Cell):** Bricht bei großen, dauerhaften Schreibvorgängen (z. B. Docker-Image-Builds) stark ein.

### HDDs: CMR vs. SMR
* **CMR (Conventional Magnetic Recording):** Konstante Schreibdatenraten, geeignet für NAS, Backups und Test-Datenbanken.
* **SMR (Shingled Magnetic Recording):** Überlappende Spuren. Absolut ungeeignet für Entwicklungs- & Datenbankumgebungen, da Schreibdatenraten bei dauerhafter Belastung extrem einbrechen.

---

## 4. Grafikkarte (GPU), Stromversorgung & Kühlung

### Grafikkarte (GPU): Dedicated vs. Integrated
* **Integrated Graphics (iGPU):** Reicht für Standard-Softwareentwicklung, Multi-Monitor-Betrieb und Office vollkommen aus.
* **Dedicated GPU (dGPU):** Erforderlich für GPGPU, CUDA-Entwicklung, KI/Machine-Learning (PyTorch/TensorFlow), Game Development und 3D-CAD.

### Netzteil & Effizienz (80 PLUS)
* **Wirkungsgrad:** 80 PLUS (Bronze bis Titanium) definiert die Umwandlungseffizienz von Wechselstrom (AC) in Gleichstrom (DC).
* **12V-Schiene:** Versorgt CPU und GPU. Bei dauerhaften Build-Prozessen schützt eine stabile 12V-Schiene vor Systemabstürzen.

### Kühlung & Thermal Throttling
Erreicht die CPU unter Volllast (z. B. beim Kompilieren großer Projekte) ihre kritische Temperatur, regelt sie den Takt herunter (Thermal Throttling). Eine adäquate Luft- oder Wasserkühlung sichert dauerhafte Peak-Performance.

---

## 5. Peripherie, Ergonomie & Barrierefreiheit (Accessibility)

### Ergonomie am Dev-Arbeitsplatz
* **Multi-Monitor-Setups:** Standard für Entwickler (z. B. Monitor 1: IDE, Monitor 2: Browser/App-Preview, Monitor 3: Dokumentation/Terminal).
* **Dockingstation (Thunderbolt/USB-C):** Ermöglicht nahtloses Wechseln zwischen mobiler Arbeit und stationärem Arbeitsplatz.

### Barrierefreiheit (Accessibility / BITV / WCAG)
Entwickler müssen Hardware und Software so konzipieren, dass sie barrierefrei nutzbar sind:
* **Eingabegeräte:** Unterstützung alternativer Eingaben (Screenreader, Spezialtastaturen, Spracheingabe).
* **Zwei-Sinne-Prinzip:** Informationen müssen über mindestens zwei der drei Sinne (Sehen, Hören, Tasten) wahrnehmbar sein (z. B. visuelle und akustische Signale bei Software-Systemfehlern).
* **Monitor-Anforderungen:** Hohe Kontrastverhältnisse, Farbtreue und flicker-freie Panels für Barrierefreiheit nach WCAG/BITV.

---

## 6. Matrix: Hardware-Auswahl nach FIAE-Einsatzbereich

| Einsatzbereich | CPU | RAM | Massenspeicher | GPU | Peripherie / Extras |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Web- & Frontend-Dev** | 6–8 Kerne | 16–32 GB | 512 GB NVMe SSD | iGPU | Dual-Monitor, USB-C Docking |
| **Backend- & Microservices-Dev** | 8–16 Kerne | 32–64 GB | 1–2 TB NVMe SSD | iGPU | Virtualisierung aktiv (VT-x), Linux/WSL2 |
| **AI / Data Science Dev** | 12+ Kerne | 64+ GB | 2 TB NVMe SSD | Dedicated NVIDIA (CUDA) | High-VRAM GPU, Effiziente Kühlung |
| **Mobile App Dev (iOS/Android)** | 8–12 Kerne | 32 GB | 1 TB NVMe SSD | iGPU / Mac Silicon | Xcode/Android Studio Emulatoren, Test-Devices |

---

## Zusammenfassung (FIAE-Perspektive)

Ein leistungsfähiger Entwickler-Arbeitsplatz erfordert ein ausgewogenes System ohne Flaschenhälse. Während CPU-Kerne die Kompilierzeit bestimmen und ausreichend RAM den flüssigen Betrieb von Container-Umgebungen sichert, sorgen schnelle NVMe-SSDs für zügige Build-Prozesse. Ergänzt durch ergonomische Multi-Monitor-Setups und barrierefreie Schnittstellen entsteht eine produktive und nachhaltige Arbeitsumgebung.
