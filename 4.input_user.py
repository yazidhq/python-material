# input user

# data yang dimasukkan pasti bertipe string
data = input("Masukkan data: ")
print("data= ", data, "| tipe= ", type(data))

# jika ingin mengambil data menjadi int
angka = float(input("Masukkan angka: "))  # bisa int, karna sama sama angka
print("data= ", angka, "| tipe= ", type(angka))

# data yang dimasukkan pasti bertipe boolean
# jika tidak dicast ke int terlebih dahulu, hasil akan terus bertipe true
biner = bool(int(input("Masukkan data: ")))
print("data= ", biner, "| tipe= ", type(biner))
