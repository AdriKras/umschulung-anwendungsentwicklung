# 4. Docker Compose

In diesem Kapitel geht es um Docker Compose aus Sicht der Softwareentwicklung.

Docker Compose ist ein Werkzeug, mit dem mehrere zusammengehörende Container gemeinsam definiert, gestartet, gestoppt und verwaltet werden können. Statt komplexe, unübersichtliche `docker run`-Befehle im Terminal auszuführen, beschreibt man die gesamte Anwendungsarchitektur deklarativ in einer YAML-Datei.

Für Fachinformatiker für Anwendungsentwicklung ist Docker Compose unverzichtbar, da moderne Software selten als Monolith isoliert läuft. Typische Entwicklungs-Setups bestehen aus einer Kombination von Frontend, Backend-API, Datenbank, In-Memory-Cache (Redis) und Admin-Tools.

---

## Kurz erklärt

Docker Compose orchestriert Multi-Container-Umgebungen über eine zentrale Konfigurationsdatei.

Standard-Dateiname:

```text
docker-compose.yml
```

oder die moderne Kurzform:

```text
compose.yml
```

Wichtigste Steuerungsbefehle:

* Entire Stack starten: `docker compose up -d`
* Entire Stack stoppen & aufräumen: `docker compose down`
* Anwendungs-Logs verfolgen: `docker compose logs -f`

Zentrale Bausteine einer `compose.yml`:

* **services:** Definiert die auszuführenden Container (z. B. `api`, `db`, `web`)
* **build:** Weist Compose an, das Image lokal via `Dockerfile` zu bauen
* **image:** Verwendet ein vorgefertigtes Registry-Image
* **ports:** Verbindet Host-Ports mit Container-Ports
* **volumes:** Verknüpft Persistenz-Volumes oder Bind Mounts für Live-Reloading
* **environment / env_file:** Injiziert Umgebungsvariablen für App-Konfigurationen
* **depends_on:** Steuert Startreihenfolgen und Bedingungen (Condition/Healthcheck)

---

## Warum Anwendungsentwickler Docker Compose nutzen

Ein lokales Entwicklungs-Setup ohne Compose erfordert viele manuelle Schritte:

```bash
docker network create app-net
docker run -d --name db --network app-net -v pg_data:/var/lib/postgresql/data postgres:16
docker run -d --name redis --network app-net redis:alpine
docker run -d --name api --network app-net -p 5000:5000 -v "$(pwd)":/app my-api
```

Probleme dabei: Schlechtes Onboarding für neue Entwickler, fehleranfällig und schwer zu versionieren.

Mit Docker Compose genügt ein einziger Befehl im Projekt-Root:

```bash
docker compose up -d
```

Vorteile für Entwickler-Teams:

* Exakte Dokumentation der Anwendungs-Infrastruktur im Git-Repository
* Identischer Tech-Stack für alle Teammitglieder (*Environment Parity*)
* Automatische Erstellung isolierter Netzwerke und Volumes
* Einfaches Einbinden von Quellcode zur Live-Entwicklung

---

## Aufbau einer Entwickler-Compose-Datei

Typisches Setup für ein Fullstack-Projekt (Frontend, Backend, DB):

```yaml
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - DB_HOST=database
      - DB_USER=appuser
      - DB_PASSWORD=secret
    depends_on:
      database:
        condition: service_healthy

  database:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=appuser
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=devdb
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser -d devdb"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  db_data:
```

---

## `image` vs. `build`

In Compose kannst du zwei Wege nutzen, um Container bereitzustellen:

1. **Offizielles Image ziehen (`image`):** Ideal für Standard-Infrastruktur wie Datenbanken oder Webserver.
   ```yaml
   db:
     image: postgres:16-alpine
   ```
2. **Eigenen Code bauen (`build`):** Weist Compose an, das lokale `Dockerfile` der eigenen Applikation zu kompilieren.
   ```yaml
   api:
     build: .
   ```

Wenn du Codeänderungen vorgenommen hast, baut folgender Befehl das Image neu und startet den Container:

```bash
docker compose up -d --build
```

---

## Steuerung von Umgebungsvariablen (`.env`)

Passwörter, API-Keys und Datenbank-Zugangsdaten dürfen **niemals** hart-codiert in der `compose.yml` im Git-Repo landen.

Nutze eine `.env`-Datei im selben Verzeichnis:

Inhalt `.env` (wird in `.gitignore` ignoriert):

```env
DB_USER=devuser
DB_PASSWORD=supersecret
DB_NAME=production_copy
PORT=5000
```

Einbinden in der `docker-compose.yml`:

```yaml
services:
  backend:
    build: .
    ports:
      - "${PORT}:${PORT}"
    environment:
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
```

Tipp für das Git-Repo: Erstelle immer eine `.env.example`-Datei ohne echte Passwörter als Vorlage für dein Team.

---

## Service-Reihenfolge & Healthchecks (`depends_on`)

Ein häufiges Problem in verteilten Systemen: Die Backend-Applikation startet schneller als die Datenbank bereit ist zu antworten. Die Folge ist ein App-Crash (`Connection refused`).

Nur `depends_on: [db]` wartet lediglich auf das Erstellen des Containers – nicht auf die Betriebsbereitschaft des DB-Dienstes!

Lösung via Healthcheck:

```yaml
services:
  api:
    build: .
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 3s
      timeout: 3s
      retries: 5
```

Erst wenn der `healthcheck` der Datenbank erfolgreich ist, startet Compose das `api`-Backend.

---

## Wichtigste CLI-Befehle im Entwickler-Alltag

* **Stack im Hintergrund starten:**
  ```bash
  docker compose up -d
  ```
* **Container neu bauen und starten (nach Code- oder Dependency-Änderungen):**
  ```bash
  docker compose up -d --build
  ```
* **Status aller Services im Projekt prüfen:**
  ```bash
  docker compose ps
  ```
* **Logs aller Services streamen:**
  ```bash
  docker compose logs -f
```
* **Logs eines spezifischen Services einsehen:**
  ```bash
  docker compose logs -f backend
  ```
* **Befehl im laufenden Service ausführen (z. B. DB-Migrations oder Tests):**
  ```bash
  docker compose exec backend python manage.py test
  ```
* **Stack stoppen und Netzwerke entfernen:**
  ```bash
  docker compose down
  ```
* **Achtung! Stack stoppen UND Daten-Volumes löschen:**
  ```bash
  docker compose down -v
  ```

---

## Konfiguration auf Syntaxfehler prüfen

YAML reagiert extrem empfindlich auf falsche Einrückungen (Tabs statt Leerzeichen).

Vor dem Committen oder Starten kannst du die Konfiguration validieren:

```bash
docker compose config
```

Dieser Befehl prüft die YAML-Syntax und gibt die vollständig aufgelöste Konfiguration inklusive aller Umgebungsvariablen aus.

---

## Typische Fehler bei Entwicklern

* **Falsche Einrückung:** Tabs statt Leerzeichen in der YAML-Datei genutzt.
* **Localhost-Missverständnis:** Im Backend-Code `DB_HOST=localhost` statt `DB_HOST=database` (Servicename) eingetragen.
* **Unbeabsichtigter Datenverlust:** Aus Versehen `docker compose down -v` ausgeführt und lokale Entwicklungs-Datenbank gelöscht.
* **Fehlender Rebuild:** `docker-compose.yml` oder `Dockerfile` angepasst, aber `docker compose up -d` ohne den Zusatz `--build` ausgeführt.
* **Missing `.env` File:** Vergessen, die `.env`-Datei aus der `.env.example` zu kopieren.

---

## FIAE-Bezug

Für Anwendungsentwickler ist Docker Compose das Standard-Werkzeug zur Orchestrierung der lokalen Entwicklungsumgebung:

* **One-Click Setup:** Neue Entwickler im Team sind in wenigen Minuten startklar (*Clone Repo -> `docker compose up -d`*).
* **Microservices:** Komplexe Multi-Service-Systeme lassen sich auf einem Laptop simulieren und testen.
* **Integrations-Tests:** Zusammenwirken von Frontend, Backend und Datenbank kann vor dem Git-Push lokal verifiziert werden.

---

## Kurze Zusammenfassung

Docker Compose fasst Multi-Container-Anwendungen in einer `compose.yml` zusammen. **Services** beschreiben die Container, **Volumes** sichern Daten, und **Networks** verbinden die Bausteine.

Zentrale Befehle: `docker compose up -d`, `docker compose down`, `docker compose logs -f` und `docker compose exec`.
