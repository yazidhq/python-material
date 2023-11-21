# Class dan Instance

class Hero:  # template
    # class variable
    jumlah = 0

    # dieksekusi saat object di inisialisasi
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        # bertamah setiap ada inisialiasasi object baru
        Hero.jumlah += 1


# inisialisasi object
hero1 = Hero("Sniper", 40, 100, 50)
print(hero1.jumlah)

hero1 = Hero("Sniper", 40, 100, 50)
print(hero1.jumlah)
