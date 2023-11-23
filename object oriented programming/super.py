class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(self.name, self.health))


class HeroInt(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, health=100)
        super().showInfo()


class HeroStr(Hero):
    def __init__(self, name):
        super().__init__(name, health=200)
        super().showInfo()


lina = HeroInt("lina")
axe = HeroStr("axe")
