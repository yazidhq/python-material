# # 1. mode write
# akan membuat file baru jika tidak ada
# dan menimpa atau overwrite isinya

with open("D:/Belajar Data Analis/Python/write external file/data_1.txt", mode="w", encoding="utf-8") as file:
    file.write("John si johny")

# ketimpa
with open("D:/Belajar Data Analis/Python/write external file/data_1.txt", mode="w", encoding="utf-8") as file:
    file.write("Ucup Surucup")


# # 2. mode append
with open("D:/Belajar Data Analis/Python/write external file/data_2.txt", mode="w", encoding="utf-8") as file:
    file.write("John si johny\n")

with open("D:/Belajar Data Analis/Python/write external file/data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("Ucup Surucup\n")

with open("D:/Belajar Data Analis/Python/write external file/data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("Dono Situpang")


# # mode r+
with open("D:/Belajar Data Analis/Python/write external file/data_3.txt", mode="w", encoding="utf-8") as file:
    file.write("data ke3\n")

with open("D:/Belajar Data Analis/Python/write external file/data_3.txt", mode="r+", encoding="utf-8") as file:
    file.write("menambah dengan r+ baris 1\n")
    file.write("menambah dengan r+ baris 2\n")
    file.write("menambah dengan r+ baris 3\n")

with open("D:/Belajar Data Analis/Python/write external file/data_3.txt", mode="r+", encoding="utf-8") as file:
    print(file.read())

with open("D:/Belajar Data Analis/Python/write external file/data_3.txt", mode="r+", encoding="utf-8") as file:
    file.write("otong surotong")  # akan menimpa isi text sesuai panjang data
