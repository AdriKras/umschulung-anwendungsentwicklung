# 04-07: LF 4.3 Awareness, Physische Sicherheit & AI-Driven Threats

Dieses Modul behandelt moderne Awareness-Programme, den Umgang mit physischem Social Engineering (USB-Baiting), lösungsorientierte Phishing-Simulationen sowie Bedrohungen und Verteidigung durch Künstliche Intelligenz.

---

## 1. Sicherheitskultur, Awareness & Physisches Social Engineering

### Einmalige Schulung vs. Kontinuierliches Awareness-Programm
* **Einmalige Schulung:** Rein passives Frontalwissen; Wissen verblasst schnell, baut keine nachhaltige Sicherheitskultur auf.
* **Kontinuierliches Programm:** Regelmäßige, kurze Impulse (Micro-Learning), interaktive Tests und reale Simulationen verankern Sicherheitsbewusstsein im Alltag.

### Physische Angriffe: USB-Baiting / Dropping
* **Risiko:** Zielgerichtetes Auslegen scheinbar präparierter USB-Sticks (mit Rubber-Ducky-Payloads) auf dem Firmenparkplatz oder im Büro.
* **Verhaltensregel:** Fremde USB-Sticks **niemals** an Dienstgeräte anschließen! Abgabe direkt bei der IT-Sicherheit oder Nutzung einer isolierten "Hardware-Quarantäne-Station".

### Lösungsorientiertes Phishing-Simulationskonzept
1. **Kein Blaming / Keine Bestrafung:** Fehlerfreie Meldekultur (*No-Blame-Culture*) etablieren.
2. **Direktes Feedback:** Wer auf eine Test-Mail klickt, erhält sofort eine kurze, wertschätzende Erklärung der Erkennungsmerkmale.
3. **Einfacher Melde-Button:** Integration eines "Phishing melden"-Buttons direkt im E-Mail-Client.

---

## 2. KI-gestützte Bedrohungen & Defense AI

Künstliche Intelligenz verändert die Angriffs- und Verteidigungsmöglichkeiten im Cyberraum drastisch.

### KI in Phishing & Social Engineering
* **Personalisierte Phishing-Mails:** KI generiert fehlerfreie, grammatikalisch perfekte und hochgradig auf das Opfer zugeschnittene E-Mails unter Auswertung öffentlicher Social-Media-Profile.
* **Deepfakes (Audio & Video):** Echtzeit-Imitation von Stimmen und Videostreams der Geschäftsführung (*CEO Fraud* / *Voice Phishing*), um Mitarbeiter zur Freigabe von Überweisungen oder Zugängen zu verleiten.

### Offensive AI vs. Defensive AI

| Kategorie | Ausrichtung | FIAE- & Praxis-Beispiele |
| :--- | :--- | :--- |
| **Offensive AI** | Automatisierung von Angriffen durch Angreifer. | Automatisiertes Scannen nach Schwachstellen, KI-generierter polymorpher Schadcode, Deepfakes. |
| **Defensive AI** | Automatisierte Abwehr & Analyse durch IT-Security. | Verhaltensanalyse in Echtzeit (Anomaly Detection), KI-gestütztes Log-Monitoring (SIEM), automatisierte SOC-Reaktionen. |

---

## FIAE-Zusammenfassung
Softwareentwickler unterstützen die Awareness durch den Einbau von Melde-Buttons in firmeninternen Tools und berücksichtigen die Gefahren durch KI-basierte Social-Engineering-Angriffe bei Authentifizierungsprozessen (z. B. Mehr-Augen-Prinzip statt reiner Sprachfreigabe).
