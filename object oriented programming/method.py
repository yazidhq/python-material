class Hero:
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # void function: method tanpa argumen dan return
    def sayHi(self):
        print(f"Namaku: {self.name}")

    # method dengan argument tanpa return
    def healthUp(self, up):
        self.health += up
        print(f"Darah {self.name}: {self.health}")

    # method dengan return
    def getHealth(self):
        return print(self.health)


hero1 = Hero('sniper', 100, 10, 5)
hero2 = Hero('axe', 200, 10, 50)
print(hero1.__dict__)
print(hero2.__dict__)

hero1.sayHi()
hero1.healthUp(10)
hero1.getHealth()
