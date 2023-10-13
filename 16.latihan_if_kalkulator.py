# latihan

# kalkulator sederhana

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
aritmatika = int(input("Pilih perhitungan yang ingin dihitung: "))

angka1 = int(input("angka pertama: "))
angka2 = int(input("angka kedua: "))

if aritmatika == 1:
    hasil = angka1 + angka2
    print(f"Hasilnnya {hasil}")
elif aritmatika == 2:
    hasil = angka1 - angka2
    print(f"Hasilnnya {hasil}")
elif aritmatika == 3:
    hasil = angka1 * angka2
    print(f"Hasilnnya {hasil}")
elif aritmatika == 4:
    hasil = angka1 / angka2
    print(f"Hasilnnya {hasil}")
else:
    print("Anda memilih diluar pilihan")
