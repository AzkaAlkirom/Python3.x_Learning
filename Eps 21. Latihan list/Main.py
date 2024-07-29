# latihan list 

list_buku = []
while True: 
    print("\n"+" Latihan List ".center(40,"="))
    print("masukkan data buku yang anda inginkan")

    judul = input("masukkan judul buku       : ")
    penulis = input("masukkan penulis buku   : ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}. {buku[0]} ciptaan {buku[1]}")

    print("\n"+" Attention!! ".center(40,"="))
    isLanjut = input("Apakah anda ingin menginput lagi? (y/n) : ")

    if isLanjut == "n":
        break

