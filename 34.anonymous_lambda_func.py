# Lambda Function: bisa membuat program menjadi lebih simple

# function biasa
def f_kuadrat(angka):
    return angka**2


print(f_kuadrat(2))


# menggunakan lambda function
# output = lambda argument
# kuadrat= lambda angka:angka**2
def kuadrat(angka): return angka**2


print(kuadrat(6))


# pangkat = lambda num, pow:num**pow
def pangkat(num, pow): return num**pow


print(pangkat(4, 2))


# # Kegunaan

# sorting untuk list biasa
data_list = ["otong", "ucup", "dudung"]
data_list.sort()
print(data_list)


# sorting pakai panjang
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(data_list)


# sort pakai lambda
data_list = ["otong", "ucup", "dudung"]
data_list.sort(key=lambda nama: len(nama))
print(data_list)


# filter pakai lambda
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# kasus angka kurang dari 5 dengan biasa
def kurang_dari_lima(angka):
    return angka < 5


data_angka_baru_biasa = list(filter(kurang_dari_lima, data_angka))
print(data_angka_baru_biasa)


# kasus angka kurang dari 5 dengan lambda
data_angka_baru_lambda = list(filter(lambda x: x < 7, data_angka))
print(data_angka_baru_lambda)

# kasus genap
data_genap = list(filter(lambda x: x % 2 == 0, data_angka))
print(data_genap)

# kelipatan 3
data_3 = list(filter(lambda x: x % 3 == 0, data_angka))
print(data_3)

# # anonymouse function
# currying -> haskell curry


# fungsi biasa
def pangkat(angka, n):
    hasil = angka**n
    return hasil


print(pangkat(3, 4))


# fungsi dengan currying
def pangkat(n):
    return lambda angka: angka**n


print(pangkat(2)(5))  # pangkat 2 dari 5
print(pangkat(5)(5))  # pangkat 5 dari 5
