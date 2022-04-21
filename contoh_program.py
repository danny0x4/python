from re import M


data_aja = {
    'data1':'kevin',
    'data2':'bayu',
    'data3':'tia',
    'data4':'danny',
    'data5':'ariq',
}
print(f"Datanya adalah = {data_aja}")

for key,values in data_aja.items():
    print(f"Datanya itu = {key} dan isinya {values}")


print("="*10,"Matematika Bocil","="*10)
alas = float(input('Tulis alasnya: '))
tinggi = float(input('Tulis tingginya: '))

luas = alas * tinggi / 2
print('Luas segitiga adalah %0.2f' %luas)

sisi = float(input('Masukan sisi: '))

volume = sisi **3
print(f'Volume kubus adalah %0.2f', {volume})

panjang = int(input('Masukan panjang: '))
fibo = [0, 1]
for test in fibo(2, panjang):
    print(f'deret ke {(test + 1)}')