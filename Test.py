# library waktu untuk cek antara intepreted dan compile lebih cepet mana
import time
start_time = time.time()

# dieksekusi berurutan dan interpreted

print("Apa kabar?")
print("Kabar baik")
print("Hello World!")
# baris kosong tidak berpengaruh
print("Hi mniez!")

# ini adalah komentar
"""komentar
multiline"""

a = 10  # assignment

# python juga bisa compile ke bytecode
# bytecode : proses compile seperti bahasa c++
# python -m py_compile Test.py (terminal)
# hasil compile folder _pycache_
# masuk ke folder __pycache__ dan gunakan python Test.cpython-311.pyc (klik TAB)

# contoh program looping
for i in range(1, 1000):
    a = 10
    print(a)

# mengecek lebih cepet mana
print(time.time() - start_time, "detik")

# compile bisa lebih cepat
