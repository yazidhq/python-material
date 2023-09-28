# operator assignment
# operasi yang dapat dilakukan dengan penyingkatan

# operasi ditambah dengan assignment

# assignment
a = 5

# a = a + 1
a += 1
print(a)

# a = a - 1
a -= 3
print(a)

# a = a * 1
a *= 5
print(a)

# dan seterusnya sesuai operator aritmatika.....


# operasi bitwise
# OR (|)
b = True
b |= False
print(b)

# AND (&)
b = True
b &= False
print(b)

# XOR (^)
b = True
b ^= False
print(b)

# shifting
c = 0b0100
print(format(c, "08b"))
c >>= 2
print(format(c, "08b"))
c <<= 2
print(format(c, "08b"))
