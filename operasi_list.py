data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"Data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"Jumlah angka 4 = \n{jumlah_data_4}")
print(f"Jumlah angka 3 = \n{jumlah_data_3}")

# ambil posisi data

data = ["Ucup","Otong","Dudung","Ujang"]

print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"Index si Dudung = {index_dudung}")
print(f"Index si Ujang = {index_ujang}")

# mengurutkan list
print(f"Data angka sebelum di sort = \n{data_angka}")
data_angka.sort()
print(f"Data angka sort = \n{data_angka}")

print(f"Data = {data}")
data.sort()
print(f"Data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"Data reverse = \n{data_angka} \n{data}")

