# Date and Time (latihan)

import datetime as dt

print("Silahkan masukkan tanggal, bulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal Lahir \t:{tanggal_lahir}")
print(f"Hari Lahir \t:{tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_bulan = (umur_hari.days % 365) // 30
umur_tahun = umur_hari//365
print(f"Umur Hari \t:{umur_hari.days} Hari")
print(f"Umur Bulan \t:{umur_bulan} Bulan")
print(f"Umur Tahun \t:{umur_tahun.days} Tahun")
