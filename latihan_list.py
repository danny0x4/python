# program list buku

list_buku = []
while True:
    print("Masukan Data Buku")
    judul = input("Masukan Judul Buku\t: ")
    penulis = input("Masukan Nama Penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} |{buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    isLanjut = input("Apakah masih dilanjutkan?(y/n) ")

    if isLanjut == "n":
        break
    
print("Program Selesai")

#AXXXXXXXXXXXXXXXXXXI
#AQILLACLARISSAPUTRIMAHARANI
