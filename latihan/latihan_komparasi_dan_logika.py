# latihan logika dan komparasi

# membuat gabungan area rentang dari sebuah angka

# # +++++++3----------10++++++++++
# # mengecek kurang dari 3 atau lebih dari 10
# inputUser = float(input(
#     "Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10: "))

# # kurang dari 3
# # memerika angka kurang dari 3
# isKurangDari = (inputUser < 3)

# # lebih dari 10
# # memeriksa angka lebih dari 10
# isLebihDari = (inputUser > 10)

# # memeriksa kurang dari 3 atau lebih dari 10
# isHasil = isKurangDari or isLebihDari
# print(isHasil)

# ----3++++10----
# kasus irisan
# inputUser = float(input(
#     "Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10: "))
# isIrisan = (inputUser > 3 and inputUser < 10)
# print(isIrisan)

# # latihan mandiri
# 1. ---0+++5---8+++11---
# inputUser = float(input("Masukkan angka ---0+++5---8+++11---: "))
# isHasil = inputUser > 0 and inputUser < 5 or inputUser > 8 and inputUser < 11
# print(isHasil)

# 2. +++0---5+++8---11+++
inputUser = float(input("Masukkan angka +++0---5+++8---11+++: "))
isHasil = inputUser < 0 or inputUser > 5 and inputUser < 8 or inputUser > 11
print(isHasil)
