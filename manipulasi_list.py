## Operasi 

# index 0(-3) 1(-2) 2(-1)

data = ["ucup","bayu","setan"]

data_0 = data[0]
print(f"Data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"Data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
# menggunakan len

panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item pada list sesuai posisi

print(f"Data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"Data sesudah ditambahkan = \n{data}")

# ingin menambah diakhir list
data.append("Jajang")
print(f"Data ditambah lagi = \n{data}")

# menambah list dengan list
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"Data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"Data rubah = {data}")

# mendelete data atau meremove data
data.remove("Ujang")
print(f"Data remove = \n{data}")
# data.remove("usep") ini akan error karena huruf harus sesuai. Upper dan Lowercase

# meremove data paling belakang
data_akhir = data.pop()
print(f"Data akhir = \n{data}")

print(data_akhir)