# # definisi
# syntax error: programnya langsung error ketika dirunning
# runtime error: error ketika program sudah dijalankan dan ada error di tengah jalanm

# data_input = int(input("Masukan angka: "))
# hasil = 10/data_input
# print(hasil)

# # exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana nemangkap exception
# data_input = int(input("Masukan angka: "))
# hasil = "NaN"
# try:
#     hasil = 10/data_input
# except:
#     print(f"input tidak boleh {data_input}")
# print(f"hasil {hasil}")

# contoh di aplikasi
while (True):
    angka = angka = int(input("Masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("Lanjut (y/n)")
        if is_done == "n":
            break
    except:
        print("Pembagi 0, silahkan input ulang")
print("akhir program")

# contoh lain
# jika file sudah ada
try:
    with open("D:/Belajar Data Analis/Python/exception, error, try and except/data.txt", "r") as file:
        print(file.read())
# jika file tidak ada
except:
    print("file data.txt tidak ditemukan, membuat file baru..")
    with open("D:/Belajar Data Analis/Python/exception, error, try and except/data.txt", "w", encoding="utf-8") as file:
        file.write("file baru")
        print("file berhasil dibuat")
print("Akhir program")
