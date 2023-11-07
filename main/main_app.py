# __main__ : adalah top level code environment

# __name__ = "__main__" : akan terjadi jika ada di program utama

# # __name__ pada file program external
import fungsi


import package


# # __name__ pada file program utama
print(f"Nilai __name__ pada main_app.py = {__name__}")


# # contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a: int, b: int) -> int:
    return a+b


# fungsi utama
if __name__ == "__main__":
    print(fungsi_tambah(1, 2))
