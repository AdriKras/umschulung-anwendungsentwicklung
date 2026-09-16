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
