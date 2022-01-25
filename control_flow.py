# continue, pass, break

# pass -> berfungsi sebagai dummy dan tidak akan dieksekusi

#angka = 0

#while angka < 5:
#    angka += 1
#    if angka == 3:
#        pass # < tidak akan di eksekusi
#
#    print(angka)

# continue

angka = 0

print(f"ini adalah angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang adalah {angka}") # aksi 1


    if angka == 3:
        print("Nice!")
        continue # akan membuat loop meloncat ke step selanjutnya

    print("Hello") # aksi 2

print("Selesai")