# program list buku

list_buku = []
while True:
    print("Data Buku")
    judul = input("Masukkan judul buku\t:")
    penulis = input("Masukkan penulis buku\t:")
    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print(list_buku)

    print("\n")
    print("No.\t|Judul\t|Penulis\t")
    for index, buku in enumerate(list_buku):
        print(f"{index}\t|{buku[0]}\t|{buku[1]}")
    print("\n")

    isLanjut = input("Ingin tambah buku lagi? (Y | N) :")

    if isLanjut == "N":
        print("Terimakasih!")
        break
