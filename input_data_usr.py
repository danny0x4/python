# Input user

# data yang dimasukan hasilnya pasti string

data = input("Masukan data: ")
print("data: ",data,",type =",type(data))

# jika ingin mengambil int, maka
data_int = int(input("Masukan angka: "))
print("data =",data_int,",type =",type(data_int))

# jika ingin mengambil float, maka
data_float = float(input("Masukan angka: "))
print("data = ",data_float,",type = ",type(data_float))

# jika ingin boolean, maka dijadikan int dulu untuk mendeteksi false dan true
biner = bool(int(input("Masukan angka: ")))
print("data = ",biner,"type = ",type(biner))