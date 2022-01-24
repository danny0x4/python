# format string

# contoh generic
# str

nama = "marline"
format_str = f"hello {nama}"
print(format_str)

# bool
boolean = True
format_str = f"boolean = {boolean}" 
print(format_str)


# angka
angka = 2005.5
format_str = f"angka =  + {angka} "
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal =  + {angka:.2f} "
print(format_str)

# menampilkan leading zero (angka 9 untuk menambah angka)
angka = 2005.54321
format_str = f"desimal =  + {angka:9.3f} "
print(format_str)

# menampilkan leading zero (ditambahkan angka didepan angka 9)
angka = 2005.54321
format_str = f"desimal =  + {angka:09.3f} "
print(format_str)

# menampilkan tanda + atau -
angka_mines = -10
angka_plus = 10
format_minus = f"minus = {angka_mines:+d}"
format_plus = f"plus = {angka_plus:+d}"

print(format_plus)
print(format_minus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp.{harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexa)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)