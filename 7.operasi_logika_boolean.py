# operasi logika atau boolean

# not, or, and, xor

a = True
b = False

x = True
y = True

# not
print('====NOT====')
print(not a)

# or (salah satu true, maka true)
print('====OR====')
print(a or b)
print(x or y)

# and (keduanya harus true untuk mendapatkan hasil true)
print('====AND====')
print(a and b)
print(x and y)

# xor (operator bitwise) ^
# akan true jika salah satu saja yang true, sisanya false
# jika 2 true, hasil false
print('====XOR====')
print(a ^ b)
print(x ^ y)
