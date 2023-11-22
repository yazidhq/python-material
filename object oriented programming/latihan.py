class Hero:

    def __init__(self, heroName, heroHealth, powerAttack, armorNumber):
        self.name = heroName
        self.health = heroHealth
        self.attack = powerAttack
        self.armor = armorNumber

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan):
        print(
            f"{self.name} diserang {lawan.name} dengan attack power sebesar {str(attack_lawan)}")
        attack_diterima = attack_lawan / self.armor
        print(f"serang masuk sebesar : {str(attack_diterima)}")
        self.health -= attack_diterima
        print(f'darah {self.name} tersisa {str(self.health)}')


invoker = Hero('invoker', 120, 70, 35)
lina = Hero('lina', 80, 150, 30)

invoker.serang(lina)
print("\n")
lina.serang(invoker)
