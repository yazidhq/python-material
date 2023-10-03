# string width adn Multiline

# data
data_nama = "yazid"
data_umur = 21
data_tinggi = 169.5
data_nomor_sepatu = 39

# string multiline (enter, newline, \n)
data_str = f"Nama = {data_nama}\nUmur = {data_umur}\nTinggi = {data_tinggi}\nSepatu = {data_nomor_sepatu}\n"
print(5*"="+"Data String"+"="*5)
print(data_str)

# string multiline (kutip triplets)
data_str = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Sepatu = {data_nomor_sepatu}
"""
print(5*"="+"Data String"+"="*5)
print(data_str)

# mengatur lebar
data_str = f"""Nama    = {data_nama:>10}
Umur    = {data_umur:>10}
Tinggi  = {data_tinggi:>10}
Sepatu  = {data_nomor_sepatu:>10}"""
print(5*"="+"Data String"+"="*5)
print(data_str)
