# latihan konversi satuan temperature

# celcius -> reamur = 4/5 C
# celcius -> fahrenheit = 9/5 C + 32
# celcius -> kelvin = C + 273

# reamur -> celcius = 5/4 R
# reamur -> fahrenheit = 9/4 R + 32
# reamur -> kelvin = 5/4 R + 273

# fahrenheit -> celcius = 5/9 * (f - 32)
# fahrenheit -> reamur = 4/9 * (f - 32)
# fahrenheit -> kelvin = 5/9 * (f - 32) + 273,15

# kelvin -> celcius = k - 273
# kelvin -> reamur = 4/5 * (k - 273)
# kelvin -> fahrenheit = 9/5 * (K - 273) + 32

# # program konversi celcius ke satuan lain
print("\n=====PROGRAM KONVERSI TEMPERATUR CELCIUS===\n")
celcius = float(input("Masukkan suhu celcius: "))
reamur = 4 / 5 * celcius
fahrenheit = 9 / 5 * celcius + 32
kelvin = celcius + 273
print("Hasil celcius -> reamur =", reamur, "R")
print("Hasil celcius -> fahrenheit =", fahrenheit, "F")
print("Hasil celcius -> kelvin =", kelvin, "K")

# # program konversi reamur ke satuan lain

# # program konversi fahrenheit ke satuan lain

# # program konversi kelvin ke satuan lain
