# format string

# contoh generic

# string
nama = "maler"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2005.5
# format_str = "angka = " + str(angka)
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka bulat
angka = 15
format_str = f"bil bulat = {angka:d}"
print(format_str)

# bilangan ordo ribuan
angka = 200000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:019.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.12345
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+f}"
print(format_minus)
print(format_plus)

# memformat persen %
persen = 0.55
format_persen = f"persen = {persen:.1%}"
print(format_persen)

# melakukan operasi aritmatika di dalam {}
harga = 10000
jumlah = 5
format_str = f"harga total = Rp. {harga * jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadesimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)
