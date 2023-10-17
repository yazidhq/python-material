# OPERASI
data = ["Yazid", "Dhiaulhaq", "Ismail"]

# mengambil data dari list
print(f"Data pertama (ke-0): {data[0]}")
print(f"Data terakhir: {data[-1]}")

# mengambil length list
print(f"Panjang data: {len(data)}")


# # Manipulasi Data (merubah-ubah data)

# menambah item sesuai posisi (insert(posisi, item))
data.insert(1, "Dodi")
print(data)

# menambah di akhir list
data.append("Sukijan")
print(data)

# menambah list dengan list
data_baru = [1, 2, 3]
data.extend(data_baru)
print(data)

# merubah data
# ubah data ke 2
data[2] = "Michael"
print(data)

# remove data
data.remove("Yazid")  # huruf harus sesuai
print(data)

# meremove data paling akhir
data.pop()
print(data)
