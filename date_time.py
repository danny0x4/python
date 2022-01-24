# Date and time (latihan)

import datetime as dt

#hari_ini = dt.date.today()

#print(hari_ini)
#print(f"hari ini adalah hari = {hari_ini:%A}")


#tgl = dt.date(2005,4,11)
#print(tgl)
#print(f"hari ini adalah hari = {tgl:%A}")

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tgl = int(input("Tanggal \t\t: "))
bln = int(input("Bulan \t\t: "))
thn = int(input("Tahun \t\t: "))

tgl_lhr = dt.date(thn,bln,tgl)
print(f"tanggal lahir kamu adalah {tgl_lhr}")
print(f"Hari nya adalah {tgl_lhr:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tgl_lhr
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365 // 30)

print(umur_tahun)
print(f"Umur kamu adalah: {umur_tahun} tahun, {umur_bulan_sisa}")