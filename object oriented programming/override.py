class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(
            self.name, self.health))


class HeroInt(Hero):
    def __init__(self, name):
        super().__init__(name, health=100)

    # override atau ditimpa
    def showInfo(self):
        print("{} dengan health: {} dan tipe: Intelligent".format(
            self.name, self.health))


class HeroStr(Hero):
    def __init__(self, name):
        super().__init__(name, health=200)

    # override atau ditimpa
    def showInfo(self):
        print("{} dengan health: {} dan tipe: Strength".format(
            self.name, self.health))


pugna = HeroInt("Pugna")
pugna.showInfo()
axe = HeroStr("Axe")
axe.showInfo()
