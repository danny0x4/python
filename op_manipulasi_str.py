# operasi dan manipulasi str

# 1. menyambung string (concatenate)



nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari str

panjang = len(nama_lengkap)
print(" panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator utk str

# mengecek apakah ada komponen char atau str di str

d = "d"
status = d in nama_lengkap
print(" str " + d + " ada di" + nama_lengkap + " = " + str(status) )

D = "D"
status = d in nama_lengkap
print(" str " + d + " ada di" + nama_lengkap + " = " + str(status) )

d = "d"
status = d not in nama_lengkap
print(" str " + d + " tidak ada di " + nama_lengkap + " = " + str(status) )

# mengulang str
print(20*"wkwk")

# indexing
print("index ke 0 : " + nama_lengkap[0])
print("index ke 6 : " + nama_lengkap[6])
print("index ke -1 : " + nama_lengkap[-1])
print("index ke -2 : " + nama_lengkap[-2])
print("index ke-[0:3]:" + nama_lengkap[0:3])
print("index ke-[0:3]:" + nama_lengkap[0:4])
print("index ke-[3:7]:" + nama_lengkap[3:8])
print("index ke-[0:2,4,6,8,10]:" + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

# ord (untuk mengambil unicode 1 karakter str)
# chr (adalah karakter)
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("karakter untuk ascii 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada data " + data + " = " + str(jumlah))