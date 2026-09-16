# 3. Volumes und Netzwerke

In diesem Kapitel geht es um Volumes und Netzwerke in Docker aus Sicht der Softwareentwicklung.

Container sind ephemeral (kurzlebig). Sie können jederzeit beendet, gelöscht und neu aus einem Image erstellt werden. Für Anwendungsentwickler wirft das zwei zentrale Fragen auf: Wo bleiben die Daten (z. B. der Datenbank-Inhalt) und wie kommuniziert mein Backend-Code mit der Datenbank oder dem Cache? Dafür sind Volumes und Docker-Netzwerke die wichtigsten Mechanismen.

Für Fachinformatiker für Anwendungsentwicklung ist dieses Thema essenziell, um lokale Entwicklungs-Umgebungen mit Live-Reloading aufzubauen, Entwicklungsdatenbanken persistent zu halten und Multi-Container-Architekturen sauber aufzubauen.

---

## Kurz erklärt

Volumes sichern Anwendungsdaten dauerhaft.
Docker-Netzwerke verbinden Container isoliert miteinander.

* **Volume:** Von Docker verwalteter dauerhafter Speicher auf dem Host
* **Bind Mount:** Verknüpfung eines lokalen Projektordners direkt in den Container (wichtig für Hot-Reloading)
* **tmpfs Mount:** Temporärer Speicher im Arbeitsspeicher (RAM)
* **Docker Network:** Virtuelles Netzwerk zur internen Kommunikation zwischen Containern
* **Bridge Network:** Standardnetzwerk für isolierte Container-Setups
* **Port Mapping:** Veröffentlichung eines Container-Ports an den Host (`-p 8080:80`)
* **Service DNS:** Erreichbarkeit von Containern im selben Netzwerk über ihren Namen (z. B. `DB_HOST=db`)

Kurz gesagt:

```text
Volume = Datenaufbewahrung (z. B. Postgres-Datenbank)
Bind Mount = Quellcode-Synchronisation im Entwickler-Alltag
Network = Interne Schnittstelle zwischen Backend, Frontend & DB
```

---

## Warum Volumes in der Softwareentwicklung wichtig sind

Ein Container besitzt ein flüchtiges Dateisystem. Wenn du eine Datei innerhalb des Containers erstellst oder in eine Datenbank schreibst, existieren diese Daten nur im Write-Layer des spezifischen Containers.

Wird der Container gelöscht (`docker rm`), sind alle Laufzeitdaten unwiederbringlich verloren.

Das ist kritisch bei:

* Lokalen Test-Datenbanken (PostgreSQL, MySQL, MongoDB)
* User-Uploads (z. B. Bild-Uploads in einer Web-App)
* Anwendungs-Logs und Cache-Verzeichnissen

Durch den Einsatz von Volumes wird der Lebenszyklus der Daten vom Lebenszyklus des Containers getrennt.

---

## Was ist ein Volume?

Ein Volume ist ein von Docker isolierter und verwalteter Speicherbereich auf dem Host-System.

Volume manuell erstellen:

```bash
docker volume create pg_data
```

Volumes auflisten:

```bash
docker volume ls
```

Details & Pfad auf dem Host anzeigen:

```bash
docker volume inspect pg_data
```

Volume löschen:

```bash
docker volume rm pg_data
```

---

## Named Volumes bei Datenbanken

Bei Entwicklungs-Datenbanken verwendet man bevorzugt Named Volumes.

PostgreSQL mit Named Volume starten:

```bash
docker run -d \
  --name dev-db \
  -e POSTGRES_PASSWORD=secret \
  -v pg_data:/var/lib/postgresql/data \
  postgres:16-alpine
```

Syntax-Aufbau:

* `-v pg_data:/var/lib/postgresql/data`
* `pg_data` = Name des Docker-Volumes
* `/var/lib/postgresql/data` = Pfad im Container, an dem PostgreSQL seine Daten ablegt

Selbst nach Ausführung von `docker rm -f dev-db` bleiben alle Tabellen und Datensätze im Volume `pg_data` gespeichert.

---

## Bind Mounts: Live-Reloading beim Entwickeln

Im Gegensatz zu Volumes wird bei einem Bind Mount ein lokaler Pfad deines Rechners (dein Quellcode) in den Container eingebunden.

Beispiel für Node.js oder Python mit Hot-Reloading:

```bash
docker run -d \
  --name my-api \
  -p 3000:3000 \
  -v "$(pwd)":/app \
  node:20-alpine
```

Vorteil für Anwendungsentwickler:

Sobald du in deiner IDE (z. B. VS Code) den Code speicherst, aktualisiert sich der Laufzeitcode im Container sofort, ohne dass ein langwieriges `docker build` ausgeführt werden muss.

---

## Volume vs. Bind Mount

* **Volume:** Ideal für Datenbanken und vom Container generierte Daten. Es wird komplett von Docker verwaltet.
* **Bind Mount:** Ideal für den eigenen Quellcode während der Entwicklung. Spiegelt lokale Dateien 1:1 in den Container.

Zusammenfassende Regel für Entwickler:

```text
Datenbanken & State  -> Named Volume
Eigenes Projekt-Repo -> Bind Mount
```

---

## Read-only Mounts (`:ro`)

Um versehentliches Überschreiben von Konfigurationsdateien durch die Anwendung zu verhindern, stellt man Mounts schreibgeschützt ein:

```bash
docker run -d \
  --name web \
  -v "$(pwd)/nginx.conf":/etc/nginx/nginx.conf:ro \
  nginx:alpine
```

Das Suffix `:ro` verhindert Schreibzugriffe aus dem Container heraus.

---

## Warnung vor `docker compose down -v`

Beim Arbeiten mit Docker Compose solltet ihr folgenden Unterschied kennen:

* `docker compose down`: Stoppt die Container und entfernt das erzeugte Netzwerk.
* `docker compose down -v`: Stoppt die Container UND löscht alle zugehörigen Volumes!

Wird `-v` verwendet, werden alle Testdaten eurer lokalen Datenbank unwiederbringlich gelöscht.

---

## Warum Netzwerke in der Entwicklung wichtig sind

Moderne Apps bestehen aus mehreren isolierten Diensten (z. B. Web-Frontend, REST-API, SQL-Datenbank, Redis-Cache).

Damit das Backend mit der Datenbank kommunizieren kann, müssen beide Container in ein gemeinsames virtuelles Docker-Netzwerk eingebunden sein.

Ohne eigenes Netzwerk können Container sich nicht gegenseitig über sprechende Namen finden.

---

## Eigenes Docker-Netzwerk erstellen & nutzen

Netzwerk erzeugen:

```bash
docker network create app-net
```

Netzwerke auflisten:

```bash
docker network ls
```

Container im Netzwerk starten:

```bash
docker run -d --name db-service --network app-net postgres:16-alpine
docker run -d --name backend-api --network app-net -p 5000:5000 my-api-image
```

---

## Service Discovery: Container-Kommunikation über Namen

Innerhalb eines benutzerdefinierten Docker-Netzwerks stellt Docker einen internen DNS-Server bereit.

Das bedeutet: Container können sich direkt über ihren **Containernamen** adressieren!

Im Backend-Code verbindest du dich mit der Datenbank über:

```text
Host: db-service
Port: 5432
```

Ein häufiger Entwicklerfehler ist die Angabe von `localhost` im Backend-Code. `localhost` verweist innerhalb des API-Containers auf den API-Container selbst – nicht auf den Datenbank-Container!

---

## Port Mapping vs. Interner Container-Port

* **Port Mapping (`-p 8080:80`):** Macht einen Container-Port für deinen lokalen Entwicklungs-Rechner (Host) erreichbar.
* **Internes Netzwerk:** Container im selben Docker-Netzwerk kommunizieren direkt über ihre internen Ports, ganz ohne `-p` Mapping nach außen.

Vorteil: Die Datenbank muss für maximale Sicherheit gar nicht an den Rechner-Port durchgereicht werden. Das Backend erreicht sie trotzdem über das interne Netzwerk.

---

## Docker Compose: Multi-Container Netzwerke & Volumes

Docker Compose erstellt beim Ausführen von `docker compose up` automatisch ein eigenes Projekt-Netzwerk, in dem alle Services unter ihrem **Servicenamen** erreichbar sind.

Beispiel für eine `docker-compose.yml`:

```yaml
services:
  backend:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=database
    volumes:
      - .:/app

  database:
    image: postgres:16-alpine
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

Das Backend erreicht die Datenbank hier direkt unter dem Hostnamen `database`.

---

## Netzwerke & Volumes analysieren

Detaillierte Netzwerkkonfiguration einsehen:

```bash
docker network inspect app-net
```

Prüfen, welche Mounts an einen Container angehängt sind:

```bash
docker inspect backend
```

Port-Belegungen prüfen:

```bash
docker port backend
```

---

## Typische Fehler bei Entwicklern

* **Localhost-Falle:** Versuchen, andere Container über `localhost` anzusprechen.
* **Port-Konflikt:** Ein lokaler Dienst belegt den Host-Port bereits (`port is already allocated`).
* **Vergessenes Volume:** Nach einem Container-Neustart fehlen alle Test-Datensätze.
* **Falscher Bind Mount Pfad:** Relativer Pfad stimmt nicht mit dem Arbeitsverzeichnis überein.

---

## FIAE-Bezug

Für Anwendungsentwickler sind Volumes und Netzwerke essenziell:

* **Hot-Reloading:** Ermöglicht verzögerungsfreie Code-Anpassungen via Bind Mounts.
* **Entwicklungs-Datenbanken:** Sichere Persistenz von Testdaten bei Neustarts via Volumes.
* **Microservices Architecture:** Saubere Entkopplung von Services über isolierte Netzwerke.

---

## Kurze Zusammenfassung

**Volumes** speichern Daten dauerhaft unabhängig vom Container-Status. **Bind Mounts** spiegeln lokalen Code in den Container. **Netzwerke** erlauben die Kommunikation von Containern untereinander über ihren Servicenamen.

Wichtige CLI-Befehle: `docker volume ls`, `docker volume create`, `docker network ls`, `docker network create` und `docker compose up -d`.
