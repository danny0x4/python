# Pengenalan String

data = "ini adalah string"
print(data)
print(type(data))

# cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Ini menggunakan single quote'
print(data)

data = "Menggunakan Double Quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string
print('hari jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\totong, jauhan")

# backspace
print("ucup \botong")

# newline
print("bari pertama.\nbaris kedua.") # LF -> line feed
print("Baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # cara yang salah

# menggunakan raw string
print(r'C:\new folder')

# menggunakan multiline literal string
print("""
nama : ucup
kelas : 3SD
""")

# multiline literal string dan RAW
print(r"""
nama : ucup
kelas : 3SD
Website : www.google.com/ucup
""")