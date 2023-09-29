# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "yazid"
nama_tengah = "dhiaulhaq"
nama_akhir = "ismail"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string
# Mengecek apakah ada komponen string di string
d = "d"
status = d in nama_lengkap
print(status)
status = d not in nama_lengkap
print(status)

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 = " + nama_lengkap[0])
print("index ke-1 = " + nama_lengkap[1])
print("index ke-[0, 5] = " + nama_lengkap[0:6])
print("index ke-[6, 15] = " + nama_lengkap[6:15])
print("index ke-[0, 2, 4, 6, 8, 22] = " + nama_lengkap[0:22:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling kecil : " + max(nama_lengkap))

ascii_code = ord(" ")
print(ascii_code)
data = 117
print(chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print(jumlah)

# # merubah case dari string

# merubah semua ke uppercase
salam = "brO"
salam = salam.upper()
print(salam)

# merubah semua ke lowercase
salam = salam.lower()
print(salam)


# # Pengecekan dengan isX method

# contoh pengecekan lowercase
is_lower = salam.islower()  # hasilnya boolean
print(str(is_lower))

# contoh pengecekan uppercase
is_upper = salam.isupper()  # hasilnya boolean
print(str(is_upper))

# isalpha() => mengecek apakah semuanya huruf
alpha = "hallo"
print(alpha.isalpha())

# isalnum() => apakah huruf dan angka
alnum = "halo123"
print(alnum.isalnum())

# isdecimal() => apakah angka saja
deci = "123"
print(deci.isdecimal())

# isspace() => apakah spasi, tab, newline
space = "       \n"
print(space.isspace())

# istitle() => apakah semua kata dimulai dengan huruf besar
title = "Nama Saya Yazid"
print(title.istitle())

# # ngecek kompoonen startswith() endswith() -> dimulai kata dan diangkiri kata
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print(cek_start)
cek_end = "Sangjangnim Oppa".endswith("Oppa")
print(cek_end)


# # penggabungan komponen join() split()
pisah = ['yazid', 'dhiaulhaq', 'ismail']
gabung = '-'.join(pisah)
print(gabung)  # jadi 1 dengan digabung -
print(gabung.split('-'))  # kembali jadi list

# # alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(20, '-')
print(kanan)

kiri = "kiri".ljust(20)
print(kiri)

tengah = "tengah".center(20)
print(tengah)

# kebalikan dari alokasi karakter -> strip()
kanan = kanan.strip('-')  # menghilangkan tanpa -
print(kanan)
