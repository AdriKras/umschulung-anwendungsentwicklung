# 05-06: LF 5.3 Entwicklungswerkzeuge & Versionsverwaltungssysteme (VCS)

Dieses Modul behandelt die Abgrenzung von Text-Editoren zu IDEs, Compilern und Interpretern sowie die Architektur-Unterschiede zwischen zentralen (SVN) und verteilten Versionsverwaltungssystemen (Git).

---

## 1. Entwicklungswerkzeuge: Editor vs. IDE

| Kriterium | Text-Editor / Code-Editor | Integrated Development Environment (IDE) |
| :--- | :--- | :--- |
| **Funktionsumfang** | Leichtgewichtig, Fokus auf reine Textbearbeitung (z. B. VS Code, Sublime Text, Vim). | Komplettsuite mit integrierten Tools (z. B. IntelliJ IDEA, Eclipse, Visual Studio). |
| **Features** | Syntax-Highlighting, grundlegendes Code-Completion (oft erst via Plugins). | Refactoring-Tools, integrierter Debugger, Profiler, GUI-Builder, Linter, Test-Runner. |
| **Performance** | Sehr geringer Speicherverbrauch, schneller Start. | Höherer Ressourcen- & Arbeitsspeicherverbrauch. |

---

## 2. Programmiersprachen-Ausführung: Compiler vs. Interpreter

| Kriterium | Kompilierte Sprachen (z. B. C, C++, Rust) | Interpretierte Sprachen (z. B. Python, JavaScript, PHP) |
| :--- | :--- | :--- |
| **Übersetzung** | Der Quellcode wird vor der Ausführung vollständig in Maschinencode (Binärdatei) übersetzt. | Der Quellcode wird zeilenweise zur Laufzeit durch einen Interpreter eingelesen und ausgeführt. |
| **Ausführungsgeschwindigkeit** | Sehr hoch (direkte Hardware-Ausführung). | Langsamer (Laufzeit-Overhead durch Interpreter). |
| **Plattformunabhängigkeit** | Geringer (Kompilat ist OS-/Architektur-spezifisch). | Hoch (Läuft auf jedem System mit passendem Interpreter). |
| **Fehlererkennung** | Syntax- und Typfehler werden bereits beim **Build/Compile** erkannt. | Syntax- und Laufzeitfehler treten erst **zur Laufzeit** auf. |

> **Hinweis (Bytecode / JIT):** Sprachen wie Java oder C# nutzen einen Hybrid-Ansatz: Quellcode wird in Bytecode kompiliert und von einer virtuellen Maschine (JVM / .NET CLR) via Just-In-Time (JIT) Compiler interpretiert/kompiliert.

---

## 3. Centralized vs. Distributed Version Control Systems (DVCS)

| Merkmal | Zentrales VCS (z. B. Subversion / SVN) | Verteiltes VCS / DVCS (z. B. Git, Mercurial) |
| :--- | :--- | :--- |
| **Architektur** | Ein zentraler Server hält die gesamte Historie. | **Jeder Client** besitzt eine vollständige Kopie des Repositories inkl. Historie. |
| **Offline-Arbeit** | Nicht möglich (Commits erfordern direkte Serververbindung). | Vollständig möglich (Commits, Branching und History-Logs erfolgen lokal). |
| **Single Point of Failure** | **Hoch:** Fällt der zentrale SVN-Server aus, kann niemand committen oder auf die Historie zugreifen. Ist der Server defekt, droht vollständiger Datenverlust. | **Gering:** Jeder Rechner im Team fungiert als Backup der gesamten Repository-Historie. |

---

## FIAE-Zusammenfassung
Entwickler wählen IDEs für komplexe Enterprise-Projekte wegen integrierter Debugging-Tools, verstehen Compiler- und Interpreter-Unterschiede für die Wahl des Technologiestacks und nutzen verteilte VCS (Git), um ausfallsicher und offline zu arbeiten.
