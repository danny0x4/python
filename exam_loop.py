# latihan perulangan segitiga


# menggunakan for


sisi = 50

# dummy variable
count = 1
for i in range(4):
    print("*"*count)
    count += 1

print("Akhir for")

# while

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir dari while")

# Ganjil
count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        # akan kembali keatas jika ganjil
         print(" "*spasi ,"+"*count)
         spasi -= 1
         count += 1
    else:
    
    # ini akan print jika genap
        count += 1
        continue

    # ini akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir dari while")



