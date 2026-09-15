# 05-09: LF 5.4 Python Objektorientierung (OOP) & Docker Containerisierung

Dieses Modul behandelt die Umsetzung von Klassen, Konstruktoren und Attributen in Python sowie den Vergleich von Virtuellen Maschinen mit Docker-Containern inklusive Dockerfile-Builds.

---

## 1. Objektorientierte Programmierung in Python

* **`__init__` (Konstruktor):** Wird bei der Instanziierung einer Klasse automatisch aufgerufen, um Attribute zu initialisieren.
* **`self`:** Referenz auf die aktuelle Instanz der Klasse (ermöglicht den Zugriff auf eigene Attribute und Methoden).

```python
class User:
    def __init__(self, username: str, email: str):
        self.username = username    # Instanz-Attribut
        self.email = email
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        print(f"User {self.username} wurde deaktiviert.")

# Instanziierung eines Objekts
user1 = User("adrian_dev", "adrian@dev.local")
user1.deactivate()
```

---

## 2. Docker Container vs. Traditionelle Virtuelle Maschinen (VMs)

| Kriterium | Virtuelle Maschine (VM) | Docker Container |
| :--- | :--- | :--- |
| **Virtualisierungsebene** | Hardware-Virtualisierung via Hypervisor (Typ 1/2). | Betriebssystem-Virtualisierung (Isolation auf Kernel-Ebene). |
| **Guest-Betriebssystem** | Enthält ein vollständiges eigenes Guest-OS (hoher Overhead). | **Kein eigenes Guest-OS** (teilt sich den Host-Kernel). |
| **Startzeit & Größe** | Minuten; mehrere Gigabyte groß. | **Sekunden; wenige Megabyte groß.** |
| **Ressourcenverbrauch** | Fest zugewiesene RAM-/CPU-Ressourcen. | Dynamischer Ressourcenverbrauch je nach Last. |

---

## 3. Docker-Praxis: Dockerfile, Image & Container

### Aufbau eines Dockerfiles
```dockerfile
# 1. Basis-Image festlegen
FROM python:3.11-slim

# 2. Arbeitsverzeichnis im Container definieren
WORKDIR /app

# 3. Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Quellcode in den Container kopieren
COPY . .

# 5. Startbefehl definieren
CMD ["python", "main.py"]
```

### Wichtige Docker CLI-Befehle
```bash
# Docker Image aus Dockerfile bauen
docker build -t my-python-app:1.0 .

# Container starten (Detached Mode & Port-Mapping 8080:8080)
docker run -d -p 8080:8080 --name app_instance my-python-app:1.0

# Aktive Container anzeigen & stoppen
docker ps
docker stop app_instance
```

---

## FIAE-Zusammenfassung
Entwickler strukturieren ihre Anwendungscode-Basis sauber in OOP-Klassen und packen das Ergebnis in schlanke Docker-Container, um identisches Laufzeitverhalten auf Dev-, Staging- und Produktionsservern zu garantieren.
