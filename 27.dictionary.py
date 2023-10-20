# dictionary (dict) -> associative array
# identifier index -> key

data_dict = {
    'key1': 'value1',
    'key2': 'value2',
}
print(data_dict["key1"])

# operator dictionary
data = {
    "nama": "Yazid Dhiaulhaq Ismail",
    "umur": 21,
    "npm": "31120173"
}

# panjang dictionary
lendata = len(data)
print(lendata)

# mengecek key exist atau tidak
checkkey = "nama" in data
print(checkkey)

# mengakses value(read) dengan get
print(data["nama"])
print(data.get("nama"))
print(data.get("kis"))  # hasil none, jika tidak pakai get jadi error
print(data.get("kis", "Tidak Ditemukan"))  # buat pesan sendiri kalau tidak ada

# update data manual
data["nama"] = "Yazid"
print(data)

# update
data.update({"nama": "Yazid Dhiaulhaq"})
print(data)
# jika data tidak ada, maka otomatis ditambah data baru
data.update({"TEST": "GAK ADA"})
print(data)

# mendelete data
del data["TEST"]
print(data)

# looping: hasilnya keynya
for i in data:
    print(i)

# operator untuk mengambil item/ iterables
keys = data.keys()
print(keys)
values = data.values()
print(values)
items = data.items()
print(items)

# menampilkan key
for key in data.keys():
    print(key)  # bisa data[key]

# menampilkan values
for value in data.values():
    print(value)

# menapilkan key dan value
for item in data.items():
    print(item)

# memanggil key dan values masing masing
for key, value in data.items():
    print(f"{key} : {value}")


# # Copy Dictionary
temans = {
    "cup": "Ucup Surucup",
    "dung": "Dudung Surudung",
    "tong": "Otong Surotong",
    "sep": "Asep Siacep",
}

friends = temans.copy()

print(f"Temans: {temans}\n")
print(f"Friends: {friends}\n")

temans["cup"] = "Ouch"
print(f"Temans: {temans}\n")
print(f"Friends: {friends}\n")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"{dataAsep}")
print(f"Friends: {friends}\n")

# pop item dictionary (yang terakhir)
dataAkhir = friends.popitem()
print(f"{dataAkhir}")
print(f"Friends: {friends}\n")
