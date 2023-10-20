# looping list

# for loop
angka = [4, 3, 2, 1]
for row in angka:
    print(row)

# for loop dan range
angka = [100, 90, 80, 70]
panjang_angka = len(angka)
for row in range(panjang_angka):
    print(angka[row])

# while loop
angka = [4, 7, 2, 4, 2, 6, 7]
panjang_angka = len(angka)
i = 0
while i < panjang_angka:
    print(angka[i])
    i += 1

# list comprehension
data = ["Yazid", 22, 12, 2001]
[print(i) for i in data]

# Enumerate: mengambail index dan datanya
data = ["Yazid", 22, 12, 2001]
for index, data in enumerate(data):
    print(index, data)
