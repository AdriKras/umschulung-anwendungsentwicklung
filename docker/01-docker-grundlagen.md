# 1. Docker-Grundlagen

In diesem Kapitel geht es um die wichtigsten Grundlagen von Docker aus Sicht der Softwareentwicklung.

Docker ist eine Plattform, mit der Anwendungen in Containern ausgeführt werden können. Ein Container ist eine isolierte Umgebung, in der ein Dienst oder eine Anwendung läuft. Dadurch kann man Software einfacher entwickeln, testen, dokumentieren und auf verschiedenen Entwicklungs- und Produktionssystemen identisch ausführen.

Für Fachinformatiker für Anwendungsentwicklung ist Docker wichtig, weil Container in vielen Bereichen des Entwicklungsalltags vorkommen: Lokale Entwicklungsumgebungen, Datenbank-Integrationstests, Backend-APIs, Frontend-Builds, Microservices und automatisierte CI/CD-Deployments.

---

## Kurz erklärt

Docker hilft dabei, Anwendungen kontrolliert in Containern auszuführen.

Die wichtigsten Begriffe sind:

* **Image:** Vorlage für einen Container (enthält Code, Runtime, Bibliotheken)
* **Container:** laufende oder gestoppte Instanz eines Images
* **Dockerfile:** Bauanleitung für ein eigenes Anwendungs-Image
* **Volume:** dauerhafter Speicher für Anwendungs- und Datenbankdaten
* **Network:** Netzwerk für Containerkommunikation (z. B. Backend zu Datenbank)
* **Port Mapping:** Verbindung zwischen Host-Port und Container-Port
* **Docker Compose:** Verwaltung mehrerer Container (z. B. App + Datenbank + Cache) über eine YAML-Datei

Kurz gesagt:

```text
Image = Vorlage / Bauplan
Container = gestartete Instanz
Volume = dauerhafte Daten
Network = Verbindung zwischen Diensten
Compose = Multi-Container-Setup verwalten
```

---

## Warum Docker existiert

Ein typisches Problem in der Softwareentwicklung ist:

```text
Auf meinem Rechner funktioniert der Code, auf dem Server oder beim Kollegen nicht.
```

Das kann viele Gründe haben:

* unterschiedliche Betriebssysteme
* unterschiedliche Laufzeiten (z. B. Node-, Python- oder Java-Versionen)
* fehlende Abhängigkeiten oder Bibliotheken
* abweichende Konfigurationsdateien
* unterschiedliche Datenbankversionen
* andere Umgebungsvariablen

Docker löst dieses Problem: Die Anwendung läuft nicht unkontrolliert direkt auf dem Host-System, sondern in einer exakt definierten Container-Umgebung. Dadurch wird Software reproduzierbar, modular und unabhängig vom lokalen Rechner.

---

## Was ist ein Container?

Ein Container ist eine isolierte Umgebung für einen Prozess oder eine Anwendung.

Ein Container enthält zum Beispiel:

* Quellcode / kompilierte Anwendung
* benötigte Frameworks und Bibliotheken
* Konfigurationen
* Laufzeitumgebung (Runtime)
* Dateisystembereich
* Startbefehl

Ein Container ist keine vollständige virtuelle Maschine. Er nutzt den Kernel des Host-Systems mit. Das macht Container extrem schnell im Start und ressourcenschonend während der Entwicklung.

---

## Container im Entwickler-Alltag erklärt

Eine moderne Softwarearchitektur besteht selten aus nur einer Datei. Ein lokales Setup umfasst oft mehrere spezialisierte Container:

```text
Node.js / Python Backend-API
React / Vue Frontend-Webserver
PostgreSQL Datenbank
Redis In-Memory-Cache
Adminer Datenbank-GUI
```

Jeder Dienst läuft isoliert in einem eigenen Container:

```text
Container 1: Frontend
Container 2: Backend-API
Container 3: Datenbank
```

Über Docker-Netzwerke sprechen die Dienste miteinander, genau wie später auf dem Produktionsserver.

---

## Docker vs. Virtuelle Maschine

Docker-Container und virtuelle Maschinen werden oft verglichen.

* **Betriebssystem:** Container nutzen den Host-Kernel – VMs haben ein eigenes Gastbetriebssystem.
* **Startzeit:** Container starten in Sekunden – VMs brauchen oft Minuten.
* **Ressourcenverbrauch:** Container benötigen minimalen Arbeitsspeicher – VMs reservieren feste Ressourcen.
* **Isolation:** Container isolieren Prozesse – VMs isolieren komplette Hardware-Systeme.
* **Verwaltung:** Container werden via Dockerfile und docker-compose.yml versioniert – VMs via VM-Images und Hypervisor.
* **Nutzung:** Container dienen für Apps, APIs, Microservices und Test-Setups – VMs für komplette System-Infrastrukturen oder OS-Testing.

Für Softwareentwickler ist Docker das primäre Werkzeug zum Bauen und Ausführen von Applikationen.

---

## Host-System

Das Host-System ist der Rechner, auf dem Docker und deine Entwicklungsumgebung (IDE) laufen:

* Entwicklungs-Laptop (macOS, Windows mit WSL2, Linux)
* Dedicated Staging-Server
* CI/CD-Runner (z. B. GitHub Actions)

Container sind vom Host getrennt, nutzen aber dessen Ressourcen: CPU, RAM, Netzwerk und Speicherplatz.

Wichtige Befehle zur Kontrolle:

```bash
docker stats
df -h
free -h
docker system df
```

---

## Docker Engine

Die Docker Engine ist der zentrale Hintergrunddienst auf dem System. Sie verwaltet das Bauen von Images, das Starten von Containern, Netzwerke und Volumes.

Auf Linux-Entwicklungsrechnern steuert man den Dienst mit:

```bash
systemctl status docker
sudo systemctl start docker
```

---

## Docker Client und Docker Daemon

Docker arbeitet nach einer Client-Server-Architektur:

* **Docker Client:** Das Terminal-Tool (Befehl `docker`), mit dem du arbeitest.
* **Docker Daemon:** Der Hintergrunddienst (`dockerd`), der die eigentliche Arbeit erledigt.
* **Docker Engine:** Das Gesamtsystem aus Client, Daemon und API.

Wenn du `docker run` eingibst, schickt der Client eine Anfrage an den Daemon, welcher den Container startet.

---

## Docker-Version prüfen

```bash
docker --version
docker version
docker info
```

Diese Befehle zeigen dir die installierte Engine-Version, verfügbare Systemressourcen und die Anzahl aktiver Container.

---

## Image

Ein Image ist die unveränderliche (immutable) Vorlage für Container. Es wird entweder von öffentlichen Registries geladen oder über ein eigenes Dockerfile gebaut.

Beispiele für Entwickler-Images:

```text
python:3.12-slim
node:20-alpine
postgres:16
nginx:alpine
```

Image herunterladen:

```bash
docker pull node:20-alpine
```

Images auf dem Rechner anzeigen:

```bash
docker images
```

---

## Container

Ein Container ist die aktive, laufende Instanz eines Images.

Container im Hintergrund starten:

```bash
docker run -d --name my-app node:20-alpine
```

Container verwalten:

```bash
docker ps          # Laufende Container anzeigen
docker ps -a       # Alle Container (auch gestoppte) anzeigen
docker stop my-app # Container stoppen
docker start my-app# Gestoppten Container wieder starten
docker rm my-app   # Container löschen
```

---

## Image und Container unterscheiden

* **Image:** Der Bauplan / das Klasse-Konzept in OOP (unveränderlich, schreibgeschützt).
* **Container:** Das Objekt / die Instanz der Klasse zur Laufzeit.

```bash
docker pull nginx
docker run -d --name web1 nginx
docker run -d --name web2 nginx
```

`nginx` ist das Image. `web1` und `web2` sind zwei getrennte Container-Instanzen desselben Images.

---

## Docker Hub und Registries

Registries sind Speicherorte für Docker-Images. **Docker Hub** ist die größte öffentliche Plattform dafür.

Im Entwicklungsalltag nutzt man offizielle Images als Basis für eigene Applikationen. In Unternehmen werden oft private Registries (z. B. GitLab Container Registry, AWS ECR, Nexus) eingesetzt, um eigene Firmen-Software sicher zu speichern.

---

## Tags bei Images

Tags kennzeichnen Versionen eines Images:

```text
node:20
postgres:16.1
python:3.12-alpine
```

Wichtig für FIAE: Vermeide in Projekten das Tag `latest`. Nutze immer explizite Versionsnummern (z. B. `postgres:16`), um sicherzustellen, dass dein Setup bei allen Entwicklern im Team exakt gleich baut.

---

## Container starten mit docker run

Beispiel für den Start einer Web-Applikation:

```bash
docker run -d --name dev-api -p 5000:5000 my-python-api
```

Parameter erklärt:

* `docker run`: Erstellt und startet einen Container
* `-d`: Detached Mode (läuft im Hintergrund weiter)
* `--name dev-api`: Vergibt einen eindeutigen Namen
* `-p 5000:5000`: Verbindet Host-Port 5000 mit Container-Port 5000
* `my-python-api`: Das verwendete Image

---

## Port Mapping

Container sind isoliert und von außen primär nicht erreichbar. Um ein Web-API oder eine Datenbank auf deinem Entwicklungsrechner im Browser/Postman zu testen, muss der Port durchgereicht werden.

Syntax: `-p <Host-Port>:<Container-Port>`

```bash
docker run -d -p 8080:80 nginx
```

Die Anwendung im Container hört intern auf Port 80. Du erreichst sie auf deinem PC über `http://localhost:8080`.

---

## Logs

Wenn der Code im Container abstürzt oder Exceptions wirft, helfen die Container-Logs bei der Fehlersuche.

```bash
docker logs dev-api           # Einmalig Logs ausgeben
docker logs -f dev-api        # Logs live streamen (Follow-Mode)
docker logs --tail 100 dev-api# Die letzten 100 Zeilen anzeigen
```

---

## In Container hinein gehen

Um im Container zu debuggen, Konfigurationsdateien zu prüfen oder Testbefehle auszuführen:

```bash
docker exec -it dev-api bash
```

(Falls `bash` im Image nicht existiert, nutze `sh`).

---

## Container-Dateisystem & Datenhaltung

Dateien, die während der Laufzeit im Container erstellt werden, liegen im flüchtigen Layer des Containers. Wenn der Container gelöscht wird, sind diese Daten weg.

Für die Entwicklung braucht man zwei Konzepte zur Datenhaltung:

1. **Volumes:** Für persistente Daten (z. B. Daten einer lokalen Test-Datenbank).
2. **Bind Mounts:** Für Live-Reloading beim Programmieren (Code-Änderungen auf dem Host wirken sofort im Container).

---

## Volumes

Volumes werden von Docker verwaltet und dienen der dauerhaften Speicherung von Daten unabhängig vom Container-Lebenszyklus.

Volume erstellen & nutzen:

```bash
docker volume create pg-data
docker run -d --name db -v pg-data:/var/lib/postgresql/data postgres:16
```

Selbst wenn der Container `db` gelöscht wird, bleiben die Datenbank-Einträge im Volume `pg-data` erhalten.

---

## Bind Mounts (Wichtig für Entwicklung!)

Bei einem Bind Mount wird ein lokaler Quellcode-Ordner in den Container gespiegelt.

```bash
docker run -d --name my-app -p 3000:3000 -v "$(pwd)":/app node:20
```

Vorteil: Wenn du in deiner IDE eine Zeile Code änderst, sieht der Container diese Änderung sofort (Hot-Reloading), ohne dass du das Image neu bauen musst.

---

## Docker-Netzwerke

Damit deine Anwendung mit der Datenbank kommunizieren kann, müssen beide Container im selben Docker-Netzwerk liegen.

Netzwerk erstellen & nutzen:

```bash
docker network create app-net
docker run -d --name db --network app-net postgres:16
docker run -d --name api --network app-net my-api
```

Im selben Netzwerk können Container direkt über ihren **Containernamen** als Hostnamen kommunizieren (z. B. `DB_HOST=db`).

---

## Docker Compose

Docker Compose ist das wichtigste Werkzeug für Anwendungsentwickler, um Multi-Container-Umgebungen mit einem einzigen Befehl zu starten.

Die Konfiguration erfolgt in einer `docker-compose.yml`.

Projekt starten:

```bash
docker compose up -d
```

Projekt beenden:

```bash
docker compose down
```

Logs des gesamten Stacks ansehen:

```bash
docker compose logs -f
```

---

## Dockerfile

Das `Dockerfile` ist die automatisierte Bauanleitung für das eigene Anwendungs-Image.

Beispiel für ein Python-API:

```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Image bauen:

```bash
docker build -t my-python-api:1.0 .
```

---

## Docker und YAML

Docker Compose nutzt das YAML-Format.

Wichtige Syntax-Regeln:

* Keine Tabs verwenden – immer Leerzeichen zur Einrückung nutzen!
* Schreibweise ist Case-Sensitive.
* Fehlerhafte Einrückungen führen zum Abbruch beim Starten.

Syntax der Datei prüfen:

```bash
docker compose config
```

---

## Container-Lebenszyklus

Ein Container durchläuft verschiedene Zustände:

* `created`: Container ist angelegt, läuft aber nicht.
* `running`: Der Prozess läuft aktiv.
* `exited`: Der Prozess wurde beendet.
* `restarting`: Container wird nach einem Absturz neu gestartet.

Status prüfen:

```bash
docker ps -a
```

---

## Docker inspect

Liefert detaillierte JSON-Informationen über Container, Netzwerke oder Volumes:

```bash
docker inspect dev-api
```

---

## Aufräumen (Housekeeping)

Beim Entwickeln sammeln sich schnell alte Images und gestoppte Container an.

Ressourcen prüfen:

```bash
docker system df
```

Ungenutzte Container, Netzwerke und unbenannte Images löschen:

```bash
docker system prune
```

---

## Docker und Sicherheit in der Softwareentwicklung

Als FIAE musst du bei der Containerisierung von Anwendungen Sicherheitsaspekte beachten:

* **Keine Secrets im Code/Dockerfile:** Passwörter und Tokens gehören in `.env`-Dateien.
* **Non-Root User:** Anwendungen im Container nach Möglichkeit nicht als `root` ausführen.
* **Minimal Images:** Nutze schlanke Basis-Images (z. B. `alpine` oder `slim`).
* **Scan auf Schwachstellen:** Scanne eigene Images auf Sicherheitslücken.

---

## Docker in Git-Projekten

Ein sauberes Software-Repository enthält alle Dateien, um die Anwendung sofort per Docker zu starten.

Struktur eines Entwicklungs-Repositories:

```text
├── src/
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

Was gehört in die `.gitignore`?

```gitignore
.env
*.log
node_modules/
dist/
__pycache__/
```

---

## Typische Fehler am Anfang

* **Hardcoded Credentials:** Zugangsdaten fest im Image verankert.
* **Fehlendes Volume bei Datenbanken:** Nach dem Container-Stopp sind alle Testdaten gelöscht.
* **Port-Konflikte:** Der lokale Host-Port ist bereits durch einen anderen Dienst belegt.
* **Build-Kontext zu groß:** Große Ordner werden unbewusst beim `docker build` mitgeschickt.
* **Code-Änderung greift nicht:** Vergessen, das Image nach Code-Anpassungen neu zu bauen.

---

## FIAE-Bezug

Für Fachinformatiker für Anwendungsentwicklung ist Docker ein zentraler Baustein moderner Softwarearchitektur:

* **Konsistente Dev-Umgebungen:** Das gesamte Entwicklerteam arbeitet auf exakt identischen Software-Stacks.
* **Fast Onboarding:** Neue Entwickler müssen nur Git clonen und `docker compose up` ausführen.
* **Microservices:** Verschiedene Komponenten einer Anwendung können isoliert entwickelt werden.
* **CI/CD Integration:** Das definierte Image wird in der Build-Pipeline automatisch getestet und deployed.

---

## Kurze Zusammenfassung

Docker kapselt Anwendungen und deren Abhängigkeiten in leichtgewichtigen Containern. Ein **Image** ist der Bauplan, ein **Container** die ausführende Instanz. **Volumes** sichern Daten dauerhaft, **Netzwerke** verbinden Services, und **Docker Compose** steuert das Gesamtsystem aus mehreren Containern.

Die wichtigsten CLI-Befehle für Entwickler sind `docker build`, `docker run`, `docker ps`, `docker logs`, `docker exec` sowie `docker compose up -d` und `docker compose down`.
