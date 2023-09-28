# operasi komparasi
# setiap hasil dari komparasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari (>)
print("====LEBIH BESAR DARI (>)====")
hasil = a > 3
print(hasil)
hasil = b > 4
print(hasil)

# kurang dari (<)
print("====KURANG DARI (>)====")
hasil = a < 3
print(hasil)
hasil = b < 3
print(hasil)

# lebih besar dari sama dengan (>=)
print("====LEBIH BESAR DARI SAMA DENGAN (>=)====")
hasil = a >= 5
print(hasil)
hasil = b >= 2
print(hasil)


# kurang dari sama dengan (<=)
print("====KURANG DARI SAMA DENGAN (>=)====")
hasil = a <= 4
print(hasil)
hasil = b <= 2
print(hasil)

# sama dengan (==)
print("====SAMA DENGAN (==)====")
hasil = a == 4
print(hasil)
hasil = b == 4
print(hasil)

# tidak sama dengan (!=)
print("====TIDAK SAMA DENGAN (!=)====")
hasil = a != 4
print(hasil)
hasil = b != 4
print(hasil)

# is
# membandingkan objek / memori
# sebagai komparasi object identity (id / hex)
# a is b
print("====OBJECT IDENTITY IS (is)====")
x = 5  # assignment membuat object
y = 4
print("nilai x = ", x, "| id = ", hex(id(x)))
print("nilai y = ", y, "| id = ", hex(id(y)))
print(x is y)
# tidak bisa x is 10 (angka)

# is not
print("====OBJECT IDENTITY IS NOT (is not)====")
x = 5
y = 4
print("nilai x = ", x, "| id = ", hex(id(x)))
print("nilai y = ", y, "| id = ", hex(id(y)))
print(x is not y)
