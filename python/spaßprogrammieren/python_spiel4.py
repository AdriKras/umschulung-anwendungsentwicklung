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

        # Questlog
        self.aktive_quests = []

        # Inventar und Ausruestung
        self.inventar = []
        self.ausruestung = {"Waffe": None, "Rüstung": None}

    # Funktionen umbenannt zu 'get_...', um Konflikte mit den Variablen zu vermeiden
    def get_atk(self):
        bonus = 0
        if self.ausruestung["Waffe"]:
            bonus += self.ausruestung["Waffe"].bonus_atk
        return self.atk + bonus

    def get_max_leben(self):
        bonus = 0
        if self.ausruestung["Rüstung"]:
            bonus += self.ausruestung["Rüstung"].bonus_leben
        return self.max_leben + bonus

    def ep_erhalten(self, menge):
        self.ep += menge
        while self.ep >= self.ep_fuer_naechstes_level:
            self.level_up()
        print(f"{self.name} hat nun {self.ep} EP.")

    def level_up(self):
        self.ep -= self.ep_fuer_naechstes_level
        self.level += 1
        self.ep_fuer_naechstes_level = int(self.ep_fuer_naechstes_level * 1.3)

        self.atk += 3
        self.max_leben += 15
        self.leben = self.max_leben
        print(f"LEVEL UP! {self.name} ist jetzt Level {self.level}!")

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

        # Wir bauen eine Skalierung ein für das Levelsystem
        skalierung = 1 + (self.level - 1) * 0.3
        self.atk = int(basic_atk * skalierung)
        self.leben = int(basic_leben * skalierung)
        self.belohnung_gold = int(basic_gold * skalierung)
        self.belohnung_ep = int(basic_ep * skalierung)

        # Monster können auch items droppen
        self.drop_chance = drop_chance

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


# Einzelne Monster
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


class Quest:
    def __init__(
        self,
        name,
        beschreibung,
        ziel_monster,
        ziel_anzahl,
        ep_belohnung,
        gold_belohnung,
    ):
        self.name = name
        self.beschreibung = beschreibung
        self.ziel_monster = ziel_monster
        self.ziel_anzahl = ziel_anzahl
        self.fortschritt = 0
        self.ep_belohnung = ep_belohnung
        self.gold_belohnung = gold_belohnung
        self.abgeschlossen = False

    def monster_besiegt(self, monster_name):
        if not self.abgeschlossen and monster_name == self.ziel_monster:
            self.fortschritt += 1
            print(
                f"Quest-Update [{self.name}]: {self.fortschritt}/{self.ziel_anzahl} {self.ziel_monster} besiegt."
            )

            if self.fortschritt >= self.ziel_anzahl:
                self.abgeschlossen = True
                print(
                    f"Du hast die Quest '{self.name}' erfüllt! Kehre ins Dorf zurück."
                )

    def quest_abgeben(self, held):
        if self.abgeschlossen:
            print(f"\nQuest '{self.name}' abgegeben!")
            held.gold += self.gold_belohnung
            held.ep_erhalten(self.ep_belohnung)
            print(f"Belohnung: {self.ep_belohnung} EP und {self.gold_belohnung} Gold.")
            return True
        return False


class Kampf:
    def __init__(self, helden_team, monster_gruppe):
        self.helden_team = helden_team
        self.monster_gruppe = monster_gruppe

    def austragen(self):
        print("\nEin Kampf beginnt!")
        runde = 1
        main_hero = self.helden_team[0]

        while len(self.helden_team) > 0 and len(self.monster_gruppe) > 0:
            held = self.helden_team[0]
            monster = self.monster_gruppe[0]

            schaden_held = random.randint(
                1, held.get_atk()
            )  # Nutzt jetzt die get_atk() Funktion
            monster.leben -= schaden_held

            print(
                f"{held.name} trifft {monster.name} und fügt {schaden_held} Schaden zu"
            )

            # Lebt das Monster noch?
            if not monster.ist_lebendig():
                print(f"{monster.name} wurde besiegt.")
                held.gold += monster.belohnung_gold

                # Quest Update
                for quest in main_hero.aktive_quests:
                    quest.monster_besiegt(monster.name)

                main_hero.ep_erhalten(monster.belohnung_ep)

                # Itemdrop?
                gedropptes_item = monster.generierte_drops()
                if gedropptes_item:
                    held.inventar.append(gedropptes_item)
                    print(
                        f"{monster.name} hat ein Item fallen gelassen: {gedropptes_item.name}"
                    )
                else:
                    print(f"{monster.name} hat kein Item gedroppt")

                print(f"{held.name} hat damit {monster.belohnung_gold} Gold verdient")

                self.monster_gruppe.pop(0)  # Nächstes Monster
                runde += 1
                time.sleep(1)
                continue

            print(f"{monster.name} hat noch {monster.leben} HP")

            # Monster greift an
            schaden_monster = random.randint(1, monster.atk)
            held.leben -= schaden_monster
            print(f"{monster.name} hat {schaden_monster} Schaden gemacht")

            # Lebt unser Held noch? (Jetzt korrekt eingerückt!)
            if not held.ist_lebendig():
                print(f"{held.name}... RIP")
                self.helden_team.pop(0)
            else:
                print(f"{held.name} hat noch {held.leben} HP")

            runde += 1
            time.sleep(1)

        print("Kampfende")
        return len(self.helden_team) > 0


def berechne_siegchance(held, ziel_monster_name, ziel_anzahl):
    # Wir erstellen ein unsichtbares "Dummy"-Monster auf dem Level des Helden,
    # um zu gucken, wie stark die Gegner sein werden.
    if ziel_monster_name == "Goblin":
        dummy = Goblin(held.level)
    else:
        dummy = Orc(held.level)

    helden_power = held.get_atk() * held.get_max_leben()
    monster_power = (dummy.atk * dummy.leben) * ziel_anzahl

    # Eine einfache Formel, die aus dem Kräfteverhältnis eine %-Chance berechnet
    chance = int((helden_power / (helden_power + monster_power)) * 130)
    # Wir stellen sicher, dass die Anzeige immer zwischen 1% und 100% liegt
    return min(100, max(1, chance))


def dorf_menue(held):
    print("\n" + "=" * 40)
    print(f"Willkommen im Dorf, {held.name}!")
    print("=" * 40)
    print("Das Schwarze Brett hat folgende Aufgaben:")

    # 3 Quests mit unterschiedlichen Schwierigkeitsgraden
    quests_am_brett = [
        Quest(
            "Leichte Säuberung",
            "Besiege 2 Goblins",
            "Goblin",
            2,
            ep_belohnung=60,
            gold_belohnung=20,
        ),
        Quest(
            "Goblin-Lager",
            "Besiege 4 Goblins",
            "Goblin",
            4,
            ep_belohnung=150,
            gold_belohnung=60,
        ),
        Quest(
            "Die Ork-Bedrohung",
            "Besiege 2 Orcs",
            "ORCORC",
            2,
            ep_belohnung=250,
            gold_belohnung=120,
        ),
    ]

    for i, quest in enumerate(quests_am_brett):
        siegchance = berechne_siegchance(held, quest.ziel_monster, quest.ziel_anzahl)
        print(
            f"\n[{i + 1}] {quest.name} (Ziel: {quest.ziel_anzahl}x {quest.ziel_monster})"
        )
        print(f"    Belohnung: {quest.ep_belohnung} EP | {quest.gold_belohnung} Gold")
        print(f"    Erfolgschance: ~{siegchance}%")

    print("\n[0] Im Gasthaus ausruhen (Heilt alle HP)")

    wahl = input("\nWas möchtest du tun? (0, 1, 2, 3): ")

    if wahl in ["1", "2", "3"]:
        index = int(wahl) - 1
        angenommene_quest = quests_am_brett[index]
        held.aktive_quests.append(angenommene_quest)
        print(
            f"\nDu hast die Quest '{angenommene_quest.name}' angenommen! Auf in den Kampf!"
        )
        return angenommene_quest
    elif wahl == "0":
        held.leben = held.get_max_leben()
        print(
            f"\nDu schläfst eine Nacht im Gasthaus. Deine HP sind wieder voll! ({held.leben}/{held.get_max_leben()})"
        )
        time.sleep(1)
        return None
    else:
        print("\nUngültige Eingabe. Du schlenderst ziellos durchs Dorf.")
        return None


# --- SPIELSTART ---
held = Hero("Adri", atk=10, max_leben=50)

# Endlos-Schleife für das Spiel
while True:
    # 1. Menü aufrufen
    angenommene_quest = dorf_menue(held)

    # 2. Wenn eine Quest angenommen wurde, bauen wir die Gegner auf
    if angenommene_quest:
        monster_welle = []
        for _ in range(angenommene_quest.ziel_anzahl):
            if angenommene_quest.ziel_monster == "Goblin":
                monster_welle.append(Goblin(held.level))
            elif angenommene_quest.ziel_monster == "ORCORC":
                monster_welle.append(Orc(held.level))

        helden_team = [held]

        # 3. Kampf starten
        kampf = Kampf(helden_team, monster_welle)
        held_lebt = kampf.austragen()

        # 4. Prüfen ob wir gestorben sind
        if not held_lebt:
            print("\n" + "=" * 40)
            print("GAME OVER - Du bist im Kampf gefallen.")
            print("=" * 40)
            break

        # 5. Zurück im Dorf: Quests checken
        print("\n--- Zurück im Dorf ---")
        for quest in held.aktive_quests[:]:
            if quest.abgeschlossen:
                quest.quest_abgeben(held)
                held.aktive_quests.remove(quest)

    # Spielstatus nach jeder Aktion
    print(
        f"\nStatus: Level {held.level} | {held.leben}/{held.get_max_leben()} HP | {held.gold} Gold | {len(held.inventar)} Items im Rucksack"
    )
    time.sleep(2)
