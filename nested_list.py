data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

# list didalam list
list_2D = [data_0,data_1,6,7]

print(f"List 2D = {list_2D}")

# contoh penggunaan
perserta_0 = ["Ucup",25,"Laki-laki"]
perserta_1 = ["Otong",10,"Laki-laki"]
perserta_2 = ["Dedeh",50,"Perempuan"]

list_peserta = [perserta_0,perserta_1,perserta_2]
print(f"Perseta = {list_peserta}")


for perserta in list_peserta:
    print(f"Nama\t: {perserta[0]}")
    print(f"Umur\t: {perserta[1]}")
    print(f"Gender\t: {perserta[2]}\n")


# permasalahan dengan reference

list_copy = list_peserta.copy()
print(f"Perserta = {list_copy}")
perserta_0[0] = "Michael"
print(f"Perserta = {list_copy}")
print(f"Perseta = {list_peserta}")