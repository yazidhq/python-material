# bitwise
# operasi biner
# binary operation
# operasi pada masing masing bit
# int = 2 -> 000000010
# 000000010
# 76543210
# index ke 0, 2^1 = 2
# 2 | 1 -> 00000010 | 00000001
# hasilnya 3

a = 9
b = 5

# bitwise OR (|)
print("===OR (|)===")
c = a | b
print("nilai a: ", a, "binary", format(a, "08b"))
print("nilai b: ", b, "binary", format(b, "08b"))
print("--------------------------- |")
print("nilai c: ", c, "binary", format(c, "08b"))

# bitwise AND (&)
print("===AND (&)===")
c = a & b
print("nilai a: ", a, "binary", format(a, "08b"))
print("nilai b: ", b, "binary", format(b, "08b"))
print("--------------------------- &")
print("nilai c: ", c, "binary", format(c, "08b"))

# bitwise XOR (^)
print("===XOR (^)===")
c = a ^ b
print("nilai a: ", a, "binary", format(a, "08b"))
print("nilai b: ", b, "binary", format(b, "08b"))
print("--------------------------- ^")
print("nilai c: ", c, "binary", format(c, "08b"))

# bitwise NOT (~)
print("===NOT (~)===")
c = ~a
print("nilai a: ", a, "binary", format(a, "08b"))
print("--------------------------- ~")
print("nilai c: ", c, "binary", format(c, "08b"))

# shifting (menggeser)
# sihft right (>>)
print("===SHIFT RIGHT (>>)===")
c = a >> 1
print("nilai a: ", a, "binary", format(a, "08b"))
print("--------------------------- >>")
print("nilai c: ", c, "binary", format(c, "08b"))

# sihft left (<<)
print("===SHIFT LEFT (<<)===")
c = a << 3
print("nilai a: ", a, "binary", format(a, "08b"))
print("--------------------------- >>")
print("nilai c: ", c, "binary", format(c, "08b"))
