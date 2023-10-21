import datetime as dt

# multikeys
mahasiswa1 = {
    'nama': 'Yazid Dhiaulhaq Ismail',
    'npm': '31120173',
    'sks': 115,
    'beasiswa': True,
    'lahir': dt.datetime(2001, 12, 22)
}

mahasiswa2 = {
    'nama': 'Denny Danang',
    'npm': '31120174',
    'sks': 115,
    'beasiswa': False,
    'lahir': dt.datetime(2001, 10, 10)
}

mahasiswa3 = {
    'nama': 'Siti Marinah',
    'npm': '31120175',
    'sks': 115,
    'beasiswa': False,
    'lahir': dt.datetime(2000, 9, 1)
}

data_mhs = {
    'mhs1': mahasiswa1,
    'mhs2': mahasiswa2,
    'mhs3': mahasiswa3
}

print(f"{'KEY':<6}{'Nama':<25}{'NPM':<10}{'SKS':<5}{'Beasiswa':<10}{'Lahir':<6}")
print("-"*65)
for mhs in data_mhs:
    KEY = mhs
    NAMA = data_mhs[KEY]['nama']
    NPM = data_mhs[KEY]['npm']
    SKS = data_mhs[KEY]['sks']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<6}{NAMA:<25}{NPM:<10}{SKS:<5}{BEASISWA:^10}{LAHIR:<6}")
