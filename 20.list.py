# LIST

angka1 = 1
angka2 = 2
angka3 = 3


# Kumpulan data angka
data_angka = [1, 2, 3]
print(data_angka)

# kumpulan data string
data_string = ["yazid", "dhiaulhlaq", "ismail"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False]
print(data_boolean)

# campuran
data_campuran = [1, "donat", True]
print(data_campuran)

# Cara lain membuat List (Alternative)
data_range = range(0, 10, 3)  # 0 sampai 9 kelipatan 3
print(data_range)
data_list = list(data_range)
print(data_list)

# List dengan for loop, list comprehension
list_for = [i**2 for i in range(0, 10)]
print(list_for)

# list dengan for dan if
list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_for_if)
