import json
import os
import random
import xml.etree.ElementTree as ET

# 1. Terminal direkt zu Beginn leeren
os.system("clear")

# Vorhandene Dateien suchen
datei = [f for f in os.listdir() if f.endswith((".json", ".xml"))]

geladene_datei = {}
wahl_datei = ""  # Vorab leer, um NameErrors zu verhindern

while True:
    try:
        spieler_anzahl = int(input("Wie viele Spieler spielen? "))
        if 1 <= spieler_anzahl <= 99:
            break  # Es wird eine gültige Anzahl angegeben, raus aus der while Schleife
        else:
            print("Zwischen 1 und 99")
    except ValueError:
        print("Bitte Zahlen eingeben ")

spieler_liste = []  # Liste für die aktuellen Spieler

for i in range(spieler_anzahl):
    while True:
        name_eingabe = input(f"Wie heißt Spieler {i + 1}? ")

        name_ist_gueltig = True

        if name_eingabe == "":
            name_ist_gueltig = False  # keine leeren Namen

        ungueltige_zeichen = (
            "0123456789!§$%&/()="  # Zeichen die im Namen nicht auftauchen dürfen
        )

        for zeichen in name_eingabe:
            if zeichen in ungueltige_zeichen:
                name_ist_gueltig = False

        if name_ist_gueltig == True:
            spieler_liste.append(name_eingabe)
            break
        else:
            print("Keine Sonderzeichen oder Zahlen erlaubt!")

# Spielstand laden, falls Dateien existieren
if datei:
    print("Gefundene Speicherdateien:", datei)
    wahl_datei = input("Welche Datei laden? (Enter für neu): ")
    if wahl_datei in datei:
        try:
            if wahl_datei.endswith(".json"):
                with open(wahl_datei, "r") as f:
                    geladene_datei = json.load(f)
            else:
                wahl_datei.endswith(".xml")
                tree = ET.parse(wahl_datei)
                root = tree.getroot()
                for eintrag in root.findall("Spieler"):
                    n = eintrag.get("name")
                    p_text = eintrag.find("Punkte").text
                    if n and p_text:
                        geladene_datei[n] = int(p_text)
            print(f"'{wahl_datei}' erfolgreich geladen.\n")
        except Exception as e:
            print(f"Fehler beim Laden: {e}")
            geladene_datei = {}

# Falls geladene Daten existieren, übernehmen wir sie. Ansonsten starten alle bei 0.
for spieler in spieler_liste:
    if spieler not in geladene_datei:
        geladene_datei[spieler] = 0

# Würfel-Bereich
print("\nLet's go!")

max_punkte = int(input("Bis wie vielen Gesamtpunkten soll das Spiel gehen? "))
# print(
#   "Wenn du das Spiel pausieren und die Runde abbrechen möchtest, dann drück j für json oder x für xml"

runde = 1  # p2.3.2 abgeändert
spiel_laeuft = True

# Das Spiel läuft so lange, bis spiel_laeuft auf False gesetzt wird
while spiel_laeuft:
    print(f"SPIELRUNDE {runde}")

    # Alle Spieler nacheinander kommen in dieser Runde dran
    for spieler in spieler_liste:
        print(
            f"\n {spieler} ist an der Reihe! (Aktuell: {geladene_datei[spieler]} Punkte)"
        )
        eingabe = input(
            "Drücke ENTER um zu würfeln "
        )  # .oder "j"um das Spiel zu unterbrechen").lower() # Nur noch Enter drücken oder j)

        # if input({j}):
        #    with open("savegame.json", "w") as f:
        #    json.dump(geladene_datei, f)
        #    break

        wuerfel = random.randint(1, 6)
        print(f" Du hast eine {wuerfel} gewürfelt!")

        # Punkte direkt dem aktuellen Spieler hinzurechnen
        geladene_datei[spieler] += wuerfel
        print(f"Neue Gesamtpunkte von {spieler}: {geladene_datei[spieler]}")

    #  RUNDENENDE: Jetzt prüfen wir fair, ob jemand gewonnen hat
    moegliche_gewinner = []

    for spieler in spieler_liste:
        if geladene_datei[spieler] >= max_punkte:
            moegliche_gewinner.append(spieler)
    #   else if input({j}):
    #      input("Drücke j um das Spiel zu unterbrechen und zu speichern").lower()
    #  with open("savegame.json", "w") as f:
    #      json.dump(geladene_datei, f)
    #  break
    # Wenn mindestens ein Spieler das Limit erreicht hat
    if len(moegliche_gewinner) == 1:
        # hoechste_punkte = -1
        gewinner_name = ""

        print(
            f"\n {gewinner_name} hat das Spiel mit {geladene_datei} Punkten gewonnen!"
        )
        spiel_laeuft = False  # Beendet die Hauptschleife
    else:
        runde += 1  # Keiner hat das Limit erreicht? Dann ab in die nächste Runde!

# Bubble-sort W2.3.3
n = len(spieler_liste)
for i in range(n - 1):
    for j in range(n - i - 1):
        if geladene_datei[spieler_liste[j]] < geladene_datei[spieler_liste[j + 1]]:
            spieler_liste[j], spieler_liste[j + 1] = (
                spieler_liste[j + 1],
                spieler_liste[j],
            )

# print("PUNKTE-ENDSTAND")
# print(f"{n}")

# print(spieler_liste)

# P2.3.5

for platz, spieler in enumerate(spieler_liste, start=1):
    print("platz   |  Spieler  | Punkte")
    print(f"{platz} |  {spieler:} | {geladene_datei[spieler]}")

# Rangliste nicht gut formatiert
# SPEICHERN:
wahl_datei = input("\n In welchem Format speichern? (json / xml): ").lower()


if wahl_datei == "x":
    root = ET.Element("Bestenliste")
    for spieler, punkte in geladene_datei.items():
        s_node = ET.SubElement(root, "Spieler", name=spieler)
        p_node = ET.SubElement(s_node, "Punkte")
        p_node.text = str(punkte)

    baum = ET.ElementTree(root)
    baum.write("savegame.xml", xml_declaration=True, encoding="utf-8")
    print("Erfolgreich als savegame.xml gespeichert!")
else:
    ("x für xml, sonst als json abgespeichert")
    with open("savegame.json", "w") as f:
        json.dump(geladene_datei, f, indent=4)
    print("Erfolgreich als savegame.json gespeichert!")
