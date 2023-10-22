# Function

# definition, nama fungsi, (arg1, arg2, ...)
#                 badan fungsi

# Pemanggilan fungsi harus setelah dibuatnya fungsi

# hello_world("Hello World", 5) # tidak bisa seperti ini


def hello_world(word, reps):
    i = 0
    while i < reps:
        print(word)
        i += 1


hello_world("Hello World", 2)


def hi(nama):
    print(f"Selamat datang {nama}")


hi("Yazid")


def tambah(a1, a2):
    hasil = a1 + a2
    print(hasil)


tambah(1, 2)


def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Hallo, {peserta}")


anggota = ['Ucup', 'Otong', 'Dudung']
say_hi(anggota)


# dengan return
def kuadrat(x):
    hasil = x**2
    return hasil


y = kuadrat(5)
print(y)


def operasi_mtk(a1, a2):
    tambah = a1 + a2
    kurang = a1 - a2
    kali = a1 * a2
    bagi = a1 / a2
    return tambah, kurang, kali, bagi


k, l, m, n = operasi_mtk(10, 5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")


# DEFAULT ARGUMENT IN FUNCTION
# def fungsi(argumen):
# def fungsi(argument = nilai defaultnya)
def student(nama="NONE"):
    print(f"Hi, {nama}")


student()


# akses argumen
def total(i1=1, i2=2, i3=3, i4=4):
    hasil = i1+i2+i3+i4
    return hasil


print(total(i3=100))
