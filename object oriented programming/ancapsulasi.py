# Encapsulasi:
# - buat semua variable private
# - getter & setter untuk akses data yang dibutuhkan dari variable private

class Hero:

    # private
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    # getter dari private variable
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter untuk set private variable
    def setDiserang(self, attackPower):
        self.__health -= attackPower


# awal dari game
windRanger = Hero('windranger', 40, 120)

print(windRanger.__dict__)

# game berjalan
print(windRanger.getName())
print(windRanger.getHealth())
windRanger.setDiserang(5)
print(windRanger.getHealth())
