# modul matematika
def math(n, *args, **kwargs):
    hasil = 0
    if kwargs["option"] == "tambah":
        for data in args:
            hasil += data
        return hasil
    elif kwargs["option"] == "kurang":
        for data in args:
            hasil -= data
        return hasil
    elif kwargs["option"] == "kali":
        hasil = 1
        for data in args:
            hasil *= data
        return hasil
    elif kwargs["option"] == "bagi":
        hasil = 1
        for data in args:
            hasil /= data
        return hasil


def pangkat(n: int):
    return lambda x: x**n
