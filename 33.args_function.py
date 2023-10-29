# *args dan *kwargs

# # *args

# memasukkan data/ argument
def fungsi(nama, tinggi, berat):
    print(f"{nama}, tinggi: {tinggi}, berat: {berat}")


fungsi("Yazid", 174, 75)


# menggunakan data list
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama}, tinggi: {tinggi}, berat: {berat}")


fungsi(["Otong", 170, 55])


# dengan *args(tidak peri list lagi ([]))
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama}, tinggi: {tinggi}, berat: {berat}")


fungsi("Ucok", 150, 95)


# studi kasus: jadi bisa berapa banyak inputnya
def tambah(*data):
    # data tipenya adalah tuple, bisa diiterasi
    hasil = 0
    for angka in data:
        hasil += angka
    return hasil


print(tambah(1, 23, 4, 5, 6, 7))
print(tambah(56, 37, 5, 3, 5, 6, 4,))


# # *kwargs
def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama}, tinggi: {tinggi}, berat: {berat}")


fungsi(nama="Yazid", tinggi=174, berat=75)


# studi kasus
def math(*args, **kwargs):
    hasil = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            hasil += angka
    elif kwargs["option"] == "kurang":
        for angka in args:
            hasil -= angka
    return hasil


print(math(1, 2, 3, 4, 5, 6, option="tambah"))
print(math(1, 2, 3, 4, 5, 6, option="kurang"))
