# perulangan (loop)

# for kondisi :
#   aksi

# ini dengan list
angka2 = [0,5,6,9,4] # ini adalah list
print(angka2)

for i in angka2:
    print(f"i sekarang -> {i}")


print("ini adalah akhir dari program 1\n")

# ini dengan range
angka3 = range(5)

for i in angka3:
    print(f"i sekarang -> {i}")

print("Ini adalah akhir dari program 2\n")

angka4 = range(1,11)

for i in angka4:
    print(f"i sekarang -> {i}")
    #print("saya keren")

print("Ini adalah akhir dari program 3\n")

# menggunakan str
data_str = "saya ganteng abis"

for huruf in data_str:
    print(huruf)
print("Ini adalah akhir dari program 4\n")
