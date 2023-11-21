# Constructor init

class Hero:  # template
    # dieksekusi saat object di inisialisasi
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


# inisialisasi object
hero1 = Hero("Sniper", 40, 100, 50)

print(hero1.__dict__)
