# 04-04: LF 4.2 TOMs, OWASP SQL-Injection, CVSS & Incident Response

Dieses Modul behandelt technische und organisatorische Maßnahmen (TOMs), OWASP-Sicherheitslücken (SQL Injection), den Lifecycle von Vulnerabilities (CVE/CVSS), Update-Rollouts sowie den Incident-Response-Prozess.

---

## 1. TOMs nach DSGVO Art. 32 & Moderne Passwort-Standards

* **Technische Maßnahmen (TOM-T):** Verschlüsselung (TLS 1.3, AES-256), Firewalls, Datenbank-Hardening, Passkey/MFA-Zwang.
* **Organisatorische Maßnahmen (TOM-O):** Berechtigungskonzepte, Notfallhandbuch, regelmäßige Awareness-Trainings.

### Moderne Passwort-Richtlinien (BSI / NIST SP 800-63B)
* **Keine erzwungene periodische Rotation** (führt sonst zu schwachen Variationen wie `Sommer2024!`).
* **Länge vor Komplexität:** Passphrasen mit mindestens 12–16 Zeichen bevorzugen.
* **Prüfung gegen Leaks:** Passwörter gegen Listen kompromittierter Passwörter prüfen (z. B. HaveIBeenPwned API).
* **MFA Pflicht:** Multi-Faktor-Authentifizierung für alle Zugänge.

---

## 2. SQL-Injection (SQLi) & Defense ("Never Trust User Input")

Eine SQL-Injection entsteht, wenn ungeprüfte Benutzereingaben direkt in Datenbank-Queries konkateniert werden.

### Verwundbarer Code (Beispiel)
```sql
-- Eingabe im Formular: admin' --
SELECT * FROM users WHERE username = 'admin' --' AND password = '...'
-- Bypasst die Passwort-Abfrage vollständig!
```

### Effektive Gegenmaßnahmen für Entwickler
1. **Prepared Statements / Parameterized Queries (Standard):** Trennung von Code und Daten auf Treiber-Ebene.
```python
# Sichere Variante in Python/DB-API
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user_input, pass_input))
```
2. **ORM-Frameworks nutzen:** Einsatz von SQLAlchemy, Hibernate, Entity Framework.
3. **Input Validation & Sanitization:** Strikte Typisierung und Whitelisting von Eingabewerten.

---

## 3. Vulnerability Management: CVE, CVSS & Update-Rollout

### Lifecycle einer Sicherheitslücke
 Entdeckung $\rightarrow$ Stille Meldung an Hersteller (*Responsible Disclosure*) $\rightarrow$ Patch-Entwicklung $\rightarrow$ Zuweisung einer **CVE-ID** (Common Vulnerabilities and Exposures) $\rightarrow$ Veröffentlichung.

### CVSS-Score (Common Vulnerability Scoring System)
Bewertungsschema von `0.0` bis `10.0` basierend auf Metriken:
* **Base Metrics:** Angriffsvektor (Network/Local), Komplexität, erforderliche Rechte, Nutzerinteraktion, Auswirkung auf CIA.
* **Scores:** 0.0–3.9 (Low), 4.0–6.9 (Medium), 7.0–8.9 (High), 9.0–10.0 (Critical).

### Sicherer Update- & Patch-Rollout-Prozess
```text
[ Security Advisory ] ---> [ Test in Staging-Umgebung ] ---> [ Freigabe Pipeline ] ---> [ Blue-Green Deployment / Rollback-Plan ]
```

---

## 4. Incident-Response-Prozess & 72h-DSGVO-Meldepflicht

### Die 6 Phasen nach NIST SP 800-61
1. **Vorbereitung (Preparation):** Erstellen von Reaktionsplänen, Tools und Kontaktlisten.
2. **Identifikation (Detection & Analysis):** Erkennen des Sicherheitsvorfalls über SIEM/Logs.
3. **Eindämmung (Containment):** Isolation betroffener Systeme vom Netz (VLAN trennen/Netzwerkkabel ziehen).
4. **Beseitigung (Eradication):** Entfernen der Schadsoftware/Ursache, Schließen der Lücke.
5. **Wiederherstellung (Recovery):** Geplantes Einspielen sauberer Backups und System-Re-Integration.
6. **Nachbereitung (Lessons Learned):** Dokumentation und Optimierung der Schutzmaßnahmen.

### Sofortmaßnahmen bei Ransomware
* System umgehend **vom Netzwerk trennen** (WLAN aus, Ethernet ziehen).
* System **nicht ausschalten** (Arbeitsspeicher/RAM für forensische Analysen erhalten, sofern möglich).
* Incident-Response-Team und Datenschutzbeauftragten informieren.

### DSGVO Art. 33 Meldepflicht
Im Falle einer Verletzung des Schutzes personenbezogener Daten mit Risiko für Betroffene muss die Meldung an die zuständige Datenschutz-Aufsichtsbehörde **unverzüglich, spätestens innerhalb von 72 Stunden** erfolgen.

---

## FIAE-Zusammenfassung
Entwickler verhindern OWASP-Schwachstellen durch Prepared Statements, prüfen Abhängigkeiten automatisiert auf CVE-Einträge und kennen ihren Part im Incident-Response-Plan.
