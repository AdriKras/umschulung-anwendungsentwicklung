# 02-04: Komponenten & Systemarchitektur von IT-Arbeitsplätzen

Dieses Modul fasst die Kernkomponenten modularer PC-Systeme, Bus-Systeme und Evaluierungskriterien für Hardware-Komponenten zusammen.

---

## 1. Hauptkomponenten eines IT-Arbeitsplatzes
* **Mainboard (Motherboard):** Zentrale Platine mit Chipsatz (Formfaktoren: ATX, Micro-ATX, Mini-ITX). Verknüpft CPU, RAM und Erweiterungskarten via Bus-Systeme.
* **Prozessor (CPU):** Steuerung und Berechnung (Taktfrequenz, Anzahl Kerne/Threads, Cache L1/L2/L3).
* **Arbeitsspeicher (RAM):** Volatiler Hauptspeicher (DDR4/DDR5). Entscheidend für Multitasking und Entwicklungsumgebungen (IDEs, Docker).
* **Massenspeicher:** SSD (NVMe via PCIe vs. SATA) für Betriebssystem und Projekt-Repositorys; HDDs für Langzeit-Archivierung.

---

## 2. Bus-Systeme & Interne Schnittstellen
* **PCIe (PCI Express):** Serielle Punkt-zu-Punkt-Verbindung (PCIe 3.0/4.0/5.0) für Grafikkarten und schnelle NVMe-SSDs.
* **Bussysteme:** Datenbus (Datenübertragung), Adressbus (Adressierung von Speicherzellen), Steuerbus (Signale & Befehle).

---

## 3. Komponentenauswahl für Entwickler-Workstations
* **Dimensionierung:** Priorisierung von hohem RAM (min. 32 GB) und schneller NVMe-SSD gegenüber Highend-Grafikkarten.
* **Kühl- und Netzteil-Auslegung:** Effiziente Netzteile (80 PLUS Gold/Platinum) und leise Kühlung für ergonomische Geräuschemissionen nach ArbStättV.
