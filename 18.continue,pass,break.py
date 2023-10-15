# Control flow: Continue, pass, break

# pass => berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass  # tidak diekseskusi
    print(angka)
print("akhir program")

# continue => skip aksi selanjutnya dan loncat ke steap selanjutnya
angka1 = 0
while angka1 < 5:
    angka1 += 1
    if angka1 == 3:
        print("CHECK!")
        # membuat loop loncat ke steap selanjutnya (kasus ini angka 3 diskip)
        continue
    print(f"angka {angka1}")
print("akhir program")

# break => skip aksi selanjutnya dan langsung selesai
angka2 = 0
while angka2 < 10000000:
    angka2 += 1
    if angka2 == 11:
        print("CHECK!")
        break  # langsung menyelesaikan looping dan ke akhir progran
    print(f"angka {angka2}")
print("akhir program")

# contoh lain break dan continue
data = int(input("hitung sampai = "))
angka3 = 0
while True:
    if data < 0:
        print("Anda memasukkan dibawah 0")
        break
    angka3 += 1
    if angka3 == 1:
        print(f"Mulai di angka {angka3}")
        continue
    print(f"Count {angka3}")
    if angka3 == data:
        print(f"Selesai di angka {data}")
        break
