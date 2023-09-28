# casting adalah merubah suatu tipe data ke tipe data yang lain

# # INTEGER
print("====INTEGER====")
data_int = 9
print("Data: ", data_int)
print("Tipe: ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data: ", data_float, "Tipe: ", type(data_float))
print("Data: ", data_str, "Tipe: ", type(data_str))
print("Data: ", data_bool, "Tipe: ", type(data_bool))

# # FLOAT
print("====FLOAT====")
data_float = 9.9
print("Data: ", data_float)
print("Tipe: ", type(data_float))

data_int = int(data_float)  # dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
print("Data: ", data_int, "Tipe: ", type(data_int))
print("Data: ", data_str, "Tipe: ", type(data_str))
print("Data: ", data_bool, "Tipe: ", type(data_bool))

# # BOOELAN
print("====BOOELAN====")
data_bool = True
print("Data: ", data_bool)
print("Tipe: ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)  # false jika nilai 0
print("Data: ", data_int, "Tipe: ", type(data_int))
print("Data: ", data_str, "Tipe: ", type(data_str))
print("Data: ", data_float, "Tipe: ", type(data_float))

# # STRING
print("====STRING====")
data_str = "15"
print("Data: ", data_str)
print("Tipe: ", type(data_str))

data_int = int(data_str)  # string harus berisi angka
data_bool = bool(data_str)  # false jika string 0
data_float = float(data_str)  # string harus berisi angka
print("Data: ", data_int, "Tipe: ", type(data_int))
print("Data: ", data_bool, "Tipe: ", type(data_bool))
print("Data: ", data_float, "Tipe: ", type(data_float))
