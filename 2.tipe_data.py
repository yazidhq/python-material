# a = 10, adalah variabel dengan nilai 10

# tipe data: integer (angka satuan)
from ctypes import c_double
data_int = 1  # tidak ada koma
print(type(data_int))  # cara melihat tipe data apa yang disimpan

# tipe data: float (angka dengan koma)
data_float = 1.5
print(type(data_float))  # float

# tipe data: string (kumpulan karakter)
data_string = "Yazid Dhiaulhaq"
print(type(data_string))  # str

# tipe data: boolean (biner true/false)
data_boolean = False
print(type(data_boolean))  # bool

# # tipe data khusus
# bilangan kompleks
data_complex = complex(5, 6)
print(data_complex)
print(type(data_complex))  # complex

# tipe data dari bahasa C
# from ctypes import c_double, c_char, c_long, dkk
data_c_double = c_double(10.5)
print(data_c_double)
print(type(data_c_double))
