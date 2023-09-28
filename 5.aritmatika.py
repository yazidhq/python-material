# operasi aritmatika

a = 10
b = 3

# penjumlahan
print(a+b)

# pengurangan
print(a-b)

# perkalian
print(a*b)

# pembagian
print(a/b)  # otomatis float

# eksponen (pangkat)
print(a**b)  # a pangkat b

# modulus (sisa pembagian)
print(a % b)

# floor division (counter part dari modulus)
print(a//b)  # bulet kebawah

# # prioritas operasi aritmatika
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(hasil)
# 3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3
# urutan:  (), eksponen, perkalian (pembagian, modulus dan floor division), pertambahan (pengurangan)
