# 2. Images und Container

In diesem Kapitel geht es um Images und Container in Docker aus Sicht der Softwareentwicklung.

Images und Container sind die zentralen Bausteine von Docker. Ein Image ist die unveränderliche Vorlage (der Bauplan). Ein Container ist die gestartete Instanz dieser Vorlage. Ein tiefes Verständnis dieser beiden Konzepte verhindert typische Entwicklungsfehler und vereinfacht das Ausführen und Testen von eigenen Applikationen.

Für Fachinformatiker für Anwendungsentwicklung ist dieses Thema essenziell, um eigene Programme über ein `Dockerfile` in Images zu verpacken, lokale Test-Container zu steuern und Anwendungen sauber von Abhängigkeiten zu isolieren.

---

## Kurz erklärt

Ein Docker-Image ist die Vorlage (Bauplan).
Ein Docker-Container ist die laufende oder gestoppte Instanz eines Images.

* **Image:** Schreibgeschützte Vorlage mit Anwendungs-Code, Runtime und Abhängigkeiten
* **Container:** Ausführende Instanz des Images im Arbeitsspeicher
* **Tag:** Version oder Variante eines Images (z. B. `python:3.12-slim`)
* **Registry:** Speicherort für Images (z. B. Docker Hub, GitLab Registry)
* **Layer:** Einzelne schreibgeschützte Schichten, aus denen ein Image besteht
* **Container-ID:** Eindeutige Kennung einer aktiven oder beendeten Instanz
* **Containername:** Eindeutiger Name für einfache Referenzierung im Dev-Alltag

Analogie zur Objektorientierten Programmierung (OOP):

```text
Image = Klasse (Definition, Bauplan, unveränderlich)
Container = Objekt / Instanz (Laufzeitumgebung mit Zustand)
```

---

## Image und Container unterscheiden

Ein Image selbst führt keinen Code aus.
Ein Container führt die Anwendung aus oder befindet sich im beendeten Zustand.

Beispiel für eine Node.js-Umgebung:

```bash
docker pull node:20-alpine
docker run -d --name my-api node:20-alpine
```

Dabei passiert Folgendes:

* `docker pull node:20-alpine` lädt das Image vom Docker Hub herunter.
* `docker run ... node:20-alpine` erzeugt eine neue Container-Instanz und startet den Prozess.
* `--name my-api` gibt der Laufzeit-Instanz den sprechenden Namen `my-api`.

Aus einem einzigen Image können beliebig viele unabhängige Container instanziiert werden.

---

## Beispiel mit mehreren Containern aus einem Image

In verteilten Architekturen (z. B. Microservices oder Load-Balancing-Tests) startet man oft mehrere Instanzen desselben Images.

Beispiel:

```bash
docker run -d --name api-service-1 -p 8081:80 nginx:alpine
docker run -d --name api-service-2 -p 8082:80 nginx:alpine
```

Beide Container nutzen dasselbe Basis-Image (`nginx:alpine`), laufen aber völlig isoliert voneinander:

* `api-service-1` erreicht man über Port `8081`
* `api-service-2` erreicht man über Port `8082`

---

## Images anzeigen

Lokale Images auf dem Entwickler-Rechner auflisten:

```bash
docker images
```

oder:

```bash
docker image ls
```

Beispielausgabe:

```text
REPOSITORY    TAG          IMAGE ID       CREATED        SIZE
node          20-alpine    abc123def456   2 days ago     170MB
python        3.12-slim    ghi789jkl012   1 week ago     150MB
postgres      16-alpine    mno345pqr678   2 weeks ago    80MB
```

* **REPOSITORY:** Name des Basis-Images oder der eigenerstellten Anwendung.
* **TAG:** Versionsmarkierung.
* **SIZE:** Größe des Images auf dem Laufwerk.

---

## Images herunterladen

Ein Image lädt man gezielt mit `docker pull` aus einer Registry:

```bash
docker pull python:3.12-slim
docker pull postgres:16
```

Wird kein Tag angegeben, ergänzt Docker automatisch `:latest`.

---

## Image-Tags & Versionierung im Team

Tags definieren Versionen oder Architekturen eines Images:

* `python:3.12` (Vollständiges Image)
* `python:3.12-slim` (Ressourcenschonend, reduzierte Abhängigkeiten)
* `node:20-alpine` (Minimales Linux auf Alpine-Basis, ideal für Produktions-Builds)

Wichtig für Anwendungsentwickler:

Vermeide das Tag `latest` in produktiven Projekten oder im Entwicklerteam! Das Tag `latest` ist ein dynamischer Zeiger. Wenn ein Kollege das Image später zieht, erhält er evtl. neuere Breaking Changes.

Setze in Projekt-Konfigurationen immer feste Versionen ein (z. B. `postgres:16.1`), um konsistente Builds auf allen Entwickler-Laptops zu garantieren.

---

## Image-Details & Layers verstehen

Ein Image besteht aus mehreren schreibgeschützten Layern (Schichten). Jeder Befehl im `Dockerfile` erzeugt eine neue Schicht.

Inspect-Befehl für technische JSON-Details:

```bash
docker inspect python:3.12-slim
```

Befehlshistorie und Schichten des Images einsehen:

```bash
docker history python:3.12-slim
```

Das Verständnis der Layer hilft Entwicklern dabei, `Dockerfiles` so zu optimieren, dass der Build-Cache optimal ausgenutzt wird (z. B. `COPY requirements.txt` vor `COPY . .`).

---

## Local Images löschen

Nicht mehr benötigte Images von der Festplatte entfernen:

```bash
docker rmi node:20-alpine
```

Falls noch gestoppte Container auf diesem Image basieren, verweigert Docker das Löschen. Lösche in dem Fall zuerst die Container oder nutze `-f` (mit Vorsicht).

Ungenutzte Dangling-Images aufräumen:

```bash
docker image prune
```

---

## Container anzeigen & Status kontrollieren

Nur aktuell laufende Container anzeigen:

```bash
docker ps
```

Alle Container (inklusive beendeter, gecrashter oder gestoppter) anzeigen:

```bash
docker ps -a
```

* **STATUS:** Zeigt an, ob der Container `Up` (aktiv) oder `Exited` (beendet) ist.
* **PORTS:** Zeigt das entwickelte Port-Mapping (z. B. `0.0.0.0:8080->80/tcp`).

---

## Container erzeugen und ausführen mit `docker run`

Der Befehl `docker run` erstellt einen neuen Container aus einem Image und startet seinen Hauptprozess.

Container detached (im Hintergrund) mit Port-Freigabe starten:

```bash
docker run -d --name my-web-app -p 8080:80 nginx:alpine
```

Wichtige Flags für Entwickler:

* `-d`: Detached Mode (Terminal bleibt frei)
* `--name`: Setzt den sprechenden Instanznamen
* `-p 8080:80`: Leitet Traffic von localhost:8080 an den Container-Port 80
* `-e`: Setzt Umgebungsvariablen (z. B. `-e DB_HOST=postgres`)
* `-v`: Verbindet Ordner vom Host für Live-Reloading (`Bind Mount`)
* `--rm`: Löscht den Container automatisch beim Beenden

---

## `docker run` vs. `docker start`

Ein häufiger Missverständnis-Punkt bei Einsteigern:

* `docker run`: Erstellt eine **NEUE** Container-Instanz aus einem Image.
* `docker start`: Startet eine **BEREITS EXISTIERENDE**, gestoppte Instanz neu.

Wenn du nach einem `docker stop my-api` erneut `docker run --name my-api ...` ausführst, meldet Docker einen Namenskonflikt. Verwende stattdessen:

```bash
docker start my-api
```

---

## Container stoppen, neu starten & löschen

Container geordnet stoppen (sendet SIGTERM):

```bash
docker stop my-api
```

Container neu starten (z. B. nach Konfigurationsänderungen):

```bash
docker restart my-api
```

Gestoppten Container löschen:

```bash
docker rm my-api
```

Laufenden Container erzwingend stoppen und löschen:

```bash
docker rm -f my-api
```

Alle gestoppten Test-Container auf einmal aufräumen:

```bash
docker container prune
```

---

## Der Container-Lebenszyklus in der App-Entwicklung

Ein Container existiert nur so lange, wie sein Hauptprozess (PID 1) läuft.

Beispiel für Missverständnisse:

```bash
docker run ubuntu
```

Dieser Container wird sofort beendet (`Exited`), weil `ubuntu` standardmäßig nur eine Shell startet, die ohne interaktive Eingabe direkt terminiert.

Dienste wie Node.js-Server, Python-APIs oder Datenbanken bleiben dauerhaft aktiv, da ihr Hauptprozess auf Anfragen lauscht.

Interaktives Debugging in einem neuen Container:

```bash
docker run --rm -it python:3.12-slim python
```

Startet direkt die interaktive Python-REPL im Container und löscht ihn nach dem Beenden (`--rm`).

---

## Befehle im laufenden Container ausführen (`docker exec`)

Mit `docker exec` kannst du zusätzliche Befehle in einer bereits laufenden Instanz ausführen (z. B. für Datenbank-Migrations oder Debugging).

Einzelnen Befehl ausführen:

```bash
docker exec my-api python manage.py migrate
```

Interaktive Shell im Container öffnen:

```bash
docker exec -it my-api bash
```

(Falls im Minimal-Image `bash` fehlt, verwende `sh`).

---

## Container-Logs analysieren

Tritt in deinem Anwendungs-Code ein Fehler oder eine ungematchte Exception auf, sind die Logs die erste Anlaufstelle:

```bash
docker logs my-api            # Logs der Applikation ausgeben
docker logs -f my-api         # Live-Output verfolgen (Follow Mode)
docker logs --tail 50 my-api   # Nur die letzten 50 Zeilen anzeigen
```

---

## Umgebungsvariablen injizieren (`-e`)

Moderne Apps folgen der *12-Factor-App*-Methodik: Konfigurationen werden über Umgebungsvariablen von der Codebasis getrennt.

Beim Container-Start Parameter mitgeben:

```bash
docker run -d \
  --name dev-db \
  -e POSTGRES_USER=appuser \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=devdb \
  postgres:16-alpine
```

In deinem Anwendungscode greifst du darauf zu (z. B. `os.environ["POSTGRES_USER"]` in Python oder `process.env.POSTGRES_USER` in Node.js).

---

## Eigenes Image bauen (`docker build`)

Um deine eigene Applikation zu containerisieren, schreibst du ein `Dockerfile` und baust daraus ein Image.

Befehl zum Bauen:

```bash
docker build -t my-app:1.0 .
```

* `-t my-app:1.0`: Vergibt Namen und Tag
* `.`: Bestimmt das aktuelle Verzeichnis als Build-Kontext

Danach kannst du deine Anwendung wie jedes offizielle Image starten:

```bash
docker run -d --name running-app -p 3000:3000 my-app:1.0
```

---

## Typische Fehler in der Entwickler-Praxis

* **Datenverlust nach Stopp:** Datenbank-Dateien wurden nicht in ein Volume ausgelagert.
* **Hardcoded Localhost:** Code versucht im Container über `localhost` auf die DB zuzugreifen, statt den Namen des DB-Containers im Docker-Netzwerk zu nutzen.
* **Vergessenes Re-Building:** Code-Änderungen im Projekt werden ohne Bind Mount vorgenommen, aber das Image wurde nicht mit `docker build` neu gebaut.
* **Riesige Images:** Es wird kein schlankes Base-Image (wie `alpine` oder `slim`) genutzt, was CI/CD-Pipelines verlangsamt.

---

## FIAE-Bezug

Für Fachinformatiker für Anwendungsentwicklung ist der saubere Umgang mit Images und Containern die Grundlage moderner Softwareentwicklung:

* **Microservices bauen:** Große Systeme werden in kleine, über Docker gekoppelte Einheiten zerlegt.
* **Environment Parity:** Die Entwicklungsumgebung entspricht exakt der Produktion. Bugs durch unterschiedliche Node/Python-Versionen gehören der Vergangenheit an.
* **CI/CD Build Pipeline:** Automatisierte Tests bauen bei jedem Git-Push das Image neu und validieren die Funktionalität.

---

## Kurze Zusammenfassung

Ein **Image** ist die unbegrenzt wiederverwendbare, schreibgeschützte Vorlage. Ein **Container** ist die isolierte, laufende Instanz im Speicher.

Wichtige Befehle für Entwickler sind `docker build`, `docker run`, `docker ps`, `docker logs`, `docker exec`, `docker stop` und `docker rm`.
