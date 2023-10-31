# python standart library
import datetime
from collections import Counter
import io

waktu = datetime.datetime.now()
print(f"waktu sekarang: {waktu}")
print(f"tahun sekarang: {waktu.year}")
print(f"hari sekarang: {waktu.strftime('%A')}")  # hari sekarang

# collections
data = ["a", "b", "c", "a", "c", "c"]

# menghitung jumlah a cara biasa
count = 0
for i in data:
    if i == "a":
        count += 1
print(count)

# dengan library collections
count = Counter(data)
print(count)
print(f"jumlah c: {count['c']}")

# dengan io library
file = io.open("text.txt", "r")
print(file.read())
