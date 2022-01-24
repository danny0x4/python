# Latihan

# kalkulator sederhana
from ast import operator


print(20*"=")
print("Kalkukator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukan angka pertama = "))
op = input("Operator (+,-,x,/): ")
angka_2 = float(input("Masukan angka kedua = "))

# percabangannya

if op == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}:")
elif op == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah = {hasil}")
elif op == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah = {hasil}")
elif op == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah = {hasil}")
else:
    print("Tolong masukan yang benar")

print("Hasil akhir program")