class Hero:

    # private class vvariable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object (tidak untuk class)
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk object (berlaku untuk class)
    def getJumlahClass():
        return Hero.__jumlah

    # cara agar berlaku untuk object dan juga class (Method Static: decorator)
    @staticmethod
    def getJumlahStatic():
        return Hero.__jumlah

    # agar tidak perlu mengubah nama Class (object dan class bisa)
    @classmethod
    def getJumlahClassMethod(cls):
        return cls.__jumlah


sniper = Hero('sniper')
print(sniper.getJumlah())
print(Hero.getJumlahClass())

# static method
print(sniper.getJumlahStatic())
print(Hero.getJumlahStatic())

# class method
print(sniper.getJumlahClassMethod())
print(Hero.getJumlahClassMethod())
