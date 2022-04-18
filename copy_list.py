# Teknik menduplikat list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # pass by reference (memberikan referen ke si b)
print(f"b = {b}")


# kita akan merubah member dari a

a[1] = ("Michael")
b.sort()
print(f"a = {a}")
print(f"b = {b}")


# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy

print(f"Membuat list c dengan a.copy()")
c = a.copy() # full duplikat atau membuat data baru
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


print(f"Kita mengubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"Kita mengubah data 1")
c[1] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")