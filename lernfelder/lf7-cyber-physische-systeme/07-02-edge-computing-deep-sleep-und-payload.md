# 07-02: LF 7.2 Edge Computing, Deep Sleep & effiziente Datenübertragung

Dieses Modul behandelt die lokale Verarbeitung von Sensordaten, die Optimierung batteriebetriebener Geräte und den Entwurf kompakter Nachrichtenformate. Ziel ist es, Cloud-Abhängigkeit, Reaktionszeit und Energieverbrauch zu reduzieren.

---

## 1. Edge Computing: Daten vor Ort verarbeiten

**Edge Computing** bedeutet, Daten nahe an ihrer Quelle zu verarbeiten – beispielsweise auf einem Mikrocontroller oder einem lokalen Gateway wie einem Raspberry Pi. Je nach Anwendung werden Rohdaten, zusammengefasste Werte oder nur relevante Ereignisse weitergeleitet.

| Vorteil | Erklärung | Beispiel |
| :--- | :--- | :--- |
| **Geringere Latenz** | Lokale Entscheidungen benötigen keinen Umweg über das Internet. | Lüfter bei Überschreiten einer Temperaturgrenze einschalten |
| **Weniger Datenverkehr** | Messwerte werden gefiltert oder zusammengefasst. | Minutenmittelwert statt vieler Einzelmessungen senden |
| **Geringere Cloud-Abhängigkeit** | Lokal implementierte Funktionen können ohne Internet weiterarbeiten. | Temperaturregelung bleibt bei Cloud-Ausfall aktiv |

**Wichtig:** Edge Computing garantiert nicht automatisch Reaktionen in Millisekunden oder vollständige Autarkie. Das hängt von Hardware, Software und lokalen Abhängigkeiten ab.

### Beispielkonzept: Raumklima überwachen

* **Sensorknoten:** Temperatur und Luftfeuchtigkeit erfassen.
* **Lokales Gateway:** Werte prüfen, Mittelwerte bilden und einen Lüfter mit Hysterese steuern: über 28 °C einschalten, unter 26 °C ausschalten.
* **Cloud:** Zusammenfassungen und Alarme speichern und im Dashboard anzeigen.
* **Bei Internetausfall:** Lokale Steuerung fortsetzen und Nachrichten begrenzt puffern; beim Nachsenden ursprüngliche Messzeitpunkte erhalten.

Das Gateway kann zusätzlich Protokolle übersetzen, etwa BLE-Messwerte entgegennehmen und als MQTT-Nachrichten über ein IP-Netz weitergeben.

**FIAE-Bezug:** Entwickler teilen Aufgaben zwischen Gerät, Gateway und Backend auf. Sie implementieren Filter, Regeln, Schnittstellen und das Verhalten bei Verbindungsausfällen.

---

## 2. Deep Sleep und Aufweckquellen

Aktive Funkkommunikation benötigt deutlich mehr Strom als eine Schlafphase. Der tatsächliche Verbrauch hängt unter anderem von Funkmodus, Sendeleistung und Board ab.

| Zustand | Verhalten |
| :--- | :--- |
| **Aktiv** | CPU verarbeitet Daten; Funk kann senden und empfangen. |
| **Deep Sleep** | Hauptprozessor, große Teile des RAM und Funk sind abgeschaltet; ausgewählte stromsparende Bereiche bleiben je nach Konfiguration aktiv. |

Beim klassischen ESP32 nennt das Datenblatt beispielsweise **10 µA für Deep Sleep mit RTC-Timer und RTC-Speicher**. Ein komplettes Entwicklungsboard kann durch Spannungsregler, LEDs und Sensoren erheblich mehr benötigen.

**RTC** bezeichnet den stromsparenden Zeitgeber-/Steuerungsbereich. Der **ULP-Coprozessor** ist eine separate Einheit und kann bei geeigneter Konfiguration einfache Aufgaben während des Tiefschlafs übernehmen. Er ist nicht mit der RTC gleichzusetzen.

### Aufwecken nach Zeit oder Ereignis

| Methode | Funktionsweise | Einsatz |
| :--- | :--- | :--- |
| **Timer-Wakeup** | Aufwachen nach einem festgelegten Intervall | Alle 15 Minuten Temperatur messen |
| **Externes Wakeup** | Ein geeignetes externes Signal weckt das Gerät über eine unterstützte Wakeup-Quelle | Türkontakt oder Bewegungssensor |

Ein gewöhnlicher GPIO-Interrupt ist nicht automatisch als Deep-Sleep-Wakeup geeignet. Unterstützte Pins und Signalbedingungen hängen vom Chip ab.

Nach Deep Sleep erfolgt beim ESP32 ein Neustartablauf. Benötigter Zustand muss gezielt erhalten oder rekonstruiert werden; die Funkverbindung wird neu aufgebaut.

**FIAE-Bezug:** Software muss Aufweckursachen unterscheiden, Zustände verwalten und Messung, Verbindung und Übertragung in möglichst kurzen Aktivphasen erledigen.

---

## 3. Batterielaufzeit bewerten und optimieren

Für eine überschlägige Rechnung gilt bei vergleichbaren Spannungsverhältnissen:

```text
Mittlerer Strom:
I_mittel = (I_aktiv × t_aktiv + I_schlaf × t_schlaf) / t_gesamt

Ideale Laufzeit in Stunden:
Laufzeit = nutzbare Kapazität in mAh / I_mittel in mA
```

### Rechenbeispiel

Annahmen: **2500 mAh**, **200 mA aktiv**, **10 µA = 0,01 mA im Schlaf** und ein Zyklus von **900 Sekunden**. Die Werte dienen als vereinfachtes Modell.

| Betrieb | Mittlerer Strom | Ideale Laufzeit |
| :--- | :--- | :--- |
| Dauerhaft aktiv | 200 mA | 12,5 Stunden |
| 2 Sekunden aktiv, 898 Sekunden Deep Sleep | ca. 0,454 mA | ca. 5501 Stunden bzw. 229 Tage |

Die Praxislaufzeit ist durch Selbstentladung, Temperatur, Spannungswandlung, Abschaltspannung und weitere Verbraucher begrenzt. Verbindungsaufbau und Wiederholungen zählen zur Aktivzeit und müssen gemessen werden.

### Maßnahmen zur Optimierung

* Sendeintervalle an den tatsächlichen Informationsbedarf anpassen.
* Bei Bedarf ereignisgesteuert aufwachen und Kontakte entprellen.
* Sensoren und Funk nur so lange wie nötig aktiv halten.
* Verbindungsversuche zeitlich begrenzen; endlose Wiederholungen vermeiden.
* Messwerte bündeln und unnötige Übertragungen vermeiden.
* Strom am gesamten Gerät messen und Annahmen damit überprüfen.

**Abwägung:** Ein schlafender Knoten führt nicht ständig seine normale Mess- und Steuerungslogik aus. Lange Schlafintervalle müssen zu den erlaubten Erkennungszeiten passen; ein externes Wakeup kann Ereignisse zusätzlich erfassen.

**FIAE-Bezug:** Energieeffizienz ist auch eine Softwareaufgabe: Zeitlimits, Zustandsautomaten und Sendeentscheidungen beeinflussen die Laufzeit direkt.

---

## 4. Payload, Overhead und Datenformate

* **Payload:** Die Nutzdaten auf der betrachteten Protokollebene, beispielsweise Temperatur und Luftfeuchtigkeit.
* **Overhead:** Zusätzliche Informationen für die Übertragung, etwa MQTT-Topic, TCP-/IP-Header und Sicherungsinformationen.

Welche Bytes Payload sind, hängt von der Ebene ab: Eine komplette MQTT-Nachricht ist beispielsweise Teil der TCP-Nutzdaten.

### Dasselbe Wertepaar in verschiedenen Formaten

Beispiel: **22,5 °C** und **60,0 % relative Luftfeuchtigkeit**. Die Größen gelten ohne Zeilenumbruch und ohne Protokoll-Overhead.

| Format | Darstellung | Größe |
| :--- | :--- | :--- |
| **JSON** | `{"temperatur":22.5,"feuchte":60.0}` | 34 Bytes in UTF-8 |
| **Kompakter Text** | `22.5;60.0` | 9 Bytes in UTF-8 |
| **Binär** | Zwei 16-Bit-Ganzzahlen: 225 und 600 | 4 Bytes |
| **Hex-Text dieser Binärdaten** | `00e10258` | 8 Bytes in UTF-8 |

### Ein kompaktes Binärformat festlegen

| Position | Datentyp | Bedeutung |
| :--- | :--- | :--- |
| Byte 0–1 | Signed 16 Bit, Big Endian | Temperatur in Zehntelgrad Celsius |
| Byte 2–3 | Unsigned 16 Bit, Big Endian | Relative Luftfeuchtigkeit in Zehntelprozent |

**Hexadezimal ist zunächst eine Darstellung, kein automatischer Speichergewinn.** Ein Byte benötigt zwei Hex-Zeichen. Als Text versendete Hex-Daten sind deshalb größer als die entsprechenden Rohbytes.

Auch die Skalierung muss stimmen: **22,5 × 10 = 225 = 0x00E1**. Der Wert `0x165` entspricht dagegen 357.

**FIAE-Bezug:** Sender und Backend müssen Reihenfolge, Datentypen, Byte-Reihenfolge, Skalierung und Einheiten gemeinsam festlegen. Für Erweiterungen ist eine Formatversion sinnvoll.

---

## 5. Time-on-Air und Verarbeitung im Backend

**Time-on-Air** ist die Dauer einer Funkübertragung. Kleinere Nachrichten können die aktive Sendezeit und damit den Energiebedarf reduzieren.

Bei unveränderter Datenrate gilt vereinfacht:

```text
Sendezeit ≈ übertragene Bits / Datenrate
```

Eine Reduktion von **100 auf 10 Payload-Bytes** spart **90 % der Nutzdaten**. Die gesamte Funkzeit sinkt nicht zwingend um 90 %: Präambel, Header, Bestätigungen und Funkparameter tragen ebenfalls dazu bei. Bei LoRa kommen unter anderem Spreading Factor und Bandbreite hinzu.

### Anforderungen an das Backend

1. **Format erkennen:** Gerätetyp und gegebenenfalls Formatversion bestimmen.
2. **Nachricht prüfen:** Länge, Datentypen und Wertebereiche kontrollieren.
3. **Dekodieren:** Bytes mit vereinbarter Byte-Reihenfolge lesen und skalieren.
4. **Zuordnen:** Sensoridentität und Messzeitpunkt aus Nachricht oder Übertragungskontext übernehmen.
5. **Speichern:** Einheitliche Werte in der Datenbank ablegen; fehlerhafte Nachrichten nachvollziehbar behandeln.

Beispiel für das oben definierte Format mit der Python-Standardbibliothek:

```python
import struct

payload = struct.pack(">hH", 225, 600)
temperatur_roh, feuchte_roh = struct.unpack(">hH", payload)

temperatur_c = temperatur_roh / 10
luftfeuchtigkeit_prozent = feuchte_roh / 10
```

**FIAE-Bezug:** Kompakte Übertragung verschiebt Aufwand in die Software. Ein dokumentiertes Datenformat und passende Prüfungen verhindern, dass Bytes falsch interpretiert werden.

---

## FIAE-Zusammenfassung

1. **Lokal verarbeiten:** Filter und Steuerungsregeln nahe an den Sensoren ausführen.
2. **Abhängigkeiten reduzieren:** Lokale Funktionen und begrenzte Puffer für Internetausfälle vorsehen.
3. **Aktivzeit verkürzen:** Schlafphasen, Wakeup-Ereignisse und Verbindungsaufbau aufeinander abstimmen.
4. **Daten kompakt übertragen:** Lesbarkeit, Datenmenge und Dekodierungsaufwand gegeneinander abwägen.
5. **Wirkung messen:** Stromverbrauch, Reaktionszeiten und Datenvolumen am realen System prüfen.

**Merksatz:** Weniger Cloud-Aufrufe, kürzere Aktivphasen und kompakte Nachrichten können Energie sparen – wenn sie zu den Anforderungen der Anwendung passen.

---

## Quellen zur fachlichen Vertiefung

* [Espressif: ESP32 Sleep Modes](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/sleep_modes.html)
* [Espressif: ESP32 Series Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
* [RFC 8259: JSON](https://www.rfc-editor.org/rfc/rfc8259.html)
* [RFC 4648: Base16-/Hex-Kodierung](https://www.rfc-editor.org/rfc/rfc4648.html)

