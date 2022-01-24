# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nProgram Konversi Temperature\n")

celcius = float(input('Masukan Suhu dalam Celcius :'))
print("suhu celcius = ",celcius)

# reamur
reamur = (4/5) * celcius
print("suhu reamur = ",reamur)

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu fahrenheit =",fahrenheit)

# kelvin
kelvin = celcius + 273
print("Suhu Kelvin =",kelvin)