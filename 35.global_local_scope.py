# # Global dan Local Scope

nama_global = "Yazid"


# akses variable global pada fungsi
def fungsi():
    print(nama_global)


fungsi()

# akses variable global pada loop
for i in range(0, 3):
    print(f"{i} = {nama_global}")


# variable local scope
def fungsi2():
    nama_local = "Dhiaulhaq"


# print(nama_local)  # error karena tidak bisa mengakses variabel local di global


# # Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")


nama = "otong"
say_otong()

# # Contoh 2: merubah variabel global
angka = 0
name = "Yazid"


def ubah_angka(nilai_baru, nama_baru):
    global angka, name
    angka = nilai_baru
    name = nama_baru


print(angka)
print(name)
ubah_angka(10, "otong")
print(angka)
print(name)


# # Contoh 3: bisa mengakses dan merubah variabel untuk for dan if
angka = 0
for i in range(0, 5):
    angka += i
    angka_dummy = 1

if True:
    kata_dummy = "tes"

print(angka)
print(angka_dummy)  # bisa diakses di scope for
print(kata_dummy)  # bisa diakses di scope for
