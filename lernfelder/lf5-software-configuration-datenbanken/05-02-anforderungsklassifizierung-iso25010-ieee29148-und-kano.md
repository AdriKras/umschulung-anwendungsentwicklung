# 05-02: LF 5.1 Anforderungsklassifizierung, ISO/IEC 25010, IEEE 29148 Syntax & Kano-Modell

Dieses Modul behandelt die Kategorisierung von Anforderungen, das Qualitätsmodell nach ISO/IEC 25010, die atomsichere Formulierung nach IEEE 29148 Syntax sowie die Priorisierung mittels Kano-Modell.

---

## 1. Klassifizierung von Anforderungen

| Anforderungstyp | Definition | FIAE-Praxisbeispiel |
| :--- | :--- | :--- |
| **Funktionale Anforderung (FA)** | Beschreibt, *was* das System direkt leisten oder berechnen muss (Funktionen, Prozesse). | "Das System muss Rechnungs-PDFs automatisch aus Bestelldaten generieren." |
| **Nicht-Funktionale Anforderung (NFA)** | Beschreibt Qualitätskriterien und Performance-Eigenschaften des Systems. | "Die DB-Abfrage darf unter Vollast max. 100ms dauern." |
| **Randbedingung (Constraint)** | Organisatorische, rechtliche oder technologische Einschränkungen. | "Das Backend muss in Java 21 auf Docker-Containern betrieben werden." |

---

## 2. Das Qualitätsmodell nach ISO/IEC 25010

NFAs werden nach ISO/IEC 25010 in 8 Hauptqualitätsmerkmale unterteilt:

* **Funktionale Angemessenheit:** Vollständigkeit und Korrektheit der Funktionen.
* **Leistungseffizienz (Performance):** Antwortzeiten, Durchsatz, Ressourcenverbrauch.
* **Kompatibilität:** Interoperabilität mit anderen Systemen und Schnittstellen.
* **Benutzbarkeit (Usability):** Erlernbarkeit, Barrierefreiheit, Fehlerschutz.
* **Zuverlässigkeit (Reliability):** Verfügbarkeit, Fehlertoleranz, Wiederherstellbarkeit.
* **Sicherheit (Security):** Vertraulichkeit, Integrität, Nicht-Abstreitbarkeit, Authentizität.
* **Wartbarkeit (Maintainability):** Modulariät, Analysierbarkeit, Testbarkeit, Modifizierbarkeit.
* **Übertragbarkeit (Portability):** Anpassbarkeit, Installierbarkeit, Austauschbarkeit.

---

## 3. Exakte Formulierung nach IEEE 29148 (Schablonentechnik)

Anforderungen müssen **messbar, atomar (nicht zusammengesetzt) und prüfbar** sein.

### Syntax-Schema für Satzschablonen
```text
[System] + [Verbindlichkeit (muss/soll/kann)] + [Bedingung/Wenn] + [Aktivität/Prozess] + [Objekt]
```

### Beispiel für die Transformation einer vagen Aussage
* **Vage / Zusammengesetzt:** *"Das System soll Benutzern das Einloggen erlauben und Passwörter sicher speichern und schnell sein."*
* **Atomarisierung nach IEEE 29148:**
  1. **FA 01:** "Das System **muss** dem Benutzer eine Maske zur Eingabe von Benutzername und Passwort bereitstellen."
  2. **FA 02:** "Das System **muss** eingehende Passwörter mittels Argon2id vor der Speicherung hashen."
  3. **NFA 01:** "Das System **muss** den Authentifizierungsprozess in unter 300 Millisekunden abschließen."

---

## 4. Priorisierung mit dem Kano-Modell

Das Kano-Modell teilt Merkmale basierend auf ihrer Auswirkung auf die Kundenzufriedenheit ein:

| Merkmalsart | Auswirkung / Beschreibung | Entwickler-Konsequenz |
| :--- | :--- | :--- |
| **Basis-Merkmale (Must-Have)** | Werden als selbstverständlich vorausgesetzt. Fehlen führt zu extremer Unzufriedenheit, Erfüllung schafft keine Extra-Begeisterung. | Absolute Pflicht (z. B. Absturzsicherheit, Login-Funktion). |
| **Leistungs-Merkmale (Performance)** | Werden explizit gefordert. Zufriedenheit steigt proportional zur Leistung. | Erfüllung ist Kern des Vertrags (z. B. Akkulaufzeit, Ladezeit). |
| **Begeisterungs-Merkmale (Delighter)** | Unerwartete Zusatzfunktionen. Fehlen stört nicht, Vorhandensein erzeugt hohe Begeisterung. | Differenzierung am Markt (z. B. Ein-Klick-Export, KI-Auto-Complete). |

---

## FIAE-Zusammenfassung
Entwickler zerlegen komplexe Kundenanforderungen mit der IEEE 29148 Schablone in eindeutige, atomare Testfälle und klassifizieren Nicht-Funktionale Anforderungen strikt nach ISO/IEC 25010.
