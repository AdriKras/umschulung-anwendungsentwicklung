class Umschueler:
    def __init__(self, name, alter, kinder, country):
        self.name = name
        self.alter = alter
        self.kinder = kinder
        self.country = country


Ums1 = Umschueler("Adrian", 28, 0, "Deutschland")
Ums2 = Umschueler("Miri", 26, 1, "Serbien")
Ums3 = Umschueler("Bilgin", 25, 0, "Bulgarien")

print(f"In unserer Gruppe haben wir 2 Umschüler: {Ums1.name} und {Ums2.name}.")

print(f"{Ums1.name} ist {Ums1.alter} Jahre alt und kommt aus {Ums1.country}.")

print(f"{Ums2.name} ist {Ums2.alter} Jahre alt und kommt aus {Ums2.country}.")

print(f"{Ums3.name} ist {Ums3.alter} Jahre alt und kommt aus {Ums3.country}")
