# LF 2.1: Die Logik der Maschine & Hardware-Grundlagen (FIAE-Fokus)

In diesem Themenbereich werden die mathematischen, logischen und architektonischen Grundlagen von Computersystemen behandelt. Für Anwendungsentwickler bildet dieses Wissen das Fundament für datentypsicheres Programmieren, Bit-Operationen, Speicherverwaltung und die systemnahe Optimierung von Algorithmen.

---

## 1. Zahlensysteme & Speichergrößen in der Anwendungsentwicklung

### Zahlensysteme (Dezimal, Dual, Hexadezimal)

In der Softwareentwicklung werden Daten auf unterster Ebene binär verarbeitet und im Quellcode oder Debugger häufig hexadezimal dargestellt (z. B. Speicheradressen, Farbwerte, Byte-Arrays).

* **Dezimalsystem (Basis 10):** Menschliche Zahlendarstellung (0-9).
* **Dualsystem / Binärsystem (Basis 2):** Maschinenverarbeitung (0, 1).
* **Hexadezimalsystem (Basis 16):** Kompakte Darstellung von Binärdaten (0-9, A-F). Ein Hex-Zeichen entspricht exakt 4 Bits (Nibble).

#### Umrechnungsbeispiel (Zahl 213)
* **Dezimal:** 213
* **Dual:** 11010101 (128 + 64 + 0 + 16 + 0 + 4 + 0 + 1)
* **Hexadezimal:** D5 (1101 = D, 0101 = 5)

### Speichergrößen: SI-Präfixe vs. IEC-Binärpräfixe

Ein häufiges Problem bei Datenbankspeichern, File-Uploads und Festplattenherstellern ist die Abweichung zwischen dezimaler (SI) und binärer (IEC) Speicherberechnung.

| Standard | Basis | Einheiten | Beispiel | Verwendung |
| :--- | :--- | :--- | :--- | :--- |
| **SI-Standard (Dezimal)** | 10^3 = 1.000 | KB, MB, GB, TB | 1 GB = 1.000.000.000 Bytes | Marketing, Festplattenhersteller, Netzwerkspeed |
| **IEC-Standard (Binär)** | 2^10 = 1.024 | KiB, MiB, GiB, TiB | 1 GiB = 1.073.741.824 Bytes | Betriebssysteme (Windows/Linux), RAM, Datenbank-Caches |

#### Mathematische Herleitung der Diskrepanz
Wird eine Festplatte mit 1 TB (10^12 Bytes) im Betriebssystem angezeigt, rechnet dieses in Tebibytes (TiB) bzw. Gibibytes (GiB):

1.000.000.000.000 Bytes / 1.024^3 = 931,32 GiB

**FIAE-Praxisrelevanz:** Bei der Entwicklung von APIs, Validierungslogiken (z. B. File-Upload-Limits) und Datenbankinfrastrukturen muss explizit zwischen Megabyte (MB) und Mebibyte (MiB) unterschieden werden, um Speicherüberläufe und Parsing-Fehler zu vermeiden.

---

## 2. Logische Schaltglieder (Gatter) & Boolesche Algebra

Logikgatter bilden die physikalische Basis für Prozessoren und spiegeln sich direkt in den logischen Operatoren von Programmiersprachen wider (&&, ||, !, ^).

### Wahrheitstabellen der Grundgatter

#### AND (UND) – &&
Beide Eingänge müssen 1 sein.
| A | B | Y |
| :-: | :-: | :-: |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

#### OR (ODER) – ||
Mindestens ein Eingang muss 1 sein.
| A | B | Y |
| :-: | :-: | :-: |
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **1** |

#### XOR (Exklusiv-ODER) – ^
Genau ein Eingang muss 1 sein (ungleiche Eingänge).
| A | B | Y |
| :-: | :-: | :-: |
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | 0 |

#### NOT (Inverter) – !
Invertiert den Eingangszustand.
| A | Y |
| :-: | :-: |
| 0 | **1** |
| 1 | **0** |

**FIAE-Praxisrelevanz:** Neben Bedingungsprüfungen (if/else) werden bitweise Operationen (Bit-Maskierung via XOR/AND) für Hochleistungsanwendungen, Rechteverwaltung (Bitmasks) und Kryptographie eingesetzt.

---

## 3. Die Von-Neumann-Architektur & Datenfluss

Die Von-Neumann-Architektur beschreibt das Grundmodell eines Universalrechners. Kennzeichnend ist, dass sich Daten und Befehle im selben Speicher (Shared Memory) befinden.

### Grundkomponenten

1. **CPU (Central Processing Unit):**
   * **ALU (Arithmetic Logic Unit):** Führt arithmetische und logische Operationen aus.
   * **Control Unit (Steuerwerk):** Dekodiert Befehle und steuert den Datenfluss.
   * **Register:** Extrem schnelle, interne Speichereinheiten (z. B. Akkumulator, Befehlszähler).
2. **Hauptspeicher (RAM):** Speichert sowohl den auszuführenden Quellcode (Maschinenbefehle) als auch die Laufzeitdaten (Variablen, Objekte).
3. **I/O-Einheit (Input/Output):** Schnittstelle zur Außenwelt (Tastatur, Bildschirm, Netzwerkkarten).
4. **Bussysteme:** Verbinden die Komponenten.

### Die drei Bussysteme

* **Datenbus:** Überträgt die eigentlichen Daten und Befehle (bidirektional).
* **Adressbus:** Überträgt die Speicheradresse, von der gelesen oder auf die geschrieben werden soll (unidirektional von CPU zu RAM).
* **Steuerbus (Controlbus):** Überträgt Steuersignale (z. B. Read/Write-Befehle, Taktimpulse, Interrupts).

### Das EVA-Prinzip (Eingabe - Verarbeitung - Ausgabe)

Jede Softwareanwendung folgt dem EVA-Prinzip:
* **Eingabe:** Tastatureingabe, REST-API-Request, Sensorwerte.
* **Verarbeitung:** Algorithmen in der CPU, Datenbankabfragen im RAM.
* **Ausgabe:** GUI-Anzeige, JSON-Response, Speichern auf Massenspeicher.

**FIAE-Praxisrelevanz (Von-Neumann-Flaschenhals):** Da Daten und Befehle über denselben Bus transportiert werden, entsteht bei datenintensiven Anwendungen ein Engpass zwischen CPU und RAM. Entwickler steuern dem durch effizientes Caching, Vermeidung unnötiger Speichertransfers und Nutzung lokaler Variablen entgegen.

---

## 4. Befehlszyklus & Prozessorperformance

Ein Prozessor arbeitet Programme ab, indem er Maschinenbefehle im Takt der CPU kontinuierlich durchläuft.

### Der Befehlszyklus (Fetch - Decode - Execute)

1. **Fetch (Holen):** Die Control Unit liest den nächsten Befehl aus der im Befehlszähler (Instruction Pointer) hinterlegten RAM-Adresse.
2. **Decode (Dekodieren):** Der Befehl wird im Befehlsdekoder aufgeschlüsselt (Welche Operation? Welche Register/Operanden?).
3. **Fetch Operands (Operanden holen):** Bei Bedarf werden benötigte Variablenwerte aus dem RAM/Register nachgeladen.
4. **Execute (Ausführen):** Die ALU führt die Berechnung aus (z. B. Addition zweier Registerwerte).
5. **Writeback (Rückschreiben):** Das Ergebnis wird in ein Register oder zurück in den Hauptspeicher geschrieben.

### Taktfrequenz & Rechengeschwindigkeit

* **Taktfrequenz (Hz):** Gibt an, wie viele Taktimpulse die CPU pro Sekunde erzeugt (z. B. 3,5 GHz = 3,5 Milliarden Taktzyklen/Sekunde).
* **IPC (Instructions Per Cycle):** Anzahl der Befehle, die pro Taktzyklus abgearbeitet werden können.
* **Performance-Formel:** Prozessorleistung = Taktfrequenz x IPC

---

## 5. Didaktische Reduktion für Nicht-Techniker (Kunden-Kommunikation)

Als Anwendungsentwickler muss man komplexe Hardware-Abläufe gegenüber Kunden oder dem Management verständlich erklären können.

### Analogie: Die CPU als Chefkoch in einer Großküche

* **CPU (Prozessor):** Der Chefkoch. Seine Arbeitsgeschwindigkeit entspricht der Taktfrequenz.
* **Register:** Die Schneidebretter direkt in der Hand des Kochs (sofort verfügbar, sehr klein).
* **RAM (Hauptspeicher):** Der Arbeitstisch in der Küche. Alles, was aktuell zubereitet wird, liegt hier bereit.
* **Festplatte/SSD (Massenspeicher):** Der Kühlraum im Keller. Sehr groß, aber der Weg dorthin dauert lange.
* **Bussystem:** Die Küchengehilfen, die Zutaten zwischen Keller, Arbeitstisch und Chefkoch hin- und hertragen.
* **Befehlszyklus (Fetch-Decode-Execute):** 
  1. Rezeptzeile lesen (Fetch).
  2. Verstehen, welche Zutaten gebraucht werden (Decode).
  3. Zutaten mischen/kochen (Execute).
