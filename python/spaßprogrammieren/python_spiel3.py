import random
import time

# Ein Held wird mit Items stärker


class item:
    def __init__(self, name, item_typ, bonus_atk=0, bonus_leben=0, wert=0, level=1):
        self.name = name
        self.item_typ = item_typ
        self.bonus_atk = bonus_atk
        self.bonus_leben = bonus_leben
        self.wert = wert
        self.level = level


# Ich habe mir für mein nächstes Spiel überlegt, dass es ausreicht nur ein Held zu definieren und dieser Kämpft gegen alle
# Der Main Character gibt die Level vom Spiel vor.


class Hero:
    def __init__(self, name, atk, max_leben):
        self.name = name
        self.atk = atk
        self.max_leben = max_leben
        self.leben = max_leben
        self.gold = 0

        self.level = 1
        self.ep = 0
        self.ep_fuer_naechstes_level = 100

        # Inventar und Ausruestung

        self.inventar = []
        self.ausruestung = {"Waffe": None, "Rüstung": None}

    def atk(self):
        bonus = 0
        if self.ausruestung["Waffe"]:
            bonus += self.ausruestung["Waffe"].bonus_atk
        return self.basic_atk + bonus

    def max_leben(self):
        bonus = 0
        if self.ausruestung["Rüstung"]:
            bonus += self.ausruestung["Rüsung"].bonus_max_leben
        return self.basic_max_leben + bonus

    def ep_erhalten(self, menge):
        self.ep += menge

        while self.ep >= self.ep_fuer_naechstes_level:
            self.level_up()
        print(f"{self.name} ist ein Level aufgestiegen")

    def level_up(self):
        self.ep -= self.ep_fuer_naechstes_level
        self.level += 1
        self.ep_fuer_naechstes_level = int(self.ep_fuer_naechstes_level * 1.3)

        self.atk += 3
        self.max_leben += 15
        self.leben = self.max_leben

    def ist_lebendig(self):
        return self.leben > 0


# Gegen diese Monster wird der Held kämpfen müssen


class Monster:
    def __init__(
        self,
        name,
        basic_atk,
        basic_leben,
        basic_ep,
        basic_gold,
        main_hero_level,
        drop_chance=0.2,
    ):
        self.name = name
        self.level = main_hero_level

        # Wir bauen eine Skalierung ein, damit für das Levelsystem

        skalierung = 1 + (self.level - 1) * 0.3
        self.atk = int(basic_atk * skalierung)
        self.leben = int(basic_leben * skalierung)
        self.belohnung_gold = int(basic_gold * skalierung)
        self.belohnung_ep = int(basic_ep * skalierung)

        # Monster können auch items droppen

        self.drop_chance = drop_chance  # Haben wir oben auf 0,2 fest definiert
        drop_chance = 0.2

    def generierte_drops(self):
        # Item wird randomisiert
        if random.random() <= self.drop_chance:
            item_level = max(1, self.level - 1)  # Damit keine OP Items gedroppt werden

            moegliche_drops = [
                item(
                    "Abgenutztes Schwert",
                    "Waffe",
                    bonus_atk=2 * item_level,
                    wert=15 * item_level,
                    level=item_level,
                ),
                item(
                    "Einfaches Lederhemd",
                    "Rüstung",
                    bonus_leben=10 * item_level,
                    wert=10 * item_level,
                    level=item_level,
                ),
                item(
                    "Rostiger Dolch",
                    "Waffe",
                    bonus_atk=1 * item_level,
                    wert=8 * item_level,
                    level=item_level,
                ),
            ]

            return random.choice(moegliche_drops)

        return None  # Kein Drop

    def ist_lebendig(self):
        return self.leben > 0


# Jetzt werden die einzelnen Monster defiiniert.


class Goblin(Monster):
    def __init__(self, main_hero_level=1):
        super().__init__(
            name="Goblin",
            basic_atk=5,
            basic_leben=25,
            basic_gold=10,
            basic_ep=40,
            main_hero_level=main_hero_level,
            drop_chance=0.15,
        )


class Orc(Monster):
    def __init__(self, main_hero_level=1):
        super().__init__(
            name="ORCORC",
            basic_atk=10,
            basic_leben=45,
            basic_gold=25,
            basic_ep=80,
            main_hero_level=main_hero_level,
            drop_chance=0.2,
        )


# Jetzt haben wir ein Fundament und bauen daraus ein Spiel.
# Nur neu ist, dass die Monster auch Items droppen können


class Kampf:
    def __init__(self, helden_team, monster_gruppe):
        self.helden_team = helden_team
        self.monster_gruppe = monster_gruppe

    def austragen(self):
        print("n Kampf beginnt!")

        runde = 1
        main_hero = self.helden_team[0]

        while len(self.helden_team) > 0 and len(self.monster_gruppe) > 0:
            held = self.helden_team[0]
            monster = self.monster_gruppe[0]

            schaden_held = random.randint(1, held.atk)
            monster.leben -= schaden_held

            print(f"{held.name} trifft {monster.name} und fügt {schaden_held} zu")

            # Lebt das Monster noch?

            if not monster.ist_lebendig():
                print(f"{monster.name} wurde besiegt.")
                held.gold += monster.belohnung_gold
                main_hero.ep_erhalten(monster.belohnung_ep)
                # Itemdrop?
                gedropptes_item = monster.generierte_drops()
                if gedropptes_item:
                    held.inventar.append(gedropptes_item)
                    print(
                        f"{monster.name} hat ein Item fallen gelassen: {gedropptes_item.name}"
                    )
                    print("Das Item wurde dem Inventar hinzugefügt")
                else:
                    print(f"{monster.name} hat kein Item gedroppt")

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

        if not held.ist_lebendig():
            print(f"{held.name}... RIP")
            self.helden_team.pop(0)
        else:
            print(f"{held.name} hat noch {held.leben} hp")

        runde += 1
        time.sleep(1)

        print("Kampfende")
        return len(self.helden_team) > 0


# Testversuch
held = Hero("Adri", atk=10, max_leben=50)
helden_team = [held]

monster_welle = [Goblin(held.level), Orc(held.level), Goblin(held.level)]

kampf = Kampf(helden_team, monster_welle)
kampf.austragen()

print(f"\n Inventar von {held.name}:")
if len(held.inventar) == 0:
    print("Keine Inventare gesammelt")
else:
    for item in held.inventar:
        print(f"{item}")
# Das ist das allgemeine Spielsystem, wie ein Kampf aussieht
# Jetzt fügen wir ein Spiel ein. Mit Quests

# class Quest:
#   def __init__(self, ):
#      pass
