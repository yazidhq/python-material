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
