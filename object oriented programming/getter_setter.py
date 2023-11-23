class Hero:

    def __init__(self, name, armor, health):
        self.__name = name
        self.__armor = armor
        self.__health = health
        # self.info = "name : {} \nhealth: {}".format(self.__name, self.__health)

    # merubah method menjadi seperti variable
    @property
    def info(self):
        return "name : {} \nhealth: {}".format(self.__name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None


drowranger = Hero("Drow Ranger", 60, 70)
print(drowranger.info)

print("\nGetter Setter __armor")
print(drowranger.armor)  # getter
drowranger.armor = 30  # setter
print(drowranger.armor)
del drowranger.armor  # deleter

print(drowranger.__dict__)
