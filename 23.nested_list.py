from copy import deepcopy

data_0 = [1, 2]
data_1 = [3, 4]

data_list = [1, 2, 3, 4]
print(data_list)

data_nested_list = [data_0, data_1]
print(data_nested_list)

# contoh
peserta_0 = ["ucup", 25, "Pria"]
peserta_1 = ["Otong", 20, "Pria"]
peserta_2 = ["Siti", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(list_peserta)

for peserta in list_peserta:
    print(f"nama: {peserta[0]}")
    print(f"umur: {peserta[1]}")
    print(f"kelamin: {peserta[2]}\n")

# dengan reference
list_copy = list_peserta.copy()
print(list_copy)
peserta_0[0] = "Yazid"
print(list_copy)

# # Copy Nested List (deep copy)
data_0 = [1, 2]
data_2 = [3, 4]

# general copy
data = [data_0, data_1, 10]
data_copy = data.copy()

print(data)
print(data_copy)

# adress
print(f"addres data{hex(id(data))}")
print(f"addres data{hex(id(data_copy))}")

print(f"address member ke-1 = {hex(id(data[0]))}")
print(f"address member ke-1 = {hex(id(data_copy[0]))}")

data[1][0] = 5
data[2] = 7
print(data)
print(data_copy)


print("DEEP COPY")
# deep copy (import)
data = [data_0, data_1]
data_deep_copy = deepcopy(data)
data[1][0] = 3
print(data)
print(data_deep_copy)
