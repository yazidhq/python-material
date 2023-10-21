import datetime as dt
import os
import string as str
import random as rd

# template dict mhs
mahasiswa_tamplate = {
    'nama': 'nama',
    'npm': '000000000',
    'sks': 0,
    'lahir': dt.datetime(1111, 1, 11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print('-'*60)
    print(f"{'SELAMAT DATANG':^60}")
    print(f"{'INPUT DATA MAHASISWA':^60}")
    print('-'*60)

    # fromkeys: menyesuaikan key dari template yang dibuat
    mahasiswa = dict.fromkeys(mahasiswa_tamplate.keys())

    mahasiswa['nama'] = input("Nama Mahasiswa\t\t:")
    mahasiswa['npm'] = input("NPM Mahasiswa\t\t:")
    mahasiswa['sks'] = int(input("SKS Lulus\t\t:"))
    TAHUN = int(input("Tahun Lahir (YYYY)\t:"))
    BULAN = int(input("Bulan Lahir (MM)\t:"))
    TANGGAL = int(input("Tanggal Lahir (DD)\t:"))
    mahasiswa['lahir'] = dt.datetime(TAHUN, BULAN, TANGGAL)

    # random key
    KEY = ''.join((rd.choice(str.ascii_uppercase) for i in range(6)))

    # memasukkan mahasiswa ke data_mahasiswa
    data_mahasiswa.update({KEY: mahasiswa})

    print("\n")
    print("-"*65)
    print(f"{'KEY':<8}{'Nama':<25}{'NPM':<10}{'SKS':<5}{'Lahir':<6}")
    print("-"*65)

    for mhs in data_mahasiswa:
        KEY = mhs
        NAMA = data_mahasiswa[KEY]['nama']
        NPM = data_mahasiswa[KEY]['npm']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

        print(f"{KEY:<8}{NAMA:<25}{NPM:<10}{SKS:<5}{LAHIR:<6}")

    is_lanjut = input("\nApakah ingin menambah lagi (n/y): ")
    if is_lanjut == 'n':
        break

print("Terimakasih!")
