import random
import time

# Umso größer das Spiel wird, desto unübersichtlicher werden die Gruppen, wenn die selben variablen für unterschiedliche Gruppen benutzt werden.
# Wir erstellen eine class Character


class character:
    def __init__(self, name, atk, leben):
        self.name = name
        self.atk = atk
        self.leben = leben


class Kampf:
    def __init__(self, helden_team, gegner_team):
        self.helden_team = helden_team
        self.gegner_team = gegner_team

    def austragen(self):
        held = self.helden_team[0]
        gegner = self.gegner_team[0]

        print(f"Der Kampf beginnt: {held.name} gegen {gegner.name}")

        # Beide starten mit 100 HP
        # self.held.leben = 100
        # self.gegner.leben = 100

        runde = 1

        # Schleife läuft, solange BEIDE noch Leben haben
        while len(self.helden_team) > 0 and len(self.gegner_team) > 0:
            #   held = self.helden_team[0]
            #   gegner = self.gegner_team[0]
            # Zufallsschaden berechnen
            schaden_held = random.randint(1, 10)
            schaden_gegner = random.randint(1, 8)

            # Held greift an
            gegner.leben -= schaden_held
            print(f"{held.name} greift an und macht {schaden_held} Schaden!")
            print(f"{gegner.name} hat noch {gegner.leben} HP.")

            # Prüfen, ob der Gegner schon besiegt ist
            if gegner.leben <= 0 or held.leben <= 0:
                break
            # Gegner greift an
            held.leben -= schaden_gegner
            print(f"{gegner.name} greift an und macht {schaden_gegner} Schaden!")
            print(f"{held.name} hat noch {held.leben} HP.")

            runde += 1
            time.sleep(1)
        # Gewinner verkünden
        print("KAMPFENDE")
        if held.leben > 0:
            print(f"{held.name} hat gewonnen! <3")
        else:
            print(f"{gegner.name} hat gewonnen! -.-")


# t1 = input()
t1 = character("adi", 10, 50)
t2 = character("CORE", 7, 50)
g1 = character("miri", 10, 50)
g2 = character("Koleidos", 3, 70)
helden_team = [t1, t2]
gegner_team = [g1, g2]

k = Kampf(helden_team, gegner_team)
# if t1 < 0 or g1 < 0:
#    try t1 : t2 or g1 : g2
k.austragen()
