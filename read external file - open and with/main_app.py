# membaca file ekternal

print(3*"=", "Membaca file txt", 3*"=")
file_path = "D:/Belajar Data Analis/Python/read external file - open and with/data.txt"
file = open(file_path, mode="r")

# mengecek status apakah bisa read atau tidak
print(f"status read : {file.readable()}")

# mengecek status apakah bisa write atau tidak
print(f"status write : {file.writable()}")


# # baca seluruh file
print(file.read())

# # baca perbaris
# # membaca baris pertama, dengan end="" untuk menggantikan /n menjadi string kosong
# print(file.readline(), end="")
# # membaca baris kedua
# print(file.readline())

# # baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose? {file.closed}")

# cara close
file.close()

print(f"apakah file sudah diclose? {file.closed}")


# # salah satu teknik membuka file di python

# menggunakan with
print("\n\n", 3*"=", "Membaca file dengan with", 3*"=")

# jadi tidak perlu menggunakan file close, diluar with sudah otomatis close
with open(file_path, mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file sudah diclose? {file.closed}")

print(f"apakah file sudah diclose? {file.closed}")
