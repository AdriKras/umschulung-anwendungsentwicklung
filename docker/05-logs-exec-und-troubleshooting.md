# 5. Logs, Exec und Troubleshooting

In diesem Kapitel geht es um Logging, interaktive Shells (`exec`) und systematische Fehlersuche in Docker aus Sicht der Softwareentwicklung.

Da Container isolierte Hintergrundprozesse ausführen, sieht man Anwendungsfehler (z. B. Unhandled Exceptions, Crash-Loops oder fehlgeschlagene Datenbank-Verbindungen) nicht direkt auf dem Host-Bildschirm. Ein strukturierter Ansatz bei der Fehlersuche über CLI-Tools ist daher essenziell.

Für Fachinformatiker für Anwendungsentwicklung ist dieses Thema entscheidend, um eigenen Code im Container zu debuggen, Log-Streams zu analysieren, Umgebungsvariablen zur Laufzeit zu prüfen und Entwicklungsfehler rasch einzugrenzen.

---

## Kurz erklärt

Troubleshooting in der Entwicklung bedeutet:

* **Crash-Ursachen ermitteln:** Logs und Stack-Traces der Anwendung auslesen
* **Runtime-Zustand prüfen:** Mit `docker exec` interaktiv im Container debuggen
* **Netzwerk & Ports prüfen:** Verbindungen zwischen Backend und Datenbank validieren
* **Konfigurationen inspecten:** Geladene `.env`-Variablen und Mounts kontrollieren

Die wichtigsten Werkzeuge:

* `docker ps -a`: Status aller Container einsehen (z. B. `Exited (1)`)
* `docker logs -f <container>`: Applikations-Output live mitverfolgen
* `docker exec -it <container> sh`: Interaktive Shell im laufenden Container öffnen
* `docker inspect <container>`: Technische JSON-Details (Env-Vars, Mounts, Ports) auslesen
* `docker compose logs -f <service>`: Logs eines spezifischen Microservices ausgeben

---

## Anwendungs-Logs analysieren (`docker logs`)

Alles, was dein Anwendungscode auf `STDOUT` (Standard Output) oder `STDERR` (Standard Error) schreibt (z. B. `print()`, `console.log()` oder Logger-Frameworks), wird von Docker aufgefangen.

Logs einmalig ausgeben:

```bash
docker logs my-api
```

Logs live mitverfolgen (*Follow-Mode*, ideal beim lokalen Testen von Endpunkten):

```bash
docker logs -f my-api
```

Die letzten 50 Zeilen anzeigen:

```bash
docker logs --tail 50 my-api
```

Logs mit Zeitstempeln versehen:

```bash
docker logs -t my-api
```

---

## Logging bei Docker Compose

In Multi-Container-Umgebungen streamt Compose die Logs aller Services gleichzeitig in farblich getrennter Form:

```bash
docker compose logs -f
```

Gezielt nur die Logs der Datenbank oder des Backends anzeigen:

```bash
docker compose logs -f backend
```

---

## Warum Container sofort beendet werden (`Exited`)

Ein häufiges Problem beim Entwickeln eigener Images: Der Container startet, stoppt aber sofort wieder (`Exited (0)` oder `Exited (1)`).

Ursache:
Ein Container existiert nur so lange, wie sein Hauptprozess (PID 1) läuft. Wenn deine Anwendung abstürzt oder der Startbefehl ins Leere läuft, stoppt der Container.

Schritt-für-Schritt-Analyse:

1. Alle Container inklusive gestoppter anzeigen:
   ```bash
   docker ps -a
   ```
2. Logs des abgestürzten Containers lesen:
   ```bash
   docker logs <container_id>
   ```

Typische Gründe in der Softwareentwicklung:

* **Syntaxfehler / Missing Imports:** Der Code bricht beim Starten mit einer Exception ab.
* **Fehlende Dependency:** Ein Paket aus `requirements.txt` oder `package.json` wurde im `Dockerfile` nicht installiert.
* **Falscher CMD/ENTRYPOINT:** Der Startbefehl im `Dockerfile` ist fehlerhaft angegeben.
* **Missing Environment Variables:** Die App bricht ab, weil eine Pflicht-Variable (z. B. `DATABASE_URL`) fehlt.

---

## Interaktives Debugging mit `docker exec`

Mit `docker exec` führst du Befehle innerhalb einer laufenden Container-Instanz aus.

Interaktive Shell im Container öffnen:

```bash
docker exec -it my-api sh
```

(Falls das Image `bash` unterstützt, kann auch `bash` genutzt werden).

Nützliche Debug-Schritte im Container:

* Vorhandene Dateien & Pfade prüfen: `ls -la /app`
* Injizierte Umgebungsvariablen kontrollieren: `env`
* Netzwerkverbindung zur Datenbank testen: `ping database` oder `nc -zv database 5432`
* Manuelle Skript-Ausführung: `python manage.py check`

Container-Shell mit `exit` wieder verlassen.

---

## Umgebungsvariablen & Laufzeit-Konfiguration prüfen

Häufige Fehlerquelle: Die Applikation verbindet sich mit den falschen Zugangsdaten, weil Variablen aus der `.env`-Datei nicht richtig durchgereicht wurden.

Umgebungsvariablen im laufenden Container auslesen:

```bash
docker exec my-api env
```

Alternativ via `docker inspect` in den JSON-Metadata suchen:

```bash
docker inspect my-api
```

---

## System- & Ressourcen-Monitoring (`docker stats` & `top`)

Wenn deine Anwendung träge reagiert, unendlich viel Speicher verbraucht oder in eine Endlosschleife gerät:

Laufende Prozesse im Container anzeigen:

```bash
docker top my-api
```

Live-Ressourcenverbrauch (CPU, RAM, Network I/O) aller Container überwachen:

```bash
docker stats
```

---

## Port-Mapping & Erreichbarkeit kontrollieren

Wenn du deine API nicht im Browser oder in Postman unter `http://localhost:5000` erreichst:

1. Prüfen, ob der Port korrekt gemappt ist:
   ```bash
   docker port my-api
   ```
2. Prüfen, ob der Host-Port bereits von einem anderen lokalen Prozess belegt ist:
   ```bash
   ss -tulpen | grep 5000
   ```
3. Prüfen, ob deine App im Container an `0.0.0.0` gebunden ist und nicht an `127.0.0.1`!
   *(Apps, die intern nur an `127.0.0.1` lauschen, nehmen keine Anfragen von außerhalb des Containers entgegen).*

---

## Der Troubleshooting-Leitfaden für FIAE

Treten Probleme bei der Ausführung auf, gehe systematisch vor:

```text
[1] docker ps -a          ---> Läuft der Container oder ist er abgebrochen?
[2] docker logs <app>     ---> Welche Exception / Fehlermeldung wird ausgegeben?
[3] docker compose config ---> Stimmt die YAML-Syntax & sind Variablen gesetzt?
[4] docker exec -it ...   ---> Sind Dateien, Pfade & DB-Verbindungen im Container okay?
[5] docker compose up --build ---> Code/Dockerfile geändert? Neu bauen!
```

---

## Typische Fehler in der Entwickler-Praxis

* **Logs werden ignoriert:** Statt die Fehlermeldung zu lesen, wird auf Verdacht herumprobiert.
* **Blindes Re-Building:** Es wird stundenlang neu gebaut, obwohl nur eine Umgebungsvariable in der `.env` gefehlt hat.
* **`localhost` im Container-Code:** Verbindungen zu Datenbanken schlagen fehl, weil `localhost` statt des Container-Names genutzt wurde.
* **Passwörter im Log-Output:** Sensible Tokens oder Datenbank-Passwörter werden unbedacht per `print()` geloggt.
* **Hardcoded Port Bindings:** Anwendungs-Code lauscht auf `127.0.0.1` statt auf `0.0.0.0`.

---

## FIAE-Bezug

Für Anwendungsentwickler ist gezieltes Troubleshooting essenziell:

* **Effiziente Fehlersuche:** Schnelles Identifizieren von Syntaxfehler-, Runtime- & Datenbank-Issues.
* **Remote Debugging:** Verstehen, wie Prozesse in isolierten Umgebungen reagieren.
* **Logging Best Practices:** Sauberes Schreiben von Log-Ausgaben auf `STDOUT`/`STDERR`, um sie in Container-Plattformen oder Cloud-Monitoring-Tools (z. B. ELK Stack, Grafana Loki) auszuwerten.

---

## Kurze Zusammenfassung

Logging und Inspection sind die Grundpfeiler des Container-Debuggings. `docker logs` zeigt Anwendungs-Output, `docker exec` gewährt Zugriff auf die Laufzeitumgebung, und `docker inspect` offenbart technische Details.

Wichtigste Befehle: `docker ps -a`, `docker logs -f`, `docker exec -it <container> sh`, `docker inspect` und `docker compose config`.
