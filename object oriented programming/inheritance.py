# Inheritance: pewarisan

class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_int(Hero):
    pass


class Hero_str(Hero):
    pass


lina = Hero("lina", 100)
tecis = Hero_int("tecis", 100)
axe = Hero_int("axe", 100)
print(lina.name)
print(tecis.name)
print(axe.name)
