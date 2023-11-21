# Contoh membuat exception

from numbers import Number


def tambah(a: int, b: int) -> int:
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "input harus angka"
    return a+b


print(tambah(1, 1))


# menangkap tipe exceptionnya
angka = 0
try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)

# atau bisa langsung
angka = 0
try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)
