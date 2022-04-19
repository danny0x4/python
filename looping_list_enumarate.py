# looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"Angka = {angka}")

peserta = ["Ucup","Otong","Dadang","Diding","Dudung"]

for nama in peserta:
    print(f"Nama = {nama}")

# for loop dan range
print("\nFor Loop dan range")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka = {kumpulan_angka[i]}")

# while
print("\nWhile Loop")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"Angka = {kumpulan_angka[i]}")
    i += 1


# list comprehension
data = ["Ucup",1,2,3,"Otong"]

[print(f"Data = {i}") for i in data]

angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)


# enumarate
print("\nEnumarate")
data_list = ["Ucup",1,2,3,"Otong"]

for index,data in enumerate(data_list):
    print(f"Index = {index}, data = {data}")