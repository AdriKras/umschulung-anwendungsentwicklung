# 6. Docker in der FIAE-Praxis

In diesem Kapitel geht es darum, wie Docker im Alltag eines Fachinformatikers für Anwendungsentwicklung (FIAE) eingesetzt wird.

Docker ist in der modernen Softwareentwicklung längst Standard. Es bildet das Bindeglied zwischen Anwendungs-Code, lokalen Testumgebungen und automatisierter Deployment-Pipeline (DevOps). Wer eigene Software entwickelt, packt sie in Docker-Images, um konsistente Laufzeitumgebungen für Entwickler, Tester und Produktiv-Server sicherzustellen.

---

## Kurz erklärt

Docker vereinfacht den gesamten Software-Entwicklungs-Zyklus.

Typische FIAE-Einsatzbereiche:

* **Lokale Dev-Umgebungen:** Entwickler starten die komplexe Infrastruktur (DB, Redis, Message Queues) mit einem Befehl.
* **Application Packaging:** Die eigene App wird samt Runtime (Node, Python, Java) via `Dockerfile` verpackt.
* **Integrationstests:** Automatisierte Unit- und End-to-End-Tests laufen isoliert in Container-Instanzen.
* **CI/CD Pipelines:** GitHub Actions / GitLab CI bauen bei jedem Git-Push das Docker-Image und testen die Anwendung.
* **Cloud & Microservices:** Anwendungen werden in wiederverwendbare Microservices aufgeteilt und in Cloud-Cluster (z. B. Kubernetes oder Docker Swarm) deployed.

Technologie-Schnittstellen für Entwickler:

```text
Codebase (Python, JS, Java, C#)
  └── Dockerfile (App Packaging)
       └── docker-compose.yml (Local Multi-Container Dev)
            └── CI/CD-Pipeline (Automated Build & Test)
                 └── Cloud/Production Container Runtime
```

---

## Warum Docker für FIAE essenziell ist

Softwareentwickler arbeiten selten an isolierten Skripten. Moderne Systeme hängen von spezifischen Datenbank-Versionen, Caches, Queueing-Systemen und Frameworks ab.

Docker löst die typischen Probleme des Entwickler-Alltags:

* **"It works on my machine":** Durch identische Container-Laufzeiten verhält sich die Software auf dem Entwickler-Laptop exakt wie auf dem Staging- und Produktions-Server.
* **Schnelles Team-Onboarding:** Neue Entwickler müssen keine Datenbanken oder Caches lokal installieren – ein `git clone` und `docker compose up -d` genügen.
* **Isolierte Test-Umgebungen:** Testdatenbanken können in Sekunden hochgefahren, mit Test-Fixtures befüllt und nach den automatisierten Tests wieder verworfen werden.

---

## Der ideale FIAE-Entwicklungs-Workflow

Ein strukturierter Ablauf beim Entwickeln von containerisierter Software:

1. **Feature entwickeln:** Code lokal in der IDE schreiben (Bind Mount sorgt für Live-Reloading im Container).
2. **Lokal testen:** Integrations-Tests im Docker-Netzwerk ausführen.
3. **Image bauen:** `docker build -t app:latest .` auf dem Entwickler-Rechner testen.
4. **Git Push:** Code und `Dockerfile` in das Git-Repository committen.
5. **CI/CD Pipeline:** Die Pipeline baut das Image automatisiert, führt Tests aus und pusht das Image in eine Registry (z. B. Docker Hub, GitHub Packages).
6. **Deployment:** Das geprüfte Image wird auf dem Server als Container gestartet.

---

## Projektstruktur eines containerisierten Anwendungs-Repos

Ein professionelles Software-Repository im Anwendungsentwickler-Umfeld sollte folgende Grundstruktur aufweisen:

```text
my-app-repo/
├── src/                    # Quellcode der Applikation
├── tests/                  # Unittests & Integrationstests
├── .dockerignore           # Schließt node_modules, .git etc. vom Image-Build aus
├── .env.example            # Vorlage für Umgebungsvariablen (ohne Secrets!)
├── .gitignore              # Ignoriert .env, Build-Artefakte und lokale Logs
├── Dockerfile              # Bauanleitung für das Anwendungs-Image
├── docker-compose.yml      # Orchestrierung für die lokale Entwicklung
└── README.md               # Setup-Dokumentation für Entwickler
```

---

## Die `.dockerignore`-Datei (Wichtig für performante Builds!)

Ähnlich wie `.gitignore` verhindert `.dockerignore`, dass unnötige oder sensible Dateien beim `docker build` in den Build-Kontext übertragen werden.

Beispiel `.dockerignore`:

```gitignore
.git
.env
node_modules
__pycache__
dist
build
*.log
```

Vorteile:

* Beschleunigt die Image-Build-Zeiten extrem
* Verhindert das unbewusste Kopieren von Secrets oder lokalen Modulen ins Image
* Hält das finale Docker-Image schlank

---

## Docker-Projekte im GitHub-Portfolio

Für Bewerbungen und das berufliche Portfolio zeigen saubere Docker-Projekte deine Professionalität als Entwickler.

Ein gutes FIAE-Portfolio-Projekt auf GitHub sollte enthalten:

* **Ein funktionierendes `Dockerfile`:** Verwende Multi-Stage-Builds oder schlanke Base-Images (`alpine` / `slim`).
* **Eine `docker-compose.yml`:** Zeigt, dass du Applikation, Datenbank und Services miteinander verknüpfen kannst.
* **Saubere Trennung von Konfigurationsdaten:** Nutze `.env.example` und halte echte Zugangsdaten aus dem Repo fern.
* **Eine verständliche `README.md`:** Erkläre Schritt für Schritt, wie das Projekt lokal geklont und mit `docker compose up` gestartet wird.

---

## Sicherheits-Best-Practices für Entwickler

* **Keine Root-Rechte im Container:** Verwende im `Dockerfile` nach dem Setup einen Non-Root-User (`USER node` oder `USER appuser`).
* **Keine Passwörter im Code/Dockerfile:** Nutze Umgebungsvariablen (`ENV` / `.env`).
* **Schlanke Basis-Images:** Bevorzuge `python:3.12-slim` oder `node:20-alpine` vor fetten Full-OS-Images, um Sicherheitslücken (CVEs) zu reduzieren.
* **Verbindungssicherheit:** Datenbank-Ports in Compose-Setups nicht unnötig an den Host durchreichen, wenn sie nur intern gebraucht werden.
* **Fixierte Image-Tags:** Nutze `postgres:16.1-alpine` statt `postgres:latest`.

---

## Checkliste vor dem Push ins Repository

```text
 [ ] Sind alle Passwörter/API-Keys aus dem Code & Dockerfile entfernt?
 [ ] Existiert eine .env.example als Muster für das Team?
 [ ] Ist .env in der .gitignore eingetragen?
 [ ] Wurde eine .dockerignore angelegt?
 [ ] Funktioniert docker compose up -d auf einem frischen Setup?
 [ ] Ist die README.md mit Start- & Test-Befehlen aktualisiert?
```

---

## FIAE-Bezug

Für Fachinformatiker für Anwendungsentwicklung ist Docker das Schlüssel-Werkzeug für moderne Software-Entwicklungs-Prozesse:

* **End-to-End Verantwortung:** Vom Schreiben der ersten Codezeile bis zur containerisierten Bereitstellung.
* **DevOps-Grundlagen:** Verständnis für automatisierte Container-Builds, Registries und Cloud-Deployments.
* **Moderne Architekturen:** Befähigung zur Arbeit in verteilten Microservice-Umgebungen.

---

## Kurze Zusammenfassung

Docker verbindet Quellcode, Abhängigkeiten und Infrastruktur zu einem reproduzierbaren Paket. Für Anwendungsentwickler gehören `Dockerfile`, `docker-compose.yml`, `.dockerignore` und sauberes Environment-Handling zum täglichen Handwerkszeug.

Mit diesem Kapitel hast du die Grundlagen von Docker im FIAE-Umfeld vollständig erarbeitet!
