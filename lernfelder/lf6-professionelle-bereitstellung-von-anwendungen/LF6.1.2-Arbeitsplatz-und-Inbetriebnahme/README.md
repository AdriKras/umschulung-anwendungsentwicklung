# LF 6.1.2 - Arbeitsplatzaufbau, Ergonomie und elektrische Sicherheit

## 1. Übersicht und Einordnung

Vor der Inbetriebnahme von IT-Systemen im Betrieb oder beim Kunden müssen Hardwaresysteme sachgerecht aufgebaut, sicher verkabelt und geprüft werden. Für Anwendungsentwickler (FIAE) ist dies sowohl bei der Einrichtung des eigenen Entwicklerarbeitsplatzes als auch beim Testen von Hardware-Schnittstellen und Rollouts relevant. Es gelten strenge gesetzliche Arbeitsschutzvorschriften (DGUV, ArbStättV) und technische Prüfstandards (VDE).

---

## 2. Elektrische Sicherheit und DGUV Vorschrift 3 (AP1-Basiswissen)

### Sichere Inbetriebnahme und VDE-Sichtprüfung (DGUV V3 / VDE 0701-0702)
Jedes elektrische Betriebsmittel (PC, Monitor, Netzteil) muss vor der ersten Nutzung sowie nach Reparaturen oder Änderungen einer Sichtprüfung unterzogen werden.

* **Prüfkriterien der Sichtprüfung:**
  * **Gehäuse:** Schutzeinrichtungen intakt, keine Risse oder Ausbrüche, keine thermischen Verfärbungen / Hitzespuren.
  * **Isolierung & Leitungen:** Keine Quetschungen, Knicke, Schnitte oder offenen Adern bei Anschlusskabeln.
  * **Zugentlastung:** Netzstecker und Geräteeinführungen müssen mechanisch gegen Ausreißen gesichert sein.
  * **Stecker:** Keine verbogenen Kontakte, keine Schmorerspuren, Schutzleiterkontakte sauber.
* **Maßnahme bei Mängeln:** Betroffene Geräte dürfen **nicht in Betrieb genommen** werden, müssen sofort gekennzeichnet/gesperrt und durch eine Elektrofachkraft instandgesetzt oder entsorgt werden.

---

## 3. Ergonomie am Bildschirmarbeitsplatz (Arbeitsstättenverordnung)

Die Gestaltung von Bildschirmarbeitsplätzen ist in der Arbeitsstättenverordnung (Anhang 6) und DGUV Information 215-410 geregelt. Ziel ist das Vermeiden körperlicher Fehlbelastungen und Sehkorrekturen.

### Anordnung von Bildschirm und Peripherie
* **Sehabstand:** Der Abstand zwischen Augen und Monitor sollte je nach Bildschirmdiagonale **50 bis 70 cm** betragen.
* **Monitorhöhe:** Die Oberkante des Bildschirms sollte maximal auf Augenhöhe liegen (Blickachse leicht nach unten geneigt um ca. 35°).
* **Lichteinfall und Reflexionen:**
  * Blickrichtung parallel zur Fensterfront ausrichten.
  * Vermeidung von Blendungen und Spiegelungen auf dem Bildschirm durch direkte Sonneneinstrahlung im Rücken oder vor dem Monitor.
* **Eingabegeräte:** Tastatur und Maus auf einer Ebene platziert. Handgelenke müssen bei der Bedienung flach aufliegen können (ca. 5–10 cm Platz vor der Tastatur).

---

## 4. Verkabelung und Kabelmanagement

### Trennung von Strom- und Datenleitungen
* **Physikalische Trennung:** Stromführende Netzkabel (230V) und empfindliche Datenkabel (z. B. Ethernet, USB, HDMI) müssen räumlich getrennt verlegt werden.
* **Elektromagnetische Verträglichkeit (EMV):** Parallel verlegte Wechselstromleitungen können Induktionen erzeugen und Datenübertragungsfehler verursachen.
* **Stolperfallen vermeiden (DGUV-Regel 108-007):**
  * Kabel dürfen nicht lose im Fußraum oder über Verkehrswege hängen.
  * Einsatz von Kabelkanälen, Klettbindern, Kabelbrücken oder Unter-Tisch-Wannen.
  * Gefahren bei Kabelsalat: Personalstolpern (Verletzungsgefahr) und Absturzgefahr für Hardware.

---

## 5. Bedeutung für die Anwendungsentwicklung (FIAE)

* **Einhaltung von Arbeitsschutzstandards:** Eigenständige und rechtssichere Einrichtung des Entwicklungsarbeitsplatzes (Höhenverstellbarkeit, Lichtverhältnisse, Ergonomie für langes Codieren).
* **Betriebssicherheit beim Testen:** Beim Anschluss von Testgeräten, Entwicklerboards oder Peripherie muss die elektrische Unversehrtheit sichergestellt sein.
* **Ausfallprävention:** Ordnungsgemäße Verkabelung verhindert Datenverluste, Netzwerkausfälle und Hardwareschäden durch versehentliches Herausziehen von Kabeln im laufenden Betrieb.
