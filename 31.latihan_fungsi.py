import os

# program menghitung luas dan keliling persegipanjang

# # membuat header program
# os.system('cls')
# print(f"{'PROGAM MENGHITUNG LUAS':^80}\n{'DAN KELILING PERSEGI PANJANG':^80}")
# print(f"{'-'*40:^80}")

# # mengambil user input
# LEBAR = int(input("Masukkan lebar persegi panjang: "))
# PANJANG = int(input("Masukkan panjang persegi panjang: "))

# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # Hasil
# print(f"Hasil perhitungan Luas = {LUAS}")
# print(f"Hasil perhitungan Keliling = {KELILING}")


# # DENGAN FUNCTION

# header
def header():
    os.system('cls')
    print(f"{'PROGAM MENGHITUNG LUAS':^80}\n{'DAN KELILING PERSEGI PANJANG':^80}")
    print(f"{'-'*40:^80}")


# mengambil user input
def input_user():
    lebar = int(input("Masukkan lebar persegi panjang: "))
    panjang = int(input("Masukkan panjang persegi panjang: "))
    return lebar, panjang


# menghitung luas
def hitung_luas(panjang, lebar):
    return panjang * lebar


# menghitung keliling
def hitung_keliling(panjang, lebar):
    return 2 * (panjang + lebar)


# output
def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")


# main program
while True:
    header()

    print("Pilih perhitungan")
    print("1. Luas")
    print("2. Keliling")
    print("3. Keduanya")

    opsi = int(input("Pilih opsi diatas (1/ 2/ 3): "))

    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(PANJANG, LEBAR)
    KELILING = hitung_keliling(PANJANG, LEBAR)

    if opsi == 1:
        display("luas", LUAS)
    elif opsi == 2:
        display("keliling", KELILING)
    else:
        display("luas", LUAS)
        display("keliling", KELILING)

    is_continue = input("Apakah lanjut (y/n): ")
    if is_continue == "n":
        break

print("Program Selesai")
