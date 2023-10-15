# latihan looping triangle

sisi = 10

# for
count = 1
for i in range(sisi):
    print(f"*" * count)
    count += 1

# while
count = 1
while True:
    print(f"*" * count)
    count += 1
    if count > sisi:
        break

# hanya ganjil saja
count = 1
spasi = int(sisi/2)
while True:
    if count % 2:
        # print jika ganjil
        print("+"*count)
        count += 1
    else:
        # ditambah 1 dan kembail ke atas jika genap
        count += 1
        continue
    # break jika count > sisi
    if count > sisi:
        break

# segitiga samakaki
count = 1
spasi = int(sisi/2)
while True:
    if count % 2:
        # print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        # ditambah 1 dan kembail ke atas jika genap
        count += 1
        continue
    # break jika count > sisi
    if count > sisi:
        break
