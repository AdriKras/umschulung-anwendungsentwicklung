# 04-03: LF 4.2 BSI-Grundschutz-Methodik, Infrastruktur & Datenträgersicherheit

Dieses Modul behandelt den BSI-Grundschutz-Prozess, Schutzbedarfsanalyse-Regeln (Maximumprinzip, Kumulations-/Verteilungseffekt), physische Infrastruktursicherheit (USV-Berechnung, Kühlung) sowie sicheres Decommissioning von Datenträgern.

---

## 1. BSI-Grundschutz-Methodik & Schutzbedarfsanalyse

### Phasen der BSI-Analyse
1. **Strukturanalyse:** Erfassung aller IT-Systeme, Anwendungen, Räume und Netzwerke im Informationsverbund.
2. **Schutzbedarfsfeststellung:** Bewertung bezüglich Vertraulichkeit, Integrität und Verfügbarkeit in den Stufen *Normal*, *Hoch* und *Sehr hoch*.
3. **Modellierung & Maßnahmenableitung:** Zuordnung passender BSI-Bausteine und Umsetzungsprüfung von TOMs.

### Regeln der Schutzbedarfs-Vererbung
* **Maximumprinzip (Grundregel):** Ein IT-System übernimmt den höchsten Schutzbedarf der darauf verarbeiteten Anwendungen oder Daten.
* **Kumulationseffekt (Abweichung nach oben):** Mehrere Anwendungen mit "Normalem" Schutzbedarf auf einem System können in der Summe zu einem "Hohen" Gesamtschaden bei Ausfall führen.
* **Verteilungseffekt (Abweichung nach unten):** Der Schutzbedarf verringert sich für ein Einzelsystem, wenn Daten redundant auf mehrere unabhängige Server verteilt sind.

---

## 2. Physische Infrastruktur, USV & Kühlung

### Physische Hauptrisiken
Brand (Rauchgase/Hitze), Wasserschaden (Rohrbruch/Löschwasser), Diebstahl/Zutritt Unbefugter, Stromausfall/Spannungsschwankungen.

### USV-Berechnung (Unterbrechungsfreie Stromversorgung)
Formel für die benötigte elektrische Wirkleistung $P$ (in Watt) und Scheinleistung $S$ (in VA):
$$P_{\text{Gesamt}} = \sum P_{\text{Komponenten}} \times \text{Sicherheitsreserve (z. B. 1,2)}$$
$$S = \frac{P}{\cos \varphi} \quad (\text{wobei } \cos \varphi \approx 0{,}8 \text{ bis } 0{,}9 \text{ Leistungsfaktor})$$

* **USV-Überbrückungszeit:** Muss ausreichen, um Server bei Stromausfall über Skripte geordnet herunterzufahren (*Graceful Shutdown*).
* **Kühlung (PUE - Power Usage Effectiveness):** Verwendungsgrad der Energie im Rechenzentrum ($\text{PUE} = \frac{\text{Gesamtenergie}}{\text{IT-Energie}}$). Optimierung durch Warm-/Kaltgang-Trennung.

---

## 3. Risiken mobiler Datenträger & Sicheres Decommissioning

### Risiken bei USB-Sticks, externen SSDs & Laptops
Verlust/Diebstahl ohne Verschlüsselung, Einschleppen von Malware (Baiting), Datenverlust durch mechanische/elektrische Schäden.

### Löschen vs. Sicheres Vernichten (Decommissioning)
* **Logisches Löschen (Dateisystem):** Entfernt nur den Verweis im Dateisystem-Index (z. B. FAT/NTFS). Die Rohdaten sind mit Forensik-Tools vollständig rekonstruierbar!
* **Mehrfaches Überschreiben (HDD):** Sicheres Überschreiben der gesamten Festplatte mit Zufallsmustern (z. B. DoD 5220.22-M, `dd`, `shred`).
* **Secure Erase / ATA Sanitization (SSD):** Durchführen eines NVMe/SATA Hardware-Reset-Befehls zum Löschen der Flash-Zellen.
* **Physische Vernichtung:** Mechanisches Zerschreddern (Shreddern nach DIN 66399 Schutzklasse 3) oder Entmagnetisieren (Degaussing - nur bei HDDs/Bändern).

---

## FIAE-Zusammenfassung
Entwickler müssen den Verteilungseffekt bei Microservices nutzen (High Availability) und beim Bau mobiler Apps darauf achten, dass lokale Daten auf Endgeräten zwingend verschlüsselt gespeichert werden.
