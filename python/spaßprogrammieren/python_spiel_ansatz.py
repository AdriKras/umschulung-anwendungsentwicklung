import random
import time


class gegner:
    def __init__(self, name, atk, leben):
        self.name = name
        self.Atake = atk
        self.leben = leben


class team:
    def __init__(self, name, atk, leben):
        self.name = name
        self.atk = atk
        self.leben = leben


class Kampf:
    def __init__(self, held, gegner):
        self.held = held
        self.gegner = gegner

    def austragen(self):
        print(f"Der Kampf beginnt: {self.held.name} gegen {self.gegner.name}")

        # Beide starten mit 100 HP
        self.held.leben = 100
        self.gegner.leben = 100

        runde = 1

        # Schleife läuft, solange BEIDE noch Leben haben
        while self.held.leben > 0 and self.gegner.leben > 0:
            print(f"Runde {runde}")

            # Zufallsschaden berechnen
            schaden_held = random.randint(1, 10)
            schaden_gegner = random.randint(1, 7)

            # Held greift an
            self.gegner.leben -= schaden_held
            print(f"{self.held.name} greift an und macht {schaden_held} Schaden!")
            print(f"{self.gegner.name} hat noch {self.gegner.leben} HP.")

            # Prüfen, ob der Gegner schon besiegt ist
            if self.gegner.leben <= 0:
                break

            # Gegner greift an
            self.held.leben -= schaden_gegner
            print(f"{self.gegner.name} greift an und macht {schaden_gegner} Schaden!")
            print(f"{self.held.name} hat noch {self.held.leben} HP.")

            runde += 1
            time.sleep(1)
        # Gewinner verkünden
        print("KAMPFENDE")
        if self.held.leben > 0:
            print(f"{self.held.name} hat gewonnen! <3")
        else:
            print(f"{self.gegner.name} hat gewonnen! -.-")


t1 = team("adi", 10, 50)
g1 = gegner("monster", 10, 50)

k = Kampf(t1, g1)
k.austragen()
