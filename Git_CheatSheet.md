# Git & GitHub Cheat-Sheet (FIAE-Edition)

Ein kompakter Spickzettel für die tägliche Arbeit im Terminal mit Git, geordnet nach Workflow-Phasen.

---

## 1. Setup & Konfiguration

```bash
git config --global user.name "Dein Name"         # Globalen Benutzernamen setzen
git config --global user.email "deine@email.de"   # Globale E-Mail setzen
git config --list                                 # Alle Einstellungen anzeigen
```

---

## 2. Repositories erstellen & klonen

```bash
git init                                          # Neues lokales Git-Repo im Ordner erstellen
git clone <URL>                                   # Repository von GitHub lokal klonen
```

---

## 3. Die 3 Dateizustände & Commits (Der tägliche Loop)

```bash
git status                                        # Status der Dateien (Modified, Staged, Untracked) anzeigen
git add <dateiname>                               # Einzelne Datei für Staging vormerken
git add .                                         # Alle geänderten Dateien für Staging vormerken
git commit -m "Typ: Aussagekraeftige Nachricht"   # Snapshot im lokalen Repo speichern
git log --oneline                                 # Kompakte History aller Commits anzeigen
```

---

## 4. Branches (Zweige) & Merging

```bash
git branch                                        # Alle lokalen Branches anzeigen (* markiert aktiven)
git branch <branch-name>                          # Neuen Branch erstellen
git checkout <branch-name>                        # Zu einem anderen Branch wechseln
git switch -c <branch-name>                       # Neuer Branch erstellen UND direkt hinwechseln
git merge <branch-name>                           # Ziel-Branch in den aktuellen Branch mergen
git branch -d <branch-name>                       # Branch lokal loeschen
```

---

## 5. Remote Repositories & Synchronisation

```bash
git remote add origin <URL>                       # Remote Repository verknuepfen
git remote -v                                     # Verknuepfte Remote-URLs anzeigen
git push origin main                              # Lokale Commits auf GitHub hochladen
git pull origin main                              # Aenderungen von GitHub holen & mergen
git pull --rebase origin main                     # Sauberer Pull: setzt lokale Commits oben drauf
```

---

## 6. Notfall-Tipps & Rückgängig machen (Troubleshooting)

```bash
git restore <dateiname>                            # Aenderungen in einer Datei verwertfen (Working Dir)
git restore --staged <dateiname>                  # Datei aus Staging Area zurück ins Working Dir holen
git commit --amend -m "Neue Nachricht"            # Die Nachricht des letzten Commits korrigieren
git reset --soft HEAD~1                           # Letzten Commit aufheben, Aenderungen bleiben im Staging
```
