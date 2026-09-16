Guten Morgen! Hier ist der komplette Text als sauber formatierter Fließtext. Du kannst ihn direkt kopieren und in deine docker/README.md einfügen.

Docker
In diesem Bereich sammle ich Grundlagen und praktische Notizen zu Docker. Docker ist eine Plattform, mit der Anwendungen in Containern ausgeführt werden können. Ein Container enthält alles, was eine Anwendung zum Starten braucht: Programmdateien, Abhängigkeiten, Konfigurationen und eine passende Laufzeitumgebung. Für Fachinformatiker für Anwendungsentwicklung (FIAE) ist Docker wichtig, weil Container häufig für lokale Entwicklungsumgebungen, Microservices, Datenbank-Containerisierung, automatisierte Testumgebungen und einfache Deployments genutzt werden.

Ziel dieses Bereichs
Dieser Bereich erklärt Docker Schritt für Schritt und praxisnah. Es geht nicht nur darum, einzelne Docker-Befehle auswendig zu lernen. Wichtig ist zu verstehen, wie Images, Container, Volumes, Netzwerke und Docker Compose zusammenhängen.

Der Fokus liegt auf:

Docker-Grundlagen verstehen

Images und Container unterscheiden

Container starten, stoppen und löschen

Logs lesen und Fehler finden

Volumes für dauerhafte Daten nutzen

Docker-Netzwerke verstehen

Docker Compose verwenden

einfache Testumgebungen aufbauen

typische Fehler erkennen

Docker im FIAE-Alltag einordnen

Kapitelübersicht
Kapitel 1: Docker-Grundlagen

Kapitel 2: Images und Container

Kapitel 3: Volumes und Netzwerke

Kapitel 4: Docker Compose

Kapitel 5: Logs, Exec und Troubleshooting

Kapitel 6: Docker in der FIAE-Praxis

Was ist Docker?
Docker ist ein Werkzeug, um Anwendungen in Containern auszuführen. Ein Container ist eine isolierte Umgebung für eine Anwendung.

Beispiel: Eine Webanwendung braucht vielleicht einen Webserver, bestimmte Bibliotheken, eine bestimmte Laufzeitumgebung, Konfigurationsdateien, Netzwerkzugriff und eventuell eine Datenbank. Mit Docker kann diese Umgebung kontrollierter bereitgestellt werden. Dadurch läuft eine Anwendung auf verschiedenen Systemen oft gleich oder zumindest sehr ähnlich.

Warum Docker genutzt wird
Docker wird genutzt, weil es viele typische IT-Probleme vereinfacht.

Ohne Docker kann es passieren:

"Auf meinem Rechner funktioniert es."

"Auf dem anderen Rechner funktioniert es nicht."

Gründe können sein: andere Programmversionen, fehlende Abhängigkeiten, andere Betriebssystemumgebung, falsche Konfiguration, unterschiedliche Ports, fehlende Dienste oder unterschiedliche Datenbankversionen. Mit Docker beschreibt man die Umgebung genauer. Dadurch wird ein Projekt leichter startbar, testbar und dokumentierbar.

Wichtige Docker-Begriffe
Image: Vorlage für einen Container

Container: laufende oder gestoppte Instanz eines Images

Dockerfile: Bauanleitung für ein eigenes Image

Volume: dauerhafter Speicher für Containerdaten

Network: Netzwerk für Containerkommunikation

Port Mapping: Verbindung zwischen Host-Port und Container-Port

Docker Compose: Verwaltung mehrerer Container über eine YAML-Datei

Registry: Speicherort für Images, zum Beispiel Docker Hub

Kurz gesagt: Image = Vorlage | Container = gestartete Instanz | Volume = dauerhafte Daten | Network = Verbindung | Compose = mehrere Container gemeinsam verwalten.

Image und Container
Ein häufiger Anfängerfehler ist die Verwechslung von Image und Container.

Image: wie eine Installationsvorlage

Container: wie ein gestartetes Programm aus dieser Vorlage

Beispiel:

Bash
docker pull nginx
docker run -d --name web -p 8080:80 nginx
Dabei ist nginx das Image. Der Container web ist die laufende Instanz daraus. Ein Image kann für viele Container verwendet werden.

Docker im Vergleich zu virtuellen Maschinen
Docker-Container sind nicht dasselbe wie virtuelle Maschinen.

Betriebssystem: Container nutzen den Kernel des Hosts mit – Virtuelle Maschinen haben ein eigenes Gastbetriebssystem.

Startzeit: Container sind meist sehr schnell – Virtuelle Maschinen starten langsamer.

Ressourcenverbrauch: Container verbrauchen eher wenig Ressourcen – Virtuelle Maschinen benötigen deutlich mehr.

Isolation: Container bieten prozessbasierte Trennung – Virtuelle Maschinen sind stärker getrennt.

Nutzung: Container eignen sich für Apps, Dienste und Testumgebungen – Virtuelle Maschinen für komplette Systeme und Server.

Verwaltung: Container nutzen Images und Compose – Virtuelle Maschinen nutzen VM-Images und Hypervisor.

Container ersetzen virtuelle Maschinen nicht vollständig. Beide haben ihren Platz. Für viele Dienste und Testumgebungen ist Docker sehr praktisch. Für komplette Betriebssystem-Labs sind virtuelle Maschinen oft besser geeignet.

Typische Docker-Einsatzbereiche
Docker wird häufig genutzt für Webserver, Datenbanken, lokale Testumgebungen, Entwicklungsumgebungen, kleine Dienste, APIs, Admin-Tools, Monitoring-Tools, Schul- und Lernprojekte, Home-Lab-Setups, CI/CD-Pipelines und einfache Deployments.

Beispiele: nginx als Webserver, PostgreSQL als Datenbank, Adminer als Datenbank-GUI, Python-Apps als Container oder Testumgebungen mit Docker Compose.

Docker und Linux
Docker läuft sehr stark im Linux-Umfeld. Viele Docker-Grundlagen hängen mit Linux zusammen: Prozesse, Dateisystem, Rechte, Netzwerke, Ports, Logs, Benutzer, Dienste, Mounts und Ressourcen. Deshalb ist Linux-Wissen für Docker sehr hilfreich. Wer Linux-Grundlagen versteht, versteht Docker deutlich leichter.

Docker und Git
Docker-Projekte werden oft mit Git versioniert.

Typische Dateien in einem Docker-Projekt: Dockerfile, docker-compose.yml, README.md, .env.example, scripts/, configs/.

Nicht ins öffentliche Repository gehören meistens: .env, echte Passwörter, private Schlüssel, lokale Datenbankdaten, große Dumps und private Logs. Eine passende .gitignore ist deshalb wichtig.

Docker und Docker Compose
Ein einzelner Container kann mit docker run gestartet werden. Mehrere zusammengehörende Container verwaltet man oft mit Docker Compose (z. B. Webanwendung + Datenbank + Admin-Tool).

Mit Docker Compose beschreibt man diese Services in einer Datei: docker-compose.yml.

Dann kann man alles gemeinsam starten mit docker compose up -d und wieder stoppen mit docker compose down. Docker Compose ist besonders praktisch für kleine Labore und Lernprojekte.

Typische Docker-Befehle
docker ps – zeigt laufende Container

docker ps -a – zeigt alle Container

docker images – zeigt lokale Images

docker run – startet neuen Container

docker stop – stoppt Container

docker start – startet gestoppten Container

docker restart – startet Container neu

docker rm – löscht Container

docker rmi – löscht Image

docker logs – zeigt Container-Logs

docker exec -it – führt Befehl im Container aus

docker inspect – zeigt technische Details

docker compose up -d – startet Compose-Projekt

docker compose down – stoppt Compose-Projekt

Beispiel: einfacher nginx-Container
Ein einfacher Webserver kann so gestartet werden:

Bash
docker run -d --name web -p 8080:80 nginx
Bedeutung der Parameter: docker run startet den Container, -d lässt ihn im Hintergrund laufen, --name web vergibt den Namen, -p 8080:80 verbindet den Host-Port 8080 mit dem Container-Port 80, und nginx ist das verwendete Image.

Prüfen: docker ps, docker logs web, docker port web. Im Browser aufrufbar unter http://localhost:8080.

Stoppen und löschen: docker stop web und docker rm web.

Warum Volumes wichtig sind
Container selbst sind nicht als dauerhafter Speicher gedacht. Wenn ein Container gelöscht wird, können Daten im Container verloren gehen. Für dauerhafte Daten (wie Datenbankdaten, Uploads oder Konfigurationen) nutzt man Volumes.

Beispiel:

Bash
docker volume create db_data
docker volume ls
docker run -d --name db -v db_data:/var/lib/postgresql/data postgres
Warum Netzwerke wichtig sind
Container müssen oft miteinander kommunizieren (z. B. Web-App zu Datenbank oder Frontend zu Backend). Docker kann eigene Netzwerke erstellen: docker network ls, docker network create appnet und docker network inspect appnet. In Docker Compose bekommen Services oft automatisch ein gemeinsames Netzwerk und können sich über ihre Servicenamen erreichen.

Docker und Sicherheit
Docker ist praktisch, aber nicht automatisch sicher. Wichtige Punkte:

Keine echten Passwörter oder privaten Schlüssel ins Repository/Image kopieren

Images aus vertrauenswürdigen Quellen nutzen

Container nicht unnötig mit Root-Rechten betreiben

Nur benötigte Ports veröffentlichen und Volumes bewusst nutzen

Container regelmäßig aktualisieren und Logs prüfen

.env-Dateien nicht öffentlich committen

Docker erleichtert Betrieb und Tests, ersetzt aber keine Sicherheitsprüfung.

Typische Fehler beim Lernen
Image und Container verwechseln: falsche Befehle werden genutzt

Container löschen und Daten verlieren: Daten waren nicht in einem Volume

Port falsch mappen: Dienst ist nicht erreichbar

Logs nicht lesen: Ursache bleibt unbekannt

Containername falsch schreiben: Befehl wirkt nicht

docker compose down -v blind nutzen: Volumes werden gelöscht

.env committen: Zugangsdaten können veröffentlicht werden

Compose-Datei ändern, aber nicht neu starten: alte Konfiguration läuft weiter

Zu viele alte Container/Images behalten: System wird unübersichtlich

Docker als VM-Ersatz missverstehen: falsche Erwartungen entstehen

FIAE-Bezug
Für Fachinformatiker für Anwendungsentwicklung ist Docker ein unverzichtbares Werkzeug, um eigene Anwendungen isoliert zu packen und in konsistenten Laufzeitumgebungen bereitzustellen.

In der Praxis bedeutet das:

Lokale Entwicklungsumgebungen schnell und unabhängig vom Host-System aufbauen

Datenbanken (z. B. PostgreSQL, Redis) lokal ohne aufwendige Installation bereitstellen

Eigene Anwendungen über ein Dockerfile containerisieren

Multi-Container-Architekturen (z. B. Frontend, Backend, Datenbank) mit Docker Compose verwalten

Anwendungen isoliert testen und Identität zwischen Entwicklungs- und Produktionsumgebung sichern

Grundlagen für automatisierte CI/CD-Pipelines und moderne Cloud-Deployments schaffen

Docker verbindet die Softwareentwicklung mit modernen Operations-Praktiken (DevOps) und ermöglicht eine saubere Trennung von Anwendungslogik und Infrastruktur.

Kurze Zusammenfassung
Docker ist ein Werkzeug, um Anwendungen in Containern auszuführen. Ein Image ist die Vorlage. Ein Container ist die gestartete Instanz. Volumes speichern Daten dauerhaft. Netzwerke verbinden Container. Docker Compose verwaltet mehrere Container gemeinsam.

Wichtige Befehle sind docker ps, docker images, docker run, docker stop, docker rm, docker logs, docker exec, docker inspect, docker volume ls, docker network ls, docker compose up -d und docker compose down.

Für FIAE ist Docker wichtig, weil Container häufig für lokale Entwicklungsumgebungen, Datenbank-Integrationen, Anwendungs-Deployments, Testumgebungen und DevOps-Grundlagen genutzt werden.
