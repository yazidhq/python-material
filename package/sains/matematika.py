# Modul Matematika

def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
    return hasil


def kurang(*args):
    hasil = 0
    for data in args:
        hasil -= data
    return hasil


def pangkat(n: int):
    return lambda angka: angka**n
