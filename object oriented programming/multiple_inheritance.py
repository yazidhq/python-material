# class A:
#     def method_A(self):
#         print("ini adalah method A")


# class B:
#     def method_B(self):
#         print("ini adalah method B")


# # multiple inheritance
# class C(A, B):
#     pass


# objek = C()

# objek.method_A()
# objek.method_B()

# CONTOH
class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)


class TypeHero:
    def setType(self, type):
        self.type = type

    def showType(self):
        print(self.type)


class Hero(Team, TypeHero):
    def __init__(self, name, health):
        self.name = name
        self.health = health


# bloodseeker = Hero("Bloodseeker", 100)
# bloodseeker.setTeam("Dire")
# bloodseeker.setType("Core")

# bloodseeker.showTeam()
# bloodseeker.showType()


# # Method resolution order
# class A:
#     def show(self):
#         print("ini adalah method A")


# class B:
#     def show(self):
#         print("ini adalah method B")


# class C(B, A):
#     pass


# objek = C()
# objek.show()


# - Diamond Problem
class A:
    def show(self):
        print("ini adalah method A")


class B(A):
    def show(self):
        print("ini adalah method B")


class C(A):
    def show(self):
        print("ini adalah method C")


class D(B, C):
    pass


objek = D()
objek.show()
