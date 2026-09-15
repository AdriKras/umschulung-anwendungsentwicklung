# 02-07: Betriebssysteme, Kernel-Architektur & Systemkonzeption

Betriebssysteme (OS) bilden die Abstraktionsschicht zwischen Hardware und Software. Sie verwalten Ressourcen und schützen das System vor Fehlfunktionen.

---

## 1. Kernaufgaben (Abstraktion & Ressourcen)
* **Abstraktion:** Einheitliche Schnittstellen (System Calls / APIs) zur Hardware.
* **Ressourcenverwaltung:** CPU-Scheduling, virtuelle Speicherverwaltung (Paging) und I/O-Steuerung.

---

## 2. Kernel-Architektur & Ring-Modell
* **Ring-Modell:** Schutzebenen von Ring -3 bis Ring 3.
  * **Ring 0 (Kernel Space):** Volle Hardwarerechte, Treiber, Memory Manager. Absturz = Kernel Panic.
  * **Ring 3 (User Space):** Eingeschränkte Rechte für Anwendungen. Zugriff nur via Syscalls.
* **Sicherheit:** Bootkits unter Ring 0 begegnen mit **Secure Boot** (UEFI-PKI) und TPM 2.0.

---

## 3. Historie & Generationen
* **4 Generationen:** Vakuumröhren (kein OS) -> Transistoren (Batch) -> ICs (Time-Sharing) -> VLSI/Mikroprozessoren (GUIs, PCs).
* **Batch vs. Time-Sharing:** Sequential-Abarbeitung ohne Interaktion (Batch) vs. Zeit-Slicing für Multitasking (Time-Sharing).
* **Meilensteine:** GM-NAA I/O (erstes OS), Unix (C, "Everything is a file"), Windows NT (32-Bit Kernel).

---

## 4. Plattformen im Vergleich
* **Windows:** Entstehung aus DOS & NT (Fusion in XP). OEM-Bündelung bringt Marktführerschaft. Nutzt Registry und Laufwerksbuchstaben.
* **Linux & GNU:** Kernel von Torvalds + Tools von Stallman. Open Source. Struktur nach Filesystem Hierarchy Standard (FHS; `/`, `/bin`, `/etc`).
* **macOS / BSD:** Unix-Basis (Darwin/BSD). APFS-Dateisystem, enge HW-SW-Verzahnung. FreeBSD (Server/Storage), OpenBSD (Focus auf Security).
* **Mobile (Android/iOS):** Android nutzt Linux-Kernel; iOS nutzt XNU. **Sandboxing** isoliert Apps. App-Store-Zwang vs. Sideloading (EU DMA).

---

## 5. Dateisysteme
| System | Max. Dateigröße | Plattform | Features |
| :--- | :--- | :--- | :--- |
| **FAT32** | 4 GB | Universell | Kein Journaling, keine Rechte. |
| **exFAT** | 16 EB | Cross-Platform | Ideal für Flash-Speicher/USB. |
| **NTFS** | 8 PB | Windows | Journaling, ACL-Rechte, EFS. |
| **ext4** | 16 TB | Linux | Journaling, POSIX-Rechte (`rwx`). |
| **APFS** | 8 EB | macOS/iOS | Snapshots, Fast-Cloning, Encryption. |

---

## 6. OS-Strategie & Infrastruktur
* **Einsatzzwecke:** Windows (Office/AD), Linux (Server/Docker/Kiosk), macOS (iOS-Dev/Design).
* **Legacy-Systeme:** Isolation alter OS-Versionen in separaten VLANs oder via VDI/Container.
* **Mobile & Cloud:** MDM für Policies, Work-Profiles für BYOD und Zero-Trust mit MFA/VPN.
