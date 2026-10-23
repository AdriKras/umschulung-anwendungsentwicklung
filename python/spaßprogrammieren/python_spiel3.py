import random
import time

# Ich habe mir für mein nächstes Spiel überlegt, dass es ausreicht nur ein Held zu definieren und dieser Kämpft gegen alle


class Hero:
    def __init__(self, name, atk, max_leben):
        self.name = name
        self.atk = atk
        self.max_leben = max_leben
        self.leben = max_leben
        self.gold = 0

    def ist_lebendig(self):
        return self.leben > 0


# Gegen diese Monster wird der Held kämpfen müssen


class Monster:
    def __init__(self, name, atk, leben, belohnung_gold=10):
        self.name = name
        self.atk = atk
        self.leben = leben
        self.belohnung_gold = belohnung_gold

    def ist_lebendig(self):
        return self.leben > 0


# Jetzt werden die einzelnen Monster defiiniert.


class Goblin(Monster):
    super().__init__(name="Goblin", atk=5, leben=20, belohnung_gold=5)


class Orc(Monster):
    super().__init__(name="ORCORC", atk=10, leben=35, belohnung_gold=15)


class Drache(Monster):
    super().__init__(name="Weißer Drache", atk=20, leben=100, belohnung_gold=100)


# Kampf ist ähnlich aufgebaut wie in den anderen Spielen


class Kampf:
    def __init__(self, helden_team, monster_gruppe):
        self.helden_team = helden_team
        self.monster_gruppe = monster_gruppe

    def austragen(self):
        print("n Kampf beginnt!")

        runde = 1

        while len(self.helden_team) > 0 and len(self.monster_gruppe) > 0:
            held = self.helden_team[0]
            monster = self.monster_gruppe[0]

            schaden_held = random.randint(1, held.atk)
            monster.leben -= schaden_held

            print(f"{held} trifft {monster} und fügt {schaden_held} zu")

        # Lebt das Monster noch?

        if not monster.ist_lebendig():
            print(f"{monster.name} wurde besiegt.")
            held.gold += monster.belohnung_gold
            print(f"{held.name} hat damit {monster.belohnung_gold} verdient")
            self.monster_gruppe.pop(0)  # Nächstes Monster
            runde += 1
            time.sleep(1)
            continue

        print(f"{monster.name} hat noch {monster.leben} HP")

        # Monster greift an

        schaden_monster = random.randint(1, monster.atk)
        held.leben -= schaden_monster
        print(f"{monster.name} hat {schaden_monster} gemacht")

        # Lebt unser Held noch?

        if not Hero.ist_lebendig():
            print(f"{held.name}... RIP")

        runde += 1
        time.sleep(1)

    print("Kampfende")
    if len(self.helden_team) > 0:
        print("Wir haben gewonnen")
        return True
    else:
        print("RIP. wir sind trotzdem stolz auf unsere Helden!!")
        return False


# Das ist das allgemeine Spielsystem, wie ein Kampf aussieht
# Jetzt fügen wir ein Spiel ein. Mit Quests
